#!/usr/bin/env python3
"""
Step 2b: permutation filter of the candidate clusters from Step 2.

Test (per tissue pair A-B, every candidate cluster from analysis/{pair}.json, members held fixed):
  observed  number of within-cluster member pairs that are positive edges in both the A and the B network
            (shared edges).
  null      the A network is held fixed and the protein labels of B are permuted among proteins of similar
            degree in B (proteins sorted by B degree, strata of STRATUM proteins, shuffled within strata), so
            the structure of the B network is preserved; the statistic counts the within-cluster A edges that
            are still present in B after relabelling. One permutation acts on all clusters of the pair at once.
  direction done twice (A fixed / B permuted and B fixed / A permuted); the larger P is kept.
  P         (1 + #null >= observed) / (perm + 1); BH correction across all clusters of all pairs;
            a cluster passes when q < 0.05 (column "significant").

The protein set is the node set of the consensus network (analysis/{pair}/consensus_{pair}.pkl: housekeeping
and unannotated proteins already removed). Edges are the edges with weight > 0 in the tissue networks in
graph/. Edges present in both tissue networks but not in the consensus network (or the reverse) are counted
in consensus_mismatch and do not stop the run.

Apply (run after the test unless --no-apply): for every tested pair, analysis/{pair}.json is rewritten as
{"<cluster id>": [member records], ...} with only the clusters that pass (original ids and members kept),
and analysis/{pair}/module_{id}_*.graphml of removed clusters are deleted. If no cluster of a pair passes,
analysis/{pair}.json and the module GraphML files are deleted (the consensus pkl is kept). The columns
"modules" and "proteins_in_modules" of analysis/summary.csv are updated, and "json_written" is set to False
for pairs whose json was deleted. Applying is idempotent.

Inputs   analysis/summary.csv, analysis/{pair}.json, analysis/{pair}/consensus_{pair}.pkl, graph/{tissue}.pkl
Outputs  work/cluster_filter/cluster_results.csv   per cluster: observed count, null means/maxima and P of both
                                                   directions, P, BH q, significant
         work/cluster_filter/pair_results.csv      per pair: proteins, edges, consensus check
         work/cluster_filter/run_config.json, status.json, cluster_filter.log
         (apply) filtered analysis/{pair}.json, module GraphML files and analysis/summary.csv

Usage    python step2b_cluster_filter.py --perm 10000 --workers 40
         python step2b_cluster_filter.py --perm 500 --pairs bone_marrow_liver colon_rectum --no-apply
         python step2b_cluster_filter.py --apply-only
"""
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib
import json
import os
from pathlib import Path
import pickle
import time
import traceback

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import numpy as np
import pandas as pd

from common import PATHS, load_clusters

OUT = PATHS["work"] / "cluster_filter"
LOG_NAME = "cluster_filter.log"
STRATUM = 20  # proteins per degree stratum
_log_file = None


def log(msg=""):
    print(msg, flush=True)
    if _log_file is not None:
        with open(_log_file, "a") as fh:
            fh.write(f"{msg}\n")


def bh(p):
    p = np.asarray(p, dtype=float)
    n = len(p)
    order = np.argsort(p)
    q = p[order] * n / np.arange(1, n + 1)
    q = np.minimum.accumulate(q[::-1])[::-1]
    out = np.empty(n)
    out[order] = np.minimum(q, 1.0)
    return out


def positive_keys(tissue, pos, P):
    """Edges of a tissue network with weight > 0 and both ends in the protein set, encoded as min*P+max, sorted and unique."""
    g = pickle.loads((PATHS["graph"] / f"{tissue}.pkl").read_bytes())
    if g.ecount() == 0:
        return np.zeros(0, dtype=np.int64)
    el = np.asarray(g.get_edgelist(), dtype=np.int64)
    w = np.asarray(g.es["weight"], dtype=float)
    m = np.array([pos.get(n, -1) for n in g.vs["name"]], dtype=np.int64)
    a, b = m[el[:, 0]], m[el[:, 1]]
    ok = (a >= 0) & (b >= 0) & (w > 0)
    a, b = a[ok], b[ok]
    return np.unique(np.minimum(a, b) * P + np.maximum(a, b))


