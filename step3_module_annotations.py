#!/usr/bin/env python3
"""
Step 3: database annotation and description of conserved modules (agent workflow).

For every tissue pair, an agent (smolagents CodeAgent, OpenAI model) calls tools that collect the annotations below for
each module, writes a description of each module, and produces a summary used by Step 4. All annotations serve to
interpret the modules.
  HPA gene annotation   per-gene RNA tissue specificity, single cell type specificity, blood cell specificity,
                        secretome location and subcellular location
  HPA IHC               the agent chooses the matching HPA normal tissue(s) for each tissue group (several or none)
                        and the detection level of module proteins is looked up there
  hu.MAP 3.0            protein complexes with at least 2 members in the module
  GO / KEGG             local hypergeometric test from step3_enrichment.py; BH within module and across all
                        module-term tests; primary result q_global < 0.05
  STRING enrichment     FDR < 0.05; same background
  STRING interactions   known interactions with score >= 700
  Web search            DuckDuckGo
Modules with fewer than 3 genes are not tested for GO/KEGG or STRING enrichment.

The agent reads the overview of one module at a time, writes that module's description in the next step and submits it
with save_module_description(); only one description can be submitted per step. Descriptions that paste raw data, fill
templates with counts, or repeat sentences from other modules are rejected and must be rewritten.
The knowledge JSON is assembled by the program and checked against the template and the tool results; after each run
the output is checked again and, if incomplete, the run is repeated with the problems listed (at most 3 attempts).
STRING query results are cached in knowledge/cache/annotations/{pair}/bio_knowledge_{pair}.json; pairs with cached
results are read from there instead of being queried online again.

Input   analysis/{pair}.json, analysis/{pair}/consensus_{pair}.pkl, analysis/{pair}/module_*.graphml
        data/proteinatlas.tsv, data/normal_ihc_data.tsv, data/hu.MAP3.0_complexes_*.csv, data/uniprot_human_reviewed.tsv
        knowledge/enrichment/ (step3_enrichment.py)
Output  knowledge/{pair}/bio_knowledge_{pair}.json    annotations and description of every module
        knowledge/{pair}/summary_{pair}.txt           summary written by the agent (input of Step 4)
        knowledge/module_summary.csv, knowledge/sources.json, knowledge/cache/string_ids.tsv, knowledge/cache/annotations/
        agent_traces/step3/                           full trajectory of every run of every pair, and status.csv
All directories are set in config.yaml (see common.py).

Usage   python step3_module_annotations.py                      # all pairs with modules
        python step3_module_annotations.py --pairs breast_colon
        python step3_module_annotations.py --model gpt-5.5 --temperature default
"""
import argparse
import itertools
import json
import pickle
import re
import threading
import time
import traceback
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd
import requests
from smolagents import CodeAgent, DuckDuckGoSearchTool, OpenAIServerModel, tool

from common import PATHS, load_api_key, load_clusters

ANALYSIS = PATHS["analysis"]
DATA = PATHS["data"]
HPA_GENES = DATA / "proteinatlas.tsv"
HPA_IHC = DATA / "normal_ihc_data.tsv"
HUMAP = DATA / "hu.MAP3.0_complexes_wConfidenceScores_total15326_wGenenames_20240922.csv"
UNIPROT = DATA / "uniprot_human_reviewed.tsv"

GPROFILER = "https://biit.cs.ut.ee/gprofiler/api/gost/profile/"
STRING = "https://string-db.org/api"
STRING_CALLER = "coabundance_module_annotation"
STRING_SCORE = 700
MIN_GENES_FOR_ENRICHMENT = 3
HUMAP_MIN_OVERLAP = 2
DETECTED_LEVELS = {"Low", "Medium", "High"}

MODEL_ID = "gpt-5.6-luna"
TEMPERATURE = "default"              # gpt-5.x only accepts the default temperature; "default" means the parameter is not sent
TISSUE_STEPS = 8                     # step limit for choosing the HPA tissues of one tissue group
MODULE_STEPS = 10                    # step limit of one run for one module
SUMMARY_STEPS = 8
PLANNING_INTERVAL = None             # no planning steps (gpt-5.x tends to forget the tools after a planning step)
MAX_ATTEMPTS = 3
AUTHORIZED_IMPORTS = ["json", "math", "pandas", "collections", "re"]

PROMPT_HEAD = ("\nYou are a top rated biological researcher and you are doing research related to "
               "protein co-abundance network in multiple human tissue groups.\n")

CONFIG = {"out": PATHS["knowledge"], "traces": PATHS["traces"] / "step3"}
ENRICH = PATHS["knowledge"] / "enrichment"   # globally BH-corrected enrichment results (step3_enrichment.py)
_cache: dict = {}
_cache_lock = threading.RLock()
_registry: dict = {}                 # annotations returned by online tools in this run: (pair, field, module id) -> value
_registry_lock = threading.Lock()
_progress: dict = {}                 # pair -> {"step": current step, "viewed": {module id: step of overview}, "saved_at": {step: module id}, "descriptions": {module id: text}}
_string_lock = threading.Lock()
_last_string_call = [0.0]
_session = requests.Session()


def cached(key, fn):
    with _cache_lock:
        if key not in _cache:
            _cache[key] = fn()
        return _cache[key]


def cached_annotations(prefix):
    """Saved online query results as {module id: annotations of that module}; None when nothing is saved."""
    def load():
        path = CONFIG["out"] / "cache" / "annotations" / prefix / f"bio_knowledge_{prefix}.json"
        if not path.exists():
            return None
        return {int(m["module"]): m for m in json.loads(path.read_text())["modules"]}
    return cached(("annotations", prefix), load)


def choices_path():
    return CONFIG["out"] / "hpa_tissue_choices.json"


def tissue_choices():
    """{tissue group: {"hpa_tissues": [...], "note": reason}}, chosen once per tissue group by the agent and shared by all pairs."""
    p = choices_path()
    return json.loads(p.read_text()) if p.exists() else {}


def progress_path(prefix):
    return CONFIG["out"] / prefix / "_progress.json"


def progress(prefix):
    """Progress of one pair: the HPA tissues chosen by the agent and the accepted module descriptions. Saved to disk so
    that an interrupted run can resume."""
    with _registry_lock:
        st = _progress.get(prefix)
        if st is None:
            saved = json.loads(progress_path(prefix).read_text()) if progress_path(prefix).exists() else {}
            st = _progress[prefix] = {"step": 1, "viewed": {}, "saved_at": {},
                                      "descriptions": {int(k): v for k, v in saved.get("descriptions", {}).items()},
                                      "hpa_tissues": {}}
        return st


def save_progress(prefix):
    st = progress(prefix)
    progress_path(prefix).parent.mkdir(parents=True, exist_ok=True)
    progress_path(prefix).write_text(json.dumps({"descriptions": st["descriptions"]},
                                                indent=1, ensure_ascii=False))


def register(prefix, field, module, value):
    with _registry_lock:
        _registry[(prefix, field, module)] = value


# ════════════════════════════════════════════════════════════════════
# Data and online queries
# ════════════════════════════════════════════════════════════════════
def http(method, url, retries=5, **kw):
    for attempt in range(1, retries + 1):
        try:
            r = _session.request(method, url, timeout=300, **kw)
            if r.status_code == 429 or r.status_code >= 500:
                raise requests.HTTPError(f"HTTP {r.status_code}")
            r.raise_for_status()
            return r
        except (requests.RequestException, ValueError):
            if attempt == retries:
                raise
            time.sleep(5 * attempt)


