#!/usr/bin/env python3
"""Step 3a: GO/KEGG over-representation for every conserved co-abundance module (paper Eq. 5).

Runs after Step 2/2b and before step3_module_annotations.py, which reads the published results through
load_corrected_enrichment(prefix). No project data are sent to any external service.

Inputs
  analysis/{pair}.json                      module members (module id -> member records)
  analysis/{pair}/consensus_{pair}.pkl      consensus network; all of its nodes form the pair background
  analysis/{pair}/module_{id}_sz{n}_d{w}.graphml
  data/uniprot_human_reviewed.tsv           UniProt entry name -> primary gene symbol
  <work>/sources/                           public annotation downloads:
    gprofiler_full_hsapiens.ENSG.gmt  https://biit.cs.ut.ee/gprofiler/static/gprofiler_full_hsapiens.ENSG.gmt
    go-basic.obo                      https://current.geneontology.org/ontology/go-basic.obo
    hgnc_complete_set.txt             https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt
    kegg_hsa_pathway.tsv              https://rest.kegg.jp/link/pathway/hsa
    kegg_pathways.tsv                 https://rest.kegg.jp/list/pathway/hsa

Method
  Gene symbols are resolved to Ensembl genes through HGNC (approved symbols first, then unambiguous aliases or
  previous symbols). For module genes Q in pair background U and term gene set T: N = |U|, n = |Q|,
  K = |T & U|, k = |T & Q|, p_raw = Pr[X >= k] with X ~ Hypergeometric(N, K, n) (one-sided). Sources are
  GO:BP, GO:MF, GO:CC (GO roots excluded) and KEGG. Each module tests every term with K > 0 in its pair
  background. q_within_module: BH within one module; q_global: BH across all module-term tests of all pairs.

Outputs (work dir, default <work>/enrichment; copied to <knowledge>/enrichment with --publish)
  module_enrichment_summary.csv, enrichment_all_tests.csv.gz, by_pair/{pair}.json (module id -> terms with
  q_global < 0.05), background_genes.csv, gene_mapping_audit.csv, input_sha256.json, run_summary.json,
  COMPLETE.json. The work dir also keeps significant_terms_global.csv and kegg_genes_without_hgnc_ensembl.json.
"""
from __future__ import annotations
import argparse
import csv
import gzip
import hashlib
import json
import pickle
import re
import shutil
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.stats import hypergeom

from common import PATHS, load_clusters

DEFAULT_WORK = PATHS['work'] / 'enrichment'
PUBLISHED = PATHS['knowledge'] / 'enrichment'
SOURCES = ('GO:BP', 'GO:MF', 'GO:CC', 'KEGG')
# Keys of input_sha256.json are "analysis/<path relative to the analysis directory>".
HASH_PREFIX = 'analysis/'
PUBLISHED_FILES = ('module_enrichment_summary.csv', 'enrichment_all_tests.csv.gz', 'by_pair', 'background_genes.csv',
                   'gene_mapping_audit.csv', 'input_sha256.json', 'run_summary.json')
GRAPHML = re.compile(r'module_(\d+)_sz\d+_d[\d.]+\.graphml$')


def overrepresentation(N, K, n, k):
    return hypergeom.sf(np.asarray(k) - 1, N, K, n)


def bh(p, total_tests=None):
    """BH, allowing omitted p=1 tests only; never omit non-unit p values."""
    p = np.asarray(p, dtype=float)
    m = len(p) if total_tests is None else int(total_tests)
    if m < len(p) or np.any(~np.isfinite(p)) or np.any((p < 0) | (p > 1)):
        raise ValueError('Invalid p values or family size')
    if not len(p):
        return p.copy()
    order = np.argsort(p, kind='stable')
    ranked = p[order] * m / np.arange(1, len(p) + 1)
    adjusted = np.minimum(1, np.minimum.accumulate(ranked[::-1])[::-1])
    out = np.empty_like(p); out[order] = adjusted
    return out


def resolve_gene(gene, direct, aliases):
    if gene in direct:
        return direct[gene], 'approved_symbol'
    hits = aliases.get(gene, set())
    if len(hits) == 1:
        return next(iter(hits)), 'alias_or_previous_symbol'
    return None, 'ambiguous' if hits else 'unmapped'


