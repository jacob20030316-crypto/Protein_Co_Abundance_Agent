# Conserved co-abundance modules: skin and stem_cells

## Module 0

**Tissue pair**: skin and stem_cells  
**Genes (15)**: PGD, ABCD1, ASAH1, ENO3, ERI1, GPNMB, IDH3A, MPDU1, NCSTN, NUDT19, RAB6B, RETSAT, MRPS15, SLC12A9, STX7

### Function

This is a sparse, heterogeneous co-abundance module rather than a clearly defined canonical pathway. The strongest network structure centers on RETSAT, with links toward lipid and membrane-trafficking genes, while other branches connect vesicle transport, mitochondrial metabolism, glycolysis, lysosomal function, glycosylation, and RNA processing. The gene annotations are compatible with coordinated cellular metabolism, membrane and organelle trafficking, and tissue or cell-state composition. However, no GO or KEGG term passed global correction, so no pathway-level enrichment can be claimed from the primary enrichment analysis. The absence of a globally significant term does not invalidate the module; it indicates that the gene set does not support a single statistically established functional label.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only a small subset is annotated as secreted, and most genes are intracellular or membrane-associated. HPA data show a mixture of low tissue specificity and tissue-enhanced or tissue-enriched genes, with skin protein detection for most genes where measurements are available. Every gene has cell-type-enhanced specificity, with recurrent signals involving neutrophils, monocytes, melanocytes, esophageal cells, trophoblast-related cells, and other specialized populations. Blood-cell specificity is low for most genes, but several genes show group-enriched, immune-enhanced, or immune-enriched patterns. Thus, the shared module may partly reflect shared cell types or sample-composition effects, including immune-cell and melanocyte-related signals, rather than a universal skin–stem-cell biochemical program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There is no supplementary STRING functional enrichment. None of the module gene pairs meets the stated high-confidence STRING interaction threshold, and no hu.MAP complex contains multiple module members. Therefore, the co-abundance relationships are not supported here by established high-confidence physical interaction or complex membership. The internal edges may instead reflect correlated expression, shared cell composition, parallel organelle states, or indirect biological coupling. Some individual functions are well established from the gene annotations: RETSAT in retinoid metabolism, GPNMB in membrane and signaling biology, STX7 in endosome–lysosome and phagosome fusion, and PGD in the oxidative pentose-phosphate pathway. These annotations support biological interpretability but do not establish a single physical complex.

**STRING interactions (score >= 0.7)**: 0 of 105 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module cannot be established as a new biological discovery solely because it is absent from STRING and hu.MAP; database absence is not proof of novelty. The module is nevertheless unusual in combining a coherent-looking co-abundance pattern with no high-confidence STRING pair, no multi-member hu.MAP complex, and no globally significant GO or KEGG term. Its possible novelty is therefore at the level of a tissue-pair-specific expression or cell-composition signature, not a demonstrated new pathway. Independent validation in additional skin and stem-cell cohorts, with adjustment for cell composition and technical effects, would be required before calling it a novel conserved mechanism.

**Hypothesis.** Hypothesis: the module may represent a shared cell-state or cellular-composition program involving lipid and retinoid handling, lysosomal and endosomal trafficking, redox-supporting metabolism, and specialized epithelial or immune-associated cells. RETSAT could mark the metabolic axis, while GPNMB and STX7 could link membrane trafficking and lysosomal or phagosomal biology; PGD could provide reducing-power support in metabolically active or stress-exposed cells. The observed co-abundance may arise from coordinated activation of these processes within particular skin-associated cell populations, or from recurring mixtures of melanocyte, keratinocyte, and myeloid signals, rather than direct interaction among all module proteins. This is a hypothesis, not an enrichment-supported mechanism.

### Important genes

#### RETSAT

- **Related proteins** (co-abundance neighbors): ABCD1 (0.93), RAB6B (0.91), ASAH1 (0.85), STX7 (0.82), MRPS15 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: retinol saturase. Predicted to enable all-trans-retinol 13,14-reductase activity. Predicted to be involved in retinol metabolic process. Located in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.077); pancreatic ductal adenocarcinoma (0.073); subarachnoid hemorrhage (0.042); cancer (0.038); diabetic kidney disease (0.027)
- **Europe PMC papers**: 477
- **Why important**: RETSAT has the most central position in the module network and connects to genes associated with membrane transport, lipid biology, mitochondrial ribosomes, and lysosomal or vesicular function. Its established annotation concerns retinol and retinoid metabolism, and HPA supports tissue enhancement in adipose tissue together with cell-type enhancement in adipocytes, enterocytes, colonocytes, foveolar cells, and melanocytes. It also has substantial literature coverage and disease associations including neoplasm and diabetic kidney disease.
- **Conclusion**: Established evidence supports RETSAT as the leading metabolic anchor of the module, especially for retinoid metabolism. It is not established that RETSAT drives the other module branches. Its role as a coordinating metabolic signal in this skin–stem-cell module remains a hypothesis.

