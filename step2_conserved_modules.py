#!/usr/bin/env python3
"""
Step 2: conserved co-abundance modules of every tissue pair (agent workflow)

For each tissue pair the agent (smolagents CodeAgent, OpenAI GPT-4.1) calls the tools in order:
  (1) consensus network: nodes and edges shared by both tissues, edge weight = min(w_A, w_B), only edges > 0 kept;
      protein entry names are mapped to UniProt accessions and gene names (local table); unmapped proteins and
      housekeeping genes are removed when the network is built
  (2) Leiden modules: modularity, resolution 1.0, seed 42; communities with 5-50 members and mean edge
      weight >= 0.15 are kept, each module is saved as a GraphML file
  (3) save_modules_json() saves the module JSON: the tool checks the format and compares every module with the
      modules of this pair; on failure it returns the specific problems and the agent fixes and resubmits
  (4) a markdown analysis note is written
Pairs without modules get no JSON file.

Before the final answer the agent's JSON is checked; after the run all outputs are checked again, and an incomplete
run is restarted with a description of the problem, up to 3 attempts.
Candidate modules are filtered by step2b_cluster_filter.py.

Input    graph/{tissue}.pkl
         data/uniprot_human_reviewed.tsv
         data/Housekeeping_GenesHuman.csv
Output   analysis/{tissueA}_{tissueB}.json          [ [ {protein_entry, accession, gene}, ... ], ... ], element i is module_i
         analysis/{tissueA}_{tissueB}/consensus_{tissueA}_{tissueB}.pkl
         analysis/{tissueA}_{tissueB}/module_{i}_sz{size}_d{mean weight}.graphml
         analysis/{tissueA}_{tissueB}/analysis_{tissueA}_{tissueB}.md
         analysis/summary.csv                       consensus size, module count and member count of every pair
         agent_traces/step2/                        full trajectory of every run of every pair, and status.csv
         (folders as configured in config.yaml)

Usage    python step2_conserved_modules.py                       # all tissue pairs
         python step2_conserved_modules.py --pairs brain_colon liver_prostate
"""
import argparse
import itertools
import json
import pickle
import random
import sys
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import igraph as ig
import numpy as np
import pandas as pd
from smolagents import CodeAgent, OpenAIServerModel, tool

from common import PATHS, load_api_key, load_clusters

UNIPROT_TSV = PATHS["data"] / "uniprot_human_reviewed.tsv"
HK_CSV = PATHS["data"] / "Housekeeping_GenesHuman.csv"

SEED = 42
RESOLUTION = 1.0
MIN_SIZE, MAX_SIZE = 5, 50
MIN_DENSITY = 0.15

MODEL_ID = "gpt-4.1"
TEMPERATURE = 0.5
MAX_STEPS = 20
PLANNING_INTERVAL = 16
MAX_ATTEMPTS = 3
AUTHORIZED_IMPORTS = ["json", "math", "pandas", "numpy", "igraph"]

PROMPT_HEAD = ("\nYou are a top rated biological researcher and you are doing research related to "
               "protein co-abundance network in multiple human tissue groups.\n")

CONFIG = {"graphs": PATHS["graph"], "out": PATHS["analysis"], "traces": PATHS["traces"] / "step2"}
_cache: dict = {}
_cache_lock = threading.RLock()
_leiden_lock = threading.Lock()         # igraph's RNG is process-global, so Leiden runs serially
_records: dict = {}                     # tool records: tissue pair -> consensus and module statistics
_records_lock = threading.Lock()


def cached(key, fn):
    with _cache_lock:
        if key not in _cache:
            _cache[key] = fn()
        return _cache[key]


# ════════════════════════════════════════════════════════════════════
# Computation
# ════════════════════════════════════════════════════════════════════
def load_graph(tissue: str) -> ig.Graph:
    with open(CONFIG["graphs"] / f"{tissue}.pkl", "rb") as fh:
        return pickle.load(fh)


