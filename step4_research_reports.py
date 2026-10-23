#!/usr/bin/env python3
"""
Step 4: research reports for conserved modules (code aligns the evidence, an agent integrates and interprets it)

Division of work
  code   (1) queries MyGene.info (function), Open Targets (disease associations) and Europe PMC (paper counts) for
             all module genes and caches the results in knowledge/cache/gene_facts.json;
         (2) builds a fact sheet per module that aligns, gene by gene, network position, HPA, hu.MAP, STRING,
             enrichment terms and the three databases above; at module level it adds the GO/KEGG global BH results
             ([E*]), supplementary STRING enrichment ([S*]) and hu.MAP complexes ([C*]);
         (3) assembles the report from the agent's interpretation and the fact-sheet numbers, and checks it.
  agent  one fresh agent per module (smolagents CodeAgent or ToolCallingAgent) that sees only this module's fact sheet
         and can only search the web. It integrates the evidence: infers the function, considers cell composition or
         blood as alternative explanations, judges novelty, selects important genes and gives conclusions and a
         mechanistic hypothesis. It writes no numbers; it cites evidence as [E1]/[S1]/[C1] and by gene symbol, and all
         numbers are filled in by code from the fact sheet.

Checks: the answer is complete; important genes belong to the module; cited evidence tags exist; every number in the
interpretation appears in the fact sheet; no placeholders. On failure the problems are added to the task and a fresh
agent runs again, at most 3 times. Accepted sections are merged into report/{pair}.md.

Input    analysis/{pair}.json, analysis/{pair}/module_*.graphml
         knowledge/{pair}/bio_knowledge_{pair}.json, data/uniprot_human_reviewed.tsv
Output   report/{pair}.md
         knowledge/cache/gene_facts.json   gene-level database results (reusable)
         agent_traces/step4/               per module and attempt: task with fact sheet, agent output and trajectory; modules.csv
All directories are taken from the configuration file (see common.py).

Usage    python step4_research_reports.py --prefetch-only                    # only query and cache gene facts
         python step4_research_reports.py --model gpt-5.6-luna --max-modules 50
         python step4_research_reports.py --only bone_marrow_liver:0 brain_colon:3
"""
import argparse
import datetime
import glob
import json
import re
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import igraph as ig
import pandas as pd
import requests
from smolagents import CodeAgent, DuckDuckGoSearchTool, OpenAIServerModel, ToolCallingAgent

from common import PATHS, load_api_key, load_clusters

ANALYSIS = PATHS["analysis"]
KNOWLEDGE = PATHS["knowledge"]
GENE_FACTS = KNOWLEDGE / "cache" / "gene_facts.json"
UNIPROT = PATHS["data"] / "uniprot_human_reviewed.tsv"

MODEL_ID = "gpt-5.6-luna"
MAX_STEPS = 10
MAX_ATTEMPTS = 3                     # maximum runs per module
TOP_DISEASES = 5                     # diseases listed per gene
# List price per million tokens (input, output); only used to print a cost estimate
PRICES = {"gpt-4.1": (2.0, 8.0), "gpt-5.6-luna": (0.20, 1.20), "gpt-5.6-terra": (2.0, 12.0), "gpt-5.6-sol": (5.0, 30.0)}

PROMPT_HEAD = ("\nYou are a top rated biological researcher and you are doing research related to "
               "protein co-abundance network in multiple human tissue groups.\n")

CONFIG = {"report": PATHS["report"], "traces": PATHS["traces"] / "step4"}
OPENTARGETS_URL = "https://api.platform.opentargets.org/api/v4/graphql"
OPENTARGETS_QUERY = """
query diseaseAssoc($ensemblId: String!, $size: Int!) {
  target(ensemblId: $ensemblId) {
    approvedSymbol
    associatedDiseases(page: { index: 0, size: $size }) {
      count
      rows { disease { id name } score }
    }
  }
}
"""


def http(method, url, retries=5, **kw):
    """HTTP request that retries on timeouts, 429 and 5xx responses."""
    for attempt in range(1, retries + 1):
        try:
            r = requests.request(method, url, timeout=60, **kw)
            if r.status_code == 429 or r.status_code >= 500:
                raise requests.HTTPError(f"HTTP {r.status_code}")
            r.raise_for_status()
            return r
        except requests.RequestException:
            if attempt == retries:
                raise
            time.sleep(3 * attempt)


# ════════════════════════════════════════════════════════════════════
# Gene-level database queries (done by code, cached)
# ════════════════════════════════════════════════════════════════════
def mygene(gene):
    r = http("GET", "https://mygene.info/v3/query",
             params={"q": f"symbol:{gene}", "species": "human", "fields": "symbol,name,summary,go,ensembl.gene", "size": 1})
    hits = r.json().get("hits", [])
    if not hits:
        raise ValueError(f"No MyGene.info record for gene {gene}.")
    hit = hits[0]
    bp = hit.get("go", {}).get("BP", [])
    bp = bp if isinstance(bp, list) else [bp]
    terms = list(dict.fromkeys(t.get("term") for t in bp if isinstance(t, dict) and t.get("term")))
    ens = hit.get("ensembl") or []
    ensembl_ids = [e.get("gene") for e in (ens if isinstance(ens, list) else [ens]) if isinstance(e, dict) and e.get("gene")]
    return {"symbol": hit.get("symbol"), "name": hit.get("name"), "summary": hit.get("summary"),
            "biological_process_terms": terms[:20]}, ensembl_ids


