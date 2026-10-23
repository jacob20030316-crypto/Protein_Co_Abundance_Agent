# Conserved co-abundance modules: bone and kidney

## Module 0

**Tissue pair**: bone and kidney  
**Genes (31)**: PPP2R5D, ATXN10, ATXN2L, CCDC6, NCAPH, DBNL, DYNC1I2, DPYSL2, EGLN1, CCDC88A, GYS1, HS1BP3, CAST, IFI16, INF2, KLC2, LIMA1, MVP, MYO9B, NUP214, PARP4, PXN, PPP3CA, PPP6R3, SH3KBP1, SKIC8, STK10, SWAP70, CARS1, TCP11L1, VPS4B

### Function

The strongest supported interpretation is a conserved intracellular cytosol and cytoskeleton-associated module. (GO:CC cytosol; q_global = 0.0337) supports broad cytosolic localization, while (GO:CC cytoskeleton; q_global = 0.0355) supports cytoskeletal involvement. The module contains proteins involved in actin organization, focal adhesion, cell migration, microtubule-based transport, vesicle and lysosomal trafficking, intracellular signaling, phosphorylation control, RNA handling, oxygen sensing, and cell-cycle or chromosome organization. These annotations indicate a cellular architecture and trafficking program rather than a single specialized biochemical pathway. EGLN1 adds an oxygen-sensing component, PPP2R5D and PPP3CA provide phosphatase regulation, and VPS4B, KLC2, DYNC1I2, DBNL, MYO9B, LIMA1, PXN, and CCDC88A connect trafficking or cytoskeletal organization with signaling. The globally corrected evidence is limited to the cytosol and cytoskeleton terms; no globally corrected GO biological-process or KEGG pathway term is supplied. The absence of such a term does not invalidate the module, especially because the genes span several related intracellular processes.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and kidney protein detection is widespread among the genes with available kidney evidence. At the same time, many genes are cell-type enhanced, with recurrent signals in neutrophils and neutrophil progenitors, as well as monocytes, myeloid dendritic cells, brain cells, reproductive cells, and epithelial populations. The module therefore appears to mix broad intracellular machinery with cell-type-associated expression. The recurrent myeloid and neutrophil signal means that blood or immune-cell representation in the samples could contribute to the bone–kidney conservation. It should not be described as a purely tissue-resident bone or kidney program. The absence of secreted proteins argues against a circulating plasma-protein explanation.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC cytosol | 0.0337 | ATXN10, ATXN2L, CARS1, CCDC6, CCDC88A, DBNL, DPYSL2, DYNC1I2, EGLN1, GYS1, IFI16, KLC2, LIMA1, MVP, MYO9B, NCAPH, NUP214, PARP4, PPP2R5D, PPP3CA, PPP6R3, PXN, SH3KBP1, SKIC8, STK10, SWAP70, VPS4B |
| GO:CC cytoskeleton | 0.0355 | ATXN10, CCDC6, CCDC88A, DBNL, DPYSL2, DYNC1I2, INF2, KLC2, LIMA1, MVP, MYO9B, PARP4, PXN, SH3KBP1, SWAP70, TCP11L1, VPS4B |

### STRING and hu.MAP

STRING provides only a small set of high-confidence relationships within the module. The strongest established link is MVP–PARP4, and STRING also supports PPP2R5D–PPP3CA. These relationships are consistent with intracellular regulatory and protein-complex organization, but they do not by themselves establish a single unified pathway for the whole module. The supplementary STRING terms (STRING Component Cytosol; within-query FDR = 0.004) through (STRING Keyword Cytoplasm; within-query FDR = 0.0231) reinforce cytosolic, cytoplasmic, phosphoprotein, and cytoskeletal characteristics, but they are not global enrichment evidence. hu.MAP independently places MVP and PARP4 together in several complexes (hu.MAP huMAP3_04199.1) through (hu.MAP huMAP3_10679.1), although those complexes often include additional proteins outside the module. PPP2R5D and CCDC6 recur together in broader hu.MAP phosphatase-associated complexes (hu.MAP huMAP3_05182.1) through (hu.MAP huMAP3_13510.1). Thus, the module contains a small experimentally supported interaction core embedded in a broader co-abundance neighborhood. Most co-abundance edges are not represented by high-confidence STRING links or by a complete hu.MAP complex, so co-abundance should not be treated as direct physical interaction.