def string_call(endpoint, data):
    """STRING asks for about 1 second between requests; all threads share one clock."""
    with _string_lock:
        wait = 1.0 - (time.time() - _last_string_call[0])
        if wait > 0:
            time.sleep(wait)
        r = http("POST", f"{STRING}/{endpoint}", data={**data, "species": 9606, "caller_identity": STRING_CALLER})
        _last_string_call[0] = time.time()
        return r


def query_symbol(gene):
    """A few proteins are encoded by several genes, written 'HBA1; HBA2' in UniProt; external databases are queried
    with the first gene name."""
    return gene.split(";")[0].strip()


def parse_named_values(text):
    if not isinstance(text, str):
        return []
    return [part.split(":")[0].strip() for part in text.split(";") if part.strip()]


def hpa_genes():
    def load():
        d = pd.read_csv(HPA_GENES, sep="\t", low_memory=False)
        cols = {"tissue_specificity": "RNA tissue specificity", "tissue_distribution": "RNA tissue distribution",
                "enriched_tissues": "RNA tissue specific nTPM",
                "single_cell_type_specificity": "RNA single cell type specificity",
                "enriched_single_cell_types": "RNA single cell type specific nCPM",
                "blood_cell_specificity": "RNA blood cell specificity", "enriched_blood_cells": "RNA blood cell specific nTPM",
                "secretome_location": "Secretome location", "subcellular_main_location": "Subcellular main location"}
        by_acc, by_gene = {}, {}
        for _, r in d.iterrows():
            ann = {k: parse_named_values(r[c]) if k.startswith("enriched_") else (r[c] if isinstance(r[c], str) else None)
                   for k, c in cols.items()}
            by_gene.setdefault(r["Gene"], ann)
            if isinstance(r["Uniprot"], str):
                for acc in re.split(r"[,\s]+", r["Uniprot"].strip()):
                    if acc:
                        by_acc.setdefault(acc, ann)
        return by_acc, by_gene
    return cached("hpa_genes", load)


def hpa_ihc():
    """{(gene name, HPA tissue): (detected, detected cell types)}, and all HPA tissue names."""
    def load():
        d = pd.read_csv(HPA_IHC, sep="\t", usecols=["Gene name", "Tissue", "Cell type", "Level"])
        d = d.dropna(subset=["Gene name", "Tissue"])
        flags = d["Level"].isin(DETECTED_LEVELS).to_numpy()
        table = {}
        for g, t, c, flag in zip(d["Gene name"].to_numpy(), d["Tissue"].to_numpy(), d["Cell type"].to_numpy(), flags):
            e = table.get((g, t))
            if e is None:
                e = table[(g, t)] = [False, set()]
            if flag:
                e[0] = True
                if isinstance(c, str):
                    e[1].add(c)
        return {k: (v[0], sorted(v[1])) for k, v in table.items()}, sorted(d["Tissue"].unique())
    return cached("hpa_ihc", load)


def humap():
    def load():
        d = pd.read_csv(HUMAP)
        complexes, acc_index = [], {}
        for r in d.itertuples(index=False):
            accs = str(r.Uniprot_ACCs).split()
            idx = len(complexes)
            complexes.append({"complex_id": r.HuMAP3_ID, "confidence": int(r.ComplexConfidence),
                              "accessions": accs, "genes": str(r.genenames).split()})
            for a in accs:
                acc_index.setdefault(a, []).append(idx)
        return complexes, acc_index
    return cached("humap", load)


def entry_to_gene():
    def load():
        u = pd.read_csv(UNIPROT, sep="\t")
        return {e: g for e, g in zip(u["Entry Name"], u["Gene Names (primary)"]) if isinstance(g, str)}
    return cached("entry2gene", load)


def string_ids(genes):
    """Gene name -> STRING ID, cached in knowledge/cache/string_ids.tsv."""
    with _cache_lock:
        path = CONFIG["out"] / "cache" / "string_ids.tsv"
        path.parent.mkdir(parents=True, exist_ok=True)
        known = _cache.get("string_ids")
        if known is None:
            known = dict(pd.read_csv(path, sep="\t", keep_default_na=False).values) if path.exists() else {}
            _cache["string_ids"] = known
        missing = sorted(set(genes) - set(known))
        for i in range(0, len(missing), 2000):
            batch = missing[i:i + 2000]
            res = string_call("json/get_string_ids", {"identifiers": "\r".join(batch), "limit": 1, "echo_query": 1}).json()
            mapped = {x["queryItem"]: x["stringId"] for x in res}
            for g in batch:
                known[g] = mapped.get(g, "")
            pd.DataFrame(sorted(known.items()), columns=["gene", "string_id"]).to_csv(path, sep="\t", index=False)
        return {g: known[g] for g in genes if known.get(g)}


def pair_context(prefix):
    def load():
        a, b = split_pair(prefix)
        clusters = load_clusters(ANALYSIS / f"{prefix}.json")
        with open(ANALYSIS / prefix / f"consensus_{prefix}.pkl", "rb") as fh:
            gC = pickle.load(fh)
        e2g = entry_to_gene()
        background = sorted({query_symbol(e2g[n]) for n in gC.vs["name"] if n in e2g})
        graphml = {int(re.match(r"module_(\d+)_", p.name).group(1)): p.name for p in (ANALYSIS / prefix).glob("module_*.graphml")}
        modules = [{"module": i, "graphml": graphml.get(i), "genes": [query_symbol(p["gene"]) for p in m],
                    "accessions": [p["accession"] for p in m], "protein_entries": [p["protein_entry"] for p in m]}
                   for i, m in sorted(clusters.items())]
        bg_ids = string_ids(background)
        return {"tissue_pair": prefix, "tissue_a": a, "tissue_b": b, "consensus_proteins": gC.vcount(),
                "background_genes": len(background), "background_string_ids": len(set(bg_ids.values())),
                "background": background, "background_ids": sorted(set(bg_ids.values())), "modules": modules}
    return cached(("pair", prefix), load)


def module_of(ctx, module_id):
    """The module with this id (ids come from the cluster file and need not be contiguous)."""
    for m in ctx["modules"]:
        if m["module"] == module_id:
            return m
    raise ValueError(f"module {module_id} does not exist in {ctx['tissue_pair']}; "
                     f"module ids are {[m['module'] for m in ctx['modules']]}.")


def all_pairs():
    tissues = sorted(p.stem for p in PATHS["graph"].glob("*.pkl"))
    return [f"{a}_{b}" for a, b in itertools.combinations(tissues, 2)], tissues


def split_pair(prefix):
    _, tissues = all_pairs()
    for a, b in itertools.combinations(tissues, 2):
        if f"{a}_{b}" == prefix:
            return a, b
    raise ValueError(f"unknown tissue pair: {prefix}")