def europepmc(gene):
    r = http("GET", "https://www.ebi.ac.uk/europepmc/webservices/rest/search",
             params={"query": f"{gene} AND gene", "format": "json", "pageSize": 1})
    return int(r.json().get("hitCount", 0))


def opentargets(ensembl_id, topn=10):
    r = http("POST", OPENTARGETS_URL, json={"query": OPENTARGETS_QUERY,
                                            "variables": {"ensemblId": ensembl_id, "size": int(topn)}})
    data = r.json()
    if data.get("errors"):
        raise RuntimeError(json.dumps(data["errors"])[:300])
    target = data["data"]["target"]
    if target is None:
        raise RuntimeError(f"No Open Targets target for {ensembl_id}")
    return [{"name": row["disease"]["name"], "score": float(row["score"])} for row in target["associatedDiseases"]["rows"]][:topn]


def query_gene(gene):
    out = {"fetched_at": datetime.date.today().isoformat(), "errors": {}}
    ensembl_ids = []
    try:
        out["mygene"], ensembl_ids = mygene(gene)
    except Exception as e:
        out["errors"]["mygene"] = f"{type(e).__name__}: {e}"[:200]
    try:
        out["europepmc_papers"] = europepmc(gene)
    except Exception as e:
        out["errors"]["europepmc"] = f"{type(e).__name__}: {e}"[:200]
    errs = []
    for ensembl_id in sorted(ensembl_ids):        # try each Ensembl id (e.g. alternate haplotypes)
        try:
            out["opentargets"] = opentargets(ensembl_id, 10)
            break
        except Exception as e:
            errs.append(f"{type(e).__name__}: {e}"[:120])
    if "opentargets" not in out:
        out["errors"]["opentargets"] = ("; ".join(errs) or "no Ensembl gene id from MyGene.info")[:300]
    return gene, out


_facts: dict = {}
_facts_lock = threading.Lock()


def gene_facts():
    with _facts_lock:
        if not _facts and GENE_FACTS.exists():
            _facts.update(json.loads(GENE_FACTS.read_text()))
    return _facts


def prefetch_gene_facts(genes, workers=8):
    facts = gene_facts()
    todo = sorted(set(genes) - set(facts))
    if not todo:
        return
    print(f"Querying MyGene.info / Open Targets / Europe PMC for {len(todo)} genes …", flush=True)
    GENE_FACTS.parent.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for k, (g, out) in enumerate(pool.map(query_gene, todo), 1):
            with _facts_lock:
                facts[g] = out
            if k % 200 == 0 or k == len(todo):
                with _facts_lock:
                    tmp = GENE_FACTS.with_suffix(".tmp")
                    tmp.write_text(json.dumps(facts, ensure_ascii=False))
                    tmp.replace(GENE_FACTS)
                print(f"  {k}/{len(todo)}", flush=True)


# ════════════════════════════════════════════════════════════════════
# Module fact sheet (done by code)
# ════════════════════════════════════════════════════════════════════
_uniprot_cache = {}
_uniprot_lock = threading.Lock()


def _uniprot():
    with _uniprot_lock:
        if not _uniprot_cache:
            d = pd.read_csv(UNIPROT, sep="\t")
            _uniprot_cache.update({e: (a, g if isinstance(g, str) else None)
                                   for e, a, g in zip(d["Entry Name"], d["Entry"], d["Gene Names (primary)"])})
    return _uniprot_cache


def module_graph(prefix, i):
    path = sorted(glob.glob(str(ANALYSIS / prefix / f"module_{i}_*.graphml")))[0]
    g = ig.Graph.Read_GraphML(path)
    u = _uniprot()
    gene = {v.index: (u.get(v["name"], (None, None))[1] or v["name"]) for v in g.vs}
    w = g.es["weight"] if "weight" in g.es.attributes() else [1.0] * g.ecount()
    nodes = {}
    for v in g.vs:
        inc = g.incident(v.index)
        nbr = sorted(((gene[g.es[e].target if g.es[e].source == v.index else g.es[e].source], w[e]) for e in inc),
                     key=lambda x: -x[1])
        nodes[gene[v.index]] = {"degree": len(inc), "strength": sum(x[1] for x in nbr), "neighbors": nbr}
    return {"n_nodes": g.vcount(), "n_edges": g.ecount(), "nodes": nodes}


def fmt(x, digits=3):
    return f"{x:.{digits}g}" if isinstance(x, float) else str(x)