**STRING interactions (score >= 0.7)**: 2 of 465 gene pairs: MVP–PARP4 (0.999); PPP2R5D–PPP3CA (0.722)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Cytosol (FDR = 0.004, 27 genes); Keyword Phosphoprotein (FDR = 0.013, 30 genes); COMPARTMENTS Cytosol (FDR = 0.0132, 22 genes); Keyword Cytoskeleton (FDR = 0.0154, 12 genes); Keyword Cytoplasm (FDR = 0.0231, 23 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04199.1 (MVP, PARP4; 2/2); huMAP3_07373.1 (MVP, PARP4; 2/4); huMAP3_14130.1 (MVP, PARP4; 2/4); huMAP3_08496.1 (MVP, PARP4; 2/6); huMAP3_09304.1 (MVP, PARP4; 2/7); huMAP3_10679.1 (MVP, PARP4; 2/9); huMAP3_05182.1 (PPP2R5D, CCDC6; 2/10); huMAP3_06695.1 (PPP2R5D, CCDC6; 2/25); huMAP3_07998.1 (PPP2R5D, CCDC6; 2/26); huMAP3_09709.1 (PPP2R5D, CCDC6; 2/57); huMAP3_10333.1 (PPP2R5D, CCDC6; 2/63); huMAP3_13510.1 (PPP2R5D, CCDC6; 2/85)

### Novelty

The module is potentially novel as a conserved bone–kidney co-abundance pattern, but the fact sheet does not establish that it is a new biological complex or pathway. The limited overlap with high-confidence STRING interactions and the partial rather than complete representation in hu.MAP suggest that the particular cross-tissue organization may not be a previously defined interaction module. However, many component functions and some component relationships are already well established, including MVP–PARP4, PPP2R5D–PPP3CA, cytoskeletal regulation, vesicle transport, phosphatase signaling, and oxygen sensing. Therefore the defensible conclusion is that the conserved co-abundance configuration may be novel, whereas its individual molecular parts are not. Absence from STRING or hu.MAP alone is insufficient to claim discovery of a new mechanism. Novelty should be tested against independent bone and kidney cohorts, cell-composition adjustment, and perturbation or spatial experiments.

**Hypothesis.** Hypothesis: this module reflects a shared intracellular adaptation program in bone and kidney cells that couples oxygen sensing and phosphorylation control to cytoskeletal remodeling, adhesion, and vesicle trafficking. EGLN1 could provide oxygen-responsive regulation; PPP2R5D and PPP3CA could tune phosphorylation-dependent signaling; CCDC88A, PXN, LIMA1, MYO9B, DBNL, and SH3KBP1 could organize actin-linked adhesion and migration; and VPS4B, KLC2, DYNC1I2, and related transport proteins could redistribute membrane and organelle cargo. MVP–PARP4 may represent a stable regulatory subcomplex within this state. A further possibility is that the conserved signal partly reflects shared myeloid or neutrophil-related cell content rather than coordinated regulation within bone or kidney parenchymal cells. This is a hypothesis, not a causal demonstration; testing requires cell-resolved expression, perturbation of the candidate regulators, and measurement of oxygen response, phosphorylation, adhesion, and trafficking phenotypes.

### Important genes

#### EGLN1

- **Related proteins** (co-abundance neighbors): PXN (0.90), MVP (0.87), PARP4 (0.84), SH3KBP1 (0.82), HS1BP3 (0.82), DPYSL2 (0.81), CAST (0.80), INF2 (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: egl-9 family hypoxia inducible factor 1. The protein encoded by this gene catalyzes the post-translational formation of 4-hydroxyproline in hypoxia-inducible factor (HIF) alpha proteins. HIF is a transcriptional complex that plays a central role in mammalian oxygen homeostasis. This protein functions as a cellular oxygen sensor, and under normal oxygen concentration, modification by prolyl hydroxylation is a key regulatory event that tar…
- **Diseases (Open Targets)**: erythrocytosis, familial, 3 (0.729); anemia (0.599); chronic kidney disease (0.580); anemia (phenotype) (0.580); neurodegenerative disease (0.480)
- **Europe PMC papers**: 3215
- **Why important**: EGLN1 has the strongest network position in the module and connects PXN, MVP, PARP4, SH3KBP1, HS1BP3, DPYSL2, CAST, and INF2. Its established function is oxygen-dependent hydroxylation of HIF alpha proteins, linking it to hypoxia and oxygen homeostasis. It is detected in kidney, has an immune-cell association with neutrophils, and has substantial literature and disease links including chronic kidney disease and anemia. It is therefore a plausible bridge between tissue physiology and the cytoskeletal neighborhood.
- **Conclusion**: Established: EGLN1 is an oxygen-sensing enzyme and a highly connected module member with kidney detection. Hypothesis: EGLN1 may coordinate oxygen status with adhesion and cytoskeletal remodeling in the shared module; the co-abundance data do not prove that it regulates the other module genes.

#### MVP

- **Related proteins** (co-abundance neighbors): EGLN1 (0.87); STRING partners: PARP4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_04199.1, huMAP3_07373.1, huMAP3_14130.1, huMAP3_08496.1, huMAP3_09304.1, huMAP3_10679.1
- **Function (MyGene.info)**: major vault protein. This gene encodes the major component of the vault complex. Vaults are multi-subunit ribonucleoprotein structures that may be involved in nucleo-cytoplasmic transport. The encoded protein may play a role in multiple cellular processes by regulating the MAP kinase, JAK/STAT and phosphoinositide 3-kinase/Akt signaling pathways. The encoded protein also plays a role in multidrug resistance, and expre…
- **Diseases (Open Targets)**: neurodegenerative disease (0.392); Alzheimer disease (0.349); Parkinson disease (0.332); lysosomal storage disease (0.331); glioblastoma (0.112)
- **Europe PMC papers**: 6545
- **Why important**: MVP is directly connected to PARP4 by STRING and appears with PARP4 across several hu.MAP complexes (hu.MAP huMAP3_04199.1) through (hu.MAP huMAP3_10679.1). It is a major component of the vault complex and is annotated for intracellular transport and regulation of MAP kinase, JAK–STAT, and PI3K–Akt signaling. It has kidney protein detection and a substantial literature, including work on transport, signaling, multidrug resistance, and cancer.
- **Conclusion**: Established: MVP has an experimentally supported relationship with PARP4 and belongs to a known vault-associated protein system. Hypothesis: the MVP–PARP4 pair may form a regulatory anchor that links transport or stress responses to the wider cytoskeletal co-abundance state.

#### PPP2R5D

- **Related proteins** (co-abundance neighbors): MYO9B (0.89), KLC2 (0.81), ATXN2L (0.80); STRING partners: PPP3CA (0.722)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_05182.1, huMAP3_06695.1, huMAP3_07998.1, huMAP3_09709.1, huMAP3_10333.1, huMAP3_13510.1
- **Function (MyGene.info)**: protein phosphatase 2 regulatory subunit B'delta. The product of this gene belongs to the phosphatase 2A regulatory subunit B family. Protein phosphatase 2A is one of the four major Ser/Thr phosphatases, and it is implicated in the negative control of cell growth and division. It consists of a common heteromeric core enzyme, which is composed of a catalytic subunit and a constant regulatory subunit, that associates with a variety of regulatory su…
- **Diseases (Open Targets)**: Houge-Janssens syndrome 1 (0.804); Intellectual disability (0.647); cancer (0.533); neurodegenerative disease (0.527); hereditary disease (0.521)
- **Europe PMC papers**: 635
- **Why important**: PPP2R5D is connected in the module to MYO9B, KLC2, and ATXN2L and has a STRING relationship with the calcineurin catalytic subunit PPP3CA. It is a regulatory subunit of protein phosphatase two A and can influence substrate selection and catalytic activity. It is represented in multiple hu.MAP phosphatase-associated complexes (hu.MAP huMAP3_05182.1) through (hu.MAP huMAP3_13510.1), has kidney detection, and has disease associations involving neurodevelopment, intellectual disability, cancer, and neurodegeneration.
- **Conclusion**: Established: PPP2R5D is a phosphatase regulatory component with independent STRING and hu.MAP support. Hypothesis: it may tune phosphorylation of cytoskeletal or transport regulators and thereby connect signaling control to the module's structural phenotype.

#### VPS4B

- **Related proteins** (co-abundance neighbors): SH3KBP1 (0.86), ATXN10 (0.82), PPP3CA (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vacuolar protein sorting 4 homolog B. The protein encoded by this gene is a member of the AAA protein family (ATPases associated with diverse cellular activities), and is the homolog of the yeast Vps4 protein. In humans, two paralogs of the yeast protein have been identified. The former share a high degree of aa sequence similarity with each other, and also with yeast Vps4 and mouse Skd1 proteins. Mouse Skd1 (suppressor of K+ transpor…
- **Diseases (Open Targets)**: HIV infectious disease (0.462); dentin dysplasia type I (0.375); atypical dentin dysplasia due to SMOC2 deficiency (0.372); cystic kidney disease (0.194); enteritis (0.191)
- **Europe PMC papers**: 868
- **Why important**: VPS4B connects SH3KBP1, ATXN10, and PPP3CA in the module and is annotated for plasma membrane repair, autophagy, vacuole organization, lysosomal transport, and intracellular organization. It is detected in kidney and is enhanced in several epithelial and neutrophil-related cell types. Its position at the intersection of trafficking, membrane repair, and phosphatase-associated signaling makes it important for interpreting the module's cellular logistics.
- **Conclusion**: Established: VPS4B is an AAA-family trafficking and membrane-repair factor with relevant kidney and cell-type evidence. Hypothesis: VPS4B may connect vesicle or membrane turnover to actin remodeling in the conserved module, although the module does not establish direct physical binding to most of its neighbors.

#### MYO9B

- **Related proteins** (co-abundance neighbors): PPP2R5D (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin IXB. This gene encodes a member of the myosin family of actin-based molecular motor heavy chain proteins. The protein represents an unconventional myosin; it should not be confused with the conventional non-muscle myosin-9 (MYH9). The protein has four IQ motifs located in the neck domain that bind calmodulin, which serves as a light chain. The protein complex has a single-headed structure and exhibits …
- **Diseases (Open Targets)**: neurodegenerative disease (0.522); Abnormality of the skeletal system (0.470); hypertensive disorder (0.448); coronary artery disorder (0.406); essential hypertension (0.378)
- **Europe PMC papers**: 722
- **Why important**: MYO9B is linked to PPP2R5D and encodes an unconventional myosin with actin-based motor activity and Rho-GTPase regulatory capacity. Its annotations include actin movement and regulation of Rho signaling, while HPA shows lymphoid-tissue enhancement and cell-type enhancement in macrophages, monocytes, and neutrophil-related populations. It also has disease associations involving skeletal abnormalities, hypertension, and neurodegeneration.
- **Conclusion**: Established: MYO9B is a mechanistically relevant actin and Rho-signaling protein connected to the phosphatase regulatory branch. Hypothesis: it may translate phosphorylation and trafficking signals into changes in cell shape, motility, or adhesion in bone- and kidney-associated cells.

#### INF2

- **Related proteins** (co-abundance neighbors): EGLN1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inverted formin 2. This gene represents a member of the formin family of proteins. It is considered a diaphanous formin due to the presence of a diaphanous inhibitory domain located at the N-terminus of the encoded protein. Studies of a similar mouse protein indicate that the protein encoded by this locus may function in polymerization and depolymerization of actin filaments. Mutations at this locus have been associ…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease dominant intermediate E (0.827); focal segmental glomerulosclerosis 5 (0.807); focal segmental glomerulosclerosis (0.614); familial idiopathic steroid-resistant nephrotic syndrome (0.554); hereditary disease (0.503)
- **Europe PMC papers**: 1742
- **Why important**: INF2 is an established actin-formin gene and is annotated for actin filament polymerization, cytoskeleton organization, and mitochondrial fission. It is connected to EGLN1 in the module, is detected in kidney, and has strong disease associations with focal segmental glomerulosclerosis and related nephrotic syndromes. Its kidney disease relevance provides a direct tissue-specific rationale for prioritizing it despite its peripheral network position.
- **Conclusion**: Established: INF2 regulates actin-related processes and is associated with kidney disease, especially focal segmental glomerulosclerosis. Hypothesis: INF2 may be a structural effector through which the conserved module influences cell architecture or organelle dynamics; the present data do not establish that EGLN1 controls INF2.

## Module 1

**Tissue pair**: bone and kidney  
**Genes (9)**: PPP2R2A, CIP2A, NCAPD2, DIAPH1, TUBGCP2, IRAK1, OGFOD1, SMC2, SMC4

### Function

The strongest interpretation is a chromosome organization and cell-division module centered on condensin. The recurring (7 globally significant GO/KEGG terms, q_global 0.000898–0.0133; see the table) and (4 globally significant GO/KEGG terms, q_global 0.017–0.0439; see the table) terms identify chromosome condensation, chromosome segregation, and condensed nuclear chromosomes, while (GO:BP meiotic cell cycle; q_global = 0.0135) additionally links the module to meiotic cell-cycle processes. The core evidence comes from NCAPD2, SMC2, and SMC4, which occur together across the globally corrected GO terms. TUBGCP2 and PPP2R2A extend the signal toward mitotic organization, chromosome segregation, and microtubule-related cell division. The sparse network is not a uniformly connected pathway: it contains a highly coherent condensin-centered core and peripheral links involving signaling, cytoskeletal, translational, and phosphatase-related genes. Thus, the module most likely reflects coordinated abundance of chromosome-condensation machinery together with proteins associated with proliferating or differentiating cells. No KEGG enrichment is reported in the fact sheet.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are intracellular or nuclear. Most genes have low tissue specificity, while every gene has cell-type-enhanced evidence. The most frequent cell-type enrichments involve erythrocyte, megakaryocyte, monocyte, and neutrophil progenitors, with additional enrichment in early primary spermatocytes. Most genes have low immune-cell specificity, one is not detected in immune cells, and SMC4 is immune-cell enhanced. The pattern therefore does not support a simple mature blood-cell module, but it does raise the possibility that the bone–kidney conservation partly reflects shared progenitor, proliferative, or hematopoietic-related cell populations in the samples. Kidney protein detection is present for every module gene. The bone HPA comparison has no matching HPA tissue, so it cannot independently establish protein detection in bone.

**GO/KEGG enrichment**: 12 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP meiotic chromosome condensation | 0.000898 | NCAPD2, SMC2, SMC4 |
| GO:CC condensin complex | 0.00183 | NCAPD2, SMC2, SMC4 |
| GO:BP regulation of chromosome condensation | 0.00183 | NCAPD2, SMC2, SMC4 |
| GO:BP positive regulation of chromosome condensation | 0.00183 | NCAPD2, SMC2, SMC4 |
| GO:BP mitotic chromosome condensation | 0.0101 | NCAPD2, SMC2, SMC4 |
| GO:BP positive regulation of chromosome segregation | 0.0133 | NCAPD2, SMC2, SMC4 |
| GO:BP positive regulation of chromosome separation | 0.0133 | NCAPD2, SMC2, SMC4 |
| GO:BP meiotic cell cycle | 0.0135 | NCAPD2, SMC2, SMC4, TUBGCP2 |
| GO:BP chromosome organization involved in meiotic cell cycle | 0.017 | NCAPD2, SMC2, SMC4 |
| GO:BP regulation of chromosome segregation | 0.0178 | NCAPD2, PPP2R2A, SMC2, SMC4 |
| GO:BP chromosome segregation | 0.0302 | NCAPD2, PPP2R2A, SMC2, SMC4, TUBGCP2 |
| GO:CC condensed nuclear chromosome | 0.0439 | NCAPD2, SMC2, SMC4 |

### STRING and hu.MAP

STRING directly supports the condensin core through the very strong NCAPD2–SMC2, NCAPD2–SMC4, and SMC2–SMC4 relationships. STRING also supports an IRAK1–PPP2R2A relationship, but does not provide a comparable direct interaction network for the remaining peripheral genes. The STRING functional results (12 supplementary STRING terms; within-query FDR 0.0012–0.0393) independently reinforce DNA condensation, condensin, mitotic and meiotic chromosome processes, and the SMC flexible-hinge domain; these are supplementary because they are not global enrichment tests. hu.MAP complexes (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_14663.1) repeatedly place NCAPD2, SMC2, and SMC4 together in condensin-related complexes, alongside additional condensin subunits. Together, STRING and hu.MAP show that the central triad is an already established molecular complex, whereas the co-abundance links connecting that triad to IRAK1, TUBGCP2, CIP2A, DIAPH1, OGFOD1, and PPP2R2A are less directly established by these resources.

**STRING interactions (score >= 0.7)**: 4 of 36 gene pairs: IRAK1–PPP2R2A (0.91); NCAPD2–SMC2 (0.999); NCAPD2–SMC4 (0.999); SMC2–SMC4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword DNA condensation (FDR = 0.0012, 3 genes); Component Condensin complex (FDR = 0.0027, 3 genes); COMPARTMENTS Condensin complex (FDR = 0.0043, 3 genes); NetworkNeighborAL Positive regulation of chromosome condensation (FDR = 0.0046, 3 genes); RCTM Condensation of Prometaphase Chromosomes (FDR = 0.0086, 3 genes); Process Meiotic chromosome condensation (FDR = 0.0106, 3 genes); Process Meiotic cell cycle (FDR = 0.0106, 4 genes); Process Positive regulation of chromosome condensation (FDR = 0.0106, 3 genes); Process Mitotic chromosome condensation (FDR = 0.0131, 3 genes); RCTM M Phase (FDR = 0.022, 5 genes); RCTM Mitotic Prometaphase (FDR = 0.0334, 4 genes); SMART SMC proteins Flexible Hinge Domain (FDR = 0.0393, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03084.1 (SMC2, NCAPD2, SMC4; 3/8); huMAP3_14385.1 (SMC2, NCAPD2, SMC4; 3/9); huMAP3_09855.1 (SMC2, NCAPD2, SMC4; 3/10); huMAP3_11457.1 (SMC2, NCAPD2, SMC4; 3/10); huMAP3_14663.1 (SMC2, NCAPD2, SMC4; 3/14)

### Novelty

The condensin interpretation itself is not a new molecular finding: the NCAPD2–SMC2–SMC4 relationship is already supported by STRING, by several hu.MAP complexes, and by the globally corrected GO terms. The potentially novel aspect is the coordinated co-abundance of this condensin core with the particular peripheral genes in a module conserved across bone and kidney. That claim should remain cautious because absence of a relationship from STRING or hu.MAP does not prove novelty, and co-abundance can arise from shared cell composition, proliferation state, or technical and tissue-sampling effects. The module is therefore best described as a potentially tissue-pair-specific co-abundance configuration built around a known condensin core, rather than as discovery of a new condensin complex.

**Hypothesis.** Hypothesis: in both bone and kidney samples, a shared population of proliferating or differentiating cells produces coordinated abundance of condensin machinery, centrosomal components, cytoskeletal regulators, and signaling or phosphatase regulators. The NCAPD2–SMC2–SMC4 core could support chromosome condensation and segregation, while TUBGCP2 could reflect centrosomal and microtubule organization, PPP2R2A could modulate division-related dephosphorylation, and IRAK1 could connect inflammatory or innate-signaling state to the co-abundance pattern. The progenitor-enrichment pattern in HPA makes a shared cellular-composition or cell-state explanation plausible, but the available evidence does not demonstrate physical interaction or causal regulation among all module genes. This hypothesis should be tested using cell-resolved data, matched tissue histology, and perturbation of the condensin core and the peripheral regulators.

### Important genes

#### SMC2

- **Related proteins** (co-abundance neighbors): OGFOD1 (0.85), IRAK1 (0.80); STRING partners: NCAPD2 (0.999), SMC4 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_03084.1, huMAP3_14385.1, huMAP3_09855.1, huMAP3_11457.1, huMAP3_14663.1
- **Function (MyGene.info)**: structural maintenance of chromosomes 2. Predicted to enable ATP binding activity; chromatin binding activity; and single-stranded DNA binding activity. Involved in mitotic chromosome condensation. Located in condensed chromosome; cytoplasm; and nuclear lumen. Part of condensin complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: basal cell carcinoma (0.464); ovarian carcinoma (0.383); aortic stenosis (0.380); cancer (0.363); alcohol drinking (0.359)
- **Europe PMC papers**: 2065
- **Why important**: SMC2 is a central member of the condensin core, directly linked to NCAPD2 and SMC4 in STRING and present in every primary GO term (12 globally significant GO/KEGG terms, q_global 0.000898–0.0439; see the table). Its annotations identify chromosome condensation, chromosome organization, chromosome segregation, and condensin-complex membership. It has substantial literature support and disease associations involving cancer-related traits.
- **Conclusion**: Established evidence supports SMC2 as a structural and functional anchor of the module's chromosome-condensation interpretation. A hypothesis is that its co-abundance marks cells actively preparing for or undergoing chromosome segregation in both tissues; the fact sheet does not establish that activity directly.

#### SMC4

- **Related proteins** (co-abundance neighbors): NCAPD2 (0.88); STRING partners: NCAPD2 (0.999), SMC2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nuclear speckles, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_03084.1, huMAP3_14385.1, huMAP3_09855.1, huMAP3_11457.1, huMAP3_14663.1
- **Function (MyGene.info)**: structural maintenance of chromosomes 4. This gene belongs to the 'structural maintenance of chromosomes' (SMC) gene family. Members of this gene family play a role in two changes in chromosome structure during mitotic segregation of chromosomes- chromosome condensation and sister chromatid cohesion. The protein encoded by this gene is likely a subunit of the 13S condensin complex, which is involved in chromosome condensation. A pseudoge…
- **Diseases (Open Targets)**: clonal hematopoiesis (0.233); bone marrow failure syndrome (0.148); hepatocellular carcinoma (0.111); central nervous system cancer (0.107); glioma (0.107)
- **Europe PMC papers**: 1967
- **Why important**: SMC4 is the other structural SMC component of the condensin core and forms the strongly supported triad with NCAPD2 and SMC2. It is present in every primary GO term (12 globally significant GO/KEGG terms, q_global 0.000898–0.0439; see the table), is annotated for chromosome condensation and sister-chromatid segregation, and has substantial literature support. Its HPA profile includes lymphoid tissue, progenitor cell types, and immune-cell enhancement in basophils.
- **Conclusion**: Established evidence supports SMC4 as a core condensin component and a major explanation for the module's enrichment. Its progenitor and immune-related expression pattern supports, but does not prove, a cell-state or cell-composition contribution to the bone–kidney module.

#### NCAPD2

- **Related proteins** (co-abundance neighbors): IRAK1 (0.89), SMC4 (0.88), DIAPH1 (0.85); STRING partners: SMC2 (0.999), SMC4 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_03084.1, huMAP3_14385.1, huMAP3_09855.1, huMAP3_11457.1, huMAP3_14663.1
- **Function (MyGene.info)**: non-SMC condensin I complex subunit D2. Enables histone binding activity. Involved in mitotic chromosome condensation. Located in condensed chromosome; cytosol; and nucleoplasm. Part of condensin complex. Colocalizes with cytoplasm and nuclear chromosome. Implicated in primary autosomal recessive microcephaly. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: microcephaly 21, primary, autosomal recessive (0.592); autosomal recessive primary microcephaly (0.462); neurodegenerative disease (0.376); hereditary disease (0.194); lung adenocarcinoma (0.105)
- **Europe PMC papers**: 623
- **Why important**: NCAPD2 has a prominent position at the interface between the condensin core and module peripherals, connecting to SMC2, SMC4, IRAK1, and DIAPH1. It appears in every primary GO term (12 globally significant GO/KEGG terms, q_global 0.000898–0.0439; see the table), in the STRING condensin results (11 supplementary STRING terms; within-query FDR 0.0012–0.0334), and in every listed hu.MAP complex (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_14663.1). Its condensin annotation and association with primary autosomal recessive microcephaly provide functional and disease relevance.
- **Conclusion**: Established evidence makes NCAPD2 the strongest integrative marker of the module: it anchors a known condensin complex while occupying a network position connected to peripheral genes. A hypothesis is that NCAPD2 abundance couples chromosome organization to cytoskeletal or signaling state, but the co-abundance data alone do not establish such coupling.

#### IRAK1

- **Related proteins** (co-abundance neighbors): CIP2A (0.93), NCAPD2 (0.89), TUBGCP2 (0.88), SMC2 (0.80); STRING partners: PPP2R2A (0.91)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: interleukin 1 receptor associated kinase 1. This gene encodes the interleukin-1 receptor-associated kinase 1, one of two putative serine/threonine kinases that become associated with the interleukin-1 receptor (IL1R) upon stimulation. This gene is partially responsible for IL1-induced upregulation of the transcription factor NF-kappa B. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [pro…
- **Diseases (Open Targets)**: myelofibrosis (0.492); systemic lupus erythematosus (0.490); primary myelofibrosis (0.484); neoplasm (0.398); rheumatoid arthritis (0.393)
- **Europe PMC papers**: 10036
- **Why important**: IRAK1 has the highest network connectivity in the module and links the condensin-associated genes to CIP2A and TUBGCP2, while also having a high-confidence STRING relationship with PPP2R2A. Its established function in interleukin and Toll-like receptor signaling and NF-kappa B regulation provides a biologically distinct signaling axis. It has extensive literature support and disease associations including inflammatory and hematologic disorders.
- **Conclusion**: Established evidence supports IRAK1 as a signaling-associated peripheral hub rather than a condensin component. A hypothesis is that inflammatory signaling or shared progenitor-state regulation contributes to the module's conservation across tissues; the fact sheet does not show that IRAK1 directly regulates condensin in this module.

#### TUBGCP2

- **Related proteins** (co-abundance neighbors): IRAK1 (0.88), PPP2R2A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Centrosome, Basal body; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tubulin gamma complex component 2. Predicted to enable gamma-tubulin binding activity. Predicted to contribute to microtubule minus-end binding activity. Involved in brain development and neuron migration. Located in centrosome and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: pachygyria, microcephaly, developmental delay, and dysmorphic facies, with or without seizures (0.727); Abnormality of neuronal migration (0.381); influenza A (H1N1) (0.300); autosomal recessive spondylocostal dysostosis (0.065); spondylolisthesis (0.061)
- **Europe PMC papers**: 608
- **Why important**: TUBGCP2 connects IRAK1 and PPP2R2A and is the peripheral gene contributing to the primary meiotic-cell-cycle and chromosome-segregation terms (GO:BP meiotic cell cycle; q_global = 0.0135) and (GO:BP chromosome segregation; q_global = 0.0302). Its annotations implicate the centrosome, gamma-tubulin binding, microtubule nucleation, mitotic cell cycle, and brain development. Its disease associations and literature support make it relevant to division and developmental mechanisms, despite its lack of STRING or hu.MAP relationships in this module.
- **Conclusion**: Established evidence supports TUBGCP2 as a centrosomal and microtubule-related complement to the condensin signal. A hypothesis is that it reflects coordination between chromosome segregation and spindle or centrosome organization; this proposed connection is not directly demonstrated by the available interaction resources.

#### PPP2R2A

- **Related proteins** (co-abundance neighbors): TUBGCP2 (0.81); STRING partners: IRAK1 (0.91)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase 2 regulatory subunit Balpha. The product of this gene belongs to the phosphatase 2 regulatory subunit B family. Protein phosphatase 2 is one of the four major Ser/Thr phosphatases, and it is implicated in the negative control of cell growth and division. It consists of a common heteromeric core enzyme, which is composed of a catalytic subunit and a constant regulatory subunit, that associates with a variety of regulatory subu…
- **Diseases (Open Targets)**: neurodegenerative disease (0.568); hypertensive disorder (0.332); lysosomal storage disease (0.324); autoimmune disorder of central nervous system (0.316); type 2 diabetes mellitus (0.315)
- **Europe PMC papers**: 1549
- **Why important**: PPP2R2A provides a phosphatase-regulatory perspective on the module, connects to TUBGCP2 in the co-abundance network, and has a high-confidence STRING relationship with IRAK1. It contributes to the primary chromosome-segregation terms (GO:BP regulation of chromosome segregation; q_global = 0.0178) and (GO:BP chromosome segregation; q_global = 0.0302) and is annotated for protein dephosphorylation and regulation of chromosome segregation. It also has substantial literature support and disease associations spanning neurological, metabolic, and hypertensive disorders.
- **Conclusion**: Established evidence supports PPP2R2A as a plausible regulator of division-related signaling rather than as a condensin subunit. A hypothesis is that phosphatase-dependent control helps coordinate the condensin and centrosomal components, but the current evidence cannot distinguish direct regulation from correlated cell-state abundance.

## Module 2

**Tissue pair**: bone and kidney  
**Genes (37)**: HIBADH, ABHD10, ACADM, ACOT1, SLC25A4, AIFM1, ALDH4A1, ALDH2, ATP5F1A, ATP5F1B, ATP5F1C, CLU, CYB5A, HSD17B8, GLUD1, DHRS4, SLC25A10, ECHS1, ECI1, FAHD1, FMC1, FH, GGH, HIBCH, HSDL2, IVD, AK4, MFGE8, ALDH6A1, PCCB, SDHA, SPRYD4, SUCLG1, SUCLG2, ACAT1, ACAA2, TST

### Function

This is a strongly supported mitochondrial oxidative-metabolism module shared by bone and kidney. The primary evidence is the globally corrected enrichment for mitochondrion and mitochondrial matrix (GO:CC mitochondrion; q_global = 3.96e-16) (GO:CC mitochondrial matrix; q_global = 4.76e-14), small-molecule and organic-acid metabolism (7 globally significant GO/KEGG terms, q_global 2.18e-10–1.16e-06; see the table), and metabolic pathways (KEGG Metabolic pathways - Homo sapiens (human); q_global = 6.53e-08). The module particularly represents fatty-acid oxidation (6 globally significant GO/KEGG terms, q_global 0.000481–0.00319; see the table), branched-chain amino-acid and valine, leucine and isoleucine catabolism (4 globally significant GO/KEGG terms, q_global 1.73e-07–0.0109; see the table), carbon metabolism (KEGG Carbon metabolism - Homo sapiens (human); q_global = 4.46e-05), and mitochondrial energy generation (GO:BP generation of precursor metabolites and energy; q_global = 0.00676). The catalytic-activity and oxidoreductase terms (GO:MF catalytic activity; q_global = 0.00578) (GO:MF oxidoreductase activity; q_global = 0.0111) are consistent with a coordinated set of mitochondrial enzymes rather than a narrowly specialized signaling pathway. The extensive STRING supplementary evidence independently points to mitochondrial localization, matrix residence, fatty-acid beta-oxidation, and branched-chain amino-acid degradation (15 supplementary STRING terms; within-query FDR 1.5e-19–2.34e-07).

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins and is not broadly characterized as a blood-cell module. HPA assigns low immune-cell specificity to most genes, while only a small subset shows immune cell enhancement or enrichment. Most members are intracellular mitochondrial enzymes or transport and respiratory proteins. The HPA pattern is nevertheless tissue-biased: liver and kidney are frequent enriched tissues, with additional representation in muscle and other metabolically active tissues. Hepatocytes are the most frequent enriched cell type, and proximal-tubule representation is present for some genes. Kidney protein detection is reported for nearly all members, whereas bone lacks a matching HPA tissue assay. There are secreted exceptions: CLU is secreted to blood and MFGE8 is also secreted to blood. These genes, especially CLU, could reflect extracellular, vascular, or tissue-fluid contributions rather than the core mitochondrial program. Overall, the shared module is more plausibly a conserved metabolic program of metabolically active cells, with possible contribution from shared cell types or tissue handling, than a blood-contamination signature.

**GO/KEGG enrichment**: 42 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrion | 3.96e-16 | ABHD10, ACAA2, ACADM, ACAT1, ACOT1, AIFM1, AK4, ALDH2, ALDH4A1, ALDH6A1, ATP5F1A, ATP5F1B, ATP5F1C, CLU, CYB5A, DHRS4, ECHS1, ECI1, FAHD1, FH, FMC1, GLUD1, HIBADH, HIBCH, HSD17B8, HSDL2, IVD, PCCB, SDHA, SLC25A10, SLC25A4, SPRYD4, SUCLG1, SUCLG2, TST |
| GO:CC mitochondrial matrix | 4.76e-14 | ABHD10, ACAA2, ACADM, ACAT1, AK4, ALDH2, ALDH4A1, ALDH6A1, ATP5F1A, ATP5F1B, ATP5F1C, ECHS1, ECI1, FAHD1, FH, GLUD1, HIBADH, HIBCH, HSD17B8, IVD, PCCB, SDHA, SUCLG1, SUCLG2, TST |
| GO:BP small molecule metabolic process | 2.18e-10 | ACAA2, ACADM, ACAT1, ACOT1, AK4, ALDH2, ALDH4A1, ALDH6A1, ATP5F1A, ATP5F1B, ATP5F1C, DHRS4, ECHS1, ECI1, FAHD1, FH, GGH, GLUD1, HIBADH, HIBCH, HSD17B8, IVD, PCCB, SDHA, SLC25A10, SUCLG1, SUCLG2, TST |
| KEGG Metabolic pathways - Homo sapiens (human) | 6.53e-08 | ACAA2, ACADM, ACAT1, ACOT1, AK4, ALDH2, ALDH4A1, ALDH6A1, ATP5F1A, ATP5F1B, ATP5F1C, DHRS4, ECHS1, FAHD1, FH, GLUD1, HIBADH, HIBCH, HSD17B8, IVD, PCCB, SDHA, SUCLG1, SUCLG2, TST |
| GO:BP organic acid catabolic process | 1.43e-07 | ACAA2, ACADM, ACAT1, ALDH4A1, ALDH6A1, ECHS1, ECI1, GLUD1, HIBADH, HIBCH, IVD, PCCB, TST |
| GO:BP carboxylic acid catabolic process | 1.43e-07 | ACAA2, ACADM, ACAT1, ALDH4A1, ALDH6A1, ECHS1, ECI1, GLUD1, HIBADH, HIBCH, IVD, PCCB, TST |
| KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human) | 1.73e-07 | ACAA2, ACADM, ACAT1, ALDH2, ALDH6A1, ECHS1, HIBADH, HIBCH, IVD, PCCB |
| GO:BP carboxylic acid metabolic process | 2.61e-07 | ACAA2, ACADM, ACAT1, ACOT1, ALDH4A1, ALDH6A1, ECHS1, ECI1, FAHD1, FH, GGH, GLUD1, HIBADH, HIBCH, HSD17B8, IVD, PCCB, SDHA, TST |
| GO:BP oxoacid metabolic process | 3.85e-07 | ACAA2, ACADM, ACAT1, ACOT1, ALDH4A1, ALDH6A1, ECHS1, ECI1, FAHD1, FH, GGH, GLUD1, HIBADH, HIBCH, HSD17B8, IVD, PCCB, SDHA, TST |
| GO:BP organic acid metabolic process | 4.15e-07 | ACAA2, ACADM, ACAT1, ACOT1, ALDH4A1, ALDH6A1, ECHS1, ECI1, FAHD1, FH, GGH, GLUD1, HIBADH, HIBCH, HSD17B8, IVD, PCCB, SDHA, TST |
| GO:BP small molecule catabolic process | 1.16e-06 | ACAA2, ACADM, ACAT1, ALDH2, ALDH4A1, ALDH6A1, ECHS1, ECI1, GLUD1, HIBADH, HIBCH, IVD, PCCB, TST |
| GO:BP branched-chain amino acid metabolic process | 1.07e-05 | ACAT1, ALDH6A1, ECHS1, HIBADH, HIBCH, IVD, PCCB |
| KEGG Carbon metabolism - Homo sapiens (human) | 4.46e-05 | ACAT1, ALDH6A1, ECHS1, FH, GLUD1, HIBCH, PCCB, SDHA, SUCLG1, SUCLG2 |
| GO:BP amino acid catabolic process | 5.36e-05 | ACAT1, ALDH4A1, ALDH6A1, ECHS1, GLUD1, HIBADH, HIBCH, IVD |
| GO:BP branched-chain amino acid catabolic process | 6.43e-05 | ACAT1, ALDH6A1, ECHS1, HIBADH, HIBCH, IVD |

### STRING and hu.MAP

STRING contains many high-confidence relationships among the module genes, especially within the fatty-acid oxidation and branched-chain amino-acid catabolism groups. Examples include the connected relationships around ACAA2, ACAT1, ACADM, ECHS1, ECI1, HIBCH, HIBADH, IVD, ALDH6A1, PCCB, and HSDL2, as well as the respiratory and tricarboxylic-acid relationships involving ATP5F1A, ATP5F1B, ATP5F1C, FH, SDHA, SUCLG1, and SUCLG2. STRING therefore supports biological coherence and shows that much of the module recapitulates established functional associations; its enrichment statistics remain supplementary rather than global enrichment evidence. hu.MAP independently identifies a mitochondrial metabolic complex containing PCCB, IVD, ALDH4A1, ACAA2, and HSD17B8 (hu.MAP huMAP3_13468.1), the ATP synthase F1 subunit group containing ATP5F1A, ATP5F1B, and ATP5F1C (hu.MAP huMAP3_09307.1) (hu.MAP huMAP3_11095.1), and smaller complexes involving ALDH2 with ALDH6A1, ECHS1 with ECI1, and ACADM with TST (hu.MAP huMAP3_06207.1) (hu.MAP huMAP3_12099.1) (hu.MAP huMAP3_15255.1) (hu.MAP huMAP3_13307.1) (hu.MAP huMAP3_03498.1). These complexes provide physical or complex-level support, while the co-abundance edges may also reflect shared abundance regulation rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 73 of 666 gene pairs: ACAA2–ACADM (0.937); ACAA2–ACAT1 (0.963); ACAA2–ALDH6A1 (0.957); ACAA2–ECHS1 (0.975); ACAA2–ECI1 (0.859); ACAA2–HIBCH (0.73); ACAA2–HSDL2 (0.918); ACAA2–PCCB (0.962); ACAA2–SDHA (0.753); ACAA2–SUCLG1 (0.912); ACAA2–SUCLG2 (0.88); ACADM–ACAT1 (0.717); ACADM–ECHS1 (0.863); ACADM–ECI1 (0.732); ACADM–HIBCH (0.729); ACADM–HSDL2 (0.835); ACADM–PCCB (0.726); ACAT1–ALDH6A1 (0.938); ACAT1–ECHS1 (0.85); ACAT1–HIBCH (0.751); ACAT1–HSDL2 (0.909); ACAT1–SDHA (0.762); ACAT1–SUCLG1 (0.907); ACAT1–SUCLG2 (0.867); AK4–ATP5F1C (0.722); ALDH2–ALDH4A1 (0.85); ALDH2–ALDH6A1 (0.961); ALDH2–FH (0.723); ALDH2–GLUD1 (0.874); ALDH2–HIBADH (0.939); ALDH2–PCCB (0.843); ALDH4A1–GLUD1 (0.962); ALDH6A1–ECHS1 (0.723); ALDH6A1–HIBADH (0.996); ALDH6A1–HIBCH (0.811); ALDH6A1–PCCB (0.967); ATP5F1A–ATP5F1B (0.999); ATP5F1A–ATP5F1C (0.999); ATP5F1A–FH (0.793); ATP5F1A–SDHA (0.972); ATP5F1A–SLC25A4 (0.868); ATP5F1A–SUCLG1 (0.853); ATP5F1B–ATP5F1C (0.999); ATP5F1B–SDHA (0.917); ATP5F1B–SLC25A4 (0.824); ATP5F1B–SUCLG1 (0.733); ATP5F1C–SDHA (0.75); ATP5F1C–SUCLG1 (0.934); ATP5F1C–SUCLG2 (0.728); ECHS1–ECI1 (0.855); ECHS1–HIBADH (0.733); ECHS1–HIBCH (0.984); ECHS1–HSDL2 (0.8); ECHS1–IVD (0.973); ECHS1–PCCB (0.731); ECHS1–SUCLG1 (0.719); ECI1–HSDL2 (0.815); FAHD1–FH (0.869); FAHD1–SDHA (0.867); FH–GLUD1 (0.709); FH–SDHA (0.999); FH–SUCLG1 (0.926); FH–SUCLG2 (0.796); HIBADH–HIBCH (0.998); HIBADH–PCCB (0.908); HIBCH–HSDL2 (0.801); HIBCH–IVD (0.704); HIBCH–PCCB (0.701); HSDL2–IVD (0.777); IVD–PCCB (0.842); SDHA–SUCLG1 (0.999); SDHA–SUCLG2 (0.997); SUCLG1–SUCLG2 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Mitochondrion (FDR = 1.5e-19, 33 genes); Component Mitochondrion (FDR = 6.15e-17, 33 genes); Keyword Mitochondrion (FDR = 2.21e-15, 29 genes); Component Mitochondrial matrix (FDR = 4.95e-15, 24 genes); Keyword Transit peptide (FDR = 7.36e-14, 23 genes); NetworkNeighborAL Fatty acid beta-oxidation, and Valine, leucine and isoleucine degradation (FDR = 3.56e-10, 12 genes); COMPARTMENTS Mitochondrial matrix (FDR = 3.61e-10, 19 genes); NetworkNeighborAL Fatty acid beta-oxidation, and Valine, leucine and isoleucine degradation (FDR = 1.09e-09, 11 genes); Process Small molecule metabolic process (FDR = 1.38e-09, 27 genes); KEGG Metabolic pathways (FDR = 4.98e-09, 24 genes); NetworkNeighborAL Fatty acid beta-oxidation, and Ketone body metabolism (FDR = 1.63e-08, 10 genes); NetworkNeighborAL Fatty acid beta-oxidation, and Valine catabolic process (FDR = 4.47e-08, 9 genes); RCTM Metabolism (FDR = 4.9e-08, 27 genes); Process Organic acid catabolic process (FDR = 1.18e-07, 13 genes); KEGG Valine, leucine and isoleucine degradation (FDR = 2.34e-07, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (PCCB, IVD, ALDH4A1, ACAA2, HSD17B8; 5/99); huMAP3_09307.1 (ATP5F1B, ATP5F1A, ATP5F1C; 3/35); huMAP3_11095.1 (ATP5F1B, ATP5F1A, ATP5F1C; 3/45); huMAP3_06207.1 (ALDH2, ALDH6A1; 2/2); huMAP3_12099.1 (ECHS1, ECI1; 2/2); huMAP3_15255.1 (ACADM, TST; 2/3); huMAP3_13307.1 (ALDH2, ALDH6A1; 2/3); huMAP3_03498.1 (ACADM, TST; 2/4); huMAP3_08750.1 (ATP5F1B, ATP5F1A; 2/12); huMAP3_08716.1 (ATP5F1B, ATP5F1C; 2/15); huMAP3_10458.1 (PCCB, ACAA2; 2/16); huMAP3_07476.1 (ATP5F1B, ATP5F1C; 2/18); huMAP3_09775.1 (ATP5F1B, ATP5F1C; 2/21)

### Novelty

The module should not be described as a wholly new mitochondrial pathway. Its dominant biology is already well established by enzyme functions, globally corrected GO and KEGG terms, high-confidence STRING relationships, and hu.MAP complexes (GO:CC mitochondrion; q_global = 3.96e-16) (GO:CC mitochondrial matrix; q_global = 4.76e-14) (GO:BP small molecule metabolic process; q_global = 2.18e-10) (KEGG Metabolic pathways - Homo sapiens (human); q_global = 6.53e-08) (GO:BP organic acid catabolic process; q_global = 1.43e-07) (GO:BP carboxylic acid catabolic process; q_global = 1.43e-07) (KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 1.73e-07) (GO:BP carboxylic acid metabolic process; q_global = 2.61e-07) (GO:BP oxoacid metabolic process; q_global = 3.85e-07) (GO:BP organic acid metabolic process; q_global = 4.15e-07) (GO:BP small molecule catabolic process; q_global = 1.16e-06) (GO:BP branched-chain amino acid metabolic process; q_global = 1.07e-05) (KEGG Carbon metabolism - Homo sapiens (human); q_global = 4.46e-05) (GO:BP amino acid catabolic process; q_global = 5.36e-05) (GO:BP branched-chain amino acid catabolic process; q_global = 6.43e-05) (GO:BP L-amino acid catabolic process; q_global = 0.000219) (GO:BP proteinogenic amino acid catabolic process; q_global = 0.000219) (KEGG Propanoate metabolism - Homo sapiens (human); q_global = 0.000272) (GO:BP alpha-amino acid catabolic process; q_global = 0.000285) (GO:BP fatty acid catabolic process; q_global = 0.000481) (GO:BP lipid metabolic process; q_global = 0.0017) (GO:BP fatty acid beta-oxidation; q_global = 0.00192) (GO:BP monocarboxylic acid catabolic process; q_global = 0.00205) (GO:BP fatty acid metabolic process; q_global = 0.00217) (KEGG Fatty acid degradation - Homo sapiens (human); q_global = 0.00248) (GO:BP fatty acid oxidation; q_global = 0.00319) (GO:BP lipid oxidation; q_global = 0.00319) (GO:BP amino acid metabolic process; q_global = 0.00324) (GO:BP lipid catabolic process; q_global = 0.0033) (GO:BP alpha-amino acid metabolic process; q_global = 0.00423) (GO:MF catalytic activity; q_global = 0.00578) (GO:BP generation of precursor metabolites and energy; q_global = 0.00676) (GO:BP L-amino acid metabolic process; q_global = 0.00989) (GO:BP proteinogenic amino acid metabolic process; q_global = 0.00989) (GO:BP L-valine catabolic process; q_global = 0.0109) (GO:BP lipid modification; q_global = 0.0109) (GO:BP catabolic process; q_global = 0.011) (GO:MF oxidoreductase activity; q_global = 0.0111) (KEGG beta-Alanine metabolism - Homo sapiens (human); q_global = 0.0113) (GO:BP monocarboxylic acid metabolic process; q_global = 0.0149) (GO:BP sulfur compound catabolic process; q_global = 0.0263) (GO:CC mitochondrial envelope; q_global = 0.0379) (STRING COMPARTMENTS Mitochondrion; within-query FDR = 1.5e-19) (STRING Component Mitochondrion; within-query FDR = 6.15e-17) (STRING Keyword Mitochondrion; within-query FDR = 2.21e-15) (STRING Component Mitochondrial matrix; within-query FDR = 4.95e-15) (STRING Keyword Transit peptide; within-query FDR = 7.36e-14) (STRING NetworkNeighborAL Fatty acid beta-oxidation, and Valine, leucine and isoleucine degradation; within-query FDR = 3.56e-10) (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 3.61e-10) (STRING NetworkNeighborAL Fatty acid beta-oxidation, and Valine, leucine and isoleucine degradation; within-query FDR = 1.09e-09) (STRING Process Small molecule metabolic process; within-query FDR = 1.38e-09) (STRING KEGG Metabolic pathways; within-query FDR = 4.98e-09) (STRING NetworkNeighborAL Fatty acid beta-oxidation, and Ketone body metabolism; within-query FDR = 1.63e-08) (STRING NetworkNeighborAL Fatty acid beta-oxidation, and Valine catabolic process; within-query FDR = 4.47e-08) (STRING RCTM Metabolism; within-query FDR = 4.9e-08) (STRING Process Organic acid catabolic process; within-query FDR = 1.18e-07) (STRING KEGG Valine, leucine and isoleucine degradation; within-query FDR = 2.34e-07) (hu.MAP huMAP3_13468.1) (hu.MAP huMAP3_09307.1) (hu.MAP huMAP3_11095.1) (hu.MAP huMAP3_06207.1) (hu.MAP huMAP3_12099.1) (hu.MAP huMAP3_15255.1) (hu.MAP huMAP3_13307.1) (hu.MAP huMAP3_03498.1) (hu.MAP huMAP3_08750.1) (hu.MAP huMAP3_08716.1) (hu.MAP huMAP3_10458.1) (hu.MAP huMAP3_07476.1) (hu.MAP huMAP3_09775.1). The potentially novel result is the conserved co-abundance organization of this particular combination across bone and kidney, especially the integration of fatty-acid oxidation, branched-chain amino-acid catabolism, tricarboxylic-acid metabolism, ATP synthesis, and a small extracellular component. Absence of a complete matching STRING interaction network or hu.MAP complex would not establish novelty, because those resources describe known molecular associations rather than this tissue-pair co-abundance pattern. Novelty therefore requires comparison with prior bone-kidney co-abundance modules, independent cohorts, and orthogonal measurements; the fact sheet alone supports a biologically coherent conserved module, but not a claim of an entirely new molecular mechanism.

**Hypothesis.** Hypothesis: bone and kidney cells sharing this module coordinate mitochondrial substrate oxidation and energy conversion under a common metabolic state. Flux through fatty-acid oxidation and branched-chain amino-acid catabolism may supply acetyl-CoA, propionyl-CoA, reducing equivalents, and tricarboxylic-acid intermediates, while succinate metabolism, ATP synthase, adenine-nucleotide transport, and related mitochondrial functions couple substrate use to energy availability. The co-abundance pattern may therefore mark a coordinated mitochondrial capacity that supports energetic and biosynthetic demands in both tissues. CLU and MFGE8 could represent a linked stress, tissue-remodeling, vascular, or extracellular-clearance component, but this connection is a hypothesis rather than proof of a common pathway. It should be tested using cell-resolved expression, mitochondrial flux, substrate tracing, and independent bone and kidney cohorts.

### Important genes

#### ACAA2

- **Related proteins** (co-abundance neighbors): ACAT1 (0.89), ECHS1 (0.86), FH (0.82), HIBADH (0.82), AK4 (0.81), TST (0.80), ECI1 (0.80), CLU (0.80); STRING partners: ACADM (0.937), ACAT1 (0.963), ALDH6A1 (0.957), ECHS1 (0.975), ECI1 (0.859), HIBCH (0.73), HSDL2 (0.918), PCCB (0.962), SDHA (0.753), SUCLG1 (0.912), SUCLG2 (0.88)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10458.1
- **Function (MyGene.info)**: acetyl-CoA acyltransferase 2. The encoded protein catalyzes the last step of the mitochondrial fatty acid beta-oxidation spiral. Unlike most mitochondrial matrix proteins, it contains a non-cleavable amino-terminal targeting signal. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: bone remodeling disease (0.270); sinusitis (0.260); refractive error (0.190); kidney disorder (0.151); myopia (0.141)
- **Europe PMC papers**: 3056
- **Why important**: ACAA2 has the strongest network position in the supplied module and connects multiple core metabolic neighbors, including ACAT1, ECHS1, FH, HIBADH, ECI1, and TST. It is a mitochondrial enzyme catalyzing the last step of the fatty-acid beta-oxidation spiral, appears in many primary enrichment terms, and is supported by extensive STRING relationships and hu.MAP complexes (hu.MAP huMAP3_13468.1) (hu.MAP huMAP3_10458.1). HPA detects it in kidney and shows liver enhancement. Its disease and literature associations are substantial, making it a strong marker of the module's central mitochondrial lipid-catabolic axis.
- **Conclusion**: Established: ACAA2 is a central, mitochondrially localized fatty-acid oxidation enzyme and a highly connected module member. Hypothesis: its network position makes it a useful integrator or readout of coordinated mitochondrial lipid oxidation in the shared bone-kidney state, but co-abundance does not demonstrate that it controls the module.

#### ACAT1

- **Related proteins** (co-abundance neighbors): ACOT1 (0.91), ACAA2 (0.89), SUCLG2 (0.80); STRING partners: ACAA2 (0.963), ACADM (0.717), ALDH6A1 (0.938), ECHS1 (0.85), HIBCH (0.751), HSDL2 (0.909), SDHA (0.762), SUCLG1 (0.907), SUCLG2 (0.867)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA acetyltransferase 1. This gene encodes a mitochondrially localized enzyme that catalyzes the reversible formation of acetoacetyl-CoA from two molecules of acetyl-CoA. Defects in this gene are associated with 3-ketothiolase deficiency, an inborn error of isoleucine catabolism characterized by urinary excretion of 2-methyl-3-hydroxybutyric acid, 2-methylacetoacetic acid, tiglylglycine, and butanone. [provided by RefSeq,…
- **Diseases (Open Targets)**: beta-ketothiolase deficiency (0.817); hereditary disease (0.470); Abnormality of the skeletal system (0.239); neoplasm (0.115); nonpapillary renal cell carcinoma (0.105)
- **Europe PMC papers**: 4147
- **Why important**: ACAT1 is among the most functionally central genes in the module's primary enrichment profile. It catalyzes reversible acetoacetyl-CoA formation and participates in fatty-acid and isoleucine catabolism, with strong STRING links to ACAA2, ACADM, ALDH6A1, ECHS1, HIBCH, HSDL2, and succinate-pathway proteins. HPA shows enhancement in kidney and liver, and the gene has a substantial literature base and a direct association with beta-ketothiolase deficiency.
- **Conclusion**: Established: ACAT1 is a mitochondrial metabolic hub connecting acetyl-CoA handling with lipid and branched-chain amino-acid catabolism. Hypothesis: it may help couple substrate selection to energy production in the shared module, although the network cannot establish altered enzymatic flux.

#### ECHS1

- **Related proteins** (co-abundance neighbors): ACAA2 (0.86), TST (0.83), CLU (0.82); STRING partners: ACAA2 (0.975), ACADM (0.863), ACAT1 (0.85), ALDH6A1 (0.723), ECI1 (0.855), HIBADH (0.733), HIBCH (0.984), HSDL2 (0.8), IVD (0.973), PCCB (0.731), SUCLG1 (0.719)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_12099.1
- **Function (MyGene.info)**: enoyl-CoA hydratase, short chain 1. The protein encoded by this gene functions in the second step of the mitochondrial fatty acid beta-oxidation pathway. It catalyzes the hydration of 2-trans-enoyl-coenzyme A (CoA) intermediates to L-3-hydroxyacyl-CoAs. The gene product is a member of the hydratase/isomerase superfamily. It localizes to the mitochondrial matrix. Transcript variants utilizing alternative transcription initiation site…
- **Diseases (Open Targets)**: mitochondrial short-chain Enoyl-Coa hydratase 1 deficiency (0.848); Leigh syndrome (0.759); hereditary disease (0.509); neurodegenerative disease (0.371); colorectal carcinoma (0.095)
- **Europe PMC papers**: 1714
- **Why important**: ECHS1 is a mitochondrial matrix enzyme in the second step of fatty-acid beta-oxidation and also participates in valine and other branched-chain amino-acid catabolism. It is linked in STRING to many core module enzymes, including ACAA2, ACADM, ACAT1, ECI1, HIBCH, IVD, PCCB, and SUCLG1, and it forms a hu.MAP-supported complex with ECI1 (hu.MAP huMAP3_12099.1). It occurs across many primary metabolic terms and has established disease associations including mitochondrial short-chain enoyl-CoA hydratase deficiency and Leigh syndrome.
- **Conclusion**: Established: ECHS1 provides a biochemical bridge between lipid oxidation and branched-chain amino-acid catabolism. Hypothesis: it may be a particularly informative marker of coordinated substrate oxidation in both tissues, but the module does not show whether ECHS1 activity is limiting.

#### IVD

- **Related proteins** (co-abundance neighbors): ALDH4A1 (0.83), CLU (0.81), ALDH2 (0.80); STRING partners: ECHS1 (0.973), HIBCH (0.704), HSDL2 (0.777), PCCB (0.842)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: isovaleryl-CoA dehydrogenase. Isovaleryl-CoA dehydrogenase (IVD) is a mitochondrial matrix enzyme that catalyzes the third step in leucine catabolism. The genetic deficiency of IVD results in an accumulation of isovaleric acid, which is toxic to the central nervous system and leads to isovaleric acidemia. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Aug 2017].
- **Diseases (Open Targets)**: isovaleric acidemia (0.848); hereditary disease (0.514); idiopathic pulmonary fibrosis (0.252); interstitial lung disease (0.159); postinflammatory pulmonary fibrosis (0.124)
- **Europe PMC papers**: 11719
- **Why important**: IVD is the mitochondrial enzyme catalyzing a step in leucine catabolism and is included in the globally corrected branched-chain amino-acid, organic-acid, lipid-catabolic, and mitochondrial terms (15 globally significant GO/KEGG terms, q_global 3.96e-16–6.43e-05; see the table). It has strong STRING relationships with ECHS1, HIBCH, HSDL2, and PCCB and is a member of the hu.MAP metabolic complex (hu.MAP huMAP3_13468.1). HPA detects it in kidney and identifies hepatocyte enhancement. Its association with isovaleric acidemia and its substantial literature support make it a biologically interpretable marker of branched-chain substrate utilization.
- **Conclusion**: Established: IVD anchors the leucine-catabolic component of the module and is supported by both pathway and complex evidence. Hypothesis: coordinated IVD abundance may indicate shared handling of branched-chain substrates by bone- and kidney-associated cells, but this requires metabolite or flux validation.

#### ATP5F1B

- **Related proteins** (co-abundance neighbors): GLUD1 (0.84), ATP5F1A (0.80); STRING partners: ATP5F1A (0.999), ATP5F1C (0.999), SDHA (0.917), SLC25A4 (0.824), SUCLG1 (0.733)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_09307.1, huMAP3_11095.1, huMAP3_08750.1, huMAP3_08716.1, huMAP3_07476.1, huMAP3_09775.1
- **Function (MyGene.info)**: ATP synthase F1 subunit beta. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: hypermetabolism due to uncoupled mitochondrial oxidative phosphorylation 2 (0.499); hypertrophic cardiomyopathy (0.212); Alzheimer disease (0.177); hypertensive disorder (0.117); response to xenobiotic stimulus (0.117)
- **Europe PMC papers**: 735
- **Why important**: ATP5F1B encodes the beta subunit of mitochondrial ATP synthase and represents the energy-conversion arm of the module. It is part of the globally corrected mitochondrial and energy-generation terms (6 globally significant GO/KEGG terms, q_global 3.96e-16–0.0379; see the table), has very strong STRING relationships with ATP5F1A and ATP5F1C, and appears in multiple hu.MAP ATP synthase complexes (hu.MAP huMAP3_09307.1) (hu.MAP huMAP3_11095.1) (hu.MAP huMAP3_08750.1) (hu.MAP huMAP3_08716.1) (hu.MAP huMAP3_07476.1) (hu.MAP huMAP3_09775.1). HPA shows enhancement in skeletal muscle and kidney protein detection, and the gene has established associations with mitochondrial complex disorders and osteoblast differentiation.
- **Conclusion**: Established: ATP5F1B identifies the oxidative-phosphorylation and ATP-synthesis component and is supported by known complex membership. Hypothesis: its co-abundance with substrate-catabolic enzymes may indicate coordinated matching of fuel oxidation to ATP demand in the shared module.

#### CLU

- **Related proteins** (co-abundance neighbors): SLC25A4 (0.84), SUCLG2 (0.84), ECHS1 (0.82), IVD (0.81), ACAA2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: clusterin. The protein encoded by this gene is a secreted chaperone that can under some stress conditions also be found in the cell cytosol. It has been suggested to be involved in several basic biological events such as cell death, tumor progression, and neurodegenerative disorders. Alternate splicing results in both coding and non-coding variants.[provided by RefSeq, May 2011].
- **Diseases (Open Targets)**: Alzheimer disease (0.583); dementia (0.525); refractive error (0.444); late-onset Alzheimers disease (0.406); prostate cancer (0.376)
- **Europe PMC papers**: 10677
- **Why important**: CLU is important because it is a network bridge and a clear compositional exception. It connects to SLC25A4, SUCLG2, ECHS1, IVD, and ACAA2 in the co-abundance graph and appears in mitochondrial and lipid-related primary terms (4 globally significant GO/KEGG terms, q_global 3.96e-16–0.0379; see the table), but STRING reports no listed partners and hu.MAP reports no listed complex for it. Unlike the core enzymes, HPA describes CLU as secreted to blood, with liver enhancement and immune-cell enrichment in basophils, and reports no kidney immunohistochemistry detection. CLU also has a large literature base and disease associations involving neurodegeneration and cancer.
- **Conclusion**: Established: CLU is a secreted chaperone with a module-level co-abundance position but limited direct network and complex support. Hypothesis: CLU may connect mitochondrial metabolic state to extracellular stress, clearance, or tissue remodeling, or it may reflect sample composition; it should not be treated as evidence that CLU is a mitochondrial enzyme.

## Module 3

**Tissue pair**: bone and kidney  
**Genes (39)**: ACACA, AFG2A, C1orf122, CNOT1, CTBP2, DNAAF5, EIF2AK2, EDC4, EPS15L1, EP300, EPS15, EXOC8, EXOSC2, EXOSC3, GEMIN5, HSPBP1, LRWD1, LTN1, NUP155, NUP85, NUP88, PM20D2, TRIP13, PPM1B, PRRC2A, RAI14, RBM12, UPF1, RPAP3, STRN, SYNPO, TRMT1, TXNL4A, UBE3A, USP16, UNC45A, UTP25, ZC3HAV1, ZFR

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established pathway annotation from those analyses. Its gene-level evidence instead points to a heterogeneous intracellular gene-expression maintenance program, combining RNA binding and processing, mRNA surveillance and decay, nuclear pore transport, transcriptional regulation, ubiquitin-dependent control, and vesicle trafficking. The strongest coherent structural signals are the nuclear-pore group NUP155, NUP88, and NUP85; the exosome pair EXOSC2 and EXOSC3; the endocytic pair EPS15 and EPS15L1; and RNA-surveillance or decay relationships involving EDC4, CNOT1, and UPF1. The module is therefore best interpreted as a coordinated cellular homeostasis module rather than a specific bone or kidney pathway. The co-abundance structure may reflect shared cellular physiology or cell composition rather than a single dedicated biological process.

**Cell composition.** The module is not dominated by secreted or plasma proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and the kidney protein data detect many module proteins, supporting broad intracellular expression in kidney rather than a kidney-exclusive program. The HPA single-cell results show substantial cell-type enhancement, especially in spermatid and spermatocyte populations, astrocytes, Bergmann glia, and neutrophils, but the blood-cell specificity summary is largely low and only one gene is immune-cell enhanced. This argues against a simple plasma-protein or blood-cell contamination explanation, while still leaving shared cell types, general cellular state, and tissue-composition effects as plausible contributors. Bone protein evidence is unavailable in the supplied HPA summary, so bone-specific protein expression cannot be assessed from this sheet.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a small set of high-confidence relationships rather than broad support for one unified interaction network. Established relationships include CNOT1 with EDC4, EDC4 with UPF1, CTBP2 with EP300, EPS15 with EPS15L1, EXOSC2 with EXOSC3, and the interconnected nucleoporin relationships among NUP155, NUP85, and NUP88. The hu.MAP evidence independently reinforces several physical-complex interpretations: the nucleoporin trio occurs in one nuclear-pore complex, EXOSC2 and EXOSC3 occur in exosome complexes, EPS15 and EPS15L1 recur across multiple endocytic complexes, UPF1 and ZFR occur in an RNA-associated complex, TRIP13 and UNC45A share a complex, and TXNL4A and GEMIN5 occur in spliceosomal or snRNP-related complexes. These observations support real molecular modules embedded within the co-abundance network, but the many pairs without STRING or hu.MAP support indicate that co-abundance does not by itself establish direct physical interaction.

**STRING interactions (score >= 0.7)**: 8 of 741 gene pairs: CNOT1–EDC4 (0.79); CTBP2–EP300 (0.95); EDC4–UPF1 (0.942); EPS15–EPS15L1 (0.99); EXOSC2–EXOSC3 (0.999); NUP155–NUP85 (0.998); NUP155–NUP88 (0.995); NUP85–NUP88 (0.998)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12581.1 (NUP155, NUP88, NUP85; 3/58); huMAP3_05120.1 (EPS15, EPS15L1; 2/14); huMAP3_05382.1 (EXOSC2, EXOSC3; 2/18); huMAP3_06283.1 (EPS15, EPS15L1; 2/19); huMAP3_08540.1 (EPS15, EPS15L1; 2/19); huMAP3_14264.1 (EXOSC2, EXOSC3; 2/20); huMAP3_05849.1 (EPS15, EPS15L1; 2/21); huMAP3_09107.1 (EPS15, EPS15L1; 2/23); huMAP3_08320.1 (EPS15, EPS15L1; 2/24); huMAP3_09403.1 (EPS15, EPS15L1; 2/26); huMAP3_09042.1 (TRIP13, UNC45A; 2/26); huMAP3_10876.1 (EPS15, EPS15L1; 2/40); huMAP3_10625.1 (UPF1, ZFR; 2/57); huMAP3_10762.1 (EPS15, EPS15L1; 2/62); huMAP3_12918.1 (EPS15, EPS15L1; 2/62); huMAP3_06511.1 (TXNL4A, GEMIN5; 2/79); huMAP3_08980.1 (TXNL4A, GEMIN5; 2/97); huMAP3_12394.1 (EPS15, EPS15L1; 2/98)

### Novelty

This module should not be called a newly discovered molecular complex or a new pathway. Several of its internal relationships are already established by STRING and hu.MAP, and the functions of its major components are well documented. A potentially novel aspect is the reproducible co-abundance of these otherwise distinct RNA-processing, nuclear-pore, endocytic, and regulatory components across bone and kidney. However, the fact sheet does not provide an external comparison with previously reported cross-tissue modules, replication in independent cohorts, perturbation evidence, or tissue-resolved causal experiments. Consequently, the defensible conclusion is that the cross-tissue co-abundance configuration is a candidate observation requiring validation, not proof of novelty. Lack of database interaction evidence for some genes cannot establish novelty because databases are incomplete and co-abundance can represent indirect regulation or shared cell state.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular quality-control and trafficking state present in relevant bone and kidney cell populations. In this model, nuclear pores regulate exchange of RNA and proteins, RNA-binding, spliceosomal, exosome, decapping, and nonsense-mediated-decay components maintain transcript quality, and ubiquitin, chaperone, phosphatase, and endocytic machinery adjust protein turnover and receptor trafficking. The coordinated abundance of these systems could support cellular adaptation to differentiation, stress, or changing transport demands. This is a mechanistic hypothesis, not an established pathway assignment; it should be tested with cell-type-resolved expression, independent cohorts, protein-level measurements, and perturbation of representative RNA-surveillance and nuclear-pore components.

### Important genes

#### ZFR

- **Related proteins** (co-abundance neighbors): GEMIN5 (0.90), ACACA (0.89), HSPBP1 (0.88), CNOT1 (0.88), UTP25 (0.86), RPAP3 (0.85), TRMT1 (0.84), LRWD1 (0.84), DNAAF5 (0.83), LTN1 (0.80), UNC45A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_10625.1
- **Function (MyGene.info)**: zinc finger RNA binding protein. This gene encodes an RNA-binding protein characterized by its DZF (domain associated with zinc fingers) domain. The encoded protein may play a role in the nucleocytoplasmic shuttling of another RNA-binding protein, Staufen homolog 2, in neurons. Expression of this gene is regulated through alternative polyadenylation that mediates differential microRNA targeting. Elevated expression of this gene h…
- **Diseases (Open Targets)**: neurodegenerative disease (0.483); autosomal recessive spastic paraplegia type 71 (0.370); hyperaldosteronism (0.320); placental abruption (0.311); hearing loss disorder (0.242)
- **Europe PMC papers**: 793
- **Why important**: ZFR has the strongest network connectivity in the supplied module and links multiple otherwise separated portions of the graph, including CNOT1, GEMIN5, EXOSC3, and several regulatory or RNA-associated genes. Its annotation as a zinc-finger RNA-binding protein and its hu.MAP membership with UPF1 place it at the intersection of RNA handling and nucleocytoplasmic regulation. It also has substantial literature support and disease associations involving neurodegenerative and neurodevelopmental conditions.
- **Conclusion**: Established evidence supports ZFR as a central RNA-associated connector in this module. The hypothesis that it organizes the cross-tissue co-abundance pattern is plausible from its network position, but direct control of the other module genes is not demonstrated.

#### NUP155

- **Related proteins** (co-abundance neighbors): ACACA (0.85), TRIP13 (0.82), SYNPO (0.81); STRING partners: NUP85 (0.998), NUP88 (0.995)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 155. Nucleoporins are proteins that play an important role in the assembly and functioning of the nuclear pore complex (NPC) which regulates the movement of macromolecules across the nuclear envelope (NE). The protein encoded by this gene plays a role in the fusion of NE vesicles and formation of the double membrane NE. The protein may also be involved in cardiac physiology and may be associated with t…
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); atrial fibrillation (0.470); familial atrial fibrillation (0.390)
- **Europe PMC papers**: 944
- **Why important**: NUP155 is a member of the high-confidence hu.MAP nuclear-pore complex with NUP88 and NUP85, and STRING independently supports all of those nucleoporin relationships. It connects that pore group to ACACA, TRIP13, and SYNPO in the co-abundance graph. Its established role in nuclear-pore assembly, nucleocytoplasmic transport, and nuclear-envelope organization gives it a clear mechanistic anchor, while its disease associations include atrial-fibrillation-related conditions.
- **Conclusion**: Established evidence identifies NUP155 as a structural nuclear-pore component and a supported module subnetwork anchor. Its connection to the other functional branches may reflect shared transport demand or indirect regulation; a specific bone-kidney role remains a hypothesis.

#### EPS15

- **Related proteins** (co-abundance neighbors): UBE3A (0.84), AFG2A (0.83), EPS15L1 (0.82), STRN (0.81); STRING partners: EPS15L1 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_05120.1, huMAP3_06283.1, huMAP3_08540.1, huMAP3_05849.1, huMAP3_09107.1, huMAP3_08320.1, huMAP3_09403.1, huMAP3_10876.1, huMAP3_10762.1, huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: epidermal growth factor receptor pathway substrate 15. This gene encodes a protein that is part of the EGFR pathway. The protein is present at clatherin-coated pits and is involved in receptor-mediated endocytosis of EGF. Notably, this gene is rearranged with the HRX/ALL/MLL gene in acute myelogeneous leukemias. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, May 2009].
- **Diseases (Open Targets)**: atrial fibrillation (0.399); Abnormality of the skeletal system (0.383); bile duct carcinoma (0.370); esophageal adenocarcinoma (0.370); B-cell acute lymphoblastic leukemia (0.370)
- **Europe PMC papers**: 2810
- **Why important**: EPS15 is connected to EPS15L1, STRN, UBE3A, and AFG2A, and the pair with EPS15L1 is supported by STRING and repeatedly represented in hu.MAP endocytic complexes. Its established role in clathrin-associated receptor-mediated endocytosis and receptor recycling provides the clearest membrane-trafficking component of the module. It also has extensive literature and disease associations including skeletal-system abnormalities and leukemia-related rearrangement.
- **Conclusion**: Established evidence supports EPS15 as an endocytic and receptor-trafficking representative of the module. Its co-abundance with nuclear and RNA-processing genes may indicate coordinated cellular logistics, but does not establish that EPS15 directly regulates those processes.

#### EXOSC3

- **Related proteins** (co-abundance neighbors): LRWD1 (0.89), HSPBP1 (0.81); STRING partners: EXOSC2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_05382.1, huMAP3_14264.1
- **Function (MyGene.info)**: exosome component 3. This gene encodes a non-catalytic component of the human exosome, a complex with 3'-5' exoribonuclease activity that plays a role in numerous RNA processing and degradation activities. Related pseudogenes of this gene are found on chromosome 19 and 21. Alternatively spliced transcript variants encoding different isoforms have been described. [provided by RefSeq, Jun 2012].
- **Diseases (Open Targets)**: pontocerebellar hypoplasia type 1 (0.763); pontocerebellar hypoplasia (0.607); neurodegenerative disease (0.528); hereditary disease (0.414); pontocerebellar hypoplasia type 1A (0.370)
- **Europe PMC papers**: 2616
- **Why important**: EXOSC3 is supported by STRING interaction with EXOSC2 and by hu.MAP membership in exosome complexes. Its annotation establishes a role in RNA processing, RNA degradation, and ribosomal RNA maturation. The gene has substantial literature and strong disease associations with pontocerebellar hypoplasia, making it a biologically consequential representative of the RNA-quality-control branch.
- **Conclusion**: Established evidence supports EXOSC3 as part of the nuclear RNA-exosome machinery within the module. Its presence is consistent with transcript surveillance and processing, while any specific contribution to bone-kidney sharing remains untested.

#### CNOT1

- **Related proteins** (co-abundance neighbors): ZFR (0.88), PM20D2 (0.87), RPAP3 (0.85), NUP85 (0.81); STRING partners: EDC4 (0.79)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CCR4-NOT transcription complex subunit 1. Enables armadillo repeat domain binding activity; molecular adaptor activity; and nuclear receptor binding activity. Contributes to poly(A)-specific ribonuclease activity. Involved in several processes, including negative regulation of signal transduction; positive regulation of cytoplasmic mRNA processing body assembly; and regulation of gene expression. Located in P-body and cytosol. Part of CCR…
- **Diseases (Open Targets)**: holoprosencephaly 12 with or without pancreatic agenesis (0.749); Vissers-Bodmer syndrome (0.697); hereditary disease (0.515); complex neurodevelopmental disorder (0.474); neurodegenerative disease (0.471)
- **Europe PMC papers**: 1262
- **Why important**: CNOT1 is a central adaptor of the CCR4-NOT complex and connects ZFR, PM20D2, RPAP3, and NUP85 in the co-abundance graph. STRING supports its relationship with EDC4, linking transcriptional and mRNA-decay machinery. Its established roles in deadenylation-dependent mRNA decay, translational regulation, and P-body organization, together with substantial literature and developmental disease associations, make it an important regulatory bridge.
- **Conclusion**: Established evidence supports CNOT1 as a broad post-transcriptional regulatory component and a network bridge. The proposition that it coordinates the module's nuclear-pore and endocytic branches is a hypothesis requiring perturbation or temporal evidence.

## Module 4

**Tissue pair**: bone and kidney  
**Genes (49)**: AIMP2, GPT2, ARFIP2, CBS, GPS1, COPS3, DDX46, DHX57, DPH2, EIF2B2, EIF3F, ERGIC2, FAM120A, FAF1, FEN1, FHL3, GSDMD, HMGB3, MKI67, KIF2A, LANCL2, LARP7, LBR, WDR77, MAP2K3, NHLRC2, NSF, NT5DC1, PDCD4, PIH1D1, POGLUT3, PPP4C, PSMC6, PSMC4, PSMC2, PSMD13, ADSL, ERC1, SEPTIN2, SEPTIN8, GINS4, U2SURP, SRC, SRP68, SRP72, TBCE, TRIM33, NAE1, XRN2

### Function

The strongest interpretation is a proteasome-regulatory and protein-quality-control module. The primary evidence is the global enrichment of the proteasome regulatory particle and proteasome accessory complex (GO:CC proteasome regulatory particle; q_global = 0.00358) (GO:CC proteasome accessory complex; q_global = 0.00358), together with proteasome-activating activity (GO:MF proteasome-activating activity; q_global = 0.0216). PSMC2, PSMC4 and PSMC6 are proteasome ATPase subunits, while PSMD13 is a proteasome non-ATPase subunit, so the enriched genes represent a coherent regulatory-particle component rather than an isolated annotation. The module also contains genes linked to ubiquitin-dependent protein catabolism, oxidative-stress responses, protein neddylation, translation, RNA processing, DNA replication and cytoskeletal or vesicle processes. Those additional signals are distributed across the module and should be viewed as contextual features rather than equally established module functions. The network is relatively sparse overall, but its most convincing connected structure is the proteasome subnetwork, which is also supported by (STRING Component Proteasome regulatory particle; within-query FDR = 0.0242) and (STRING COMPARTMENTS Proteasome regulatory particle; within-query FDR = 0.026).

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module: the genes are overwhelmingly intracellular, and only a small minority are annotated as secreted. HPA indicates generally low tissue specificity and generally low immune-cell specificity, with many proteins detected in kidney. The available bone HPA protein field has no matching data, so absence of bone detection cannot be interpreted biologically. The module therefore does not strongly support a blood-cell contamination explanation, although several genes have enhanced or enriched signals in bone marrow, lymphoid tissue, erythroid or myeloid populations, and some genes are enhanced in specialized cell types. The shared bone-kidney signal could consequently reflect broadly expressed cellular machinery, shared proliferative or stress-related states, or contributions from particular cell populations rather than a bone-and-kidney-specific secreted program. HPA also shows frequent enhancement in reproductive, epithelial, skeletal-muscle and neural cell types, arguing against a single clearly defined tissue lineage as the sole explanation.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC proteasome regulatory particle | 0.00358 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:CC proteasome accessory complex | 0.00358 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:MF proteasome-activating activity | 0.0216 | PSMC2, PSMC4, PSMC6 |

### STRING and hu.MAP

STRING provides strong, internally coherent evidence for the proteasome core of the module: PSMC2, PSMC4, PSMC6 and PSMD13 are mutually connected at high confidence, and the same four genes drive the STRING proteasome regulatory-particle and compartment enrichments (STRING Component Proteasome regulatory particle; within-query FDR = 0.0242) (STRING COMPARTMENTS Proteasome regulatory particle; within-query FDR = 0.026). STRING also recovers established relationships for COPS3 with GPS1, DDX46 with U2SURP, SEPTIN2 with SEPTIN8, and SRP68 with SRP72. hu.MAP independently places the four proteasome genes together in several proteasome-related complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). It also supports SEPTIN2–SEPTIN8 (hu.MAP huMAP3_02362.1), GPS1–COPS3 (hu.MAP huMAP3_08550.1) (hu.MAP huMAP3_09779.1) (hu.MAP huMAP3_14528.1), LBR–FAF1 (hu.MAP huMAP3_10150.1) (hu.MAP huMAP3_13593.1), DDX46–WDR77 (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_08980.1), and LARP7–FAM120A (hu.MAP huMAP3_05807.1). These results show that the module contains several embedded, already characterized protein-complex fragments, with the proteasome fragment being the most compelling. The many module genes lacking high-confidence STRING links or multi-member hu.MAP support should not be treated as novel physical interactions merely because they co-abound.

**STRING interactions (score >= 0.7)**: 12 of 1176 gene pairs: COPS3–GPS1 (0.999); DDX46–U2SURP (0.918); DHX57–LARP7 (0.74); EIF3F–PSMD13 (0.705); PSMC2–PSMC4 (0.999); PSMC2–PSMC6 (0.999); PSMC2–PSMD13 (0.999); PSMC4–PSMC6 (0.999); PSMC4–PSMD13 (0.999); PSMC6–PSMD13 (0.999); SEPTIN2–SEPTIN8 (0.997); SRP68–SRP72 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Proteasome regulatory particle (FDR = 0.0242, 4 genes); COMPARTMENTS Proteasome regulatory particle (FDR = 0.026, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05064.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/31); huMAP3_09656.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/64); huMAP3_13725.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/69); huMAP3_02362.1 (SEPTIN2, SEPTIN8; 2/14); huMAP3_08550.1 (GPS1, COPS3; 2/34); huMAP3_10150.1 (LBR, FAF1; 2/38); huMAP3_13593.1 (LBR, FAF1; 2/42); huMAP3_09779.1 (GPS1, COPS3; 2/44); huMAP3_14528.1 (GPS1, COPS3; 2/49); huMAP3_14442.1 (ADSL, NT5DC1; 2/57); huMAP3_06511.1 (DDX46, WDR77; 2/79); huMAP3_05807.1 (LARP7, FAM120A; 2/81); huMAP3_08980.1 (DDX46, WDR77; 2/97)

### Novelty

The proteasome component is not a new biological discovery: its subunit identities, physical relationships and complex membership are already well established by STRING and hu.MAP. The co-abundance module may still be a new observation at the level of coordinated expression across bone and kidney, particularly because the full module combines the proteasome core with RNA-processing, translation, signaling, cytoskeletal and metabolic genes. However, the current evidence does not establish that this broader arrangement is a previously unknown biochemical complex or a bone-kidney-specific mechanism. The appropriate conclusion is conditional novelty: potentially novel as a tissue-pair co-abundance pattern, but not novel as a proteasome complex or as a set of individual protein interactions. Validation in independent bone and kidney cohorts, cell-composition adjustment, and testing whether the broader non-proteasome genes reproducibly track proteasome activity would be needed to support a stronger novelty claim.

**Hypothesis.** Hypothesis: the shared bone-kidney module reflects coordinated proteostasis during cellular stress or remodeling. The proteasome regulatory particle may couple ubiquitin-dependent degradation and oxidative-stress handling to changes in translation, RNA processing, DNA replication and vesicle or cytoskeletal organization. In bone, this could accompany matrix-producing or remodeling cells; in kidney, it could accompany metabolically active epithelial cells. The hypothesis is consistent with the proteasome enrichment (GO:CC proteasome regulatory particle; q_global = 0.00358) (GO:CC proteasome accessory complex; q_global = 0.00358) (GO:MF proteasome-activating activity; q_global = 0.0216), the proteasome interaction structure (STRING Component Proteasome regulatory particle; within-query FDR = 0.0242) (STRING COMPARTMENTS Proteasome regulatory particle; within-query FDR = 0.026), and the presence of stress, translation, trafficking and cell-cycle annotations, but those cross-process links are not directly demonstrated by the enrichment results. An alternative explanation is coordinated abundance from shared broadly expressed cellular machinery or variable cell-state composition in the samples.

### Important genes

#### PSMC2

- **Related proteins** (co-abundance neighbors): PSMC4 (0.91), MAP2K3 (0.84), ADSL (0.83), SRP72 (0.83), NT5DC1 (0.82), GPS1 (0.82), EIF3F (0.81), NHLRC2 (0.81); STRING partners: PSMC4 (0.999), PSMC6 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is the strongest network hub among the annotated module genes and connects the proteasome subnetwork with several other module regions. It belongs to the proteasome regulatory particle and is present in all primary proteasome terms (GO:CC proteasome regulatory particle; q_global = 0.00358) (GO:CC proteasome accessory complex; q_global = 0.00358) (GO:MF proteasome-activating activity; q_global = 0.0216), both STRING supplementary terms (STRING Component Proteasome regulatory particle; within-query FDR = 0.0242) (STRING COMPARTMENTS Proteasome regulatory particle; within-query FDR = 0.026), and the proteasome hu.MAP complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). Its HPA profile is broadly expressed with kidney protein detection, and its extensive literature and disease associations provide substantial external support.
- **Conclusion**: Established evidence supports PSMC2 as a central proteasome regulatory-particle component and a strong marker of the module's principal function. It is plausible, but not established here, that PSMC2 helps couple proteasome activity to oxidative-stress or remodeling states shared by bone and kidney.

#### PSMC4

- **Related proteins** (co-abundance neighbors): PSMC2 (0.91), PSMC6 (0.88), PSMD13 (0.85), PDCD4 (0.82), PPP4C (0.81); STRING partners: PSMC2 (0.999), PSMC6 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 4. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.603); mantle cell lymphoma (0.542); neoplasm (0.519); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1065
- **Why important**: PSMC4 is embedded in the same experimentally supported proteasome subnetwork as PSMC2, PSMC6 and PSMD13. It contributes to all primary proteasome terms (GO:CC proteasome regulatory particle; q_global = 0.00358) (GO:CC proteasome accessory complex; q_global = 0.00358) (GO:MF proteasome-activating activity; q_global = 0.0216), both STRING terms (STRING Component Proteasome regulatory particle; within-query FDR = 0.0242) (STRING COMPARTMENTS Proteasome regulatory particle; within-query FDR = 0.026), and the proteasome hu.MAP complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). It is also a prominent module connector and has kidney protein detection, while its disease associations and literature volume support its biological relevance.
- **Conclusion**: Established evidence identifies PSMC4 as a core ATPase component of the proteasome regulatory particle and one of the most reliable anchors of this module. Its coordinated abundance may report proteasome capacity or demand, but a specific bone-kidney regulatory role remains a hypothesis.

