# Conserved co-abundance modules: cell line and stem_cells

## Module 0

**Tissue pair**: cell line and stem_cells  
**Genes (6)**: EIF4EBP1, GNG4, PQBP1, VAMP4, ZNF121, RCHY1

### Function

No GO/KEGG term passed global correction, and there were no supplementary STRING enrichment terms. The module therefore does not support a statistically established pathway-level function. Its gene annotations suggest a mixed cellular program involving G-protein-coupled receptor signaling and growth regulation through GNG4, membrane trafficking and vesicle fusion through VAMP4, translational repression and TOR-linked regulation through EIF4EBP1, transcriptional regulation through ZNF121 and PQBP1, and ubiquitin-dependent protein turnover through RCHY1. The network pattern is hub-and-spoke, with GNG4 connected to every other member while the remaining genes are peripheral. This is compatible with coordinated regulation across distinct cellular processes, but it does not establish a single common mechanism.

**Cell composition.** The module is not dominated by plasma or secreted proteins: all members are annotated as non-secreted, and none is classified as a secreted gene. Most members have low tissue specificity and low immune-cell specificity, which is more consistent with broadly distributed cellular proteins than with a blood-cell module. GNG4 is tissue enhanced in brain, ovary, and pituitary gland and is enriched in several neuroendocrine-related cell types. EIF4EBP1 is tissue enhanced in pancreas and has cell-type enrichment in epithelial, lactating, and trophoblast populations. RCHY1 is immune-cell enhanced in basophils, but the overall HPA profile does not indicate a blood-cell-dominated module. HPA protein detection in the relevant cell line and stem-cell contexts was unavailable, so tissue-level evidence should not be treated as direct protein confirmation in these samples.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no STRING functional enrichment was present. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated here by known physical interactions or a shared curated complex. The lack of STRING and hu.MAP support argues against interpreting the module as a canonical protein complex, while still allowing the possibility that coordinated abundance reflects shared regulation, cell state, or indirect biological coupling.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially unusual co-abundance pattern because the genes span vesicle trafficking, signaling, translation control, transcriptional regulation, and ubiquitin-mediated turnover without a globally significant GO/KEGG or STRING annotation and without a shared hu.MAP complex. However, it cannot be called a new biological pathway solely because the relationships are absent from STRING and hu.MAP. The most defensible conclusion is that the coordinated abundance association may be a new observation in these datasets, whereas the underlying gene functions are established and heterogeneous. Independent replication, preservation in additional datasets, perturbation experiments, and assessment of batch, differentiation-state, and cell-composition effects would be required to establish novelty.

**Hypothesis.** Hypothesis: the module may represent a shared cell-state program linking G-protein signaling through GNG4 with intracellular trafficking through VAMP4, translational restraint through EIF4EBP1, nuclear transcriptional or RNA-regulatory processes through ZNF121 and PQBP1, and proteasome-linked protein quality control through RCHY1. GNG4 may mark or help coordinate this state because it is the network hub, but the co-abundance network does not demonstrate that it regulates the other genes. An alternative hypothesis is that the association reflects a common differentiation or cellular-composition signal shared by cell line and stem-cell samples rather than direct molecular coupling.

### Important genes

#### GNG4

- **Related proteins** (co-abundance neighbors): VAMP4 (0.99), ZNF121 (0.90), PQBP1 (0.82), RCHY1 (0.81), EIF4EBP1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein subunit gamma 4. Predicted to enable G-protein beta-subunit binding activity. Involved in negative regulation of cell growth. Located in extracellular exosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.451); smoking initiation (0.384); Parkinson disease (0.354); Alzheimer disease (0.354); lysosomal storage disease (0.353)
- **Europe PMC papers**: 791
- **Why important**: GNG4 is the network hub, connected to every other module member with the strongest overall network position. Its annotated functions include G-protein beta-subunit binding, G-protein-coupled receptor signaling, and negative regulation of cell growth. HPA supports tissue and cell-type specificity in brain, pituitary, ovary, and neuroendocrine-related populations. It also has disease links involving neurodegenerative and lysosomal disorders and a substantial literature base.
- **Conclusion**: Established evidence supports GNG4 as the central co-abundance marker and as a signaling-associated gene with neuroendocrine-related expression patterns. It is plausible, but unproven, that GNG4 organizes the module biologically; the network alone cannot establish a causal hub role.

#### VAMP4

- **Related proteins** (co-abundance neighbors): GNG4 (0.99); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vesicle associated membrane protein 4. Synaptobrevins/VAMPs, syntaxins, and the 25-kD synaptosomal-associated protein SNAP25 are the main components of a protein complex involved in the docking and/or fusion of synaptic vesicles with the presynaptic membrane. The protein encoded by this gene is a member of the vesicle-associated membrane protein (VAMP)/synaptobrevin family. This protein may play a role in trans-Golgi network-to-endosom…
- **Diseases (Open Targets)**: Parkinson disease (0.140); Menorrhagia (0.098); uterine corpus leiomyoma (0.089); endometriosis (0.059); diabetes mellitus (0.057)
- **Europe PMC papers**: 178716
- **Why important**: VAMP4 is the strongest directly connected peripheral member and has a well-established role in vesicle-mediated transport, endocytic recycling, SNARE assembly, membrane fusion, and trans-Golgi network-to-endosome transport. Its large literature base makes its cellular function comparatively well characterized. Its connection to GNG4 may indicate coordination between signaling and membrane trafficking.
- **Conclusion**: Established evidence supports VAMP4 as a membrane-trafficking and vesicle-fusion component. Its membership supports a trafficking aspect of the module, but there is no direct evidence that it physically interacts with GNG4 or that the module is a vesicle complex.

#### EIF4EBP1

- **Related proteins** (co-abundance neighbors): GNG4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4E binding protein 1. This gene encodes one member of a family of translation repressor proteins. The protein directly interacts with eukaryotic translation initiation factor 4E (eIF4E), which is a limiting component of the multisubunit complex that recruits 40S ribosomal subunits to the 5' end of mRNAs. Interaction of this protein with eIF4E inhibits complex assembly and represses translation. This protein is phosphor…
- **Diseases (Open Targets)**: stroke disorder (0.328); alcohol drinking (0.326); ovulation (0.276); menopause (0.250); neurodegenerative disease (0.174)
- **Europe PMC papers**: 10878
- **Why important**: EIF4EBP1 is a central translational regulator that binds eIF4E and represses translation, with regulation linked to TOR signaling, insulin signaling, and cell-cycle transitions. It has the largest literature footprint among the selected genes and shows HPA enrichment across pancreatic, epithelial, lactating, and trophoblast-related cell types. Its presence connects the module to growth-state and protein-synthesis control.
- **Conclusion**: Established evidence supports EIF4EBP1 as a growth-responsive translational brake. Its co-abundance with GNG4 may reflect a shared cell-state program involving signaling and translation, but this connection remains a hypothesis rather than a demonstrated pathway.

#### PQBP1

- **Related proteins** (co-abundance neighbors): GNG4 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles, Primary cilium; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polyglutamine binding protein 1. This gene encodes a nuclear polyglutamine-binding protein that is involved with transcription activation. The encoded protein contains a WW domain. Mutations in this gene have been found in patients with Renpenning syndrome 1 and other syndromes with X-linked cognitive disability. Multiple alternatively spliced transcript variants that encode different protein isoforms have been described for this…
- **Diseases (Open Targets)**: Renpenning syndrome (0.787); neurodegenerative disease (0.531); hereditary disease (0.466); Intellectual disability (0.449); microcephaly (0.419)
- **Europe PMC papers**: 1075
- **Why important**: PQBP1 is a nuclear protein involved in transcription activation, alternative mRNA splicing, innate immune and antiviral responses, and neuron projection development. It is associated with Renpenning syndrome and other neurodevelopmental phenotypes, giving it strong disease relevance despite its peripheral network position. Its nuclear localization contrasts with the membrane-trafficking role of VAMP4 and broadens the possible interpretation of the module.
- **Conclusion**: Established evidence supports PQBP1 as a nuclear transcriptional and RNA-regulatory factor with neurodevelopmental relevance. Its inclusion may indicate coordinated cell-state regulation or RNA processing, but there is no evidence that PQBP1 is a direct mechanistic partner of GNG4.

#### RCHY1

- **Related proteins** (co-abundance neighbors): GNG4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ring finger and CHY zinc finger domain containing 1. The protein encoded by this gene has ubiquitin ligase activity. It mediates E3-dependent ubiquitination and proteasomal degradation of target proteins, including tumor protein 53, histone deacetylase 1, and cyclin-dependent kinase inhibitor 1B, thus regulating their levels and cell cycle progression. Alternatively spliced transcript variants encoding different isoforms have been described for this…
- **Diseases (Open Targets)**: hypercholesterolemia, familial, 1 (0.333); non-neoplastic bile duct disorder (0.274); Jaundice (0.179); respiratory system disorder (0.173); musculoskeletal system disorder (0.105)
- **Europe PMC papers**: 473
- **Why important**: RCHY1 encodes an ubiquitin ligase involved in ubiquitination and proteasomal degradation of regulatory proteins, with effects on cell-cycle progression and rescue of stalled cytosolic ribosomes. Its cytosolic localization and basophil-enriched HPA profile provide a possible link to protein quality control and context-dependent cellular state. Its literature base is smaller than that of VAMP4 or EIF4EBP1 but sufficient to support a defined molecular function.
- **Conclusion**: Established evidence supports RCHY1 as a protein-turnover and cell-cycle regulator. Its module membership is consistent with coordinated proteostasis, but the data do not show that RCHY1 drives the observed co-abundance pattern or that the module is immune-cell specific.

## Module 1

**Tissue pair**: cell line and stem_cells  
**Genes (46)**: APP, ABL1, ATP2B4, C2CD3, CHMP1B, CORO1B, CYBC1, ETNK1, ERCC3, EXOG, FN3K, KPNA2, KCT2, MVK, LANCL1, LSM6, MAP4K4, MINPP1, MDK, NAA35, PAFAH1B3, PHLDA1, PJA1, PLEKHA8, PPP4C, PSMA1, PSMG1, RDX, RAN, RELCH, RACGAP1, RRM2, RMI2, POLRMT, MRRF, SAAL1, SPRYD7, STAT2, TAF5, TENM3, TNIK, UBE2D1, VAT1L, VCL, VPS45, YBX3

### Function

This is a heterogeneous, sparse co-abundance module rather than a module with one statistically established GO or KEGG function. No GO/KEGG term passed global correction, and STRING reported no functional enrichment. The gene annotations nevertheless point to several recurring cellular themes: nuclear transport and cell-cycle control through KPNA2 and RAN; DNA synthesis and repair through RRM2, ERCC3, RMI2, PPP4C and ABL1; proteasome assembly and ubiquitin-dependent protein handling through PSMG1, PSMA1, UBE2D1 and PJA1; cytoskeletal, adhesion and migration processes through RDX, VCL, CORO1B, MAP4K4 and TNIK; and mitochondrial gene expression or maintenance through POLRMT, EXOG and MRRF. These convergent annotations support a broad proliferative, genome-maintenance and intracellular-trafficking interpretation, but they do not establish one specific pathway for the module.

**Cell composition.** The module is not dominated by plasma or secreted proteins, and it is not a blood-cell-specific module. Only APP, MDK and MINPP1 are annotated as secreted to blood. Most genes have low tissue specificity or are tissue- or cell-type-enhanced across diverse tissues and cell types. The strongest recurring HPA patterns involve testis and spermatogenic cell types, with additional representation of skeletal muscle, brain, lymphoid tissue, bone marrow and trophoblast-related cells. Many genes are broadly cellular proteins involved in proteostasis, nuclear transport, DNA maintenance, metabolism or cytoskeletal organization. Therefore, the shared cell-line and stem-cell signal is more plausibly related to shared cellular state or basic cell biology than to plasma contamination or a single blood-cell population. HPA protein detection for the two relevant sample categories was unavailable, so protein-level confirmation in those categories is not possible.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited set of specific relationships rather than a densely connected module. Particularly coherent links include ERCC3 with TAF5, KPNA2 with RAN, KPNA2 with RACGAP1 and RRM2, RACGAP1 with RRM2, PSMA1 with PSMG1, and RDX with VCL. These relationships connect nuclear transport, cytokinesis or nucleotide metabolism, proteasome assembly, and membrane-cytoskeletal organization. hu.MAP independently places PSMA1 with PSMG1 in proteasome-related complexes (hu.MAP huMAP3_00356.1), (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1); KPNA2 with RAN in nuclear-transport complexes (hu.MAP huMAP3_10000.1) and (hu.MAP huMAP3_12581.1); SAAL1 with EXOG in complexes (hu.MAP huMAP3_10202.1) and (hu.MAP huMAP3_10287.1); and MAP4K4 with PPP4C in phosphatase-associated complexes (hu.MAP huMAP3_09709.1), (hu.MAP huMAP3_10333.1) and (hu.MAP huMAP3_13510.1). However, each hu.MAP complex contains only a small subset of this module, while most module genes have no listed hu.MAP complex or high-confidence STRING partner. Thus, the network combines several known molecular neighborhoods but does not demonstrate one unified physical complex.

**STRING interactions (score >= 0.7)**: 7 of 1035 gene pairs: ERCC3–TAF5 (0.981); KPNA2–RACGAP1 (0.714); KPNA2–RAN (0.944); KPNA2–RRM2 (0.743); PSMA1–PSMG1 (0.935); RACGAP1–RRM2 (0.789); RDX–VCL (0.753)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00356.1 (PSMG1, PSMA1; 2/33); huMAP3_10000.1 (KPNA2, RAN; 2/44); huMAP3_10202.1 (SAAL1, EXOG; 2/52); huMAP3_10287.1 (SAAL1, EXOG; 2/53); huMAP3_09709.1 (MAP4K4, PPP4C; 2/57); huMAP3_12581.1 (KPNA2, RAN; 2/58); huMAP3_10333.1 (MAP4K4, PPP4C; 2/63); huMAP3_09656.1 (PSMG1, PSMA1; 2/64); huMAP3_13725.1 (PSMG1, PSMA1; 2/69); huMAP3_13510.1 (MAP4K4, PPP4C; 2/85)

### Novelty

The module may be novel as a cross-context co-abundance pattern, but the evidence does not justify calling it a newly discovered molecular pathway or complex. Several relationships and substructures are already known from STRING and hu.MAP, including proteasome assembly, nuclear transport, phosphatase-associated organization and cytoskeletal linkage. The apparent novelty is therefore the co-abundance of these otherwise partly separate neighborhoods across cell line and stem-cell samples. Because no comparison against all published co-expression modules, tissue atlases or prior studies was provided, novelty remains provisional. Absence of a STRING or hu.MAP entry for many genes cannot by itself establish novelty.

**Hypothesis.** Hypothesis: this shared module reflects a common proliferative or developmentally plastic cellular state in which nuclear import, DNA precursor production and repair, proteasome capacity, mitochondrial maintenance, and cytoskeletal remodeling are coordinated. KPNA2-RAN may support nuclear trafficking, RRM2 may supply deoxyribonucleotides, RACGAP1 may couple the state to cytokinesis, PSMG1-PSMA1 may support proteasome maturation, and MAP4K4-PPP4C or RDX-VCL may connect signaling to adhesion and cytoskeletal behavior. The HPA enrichment for spermatogenic and progenitor-like cell types suggests that this state may be particularly visible in cells undergoing differentiation or proliferation, but the module should be tested experimentally rather than interpreted as a dedicated stem-cell or germ-cell program.

### Important genes

#### KPNA2

- **Related proteins** (co-abundance neighbors): UBE2D1 (0.88); STRING partners: RACGAP1 (0.714), RAN (0.944), RRM2 (0.743)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10000.1, huMAP3_12581.1
- **Function (MyGene.info)**: karyopherin subunit alpha 2. The import of proteins into the nucleus is a process that involves at least 2 steps. The first is an energy-independent docking of the protein to the nuclear envelope and the second is an energy-dependent translocation through the nuclear pore complex. Imported proteins require a nuclear localization sequence (NLS) which generally consists of a short region of basic amino acids or 2 such regions s…
- **Diseases (Open Targets)**: severe acute respiratory syndrome (0.462); Orthomyxoviridae infectious disease (0.462); dengue disease (0.462); COVID-19 (0.373); non-alcoholic fatty liver (0.324)
- **Europe PMC papers**: 2442
- **Why important**: KPNA2 is a central bridge in the module's known-interaction evidence: STRING links it to RAN, RACGAP1 and RRM2, and hu.MAP places it with RAN in nuclear-transport complexes (hu.MAP huMAP3_10000.1) and (hu.MAP huMAP3_12581.1). Its established function is import of proteins carrying nuclear localization signals. HPA shows testis enhancement and enhancement in several germ-cell and trophoblast-related cell types, while the literature volume is substantial.
- **Conclusion**: Established evidence supports KPNA2 as a nuclear-import component that connects transport to other module neighborhoods. Hypothesis: its co-abundance may mark increased nuclear trafficking during proliferative or differentiating states. The module does not prove that KPNA2 regulates the other genes directly.

#### RAN

- **Related proteins** (co-abundance neighbors): UBE2D1 (0.85); STRING partners: KPNA2 (0.944)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10000.1, huMAP3_12581.1
- **Function (MyGene.info)**: RAN, member RAS oncogene family. RAN (ras-related nuclear protein) is a small GTP binding protein belonging to the RAS superfamily that is essential for the translocation of RNA and proteins through the nuclear pore complex. The RAN protein is also involved in control of DNA synthesis and cell cycle progression. Nuclear localization of RAN requires the presence of regulator of chromosome condensation 1 (RCC1). Mutations in RAN di…
- **Diseases (Open Targets)**: HIV infectious disease (0.565); Orthomyxoviridae infectious disease (0.376); pemphigus foliaceus (0.298); neurodegenerative disease (0.270); Genu valgum (0.136)
- **Europe PMC papers**: 133080
- **Why important**: RAN is the most extensively studied gene among the selected representatives and has a strong known STRING relationship with KPNA2. It is a small GTP-binding protein required for nuclear and ribosomal transport and is also involved in DNA synthesis and cell-cycle progression. HPA places it in several progenitor, trophoblast and spermatocyte-related cell types.
- **Conclusion**: Established evidence supports RAN as a plausible transport and cell-cycle anchor. Hypothesis: coordinated RAN and KPNA2 abundance could reflect increased nuclear exchange in the shared cellular state. Co-abundance alone cannot establish altered RAN activity or GTP loading.

