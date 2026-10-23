# Agentic AI uncovers conserved cross-tissue protein co-abundance programs

An LLM-agent framework that compares human protein co-abundance across every pair of tissues. Starting from
sample-level proteomic data in ProteomicsDB, the agents build a co-abundance network for each tissue, identify
conserved co-abundance clusters for each tissue pair, retrieve evidence for every cluster and propose mechanistic
hypotheses in which each conclusion cites its evidence.

## Pipeline

| Step | Script | Agent | Output |
|---|---|---|---|
| 0 | `download.py` | – | sample-by-protein abundance matrices (`data/proteins/`) |
| 1 | `step1_tissue_networks.py` | Code Agent | one co-abundance network per tissue (`graph/`) |
| 2 | `step2_conserved_modules.py` | Analysis Agent | consensus network and candidate clusters per tissue pair (`analysis/`) |
| 2b | `step2b_cluster_filter.py` | – | degree-stratified permutation filter; keeps the conserved clusters (`analysis/`) |
| 3a | `step3_enrichment.py` | – | GO and KEGG enrichment with global Benjamini–Hochberg correction (`knowledge/enrichment/`) |
| 3b | `step3_module_annotations.py` | Knowledge Agent | evidence and description for every cluster (`knowledge/`) |
| 4 | `step4_research_reports.py` | Research Agent | function, novelty and mechanistic hypotheses for every cluster (`report/`) |

In the code and output files a conserved co-abundance cluster is called a *module*.

## Setup

```bash
conda create -n coabundance python=3.13 -y
conda activate coabundance
pip install -r requirements.txt

cp config.example.yaml config.yaml   # set the data and output directories
cp .env.example .env                 # add your OpenAI API key (or export OPENAI_API_KEY)
```

All scripts read their directories from `config.yaml`; set `COABUNDANCE_CONFIG` to use a configuration file
elsewhere. Every script has a `--help` option.

## Running

```bash
python download.py                     # download ProteomicsDB data and export the matrices
python step1_tissue_networks.py
python step2_conserved_modules.py
python step2b_cluster_filter.py --perm 10000
python step3_enrichment.py --publish
python step3_module_annotations.py
python step4_research_reports.py
```

Steps 1, 2, 3b and 4 call the OpenAI API (models are set in each script and can be changed on the command line).
Each tissue, tissue pair or cluster is analysed in its own agent run, and every run writes its full trajectory to
the `traces` directory.

## Data sources

ProteomicsDB, UniProt, Human Protein Atlas, hu.MAP 3.0, STRING, CORUM, Gene Ontology, KEGG, MyGene.info,
Open Targets and Europe PMC. Please cite the original resources and follow their terms of use.