def test_module(background, query, terms):
    if not query <= background:
        raise ValueError('Module contains genes outside its eligible background')
    K = np.array([len(t['genes'] & background) for t in terms], dtype=int)
    k = np.array([len(t['genes'] & query) for t in terms], dtype=int)
    p = overrepresentation(len(background), K, len(query), k) if query else np.ones(len(K))
    return dict(K=K, k=k, p=p, q=bh(p))


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''): h.update(block)
    return h.hexdigest()


def hash_key(path, analysis_dir):
    return HASH_PREFIX + Path(path).relative_to(analysis_dir).as_posix()


def hash_path(key, analysis_dir):
    """Resolve an input_sha256.json key ("analysis/<rel>" or "<rel>") against the analysis directory."""
    return Path(analysis_dir) / key.removeprefix(HASH_PREFIX)


def dump_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')
    tmp.replace(path)


def read_identifiers(src):
    direct, aliases, canonical, entrez = {}, defaultdict(set), {}, {}
    with open(src / 'hgnc_complete_set.txt') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            ensg = r['ensembl_gene_id']
            if r['status'] != 'Approved' or not ensg: continue
            direct[r['symbol']] = ensg; canonical[ensg] = r['symbol']
            if r['entrez_id']: entrez[r['entrez_id']] = ensg
            for key in ('alias_symbol', 'prev_symbol'):
                for symbol in r[key].split('|'):
                    if symbol: aliases[symbol].add(ensg)
    return direct, aliases, canonical, entrez


def read_terms(src, entrez):
    # OBO assigns ontology namespace; the GMT itself carries propagated memberships.
    namespaces, record = {}, {}
    ns = {'biological_process':'GO:BP','molecular_function':'GO:MF','cellular_component':'GO:CC'}
    def save():
        if record.get('id') and record.get('namespace') in ns:
            for identifier in [record['id']] + record.get('alt_id', []):
                namespaces[identifier] = ns[record['namespace']]
    with open(src / 'go-basic.obo') as f:
        for line in f:
            line = line.strip()
            if line.startswith('['): save(); record = {}
            elif ': ' in line:
                k,v = line.split(': ',1)
                if k == 'alt_id': record.setdefault(k, []).append(v)
                elif k in ('id','namespace'): record[k] = v
        save()
    # The three ontology roots are annotation universes, not biological hypotheses.
    roots = {'GO:0008150','GO:0003674','GO:0005575'}
    terms, missing = {}, []
    with open(src / 'gprofiler_full_hsapiens.ENSG.gmt') as f:
        for line in f:
            parts = line.rstrip('\n').split('\t'); identifier = parts[0]
            if not identifier.startswith('GO:') or identifier in roots: continue
            if identifier not in namespaces: missing.append(identifier); continue
            terms[identifier] = dict(id=identifier,name=parts[1],source=namespaces[identifier],genes=set(parts[2:]))
    # GO OBO and GMT can differ in obsolete terms. Fail rather than silently discard.
    if missing: raise ValueError(f'GO namespace not found for {len(missing)} GMT terms: {missing[:20]}')
    names = {}
    with open(src / 'kegg_pathways.tsv') as f:
        for line in f:
            k,v = line.rstrip('\n').split('\t'); names[k.removeprefix('path:')] = v
    for identifier,name in names.items():
        terms['KEGG:'+identifier] = dict(id='KEGG:'+identifier,name=name,source='KEGG',genes=set())
    unmapped_kegg = set()
    with open(src / 'kegg_hsa_pathway.tsv') as f:
        for line in f:
            gene,pathway = line.strip().split('\t'); eid=gene.removeprefix('hsa:')
            tid='KEGG:'+pathway.removeprefix('path:')
            if eid in entrez: terms[tid]['genes'].add(entrez[eid])
            else: unmapped_kegg.add(eid)
    return sorted(terms.values(),key=lambda t:(SOURCES.index(t['source']),t['id'])), sorted(unmapped_kegg)