def contains(sorted_keys, q):
    if len(sorted_keys) == 0:
        return np.zeros(len(q), dtype=bool)
    i = np.searchsorted(sorted_keys, q)
    i[i == len(sorted_keys)] = 0
    return sorted_keys[i] == q


def strata_of(keys, P):
    """Sort proteins by degree (ties by index) and cut into strata of STRATUM proteins; a short tail joins the previous stratum."""
    deg = np.bincount(np.concatenate([keys // P, keys % P]), minlength=P) if len(keys) else np.zeros(P, int)
    order = np.lexsort((np.arange(P), deg))
    nb = max(1, P // STRATUM)
    strata = np.empty(P, dtype=np.int64)
    for s, chunk in enumerate(np.array_split(order, nb)):
        strata[chunk] = s
    return strata


def null_counts(fixed_pairs, cid, n_clusters, other_keys, strata, P, perm, rng):
    """fixed_pairs: ends (u, v) of within-cluster edges in the fixed network; after permuting the labels of the
    other side within degree strata, count for each cluster how many of these edges are still present."""
    u, v = fixed_pairs
    base = np.argsort(strata, kind="stable")
    out = np.zeros((perm, n_clusters), dtype=np.int64)
    for r in range(perm):
        shuffled = np.lexsort((rng.random(P), strata))
        pi = np.empty(P, dtype=np.int64)
        pi[base] = shuffled
        x, y = pi[u], pi[v]
        hit = contains(other_keys, np.minimum(x, y) * P + np.maximum(x, y))
        out[r] = np.bincount(cid[hit], minlength=n_clusters)
    return out


def run_pair(task):
    pair, tissue_a, tissue_b, perm = task
    t0 = time.time()
    gC = pickle.loads((PATHS["analysis"] / pair / f"consensus_{pair}.pkl").read_bytes())
    jp = PATHS["analysis"] / f"{pair}.json"
    clusters = load_clusters(jp) if jp.exists() else {}
    ids = sorted(clusters)  # cluster ids from the file (not necessarily contiguous)
    saved = [[x["protein_entry"] for x in clusters[k]] for k in ids]
    names = gC.vs["name"]
    P = len(names)
    pos = {n: i for i, n in enumerate(names)}
    kA = positive_keys(tissue_a, pos, P)
    kB = positive_keys(tissue_b, pos, P)
    kC = np.unique(np.array([min(e) * P + max(e) for e in gC.get_edgelist()], dtype=np.int64))
    k_shared = np.intersect1d(kA, kB)
    pair_row = dict(pair=pair, tissue_a=tissue_a, tissue_b=tissue_b, proteins=P,
                    edges_a=len(kA), edges_b=len(kB), shared_edges=len(k_shared), consensus_edges=len(kC),
                    consensus_mismatch=int(len(np.setxor1d(k_shared, kC))), clusters=len(saved))
    if not saved:
        pair_row["seconds"] = round(time.time() - t0, 1)
        return pair_row, []

    # all member pairs of each cluster (j = position in `ids`); record which are present in A and in B
    cl_pairs, cid = [], []
    for j, m in enumerate(saved):
        idx = np.array([pos[x] for x in m], dtype=np.int64)
        iu, ju = np.triu_indices(len(idx), 1)
        a, b = np.minimum(idx[iu], idx[ju]), np.maximum(idx[iu], idx[ju])
        cl_pairs.append((a, b))
        cid.append(np.full(len(a), j))
    a_all = np.concatenate([p[0] for p in cl_pairs])
    b_all = np.concatenate([p[1] for p in cl_pairs])
    cid = np.concatenate(cid)
    keys_all = a_all * P + b_all
    inA, inB = contains(kA, keys_all), contains(kB, keys_all)
    n = len(saved)
    obs = np.bincount(cid[inA & inB], minlength=n)
    e_a = np.bincount(cid[inA], minlength=n)
    e_b = np.bincount(cid[inB], minlength=n)

    seed = int.from_bytes(hashlib.sha256(f"cluster-preservation-v1:{pair}".encode()).digest()[:4], "big")
    rng = np.random.default_rng(seed)
    null_ab = null_counts((a_all[inA], b_all[inA]), cid[inA], n, kB, strata_of(kB, P), P, perm, rng)  # A fixed, B permuted
    null_ba = null_counts((a_all[inB], b_all[inB]), cid[inB], n, kA, strata_of(kA, P), P, perm, rng)  # B fixed, A permuted
    p_ab = (1 + (null_ab >= obs).sum(0)) / (perm + 1)
    p_ba = (1 + (null_ba >= obs).sum(0)) / (perm + 1)
    rows = [dict(pair=pair, cluster_id=ids[j], size=len(saved[j]), edges_in_a=int(e_a[j]), edges_in_b=int(e_b[j]),
                 shared_edges=int(obs[j]),
                 null_mean_fix_a=float(null_ab[:, j].mean()), null_max_fix_a=int(null_ab[:, j].max()), p_fix_a=float(p_ab[j]),
                 null_mean_fix_b=float(null_ba[:, j].mean()), null_max_fix_b=int(null_ba[:, j].max()), p_fix_b=float(p_ba[j]),
                 p=float(max(p_ab[j], p_ba[j])))
            for j in range(n)]
    pair_row.update(seed=seed, seconds=round(time.time() - t0, 1))
    return pair_row, rows


def export(pair_rows, rows, total, failures, out):
    complete = len(pair_rows) == total and not failures
    if pair_rows:
        pd.DataFrame(pair_rows).sort_values("pair").to_csv(out / "pair_results.csv", index=False)
    if rows:
        df = pd.DataFrame(rows).sort_values(["pair", "cluster_id"])
        if complete:
            df["q"] = bh(df.p)
            df["significant"] = df.q < 0.05
        df.to_csv(out / "cluster_results.csv", index=False)
    (out / "status.json").write_text(json.dumps(dict(
        complete=complete, finished_pairs=len(pair_rows), total_pairs=total, failures=failures), indent=2))
    return complete


def run_test(summary, args, out):
    (out / "run_config.json").write_text(json.dumps(dict(
        perm=args.perm, workers=args.workers, stratum_size=STRATUM, pairs=summary.pair.tolist(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), numpy_version=np.__version__), indent=2))
    tasks = [(r.pair, r.tissue_a, r.tissue_b, args.perm) for r in summary.sort_values("consensus_edges", ascending=False).itertuples()]
    pair_rows, rows, failures = [], [], {}
    log(f"{len(tasks)} pairs; B={args.perm}; workers={args.workers}")
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(run_pair, t): t[0] for t in tasks}
        for fut in as_completed(futs):
            pair = futs[fut]
            try:
                pr, rs = fut.result()
                pair_rows.append(pr)
                rows.extend(rs)
                worst = max((r["p"] for r in rs), default=float("nan"))
                log(f"[{len(pair_rows)}/{len(tasks)}] {pair} clusters={pr['clusters']} max_p={worst:.5f} "
                    f"mismatch={pr['consensus_mismatch']} ({pr['seconds']}s)")
            except Exception as exc:
                failures[pair] = repr(exc)
                log(f"FAILED {pair}:\n{traceback.format_exc()}")
            export(pair_rows, rows, len(tasks), failures, out)
    if failures:
        raise SystemExit(f"{len(failures)} pairs failed; no final BH correction, nothing applied")
    df = pd.read_csv(out / "cluster_results.csv")
    log(f"COMPLETE: {int(df.significant.sum())}/{len(df)} clusters q<0.05")


def apply_filter(out, pairs=None):
    """Keep only the clusters with significant == True in analysis/{pair}.json; delete GraphML files of removed clusters."""
    res_path = out / "cluster_results.csv"
    if not res_path.exists():
        raise SystemExit(f"{res_path} not found; run the test first")
    status = out / "status.json"
    if status.exists() and not json.loads(status.read_text()).get("complete", False):
        raise SystemExit(f"{status}: the test run is incomplete; nothing applied")
    res = pd.read_csv(res_path)
    if "significant" not in res.columns:
        raise SystemExit(f"{res_path} has no 'significant' column (incomplete run); nothing applied")
    if pairs:
        res = res[res.pair.isin(pairs)]
    analysis = PATHS["analysis"]
    counts = {}
    kept_total = removed_total = 0
    for pair, grp in res.groupby("pair", sort=True):
        jp = analysis / f"{pair}.json"
        mod_dir = analysis / pair
        if not jp.exists():
            log(f"apply: {pair}: {jp.name} not found, skipped")
            continue
        clusters = load_clusters(jp)
        tested = {int(r.cluster_id): (int(r.size), bool(r.significant)) for r in grp.itertuples()}
        untested = sorted(set(clusters) - set(tested))
        bad = [k for k in clusters if k in tested and tested[k][0] != len(clusters[k])]
        if untested or bad:
            raise SystemExit(f"apply: {pair}: {jp.name} does not match {res_path.name} "
                             f"(untested ids {untested}, size mismatch {bad}); rerun the test")
        keep = {k: clusters[k] for k in sorted(clusters) if tested[k][1]}
        removed = [k for k in sorted(clusters) if k not in keep]
        if keep:
            text = json.dumps({str(k): v for k, v in keep.items()}, indent=1, ensure_ascii=False)
            if jp.read_text() != text:
                jp.write_text(text)
        else:
            jp.unlink()
        for k in (removed if keep else sorted(clusters)):
            for f in mod_dir.glob(f"module_{k}_*.graphml"):
                f.unlink()
        counts[pair] = (len(keep), sum(len(v) for v in keep.values()))
        kept_total += len(keep)
        removed_total += len(removed)
        if removed:
            log(f"apply: {pair}: kept {len(keep)}, removed {len(removed)} {removed}"
                + ("" if keep else " (json deleted)"))

    summary_path = analysis / "summary.csv"
    if summary_path.exists() and counts:
        summary = pd.read_csv(summary_path)
        new = summary.copy()
        for pair, (n_mod, n_prot) in counts.items():
            sel = new.pair == pair
            new.loc[sel, "modules"] = n_mod
            new.loc[sel, "proteins_in_modules"] = n_prot
            if "json_written" in new.columns:
                new.loc[sel, "json_written"] = n_mod > 0
        if not new.equals(summary):
            eol = "\r\n" if b"\r\n" in summary_path.read_bytes() else "\n"  # keep the file's line endings
            new.to_csv(summary_path, index=False, lineterminator=eol)
    pairs_kept = sum(1 for n_mod, _ in counts.values() if n_mod > 0)
    log(f"APPLIED: kept {kept_total} modules in {pairs_kept} pairs "
        f"(removed {removed_total} modules; {len(counts) - pairs_kept} pairs left without modules)")


def main():
    global _log_file
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--perm", type=int, default=10000, help="number of permutations per direction (default 10000)")
    ap.add_argument("--workers", type=int, default=40)
    ap.add_argument("--pairs", nargs="+", help="tissue pairs to test/apply (default: all pairs in analysis/summary.csv)")
    ap.add_argument("--out", type=Path, default=OUT, help="output folder (default: <work>/cluster_filter)")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--no-apply", action="store_true", help="run the test only; leave analysis/ unchanged")
    mode.add_argument("--apply-only", action="store_true", help="apply an existing cluster_results.csv without recomputing")
    args = ap.parse_args()
    out = args.out
    out.mkdir(parents=True, exist_ok=True)
    _log_file = out / LOG_NAME

    if args.apply_only:
        apply_filter(out, args.pairs)
        return

    summary = pd.read_csv(PATHS["analysis"] / "summary.csv")
    if args.pairs:
        unknown = set(args.pairs) - set(summary.pair)
        if unknown:
            ap.error(f"unknown tissue pairs: {sorted(unknown)}")
        summary = summary[summary.pair.isin(args.pairs)]
    has_json = summary.pair.map(lambda p: (PATHS["analysis"] / f"{p}.json").exists())
    if (~has_json).any():
        log(f"skipping {int((~has_json).sum())} pairs without analysis/{{pair}}.json")
    summary = summary[has_json]
    if summary.empty:
        raise SystemExit("no tissue pairs with cluster files to test")
    run_test(summary, args, out)
    if not args.no_apply:
        apply_filter(out, summary.pair.tolist())


if __name__ == "__main__":
    main()
