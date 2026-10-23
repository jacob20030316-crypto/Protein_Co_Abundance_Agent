# Conserved co-abundance modules: myometrium and stem_cells

## Module 0

**Tissue pair**: myometrium and stem_cells  
**Genes (14)**: PGD, COPS3, NAA15, PDXP, PPM1G, GART, AARS1, TNPO1, TNPO3, UBA3, USO1, XPO1, CSE1L, XPO7

### Function

The strongest interpretation is a nucleocytoplasmic transport module. The primary evidence is the convergence of (GO:MF nucleocytoplasmic carrier activity; q_global = 0.000246), (KEGG Nucleocytoplasmic transport - Homo sapiens (human); q_global = 0.00182), and (GO:MF molecular carrier activity; q_global = 0.00825) on carrier-mediated movement between the nucleus and cytoplasm, together with (GO:MF nuclear export signal receptor activity; q_global = 0.0228) implicating nuclear export signal receptor activity. The five genes shared by the carrier terms—CSE1L, TNPO1, TNPO3, XPO1, and XPO7—form the functional core. The module also contains genes involved in vesicle transport, protein maturation, ubiquitin-like modification, purine synthesis, pentose-phosphate metabolism, phosphatase activity, and signalosome function, but these annotations are not supported by globally corrected GO/KEGG enrichment in this module. Thus, the module is best viewed as a transport-centered regulatory program rather than a broad metabolic pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the encoded proteins are predominantly intracellular. Most genes have low tissue specificity and low immune-cell specificity, consistent with broadly expressed cellular machinery or housekeeping-like functions. HPA does identify selected cell-type or tissue enrichments, including germ-cell, neutrophil-lineage, brain, liver, skeletal-muscle, and testis-associated patterns, but these are distributed across individual genes rather than defining the whole module. PGD is particularly compatible with blood or hematopoietic contribution because it is enriched in several blood-cell categories and in neutrophil-related cell types. However, the overall composition does not support a predominantly blood-cell or plasma-contamination explanation. Myometrium protein detection is present for many of the genes, whereas the stem-cell comparison has no matching HPA tissue category, so HPA cannot independently establish the cellular source of the shared stem-cell signal.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleocytoplasmic carrier activity | 0.000246 | CSE1L, TNPO1, TNPO3, XPO1, XPO7 |
| KEGG Nucleocytoplasmic transport - Homo sapiens (human) | 0.00182 | CSE1L, TNPO1, TNPO3, XPO1, XPO7 |
| GO:MF molecular carrier activity | 0.00825 | CSE1L, TNPO1, TNPO3, XPO1, XPO7 |
| GO:MF nuclear export signal receptor activity | 0.0228 | CSE1L, XPO1, XPO7 |

### STRING and hu.MAP

STRING provides established high-confidence relationships among the transport genes: CSE1L connects strongly with XPO1, XPO7, and TNPO1; TNPO1 connects with TNPO3 and XPO1; TNPO3 connects with XPO1; and XPO1 connects with XPO7. These relationships support a coherent karyopherin and nuclear-transport core rather than an arbitrary co-abundance grouping. The STRING functional results (STRING NetworkNeighborAL Nucleocytoplasmic carrier activity, and Exportin-2, central domain; within-query FDR = 0.00011) through (STRING Function Small GTPase binding; within-query FDR = 0.0203) independently reinforce nucleocytoplasmic carrier activity, importin-beta-like domains, nuclear export receptor activity, armadillo-type folds, and small-GTPase binding, but they remain supplementary rather than global enrichment evidence. hu.MAP supplies orthogonal complex-level support. In particular, TNPO1, TNPO3, and XPO7 co-occur in (hu.MAP huMAP3_11232.1), while XPO1, CSE1L, and TNPO1 co-occur in (hu.MAP huMAP3_09592.1); additional hu.MAP complexes repeatedly contain XPO1 with CSE1L, XPO7 with TNPO3, or TNPO1 with TNPO3 in (hu.MAP huMAP3_05832.1) through (hu.MAP huMAP3_10287.1). These complexes are generally large and include many proteins outside the module, so they support membership in known transport-associated assemblies but do not show that the entire co-abundance module is one purified physical complex. The non-transport genes have limited direct STRING or hu.MAP support in the supplied evidence, apart from AARS1 and PGD appearing together in (hu.MAP huMAP3_14442.1).

