#!/usr/bin/env python3
"""
Step 1: per-tissue protein co-abundance networks (agent workflow)

For each tissue the agent (smolagents CodeAgent, OpenAI GPT-4.1) checks whether the network already exists,
looks up the tissue list, loads the protein abundance matrix, builds the network with a tool and checks its quality.

Network rule (applied inside the build_co_abundance_network tool, identical for all tissues): proteins i and j are
linked if and only if
  (1) they are both measured in n_ij >= N shared samples (default 10)
  (2) the Benjamini-Hochberg FDR within the tissue is < 0.05 (corrected over all pairs with n_ij >= N)
  (3) |r| >= 0.8
r is the Pearson correlation over the shared samples only; the p value comes from t = r * sqrt((n_ij - 2) / (1 - r^2))
with n_ij - 2 degrees of freedom, two-sided.
Edge weight = r (sign kept); nodes = proteins measured in at least N samples; the mixed group (mixed samples) gets
no network.

After the agent finishes we check that the run ended normally, that the tool actually built this tissue and that the
network file was saved completely; otherwise the agent is rerun with a description of the problem, at most 3 times.

Input   <data>/proteins/{tissue}.parquet
Output  <graph>/{tissue}.pkl            igraph: vs["name"], es["weight"], g["tissue_group"]
        <graph>/summary.csv             per tissue: N, samples, nodes, edges, status
        <traces>/step1/                 full trajectory of every run of every tissue, plus status.csv
(<data>, <graph>, <traces> are the directories configured in config.yaml)

Usage   python step1_tissue_networks.py                                       # all tissues
        python step1_tissue_networks.py --tissues liver prostate
        python step1_tissue_networks.py --tissues adipose --min-shared-samples 5
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "16")

import argparse
import json
import pickle
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import igraph as ig
import numpy as np
import pandas as pd
from scipy import stats
from smolagents import CodeAgent, OpenAIServerModel, tool

from common import PATHS, load_api_key

PROTEINS = PATHS["data"] / "proteins"

FDR = 0.05
MIN_ABS_R = 0.8
EXCLUDE = {"mixed"}

MODEL_ID = "gpt-4.1"
TEMPERATURE = 0.5
MAX_STEPS = 12
PLANNING_INTERVAL = 12
MAX_ATTEMPTS = 3
AUTHORIZED_IMPORTS = ["json", "math", "pandas", "numpy", "igraph"]

PROMPT_HEAD = ("\nYou are a top rated biological researcher and you are doing research related to "
               "protein co-abundance network in multiple human tissue groups.\n")

# Runtime settings (set from the command line)
CONFIG = {"min_shared_samples": 10, "graphs": PATHS["graph"], "traces": PATHS["traces"] / "step1"}
_records: dict = {}                     # build results recorded by the tool: tissue -> statistics
_records_lock = threading.Lock()
_build_slots = threading.Semaphore(2)   # at most 2 tissues compute correlation matrices at once


# ════════════════════════════════════════════════════════════════════
# Computation
# ════════════════════════════════════════════════════════════════════
def pairwise_corr(mat: pd.DataFrame):
    """Pairwise-complete Pearson: each protein pair uses only samples where both are measured. Returns r, the number
    of shared samples n (diagonal 0) and the number of measured samples per protein."""
    X = mat.to_numpy(np.float64)
    M = ~np.isnan(X)
    X0 = np.where(M, X, 0.0)
    Mf = M.astype(np.float64)
    n = Mf.T @ Mf
    Sx = X0.T @ Mf
    Sxy = X0.T @ X0
    Sxx = (X0 * X0).T @ Mf
    with np.errstate(invalid="ignore", divide="ignore"):
        r = (n * Sxy - Sx * Sx.T) / np.sqrt((n * Sxx - Sx * Sx) * (n * Sxx.T - Sx.T * Sx.T))
    np.fill_diagonal(n, 0)
    return r, n.astype(np.int32), M.sum(axis=0)


def bh_min_abs_r(r_vec, n_vec, n_max):
    """BH correction over all tested protein pairs. Returns (p*, r_crit); r_crit[n] is the minimum |r| that reaches
    the FDR with n shared samples."""
    df = n_vec.astype(np.float64) - 2
    rr = np.clip(np.abs(r_vec), 0, 1 - 1e-15)
    p = 2 * stats.t.sf(rr * np.sqrt(df / (1 - rr * rr)), df)
    p[~np.isfinite(p)] = 1.0
    p.sort()
    m = len(p)
    passed = np.nonzero(p <= FDR * np.arange(1, m + 1) / m)[0]
    r_crit = np.full(n_max + 1, np.inf)
    if len(passed) == 0:
        return None, r_crit
    p_star = p[passed[-1]]
    for k in range(3, n_max + 1):
        t = stats.t.isf(p_star / 2, k - 2)
        r_crit[k] = t / np.sqrt(t * t + k - 2)
    return p_star, r_crit


def build_network(tissue: str, mat: pd.DataFrame, min_shared: int):
    r, n, n_obs = pairwise_corr(mat)
    testable = n >= min_shared
    upper = np.triu(testable, 1)
    p_star, r_crit = bh_min_abs_r(r[upper], n[upper], int(n.max()))
    keep = testable & (np.abs(r) >= np.maximum(MIN_ABS_R, r_crit[n]))
    u, v = np.nonzero(np.triu(keep, 1))
    nodes = np.where(n_obs >= min_shared)[0]
    new_index = np.full(mat.shape[1], -1)
    new_index[nodes] = np.arange(len(nodes))
    g = ig.Graph(n=len(nodes), edges=np.column_stack([new_index[u], new_index[v]]), directed=False)
    g.vs["name"] = mat.columns[nodes].tolist()
    g.es["weight"] = r[u, v].tolist()
    g["tissue_group"] = tissue
    return g, int(upper.sum()), p_star


# ════════════════════════════════════════════════════════════════════
# Tools
# ════════════════════════════════════════════════════════════════════
@tool
def get_tissue_list() -> dict:
    """
    Retrieves all tissue groups that have a protein abundance matrix, with their number of samples.

    Returns:
        dict: tissue group name -> number of samples.
    """
    return {f.stem: int(pd.read_parquet(f, columns=[]).shape[0]) for f in sorted(PROTEINS.glob("*.parquet"))}


@tool
def get_proteins(tissue_group: str) -> Any:
    """
    Retrieves the protein abundance matrix of a tissue group. Rows are sample_id, columns are proteins,
    values are log10 normalized expression, missing measurements are NaN. The matrix is large; never print it whole.

    Args:
        tissue_group: The tissue group name.

    Returns:
        pandas.DataFrame: sample x protein abundance matrix.
    """
    path = PROTEINS / f"{tissue_group}.parquet"
    if not path.exists():
        raise ValueError(f"No protein data for tissue group '{tissue_group}'.")
    return pd.read_parquet(path)


@tool
def build_co_abundance_network(protein_matrix: Any, tissue_group_name: str) -> dict:
    """
    Builds and saves the protein co-abundance network of one tissue group with the pre-specified rule:
    an edge links proteins i and j if they share at least N samples, the Pearson correlation is significant
    after Benjamini-Hochberg correction within the tissue (FDR < 0.05), and |r| >= 0.8. Edge weight is r.
    The rule is fixed; do not filter proteins or choose thresholds yourself. Build only one network per call.

    Args:
        protein_matrix: The sample x protein matrix returned by get_proteins().
        tissue_group_name: The tissue group name.

    Returns:
        dict: status ("included" or the reason it was excluded), numbers of nodes and edges.
    """
    N = CONFIG["min_shared_samples"]
    mat = protein_matrix
    rec = dict(tissue=tissue_group_name, min_shared_samples=N, samples=int(mat.shape[0]), proteins=int(mat.shape[1]),
               nodes=0, edges=0, positive_edges=0, tested_pairs=0, bh_p_threshold=np.nan)
    if tissue_group_name in EXCLUDE:
        rec["status"] = "excluded: mixed samples"
    elif mat.shape[0] < N:
        rec["status"] = f"excluded: samples < {N}"
    else:
        with _build_slots:
            g, tested, p_star = build_network(tissue_group_name, mat, N)
        w = np.asarray(g.es["weight"])
        rec.update(nodes=g.vcount(), edges=g.ecount(), positive_edges=int((w > 0).sum()),
                   tested_pairs=tested, bh_p_threshold=p_star)
        if g.ecount() == 0:
            rec["status"] = "excluded: no edges"
        else:
            CONFIG["graphs"].mkdir(parents=True, exist_ok=True)
            with open(CONFIG["graphs"] / f"{tissue_group_name}.pkl", "wb") as fh:
                pickle.dump(g, fh, protocol=pickle.HIGHEST_PROTOCOL)
            rec["status"] = "included"
    with _records_lock:
        _records[tissue_group_name] = rec
    return {k: rec[k] for k in ("tissue", "status", "samples", "nodes", "edges")}


@tool
def get_network(tissue_group: str) -> dict:
    """
    Checks whether the co-abundance network of a tissue group has been built, and summarises it.

    Args:
        tissue_group: The tissue group name.

    Returns:
        dict: exists (bool); if it exists, numbers of nodes, edges, positive edges, connected components
        and the fraction of nodes in the largest component.
    """
    path = CONFIG["graphs"] / f"{tissue_group}.pkl"
    if not path.exists():
        return {"tissue_group": tissue_group, "exists": False}
    with open(path, "rb") as fh:
        g = pickle.load(fh)
    comps = g.connected_components()
    return {"tissue_group": tissue_group, "exists": True, "nodes": g.vcount(), "edges": g.ecount(),
            "positive_edges": int(sum(w > 0 for w in g.es["weight"])), "components": len(comps),
            "largest_component_fraction": round(max(comps.sizes()) / g.vcount(), 3)}


PROMPT = """
  Do these steps for the tissue group "{tissue}":

    (0) Use get_network() to see if there's a network for {tissue}. If the network exists, end all operations!!

    (1) Use get_tissue_list() to get all tissue groups and their numbers of samples. Only focus on {tissue}.

    (2) Use get_proteins() to get the sample x protein abundance matrix of {tissue}.
    Always remember don't print the whole protein data, it's too long!!

    (3) Build the protein co-abundance network for {tissue} with build_co_abundance_network().
    The edge rule is pre-specified inside the tool (shared samples >= N, BH FDR < 0.05, |r| >= 0.8).
    Do NOT filter proteins, change thresholds or compute correlations yourself!!
    If the tool reports that the tissue group is excluded, end all operations and report the reason.

    (4) Use get_network() to get the generated network and report its quality: numbers of nodes and edges,
    connectivity and the largest component. Do NOT rebuild the network!!

    Write code step by step, don't generate all code at one time!!
    Finally, call final_answer() with a short summary of what you did and the network statistics.