def build_facts(prefix, i):
    """Return (fact sheet text, context). The context is used to render and check the report."""
    kb = json.loads((KNOWLEDGE / prefix / f"bio_knowledge_{prefix}.json").read_text())
    mod = next(m for m in kb["modules"] if m["module"] == i)
    members = load_clusters(ANALYSIS / f"{prefix}.json")[i]
    entry = {m["gene"]: m["protein_entry"] for m in members}
    genes = mod["genes"]
    graph = module_graph(prefix, i)
    facts = gene_facts()
    a, b = kb["tissue_a"], kb["tissue_b"]
    ets = mod.get("enrichment_test_summary") or {}
    E = {f"E{k}": t for k, t in enumerate(sorted(mod.get("go_kegg_enrichment") or [], key=lambda t: t["q_global"]), 1)}
    S = {f"S{k}": t for k, t in enumerate(sorted(mod.get("string_enrichment") or [], key=lambda t: t["fdr"])[:15], 1)}
    C = {f"C{k}": c for k, c in enumerate(mod.get("humap_complexes") or [], 1)}
    string = mod.get("string_interactions") or []
    ihc = mod.get("hpa_ihc_detection") or {}
    hpa = mod.get("hpa_gene_annotation") or {}
    hsum = mod.get("hpa_gene_annotation_summary") or {}

    L = [f"MODULE module_{i} of tissue pair {prefix} ({a} and {b}): {len(genes)} genes; "
         f"co-abundance subgraph with {graph['n_nodes']} nodes and {graph['n_edges']} edges.",
         "", "== GO/KEGG enrichment (one-sided hypergeometric; BH within module and across ALL module-term tests) =="]
    if ets:
        L.append(f"tests in this module: {ets.get('n_tests')}; background genes: {ets.get('n_background_mapped')}; "
                 f"terms with q_global < 0.05: {ets.get('n_global_bh_005')}; terms with q_within_module < 0.05: {ets.get('n_within_bh_005')}; "
                 f"minimum p_raw {fmt(ets.get('min_p_raw'))}, minimum q_within_module {fmt(ets.get('min_q_within'))}, "
                 f"minimum q_global {fmt(ets.get('min_q_global'))}.")
    if E:
        L.append("Terms passing global BH (primary evidence):")
        for k, t in E.items():
            L.append(f"[{k}] {t['source']} {t['term_id']} {t['name']}: p_raw {fmt(t['p_raw'])}, q_within_module {fmt(t['q_within_module'])}, "
                     f"q_global {fmt(t['q_global'])}, overlap {t['intersection_size']}/{t['query_size']}, "
                     f"background {t['term_size']}/{t['effective_domain_size']}, fold {fmt(t['fold_enrichment'])}; genes {', '.join(t['genes'])}")
    else:
        L.append("No GO/KEGG term passes global BH. Do not describe any GO/KEGG term as significantly enriched.")
    L += ["", "== STRING functional enrichment (supplementary; original within-query FDR, NOT corrected across modules) =="]
    L += [f"[{k}] {t['category']} {t['description']}: FDR {fmt(t['fdr'])}, {t['number_of_genes']}/{t['number_of_genes_in_background']}; "
          f"genes {', '.join(t['genes'])}" for k, t in S.items()] or ["none"]
    sp = mod.get("string_interaction_pairs") or {}
    L += ["", f"== STRING interactions (score >= 0.7): {len(string)} of {sp.get('possible', '?')} possible gene pairs =="]
    L += [f"{x['gene_a']} - {x['gene_b']} ({x['score']})" for x in string] or ["none"]
    L += ["", "== hu.MAP 3.0 complexes with >= 2 module members =="]
    L += [f"[{k}] {c['complex_id']} (confidence {c['confidence']}; {len(c['members_in_module'])} of {c['complex_size']} complex members in module): "
          f"members in module {', '.join(c['members_in_module'])}; other complex members {', '.join(x for x in c['complex_genes'] if x not in c['members_in_module'])}"
          for k, c in C.items()] or ["none"]
    L += ["", "== HPA summary of the module ==", json.dumps(hsum, ensure_ascii=False)]
    for t, d in ihc.items():
        L.append(f"HPA protein detection in {t} ({', '.join(d.get('hpa_tissues') or []) or 'no matching HPA tissue'}): "
                 f"detected {len(d.get('detected', []))}, not detected {len(d.get('not_detected', []))}, no data {len(d.get('no_data', []))}")
    L += ["", "== Genes (sorted by weighted degree in the module subgraph) =="]
    order = sorted(genes, key=lambda g: -graph["nodes"].get(g, {"strength": 0})["strength"])
    for g in order:
        n = graph["nodes"].get(g, {"degree": 0, "strength": 0.0, "neighbors": []})
        f = facts.get(g, {})
        h = hpa.get(g) or {}
        det = [t for t, d in ihc.items() if g in d.get("detected", [])]
        nod = [t for t, d in ihc.items() if g in d.get("not_detected", [])]
        my = f.get("mygene") or {}
        ot = f.get("opentargets")
        L.append(f"--- {g} ({entry.get(g, '?')})")
        L.append(f"  network: degree {n['degree']}, weighted strength {n['strength']:.2f}; neighbors "
                 + (", ".join(f"{x} ({wt:.2f})" for x, wt in n["neighbors"][:8]) or "none"))
        if h:
            L.append(f"  HPA: tissue {h.get('tissue_specificity')} {h.get('enriched_tissues') or ''}; single cell "
                     f"{h.get('single_cell_type_specificity')} {(h.get('enriched_single_cell_types') or [])[:5]}; blood "
                     f"{h.get('blood_cell_specificity')} {h.get('enriched_blood_cells') or ''}; secretome {h.get('secretome_location')}; "
                     f"location {h.get('subcellular_main_location')}; IHC detected in {det or 'none'}, not detected in {nod or 'none'}")
        else:
            L.append("  HPA: no annotation")
        L.append(f"  hu.MAP: {', '.join(k for k, c in C.items() if g in c['members_in_module']) or 'none'}; STRING partners: "
                 + (", ".join(f"{x['gene_b'] if x['gene_a'] == g else x['gene_a']} ({x['score']})" for x in string if g in (x['gene_a'], x['gene_b'])) or "none"))
        L.append(f"  in GO/KEGG [E] terms: {', '.join(k for k, t in E.items() if g in t['genes']) or 'none'}; "
                 f"in STRING [S] terms: {', '.join(k for k, t in S.items() if g in t['genes']) or 'none'}")
        L.append(f"  MyGene.info: {my.get('name') or 'not available'}. {(my.get('summary') or '')[:500]}"
                 + (f" GO BP: {'; '.join(my.get('biological_process_terms', [])[:6])}" if my.get("biological_process_terms") else ""))
        L.append("  Open Targets: " + ("; ".join(f"{d['name']} ({d['score']:.2f})" for d in ot[:TOP_DISEASES]) if ot else "not available"))
        L.append(f"  Europe PMC papers: {f.get('europepmc_papers', 'not available')}")
    ctx = dict(prefix=prefix, module=i, kb=kb, mod=mod, genes=genes, entry=entry, graph=graph, E=E, S=S, C=C,
               string=string, ihc=ihc, hpa=hpa, ets=ets, a=a, b=b)
    return "\n".join(L), ctx