#### RRM2

- **Related proteins** (co-abundance neighbors): UBE2D1 (0.91), PLEKHA8 (0.88); STRING partners: KPNA2 (0.743), RACGAP1 (0.789)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribonucleotide reductase regulatory subunit M2. This gene encodes one of two non-identical subunits for ribonucleotide reductase. This reductase catalyzes the formation of deoxyribonucleotides from ribonucleotides. Synthesis of the encoded protein (M2) is regulated in a cell-cycle dependent fashion. Transcription from this gene can initiate from alternative promoters, which results in two isoforms that differ in the lengths of their N-termini. …
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.622); B-cell chronic lymphocytic leukemia (0.593); sickle cell disease (0.581); melanoma (0.580); exocrine pancreatic carcinoma (0.580)
- **Europe PMC papers**: 8185
- **Why important**: RRM2 supplies one subunit of ribonucleotide reductase and is required for deoxyribonucleotide production, DNA synthesis and DNA repair. It connects in STRING to KPNA2 and RACGAP1 and is co-abundant with UBE2D1 and PLEKHA8 in the module network. HPA shows enhancement in bone marrow and lymphoid tissue and in several progenitor or trophoblast-related cell types. It also has a large disease and literature record.
- **Conclusion**: Established evidence supports RRM2 as a marker of nucleotide demand and genome duplication or repair. Hypothesis: RRM2 may help explain the module's association with proliferative or differentiating cells. The data do not show that DNA replication is the sole or statistically enriched function of the module.

#### PSMG1

- **Related proteins** (co-abundance neighbors): UBE2D1 (0.82); STRING partners: PSMA1 (0.935)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_00356.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome assembly chaperone 1. Enables molecular adaptor activity. Involved in chaperone-mediated protein complex assembly. Located in several cellular components, including Golgi apparatus; endoplasmic reticulum; and nucleoplasm. Part of chaperone complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.541); intelligence (0.326); smoking initiation (0.322); atrial fibrillation (0.312); attention deficit-hyperactivity disorder (0.240)
- **Europe PMC papers**: 358
- **Why important**: PSMG1 is a proteasome assembly chaperone and is paired with PSMA1 by high-confidence STRING evidence. Both genes occur together in several hu.MAP proteasome-related complexes (hu.MAP huMAP3_00356.1), (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1). HPA shows testis enhancement and enhancement in spermatids, spermatocytes and oocytes, making it relevant to the recurring reproductive-cell pattern.
- **Conclusion**: Established evidence supports PSMG1 as evidence for proteasome maturation and protein-quality control within one module neighborhood. Hypothesis: elevated proteasome assembly capacity may help cells manage increased protein turnover during proliferation or differentiation. The limited complex overlap means this does not establish that the full module is a proteasome module.

#### MAP4K4

- **Related proteins** (co-abundance neighbors): C2CD3 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09709.1, huMAP3_10333.1, huMAP3_13510.1
- **Function (MyGene.info)**: mitogen-activated protein kinase kinase kinase kinase 4. The protein encoded by this gene is a member of the serine/threonine protein kinase family. This kinase has been shown to specifically activate MAPK8/JNK. The activation of MAPK8 by this kinase is found to be inhibited by the dominant-negative mutants of MAP3K7/TAK1, MAP2K4/MKK4, and MAP2K7/MKK7, which suggests that this kinase may function through the MAP3K7-MAP2K4-MAP2K7 kinase cascade, and medi…
- **Diseases (Open Targets)**: neurodegenerative disease (0.572); hereditary disease (0.527); multiple congenital anomalies/dysmorphic syndrome-intellectual disability (0.503); RASopathy (0.400); asthma (0.372)
- **Europe PMC papers**: 2843
- **Why important**: MAP4K4 is a serine/threonine kinase linked to MAPK signaling, cell migration, cell-matrix adhesion and Hippo-related signaling. It is connected in the module to C2CD3 and appears with PPP4C in several hu.MAP complexes (hu.MAP huMAP3_09709.1), (hu.MAP huMAP3_10333.1) and (hu.MAP huMAP3_13510.1). HPA shows brain tissue enhancement and enhancement in microglia, monocytes, neutrophils and oligodendrocytes. Its disease-association and literature evidence are substantial.
- **Conclusion**: Established evidence supports MAP4K4 as a signaling and cytoskeletal-regulatory component rather than a core member of the proteasome or nuclear-transport neighborhoods. Hypothesis: MAP4K4 may provide a signaling interface linking the shared cellular state to migration or adhesion. The module does not establish activation of the MAPK pathway.

## Module 2

**Tissue pair**: cell line and stem_cells  
**Genes (41)**: ABCB7, PRMT7, ARHGEF2, ATF7, ATG12, CDC42EP4, CARD11, CENPK, CHCHD5, CWC22, DCP1A, DPYSL5, FZD7, GON7, IFT54, PRKACG, CSNK1E, KRTCAP3, KIDINS220, KDM2B, KIRREL1, LIMK2, MAPKAPK5, MCM6, TWNK, PDCL, POT1, PIP4P2, PTGIS, SCOC, SYNGR3, PIPOX, STK38L, STK39, TARS2, GTF3C5, TMUB1, UCK1, WEE1, XPO6, ZSCAN18

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent. Therefore, the module has no statistically established pathway-level function from enrichment. Gene-level annotations suggest a heterogeneous signaling and cell-state program involving cyclic-AMP and protein phosphorylation through PRKACG and CSNK1E, Wnt signaling through FZD7, prostacyclin and lipid metabolism through PTGIS, ciliary transport through IFT54, cell-cycle and genome maintenance through WEE1, MCM6, CENPK and POT1, and neuronal or vesicular biology through SYNGR3 and KIDINS220. These themes are distributed across weakly connected neighborhoods, so they should be regarded as biological context rather than a definitive module annotation.

**Cell composition.** The module is not dominated by plasma or secreted proteins: HPA reports no secreted genes. Most genes have low tissue specificity. The more prominent tissue and cell-type signals include lymphoid tissue, brain, blood vessel, bone marrow, germ-cell populations and neutrophils. Overall immune-cell specificity is mostly low, although several genes are enhanced or enriched in neutrophils, plasmacytoid dendritic cells and other immune populations. Thus, the module does not strongly resemble a plasma-protein module or a purely blood-cell module. It may instead reflect broadly expressed cellular machinery combined with variable representation of immune, neural, vascular or germ-cell-like states. Matched protein-detection data for the cell line and stem-cell contexts were unavailable, so they do not provide additional evidence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides limited prior interaction support. The only high-confidence STRING relationship is between CSNK1E and PRKACG, linking two signaling genes that are also prominent in the module topology. STRING functional enrichment was absent. hu.MAP identifies complex huMAP3_10725.1, with TMUB1 and KIDINS220 represented in the module (hu.MAP huMAP3_10725.1); the other listed complex members are outside the module. This supports a possible membrane, trafficking or signaling-complex context, but only a small part of the complex is represented. Most module edges therefore appear to be co-abundance relationships rather than established physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 820 gene pairs: CSNK1E–PRKACG (0.914)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10725.1 (TMUB1, KIDINS220; 2/59)

### Novelty

The cross-context co-abundance pattern may be a previously unreported observational module, but it cannot be called a new molecular complex or pathway on the present evidence. The limited STRING connectivity, absent STRING enrichment, absence of globally significant GO or KEGG terms, and small hu.MAP overlap argue against a canonical established module. However, absence from STRING or hu.MAP does not prove novelty, because co-abundance can reflect shared regulation, indirect signaling, cell-state composition or context-specific biology. The defensible conclusion is that the module is potentially novel as an observational pattern, while its mechanism remains unvalidated.

**Hypothesis.** Hypothesis: the module may represent a heterogeneous signaling-and-maintenance state in which cyclic-AMP and casein-kinase signaling intersect with Wnt receptor activity, prostacyclin metabolism, ciliary transport, vesicle biology and cell-cycle control. PRKACG and CSNK1E may form a signaling backbone, while FZD7 and PTGIS provide receptor and lipid-mediated inputs. IFT54, SYNGR3 and KIDINS220 may connect this state to cilia, trafficking or neuronal-like membrane organization. The mixture of broadly expressed genes and cell-type-enhanced genes suggests a shared differentiation or signaling state rather than a dedicated pathway. This hypothesis should be tested by replication in independent datasets, perturbation of the kinase and receptor components, and assessment of whether the module tracks a specific cell state or sample composition.

### Important genes

#### PRKACG

- **Related proteins** (co-abundance neighbors): LIMK2 (0.97), STK38L (0.94), STK39 (0.92), PIP4P2 (0.88), CENPK (0.87), CHCHD5 (0.83), IFT54 (0.82), PTGIS (0.82), ABCB7 (0.81), TARS2 (0.81), ATG12 (0.80); STRING partners: CSNK1E (0.914)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase cAMP-activated catalytic subunit gamma. Cyclic AMP-dependent protein kinase (PKA) consists of two catalytic subunits and a regulatory subunit dimer. This gene encodes the gamma form of its catalytic subunit. The gene is intronless and is thought to be a retrotransposon derived from the gene for the alpha form of the PKA catalytic subunit. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: platelet-type bleeding disorder 19 (0.503); Rare hemorrhagic disorder due to a constitutional platelet anomaly (0.462); neurodegenerative disease (0.241); nephrolithiasis (0.183); lymphoma (0.037)
- **Europe PMC papers**: 665
- **Why important**: PRKACG has the strongest network position in the module and connects to kinase, cytoskeletal, lipid-signaling and ciliary-associated genes. It encodes the gamma catalytic subunit of protein kinase A and is annotated to cyclic-AMP receptor signaling, spermatogenesis and insulin secretion. It is tissue-enriched in testis-related contexts and has substantial literature and disease associations involving platelet and hemorrhagic disorders.
- **Conclusion**: Established evidence supports PRKACG as a central signaling kinase and plausible module anchor. Its proposed role in linking cyclic-AMP signaling to the other module neighborhoods is biologically plausible, but this dataset does not demonstrate a physical or causal relationship.

#### CSNK1E

- **Related proteins** (co-abundance neighbors): PTGIS (0.89), FZD7 (0.88), XPO6 (0.86), SCOC (0.84), IFT54 (0.81); STRING partners: PRKACG (0.914)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: casein kinase 1 epsilon. The protein encoded by this gene is a serine/threonine protein kinase and a member of the casein kinase I protein family, whose members have been implicated in the control of cytoplasmic and nuclear processes, including DNA replication and repair. The encoded protein is found in the cytoplasm as a monomer and can phosphorylate a variety of proteins, including itself. This protein has been shown to…
- **Diseases (Open Targets)**: follicular lymphoma (0.524); marginal zone lymphoma (0.476); neoplasm (0.390); neurodegenerative disease (0.371); B-cell chronic lymphocytic leukemia (0.341)
- **Europe PMC papers**: 1420
- **Why important**: CSNK1E is connected to several module neighborhoods and has the only high-confidence STRING interaction in the module, with PRKACG. It is an established serine/threonine kinase involved in phosphorylation, DNA repair, signal transduction, proteasomal regulation and Wnt signaling. It has substantial literature and disease associations involving lymphoma, leukemia, neoplasia and neurodegenerative disease.
- **Conclusion**: Established evidence makes CSNK1E a strong candidate for coordinating signaling within the module, particularly with PRKACG and FZD7. A module-level regulatory role remains hypothetical because global enrichment and broader physical-interaction support are absent.

#### FZD7

- **Related proteins** (co-abundance neighbors): GON7 (0.89), CSNK1E (0.88), GTF3C5 (0.87), CWC22 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: frizzled class receptor 7. Members of the 'frizzled' gene family encode 7-transmembrane domain proteins that are receptors for Wnt signaling proteins.  The FZD7 protein contains an N-terminal signal sequence, 10 cysteine residues typical of the cysteine-rich extracellular domain of Fz family members, 7 putative transmembrane domains, and an intracellular C-terminal tail with a PDZ domain-binding motif.  FZD7 gene expression…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.462); attention deficit-hyperactivity disorder (0.244); uterine corpus leiomyoma (0.243); substance abuse (0.243); bone fracture (0.223)
- **Europe PMC papers**: 3473
- **Why important**: FZD7 is a receptor-level component connecting the module to Wnt signaling and stem-cell population maintenance. It encodes a seven-transmembrane Wnt receptor annotated to receptor signaling, non-canonical Wnt signaling and neuron differentiation. It has extensive literature and disease associations, and its connection to CSNK1E provides a plausible signaling bridge.
- **Conclusion**: Established evidence supports FZD7 as a biologically meaningful signaling input and candidate contributor to the shared stem-cell-associated state. It is not established that Wnt signaling defines the whole module because no GO or KEGG term passed global correction.

#### PTGIS

- **Related proteins** (co-abundance neighbors): MAPKAPK5 (0.91), CSNK1E (0.89), PRKACG (0.82), CWC22 (0.82), IFT54 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prostaglandin I2 synthase. This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. However, this protein is considered a member of the cytochrome P450 superfamily on the basis of sequence similarity rather than functional similarity. This endopla…
- **Diseases (Open Targets)**: essential hypertension (0.410); coronary artery bypass (0.307); schizophrenia (0.286); mixed connective tissue disease (0.273); Rare pervasive developmental disorder (0.267)
- **Europe PMC papers**: 1485
- **Why important**: PTGIS connects to the kinase-centered portion of the network and to MAPKAPK5. It encodes prostaglandin I2 synthase, an endoplasmic-reticulum enzyme involved in prostacyclin production and prostaglandin, lipid and icosanoid metabolism. It is tissue-enhanced in blood vessel and several stromal or vascular-associated cell types and has substantial literature and disease associations involving vascular and inflammatory conditions.
- **Conclusion**: Established evidence supports PTGIS as a vascular and lipid-signaling component that may provide a context-sensitive extracellular-response dimension. Its functional partnership with the kinase and Wnt neighborhoods is a co-abundance hypothesis rather than a demonstrated biochemical interaction.

#### IFT54