#### PSMC6

- **Related proteins** (co-abundance neighbors): PSMD13 (0.89), PSMC4 (0.88), WDR77 (0.83), COPS3 (0.82), DHX57 (0.82); STRING partners: PSMC2 (0.999), PSMC4 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 6. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.606); mantle cell lymphoma (0.542); neoplasm (0.528); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 748
- **Why important**: PSMC6 is part of the mutually connected proteasome group and is present in all primary proteasome terms (GO:CC proteasome regulatory particle; q_global = 0.00358) (GO:CC proteasome accessory complex; q_global = 0.00358) (GO:MF proteasome-activating activity; q_global = 0.0216), the STRING proteasome results (STRING Component Proteasome regulatory particle; within-query FDR = 0.0242) (STRING COMPARTMENTS Proteasome regulatory particle; within-query FDR = 0.026), and the three proteasome hu.MAP complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). It links the proteasome core to additional module genes, including WDR77, COPS3 and DHX57, and has kidney protein detection. Its annotations include proteasomal degradation, oxidative-stress response and endoplasmic-reticulum-associated degradation.
- **Conclusion**: Established evidence supports PSMC6 as a proteasome ATPase and a biologically meaningful bridge between the module's core and peripheral genes. The possible role of this bridge in coordinating proteostasis with RNA or stress responses is mechanistically attractive but not proven by the present data.