# ════════════════════════════════════════════════════════════════════
# Agent task, checks and report rendering
# ════════════════════════════════════════════════════════════════════
PROMPT = """
  You interpret ONE conserved co-abundance module shared by {a} and {b}. Each module is interpreted by a separate,
  independent researcher. All data about this module, already retrieved from the databases and aligned by gene,
  are in the FACT SHEET below. You may additionally search online with web_search (for example to assess novelty).

  Integrate the evidence like a careful scientist:
  (1) Infer the module function from the genes, network structure, GO/KEGG and STRING evidence.
      GO/KEGG primary evidence is ONLY the [E] terms (q_global < 0.05 across all module-term tests).
      If there are no [E] terms, say that no GO/KEGG term passed global correction; never present a nominal p value,
      a within-module q value or a STRING FDR as global significance. [S] terms are supplementary only.
      No enriched term does not mean a module is false.
  (2) Composition: if most genes are plasma / secreted proteins, blood-cell enriched, or broadly expressed
      housekeeping-type genes, point this out, because the shared module may then reflect blood in the samples or
      shared cell types. Use the HPA evidence.
  (3) STRING and hu.MAP: which relationships are already known, and what this means for the module.
  (4) Novelty: is this module a new finding? Give reasons. Absence from STRING or hu.MAP alone does not prove novelty.
  (5) Choose the IMPORTANT genes of this module (3 to 6 genes, all from this module) and explain why each matters,
      using its network position, annotations, function, disease associations and literature volume.
  (6) For each important gene give your own conclusion. Separate established evidence from hypotheses.
  (7) Propose a mechanistic hypothesis for the module, clearly labelled as a hypothesis.

  STRICT RULES
  - Do NOT write any numbers yourself (no p, q, scores, counts, degrees). The numbers are inserted by code.
    Refer to evidence by tags like [E1], [S2], [C1] and by gene symbols; describe amounts in words if needed.
  - Use only facts from the FACT SHEET or from your web searches; do not invent annotations.
  - Return the result with final_answer() as ONE dictionary with exactly these keys (all values are strings except
    important_genes and web_sources):
      "function", "composition", "string_and_complexes", "novelty", "hypothesis",
      "important_genes": a list of {{"gene": "<symbol>", "why_important": "...", "conclusion": "..."}},
      "web_sources": a list of URLs you actually used (may be empty)

=========================== FACT SHEET ===========================
{facts}
==================================================================
"""

PLACEHOLDERS = re.compile(r"to be (filled|added|completed)|see above|see main text|would go here|\bTODO\b|\[placeholder|"
                          r"can be performed as needed", re.I)
REQUIRED_HEADINGS = {"Function": r"function", "STRING": r"string", "Novelty": r"novel", "Important genes": r"important gene"}
TAG_GROUP = re.compile(r"\[([ESC]\d+(?:\s*(?:,\s*and|,\s*or|[,;]|[-–—]|to|through|and|or)\s*[ESC]?\d+)*)\]")   # [E1] [E1, E3] [E1–E4]


def tag_ids(group):
    """Expand a group of evidence tags: 'E1, E3' -> [E1, E3]; 'E1–E4' -> [E1, E2, E3, E4]."""
    out, prev = [], None
    for m in re.finditer(r"([ESC]?)(\d+)|([-–—]|\bto\b|\bthrough\b)", group):
        if m.group(3):
            prev = ("range", prev)
            continue
        kind = m.group(1) or (prev[1][0] if isinstance(prev, tuple) and prev[1] else (out[-1][0] if out else "E"))
        n = int(m.group(2))
        if isinstance(prev, tuple) and prev[0] == "range" and prev[1] and prev[1][0] == kind:
            out += [f"{kind}{k}" for k in range(int(prev[1][1:]) + 1, n + 1)]
        else:
            out.append(f"{kind}{n}")
        prev = out[-1]
    return out