- **Related proteins** (co-abundance neighbors): PIPOX (0.92), PRKACG (0.82), CSNK1E (0.81), PTGIS (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nuclear bodies, Primary cilium transition zone; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: intraflagellar transport 54. The protein encoded by this gene interacts with TNF receptor-associated factor 3, tethering it to cytoskeletal microtubules. The encoded protein is also an inhibitor of the innate type I IFN response. Defects in this gene are a cause of Senior-Loken syndrome 9. [provided by RefSeq, Mar 2017].
- **Diseases (Open Targets)**: Senior-Loken syndrome (0.683); Senior-Loken syndrome 9 (0.611); Jeune syndrome (0.418); short-rib thoracic dysplasia 6 with or without polydactyly (0.416); short rib-polydactyly syndrome, Majewski type (0.370)
- **Europe PMC papers**: 166
- **Why important**: IFT54 connects PRKACG, CSNK1E and PTGIS and is annotated to the primary-cilium transition zone, intraciliary anterograde transport, polarized epithelial morphogenesis and regulation of type I interferon production. It is enhanced in several ciliated cell types and is associated with Senior-Loken syndrome and related ciliopathies. Its compartment specificity makes it informative despite a smaller literature base than the major kinases.
- **Conclusion**: Established evidence supports IFT54 as a ciliary and epithelial-organization component with a direct disease connection. The idea that ciliary signaling connects FZD7, kinase activity and prostacyclin-related biology is plausible, but not established by the module.

#### CARD11

- **Related proteins** (co-abundance neighbors): SCOC (0.94), TWNK (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caspase recruitment domain family member 11. The protein encoded by this gene belongs to the membrane-associated guanylate kinase (MAGUK) family, a class of proteins that functions as molecular scaffolds for the assembly of multiprotein complexes at specialized regions of the plasma membrane. This protein is also a member of the CARD protein family, which is defined by carrying a characteristic caspase-associated recruitment domain (CARD). T…
- **Diseases (Open Targets)**: severe combined immunodeficiency due to CARD11 deficiency (0.785); BENTA disease (0.780); immunodeficiency 11b with atopic dermatitis (0.700); diffuse large B-cell lymphoma (0.514); asthma (0.509)
- **Europe PMC papers**: 3551
- **Why important**: CARD11 provides an immune-signaling anchor. It is enhanced in lymphoid tissue and intestine and in B cells, innate lymphoid cells, microglia and NK cells. It is annotated to canonical NF-kappaB signaling, T-cell costimulation and TORC1 signaling, and has strong disease associations involving immunodeficiency, BENTA disease, atopic dermatitis and diffuse large B-cell lymphoma. Its limited direct connectivity suggests that immune biology may be peripheral or composition-related rather than the module core.
- **Conclusion**: Established evidence supports CARD11 as an immune-cell signaling gene with strong disease relevance. Its presence does not prove that the module is an immune module; it may reflect a shared cell state or sample composition. A causal role in the complete module remains hypothetical.

## Module 3

**Tissue pair**: cell line and stem_cells  
**Genes (5)**: ABCD3, ADAM9, LARP7, MYOF, TBL2

### Function

The module does not have a statistically supported GO or KEGG functional label: no GO or KEGG term passed global correction. Its gene composition and sparse network instead suggest a possible connection among membrane biology, lipid and peroxisomal metabolism, extracellular proteolysis, and transcriptional regulation. ABCD3 provides the clearest metabolic anchor through peroxisomal transport of fatty acids and its links to fatty acid oxidation, lipid transport, bile acid biosynthesis, and peroxisome organization. MYOF and ADAM9 provide membrane-associated components, while LARP7 represents RNA polymerase II transcriptional control and TBL2 has annotations related to cellular responses to unfolded protein, glucose starvation, and hypoxia. These annotations support a biologically heterogeneous module rather than a confidently defined single process.

**Cell composition.** The module is not dominated by secreted proteins: only ADAM9 is annotated as secreted, with unknown location. It is also not strongly blood-cell enriched overall. Most genes have low tissue or immune-cell specificity, although MYOF and ADAM9 show cell-type enhancement in epithelial populations and monocytes, TBL2 is enriched in testis germ-cell populations, and ABCD3 is enhanced in liver. The pattern is therefore compatible with broadly expressed intracellular and membrane biology with contributions from tissue-specific cell states, rather than being clearly explained by plasma proteins or a blood-cell contaminant. Protein detection data for the matched cell line and stem-cell contexts provide no additional evidence because all entries are reported as having no available matching tissue data.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional enrichment and no high-confidence STRING pairwise interactions were reported. Thus, STRING does not independently support a densely connected known interaction network for this module. The principal external complex evidence is hu.MAP complex (hu.MAP huMAP3_09359.1), which contains ABCD3 and MYOF together with other proteins. This supports a possible shared complex or cellular compartment context for those two genes, but only a minority of that complex is represented in the module, so it should not be interpreted as a complete complex or as proof that all module edges are physical interactions. The co-abundance edges may therefore reflect coordinated regulation, shared cell state, or compartmental biology rather than established direct binding relationships.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09359.1 (ABCD3, MYOF; 2/13)

### Novelty

The module may represent a previously unrecognized co-abundance relationship, because its particular combination of genes has no reported high-confidence STRING interaction pairs or STRING enrichment and only partial overlap with the hu.MAP complex (hu.MAP huMAP3_09359.1). However, this is not sufficient to claim a new biological pathway. Several genes have substantial prior literature and established individual functions, and the module lacks globally significant GO or KEGG enrichment. The most defensible conclusion is that the coordinated expression pattern is potentially novel, while the underlying gene functions and the ABCD3–MYOF complex context are not novel. Independent replication, tissue- or state-specific testing, and experimental interaction or perturbation studies would be needed to establish novelty.

**Hypothesis.** Hypothesis: the module reflects coordination between peroxisomal lipid handling, membrane remodeling or repair, extracellular proteolysis, and cellular stress or transcriptional state. In this model, ABCD3 marks lipid and peroxisomal metabolism; MYOF and ADAM9 mark membrane trafficking, membrane repair, adhesion, and ectodomain processing; TBL2 may connect the state to metabolic or stress responses; and LARP7 may modulate transcriptional elongation through the seven-SK ribonucleoprotein system. The hypothesized coordination could arise from a shared differentiated or stress-responsive cell state rather than from one physical multiprotein complex. This remains a hypothesis because the module has no globally significant enrichment and no STRING-supported pairwise interactions.

### Important genes

#### ABCD3

- **Related proteins** (co-abundance neighbors): LARP7 (0.81), TBL2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Peroxisomes; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09359.1
- **Function (MyGene.info)**: ATP binding cassette subfamily D member 3. The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the ALD subfamily, which is involved in peroxisomal import of fatty acids and/…
- **Diseases (Open Targets)**: congenital bile acid synthesis defect 5 (0.454); oculopharyngodistal myopathy (0.380); Abnormality of the skeletal system (0.359); food allergy (0.097); colorectal carcinoma (0.097)
- **Europe PMC papers**: 1205
- **Why important**: ABCD3 is a strong functional anchor because it is annotated to peroxisomal import of fatty acids or fatty acyl-CoAs, lipid transport, fatty acid oxidation, bile acid biosynthesis, and peroxisome organization. It occupies an internal network position, connects to TBL2, and is one of the two module members in hu.MAP complex (hu.MAP huMAP3_09359.1). Its liver-enhanced expression and substantial literature support make it particularly informative for interpreting the module. Its disease associations include congenital bile acid synthesis defect and other disorders.
- **Conclusion**: Established evidence supports ABCD3 as the module's principal peroxisomal and lipid-metabolic component. The hypothesis that it organizes the broader module around lipid stress or metabolic state is plausible but not established by the available network or enrichment evidence.

#### MYOF

- **Related proteins** (co-abundance neighbors): ADAM9 (0.82), TBL2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Plasma membrane, Centriolar satellite; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09359.1
- **Function (MyGene.info)**: myoferlin. Mutations in dysferlin, a protein associated with the plasma membrane, can cause muscle weakness that affects both proximal and distal muscles. The protein encoded by this gene is a type II membrane protein that is structurally similar to dysferlin. It is a member of the ferlin family and associates with both plasma and nuclear membranes. The protein contains C2 domains that play a role in calcium…
- **Diseases (Open Targets)**: hereditary angioedema (0.443); neurodegenerative disease (0.413); cervical carcinoma (0.134); type 2 diabetes mellitus (0.131); neoplasm (0.112)
- **Europe PMC papers**: 1200
- **Why important**: MYOF is the most connected membrane-associated node in the module and links to ADAM9 and TBL2. It is a ferlin-family type membrane protein with C two domains implicated in calcium-mediated membrane fusion, and its annotations include plasma membrane repair, muscle contraction, blood circulation, and regulation of neurotransmitter secretion. It is also the second module member in hu.MAP complex (hu.MAP huMAP3_09359.1). Its relatively extensive literature and disease associations, including hereditary angioedema and neurodegenerative disease, make it an important bridge between membrane biology and the rest of the module.
- **Conclusion**: Established evidence supports MYOF as a membrane repair and membrane-fusion component with a central position in the co-abundance network. Its proposed role as the physical membrane interface connecting metabolic and proteolytic signals is a hypothesis, not a demonstrated mechanism here.

#### ADAM9

- **Related proteins** (co-abundance neighbors): MYOF (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ADAM metallopeptidase domain 9. This gene encodes a member of the ADAM (a disintegrin and metalloprotease domain) family. Members of this family are membrane-anchored proteins structurally related to snake venom disintegrins, and have been implicated in a variety of biological processes involving cell-cell and cell-matrix interactions, including fertilization, muscle development, and neurogenesis. The protein encoded by this gen…
- **Diseases (Open Targets)**: cone-rod dystrophy (0.718); retinitis pigmentosa (0.504); Abnormality of the skeletal system (0.464); inherited retinal dystrophy (0.373); autosomal recessive cone rod dystrophy (0.370)
- **Europe PMC papers**: 2887
- **Why important**: ADAM9 is the module's secreted or extracellularly relevant component and is connected to MYOF. Its established annotations include proteolysis, membrane-protein ectodomain proteolysis, cell adhesion, cell-matrix adhesion, transforming growth factor beta receptor signaling, and integrin-mediated signaling. HPA reports cell-type enhancement in endometrial and urothelial epithelial populations and immune enhancement in classical monocytes. It also has the largest literature volume among the module genes and disease associations involving inherited retinal degeneration.
- **Conclusion**: Established evidence supports ADAM9 as a proteolytic and adhesion-related membrane or extracellular regulator. Its connection to MYOF may indicate coordinated membrane remodeling, but the available data do not establish a direct interaction or show that ADAM9 drives the entire module.

#### LARP7

- **Related proteins** (co-abundance neighbors): ABCD3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: La ribonucleoprotein 7, transcriptional regulator. This gene encodes a protein which is found in the 7SK snRNP (small nuclear ribonucleoprotein). This snRNP complex inhibits a cyclin-dependent kinase, positive transcription elongation factor b, which is required for paused RNA polymerase II at a promoter to begin transcription elongation. A pseudogene of this gene is located on chromosome 3. Alternative splicing results in multiple transcript vari…
- **Diseases (Open Targets)**: microcephalic primordial dwarfism, Alazami type (0.791); Intellectual disability (0.484); hereditary disease (0.415); isolated growth hormone deficiency type IA (0.373); Epileptic encephalopathy (0.340)
- **Europe PMC papers**: 892
- **Why important**: LARP7 is connected to ABCD3 and encodes a component of the seven-SK ribonucleoprotein system that inhibits positive transcription elongation factor b. Its annotations include negative regulation of RNA polymerase II transcription elongation, RNA processing, and spermatogenesis. It has substantial literature and disease associations including microcephalic primordial dwarfism and intellectual disability. Its presence adds a nuclear regulatory layer to a module otherwise marked by membrane and metabolic genes.
- **Conclusion**: Established evidence supports LARP7 as a transcriptional elongation and RNA-processing regulator. Its co-abundance with ABCD3 could reflect shared cellular state or coordinated transcriptional control, but a mechanistic connection to peroxisomal metabolism is only hypothesized.

#### TBL2

- **Related proteins** (co-abundance neighbors): MYOF (0.82), ABCD3 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transducin beta like 2. This gene encodes a member of the beta-transducin protein family. Most proteins of the beta-transducin family are involved in regulatory functions. This protein is possibly involved in some intracellular signaling pathway. This gene is deleted in Williams-Beuren syndrome, a developmental disorder caused by deletion of multiple genes at 7q11.23. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: gout (0.305); physical activity (0.280); type 2 diabetes mellitus (0.257); Abnormality of the skeletal system (0.243); diabetes mellitus (0.200)
- **Europe PMC papers**: 346
- **Why important**: TBL2 is an internal network node linking MYOF with ABCD3. It belongs to the beta-transducin protein family and is annotated with cellular responses to unfolded protein, glucose starvation, and hypoxia. HPA reports tissue enhancement in testis and enrichment in spermatogenic cell populations. Its disease associations include gout, type two diabetes, and skeletal abnormalities, providing a possible link between metabolic state and cell-type context.
- **Conclusion**: Established evidence supports TBL2 as a regulatory protein associated with metabolic and cellular stress responses. Its network position makes it a plausible connector between ABCD3 and MYOF, but the fact sheet does not establish whether it mediates that relationship or merely shares a regulated expression state.

## Module 5

**Tissue pair**: cell line and stem_cells  
**Genes (5)**: ACADSB, DNAJB14, MYO18A, NDUFS5, SHQ1

### Function

The module does not support a single statistically established GO or KEGG function: no GO or KEGG term passed global correction. Its genes represent several established cellular activities: SHQ1 supports H/ACA ribonucleoprotein assembly and telomerase RNA localization; DNAJB14 supports endoplasmic-reticulum protein folding and complex assembly; ACADSB supports short and branched-chain acyl-CoA and amino-acid or fatty-acid catabolism; NDUFS5 is a component of mitochondrial respiratory complex I; and MYO18A participates in Golgi organization, actomyosin organization, and cell migration. The co-abundance structure is therefore better interpreted as a small cross-compartment cellular-state module than as evidence for one canonical pathway. SHQ1 is the network hub, whereas the other genes are singly connected to it.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary identifies no secreted genes. It also does not resemble a blood-cell-enriched module. Most genes have low immune-cell specificity, one is not detected in immune cells, and no enriched blood-cell category is reported. Most genes have low tissue specificity, while ACADSB is liver and hepatocyte associated and MYO18A is enhanced in skeletal muscle and tongue and in several differentiated cell types including cardiomyocytes and myonuclei. These observations argue against a simple blood-contamination explanation. They instead suggest a mixture of broadly expressed cellular machinery with tissue- or cell-state-associated contributions. The HPA protein-detection fields do not provide matching cell-line or stem-cell tissue evidence, so protein-level expression in the two sampled groups cannot be inferred from those fields.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module gene pair reaches the supplied STRING interaction threshold, and no STRING functional-enrichment result is present. No hu.MAP complex contains multiple module members. Thus, the four co-abundance edges should be treated as dataset-level co-variation rather than established physical interactions. The individual annotations do establish that several genes belong to larger cellular systems, including H/ACA ribonucleoprotein biology, endoplasmic-reticulum chaperone biology, mitochondrial complex I, and cytoskeletal or Golgi processes, but the supplied databases do not establish that these five proteins form one molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a novel co-abundance pattern in this cell-line and stem-cell comparison, but the evidence is insufficient to call it a newly discovered biological pathway or complex. The absence of STRING interactions and hu.MAP co-membership supports the observation that this particular gene combination is not represented as a known interaction module, but database absence alone does not prove novelty. The lack of globally significant GO or KEGG enrichment, the small and cross-compartment composition, and the presence of well-characterized genes with unrelated established functions all favor describing it as a potentially novel dataset-specific association that requires replication. A stronger novelty claim would require independent cohorts, preservation across datasets, control for cell composition, and experimental testing of the co-abundance relationships.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-maintenance or cell-state program rather than a direct biochemical complex. In this model, SHQ1-linked variation tracks a state in which RNA or ribonucleoprotein assembly, endoplasmic-reticulum proteostasis, mitochondrial energy metabolism, and Golgi or actomyosin organization covary across cell-line and stem-cell samples. The apparent hub role of SHQ1 may be statistical coordination caused by shared regulation, cellular state, or sample composition, not a physical bridge among all partners. This hypothesis predicts that the module should be tested by replication in independent cell-line and stem-cell data, examination of sample-level cell-state covariates, and targeted assays for the relevant RNA-assembly, proteostasis, mitochondrial, and cytoskeletal programs.

### Important genes

#### SHQ1

- **Related proteins** (co-abundance neighbors): DNAJB14 (0.85), ACADSB (0.85), NDUFS5 (0.84), MYO18A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SHQ1, H/ACA ribonucleoprotein assembly factor. SHQ1 assists in the assembly of H/ACA-box ribonucleoproteins that function in the processing of ribosomal RNAs, modification of spliceosomal small nuclear RNAs, and stabilization of telomerase (see MIM 602322) (Grozdanov et al., 2009 [PubMed 19383767]).[supplied by OMIM, Dec 2010].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dystonia and seizures (0.759); dystonia 35, childhood-onset (0.503); dystonia 28, childhood-onset (0.462); early-onset generalized limb-onset dystonia (0.370); type 2 diabetes mellitus (0.356)
- **Europe PMC papers**: 314
- **Why important**: SHQ1 is the central node of the supplied co-abundance subgraph and connects to every other module member. Its established function in H/ACA ribonucleoprotein assembly, protein-RNA complex assembly, and telomerase RNA localization gives it a plausible role in a broad cellular-maintenance program. It has substantial literature coverage and disease associations including neurodevelopmental disorder with dystonia and seizures and childhood-onset dystonia.
- **Conclusion**: Established: SHQ1 is the network hub and an H/ACA ribonucleoprotein assembly factor. Hypothesis: it may mark or help coordinate the shared cellular state represented by the module. The co-abundance data do not establish that SHQ1 physically interacts with the other four proteins.

#### ACADSB

- **Related proteins** (co-abundance neighbors): SHQ1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA dehydrogenase short/branched chain. Short/branched chain acyl-CoA dehydrogenase(ACADSB) is a member of the acyl-CoA dehydrogenase family of enzymes that catalyze the dehydrogenation of acyl-CoA derivatives in the metabolism of fatty acids or branch chained amino acids. Substrate specificity is the primary characteristic used to define members of this gene family. The ACADSB gene product has the greatest activity towards the short br…
- **Diseases (Open Targets)**: 2-methylbutyryl-CoA dehydrogenase deficiency (0.780); hereditary disease (0.311); malnutrition (0.166); microcephaly (0.111); nonpapillary renal cell carcinoma (0.081)
- **Europe PMC papers**: 1182
- **Why important**: ACADSB is directly connected to the hub and provides the clearest metabolic component of the module. Its established role is dehydrogenation of short and branched-chain acyl-CoA substrates, with functions in isoleucine catabolism and fatty-acid or carboxylic-acid metabolism. It has extensive literature coverage and a strong disease association with two-methylbutyryl-CoA dehydrogenase deficiency. Its liver and hepatocyte enrichment makes it informative for evaluating tissue or cell-state composition.
- **Conclusion**: Established: ACADSB is a mitochondrial metabolic enzyme associated with branched-chain substrate catabolism. Hypothesis: its co-variation with SHQ1 may indicate a shared metabolic state in the sampled cells rather than a direct interaction.

#### NDUFS5

- **Related proteins** (co-abundance neighbors): SHQ1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit S5. This gene is a member of the NADH dehydrogenase (ubiquinone) iron-sulfur protein family. The encoded protein is a subunit of the NADH:ubiquinone oxidoreductase (complex I), the first enzyme complex in the electron transport chain located in the inner mitochondrial membrane. Alternative splicing results in multiple transcript variants and pseudogenes have been identified on chromosomes 1, 4 and 17.…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.608); Parkinson disease (0.605); diabetes mellitus (0.578); neurodegenerative disease (0.576); Alzheimer disease (0.536)
- **Europe PMC papers**: 800
- **Why important**: NDUFS5 is directly connected to SHQ1 and represents mitochondrial respiratory machinery within the module. It is an NADH dehydrogenase subunit involved in complex I, mitochondrial electron transport, aerobic respiration, and respiratory-complex assembly. It has substantial literature coverage and disease associations involving diabetes, Parkinson disease, and neurodegenerative disease.
- **Conclusion**: Established: NDUFS5 is a component of mitochondrial complex I and supports oxidative-energy metabolism. Hypothesis: its association with SHQ1 may reflect coordinated demand for biosynthetic and respiratory capacity during a shared cellular state. No supplied evidence demonstrates a direct NDUFS5–SHQ1 molecular interaction.

#### MYO18A

- **Related proteins** (co-abundance neighbors): SHQ1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin XVIIIA. The protein encoded by this gene can bind GOLPH3, linking the Golgi to the cytoskeleton and influencing Golgi membrane trafficking. The encoded protein is also part of a complex that assembles lamellar actomyosin bundles and may be required for cell migration. [provided by RefSeq, Oct 2016].
- **Diseases (Open Targets)**: cancer (0.607); chronic myeloid leukemia (0.371); myelodysplastic syndrome (0.370); acute lymphoblastic leukemia (0.370); leukemia (0.370)
- **Europe PMC papers**: 734
- **Why important**: MYO18A is directly connected to SHQ1 and contributes a structural and trafficking dimension absent from the mitochondrial and RNA-assembly annotations. Its established functions include GOLPH3 binding, Golgi-to-cytoskeleton linkage, Golgi membrane trafficking, lamellar actomyosin organization, and cell migration. It has substantial literature coverage and associations with cancer and hematologic malignancies. Its enhancement in skeletal muscle, tongue, cardiomyocytes, and myonuclei makes it relevant to assessing differentiated cell-state contributions.
- **Conclusion**: Established: MYO18A participates in Golgi, cytoskeletal, and migration-related biology. Hypothesis: its co-abundance with SHQ1 may report coordinated remodeling or differentiation state rather than a shared physical complex.

#### DNAJB14

- **Related proteins** (co-abundance neighbors): SHQ1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DnaJ heat shock protein family (Hsp40) member B14. Enables Hsp70 protein binding activity. Involved in cellular protein-containing complex assembly and chaperone cofactor-dependent protein refolding. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.133); open-angle glaucoma (0.120); renal carcinoma (0.104); renal cell carcinoma (0.072); gout (0.050)
- **Europe PMC papers**: 226
- **Why important**: DNAJB14 is the sole module member connected only to SHQ1 and supplies an endoplasmic-reticulum proteostasis component. It is an Hsp40-family protein that enables Hsp70 binding and participates in protein folding, complex assembly, and responses to misfolded proteins. Its literature coverage is meaningful, although less extensive than that of several other module genes, and reported disease associations include skeletal abnormality, glaucoma, and renal carcinoma.
- **Conclusion**: Established: DNAJB14 is an endoplasmic-reticulum chaperone cofactor involved in protein quality control. Hypothesis: its association with SHQ1 may indicate that RNA-complex assembly and proteostasis vary together during a shared cellular stress or maturation state. The supplied evidence does not establish a direct physical interaction.

## Module 6

**Tissue pair**: cell line and stem_cells  
**Genes (5)**: ALDH1B1, HNRNPLL, NDUFV2, CHGB, SUCLG2

### Function

The module does not have a GO/KEGG term that passes global multiple-testing correction, so its function cannot be assigned from enrichment alone. At the gene level, it combines mitochondrial energy and intermediary metabolism, represented by SUCLG2, ALDH1B1, and NDUFV2, with RNA-splicing regulation represented by HNRNPLL and endocrine or neuronal secretory-vesicle biology represented by CHGB. The network is centered on CHGB, which is connected to every other module member, while the peripheral genes are otherwise weakly connected in the module. Overall, the evidence is most consistent with a mixed cellular-state or cell-type-associated co-abundance pattern rather than a single established pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only CHGB is annotated in the secretome, and it is described as intracellular and membrane-associated with vesicle localization. The genes show tissue-enhanced patterns involving adrenal gland, brain, pituitary gland, liver, and blood vessel, while single-cell enrichment includes endocrine, hepatic, intestinal, and other specialized cell types. All module genes have cell-type-enhanced annotations, but the blood-cell evidence does not support an immune-cell-dominated module: most have low immune-cell specificity and CHGB is not detected in immune cells. The composition therefore suggests specialized cellular states or mixed tissue-lineage signals more than blood contamination or a broadly expressed housekeeping program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship among module members is the interaction between NDUFV2 and SUCLG2. No STRING functional enrichment is reported, and no hu.MAP complex contains multiple module members. CHGB has no recorded STRING partners in the fact sheet, despite being the network hub in the co-abundance graph. Thus, the module contains one independently supported mitochondrial relationship, but most of its co-abundance edges are not supported by the listed physical-interaction or complex resources. This favors interpreting the graph primarily as coordinated abundance across the sampled cell-line and stem-cell data rather than as a demonstrated physical complex.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: NDUFV2–SUCLG2 (0.713)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a potentially interesting cross-context co-abundance pattern, but the fact sheet does not establish it as a new biological discovery. Its lack of a globally significant GO/KEGG term, lack of STRING enrichment, and absence of a multi-member hu.MAP complex limit pathway-level interpretation. The limited database support may reflect a novel co-regulation pattern, context-specific biology, indirect relationships, or data and annotation limitations. Novelty would require independent replication, comparison with prior co-expression or proteomic modules, and experimental testing of the proposed cross-compartment relationship.

**Hypothesis.** Hypothesis: in cell-line and stem-cell contexts, a shared cellular state may coordinate mitochondrial energy metabolism and aldehyde handling with endocrine or vesicle-associated programs, while also involving RNA-splicing regulation. CHGB may act as a cell-state marker or abundance-linked hub rather than a direct molecular bridge, with SUCLG2 and NDUFV2 providing the strongest evidence for a mitochondrial metabolic component. ALDH1B1 could reflect oxidative or aldehyde-processing demands, and HNRNPLL could reflect accompanying changes in RNA processing. This is a hypothesis based on co-abundance and annotations, not an established physical pathway.

### Important genes

#### CHGB

- **Related proteins** (co-abundance neighbors): SUCLG2 (0.87), HNRNPLL (0.83), ALDH1B1 (0.81), NDUFV2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromogranin B. This gene encodes a tyrosine-sulfated secretory protein abundant in peptidergic endocrine cells and neurons. This protein may serve as a precursor for regulatory peptides. [provided by RefSeq, Jan 2009].
- **Diseases (Open Targets)**: Meniere disease (0.190); prostate cancer (0.112); Familial prostate cancer (0.112); placenta praevia (0.112); hypertensive disorder (0.111)
- **Europe PMC papers**: 1555
- **Why important**: CHGB is the central node in the module co-abundance graph, connecting to every other member with the strongest overall network position. It encodes chromogranin B, a secretory protein abundant in peptidergic endocrine cells and neurons, and is associated with vesicles and endocrine or neuroendocrine cell types in HPA. It also has the largest literature volume among the module genes and disease associations including Meniere disease and prostate cancer.
- **Conclusion**: Established evidence supports CHGB as the module's co-abundance hub and as a marker of specialized endocrine or neuronal secretory biology. It is not established that CHGB mechanistically drives the mitochondrial, metabolic, or splicing associations in this module; its hub role may instead reflect shared cell state or lineage.

#### NDUFV2

- **Related proteins** (co-abundance neighbors): CHGB (0.81); STRING partners: SUCLG2 (0.713)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit V2. The NADH-ubiquinone oxidoreductase complex (complex I) of the mitochondrial respiratory chain catalyzes the transfer of electrons from NADH to ubiquinone, and consists of at least 43 subunits. The complex is located in the inner mitochondrial membrane. This gene encodes the 24 kDa subunit of complex I, and is involved in electron transfer. Mutations in this gene are implicated in Parkinson's disea…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 7 (0.717); mitochondrial complex I deficiency (0.623); type 2 diabetes mellitus (0.608); Parkinson disease (0.606); diabetes mellitus (0.579)
- **Europe PMC papers**: 1539
- **Why important**: NDUFV2 connects the module to mitochondrial respiratory-chain biology and is the partner in the only high-confidence STRING interaction listed for the module, with SUCLG2. Its annotations include mitochondrial electron transport, aerobic respiration, proton motive force-driven ATP synthesis, and complex-I-related disease associations including Parkinson disease and mitochondrial complex-I deficiency. It also has substantial literature support.
- **Conclusion**: Established evidence supports NDUFV2 as a complex-I and mitochondrial respiration gene and supports its database relationship with SUCLG2. Its connection to CHGB in the co-abundance network is not independently established as a physical interaction, so any link to secretory-vesicle biology remains a hypothesis.

#### SUCLG2

- **Related proteins** (co-abundance neighbors): CHGB (0.87); STRING partners: NDUFV2 (0.713)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase GDP-forming subunit beta. This gene encodes a GTP-specific beta subunit of succinyl-CoA synthetase. Succinyl-CoA synthetase catalyzes the reversible reaction involving the formation of succinyl-CoA and succinate. Alternate splicing results in multiple transcript variants. Pseudogenes of this gene are found on chromosomes 5 and 12. [provided by RefSeq, Apr 2010].
- **Diseases (Open Targets)**: smoking initiation (0.377); breast disorder (0.325); vitamin B deficiency (0.318); alcohol drinking (0.314); duodenal ulcer (0.270)
- **Europe PMC papers**: 1184
- **Why important**: SUCLG2 contributes a distinct mitochondrial metabolic function as the GDP-forming beta subunit of succinyl-CoA synthetase in the tricarboxylic acid cycle and succinyl-CoA metabolism. It is connected to NDUFV2 by the only listed high-confidence STRING interaction and is tissue-enhanced in liver, with hepatocyte and parietal-cell enrichment in HPA.
- **Conclusion**: Established evidence supports SUCLG2 as a mitochondrial tricarboxylic-acid-cycle enzyme component and supports its interaction with NDUFV2 in STRING. The co-abundance connection between SUCLG2 and CHGB is not validated by the listed complex resources; its interpretation as coordination with secretory biology remains a hypothesis.

#### ALDH1B1

- **Related proteins** (co-abundance neighbors): CHGB (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 1 family member B1. This protein belongs to the aldehyde dehydrogenases family of proteins. Aldehyde dehydrogenase is the second enzyme of the major oxidative pathway of alcohol metabolism. This gene does not contain introns in the coding sequence. The variation of this locus may affect the development of alcohol-related problems. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.496); alcohol drinking (0.435); non-neoplastic bile duct disorder (0.336); renal osteodystrophy (0.257); ovarian dysfunction (0.252)
- **Europe PMC papers**: 1095
- **Why important**: ALDH1B1 provides aldehyde and ethanol catabolic biology and is localized to mitochondria. Its HPA pattern includes liver and blood vessel tissue enhancement and enrichment in cholangiocytes, enteric stem cells, enteric transient amplifying cells, extravillous trophoblasts, and hepatic stellate cells. It is also associated with neurodegenerative disease, alcohol drinking, and non-neoplastic bile-duct disorder.
- **Conclusion**: Established evidence supports ALDH1B1 as a mitochondrial aldehyde-metabolism gene with relevance to hepatic and specialized progenitor-like cell contexts. Its direct functional relationship with CHGB or the other module members is not established by the supplied interaction resources; coordinated oxidative-stress or metabolic-state regulation is a hypothesis.

#### HNRNPLL

- **Related proteins** (co-abundance neighbors): CHGB (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L like. HNRNPLL is a master regulator of activation-induced alternative splicing in T cells. In particular, it alters splicing of CD45 (PTPRC; MIM 151460), a tyrosine phosphatase essential for T-cell development and activation (Oberdoerffer et al., 2008 [PubMed 18669861]).[supplied by OMIM, Aug 2008].
- **Diseases (Open Targets)**: placenta praevia (0.222); gastric ulcer (0.222); hemorrhage (0.222); post term pregnancy (0.079); kidney disorder (0.079)
- **Europe PMC papers**: 335
- **Why important**: HNRNPLL adds a regulatory layer distinct from the mitochondrial genes. It is a nucleoplasmic heterogeneous nuclear ribonucleoprotein involved in mRNA processing and alternative-splicing regulation, including activation-induced splicing of CD45 in T cells. It occupies a peripheral position connected only to CHGB, has specialized single-cell annotations, and has a smaller literature base than the other selected genes, making it informative as a possible state-associated regulatory component rather than a well-supported module core.
- **Conclusion**: Established evidence supports HNRNPLL as an RNA-splicing regulator. The module does not show globally significant enrichment for RNA processing, and the supplied data do not establish that HNRNPLL regulates the mitochondrial or secretory genes here. Its inclusion is therefore best viewed as a candidate marker of coordinated cell-state regulation.

## Module 7

**Tissue pair**: cell line and stem_cells  
**Genes (6)**: ANKRD39, GGT7, PRKCQ, MAPRE2, OIP5, PEG10

### Function

No GO/KEGG term passed global correction, and there are no supplementary STRING enrichment terms. The module therefore has no statistically supported pathway-level functional label from the supplied enrichment analyses. Its co-abundance structure is organized around PRKCQ, with connections to OIP5, ANKRD39, MAPRE2, and PEG10, while ANKRD39 connects to GGT7. The annotations suggest a heterogeneous combination of signaling, cell-cycle and chromatin organization, microtubule and spindle biology, imprinted-gene regulation, and glutathione-related metabolism. These annotations support biological plausibility, but they do not establish a single shared function for the module. The module may represent coordinated state variation rather than a canonical pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not predominantly blood-cell enriched. Most genes have low immune-cell specificity, although PRKCQ has group-enriched expression in several lymphoid populations and the module includes associations with NK-cell and T-cell populations. HPA tissue annotations are heterogeneous, including skeletal muscle, lymphoid tissue, tongue, brain, bone marrow, adrenal gland, placenta, and testis. Cell-type annotations are likewise diverse, with repeated associations to myonuclei, oocytes, and NK-cells alongside several specialized cell types. This pattern argues against a simple plasma-protein or generic blood-cell explanation, but shared cell-type composition or cellular-state differences in cell-line and stem-cell samples remain plausible confounders.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and no hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not supported by the supplied physical-interaction or curated-complex evidence. PRKCQ is the network hub, ANKRD39 is the only intermediate connector, and the remaining genes are peripheral in this subgraph. The absence of STRING and hu.MAP support means that the module should be interpreted as a coordinated expression or protein-abundance pattern, not as an established physical complex. It also limits claims that the genes act in one molecular pathway.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a novel co-abundance association in this tissue-pair analysis, because its particular gene combination has no reported STRING interactions, no shared hu.MAP complex, and no globally significant GO/KEGG enrichment. However, these observations do not prove novelty: database coverage is incomplete, co-abundance relationships can be indirect, and several member genes have well-established individual functions and literature. The defensible conclusion is that the module-level combination and its coordination across cell line and stem_cells appear insufficiently characterized, while its individual biological components are not novel.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program linking PRKCQ-associated signaling with proliferative or structural remodeling and stress-related metabolism. PRKCQ may provide the central signaling axis; OIP5 and MAPRE2 could mark chromatin, centrosomal, or mitotic organization; PEG10 could reflect developmental or vesicle-associated state regulation; and ANKRD39 with GGT7 could connect the pattern to protein-modification and glutathione-related processes. This is a hypothesis rather than an established pathway model, because there is no globally significant enrichment, no STRING support, and no hu.MAP complex support.

### Important genes

#### PRKCQ

- **Related proteins** (co-abundance neighbors): OIP5 (0.88), ANKRD39 (0.87), MAPRE2 (0.84), PEG10 (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Centriolar satellite; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase C theta. Protein kinase C (PKC) is a family of serine- and threonine-specific protein kinases that can be activated by calcium and the second messenger diacylglycerol. PKC family members phosphorylate a wide variety of protein targets and are known to be involved in diverse cellular signaling pathways. PKC family members also serve as major receptors for phorbol esters, a class of tumor promoters. Each mem…
- **Diseases (Open Targets)**: asthma (0.565); atopic eczema (0.552); acute myeloid leukemia (0.541); childhood onset asthma (0.482); mast cell leukemia (0.475)
- **Europe PMC papers**: 1961
- **Why important**: PRKCQ is the network hub, connecting four other module members with the strongest central position in the supplied subgraph. Its established protein-kinase function and roles in signal transduction, cell growth, transcriptional regulation, axon guidance, and telomere maintenance make it the most plausible organizing gene. It also has substantial literature and disease associations involving immune and inflammatory disorders and leukemia.
- **Conclusion**: Established evidence supports PRKCQ as a signaling kinase and as the structural hub of this module. The hypothesis that it drives coordination of the other genes is plausible from network position but is not demonstrated by the supplied interaction or enrichment data.

#### ANKRD39

- **Related proteins** (co-abundance neighbors): PRKCQ (0.87), GGT7 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ankyrin repeat domain 39. Predicted to contribute to ubiquitin-protein transferase activity. Predicted to be involved in protein K6-linked ubiquitination. Predicted to be part of BRCA1-A complex and BRCA1-BARD1 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: diabetes mellitus (0.320); metabolic syndrome (0.074); mathematical ability (0.031); pernicious anemia (0.021); prostate cancer (0.005)
- **Europe PMC papers**: 49
- **Why important**: ANKRD39 is the only connector between PRKCQ and GGT7, giving it a potentially important bridging position despite limited literature. Its annotation points to predicted ubiquitin-transferase-related activity and possible participation in BRCA-associated complexes. Its tissue and cell-type annotations are broad and include oocytes, melanocytes, and gastric chief cells, which may indicate state dependence rather than a narrowly defined lineage.
- **Conclusion**: Established evidence is limited and much of the functional annotation is predicted. Its bridge position makes it important for interpreting module topology, but a role linking kinase signaling to protein modification or glutathione biology remains a hypothesis.

#### OIP5

- **Related proteins** (co-abundance neighbors): PRKCQ (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Opa interacting protein 5. The protein encoded by this gene localizes to centromeres, where it is essential for recruitment of CENP-A through the mediator Holliday junction recognition protein. Expression of this gene is upregulated in several cancers, making it a putative therapeutic target. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.546); allergic rhinitis (0.141); neoplasm (0.115); breast carcinoma (0.112); breast cancer (0.109)
- **Europe PMC papers**: 1968
- **Why important**: OIP5 is directly connected to the PRKCQ hub and has substantial literature. Its established localization to centromeres and role in recruitment of CENP-A connect it to chromatin and cell-division biology. Its enhanced expression in bone marrow, skeletal muscle, and testis, together with associations with differentiating germ cells and cardiomyocytes, is consistent with proliferative or differentiation-related state variation.
- **Conclusion**: Established evidence supports OIP5 as a centromere and CENP-A-associated chromatin factor with cancer relevance. Its participation in a PRKCQ-centered module is not established; the proposed link to signaling-dependent cell-state control is a hypothesis.

#### MAPRE2

- **Related proteins** (co-abundance neighbors): PRKCQ (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: microtubule associated protein RP/EB family member 2. The protein encoded by this gene shares significant homology to the adenomatous polyposis coli (APC) protein-binding EB1 gene family. This protein is a microtubule-associated protein that is necessary for spindle symmetry during mitosis. It is thought to play a role in the tumorigenesis of colorectal cancers and the proliferative control of normal cells. Alternative splicing of this gene results i…
- **Diseases (Open Targets)**: multiple benign circumferential skin creases on limbs (0.746); skin creases, congenital symmetric circumferential, 2 (0.697); neurodegenerative disease (0.464); Brugada syndrome (0.388); developmental disability (0.340)
- **Europe PMC papers**: 475
- **Why important**: MAPRE2 is connected directly to PRKCQ and is annotated as a microtubule-associated protein involved in spindle symmetry, microtubule organization, and focal-adhesion-related processes. Its brain tissue association and cell-type enhancement in myonuclei, NK-cells, and retinal bipolar cells broaden the possible cellular contexts. Although its literature volume is more limited than that of PRKCQ, its structural function is highly relevant to a module containing a signaling hub and a chromatin or mitotic gene.
- **Conclusion**: Established evidence supports MAPRE2 as a microtubule and spindle regulator. A coordinated relationship with PRKCQ or OIP5 could indicate coupling between signaling and cytoskeletal or mitotic state, but the supplied data do not establish that mechanism.

#### PEG10

- **Related proteins** (co-abundance neighbors): PRKCQ (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: paternally expressed 10. This is a paternally expressed imprinted gene that is thought to have been derived from the Ty3/Gypsy family of retrotransposons. It contains two overlapping open reading frames, RF1 and RF2, and expresses two proteins: a shorter, gag-like protein (with a CCHC-type zinc finger domain) from RF1; and a longer, gag/pol-like fusion protein (with an additional aspartic protease motif) from RF1/RF2 by -…
- **Diseases (Open Targets)**: neurodegenerative disease (0.463); luminal A breast carcinoma (0.218); carpal tunnel syndrome (0.097); self-injurious ideation (0.092); total knee arthroplasty (0.083)
- **Europe PMC papers**: 2538
- **Why important**: PEG10 is directly connected to PRKCQ and has substantial literature. It is an imprinted, retrotransposon-derived gene encoding frameshifted products and is annotated in placenta development, transforming-growth-factor-beta receptor signaling, mRNA transport, protein homooligomerization, and vesicle-mediated intercellular transport. Its tissue enhancement in adrenal gland and placenta and its cytosolic localization provide a distinct developmental and intracellular component of the module.
- **Conclusion**: Established evidence supports PEG10 as an imprinted gene with unusual protein products and roles associated with development and intracellular transport. Its co-abundance with PRKCQ may reflect a shared developmental or cellular-state program, but any direct mechanistic connection is hypothetical.

#### GGT7

- **Related proteins** (co-abundance neighbors): ANKRD39 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gamma-glutamyltransferase 7. This gene is a member of a gene family that encodes enzymes involved in both the metabolism of glutathione and in the transpeptidation of amino acids. Changes in the activity of gamma-glutamyltransferase may signal preneoplastic or toxic conditions in the liver or kidney. The protein encoded by this gene consists of a heavy and a light chain, and it can interact with CT120, a plasma membrane-assoc…
- **Diseases (Open Targets)**: angina pectoris (0.292); coronary artery disorder (0.285); poisoning (0.259); intermediate coronary syndrome (0.225); myocardial infarction (0.225)
- **Europe PMC papers**: 279
- **Why important**: GGT7 is the terminal member of the ANKRD39 branch and provides the clearest metabolic annotation in the module. Its gene-family function relates to glutathione metabolism and amino-acid transpeptidation, with annotations involving glutathione catabolism and oxidative-stress response. Its vesicular localization and cardiovascular disease associations make it relevant to a possible redox or metabolic component of the module, despite relatively limited literature.
- **Conclusion**: Established evidence supports GGT7 as a gamma-glutamyltransferase-family metabolic protein associated with glutathione biology. Its connection to ANKRD39 and the broader module may indicate redox-state coordination, but this is a hypothesis unsupported by enrichment or physical-interaction evidence.

## Module 8

**Tissue pair**: cell line and stem_cells  
**Genes (39)**: ANXA2, ARRB1, BRD8, CANX, MT-CO2, CRY1, SPECC1L, DIDO1, DBN1, DRG2, FAM98B, FLOT1, FTH1, GOLM1, HEXB, HMGA1, INTS1, ITGB1, LARP4, MAIP1, MED17, MAT2A, MORC3, MSH2, MYH10, NUP98, PARVA, PAWR, POGZ, PYM1, MRPL1, RRBP1, WARS1, GTF3C1, TNPO1, TOP2B, VASP, VRK1, ZNF512

### Function

The strongest primary evidence supports positive regulation of biosynthetic processes (GO:BP positive regulation of biosynthetic process; q_global = 0.0313). The contributing genes include regulators of transcription, chromatin, DNA maintenance, RNA processing, translation, mitochondrial activity, membrane trafficking, adhesion, and cytoskeletal organization. This combination is more consistent with a conserved cellular-state program than with one narrowly defined pathway. CRY1 is the central co-abundance hub, but network centrality does not establish direct physical interaction or regulation. STRING provides no functional enrichment, so the broader themes beyond (GO:BP positive regulation of biosynthetic process; q_global = 0.0313) should be treated as interpretation of gene annotations rather than globally corrected enrichment findings.

**Cell composition.** The module is not dominated by plasma or secreted proteins. ANXA2 is secreted to blood, whereas HEXB is annotated as intracellular and membrane-associated; most other genes are not secreted. HPA indicates predominantly low tissue specificity, consistent with broadly expressed or housekeeping-like biology rather than a strongly tissue-restricted program. Cell-type-enhanced signals are diverse, including esophageal epithelial cells, late spermatids, trophoblasts, podocytes, and neutrophils. Several genes show monocyte or neutrophil-associated signals, but overall immune-cell specificity is mostly low. Blood or shared-cell-type effects are therefore possible in mixed samples, but the module does not establish blood contamination. The supplied HPA protein-detection comparison adds no discriminatory evidence for the cell-line and stem-cell samples.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP positive regulation of biosynthetic process | 0.0313 | ANXA2, ARRB1, BRD8, CRY1, FLOT1, HEXB, HMGA1, LARP4, MED17, MSH2, NUP98, PAWR, POGZ, PYM1, TOP2B, TSLIG3B, WARS1 |

### STRING and hu.MAP

STRING supports three high-confidence relationships: ITGB1 with PARVA, ITGB1 with VASP, and NUP98 with TNPO1. These support an adhesion and actin-associated component and a nucleocytoplasmic-transport component. hu.MAP provides partial complex support for MSH2 with MAIP1 in (hu.MAP huMAP3_09889.1) and for FLOT1 with ANXA2 in (hu.MAP huMAP3_05674.1) and (hu.MAP huMAP3_09165.1). The repeated FLOT1–ANXA2 membership supports membrane organization, vesicle trafficking, and adhesion-related biology. The MSH2–MAIP1 pairing indicates shared complex membership but does not establish a unified DNA-repair and mitochondrial mechanism. Most module pairs lack known STRING or hu.MAP support. The module is therefore best regarded as a co-abundance organization spanning several cellular systems, not as one established physical complex.

**STRING interactions (score >= 0.7)**: 3 of 741 gene pairs: ITGB1–PARVA (0.808); ITGB1–VASP (0.72); NUP98–TNPO1 (0.914)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09889.1 (MSH2, MAIP1; 2/3); huMAP3_05674.1 (FLOT1, ANXA2; 2/12); huMAP3_09165.1 (FLOT1, ANXA2; 2/39)

### Novelty

The specific shared co-abundance pattern may be a new finding because the supplied databases do not identify a pre-existing unified interaction or complex containing the module as a whole. However, absence from STRING or hu.MAP does not prove novelty: database coverage is incomplete, co-abundance is not equivalent to physical interaction, and many component functions are already well established. The defensible conclusion is that the particular conserved module organization is potentially novel, whereas its individual biological processes and several internal relationships are known.

**Hypothesis.** Hypothesis: the module represents a conserved cellular-state program in which circadian regulation involving CRY1 is coordinated with biosynthetic capacity, transcriptional and RNA-processing activity, genome maintenance, mitochondrial function, and membrane–cytoskeletal remodeling. In cell-line and stem-cell contexts, this may reflect a shared balance between biosynthetic or proliferative demand and adhesion, trafficking, and stress adaptation. ANXA2, FLOT1, ITGB1, PARVA, and VASP may represent the membrane–cytoskeletal arm, while MSH2, NUP98, and TNPO1 may represent genome-maintenance and nuclear-transport requirements. This is a mechanistic model for testing, not evidence of direct regulation by CRY1 or of one physical multiprotein complex.

### Important genes

#### CRY1

- **Related proteins** (co-abundance neighbors): ARRB1 (0.98), PARVA (0.96), HEXB (0.94), MT-CO2 (0.94), FAM98B (0.93), MSH2 (0.93), POGZ (0.92), DBN1 (0.92), VASP (0.91), FTH1 (0.90), BRD8 (0.90), WARS1 (0.90), LARP4 (0.87), INTS1 (0.87), GOLM1 (0.86), TOP2B (0.86), MRPL1 (0.86), DRG2 (0.86), MAIP1 (0.85), ANXA2 (0.85), SPECC1L (0.84), PAWR (0.84), DIDO1 (0.84), NUP98 (0.83), GTF3C1 (0.83), MYH10 (0.83), ITGB1 (0.83), MAT2A (0.81), MORC3 (0.81), RRBP1 (0.81), ZNF512 (0.81), HMGA1 (0.81), MED17 (0.81), PYM1 (0.81), VRK1 (0.81), FLOT1 (0.80), TNPO1 (0.80), CANX (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane, Microtubules; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cryptochrome circadian regulator 1. This gene encodes a flavin adenine dinucleotide-binding protein that is a key component of the circadian core oscillator complex, which regulates the circadian clock. This gene is upregulated by CLOCK/ARNTL heterodimers but then represses this upregulation in a feedback loop using PER/CRY heterodimers to interact with CLOCK/ARNTL. Polymorphisms in this gene have been associated with altered sleep …
- **Diseases (Open Targets)**: attention deficit-hyperactivity disorder (0.429); insomnia (0.371); metabolic disease (0.265); vitiligo (0.218); ovarian dysfunction (0.216)
- **Europe PMC papers**: 10077
- **Why important**: CRY1 is the central co-abundance hub and the clearest network-level organizer. It is a core circadian oscillator component that participates in transcriptional feedback, and it is associated in the supplied evidence with sleep, metabolic, and neurodevelopmental or behavioral disease areas. It is also represented in the globally corrected biosynthetic-process term (GO:BP positive regulation of biosynthetic process; q_global = 0.0313). Its extensive literature makes its basic biological interpretation well established.
- **Conclusion**: Established evidence supports CRY1 as a circadian regulator and as the statistical center of this module. It is not established that CRY1 physically binds or directly regulates the other module genes. Its role as a coordinator of the broader module is a hypothesis requiring perturbation or time-resolved testing.

#### ANXA2

- **Related proteins** (co-abundance neighbors): CRY1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05674.1, huMAP3_09165.1
- **Function (MyGene.info)**: annexin A2. This gene encodes a member of the annexin family. Members of this calcium-dependent phospholipid-binding protein family play a role in the regulation of cellular growth and in signal transduction pathways. This protein functions as an autocrine factor which heightens osteoclast formation and bone resorption. This gene has three pseudogenes located on chromosomes 4, 9 and 10, respectively. Multiple…
- **Diseases (Open Targets)**: neurodegenerative disease (0.443); Alzheimer disease (0.312); Parkinson disease (0.298); lysosomal storage disease (0.289); benign urinary system neoplasm (0.270)
- **Europe PMC papers**: 12966
- **Why important**: ANXA2 occurs in (GO:BP positive regulation of biosynthetic process; q_global = 0.0313), is annotated by HPA as secreted to blood, and has established roles in receptor recycling, vesicle budding, membrane-raft assembly, and cell adhesion. It appears with FLOT1 in both (hu.MAP huMAP3_05674.1) and (hu.MAP huMAP3_09165.1), providing notable complex-context support within the module. Its disease associations include neurodegenerative and neoplastic contexts, and its literature is substantial.
- **Conclusion**: Established evidence supports ANXA2 as a membrane, trafficking, adhesion, and extracellularly detectable component. Its presence may also make the module sensitive to sample composition. It is not established that ANXA2 drives the shared program; its proposed role as a mediator or marker of the membrane-remodeling arm is a hypothesis.

#### ITGB1

- **Related proteins** (co-abundance neighbors): CRY1 (0.83); STRING partners: PARVA (0.808), VASP (0.72)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is a plasma-membrane and focal-adhesion receptor with established roles in cell adhesion, embryogenesis, tissue repair, immunity, and cell–matrix interactions. Its STRING relationships with PARVA and VASP provide the clearest supported adhesion and actin-associated subnetwork. HPA places it at focal adhesions and reports cell-type-enhanced expression in endometrial glandular cells, pancreatic duct cells, and platelets. It has extensive literature and disease associations involving inflammatory and autoimmune contexts.
- **Conclusion**: Established evidence supports ITGB1 as an adhesion-related anchor and as part of known relationships with PARVA and VASP. The module may capture a shared adhesion state, but it does not establish that ITGB1 controls the nuclear, mitochondrial, or biosynthetic components.

#### MSH2

- **Related proteins** (co-abundance neighbors): CRY1 (0.93); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09889.1
- **Function (MyGene.info)**: mutS homolog 2. This locus is frequently mutated in hereditary nonpolyposis colon cancer (HNPCC). When cloned, it was discovered to be a human homolog of the E. coli mismatch repair gene mutS, consistent with the characteristic alterations in microsatellite sequences (RER+ phenotype) found in HNPCC. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: Lynch syndrome (0.891); colorectal cancer (0.776); mismatch repair cancer syndrome (0.775); Muir-Torre syndrome (0.752); mismatch repair cancer syndrome 1 (0.740)
- **Europe PMC papers**: 22581
- **Why important**: MSH2 is included in (GO:BP positive regulation of biosynthetic process; q_global = 0.0313) and has established roles in mismatch repair, DNA damage tolerance, and recombination. It has strong disease associations with Lynch syndrome and colorectal cancer and a substantial literature base. Its membership with MAIP1 in (hu.MAP huMAP3_09889.1) provides complex-level support distinct from the membrane-associated evidence. MSH2 gives the module a genome-maintenance dimension relevant to proliferative cellular systems.
- **Conclusion**: Established evidence supports MSH2 as a DNA-repair component and as a member of the hu.MAP relationship (hu.MAP huMAP3_09889.1). Its co-abundance with CRY1 and membrane or metabolic genes is not mechanistically established. Coordinated biosynthetic and genome-maintenance demand is a reasonable but testable interpretation.

#### NUP98

- **Related proteins** (co-abundance neighbors): CRY1 (0.83); STRING partners: TNPO1 (0.914)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 98 and 96 precursor. Nuclear pore complexes (NPCs) regulate the transport of macromolecules between the nucleus and cytoplasm, and are composed of many polypeptide subunits, many of which belong to the nucleoporin family. This gene belongs to the nucleoporin gene family and encodes a 186 kDa precursor protein that undergoes autoproteolytic cleavage to generate a 98 kDa nucleoporin and 96 kDa nucleoporin. The 98 kDa nu…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); acute myeloid leukemia (0.399); lung carcinoma (0.376)
- **Europe PMC papers**: 4839
- **Why important**: NUP98 is included in (GO:BP positive regulation of biosynthetic process; q_global = 0.0313) and functions in nucleocytoplasmic transport, RNA export, nuclear-pore organization, and genome organization at the nuclear periphery. Its high-confidence STRING relationship with TNPO1 supports a nuclear-import and transport submodule. HPA reports a neutrophil-enriched single-cell signal, although its overall tissue specificity is low. Its disease evidence includes viral infection and acute myeloid leukemia, giving it relevance to both normal transport and pathological cell states.
- **Conclusion**: Established evidence supports NUP98 as a nuclear-pore and transport component connected to TNPO1. The module does not demonstrate a direct NUP98–CRY1 mechanism. Its representation of transport capacity needed for the transcriptional and biosynthetic state is a plausible hypothesis.

## Module 9

**Tissue pair**: cell line and stem_cells  
**Genes (5)**: ANXA3, CYTH2, FBLIM1, FRYL, TXNRD1

### Function

The module has no GO or KEGG term passing global multiple-testing correction, so no pathway-level function can be claimed from primary enrichment evidence. Its topology is a hub-and-spoke pattern centered on CYTH2, with links to FBLIM1, TXNRD1, FRYL, and ANXA3. The annotations suggest convergence of membrane-associated signaling and vesicle or actin regulation through CYTH2, cell adhesion and integrin regulation through FBLIM1, redox homeostasis through TXNRD1, cell polarity and morphogenesis through FRYL, and calcium-dependent membrane signaling, phagocytosis, neutrophil degranulation, and endothelial migration through ANXA3. These annotations support a possible interface between cytoskeletal organization, membrane trafficking, redox control, and adhesion, but they do not establish a unified biological pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: all listed genes have no secretome annotation. It is also not uniformly blood-cell specific. HPA indicates mixed patterns, including low tissue specificity for several genes, tissue enrichment in blood vessel or bone marrow for individual genes, and immune-cell enrichment or enhancement for some genes. Single-cell annotations span epithelial, reproductive, neural-support, vascular, stromal, megakaryocyte, basophil, and neutrophil populations. Thus, the shared module may reflect broadly distributed cellular machinery, shared cell states, or cellular composition effects rather than a blood-specific secreted-protein program. The available HPA protein-detection fields provide no positive protein-detection evidence for either study context.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No listed gene pair meets the specified STRING interaction threshold, and no hu.MAP complex contains multiple module members. Therefore, the co-abundance relationships are not supported here by high-confidence known physical or functional interactions or by a shared annotated complex. The absence of STRING and hu.MAP support means that the module should be interpreted as a co-abundance pattern rather than as a demonstrated protein complex. It may reflect indirect regulation, shared cellular state, correlated expression, or context-dependent interactions that are not represented in these resources.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a potentially novel co-abundance association, because the module links these genes despite the absence of high-confidence STRING pairings and shared hu.MAP complexes. However, that resource-level absence does not prove biological novelty. Several members have established individual functions and substantial literature, and the apparent hub status of CYTH2 is a property of this co-abundance network rather than proof of a previously unknown molecular interaction. The strongest defensible conclusion is that the specific cross-context co-abundance configuration is insufficiently characterized, while the individual gene biology is not necessarily new.

**Hypothesis.** Hypothesis: the module represents a shared cell-state program in which CYTH2-associated membrane trafficking and ARF signaling coordinate with FBLIM1-linked adhesion and actin organization, while TXNRD1 supports redox buffering and FRYL contributes to polarity or morphogenesis; ANXA3 may connect this state to calcium-dependent membrane behavior, migration, phagocytic activity, or granulocyte-related functions. A composition-driven explanation remains plausible because the genes have heterogeneous tissue and single-cell enrichment patterns. This hypothesis should be tested with cell-type-resolved expression, perturbation of CYTH2 and its four module partners, and independent datasets from the two study contexts.

### Important genes

#### CYTH2

- **Related proteins** (co-abundance neighbors): FBLIM1 (0.88), TXNRD1 (0.85), FRYL (0.82), ANXA3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytohesin 2. The protein encoded by this gene is a member of the PSCD family. Members of this family have identical structural organization that consists of an N-terminal coiled-coil motif, a central Sec7 domain, and a C-terminal pleckstrin homology (PH) domain. The coiled-coil motif is involved in homodimerization, the Sec7 domain contains guanine-nucleotide exchange protein (GEP) activity, and the PH domain …
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); IgA glomerulonephritis (0.320); brain compression (0.107); edema (0.107); colorectal cancer (0.073)
- **Europe PMC papers**: 190
- **Why important**: CYTH2 is the network hub, connected to every other module member. Its Sec seven domain supports ARF guanine-nucleotide exchange activity, while its pleckstrin-homology domain supports membrane association. Its curated functions include endocytosis, vesicle-mediated transport, actin cytoskeleton organization, and regulation of ARF signaling. It therefore provides the strongest mechanistic anchor for a membrane-trafficking and cytoskeletal interpretation. Its disease associations and literature record indicate that it is biologically studied, although the fact sheet does not establish these module links as known interactions.
- **Conclusion**: Established: CYTH2 is a membrane-associated ARF regulatory protein with functions in trafficking and actin organization, and it is the central node of this module. Hypothesis: CYTH2 may organize the shared co-abundance state by coordinating the other genes, but network centrality alone does not demonstrate causal control.

#### FBLIM1

- **Related proteins** (co-abundance neighbors): CYTH2 (0.88); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Cell Junctions, Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin binding LIM protein 1. This gene encodes a protein with an N-terminal filamin-binding domain, a central proline-rich domain, and, multiple C-terminal LIM domains. This protein localizes at cell junctions and may link cell adhesion structures to the actin cytoskeleton. This protein may be involved in the assembly and stabilization of actin-filaments and likely plays a role in modulating cell adhesion, cell morphology and…
- **Diseases (Open Targets)**: neurodegenerative disease (0.247); COVID-19 (0.219); severe acute respiratory syndrome (0.219); arthritic joint disease (0.126); central nervous system cancer (0.099)
- **Europe PMC papers**: 438
- **Why important**: FBLIM1 is directly connected to CYTH2 and has a tissue-enriched blood-vessel annotation. Its localization at cell junctions and focal adhesion sites, together with roles in integrin activation, cell-cell adhesion, actin-filament stabilization, cell morphology, and motility, makes it important for interpreting the module as a possible adhesion or cytoskeletal state. Its basophil enrichment also warrants attention to cellular composition.
- **Conclusion**: Established: FBLIM1 is associated with adhesion structures, integrin regulation, and actin organization. Hypothesis: its co-abundance with CYTH2 may indicate coordinated regulation of adhesion-linked membrane remodeling, but the module does not prove a direct molecular partnership.

#### TXNRD1

- **Related proteins** (co-abundance neighbors): CYTH2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin reductase 1. The protein encoded by this gene belongs to the pyridine nucleotide-disulfide oxidoreductase family, and is a member of the thioredoxin (Trx) system. Three thioredoxin reductase (TrxR) isozymes are found in mammals. TrxRs are selenocysteine-containing flavoenzymes, which reduce thioredoxins, as well as other substrates, and play a key role in redox homoeostasis. This gene encodes an ubiquitously e…
- **Diseases (Open Targets)**: acute promyelocytic leukemia (0.588); neoplasm (0.397); brain cancer (0.371); acute myeloid leukemia (0.370); arthritic joint disease (0.370)
- **Europe PMC papers**: 4293
- **Why important**: TXNRD1 is directly connected to CYTH2 and is the clearest redox-related member. It encodes a cytosolic thioredoxin reductase involved in thioredoxin reduction, redox homeostasis, selenium metabolism, and cellular oxidant detoxification. Its broad tissue annotation and extensive literature make it a plausible marker of a general cellular state rather than a tissue-restricted pathway.
- **Conclusion**: Established: TXNRD1 supports thioredoxin-dependent redox control and oxidant detoxification. Hypothesis: redox buffering may permit or accompany the membrane and cytoskeletal changes represented by the module, but no direct redox mechanism is demonstrated by the available network evidence.

#### FRYL

- **Related proteins** (co-abundance neighbors): CYTH2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FRY like transcription coactivator. Predicted to be involved in cell morphogenesis and neuron projection development. Predicted to be active in cell cortex and site of polarized growth. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Pan-Chung-Bellen syndrome (0.668); type 2 diabetes mellitus (0.277); migraine disorder (0.269); thrombophilia (0.130); dementia (0.118)
- **Europe PMC papers**: 331
- **Why important**: FRYL is directly connected to CYTH2 and contributes a polarity and morphogenesis dimension. Its annotations include cell morphogenesis, maintenance of cell polarity, neuron projection development, cell cortex, and polarized growth. Its single-cell associations include goblet cells and oligodendrocytes, while its blood annotation includes basophil enrichment, reinforcing the heterogeneous cellular context of the module.
- **Conclusion**: Established: FRYL is annotated in processes involving polarity, morphogenesis, and polarized growth. Hypothesis: FRYL may connect CYTH2-associated membrane trafficking to changes in cell shape or polarity, but the fact sheet does not establish a direct biochemical interaction.

#### ANXA3

- **Related proteins** (co-abundance neighbors): CYTH2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A3. This gene encodes a member of the annexin family.  Members of this calcium-dependent phospholipid-binding protein family play a role in the regulation of cellular growth and in signal transduction pathways.  This protein functions in the inhibition of phopholipase A2 and cleavage of inositol 1,2-cyclic phosphate to form inositol 1-phosphate. This protein may also play a role in anti-coagulation. […
- **Diseases (Open Targets)**: rheumatoid arthritis (0.318); Meniere disease (0.276); insomnia (0.255); hair color (0.209); refractive error (0.176)
- **Europe PMC papers**: 2243
- **Why important**: ANXA3 is directly connected to CYTH2 and is the module member with the strongest membrane and innate-cell functional interpretation. It is a calcium-dependent phospholipid-binding annexin associated with plasma membrane localization, phagocytosis, neutrophil degranulation, defense against bacteria, endothelial migration, and angiogenesis. Its bone-marrow tissue enhancement and neutrophil enrichment make it especially relevant to possible blood-cell or sample-composition effects.
- **Conclusion**: Established: ANXA3 participates in calcium-dependent membrane biology and is annotated in phagocytic, neutrophil, endothelial-migration, and angiogenic processes. Hypothesis: ANXA3 may mark an immune or vascular component of the shared module, or may couple membrane remodeling to cell migration, but the module does not establish which explanation is correct.

## Module 10

**Tissue pair**: cell line and stem_cells  
**Genes (20)**: AP1S1, ANAPC1, BRD2, CHAF1B, COG1, COG2, IFT25, CD46, PDCL3, PKP4, PTPA, RCC1L, POLR1B, SACK1F, SKA1, STX6, DARS2, TM9SF4, TMEM11, ZNG1B

### Function

The strongest functional interpretation is a trans-Golgi network membrane and vesicle-trafficking module. The globally corrected GO evidence identifies the trans-Golgi network membrane (GO:CC trans-Golgi network membrane; q_global = 0.0456), supported by AP1S1, COG1, COG2, and STX6; the independent STRING enrichment points to the same compartment (STRING Component trans-Golgi network membrane; within-query FDR = 0.0281). AP1S1 supports clathrin-associated Golgi sorting, COG1 and COG2 support COG-complex function, and STX6 supports SNARE-mediated vesicle fusion and endosome-to-Golgi transport. The remaining genes do not form a comparably coherent annotated pathway, so the module should not be interpreted as a uniformly established Golgi pathway for every member. Its co-abundance structure may combine a Golgi-trafficking signal with cell-state or lineage-related signals.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, while many show cell-type-enhanced expression across diverse epithelial, germ-cell, muscle, neuronal, ciliated, and progenitor populations. Immune-cell specificity is generally low, with only limited blood-cell enrichment represented by CD46 and other isolated annotations. Therefore, the module does not primarily resemble a blood or plasma contamination signature. The broad and heterogeneous HPA pattern instead supports a shared cellular program, potentially including membrane trafficking, organelle maintenance, proliferation, and differentiation state. HPA protein detection in the relevant cell-line and stem-cell contexts is unavailable, so transcript co-abundance should not be treated as direct protein-level confirmation.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC trans-Golgi network membrane | 0.0456 | AP1S1, COG1, COG2, STX6 |

### STRING and hu.MAP

Known molecular support is concentrated in a small part of the module. COG1 and COG2 have a very strong STRING relationship, and they co-occur in several hu.MAP complexes (hu.MAP huMAP3_04294.1), (hu.MAP huMAP3_14423.1), and (hu.MAP huMAP3_09176.1), where the other listed members include additional COG subunits and trafficking-associated proteins. AP1S1 occurs with PKP4 in a large hu.MAP complex (hu.MAP huMAP3_12394.1), although that complex is broad and does not establish a direct AP1S1–PKP4 interaction. ANAPC1 and IFT25 also have a high-confidence STRING relationship. The sparse STRING graph means that most module edges are not supported as established physical interactions. Thus, the module is best viewed as a co-abundance module containing a well-supported COG and trans-Golgi submodule, rather than as one experimentally validated multiprotein complex.

**STRING interactions (score >= 0.7)**: 2 of 190 gene pairs: ANAPC1–IFT25 (0.886); COG1–COG2 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component trans-Golgi network membrane (FDR = 0.0281, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04294.1 (COG2, COG1; 2/10); huMAP3_14423.1 (COG2, COG1; 2/11); huMAP3_09176.1 (COG2, COG1; 2/12); huMAP3_12394.1 (AP1S1, PKP4; 2/98)

### Novelty

The core biology is not new: Golgi organization, COG-complex activity, adaptor-mediated trafficking, and STX6-dependent vesicle fusion are established functions, and the COG1–COG2 relationship is already represented in STRING and hu.MAP. What may be new is the observation that these genes co-abound with the broader set of ciliary, mitochondrial, chromatin, cell-cycle, junctional, and signaling genes in a conserved cell-line/stem-cell module. However, the fact sheet does not provide a comparison against previously published co-abundance modules or an exhaustive literature search for this exact gene combination. Consequently, this module can be described as a potentially novel network-level association, not as a definitively new biological mechanism. Lack of STRING or hu.MAP support for most edges is evidence of limited prior molecular annotation, not proof of novelty.

**Hypothesis.** Hypothesis: the module reflects a shared developmental cell state in which trans-Golgi trafficking and organelle organization are coordinated with proliferation, cilium-related programs, mitochondrial function, chromatin assembly, and cell adhesion. In this model, the COG1–COG2 core maintains Golgi organization and glycoprotein recycling, while AP1S1 and STX6 connect cargo sorting and vesicle fusion to the trans-Golgi network. Co-abundance with genes such as IFT25, SKA1, ANAPC1, CHAF1B, and PKP4 could reflect coordinated remodeling of trafficking, cytoskeletal, ciliary, junctional, and cell-cycle systems during differentiation. This is a mechanistic hypothesis rather than an established interaction map; the sparse physical-interaction evidence argues that these relationships should be tested experimentally.

### Important genes

#### COG1

- **Related proteins** (co-abundance neighbors): COG2 (0.82), DARS2 (0.82); STRING partners: COG2 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_04294.1, huMAP3_14423.1, huMAP3_09176.1
- **Function (MyGene.info)**: component of oligomeric golgi complex 1. The protein encoded by this gene is one of eight proteins (Cog1-8) which form a Golgi-localized complex (COG) required for normal Golgi morphology and function. It is thought that this protein is required for steps in the normal medial and trans Golgi-associated processing of glycoconjugates and plays a role in the organization of the Golgi-localized complex. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: COG1-congenital disorder of glycosylation (0.789); congenital disorder of glycosylation (0.371); dengue disease (0.370); neurodegenerative disease (0.369); hereditary disease (0.194)
- **Europe PMC papers**: 535
- **Why important**: COG1 is one of the clearest anchors of the module's inferred function. It is annotated as a subunit of the conserved oligomeric Golgi complex, participates in Golgi organization and retrograde vesicle recycling, contributes to the globally significant trans-Golgi network membrane term (GO:CC trans-Golgi network membrane; q_global = 0.0456), has a direct STRING relationship with COG2, and appears with COG2 in several hu.MAP complexes (hu.MAP huMAP3_04294.1), (hu.MAP huMAP3_14423.1), and (hu.MAP huMAP3_09176.1). Its disease associations include congenital disorder of glycosylation, and it has substantial literature support. Within the co-abundance graph it connects to COG2 and DARS2, providing a bridge between the Golgi signal and the broader module.
- **Conclusion**: Established evidence supports COG1 as a Golgi-complex and glycoprotein-trafficking component and as part of the module's best-supported molecular core. The hypothesis that its coordinated abundance with the non-Golgi genes marks a shared developmental trafficking state remains unproven.

#### COG2

- **Related proteins** (co-abundance neighbors): ZNG1B (0.91), COG1 (0.82); STRING partners: COG1 (0.999)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_04294.1, huMAP3_14423.1, huMAP3_09176.1
- **Function (MyGene.info)**: component of oligomeric golgi complex 2. This gene encodes a subunit of the conserved oligomeric Golgi complex that is required for maintaining normal structure and activity of the Golgi complex. The encoded protein specifically interacts with the USO1 vesicle docking protein and may be necessary for normal Golgi ribbon formation and trafficking of Golgi enzymes. Mutations of this gene are associated with abnormal glycosylation within th…
- **Diseases (Open Targets)**: congenital disorder of glycosylation, type IIq (0.671); neurodegenerative disease (0.474); congenital disorder of glycosylation type II (0.462); spinal cord disorder (0.215); polycystic ovary syndrome (0.214)
- **Europe PMC papers**: 378
- **Why important**: COG2 is a direct functional partner of COG1 and is the other principal anchor of the COG submodule. It contributes to (GO:CC trans-Golgi network membrane; q_global = 0.0456) and (STRING Component trans-Golgi network membrane; within-query FDR = 0.0281), is localized by HPA to the Golgi apparatus, and is described as required for Golgi structure, intra-Golgi transport, and normal glycosylation. It is represented in several hu.MAP complexes (hu.MAP huMAP3_04294.1), (hu.MAP huMAP3_14423.1), and (hu.MAP huMAP3_09176.1), and its disease associations include congenital disorders of glycosylation. Its co-abundance link to the high-connectivity gene ZNG1B places it at the interface between the annotated Golgi signal and the larger module.
- **Conclusion**: Established evidence identifies COG2 as a Golgi-maintenance and trafficking component with disease relevance through defective glycosylation. It is reasonable to regard COG2 as a functional marker of the module's Golgi component, but not as proof that ZNG1B or the other module members physically operate in the COG complex.

#### AP1S1

- **Related proteins** (co-abundance neighbors): ZNG1B (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: adaptor related protein complex 1 subunit sigma 1. The protein encoded by this gene is part of the clathrin coat assembly complex which links clathrin to receptors in coated vesicles. These vesicles are involved in endocytosis and Golgi processing. This protein, as well as beta-prime-adaptin, gamma-adaptin, and the medium (mu) chain AP47, form the AP-1 assembly protein complex located at the Golgi vesicle. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: MEDNIK syndrome (0.762); HIV infectious disease (0.504); Abnormality of the skeletal system (0.359); neurodegenerative disease (0.344); hereditary disease (0.336)
- **Europe PMC papers**: 462
- **Why important**: AP1S1 contributes to the only globally corrected term (GO:CC trans-Golgi network membrane; q_global = 0.0456) and the concordant STRING term (STRING Component trans-Golgi network membrane; within-query FDR = 0.0281). It is a component of the AP-1 clathrin adaptor complex at the Golgi and supports intracellular protein transport, receptor-mediated endocytosis, and vesicle-mediated transport. HPA places it at the Golgi and in vesicles, and it appears in the broad trafficking-related hu.MAP complex (hu.MAP huMAP3_12394.1). Its disease associations include MEDNIK syndrome and neurodegenerative disease, and its literature base supports an established trafficking role. Its co-abundance connection to ZNG1B links it to the module's most connected node.
- **Conclusion**: Established evidence supports AP1S1 as a cargo-sorting and Golgi-vesicle trafficking component. The hypothesis that AP1S1 coordinates with the ciliary, junctional, or cell-cycle genes in this module is plausible from co-abundance but is not established by the available physical-interaction data.

#### STX6

- **Related proteins** (co-abundance neighbors): ZNG1B (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntaxin 6. Enables syntaxin binding activity. Involved in several processes, including Golgi ribbon formation; retrograde transport, endosome to Golgi; and vesicle fusion. Acts upstream of or within endocytic recycling. Located in several cellular components, including early endosome; perinuclear region of cytoplasm; and trans-Golgi network. Part of SNARE complex. [provided by Alliance of Genome Resources, A…
- **Diseases (Open Targets)**: progressive supranuclear palsy (0.372); sporadic Creutzfeld Jacob disease (0.268); alcohol drinking (0.227); menopause (0.166); neoplasm (0.102)
- **Europe PMC papers**: 850
- **Why important**: STX6 is one of the four genes supporting (GO:CC trans-Golgi network membrane; q_global = 0.0456) and (STRING Component trans-Golgi network membrane; within-query FDR = 0.0281). It is a Golgi and trans-Golgi network syntaxin involved in SNARE-mediated vesicle fusion, endosome-to-Golgi retrograde transport, and endocytic recycling. HPA places it at the Golgi, and its disease and neurological literature associations provide biological relevance beyond the enrichment result. Its connection to ZNG1B makes it part of the module's central co-abundance neighborhood even though the fact sheet does not report a STRING or hu.MAP relationship for STX6.
- **Conclusion**: Established evidence supports STX6 as a membrane-fusion and recycling component of the trans-Golgi network. Its placement in this module supports a trafficking interpretation, while any proposed role in coordinating the broader developmental program remains a hypothesis.

#### IFT25

- **Related proteins** (co-abundance neighbors): ZNG1B (0.93), SACK1F (0.81); STRING partners: ANAPC1 (0.886)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece, Principal piece, End piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: intraflagellar transport 25. Predicted to enable metal ion binding activity. Predicted to be involved in kidney development and spermatogenesis. Predicted to act upstream of or within animal organ development; left/right axis specification; and skeletal system development. Predicted to be located in ciliary tip. Predicted to be part of intraciliary transport particle B. Predicted to be active in centrosome and cilium. [provid…
- **Diseases (Open Targets)**: Hashimoto thyroiditis (0.236); hypothyroidism (0.224); renal agenesis (0.111); hepatocellular carcinoma (0.076); Heterotaxia (0.069)
- **Europe PMC papers**: 266
- **Why important**: IFT25 provides a contrasting but potentially informative component. It is annotated as part of intraflagellar transport and cilium assembly, with roles in kidney development, smoothened signaling, and spermatogenesis; HPA shows enhancement in several ciliated cell types. It has a high-confidence STRING relationship with ANAPC1 and is connected in the module to ZNG1B and SACK1F. Its disease associations include renal developmental abnormalities and heterotaxia, and it has a substantial literature base. These features make it a useful candidate for testing whether the module links Golgi trafficking with ciliary or developmental state.
- **Conclusion**: Established evidence supports IFT25 as a ciliary transport factor with developmental relevance. Its inclusion in a Golgi-enriched module does not establish a Golgi–cilium mechanism; that connection is a testable hypothesis suggested by co-abundance and should be validated with perturbation or localization experiments.

## Module 11

**Tissue pair**: cell line and stem_cells  
**Genes (33)**: APOL2, ASAP3, ATP1B3, BST2, CPD, C3orf38, CLPB, CPSF6, DGKA, ECI2, TBRG4, GALNT3, TUBGCP6, GIPC1, GULP1, CAMK2D, KRI1, MLC1, IGF2R, NISCH, NUP54, PAPSS2, PCYT2, PDE5A, PTPRF, PTPRK, RBM26, SH3BP4, SPTBN1, STAT1, SUN1, TMEM209, UBXN4

### Function

No GO or KEGG term passed global correction, and STRING reported no functional enrichment; therefore the module does not support a single statistically established pathway. Its structure is highly hub-centered around MLC1, with most other genes connected to MLC1 rather than to one another, so co-abundance does not by itself establish a physical complex. The annotations instead suggest a broad membrane, vesicle, trafficking, cytoskeletal, and signaling theme. MLC1 is linked to vesicle-mediated transport, intracellular transport, osmotic response, and caveolin-mediated endocytosis. GIPC1 and SH3BP4 support receptor trafficking, clathrin-mediated endocytosis, actin organization, and Rho signaling, while IGF2R and CPD support lysosomal targeting, protein processing, and intracellular trafficking. Additional genes represent phospholipid synthesis, cyclic-nucleotide signaling, ion transport, RNA processing, mitochondrial metabolism, and antiviral or interferon-related responses. The most defensible interpretation is a heterogeneous cell-state or membrane-trafficking module rather than a narrowly defined pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a single secreted gene, and many proteins are intracellular or membrane-associated. Most genes have low tissue specificity, while the tissue-enhanced and tissue-enriched genes are distributed across brain, adrenal gland, testis, liver, heart muscle, ovary, salivary gland, and other tissues. Cell-type annotations are similarly diverse, with repeated signals in spermatids, hepatocytes, astrocytes, epithelial cells, and several other populations. Most genes have low immune-cell specificity, although some are enhanced or group-enriched in myeloid dendritic cells, neutrophils, basophils, monocytes, and related immune populations. Thus, the module is not a classic blood-cell or plasma-protein signature, but some shared cell-type composition or immune-state contribution remains possible. HPA protein-detection fields for the two queried systems provide no additional discrimination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a small set of high-confidence relationships within the module: BST2 with STAT1, CPD with IGF2R, and GIPC1 with SH3BP4. These links independently support several biologically plausible subthemes: antiviral or interferon-associated regulation, lysosomal or protein-processing trafficking, and receptor or cargo trafficking. They do not support a densely connected module-wide protein complex. hu.MAP repeatedly places GIPC1 and SH3BP4 together in complexes containing NTRK3, GIPC2, GIPC3, APPL proteins, DOCK proteins, BICC1, or MS4A10, depending on the complex. hu.MAP also places CPSF6 and RBM26 together in a larger RNA-processing complex. These results indicate that selected pairs have known complex or interaction context, while most module edges are not supported by the queried interaction resources and may represent co-abundance, indirect regulation, shared cell composition, or database incompleteness.

**STRING interactions (score >= 0.7)**: 3 of 528 gene pairs: BST2–STAT1 (0.813); CPD–IGF2R (0.738); GIPC1–SH3BP4 (0.746)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05570.1 (GIPC1, SH3BP4; 2/3); huMAP3_07477.1 (GIPC1, SH3BP4; 2/4); huMAP3_13141.1 (GIPC1, SH3BP4; 2/7); huMAP3_13127.1 (GIPC1, SH3BP4; 2/8); huMAP3_13139.1 (GIPC1, SH3BP4; 2/8); huMAP3_12235.1 (GIPC1, SH3BP4; 2/9); huMAP3_13497.1 (GIPC1, SH3BP4; 2/9); huMAP3_11453.1 (CPSF6, RBM26; 2/16)

### Novelty

This module should not be described as a newly discovered molecular complex or as a novel pathway. The absence of global GO or KEGG enrichment, the absence of STRING functional enrichment, the sparse STRING interaction support, and the star-like network structure all argue for caution. Some relationships are already known through STRING and hu.MAP, especially the GIPC1–SH3BP4 pair and the CPSF6–RBM26 pair, so the underlying biology is not wholly unprecedented. A potentially novel aspect could be the reproducible co-abundance of this particular combination in cell line and stem_cells, but that requires replication, comparison with published co-expression studies, control for cell composition and technical effects, and experimental validation. Database absence alone cannot establish novelty.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state involving membrane organization and cargo trafficking centered on MLC1, with contributions from receptor scaffolding, endocytosis, cytoskeletal remodeling, lipid handling, and intracellular transport. GIPC1–SH3BP4 may represent a trafficking-associated submodule, IGF2R–CPD a lysosomal or protein-processing branch, and STAT1–BST2 an inducible antiviral or interferon-responsive branch. In cell line and stem_cells, coordinated expression of these branches may arise during changes in membrane turnover, differentiation, stress adaptation, or cell-state composition rather than from one stable multiprotein complex. This hypothesis predicts that the module should track trafficking and membrane-state phenotypes more strongly than any single canonical pathway, and that its apparent coherence should be tested after controlling for cell identity and inflammatory state.

### Important genes

#### MLC1

- **Related proteins** (co-abundance neighbors): PTPRF (0.96), TBRG4 (0.96), C3orf38 (0.95), CAMK2D (0.95), SH3BP4 (0.93), NUP54 (0.93), PAPSS2 (0.92), PDE5A (0.90), TUBGCP6 (0.89), PTPRK (0.89), CPSF6 (0.88), STAT1 (0.88), APOL2 (0.88), IGF2R (0.88), GULP1 (0.87), BST2 (0.87), TMEM209 (0.86), UBXN4 (0.86), ATP1B3 (0.85), CLPB (0.85), SUN1 (0.84), SPTBN1 (0.84), NISCH (0.84), KRI1 (0.83), PCYT2 (0.83), RBM26 (0.82), CPD (0.82), ECI2 (0.81), GIPC1 (0.81), GALNT3 (0.81), DGKA (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: modulator of VRAC current 1. The function of this gene product is unknown; however, homology to other proteins suggests that it may be an integral membrane transporter. Mutations in this gene have been associated with megalencephalic leukoencephalopathy with subcortical cysts, an autosomal recessive neurological disorder. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by …
- **Diseases (Open Targets)**: megalencephalic leukoencephalopathy with subcortical cysts (0.827); hereditary disease (0.414); Seizure (0.370); Bilateral tonic-clonic seizure (0.370); Abnormality of the nervous system (0.340)
- **Europe PMC papers**: 1511
- **Why important**: MLC1 is the dominant network hub, connected to the other module members with the strongest overall module connectivity. Its annotations connect it to vesicle-mediated transport, intracellular transport, osmotic response, cholesterol response, and caveolin-mediated endocytosis. HPA identifies brain enrichment and astrocyte enhancement, and disease resources link it strongly to megalencephalic leukoencephalopathy with subcortical cysts and related neurological phenotypes. Its substantial literature support makes it the most informative anchor for interpreting the module, although it has no STRING partner or hu.MAP complex in this module.
- **Conclusion**: Established evidence supports MLC1 as a trafficking- and membrane-associated disease gene and as the central abundance correlate in this network. It is reasonable to regard MLC1 as an interpretive hub, but not as proof that it physically regulates every connected gene. A role as the organizing driver of the whole module remains a hypothesis.

#### GIPC1

- **Related proteins** (co-abundance neighbors): MLC1 (0.81); STRING partners: SH3BP4 (0.746)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05570.1, huMAP3_07477.1, huMAP3_13141.1, huMAP3_13127.1, huMAP3_13139.1, huMAP3_12235.1, huMAP3_13497.1
- **Function (MyGene.info)**: GIPC PDZ domain containing family member 1. GIPC1 is a scaffolding protein that regulates cell surface receptor expression and trafficking (Lee et al., 2008 [PubMed 18775991]).[supplied by OMIM, Apr 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); oculopharyngodistal myopathy 2 (0.409); oculopharyngodistal myopathy (0.376); smoking initiation (0.205); risk-taking behaviour (0.192)
- **Europe PMC papers**: 653
- **Why important**: GIPC1 is directly connected to SH3BP4 in STRING and recurs with SH3BP4 across several hu.MAP complexes. It is a PDZ-domain scaffolding protein involved in cell-surface receptor expression and trafficking, actin organization, Rho signaling, and synaptic or glutamatergic processes. Its plasma-membrane and cell-junction localization is consistent with the module's membrane-trafficking interpretation. It also has established disease associations involving neurodegenerative disease and oculopharyngodistal myopathy.
- **Conclusion**: Established evidence supports GIPC1 as a receptor-trafficking scaffold and as the best-supported complex-linked component of the module. Its repeated complex membership strengthens the trafficking interpretation, but the module does not demonstrate that all MLC1-linked genes act through GIPC1. Its broader role in this shared module is therefore a hypothesis.

#### SH3BP4

- **Related proteins** (co-abundance neighbors): MLC1 (0.93); STRING partners: GIPC1 (0.746)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05570.1, huMAP3_07477.1, huMAP3_13141.1, huMAP3_13127.1, huMAP3_13139.1, huMAP3_12235.1, huMAP3_13497.1
- **Function (MyGene.info)**: SH3 domain binding protein 4. This gene encodes a protein with 3 Asn-Pro-Phe (NPF) motifs, an SH3 domain, a PXXP motif, a bipartite nuclear targeting signal, and a tyrosine phosphorylation site. This protein is involved in cargo-specific control of clathrin-mediated endocytosis, specifically controlling the internalization of a specific protein receptor. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.525); alcohol drinking (0.364); sialolithiasis (0.356); duodenitis (0.312); urolithiasis (0.307)
- **Europe PMC papers**: 395
- **Why important**: SH3BP4 forms the module's clearest trafficking-associated pair with GIPC1 in STRING and is present with GIPC1 in multiple hu.MAP complexes. Its known functions include cargo-specific control of clathrin-mediated endocytosis, actin organization, Rho signaling, autophagy, and TOR-related regulation. HPA shows enhancement in secretory epithelial cell types and enrichment in selected antigen-presenting or granulocyte-related blood-cell categories. These features connect membrane trafficking with cell-state regulation.
- **Conclusion**: Established evidence supports SH3BP4 as an endocytic and cytoskeletal adaptor that gives biological credibility to the GIPC1-associated submodule. The data do not establish that SH3BP4 mediates the broad module-wide correlation or that immune annotations explain the module in the two queried systems.

#### IGF2R

- **Related proteins** (co-abundance neighbors): MLC1 (0.88); STRING partners: CPD (0.738)
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enhanced; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor 2 receptor. This gene encodes a receptor for both insulin-like growth factor 2 and mannose 6-phosphate. The binding sites for each ligand are located on different segments of the protein. This receptor has various functions, including in the intracellular trafficking of lysosomal enzymes, the activation of transforming growth factor beta, and the degradation of insulin-like growth factor 2. Mutation or loss o…
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.498); coronary artery disorder (0.477); Hypercholesterolemia (0.369); myocardial ischemia (0.359); coronary atherosclerosis (0.349)
- **Europe PMC papers**: 12245
- **Why important**: IGF2R is paired with CPD in STRING, and both genes have trafficking or protein-processing annotations. IGF2R binds insulin-like growth factor two and mannose six-phosphate, targets lysosomal enzymes, participates in lysosomal transport, and has roles in growth-factor and liver biology. HPA specifically identifies neutrophil enrichment, while disease resources associate the gene with hepatocellular carcinoma and cardiovascular phenotypes. Its extensive literature support makes it a strong candidate for the lysosomal and cargo-sorting branch.
- **Conclusion**: Established evidence supports IGF2R as a multifunctional cargo and lysosomal trafficking receptor, with a known CPD relationship in this module. The interpretation that its co-abundance with MLC1 reflects coordinated lysosomal or membrane turnover is plausible but remains a hypothesis.

#### STAT1

- **Related proteins** (co-abundance neighbors): MLC1 (0.88); STRING partners: BST2 (0.813)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal transducer and activator of transcription 1. The protein encoded by this gene is a member of the STAT protein family. In response to cytokines and growth factors, STAT family members are phosphorylated by the receptor associated kinases, and then form homo- or heterodimers that translocate to the cell nucleus where they act as transcription activators. The protein encoded by this gene can be activated by various ligands including interferon-…
- **Diseases (Open Targets)**: immunodeficiency 31B (0.786); chronic mucocutaneous candidiasis (0.775); autoimmune enteropathy and endocrinopathy - susceptibility to chronic infections syndrome (0.772); cancer (0.554); immunodeficiency disease (0.482)
- **Europe PMC papers**: 66602
- **Why important**: STAT1 forms a high-confidence STRING relationship with BST2 and is a well-characterized cytokine- and growth-factor-responsive transcription factor. Its annotations include antiviral defense, interferon-related response, and transcriptional regulation, and disease resources strongly associate it with immunodeficiency and chronic infection susceptibility. It therefore provides a mechanistically distinct, inducible signaling branch that could explain part of the module's shared abundance pattern under stress or inflammatory conditions.
- **Conclusion**: Established evidence supports STAT1 as an antiviral and cytokine-responsive transcriptional regulator, and the BST2 relationship supports an immune-response submodule. It is not established that interferon signaling drives the complete module, particularly because the module lacks global enrichment and most genes have low immune-cell specificity.

## Module 12

**Tissue pair**: cell line and stem_cells  
**Genes (9)**: CDH2, COPB1, DTWD2, ELOVL6, GNAO1, HAUS6, IDI1, MED24, SUGP2

### Function

No single module function is established by the enrichment analysis: no GO or KEGG term passed global correction, and there was no supplementary STRING functional enrichment. The network is hub-centered, with ELOVL6 connected to every other member while the remaining genes are peripheral. The annotations nevertheless suggest several biological themes that may explain the co-abundance pattern: ELOVL6 and IDI1 support lipid, isoprenoid, and cholesterol-related metabolism; COPB1 supports Golgi and endoplasmic-reticulum vesicle trafficking; MED24 supports RNA polymerase II transcription; SUGP2 supports RNA processing; DTWD2 supports tRNA modification; HAUS6 supports microtubule organization and chromosome segregation; and CDH2 and GNAO1 support cell adhesion and signal transduction, respectively. Taken together, this is better described as a mixed cellular-expression module centered on ELOVL6 than as a demonstrated pathway or molecular complex. The functional interpretation remains hypothesis-generating because the co-abundance association does not establish biochemical interaction or common pathway membership.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of its members is annotated as secreted. It is also not clearly a blood-cell module. HPA annotations show generally broad tissue behavior for most members, with a smaller set having tissue-enhanced expression in liver, brain, retina, or heart muscle. Many genes are cell-type enhanced, but the reported cell types are heterogeneous and include neural, cardiac, epithelial, germ-cell, and erythroid-related populations. Most members have low immune-cell specificity, while only a minority show blood-cell group enrichment and others are not detected in immune cells. Thus, contamination by plasma proteins is not a plausible explanation, and a single blood-cell source is not supported. The broad and heterogeneous HPA pattern is compatible with shared cellular-state, developmental, or housekeeping-like transcriptional effects, but HPA protein detection provides no direct protein-level confirmation for either sampled context.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship was detected among the module members, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. These findings argue against interpreting the module as a known physical protein complex or as a set of established direct protein interactions. They do not invalidate the co-abundance pattern: co-regulation, shared cell state, indirect pathway coupling, compartmental coordination, or context-specific interactions can occur without representation in STRING or hu.MAP. The star-like topology therefore reflects the observed co-abundance structure rather than validated molecular binding.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared co-abundance pattern appears potentially novel as a network-level observation because the member set has no matching high-confidence STRING interactions or multi-member hu.MAP complex. However, this is not proof of a new biological mechanism. Most constituent genes have established individual functions and disease or literature associations, so the novelty would reside in their coordinated abundance across cell line and stem-cell samples, particularly the central association of ELOVL6 with genes spanning metabolism, trafficking, transcription, RNA processing, cytoskeletal organization, adhesion, and signaling. Independent replication, preservation after adjustment for cell composition and expression breadth, and perturbation or time-course experiments would be needed to establish that the module represents a reproducible biological program rather than a dataset-specific correlation.

**Hypothesis.** Hypothesis: ELOVL6 may mark a coordinated cellular state in which membrane-lipid or isoprenoid metabolism is coupled to the biosynthetic and structural demands of proliferating or differentiating cells. In this model, IDI1 could reflect related lipid and isoprenoid supply, COPB1 could reflect membrane and secretory-trafficking requirements, HAUS6 could reflect cytoskeletal or cell-cycle demands, and MED24, SUGP2, and DTWD2 could reflect transcriptional, RNA-processing, and translational-support programs. CDH2 and GNAO1 may capture context-dependent changes in cell adhesion and signaling. This is a mechanistic hypothesis only: the supplied data do not show that ELOVL6 regulates the other genes, that the proteins physically interact, or that lipid metabolism causes the other module features.

### Important genes

#### ELOVL6

- **Related proteins** (co-abundance neighbors): GNAO1 (0.92), CDH2 (0.92), HAUS6 (0.90), COPB1 (0.88), MED24 (0.85), SUGP2 (0.84), DTWD2 (0.80), IDI1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ELOVL fatty acid elongase 6. Fatty acid elongases (EC 6.2.1.3), such as ELOVL6, use malonyl-CoA as a 2-carbon donor in the first and rate-limiting step of fatty acid elongation (Moon et al., 2001 [PubMed 11567032]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: hypertensive disorder (0.505); atrial fibrillation (0.463); Increased blood pressure (0.422); alcohol drinking (0.221); urolithiasis (0.221)
- **Europe PMC papers**: 2959
- **Why important**: ELOVL6 is the sole network hub, connected to every other module member with the strongest aggregate association. Its established function is fatty-acid elongation, including saturated and monounsaturated fatty-acid and sphingolipid biosynthetic processes. It has extensive literature and disease-trait associations involving cardiovascular and metabolic phenotypes. Because it links genes from otherwise disparate functional categories, it is the leading candidate for a shared metabolic or cellular-state signal.
- **Conclusion**: Established evidence supports ELOVL6 as the structural center of the co-abundance module and as a lipid-metabolism gene. It is not established that ELOVL6 drives the peripheral genes. A plausible hypothesis is that its abundance tracks a broader membrane-lipid or biosynthetic state.

#### IDI1

- **Related proteins** (co-abundance neighbors): ELOVL6 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: isopentenyl-diphosphate delta isomerase 1. IDI1 encodes a peroxisomally-localized enzyme that catalyzes the interconversion of isopentenyl diphosphate (IPP) to its highly electrophilic isomer, dimethylallyl diphosphate (DMAPP), which are the substrates for the successive reaction that results in the synthesis of farnesyl diphosphate and, ultimately, cholesterol.  It has been shown in peroxisomal deficiency diseases such as Zellweger syndro…
- **Diseases (Open Targets)**: neurodegenerative disease (0.539); hypotensive disorder (0.215); placental retention (0.191); liver disorder (0.147); esophageal cancer (0.138)
- **Europe PMC papers**: 1844
- **Why important**: IDI1 is directly connected to the hub and encodes an enzyme in isoprenoid and cholesterol biosynthesis. Its annotation provides the clearest metabolic complement to ELOVL6, linking fatty-acid elongation with sterol and prenylation-related precursor supply. It has a substantial literature and disease associations spanning neurological, hepatic, placental, and esophageal contexts.
- **Conclusion**: Established evidence supports IDI1 as an isoprenoid and cholesterol-biosynthesis enzyme that could biologically complement ELOVL6. The module does not establish a coordinated lipid pathway, but joint regulation of these genes is a testable hypothesis.

#### CDH2

- **Related proteins** (co-abundance neighbors): ELOVL6 (0.92); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cadherin 2. This gene encodes a classical cadherin and member of the cadherin superfamily. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein is proteolytically processed to generate a calcium-dependent cell adhesion molecule and glycoprotein. This protein plays a role in the establishment of left-right asymmetry, development of the nervous system and t…
- **Diseases (Open Targets)**: agenesis of corpus callosum, cardiac, ocular, and genital syndrome (0.809); arrhythmogenic right ventricular dysplasia, familial, 14 (0.583); Agenesis of corpus callosum (0.515); attention deficit-hyperactivity disorder 8 (0.505); aortic stenosis (0.481)
- **Europe PMC papers**: 35205
- **Why important**: CDH2 is a direct hub neighbor and encodes a plasma-membrane classical cadherin involved in calcium-dependent cell adhesion, cell-cell junctions, nervous-system development, and synapse assembly. Its tissue and cell-type annotations include heart, neural, and epithelial contexts, and it has very extensive literature together with developmental and cardiac disease associations. It may connect the metabolic signal to cell architecture or differentiation state.
- **Conclusion**: Established evidence supports CDH2 as an adhesion and developmental regulator with broad relevance to the sampled cell states. Its co-abundance with ELOVL6 does not demonstrate a direct metabolic-adhesion mechanism; that connection remains a hypothesis requiring cell-state and perturbation analyses.

#### GNAO1

- **Related proteins** (co-abundance neighbors): ELOVL6 (0.92); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein subunit alpha o1. The protein encoded by this gene represents the alpha subunit of the Go heterotrimeric G-protein signal-transducing complex. Defects in this gene are a cause of early-onset epileptic encephalopathy. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2015].
- **Diseases (Open Targets)**: neurodevelopmental disorder with involuntary movements (0.809); developmental and epileptic encephalopathy, 17 (0.801); genetic developmental and epileptic encephalopathy (0.692); Epileptic encephalopathy (0.657); infantile epileptic encephalopathy (0.555)
- **Europe PMC papers**: 1546
- **Why important**: GNAO1 is a direct, relatively strong hub neighbor and encodes the alpha subunit of a Go heterotrimeric G-protein complex. It participates in inhibitory GPCR signaling and is strongly associated with early-onset epileptic encephalopathy and neurodevelopmental disorders. Its HPA pattern is enriched in brain and retina and in several neural cell types, making it informative for interpreting the module's heterogeneous cellular context despite its peripheral network position.
- **Conclusion**: Established evidence supports GNAO1 as a neuronal signaling gene with important developmental disease relevance. The supplied data do not establish that the module is neuronal or that ELOVL6 controls GNAO1; neural-cell representation or a shared differentiation state is an alternative hypothesis.

#### HAUS6

- **Related proteins** (co-abundance neighbors): ELOVL6 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Centriolar satellite, Cytosol, Acrosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HAUS augmin like complex subunit 6. The protein encoded by this gene is a subunit of the augmin complex. The augmin complex plays a role in microtubule attachment to the kinetochore and central spindle formation. This protein may have a role in efficient chromosome congression and segregation by promoting microtubule-dependent microtubule amplification. Pseudogenes of this gene are located on chromosomes 7 and 20. Alternative splici…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.361); Abnormality of the skeletal system (0.312); prostate carcinoma (0.310); aortic stenosis (0.284); coronary artery disorder (0.249)
- **Europe PMC papers**: 233
- **Why important**: HAUS6 is a direct hub neighbor and a component of the augmin complex, which supports microtubule attachment, spindle assembly, centrosome-related processes, and chromosome segregation. Its HPA annotations include erythrocyte progenitors and germ-cell populations, contexts in which proliferation and division are prominent. Although its literature volume is more limited than that of ELOVL6 or CDH2, its function offers a concrete cell-cycle and cytoskeletal interpretation of the module.
- **Conclusion**: Established evidence supports HAUS6 as a microtubule and chromosome-segregation factor. Its presence may reflect a proliferative or differentiation-associated cellular state, but the data do not show that cell-cycle activity is the cause of the module or that HAUS6 is mechanistically linked to ELOVL6.

## Module 13

**Tissue pair**: cell line and stem_cells  
**Genes (5)**: CCDC77, HSDL1, PEX14, TMEM222, SLC7A6

### Function

No single module function is established by the enrichment analysis: no GO or KEGG term passed global correction, and STRING functional enrichment was absent. The gene annotations nevertheless point to a possible cellular logistics and metabolic-maintenance theme spanning amino-acid transport, peroxisomal protein import, mitochondrial oxidoreduction, membrane biology, and centrosomal or nuclear-membrane organization. This is an interpretive synthesis of individual annotations rather than a significantly enriched pathway. The co-abundance topology places CCDC77 at the center, linking TMEM222, HSDL1, and PEX14, while SLC7A6 connects through TMEM222.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins: the HPA summary reports no secreted genes. All members have low immune-cell specificity, with no enriched blood-cell category, arguing against an obvious blood-cell or plasma-protein signature. Most genes have low tissue specificity, although SLC7A6 is tissue enhanced in skeletal muscle. Each gene is cell-type enhanced, but the highlighted cell types are heterogeneous, including cardiomyocytes, esophageal apical cells, late spermatocytes or spermatids, platelets, rod photoreceptor cells, adipocytes, and myonuclei. Thus the shared module may reflect broadly expressed cellular machinery or mixed cell-type contributions rather than a single lineage-specific program. HPA protein detection for the relevant cell-line and stem-cell tissue comparisons was unavailable.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair met the stated STRING interaction threshold, and no STRING functional-enrichment result was reported. No hu.MAP complex contained multiple module members. Therefore the co-abundance edges are not supported here as established high-confidence physical interactions or as a known multiprotein complex. The absence of STRING and hu.MAP support does not invalidate the co-abundance module; it indicates that its relationships may be indirect, context-dependent, poorly characterized, or driven by coordinated regulation rather than direct binding.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is a potentially novel co-abundance association because its internal pattern is not represented by a recognized STRING interaction set or hu.MAP complex, and no established enriched pathway explains it. However, it cannot be called a definitively new biological discovery from this evidence alone. The absence of external database support is not proof of novelty, and the lack of globally significant GO or KEGG enrichment means that the proposed shared program remains weakly characterized. Independent replication, expression-level validation, perturbation, and comparison with additional tissue groups would be needed to establish novelty and biological reproducibility.

**Hypothesis.** Hypothesis: in cell-line and stem-cell contexts, coordinated regulation of membrane and organelle homeostasis links SLC7A6-mediated basic-amino-acid transport with TMEM222 membrane biology, while CCDC77 may act as a structural or organizational connector associated with the nuclear membrane or centrosome. HSDL1 could represent a mitochondrial redox component and PEX14 a peroxisomal import component, together forming a broader stress-sensitive cellular-maintenance program. This hypothesis is based on co-abundance and individual gene annotations; it is not demonstrated by enrichment, physical-interaction, or complex evidence.

### Important genes

#### CCDC77

- **Related proteins** (co-abundance neighbors): TMEM222 (0.87), HSDL1 (0.83), PEX14 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coiled-coil domain containing 77. Located in centrosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: obstructive sleep apnea syndrome (0.325); neurodegenerative disease (0.311); type 2 diabetes mellitus (0.205); lacrimal apparatus disorder (0.079); diabetes mellitus (0.065)
- **Europe PMC papers**: 111
- **Why important**: CCDC77 has the strongest central network position in the module and connects to TMEM222, HSDL1, and PEX14. Its annotation places it at the centrosome and nuclear membrane, making it the most informative candidate for a structural or organizational role. Its disease associations include obstructive sleep apnea syndrome, neurodegenerative disease, and type two diabetes mellitus, while its literature volume is moderate relative to the other selected genes.
- **Conclusion**: Established evidence supports CCDC77 as the module's central co-abundance connector and as a centrosome-associated protein. A coordinating role between membrane, organelle, and cytoskeletal processes is a hypothesis, not an established function.

#### PEX14

- **Related proteins** (co-abundance neighbors): CCDC77 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Peroxisomes; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peroxisomal biogenesis factor 14. This gene encodes an essential component of the peroxisomal import machinery. The protein is integrated into peroxisome membranes with its C-terminus exposed to the cytosol, and interacts with the cytosolic receptor for proteins containing a PTS1 peroxisomal targeting signal. The protein also functions as a transcriptional corepressor and interacts with a histone deacetylase. A mutation in this ge…
- **Diseases (Open Targets)**: Zellweger spectrum disorders (0.784); peroxisome biogenesis disorder 13A (Zellweger) (0.739); peroxisome biogenesis disorder, complementation group K (0.663); peroxisome biogenesis disorder (0.597); peroxisomal disease (0.597)
- **Europe PMC papers**: 1422
- **Why important**: PEX14 is directly connected to CCDC77 and has the clearest established organelle function in the module. It is an essential component of peroxisomal import machinery, participates in peroxisome organization and matrix-protein import, and is linked to reactive-oxygen-species responses. Its disease associations include Zellweger spectrum and other peroxisome-biogenesis disorders, and it has the largest literature volume among the module genes.
- **Conclusion**: Established evidence identifies PEX14 as a peroxisomal import and biogenesis factor with strong disease relevance. Its participation in the shared module suggests coordinated peroxisomal maintenance, but does not prove that PEX14 mechanistically drives the module.

#### SLC7A6

- **Related proteins** (co-abundance neighbors): TMEM222 (0.95); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 7 member 6. Enables basic amino acid transmembrane transporter activity. Involved in basic amino acid transmembrane transport and ornithine transport. Located in intracellular membrane-bounded organelle and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.479); hepatocellular carcinoma (0.072); urinary bladder carcinoma (0.060); urinary bladder cancer (0.060); hypothyroidism (0.052)
- **Europe PMC papers**: 677
- **Why important**: SLC7A6 is the module's strongest weighted edge partner through TMEM222 and is the only member with tissue-enhanced HPA expression, notably in skeletal muscle. It enables basic-amino-acid transport and is annotated in ornithine, neutral-amino-acid, leucine, glycine-betaine, and nitric-oxide-related biology. It also has substantial disease-association and literature coverage.
- **Conclusion**: Established evidence supports SLC7A6 as a membrane amino-acid transporter with possible relevance to muscle-associated metabolism. Its connection to the module may reflect coordinated nutrient and organelle homeostasis, but the module does not establish a new transporter function or causal disease mechanism.

#### TMEM222

- **Related proteins** (co-abundance neighbors): SLC7A6 (0.95), CCDC77 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transmembrane protein 222. Predicted to be integral component of membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder with motor and speech delay and behavioral abnormalities (0.686); complex neurodevelopmental disorder (0.370); hereditary disease (0.191); ovarian dysfunction (0.024); neurodevelopmental disorder (0.009)
- **Europe PMC papers**: 81
- **Why important**: TMEM222 links SLC7A6 to the central CCDC77 node and is annotated as an integral membrane protein located at the plasma membrane and in the cytosol. Its cell-type-enhanced pattern is heterogeneous, including esophageal apical cells and late spermatids, and its disease associations include a neurodevelopmental disorder with motor, speech, and behavioral abnormalities.
- **Conclusion**: Established evidence supports TMEM222 as a membrane-associated protein and as a co-abundance bridge within this module. Its molecular function and mechanism remain insufficiently defined, so any role in coupling amino-acid transport to structural or organelle processes is hypothetical.

#### HSDL1

- **Related proteins** (co-abundance neighbors): CCDC77 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydroxysteroid dehydrogenase like 1. Predicted to enable oxidoreductase activity. Located in intermediate filament cytoskeleton and mitochondrion. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.459); mathematical ability (0.318); uveitis (0.027); neoplasm (0.013); prostate carcinoma (0.006)
- **Europe PMC papers**: 133
- **Why important**: HSDL1 connects directly to CCDC77 and is annotated as a hydroxysteroid-dehydrogenase-like protein with predicted oxidoreductase activity in mitochondria and the intermediate-filament cytoskeleton. Its HPA cell-type-enhanced annotations include late primary spermatocytes and platelets, and its disease associations include neurodegenerative disease. The available literature is limited compared with PEX14 and SLC7A6.
- **Conclusion**: Established evidence supports a predicted oxidoreductase role and mitochondrial localization, but functional characterization is comparatively limited. Its co-abundance with CCDC77 may indicate redox-sensitive structural coordination, although that mechanism remains a hypothesis.