#### PSMD13

- **Related proteins** (co-abundance neighbors): PSMC6 (0.89), PSMC4 (0.85), AIMP2 (0.80); STRING partners: EIF3F (0.705), PSMC2 (0.999), PSMC4 (0.999), PSMC6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 is the non-ATPase member of the central proteasome group and is included in the regulatory-particle and accessory-complex enrichments (GO:CC proteasome regulatory particle; q_global = 0.00358) (GO:CC proteasome accessory complex; q_global = 0.00358), as well as the STRING terms (STRING Component Proteasome regulatory particle; within-query FDR = 0.0242) (STRING COMPARTMENTS Proteasome regulatory particle; within-query FDR = 0.026) and proteasome hu.MAP complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). It is connected to PSMC2, PSMC4 and PSMC6 in STRING and also links to EIF3F and AIMP2 in the module network. Its kidney detection, proteasome annotations and disease associations reinforce its importance despite a less dominant network position than PSMC2.
- **Conclusion**: Established evidence supports PSMD13 as a structural regulatory-particle component that helps define the proteasome identity of the module. Its connections to translation-related and aminoacylation-related genes suggest a possible interface between protein synthesis and degradation, but that interface is a hypothesis rather than a demonstrated module mechanism.

## Module 5

**Tissue pair**: bone and kidney  
**Genes (5)**: AP3B1, BPNT1, PFKM, VAC14, WIPF2

### Function