def check_pair_files(pair, clusters, analysis_dir):
    """Every module id of the pair json has exactly one graphml file, and every graphml file has a module."""
    found = defaultdict(list)
    for path in (analysis_dir / pair).glob('module_*.graphml'):
        m = GRAPHML.match(path.name)
        if not m: raise ValueError(f'{pair}: unexpected graphml file name {path.name}')
        found[int(m.group(1))].append(path)
    duplicated = sorted(i for i, paths in found.items() if len(paths) > 1)
    missing = sorted(set(clusters) - set(found)); extra = sorted(set(found) - set(clusters))
    if duplicated or missing or extra:
        raise ValueError(f'{pair}: module json and graphml files disagree '
                         f'(duplicated {duplicated}, without graphml {missing}, graphml without module {extra})')
    return sorted(paths[0] for paths in found.values())


def load_inputs(direct, aliases, canonical):
    analysis_dir = PATHS['analysis']
    with open(PATHS['data'] / 'uniprot_human_reviewed.tsv') as f:
        e2g={r['Entry Name']:r['Gene Names (primary)'].split(';')[0].strip() for r in csv.DictReader(f,delimiter='\t')}
    pair_files = sorted(analysis_dir.glob('*.json'))
    if not pair_files: raise FileNotFoundError(f'No module files (<pair>.json) in the analysis directory')
    pairs, audits, hashes = [], {}, {}
    for modulepath in pair_files:
        pair = modulepath.stem
        graphpath = analysis_dir/pair/f'consensus_{pair}.pkl'
        clusters = load_clusters(modulepath)
        graphmls = check_pair_files(pair, clusters, analysis_dir)
        with open(graphpath,'rb') as f: graph = pickle.load(f)
        raw_bg = sorted({e2g[e] for e in graph.vs['name'] if e2g.get(e)})
        mapping = {}
        for gene in raw_bg:
            ensg,status = resolve_gene(gene,direct,aliases)
            mapping[gene] = ensg
            audits[gene] = dict(input_gene=gene,ensembl_gene_id=ensg or '',canonical_symbol=canonical.get(ensg,''),status=status)
        background = {x for x in mapping.values() if x}
        modules=[]
        for mid in sorted(clusters):
            members = clusters[mid]
            genes = [x['gene'].split(';')[0].strip() for x in members]
            if not set(genes)<=set(raw_bg):raise ValueError(f'{pair} module {mid}: genes outside the consensus background')
            query={mapping[g] for g in genes if mapping[g]}
            modules.append(dict(module=mid,query=query,raw_genes=genes,n_proteins=len(members),
                                unmapped=sorted({g for g in genes if not mapping[g]})))
        if not modules:
            print(f'{pair}: no modules, skipped',flush=True); continue
        pairs.append(dict(pair=pair,background=background,raw_background=raw_bg,mapping=mapping,modules=modules))
        for path in [modulepath, graphpath, *graphmls]:
            hashes[hash_key(path, analysis_dir)] = sha256(path)
    return pairs, list(audits.values()), hashes