"""


# ════════════════════════════════════════════════════════════════════
# Run
# ════════════════════════════════════════════════════════════════════
def check_output(tissue: str) -> str | None:
    rec = _records.get(tissue)
    if rec is None:
        return "build_co_abundance_network() was not called for this tissue group."
    path = CONFIG["graphs"] / f"{tissue}.pkl"
    if rec["status"] != "included":
        return f"{tissue} is excluded, but a network file exists." if path.exists() else None
    if not path.exists():
        return f"network file for {tissue} was not saved."
    with open(path, "rb") as fh:
        g = pickle.load(fh)
    if (g.vcount(), g.ecount()) != (rec["nodes"], rec["edges"]):
        return f"saved network of {tissue} does not match the build result."
    return None


def run_tissue(tissue: str, model) -> dict:
    CONFIG["traces"].mkdir(parents=True, exist_ok=True)
    t0, feedback, tokens_in, tokens_out = time.time(), "", 0, 0
    for attempt in range(1, MAX_ATTEMPTS + 1):
        with _records_lock:
            _records.pop(tissue, None)
        (CONFIG["graphs"] / f"{tissue}.pkl").unlink(missing_ok=True)
        agent = CodeAgent(tools=[get_tissue_list, get_proteins, build_co_abundance_network, get_network],
                          model=model, max_steps=MAX_STEPS, planning_interval=PLANNING_INTERVAL,
                          additional_authorized_imports=AUTHORIZED_IMPORTS, verbosity_level=0)
        task = PROMPT_HEAD + PROMPT.format(tissue=tissue)
        if feedback:
            task += f"\nA previous attempt was not completed: {feedback}\nStart over and fix this.\n"
        error = None
        try:
            result = agent.run(task, return_full_result=True)
            usage = getattr(result, "token_usage", None)
            if usage is not None:
                tokens_in += usage.input_tokens or 0
                tokens_out += usage.output_tokens or 0
            if result.state != "success":
                error = f"agent did not finish normally (state={result.state})"
        except Exception as e:
            error = f"{type(e).__name__}: {e}"
        with open(CONFIG["traces"] / f"{tissue}_attempt{attempt}.json", "w") as fh:
            json.dump({"task": task, "error": error, "steps": agent.memory.get_full_steps()}, fh,
                      indent=1, default=str, ensure_ascii=False)
        problem = check_output(tissue) or (None if error is None else "the agent run did not complete successfully")
        if problem is None:
            return dict(name=tissue, attempts=attempt, passed=True, seconds=round(time.time() - t0),
                        input_tokens=tokens_in, output_tokens=tokens_out, note="")
        feedback = problem if error is None else f"{problem} ({error[:300]})"
    return dict(name=tissue, attempts=MAX_ATTEMPTS, passed=False, seconds=round(time.time() - t0),
                input_tokens=tokens_in, output_tokens=tokens_out, note=feedback[:500])


def update_csv(path: Path, rows: list, key: str):
    new = pd.DataFrame(rows)
    if path.exists():
        old = pd.read_csv(path)
        new = pd.concat([old[~old[key].isin(new[key])], new], ignore_index=True)
    new.to_csv(path, index=False)
    return new


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tissues", nargs="+", help="run only these tissues (default: all)")
    ap.add_argument("--min-shared-samples", type=int, default=10)
    ap.add_argument("--graphs", default=str(CONFIG["graphs"]), help="network output directory")
    ap.add_argument("--traces", default=str(CONFIG["traces"]), help="agent trace directory")
    ap.add_argument("--workers", type=int, default=2)
    args = ap.parse_args()
    CONFIG.update(min_shared_samples=args.min_shared_samples, graphs=Path(args.graphs), traces=Path(args.traces))
    CONFIG["graphs"].mkdir(parents=True, exist_ok=True)

    tissues = args.tissues or sorted(f.stem for f in PROTEINS.glob("*.parquet"))
    summary_path = CONFIG["graphs"] / "summary.csv"
    if summary_path.exists():
        s = pd.read_csv(summary_path)
        done = {r.tissue for r in s.itertuples()
                if r.status != "included" or (CONFIG["graphs"] / f"{r.tissue}.pkl").exists()}
        skipped = [t for t in tissues if t in done]
        tissues = [t for t in tissues if t not in done]
        if skipped:
            print(f"Skipping {len(skipped)} tissues that are already done", flush=True)

    model = OpenAIServerModel(model_id=MODEL_ID, api_key=load_api_key(), temperature=TEMPERATURE)
    statuses, t0 = [], time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(run_tissue, t, model): t for t in tissues}
        for i, fut in enumerate(as_completed(futures), 1):
            t = futures[fut]
            try:
                st = fut.result()
            except Exception:
                st = dict(name=t, attempts=0, passed=False, seconds=0, input_tokens=0, output_tokens=0,
                          note=traceback.format_exc()[-500:])
            statuses.append(st)
            if st["passed"]:
                update_csv(summary_path, [_records[t]], "tissue")
            rec = _records.get(t, {})
            print(f"[{i}/{len(tissues)}] {t:26s} passed={st['passed']} attempts={st['attempts']} "
                  f"{rec.get('status', '-')} nodes={rec.get('nodes', '-')} edges={rec.get('edges', '-')} "
                  f"{st['seconds']}s tokens={st['input_tokens']}+{st['output_tokens']} {st['note'][:80]}", flush=True)

    if statuses:
        s = update_csv(CONFIG["traces"] / "status.csv", statuses, "name")
        print(f"\nPassed {int(s.passed.sum())}/{len(s)}, this run took {(time.time() - t0) / 60:.1f} min, "
              f"tokens {int(s.input_tokens.sum()):,} input + {int(s.output_tokens.sum()):,} output")


if __name__ == "__main__":
    main()
