#!/usr/bin/env python3
"""
Download and organise ProteomicsDB protein expression data.

Data are downloaded per sample through the proteinexpression endpoint (GROUP_BY_TISSUE=0), so every value
carries a SAMPLE_ID. On export, values are aligned by sample_id into sample x protein matrices:
  - MS1 and MS2 data are merged
  - tissue assignment uses ProteomicsDB's TISSUE_GROUP_NAME, with no distinction between tissue and cell line
  - the "unknown" group is not exported
  - per tissue, only proteins with values in at least 2 samples are kept
  - proteins are named by UniProt entry name (e.g. 1433B_HUMAN)
  - tissues that the current endpoint no longer serves, but whose original XML is kept in
    <raw_data>/legacy_xml/ (e.g. adipose), are exported from that XML; their row index is SAMPLE_NAME
    (the original XML has no SAMPLE_ID)

Directories (raw_data and data are set in config.yaml):
    <raw_data>/raw/                    raw responses (gzip)
    <raw_data>/reference/              UniProt protein list, ProteomicsDB tissue list
    <raw_data>/legacy_xml/             previously saved proteinspertissue XML
    <raw_data>/download_ledger.csv     download log
    <data>/proteins/{tissue}.parquet   rows = sample_id, columns = proteins, values = expression, missing = NaN

Usage:
    python download.py                   # full run: reference -> download -> export
    python download.py --step export     # re-export only (raw files already downloaded)
    python download.py --step download   # download only; rerun after an interruption to resume
    python download.py --retry-failed    # retry failed requests only
"""
from __future__ import annotations

import argparse
import csv
import gzip
import json
import random
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

import pandas as pd
import requests

from common import PATHS

# ══════════════════════════════════════════════════════════════════
# Configuration
# ══════════════════════════════════════════════════════════════════
DATA = PATHS["raw_data"]                    # raw downloads: raw/, reference/, download_ledger.csv
PROTEINS = PATHS["data"] / "proteins"       # exported sample x protein matrices
LEGACY_XML = DATA / "legacy_xml"            # original proteinspertissue XML (endpoint no longer available)

# --- Download parameters ---
MS_LEVELS = [1, 2]              # 1 = label-free, 2 = TMT/iTRAQ
GROUP_BY_TISSUE = 0             # 0 = one row per sample, each with SAMPLE_ID
CALCULATION_METHOD = 0          # 0 = iBAQ
SCOPE_SELECTION = 1             # 1 = Proteome
TISSUE_CATEGORY = "tissue;fluid;cell line"
TAXCODE = 9606

# --- Export parameters ---
EXCLUDE_GROUPS = {"unknown"}
MIN_VALUES_PER_PROTEIN = 2      # minimum number of samples with a value per protein, per tissue

# --- Network ---
MAX_WORKERS = 4
TIMEOUT = 120
MAX_RETRIES = 5
BACKOFF = 2.0
DELAY = 0.15
UA = "co-abundance-redownload/1.0 (academic research; UIUC)"

PDB = "https://www.proteomicsdb.org/proteomicsdb/logic/api"
UNIPROT = "https://rest.uniprot.org/uniprotkb/stream"

FIELDS = ["UNIQUE_IDENTIFIER", "TISSUE_ID", "TISSUE_NAME", "TISSUE_SAP_SYNONYM",
          "SAMPLE_ID", "SAMPLE_NAME", "AFFINITY_PURIFICATION",
          "EXPERIMENT_ID", "EXPERIMENT_NAME", "EXPERIMENT_SCOPE", "EXPERIMENT_SCOPE_NAME",
          "PROJECT_ID", "PROJECT_NAME", "PROJECT_STATUS",
          "UNNORMALIZED_INTENSITY", "NORMALIZED_INTENSITY", "SAMPLES"]
TISSUE_FIELDS = ["TISSUE_ID", "TISSUE_NAME", "TISSUE_GROUP_NAME", "TISSUE_CATEGORY",
                 "SCOPE_NAME", "QUANTIFICATION_METHOD_NAME", "MS_LEVEL", "TAXCODE"]


# ══════════════════════════════════════════════════════════════════
# HTTP: GET with validation
# ══════════════════════════════════════════════════════════════════
class ApiError(RuntimeError):
    pass


class Truncated(RuntimeError):
    pass


_local = threading.local()
_lock = threading.Lock()


def session() -> requests.Session:
    if not hasattr(_local, "s"):
        _local.s = requests.Session()
        _local.s.headers.update({"Accept": "application/json", "User-Agent": UA})
    return _local.s