#### GPNMB

- **Related proteins** (co-abundance neighbors): STX7 (0.84), SLC12A9 (0.82), MPDU1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycoprotein nmb. The protein encoded by this gene is a type I transmembrane glycoprotein which shows homology to the pMEL17 precursor, a melanocyte-specific protein. GPNMB shows expression in the lowly metastatic human melanoma cell lines and xenografts but does not show expression in the highly metastatic cell lines. GPNMB may be involved in growth delay and reduction of metastatic potential. Two transcript varia…
- **Diseases (Open Targets)**: familial primary localized cutaneous amyloidosis (0.701); Parkinson disease (0.481); amyloidosis cutis dyschromia (0.463); primary cutaneous amyloidosis (0.371); lymphoma (0.370)
- **Europe PMC papers**: 4875
- **Why important**: GPNMB is a prominent connector between RETSAT-linked biology and genes associated with vesicular or membrane processes, including STX7, SLC12A9, and MPDU1. It is tissue-enhanced in skin and cell-type-enhanced in basal keratinocytes, fibroblasts, and several macrophage-lineage populations. Its established annotations include cell adhesion, signaling, regulation of cytokine production, and regulation of cell migration. It has extensive literature coverage and notable associations with cutaneous amyloidosis, Parkinson disease, lymphoma, and other disorders.
- **Conclusion**: Established evidence supports GPNMB as a skin-relevant membrane and signaling marker with links to epithelial and myeloid cell states. The module does not establish that GPNMB physically interacts with its neighboring genes or controls the complete module. A role in coordinating tissue repair, immune signaling, or cell migration is plausible but remains hypothetical here.

#### STX7

- **Related proteins** (co-abundance neighbors): GPNMB (0.84), RETSAT (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Lysosomes; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntaxin 7. The protein encoded by this gene is a syntaxin family membrane receptor involved in vesicle transport. The encoded protein binds alpha-SNAP, an important regulator of transport vesicle fusion. Along with syntaxin 13, this protein plays a role in the ordered fusion of endosomes and lysosomes with the phagosome. [provided by RefSeq, May 2016].
- **Diseases (Open Targets)**: neurodegenerative disease (0.489); Abnormality of neuronal migration (0.259); Raynaud disease (0.180); placental abruption (0.166); aortic stenosis (0.081)
- **Europe PMC papers**: 701
- **Why important**: STX7 provides a functional bridge between GPNMB and RETSAT in the module network. Its established function is membrane-vesicle fusion, including ordered fusion involving endosomes, lysosomes, and phagosomes. HPA places it in lysosomes and shows enhancement across multiple immune and melanocytic cell types, with broad blood-cell representation. Its disease associations include neurodegenerative disease and several other disorders.
- **Conclusion**: Established evidence supports STX7 as a vesicle-trafficking and lysosomal component that could connect membrane turnover with immune-cell or melanocyte biology. The module does not prove a direct STX7–GPNMB or STX7–RETSAT interaction. Its proposed bridging role is therefore a mechanistic hypothesis based on network placement and known function.

#### PGD

- **Related proteins** (co-abundance neighbors): MRPS15 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphogluconate dehydrogenase. 6-phosphogluconate dehydrogenase is the second dehydrogenase in the pentose phosphate shunt. Deficiency of this enzyme is generally asymptomatic, and the inheritance of this disorder is autosomal dominant. Hemolysis results from combined deficiency of 6-phosphogluconate dehydrogenase and 6-phosphogluconolactonase suggesting a synergism of the two enzymopathies. Several transcript variants encoding…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); Abnormality of the skeletal system (0.329); autoimmune disorder of central nervous system (0.246); smoking behavior (0.245); essential hypertension (0.199)
- **Europe PMC papers**: 8652
- **Why important**: PGD is connected to MRPS15 and occupies a branch associated with mitochondrial protein synthesis and cellular metabolism. Its established function is the oxidative pentose-phosphate pathway and NADPH regeneration. HPA shows enrichment in bone marrow and esophagus, with cell-type signals involving esophageal cells and neutrophil-related populations, and blood-cell group enrichment across several myeloid cell types. It has substantial literature coverage and disease associations that include neurological and skeletal abnormalities.
- **Conclusion**: Established evidence supports PGD as a redox and metabolic marker, particularly relevant to proliferating, immune-associated, or stress-exposed cells. The module does not establish that pentose-phosphate activity is the central function of the entire module. Its inclusion may reflect metabolic state or cell composition rather than a direct shared pathway.

## Module 1