TEXT_KEYS = ("function", "composition", "string_and_complexes", "novelty", "hypothesis")


def parse_answer(out):
    if isinstance(out, str):
        s = out.strip()
        s = re.sub(r"^```(?:json)?|```$", "", s, flags=re.M).strip()
        out = json.loads(s)
    if not isinstance(out, dict):
        raise ValueError("final answer is not a dictionary")
    return out


def answer_problems(ans, ctx, facts_text):
    problems = []
    for k in TEXT_KEYS:
        if not isinstance(ans.get(k), str) or len(ans[k].strip()) < 40:
            problems.append(f"'{k}' is missing or too short")
    genes = ans.get("important_genes")
    if not isinstance(genes, list) or not genes:
        problems.append("'important_genes' is missing")
        genes = []
    for g in genes:
        if not isinstance(g, dict) or g.get("gene") not in ctx["genes"]:
            problems.append(f"important gene {g.get('gene') if isinstance(g, dict) else g!r} is not a gene of this module")
        elif not all(isinstance(g.get(k), str) and len(g[k].strip()) > 20 for k in ("why_important", "conclusion")):
            problems.append(f"important gene {g['gene']} lacks why_important / conclusion")
    texts = [ans.get(k) or "" for k in TEXT_KEYS] + [x for g in genes if isinstance(g, dict) for x in (g.get("why_important") or "", g.get("conclusion") or "")]
    text = "\n".join(t for t in texts if isinstance(t, str))
    text = join_ranges(text)
    known = set(ctx["E"]) | set(ctx["S"]) | set(ctx["C"])
    used = {t for grp in TAG_GROUP.findall(text) for t in tag_ids(grp)}
    bad_tags = sorted(used - known) + sorted(set(re.findall(r"\[[ESC](?![\d\s,;–-]*[\d\]])[^\]]*\]", text)))
    if bad_tags:
        problems.append("these evidence tags do not exist: " + ", ".join(bad_tags))
    if not ctx["E"]:
        negation = re.compile(r"\b(no|not|lack|lacks|lacking|absence|absent|without|none|neither|nor|fail|fails|failed|cannot|rather than|instead of|beyond|unsupported)\b", re.I)
        for m in re.finditer(r"significantly enriched|globally significant", text, re.I):
            before = re.split(r"[.;:!?]\s", text[max(0, m.start() - 400):m.start()])[-1]   # same sentence, before the phrase
            if not negation.search(before):
                problems.append("it describes GO/KEGG enrichment as significant although no term passed global BH")
                break
    stripped = TAG_GROUP.sub(" ", text)
    stripped = re.sub(r"https?://\S+|\b(?:GO|KEGG|hsa|HSA|R-HSA|KW|BTO|WP|huMAP3)[:_-]?\w*[\d.]*", " ", stripped)
    values = set(re.findall(r"(?<![\w.])\d+(?:[.,]\d+)*(?:e-?\d+)?%?(?![\w])", stripped))       # standalone numbers, not names such as eIF5A
    unknown = sorted(v for v in values if v.rstrip("%") not in facts_text)
    if unknown:
        problems.append("it writes numbers that are not in the fact sheet (write no numbers yourself): " + ", ".join(unknown[:10]))
    if PLACEHOLDERS.search(text):
        problems.append("it contains placeholders instead of analysis")
    return problems


def join_ranges(text):
    """Merge '[E1]–[E12]' into '[E1–E12]'."""
    return re.sub(r"\[([ESC])(\d+)\]\s*(?:[-–—]|to)\s*\[\1?(\d+)\]", r"[\1\2–\1\3]", text)


def cite(text, ctx):
    text = join_ranges(text)

    def group(ids):
        if len(ids) > 3 and all(k in ctx["E"] for k in ids):
            q = [ctx["E"][k]["q_global"] for k in ids]
            return f"({len(ids)} globally significant GO/KEGG terms, q_global {fmt(min(q))}–{fmt(max(q))}; see the table)"
        if len(ids) > 3 and all(k in ctx["S"] for k in ids):
            return f"({len(ids)} supplementary STRING terms; within-query FDR {fmt(min(ctx['S'][k]['fdr'] for k in ids))}–{fmt(max(ctx['S'][k]['fdr'] for k in ids))})"
        return " ".join(one(k) for k in ids)

    def one(k):
        if k in ctx["E"]:
            t = ctx["E"][k]
            return f"({t['source']} {t['name']}; q_global = {fmt(t['q_global'])})"
        if k in ctx["S"]:
            t = ctx["S"][k]
            return f"(STRING {t['category']} {t['description']}; within-query FDR = {fmt(t['fdr'])})"
        c = ctx["C"][k]
        return f"(hu.MAP {c['complex_id']})"
    text = TAG_GROUP.sub(lambda m: group(tag_ids(m.group(1))), text)

    def loose(m):                       # '[E1–E71 where annotated]', '[S1–S10 except S9]'
        body = m.group(1)
        keep, _, drop = body.partition(" except ")
        span = re.match(r"[ESC]\d+(?:\s*(?:[-–—]|to|through)\s*[ESC]?\d+)?", keep).group(0)
        ids = [k for k in tag_ids(span) if k not in set(tag_ids(drop))] if drop else tag_ids(span)
        ids = [k for k in ids if k in ctx["E"] or k in ctx["S"] or k in ctx["C"]]
        return group(ids) if ids else ""
    text = re.sub(r"\[([ESC]\d+[^\]]{0,60})\]", loose, text)
    return clean_tags(text)