def expr_url(acc: str, ms_level: int) -> str:
    p = (f"PROTEINFILTER='{acc}',MS_LEVEL={ms_level},TISSUE_ID_SELECTION='',"
         f"TISSUE_CATEGORY_SELECTION='{quote(TISSUE_CATEGORY, safe=';')}',"
         f"SCOPE_SELECTION={SCOPE_SELECTION},GROUP_BY_TISSUE={GROUP_BY_TISSUE},"
         f"CALCULATION_METHOD={CALCULATION_METHOD},EXP_ID=-1")
    return (f"{PDB}/proteinexpression.xsodata/InputParams({p})/Results"
            f"?$select={','.join(FIELDS)}&$format=json&$inlinecount=allpages")


def get(url: str, strict: bool = True):
    """GET + validation + retry with backoff. Returns (raw text, results, __count).

    ProteomicsDB has been observed to return HTTP 200 with a truncated body, so every response must parse as
    complete JSON and its __count must equal the number of rows received (except for paged requests).
    """
    err = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = session().get(url, timeout=TIMEOUT)
            if r.status_code == 429:
                time.sleep(float(r.headers.get("Retry-After", BACKOFF ** attempt)))
                err = RuntimeError("429")
                continue
            r.raise_for_status()
            obj = json.loads(r.text)
            if "error" in obj:
                m = obj["error"].get("message", {})
                raise ApiError(str(m.get("value", m))[:200])
            res, cnt = obj["d"]["results"], obj["d"].get("__count")
            if cnt is not None:
                cnt = int(cnt)
                if strict and cnt != len(res):
                    raise Truncated(f"__count={cnt} but only {len(res)} rows received")
            return r.text, res, cnt
        except ApiError:
            raise
        except (requests.RequestException, json.JSONDecodeError, Truncated, KeyError) as e:
            err = e
            if attempt < MAX_RETRIES:
                time.sleep(BACKOFF ** attempt + random.uniform(0, 1))
    raise RuntimeError(f"Still failing after {MAX_RETRIES} retries: {err}")


# ══════════════════════════════════════════════════════════════════
# Step 1: reference data (full UniProt protein set + ProteomicsDB tissue list)
# ══════════════════════════════════════════════════════════════════
def step_reference() -> None:
    ref = DATA / "reference"
    ref.mkdir(parents=True, exist_ok=True)

    tsv = ref / "uniprot_human_reviewed.tsv"
    if not tsv.exists():
        print("[ref] Downloading all reviewed human UniProt entries ...")
        r = requests.get(UNIPROT, timeout=300, headers={"User-Agent": UA}, params={
            "query": "reviewed:true AND organism_id:9606",
            "fields": "accession,id,gene_primary,protein_name", "format": "tsv"})
        r.raise_for_status()
        tsv.write_text(r.text)
    print(f"[ref] UniProt: {len(pd.read_csv(tsv, sep=chr(9))):,} proteins")

    raw = ref / "tissuelist_raw.json"
    if not raw.exists():
        rows, skip, page, total = [], 0, 1000, None
        while True:                                   # must page; a single full request gets truncated
            url = (f"{PDB}/tissuelist.xsodata/CA_AVAILABLEBIOLOGICALSOURCES_API"
                   f"?$select={','.join(TISSUE_FIELDS)}&$format=json"
                   f"&$top={page}&$skip={skip}&$inlinecount=allpages")
            _, res, cnt = get(url, strict=False)
            total = cnt if cnt is not None else total
            rows += res
            if len(res) < page:
                break
            skip += page
        if total is not None and len(rows) != total:
            raise Truncated(f"tissuelist: only {len(rows)} rows received, __count={total}")
        raw.write_text(json.dumps(rows, ensure_ascii=False))
    print(f"[ref] tissuelist: {len(json.loads(raw.read_text())):,} rows")


# ══════════════════════════════════════════════════════════════════
# Step 2: download
# ══════════════════════════════════════════════════════════════════
def raw_path(acc: str, ms: int) -> Path:
    return DATA / "raw" / f"ms{ms}" / acc[:2] / f"{acc}.json.gz"


def ledger_append(row: dict) -> None:
    f = DATA / "download_ledger.csv"
    cols = ["accession", "ms_level", "status", "rows", "bytes", "at", "error"]
    with _lock:
        new = not f.exists()
        with f.open("a", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols)
            if new:
                w.writeheader()
            w.writerow(row)