# Local annotations (shared by the tools and the validation)
def compute_hpa_gene_annotation(genes, accessions):
    by_acc, by_gene = hpa_genes()
    per_gene = {g: by_acc.get(a) or by_gene.get(g) for g, a in zip(genes, accessions)}
    found = [v for v in per_gene.values() if v]
    count = lambda key: dict(Counter(v[key] for v in found if v[key]).most_common())
    top = lambda key: [{"name": n, "genes": c} for n, c in Counter(x for v in found for x in v[key]).most_common(5)]
    return per_gene, {
        "genes_with_hpa_annotation": len(found),
        "tissue_specificity": count("tissue_specificity"),
        "most_frequent_enriched_tissues": top("enriched_tissues"),
        "single_cell_type_specificity": count("single_cell_type_specificity"),
        "most_frequent_enriched_single_cell_types": top("enriched_single_cell_types"),
        "blood_cell_specificity": count("blood_cell_specificity"),
        "most_frequent_enriched_blood_cells": top("enriched_blood_cells"),
        "secreted_genes": sum(1 for v in found if v["secretome_location"]),
    }


def compute_ihc(hpa_tissues, genes):
    table, _ = hpa_ihc()
    detected, not_detected, no_data, cell_types = [], [], [], {}
    for g in genes:
        vals = [table[(g, t)] for t in hpa_tissues if (g, t) in table]
        if not vals:
            no_data.append(g)
        elif any(v[0] for v in vals):
            detected.append(g)
            cell_types[g] = sorted({c for v in vals for c in v[1]})
        else:
            not_detected.append(g)
    return {"hpa_tissues": list(hpa_tissues), "detected": detected, "not_detected": not_detected,
            "no_data": no_data, "detected_cell_types": cell_types}


def compute_humap(accessions, genes):
    complexes, acc_index = humap()
    acc2gene = dict(zip(accessions, genes))
    hits = Counter(i for a in accessions for i in acc_index.get(a, []))
    out = []
    for i, k in hits.items():
        if k < HUMAP_MIN_OVERLAP:
            continue
        c = complexes[i]
        members = [acc2gene[a] for a in c["accessions"] if a in acc2gene]
        out.append({"complex_id": c["complex_id"], "confidence": c["confidence"], "complex_size": len(c["accessions"]),
                    "members_in_module": members, "fraction_of_complex": round(len(members) / len(c["accessions"]), 3),
                    "complex_genes": c["genes"]})
    return sorted(out, key=lambda x: (-len(x["members_in_module"]), -x["fraction_of_complex"]))


# ════════════════════════════════════════════════════════════════════
# Tools
# ════════════════════════════════════════════════════════════════════
@tool
def read_file(file_path: str) -> str:
    """
    Reads a text file inside the knowledge output folder. Raises FileNotFoundError if the file does not exist.

    Args:
        file_path: Path relative to the knowledge output folder, e.g. 'breast_colon/bio_knowledge_breast_colon.json'.

    Returns:
        str: The content of the file.
    """
    base = CONFIG["out"].resolve()
    path = (base / file_path).resolve()
    if base not in path.parents:
        raise ValueError("Only files inside the knowledge output folder can be read.")
    return path.read_text()


@tool
def load_conserved_modules(tissues_prefix: str) -> dict:
    """
    Loads the conserved modules of a tissue pair and the enrichment background (all proteins of the consensus network).

    Args:
        tissues_prefix: The tissue pair prefix, e.g. 'breast_colon'.

    Returns:
        dict: tissue_pair, tissue_a, tissue_b, consensus_proteins, background_genes (count), background_string_ids (count),
        and modules: a list of {module, graphml, genes, accessions, protein_entries}.
    """
    if not (ANALYSIS / f"{tissues_prefix}.json").exists():
        raise ValueError(f"{tissues_prefix} has no conserved modules.")
    ctx = pair_context(tissues_prefix)
    return {k: v for k, v in ctx.items() if k not in ("background", "background_ids")}


@tool
def get_hpa_gene_annotation(genes: list, accessions: list) -> dict:
    """
    Gets Human Protein Atlas gene-level annotation for module genes: RNA tissue specificity, single cell type specificity,
    blood cell specificity, secretome and subcellular location, plus a module-level summary.

    Args:
        genes: Gene names of the module.
        accessions: UniProt accessions of the module, in the same order as genes.

    Returns:
        dict: {"per_gene": {gene: annotation or None}, "summary": {...}}.
    """
    per_gene, summary = compute_hpa_gene_annotation(genes, accessions)
    return {"per_gene": per_gene, "summary": summary}


@tool
def get_hpa_tissue_names() -> list:
    """
    Lists all normal tissue names in the Human Protein Atlas tissue atlas (immunohistochemistry).

    Returns:
        list: HPA normal tissue names.
    """
    return hpa_ihc()[1]


@tool
def get_genes_from_tissue_hpa(hpa_tissues: list, genes: list) -> dict:
    """
    Gets HPA immunohistochemistry protein detection of module genes in the chosen HPA normal tissue(s).
    A gene counts as detected when any cell type in the chosen tissues has level Low, Medium or High.

    Args:
        hpa_tissues: HPA normal tissue names chosen for one tissue group (from get_hpa_tissue_names()).
        genes: Gene names of the module.

    Returns:
        dict: hpa_tissues, detected, not_detected, no_data, and detected_cell_types {gene: [cell types]}.
    """
    valid = set(hpa_ihc()[1])
    bad = [t for t in hpa_tissues if t not in valid]
    if bad:
        raise ValueError(f"Unknown HPA tissue names: {bad}. Use names from get_hpa_tissue_names().")
    return compute_ihc(hpa_tissues, genes)


@tool
def get_gene_complexes_hu_map_3(accessions: list, genes: list) -> list:
    """
    Retrieves hu.MAP 3.0 protein complexes that have at least 2 members in the module.

    Args:
        accessions: UniProt accessions of the module.
        genes: Gene names of the module, in the same order as accessions.

    Returns:
        list: complexes with complex_id, confidence, complex_size, members_in_module, fraction_of_complex, complex_genes.
    """
    return compute_humap(accessions, genes)


@tool
def infer_module_function_go_kegg(tissues_prefix: str) -> dict:
    """
    Loads completed local GO/KEGG enrichment with BH over all modules and terms.
    Background: all eligible saved consensus nodes mapped to unique genes.
    These functional annotations do not test co-abundance or module structure.

    Args:
        tissues_prefix: The tissue pair prefix, e.g. 'breast_colon'.

    Returns:
        dict: module_<i> to terms with q_global < 0.05. Fields include source,
        term_id, name, p_raw, q_within_module, q_global, fold_enrichment,
        intersection_size, query_size, term_size, effective_domain_size and genes.
        The complete family, including nonsignificant terms, is in knowledge/enrichment/.
    """
    from step3_enrichment import load_corrected_enrichment
    out = cached(('corrected_enrichment', tissues_prefix), lambda: load_corrected_enrichment(tissues_prefix))
    for q, values in out.items():
        register(tissues_prefix, 'go_kegg_enrichment', int(q.split('_')[1]), values)
    return out