**Tissue pair**: skin and stem_cells  
**Genes (6)**: ACIN1, ALG9, RNF40, CNOT9, FAM107B, RCOR1

### Function

No GO or KEGG term passed global correction, and there was no STRING functional enrichment. The strongest functional interpretation therefore comes from the individual gene annotations and the network structure. ALG9 is an endoplasmic-reticulum alpha-mannosyltransferase involved in lipid-linked oligosaccharide assembly and protein N-linked glycosylation. The other genes represent transcriptional repression and differentiation control through RCOR1, mRNA turnover and CCR4-NOT activity through CNOT9, RNA splicing and apoptotic chromatin condensation through ACIN1, and transcriptional regulation, ubiquitination, and cell-cycle control through RNF40. The module is therefore best viewed as a mixed cellular-state module rather than a demonstrated single biochemical pathway. ALG9 is the central co-abundance hub, whereas the remaining genes form peripheral associations with it.

**Cell composition.** This is not a plasma-protein or secreted-protein module: none of the genes is annotated as secreted. All genes have low tissue specificity in HPA, and protein detection is reported for every module gene in skin. HPA reports low immune-cell specificity for all genes and no enriched blood-cell category, arguing against a clearly blood-derived module. Nevertheless, several genes have enhanced expression in selected cell types, including neutrophils or neutrophil progenitors for RCOR1 and FAM107B, and neural or glial cell types for ALG9. This leaves shared cell composition or a broadly expressed cellular program as possible contributors, but the HPA evidence does not support calling the module a blood-cell module. There is no matching HPA tissue for stem cells, so the cross-tissue interpretation is limited by that comparison.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and no hu.MAP complex contains multiple module members. Thus, the co-abundance relationships are not corroborated here as established physical interactions or membership in a known multiprotein complex. The observed network is centered on ALG9, which is co-abundant with each of the other genes, while the other genes do not show additional within-module connectivity. Known biology exists for the individual proteins, but the fact sheet provides no evidence that they operate together in one physical complex.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unrecognized co-abundance association because it lacks high-confidence STRING links, lacks a shared hu.MAP complex, and has no globally significant GO or KEGG enrichment. However, those absences do not establish that the module is novel: the genes have substantial prior literature, and co-abundance can arise from shared cell state, expression breadth, or sample composition without a new molecular mechanism. The defensible conclusion is that the specific cross-tissue co-abundance pattern is potentially novel, whereas the individual gene functions are established and not novel.

**Hypothesis.** Hypothesis: in skin and stem-cell samples, a broadly expressed cellular state may coordinately support endoplasmic-reticulum glycan assembly through ALG9 together with changes in RNA turnover, transcriptional repression, splicing, apoptotic readiness, and ubiquitin-linked regulation through the peripheral genes. ALG9 may act as the principal expression anchor rather than as a proven physical binding partner. The recurring neutrophil-progenitor and neutrophil annotations suggest that shared cell composition could contribute, but the low immune-cell specificity and lack of blood-cell enrichment make this only a secondary hypothesis. This model requires validation with independent cohorts, cell-composition adjustment, perturbation experiments, and direct protein-interaction assays.

### Important genes

#### ALG9

- **Related proteins** (co-abundance neighbors): RCOR1 (0.88), CNOT9 (0.87), FAM107B (0.85), ACIN1 (0.81), RNF40 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ALG9 alpha-1,2-mannosyltransferase. This gene encodes an alpha-1,2-mannosyltransferase enzyme that functions in lipid-linked oligosaccharide assembly. Mutations in this gene result in congenital disorder of glycosylation type Il. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2008].
- **Diseases (Open Targets)**: ALG9-congenital disorder of glycosylation (0.824); ALG9-associated autosomal dominant polycystic kidney disease (0.614); autosomal dominant polycystic kidney disease (0.575); congenital disorder of glycosylation type I (0.462); neurodegenerative disease (0.459)
- **Europe PMC papers**: 910
- **Why important**: ALG9 is the central network gene, connected to every other module member and having the strongest weighted centrality in the subgraph. Its established role in endoplasmic-reticulum lipid-linked oligosaccharide assembly and protein N-linked glycosylation provides the clearest mechanistic anchor. It is associated with congenital disorder of glycosylation and polycystic kidney disease, and it has substantial literature support.
- **Conclusion**: Established evidence supports ALG9 as a glycosylation enzyme and as the network anchor. It is reasonable to hypothesize that ALG9 helps mark the shared cellular state captured by the module, but the network does not demonstrate that ALG9 regulates the other genes or physically interacts with them.

#### RCOR1