def fetch_one(job: tuple[str, int]) -> dict:
    acc, ms = job
    at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    try:
        text, res, _ = get(expr_url(acc, ms))
        p = raw_path(acc, ms)
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_suffix(".tmp")
        tmp.write_bytes(gzip.compress(text.encode(), 6))   # write tmp then rename, so no partial files are left
        tmp.replace(p)
        out = {"status": "ok", "rows": len(res), "bytes": p.stat().st_size, "error": ""}
    except Exception as e:
        out = {"status": "error", "rows": 0, "bytes": 0, "error": f"{type(e).__name__}: {e}"[:250]}
    time.sleep(DELAY)
    return {"accession": acc, "ms_level": ms, "at": at, **out}


def step_download(args) -> None:
    tsv = DATA / "reference" / "uniprot_human_reviewed.tsv"
    if not tsv.exists():
        sys.exit("Protein list missing; run python download.py --step ref first")
    accs = pd.read_csv(tsv, sep="\t")["Entry"].dropna().astype(str).tolist()

    if args.retry_failed:
        led = DATA / "download_ledger.csv"
        if not led.exists():
            sys.exit("No download ledger found; cannot --retry-failed")
        d = pd.read_csv(led)
        jobs = sorted({(str(r.accession), int(r.ms_level)) for r in d[d.status != "ok"].itertuples()})
    else:
        jobs = [(a, ms) for a in accs for ms in MS_LEVELS]
        jobs = [j for j in jobs if not raw_path(*j).exists()]

    if not jobs:
        print("[dl] Everything already downloaded.")
        return
    print(f"[dl] {len(jobs):,} requests to download, {args.workers} workers")

    t0, ok, err = time.time(), 0, 0
    try:
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            for i, f in enumerate(as_completed([pool.submit(fetch_one, j) for j in jobs]), 1):
                row = f.result()
                ledger_append(row)
                if row["status"] == "ok":
                    ok += 1
                else:
                    err += 1
                    print(f"  ✗ {row['accession']} ms{row['ms_level']}: {row['error'][:110]}")
                if i % 500 == 0 or i == len(jobs):
                    rate = i / (time.time() - t0)
                    print(f"  [{i:>6,}/{len(jobs):,}] ok={ok:,} err={err:,} | {rate:.1f}/s "
                          f"| ETA {(len(jobs) - i) / rate / 60:.0f} min")
    except KeyboardInterrupt:
        print("\n[dl] Interrupted; completed files are on disk, rerun to resume.")
        raise SystemExit(130)
    print(f"[dl] ok={ok:,} err={err:,}, took {(time.time() - t0) / 60:.1f} min")


# ══════════════════════════════════════════════════════════════════
# Step 3: export  <data>/proteins/{tissue}.parquet
# ══════════════════════════════════════════════════════════════════
def load_tissue_groups() -> dict[str, str]:
    """tissue_id -> group name (ProteomicsDB TISSUE_GROUP_NAME, lower case)."""
    rows = json.loads((DATA / "reference" / "tissuelist_raw.json").read_text())
    groups = {}
    for r in rows:
        g = (r.get("TISSUE_GROUP_NAME") or "").strip().lower()
        if str(r.get("TAXCODE")) == str(TAXCODE) and g:
            groups.setdefault(r["TISSUE_ID"], g)
    return groups


def export_legacy(done: set[str], acc2entry: dict[str, str]) -> None:
    """Export tissues the current endpoint no longer serves from the original XML. File name: proteins_{tissue}_{tissue_id}_9606.xml"""
    import re
    import xml.etree.ElementTree as ET
    ns = {"atom": "http://www.w3.org/2005/Atom",
          "d": "http://schemas.microsoft.com/ado/2007/08/dataservices",
          "m": "http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"}
    by_group: dict[str, list[Path]] = {}
    for f in sorted(LEGACY_XML.glob("proteins_*_9606.xml")):
        m = re.match(r"^proteins_(.+)_([A-Za-z]+:[^_]+)_9606\.xml$", f.name)
        if m and m.group(1) not in done and m.group(1) not in EXCLUDE_GROUPS:
            by_group.setdefault(m.group(1), []).append(f)

    for g, files in by_group.items():
        recs = []
        for f in files:
            for e in ET.parse(f).getroot().findall("atom:entry", ns):
                p = e.find("atom:content/m:properties", ns)
                t = lambda k: p.findtext(f"d:{k}", default="", namespaces=ns)
                recs.append((t("SAMPLE_NAME").strip(), acc2entry.get(t("UNIQUE_IDENTIFIER"), t("ENTRY_NAME")),
                             float(t("NORMALIZED_EXPRESSION"))))
        df = pd.DataFrame(recs, columns=["sample_id", "protein", "value"])
        dup = int(df.duplicated(["sample_id", "protein"]).sum())
        if dup:
            raise RuntimeError(f"legacy {g}: {dup} duplicate (SAMPLE_NAME, protein) pairs, cannot align")
        mat = df.pivot(index="sample_id", columns="protein", values="value")
        mat = mat.loc[:, mat.notna().sum() >= MIN_VALUES_PER_PROTEIN]
        mat = mat.dropna(how="all").sort_index().sort_index(axis=1)
        if mat.empty:
            continue
        mat.columns.name = None
        mat.to_parquet(PROTEINS / f"{g.replace('/', '_')}.parquet")
        print(f"  {g:26s} {mat.shape[0]:4d} samples × {mat.shape[1]:6,d} proteins   <- original XML")