@tool
def infer_module_function_string(tissues_prefix: str, module_id: int) -> list:
    """
    Infers the functions of one module with STRING functional enrichment (FDR < 0.05, background = all proteins of the
    consensus network). Raises an error for modules with fewer than 3 genes, which are not tested.

    Args:
        tissues_prefix: The tissue pair prefix, e.g. 'breast_colon'.
        module_id: The module index.

    Returns:
        list: enriched terms with category, term, description, number_of_genes, number_of_genes_in_background, p_value, fdr, genes.
    """
    ctx = pair_context(tissues_prefix)
    genes = module_of(ctx, module_id)["genes"]
    if len(genes) < MIN_GENES_FOR_ENRICHMENT:
        raise ValueError(f"module {module_id} has fewer than {MIN_GENES_FOR_ENRICHMENT} genes; enrichment is not performed "
                         f"(set go_kegg_enrichment and string_enrichment to null).")
    saved = cached_annotations(tissues_prefix)
    ids = [] if saved is not None else list(string_ids(genes).values())
    terms = saved[module_id]["string_enrichment"] if saved is not None else []
    if len(ids) >= MIN_GENES_FOR_ENRICHMENT:
        res = string_call("json/enrichment", {"identifiers": "\r".join(ids),
                                              "background_string_identifiers": "\r".join(ctx["background_ids"])}).json()
        keep = ["category", "term", "description", "number_of_genes", "number_of_genes_in_background", "p_value", "fdr"]
        terms = sorted(({**{k: x[k] for k in keep}, "genes": x["preferredNames"]} for x in res), key=lambda t: t["fdr"])
    register(tissues_prefix, "string_enrichment", module_id, terms)
    return terms


@tool
def get_module_network_string(tissues_prefix: str) -> dict:
    """
    Gets known STRING interactions (score >= 700) among the genes of every module of a tissue pair, in one query.

    Args:
        tissues_prefix: The tissue pair prefix, e.g. 'breast_colon'.

    Returns:
        dict: {"module_<i>": list of {gene_a, gene_b, score}} for every module.
    """
    ctx = pair_context(tissues_prefix)
    saved = cached_annotations(tissues_prefix)
    if saved is not None:
        out = {f"module_{m['module']}": saved[m["module"]]["string_interactions"] for m in ctx["modules"]}
        for m in ctx["modules"]:
            register(tissues_prefix, "string_interactions", m["module"], out[f"module_{m['module']}"])
        return out
    ids = string_ids([g for m in ctx["modules"] for g in m["genes"]])
    edges = set()
    if len(ids) >= 2:
        id2gene = {s: g for g, s in ids.items()}
        lines = string_call("tsv/network", {"identifiers": "\r".join(ids.values()),
                                            "required_score": STRING_SCORE}).text.strip().splitlines()
        if len(lines) > 1:
            head = lines[0].split("\t")
            ia, ib, isc = head.index("stringId_A"), head.index("stringId_B"), head.index("score")
            for ln in lines[1:]:
                f = ln.split("\t")
                a, b = id2gene.get(f[ia]), id2gene.get(f[ib])
                if a and b and a != b:
                    edges.add((min(a, b), max(a, b), float(f[isc])))
    out = {}
    for m in ctx["modules"]:
        gset = set(m["genes"])
        out[f"module_{m['module']}"] = [{"gene_a": x, "gene_b": y, "score": s} for x, y, s in sorted(edges)
                                        if x in gset and y in gset]
        register(tissues_prefix, "string_interactions", m["module"], out[f"module_{m['module']}"])
    return out


@tool
def get_module_overview(tissues_prefix: str, module_id: int, top_terms: int = 10) -> dict:
    """
    Gives a compact overview of one module to read before describing it: genes, HPA gene-level summary, the most
    significant GO/KEGG and STRING terms, hu.MAP 3.0 complexes and STRING interactions.

    Args:
        tissues_prefix: The tissue pair prefix, e.g. 'breast_colon'.
        module_id: The module index.
        top_terms: Number of most significant terms to show per database (default 10).

    Returns:
        dict: module, n_genes, genes, hpa_summary, go_kegg_top (source, name, p_raw, q_within_module, q_global, fold_enrichment, genes), go_kegg_total,
        string_top (category, description, fdr, genes), string_total, humap_complexes (complex_id, members_in_module,
        complex_size), string_interactions.
    """
    ctx = pair_context(tissues_prefix)
    m = module_of(ctx, module_id)
    genes = m["genes"]
    st = progress(tissues_prefix)
    st["viewed"].setdefault(module_id, st["step"])
    out = {"module": module_id, "n_genes": len(genes), "genes": genes}
    if not genes:
        return {**out, "note": "all proteins of this module were removed as housekeeping genes"}
    out["hpa_summary"] = compute_hpa_gene_annotation(genes, m["accessions"])[1]
    out["humap_complexes"] = [{k: c[k] for k in ("complex_id", "members_in_module", "complex_size")}
                              for c in compute_humap(m["accessions"], genes)]
    out["string_interactions"] = get_module_network_string(tissues_prefix)[f"module_{module_id}"]
    if len(genes) < MIN_GENES_FOR_ENRICHMENT:
        return {**out, "enrichment": f"not performed (fewer than {MIN_GENES_FOR_ENRICHMENT} genes)"}
    go = infer_module_function_go_kegg(tissues_prefix)[f"module_{module_id}"]
    st = infer_module_function_string(tissues_prefix, module_id)
    out["go_kegg_total"], out["string_total"] = len(go), len(st)
    out["go_kegg_top"] = [{k: t[k] for k in ("source", "name", "p_raw", "q_within_module", "q_global", "fold_enrichment", "intersection_size", "query_size", "term_size", "effective_domain_size", "genes")} for t in go[:top_terms]]
    out["string_top"] = [{k: t[k] for k in ("category", "description", "fdr", "genes")} for t in st[:top_terms]]
    return out


@tool
def save_hpa_tissue_choice(tissues_prefix: str, tissue_group: str, hpa_tissues: list, note: str = "") -> str:
    """
    Saves the HPA normal tissue(s) you chose for one tissue group of the pair. The immunohistochemistry detection of
    every module is then looked up in these tissues. Choose an empty list when no HPA tissue matches the tissue group
    (for example body fluids, cell lines or stem cells) and explain why in 'note'.

    Args:
        tissues_prefix: The tissue pair prefix, e.g. 'breast_colon'.
        tissue_group: One of the two tissue groups of the pair.
        hpa_tissues: HPA normal tissue names from get_hpa_tissue_names(), or an empty list.
        note: Why no HPA tissue matches, required when hpa_tissues is empty.

    Returns:
        str: confirmation and the tissue groups that still need a choice.
    """
    ctx = pair_context(tissues_prefix)
    if tissue_group not in (ctx["tissue_a"], ctx["tissue_b"]):
        raise ValueError(f"tissue_group must be {ctx['tissue_a']!r} or {ctx['tissue_b']!r}.")
    valid = set(hpa_ihc()[1])
    bad = [t for t in hpa_tissues if t not in valid]
    if bad:
        raise ValueError(f"Unknown HPA tissue names: {bad}. Use names from get_hpa_tissue_names().")
    if not hpa_tissues and not note.strip():
        raise ValueError("No HPA tissue chosen, so give a note explaining why.")
    st = progress(tissues_prefix)
    st["hpa_tissues"][tissue_group] = {"hpa_tissues": list(hpa_tissues), "note": note.strip()}
    save_progress(tissues_prefix)
    todo = [t for t in (ctx["tissue_a"], ctx["tissue_b"]) if t not in st["hpa_tissues"]]
    return f"saved HPA tissues for {tissue_group}; still to choose: {todo}"


_choices_lock = threading.Lock()