- **Related proteins** (co-abundance neighbors): ALG9 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: REST corepressor 1. This gene encodes a protein that is well-conserved, downregulated at birth, and with a specific role in determining neural cell differentiation. The encoded protein binds to the C-terminal domain of REST (repressor element-1 silencing transcription factor). [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: secondary malignant neoplasm (0.269); adrenal gland hyperfunction (0.265); hyperaldosteronism (0.265); venous thromboembolism (0.259); Joubert syndrome (0.259)
- **Europe PMC papers**: 952
- **Why important**: RCOR1 is a transcriptional coregulator that binds REST and participates in neural differentiation and transcriptional repression. Its HPA profile includes enhanced expression in neutrophil progenitors, neutrophils, and suprabasal keratinocytes, making it relevant to both possible cell-composition effects and skin biology. It is a peripheral ALG9 neighbor and has substantial literature and disease-association evidence.
- **Conclusion**: Established evidence supports RCOR1 as a transcriptional and differentiation regulator. Its inclusion may reflect a shared differentiation or cell-state program, but the module does not establish a specific RCOR1–ALG9 regulatory relationship.

#### CNOT9

- **Related proteins** (co-abundance neighbors): ALG9 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytoplasmic bodies; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CCR4-NOT transcription complex subunit 9. This gene encodes a member of the highly conserved RCD1 protein family. The encoded protein is a transcriptional cofactor and a core protein of the CCR4-NOT complex. It may be involved in signal transduction as well as retinoic acid-regulated cell differentiation and development. Alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Oct 2012].
- **Diseases (Open Targets)**: melanoma (0.378); epilepsy (0.372); cutaneous melanoma (0.371); Intellectual disability (0.370); neuroendocrine neoplasm (0.192)
- **Europe PMC papers**: 283
- **Why important**: CNOT9 is a core component of the conserved CCR4-NOT complex, with established roles in mRNA polyadenylate-tail shortening and mRNA catabolism. Its annotations also include regulation of epidermal growth-factor-receptor signaling and differentiation-related processes. It is a peripheral ALG9 neighbor and connects the module to post-transcriptional control; its disease associations include melanoma and intellectual disability.
- **Conclusion**: Established evidence supports CNOT9 as an mRNA-regulatory complex component. Its module association is consistent with coordinated RNA-management activity, but there is no evidence here that CNOT9 directly acts with ALG9 or that the module is a CCR4-NOT complex.

#### ACIN1

- **Related proteins** (co-abundance neighbors): ALG9 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apoptotic chromatin condensation inducer 1. Apoptosis is defined by several morphologic nuclear changes, including chromatin condensation and nuclear fragmentation. This gene encodes a nuclear protein that induces apoptotic chromatin condensation after activation by caspase-3, without inducing DNA fragmentation. This protein has also been shown to be a component of a splicing-dependent multiprotein exon junction complex (EJC) that is deposi…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); adolescent idiopathic scoliosis (0.090); hepatocellular carcinoma (0.076); acute lymphoblastic leukemia (0.074); pancreatic neoplasm (0.045)
- **Europe PMC papers**: 894
- **Why important**: ACIN1 links two relevant processes: RNA splicing through its exon-junction-complex association and apoptosis through caspase-dependent chromatin condensation. It is also annotated in differentiation-related processes and is a peripheral ALG9 neighbor. Its disease associations and substantial literature make it a biologically interpretable indicator of RNA processing and apoptotic readiness.
- **Conclusion**: Established evidence supports ACIN1 functions in splicing-associated biology and apoptotic chromatin condensation. Its presence may indicate a cell-state program balancing RNA processing and apoptotic competence, but that interpretation remains inferential and is not a demonstrated pathway enrichment.

#### RNF40

- **Related proteins** (co-abundance neighbors): ALG9 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ring finger protein 40. The protein encoded by this gene contains a RING finger, a motif known to be involved in protein-protein and protein-DNA interactions. This protein was reported to interact with the tumor suppressor protein RB1. Studies of the rat counterpart suggested that this protein may function as an E3 ubiquitin-protein ligase, and facilitate the ubiquitination and degradation of syntaxin 1, which is an esse…
- **Diseases (Open Targets)**: neurodegenerative disease (0.536); lysosomal storage disease (0.319); atrial fibrillation (0.234); neoplasm (0.086); breast cancer (0.085)
- **Europe PMC papers**: 749
- **Why important**: RNF40 is a RING-containing protein associated with ubiquitin-linked regulation, transcriptional control, and mitotic cell-cycle regulation. It is a peripheral ALG9 neighbor and provides a plausible connection to chromatin or protein-quality regulation. Its annotations include neurodegenerative and neoplastic disease associations, with substantial literature support.
- **Conclusion**: Established evidence supports RNF40 as a regulator related to ubiquitination and transcription. Its co-abundance with ALG9 may reflect a shared proliferative, transcriptional, or proteostasis state, but the module does not establish a direct RNF40–ALG9 mechanism.