**STRING interactions (score >= 0.7)**: 7 of 91 gene pairs: CSE1L–TNPO1 (0.824); CSE1L–XPO1 (0.976); CSE1L–XPO7 (0.765); TNPO1–TNPO3 (0.974); TNPO1–XPO1 (0.868); TNPO3–XPO1 (0.764); XPO1–XPO7 (0.879)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Nucleocytoplasmic carrier activity, and Exportin-2, central domain (FDR = 0.00011, 5 genes); Function Nucleocytoplasmic carrier activity (FDR = 0.00024, 5 genes); SMART Importin-beta N-terminal domain (FDR = 0.00087, 4 genes); InterPro Armadillo-like helical (FDR = 0.0019, 6 genes); InterPro Importin-beta, N-terminal domain (FDR = 0.0024, 4 genes); InterPro Armadillo-type fold (FDR = 0.0045, 6 genes); NetworkNeighborAL Importin-beta, N-terminal domain (FDR = 0.0071, 3 genes); Function Nuclear export signal receptor activity (FDR = 0.0133, 3 genes); Function Small GTPase binding (FDR = 0.0203, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11232.1 (TNPO1, XPO7, TNPO3; 3/78); huMAP3_09592.1 (XPO1, CSE1L, TNPO1; 3/95); huMAP3_05832.1 (XPO7, TNPO3; 2/14); huMAP3_07170.1 (XPO1, CSE1L; 2/14); huMAP3_06077.1 (XPO7, TNPO3; 2/15); huMAP3_08298.1 (XPO7, TNPO3; 2/24); huMAP3_09053.1 (TNPO1, TNPO3; 2/25); huMAP3_09042.1 (XPO1, CSE1L; 2/26); huMAP3_09114.1 (XPO7, TNPO3; 2/30); huMAP3_06791.1 (XPO1, CSE1L; 2/31); huMAP3_10202.1 (XPO7, TNPO3; 2/52); huMAP3_10287.1 (XPO7, TNPO3; 2/53); huMAP3_14442.1 (AARS1, PGD; 2/57)

### Novelty

The transport function itself is not a new biological discovery: the core genes have established annotations, STRING relationships, and repeated hu.MAP complex membership. The potentially novel aspect is the observation that this particular combination of transport factors and broadly expressed cellular genes forms a conserved co-abundance module shared by myometrium and stem_cells. That claim is plausible but cannot be called definitively new from the supplied databases alone. Known STRING and hu.MAP relationships explain much of the core, while the module-level organization and its tissue-pair conservation may represent a new systems-level observation. Absence of database relationships for some peripheral genes is not evidence of novelty, because database coverage, tissue context, and co-abundance do not require direct physical interaction.

**Hypothesis.** Hypothesis: the shared module reflects coordinated control of nuclear import and export that helps maintain a responsive cellular state across myometrial and stem-cell contexts. The transport core could jointly regulate the nuclear availability of transcriptional regulators, splicing factors, and other cargoes, with TNPO3 potentially influencing transport of serine/arginine-rich splicing factors, XPO1 and XPO7 supporting export, and CSE1L supporting recycling of importin-alpha. USO1 may connect this program to endoplasmic-reticulum-to-Golgi trafficking, while NAA15, UBA3, COPS3, PPM1G, GART, PGD, PDXP, and AARS1 may reflect coupled demands for protein maturation, modification, translation, nucleotide metabolism, and stress adaptation. This is a mechanistic model, not a demonstrated causal pathway; direct perturbation and cargo-level experiments would be required to test it.

### Important genes

#### XPO1

- **Related proteins** (co-abundance neighbors): CSE1L (0.86), USO1 (0.82); STRING partners: CSE1L (0.976), TNPO1 (0.868), TNPO3 (0.764), XPO7 (0.879)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_09592.1, huMAP3_07170.1, huMAP3_09042.1, huMAP3_06791.1
- **Function (MyGene.info)**: exportin 1. This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSe…
- **Diseases (Open Targets)**: plasma cell myeloma (0.642); B-cell chronic lymphocytic leukemia (0.626); diffuse large B-cell lymphoma (0.602); HIV infectious disease (0.561); neurodegenerative disease (0.522)
- **Europe PMC papers**: 5357
- **Why important**: XPO1 is a central transport-core gene supported by all primary enrichment terms (GO:MF nucleocytoplasmic carrier activity; q_global = 0.000246) through (GO:MF nuclear export signal receptor activity; q_global = 0.0228) and by the STRING carrier and export findings (STRING NetworkNeighborAL Nucleocytoplasmic carrier activity, and Exportin-2, central domain; within-query FDR = 0.00011), (STRING Function Nucleocytoplasmic carrier activity; within-query FDR = 0.00024), and (STRING Function Nuclear export signal receptor activity; within-query FDR = 0.0133). It has established roles in export of nuclear proteins and RNA-related cargoes and connects in STRING to CSE1L, TNPO1, TNPO3, and XPO7. It is also represented in several hu.MAP assemblies (hu.MAP huMAP3_09592.1), (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), and (hu.MAP huMAP3_06791.1). Its large literature base and disease associations make it the most extensively characterized anchor for interpreting the module.
- **Conclusion**: Established evidence supports XPO1 as a core nuclear-export component and a major interpretive anchor. Its co-abundance here is consistent with coordinated transport capacity, but the data do not establish altered XPO1 activity, cargo specificity, or causality in either tissue.

#### TNPO1

- **Related proteins** (co-abundance neighbors): TNPO3 (0.88), NAA15 (0.86), USO1 (0.83), AARS1 (0.82); STRING partners: CSE1L (0.824), TNPO3 (0.974), XPO1 (0.868)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_11232.1, huMAP3_09592.1, huMAP3_09053.1
- **Function (MyGene.info)**: transportin 1. This gene encodes the beta subunit of the karyopherin receptor complex which interacts with nuclear localization signals to target nuclear proteins to the nucleus. The karyopherin receptor complex is a heterodimer of an alpha subunit which recognizes the nuclear localization signal and a beta subunit which docks the complex at nucleoporins. Alternate splicing of this gene results in several transc…
- **Diseases (Open Targets)**: atrial fibrillation (0.415); neurodegenerative disease (0.370); hypothyroidism (0.320); injury (0.198); bladder calculus (0.183)
- **Europe PMC papers**: 822
- **Why important**: TNPO1 is a high-connectivity module gene and participates in the primary carrier terms (GO:MF nucleocytoplasmic carrier activity; q_global = 0.000246), (KEGG Nucleocytoplasmic transport - Homo sapiens (human); q_global = 0.00182), and (GO:MF molecular carrier activity; q_global = 0.00825). Its known function as a karyopherin beta-family import receptor directly matches the module interpretation. STRING links TNPO1 to CSE1L, TNPO3, and XPO1, and hu.MAP places it in (hu.MAP huMAP3_11232.1), (hu.MAP huMAP3_09592.1), and (hu.MAP huMAP3_09053.1). Its network position bridges the transport core with AARS1 and USO1, while its substantial literature supports a well-established cellular role.
- **Conclusion**: Established evidence supports TNPO1 as an import-receptor component that helps define the module's transport identity. It may coordinate import with export factors in the shared program, but coordinated regulation is a hypothesis rather than a demonstrated interaction in these samples.

#### TNPO3

- **Related proteins** (co-abundance neighbors): TNPO1 (0.88), USO1 (0.83); STRING partners: TNPO1 (0.974), XPO1 (0.764)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_11232.1, huMAP3_05832.1, huMAP3_06077.1, huMAP3_08298.1, huMAP3_09053.1, huMAP3_09114.1, huMAP3_10202.1, huMAP3_10287.1
- **Function (MyGene.info)**: transportin 3. The protein encoded by this gene is a nuclear import receptor for serine/arginine-rich (SR) proteins such as the splicing factors SFRS1 and SFRS2. The encoded protein has also been shown to be involved in HIV-1 infection, apparently through interaction with the HIV-1 capsid protein. Several protein-coding and non-coding transcript variants have been found for this gene. [provided by RefSeq, Apr 20…
- **Diseases (Open Targets)**: autosomal dominant limb-girdle muscular dystrophy type 1F (0.722); neurodegenerative disease (0.521); lysosomal storage disease (0.492); Parkinson disease (0.462); Alzheimer disease (0.462)
- **Europe PMC papers**: 1366
- **Why important**: TNPO3 is included in the primary carrier terms (GO:MF nucleocytoplasmic carrier activity; q_global = 0.000246), (KEGG Nucleocytoplasmic transport - Homo sapiens (human); q_global = 0.00182), and (GO:MF molecular carrier activity; q_global = 0.00825), has a strong STRING relationship with TNPO1, and connects to XPO1. Its established function in nuclear import of serine/arginine-rich splicing factors gives the module a potential link between nucleocytoplasmic transport and RNA processing. TNPO3 recurs across many hu.MAP complexes, including (hu.MAP huMAP3_11232.1), (hu.MAP huMAP3_05832.1), (hu.MAP huMAP3_06077.1), (hu.MAP huMAP3_08298.1), (hu.MAP huMAP3_09053.1), (hu.MAP huMAP3_09114.1), (hu.MAP huMAP3_10202.1), and (hu.MAP huMAP3_10287.1). Its disease associations and substantial literature further support its importance.
- **Conclusion**: Established evidence supports TNPO3 as a transport receptor with a plausible connection to splice-factor trafficking. A role in coordinating splicing-related nuclear transport within this module is biologically plausible, but it remains a hypothesis without cargo or perturbation measurements.

#### CSE1L

- **Related proteins** (co-abundance neighbors): AARS1 (0.88), XPO1 (0.86), PDXP (0.86); STRING partners: TNPO1 (0.824), XPO1 (0.976), XPO7 (0.765)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09592.1, huMAP3_07170.1, huMAP3_09042.1, huMAP3_06791.1
- **Function (MyGene.info)**: chromosome segregation 1 like. Proteins that carry a nuclear localization signal (NLS) are transported into the nucleus by the importin-alpha/beta heterodimer. Importin-alpha binds the NLS, while importin-beta mediates translocation through the nuclear pore complex. After translocation, RanGTP binds importin-beta and displaces importin-alpha. Importin-alpha must then be returned to the cytoplasm, leaving the NLS protein behind.…
- **Diseases (Open Targets)**: intelligence (0.293); neurodegenerative disease (0.269); Alzheimer disease (0.199); celiac disease (0.187); autism spectrum disorder (0.178)
- **Europe PMC papers**: 860
- **Why important**: CSE1L is present in every primary enrichment term (GO:MF nucleocytoplasmic carrier activity; q_global = 0.000246) through (GO:MF nuclear export signal receptor activity; q_global = 0.0228) and is strongly connected in STRING to XPO1, XPO7, and TNPO1. Its known role in recycling importin-alpha after nuclear import provides a mechanistic complement to the import and export receptors. It is represented in several hu.MAP assemblies (hu.MAP huMAP3_09592.1), (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), and (hu.MAP huMAP3_06791.1), and it has a substantial literature base and disease associations. Its module position links the transport core with AARS1 and PDXP.
- **Conclusion**: Established evidence supports CSE1L as a recycling factor that reinforces the interpretation of a coordinated karyopherin system. Its lack of myometrial protein detection in HPA cautions against assuming uniform protein-level activity, and the co-abundance result alone cannot distinguish regulation from shared transcriptional control.

#### XPO7

- **Related proteins** (co-abundance neighbors): AARS1 (0.81); STRING partners: CSE1L (0.765), XPO1 (0.879)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11232.1, huMAP3_05832.1, huMAP3_06077.1, huMAP3_08298.1, huMAP3_09114.1, huMAP3_10202.1, huMAP3_10287.1
- **Function (MyGene.info)**: exportin 7. The transport of protein and large RNAs through the nuclear pore complexes (NPC) is an energy-dependent and regulated process. The import of proteins with a nuclear localization signal (NLS) is accomplished by recognition of one or more clusters of basic amino acids by the importin-alpha/beta complex; see MIM 600685 and MIM 602738. The small GTPase RAN (MIM 601179) plays a key role in NLS-dependen…
- **Diseases (Open Targets)**: atrial fibrillation (0.474); neurodegenerative disease (0.471); substance-related disorder (0.353); Alzheimer disease (0.351); Parkinson disease (0.351)
- **Europe PMC papers**: 450
- **Why important**: XPO7 is included in all primary enrichment terms (GO:MF nucleocytoplasmic carrier activity; q_global = 0.000246) through (GO:MF nuclear export signal receptor activity; q_global = 0.0228) and is supported by STRING relationships with CSE1L and XPO1. Its annotation as an exportin involved in protein and large-RNA transport broadens the module beyond a single export route. XPO7 repeatedly occurs with TNPO3 in hu.MAP complexes (hu.MAP huMAP3_11232.1), (hu.MAP huMAP3_05832.1), (hu.MAP huMAP3_06077.1), (hu.MAP huMAP3_08298.1), (hu.MAP huMAP3_09114.1), (hu.MAP huMAP3_10202.1), and (hu.MAP huMAP3_10287.1). It is therefore both a primary-term gene and a recurrent complex-associated component despite a more peripheral position in the co-abundance graph.
- **Conclusion**: Established evidence supports XPO7 as a second export-related component of the transport core. Its coordinated abundance with TNPO3 may indicate shared transport or cargo-regulatory biology, but the tissue-pair data do not identify the transported substrates or prove functional dependence.

## Module 1

**Tissue pair**: myometrium and stem_cells  
**Genes (29)**: ABCF1, ACO1, ACSL1, ANXA6, CANX, CAPN1, CAPN2, GPS1, HSD17B4, ENG, EML1, FERMT2, H6PD, GARS1, GSN, GBE1, IQGAP1, MOGS, REXO2, PDIA4, PFKM, PFKP, PLCD1, CTPS1, SEC23A, SSH3, STAT1, SWAP70, TARS1

### Function

The strongest functional interpretation is a calcium-responsive cellular maintenance module. Primary evidence is the globally corrected GO molecular-function term (GO:MF calcium ion binding; q_global = 0.0327), calcium ion binding, contributed by ANXA6, CANX, CAPN1, CAPN2, EML1, GSN, IQGAP1, PLCD1 and SWAP70. These genes connect calcium sensing or binding with calpain-mediated proteolysis, actin remodeling, membrane and phospholipid signaling, and cell adhesion. The module also contains coherent but less directly connected endoplasmic-reticulum and metabolic components: CANX, PDIA4 and MOGS support glycoprotein folding and quality control; PFKM, PFKP, H6PD and GBE1 support carbohydrate and energy metabolism; and ACO1, ACSL1 and HSD17B4 support central or lipid metabolism. STRING carbohydrate-binding enrichment (STRING Function Carbohydrate binding; within-query FDR = 0.0454) is supplementary rather than primary evidence. No other GO or KEGG term passed global correction. Thus, the module is best viewed as a calcium-linked cytoskeletal, proteostatic and metabolic state rather than as evidence for one narrowly defined pathway.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: only a minority of its genes are secreted, and most proteins are intracellular or membrane-associated. The HPA profile shows low tissue specificity for most genes, with additional enrichment in liver, skeletal muscle and heart muscle, and a smaller signal in adipose tissue and esophagus. Most genes have cell-type-enhanced rather than broadly uniform single-cell expression, with recurring signals in esophageal epithelial cells, spermatogenic cells, hepatocytes and syncytiotrophoblasts. Blood-cell specificity is generally low, although ENG, SWAP70, GSN, SSH3 and ACSL1 show immune or blood-cell associations. Therefore, a blood-contamination explanation is not strongly supported, but shared stromal, smooth-muscle, vascular, epithelial, metabolic or other cell populations could contribute to the conserved signal. Protein detection in myometrium supports biological presence for many module proteins; the stem-cell comparison has no matching HPA tissue annotation, so HPA cannot independently validate protein abundance in stem cells.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF calcium ion binding | 0.0327 | ANXA6, CANX, CAPN1, CAPN2, EML1, GSN, IQGAP1, PLCD1, SWAP70 |

### STRING and hu.MAP

STRING provides a limited but biologically coherent set of high-confidence relationships. The best-established links are the CAPN1-CAPN2 calpain pair, the CANX-MOGS and CANX-PDIA4 endoplasmic-reticulum relationships, the GARS1-TARS1 aminoacyl-tRNA synthetase relationship, the PFKM-PFKP glycolytic relationship, and links among H6PD, GBE1 and PFKM. These interactions support real protease, ER-quality-control, translation and carbohydrate-metabolism substructures, but they do not connect the whole module into one established physical complex. hu.MAP independently reinforces the CAPN1-CAPN2 association across many complexes and supports the PFKM-PFKP pair; it also places ACO1 and REXO2 together in one complex. The repeated CAPN1-CAPN2 representation indicates that the calpain core is particularly well established, whereas most other module edges lack corresponding STRING or hu.MAP support. The network therefore combines known molecular neighborhoods with co-abundance relationships that may reflect shared regulation, cell composition or state rather than direct binding.

**STRING interactions (score >= 0.7)**: 8 of 406 gene pairs: CANX–MOGS (0.952); CANX–PDIA4 (0.931); CAPN1–CAPN2 (0.978); GARS1–TARS1 (0.909); GBE1–H6PD (0.712); H6PD–PFKM (0.804); MOGS–PDIA4 (0.73); PFKM–PFKP (0.991)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Calcium ion binding (FDR = 0.0454, 9 genes); Function Carbohydrate binding (FDR = 0.0454, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03767.1 (CAPN1, CAPN2; 2/3); huMAP3_08670.1 (CAPN1, CAPN2; 2/4); huMAP3_04277.1 (PFKM, PFKP; 2/4); huMAP3_12414.1 (ACO1, REXO2; 2/5); huMAP3_09127.1 (CAPN1, CAPN2; 2/5); huMAP3_09328.1 (CAPN1, CAPN2; 2/6); huMAP3_10242.1 (CAPN1, CAPN2; 2/6); huMAP3_13615.1 (CAPN1, CAPN2; 2/7); huMAP3_14229.1 (CAPN1, CAPN2; 2/7); huMAP3_11557.1 (CAPN1, CAPN2; 2/8); huMAP3_12716.1 (CAPN1, CAPN2; 2/8); huMAP3_12926.1 (CAPN1, CAPN2; 2/8)

### Novelty

The exact conserved co-abundance module may be a new systems-level observation, because its full gene combination is not represented as one established STRING interaction network or one hu.MAP complex. However, it would be unjustified to call the biology wholly novel: calcium binding, calpain activity, ER folding, actin regulation, glycolysis and carbohydrate metabolism are individually well established, and several relationships are already recorded by STRING or hu.MAP. Absence from those resources cannot prove novelty because database coverage is incomplete and co-abundance is not equivalent to physical interaction. The defensible novelty claim is therefore the conservation and combination of these signals across myometrium and stem_cells, which should be tested in independent cohorts, by cell-composition adjustment and with orthogonal protein or perturbation measurements. The web search did not identify a module-specific publication establishing this exact combination.

**Hypothesis.** Hypothesis: the conserved module marks a shared calcium-sensitive structural and metabolic state in myometrial and stem-cell populations. Calcium-dependent annexin and gelsolin functions, PLC-mediated phosphoinositide signaling and calpain proteolysis could coordinate cytoskeletal remodeling, adhesion and responses to mechanical or differentiation-related cues. In parallel, the CANX-PDIA4-MOGS relationships could maintain ER folding capacity, while PFKM-PFKP, H6PD, GBE1, ACO1 and ACSL1 provide metabolic support. A plausible model is that calcium flux or mechanical stimulation couples membrane signaling to calpain and actin remodeling, with ER and carbohydrate metabolism adapting to the resulting protein-synthesis and energy demands. This is a mechanistic hypothesis, not demonstrated causation; the co-abundance data do not establish directionality, direct binding or whether the shared signal originates from the same cell type in both tissues.

Web sources: https://www.proteinatlas.org/

### Important genes

#### CAPN2

- **Related proteins** (co-abundance neighbors): ACO1 (0.92), H6PD (0.90), ACSL1 (0.86), PLCD1 (0.85), GSN (0.83); STRING partners: CAPN1 (0.978)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Connecting piece, Mid piece; IHC detected in none
- **hu.MAP 3.0**: huMAP3_03767.1, huMAP3_08670.1, huMAP3_09127.1, huMAP3_09328.1, huMAP3_10242.1, huMAP3_13615.1, huMAP3_14229.1, huMAP3_11557.1, huMAP3_12716.1, huMAP3_12926.1
- **Function (MyGene.info)**: calpain 2. The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpa…
- **Diseases (Open Targets)**: Alzheimer disease (0.389); urolithiasis (0.288); alcohol drinking (0.288); aortic stenosis (0.141); neoplasm (0.105)
- **Europe PMC papers**: 1796
- **Why important**: CAPN2 is a central calcium-activated intracellular protease in the module, linked in the module network to ACO1, H6PD, ACSL1, PLCD1 and GSN. It contributes directly to the primary calcium-binding annotation (GO:MF calcium ion binding; q_global = 0.0327) and to the supplementary STRING calcium-binding signal (STRING Function Calcium ion binding; within-query FDR = 0.0454). Its partnership with CAPN1 is strongly supported by STRING and repeatedly supported by hu.MAP complexes (hu.MAP huMAP3_03767.1) through (hu.MAP huMAP3_12926.1). Its established roles include proteolysis, response to hypoxia, response to mechanical stimulus and pregnancy-related biology. It therefore provides the clearest mechanistic bridge between calcium regulation and structural remodeling.
- **Conclusion**: Established evidence supports CAPN2 as a core calpain component and a major anchor of the calcium-related interpretation. The hypothesis that CAPN2 is the active driver coupling calcium flux to module-wide remodeling remains to be tested, because co-abundance does not demonstrate protease activation.

#### CAPN1

- **Related proteins** (co-abundance neighbors): ENG (0.88), PLCD1 (0.85), GSN (0.80); STRING partners: CAPN2 (0.978)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_03767.1, huMAP3_08670.1, huMAP3_09127.1, huMAP3_09328.1, huMAP3_10242.1, huMAP3_13615.1, huMAP3_14229.1, huMAP3_11557.1, huMAP3_12716.1, huMAP3_12926.1
- **Function (MyGene.info)**: calpain 1. The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpa…
- **Diseases (Open Targets)**: Autosomal recessive spastic paraplegia type 76 (0.781); Alzheimer disease (0.383); neurodegenerative disease (0.326); hereditary spastic paraplegia 11 (0.266); hereditary disease (0.193)
- **Europe PMC papers**: 1869
- **Why important**: CAPN1 forms the best-supported physical pair in the module with CAPN2 and participates in the repeated hu.MAP calpain complexes (hu.MAP huMAP3_03767.1) through (hu.MAP huMAP3_12926.1). It is also part of the primary calcium-binding term (GO:MF calcium ion binding; q_global = 0.0327) and STRING calcium signal (STRING Function Calcium ion binding; within-query FDR = 0.0454). Its established functions include calcium-activated proteolysis, regulation of catalytic activity, autoprocessing and macroautophagy, while its HPA profile includes myometrial protein detection. Its substantial literature and disease annotation make it a well-characterized interpretive anchor rather than an unannotated hub.
- **Conclusion**: Established evidence supports CAPN1 as a partner of CAPN2 in a conserved calcium-regulated proteolytic unit. It is reasonable to hypothesize that this pair contributes to cytoskeletal or mechanical adaptation in both tissues, but the module does not establish their activation state or tissue-specific substrate.

#### CANX

- **Related proteins** (co-abundance neighbors): H6PD (0.90), EML1 (0.86), TARS1 (0.86), PDIA4 (0.84), GSN (0.80); STRING partners: MOGS (0.952), PDIA4 (0.931)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is a high-connectivity module gene linking H6PD, EML1, TARS1, PDIA4 and GSN. It is part of (GO:MF calcium ion binding; q_global = 0.0327) and both supplementary STRING terms (STRING Function Calcium ion binding; within-query FDR = 0.0454) and (STRING Function Carbohydrate binding; within-query FDR = 0.0454). Calnexin is an ER calcium-binding chaperone involved in folding and quality control of newly synthesized glycoproteins. Its strong STRING relationships with PDIA4 and MOGS define an established ER proteostasis neighborhood, and HPA detects the protein in myometrium. Its broad literature and disease associations further support its importance for interpreting a shared cellular state.
- **Conclusion**: Established evidence supports CANX as the module link between calcium handling and ER protein quality control. The hypothesis that CANX couples calcium availability to the metabolic and cytoskeletal portions of the module is plausible but not proven by the observed network.

#### H6PD

- **Related proteins** (co-abundance neighbors): MOGS (0.91), CANX (0.90), CAPN2 (0.90), TARS1 (0.89), ABCF1 (0.87), SEC23A (0.86), CTPS1 (0.83), GPS1 (0.80); STRING partners: GBE1 (0.712), PFKM (0.804)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hexose-6-phosphate dehydrogenase/glucose 1-dehydrogenase. There are 2 forms of glucose-6-phosphate dehydrogenase. G form is X-linked and H form, encoded by this gene, is autosomally linked. This H form shows activity with other hexose-6-phosphates, especially galactose-6-phosphate, whereas the G form is specific for glucose-6-phosphate. Both forms are present in most tissues, but H form is not found in red cells. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: cortisone reductase deficiency (0.735); Abnormality of the skeletal system (0.473); obesity disorder (0.364); stroke disorder (0.325); alcohol drinking (0.324)
- **Europe PMC papers**: 3634
- **Why important**: H6PD has high module connectivity, linking MOGS, CANX, CAPN2, TARS1, ABCF1, SEC23A, CTPS1 and GPS1. It connects to GBE1 and PFKM in STRING and contributes to the supplementary carbohydrate-binding term (STRING Function Carbohydrate binding; within-query FDR = 0.0454). Its established biology includes hexose-phosphate metabolism, the oxidative pentose-phosphate shunt, NADP-related metabolism and nutrient responses. HPA shows liver enhancement and expression in hepatocytes and myonuclei, while protein is detected in myometrium. Its substantial literature and disease associations make it a strong candidate for the metabolic component of the module.
- **Conclusion**: Established evidence supports H6PD as a metabolic and redox-related connector between ER-associated and carbohydrate-associated module neighborhoods. It may help supply reducing power or metabolic flexibility during calcium-linked remodeling, but that causal role is a hypothesis.

#### EML1

- **Related proteins** (co-abundance neighbors): TARS1 (0.96), STAT1 (0.87), SSH3 (0.87), SWAP70 (0.87), GARS1 (0.87), CTPS1 (0.86), REXO2 (0.86), CANX (0.86), GPS1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EMAP like 1. Human echinoderm microtubule-associated protein-like is a strong candidate for the Usher syndrome type 1A gene. Usher syndromes (USHs) are a group of genetic disorders consisting of congenital deafness, retinitis pigmentosa, and vestibular dysfunction of variable onset and severity depending on the genetic type. The disease process in USHs involves the entire brain and is not limited to the poster…
- **Diseases (Open Targets)**: subcortical band heterotopia (0.719); Abnormality of the skeletal system (0.460); atrial fibrillation (0.430); coronary artery disorder (0.368); angina pectoris (0.275)
- **Europe PMC papers**: 533
- **Why important**: EML1 has the greatest network connectivity and links translation-related genes, signaling and cytoskeletal genes, CTPS1, REXO2 and CANX. It contributes to the primary calcium-binding term (GO:MF calcium ion binding; q_global = 0.0327) and appears in supplementary STRING calcium enrichment (STRING Function Calcium ion binding; within-query FDR = 0.0454), although STRING does not provide a direct partner for it in this module. Its established annotations include microtubule cytoskeleton organization, mitotic spindle organization, neuroblast proliferation and brain development. It is not detected in immune cells by HPA and is detected in myometrium, which makes a blood-derived explanation less likely for this particular highly connected gene. Its literature volume is substantial, and its disease associations include Usher syndrome-related biology and neurodevelopmental phenotypes.
- **Conclusion**: Established evidence supports EML1 as a cytoskeletal and cell-state connector within the co-abundance network, with participation in the calcium-binding annotation. The hypothesis that EML1 coordinates microtubule organization with calcium-dependent proteolysis or ER function is suggestive but requires direct localization and perturbation experiments.

## Module 2

**Tissue pair**: myometrium and stem_cells  
**Genes (7)**: ACOT9, BAG2, BAG3, DPP9, ITGA5, LAMC1, PALM2AKAP2

### Function

The module is most consistent with a coordinated proteostasis and cell-adhesion program, with a possible interface between intracellular protein quality control and extracellular-matrix signaling. BAG2 and BAG3 provide the clearest functional anchor: both are Hsp70-associated cochaperones, and both occur in the supplementary STRING BAG-domain term (STRING SMART BAG domains, present in regulator of Hsp70 proteins; within-query FDR = 0.0295) and in several hu.MAP complexes (hu.MAP huMAP3_07919.1) through (hu.MAP huMAP3_14723.1). LAMC1 and ITGA5 define a second adhesion-related component, supported by their known STRING relationship and by the functions of laminin gamma one and integrin alpha five. DPP9, ACOT9, and PALM2AKAP2 may connect this core to proteolysis, lipid metabolism, and cell-shape regulation through the co-abundance network. No GO or KEGG term passed global correction, so the proposed function is an interpretation of gene functions and network structure rather than a globally significant pathway-enrichment result.

**Cell composition.** The module is mixed rather than predominantly secreted, plasma-protein, or housekeeping in character. LAMC1 is secreted to the extracellular matrix, whereas the other genes are not classified as secreted. Several genes show low tissue specificity, while others are enhanced in skeletal muscle, blood vessel, or placenta. Single-cell annotations repeatedly implicate smooth muscle cells, monocytes, neutrophils, decidual stromal cells, fibroblast-related populations, and other cell types. Three genes are immune-cell enhanced, one is not detected in immune cells, and the remainder have low immune-cell specificity. This pattern is compatible with a shared smooth-muscle or stromal component in myometrium and stem-cell samples, but it also leaves open a contribution from immune or vascular cells. HPA protein detection supports expression of most annotated proteins in myometrium, while no matching HPA tissue is available for the stem-cell group. The module therefore should not be interpreted as a uniformly myometrial intracellular program without considering shared cell types or sample composition.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports two high-confidence relationships within the module: BAG2 with BAG3, and ITGA5 with LAMC1. The BAG2-BAG3 relationship directly supports a chaperone-associated submodule, while the ITGA5-LAMC1 relationship supports an extracellular-matrix and adhesion submodule. The supplementary STRING domain result (STRING SMART BAG domains, present in regulator of Hsp70 proteins; within-query FDR = 0.0295) is consistent with the BAG2-BAG3 connection but is not global enrichment evidence. hu.MAP independently places BAG2 and BAG3 together in several complexes (hu.MAP huMAP3_07919.1) through (hu.MAP huMAP3_14723.1), each containing broader Hsp70, Hsp40, BAG-family, and protein-quality-control machinery. DPP9, ACOT9, and PALM2AKAP2 have no listed STRING partners or hu.MAP complexes, so their co-abundance links are not independently corroborated by those resources. Overall, the evidence supports a real BAG2-BAG3 proteostasis component and a real ITGA5-LAMC1 adhesion relationship, but not a single experimentally established multiprotein complex containing all module genes.

**STRING interactions (score >= 0.7)**: 2 of 21 gene pairs: BAG2–BAG3 (0.977); ITGA5–LAMC1 (0.865)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART BAG domains, present in regulator of Hsp70 proteins (FDR = 0.0295, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07919.1 (BAG2, BAG3; 2/27); huMAP3_11049.1 (BAG2, BAG3; 2/30); huMAP3_13774.1 (BAG2, BAG3; 2/33); huMAP3_14723.1 (BAG2, BAG3; 2/52)

### Novelty

This module may represent a novel tissue-pair co-abundance pattern, but the evidence does not establish a new molecular complex or a new biological pathway. The BAG2-BAG3 and ITGA5-LAMC1 relationships are already known through STRING, and BAG2-BAG3 recur in hu.MAP complexes. The apparent novelty lies instead in their coordinated abundance with DPP9, ACOT9, and PALM2AKAP2 across myometrium and stem-cell samples. The lack of STRING or hu.MAP support for those additional links is compatible with a context-specific regulatory or cellular-composition signal, but absence from reference databases alone cannot prove novelty. Because no GO or KEGG term passed global correction, there is no globally significant pathway result that independently establishes a new functional annotation.

**Hypothesis.** Hypothesis: the module reflects a shared smooth-muscle or stromal state in which extracellular-matrix adhesion through the LAMC1 and ITGA5 axis is coordinated with intracellular protein quality control through BAG2 and BAG3. DPP9 may connect this state to regulated proteolysis and inflammatory cell-death biology, while ACOT9 may reflect accompanying mitochondrial or fatty-acid metabolic activity and PALM2AKAP2 may relate to cell shape or membrane organization. An alternative explanation is that the module partly reflects shared vascular, stromal, or immune-cell admixture rather than a single pathway operating within one cell type. This hypothesis requires validation with cell-resolved data, perturbation experiments, and protein-level interaction or localization assays.

### Important genes

#### BAG3

- **Related proteins** (co-abundance neighbors): DPP9 (0.91); STRING partners: BAG2 (0.977)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_07919.1, huMAP3_11049.1, huMAP3_13774.1, huMAP3_14723.1
- **Function (MyGene.info)**: BAG cochaperone 3. BAG proteins compete with Hip for binding to the Hsc70/Hsp70 ATPase domain and promote substrate release. All the BAG proteins have an approximately 45-amino acid BAG domain near the C terminus but differ markedly in their N-terminal regions. The protein encoded by this gene contains a WW domain in the N-terminal region and a BAG domain in the C-terminal region. The BAG domains of BAG1, BAG2, and …
- **Diseases (Open Targets)**: dilated cardiomyopathy 1HH (0.821); myofibrillar myopathy 6 (0.789); dilated cardiomyopathy (0.726); familial isolated dilated cardiomyopathy (0.678); heart failure (0.654)
- **Europe PMC papers**: 4304
- **Why important**: BAG3 is a central functional marker of the proteostasis interpretation. It is tissue enhanced in skeletal muscle, cell-type enhanced in smooth muscle cells and monocytes, and immune-cell enhanced in a T-cell population. It forms the strongest listed STRING relationship with BAG2 and occurs with BAG2 in every reported hu.MAP complex (hu.MAP huMAP3_07919.1) through (hu.MAP huMAP3_14723.1). Its annotations include protein folding, autophagosome assembly, heat response, and protection of striated muscle cells from apoptosis. It also has extensive disease and literature associations, especially involving cardiomyopathy and myofibrillar muscle disease.
- **Conclusion**: Established evidence supports BAG3 as a chaperone-associated and muscle-relevant component of the module. Its co-abundance with DPP9 and its broader module context suggest, but do not establish, a connection between proteostasis and inflammatory or metabolic regulation.

#### BAG2

- **Related proteins** (co-abundance neighbors): LAMC1 (0.86), ACOT9 (0.80); STRING partners: BAG3 (0.977)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_07919.1, huMAP3_11049.1, huMAP3_13774.1, huMAP3_14723.1
- **Function (MyGene.info)**: BAG cochaperone 2. BAG proteins compete with Hip for binding to the Hsc70/Hsp70 ATPase domain and promote substrate release. All the BAG proteins have an approximately 45-amino acid BAG domain near the C terminus but differ markedly in their N-terminal regions. The predicted BAG2 protein contains 211 amino acids. The BAG domains of BAG1, BAG2, and BAG3 interact specifically with the Hsc70 ATPase domain in vitro and …
- **Diseases (Open Targets)**: dengue disease (0.370); neurodegenerative disease (0.335); RAB23-related Carpenter syndrome (0.190); neoplasm (0.112); gastric cancer (0.098)
- **Europe PMC papers**: 1122
- **Why important**: BAG2 is a direct partner of BAG3 in STRING and is present with BAG3 in all reported hu.MAP complexes (hu.MAP huMAP3_07919.1) through (hu.MAP huMAP3_14723.1). Its annotated functions include protein folding, protein stabilization, protein processing, and proteasome-linked protein catabolism. It is detected in myometrium and is cell-type enhanced in several reproductive and stromal-related populations. Its literature and disease associations are substantial enough to make it a stronger mechanistic anchor than the less characterized module members.
- **Conclusion**: Established evidence supports BAG2 as the second component of a chaperone and protein-quality-control submodule. Its links to LAMC1 and ACOT9 in the co-abundance graph are hypotheses about shared regulation or cell state, not established physical interactions.

#### LAMC1

- **Related proteins** (co-abundance neighbors): BAG2 (0.86), ITGA5 (0.82); STRING partners: ITGA5 (0.865)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Plasma membrane; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit gamma 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: Fuchs' endothelial dystrophy (0.487); prostate carcinoma (0.467); colorectal cancer (0.447); eye disorder (0.434); benign colon neoplasm (0.427)
- **Europe PMC papers**: 4227
- **Why important**: LAMC1 provides the main extracellular-matrix component. Laminin gamma one is a structural basement-membrane glycoprotein involved in adhesion, migration, tissue development, and signaling. It is secreted to the extracellular matrix, tissue enhanced in placenta, detected in myometrium, and expressed in fibroblast-related and stromal cell types. Its STRING relationship with ITGA5 supplies independent support for an adhesion-related submodule. It also has a large literature base and broad disease associations.
- **Conclusion**: Established evidence supports LAMC1 as an extracellular-matrix and adhesion component of the module. Its co-abundance with BAG2 is not supported by a listed STRING or hu.MAP interaction and should be treated as a tissue-state association rather than a direct molecular interaction.

#### ITGA5

- **Related proteins** (co-abundance neighbors): LAMC1 (0.82); STRING partners: LAMC1 (0.865)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha 5. The product of this gene belongs to the integrin alpha chain family. Integrins are heterodimeric integral membrane proteins composed of an alpha subunit and a beta subunit that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha 5 subunit. This subunit associates with the beta 1 subunit t…
- **Diseases (Open Targets)**: skin disorder (0.223); body weight gain (0.174); non-small cell lung carcinoma (0.116); neoplasm (0.115); hepatocellular carcinoma (0.108)
- **Europe PMC papers**: 6985
- **Why important**: ITGA5 is the membrane adhesion counterpart to LAMC1 in the observed network. It forms a fibronectin receptor with integrin beta one and is annotated for cell adhesion, cell-matrix adhesion, integrin signaling, angiogenesis, and pregnancy-related biology. It is tissue enhanced in blood vessel, cell-type enhanced in stromal, endothelial, trophoblast, and monocyte populations, and immune-cell enhanced in neutrophils. Its STRING relationship with LAMC1 is one of the two independently supported module relationships.
- **Conclusion**: Established evidence supports ITGA5 as an adhesion and vascular or stromal marker that may explain part of the shared tissue signal. The link from ITGA5 to the BAG proteins is a co-abundance pattern and not evidence of a direct physical complex.

#### DPP9

- **Related proteins** (co-abundance neighbors): BAG3 (0.91), ACOT9 (0.88), PALM2AKAP2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dipeptidyl peptidase 9. This gene encodes a protein that is a member of the S9B family in clan SC of the serine proteases. The protein has been shown to have post-proline dipeptidyl aminopeptidase activity, cleaving Xaa-Pro dipeptides from the N-termini of proteins. Although the activity of this protein is similar to that of dipeptidyl peptidase 4 (DPP4), it does not appear to be membrane bound. In general, dipeptidyl pe…
- **Diseases (Open Targets)**: hatipoglu immunodeficiency syndrome (0.624); COVID-19 (0.556); idiopathic pulmonary fibrosis (0.436); neurodegenerative disease (0.397); respiratory failure (0.351)
- **Europe PMC papers**: 1869
- **Why important**: DPP9 has the highest weighted connectivity in the module and links BAG3, ACOT9, and PALM2AKAP2 in the co-abundance graph. It is a cytosolic post-proline dipeptidyl aminopeptidase with annotations involving proteolysis, negative regulation of programmed cell death, and pyroptotic inflammatory response. It has low tissue specificity, is cell-type enhanced in alveolar cells, and has broad disease associations and extensive literature coverage. Despite its network position, it has no listed STRING partners, no hu.MAP complex, and no enrichment-term assignment in this module.
- **Conclusion**: Established evidence supports DPP9 as a cytosolic protease with links to cell-death and inflammatory biology, and the network identifies it as a potentially important connector. Whether it functionally couples the BAG-associated proteostasis signal to the metabolic or membrane-associated genes remains a hypothesis requiring experimental testing.

## Module 3

**Tissue pair**: myometrium and stem_cells  
**Genes (7)**: ACSL3, EHD2, EZR, ILK, PARVA, TGFB1I1, TF

### Function

The module is most consistent with an integrin-linked focal-adhesion and actin-cytoskeleton program, with possible coupling to cell adhesion, membrane organization, lipid handling, and iron transport. The strongest evidence is the coherent ILK–PARVA–TGFB1I1 focal-adhesion connection in the network and the annotated functions of ILK, PARVA, TGFB1I1, EHD2, and EZR. ILK and PARVA are associated with integrin signaling, actin organization, cell adhesion, polarity, motility, and survival; TGFB1I1 is associated with adhesion and transforming-growth-factor receptor signaling; EHD2 links the plasma membrane and actin cytoskeleton through endocytic processes; and EZR links the plasma membrane to actin. ACSL3 contributes a potentially distinct lipid-metabolic component, while TF contributes iron transport and cell-surface signaling. No GO or KEGG term passed global correction, so these annotations support biological interpretation but do not establish significant pathway enrichment. The absence of a globally significant term does not invalidate the module.

**Cell composition.** This does not look like a plasma-protein-dominated or broadly secreted module. TF is the sole secreted-to-blood gene and is strongly associated with liver and retina, so its presence could reflect circulating protein or sample-composition effects rather than a myometrial intracellular program. The remaining genes are non-secreted proteins with membrane, focal-adhesion, cytoskeletal, or metabolic annotations. HPA supports a shared stromal or contractile-cell interpretation: smooth-muscle enrichment is observed for ILK and PARVA, and related stromal, pericyte, myoid, or hepatic-stellate cell patterns occur across several genes. Most genes have low tissue specificity or cell-type-enhanced patterns rather than a uniform tissue-specific signature. Immune-cell specificity is generally low or absent, although isolated immune-cell enhancement occurs for TGFB1I1, PARVA, and another module member. Myometrial protein detection is present for most assessed genes, whereas there is no matching HPA tissue for stem cells. Thus, contamination by blood cells is not the leading explanation, but TF and the heterogeneous cell-type patterns warrant caution about shared cell composition and circulating-protein effects.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a particularly strong ILK–PARVA relationship and additional ILK–TGFB1I1 and PARVA–TGFB1I1 relationships. These links independently reinforce a focal-adhesion and integrin-associated core, but STRING reports no supplementary functional-enrichment terms for the module. hu.MAP identifies two complexes containing ILK and PARVA together. The overlapping partners include LIMS proteins, PXN, PARVG, PARVB, and RSU1, with one complex also containing additional proteins linked to the reported assembly. These complexes indicate that ILK and PARVA are already recognized components of larger adhesion-associated assemblies. The other module genes are not represented in the reported hu.MAP complexes, so the full module is not an established single protein complex. The network therefore combines a known ILK–PARVA adhesion core with less-established co-abundance links involving membrane, metabolic, and secreted proteins.

**STRING interactions (score >= 0.7)**: 3 of 21 gene pairs: ILK–PARVA (0.999); ILK–TGFB1I1 (0.745); PARVA–TGFB1I1 (0.724)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09385.1 (ILK, PARVA; 2/8); huMAP3_11194.1 (ILK, PARVA; 2/10)

### Novelty

The focal-adhesion core is not a new molecular concept: ILK, PARVA, and TGFB1I1 have known functional relationships, and ILK–PARVA occurs in hu.MAP complexes. The possible novelty lies instead in the tissue-pair co-abundance pattern, particularly the association of this adhesion core with ACSL3, TF, EHD2, and EZR across myometrium and stem cells. This cannot be called a newly discovered pathway because there is no globally significant GO or KEGG enrichment, no STRING functional enrichment, and only part of the module is represented in known complexes. Absence from STRING or hu.MAP would not by itself prove novelty. The most defensible conclusion is that this is a potentially informative tissue-shared co-abundance module built around a known adhesion scaffold, with a novel or context-dependent peripheral composition that requires independent validation.

**Hypothesis.** Hypothesis: the shared module reflects a contractile or stromal-cell state in which integrin-linked focal adhesions coordinate actin organization, membrane trafficking, and extracellular-matrix interaction, while TGFB1I1 may connect adhesion to transforming-growth-factor signaling. EHD2 and EZR could support membrane–actin remodeling and trafficking, ACSL3 could supply a lipid-metabolic or membrane-composition component, and TF could represent either iron-related support for proliferating cells or a circulating-protein contribution from sample composition. In this model, the ILK–PARVA–TGFB1I1 core is the mechanistic center, while the remaining genes are context-dependent associates rather than proven members of one biochemical complex. This hypothesis should be tested by cell-type-resolved expression, protein-level co-localization, and perturbation of the ILK–PARVA axis in myometrial and stem-cell-derived relevant populations.

### Important genes

#### ILK

- **Related proteins** (co-abundance neighbors): TGFB1I1 (0.92), EHD2 (0.87), PARVA (0.85); STRING partners: PARVA (0.999), TGFB1I1 (0.745)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: integrin linked kinase. This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastas…
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); familial hypertrophic cardiomyopathy (0.194); Abnormality of the cardiovascular system (0.148); Prolonged QT interval (0.118); neoplasm (0.118)
- **Europe PMC papers**: 8401
- **Why important**: ILK is the most connected gene in the module and links TGFB1I1, EHD2, and PARVA. It is localized to focal-adhesion sites, is detected in myometrium, and is annotated for integrin-mediated signaling, cell–matrix adhesion, morphogenesis, and mitotic-spindle organization. Its very large literature base and disease associations make it the strongest established anchor for interpreting the module.
- **Conclusion**: Established evidence supports ILK as the central integrin-linked adhesion scaffold. It is plausible, but not proven here, that ILK coordinates the module's adhesion, cytoskeletal, and membrane-remodeling signals.

#### PARVA

- **Related proteins** (co-abundance neighbors): ILK (0.85); STRING partners: ILK (0.999), TGFB1I1 (0.724)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Actin filaments, Focal adhesion sites; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: parvin alpha. This gene encodes a member of the parvin family of actin-binding proteins. Parvins are associated with focal contacts and contain calponin homology domains that bind to actin filaments. The encoded protein is part of the integrin-linked kinase signaling complex and plays a role in cell adhesion, motility and survival. [provided by RefSeq, Dec 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.487); osteoarthritis, hip (0.339); total hip arthroplasty (0.339); open-angle glaucoma (0.337); Pancreatic pseudocyst (0.331)
- **Europe PMC papers**: 3949
- **Why important**: PARVA is a focal-adhesion and actin-filament protein, is cell-type enhanced in smooth muscle cells, and is part of both reported hu.MAP complexes with ILK. Its STRING relationship with ILK is especially strong, and its annotations include cell adhesion, polarity, actin organization, angiogenesis, motility, and survival. It therefore provides a direct structural bridge between the network and a contractile-cell interpretation.
- **Conclusion**: Established evidence supports PARVA as a bona fide component of the ILK-centered adhesion machinery. Its shared co-abundance with the other genes may indicate coordinated cytoskeletal state, but the module does not establish a direct biochemical interaction for every member.

#### TGFB1I1

- **Related proteins** (co-abundance neighbors): ILK (0.92), TF (0.81); STRING partners: ILK (0.745), PARVA (0.724)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Focal adhesion sites; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transforming growth factor beta 1 induced transcript 1. This gene encodes a coactivator of the androgen receptor, a transcription factor which is activated by androgen and has a key role in male sexual differentiation. The encoded protein is thought to regulate androgen receptor activity and may have a role to play in the treatment of prostate cancer. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by R…
- **Diseases (Open Targets)**: neurodegenerative disease (0.318); Glycosuria (0.226); mucous membrane pemphigoid (0.074); triple-A syndrome (0.074); esophageal squamous cell carcinoma (0.058)
- **Europe PMC papers**: 874
- **Why important**: TGFB1I1 is connected to both ILK and PARVA, is localized to focal-adhesion sites, and is detected in myometrium. Its annotations include cell adhesion, transforming-growth-factor receptor signaling, epithelial-to-mesenchymal transition, and regulation of proliferation. Its stromal and myoepithelial cell-type associations make it a plausible signaling interface between adhesion and cell-state regulation.
- **Conclusion**: Established evidence supports TGFB1I1 as an adhesion-associated signaling regulator linked to the ILK–PARVA core. Its role as the pathway-level driver of the shared module remains a hypothesis rather than a demonstrated causal conclusion.

#### EHD2

- **Related proteins** (co-abundance neighbors): ILK (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EH domain containing 2. This gene encodes a member of the EH domain-containing protein family. These proteins are characterized by a C-terminal EF-hand domain, a nucleotide-binding consensus site at the N terminus and a bipartite nuclear localization signal. The encoded protein interacts with the actin cytoskeleton through an N-terminal domain and also binds to an EH domain-binding protein through the C-terminal EH domai…
- **Diseases (Open Targets)**: disorder of patella (0.201); neuromuscular disease (0.201); muscular disease (0.201); triple-negative breast carcinoma (0.095); breast cancer (0.094)
- **Europe PMC papers**: 1131
- **Why important**: EHD2 connects to ILK in the module and is localized to the plasma membrane. Its annotations support endocytosis, endocytic recycling, plasma-membrane tubulation, membrane localization, and interaction with the actin cytoskeleton. Its enhancement in stromal and fibroblast-like cell types gives it a plausible role in coupling focal adhesions to membrane dynamics, despite its peripheral network position.
- **Conclusion**: Established evidence supports EHD2 as a membrane–actin trafficking protein. Its co-abundance with ILK may reflect coordinated adhesion and membrane remodeling, but a direct functional connection in this tissue pair has not been established.

#### ACSL3

- **Related proteins** (co-abundance neighbors): TF (0.90), EZR (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 3. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme is highly expressed…
- **Diseases (Open Targets)**: prostate adenocarcinoma (0.370); acute myeloid leukemia (0.313); neurodegenerative disease (0.300); ovarian dysfunction (0.253); Abnormality of the skeletal system (0.215)
- **Europe PMC papers**: 2930
- **Why important**: ACSL3 occupies an intermediate position between TF and EZR and encodes a long-chain fatty-acyl-CoA synthetase involved in fatty-acid metabolism, lipid biosynthesis, fatty-acid degradation, and very-low-density-lipoprotein assembly. It is detected in myometrium and has cell-type enhancement in neutrophils and prostatic glandular cells. Its presence broadens the module beyond adhesion and raises the possibility of a membrane-lipid or metabolic context.
- **Conclusion**: Established evidence supports ACSL3 as a lipid-metabolic enzyme, not as a known member of the ILK–PARVA adhesion complex. Its module membership may reflect metabolic support for membrane remodeling or may arise from tissue-composition effects; this distinction requires validation.

#### TF

- **Related proteins** (co-abundance neighbors): ACSL3 (0.90), TGFB1I1 (0.81); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transferrin. This gene encodes a glycoprotein with an approximate molecular weight of 76.5 kDa. It is thought to have been created as a result of an ancient gene duplication event that led to generation of homologous C and N-terminal domains each of which binds one ion of ferric iron. The function of this protein is to transport iron from the intestine, reticuloendothelial system, and liver parenchymal cells t…
- **Diseases (Open Targets)**: atransferrinemia (0.776); alcohol drinking (0.492); hemochromatosis type 1 (0.471); neurodegenerative disease (0.400); urolithiasis (0.329)
- **Europe PMC papers**: 143656
- **Why important**: TF is connected to ACSL3 and TGFB1I1 and encodes the major iron-transport glycoprotein transferrin, with roles in iron transport, intracellular iron homeostasis, and cell-surface receptor signaling. It has very extensive literature and strong liver-associated expression, is secreted to blood, and is not detected in myometrial tissue by HPA. These features make it important both biologically and as a potential sample-composition indicator.
- **Conclusion**: Established evidence supports TF as a circulating iron-transport protein rather than a demonstrated focal-adhesion component. Its co-abundance may reflect iron demand or shared biological state, but blood or extracellular carryover is an important alternative explanation.

## Module 4

**Tissue pair**: myometrium and stem_cells  
**Genes (8)**: ALB, DPYSL2, FDPS, LDHB, PLS3, ATIC, TPM1, WDR1

### Function

The module does not have a confidently assigned pathway function from enrichment: no GO or KEGG term passed global multiple-testing correction, and no STRING functional-enrichment result was available. Its network is instead suggestive of a mixed cytoskeletal, contractile, and metabolic program. DPYSL2 is the central co-abundance connector, linking the actin-associated genes WDR1 and PLS3 with LDHB and the purine-biosynthesis enzyme ATIC. TPM1 contributes a smooth-muscle and actin-filament interpretation, while LDHB, ATIC, and FDPS represent cellular energy, purine, and sterol-related metabolism. These annotations support biological plausibility but do not establish one unified pathway. The sparse network and lack of STRING-supported physical interactions favor interpreting this as a co-abundance signature rather than a demonstrated molecular complex.

**Cell composition.** The module is compositionally mixed rather than a clean tissue-specific pathway. ALB is a liver-enriched, hepatocyte-enriched protein secreted to blood and is the most conspicuous indicator of possible plasma contamination or blood-derived signal. Several other genes have blood-cell or vascular, epithelial, platelet, or megakaryocyte associations in HPA. DPYSL2 shows enrichment in several myeloid-cell categories, PLS3 in NK-cell and plasmacytoid dendritic-cell groups, TPM1 and WDR1 in megakaryocyte or platelet-related contexts, and the module includes vascular smooth-muscle-associated signals. At the same time, TPM1, LDHB, ATIC, WDR1, PLS3, and DPYSL2 were detected in myometrium by HPA, whereas ALB and FDPS were not detected there; stem_cells have no matching HPA tissue measurement. Thus, the shared signal may reflect a combination of smooth-muscle or stromal cellular content, broadly distributed cytoskeletal and metabolic expression, and variable blood or plasma contribution. The module should not be interpreted as evidence that all of its genes are produced by one myometrial or stem-cell population.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and no STRING functional-enrichment result was reported. Therefore, STRING provides no established protein-protein interaction support for the co-abundance edges. hu.MAP provides one relevant partial complex observation: (hu.MAP huMAP3_14442.1) contains PLS3 and ATIC among its members. Because only these module members overlap that large complex, (hu.MAP huMAP3_14442.1) supports a possible connection between PLS3 and ATIC at the complex-membership level but does not validate the entire module or imply that all co-abundance relationships are physical interactions. The remaining genes had no reported hu.MAP complex with multiple module members. Overall, the network is better viewed as an expression-covariation structure with limited external molecular-complex support.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (PLS3, ATIC; 2/57)

### Novelty

The module may be a new co-abundance observation, but the supplied evidence is insufficient to call it a newly discovered biological complex or pathway. Its lack of high-confidence STRING interactions and the limited hu.MAP overlap make a previously catalogued compact interaction module less likely. However, absence from STRING or hu.MAP does not prove novelty, because co-abundance can arise from shared cell composition, regulation, tissue mixtures, or indirect physiology. The presence of well-studied genes such as ALB, LDHB, TPM1, ATIC, and FDPS also argues against claiming that the individual biology is novel. A defensible conclusion is that the particular conserved co-abundance combination across myometrium and stem_cells is a candidate novel signature requiring independent replication, cell-resolved analysis, and experimental validation.

**Hypothesis.** Hypothesis: the conserved signal reflects coordinated variation in cytoskeletal and contractile state together with cellular metabolic demand, rather than a single physical complex. DPYSL2 may mark the shared cytoskeletal or microtubule-associated state, WDR1 and PLS3 may report actin remodeling, and TPM1 may report smooth-muscle or contractile architecture. LDHB, ATIC, and FDPS could vary with energetic, purine, and sterol requirements of the same cellular populations. ALB may represent blood or plasma carryover rather than a core intracellular component. A testable model is that the module becomes prominent when samples contain related vascular, smooth-muscle, stromal, platelet-associated, or contaminating blood components, with metabolic genes tracking the state of those cells. This hypothesis should be tested using cell-type deconvolution, plasma-contamination markers, single-cell or spatial data, and independent cohorts.

### Important genes

#### DPYSL2

- **Related proteins** (co-abundance neighbors): LDHB (0.85), ATIC (0.83), WDR1 (0.83), PLS3 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Microtubules, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dihydropyrimidinase like 2. This gene encodes a member of the collapsin response mediator protein family. Collapsin response mediator proteins form homo- and hetero-tetramers and facilitate neuron guidance, growth and polarity. The encoded protein promotes microtubule assembly and is required for Sema3A-mediated growth cone collapse, and also plays a role in synaptic signaling through interactions with calcium channels. This…
- **Diseases (Open Targets)**: hypertensive disorder (0.431); autosomal dominant non-syndromic intellectual disability (0.370); cardiovascular disorder (0.297); ovarian neoplasm (0.292); glomerulonephritis (0.269)
- **Europe PMC papers**: 1328
- **Why important**: DPYSL2 has the strongest network connectivity in the module and links the cytoskeletal genes WDR1 and PLS3 to LDHB and ATIC. Its established functions include collapsin-response-mediator activity, microtubule assembly, neuronal guidance, and cytoskeletal organization. HPA places it in brain-related and several myeloid-cell contexts, while its protein was not detected in myometrium. Its broad disease literature and substantial publication record make it an informative but potentially heterogeneous hub.
- **Conclusion**: Established evidence supports DPYSL2 as the principal co-abundance connector and a cytoskeletal or microtubule-associated marker. The module does not establish that DPYSL2 drives the other genes, and its brain and myeloid associations make cell-composition effects plausible. Its role as a mechanistic hub in this tissue pair remains a hypothesis.

#### TPM1

- **Related proteins** (co-abundance neighbors): LDHB (0.89), ALB (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tropomyosin 1. This gene is a member of the tropomyosin family of highly conserved, widely distributed actin-binding proteins involved in the contractile system of striated and smooth muscles and the cytoskeleton of non-muscle cells. Tropomyosin is composed of two alpha-helical chains arranged as a coiled-coil. It is polymerized end to end along the two grooves of actin filaments and provides stability to the fi…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy (0.798); left ventricular noncompaction (0.760); left ventricular noncompaction 9 (0.664); familial isolated dilated cardiomyopathy (0.639); hypertrophic cardiomyopathy 3 (0.596)
- **Europe PMC papers**: 6278
- **Why important**: TPM1 connects LDHB and ALB and provides the clearest smooth-muscle and contractile interpretation. It is an actin-binding tropomyosin expressed in contractile and non-muscle cytoskeletal systems, is tissue-enhanced in heart and skeletal muscle, and was detected in myometrium. It also has strong established disease associations involving cardiomyopathy, giving it substantial biological and literature support.
- **Conclusion**: Established evidence supports TPM1 as a marker of actin-filament organization and contractile-cell content, consistent with a myometrial component. It is reasonable to hypothesize that TPM1 captures smooth-muscle or related stromal state in the shared module, but the co-abundance data do not demonstrate altered contraction or a direct TPM1 interaction with the other module genes.

#### ALB

- **Related proteins** (co-abundance neighbors): LDHB (0.87), TPM1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB is directly connected to LDHB and TPM1 in the co-abundance network and is biologically distinctive because it is liver-enriched, hepatocyte-enriched, and secreted to blood. It is the most abundant protein in human blood and has extensive literature and disease annotation. It was not detected in myometrium, making it especially important for interpreting sample composition.
- **Conclusion**: Established evidence supports ALB as a plasma or blood-associated signal rather than a likely intracellular core of the myometrial module. Its presence may indicate blood carryover, vascular content, or sample handling effects. A direct functional role for ALB in the conserved intracellular program is not supported by the supplied evidence and should be treated as a hypothesis only.

#### ATIC

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.83), FDPS (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: 5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase. This gene encodes a bifunctional protein that catalyzes the last two steps of the de novo purine biosynthetic pathway. The N-terminal domain has phosphoribosylaminoimidazolecarboxamide formyltransferase activity, and the C-terminal domain has IMP cyclohydrolase activity. A mutation in this gene results in AICA-ribosiduria. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: AICA-ribosiduria (0.708); cancer (0.571); Intellectual disability (0.463); lung adenocarcinoma (0.390); anaplastic large cell lymphoma (0.374)
- **Europe PMC papers**: 5200
- **Why important**: ATIC connects DPYSL2 with FDPS and is one of the two module genes represented in the hu.MAP complex (hu.MAP huMAP3_14442.1). It is a bifunctional enzyme catalyzing the final steps of de novo purine biosynthesis and is detected in myometrium. Its established links to purine metabolism, AICA-ribosiduria, cancer, and intellectual disability give it both functional and disease relevance.
- **Conclusion**: Established evidence supports ATIC as a metabolic component and as a partial bridge to the hu.MAP observation (hu.MAP huMAP3_14442.1). The module may reflect biosynthetic demand coupled to cytoskeletal state, but no enrichment or physical-interaction evidence demonstrates that ATIC forms a functional complex with DPYSL2 or FDPS in these samples.

#### WDR1

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions, Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 1. This gene encodes a protein containing 9 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, mostly including a trp-asp at the C-terminal end. WD domains are involved in protein-protein interactions. The encoded protein may help induce the disassembly of actin filaments. Two transcript variants encoding different isoforms have been found for…
- **Diseases (Open Targets)**: periodic fever, immunodeficiency, and thrombocytopenia syndrome (0.705); gout (0.528); neurodegenerative disease (0.526); atrial fibrillation (0.519); intellectual developmental disorder 61 (0.416)
- **Europe PMC papers**: 1861
- **Why important**: WDR1 is connected to the central DPYSL2 node and has an established role in actin-filament depolymerization and cortical cytoskeleton organization. HPA also associates it with platelet formation and megakaryocyte or platelet-related cell types, while its protein was detected in myometrium. Its disease associations include immunodeficiency and thrombocytopenia-related conditions.
- **Conclusion**: Established evidence supports WDR1 as an actin-remodeling marker that could contribute to the cytoskeletal interpretation of the module. Its platelet and blood-cell associations provide an alternative composition-based explanation for its co-abundance. A specific WDR1-dependent mechanism linking the module across myometrium and stem_cells remains unproven.

#### PLS3

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: plastin 3. Plastins are a family of actin-binding proteins that are conserved throughout eukaryote evolution and expressed in most tissues of higher eukaryotes. In humans, two ubiquitous plastin isoforms (L and T) have been identified. Plastin 1 (otherwise known as Fimbrin) is a third distinct plastin isoform which is specifically expressed at high levels in the small intestine. The L isoform is expressed on…
- **Diseases (Open Targets)**: X-linked osteoporosis with fractures (0.727); congenital diaphragmatic hernia (0.553); osteoporosis (0.477); hernia, anterior diaphragmatic (0.380); postmenopausal osteoporosis (0.341)
- **Europe PMC papers**: 1365
- **Why important**: PLS3 is an actin-bundling protein connected to DPYSL2 and is the second module member in hu.MAP complex (hu.MAP huMAP3_14442.1) with ATIC. HPA places it in vascular and multiple epithelial contexts and reports group enrichment in NK-cell and plasmacytoid dendritic-cell categories; its protein was detected in myometrium. It therefore connects the cytoskeletal interpretation with possible vascular or immune-cell composition.
- **Conclusion**: Established evidence supports PLS3 as an actin-network and cell-structure component, with partial complex-level support through (hu.MAP huMAP3_14442.1). Its broad cell-type distribution means that the module may reflect shared structural or compositional features rather than a dedicated stem-cell or myometrial mechanism. Its proposed role as a bridge between cytoskeletal state and purine metabolism is a hypothesis.

## Module 5

**Tissue pair**: myometrium and stem_cells  
**Genes (12)**: BLVRA, BLVRB, CBR1, CPNE3, CZIB, QDPR, GNA13, HEBP2, PDXK, PGM1, RAB21, SCRN1

### Function

The module does not have a statistically supported GO or KEGG functional enrichment: no globally significant GO/KEGG term passed global correction. STRING functional enrichment is also absent. Its network nevertheless suggests a loose cytosolic metabolic and redox-associated program rather than a single established pathway. PDXK and PGM1 support intermediary carbohydrate and vitamin B6 metabolism; QDPR supports tetrahydrobiopterin and amino-acid-related metabolism; BLVRA and BLVRB support heme catabolism; and CBR1 supports reduction of carbonyl compounds and prostanoid-related metabolism. HEBP2 is the central co-abundance hub and connects several of these genes, but its annotation concerns mitochondrial membrane permeabilization rather than a defined pathway shared by the module. CPNE3, RAB21, SCRN1, and GNA13 add possible calcium-responsive membrane regulation, vesicle or receptor trafficking, exocytosis, adhesion, migration, and Rho-linked signaling. Overall, the evidence supports coordinated expression of broadly cytosolic metabolic, stress-response, and trafficking-related genes, while the absence of global enrichment means that this interpretation remains integrative rather than pathway-proven.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not broadly blood-cell enriched, because most genes have low immune-cell specificity. However, composition or shared-cell effects cannot be excluded. BLVRB is immune-cell enhanced for classical monocytes and is also associated with erythroid cell types, while GNA13 is enhanced in bone marrow and several myeloid cell types. Other genes show enhancement in hepatocytes, esophageal cells, spermatogenic cells, neural or glial cells, and stromal or trophoblast-related cells. This heterogeneous HPA pattern, together with several genes having low tissue specificity, is more consistent with a broadly expressed or mixed-cellular program than with a myometrium-specific mechanism. Protein detection in myometrium supports biological presence for most of the tested genes, whereas there is no matching HPA tissue assessment for stem cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only reported high-confidence STRING relationship is the BLVRA–BLVRB pair. This is biologically coherent because both enzymes participate in heme catabolism, and it provides the strongest known physical or functional connection within the module. No other module genes have reported STRING partners in the supplied evidence, and there is no STRING functional enrichment. The only hu.MAP complex containing multiple module members is (hu.MAP huMAP3_14442.1), in which BLVRB and SCRN1 occur within a much larger complex. Thus, (hu.MAP huMAP3_14442.1) provides limited complex-level support but does not establish that the whole module is one physical complex. Most module edges are therefore co-abundance relationships without corroborating known protein-interaction or complex evidence.

**STRING interactions (score >= 0.7)**: 1 of 66 gene pairs: BLVRA–BLVRB (0.993)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (BLVRB, SCRN1; 2/57)

### Novelty

The co-abundance pattern may be a new observation, but the fact sheet does not establish a new molecular mechanism. The module combines several established biochemical functions, including vitamin B6 salvage, carbohydrate metabolism, tetrahydrobiopterin metabolism, carbonyl reduction, heme catabolism, vesicle regulation, and G-protein signaling. The BLVRA–BLVRB relationship and the (hu.MAP huMAP3_14442.1) hu.MAP association are already known, so the module is not wholly novel at the interaction level. Conversely, the sparse STRING and hu.MAP support means that the specific cross-tissue co-abundance organization could be novel. That possibility should be described as a hypothesis requiring replication in independent cohorts, control for cell composition, and experimental validation rather than as a demonstrated new finding.

**Hypothesis.** Hypothesis: the conserved module reflects a shared cytosolic metabolic and stress-adaptation state present in cells contributing to both myometrium and stem-cell samples. HEBP2 may mark the co-abundance core, while PDXK, PGM1, QDPR, CBR1, BLVRA, and BLVRB provide complementary metabolic and redox functions. RAB21, CPNE3, SCRN1, and GNA13 could connect this state to membrane trafficking, exocytosis, adhesion, migration, or receptor-linked signaling. The heme-catabolic BLVRA–BLVRB pair may represent a particularly coherent submodule, but the full mechanism is uncertain because global enrichment is absent, known interaction support is sparse, and HPA profiles suggest heterogeneous cellular sources.

### Important genes

#### HEBP2

- **Related proteins** (co-abundance neighbors): CPNE3 (0.95), CZIB (0.93), RAB21 (0.93), PDXK (0.89), QDPR (0.85), GNA13 (0.84), BLVRB (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heme binding protein 2. The protein encoded by this gene is found predominately in the cytoplasm, where it plays a role in the collapse of mitochondrial membrane potential (MMP) prior to necrotic cell death. The encoded protein enhances outer and inner mitochondrial membrane permeabilization, especially under conditions of oxidative stress. [provided by RefSeq, May 2016].
- **Diseases (Open Targets)**: metabolic disease (0.311); neurodegenerative disease (0.265); Familial prostate cancer (0.111); prostate cancer (0.111); enteritis (0.084)
- **Europe PMC papers**: 290
- **Why important**: HEBP2 is the principal network hub, linking the largest portion of the module to CPNE3, CZIB, RAB21, PDXK, QDPR, GNA13, and BLVRB. Its established annotation places it in cytoplasmic control of mitochondrial membrane permeabilization during oxidative stress. It therefore provides a plausible organizing marker for a stress-associated co-abundance state, although it has no reported STRING or hu.MAP support in this module and its disease associations are comparatively indirect.
- **Conclusion**: Established evidence supports HEBP2 as the central network gene and as a protein associated with mitochondrial membrane-permeabilization responses. It is a strong candidate module marker, but its role as a causal regulator of the shared tissue program is only a hypothesis.

#### PDXK

- **Related proteins** (co-abundance neighbors): CPNE3 (0.89), PGM1 (0.89), HEBP2 (0.89), BLVRA (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyridoxal kinase. The protein encoded by this gene phosphorylates vitamin B6, a step required for the conversion of vitamin B6 to pyridoxal-5-phosphate, an important cofactor in intermediary metabolism. The encoded protein is cytoplasmic and probably acts as a homodimer. Alternatively spliced transcript variants have been described, but their biological validity has not been determined. [provided by RefSeq, Jul 200…
- **Diseases (Open Targets)**: neuropathy, hereditary motor and sensory, type VIc, with optic atrophy (0.581); neurodegenerative disease (0.429); autoimmune disorder of central nervous system (0.370); hypertensive disorder (0.188); ovarian neoplasm (0.169)
- **Europe PMC papers**: 859
- **Why important**: PDXK connects the HEBP2-centered portion of the network with CPNE3, PGM1, and BLVRA. Its established function in pyridoxal phosphate production gives the module a defined intermediary-metabolism component. HPA shows tissue enhancement in brain and cell-type enhancement in spermatogenic populations, while its disease associations include hereditary neuropathy and neurodegenerative disease. It also has a substantial literature base relative to several less characterized module genes.
- **Conclusion**: Established evidence supports PDXK as a vitamin B6 salvage enzyme and a biologically meaningful metabolic component of the module. Whether its co-abundance reflects altered cofactor metabolism in myometrium and stem cells, rather than shared cellular composition, remains unresolved.

#### PGM1

- **Related proteins** (co-abundance neighbors): PDXK (0.89), CPNE3 (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglucomutase 1. The protein encoded by this gene is an isozyme of phosphoglucomutase (PGM) and belongs to the phosphohexose mutase family. There are several PGM isozymes, which are encoded by different genes and catalyze the transfer of phosphate between the 1 and 6 positions of glucose. In most cell types, this PGM isozyme is predominant, representing about 90% of total PGM activity. In red cells, PGM2 is a majo…
- **Diseases (Open Targets)**: PGM1-congenital disorder of glycosylation (0.843); MPDU1-congenital disorder of glycosylation (0.551); developmental and epileptic encephalopathy, 36 (0.551); RFT1-congenital disorder of glycosylation (0.551); disorder of glycogen metabolism (0.506)
- **Europe PMC papers**: 3203
- **Why important**: PGM1 is connected to PDXK and CPNE3 and is the most strongly established carbohydrate-metabolism gene in the module. It is the predominant PGM isozyme in most cell types according to the supplied annotation, participates in glucose and glycogen-related processes, and is associated with PGM1-congenital disorder of glycosylation and glycogen-metabolism disorders. Its extensive literature makes it a well-supported functional anchor rather than an annotation based only on network position.
- **Conclusion**: Established evidence supports PGM1 as a core carbohydrate and glycogen-metabolism enzyme that could contribute to the energetic or biosynthetic context of the module. Its broad expression also means that it may report general cellular metabolism rather than a module-specific mechanism.

#### BLVRA

- **Related proteins** (co-abundance neighbors): PDXK (0.86); STRING partners: BLVRB (0.993)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biliverdin reductase A. The protein encoded by this gene belongs to the biliverdin reductase family, members of which catalyze the conversion of biliverdin to bilirubin in the presence of NADPH or NADH. Mutations in this gene are associated with hyperbiliverdinemia. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Dec 2011].
- **Diseases (Open Targets)**: hyperbiliverdinemia (0.618); neurodegenerative disease (0.315); poisoning (0.255); response to xenobiotic stimulus (0.255); skin disorder (0.227)
- **Europe PMC papers**: 592
- **Why important**: BLVRA forms the strongest known STRING relationship in the module with BLVRB and is connected to PDXK in the co-abundance network. Its established function is NAD-dependent or NADPH-dependent conversion of biliverdin to bilirubin, placing it in heme catabolism and redox biology. HPA detects it in myometrium and shows enhancement across several epithelial, placental, and liver-associated cell types. Its disease associations include hyperbiliverdinemia and neurodegenerative disease.
- **Conclusion**: Established evidence supports BLVRA as a redox-linked heme-catabolic gene and as one half of the module's best-supported known interaction. Its contribution to a shared oxidative-stress response is plausible, but the module data do not show that BLVRA drives the co-abundance pattern.

#### BLVRB

- **Related proteins** (co-abundance neighbors): HEBP2 (0.83); STRING partners: BLVRA (0.993)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: biliverdin reductase B. The final step in heme metabolism in mammals is catalyzed by the cytosolic biliverdin reductase enzymes A and B (EC 1.3.1.24).[supplied by OMIM, Jul 2009]
- **Diseases (Open Targets)**: neurodegenerative disease (0.125); hepatocellular carcinoma (0.076); cholangiocarcinoma (0.074); ischemic stroke (0.055); neonatal intrahepatic cholestasis due to citrin deficiency (0.045)
- **Europe PMC papers**: 1322
- **Why important**: BLVRB is the partner of BLVRA in the high-confidence STRING relationship and is also one of the two module members represented in the (hu.MAP huMAP3_14442.1) hu.MAP complex. Its established function is biliverdin reduction and heme metabolism, with additional annotation for megakaryocyte differentiation. HPA links it to bone marrow, erythroid cell types, hepatocytes, and classical monocytes, making it informative for evaluating possible blood or cell-composition effects.
- **Conclusion**: Established evidence supports BLVRB as a heme-catabolic enzyme and as the most directly corroborated interaction partner in the module. Its erythroid and monocyte-related expression raises a composition-related alternative explanation, so a tissue-intrinsic role should not be assumed without cell-resolved validation.

## Module 6

**Tissue pair**: myometrium and stem_cells  
**Genes (18)**: CALU, COL12A1, CACYBP, FKBP9, HDGF, LYPLA1, PGP, PPME1, PFAS, TP53I3, RDX, RECQL, CTTN, TBC1D9B, TCEA1, THBS1, UBE3A, ZC3HAV1L

### Function

The module does not support a single statistically established GO or KEGG function: no GO or KEGG term passed global correction. Its structure instead suggests a mixed cellular program linking genome maintenance and transcriptional control with cytoskeletal, membrane, extracellular-matrix, protein-folding, and metabolic processes. The strongest network position belongs to ZC3HAV1L, which connects genes associated with phosphoglycolate and lipid-related metabolism, oxidative-stress or p53-linked biology, phosphatase regulation, calcium-associated processes, and transcriptional regulation. RECQL and TCEA1 provide a nuclear genome-maintenance and transcriptional-elongation axis, while CTTN, RDX, THBS1, and COL12A1 suggest cell shape, adhesion, cytoskeletal, and matrix biology. These are functional interpretations from individual gene annotations and network placement, not globally significant enrichment claims.

**Cell composition.** The module is compositionally mixed rather than a coherent plasma-protein module. It includes secreted or extracellular-matrix-associated genes such as THBS1, HDGF, and COL12A1, together with intracellular and nuclear proteins. HPA reports several genes with blood-cell or immune-cell associations, including megakaryocyte, neutrophil, basophil, eosinophil, macrophage, monocyte, and platelet-related profiles, but most genes have low immune-cell specificity. Many genes have low tissue specificity, while cell-type-enhanced signals span diverse populations such as hepatic stellate cells, megakaryocytes, esophageal apical cells, late spermatids, trophoblasts, adipocytes, and progenitors. This breadth is compatible with shared ubiquitous or cell-state biology and leaves open the possibility that some co-abundance reflects shared cell types or blood-related material in samples. It is not sufficient to conclude that the module is a blood-contamination module. HPA protein detection in myometrium supports expression of several members there, whereas there is no matching HPA tissue for the stem-cell group.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional enrichment or high-confidence STRING pair was reported. Thus, the module's co-abundance links are not independently supported by the supplied STRING interaction network, and the absence of STRING edges argues against calling it a canonical interaction-defined complex. hu.MAP provides more specific support for a nuclear or protein-complex component: TCEA1 and RECQL co-occur in huMAP3_14982.1 and huMAP3_10088.1, while HDGF also occurs with TCEA1 and RECQL in huMAP3_14982.1 (hu.MAP huMAP3_14982.1). These complexes contain many additional proteins that are not in the module, so the evidence supports partial embedding in known complexes rather than a complete module-wide complex. The hu.MAP observations are consistent with the RECQL-TCEA1-HDGF nuclear axis, but they do not establish physical interaction among all module members.

**STRING interactions (score >= 0.7)**: 0 of 153 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14982.1 (TCEA1, RECQL, HDGF; 3/28); huMAP3_10088.1 (TCEA1, RECQL; 2/10)

### Novelty

The module should be regarded as a potentially novel cross-tissue co-abundance pattern, not as a proven new molecular complex or pathway. Its novelty is supported by the lack of high-confidence STRING edges, the absence of STRING enrichment, the mixed functional composition, and the fact that only a subset of genes maps together in hu.MAP complexes (hu.MAP huMAP3_14982.1) and (hu.MAP huMAP3_10088.1). However, absence from STRING or hu.MAP alone cannot prove novelty: co-abundance may reflect coordinated regulation, shared cell composition, indirect biology, or incomplete database coverage. The most defensible claim is that the shared myometrium-stem-cell co-abundance configuration appears distinct from a previously catalogued interaction network and requires independent replication and perturbation testing.

**Hypothesis.** Hypothesis: the module represents a conserved cellular-state program that couples nuclear stress tolerance and transcriptional control to remodeling of cell shape, adhesion, and extracellular matrix. In this model, RECQL supports DNA-repair and replication-fork resilience, TCEA1 and HDGF support transcriptional and proliferative responses, while CTTN, RDX, THBS1, and COL12A1 connect those responses to cytoskeletal and matrix organization. ZC3HAV1L may act as a central co-regulated hub that links these otherwise heterogeneous processes, with CACYBP providing a possible bridge to ubiquitin-dependent regulation and calcium-responsive biology. This is a hypothesis derived from network topology and annotations; the data do not establish causality, direct binding, or a common upstream regulator.

### Important genes

#### ZC3HAV1L

- **Related proteins** (co-abundance neighbors): PGP (0.90), TP53I3 (0.90), PPME1 (0.87), CACYBP (0.85), CALU (0.84), LYPLA1 (0.82), TCEA1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ZC3HAV1 like. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: stroke disorder (0.188); alcohol drinking (0.188); primary biliary cholangitis (0.134); preeclampsia (0.063); hypothyroidism (0.027)
- **Europe PMC papers**: 130
- **Why important**: ZC3HAV1L has the strongest network position in the module and connects metabolic, stress-associated, phosphatase-regulatory, calcium-associated, and transcription-related neighbors. It has no reported STRING or hu.MAP support, so its centrality is specific to this co-abundance network rather than a known interaction hub. Its disease associations include stroke disorder, primary biliary cholangitis, preeclampsia, and hypothyroidism, while its literature volume is comparatively limited.
- **Conclusion**: Established evidence supports ZC3HAV1L as the module's network hub and as a cytosolic ZC3HAV1-like protein with broad disease associations. It is a plausible marker of the shared co-abundance state, but its molecular role in this module remains uncertain. A causal bridging role is hypothetical and requires validation.

#### RECQL

- **Related proteins** (co-abundance neighbors): THBS1 (0.87), CTTN (0.84), RDX (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_14982.1, huMAP3_10088.1
- **Function (MyGene.info)**: RecQ like helicase. The protein encoded by this gene is a member of the RecQ DNA helicase family. DNA helicases are enzymes involved in various types of DNA repair, including mismatch repair, nucleotide excision repair and direct repair. The encoded protein is involved in the processing of Holliday junctions, the suppression of sister chromatid exchanges, telomere maintenance, and is required for genotoxic stress res…
- **Diseases (Open Targets)**: RECON progeroid syndrome (0.595); hereditary neoplastic syndrome (0.505); obesity disorder (0.404); myofibrillar myopathy 8 (0.334); hereditary breast ovarian cancer syndrome (0.328)
- **Europe PMC papers**: 954
- **Why important**: RECQL connects THBS1, CTTN, and RDX in the module and is independently represented in both huMAP complexes (hu.MAP huMAP3_14982.1) and (hu.MAP huMAP3_10088.1). Its established annotation links it to RecQ helicase activity, DNA repair, replication-fork processing, homologous recombination, telomere maintenance, and genotoxic-stress resistance. It has substantial literature and disease associations involving progeroid, neoplastic, myopathy, and hereditary cancer-related conditions.
- **Conclusion**: Established evidence supports RECQL as the clearest genome-maintenance component and as part of known huMAP complexes. Its co-abundance with cytoskeletal and matrix genes suggests coordinated cellular-state regulation, but does not prove that RECQL directly controls those genes or structures.

#### TCEA1

- **Related proteins** (co-abundance neighbors): HDGF (0.86), PFAS (0.84), ZC3HAV1L (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_14982.1, huMAP3_10088.1
- **Function (MyGene.info)**: transcription elongation factor A1. Predicted to enable DNA binding activity; translation elongation factor activity; and zinc ion binding activity. Predicted to be involved in positive regulation of transcription by RNA polymerase II. Predicted to act upstream of or within erythrocyte differentiation and positive regulation of transcription, DNA-templated. Located in nucleolus and nucleoplasm. Part of transcription factor TFIID com…
- **Diseases (Open Targets)**: HIV infectious disease (0.584); Salivary Gland Pleomorphic Adenoma (0.370); salivary gland adenoid cystic carcinoma (0.370); Parotid Gland Pleomorphic Adenoma (0.370); salivary gland carcinoma ex pleomorphic adenoma (0.370)
- **Europe PMC papers**: 527
- **Why important**: TCEA1 occupies a bridging position between ZC3HAV1L, HDGF, and PFAS and is present in both huMAP complexes (hu.MAP huMAP3_14982.1) and (hu.MAP huMAP3_10088.1). Its annotations support transcriptional elongation, RNA polymerase activity, nucleolar and nucleoplasmic localization, and erythrocyte differentiation-related regulation. Its disease associations include HIV infectious disease and salivary-gland neoplasms, and it has a substantial literature base.
- **Conclusion**: Established evidence supports TCEA1 as a transcriptional machinery component and a known-complex member. It is a strong candidate for coordinating expression of the heterogeneous module, but the present data do not demonstrate that it is the upstream regulator of the observed co-abundance pattern.

#### THBS1

- **Related proteins** (co-abundance neighbors): RECQL (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum, Plasma membrane; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thrombospondin 1. The protein encoded by this gene is a subunit of a disulfide-linked homotrimeric protein. This protein is an adhesive glycoprotein that mediates cell-to-cell and cell-to-matrix interactions. This protein can bind to fibrinogen, fibronectin, laminin, type V collagen and integrins alpha-V/beta-1. This protein has been shown to play roles in platelet aggregation, angiogenesis, and tumorigenesis. [pro…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.385); tooth disorder (0.350); autism spectrum disorder (0.336); neurodegenerative disease (0.323); metabolic syndrome (0.309)
- **Europe PMC papers**: 12762
- **Why important**: THBS1 links the module to extracellular matrix and cell-matrix biology and is connected to RECQL in the co-abundance graph. HPA identifies it as secreted to the extracellular matrix and enhanced in fibroblasts, hepatic stellate cells, macrophages, monocytes, and platelets, with immune-cell enhancement in eosinophils. Its established functions include cell adhesion, matrix interactions, platelet aggregation, angiogenesis, hypoxia response, and inflammatory regulation. It has a large literature base and broad disease associations.
- **Conclusion**: Established evidence supports THBS1 as the most conspicuous extracellular and stromal interface in the module. Its presence could reflect genuine matrix remodeling in myometrium, shared stromal or platelet-associated material, or both. A direct connection from THBS1 to the nuclear RECQL-TCEA1 axis remains hypothetical.

#### COL12A1

- **Related proteins** (co-abundance neighbors): CACYBP (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type XII alpha 1 chain. This gene encodes the alpha chain of type XII collagen, a member of the FACIT (fibril-associated collagens with interrupted triple helices) collagen family. Type XII collagen is a homotrimer found in association with type I collagen, an association that is thought to modify the interactions between collagen I fibrils and the surrounding matrix. Alternatively spliced transcript variants encoding di…
- **Diseases (Open Targets)**: Bethlem myopathy 2 (0.794); Ullrich congenital muscular dystrophy 2 (0.709); Bethlem myopathy (0.617); Abnormality of the skeletal system (0.533); Ullrich congenital muscular dystrophy (0.501)
- **Europe PMC papers**: 3324
- **Why important**: COL12A1 connects to CACYBP and provides a strong extracellular-matrix interpretation. HPA reports tissue enhancement in ovary, cell-type enhancement across stromal, adipocyte, epithelial, and progenitor populations, absence from immune cells, secretion to extracellular matrix, and detection in myometrium. Its established function concerns type XII collagen, collagen-fibril organization, and tissue development. It has substantial literature and disease associations involving Bethlem myopathy, Ullrich congenital muscular dystrophy, and skeletal abnormalities.
- **Conclusion**: Established evidence supports COL12A1 as a matrix-remodeling component and a plausible contributor to the shared myometrial and stem-cell tissue-state signal. Its co-abundance with nuclear and cytosolic genes does not establish a direct molecular interaction; a common stromal or differentiation state is a more cautious interpretation.

## Module 7

**Tissue pair**: myometrium and stem_cells  
**Genes (5)**: CCS, COQ9, NUBP2, PSMF1, RGS10

### Function

The module does not have a globally significant GO or KEGG annotation: no term passed global correction. Its genes nevertheless point to complementary intracellular processes. PSMF1 is related to proteasome-mediated protein turnover, NUBP2 to cytosolic iron-sulfur cluster assembly, COQ9 to mitochondrial ubiquinone biosynthesis, CCS to copper delivery for superoxide dismutase and oxidative-stress control, and RGS10 to regulation of heterotrimeric G-protein signaling. The co-abundance pattern therefore suggests a possible intracellular maintenance state involving proteostasis, mitochondrial and cofactor biology, redox control, and signaling regulation. This interpretation is provisional because the subgraph is sparse and the enrichment analyses provide no globally corrected functional support.

**Cell composition.** The module is composed of intracellular proteins rather than plasma or secreted proteins; the HPA summary identifies no secreted genes. All members have low immune-cell specificity, so the module does not specifically indicate blood-cell contamination. Several genes show cell-type-enhanced patterns, including platelets, late spermatids, esophageal cells, glial cells, hepatocytes, megakaryocytes, and immune-related cell types, while tissue specificity is generally low. HPA protein detection in myometrium is mixed, with some members detected and others not detected. The shared signal could therefore reflect a broadly distributed intracellular program or shared cellular composition, but the supplied HPA evidence does not establish a blood-derived origin.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional-enrichment term is reported, no STRING interaction among the module members meets the supplied confidence threshold, and no hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not supported here as established physical protein interactions or as membership in a known complex. The absence of STRING and hu.MAP support weakens a claim that this is a compact canonical molecular complex, but it does not invalidate a coordinated transcriptional or cellular-state association. The individual annotations still provide biologically plausible links through proteostasis, cofactors, mitochondria, redox control, and G-protein signaling.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact shared co-abundance module may be a new observation in this tissue-pair analysis because it lacks corresponding STRING interaction support, hu.MAP complex support, and globally significant GO or KEGG enrichment. However, those absences alone do not prove novelty. Several member genes have established functions and disease associations, and pairwise co-abundance can arise from broad expression programs, cellular composition, or technical and biological covariation. The defensible conclusion is that the specific cross-tissue module is insufficiently characterized and potentially novel, rather than that it represents a newly discovered molecular pathway.

**Hypothesis.** Hypothesis: the module marks a shared intracellular stress-adaptation or maintenance state present in cells represented in both myometrium and stem-cell samples. In this model, PSMF1 reflects proteostasis control, NUBP2 supports iron-sulfur protein maturation, COQ9 supports mitochondrial ubiquinone production, CCS supports antioxidant capacity, and RGS10 modulates extracellular-signal input through G-protein pathways. Coordinated regulation of these functions could help cells maintain protein quality, respiration, redox balance, and signal responsiveness. This is a mechanistic hypothesis, not an enrichment-supported conclusion, and should be tested by replication, cell-composition adjustment, and perturbation or expression-level validation.

### Important genes

#### PSMF1

- **Related proteins** (co-abundance neighbors): NUBP2 (0.91), RGS10 (0.90), CCS (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome inhibitor subunit 1. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: complex neurodevelopmental disorder with motor features (0.399); placental abruption (0.318); methicillin-resistant staphylococcus aureus infectious disease (0.308); jaw disease (0.209); neurodegenerative disease (0.188)
- **Europe PMC papers**: 411
- **Why important**: PSMF1 has the strongest network connectivity in the module and links the co-abundance pattern to proteasome-associated protein catabolism. Its cytosolic localization and low tissue specificity are consistent with a broadly deployed intracellular function. It also provides a bridge to RGS10 and CCS in the observed module structure, although no corresponding STRING or hu.MAP relationship is established here. Its disease associations and substantial literature make it a biologically interpretable anchor.
- **Conclusion**: Established: PSMF1 is a proteasome inhibitor subunit involved in ubiquitin-dependent protein catabolic processes. Hypothesis: its central module position may indicate that proteostasis is a coordinating component of the shared state, but the co-abundance data do not establish causal control.

#### COQ9

- **Related proteins** (co-abundance neighbors): NUBP2 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coenzyme Q9. This locus represents a mitochondrial ubiquinone biosynthesis gene. The encoded protein is likely necessary for biosynthesis of coenzyme Q10, as mutations at this locus have been associated with autosomal-recessive neonatal-onset primary coenzyme Q10 deficiency.[provided by RefSeq, Sep 2010].
- **Diseases (Open Targets)**: encephalopathy-hypertrophic cardiomyopathy-renal tubular disease syndrome (0.766); coenzyme Q10 deficiency (0.635); hereditary disease (0.415); mitochondrial disease (0.372); coenzyme Q10 deficiency, primary, 1 (0.370)
- **Europe PMC papers**: 958
- **Why important**: COQ9 connects the module to mitochondrial ubiquinone biosynthesis and has a tissue-enhanced skeletal-muscle pattern, while its protein is detected in myometrium. It is linked to primary coenzyme Q deficiency and mitochondrial disease, giving the gene clear functional and disease relevance. Its observed connection to NUBP2 suggests a possible cofactor or energy-maintenance relationship within the module, though this is not supported as a known physical interaction by the supplied databases.
- **Conclusion**: Established: COQ9 participates in ubiquinone production and is associated with inherited coenzyme Q deficiency syndromes. Hypothesis: COQ9 may represent a mitochondrial-energy component of the shared module, but the module does not demonstrate that mitochondrial dysfunction is present.

#### CCS

- **Related proteins** (co-abundance neighbors): PSMF1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: copper chaperone for superoxide dismutase. Copper chaperone for superoxide dismutase specifically delivers Cu to copper/zinc superoxide dismutase and may activate copper/zinc superoxide dismutase through direct insertion of the Cu cofactor. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); migraine disorder (0.129); Neurodegeneration (0.111); breast cancer (0.097); breast carcinoma (0.097)
- **Europe PMC papers**: 34249
- **Why important**: CCS is the module member with especially extensive literature and has a direct biochemical role in delivering copper to superoxide dismutase. It is connected to PSMF1 in the co-abundance graph and is detected in myometrium. Its annotation links the module to superoxide removal, oxidative-stress response, mitochondrial protein maturation, and protein import.
- **Conclusion**: Established: CCS is a copper chaperone that activates copper-zinc superoxide dismutase and supports superoxide handling. Hypothesis: CCS may indicate a redox-maintenance dimension of the shared state, but oxidative stress is not demonstrated by the module-level statistics.

#### NUBP2

- **Related proteins** (co-abundance neighbors): PSMF1 (0.91), COQ9 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NUBP iron-sulfur cluster assembly factor 2, cytosolic. This gene encodes an adenosine triphosphate (ATP) and metal-binding protein that is required for the assembly of cyotosolic iron-sulfur proteins. The encoded protein functions in a heterotetramer with nucleotide-binding protein 1 (NUBP1). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2013].
- **Diseases (Open Targets)**: metabolic syndrome (0.074); colorectal carcinoma (0.074); retinitis pigmentosa (0.066); exudative vitreoretinopathy (0.065); familial digital arthropathy-brachydactyly (0.062)
- **Europe PMC papers**: 261
- **Why important**: NUBP2 occupies an intermediate network position by connecting PSMF1 and COQ9. It is required for cytosolic iron-sulfur cluster assembly and has a broadly distributed tissue profile, with protein detected in myometrium. Its position provides a plausible link between cellular protein maintenance and mitochondrial or cofactor-related biology, while its disease associations add relevance beyond the network topology.
- **Conclusion**: Established: NUBP2 is an iron-sulfur cluster assembly factor that functions with NUBP1. Hypothesis: its placement may reflect coordinated cofactor and metabolic maintenance, but the observed edge pattern cannot establish a biochemical pathway linking NUBP2 to the other module members.

#### RGS10

- **Related proteins** (co-abundance neighbors): PSMF1 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: regulator of G protein signaling 10. Regulator of G protein signaling (RGS) family members are regulatory molecules that act as GTPase activating proteins (GAPs) for G alpha subunits of heterotrimeric G proteins. RGS proteins are able to deactivate G protein subunits of the Gi alpha, Go alpha and Gq alpha subtypes. They drive G proteins into their inactive GDP-bound forms. Regulator of G protein signaling 10 belongs to this family. A…
- **Diseases (Open Targets)**: hair color (0.310); ovarian carcinoma (0.104); ovarian cancer (0.101); Parkinson disease (0.100); type 2 diabetes mellitus (0.094)
- **Europe PMC papers**: 765
- **Why important**: RGS10 is the module member that most clearly introduces signaling regulation. It acts as a GTPase-activating regulator for heterotrimeric G-protein pathways and has tissue enhancement in lymphoid tissue together with several cell-type-enhanced patterns. Its connection to the highly connected PSMF1 makes it a potentially important interface between signaling state and intracellular maintenance.
- **Conclusion**: Established: RGS10 regulates G-protein signaling by promoting inactivation of selected G-alpha subunits. Hypothesis: RGS10 may couple extracellular signaling inputs to the proposed proteostasis, redox, and metabolic state, but this coupling is not directly demonstrated by the supplied evidence.

## Module 8

**Tissue pair**: myometrium and stem_cells  
**Genes (5)**: CNN1, GLRX, PDLIM7, PNPO, SORBS1

### Function

The module is most consistent with a cytoskeletal and smooth-muscle-associated co-abundance program, with links to actin-filament organization, focal adhesions, cell-matrix adhesion, and redox regulation. CNN1 and PDLIM7 localize to actin-associated structures, while SORBS1 is associated with focal adhesions, stress fibers, cell-substrate adhesion, and insulin signaling. GLRX provides a plausible redox-regulatory component, and PNPO represents a vitamin B6 metabolic enzyme connected to the structurally related genes only through the observed co-abundance pattern. However, no GO or KEGG term passed global correction, and STRING reported no supplementary functional enrichment, so this functional interpretation is gene-based and network-based rather than enrichment-validated.

**Cell composition.** The module is not composed of secreted proteins, and the HPA data do not indicate a dominant plasma-protein signature. All genes have tissue-enhanced and cell-type-enhanced annotations, with recurring associations to smooth muscle, vascular smooth muscle, skeletal muscle, blood vessel, and related stromal or contractile cell types. This supports a shared contractile or mesenchymal cell-state interpretation in myometrium and stem cells. Some genes have blood-cell associations, particularly SORBS1 and PDLIM7, while other genes have low immune specificity or are not detected in immune cells. Therefore, blood contamination cannot be excluded solely from the module, but the overall composition is more compatible with a structural muscle or vascular-associated cell population than with a primarily blood-derived module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The observed co-abundance network contains relationships among CNN1, GLRX, PNPO, SORBS1, and PDLIM7, but none of the possible gene pairs meets the supplied high-confidence STRING interaction threshold. No STRING partners are listed for any member, and no hu.MAP complex contains multiple module members. Thus, the network is not a recovery of an established STRING interaction cluster or known hu.MAP complex. The connected pattern may reflect coordinated expression in a shared cellular state, indirect regulation, common tissue composition, or technical covariance rather than direct physical binding. The annotations of CNN1, SORBS1, and PDLIM7 nevertheless provide a biologically coherent actin and adhesion context, while GLRX and PNPO may represent redox and metabolic coupling.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should be described as a potentially novel co-abundance association rather than a proven new biological complex or pathway. Its novelty is supported by the absence of a corresponding high-confidence STRING interaction set, the absence of a multi-member hu.MAP complex, and the lack of globally significant GO or KEGG enrichment. These observations indicate that the specific coordinated pattern is not readily explained by an established interaction or annotated pathway. They do not prove novelty, because the pattern could arise from shared cell composition, tissue state, indirect regulation, or limitations of interaction databases. Independent replication, cell-composition adjustment, and validation at the protein or perturbation level would be needed before claiming a new mechanism.

**Hypothesis.** Hypothesis: in myometrium and stem-cell-related populations, a shared smooth-muscle or mesenchymal cell state coordinates actin organization, focal-adhesion signaling, and contractile architecture through CNN1, SORBS1, and PDLIM7. GLRX may modulate the redox state of proteins involved in this structural program, while PNPO may reflect linked vitamin B6 metabolic demand or a broader metabolic state. The five-gene pattern may therefore represent coordinated regulation of a contractile structural state rather than a direct protein complex. This hypothesis should be tested by controlling for cell composition, measuring protein abundance and localization, and perturbing the candidate structural genes while monitoring adhesion, contractility, and redox-sensitive signaling.

### Important genes

#### CNN1

- **Related proteins** (co-abundance neighbors): GLRX (0.91), PNPO (0.89), SORBS1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Actin filaments; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calponin 1. Predicted to enable actin binding activity. Involved in negative regulation of vascular associated smooth muscle cell proliferation. Located in cytoskeleton. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.356); self-injurious ideation (0.114); breast cancer (0.096); neoplasm (0.093); breast carcinoma (0.086)
- **Europe PMC papers**: 3024
- **Why important**: CNN1 has the strongest network connectivity in the module and links to GLRX, PNPO, and SORBS1. It is an actin-binding calponin associated with smooth-muscle contraction, actomyosin organization, and negative regulation of vascular smooth-muscle proliferation. It is enhanced in blood vessel, intestine, and smooth muscle, detected in myometrium, and has substantial literature support.
- **Conclusion**: Established evidence supports CNN1 as the leading structural and smooth-muscle marker of the module. Its central network position makes it a strong candidate for organizing the co-abundance pattern. It is a plausible mechanistic driver, but causality is not established by the supplied data.

#### SORBS1

- **Related proteins** (co-abundance neighbors): GLRX (0.86), CNN1 (0.84), PDLIM7 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Focal adhesion sites; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sorbin and SH3 domain containing 1. This gene encodes a CBL-associated protein which functions in the signaling and stimulation of insulin. Mutations in this gene may be associated with human disorders of insulin resistance. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.454); atrial fibrillation (0.394); urinary system disorder (0.381); uterine corpus leiomyoma (0.351); hypertensive disorder (0.345)
- **Europe PMC papers**: 1367
- **Why important**: SORBS1 is highly connected and links GLRX, CNN1, and PDLIM7. Its annotated functions include focal-adhesion biology, stress-fiber assembly, cell-matrix and cell-substrate adhesion, insulin-receptor signaling, and cytoskeletal organization. It is enhanced in blood vessel and detected in myometrium, with an association to uterine corpus leiomyoma among its disease links.
- **Conclusion**: Established evidence supports SORBS1 as an adhesion and signaling bridge between the actin-associated members. Its position makes it a strong candidate for coupling extracellular or insulin-related signals to the cytoskeleton. A role in the shared module's mechanism remains a hypothesis.

#### PDLIM7

- **Related proteins** (co-abundance neighbors): SORBS1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Actin filaments, Focal adhesion sites; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 7. The protein encoded by this gene is representative of a family of proteins composed of conserved PDZ and LIM domains. LIM domains are proposed to function in protein-protein recognition in a variety of contexts including gene transcription and development and in cytoskeletal interaction. The LIM domains of this protein bind to protein kinases, whereas the PDZ domain binds to actin filaments. The g…
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); nasopharyngeal carcinoma (0.121); neoplasm (0.120); lymphoma (0.115); Hodgkins lymphoma (0.105)
- **Europe PMC papers**: 808
- **Why important**: PDLIM7 connects to SORBS1 and is localized to actin filaments and focal-adhesion sites. Its PDZ and LIM domains support protein recognition and cytoskeletal interactions, and its annotations include actin-cytoskeleton organization and muscle-structure development. It is enhanced in blood vessel, intestine, and skeletal muscle and is detected in myometrium.
- **Conclusion**: Established evidence supports PDLIM7 as a structural adaptor compatible with the module's adhesion and muscle-associated character. Its peripheral network position does not diminish its potential importance because adaptor proteins can organize local signaling without many co-abundance links. Direct involvement in this module's regulation is not demonstrated.

#### GLRX

- **Related proteins** (co-abundance neighbors): CNN1 (0.91), SORBS1 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutaredoxin. This gene encodes a member of the glutaredoxin family. The encoded protein is a cytoplasmic enzyme catalyzing the reversible reduction of glutathione-protein mixed disulfides. This enzyme highly contributes to the antioxidant defense system. It is crucial for several signalling pathways by controlling the S-glutathionylation status of signalling mediators. It is involved in beta-amyloid toxicity a…
- **Diseases (Open Targets)**: hemolysis (0.351); adolescent idiopathic scoliosis (0.289); liver disorder (0.232); vascular disorder (0.203); musculoskeletal system disorder (0.171)
- **Europe PMC papers**: 1222
- **Why important**: GLRX occupies an internal position connecting CNN1 and SORBS1. It encodes a glutaredoxin that regulates protein glutathionylation and contributes to antioxidant defense and signaling control. Its tissue annotation is enriched in skeletal muscle, and its disease associations include vascular and musculoskeletal disorders.
- **Conclusion**: Established evidence supports GLRX as a redox-regulatory component that could influence cytoskeletal or adhesion proteins indirectly. Its placement alongside CNN1 and SORBS1 makes redox control a plausible interpretive layer. The proposed redox-to-contractility connection is mechanistic speculation rather than a demonstrated interaction.

#### PNPO

- **Related proteins** (co-abundance neighbors): CNN1 (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyridoxamine 5'-phosphate oxidase. The enzyme encoded by this gene catalyzes the terminal, rate-limiting step in the synthesis of pyridoxal 5'-phosphate, also known as vitamin B6. Vitamin B6 is a required co-factor for enzymes involved in both homocysteine metabolism and synthesis of neurotransmitters such as catecholamine. Mutations in this gene result in pyridoxamine 5'-phosphate oxidase (PNPO) deficiency, a form of neonatal epil…
- **Diseases (Open Targets)**: pyridoxal phosphate-responsive seizures (0.806); hereditary disease (0.485); Seizure (0.401); neuronopathy, distal hereditary motor, type 5A (0.340); fetal growth restriction (0.333)
- **Europe PMC papers**: 20173
- **Why important**: PNPO is connected to CNN1 in the module and encodes the enzyme catalyzing the terminal step in pyridoxal phosphate synthesis. Vitamin B6-derived cofactors support neurotransmitter and homocysteine-related metabolism, and PNPO has extensive disease and literature annotation, including pyridoxal-phosphate-responsive seizures. Its liver tissue enhancement and limited network connectivity make it a potentially informative metabolic outlier.
- **Conclusion**: Established evidence supports PNPO as a vitamin B6 metabolic enzyme, but not as a smooth-muscle structural protein. Its association with CNN1 may reflect shared cell state, metabolic coupling, or indirect covariance. A specific role for PNPO in the proposed contractile module is therefore the most tentative conclusion among the selected genes.

## Module 9

**Tissue pair**: myometrium and stem_cells  
**Genes (9)**: CNOT1, ECHDC1, FABP3, FXN, HDHD2, PDLIM5, TIPRL, UBA6, VPS13C

### Function

The module does not support a single statistically established GO or KEGG function because no GO or KEGG term passed global correction. Its genes instead suggest a heterogeneous intracellular program involving membrane and lipid trafficking, fatty-acid handling, mitochondrial iron and respiration biology, ubiquitin-dependent protein regulation, RNA regulation, and muscle-associated structural signaling. The network is sparse and does not show a coherent known pathway, so these functional themes should be treated as gene-level interpretation rather than enrichment-based evidence.

**Cell composition.** The module is not dominated by plasma or secreted proteins: no member is annotated as secreted. Most genes have low tissue specificity, which is consistent with broadly expressed intracellular biology rather than a sharply restricted tissue program. A subset shows enrichment in heart muscle, skeletal muscle, or tongue, and several genes show enhanced expression in selected cell types including megakaryocytes, parietal cells, adipocytes, erythrocyte progenitors, hepatocytes, cardiomyocytes, and myonuclei. Immune-cell specificity is generally low, with only PDLIM5 showing immune-cell enrichment in basophils. Thus, the module does not strongly resemble a blood-cell or plasma-protein contaminant, although shared muscle-related cells or broadly expressed housekeeping-like programs could contribute to its conservation between myometrium and stem cells. Protein detection in myometrium supports expression of part of the module, whereas matching HPA protein evidence is unavailable for stem cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship was reported among the module genes, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. Therefore, the co-abundance relationships are not corroborated by the supplied curated interaction or complex resources. This may reflect tissue-contextual co-regulation, indirect relationships, limitations of existing databases, or a data-derived association rather than a physically interacting complex. The absence of STRING and hu.MAP support means the module should not be described as a known molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module is potentially novel as a tissue-pair co-abundance pattern because it lacks support from the supplied STRING and hu.MAP resources and does not correspond to a globally significant GO or KEGG enrichment. However, those absences do not establish biological novelty. Several component genes and their functions are well established individually, and the module could represent a previously unrecognized combination of broadly expressed intracellular, metabolic, mitochondrial, and muscle-associated genes. A stronger novelty claim would require replication in independent myometrium and stem-cell datasets, preservation of the gene-level association, comparison with published co-expression modules, and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular homeostasis program that couples lipid and membrane handling with mitochondrial function, protein turnover, and cytoskeletal or muscle-associated signaling. VPS13C and ECHDC1 could represent membrane-lipid and fatty-acid-related components; FABP3 and PDLIM5 could connect lipid handling to muscle-associated structural biology; FXN could connect the pattern to mitochondrial iron and respiration; and TIPRL or UBA6 could provide regulatory control through phosphatase inhibition and ubiquitin-like protein activation. This is a mechanistic hypothesis, not an established pathway assignment, because the module lacks globally significant enrichment and curated interaction support.

### Important genes

#### VPS13C

- **Related proteins** (co-abundance neighbors): CNOT1 (0.85), ECHDC1 (0.85), HDHD2 (0.81), TIPRL (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vacuolar protein sorting 13 homolog C. This gene encodes a member of the vacuolar protein sorting-associated 13 gene family. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Oct 2010]
- **Diseases (Open Targets)**: young-onset Parkinson disease (0.726); Parkinson disease (0.545); type 2 diabetes mellitus (0.460); neurodegenerative disease (0.456); diabetes mellitus (0.418)
- **Europe PMC papers**: 1114
- **Why important**: VPS13C is the most connected node in the module and links genes associated with membrane trafficking, lipid handling, mitochondrial biology, and regulation. Its annotated roles in Golgi-to-endosome transport, phospholipid transport, mitochondrion organization, macroautophagy, and mitophagy make it a plausible integrator of several module themes. It also has substantial literature and disease associations involving Parkinson disease and diabetes.
- **Conclusion**: Established evidence supports VPS13C as a membrane and organelle homeostasis protein with disease relevance. Its central network position makes it a strong candidate for organizing the module, but the data do not establish that it causally drives the shared myometrium–stem-cell pattern.

#### FABP3

- **Related proteins** (co-abundance neighbors): TIPRL (0.86), PDLIM5 (0.84); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Not detected in immune cells; location Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fatty acid binding protein 3. The intracellular fatty acid-binding proteins (FABPs) belongs to a multigene family. FABPs are divided into at least three distinct types, namely the hepatic-, intestinal- and cardiac-type. They form 14-15 kDa proteins and are thought to participate in the uptake, intracellular metabolism and/or transport of long-chain fatty acids. They may also be responsible in the modulation of cell growth and …
- **Diseases (Open Targets)**: early-onset non-syndromic cataract (0.114); Alzheimer disease (0.110); acute myocardial infarction (0.109); early-onset zonular cataract (0.109); early-onset nuclear cataract (0.106)
- **Europe PMC papers**: 4403
- **Why important**: FABP3 connects the module to intracellular long-chain fatty-acid transport and fatty-acid metabolism. It is connected to TIPRL and PDLIM5, and its tissue pattern is enriched in heart muscle, skeletal muscle, and tongue, making it especially relevant to the muscle-associated context. It is also among the more extensively studied genes in the module.
- **Conclusion**: Established evidence supports FABP3 as an intracellular lipid-binding and transport protein with muscle-associated expression. Its module role may involve coordinating lipid availability with muscle-cell structural or energetic demands, but that coordination remains a hypothesis.

#### PDLIM5

- **Related proteins** (co-abundance neighbors): FABP3 (0.84); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 5. This gene encodes a member of a family of proteins that possess a 100-amino acid PDZ domain at the N terminus and one to three LIM domains at the C-terminus. This family member functions as a scaffold protein that tethers protein kinases to the Z-disk in striated muscles. It is thought to function in cardiomyocyte expansion and in restraining postsynaptic growth of excitatory synapses. Alternative…
- **Diseases (Open Targets)**: prostate carcinoma (0.515); uterine corpus leiomyoma (0.461); neurodegenerative disease (0.423); prostate cancer (0.391); Abnormality of the skeletal system (0.375)
- **Europe PMC papers**: 1238
- **Why important**: PDLIM5 is a scaffold associated with the plasma membrane and muscle structure. Its annotated functions include tethering protein kinases to the Z-disc, actin cytoskeleton organization, heart development, and muscle structure development. Its muscle-enriched tissue pattern and connection to FABP3 make it a useful bridge between metabolic and structural interpretations. It also has an association with uterine corpus leiomyoma.
- **Conclusion**: Established evidence supports PDLIM5 as a muscle-related signaling and cytoskeletal scaffold. It may help explain conservation of the module in myometrium or shared muscle-like cells, but the module does not demonstrate a direct PDLIM5-centered complex.

#### FXN

- **Related proteins** (co-abundance neighbors): HDHD2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: frataxin. This nuclear gene encodes a mitochondrial protein which belongs to the FRATAXIN family. The protein functions in regulating mitochondrial iron transport and respiration. The expansion of intronic trinucleotide repeat GAA from 8-33 repeats to >90 repeats results in Friedreich ataxia. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2016].
- **Diseases (Open Targets)**: Friedreich ataxia (0.855); neurodegenerative disease (0.543); hereditary disease (0.341); migraine disorder (0.294); abscess (0.289)
- **Europe PMC papers**: 2894
- **Why important**: FXN is the module's mitochondrial iron and respiration gene, with functions in iron-sulfur cluster assembly, heme biosynthesis, iron homeostasis, and mitochondrial respiration. It is connected to HDHD2 and shows enhanced expression in several metabolically active or progenitor cell types. Its strong disease association with Friedreich ataxia and extensive literature make it an important biological anchor.
- **Conclusion**: Established evidence supports FXN as a mitochondrial iron and energy-homeostasis factor. Its presence is compatible with a module involving cellular energetic state, but it does not prove that mitochondrial dysfunction or Friedreich ataxia biology is responsible for the tissue-pair association.

#### TIPRL

- **Related proteins** (co-abundance neighbors): FABP3 (0.86), UBA6 (0.85), VPS13C (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TOR signaling pathway regulator. TIPRL is an inhibitory regulator of protein phosphatase-2A (PP2A) (see PPP2CA; MIM 176915), PP4 (see PPP4C; MIM 602035), and PP6 (see PPP6C; MIM 612725) (McConnell et al., 2007 [PubMed 17384681]).[supplied by OMIM, Nov 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.419); alcohol drinking (0.327); urolithiasis (0.327); neoplasm (0.094); lung carcinoma (0.093)
- **Europe PMC papers**: 341
- **Why important**: TIPRL occupies a connecting position between VPS13C, FABP3, and UBA6. It is annotated as a regulator of TOR signaling and an inhibitor of PP2A, PP4, and PP6, and it also participates in DNA-damage checkpoint signaling. This gives it a plausible regulatory role linking metabolism, stress responses, and protein-phosphorylation control.
- **Conclusion**: Established evidence supports TIPRL as a phosphatase-regulatory and TOR-associated protein. It could coordinate metabolic and stress signaling within the module, but this regulatory interpretation is not directly demonstrated by the co-abundance data.

## Module 10

**Tissue pair**: myometrium and stem_cells  
**Genes (14)**: CYRIB, DDAH1, DDX6, GMPS, EIF4G1, IRGQ, MAT2A, PSMC2, ADSS2, RAD50, SF3A1, SMS, NARS1, UBQLN2

### Function

This module does not have a globally significant GO or KEGG enrichment term; therefore no pathway-level function can be assigned from enrichment analysis. Its gene content instead suggests a mixed cellular maintenance program. SMS and MAT2A support polyamine and methyl-donor metabolism, while GMPS and ADSS2 support purine nucleotide biosynthesis. DDX6 and EIF4G1 connect RNA turnover, translational control, and mRNA recruitment, with SF3A1 adding pre-mRNA splicing and PSMC2 adding proteasome-associated protein quality control. DDAH1, CYRIB, IRGQ, UBQLN2, RAD50, and NARS1 add nitric-oxide regulation, cytoskeletal or migration-related control, autophagy or protein quality control, DNA repair, and translation functions. The overall interpretation is therefore a broad biosynthetic, RNA-processing, proteostasis, and genome-maintenance module rather than a narrowly defined pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. It also does not resemble a blood-cell module, because nearly all genes have low immune-cell specificity, no enriched blood-cell category is reported, and one gene is not detected in immune cells. Most genes have low tissue specificity, which is compatible with broadly expressed housekeeping or core cellular functions. At the same time, many genes have cell-type-enhanced HPA patterns, especially late spermatids, with additional signals in microglia, neutrophil progenitors, neutrophils, astrocytes, and other specialized cell types. These patterns do not establish contamination, but they indicate that shared cell states or common cellular programs could contribute to the co-abundance signal. Protein detection in myometrium for many members supports biological presence there; the stem-cell comparison cannot be assessed by matched HPA protein detection because no corresponding HPA tissue is available.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The high-confidence STRING evidence consists of three established pairwise relationships: ADSS2 with GMPS, DDX6 with EIF4G1, and MAT2A with SMS. These relationships provide independent support for local links between purine metabolism, RNA regulation, and methyl-donor or polyamine metabolism. However, STRING does not provide a connected interaction framework for the whole module, and no supplementary STRING functional enrichment is reported. No hu.MAP complex contains multiple module members. Thus, the module contains several known molecular relationships but is not supported as a pre-existing multiprotein complex. The remaining co-abundance links may reflect coordinated expression, shared cellular state, indirect regulation, or context-specific biology rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 3 of 91 gene pairs: ADSS2–GMPS (0.834); DDX6–EIF4G1 (0.857); MAT2A–SMS (0.809)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should be regarded as a potentially novel co-abundance configuration, not as a proven new pathway or complex. Its constituent functions and several pairwise relationships are already well established, and the genes have substantial prior disease and literature annotation. Conversely, the absence of a multi-member hu.MAP complex and the limited STRING connectivity mean that the specific shared co-abundance organization across myometrium and stem cells is not explained by an already recognized complex. Novelty would require replication in independent datasets, preservation of the module across processing choices, and experimental testing of coordinated regulation. Absence from interaction databases alone is insufficient to claim discovery.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular resource-management state in which nucleotide production, methyl-donor and polyamine metabolism, translation initiation, RNA decay, protein quality control, and DNA repair are coordinated. SMS and MAT2A could couple metabolic state to growth or translation, while GMPS and ADSS2 could maintain nucleotide availability. DDX6 and EIF4G1 could tune the balance between mRNA translation and decay, with UBQLN2, IRGQ, and PSMC2 helping manage damaged or misfolded proteins. This model could represent a common proliferative, differentiating, or stress-adapted cell state shared by the two tissue groups, but it remains a mechanistic hypothesis because global enrichment and multi-protein-complex evidence are absent.

### Important genes

#### SMS

- **Related proteins** (co-abundance neighbors): DDAH1 (0.89), EIF4G1 (0.88), NARS1 (0.86), CYRIB (0.85), IRGQ (0.85); STRING partners: MAT2A (0.809)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: spermine synthase. This gene encodes a protein belonging to the spermidine/spermin synthase family and catalyzes the production of spermine from spermidine. Pseudogenes of this gene are located on chromosomes 1, 5, 6 and X. Mutations in this gene cause an X-linked intellectual disability called Snyder-Robinson Syndrome (SRS). Multiple transcript variants encoding different isoforms have been found for this gene. [pr…
- **Diseases (Open Targets)**: syndromic X-linked intellectual disability Snyder type (0.814); hereditary disease (0.484); Intellectual disability (0.337); autoimmune disorder of central nervous system (0.336); neurodegenerative disease (0.331)
- **Europe PMC papers**: 14362
- **Why important**: SMS is the most central node in the module and connects to DDAH1, EIF4G1, NARS1, CYRIB, and IRGQ. Its established function is spermine production from spermidine, placing polyamine metabolism at the intersection of several otherwise heterogeneous module components. It is detected in myometrium, has low tissue specificity, and has extensive literature and disease annotation, including Snyder-Robinson syndrome.
- **Conclusion**: Established conclusion: SMS is a strong network and biochemical anchor for a metabolic interpretation. Hypothesis: its co-abundance may link polyamine availability to RNA handling, cytoskeletal regulation, or cellular stress in the shared tissue state. The module does not establish that SMS drives the other genes.

#### DDX6

- **Related proteins** (co-abundance neighbors): EIF4G1 (0.91), GMPS (0.84), UBQLN2 (0.84), RAD50 (0.81); STRING partners: EIF4G1 (0.857)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytoplasmic bodies; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 6. This gene encodes a member of the DEAD box protein family. The protein is an RNA helicase found in P-bodies and stress granules, and functions in translation suppression and mRNA degradation. It is required for microRNA-induced gene silencing. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: intellectual developmental disorder with impaired language and dysmorphic facies (0.650); Intellectual disability (0.555); neurodegenerative disease (0.459); lung carcinoma (0.371); Global developmental delay (0.371)
- **Europe PMC papers**: 3002
- **Why important**: DDX6 is among the more connected genes and links EIF4G1, GMPS, UBQLN2, and RAD50. It is an RNA helicase involved in P-bodies, stress granules, translational repression, microRNA-mediated silencing, and mRNA decay. Its high-confidence STRING relationship with EIF4G1 gives the module a particularly clear RNA regulation connection. It is detected in myometrium and has substantial literature and disease annotation.
- **Conclusion**: Established conclusion: DDX6 supports a post-transcriptional RNA-control component and has an independently supported relationship with EIF4G1. Hypothesis: DDX6 may coordinate selective translation and mRNA clearance with the metabolic and proteostasis genes in this module.

#### MAT2A

- **Related proteins** (co-abundance neighbors): GMPS (0.86), ADSS2 (0.84), PSMC2 (0.84); STRING partners: SMS (0.809)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionine adenosyltransferase 2A. The protein encoded by this gene catalyzes the production of S-adenosylmethionine (AdoMet) from methionine and ATP. AdoMet is the key methyl donor in cellular processes. [provided by RefSeq, Jun 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.545); familial thoracic aortic aneurysm and aortic dissection (0.416); autoimmune disorder of central nervous system (0.340); prostate carcinoma (0.252); Abnormality of the cardiovascular system (0.192)
- **Europe PMC papers**: 2615
- **Why important**: MAT2A occupies a central metabolic position and connects GMPS, ADSS2, and PSMC2. It produces S-adenosylmethionine, a key methyl donor, and is annotated for methyl-donor biosynthesis, oligomerization, cellular methionine response, and TORC1 regulation. It is tissue-enhanced in pancreas and cell-type enhanced in smooth muscle cells, making it especially relevant to interpreting a myometrium-associated module. It also has meaningful disease and literature annotation.
- **Conclusion**: Established conclusion: MAT2A provides a plausible metabolic and growth-regulatory anchor and is linked to the purine-related genes ADSS2 and GMPS. Hypothesis: methyl-donor availability may couple metabolic state to transcriptional or translational capacity in the shared module.

#### GMPS

- **Related proteins** (co-abundance neighbors): MAT2A (0.86), DDX6 (0.84), SF3A1 (0.83); STRING partners: ADSS2 (0.834)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: guanosine monophosphate synthase. In the de novo synthesis of purine nucleotides, IMP is the branch point metabolite at which point the pathway diverges to the synthesis of either guanine or adenine nucleotides. In the guanine nucleotide pathway, there are 2 enzymes involved in converting IMP to GMP, namely IMP dehydrogenase (IMPD1), which catalyzes the oxidation of IMP to XMP, and GMP synthetase, which catalyzes the amination of …
- **Diseases (Open Targets)**: rheumatoid arthritis (0.277); nephrotic syndrome (0.259); lupus nephritis (0.259); rhabdomyosarcoma (0.247); hepatocellular carcinoma (0.237)
- **Europe PMC papers**: 5161
- **Why important**: GMPS is positioned between MAT2A, DDX6, and SF3A1 and has a high-confidence STRING relationship with ADSS2. Its established role is GMP production in de novo purine synthesis, while its neighboring genes connect nucleotide metabolism with RNA regulation and splicing. It is tissue-enhanced in testis and cell-type enhanced across spermatogenic populations, and it has substantial literature and disease annotation.
- **Conclusion**: Established conclusion: GMPS supports a nucleotide-supply interpretation and helps connect the metabolic and RNA-processing portions of the module. Hypothesis: coordinated purine synthesis may support the RNA turnover, translation, or differentiation demands of the shared cell state.

#### EIF4G1

- **Related proteins** (co-abundance neighbors): DDX6 (0.91), SMS (0.88); STRING partners: DDX6 (0.857)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 forms a strong network connection with DDX6 and is the module's clearest translation-initiation scaffold. Its established role in the EIF4F complex links cap-dependent mRNA recruitment to the ribosome and regulation of translation. It is detected in myometrium, has low tissue specificity, and has broad disease and literature annotation, including neurodegenerative disease and Parkinson disease associations.
- **Conclusion**: Established conclusion: EIF4G1 supports a translational-control interpretation and forms a known relationship with DDX6. Hypothesis: the DDX6–EIF4G1 pair may regulate which transcripts are translated during the metabolic or stress-related state represented by the module.