@tool
def save_tissue_group_choice(tissue_group: str, hpa_tissues: list, note: str) -> str:
    """
    Saves the HPA normal tissue(s) you chose for one tissue group. The immunohistochemistry detection of every module
    involving this tissue group is then looked up in these tissues. Choose an empty list when no HPA tissue matches
    (for example body fluids, cell lines or stem cells).

    Args:
        tissue_group: The tissue group named in the task.
        hpa_tissues: HPA normal tissue names from get_hpa_tissue_names(), or an empty list.
        note: Your reasoning: why these HPA tissues represent the tissue group, or why none does.

    Returns:
        str: confirmation.
    """
    valid = set(hpa_ihc()[1])
    bad = [t for t in hpa_tissues if t not in valid]
    if bad:
        raise ValueError(f"Unknown HPA tissue names: {bad}. Use names from get_hpa_tissue_names().")
    if len(note.strip()) < 30:
        raise ValueError("Explain your choice in 'note' (at least one full sentence).")
    with _choices_lock:
        ch = tissue_choices()
        ch[tissue_group] = {"hpa_tissues": list(hpa_tissues), "note": note.strip()}
        choices_path().parent.mkdir(parents=True, exist_ok=True)
        choices_path().write_text(json.dumps(ch, indent=1, ensure_ascii=False))
    return f"saved HPA tissues for {tissue_group}: {list(hpa_tissues)}"


def writing_problems(text, genes=None):
    """The text must be written by the agent itself after reading: no pasted raw data, no templates filled with counts."""
    problems = []
    if re.search(r"[\[{]\s*['\"{]", text):
        problems.append("it contains raw data structures; write prose instead of pasting tool output")
    if len(re.findall(r"[A-Za-z][\w /-]*\(\d+\)", text)) >= 3:
        problems.append("it lists annotation categories with counts like 'Tissue enhanced (3)'; interpret them instead")
    if genes is not None:
        if not 150 <= len(text) <= 2500:
            problems.append("it should be 150-2500 characters")
        named = [g for g in set(genes) if re.search(rf"(?<![\w-]){re.escape(g)}(?![\w-])", text)]
        if len(named) < min(2, len(genes)):
            problems.append("it must name the key genes of this module")
    return problems


def shared_sentences(text, others):
    sentences = {x.strip() for x in re.split(r"(?<=[.;])\s+", text) if len(x.strip()) >= 60}
    return [x for x in sentences if any(x in o for o in others)]


@tool
def save_module_description(tissues_prefix: str, module_id: int, description: str) -> str:
    """
    Saves your description of one module. Read get_module_overview() of this module first; the description must be
    written in a later step than the overview, and only one description can be saved per step.

    Args:
        tissues_prefix: The tissue pair prefix, e.g. 'breast_colon'.
        module_id: The module index.
        description: Your own description of this module: its key genes, the functions, complexes and interactions the
            annotations point to, where the genes are expressed, and whether the module may reflect blood or shared cell types.

    Returns:
        str: confirmation and the modules that still need a description.
    """
    ctx = pair_context(tissues_prefix)
    genes = module_of(ctx, module_id)["genes"]
    st = progress(tissues_prefix)
    if not genes:
        raise ValueError(f"module {module_id} has no genes; it needs no description.")
    if module_id not in st["viewed"]:
        raise ValueError(f"call get_module_overview('{tissues_prefix}', {module_id}) and read it first.")
    if st["viewed"][module_id] >= st["step"]:
        raise ValueError("read the overview output first; save this description in your next step.")
    other = st["saved_at"].get(st["step"])
    if other is not None and other != module_id:
        raise ValueError(f"a description (module {other}) was already saved in this step; describe one module per step.")
    problems = writing_problems(description, genes)
    others = [d for i, d in st["descriptions"].items() if i != module_id]
    if shared_sentences(description, others) or any(shared_sentences(o, [description]) for o in others):   # check both directions
        problems.append("it repeats sentences from another module's description; describe each module in its own words")
    if problems:
        raise ValueError(f"description of module {module_id} rejected: " + "; ".join(problems) + ".")
    st["descriptions"][module_id] = description.strip()
    st["saved_at"][st["step"]] = module_id
    save_progress(tissues_prefix)
    todo = [m["module"] for m in ctx["modules"] if m["genes"] and m["module"] not in st["descriptions"]]
    return f"saved description of module {module_id}; modules still without description: {todo}"


def expected_module(prefix, m):
    genes = m["genes"]
    per_gene, summary = compute_hpa_gene_annotation(genes, m["accessions"])
    ctx = pair_context(prefix)
    return {**m, "n_genes": len(genes), "hpa_gene_annotation": per_gene, "hpa_gene_annotation_summary": summary,
            "humap_complexes": compute_humap(m["accessions"], genes)}