def step_export() -> None:
    groups = load_tissue_groups()
    uni = pd.read_csv(DATA / "reference" / "uniprot_human_reviewed.tsv", sep="\t")
    acc2entry = dict(zip(uni["Entry"], uni["Entry Name"]))

    files = sorted((DATA / "raw").rglob("*.json.gz"))
    if not files:
        sys.exit(f"No files under {DATA.name}/raw; run the download first")
    print(f"[export] Reading {len(files):,} raw files ...")

    tissue, sample, protein, value = [], [], [], []
    for n, f in enumerate(files, 1):
        for r in json.loads(gzip.decompress(f.read_bytes()))["d"]["results"]:
            g = groups.get(r["TISSUE_ID"])
            if g is None or g in EXCLUDE_GROUPS:
                continue
            tissue.append(g)
            sample.append(int(r["SAMPLE_ID"]))
            protein.append(acc2entry[r["UNIQUE_IDENTIFIER"]])
            value.append(float(r["NORMALIZED_INTENSITY"]))
        if n % 5000 == 0 or n == len(files):
            print(f"  [{n:>6,}/{len(files):,}] {len(value):,} values")

    df = pd.DataFrame({"tissue": tissue, "sample_id": sample, "protein": protein, "value": value})
    del tissue, sample, protein, value

    dup = int(df.duplicated(["sample_id", "protein"]).sum())
    if dup:
        raise RuntimeError(f"{dup} duplicate (sample_id, protein) pairs, cannot align into a matrix")
    print(f"[export] no duplicate (sample_id, protein) pairs ✓  {df.sample_id.nunique():,} samples in total")

    PROTEINS.mkdir(parents=True, exist_ok=True)
    for old in PROTEINS.glob("*.parquet"):
        old.unlink()

    written, skipped = 0, []
    for g, sub in df.groupby("tissue", sort=True):
        mat = sub.pivot(index="sample_id", columns="protein", values="value")
        mat = mat.loc[:, mat.notna().sum() >= MIN_VALUES_PER_PROTEIN]
        mat = mat.dropna(how="all").sort_index().sort_index(axis=1)
        if mat.empty:
            skipped.append(g)
            continue
        mat.columns.name = None
        mat.to_parquet(PROTEINS / f"{g.replace('/', '_')}.parquet")
        written += 1
        print(f"  {g:26s} {mat.shape[0]:4d} samples × {mat.shape[1]:6,d} proteins")

    done = {f.stem for f in PROTEINS.glob("*.parquet")}
    if LEGACY_XML.exists():
        export_legacy(done, acc2entry)
        skipped = [g for g in skipped if not (PROTEINS / f"{g.replace('/', '_')}.parquet").exists()]
        written = len(list(PROTEINS.glob("*.parquet")))
    print(f"\n[export] {written} tissues -> proteins/")
    if skipped:
        print(f"[export] not exported (only 1 sample, no protein with >= {MIN_VALUES_PER_PROTEIN} values): {skipped}")


# ══════════════════════════════════════════════════════════════════
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--step", choices=["all", "ref", "download", "export"], default="all")
    ap.add_argument("--workers", type=int, default=MAX_WORKERS)
    ap.add_argument("--retry-failed", action="store_true")
    args = ap.parse_args()

    if args.step in ("all", "ref"):
        step_reference()
    if args.step in ("all", "download") or args.retry_failed:
        step_download(args)
    if args.step in ("all", "export"):
        step_export()
    return 0


if __name__ == "__main__":
    sys.exit(main())