def write_csv(path, rows, fields=None):
    rows=list(rows)
    if fields is None: fields=list(rows[0]) if rows else []
    with open(path,'w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)


def load_corrected_enrichment(prefix, enrichment_dir=None, analysis_dir=None):
    """Globally corrected GO/KEGG terms of one pair as {'module_<id>': [term records]}.

    Only complete results computed from the current pair inputs are exposed: refuses if COMPLETE.json is missing or
    if any hashed input of the pair (module json, consensus network, module graphml files) has changed.
    """
    out = Path(enrichment_dir) if enrichment_dir else PUBLISHED
    analysis_dir = Path(analysis_dir) if analysis_dir else PATHS['analysis']
    if not (out / 'COMPLETE.json').exists():
        raise FileNotFoundError('Run step3_enrichment.py --publish before using corrected enrichment')
    hashes=json.loads((out/'input_sha256.json').read_text())
    relevant={k:v for k,v in hashes.items()
              if k.removeprefix(HASH_PREFIX)==f'{prefix}.json' or k.removeprefix(HASH_PREFIX).startswith(f'{prefix}/')}
    if not relevant:raise ValueError('Pair absent from the globally corrected test family')
    for name,digest in relevant.items():
        path=hash_path(name,analysis_dir)
        if not path.exists() or sha256(path)!=digest:
            raise ValueError('Inputs changed; recompute global enrichment before annotation: '+name)
    rows=json.loads((out/'by_pair'/f'{prefix}.json').read_text())
    return {f'module_{mid}':values for mid,values in rows.items()}


def main():
    ap=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--work-dir',type=Path,default=DEFAULT_WORK,
                    help='output directory; annotation downloads are read from <work-dir>/sources (default: <work>/enrichment)')
    ap.add_argument('--publish',action='store_true',help='copy the validated results to <knowledge>/enrichment')
    args=ap.parse_args(); work=args.work_dir; src=work/'sources'
    work.mkdir(parents=True,exist_ok=True); t0=time.time()
    (work/'COMPLETE.json').unlink(missing_ok=True)
    direct,aliases,canonical,entrez=read_identifiers(src)
    terms,missing_kegg=read_terms(src,entrez)
    pairs,audit,hashes=load_inputs(direct,aliases,canonical)
    nmodules=sum(len(p['modules']) for p in pairs)
    print(f'Loaded {len(pairs)} pairs, {nmodules} modules, {len(terms)} public GO/KEGG terms',flush=True)
    write_csv(work/'gene_mapping_audit.csv',audit)
    dump_json(work/'input_sha256.json',hashes)
    dump_json(work/'kegg_genes_without_hgnc_ensembl.json',missing_kegg)
    # Sparse gene->term index allows us to store only observed overlaps in RAM.
    by_gene=defaultdict(list)
    for i,t in enumerate(terms):
        for gene in t['genes']:by_gene[gene].append(i)
    stats=[];all_nonunit=[];total_tests=0; bg_rows=[]
    for pi,pair in enumerate(pairs):
        bg=pair['background']; N=len(bg); K=np.zeros(len(terms),dtype=np.int32)
        for gene in bg: K[by_gene.get(gene,[])]+=1
        ids=np.flatnonzero(K>0); pair['term_ids']=ids; pair['K']=K
        if not N:raise ValueError(f"No mapped background: {pair['pair']}")
        for g in pair['raw_background']:
            ensg=pair['mapping'][g]
            bg_rows.append(dict(pair=pair['pair'],input_gene=g,ensembl_gene_id=ensg or '',canonical_symbol=canonical.get(ensg,'')))
        for mod in pair['modules']:
            q=mod['query'];k=np.zeros(len(terms),dtype=np.int32)
            for gene in q:k[by_gene.get(gene,[])]+=1
            hit=np.flatnonzero(k>0);p=overrepresentation(N,K[hit],len(q),k[hit])
            qw=bh(p,len(ids));offset=sum(len(a) for a in all_nonunit)
            all_nonunit.append(p);total_tests+=len(ids)
            stats.append(dict(pair=pair,module=mod,hit=hit,k=k[hit],p=p,q_within=qw,offset=offset))
        if (pi+1)%20==0:print(f'Calculated {pi+1}/{len(pairs)} pairs',flush=True)
    p_all=np.concatenate(all_nonunit);q_all=bh(p_all,total_tests)
    print(f'Global BH: {total_tests:,} tests ({len(p_all):,} overlapping terms stored in RAM)',flush=True)
    write_csv(work/'background_genes.csv',bg_rows)
    del bg_rows,all_nonunit
    fields=['pair','module','source','term_id','name','n_module_proteins','n_module_genes_input','query_size','effective_domain_size','intersection_size','term_size','fold_enrichment','p_raw','q_within_module','q_global','genes','ensembl_genes']
    summaries=[];significant=[];by_pair=defaultdict(dict);written=0
    with gzip.open(work/'enrichment_all_tests.csv.gz','wt',newline='',compresslevel=4) as f:
        writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader()
        for mi,st in enumerate(stats):
            pair=st['pair'];mod=st['module'];q=mod['query'];N=len(pair['background']);n=len(q)
            pos={int(t):j for j,t in enumerate(st['hit'])};qg=q_all[st['offset']:st['offset']+len(st['p'])]
            modsig=[];nwithin=int(np.sum(st['q_within']<.05))
            for ti in pair['term_ids']:
                t=terms[ti];K=int(pair['K'][ti]);j=pos.get(int(ti));overlap=t['genes']&q
                if j is None:k,p,qw,gq=0,1.,1.,1.
                else:k,p,qw,gq=int(st['k'][j]),float(st['p'][j]),float(st['q_within'][j]),float(qg[j])
                members=sorted(canonical[e] for e in overlap)
                row=dict(pair=pair['pair'],module=mod['module'],source=t['source'],term_id=t['id'],name=t['name'],
                         n_module_proteins=mod['n_proteins'],n_module_genes_input=len(set(mod['raw_genes'])),query_size=n,
                         effective_domain_size=N,intersection_size=k,term_size=K,fold_enrichment=(k*N/(n*K) if n else ''),
                         p_raw=p,q_within_module=qw,q_global=gq,genes=';'.join(members),ensembl_genes=';'.join(sorted(overlap)))
                writer.writerow(row);written+=1
                if gq<.05:
                    significant.append(row);modsig.append(row)
            modsig.sort(key=lambda r:(r['q_global'],r['p_raw'],r['term_id']))
            # Explicit raw and adjusted fields; no ambiguous p_value.
            by_pair[pair['pair']][str(mod['module'])]=[{k:(v.split(';') if k in ('genes','ensembl_genes') else v) for k,v in r.items() if k not in ('pair','module')} for r in modsig]
            best=modsig[0] if modsig else None
            summaries.append(dict(pair=pair['pair'],module=mod['module'],n_proteins=mod['n_proteins'],
              n_input_genes=len(set(mod['raw_genes'])),n_mapped_genes=n,n_background_input=len(pair['raw_background']),n_background_mapped=N,
              n_tests=len(pair['term_ids']),n_within_bh_005=nwithin,n_global_bh_005=len(modsig),
              min_p_raw=float(st['p'].min()) if len(st['p']) else 1.,min_q_within=float(st['q_within'].min()) if len(st['p']) else 1.,
              min_q_global=float(qg.min()) if len(qg) else 1.,
              top_global_term=best['term_id'] if best else '',top_global_name=best['name'] if best else '',
              top_global_overlap=best['intersection_size'] if best else '',top_global_fold=best['fold_enrichment'] if best else '',
              unmapped_genes=';'.join(mod['unmapped']),members=';'.join(mod['raw_genes'])))
            if (mi+1)%100==0:print(f'Wrote {mi+1}/{len(stats)} modules ({written:,} rows)',flush=True)
    if written!=total_tests:raise AssertionError('Full result table missing tests')
    write_csv(work/'significant_terms_global.csv',significant,fields)
    write_csv(work/'module_enrichment_summary.csv',summaries)
    if (work/'by_pair').exists():shutil.rmtree(work/'by_pair')
    for pair,result in by_pair.items():dump_json(work/'by_pair'/f'{pair}.json',result)
    # Input integrity: the network and module files must not change during the run.
    for name,digest in hashes.items():
        if sha256(hash_path(name,PATHS['analysis']))!=digest:raise RuntimeError('Input changed during run: '+name)
    summary=dict(completed_at=datetime.now(timezone.utc).isoformat(),pairs=len(pairs),modules=nmodules,total_tests=total_tests,
                 multiple_testing='BH within each module and global BH across all module-term tests',
                 positive_overlap_tests=len(p_all),global_significant_terms=len(significant),
                 modules_with_global_significant_term=sum(s['n_global_bh_005']>0 for s in summaries),
                 modules_with_within_significant_term=sum(s['n_within_bh_005']>0 for s in summaries),
                 modules_without_mapped_genes=sum(s['n_mapped_genes']==0 for s in summaries),
                 mapped_input_symbols=sum(bool(s['ensembl_gene_id']) for s in audit),input_symbols=len(audit),
                 elapsed_seconds=time.time()-t0,sources={p.name:sha256(p) for p in sorted(src.iterdir()) if p.is_file()})
    dump_json(work/'run_summary.json',summary)
    dump_json(work/'COMPLETE.json',summary)
    if args.publish:publish(work)
    print(json.dumps(summary,indent=2),flush=True)


def publish(work, home=PUBLISHED):
    """Copy the result files to <knowledge>/enrichment; COMPLETE.json is written last."""
    home.mkdir(parents=True,exist_ok=True)
    (home/'COMPLETE.json').unlink(missing_ok=True)
    for name in PUBLISHED_FILES:
        source,target=work/name,home/name
        if source.is_dir():
            if target.exists():shutil.rmtree(target)
            shutil.copytree(source,target)
        else:shutil.copy2(source,target)
    shutil.copy2(work/'COMPLETE.json',home/'COMPLETE.json')
    print(f'Published results to {home}',flush=True)


if __name__=='__main__':main()