BARE_TAGS = {"E": "globally significant GO/KEGG", "S": "supplementary STRING", "C": "hu.MAP"}


def clean_tags(text):
    """The agent sometimes writes only the category ('no [E] terms') or invents tags ('[C-HPA]', '[STRING]'):
    the former is replaced by words, the latter removed."""
    # removed when used as a tag (sentence start, or followed by a capitalised word / another tag / punctuation);
    # replaced by words when used as a noun inside a sentence
    text = re.sub(r"(^|(?<=[.!?:;]\s)|(?<=[.!?:;]))\s*\[[ESC]\](?=\s*(?:\[|[A-Z(]|$))\s*", r"\1", text, flags=re.M)
    text = re.sub(r"\s*\[[ESC]\](?=\s*(?:\[[ESC]\]|[.,;:)]|\s+[A-Z][a-z]))", "", text)
    text = re.sub(r"\[([ESC])\]", lambda m: BARE_TAGS[m.group(1)], text)
    text = re.sub(r"\s*\[(?:[ESC](?:[-\s:][^\]\d]*)?|ST|STR|STRING|HPA|huMAP|hu\.MAP)\]", "", text)
    text = re.sub(r"\s*\[(?![ESC]\d)[A-Z][^\]\d]{0,40}\](?!\()", "", text)
    text = re.sub(r"\s*\[[ESC]-[A-Za-z0-9-]+\]", "", text)                           # e.g. '[C-SEC23A]'
        # other invented tags such as '[CMP]', '[STRING interactions]'; markdown links are left alone
    return text


def render(ans, ctx):
    i, E, S, C, ets = ctx["module"], ctx["E"], ctx["S"], ctx["C"], ctx["ets"]
    facts = gene_facts()
    R = [f"## Module {i}", "",
         f"**Tissue pair**: {ctx['a']} and {ctx['b']}  ", f"**Genes ({len(ctx['genes'])})**: {', '.join(ctx['genes'])}", "",
         "### Function", "", cite(ans["function"], ctx), "",
         f"**Cell composition.** {cite(ans['composition'], ctx)}", ""]
    if ets:
        R.append(f"**GO/KEGG enrichment**: {ets.get('n_global_bh_005')} terms pass global BH (q_global < 0.05).")
    if E:
        R += ["", "| Term | q_global | genes |", "|---|---|---|"]
        R += [f"| {t['source']} {t['name']} | {fmt(t['q_global'])} | {', '.join(t['genes'])} |"
              for t in list(E.values())[:15]]
    R += ["", "### STRING and hu.MAP", "", cite(ans["string_and_complexes"], ctx), ""]
    sp = ctx["mod"].get("string_interaction_pairs") or {}
    R.append(f"**STRING interactions (score >= 0.7)**: {len(ctx['string'])} of {sp.get('possible', '?')} gene pairs"
             + (": " + "; ".join(f"{x['gene_a']}–{x['gene_b']} ({x['score']})" for x in ctx["string"]) if ctx["string"] else "."))
    if S:
        R.append("**STRING functional enrichment (supplementary, within-query FDR)**: "
                 + "; ".join(f"{t['category']} {t['description']} (FDR = {fmt(t['fdr'])}, {t['number_of_genes']} genes)" for t in S.values()))
    R.append("**hu.MAP 3.0 complexes with >= 2 module members**: "
             + ("; ".join(f"{c['complex_id']} ({', '.join(c['members_in_module'])}; {len(c['members_in_module'])}/{c['complex_size']})" for c in C.values()) or "none"))
    R += ["", "### Novelty", "", cite(ans["novelty"], ctx), "", f"**Hypothesis.** {cite(ans['hypothesis'], ctx)}"]
    if ans.get("web_sources"):
        R += ["", "Web sources: " + "; ".join(str(u) for u in ans["web_sources"])]
    R += ["", "### Important genes"]
    for g in ans["important_genes"]:
        s = g["gene"]
        n = ctx["graph"]["nodes"].get(s, {"degree": 0, "neighbors": []})
        h = ctx["hpa"].get(s) or {}
        f = facts.get(s, {})
        my = f.get("mygene") or {}
        ot = f.get("opentargets")
        det = [t for t, d in ctx["ihc"].items() if s in d.get("detected", [])]
        R += ["", f"#### {s}", "",
              f"- **Related proteins** (co-abundance neighbors): " + (", ".join(f"{x} ({wt:.2f})" for x, wt in n["neighbors"]) or "none")
              + "; STRING partners: " + (", ".join(f"{x['gene_b'] if x['gene_a'] == s else x['gene_a']} ({x['score']})" for x in ctx["string"] if s in (x["gene_a"], x["gene_b"])) or "none"),
              f"- **HPA**: " + (f"{h.get('tissue_specificity')}; {h.get('single_cell_type_specificity')}; blood {h.get('blood_cell_specificity')}; "
                                f"location {h.get('subcellular_main_location')}; IHC detected in {', '.join(det) or 'none'}" if h else "no annotation"),
              f"- **hu.MAP 3.0**: " + (", ".join(c["complex_id"] for c in C.values() if s in c["members_in_module"]) or "no complex with >= 2 module members"),
              f"- **Function (MyGene.info)**: {my.get('name') or 'not available'}" + (f". {my['summary'][:400]}{'…' if len(my['summary']) > 400 else ''}" if my.get("summary") else ""),
              f"- **Diseases (Open Targets)**: " + ("; ".join(f"{d['name']} ({d['score']:.3f})" for d in ot[:TOP_DISEASES]) if ot else "not available"),
              f"- **Europe PMC papers**: {f.get('europepmc_papers', 'not available')}",
              f"- **Why important**: {cite(g['why_important'], ctx)}",
              f"- **Conclusion**: {cite(g['conclusion'], ctx)}"]
    return "\n".join(R)