def consensus_network(gA: ig.Graph, gB: ig.Graph) -> ig.Graph:
    """Shared nodes sorted by name; edges present in both networks, weight = min, only > 0 kept. Edges are sorted by node index for reproducibility."""
    common = sorted(set(gA.vs["name"]) & set(gB.vs["name"]))
    P = len(common)
    pos = {name: i for i, name in enumerate(common)}

    def edge_keys(g):
        if g.ecount() == 0:
            return np.array([], dtype=np.int64), np.array([])
        el = np.array(g.get_edgelist(), dtype=np.int64)
        to_common = np.array([pos.get(name, -1) for name in g.vs["name"]], dtype=np.int64)
        a, b = to_common[el[:, 0]], to_common[el[:, 1]]
        ok = (a >= 0) & (b >= 0)
        a, b = a[ok], b[ok]
        return np.minimum(a, b) * P + np.maximum(a, b), np.asarray(g.es["weight"])[ok]

    kA, wA = edge_keys(gA)
    kB, wB = edge_keys(gB)
    keys, ia, ib = np.intersect1d(kA, kB, assume_unique=True, return_indices=True)
    w = np.minimum(wA[ia], wB[ib])
    keep = w > 0
    keys, w = keys[keep], w[keep]
    gC = ig.Graph(n=P, edges=np.column_stack([keys // P, keys % P]) if len(keys) else [], directed=False)
    gC.vs["name"] = common
    gC.es["weight"] = w.tolist()
    return gC


def leiden_modules(gC: ig.Graph, save_dir: Path | None):
    """Leiden communities filtered into modules; if save_dir is not None, each module is written as GraphML. Returns (modules, number of communities)."""
    with _leiden_lock:
        random.seed(SEED)
        np.random.seed(SEED)
        ig.set_random_number_generator(random.Random(SEED))
        part = gC.community_leiden(
            weights=gC.es["weight"] if "weight" in gC.es.attributes() else None,
            objective_function="modularity", resolution=RESOLUTION, n_iterations=-1)
        modules = []
        for comm in part:
            if not (MIN_SIZE <= len(comm) <= MAX_SIZE):
                continue
            sub = gC.subgraph(comm)
            ws = sub.es["weight"] if "weight" in sub.es.attributes() else [1.0] * sub.ecount()
            dens = float(np.mean(ws)) if len(ws) > 0 else 0.0
            if dens >= MIN_DENSITY:
                modules.append(sub.vs["name"])
                if save_dir is not None:
                    sub.write_graphml(str(save_dir / f"module_{len(modules) - 1}_sz{len(comm)}_d{dens:.2f}.graphml"))
        return modules, len(part)


def protein_mapping() -> dict:
    def load():
        uni = pd.read_csv(UNIPROT_TSV, sep="\t")
        return {e: (a, g if isinstance(g, str) else None)
                for e, a, g in zip(uni["Entry Name"], uni["Entry"], uni["Gene Names (primary)"])}
    return cached("mapping", load)


def housekeeping_genes() -> set:
    return cached("hk", lambda: set(pd.read_csv(HK_CSV, sep=";")["Gene.name"].dropna()))


def analysed_network(gC):
    """Removes proteins without accession/gene name and housekeeping genes from the consensus network; the result is used for community detection."""
    mapping, hk = protein_mapping(), housekeeping_genes()
    gC.delete_vertices([v.index for v in gC.vs
                        if mapping.get(v["name"], (None, None))[1] is None or mapping[v["name"]][1] in hk])
    return gC


def annotated_modules(modules):
    """Maps accessions and gene names; keeps module and member order."""
    mapping = protein_mapping()
    return [[{"protein_entry": e, "accession": mapping[e][0], "gene": mapping[e][1]} for e in m] for m in modules]


def reference_modules(prefix: str):
    """Modules of this tissue pair (no files written), used to check the JSON submitted by the agent."""
    def compute():
        a, b = split_pair(prefix)
        gA = cached(("graph", a), lambda: load_graph(a))
        gB = cached(("graph", b), lambda: load_graph(b))
        modules, _ = leiden_modules(analysed_network(consensus_network(gA, gB)), None)
        return modules, annotated_modules(modules)
    return cached(("modules", prefix), compute)


def all_pairs():
    tissues = sorted(p.stem for p in CONFIG["graphs"].glob("*.pkl"))
    return [f"{a}_{b}" for a, b in itertools.combinations(tissues, 2)], tissues


def split_pair(prefix: str):
    _, tissues = all_pairs()
    for a, b in itertools.combinations(tissues, 2):
        if f"{a}_{b}" == prefix:
            return a, b
    raise ValueError(f"unknown tissue pair: {prefix}")


def pair_dir(prefix: str) -> Path:
    d = CONFIG["out"] / prefix
    d.mkdir(parents=True, exist_ok=True)
    return d


def record(prefix: str, **kw):
    with _records_lock:
        _records.setdefault(prefix, {"pair": prefix}).update(kw)


# ════════════════════════════════════════════════════════════════════
# Tools
# ════════════════════════════════════════════════════════════════════
@tool
def read_file(file_path: str) -> str:
    """
    Reads a text file inside the analysis output folder. Raises FileNotFoundError if the file does not exist.

    Args:
        file_path: Path relative to the analysis output folder, e.g. 'brain_colon.json'.

    Returns:
        str: The content of the file.
    """
    base = CONFIG["out"].resolve()
    path = (base / file_path).resolve()
    if base != path and base not in path.parents:
        raise ValueError("Only files inside the analysis output folder can be read.")
    if not path.exists():
        raise FileNotFoundError(f"{file_path} does not exist in the analysis output folder.")
    return path.read_text()


@tool
def build_consensus_network(tissue_a: str, tissue_b: str) -> Any:
    """
    Builds (and saves) the consensus network between two tissue co-abundance networks: nodes shared by both
    networks, edges present in both, edge weight = min(weight_A, weight_B), only edges with weight > 0 are kept.
    Proteins without a UniProt accession / gene name and housekeeping genes are removed from the network here,
    so the modules found later consist only of the proteins that are analysed.
    Tissue networks are already built; don't save networks yourself.

    Args:
        tissue_a: The tissue group A name.
        tissue_b: The tissue group B name.

    Returns:
        igraph.Graph: The consensus protein co-abundance network (vertex attribute 'name', edge attribute 'weight').
    """
    gA = cached(("graph", tissue_a), lambda: load_graph(tissue_a))
    gB = cached(("graph", tissue_b), lambda: load_graph(tissue_b))
    gC = analysed_network(consensus_network(gA, gB))
    prefix = f"{tissue_a}_{tissue_b}"
    with open(pair_dir(prefix) / f"consensus_{prefix}.pkl", "wb") as fh:
        pickle.dump(gC, fh, protocol=pickle.HIGHEST_PROTOCOL)
    record(prefix, tissue_a=tissue_a, tissue_b=tissue_b, consensus_nodes=gC.vcount(), consensus_edges=gC.ecount())
    return gC


@tool
def get_leiden_modules(tissues_prefix: str, gC: Any) -> list:
    """
    Gets conserved modules from a consensus network with the Leiden algorithm (modularity, resolution 1.0,
    seed 42); keeps communities with 5-50 members and mean edge weight >= 0.15, and saves each module as GraphML.

    Args:
        tissues_prefix: The tissue pair prefix, e.g. 'brain_colon'.
        gC: The consensus network returned by build_consensus_network().

    Returns:
        list: list of modules; each module is a list of protein entry names. Module i is saved as module_i_*.graphml.
    """
    d = pair_dir(tissues_prefix)
    for old in d.glob("module_*.graphml"):
        old.unlink()
    modules, n_comm = leiden_modules(gC, d)
    record(tissues_prefix, communities=n_comm, modules=len(modules),
           proteins_in_modules=sum(len(m) for m in modules))
    return modules


@tool
def protein_entry_to_accession_gene(entry_names: list) -> dict:
    """
    Gets UniProt accession numbers and gene names for UniProt entry names from the local UniProt table.

    Args:
        entry_names: UniProt entry names like 'DUS23_HUMAN'.

    Returns:
        dict: {entry: {"accession": str or None, "gene": str or None, "status": "OK" / "NO_ENTRY" / "NO_GENE"}}.
    """
    mapping = protein_mapping()
    out = {}
    for e in entry_names:
        acc, gene = mapping.get(e, (None, None))
        out[e] = {"accession": acc, "gene": gene,
                  "status": "NO_ENTRY" if acc is None else ("NO_GENE" if gene is None else "OK")}
    return out


@tool
def get_house_keeping_genes() -> list:
    """
    Retrieves the list of housekeeping gene names.

    Returns:
        list: housekeeping gene names.
    """
    return sorted(housekeeping_genes())


def module_problems(prefix: str, modules: Any) -> list:
    raw, ref = reference_modules(prefix)
    if len(raw) == 0:
        return ["This tissue pair has no conserved modules; no JSON file should be saved."]
    if not isinstance(modules, list):
        return ["The top level must be a JSON list of modules."]
    problems = []
    if len(modules) != len(ref):
        problems.append(f"Expected {len(ref)} modules (one per Leiden module, in the same order), got {len(modules)}.")
    for i, m in enumerate(modules[:len(ref)]):
        if not isinstance(m, list):
            problems.append(f"module {i} must be a list of protein objects.")
            continue
        if any(not isinstance(p, dict) or set(p) != {"protein_entry", "accession", "gene"}
               or not all(isinstance(v, str) for v in p.values()) for p in m):
            problems.append(f"module {i}: every item must be an object with exactly the string fields "
                            f"protein_entry, accession, gene.")
            continue
        got = {p["protein_entry"]: (p["accession"], p["gene"]) for p in m}
        want = {p["protein_entry"]: (p["accession"], p["gene"]) for p in ref[i]}
        missing, extra = sorted(set(want) - set(got)), sorted(set(got) - set(want))
        wrong = sorted(k for k in set(got) & set(want) if got[k] != want[k])
        if missing:
            problems.append(f"module {i}: missing proteins {missing[:10]}")
        if extra:
            problems.append(f"module {i}: proteins that are not in this module {extra[:10]}")
        if wrong:
            problems.append(f"module {i}: wrong accession/gene for {wrong[:10]}")
    return problems


@tool
def save_modules_json(tissues_prefix: str, modules: list) -> str:
    """
    Validates and saves the conserved modules of a tissue pair to {tissues_prefix}.json in the analysis folder.
    The JSON must follow the template exactly: a list of modules in Leiden module order (module i <-> module_i_*.graphml),
    each module a list of objects {"protein_entry": str, "accession": str, "gene": str} for every protein of the module.
    If validation fails, an error describing every problem is raised; fix the modules and call this tool again.

    Args:
        tissues_prefix: The tissue pair prefix, e.g. 'brain_colon'.
        modules: The list of modules following the template.

    Returns:
        str: the name of the saved file.
    """
    problems = module_problems(tissues_prefix, modules)
    if problems:
        raise ValueError("JSON validation failed:\n- " + "\n- ".join(problems))
    path = CONFIG["out"] / f"{tissues_prefix}.json"
    path.write_text(json.dumps(modules, indent=2))
    return path.name


@tool
def write_analysis_markdown(tissues_prefix: str, content: str) -> str:
    """
    Writes the markdown analysis report (methods and findings) of a tissue pair.

    Args:
        tissues_prefix: The tissue pair prefix, e.g. 'brain_colon'.
        content: Markdown content.

    Returns:
        str: the name of the saved file.
    """
    path = pair_dir(tissues_prefix) / f"analysis_{tissues_prefix}.md"
    path.write_text(content)
    return path.name


JSON_TEMPLATE = """
[
  [ {"protein_entry": "ACON_HUMAN", "accession": "Q99798", "gene": "ACO2"},
    {"protein_entry": "CD9_HUMAN",  "accession": "P21926", "gene": "CD9"} ],
  [ {"protein_entry": "...", "accession": "...", "gene": "..."} ]
]
"""

PROMPT = """
  Use as less steps as you can!!

  (0) Use read_file() to check if {prefix}.json exists, if exists, terminate all operations!!

  (1) Use build_consensus_network() to build a protein co-abundance consensus network between {tissues}.
  Networks are already saved, DON'T SAVE networks for latter use!!
  Nodes are proteins, edge weights are protein correlations.
  Proteins without accession/gene and housekeeping genes are already removed from this network,
  so every module found in it consists only of the proteins that are analysed.

  (2) Use get_leiden_modules() to get all conserved modules from the consensus network, param tissues_prefix should be {prefix}!!
  If there're no modules, don't create or save any json file!! And go directly to step (6)!!

  (3) For each module!!: protein_entry_to_accession_gene() will return a dictionary, use it to map the proteins of the
  module to their accession number and genes.
  You can check the housekeeping list with get_house_keeping_genes(); no module protein should be on it.

  (4) Group proteins by modules. Keep the module order returned by get_leiden_modules().

  (5) Save the modules with save_modules_json(), using exactly this JSON template (not just samples!):
  {template}
  If save_modules_json() raises a validation error, read the error, fix your modules and call it again!!

  (6) Put all your analysis including methods into markdown with write_analysis_markdown().

  Finally, call final_answer() with a short summary.
"""


# ════════════════════════════════════════════════════════════════════
# Run
# ════════════════════════════════════════════════════════════════════
def check_output(prefix: str) -> str | None:
    raw, _ = reference_modules(prefix)
    json_path = CONFIG["out"] / f"{prefix}.json"
    d = CONFIG["out"] / prefix
    if not (d / f"consensus_{prefix}.pkl").exists():
        return "the consensus network was not built and saved."
    n_graphml = len(list(d.glob("module_*.graphml")))
    if n_graphml != len(raw):
        return f"get_leiden_modules() was not run correctly ({n_graphml} GraphML files, expected {len(raw)})."
    if len(raw) == 0:
        return f"{prefix} has no modules, but a JSON file was saved." if json_path.exists() else None
    if not json_path.exists():
        return f"{prefix}.json was not saved."
    clusters = load_clusters(json_path)
    if sorted(clusters) != list(range(len(clusters))):
        return f"{prefix}.json must list the modules in Leiden module order (ids 0..n-1)."
    problems = module_problems(prefix, [clusters[k] for k in sorted(clusters)])
    return "; ".join(problems) if problems else None


def final_answer_check(prefix: str):
    def json_saved_before_final_answer(final_answer, memory, agent=None):
        problem = check_output(prefix)
        if problem:
            raise ValueError(f"Not finished yet: {problem}")
        return True
    return json_saved_before_final_answer


def clear_pair_outputs(prefix: str):
    (CONFIG["out"] / f"{prefix}.json").unlink(missing_ok=True)
    d = CONFIG["out"] / prefix
    if d.exists():
        for f in d.iterdir():
            f.unlink()
    with _records_lock:
        _records.pop(prefix, None)


def run_pair(prefix: str, model) -> dict:
    CONFIG["traces"].mkdir(parents=True, exist_ok=True)
    a, b = split_pair(prefix)
    t0, feedback, tokens_in, tokens_out = time.time(), "", 0, 0
    for attempt in range(1, MAX_ATTEMPTS + 1):
        clear_pair_outputs(prefix)
        agent = CodeAgent(tools=[read_file, build_consensus_network, get_leiden_modules, protein_entry_to_accession_gene,
                                 get_house_keeping_genes, save_modules_json, write_analysis_markdown],
                          model=model, max_steps=MAX_STEPS, planning_interval=PLANNING_INTERVAL,
                          additional_authorized_imports=AUTHORIZED_IMPORTS,
                          final_answer_checks=[final_answer_check(prefix)], verbosity_level=0)
        task = PROMPT_HEAD + PROMPT.format(prefix=prefix, tissues=(a, b), template=JSON_TEMPLATE)
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
        with open(CONFIG["traces"] / f"{prefix}_attempt{attempt}.json", "w") as fh:
            json.dump({"task": task, "error": error, "steps": agent.memory.get_full_steps()}, fh,
                      indent=1, default=str, ensure_ascii=False)
        problem = check_output(prefix) or (None if error is None else "the agent run did not complete successfully")
        if problem is None:
            return dict(name=prefix, attempts=attempt, passed=True, seconds=round(time.time() - t0),
                        input_tokens=tokens_in, output_tokens=tokens_out, note="")
        feedback = problem if error is None else f"{problem} ({error[:300]})"
    return dict(name=prefix, attempts=MAX_ATTEMPTS, passed=False, seconds=round(time.time() - t0),
                input_tokens=tokens_in, output_tokens=tokens_out, note=feedback[:500])


def summary_row(prefix: str) -> dict:
    rec = dict(_records.get(prefix, {"pair": prefix}))
    _, ref = reference_modules(prefix)
    rec.update(proteins_in_modules=sum(len(m) for m in ref),
               json_written=(CONFIG["out"] / f"{prefix}.json").exists())
    return rec


def update_csv(path: Path, rows: list, key: str):
    new = pd.DataFrame(rows)
    if path.exists():
        old = pd.read_csv(path)
        new = pd.concat([old[~old[key].isin(new[key])], new], ignore_index=True)
    new.to_csv(path, index=False)
    return new


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pairs", nargs="+", help="only run these tissue pairs, e.g. brain_colon (default: all)")
    ap.add_argument("--graphs", default=str(CONFIG["graphs"]), help="directory of the tissue networks")
    ap.add_argument("--out", default=str(CONFIG["out"]), help="output directory")
    ap.add_argument("--traces", default=str(CONFIG["traces"]), help="directory of the agent traces")
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()
    CONFIG.update(graphs=Path(args.graphs), out=Path(args.out), traces=Path(args.traces))
    CONFIG["out"].mkdir(parents=True, exist_ok=True)

    pairs = args.pairs or all_pairs()[0]
    summary_path = CONFIG["out"] / "summary.csv"
    if summary_path.exists():
        s = pd.read_csv(summary_path)
        done = {r.pair for r in s.itertuples()
                if r.modules == 0 or (CONFIG["out"] / f"{r.pair}.json").exists()}
        skipped = [p for p in pairs if p in done]
        pairs = [p for p in pairs if p not in done]
        if skipped:
            print(f"Skipping {len(skipped)} completed tissue pairs", flush=True)

    model = OpenAIServerModel(model_id=MODEL_ID, api_key=load_api_key(), temperature=TEMPERATURE)
    statuses, t0 = [], time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(run_pair, p, model): p for p in pairs}
        for i, fut in enumerate(as_completed(futures), 1):
            p = futures[fut]
            try:
                st = fut.result()
            except Exception:
                st = dict(name=p, attempts=0, passed=False, seconds=0, input_tokens=0, output_tokens=0,
                          note="".join(traceback.format_exception_only(*sys.exc_info()[:2]))[-500:])
            statuses.append(st)
            if st["passed"]:
                update_csv(summary_path, [summary_row(p)], "pair")
            rec = _records.get(p, {})
            print(f"[{i}/{len(pairs)}] {p:45s} passed={st['passed']} attempts={st['attempts']} "
                  f"modules={rec.get('modules', '-')} {st['seconds']}s "
                  f"tokens={st['input_tokens']}+{st['output_tokens']} {st['note'][:80]}", flush=True)

    if statuses:
        s = update_csv(CONFIG["traces"] / "status.csv", statuses, "name")
        print(f"\nPassed {int(s.passed.sum())}/{len(s)}, this run took {(time.time() - t0) / 60:.1f} min, "
              f"tokens {int(s.input_tokens.sum()):,} input + {int(s.output_tokens.sum()):,} output")


if __name__ == "__main__":
    main()