This is a small, internally connected co-abundance module linking cytoskeletal organization, glycolytic metabolism, phosphoinositide and nucleotide metabolism, and intracellular vesicle trafficking. The network is centered on WIPF2, with PFKM, BPNT1, AP3B1, and VAC14 connected to it, but the structure does not establish direct physical binding. No GO or KEGG term passed global multiple-testing correction; therefore, no pathway-level enrichment can be claimed. The individual gene annotations instead support a tentative interpretation involving coordinated regulation of cellular energetics, membrane trafficking, organelle function, and actin-dependent processes. The functional interpretation remains provisional because the module lacks externally supported interaction or complex evidence.

**Cell composition.** The module does not resemble a plasma-protein or secreted-protein module: none of its genes are annotated as secreted. All module proteins were detected by immunohistochemistry in kidney, while bone protein data were unavailable in the stated HPA evidence. Most genes have low tissue specificity, and the single group-enriched pattern is skeletal muscle and tongue for PFKM. Cell-type-enhanced or cell-type-enriched signals are diverse, including neutrophils, cardiomyocytes, spermatogenic cells, intestinal epithelial cells, somatotrophs, and glial or muscle-related cells. All genes have low immune-cell specificity and there is no enriched blood-cell pattern, arguing against a specifically blood-cell-driven module. Nevertheless, the broad expression and kidney detection mean that shared cell composition, a general renal cellular program, or sampling-related co-abundance could contribute to the bone–kidney association.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair met the stated high-confidence STRING interaction threshold, and there were no STRING functional-enrichment terms. No hu.MAP complex contained multiple module members. Thus, the observed co-abundance edges are not corroborated by the supplied high-confidence protein-interaction or complex resources. WIPF2 is the network hub by connectivity, but its hub position should be interpreted as a property of this co-abundance dataset rather than evidence that it physically binds each neighbor. The annotations nevertheless provide biologically plausible but heterogeneous links: PFKM supports glycolysis, BPNT1 supports phosphoinositide and nucleotide-related metabolism, AP3B1 supports vesicle and lysosome-associated trafficking, VAC14 supports the PIKfyve phosphoinositide complex, and WIPF2 supports WASP-related actin organization.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact co-abundance module appears potentially novel as a tissue-pair association because its member combination is absent from the supplied high-confidence STRING and hu.MAP evidence. That absence does not prove biological novelty: the genes are individually well studied, and several have established roles in metabolism, vesicle trafficking, phosphoinositide signaling, or cytoskeletal regulation. The module may therefore represent a new cross-tissue co-expression observation rather than a newly discovered molecular complex or pathway. Independent cohorts, cell-type-resolved data, and experimental testing would be required to establish reproducibility and biological specificity.

**Hypothesis.** Hypothesis: in a shared bone–kidney cellular context, variation in cellular energetic demand may be coordinated with membrane remodeling and intracellular trafficking. PFKM could represent the glycolytic-energy component; WIPF2 could connect actin organization to receptor or membrane responses; AP3B1 could support trafficking of lysosomal or other specialized vesicular cargo; VAC14 could regulate the phosphoinositide membrane system; and BPNT1 could link inositol or nucleotide metabolism to signaling. The module may therefore reflect a coordinated cell-state program involving energy supply, actin-dependent membrane handling, vesicle distribution, and phosphoinositide homeostasis. This is a hypothesis generated from the gene annotations and co-abundance topology, not an established mechanism.

### Important genes

#### WIPF2

- **Related proteins** (co-abundance neighbors): PFKM (0.87), BPNT1 (0.87), AP3B1 (0.84), VAC14 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WAS/WASL interacting protein family member 2. This gene encodes a WASP interacting protein (WIP)-related protein. It has been shown that this protein has a role in the WASP-mediated organization of the actin cytoskeleton and that this protein is a potential link between the activated platelet-derived growth factor receptor and the actin polymerization machinery. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.438); Parkinson disease (0.353); lysosomal storage disease (0.352); Alzheimer disease (0.352); exostosis (0.084)
- **Europe PMC papers**: 183
- **Why important**: WIPF2 is the network hub, connected to every other module member, making it the strongest topological candidate for organizing the observed co-abundance pattern. Its established annotation links it to WASP-mediated actin-cytoskeleton organization and to signaling from activated platelet-derived growth factor receptors toward actin polymerization. It has kidney protein detection, low tissue specificity, low immune-cell specificity, and the smallest literature volume among the module genes, so the network prominence may provide a useful route to investigating a less extensively characterized component.
- **Conclusion**: Established evidence supports a role for WIPF2 in actin-associated signaling and organization. Its central position supports prioritizing it as a module marker, but does not establish that WIPF2 mechanistically controls the other genes. A role as the physical or regulatory bridge between the module processes remains a hypothesis.

#### PFKM

- **Related proteins** (co-abundance neighbors): WIPF2 (0.87); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphofructokinase, muscle. Three phosphofructokinase isozymes exist in humans: muscle, liver and platelet. These isozymes function as subunits of the mammalian tetramer phosphofructokinase, which catalyzes the phosphorylation of fructose-6-phosphate to fructose-1,6-bisphosphate. Tetramer composition varies depending on tissue type. This gene encodes the muscle-type isozyme. Mutations in this gene have been associated with g…
- **Diseases (Open Targets)**: glycogen storage disease VII (0.819); disorder of glycogen metabolism (0.372); peroxisome biogenesis disorder (0.333); neurodegenerative disease (0.319); anemia (phenotype) (0.288)
- **Europe PMC papers**: 2506
- **Why important**: PFKM is the clearest metabolic anchor. It encodes the muscle-type phosphofructokinase isozyme, a catalytic component of glycolysis, and is associated with Tarui disease and glycogen metabolism disorders. It is the only group-enriched gene in the module, with enrichment in skeletal muscle and tongue, and it has the deepest literature coverage among these genes. Its direct co-abundance link to WIPF2 connects the metabolic interpretation to the module hub.
- **Conclusion**: Established evidence supports PFKM as a glycolytic and tissue-context marker. Its association with the other module genes could reflect coordinated energetic demand or cell composition, but the data do not prove that glycolysis drives the module or that PFKM regulates vesicle, phosphoinositide, or actin biology.

#### AP3B1

- **Related proteins** (co-abundance neighbors): WIPF2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor related protein complex 3 subunit beta 1. This gene encodes a protein that may play a role in organelle biogenesis associated with melanosomes, platelet dense granules, and lysosomes. The encoded protein is part of the heterotetrameric AP-3 protein complex which interacts with the scaffolding protein clathrin. Mutations in this gene are associated with Hermansky-Pudlak syndrome type 2. Two transcript variants encoding different isoforms h…
- **Diseases (Open Targets)**: Hermansky-Pudlak syndrome 2 (0.837); Hermansky-Pudlak syndrome (0.752); cancer (0.546); Parkinson disease (0.470); neurodegenerative disease (0.452)
- **Europe PMC papers**: 1324
- **Why important**: AP3B1 encodes a subunit of the AP complex involved in intracellular vesicle transport and organelle biogenesis, including lysosome-related organelles and platelet dense granules. It is associated with Hermansky–Pudlak syndrome type two and has substantial literature support. Its vesicular localization and kidney detection provide a coherent trafficking-related context, while its connection to WIPF2 places vesicle biology beside actin organization in the module.
- **Conclusion**: Established evidence supports AP3B1 as a vesicle-trafficking and organelle-biogenesis gene with disease relevance. Its participation in this module may indicate coordinated intracellular transport, but no supplied evidence demonstrates a direct AP3B1–WIPF2 interaction or a shared AP complex containing the other module members.

#### VAC14

- **Related proteins** (co-abundance neighbors): WIPF2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VAC14 component of PIKFYVE complex. This gene encodes a scaffold protein that is a component of the PIKfyve protein kinase complex. This complex is responsible for the synthesis of phosphatidylinositol 3,5-bisphosphate, an important component of cellular membranes, from phosphatidylinositol 3-phosphate. Mice lacking a functional copy of this gene exhibit severe neurodegeneration. Mutations in the human gene have been identified in p…
- **Diseases (Open Targets)**: striatonigral degeneration, childhood-onset (0.737); Yunis-Varon syndrome (0.406); hereditary disease (0.341); exocrine pancreatic carcinoma (0.228); skull disorder (0.187)
- **Europe PMC papers**: 664
- **Why important**: VAC14 is a scaffold component of the PIKfyve complex, which regulates phosphatidylinositol three-phosphate and phosphatidylinositol three-five-bisphosphate metabolism on cellular membranes. It is associated with severe neurodegenerative and developmental disease when disrupted, and its vesicular localization is consistent with membrane-trafficking biology. Its connection to WIPF2 gives the module a plausible membrane-signaling and cytoskeletal dimension.
- **Conclusion**: Established evidence supports VAC14 as a regulator of phosphoinositide-dependent membrane homeostasis and a disease-relevant scaffold. Its inclusion makes membrane signaling a credible part of the module interpretation, but the co-abundance data do not establish that VAC14 coordinates glycolysis or AP3B1-dependent trafficking in bone or kidney.

#### BPNT1

- **Related proteins** (co-abundance neighbors): WIPF2 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3'(2'), 5'-bisphosphate nucleotidase 1. BPNT1, also called bisphosphate 3-prime-nucleotidase, or BPntase, is a member of a magnesium-dependent phosphomonoesterase family. Lithium, a major drug used to treat manic depression, acts as an uncompetitive inhibitor of BPntase. The predicted human protein is 92% identical to mouse BPntase. BPntase's physiologic role in nucleotide metabolism may be regulated by inositol signaling pathways. The …
- **Diseases (Open Targets)**: cataract-growth hormone deficiency-sensory neuropathy-sensorineural hearing loss-skeletal dysplasia syndrome (0.480); Leigh syndrome (0.333); hypercholesterolemia, familial, 1 (0.333); neurodegenerative disease (0.290); polyneuropathy (0.235)
- **Europe PMC papers**: 248
- **Why important**: BPNT1 encodes a magnesium-dependent bisphosphate phosphatase involved in nucleotide-related and inositol-linked metabolism. The supplied annotation also notes that lithium inhibits BPntase and that inhibition may contribute to lithium-associated nephrotoxicity, giving this gene particular kidney relevance. It is connected to WIPF2 and has kidney protein detection, while its nuclear-speckle localization broadens the module beyond purely vesicular processes.
- **Conclusion**: Established evidence supports BPNT1 in phosphatase activity, nucleotide metabolism, and inositol signaling, with a plausible connection to renal drug toxicity. Its module association may indicate coordinated signaling or metabolic state, but the data do not show that BPNT1 mediates the bone–kidney relationship or directly interacts with WIPF2.

## Module 6

**Tissue pair**: bone and kidney  
**Genes (12)**: AP3D1, AP3S1, CARM1, CPNE1, CYFIP1, DNM2, EML4, GMPPB, LYPLA2, PDXP, TIPRL, TTLL12

### Function

The strongest interpretation is intracellular vesicle trafficking, especially AP-3-associated vesicle budding, coating, localization, and transport. This conclusion is supported by the globally corrected GO terms (5 globally significant GO/KEGG terms, q_global 0.00191–0.0454; see the table), all driven by AP3D1 and AP3S1, with DNM2 additionally contributing to the budding, transport, and localization terms. AP3D1 and AP3S1 are components of the AP-3 adaptor complex, while DNM2 is involved in membrane remodeling, endocytosis, and post-Golgi vesicle trafficking. The remaining genes suggest associated regulation of cytoskeletal dynamics, membrane processes, protein modification, glycoprotein synthesis, and intracellular signaling, but these are supporting biological context rather than globally significant enrichment. The module therefore appears more consistent with a vesicle-trafficking and membrane-organization program than with a bone- or kidney-specific biochemical pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the encoded proteins are predominantly intracellular. It is also not strongly characterized as a blood-cell module. Most genes have low tissue specificity and low immune-cell specificity, although several show cell-type-enhanced patterns involving esophageal cells, trophoblasts, neutrophils, neutrophil progenitors, and other immune-related populations. CYFIP1 is enriched in microglia and several monocyte or myeloid-cell categories, while PDXP is enriched in brain neuronal categories and a dendritic-cell category. The broad expression pattern and the lack of a coherent bone- or kidney-specific HPA signature suggest that the shared module is unlikely to represent a specialized bone or kidney program solely on the available evidence. It could instead reflect a broadly used intracellular trafficking program, with possible contribution from shared or variable cell populations in the samples. Kidney protein detection is common across the module, but the supplied HPA evidence does not establish kidney specificity; bone protein comparison is unavailable.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP synaptic vesicle budding from presynaptic endocytic zone membrane | 0.00191 | AP3D1, AP3S1, DNM2 |
| GO:BP synaptic vesicle budding | 0.00191 | AP3D1, AP3S1, DNM2 |
| GO:BP synaptic vesicle transport | 0.0281 | AP3D1, AP3S1, DNM2 |
| GO:BP synaptic vesicle localization | 0.036 | AP3D1, AP3S1, DNM2 |
| GO:BP synaptic vesicle coating | 0.0454 | AP3D1, AP3S1 |

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module: AP3D1–AP3S1. This is concordant with the globally significant AP-3 and synaptic-vesicle-related annotations and supports a real physical or functional association between these two subunits. STRING functional enrichment is absent, so no broader STRING enrichment claim is justified. hu.MAP repeatedly places AP3D1 and AP3S1 together in complexes (hu.MAP huMAP3_06230.1) (hu.MAP huMAP3_03536.1) (hu.MAP huMAP3_04238.1) (hu.MAP huMAP3_03149.1) (hu.MAP huMAP3_12325.1) (hu.MAP huMAP3_12813.1) (hu.MAP huMAP3_15082.1) (hu.MAP huMAP3_12157.1). These complexes contain additional AP-3 subunits, including AP3B1, AP3B2, AP3M1, AP3M2, AP3S2, and in some cases RNF167, EPB41L3, NAF1, or TMEM63A. The repeated co-occurrence of AP3D1 and AP3S1 supports their interpretation as a captured fragment of AP-3-related complexes, but the module does not contain the other complex members and the hu.MAP evidence does not demonstrate that all twelve module genes form one physical complex. The weak connectivity outside AP3D1–AP3S1 indicates that the module is a co-abundance structure with limited direct interaction support rather than a densely documented protein complex.

**STRING interactions (score >= 0.7)**: 1 of 66 gene pairs: AP3D1–AP3S1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06230.1 (AP3D1, AP3S1; 2/4); huMAP3_03536.1 (AP3D1, AP3S1; 2/5); huMAP3_04238.1 (AP3D1, AP3S1; 2/6); huMAP3_03149.1 (AP3D1, AP3S1; 2/7); huMAP3_12325.1 (AP3D1, AP3S1; 2/8); huMAP3_12813.1 (AP3D1, AP3S1; 2/9); huMAP3_15082.1 (AP3D1, AP3S1; 2/9); huMAP3_12157.1 (AP3D1, AP3S1; 2/10)

### Novelty

This module should not be called a wholly new molecular mechanism. The AP3D1–AP3S1 relationship, AP-3 complex membership, and vesicle-trafficking functions are established by STRING, hu.MAP, and gene annotations. The globally significant enrichment is also driven by a small AP-3 and dynamin-related subset rather than by the entire module. However, the particular conserved co-abundance pattern across bone and kidney may still be a potentially novel systems-level observation, because the supplied evidence documents a tissue-pair module rather than an already established bone–kidney module. Novelty would require comparison with published co-expression or proteomic modules and independent replication. Absence of additional STRING edges or hu.MAP complexes is not evidence of novelty; it more conservatively indicates that much of the module's co-abundance structure is not explained by currently catalogued physical interactions.

**Hypothesis.** Hypothesis: the conserved bone–kidney module reflects coordinated activity of a broadly expressed intracellular trafficking and membrane-remodeling program. AP3D1 and AP3S1 may provide an AP-3 adaptor core for vesicle budding and cargo sorting, with DNM2 contributing membrane fission or endocytic remodeling. CYFIP1, CPNE1, and possibly the cytoskeletal proteins may couple trafficking to actin organization or membrane dynamics, while TIPRL, CARM1, TTLL12, PDXP, LYPLA2, and GMPPB could modulate signaling, protein or cytoskeletal state, lipid handling, or glycoprotein-related processes. In bone, such a program could be relevant to vesicle-dependent functions including osteoclast membrane activity, whereas in kidney it may support general epithelial or intracellular trafficking. This is a mechanistic model, not an established tissue-specific pathway, and it should be tested by cell-type-resolved measurements, perturbation of AP3D1 or AP3S1, and examination of vesicle trafficking and membrane-remodeling phenotypes.

### Important genes

#### AP3D1

- **Related proteins** (co-abundance neighbors): TIPRL (0.85), CARM1 (0.80); STRING partners: AP3S1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06230.1, huMAP3_03536.1, huMAP3_04238.1, huMAP3_03149.1, huMAP3_12325.1, huMAP3_12813.1, huMAP3_15082.1, huMAP3_12157.1
- **Function (MyGene.info)**: adaptor related protein complex 3 subunit delta 1. The protein encoded by this gene is a subunit of the AP3 adaptor-like complex, which is not clathrin-associated, but is associated with the golgi region, as well as more peripheral structures. The AP-3 complex facilitates the budding of vesicles from the golgi membrane, and may be directly involved in trafficking to lysosomes. This subunit is implicated in intracellular biogenesis and trafficking …
- **Diseases (Open Targets)**: Hermansky-Pudlak syndrome 10 (0.584); Hermansky-Pudlak syndrome 2 (0.455); Hermansky-Pudlak syndrome (0.432); Alzheimer disease (0.421); lysosomal storage disease (0.417)
- **Europe PMC papers**: 637
- **Why important**: AP3D1 is a central interpretive gene because it participates in every globally significant GO term (5 globally significant GO/KEGG terms, q_global 0.00191–0.0454; see the table), has direct high-confidence STRING support with AP3S1, and appears in every listed hu.MAP complex (hu.MAP huMAP3_06230.1) (hu.MAP huMAP3_03536.1) (hu.MAP huMAP3_04238.1) (hu.MAP huMAP3_03149.1) (hu.MAP huMAP3_12325.1) (hu.MAP huMAP3_12813.1) (hu.MAP huMAP3_15082.1) (hu.MAP huMAP3_12157.1). Its annotation directly links it to AP-3 vesicle coating, intracellular transport, lysosomal transport, Golgi-to-vacuole transport, and anterograde axonal transport. It also has disease associations involving Hermansky–Pudlak syndrome and lysosomal storage disease, providing a clinically relevant connection to organelle trafficking. Its literature base is substantial enough to support established functional interpretation without relying on the module alone.
- **Conclusion**: Established evidence supports AP3D1 as a core AP-3 vesicle-trafficking component and the strongest functional anchor of the module. It is reasonable to hypothesize that AP3D1 helps generate the shared co-abundance signal, but the data do not establish that it controls the other module genes or that the module is specifically responsible for a bone or kidney phenotype.

#### AP3S1

- **Related proteins** (co-abundance neighbors): TIPRL (0.81); STRING partners: AP3D1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_06230.1, huMAP3_03536.1, huMAP3_04238.1, huMAP3_03149.1, huMAP3_12325.1, huMAP3_12813.1, huMAP3_15082.1, huMAP3_12157.1
- **Function (MyGene.info)**: adaptor related protein complex 3 subunit sigma 1. This gene encodes a subunit of the AP3 adaptor complex. This complex functions in the formation of subcellular vesicles budded from the Golgi body. Several related pseudogenes of this gene have been found. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.565); lysosomal storage disease (0.370); alcohol drinking (0.205); frozen shoulder (0.199); spondylolisthesis (0.193)
- **Europe PMC papers**: 316
- **Why important**: AP3S1 is the partner of AP3D1 in the only high-confidence STRING interaction and is present with AP3D1 in every listed hu.MAP complex (hu.MAP huMAP3_06230.1) (hu.MAP huMAP3_03536.1) (hu.MAP huMAP3_04238.1) (hu.MAP huMAP3_03149.1) (hu.MAP huMAP3_12325.1) (hu.MAP huMAP3_12813.1) (hu.MAP huMAP3_15082.1) (hu.MAP huMAP3_12157.1). It contributes to all globally significant terms (5 globally significant GO/KEGG terms, q_global 0.00191–0.0454; see the table), including synaptic vesicle budding, transport, localization, and coating. Its annotation independently identifies it as an AP-3 subunit involved in Golgi-derived vesicle formation and intracellular protein transport. Its disease associations include neurodegenerative and lysosomal-storage categories.
- **Conclusion**: Established evidence supports AP3S1 as a second core AP-3 component and strongly reinforces the vesicle-trafficking interpretation. The module supports coordinated abundance of AP3S1 with AP3D1, but it does not show that AP3S1 is a tissue-specific driver in bone or kidney.

#### DNM2

- **Related proteins** (co-abundance neighbors): CYFIP1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 2. Dynamins represent one of the subfamilies of GTP-binding proteins. These proteins share considerable sequence similarity over the N-terminal portion of the molecule, which contains the GTPase domain. Dynamins are associated with microtubules. They have been implicated in cell processes such as endocytosis and cell motility, and in alterations of the membrane that accompany certain activities such …
- **Diseases (Open Targets)**: autosomal dominant centronuclear myopathy (0.844); Charcot-Marie-Tooth disease dominant intermediate B (0.830); fetal akinesia-cerebral and retinal hemorrhage syndrome (0.739); autosomal dominant Charcot-Marie-Tooth disease type 2M (0.715); centronuclear myopathy (0.692)
- **Europe PMC papers**: 2412
- **Why important**: DNM2 contributes to the globally significant budding, transport, and localization terms (4 globally significant GO/KEGG terms, q_global 0.00191–0.036; see the table). Its established functions include GTPase-dependent membrane remodeling, endocytosis, receptor-mediated endocytosis, autophagy, and post-Golgi vesicle trafficking. Its annotation specifically notes roles in membrane alterations accompanying bone resorption by osteoclasts, making it particularly relevant to the bone side of the tissue pair. It also has strong disease associations with centronuclear myopathy and Charcot–Marie–Tooth disease, alongside a substantial literature base.
- **Conclusion**: Established evidence supports DNM2 as a membrane-remodeling and endocytic component that plausibly complements AP-3 cargo sorting. Its possible contribution to a shared bone–kidney module is a hypothesis; the supplied network gives it only a single module connection and does not establish a direct AP3D1–DNM2 or AP3S1–DNM2 interaction.

#### CYFIP1