def knowledge_problems(prefix, kb):
    ctx = pair_context(prefix)
    if not isinstance(kb, dict):
        return ["knowledge must be a JSON object following the template."]
    problems = []
    for k in ("tissue_pair", "tissue_a", "tissue_b", "consensus_proteins", "background_genes", "background_string_ids"):
        if kb.get(k) != ctx[k]:
            problems.append(f"field '{k}' should be {ctx[k]!r}.")
    mods = kb.get("modules")
    ids = [m["module"] for m in ctx["modules"]]
    if not isinstance(mods, list) or [g.get("module") if isinstance(g, dict) else None for g in mods] != ids:
        return problems + [f"'modules' must be a list of the modules {ids}, in this order."]
    required = ["module", "graphml", "genes", "accessions", "protein_entries", "n_genes", "description", "hpa_gene_annotation",
                "hpa_gene_annotation_summary", "hpa_ihc_detection", "humap_complexes", "go_kegg_enrichment",
                "string_enrichment", "enrichment_skipped", "string_interactions", "string_interaction_pairs"]
    valid_hpa = set(hpa_ihc()[1])
    descs = [g.get("description") for g, m_ctx in zip(mods, ctx["modules"]) if isinstance(g, dict) and m_ctx["genes"]]
    descs = [d for d in descs if isinstance(d, str)]
    if any(shared_sentences(d, descs[:k] + descs[k + 1:]) for k, d in enumerate(descs)):
        problems.append("different modules share description sentences; describe each module in its own words.")
    for m_ctx, got in zip(ctx["modules"], mods):
        i = m_ctx["module"]
        if not isinstance(got, dict):
            problems.append(f"module {i} must be an object."); continue
        missing = [k for k in required if k not in got]
        if missing:
            problems.append(f"module {i}: missing fields {missing}."); continue
        exp = expected_module(prefix, m_ctx)
        for k in ("module", "graphml", "genes", "accessions", "protein_entries", "n_genes", "hpa_gene_annotation",
                  "hpa_gene_annotation_summary", "humap_complexes"):
            if json.loads(json.dumps(got[k])) != json.loads(json.dumps(exp[k])):
                problems.append(f"module {i}: '{k}' does not match the tool result.")
        desc = got["description"]
        if m_ctx["genes"]:
            bad = writing_problems(desc, m_ctx["genes"]) if isinstance(desc, str) else ["it is missing"]
            if bad:
                problems.append(f"module {i}: description rejected: " + "; ".join(bad) + ".")
        elif desc != "":
            problems.append(f"module {i}: modules without genes get an empty description.")
        ihc = got["hpa_ihc_detection"]
        want_ihc = {t: expected_ihc(prefix, t, m_ctx["genes"]) for t in (ctx["tissue_a"], ctx["tissue_b"])}
        if json.loads(json.dumps(ihc)) != json.loads(json.dumps(want_ihc)):
            problems.append(f"module {i}: 'hpa_ihc_detection' does not match the chosen HPA tissues.")
        small = len(m_ctx["genes"]) < MIN_GENES_FOR_ENRICHMENT
        if small:
            if got["go_kegg_enrichment"] is not None or got["string_enrichment"] is not None or not got["enrichment_skipped"]:
                problems.append(f"module {i}: fewer than {MIN_GENES_FOR_ENRICHMENT} genes, so go_kegg_enrichment and "
                                f"string_enrichment must be null and enrichment_skipped must explain why.")
        else:
            if got["enrichment_skipped"] is not None:
                problems.append(f"module {i}: enrichment_skipped must be null for modules with >= {MIN_GENES_FOR_ENRICHMENT} genes.")
            for field, want in (("go_kegg_enrichment", infer_module_function_go_kegg(prefix)[f"module_{i}"]),
                                ("string_enrichment", infer_module_function_string(prefix, i))):
                if json.loads(json.dumps(got[field])) != json.loads(json.dumps(want)):
                    problems.append(f"module {i}: '{field}' does not match the tool result.")
        want_edges = get_module_network_string(prefix)[f"module_{i}"]
        if json.loads(json.dumps(got["string_interactions"])) != json.loads(json.dumps(want_edges)):
            problems.append(f"module {i}: 'string_interactions' does not match the tool result.")
        else:
            n = len(m_ctx["genes"])
            want = {"possible": n * (n - 1) // 2, "with_interaction": len(want_edges)}
            if got["string_interaction_pairs"] != want:
                problems.append(f"module {i}: 'string_interaction_pairs' should be {want}.")
    return problems


def expected_ihc(prefix, tissue, genes):
    """Immunohistochemistry detection in the HPA tissues the agent chose for this tissue group."""
    choice = tissue_choices().get(tissue)
    if choice is None:
        raise ValueError(f"no HPA tissue choice saved for {tissue}")
    if not choice["hpa_tissues"]:
        return {"hpa_tissues": [], "note": choice["note"]}
    return compute_ihc(choice["hpa_tissues"], genes)


_enrich_rows = {}


def enrichment_test_summary(prefix, i):
    """GO/KEGG test summary of one module (global BH), from knowledge/enrichment/module_enrichment_summary.csv."""
    with _cache_lock:
        if not _enrich_rows:
            for r in pd.read_csv(ENRICH / "module_enrichment_summary.csv", keep_default_na=False, dtype=str).to_dict("records"):
                _enrich_rows[(r["pair"], int(r["module"]))] = r
    r = dict(_enrich_rows[(prefix, i)])
    for k in ("module", "n_proteins", "n_input_genes", "n_mapped_genes", "n_background_input", "n_background_mapped",
              "n_tests", "n_within_bh_005", "n_global_bh_005"):
        r[k] = int(r[k])
    for k in ("min_p_raw", "min_q_within", "min_q_global"):
        r[k] = float(r[k])
    return r


ENRICHMENT_STATISTICS = {
    "method": "one-sided hypergeometric; BH within module and across all module-term tests",
    "primary_sources": ["GO:BP", "GO:MF", "GO:CC", "KEGG"], "primary_threshold": "q_global < 0.05",
    "background": "unique HGNC-resolved Ensembl genes of all eligible saved Step 2 consensus nodes, including isolates",
    "all_results": "enrichment/enrichment_all_tests.csv.gz",
    "string_scope": "supplementary STRING within-query FDR only; not corrected across modules",
    "does_not_test": "module structure, co-abundance replication, causal mechanism"}


def build_knowledge(prefix):
    """Assemble the JSON of one pair from the tool annotations, the HPA tissues chosen by the agent and the module
    descriptions written by the agent."""
    ctx = pair_context(prefix)
    st = progress(prefix)
    go = infer_module_function_go_kegg(prefix)
    edges = get_module_network_string(prefix)
    modules = []
    for m in ctx["modules"]:
        i, genes = m["module"], m["genes"]
        per_gene, summary = compute_hpa_gene_annotation(genes, m["accessions"])
        small = len(genes) < MIN_GENES_FOR_ENRICHMENT
        modules.append({
            **m, "n_genes": len(genes), "description": st["descriptions"].get(i, ""),
            "hpa_gene_annotation": per_gene, "hpa_gene_annotation_summary": summary,
            "hpa_ihc_detection": {t: expected_ihc(prefix, t, genes) for t in (ctx["tissue_a"], ctx["tissue_b"])},
            "humap_complexes": compute_humap(m["accessions"], genes),
            "go_kegg_enrichment": None if small else go.get(f"module_{i}", []),
            "string_enrichment": None if small else infer_module_function_string(prefix, i),
            "enrichment_skipped": f"fewer than {MIN_GENES_FOR_ENRICHMENT} genes" if small else None,
            "string_interactions": edges[f"module_{i}"],
            "string_interaction_pairs": {"possible": len(genes) * (len(genes) - 1) // 2,
                                         "with_interaction": len(edges[f"module_{i}"])},
            "enrichment_test_summary": enrichment_test_summary(prefix, i),
            "string_enrichment_scope": "supplementary; original STRING query-level FDR; no across-module control"})
    kb = {k: ctx[k] for k in ("tissue_pair", "tissue_a", "tissue_b", "consensus_proteins",
                              "background_genes", "background_string_ids")}
    kb["enrichment_statistics"] = ENRICHMENT_STATISTICS
    kb["modules"] = modules
    return kb


def write_knowledge(prefix):
    """Assemble and validate the JSON and write {prefix}/bio_knowledge_{prefix}.json; returns the list of problems."""
    kb = build_knowledge(prefix)
    problems = knowledge_problems(prefix, kb)
    if problems:
        return problems
    d = CONFIG["out"] / prefix
    d.mkdir(parents=True, exist_ok=True)
    (d / f"bio_knowledge_{prefix}.json").write_text(json.dumps(kb, indent=1, ensure_ascii=False))
    return []


@tool
def write_summary(tissues_prefix: str, content: str) -> str:
    """
    Writes the LLM prompt that summarises all knowledge of a tissue pair to {tissues_prefix}/summary_{tissues_prefix}.txt.
    It is the input of the next research step.

    Args:
        tissues_prefix: The tissue pair prefix, e.g. 'breast_colon'.
        content: The summary / LLM prompt text.

    Returns:
        str: the saved file path relative to the knowledge folder.
    """
    if not content.strip():
        raise ValueError("The summary is empty.")
    problems = writing_problems(content)
    if problems:
        raise ValueError("summary rejected: " + "; ".join(problems) + ".")
    d = CONFIG["out"] / tissues_prefix
    d.mkdir(parents=True, exist_ok=True)
    path = d / f"summary_{tissues_prefix}.txt"
    path.write_text(content)
    return str(path.relative_to(CONFIG["out"]))


TISSUE_PROMPT = """
  The tissue group "{tissue}" is one of the human tissue groups of ProteomicsDB used to build protein co-abundance
  networks. Choose which normal tissue(s) of the Human Protein Atlas (HPA) tissue atlas represent "{tissue}", so that
  the immunohistochemistry detection of module proteins can be looked up there.

  (1) Use get_hpa_tissue_names() to see all HPA normal tissues.
  (2) Decide which HPA tissue(s) correspond to "{tissue}". A tissue group can match several HPA tissues (for example
  several brain regions) or none (for example body fluids, cell lines and stem cells). Search online if needed.
  (3) Save your decision with save_tissue_group_choice("{tissue}", hpa_tissues, note), explaining your reasoning in note.
"""

SETUP_PROMPT = """
  (1) Get the conserved modules between {tissues} with load_conserved_modules("{prefix}") and understand the data.

  (2) Use get_hpa_tissue_names() to see the HPA normal tissues. For each of {tissues}, choose the matching HPA tissue(s);
  a tissue group can match several HPA tissues or none (for example body fluids, cell lines and stem cells).
  Save your choice for both tissue groups with save_hpa_tissue_choice(); the immunohistochemistry detection of every
  module will be looked up in the tissues you choose here.

  Always remember you are a scientist, feel free to expand the research scope and search online if needed.
"""

MODULE_PROMPT = """
  You work on ONE module of the conserved modules between {tissues}: {module}.

  (1) Print get_module_overview("{prefix}", {module_id}) and read it: the genes, the HPA annotation summary, the most
  GO/KEGG terms passing global BH, supplementary STRING terms (query-level FDR only), hu.MAP 3.0 complexes and STRING interactions.
  Report p_raw and q_global separately, with overlap counts and fold enrichment. Never present STRING query-level FDR as across-module control.
  Functional enrichment supports interpretation; it does not establish significant module structure, replicated co-abundance or causality.
  Some results will be empty, that is normal and NO NEED to change your code!!

  (2) In your next step, write the description of this module yourself and save it with
  save_module_description("{prefix}", {module_id}, description).
  Describe its key genes, the functions, complexes and interactions the annotations point to, and where the genes are
  expressed. If most module genes are plasma / secreted proteins, blood-cell enriched, or broadly expressed
  housekeeping-type genes, point this out, because the shared module may then reflect blood in the samples or shared
  cell types. Do NOT generate the description with code templates or if/else rules!!

  All database annotations are used to interpret the module.
  Always remember you are a scientist, feel free to expand the research scope and search online if needed.
"""

SUMMARY_PROMPT = """
  The conserved modules between {tissues} have been annotated and described. Here are the descriptions:

{descriptions}

  Generate an LLM prompt with all this knowledge and save it with write_summary("{prefix}", ...).
  It is the input of the next research step, so keep every module and write it yourself, not with code templates.
  All database annotations are used to interpret the modules.
"""


# ════════════════════════════════════════════════════════════════════
# Runs
# ════════════════════════════════════════════════════════════════════


def run_agent(prefix, model, task, tools, max_steps, label, attempt):
    """Run the agent once and save its trajectory; returns (error message, input tokens, output tokens)."""
    st = progress(prefix)
    st["step"], st["viewed"], st["saved_at"] = 1, {}, {}

    def next_step(memory_step):
        st["step"] = memory_step.step_number + 1

    agent = CodeAgent(tools=tools, model=model, max_steps=max_steps, planning_interval=PLANNING_INTERVAL,
                      step_callbacks=[next_step], additional_authorized_imports=AUTHORIZED_IMPORTS, verbosity_level=0)
    error, tin, tout = None, 0, 0
    try:
        result = agent.run(PROMPT_HEAD + task, return_full_result=True)
        usage = getattr(result, "token_usage", None)
        if usage is not None:
            tin, tout = usage.input_tokens or 0, usage.output_tokens or 0
        if result.state != "success":
            error = f"agent did not finish normally (state={result.state})"
    except Exception as e:
        error = f"{type(e).__name__}: {e}"
    with open(CONFIG["traces"] / f"{prefix}_{label}_attempt{attempt}.json", "w") as fh:
        json.dump({"task": task, "error": error, "steps": agent.memory.get_full_steps()}, fh,
                  indent=1, default=str, ensure_ascii=False)
    return error, tin, tout


BASE_TOOLS = [DuckDuckGoSearchTool(), read_file, load_conserved_modules, get_hpa_gene_annotation,
              get_gene_complexes_hu_map_3, infer_module_function_go_kegg, infer_module_function_string,
              get_module_network_string]


def run_pair(prefix, model):
    """(1) HPA tissue choice (2) one run per module that writes its description (3) summary (4) JSON assembled by
    the program. Each stage is retried on its own; finished parts are kept."""
    CONFIG["traces"].mkdir(parents=True, exist_ok=True)
    (CONFIG["out"] / prefix).mkdir(parents=True, exist_ok=True)
    a, b = split_pair(prefix)
    ctx = pair_context(prefix)
    st = progress(prefix)
    t0, tokens_in, tokens_out, runs, notes = time.time(), 0, 0, 0, []

    def run(task, tools, max_steps, label, done):
        nonlocal tokens_in, tokens_out, runs
        for attempt in range(1, MAX_ATTEMPTS + 1):
            error, tin, tout = run_agent(prefix, model, task, tools, max_steps, label, attempt)
            tokens_in += tin; tokens_out += tout; runs += 1
            if done():
                return None
        return f"{label} not finished" + (f" ({error[:200]})" if error else "")

    # (1) HPA tissues: use the choice made per tissue group (run_tissue_choice)
    missing = [t for t in (a, b) if t not in tissue_choices()]
    if missing:
        notes.append(f"no HPA tissue choice for {missing}")

    # (2) one run per module
    if not notes:
        for m in ctx["modules"]:
            i = m["module"]
            if not m["genes"] or i in st["descriptions"]:
                continue
            task = MODULE_PROMPT.format(prefix=prefix, tissues=(a, b), module=f"module_{i}", module_id=i)
            problem = run(task, BASE_TOOLS + [get_module_overview, save_module_description],
                          MODULE_STEPS, f"module{i}", lambda i=i: i in st["descriptions"])
            if problem:
                notes.append(f"module {i}: no description")

    # (3) summary
    sm = CONFIG["out"] / prefix / f"summary_{prefix}.txt"
    if not notes and not (sm.exists() and sm.read_text().strip()):
        desc = "\n\n".join(f"  module_{i}: {st['descriptions'][i]}" for i in sorted(st["descriptions"]))
        problem = run(SUMMARY_PROMPT.format(prefix=prefix, tissues=(a, b), descriptions=desc),
                      [DuckDuckGoSearchTool(), read_file, write_summary], SUMMARY_STEPS, "summary",
                      lambda: sm.exists() and sm.read_text().strip() != "")
        if problem:
            notes.append(problem)

    # (4) assemble the JSON
    if not notes:
        notes += write_knowledge(prefix)[:5]
    if not notes:
        progress_path(prefix).unlink(missing_ok=True)
    return dict(name=prefix, attempts=runs, passed=not notes, seconds=round(time.time() - t0),
                input_tokens=tokens_in, output_tokens=tokens_out, note="; ".join(notes)[:500])


def run_tissue_choice(tissue, model):
    """Choose the HPA tissues of one tissue group (fresh agent), at most MAX_ATTEMPTS attempts."""
    CONFIG["traces"].mkdir(parents=True, exist_ok=True)
    t0, tin_all, tout_all = time.time(), 0, 0
    for attempt in range(1, MAX_ATTEMPTS + 1):
        agent = CodeAgent(tools=[DuckDuckGoSearchTool(), get_hpa_tissue_names, save_tissue_group_choice], model=model,
                          max_steps=TISSUE_STEPS, planning_interval=PLANNING_INTERVAL,
                          additional_authorized_imports=AUTHORIZED_IMPORTS, verbosity_level=0)
        task = PROMPT_HEAD + TISSUE_PROMPT.format(tissue=tissue)
        error = None
        try:
            result = agent.run(task, return_full_result=True)
            usage = getattr(result, "token_usage", None)
            if usage is not None:
                tin_all += usage.input_tokens or 0; tout_all += usage.output_tokens or 0
        except Exception as e:
            error = f"{type(e).__name__}: {e}"
        with open(CONFIG["traces"] / f"tissue_{tissue}_attempt{attempt}.json", "w") as fh:
            json.dump({"task": task, "error": error, "steps": agent.memory.get_full_steps()}, fh,
                      indent=1, default=str, ensure_ascii=False)
        if tissue in tissue_choices():
            break
    return dict(name=f"tissue:{tissue}", attempts=attempt, passed=tissue in tissue_choices(), seconds=round(time.time() - t0),
                input_tokens=tin_all, output_tokens=tout_all, note="" if tissue in tissue_choices() else (error or "no choice saved")[:300])


def module_rows(prefix):
    kb = json.loads((CONFIG["out"] / prefix / f"bio_knowledge_{prefix}.json").read_text())
    rows = []
    for m in kb["modules"]:
        ts = m["hpa_gene_annotation_summary"]["tissue_specificity"] if m["genes"] else {}
        rows.append({"pair": prefix, "module": m["module"], "n_genes": m["n_genes"],
                     "go_kegg_terms": None if m["go_kegg_enrichment"] is None else len(m["go_kegg_enrichment"]),
                     "string_terms": None if m["string_enrichment"] is None else len(m["string_enrichment"]),
                     "string_interactions": len(m["string_interactions"]), "humap_complexes": len(m["humap_complexes"]),
                     "hpa_tissue_enriched_or_group_enriched": ts.get("Tissue enriched", 0) + ts.get("Group enriched", 0),
                     "hpa_low_tissue_specificity": ts.get("Low tissue specificity", 0),
                     "hpa_secreted": m["hpa_gene_annotation_summary"]["secreted_genes"] if m["genes"] else 0})
    return rows


def update_csv(path, rows, key):
    new = pd.DataFrame(rows)
    if path.exists():
        old = pd.read_csv(path)
        new = pd.concat([old[~old[key].isin(new[key])], new], ignore_index=True)
    new.to_csv(path, index=False)
    return new


def write_sources():
    path = CONFIG["out"] / "sources.json"
    src = json.loads(path.read_text()) if path.exists() else {
        "HPA gene annotation": {"file": HPA_GENES.name, "file_date": datetime.fromtimestamp(HPA_GENES.stat().st_mtime).date().isoformat(),
                                "url": "https://www.proteinatlas.org/download/proteinatlas.tsv.zip"},
        "HPA tissue atlas (IHC)": {"file": HPA_IHC.name, "detected_levels": sorted(DETECTED_LEVELS),
                                   "tissue_matching": "HPA normal tissues chosen by the agent for each tissue group",
                                   "tissue_map": {t: c["hpa_tissues"] for t, c in tissue_choices().items()}},
        "hu.MAP 3.0": {"file": HUMAP.name, "min_members_in_module": HUMAP_MIN_OVERLAP},
        "GO/KEGG": {"computed_by": "step3_enrichment.py", "sources": ["GO:BP", "GO:MF", "GO:CC", "KEGG"],
                    "correction": "BH within module and across all module-term tests", "primary_threshold": "q_global < 0.05",
                    "background": "all genes of the consensus network of the tissue pair"},
        "STRING": {"url": STRING, "required_score": STRING_SCORE, "enrichment_threshold": "FDR < 0.05",
                   "background": "all proteins in the consensus network of the tissue pair"},
        "min_genes_for_enrichment": MIN_GENES_FOR_ENRICHMENT, "queried_at": []}
    if _cache.get("gprofiler_version"):
        src["g:Profiler"]["version"] = _cache["gprofiler_version"]
    try:
        src["STRING"]["version"] = http("GET", f"{STRING}/json/version").json()[0]["string_version"]
    except Exception:
        pass
    src["queried_at"].append(datetime.now(timezone.utc).isoformat(timespec="seconds"))
    path.write_text(json.dumps(src, indent=1, ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pairs", nargs="+", help="only run these tissue pairs (default: all pairs with modules)")
    ap.add_argument("--out", default=str(CONFIG["out"]), help="output directory")
    ap.add_argument("--traces", default=str(CONFIG["traces"]), help="agent trace directory")
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--model", default=MODEL_ID)
    ap.add_argument("--temperature", default=str(TEMPERATURE), help="a number, or default (no temperature parameter is sent)")
    ap.add_argument("--choices-only", action="store_true", help="only choose the HPA tissues of each tissue group, then stop")
    args = ap.parse_args()
    CONFIG.update(out=Path(args.out), traces=Path(args.traces))
    CONFIG["out"].mkdir(parents=True, exist_ok=True)

    pairs = [p for p in (args.pairs or all_pairs()[0]) if (ANALYSIS / f"{p}.json").exists()]
    def finished(p):
        kb, sm = CONFIG["out"] / p / f"bio_knowledge_{p}.json", CONFIG["out"] / p / f"summary_{p}.txt"
        if not (kb.exists() and sm.exists() and sm.read_text().strip()):
            return False
        return not knowledge_problems(p, json.loads(kb.read_text()))
    done = [p for p in pairs if finished(p)]
    pairs = [p for p in pairs if p not in done]
    if done:
        print(f"skipping {len(done)} finished pairs", flush=True)

    kw = {} if args.temperature == "default" else {"temperature": float(args.temperature)}
    model = OpenAIServerModel(model_id=args.model, api_key=load_api_key(), **kw)

    # (0) choose the HPA tissues once for every tissue group involved
    groups = sorted({t for p in pairs for t in split_pair(p)} - set(tissue_choices()))
    if groups:
        print(f"choosing HPA tissues for {len(groups)} tissue groups", flush=True)
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            for st in pool.map(lambda t: run_tissue_choice(t, model), groups):
                ch = tissue_choices().get(st["name"].split(":", 1)[1], {})
                print(f"  {st['name']:34s} passed={st['passed']} -> {ch.get('hpa_tissues')}  tokens={st['input_tokens']}+{st['output_tokens']}", flush=True)
    if args.choices_only:
        return
    statuses, t0 = [], time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(run_pair, p, model): p for p in pairs}
        for i, fut in enumerate(as_completed(futures), 1):
            p = futures[fut]
            try:
                st = fut.result()
            except Exception:
                st = dict(name=p, attempts=0, passed=False, seconds=0, input_tokens=0, output_tokens=0,
                          note=traceback.format_exc()[-500:])
            statuses.append(st)
            if st["passed"]:
                update_csv(CONFIG["out"] / "module_summary.csv", module_rows(p), "pair")
            print(f"[{i}/{len(pairs)}] {p:45s} passed={st['passed']} attempts={st['attempts']} {st['seconds']}s "
                  f"tokens={st['input_tokens']}+{st['output_tokens']} {st['note'][:80]}", flush=True)
    if statuses:
        write_sources()
        s = update_csv(CONFIG["traces"] / "status.csv", statuses, "name")
        print(f"\npassed {int(s.passed.sum())}/{len(s)}, this run took {(time.time() - t0) / 60:.1f} min, "
              f"tokens {int(s.input_tokens.sum()):,} input + {int(s.output_tokens.sum()):,} output")


if __name__ == "__main__":
    main()