def split_pair(prefix):
    kb = json.loads((KNOWLEDGE / prefix / f"bio_knowledge_{prefix}.json").read_text())
    return kb["tissue_a"], kb["tissue_b"]


def module_sections(text):
    """{module id: its section in the report}; if a module appears more than once, the last section is used."""
    lines = text.splitlines(keepends=True)
    heads = []
    for k, line in enumerate(lines):
        h = re.match(r"^(#{1,6})\s+(.*)", line)
        if h:
            num = re.search(r"\bmodule[ _]?(\d+)\b", h.group(2), flags=re.I)
            heads.append((k, len(h.group(1)), int(num.group(1)) if num else None))
    out = {}
    for i in {m for _, _, m in heads if m is not None}:
        level = min(l for _, l, m in heads if m == i)
        start = [k for k, l, m in heads if m == i and l == level][-1]
        stop = next((k for k, l, m in heads if k > start and l <= level and m != i), len(lines))
        out[i] = "".join(lines[start:stop]).strip()
    return out


def section_problems(section, genes):
    problems = []
    if PLACEHOLDERS.search(section):
        problems.append("it contains placeholders instead of analysis")
    named = [g for g in set(genes) if re.search(rf"(?<![\w-]){re.escape(g)}(?![\w-])", section)]
    if len(named) < min(2, len(genes)):
        problems.append("it does not analyse the genes of this module")
    return problems


def module_genes(prefix):
    kb = json.loads((KNOWLEDGE / prefix / f"bio_knowledge_{prefix}.json").read_text())
    return {m["module"]: m["genes"] for m in kb["modules"] if m["genes"]}


def accepted_sections(prefix):
    report = CONFIG["report"] / f"{prefix}.md"
    secs = module_sections(report.read_text()) if report.exists() else {}
    genes = module_genes(prefix)
    return {i: sec for i, sec in secs.items() if i in genes and not section_problems(sec, genes[i])}


def write_report(prefix, sections):
    a, b = split_pair(prefix)
    body = "\n\n".join(sections[i] for i in sorted(sections))
    (CONFIG["report"] / f"{prefix}.md").write_text(f"# Conserved co-abundance modules: {a} and {b}\n\n{body}\n")


def pending_modules(prefix):
    done = accepted_sections(prefix)
    return [i for i in module_genes(prefix) if i not in done]


# ════════════════════════════════════════════════════════════════════
# Run
# ════════════════════════════════════════════════════════════════════
_pair_locks: dict = {}
_pair_locks_lock = threading.Lock()


def pair_lock(prefix):
    with _pair_locks_lock:
        return _pair_locks.setdefault(prefix, threading.Lock())


def run_module(prefix, i, model, agent_type):
    CONFIG["traces"].mkdir(parents=True, exist_ok=True)
    facts_text, ctx = build_facts(prefix, i)
    t0, tokens_in, tokens_out, feedback, problems = time.time(), 0, 0, "", []
    for attempt in range(1, MAX_ATTEMPTS + 1):
        common = dict(tools=[DuckDuckGoSearchTool()], model=model, max_steps=MAX_STEPS, verbosity_level=0)
        agent = CodeAgent(additional_authorized_imports=["json"], **common) if agent_type == "code" else ToolCallingAgent(**common)
        task = PROMPT_HEAD + PROMPT.format(a=ctx["a"], b=ctx["b"], facts=facts_text)
        if feedback:
            task += f"\n{feedback}\n"
        error, ans = None, None
        try:
            result = agent.run(task, return_full_result=True)
            usage = getattr(result, "token_usage", None)
            if usage is not None:
                tokens_in += usage.input_tokens or 0
                tokens_out += usage.output_tokens or 0
            ans = parse_answer(result.output)
            problems = answer_problems(ans, ctx, facts_text)
        except Exception as e:
            error = f"{type(e).__name__}: {e}"
            problems = [f"no valid final answer ({error[:200]})"]
        section = None
        if not problems:
            section = render(ans, ctx)
            problems = section_problems(section, ctx["genes"])
        with open(CONFIG["traces"] / f"{prefix}_module{i}_attempt{attempt}.json", "w") as fh:
            json.dump({"task": task, "agent": agent_type, "error": error, "answer": ans, "problems": problems,
                       "steps": agent.memory.get_full_steps()}, fh, indent=1, default=str, ensure_ascii=False)
        if not problems:
            with pair_lock(prefix):
                sections = accepted_sections(prefix)
                sections[i] = section
                write_report(prefix, sections)
            break
        valid = ", ".join(list(ctx["E"]) + list(ctx["S"]) + list(ctx["C"])) or "none (do not use any evidence tags)"
        feedback = ("A previous answer was rejected: " + "; ".join(problems) + ". Answer again following the STRICT RULES. "
                    f"The ONLY valid evidence tags for this module are: {valid}.")
    return dict(pair=prefix, module=i, agent=agent_type, attempts=attempt, passed=not problems,
                seconds=round(time.time() - t0), input_tokens=tokens_in, output_tokens=tokens_out,
                note="; ".join(problems)[:300])