- **Related proteins** (co-abundance neighbors): CARM1 (0.81), DNM2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Group enriched; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytoplasmic FMR1 interacting protein 1. This gene encodes a protein that regulates cytoskeletal dynamics and protein translation. The encoded protein is a component of the WAVE regulatory complex (WRC), which promotes actin polymerization. This protein also interacts with the synaptic functional regulator FMR1 protein and translation initiation factor 4E to inhibit protein translation. A large chromosomal deletion including this gene is…
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); lymphatic system disorder (0.336); vein disorder (0.336); Varicose veins (0.305); autism (0.154)
- **Europe PMC papers**: 1698
- **Why important**: CYFIP1 connects the module to actin and cytoskeletal regulation. It is linked to CARM1 and DNM2 in the module, is a component of the WAVE regulatory complex, and promotes actin polymerization while also influencing translation. HPA identifies microglial enrichment and enrichment across several monocyte or myeloid-cell categories, which is relevant when considering cellular composition as an alternative explanation for a shared tissue signal. Its disease associations include neurodegenerative disease and autism, and it has a substantial literature base.
- **Conclusion**: Established evidence supports CYFIP1 as a cytoskeletal and translational regulator that could provide a cellular context for membrane trafficking. The proposed connection between CYFIP1-driven actin organization and AP-3 or DNM2 activity in this module remains a hypothesis, not a demonstrated molecular relationship.

#### CARM1

- **Related proteins** (co-abundance neighbors): CPNE1 (0.82), TTLL12 (0.82), CYFIP1 (0.81), AP3D1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coactivator associated arginine methyltransferase 1. This gene belongs to the protein arginine methyltransferase (PRMT) family. The encoded enzyme catalyzes the methylation of guanidino nitrogens of arginyl residues of proteins. The enzyme acts specifically on histones and other chromatin-associated proteins and is involved in regulation of gene expression. The enzyme may act in association with other proteins or within multi-protein complexes and m…
- **Diseases (Open Targets)**: neurodegenerative disease (0.491); lysosomal storage disease (0.258); mucositis (0.183); oral mucositis (0.183); hypothyroidism (0.160)
- **Europe PMC papers**: 3438
- **Why important**: CARM1 has the highest network connectivity in the supplied subgraph and links CPNE1, TTLL12, CYFIP1, and AP3D1. It is a protein arginine methyltransferase involved in methylation of histones and other chromatin-associated proteins, transcriptional regulation, and cell-lineage functions. HPA indicates tissue enhancement in skeletal muscle and kidney protein detection. It also has disease associations involving neurodegenerative disease and lysosomal storage disease, with a large literature base.
- **Conclusion**: Established evidence supports CARM1 as a chromatin and transcriptional regulator and as the most connected network node in this module. Its relationship to the vesicle-trafficking signal is not established by GO enrichment, STRING, or hu.MAP here. A reasonable hypothesis is that CARM1 links cell-state or transcriptional regulation to trafficking machinery, but this requires direct testing.

#### GMPPB