def update_csv(path, rows, keys):
    new = pd.DataFrame(rows)
    if path.exists():
        old = pd.read_csv(path)
        key = lambda d: d[keys].astype(str).agg("|".join, axis=1)
        new = pd.concat([old[~key(old).isin(key(new))], new], ignore_index=True)
    new.to_csv(path, index=False)
    return new


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pairs", nargs="+", help="only run these tissue pairs (default: all pairs that finished Step 3)")
    ap.add_argument("--only", nargs="+", help="only run these modules, written as pair:module_id, e.g. bone_marrow_liver:0")
    ap.add_argument("--report", default=str(CONFIG["report"]), help="report output directory")
    ap.add_argument("--traces", default=str(CONFIG["traces"]), help="agent trace directory")
    ap.add_argument("--workers", type=int, default=8, help="number of modules run in parallel")
    ap.add_argument("--model", default=MODEL_ID)
    ap.add_argument("--agent", choices=["code", "tool"], default="code", help="code = CodeAgent, tool = ToolCallingAgent")
    ap.add_argument("--reasoning-effort", help="e.g. none / low / medium; must be none for gpt-5.x with --agent tool")
    ap.add_argument("--max-modules", type=int, help="maximum number of modules to process in this run (pending modules taken in pair-name order)")
    ap.add_argument("--prefetch-only", action="store_true", help="only query and cache database facts for all module genes")
    args = ap.parse_args()
    CONFIG.update(report=Path(args.report).resolve(), traces=Path(args.traces))
    CONFIG["report"].mkdir(parents=True, exist_ok=True)

    ready = sorted(p.name for p in KNOWLEDGE.iterdir() if (p / f"summary_{p.name}.txt").exists()) if KNOWLEDGE.exists() else []
    if args.prefetch_only:
        prefetch_gene_facts({g for p in ready for gs in module_genes(p).values() for g in gs})
        return
    if args.only:
        jobs = [(p, int(m)) for p, m in (x.rsplit(":", 1) for x in args.only) if p in ready]
        jobs = [(p, m) for p, m in jobs if m in pending_modules(p)]
    else:
        jobs = [(p, m) for p in (args.pairs or ready) if p in ready for m in pending_modules(p)]
    if args.max_modules is not None:
        jobs = jobs[:args.max_modules]
    print(f"Processing {len(jobs)} modules from {len({p for p, _ in jobs})} tissue pairs; model {args.model}, agent {args.agent}", flush=True)
    prefetch_gene_facts({g for p, m in jobs for g in module_genes(p)[m]})

    kw = {"reasoning_effort": args.reasoning_effort} if args.reasoning_effort else {}
    model = OpenAIServerModel(model_id=args.model, api_key=load_api_key(), **kw)
    pin, pout = PRICES.get(args.model, (0.0, 0.0))
    statuses, t0 = [], time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(run_module, p, m, model, args.agent): (p, m) for p, m in jobs}
        for k, fut in enumerate(as_completed(futures), 1):
            p, m = futures[fut]
            try:
                st = fut.result()
            except Exception:
                st = dict(pair=p, module=m, agent=args.agent, attempts=0, passed=False, seconds=0,
                          input_tokens=0, output_tokens=0, note=traceback.format_exc()[-300:])
            st.update(model=args.model, usd=round((st["input_tokens"] * pin + st["output_tokens"] * pout) / 1e6, 4))
            statuses.append(st)
            print(f"[{k}/{len(jobs)}] {p}:{m} passed={st['passed']} attempts={st['attempts']} {st['seconds']}s "
                  f"tokens={st['input_tokens']}+{st['output_tokens']} ${st['usd']} {st['note'][:80]}", flush=True)
    if statuses:
        update_csv(CONFIG["traces"] / "modules.csv", statuses, ["pair", "module", "model", "agent"])
        s = pd.DataFrame(statuses)
        print(f"\nPassed {int(s.passed.sum())}/{len(s)} in {(time.time() - t0) / 60:.1f} min; "
              f"tokens {int(s.input_tokens.sum()):,} input + {int(s.output_tokens.sum()):,} output; "
              f"about ${s.usd.sum():.2f} at list price")


if __name__ == "__main__":
    main()