- **Related proteins** (co-abundance neighbors): PDXP (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GDP-mannose pyrophosphorylase B. This gene is thought to encode a GDP-mannose pyrophosphorylase. The encoded protein catalyzes the conversion of mannose-1-phosphate and GTP to GDP-mannose, a reaction involved in the production of N-linked oligosaccharides. Alternatively spliced transcript variants encoding distinct isoforms have been described. [provided by RefSeq, Jan 2009].
- **Diseases (Open Targets)**: autosomal recessive limb-girdle muscular dystrophy type 2T (0.833); muscular dystrophy-dystroglycanopathy (congenital with brain and eye anomalies), type A14 (0.800); muscular dystrophy-dystroglycanopathy (congenital with intellectual disability), type B14 (0.791); muscle-eye-brain disease (0.634); congenital muscular dystrophy with cerebellar involvement (0.619)
- **Europe PMC papers**: 773
- **Why important**: GMPPB adds a biochemical and disease-relevant dimension through GDP-mannose production for N-linked glycoprotein biosynthesis. It is connected to PDXP in the module and shows cell-type enhancement in several epithelial, trophoblast, and plasma-cell categories. Its disease associations include limb-girdle muscular dystrophy and dystroglycanopathy categories, making it relevant to glycoprotein-dependent membrane and organelle biology.
- **Conclusion**: Established evidence supports GMPPB as a GDP-mannose biosynthetic enzyme with consequences for glycoprotein production. Its role in this module is not supported by a globally significant enrichment term or a documented STRING or hu.MAP relationship. Its possible contribution to trafficking through glycoprotein availability is therefore a hypothesis rather than a demonstrated mechanism.

## Module 7

**Tissue pair**: bone and kidney  
**Genes (9)**: ARPC1B, ACOT7, IFT25, MAT2A, NUDT5, OLA1, PAFAH1B3, PPME1, NANS

### Function

This is a sparse and biologically heterogeneous co-abundance module rather than a clearly established pathway. No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for this module. There was also no supplementary STRING functional enrichment. The strongest interpretive signal comes from the individual gene functions and the network topology: NUDT5 is the central connector and supports nucleotide and ADP-ribose metabolism; OLA1 is an ATPase linked to centrosome regulation; MAT2A produces the methyl donor S-adenosylmethionine; NANS supports sialic-acid biosynthesis; ACOT7 participates in long-chain fatty-acid metabolism; ARPC1B supports Arp2/3-dependent actin nucleation; and IFT25 is associated with cilium biology, kidney development, and skeletal-system development. Taken together, the module may reflect coordinated intracellular metabolic, structural, and organelle-maintenance states, but the evidence does not justify assigning it a single canonical function.

**Cell composition.** The module contains no secreted genes, so it does not resemble a plasma-protein or secreted-protein module. Most genes have low tissue specificity, and kidney protein detection is reported for nearly all genes with available kidney data, supporting a broadly expressed intracellular component. Most genes have cell-type-enhanced rather than strongly tissue-specific HPA profiles, with signals spanning Hofbauer cells, neutrophils, goblet cells, ciliated cells, smooth-muscle cells, and several other cell types. Only ACOT7 has a blood-cell group-enriched profile, while the module overall has low immune-cell specificity. Thus, the shared bone–kidney pattern is not obviously explained by a blood-cell or plasma-protein signature, although shared cell composition, ubiquitous intracellular expression, or common tissue-state effects remain plausible explanations.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair met the specified high-confidence STRING interaction threshold, and there was no STRING functional enrichment. No hu.MAP complex contained multiple module members. Therefore, the co-abundance relationships are not supported here by a previously catalogued high-confidence physical interaction network or shared hu.MAP complex. The absence of such evidence does not mean the proteins cannot interact indirectly or participate in related cellular states; it means that this module is not independently validated as a known physical complex by the supplied resources.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a new tissue-pair co-abundance pattern, but it cannot be called a newly discovered molecular pathway. Its novelty is supported only in the limited sense that the supplied STRING and hu.MAP resources do not show an established shared interaction or complex among its members. Because the genes are individually well characterized, broadly expressed, and functionally diverse, the absence of database support could reflect a regulatory or cell-state association, incomplete interaction coverage, or a statistical co-abundance pattern rather than a novel biochemical assembly. Independent replication, preservation in additional cohorts, cell-composition adjustment, and experimental testing would be required before claiming biological novelty.

**Hypothesis.** Hypothesis: the module captures a shared intracellular maintenance state present in bone and kidney, in which nucleotide and ADP-ribose handling through NUDT5, ATP and methyl-donor metabolism through OLA1 and MAT2A, sialic-acid production through NANS, lipid remodeling through ACOT7, actin organization through ARPC1B, and ciliary or developmental functions through IFT25 vary together. This could reflect coordinated demands of metabolically active or structurally remodeling cells rather than direct physical binding among the proteins. The hypothesis predicts that module activity should associate with measures of cellular metabolic state, cytoskeletal remodeling, ciliary function, or tissue repair, while remaining sensitive to cell-type composition.

### Important genes

#### NUDT5

- **Related proteins** (co-abundance neighbors): IFT25 (0.91), OLA1 (0.85), PAFAH1B3 (0.81), MAT2A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nudix hydrolase 5. This gene belongs to the Nudix (nucleoside diphosphate linked moiety X) hydrolase superfamily. The encoded enzyme catalyzes the hydrolysis of modified nucleoside diphosphates, including ADP-ribose (ADPR) and 8-oxoGua-containing 8-oxo-dADP and 8-oxo-dGDP. Protein-bound ADP ribose can be hazardous to the cell because it can modify some amino acid residues, resulting in the inhibition of ATP-activate…
- **Diseases (Open Targets)**: neurodegenerative disease (0.513); type 2 diabetes mellitus (0.332); coronary artery disorder (0.324); gout (0.315); diabetic neuropathy (0.315)
- **Europe PMC papers**: 847
- **Why important**: NUDT5 is the principal network connector, linking IFT25, OLA1, PAFAH1B3, and MAT2A. Its established enzymatic role in hydrolyzing modified nucleoside diphosphates, including ADP-ribose and oxidized guanine-containing nucleotides, gives the module a plausible nucleotide-quality-control and metabolic axis. It has a substantial literature base and disease associations spanning neurodegenerative disease, diabetes, coronary disease, gout, and diabetic neuropathy.
- **Conclusion**: Established evidence supports NUDT5 as the most influential network-organizing gene and as a nucleotide and ADP-ribose hydrolase. It is reasonable to regard NUDT5 as a candidate driver or marker of the module. It remains hypothetical that its enzymatic activity mechanistically coordinates the other module members in bone or kidney.

#### MAT2A

- **Related proteins** (co-abundance neighbors): NANS (0.83), NUDT5 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionine adenosyltransferase 2A. The protein encoded by this gene catalyzes the production of S-adenosylmethionine (AdoMet) from methionine and ATP. AdoMet is the key methyl donor in cellular processes. [provided by RefSeq, Jun 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.545); familial thoracic aortic aneurysm and aortic dissection (0.416); autoimmune disorder of central nervous system (0.340); prostate carcinoma (0.252); Abnormality of the cardiovascular system (0.192)
- **Europe PMC papers**: 2615
- **Why important**: MAT2A connects to NUDT5 and NANS and encodes the enzyme that produces S-adenosylmethionine, a central methyl donor. Its annotations include methyl-donor biosynthesis, protein oligomerization, methionine response, and positive regulation of TORC1 signaling. It is tissue-enhanced in pancreas but detected in kidney, has a large literature base, and carries disease associations involving neurodegeneration, vascular disease, autoimmunity, and cancer.
- **Conclusion**: Established evidence supports MAT2A as a central metabolic regulator with potential relevance to methylation and growth signaling. Its position at the junction with NUDT5 and NANS makes it an important interpretive anchor. A bone–kidney-specific role or direct coordination with the other module proteins remains a hypothesis.

#### ARPC1B

- **Related proteins** (co-abundance neighbors): OLA1 (0.83), PPME1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: actin related protein 2/3 complex subunit 1B. This gene encodes one of seven subunits of the human Arp2/3 protein complex. This subunit is a member of the SOP2 family of proteins and is most similar to the protein encoded by gene ARPC1A. The similarity between these two proteins suggests that they both may function as p41 subunit of the human Arp2/3 complex that has been implicated in the control of actin polymerization in cells. It is possib…
- **Diseases (Open Targets)**: platelet abnormalities with eosinophilia and immune-mediated inflammatory disease (0.771); combined immunodeficiency (0.429); autoimmune disorder of central nervous system (0.397); cutaneous leishmaniasis (0.370); immunodeficiency disease (0.346)
- **Europe PMC papers**: 1334
- **Why important**: ARPC1B is connected to OLA1 and PPME1 and encodes a subunit of the Arp2/3 complex, which controls actin polymerization. Its HPA profile includes lymphoid tissue enhancement and several immune or myeloid-associated cell types, while its disease associations include immunodeficiency and inflammatory disorders. Its literature base is substantial relative to most members.
- **Conclusion**: Established evidence supports ARPC1B as a structural cytoskeletal and immune-cell-relevant component. It may indicate actin remodeling or cell-state composition within the module. It is not established that ARPC1B forms a physical complex with the other module members in this tissue pair, and an immune explanation should not be overinterpreted because overall immune-cell specificity is low.

#### IFT25

- **Related proteins** (co-abundance neighbors): NUDT5 (0.91); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece, Principal piece, End piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: intraflagellar transport 25. Predicted to enable metal ion binding activity. Predicted to be involved in kidney development and spermatogenesis. Predicted to act upstream of or within animal organ development; left/right axis specification; and skeletal system development. Predicted to be located in ciliary tip. Predicted to be part of intraciliary transport particle B. Predicted to be active in centrosome and cilium. [provid…
- **Diseases (Open Targets)**: Hashimoto thyroiditis (0.236); hypothyroidism (0.224); renal agenesis (0.111); hepatocellular carcinoma (0.076); Heterotaxia (0.069)
- **Europe PMC papers**: 266
- **Why important**: IFT25 is the terminal partner of NUDT5 in the module and is annotated for intraciliary transport, cilium assembly, kidney development, skeletal-system development, and left–right axis specification. Its cell-type profile is enhanced in several ciliated cell populations, and its disease associations include renal developmental abnormalities and heterotaxy. Although its literature base is smaller than that of the major metabolic genes, its direct relevance to kidney and skeletal biology makes it especially informative.
- **Conclusion**: Established evidence supports IFT25 as a ciliary and developmental gene with direct conceptual relevance to the bone–kidney tissue pair. Its connection to NUDT5 provides a plausible bridge between organelle biology and nucleotide metabolism. The proposed role of IFT25 as a functional mediator of the whole module is hypothesis rather than established evidence.

#### NANS

- **Related proteins** (co-abundance neighbors): MAT2A (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-acetylneuraminate synthase. This gene encodes an enzyme that functions in the biosynthetic pathways of sialic acids. In vitro, the encoded protein uses N-acetylmannosamine 6-phosphate and mannose 6-phosphate as substrates to generate phosphorylated forms of N-acetylneuraminic acid (Neu5Ac) and 2-keto-3-deoxy-D-glycero-D-galacto-nononic acid (KDN), respectively; however, it exhibits much higher activity toward the Neu5Ac phos…
- **Diseases (Open Targets)**: spondyloepimetaphyseal dysplasia, Genevieve type (0.799); neurodegenerative disease (0.501); hereditary disease (0.192); neoplasm (0.067); mental disorder (0.056)
- **Europe PMC papers**: 2339
- **Why important**: NANS is connected to MAT2A and encodes an enzyme in sialic-acid biosynthesis, including production of phosphorylated N-acetylneuraminic-acid intermediates. It has a substantial literature base and a strong disease association with spondyloepimetaphyseal dysplasia, making it particularly relevant to skeletal biology. Its goblet-cell-enhanced profile also points to a possible epithelial or glycan-related cell-state contribution.
- **Conclusion**: Established evidence supports NANS as a sialic-acid metabolic enzyme with a clear skeletal disease connection. It may mark altered glycan production or extracellular-interface biology in the shared module. Direct involvement in a coordinated bone–kidney mechanism with MAT2A or the other genes remains unproven.

## Module 8

**Tissue pair**: bone and kidney  
**Genes (10)**: C2orf49, LUC7L, MBD3, NELFE, RAVER1, RBM27, RIOX2, SRP54, TIA1, XRCC1

### Function

The module does not have any GO or KEGG term that passed global correction, so its function cannot be assigned from statistically significant pathway enrichment. Its gene content nevertheless points to a broadly expressed nuclear RNA and genome-maintenance program. TIA1, LUC7L, RAVER1, NELFE and RBM27 support RNA binding, splice-site recognition, mRNA processing, transcriptional pausing and stress-linked RNA regulation; XRCC1 supports base-excision and single-strand-break repair; MBD3 and RIOX2 support chromatin regulation; and SRP54 represents protein targeting to the endoplasmic reticulum. The co-abundance structure therefore suggests coordinated regulation of RNA processing and cellular maintenance, with possible coupling to DNA repair and chromatin state, rather than a confidently defined tissue-specific pathway. The RNA-recognition-motif signal is supplementary STRING evidence only (STRING SMART RNA recognition motif; within-query FDR = 0.0222).

**Cell composition.** The genes are not secreted proteins and are not characterized as plasma proteins. All genes have low tissue specificity in HPA, and most have low immune-cell specificity, arguing against a module dominated by blood cells or a single immune population. Several genes show enhancement in germ-cell or trophoblast-related cell types, and RBM27 is also enhanced in megakaryocyte progenitor populations, but there is no frequent enriched blood-cell category. Kidney protein detection is reported for nearly all genes with available kidney measurements, whereas matching bone protein data are unavailable. Overall, the module is more consistent with broadly expressed intracellular proteins, potentially influenced by shared cell types or general cellular state, than with a bone- or kidney-exclusive program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No pair among the module genes reaches the supplied high-confidence STRING interaction threshold, and no hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not supported here as already established physical protein interactions or as a known multiprotein complex. STRING does provide a supplementary RNA-recognition-motif grouping involving RBM27, NELFE, TIA1 and RAVER1 (STRING SMART RNA recognition motif; within-query FDR = 0.0222). This supports a possible RNA-processing connection, but it is not global enrichment evidence and does not establish direct interactions among those proteins. The module may therefore capture coordinated expression of functionally related nuclear proteins without representing a canonical physical complex.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: SMART RNA recognition motif (FDR = 0.0222, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is plausibly a new co-abundance observation because it links a set of mostly broadly expressed intracellular proteins across bone and kidney without overlap with a supplied high-confidence STRING interaction network or a shared hu.MAP complex. However, the absence of STRING or hu.MAP support alone does not prove biological novelty: the individual genes and several of their functions are already well established, and the observed association could reflect general expression state, cell composition or technical covariance. The strongest novelty claim is consequently the cross-tissue co-abundance pattern and its particular combination of RNA regulation, DNA repair and chromatin-related genes, not discovery of previously unknown gene functions or physical interactions.

**Hypothesis.** Hypothesis: the conserved bone–kidney module represents a broadly expressed intracellular maintenance program in which RNA-binding and RNA-processing factors coordinate transcript handling during cellular stress or changing differentiation state, while XRCC1-linked genome repair and MBD3/RIOX2-linked chromatin regulation help preserve transcriptional and genomic integrity. The apparent association with germ-cell and trophoblast-related cell types may indicate a shared proliferative or differentiation-related state rather than a bone- or kidney-specific mechanism. This hypothesis requires validation with cell-resolved expression, perturbation experiments and independent cohorts, because no GO or KEGG term passed global correction and the supplied interaction resources show no established complex.

### Important genes

#### XRCC1

- **Related proteins** (co-abundance neighbors): LUC7L (0.89), NELFE (0.83), RBM27 (0.83), RIOX2 (0.83), C2orf49 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: X-ray repair cross complementing 1. The protein encoded by this gene is involved in the efficient repair of DNA single-strand breaks formed by exposure to ionizing radiation and alkylating agents. This protein interacts with DNA ligase III, polymerase beta and poly (ADP-ribose) polymerase to participate in the base excision repair pathway. It may play a role in DNA processing during meiogenesis and recombination in germ cells. A rar…
- **Diseases (Open Targets)**: autosomal recessive spinocerebellar ataxia 10 (0.695); laryngeal squamous cell carcinoma (0.477); neurodegenerative disease (0.257); breast cancer (0.116); breast carcinoma (0.113)
- **Europe PMC papers**: 7904
- **Why important**: XRCC1 is the most connected node in the module and links the RNA-associated genes NELFE, RBM27 and RIOX2 with LUC7L and C2orf49. Its established role in single-strand-break repair, base-excision repair and coordination with DNA repair machinery gives it a strong genome-maintenance interpretation. It also has the largest literature footprint in the module and a reported kidney protein signal.
- **Conclusion**: Established evidence supports XRCC1 as the principal network hub and a DNA-repair factor. It is a plausible organizing marker of the module, but it is not established that XRCC1 physically binds the other module proteins or that it causes the cross-tissue co-abundance pattern. A role linking repair state to RNA regulation remains a hypothesis.

#### TIA1

- **Related proteins** (co-abundance neighbors): RAVER1 (0.89), LUC7L (0.87), MBD3 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TIA1 cytotoxic granule associated RNA binding protein. The product encoded by this gene is a member of a RNA-binding protein family and possesses nucleolytic activity against cytotoxic lymphocyte (CTL) target cells. It has been suggested that this protein may be involved in the induction of apoptosis as it preferentially recognizes poly(A) homopolymers and induces DNA fragmentation in CTL targets. The major granule-associated species is a 15-kDa prote…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis 26 with or without frontotemporal dementia (0.663); distal myopathy, Welander type (0.648); Abnormality of the skeletal system (0.530); hereditary disease (0.187); neoplasm (0.114)
- **Europe PMC papers**: 3316
- **Why important**: TIA1 is a central connector within the RNA-associated portion of the module, linking RAVER1, LUC7L and MBD3. It has established functions in alternative splicing regulation, translational repression and cytoplasmic stress-granule assembly, and it contributes to the supplementary STRING RNA-recognition-motif signal (STRING SMART RNA recognition motif; within-query FDR = 0.0222). Its disease associations include amyotrophic lateral sclerosis and distal myopathy, and it has a substantial literature base.
- **Conclusion**: Established evidence supports TIA1 as an RNA-binding and stress-response regulator with relevance to skeletal-system phenotypes. Its position makes it a strong candidate for reflecting post-transcriptional state in the module. Whether TIA1 mediates the relationship between RNA handling and DNA repair in bone and kidney is a hypothesis.

#### NELFE

- **Related proteins** (co-abundance neighbors): XRCC1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: negative elongation factor complex member E. The protein encoded by this gene is part of a complex termed negative elongation factor (NELF) which represses RNA polymerase II transcript elongation. This protein bears similarity to nuclear RNA-binding proteins; however, it has not been demonstrated that this protein binds RNA. The protein contains a tract of alternating basic and acidic residues, largely arginine (R) and aspartic acid (D). The…
- **Diseases (Open Targets)**: HIV infectious disease (0.592); neurodegenerative disease (0.385); iridocyclitis (0.341); ankylosing spondylitis (0.304); gastric cancer (0.089)
- **Europe PMC papers**: 390
- **Why important**: NELFE connects to the high-connectivity XRCC1 node and contributes to the supplementary RNA-recognition-motif grouping (STRING SMART RNA recognition motif; within-query FDR = 0.0222). Its established function is as a component of the negative elongation factor complex, regulating RNA polymerase transcriptional pausing and elongation. HPA places it in the nucleus and reports enhancement in late spermatids, while its literature and disease associations provide additional biological context.
- **Conclusion**: Established evidence supports NELFE as a transcription-elongation regulator rather than a DNA-repair protein. Its module position suggests coordinated regulation of transcription with genome maintenance, but the cross-talk between these processes is not demonstrated by the supplied data. NELFE is therefore an informative mechanistic candidate, not proof of module function.

#### RBM27

- **Related proteins** (co-abundance neighbors): XRCC1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 27. Enables RNA binding activity. Predicted to be involved in mRNA processing. Predicted to be located in cytoplasm and nuclear speck. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.482); mathematical ability (0.075); premature birth (0.039); jaw disease (0.034); injury (0.034)
- **Europe PMC papers**: 208
- **Why important**: RBM27 is directly connected to XRCC1 in the co-abundance graph and belongs to the supplementary STRING RNA-recognition-motif grouping with TIA1, NELFE and RAVER1 (STRING SMART RNA recognition motif; within-query FDR = 0.0222). It is an RNA-binding and mRNA-processing factor located in nuclear speckles. Its cell-type enhancement in early spermatids and megakaryocyte progenitor populations suggests regulated expression in differentiated or precursor states, although its literature base is smaller than that of XRCC1 or TIA1.
- **Conclusion**: Established evidence supports RBM27 as a nuclear RNA-processing factor. Its connection to XRCC1 and the RNA-recognition-motif grouping makes it a useful candidate for testing whether the module coordinates transcript processing with genome maintenance. Any direct role in the bone–kidney module remains hypothetical.

#### MBD3

- **Related proteins** (co-abundance neighbors): TIA1 (0.86), SRP54 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methyl-CpG binding domain protein 3. DNA methylation is the major modification of eukaryotic genomes and plays an essential role in mammalian development. This gene belongs to a family of nuclear proteins which are characterized by the presence of a methyl-CpG binding domain (MBD). The encoded protein is a subunit of the NuRD, a multisubunit complex containing nucleosome remodeling and histone deacetylase activities. Unlike the other…
- **Diseases (Open Targets)**: neurodegenerative disease (0.269); neoplasm (0.094); central precocious puberty (0.087); glioma (0.085); central nervous system cancer (0.085)
- **Europe PMC papers**: 2308
- **Why important**: MBD3 bridges TIA1 to SRP54 and is the module member most directly associated with the NuRD chromatin-remodeling and histone-deacetylase complex in the supplied annotations. It has established roles in transcriptional repression, chromatin remodeling and developmental regulation, is detected in kidney, and has a substantial literature base.
- **Conclusion**: Established evidence supports MBD3 as a chromatin-regulatory factor and a plausible link between transcriptional state and the RNA-regulatory branch of the module. The graph does not establish a shared NuRD complex among module members, and a functional bridge from MBD3 to TIA1 or SRP54 is only a hypothesis.

## Module 9

**Tissue pair**: bone and kidney  
**Genes (7)**: BID, CNN2, FABP5, NSFL1C, PLIN3, S100A16, VASP

### Function

The module does not support a single definitive pathway assignment: no GO/KEGG term passed global correction, and no supplementary STRING functional term was reported. Its internal structure instead suggests a composite cellular program involving epithelial lipid handling, actin and adhesion organization, vesicle or lipid-droplet biology, and stress or apoptotic regulation. S100A16 is the central connector, linking CNN2, BID, FABP5, and NSFL1C. CNN2 and VASP support an actin-filament and adhesion component; FABP5 and PLIN3 support fatty-acid or lipid-droplet biology; NSFL1C supports membrane-trafficking biology; and BID supports mitochondrial apoptotic responses. These are functional interpretations of the genes and network, not globally significant enrichment claims.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the genes are predominantly intracellular, cytosolic, nucleoplasmic, cytoskeletal, membrane-associated, or lipid-droplet proteins, with FABP5 described as intracellular and membrane associated. HPA shows low immune-cell specificity for most genes and no frequent enriched blood-cell category, arguing against a straightforward blood-protein module. However, several genes are enriched in neutrophils or neutrophil progenitors, and BID is tissue enhanced in bone marrow, so a contribution from shared hematopoietic or myeloid cell states remains possible. The strongest recurring HPA pattern is epithelial, especially esophageal apical or suprabasal cells, with additional epithelial enrichment for FABP5 and PLIN3. Thus, the bone-kidney co-abundance signal may reflect a shared epithelial-like cellular program or a shared cell-state component rather than a tissue-specific bone or kidney pathway. Kidney protein detection is mixed across the genes, and the available bone protein annotation is absent.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, so the co-abundance edges are not independently supported by the supplied STRING interaction network. hu.MAP provides one partial complex connection in (hu.MAP huMAP3_09929.1), containing FABP5 and S100A16, but these are only a small subset of a broad complex whose other members are mostly outside the module. The remaining genes have no supplied hu.MAP complex assignment. Together, these results indicate limited prior physical-complex support for the module: the co-abundance structure may capture coordinated cellular state, tissue composition, regulation, or condition-dependent biology rather than a single established multiprotein complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09929.1 (FABP5, S100A16; 2/75)

### Novelty

The module is a potentially novel co-abundance pattern, but the fact sheet does not establish that it is a new biological discovery. Its novelty is supported only in the limited sense that the supplied STRING and hu.MAP resources provide little direct support for most of the within-module relationships, while the genes span several biological processes. Absence from those resources alone does not prove novelty, because databases are incomplete and co-abundance relationships need not be physical interactions. A stronger novelty claim would require replication in independent bone and kidney datasets, control for cell-type composition, and experimental or perturbational testing of the proposed relationships.

**Hypothesis.** Hypothesis: the module reflects a shared epithelial or epithelial-like stress-adaptation state in bone and kidney samples, combining fatty-acid handling and lipid-droplet trafficking with actin-based adhesion and membrane organization. S100A16 may coordinate this state with FABP5-associated lipid handling and CNN2-VASP-associated cytoskeletal remodeling, while NSFL1C and PLIN3 support membrane and lipid-compartment trafficking. BID may mark the susceptibility of the same state to mitochondrial apoptosis or cellular stress. The neutrophil and bone-marrow patterns in HPA raise an alternative or additional explanation involving shared hematopoietic-cell composition. This is a hypothesis rather than an established pathway assignment.

### Important genes

#### S100A16

- **Related proteins** (co-abundance neighbors): CNN2 (0.84), BID (0.83), FABP5 (0.82), NSFL1C (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09929.1
- **Function (MyGene.info)**: S100 calcium binding protein A16. Enables calcium ion binding activity and protein homodimerization activity. Predicted to act upstream of or within response to calcium ion. Located in several cellular components, including cytosol; extracellular space; and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.490); neoplasm (0.107); lung adenocarcinoma (0.104); breast cancer (0.103); breast carcinoma (0.101)
- **Europe PMC papers**: 2006
- **Why important**: S100A16 is the most connected and strongest node in the module. It links the cytoskeletal gene CNN2, the apoptosis regulator BID, the lipid-binding gene FABP5, and the trafficking-related gene NSFL1C. Its annotated calcium-binding and homodimerization activities are compatible with a coordinating role, and it is the only gene besides FABP5 assigned to the supplied hu.MAP complex (hu.MAP huMAP3_09929.1). HPA points toward esophageal epithelial cell states rather than immune-cell specificity. Its disease literature is broad, making it biologically important while not by itself proving the proposed module mechanism.
- **Conclusion**: Established: S100A16 is the central network connector, has calcium-binding and homodimerization annotations, and is associated with epithelial cell-type enrichment and (hu.MAP huMAP3_09929.1). Hypothesis: it may act as a regulatory bridge between lipid handling, cytoskeletal remodeling, and stress responses in this module.

#### FABP5

- **Related proteins** (co-abundance neighbors): S100A16 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09929.1
- **Function (MyGene.info)**: fatty acid binding protein 5. This gene encodes the fatty acid binding protein found in epidermal cells, and was first identified as being upregulated in psoriasis tissue. Fatty acid binding proteins are a family of small, highly conserved, cytoplasmic proteins that bind long-chain fatty acids and other hydrophobic ligands. FABPs may play roles in fatty acid uptake, transport, and metabolism. Polymorphisms in this gene are ass…
- **Diseases (Open Targets)**: phlebitis (0.289); Thrombophlebitis (0.289); nephrotic syndrome (0.215); response to xenobiotic stimulus (0.170); preeclampsia (0.158)
- **Europe PMC papers**: 6055
- **Why important**: FABP5 connects directly to S100A16 and supplies the clearest lipid-related interpretation. It binds long-chain fatty acids and is annotated for fatty-acid transport, lipid metabolism, epidermal development, triglyceride catabolism, and regulation of prostaglandin biosynthesis. It is enriched in several epithelial cell types and is one of the two module members in hu.MAP complex (hu.MAP huMAP3_09929.1). Its association with nephrotic syndrome and metabolic or inflammatory phenotypes increases its relevance to kidney-related interpretation, although those disease associations do not establish causality here.
- **Conclusion**: Established: FABP5 is an epithelial-associated intracellular or membrane protein with fatty-acid and lipid functions and partial complex support through (hu.MAP huMAP3_09929.1). Hypothesis: it may provide the metabolic arm of a stress-adaptive epithelial program coordinated with S100A16.

#### CNN2

- **Related proteins** (co-abundance neighbors): S100A16 (0.84), VASP (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calponin 2. The protein encoded by this gene, which can bind actin, calmodulin, troponin C, and tropomyosin, may function in the structural organization of actin filaments. The encoded protein could play a role in smooth muscle contraction and cell adhesion. Several pseudogenes of this gene have been identified, and are present on chromosomes 1, 2, 3, 6, 9, 11, 13, 15, 16, 21 and 22. Alternative splicing resu…
- **Diseases (Open Targets)**: Pulmonary artery atresia (0.416); asthma (0.410); retinitis pigmentosa (0.370); Alzheimer disease (0.366); chronic rhinosinusitis (0.333)
- **Europe PMC papers**: 983
- **Why important**: CNN2 occupies an internal position between S100A16 and VASP and provides a coherent actin-organization interpretation. Its protein binds actin, calmodulin, troponin C, and tropomyosin, and its annotations include actin-filament organization, actomyosin structure organization, cell adhesion, and mechanical response. HPA places it in epithelial, megakaryocyte, neutrophil-progenitor, and neutrophil cell states. This makes CNN2 useful for distinguishing a structural or cell-state signal from a purely metabolic interpretation.
- **Conclusion**: Established: CNN2 is an actin-associated structural regulator connected to S100A16 and VASP, with epithelial and hematopoietic cell-type patterns. Hypothesis: CNN2 may translate mechanical or adhesion changes into the module's broader lipid and stress response.

#### VASP

- **Related proteins** (co-abundance neighbors): CNN2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions, Focal adhesion sites; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vasodilator stimulated phosphoprotein. Vasodilator-stimulated phosphoprotein (VASP) is a member of the Ena-VASP protein family. Ena-VASP family members contain an EHV1 N-terminal domain that binds proteins containing E/DFPPPPXD/E motifs and targets Ena-VASP proteins to focal adhesions. In the mid-region of the protein, family members have a proline-rich domain that binds SH3 and WW domain-containing proteins. Their C-terminal EVH2 doma…
- **Diseases (Open Targets)**: neurodegenerative disease (0.215); Hypercholesterolemia (0.133); breast cancer (0.110); breast carcinoma (0.105); hepatocellular carcinoma (0.102)
- **Europe PMC papers**: 5374
- **Why important**: VASP is the terminal module member connected to CNN2 and is positioned at plasma membranes, cell junctions, and focal adhesions. Its Ena-VASP domains bind actin and support actin polymerization, while its annotations include actin remodeling and homotetramerization. HPA detects it in kidney and in several platelet, megakaryocyte, neutrophil, and trophoblast cell states. It therefore provides a plausible link between adhesion or cytoskeletal organization and the possible contribution of shared cell types.
- **Conclusion**: Established: VASP is an actin- and adhesion-associated protein with kidney detection and hematopoietic cell-type enrichment. Hypothesis: VASP may participate in the structural remodeling component of the module, but the supplied data do not demonstrate a direct interaction with CNN2 or any other module member.

#### BID

- **Related proteins** (co-abundance neighbors): S100A16 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BH3 interacting domain death agonist. This gene encodes a death agonist that heterodimerizes with either agonist BAX or antagonist BCL2, and thus regulate apoptosis. The encoded protein is a member of the BCL-2 family of cell death regulators. It is a mediator of mitochondrial damage induced by caspase-8 (CASP8); CASP8 cleaves this encoded protein, and the COOH-terminal part translocates to mitochondria where it triggers cytochrome c …
- **Diseases (Open Targets)**: neurodegenerative disease (0.505); smoking initiation (0.326); neoplasm (0.104); hepatocellular carcinoma (0.092); open-angle glaucoma (0.091)
- **Europe PMC papers**: 35202
- **Why important**: BID is directly connected to the central node S100A16 and contributes a distinct mitochondrial stress and apoptosis axis. It is a BCL two family death agonist that can be cleaved by CASP8 and promote cytochrome c release. HPA associates it with bone marrow and with dendritic-cell, monocyte, neutrophil-progenitor, and neutrophil states. Its extensive disease literature and strong connection to regulated cell death make it important for interpreting the module as a possible stress or turnover program rather than only a structural or metabolic module.
- **Conclusion**: Established: BID is an apoptosis regulator with bone-marrow and myeloid cell-state enrichment, connected to S100A16. Hypothesis: BID may indicate stress-induced mitochondrial priming within the shared module or may instead reflect hematopoietic-cell composition in the samples.

## Module 10

**Tissue pair**: bone and kidney  
**Genes (12)**: CCAR1, SPECC1L, EXOSC7, PPP1R9B, NKRF, NUP107, NUP93, POGZ, RBM19, TRMT1L, TSG101, USP15

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. The gene annotations nevertheless indicate a mixed nuclear and cytoskeletal regulatory module. Its strongest interpretable themes are nuclear transport and pore organization through NUP93 and NUP107, RNA processing and ribosome-related functions through EXOSC7 and RBM19, transcriptional regulation and genome or cell-state control through CCAR1, NKRF, POGZ and TSG101, and actin-cytoskeletal organization through SPECC1L and PPP1R9B. The sparse network suggests that this is not a single established pathway; rather, it may represent coordinated abundance of proteins involved in nuclear organization, RNA handling, cellular structural regulation and signaling. These are functional interpretations, not globally significant enrichment claims.

**Cell composition.** The module does not look like a plasma-protein or secreted-protein module: all genes have no secretome annotation. It also does not appear to be broadly blood-cell enriched, because nearly all genes have low immune-cell specificity and only USP15 is immune-cell enhanced, with neutrophil enrichment. Most genes have low tissue specificity, while two are tissue enhanced, including PPP1R9B in brain and USP15 in bone marrow. Single-cell annotations are heterogeneous, including oocytes, neutrophils, neural cell types, renal collecting duct intercalated cells and other cell types. Kidney protein detection is present for most genes with available kidney data, whereas no matching bone HPA tissue result is available. Overall, the shared signal is more consistent with broadly expressed intracellular proteins and possibly shared cellular programs than with a secreted factor or a simple blood-contamination signature, although the neutrophil-linked USP15 signal merits attention.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence known relationship within the module, NUP107–NUP93, supporting a genuine nuclear-pore connection. The absence of other STRING partners at the specified confidence threshold means that most module edges are not directly supported by the reported STRING evidence; it does not show that those relationships are false. hu.MAP identifies one complex containing SPECC1L and PPP1R9B, with many additional members outside the module, as shown by (hu.MAP huMAP3_09542.1). This supports a cytoskeletal or scaffold-related connection, but the module contains only a small subset of that complex. Together, the databases support selected local relationships rather than a fully established common complex or canonical pathway spanning all module genes.

**STRING interactions (score >= 0.7)**: 1 of 66 gene pairs: NUP107–NUP93 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09542.1 (SPECC1L, PPP1R9B; 2/38)

### Novelty

The module is potentially novel as a co-abundance pattern shared by bone and kidney because the reported database evidence covers only a small part of its internal structure: the NUP107–NUP93 relationship is known, and SPECC1L–PPP1R9B occur together in the hu.MAP complex (hu.MAP huMAP3_09542.1), while the remaining cross-functional grouping is not established by the supplied STRING or hu.MAP results. However, this is not sufficient to claim discovery of a new molecular complex or pathway. The module may instead reflect coordinated expression of broadly expressed intracellular proteins, shared cell states, or tissue-composition effects. Novelty should therefore be stated as a potentially new tissue-pair co-abundance organization requiring independent replication and cell-composition analysis.

**Hypothesis.** Hypothesis: in shared bone and kidney cellular populations, a coordinated program linking nuclear pore organization, RNA maturation, transcriptional or chromatin regulation, and actin-associated structural signaling produces the observed co-abundance module. NUP93 and NUP107 could represent the nuclear transport component; CCAR1, NKRF and POGZ could connect nuclear regulation to cell-state control; EXOSC7 and RBM19 could reflect RNA processing and nucleolar activity; and SPECC1L with PPP1R9B could connect the program to actin-associated scaffolding. TSG101 and USP15 may add vesicle, ubiquitin and transforming-growth-factor-beta regulatory context. This is a mechanistic hypothesis rather than an established pathway, and the sparse network and lack of globally significant enrichment make direct functional validation important.

### Important genes

#### CCAR1

- **Related proteins** (co-abundance neighbors): RBM19 (0.83), NKRF (0.82), TSG101 (0.81), NUP107 (0.81), SPECC1L (0.80), POGZ (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell division cycle and apoptosis regulator 1. Enables RNA polymerase II cis-regulatory region sequence-specific DNA binding activity; nuclear receptor coactivator activity; and transcription corepressor activity. Involved in positive regulation of cell migration and positive regulation of cell population proliferation. Acts upstream of or within positive regulation of apoptotic process. Located in nuclear envelope lumen. [provided by Alliance…
- **Diseases (Open Targets)**: dengue disease (0.370); neurodegenerative disease (0.288); medulloblastoma (0.199); cancer (0.103); malignant pleural mesothelioma (0.093)
- **Europe PMC papers**: 733
- **Why important**: CCAR1 has the strongest network position in the module and connects to RBM19, NKRF, TSG101, NUP107, SPECC1L and POGZ. Its established annotations include transcriptional coactivator and corepressor activity, regulation of proliferation, migration and apoptosis, and a nuclear location. Its disease associations span cancer and neurodegenerative disease, and it has a substantial literature base. This combination makes CCAR1 the leading candidate for integrating the module’s nuclear and cell-state signals.
- **Conclusion**: Established evidence supports CCAR1 as a broadly connected nuclear regulatory protein with relevance to proliferation, migration and apoptosis. It is plausible, but not demonstrated, that CCAR1 is a module-level coordinator in bone and kidney.

#### SPECC1L

- **Related proteins** (co-abundance neighbors): NUP93 (0.84), PPP1R9B (0.83), CCAR1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Actin filaments; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_09542.1
- **Function (MyGene.info)**: sperm antigen with calponin homology and coiled-coil domains 1 like. This gene encodes a coiled-coil domain containing protein. The encoded protein may play a critical role in actin-cytoskeletal reorganization during facial morphogenesis. Mutations in this gene are a cause of oblique facial clefting-1. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. A read-through transcript composed of SPECC1L (sperm antigen w…
- **Diseases (Open Targets)**: Teebi hypertelorism syndrome 1 (0.728); Opitz G/BBB syndrome (0.648); Teebi hypertelorism syndrome (0.607); Tessier number 4 facial cleft (0.589); neurodegenerative disease (0.489)
- **Europe PMC papers**: 624
- **Why important**: SPECC1L occupies a central position linking CCAR1, NUP93 and PPP1R9B. Its established annotations support actin-cytoskeleton organization and cell adhesion, and its disease associations include facial developmental syndromes. It is also one of the two module members in the hu.MAP complex (hu.MAP huMAP3_09542.1). Its substantial literature volume and structural position make it an important bridge between the nuclear and cytoskeletal portions of the module.
- **Conclusion**: Established evidence supports SPECC1L as an actin-associated and adhesion-related scaffold protein with developmental disease relevance. Its possible role as a bridge between nuclear-pore and cytoskeletal co-abundance is a hypothesis.

#### NUP93

- **Related proteins** (co-abundance neighbors): SPECC1L (0.84); STRING partners: NUP107 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 is directly connected to SPECC1L in the module and has the reported high-confidence STRING relationship with NUP107. It is a nuclear-pore component involved in nucleocytoplasmic transport, nuclear-envelope organization, messenger-RNA export and nuclear-pore assembly. It also has kidney disease associations, including nephrotic syndromes, and a substantial literature base. This gives it the clearest established molecular-complex anchor in the module.
- **Conclusion**: Established evidence identifies NUP93 as a nuclear-pore protein involved in transport and pore organization, with kidney disease relevance. Its connection to SPECC1L in this co-abundance module does not establish a direct physical interaction between those proteins.

#### USP15

- **Related proteins** (co-abundance neighbors): TSG101 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin specific peptidase 15. This gene encodes a member of the ubiquitin specific protease (USP) family of deubiquitinating enzymes. USP enzymes play critical roles in ubiquitin-dependent processes through polyubiquitin chain disassembly and hydrolysis of ubiquitin-substrate bonds. The encoded protein associates with the COP9 signalosome, and also plays a role in transforming growth factor beta signalling through deubiquitina…
- **Diseases (Open Targets)**: neurodegenerative disease (0.548); alcohol drinking (0.294); post term pregnancy (0.272); smoking initiation (0.217); injury (0.162)
- **Europe PMC papers**: 1872
- **Why important**: USP15 forms a module edge with TSG101 and is the only gene reported as immune-cell enhanced, with bone-marrow and neutrophil enrichment. Its established function is deubiquitination, including regulation of transforming-growth-factor-beta and BMP signaling, and it is linked to protein stability. It therefore provides a potentially important signaling and cell-composition-sensitive component, even though it is not a high-degree hub.
- **Conclusion**: Established evidence supports USP15 as a deubiquitinating regulator of signaling and protein stability with neutrophil and bone-marrow enrichment. A contribution from neutrophil abundance or shared immune-related cell states is plausible but not proven.

#### POGZ

- **Related proteins** (co-abundance neighbors): TRMT1L (0.81), CCAR1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pogo transposable element derived with ZNF domain. The protein encoded by this gene appears to be a zinc finger protein containing a transposase domain at the C-terminus. This protein was found to interact with the transcription factor SP1 in a yeast two-hybrid system. Alternatively spliced transcript variants encoding distinct isoforms have been observed. [provided by RefSeq, Aug 2010].
- **Diseases (Open Targets)**: white-sutton syndrome (0.784); Intellectual disability (0.635); autism spectrum disorder (0.572); hereditary disease (0.550); neurodegenerative disease (0.517)
- **Europe PMC papers**: 804
- **Why important**: POGZ connects to CCAR1 and TRMT1L and is annotated for transcriptional regulation, homologous recombination repair, sister-chromatid cohesion and kinetochore assembly. Its strong disease associations include White-Sutton syndrome, intellectual disability and autism-spectrum disorder, with a substantial literature base. It represents a plausible genome-maintenance and developmental regulatory component within an otherwise heterogeneous module.
- **Conclusion**: Established evidence supports POGZ as a nuclear regulator associated with genome maintenance, cell division and developmental disease. Its role in coordinating the bone–kidney module is inferred from co-abundance and network placement, not directly demonstrated.

## Module 11

**Tissue pair**: bone and kidney  
**Genes (43)**: CEBPB, CFAP20, DHX16, DIDO1, FXR1, GON7, HDAC1, HDAC2, IGF2BP2, IGF2BP3, IPO11, KIFBP, LUC7L2, LEMD3, MCM2, MCM4, MCM5, MCM6, MCM7, NAA10, NAA25, NRDC, OSBPL8, PALS2, PDCL3, PSMB9, GINS1, ADSS2, RBM26, RFC2, RFC4, RPP40, SLC27A4, SEC23A, SEH1L, SMN1, SUPT16H, SRPK1, STT3A, TCOF1, THOP1, TOE1, XPO5

### Function

The module is best interpreted as a nuclear DNA-replication and replication-fork maintenance module. The primary evidence is the coherent set of globally corrected terms for the MCM complex, DNA-replication preinitiation complex, CMG complex, DNA replication, replication initiation, helicase activity, DNA-strand elongation, and replication-associated break repair (23 globally significant GO/KEGG terms, q_global 2.84e-05–0.0183; see the table). The cell-cycle, nuclear-chromosome, macromolecular-conformation, and nucleic-acid-binding terms (KEGG Cell cycle - Homo sapiens (human); q_global = 0.00487), (GO:CC nuclear chromosome; q_global = 0.0241) (GO:MF macromolecular conformation isomerase activity; q_global = 0.027) (GO:MF nucleic acid binding; q_global = 0.0364) provide supporting context. The core signal is therefore not a generic proliferation annotation: it is specifically the coordinated abundance of MCM helicase components, GINS1, and RFC subunits, with additional chromatin, RNA-processing, transport, and proteostasis genes forming peripheral connections.

**Cell composition.** This is not a plasma-protein or secreted-protein module: HPA identifies no secreted genes. Most genes have low tissue specificity, and the module is predominantly nuclear or cytosolic rather than tissue-restricted. HPA nevertheless shows enrichment of several genes in bone marrow, lymphoid tissue, erythrocyte progenitors, megakaryocyte progenitors, and other proliferative precursor populations. Six genes have immune-cell-enhanced evidence, but most genes have low immune-cell specificity. The frequent reproductive precursor and germ-cell annotations also indicate a broader proliferative-cell signature rather than a kidney- or bone-exclusive program. Thus, shared abundance in bone and kidney could partly reflect proliferating, progenitor-like, or hematopoietic-associated cells in the samples, although the kidney protein-detection evidence and the replication annotations support a genuine nuclear replication program. The absence of secreted proteins argues against a circulating plasma-protein explanation.

**GO/KEGG enrichment**: 26 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC MCM complex | 2.84e-05 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC DNA replication preinitiation complex | 3.68e-05 | GINS1, MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC CMG complex | 3.68e-05 | GINS1, MCM2, MCM4, MCM5, MCM6, MCM7 |
| KEGG DNA replication - Homo sapiens (human) | 9.98e-05 | MCM2, MCM4, MCM5, MCM6, MCM7, RFC2, RFC4 |
| GO:BP regulation of DNA-templated DNA replication initiation | 0.000114 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded DNA helicase activity | 0.000206 | MCM2, MCM4, MCM5, MCM6, MCM7, RFC2, RFC4 |
| GO:BP double-strand break repair via break-induced replication | 0.000298 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication | 0.000298 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF DNA helicase activity | 0.000879 | MCM2, MCM4, MCM5, MCM6, MCM7, RFC2, RFC4 |
| GO:MF nucleic acid conformation isomerase activity | 0.00195 | DHX16, FXR1, MCM2, MCM4, MCM5, MCM6, MCM7, RFC2, RFC4 |
| GO:BP DNA-templated DNA replication | 0.00444 | GINS1, MCM2, MCM4, MCM5, MCM6, MCM7, RFC2, RFC4 |
| KEGG Cell cycle - Homo sapiens (human) | 0.00487 | HDAC1, HDAC2, MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP DNA replication initiation | 0.00729 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF helicase activity | 0.00994 | DHX16, MCM2, MCM4, MCM5, MCM6, MCM7, RFC2, RFC4 |
| GO:MF four-way junction helicase activity | 0.0102 | MCM2, MCM4, MCM5, MCM6, MCM7 |

### STRING and hu.MAP

STRING provides established support for a dense replication core. The MCM proteins are strongly connected to one another and to GINS1, while RFC2 and RFC4 connect the helicase module to replication-factor-C activity. STRING functional annotations independently point to replication stress and ATR activation, DNA-strand elongation, DNA synthesis, DNA unwinding, replication, and the MCM and CMG complexes (15 supplementary STRING terms; within-query FDR 4.04e-05–0.00022). These STRING results are supplementary rather than globally corrected enrichment evidence. hu.MAP provides orthogonal complex-level support: multiple complexes contain MCM2, MCM4, MCM5, MCM6, MCM7, and GINS1 together (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1), with additional support for the RFC2-RFC4 complex (hu.MAP huMAP3_09476.1) (hu.MAP huMAP3_03241.1) (hu.MAP huMAP3_07313.1) (hu.MAP huMAP3_08399.1) (hu.MAP huMAP3_02854.1) (hu.MAP huMAP3_08854.1) (hu.MAP huMAP3_14232.1) (hu.MAP huMAP3_08879.1) (hu.MAP huMAP3_12839.1) (hu.MAP huMAP3_00703.1) (hu.MAP huMAP3_10568.1) and the HDAC1-HDAC2 complexes (hu.MAP huMAP3_01287.1), (hu.MAP huMAP3_10311.1), (hu.MAP huMAP3_08800.1), (hu.MAP huMAP3_09031.1), (hu.MAP huMAP3_15128.1). The module therefore contains a known replication-complex core embedded in a broader co-abundance neighborhood. Several peripheral module edges, including those involving GON7, IPO11, RNA-processing proteins, and metabolic or trafficking proteins, are not represented by corresponding STRING or hu.MAP relationships and should not be treated as established physical interactions.

**STRING interactions (score >= 0.7)**: 33 of 903 gene pairs: CEBPB–HDAC1 (0.991); GINS1–MCM2 (0.999); GINS1–MCM4 (0.999); GINS1–MCM5 (0.999); GINS1–MCM6 (0.998); GINS1–MCM7 (0.999); GINS1–RFC4 (0.868); HDAC1–HDAC2 (0.999); IGF2BP2–IGF2BP3 (0.851); LUC7L2–SRPK1 (0.789); MCM2–MCM4 (0.999); MCM2–MCM5 (0.999); MCM2–MCM6 (0.999); MCM2–MCM7 (0.999); MCM2–RFC4 (0.877); MCM2–SUPT16H (0.735); MCM4–MCM5 (0.999); MCM4–MCM6 (0.999); MCM4–MCM7 (0.999); MCM4–RFC2 (0.828); MCM4–RFC4 (0.898); MCM4–SUPT16H (0.722); MCM5–MCM6 (0.999); MCM5–MCM7 (0.999); MCM5–RFC2 (0.874); MCM5–RFC4 (0.949); MCM6–MCM7 (0.999); MCM6–RFC2 (0.827); MCM6–RFC4 (0.945); MCM7–RFC2 (0.894); MCM7–RFC4 (0.906); NAA10–NAA25 (0.92); RFC2–RFC4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Activation of ATR in response to replication stress (FDR = 4.04e-05, 7 genes); RCTM DNA strand elongation (FDR = 4.04e-05, 8 genes); NetworkNeighborAL DNA replication, and Regulation of DNA-directed DNA polymerase activity (FDR = 4.18e-05, 8 genes); KEGG DNA replication (FDR = 5.46e-05, 7 genes); Process Regulation of DNA-templated DNA replication (FDR = 5.58e-05, 8 genes); Keyword DNA replication (FDR = 5.91e-05, 9 genes); RCTM Unwinding of DNA (FDR = 8.04e-05, 6 genes); RCTM Synthesis of DNA (FDR = 8.04e-05, 9 genes); WikiPathways DNA replication (FDR = 0.0001, 7 genes); KEGG Cell cycle (FDR = 0.00015, 7 genes); Component MCM complex (FDR = 0.00017, 5 genes); Component CMG complex (FDR = 0.00017, 6 genes); COMPARTMENTS MCM complex (FDR = 0.00018, 5 genes); COMPARTMENTS CMG complex (FDR = 0.00018, 6 genes); NetworkNeighborAL Activation of the pre-replicative complex, and GINS complex (FDR = 0.00022, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14758.1 (MCM4, MCM5, MCM7, MCM2, MCM6, GINS1; 6/14); huMAP3_08554.1 (MCM4, MCM5, MCM7, MCM2, MCM6, GINS1; 6/15); huMAP3_11832.1 (MCM4, MCM5, MCM7, MCM2, MCM6, GINS1; 6/15); huMAP3_12180.1 (MCM4, MCM5, MCM7, MCM2, MCM6, GINS1; 6/17); huMAP3_05529.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/6); huMAP3_11119.1 (MCM4, MCM5, MCM7, MCM6, GINS1; 5/14); huMAP3_06061.1 (MCM4, MCM7, MCM2, MCM6; 4/5); huMAP3_07113.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_10862.1 (MCM4, MCM2, MCM6, SUPT16H; 4/33); huMAP3_09860.1 (MCM4, MCM2, MCM6; 3/4); huMAP3_00154.1 (MCM4, MCM2, MCM6; 3/5); huMAP3_09238.1 (MCM5, MCM7, GINS1; 3/11); huMAP3_09466.1 (MCM4, MCM2, MCM6; 3/23); huMAP3_14306.1 (MCM4, MCM2, MCM6; 3/55); huMAP3_02602.1 (MCM4, MCM6; 2/2); huMAP3_09476.1 (RFC4, RFC2; 2/5); huMAP3_03241.1 (RFC4, RFC2; 2/9); huMAP3_07313.1 (RFC4, RFC2; 2/9); huMAP3_08399.1 (MCM5, GINS1; 2/10); huMAP3_02854.1 (RFC4, RFC2; 2/10); huMAP3_08854.1 (RFC4, RFC2; 2/10); huMAP3_14232.1 (RFC4, RFC2; 2/10); huMAP3_08879.1 (RFC4, RFC2; 2/11); huMAP3_12839.1 (RFC4, RFC2; 2/11); huMAP3_00703.1 (RFC4, RFC2; 2/12); huMAP3_10568.1 (RFC4, RFC2; 2/13); huMAP3_08848.1 (MCM4, MCM6; 2/15); huMAP3_01287.1 (HDAC1, HDAC2; 2/17); huMAP3_14804.1 (RBM26, LUC7L2; 2/19); huMAP3_10311.1 (HDAC1, HDAC2; 2/32); huMAP3_12727.1 (RFC4, RFC2; 2/32); huMAP3_08800.1 (HDAC1, HDAC2; 2/48); huMAP3_09031.1 (HDAC1, HDAC2; 2/49); huMAP3_10202.1 (XPO5, IPO11; 2/52); huMAP3_04549.1 (SMN1, TOE1; 2/52); huMAP3_06511.1 (SMN1, TOE1; 2/79); huMAP3_15128.1 (HDAC1, HDAC2; 2/96); huMAP3_08980.1 (SMN1, TOE1; 2/97)

### Novelty

The replication function itself is not a new biological discovery: the MCM, GINS, and RFC relationships are already well established by STRING, hu.MAP, and the literature. The potentially novel result is the conservation of this particular co-abundance neighborhood across bone and kidney, including its peripheral links to RNA processing, nuclear transport, chromatin regulation, and cellular metabolism. However, absence from STRING or hu.MAP cannot establish novelty, because those resources emphasize previously studied physical or functional relationships and do not test tissue-pair co-abundance conservation. A defensible conclusion is that this is a biologically credible conserved module with a known replication core, but that its tissue-pair-specific organization and peripheral membership require independent replication and targeted comparison with other tissue groups before being called a new mechanism.

**Hypothesis.** Hypothesis: the shared bone-kidney module reflects coordinated replication competence in a subset of proliferating or progenitor-like cells, in which the MCM helicase and GINS1 support replication-fork progression, RFC2-RFC4 support primer or clamp-associated replication functions, and HDAC1-HDAC2 plus SUPT16H help coordinate chromatin state during genome duplication. The peripheral RNA-processing, nucleocytoplasmic-transport, and protein-modification genes may reflect the supporting biosynthetic and nuclear infrastructure required by these cells. The HPA precursor and bone-marrow associations make a shared proliferative-cell composition plausible, but co-abundance alone does not demonstrate that these peripheral genes mechanistically regulate replication. This hypothesis should be tested by cell-composition adjustment, cell-cycle measurements, and perturbation or replication-stress experiments in relevant bone and kidney cell models.

### Important genes

#### MCM2

- **Related proteins** (co-abundance neighbors): MCM6 (0.86), MCM5 (0.84), MCM7 (0.84), IPO11 (0.82), CFAP20 (0.81), CEBPB (0.80); STRING partners: GINS1 (0.999), MCM4 (0.999), MCM5 (0.999), MCM6 (0.999), MCM7 (0.999), RFC4 (0.877), SUPT16H (0.735)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_05529.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_10862.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a central member of the replication core, has strong connections to the other MCM proteins, GINS1, RFC4, and SUPT16H, and appears across nearly all primary replication terms (25 globally significant GO/KEGG terms, q_global 2.84e-05–0.027; see the table) and all supplementary STRING terms (15 supplementary STRING terms; within-query FDR 4.04e-05–0.00022). It is present in many hu.MAP replication complexes (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1), (hu.MAP huMAP3_05529.1), (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1), (hu.MAP huMAP3_09466.1), and (hu.MAP huMAP3_14306.1). Its established function is participation in the pre-replication complex and replication-fork formation. HPA links it to bone marrow and lymphoid tissue and to progenitor populations, while its disease associations include hearing loss and developmental abnormalities. Its extensive literature makes it a particularly well-supported anchor for interpreting the module.
- **Conclusion**: Established evidence supports MCM2 as a core replication-initiation and fork-associated component and as a major driver of the module interpretation. The tissue and cell annotations support a proliferative-cell contribution, but they do not establish a bone-kidney-specific role. A role for MCM2 in coordinating the module's peripheral genes remains a hypothesis.

#### MCM4

- **Related proteins** (co-abundance neighbors): MCM6 (0.92), IPO11 (0.81); STRING partners: GINS1 (0.999), MCM2 (0.999), MCM5 (0.999), MCM6 (0.999), MCM7 (0.999), RFC2 (0.828), RFC4 (0.898), SUPT16H (0.722)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_05529.1, huMAP3_11119.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_10862.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 4. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication rel…
- **Diseases (Open Targets)**: primary immunodeficiency with natural-killer cell deficiency and adrenal insufficiency (0.714); X-linked adrenal hypoplasia congenita (0.185); lung adenocarcinoma (0.112); microcephaly (0.111); neoplasm (0.102)
- **Europe PMC papers**: 4082
- **Why important**: MCM4 is a core MCM helicase component with extensive STRING connectivity to GINS1, the other MCM proteins, RFC2, RFC4, and SUPT16H. It occurs in essentially the full set of primary MCM, replication-initiation, helicase, replication, and cell-cycle evidence (25 globally significant GO/KEGG terms, q_global 2.84e-05–0.027; see the table), and in numerous hu.MAP complexes (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1), (hu.MAP huMAP3_08848.1), and (hu.MAP huMAP3_01287.1). HPA reports bone-marrow enhancement and kidney protein detection. Its established function in the MCM complex, its replication and DNA-repair annotations, its links to immunodeficiency and developmental disease, and its substantial literature make it a strong mechanistic representative of the module core.
- **Conclusion**: Established evidence identifies MCM4 as a central component of the MCM and CMG-associated replication machinery. Its presence in the shared module is readily explained by replication biology. Any specific contribution to bone or kidney pathology is not established by this co-abundance result.

#### MCM5

- **Related proteins** (co-abundance neighbors): MCM7 (0.92), MCM2 (0.84), CFAP20 (0.82), TOE1 (0.82), CEBPB (0.81); STRING partners: GINS1 (0.999), MCM2 (0.999), MCM4 (0.999), MCM6 (0.999), MCM7 (0.999), RFC2 (0.874), RFC4 (0.949)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_05529.1, huMAP3_11119.1, huMAP3_09238.1, huMAP3_08399.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 5. The protein encoded by this gene is structurally very similar to the CDC46 protein from S. cerevisiae, a protein involved in the initiation of DNA replication. The encoded protein is a member of the MCM family of chromatin-binding proteins and can interact with at least two other members of this family. The encoded protein is upregulated in the transition from the G0 to G1/S phase of the cell cycl…
- **Diseases (Open Targets)**: Meier-Gorlin syndrome (0.563); neurodegenerative disease (0.397); lysosomal storage disease (0.362); kidney transplant (0.198); diabetic ketoacidosis (0.129)
- **Europe PMC papers**: 4143
- **Why important**: MCM5 is highly connected within the MCM core and also connects to RFC2, RFC4, CFAP20, TOE1, and CEBPB. It contributes to the globally corrected replication, helicase, cell-cycle, and DNA-repair terms (6 globally significant GO/KEGG terms, q_global 2.84e-05–0.000206; see the table), (10 globally significant GO/KEGG terms, q_global 0.000298–0.0102; see the table), (9 globally significant GO/KEGG terms, q_global 0.013–0.0364; see the table), and to every supplementary STRING category (15 supplementary STRING terms; within-query FDR 4.04e-05–0.00022). It is represented across multiple hu.MAP MCM and GINS complexes (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_11119.1), (hu.MAP huMAP3_09238.1), and (hu.MAP huMAP3_08399.1). Its established role in replication initiation and cell-cycle regulation, its association with Meier-Gorlin syndrome, and its large literature base make it important for distinguishing a true replication module from a nonspecific nuclear signal.
- **Conclusion**: Established evidence supports MCM5 as a core replication-initiation component and as part of the conserved MCM-GINS machinery. HPA bone-marrow enhancement is compatible with proliferating precursor cells, but does not prove that cell composition is the sole source of the signal.

#### MCM6

- **Related proteins** (co-abundance neighbors): MCM4 (0.92), MCM2 (0.86), IPO11 (0.82), RPP40 (0.80); STRING partners: GINS1 (0.998), MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM7 (0.999), RFC2 (0.827), RFC4 (0.945)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_05529.1, huMAP3_11119.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_10862.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 6. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: lactose intolerance (0.246); neurodegenerative disease (0.225); obesity disorder (0.166); nervous system disorder (0.141); systemic lupus erythematosus (0.140)
- **Europe PMC papers**: 3766
- **Why important**: MCM6 is a core MCM component with strong links to MCM2, MCM4, MCM5, MCM7, GINS1, RFC2, and RFC4. It contributes broadly to the primary replication, helicase, fork, initiation, repair, and cell-cycle terms (25 globally significant GO/KEGG terms, q_global 2.84e-05–0.027; see the table), to all STRING supplementary categories (15 supplementary STRING terms; within-query FDR 4.04e-05–0.00022), and to many hu.MAP complexes (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) and (hu.MAP huMAP3_08848.1). HPA associates it with lymphoid tissue and multiple hematopoietic progenitor populations, while kidney protein detection is present. Its established DNA-replication and replication-initiation functions, disease associations, and substantial literature make it a strong bridge between network structure, annotation, and tissue composition.
- **Conclusion**: Established evidence supports MCM6 as part of the conserved MCM helicase and replication-initiation machinery. Its HPA pattern makes a proliferative or progenitor-cell contribution plausible, but the data do not determine whether that contribution is biological regulation or sample composition.

#### MCM7

- **Related proteins** (co-abundance neighbors): MCM5 (0.92), MCM2 (0.84); STRING partners: GINS1 (0.999), MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM6 (0.999), RFC2 (0.894), RFC4 (0.906)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_05529.1, huMAP3_11119.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 is tightly linked to the other MCM proteins and GINS1 in STRING and is represented in numerous hu.MAP MCM and GINS complexes (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_10862.1) and (hu.MAP huMAP3_09238.1). It appears across the primary MCM, CMG, DNA-replication, helicase, strand-elongation, repair, and cell-cycle evidence (26 globally significant GO/KEGG terms, q_global 2.84e-05–0.0364; see the table) and across all supplementary STRING categories (15 supplementary STRING terms; within-query FDR 4.04e-05–0.00022). HPA reports bone-marrow enhancement, kidney protein detection, and enrichment in several proliferative precursor populations. Its established role in the MCM helicase, its links to developmental and neurological disease, and its substantial literature make it a robust marker of the module's central function.
- **Conclusion**: Established evidence supports MCM7 as a core replication-fork and helicase component. Its shared abundance is most parsimoniously explained by coordinated replication machinery, with proliferative-cell composition as a plausible contributing factor rather than a demonstrated alternative.

#### GINS1

- **Related proteins** (co-abundance neighbors): RFC2 (0.87); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM6 (0.998), MCM7 (0.999), RFC4 (0.868)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_11119.1, huMAP3_09238.1, huMAP3_08399.1
- **Function (MyGene.info)**: GINS complex subunit 1. The yeast heterotetrameric GINS complex is made up of Sld5 (GINS4; MIM 610611), Psf1, Psf2 (GINS2; MIM 610609), and Psf3 (GINS3; MIM 610610). The formation of the GINS complex is essential for the initiation of DNA replication in yeast and Xenopus egg extracts (Ueno et al., 2005 [PubMed 16287864]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: combined immunodeficiency due to GINS1 deficiency (0.683); fetal growth restriction (0.462); PHARC syndrome (0.425); Abnormality of the gastrointestinal tract (0.198); smoking initiation (0.167)
- **Europe PMC papers**: 822
- **Why important**: GINS1 is the module's direct connection between the MCM helicase group and the GINS/CMG replication apparatus. It has STRING links to all principal MCM proteins and RFC4, participates in the primary CMG, preinitiation, DNA-replication, mitotic-replication, and strand-elongation terms (GO:CC DNA replication preinitiation complex; q_global = 3.68e-05), (GO:CC CMG complex; q_global = 3.68e-05), (GO:BP DNA-templated DNA replication; q_global = 0.00444), (GO:BP mitotic DNA replication; q_global = 0.0107), (GO:BP DNA replication; q_global = 0.0159), and (GO:BP DNA strand elongation involved in DNA replication; q_global = 0.0183), and occurs in multiple hu.MAP GINS and MCM complexes (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1), (hu.MAP huMAP3_11119.1), (hu.MAP huMAP3_06061.1), (hu.MAP huMAP3_09238.1), and (hu.MAP huMAP3_08399.1). HPA associates it with lymphoid tissue, testis, erythrocyte progenitors, and other differentiating populations. Its established requirement for replication initiation and its association with combined immunodeficiency and developmental phenotypes give it high biological importance despite a more limited literature volume than the major MCM genes.
- **Conclusion**: Established evidence supports GINS1 as a CMG-associated replication-initiation and elongation factor that reinforces the interpretation of the module as functional replication machinery. The progenitor-associated HPA pattern supports, but does not prove, a cell-composition explanation for conservation across tissues.
