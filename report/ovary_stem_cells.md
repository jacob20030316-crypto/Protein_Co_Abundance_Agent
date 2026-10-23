# Conserved co-abundance modules: ovary and stem_cells

## Module 0

**Tissue pair**: ovary and stem_cells  
**Genes (10)**: SLC3A2, APP, AGPS, MTHFD1L, MAIP1, MRPS22, DARS2, NARS2, UBXN4, VAMP7

### Function

The module does not have a GO/KEGG term that passed global correction, so no GO/KEGG function can be claimed as statistically enriched. Its gene-level evidence instead points to a cross-compartment cellular maintenance program linking mitochondrial gene expression and protein production with vesicle trafficking, membrane transport, ether-lipid synthesis, ER quality control, and mitochondrial calcium handling. The strongest coherent signals are mitochondrial translation and aminoacyl-tRNA charging through DARS2 and NARS2, mitochondrial folate metabolism through MTHFD1L, vesicle fusion and endolysosomal trafficking through VAMP7, and amino-acid transport through SLC3A2. This is an interpretation of the gene annotations and network, not a globally significant enrichment result.

**Cell composition.** The module is not dominated by secreted proteins, plasma proteins, or immune-cell markers: only APP is annotated as secreted to blood, and most genes have low immune-cell specificity. Most genes have low tissue specificity, while all have some cell-type-enhanced annotation across diverse cell types, including oocytes, trophoblast-related cells, endothelial or epithelial populations, and other specialized cells. This broad and heterogeneous HPA pattern argues against a simple blood-cell module, although APP and the cell-type annotations mean that sample composition or shared specialized cell states could contribute. Protein detection in ovary supports expression of many module proteins there, whereas matching HPA tissue evidence is unavailable for stem_cells. The module therefore appears more consistent with a broadly distributed cellular program, potentially modulated by shared cell types, than with a plasma or blood contamination signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, between DARS2 and NARS2, supporting a connection between mitochondrial aminoacyl-tRNA synthetase functions. No STRING functional-enrichment result was reported. hu.MAP places DARS2, MTHFD1L, and NARS2 together in both (hu.MAP huMAP3_10525.1) and (hu.MAP huMAP3_13468.1), although each complex contains many additional proteins and only a subset of its members belongs to this module. These complex memberships support a mitochondrial metabolic and translation-related context, but they do not establish that all module genes form one physical complex. The abundance network is therefore substantially broader than the currently catalogued physical interaction network: VAMP7 is the central co-abundance connector, yet it has no reported STRING or hu.MAP relationship to the module genes. The network may capture coordinated activity across organelles or cell states rather than a single stable protein complex.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: DARS2–NARS2 (0.749)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10525.1 (DARS2, MTHFD1L, NARS2; 3/33); huMAP3_13468.1 (DARS2, MTHFD1L, NARS2; 3/99)

### Novelty

This module may represent a new co-abundance association, but novelty is not established by the supplied evidence alone. The limited STRING overlap and absence of hu.MAP annotation for most module genes indicate that much of the network is not already represented as a known physical interaction or complex. However, absence from those resources does not prove biological novelty, because co-abundance relationships can reflect indirect regulation, organelle coordination, shared cell composition, or incomplete database coverage. The most defensible conclusion is that the module contains a potentially novel systems-level association built around a known mitochondrial synthetase relationship and known mitochondrial complex context, requiring independent replication and experimental validation.

**Hypothesis.** Hypothesis: in ovary and stem-cell-related samples, a shared cellular state coordinates mitochondrial biosynthetic capacity with membrane and vesicle remodeling. MTHFD1L may support mitochondrial folate-dependent biosynthesis, DARS2 and NARS2 may support mitochondrial translation, and MAIP1 may connect mitochondrial protein insertion and calcium handling to this state. VAMP7 could couple the mitochondrial-associated program to vesicle fusion and endolysosomal trafficking, while SLC3A2 and AGPS could provide linked amino-acid transport and ether-lipid membrane supply. APP and UBXN4 may reflect membrane or ER trafficking and quality-control components. This should be treated as a mechanistic model generated from co-abundance and annotations, not as proof of direct regulation or physical assembly.

### Important genes

#### VAMP7

- **Related proteins** (co-abundance neighbors): NARS2 (0.85), MAIP1 (0.84), SLC3A2 (0.81), DARS2 (0.81), MTHFD1L (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vesicle associated membrane protein 7. This gene encodes a transmembrane protein that is a member of the soluble N-ethylmaleimide-sensitive factor attachment protein receptor (SNARE) family. The encoded protein localizes to late endosomes and lysosomes and is involved in the fusion of transport vesicles to their target membranes. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Jun 2010].
- **Diseases (Open Targets)**: neoplasm (0.083); gastric cancer (0.076); breast cancer (0.048); acute myeloid leukemia (0.042); hypospadias (0.039)
- **Europe PMC papers**: 1776
- **Why important**: VAMP7 is the principal network connector in the module, linking NARS2, MAIP1, SLC3A2, DARS2, and MTHFD1L through strong co-abundance edges. Its established SNARE function in vesicle fusion, endosome-to-lysosome transport, and exocytosis gives the module a plausible trafficking and membrane-remodeling axis. It also has substantial literature volume and ovarian protein detection.
- **Conclusion**: Established evidence supports VAMP7 as a vesicle and endolysosomal trafficking protein and as the central co-abundance connector. The hypothesis that it coordinates the mitochondrial and membrane-related portions of this module is plausible but not demonstrated by the available STRING or hu.MAP data.

#### MTHFD1L

- **Related proteins** (co-abundance neighbors): MRPS22 (0.86), VAMP7 (0.80), UBXN4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_10525.1, huMAP3_13468.1
- **Function (MyGene.info)**: methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 1 like. The protein encoded by this gene is involved in the synthesis of tetrahydrofolate (THF) in the mitochondrion. THF is important in the de novo synthesis of purines and thymidylate and in the regeneration of methionine from homocysteine. Several transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Jun 2011].
- **Diseases (Open Targets)**: Alzheimer disease (0.343); Abnormality of refraction (0.315); refractive error (0.312); COVID-19 (0.296); severe acute respiratory syndrome (0.295)
- **Europe PMC papers**: 1180
- **Why important**: MTHFD1L connects the network to mitochondrial one-carbon metabolism and belongs with DARS2 and NARS2 in (hu.MAP huMAP3_10525.1) and (hu.MAP huMAP3_13468.1). Its annotated role in mitochondrial tetrahydrofolate synthesis links the module to biosynthetic support for purine, thymidylate, and methionine-related metabolism. It is tissue-enhanced in blood vessel and detected in ovary, and it has disease associations involving neurological and developmental phenotypes.
- **Conclusion**: Established evidence supports MTHFD1L as a mitochondrial folate-pathway enzyme and as a member of the two hu.MAP contexts. Its role as a metabolic support node within the shared module is a reasonable interpretation, but a direct functional connection to VAMP7 or the other co-abundance edges remains hypothetical.

#### DARS2

- **Related proteins** (co-abundance neighbors): VAMP7 (0.81); STRING partners: NARS2 (0.749)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_10525.1, huMAP3_13468.1
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 2, mitochondrial. The protein encoded by this gene belongs to the class-II aminoacyl-tRNA synthetase family. It is a mitochondrial enzyme that specifically aminoacylates aspartyl-tRNA. Mutations in this gene are associated with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation (LBSL). [provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: leukoencephalopathy with brain stem and spinal cord involvement-high lactate syndrome (0.843); neurodegenerative disease (0.527); hereditary disease (0.518); hypertensive disorder (0.425); Cerebral cortical atrophy (0.425)
- **Europe PMC papers**: 796
- **Why important**: DARS2 is a mitochondrial aspartyl-tRNA synthetase, has a co-abundance connection to VAMP7, and forms the only reported high-confidence STRING pair with NARS2. It is also present in (hu.MAP huMAP3_10525.1) and (hu.MAP huMAP3_13468.1). Its established mitochondrial translation function and association with LBSL make it an important anchor for interpreting the module as involving mitochondrial protein production.
- **Conclusion**: Established evidence supports DARS2 in mitochondrial tRNA charging, mitochondrial translation, the DARS2–NARS2 STRING relationship, and the two hu.MAP contexts. The conclusion that DARS2 is a driver of the entire module is not established; it may instead be a marker of a coordinated mitochondrial state.

#### NARS2

- **Related proteins** (co-abundance neighbors): VAMP7 (0.85); STRING partners: DARS2 (0.749)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_10525.1, huMAP3_13468.1
- **Function (MyGene.info)**: asparaginyl-tRNA synthetase 2, mitochondrial. This gene encodes a putative member of the class II family of aminoacyl-tRNA synthetases. These enzymes play a critical role in protein biosynthesis by charging tRNAs with their cognate amino acids. This protein is encoded by the nuclear genome but is likely to be imported to the mitochondrion where it is thought to catalyze the ligation of asparagine to tRNA molecules. Mutations in this gene have…
- **Diseases (Open Targets)**: Combined oxidative phosphorylation defect type 24 (0.784); hearing loss, autosomal recessive (0.510); mitochondrial disease (0.501); neurodegenerative disease (0.498); DEND syndrome (0.370)
- **Europe PMC papers**: 448
- **Why important**: NARS2 provides the complementary mitochondrial aminoacyl-tRNA synthetase signal to DARS2. It is present in (hu.MAP huMAP3_10525.1) and (hu.MAP huMAP3_13468.1), has the module's reported STRING relationship with DARS2, and is associated with combined oxidative phosphorylation deficiency and other mitochondrial disease phenotypes. This combination of physical-network support and disease relevance makes it a key interpretive gene despite its limited module degree.
- **Conclusion**: Established evidence supports NARS2 as a mitochondrial asparaginyl-tRNA synthetase and as a known partner of DARS2 in STRING and hu.MAP contexts. Its participation in a broader coordinated mitochondrial translation program is supported by convergent annotations, while any role in linking that program to vesicle trafficking remains hypothetical.

#### SLC3A2

- **Related proteins** (co-abundance neighbors): APP (0.85), AGPS (0.84), VAMP7 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 3 member 2. This gene is a member of the solute carrier family and encodes a cell surface, transmembrane protein. The protein exists as the heavy chain of a heterodimer, covalently bound through di-sulfide bonds to one of several possible light chains. The encoded transporter plays a role in regulation of intracellular calcium levels and transports L-type amino acids. Alternatively spliced transcript variants…
- **Diseases (Open Targets)**: sensorineural hearing loss disorder (0.370); neurodegenerative disease (0.324); neoplasm (0.117); breast cancer (0.113); breast carcinoma (0.110)
- **Europe PMC papers**: 6815
- **Why important**: SLC3A2 is a membrane amino-acid transporter component and connects APP, AGPS, and VAMP7 in the co-abundance network. Its annotations provide a functional bridge from the vesicle-centered network to amino-acid transport and calcium regulation. It has broad tissue specificity, cell-type enhancement in several specialized populations, and a substantial literature base with disease associations.
- **Conclusion**: Established evidence supports SLC3A2 as a cell-surface transporter heavy chain involved in amino-acid transport and calcium regulation. Its position suggests that nutrient or membrane transport may accompany the module state, but the inferred coupling to mitochondrial translation and ether-lipid synthesis is a hypothesis rather than a demonstrated pathway.

## Module 1

**Tissue pair**: ovary and stem_cells  
**Genes (44)**: SLC1A5, ACADVL, ACOT9, ACSL3, ADAM10, ATP1B3, ATP5PB, CANX, CPD, C8orf82, CKAP4, ECE1, EGFR, EMC1, GALNS, GALNT2, GOLIM4, HK1, ITGA3, ITGAV, ITGB1, LACTB, LNPEP, LYRM4, MAN2A1, IGF2R, ABCC1, MYOF, NME3, PTCD3, PVR, RAB21, RAB32, RAB3D, RRBP1, RTN4, HM13, SPTLC1, STING1, SUPV3L1, AARS2, TIMM50, TMED3, TRAPPC4

### Function

This is a membrane-organelle and vesicle-trafficking module with a strong ER–Golgi–plasma-membrane axis. The primary evidence is the global enrichment of organelle membranes (GO:CC organelle membrane; q_global = 7.28e-06), organelle boundary membranes (GO:CC bounding membrane of organelle; q_global = 0.000235), organelle subcompartments (GO:CC organelle subcompartment; q_global = 0.000575), cytoplasmic and vesicle membranes (GO:CC cytoplasmic vesicle membrane; q_global = 0.00159) (GO:CC vesicle membrane; q_global = 0.00201), general membrane (GO:CC membrane; q_global = 0.0103), Golgi membrane and Golgi architecture (GO:CC Golgi membrane; q_global = 0.0112) (GO:CC Golgi stack; q_global = 0.0158) (GO:CC Golgi cisterna; q_global = 0.0188), ER membrane (GO:CC endoplasmic reticulum membrane; q_global = 0.0307) (GO:CC endoplasmic reticulum subcompartment; q_global = 0.0307), intracellular vesicles (GO:CC cytoplasmic vesicle; q_global = 0.033) (GO:CC intracellular vesicle; q_global = 0.0338), the ER–nuclear outer-membrane network (GO:CC nuclear outer membrane-endoplasmic reticulum membrane network; q_global = 0.036), and membrane protein complexes (GO:CC membrane protein complex; q_global = 0.0404). The module also contains cell-surface receptors and transport-related signaling components (6 globally significant GO/KEGG terms, q_global 0.0247–0.0492; see the table). Taken together, the most defensible interpretation is coordinated membrane protein maturation, sorting, trafficking, recycling, adhesion, and signaling, rather than a narrowly defined biochemical pathway. Supporting annotations include Golgi cargo processing by GOLIM4 and MAN2A1, ER folding and quality control by CANX and EMC1, ER-to-Golgi transport by TMED3 and TRAPPC4, vesicle regulation by RAB21 and RAB3D, and cell-surface adhesion or signaling through EGFR, ITGA3, ITGAV, and ITGB1. Mitochondrial, lipid, amino-acid, and innate-immune genes indicate additional links to cellular energy, membrane composition, nutrient handling, and stress response, but these are secondary interpretations rather than the central module function.

**Cell composition.** The module is not predominantly composed of plasma proteins or secreted proteins. HPA indicates low tissue specificity for most genes, with broad protein detection in ovary, and only a minority classified as secreted. Thus, the shared ovary–stem-cell signal is unlikely to be explained simply by a plasma-protein program. However, the module is not a clean lineage-specific program: many genes are cell-type enhanced, including genes associated with neutrophils and other immune cells, as well as epithelial, placental, reproductive, and podocyte populations. The repeated neutrophil and immune-cell associations create a plausible sample-composition or shared-cell-type contribution, especially for genes such as RAB3D, CPD, ECE1, IGF2R, and ADAM10. This should be tested using cell-composition estimates and independent single-cell or spatial data. HPA supports ovary protein detection for most of the module, but the stem-cell comparison lacks a matching HPA tissue entry, so equivalent protein-level support in stem cells cannot be inferred.

**GO/KEGG enrichment**: 21 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC organelle membrane | 7.28e-06 | ACADVL, ACSL3, ADAM10, ATP5PB, CANX, CKAP4, ECE1, EGFR, EMC1, GALNT2, GOLIM4, HK1, HM13, IGF2R, ITGAV, ITGB1, LNPEP, MAN2A1, MYOF, NME3, PTCD3, RAB21, RAB32, RAB3D, RRBP1, RTN4, SPTLC1, STING1, TIMM50, TMED3, TRAPPC4 |
| GO:CC bounding membrane of organelle | 0.000235 | ACSL3, ADAM10, CANX, CKAP4, ECE1, EGFR, GALNT2, GOLIM4, HK1, IGF2R, ITGAV, ITGB1, LNPEP, MAN2A1, MYOF, NME3, RAB21, RAB32, RAB3D, STING1, TMED3, TRAPPC4 |
| GO:CC organelle subcompartment | 0.000575 | ACSL3, CANX, CKAP4, EGFR, EMC1, GALNT2, GOLIM4, HM13, IGF2R, MAN2A1, RAB21, RAB32, RRBP1, RTN4, SPTLC1, STING1, TMED3, TRAPPC4 |
| GO:CC cytoplasmic vesicle membrane | 0.00159 | ADAM10, CANX, CKAP4, ECE1, EGFR, GOLIM4, IGF2R, ITGAV, ITGB1, LNPEP, MYOF, RAB21, RAB32, RAB3D, STING1, TMED3 |
| GO:CC vesicle membrane | 0.00201 | ADAM10, CANX, CKAP4, ECE1, EGFR, GOLIM4, IGF2R, ITGAV, ITGB1, LNPEP, MYOF, RAB21, RAB32, RAB3D, STING1, TMED3 |
| GO:CC membrane | 0.0103 | ABCC1, ACADVL, ACSL3, ADAM10, ATP1B3, ATP5PB, CANX, CKAP4, CPD, ECE1, EGFR, EMC1, GALNT2, GOLIM4, HK1, HM13, IGF2R, ITGA3, ITGAV, ITGB1, LNPEP, MAN2A1, MYOF, NME3, PTCD3, PVR, RAB21, RAB32, RAB3D, RRBP1, RTN4, SLC1A5, SPTLC1, STING1, TIMM50, TMED3, TRAPPC4 |
| GO:CC Golgi membrane | 0.0112 | ADAM10, EGFR, GALNT2, GOLIM4, IGF2R, MAN2A1, RAB21, STING1, TMED3, TRAPPC4 |
| GO:CC Golgi stack | 0.0158 | GALNT2, GOLIM4, MAN2A1, RAB21, TMED3, TRAPPC4 |
| GO:CC Golgi cisterna | 0.0188 | GALNT2, GOLIM4, MAN2A1, RAB21, TMED3 |
| GO:MF signaling receptor activity | 0.0247 | EGFR, IGF2R, ITGAV, ITGB1, PVR, RRBP1, SLC1A5 |
| GO:MF molecular transducer activity | 0.0247 | EGFR, IGF2R, ITGAV, ITGB1, PVR, RRBP1, SLC1A5 |
| GO:CC cell surface | 0.0275 | ADAM10, ECE1, EGFR, HM13, IGF2R, ITGA3, ITGAV, ITGB1, PVR |
| GO:CC endoplasmic reticulum membrane | 0.0307 | ACSL3, CANX, CKAP4, EGFR, EMC1, GALNT2, HM13, RAB21, RRBP1, RTN4, SPTLC1, STING1, TMED3 |
| GO:CC endoplasmic reticulum subcompartment | 0.0307 | ACSL3, CANX, CKAP4, EGFR, EMC1, GALNT2, HM13, RAB21, RRBP1, RTN4, SPTLC1, STING1, TMED3 |
| GO:CC cytoplasmic vesicle | 0.033 | ADAM10, ATP1B3, CANX, CKAP4, ECE1, EGFR, GALNS, GOLIM4, IGF2R, ITGAV, ITGB1, LNPEP, MYOF, RAB21, RAB32, RAB3D, SLC1A5, STING1, TMED3, TRAPPC4 |

### STRING and hu.MAP

STRING provides a small set of high-confidence pairwise relationships rather than a densely connected physical interaction network. The strongest established relationships include the integrin and receptor cluster EGFR–ITGB1, ITGA3–ITGB1, ITGAV–ITGB1, and ITGA3–ITGAV, together with ITGB1–RAB21; CANX–EMC1 links ER quality control; and CPD–IGF2R links peptide processing with receptor or lysosomal trafficking. These interactions support the biological interpretation of an adhesion, receptor, and membrane-trafficking axis, but they do not establish that every co-abundance edge is a direct physical interaction. STRING functional terms (15 supplementary STRING terms; within-query FDR 6.28e-12–0.00039) strongly support membrane, transmembrane, organelle-membrane, glycoprotein, and cell-surface composition, but they remain supplementary and are not global enrichment evidence. hu.MAP independently supports several coherent subassemblies: ADAM10, IGF2R, GALNS, ECE1, and MAN2A1 occur in lysosomal or glycan-processing complexes (hu.MAP huMAP3_06775.1) (hu.MAP huMAP3_09327.1) (hu.MAP huMAP3_08802.1); ITGB1, ITGA3, and LNPEP recur in adhesion or cell-surface complexes (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1) (hu.MAP huMAP3_06815.1) (hu.MAP huMAP3_08103.1) (hu.MAP huMAP3_09105.1) (hu.MAP huMAP3_08689.1); GOLIM4, CKAP4, and MYOF occur in membrane-associated complexes (hu.MAP huMAP3_10725.1) (hu.MAP huMAP3_09822.1); ACSL3, ABCC1, and HM13 occur in ER or membrane complexes (hu.MAP huMAP3_06247.1) (hu.MAP huMAP3_09592.1) (hu.MAP huMAP3_08167.1); HK1 and NME3 form a small metabolic complex (hu.MAP huMAP3_08804.1); and RAB3D with STING1 occurs in (hu.MAP huMAP3_11660.1). The partial membership of these complexes suggests that the module combines several related membrane systems rather than representing one canonical complex.

**STRING interactions (score >= 0.7)**: 7 of 946 gene pairs: CANX–EMC1 (0.854); CPD–IGF2R (0.738); EGFR–ITGB1 (0.966); ITGA3–ITGAV (0.968); ITGA3–ITGB1 (0.999); ITGAV–ITGB1 (0.999); ITGB1–RAB21 (0.815)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transmembrane helix (FDR = 6.28e-12, 27 genes); Component Integral component of membrane (FDR = 7.44e-10, 29 genes); Keyword Membrane (FDR = 6.03e-08, 33 genes); COMPARTMENTS Intrinsic component of membrane (FDR = 1.63e-07, 18 genes); COMPARTMENTS Integral component of membrane (FDR = 3.07e-07, 17 genes); Component Organelle membrane (FDR = 1.04e-06, 30 genes); Keyword Glycoprotein (FDR = 2.48e-06, 18 genes); COMPARTMENTS Organelle membrane (FDR = 4.56e-06, 25 genes); Keyword Signal-anchor (FDR = 5.64e-06, 9 genes); Keyword Cell membrane (FDR = 8.61e-06, 18 genes); Component Organelle subcompartment (FDR = 3.76e-05, 18 genes); COMPARTMENTS Membrane (FDR = 5.26e-05, 30 genes); Component Integral component of plasma membrane (FDR = 0.00023, 10 genes); COMPARTMENTS Cell surface (FDR = 0.00039, 9 genes); COMPARTMENTS Organelle subcompartment (FDR = 0.00039, 13 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (ADAM10, IGF2R, GALNS, ECE1, MAN2A1; 5/60); huMAP3_09327.1 (ADAM10, GALNS, ECE1, MAN2A1; 4/93); huMAP3_10503.1 (ITGB1, ITGA3, LNPEP; 3/27); huMAP3_10980.1 (ITGB1, ITGA3, LNPEP; 3/44); huMAP3_09336.1 (ITGB1, ITGA3, LNPEP; 3/50); huMAP3_10725.1 (GOLIM4, CKAP4, MYOF; 3/59); huMAP3_06247.1 (ATP5PB, ABCC1, HM13; 3/65); huMAP3_09592.1 (ACSL3, ABCC1, HM13; 3/95); huMAP3_08804.1 (HK1, NME3; 2/3); huMAP3_06815.1 (ITGB1, ITGA3; 2/5); huMAP3_08103.1 (ITGA3, LNPEP; 2/23); huMAP3_08167.1 (ACSL3, HM13; 2/24); huMAP3_09105.1 (ITGA3, LNPEP; 2/24); huMAP3_09822.1 (GOLIM4, CKAP4; 2/28); huMAP3_06791.1 (ABCC1, ATP1B3; 2/31); huMAP3_08802.1 (ECE1, MAN2A1; 2/33); huMAP3_08689.1 (ITGA3, LNPEP; 2/37); huMAP3_11660.1 (RAB3D, STING1; 2/43)

### Novelty

The data do not justify calling this module a wholly new molecular mechanism. Its central features—integrin adhesion, EGFR signaling, ER quality control, Golgi processing, vesicle transport, and lysosomal targeting—are already well established by STRING, hu.MAP, curated gene functions, and extensive literature. At the same time, the specific conserved co-abundance organization across ovary and stem_cells may be a useful systems-level observation, particularly because the module brings together membrane trafficking, adhesion, glycosylation, metabolism, and innate-immune components. The absence of some module edges from STRING or hu.MAP is not evidence of novelty: co-abundance can reflect shared regulation, cell composition, or indirect functional coupling. A novelty claim would require comparison with published ovary–stem-cell co-expression modules, replication in independent cohorts, preservation testing, and perturbation or spatial validation.

**Hypothesis.** Hypothesis: in both ovary and stem-cell contexts, a shared cellular state coordinates ER membrane-protein insertion and quality control with Golgi glycan processing, vesicle trafficking, integrin recycling, and receptor signaling. GOLIM4, MAN2A1, TMED3, CANX, and EMC1 could support the production and routing of properly folded and glycosylated membrane proteins; RAB21 and TRAPPC4 could direct their intracellular movement; and the ITGA3–ITGB1, ITGAV–ITGB1, and EGFR systems could convert extracellular or matrix contacts into adhesion and growth signals. ACSL3, SPTLC1, ATP1B3, SLC1A5, and mitochondrial genes may adapt membrane lipid composition, nutrient flux, and energy supply, while STING1 and the immune-associated HPA pattern may reflect stress or inflammatory modulation. This model predicts coordinated changes in surface receptor abundance, integrin recycling, Golgi glycosylation, and vesicle flux; it remains a hypothesis because co-abundance alone cannot establish direction, direct interaction, or causality.

### Important genes

#### ITGB1

- **Related proteins** (co-abundance neighbors): ATP1B3 (0.85), LYRM4 (0.85), RRBP1 (0.83), ABCC1 (0.83), SPTLC1 (0.82), ACSL3 (0.82), ITGAV (0.82), MAN2A1 (0.82), ITGA3 (0.81); STRING partners: EGFR (0.966), ITGA3 (0.999), ITGAV (0.999), RAB21 (0.815)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_10503.1, huMAP3_10980.1, huMAP3_09336.1, huMAP3_06815.1
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is one of the principal network hubs and is connected to the strongest STRING relationships in the module, including EGFR, ITGA3, ITGAV, and RAB21. It is present in many primary membrane, cell-surface, receptor, and adhesion terms (14 globally significant GO/KEGG terms, q_global 7.28e-06–0.0492; see the table), and recurs in several hu.MAP adhesion complexes (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1) (hu.MAP huMAP3_06815.1). HPA places it at the plasma membrane and focal adhesion sites. Its extensive literature and disease associations make it the clearest integrator of extracellular matrix adhesion, receptor signaling, and trafficking in this module.
- **Conclusion**: Established: ITGB1 is a central adhesion and membrane-signaling component with direct database-supported relationships to other module genes. Hypothesis: its coordinated abundance may organize the functional output of the module by linking intracellular trafficking to matrix attachment and growth signaling.

#### ITGA3

- **Related proteins** (co-abundance neighbors): GOLIM4 (0.89), LYRM4 (0.87), ABCC1 (0.85), ADAM10 (0.84), GALNT2 (0.84), MAN2A1 (0.83), RRBP1 (0.81), ITGB1 (0.81); STRING partners: ITGAV (0.968), ITGB1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_10503.1, huMAP3_10980.1, huMAP3_09336.1, huMAP3_06815.1, huMAP3_08103.1, huMAP3_09105.1, huMAP3_08689.1
- **Function (MyGene.info)**: integrin subunit alpha 3. The gene encodes a member of the integrin alpha chain family of proteins. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain that function as cell surface adhesion molecules. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha 3 subunit. This subunit joins with a beta 1 subunit to form an …
- **Diseases (Open Targets)**: epidermolysis bullosa, junctional 7, with interstitial lung disease and nephrotic syndrome (0.807); neurodegenerative disease (0.503); junctional epidermolysis bullosa (0.372); junctional epidermolysis bullosa Herlitz type (0.370); epidermolysis bullosa simplex 4, localized or generalized intermediate, autosomal recessive (0.370)
- **Europe PMC papers**: 4167
- **Why important**: ITGA3 has high network connectivity and links GOLIM4, ADAM10, GALNT2, MAN2A1, RRBP1, and ITGB1. It forms established STRING relationships with ITGAV and ITGB1 and appears repeatedly in hu.MAP cell-surface and adhesion complexes (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1) (hu.MAP huMAP3_06815.1) (hu.MAP huMAP3_08103.1) (hu.MAP huMAP3_09105.1) (hu.MAP huMAP3_08689.1). Its annotated function as an alpha integrin subunit that pairs with ITGB1 and interacts with laminin-family extracellular-matrix proteins gives the module a concrete adhesion mechanism. Its disease associations and substantial literature further support its importance.
- **Conclusion**: Established: ITGA3 is a cell-surface matrix-adhesion receptor component that is physically or functionally connected to the module integrin cluster. Hypothesis: ITGA3–ITGB1 may be a principal surface-output arm through which the conserved module influences stem-cell or ovarian cell attachment and state.

#### EGFR

- **Related proteins** (co-abundance neighbors): MAN2A1 (0.91), ACSL3 (0.86), MYOF (0.83); STRING partners: ITGB1 (0.966)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus, Plasma membrane; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: epidermal growth factor receptor. The protein encoded by this gene is a transmembrane glycoprotein that is a member of the protein kinase superfamily. This protein is a receptor for members of the epidermal growth factor family. EGFR is a cell surface protein that binds to epidermal growth factor, thus inducing receptor dimerization and tyrosine autophosphorylation leading to cell proliferation. Mutations in this gene are associat…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.850); lung adenocarcinoma (0.774); cancer (0.737); head and neck squamous cell carcinoma (0.725); lung cancer (0.717)
- **Europe PMC papers**: 223694
- **Why important**: EGFR is represented across nearly all primary enrichment themes, including organelle membranes, Golgi, ER, vesicles, cell surface, receptor activity, and signaling (21 globally significant GO/KEGG terms, q_global 7.28e-06–0.0492; see the table). It has a strong STRING relationship with ITGB1 and a high network connection to MAN2A1, ACSL3, and MYOF. HPA places it at the plasma membrane and Golgi and identifies placenta- and trophoblast-related cell-type patterns. EGFR has exceptionally extensive literature and well-established disease relevance, making it a strong signaling anchor even though its network degree is not among the highest.
- **Conclusion**: Established: EGFR is a receptor tyrosine kinase whose trafficking and signaling are consistent with the module's membrane and receptor enrichment. Hypothesis: the module may coordinate EGFR maturation, routing, and integrin-associated signaling rather than merely reflecting independent EGFR expression.

#### GOLIM4

- **Related proteins** (co-abundance neighbors): GALNT2 (0.90), ITGA3 (0.89), LYRM4 (0.86), AARS2 (0.85), MAN2A1 (0.85), MYOF (0.85), ITGAV (0.83), LNPEP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_10725.1, huMAP3_09822.1
- **Function (MyGene.info)**: golgi integral membrane protein 4. The Golgi complex plays a key role in the sorting and modification of proteins exported from the endoplasmic reticulum. The protein encoded by this gene is a type II Golgi-resident protein. It may process proteins synthesized in the rough endoplasmic reticulum and assist in the transport of protein cargo through the Golgi apparatus. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.397); mathematical ability (0.328); head injury (0.300); cholelithiasis (0.299); proliferative diabetic retinopathy (0.284)
- **Europe PMC papers**: 294
- **Why important**: GOLIM4 is a high-connectivity module gene and occupies a central position between Golgi-associated genes, integrins, MYOF, and LNPEP. It is included in the primary organelle, vesicle, Golgi, and intracellular-transport evidence (11 globally significant GO/KEGG terms, q_global 7.28e-06–0.0338; see the table) and has a Golgi localization in HPA. It also appears in hu.MAP membrane-associated complexes (hu.MAP huMAP3_10725.1) (hu.MAP huMAP3_09822.1). Its annotated role as a Golgi-resident protein involved in sorting and modifying ER-derived cargo gives it mechanistic relevance, while its more modest literature volume compared with EGFR or ITGB1 leaves room for a module-specific insight.
- **Conclusion**: Established: GOLIM4 is a Golgi-resident trafficking component aligned with the strongest cellular-compartment signal in the module. Hypothesis: it may help couple Golgi cargo processing to delivery of integrins and receptors that define the module's surface phenotype.

#### RAB21

- **Related proteins** (co-abundance neighbors): RAB3D (0.89), LYRM4 (0.84), C8orf82 (0.83), RAB32 (0.80); STRING partners: ITGB1 (0.815)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB21, member RAS oncogene family. This gene belongs to the Rab family of monomeric GTPases, which are involved in the control of cellular membrane traffic. The encoded protein plays a role in the targeted trafficking of integrins via its association with integrin alpha tails. As a consequence, the encoded protein is involved in the regulation of cell adhesion and migration. Expression of this gene is associated with a poor prognos…
- **Diseases (Open Targets)**: neurodegenerative disease (0.469); small intestine neuroendocrine neoplasm (0.095); neoplasm (0.085); posterior cortical atrophy (0.074); nonpapillary renal cell carcinoma (0.065)
- **Europe PMC papers**: 999
- **Why important**: RAB21 connects membrane-trafficking genes within the module and has an established STRING relationship with ITGB1. It is included in a broad set of primary organelle, Golgi, vesicle, and membrane terms (15 globally significant GO/KEGG terms, q_global 7.28e-06–0.0466; see the table). Its annotated role in targeted integrin trafficking, receptor-mediated endocytosis, exocytosis, and cell adhesion makes it particularly informative for linking the intracellular and cell-surface portions of the module. HPA also associates it with spermatid and neutrophil cell types, which is relevant to the mixed cellular-context caution.
- **Conclusion**: Established: RAB21 is a membrane-trafficking regulator connected to integrin handling and represented in the module's vesicle evidence. Hypothesis: altered RAB21-dependent recycling could be the dynamic step that converts the conserved co-abundance program into changes in adhesion or receptor responsiveness.

## Module 2

**Tissue pair**: ovary and stem_cells  
**Genes (23)**: ABHD10, ADPGK, CRAT, ALCAM, CD47, CD9, CPT2, DECR1, FAM3C, HIBCH, L1CAM, NAA25, NCSTN, PON2, PITRM1, UQCRC1, RHOG, SEC22B, SCO1, STX7, IARS2, TIMMDC1, VTI1A

### Function

No GO/KEGG term passed global correction, so the module does not support a formally significant pathway assignment. Its biological interpretation is instead a mixed membrane-trafficking, cell-adhesion, and mitochondrial-metabolic program. The supplementary STRING terms point toward membrane and transmembrane proteins, disulfide-bonded proteins, mitochondria, and mitochondrial targeting (6 supplementary STRING terms; within-query FDR 0.0125–0.0368). The network contains a vesicle-trafficking component centered on SEC22B, STX7, and VTI1A, a membrane-adhesion component involving ALCAM, CD9, L1CAM, and CD47, and a mitochondrial metabolism component involving SCO1, CPT2, CRAT, DECR1, HIBCH, IARS2, PITRM1, TIMMDC1, and UQCRC1. This is best viewed as a coordinated cellular-compartment or cell-state signal rather than evidence for a single canonical pathway.

**Cell composition.** The module is not dominated by secreted proteins: only a minority are annotated as secreted or secreted to blood, including PON2, ALCAM, and FAM3C, while CD9 is intracellular and membrane-associated. Most genes have low tissue specificity, and the HPA data show broad or heterogeneous cell-type enhancement rather than a uniform tissue signature. Immune-cell specificity is low for most genes, although several genes are enhanced in neutrophils, myeloid cells, B cells, or other blood-related populations. Therefore, a blood-cell contribution is possible but is not established as the main explanation. The strong ovary protein detection for most measured genes supports relevance to ovary, whereas there is no matching HPA tissue for stem_cells. The shared module may consequently reflect a broadly expressed cellular program, a shared cell type, or sample-composition effects rather than an ovary- and stem-cell-specific mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides six high-confidence pairwise relationships. ALCAM connects with L1CAM and CD9, CD47 connects with CD9, and SEC22B, STX7, and VTI1A form a strongly supported vesicle-trafficking interaction cluster. These relationships show that parts of the co-abundance module correspond to already known protein associations, especially membrane adhesion and vesicle fusion. hu.MAP independently supports a mitochondrial/metabolic grouping containing CPT2, CRAT, and IARS2 (hu.MAP huMAP3_13468.1) (hu.MAP huMAP3_10525.1), and several vesicle-trafficking complexes containing STX7 and VTI1A (hu.MAP huMAP3_06458.1) (hu.MAP huMAP3_08929.1) (hu.MAP huMAP3_10587.1) (hu.MAP huMAP3_13160.1). However, most module genes have no listed STRING partner or hu.MAP complex membership. Thus, the databases validate local submodules and biological themes, but not the entire co-abundance architecture as one established physical complex.

**STRING interactions (score >= 0.7)**: 6 of 253 gene pairs: ALCAM–CD9 (0.767); ALCAM–L1CAM (0.979); CD47–CD9 (0.736); SEC22B–STX7 (0.962); SEC22B–VTI1A (0.974); STX7–VTI1A (0.996)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Disulfide bond (FDR = 0.0125, 9 genes); Component Integral component of membrane (FDR = 0.0183, 13 genes); Keyword Membrane (FDR = 0.0368, 15 genes); Keyword Mitochondrion (FDR = 0.0368, 10 genes); Keyword Transit peptide (FDR = 0.0368, 8 genes); Keyword Transmembrane (FDR = 0.0368, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (CPT2, CRAT, IARS2; 3/99); huMAP3_10525.1 (CRAT, IARS2; 2/33); huMAP3_06458.1 (STX7, VTI1A; 2/41); huMAP3_08929.1 (STX7, VTI1A; 2/44); huMAP3_10587.1 (STX7, VTI1A; 2/45); huMAP3_13160.1 (STX7, VTI1A; 2/49)

### Novelty

The module should not be called a completely new biological mechanism. Several of its relationships and component functions are already known from STRING, hu.MAP, and gene-specific literature, including SNARE-mediated trafficking, cell adhesion, mitochondrial respiration, fatty-acid oxidation, and mitochondrial translation. At the same time, the particular cross-compartment co-abundance arrangement is not directly reproduced by the listed complexes or STRING edges. It may therefore represent a potentially novel expression-level module or shared cell-state signature, but this remains provisional. Absence of an interaction from STRING or hu.MAP cannot establish novelty, and the lack of globally significant GO/KEGG enrichment further argues for cautious interpretation.

**Hypothesis.** Hypothesis: the shared ovary and stem-cell module reflects a cell state that couples mitochondrial energetic and proteostatic capacity with membrane remodeling and vesicle trafficking. Mitochondrial fatty-acid and branched-chain-amino-acid metabolism, respiratory-chain assembly, mitochondrial translation, and peptide processing may support the energetic demands of cells undergoing adhesion, differentiation, or remodeling. In parallel, SEC22B-STX7-VTI1A trafficking and the ALCAM-CD9-L1CAM-CD47 membrane network may regulate delivery, recycling, adhesion, and intercellular signaling. A further hypothesis is that the observed co-abundance partly reflects shared cell populations or sample composition, including a possible contribution from immune or trophoblast-like cell states; this must be tested with cell-resolved expression and independent cohorts.

### Important genes

#### SEC22B

- **Related proteins** (co-abundance neighbors): TIMMDC1 (0.85), NCSTN (0.81), ABHD10 (0.81), STX7 (0.80); STRING partners: STX7 (0.962), VTI1A (0.974)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC22 homolog B, vesicle trafficking protein. The protein encoded by this gene is a member of the SEC22 family of vesicle trafficking proteins. It seems to complex with SNARE and it is thought to play a role in the ER-Golgi protein trafficking. This protein has strong similarity to Mus musculus and Cricetulus griseus proteins.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: inflammatory bowel disease (0.285); luminal A breast carcinoma (0.271); colitis (0.238); enteritis (0.238); Crohn disease (0.233)
- **Europe PMC papers**: 1006
- **Why important**: SEC22B is a relatively central node in the module and connects to TIMMDC1, NCSTN, ABHD10, and STX7. It has direct STRING support with STX7 and VTI1A and is annotated for ER-Golgi transport, retrograde transport, vesicle fusion, and autophagy (STRING Component Integral component of membrane; within-query FDR = 0.0183) (STRING Keyword Membrane; within-query FDR = 0.0368), (STRING Keyword Transmembrane; within-query FDR = 0.0368). Its HPA profile is broadly expressed but shows neutrophil enhancement, making it a useful marker of both intracellular trafficking and possible cell-state composition. Its literature is substantial.
- **Conclusion**: Established evidence supports SEC22B as a vesicle-trafficking component and as part of a known SEC22B-STX7-VTI1A interaction cluster. It is a strong anchor for the trafficking interpretation. It is not established that SEC22B mechanistically drives the entire shared module; that causal role remains a hypothesis.

#### STX7

- **Related proteins** (co-abundance neighbors): SEC22B (0.80); STRING partners: SEC22B (0.962), VTI1A (0.996)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Lysosomes; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06458.1, huMAP3_08929.1, huMAP3_10587.1, huMAP3_13160.1
- **Function (MyGene.info)**: syntaxin 7. The protein encoded by this gene is a syntaxin family membrane receptor involved in vesicle transport. The encoded protein binds alpha-SNAP, an important regulator of transport vesicle fusion. Along with syntaxin 13, this protein plays a role in the ordered fusion of endosomes and lysosomes with the phagosome. [provided by RefSeq, May 2016].
- **Diseases (Open Targets)**: neurodegenerative disease (0.489); Abnormality of neuronal migration (0.259); Raynaud disease (0.180); placental abruption (0.166); aortic stenosis (0.081)
- **Europe PMC papers**: 701
- **Why important**: STX7 is directly connected to SEC22B in STRING and belongs with VTI1A in multiple hu.MAP trafficking complexes (hu.MAP huMAP3_06458.1) (hu.MAP huMAP3_08929.1) (hu.MAP huMAP3_10587.1) (hu.MAP huMAP3_13160.1). It is a lysosomal syntaxin involved in vesicle transport, vesicle fusion, and ordered fusion of endosomes and lysosomes with phagosomes. Its HPA profile shows enhancement in several immune and myeloid cell types, including neutrophils, which makes it informative for distinguishing a trafficking program from possible immune-cell admixture.
- **Conclusion**: Established evidence supports STX7 as a membrane-fusion and endolysosomal trafficking protein with independently recognized complex membership. Its presence strengthens the trafficking interpretation, but the module does not prove that the signal is immune-cell driven or that STX7 mediates communication between the mitochondrial and membrane submodules.

#### SCO1

- **Related proteins** (co-abundance neighbors): CD9 (0.86), L1CAM (0.86), ABHD10 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: synthesis of cytochrome C oxidase 1. Mammalian cytochrome c oxidase (COX) catalyzes the transfer of reducing equivalents from cytochrome c to molecular oxygen and pumps protons across the inner mitochondrial membrane. In yeast, 2 related COX assembly genes, SCO1 and SCO2 (synthesis of cytochrome c oxidase), enable subunits 1 and 2 to be incorporated into the holoprotein. This gene is the human homolog to the yeast SCO1 gene. [provide…
- **Diseases (Open Targets)**: mitochondrial complex IV deficiency, nuclear type 4 (0.782); leigh syndrome due to mitochondrial complex iv deficiency (0.583); mitochondrial complex IV deficiency, nuclear-type (0.543); neurodegenerative disease (0.484); mitochondrial disease (0.372)
- **Europe PMC papers**: 1293
- **Why important**: SCO1 has comparatively strong network connectivity and links to ABHD10, CD9, and L1CAM. It is a mitochondrial cytochrome-c-oxidase assembly factor involved in respiratory-chain complex IV assembly and copper homeostasis. It participates in the broad STRING mitochondrial and membrane keyword sets (6 supplementary STRING terms; within-query FDR 0.0125–0.0368), and its disease associations prominently include mitochondrial complex IV deficiency and related mitochondrial disease. Its substantial literature makes its function well established.
- **Conclusion**: Established evidence identifies SCO1 as a mitochondrial respiratory-chain assembly gene, and its network position connects the mitochondrial and membrane-associated portions of the module. The data support SCO1 as an important metabolic anchor, but do not establish that altered SCO1 activity causes the co-abundance pattern.

#### CPT2

- **Related proteins** (co-abundance neighbors): CRAT (0.87), NCSTN (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: carnitine palmitoyltransferase 2. The protein encoded by this gene is a nuclear protein which is transported to the mitochondrial inner membrane. Together with carnitine palmitoyltransferase I, the encoded protein oxidizes long-chain fatty acids in the mitochondria. Defects in this gene are associated with mitochondrial long-chain fatty-acid (LCFA) oxidation disorders. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: carnitine palmitoyl transferase II deficiency, myopathic form (0.830); carnitine palmitoyl transferase II deficiency, severe infantile form (0.800); carnitine palmitoyl transferase II deficiency, neonatal form (0.772); carnitine palmitoyltransferase II deficiency (0.710); hereditary disease (0.505)
- **Europe PMC papers**: 5133
- **Why important**: CPT2 is connected to CRAT and NCSTN and is a member of the mitochondrial hu.MAP metabolic complexes (hu.MAP huMAP3_13468.1). It is a central enzyme of the carnitine shuttle and long-chain fatty-acid oxidation, with well-established associations to CPT2 deficiency and related hereditary disease. Its inclusion helps define the module's mitochondrial lipid-energy component, even though its HPA protein signal was not detected in ovary.
- **Conclusion**: Established evidence supports CPT2 as a mitochondrial fatty-acid oxidation enzyme and as part of known metabolic complexes. Its co-abundance with CRAT and other mitochondrial genes is consistent with shared metabolic regulation. The module does not demonstrate that fatty-acid oxidation is globally enriched or that CPT2 has a special ovary-stem-cell-specific function.

#### CD9

- **Related proteins** (co-abundance neighbors): SCO1 (0.86), CD47 (0.83); STRING partners: ALCAM (0.767), CD47 (0.736)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD9 molecule. This gene encodes a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Tetraspanins are cell surface glycoproteins with four transmembrane domains that form multimeric complexes with other cell surface proteins. The encoded protein functions in many cellular processes including differentiation, adhesion, and signal transduction, and expression of this gene plays a cri…
- **Diseases (Open Targets)**: diphtheria (0.527); breast cancer (0.348); poisoning (0.136); response to xenobiotic stimulus (0.136); rheumatic disorder (0.122)
- **Europe PMC papers**: 23911
- **Why important**: CD9 is a plasma-membrane tetraspanin involved in adhesion, fusion, differentiation, and signal transduction. It connects to SCO1 and CD47 in the module and has STRING relationships with ALCAM and CD47 (STRING Keyword Disulfide bond; within-query FDR = 0.0125) (STRING Component Integral component of membrane; within-query FDR = 0.0183) (STRING Keyword Membrane; within-query FDR = 0.0368), (STRING Keyword Transmembrane; within-query FDR = 0.0368). Its extensive literature and known role in cell-surface multiprotein assemblies make it an informative representative of the membrane-adhesion portion of the network. HPA detects it in ovary and shows enrichment in several epithelial and blood-cell populations.
- **Conclusion**: Established evidence supports CD9 as a membrane-organizing and adhesion-associated protein that can connect cell-surface components. It plausibly explains part of the membrane signal and may contribute to cell-composition sensitivity. It is not established that CD9 links the mitochondrial genes physically; that connection is inferred from co-abundance and network structure.

#### ALCAM

- **Related proteins** (co-abundance neighbors): PON2 (0.83); STRING partners: CD9 (0.767), L1CAM (0.979)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: activated leukocyte cell adhesion molecule. This gene encodes activated leukocyte cell adhesion molecule (ALCAM), also known as CD166 (cluster of differentiation 166), which is a member of a subfamily of immunoglobulin receptors with five immunoglobulin-like domains (VVC2C2C2) in the extracellular domain. This protein binds to T-cell differentiation antigene CD6, and is implicated in the processes of cell adhesion and migration. Multiple al…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.458); mathematical ability (0.453); open-angle glaucoma (0.396); restless legs syndrome (0.379); ovarian dysfunction (0.362)
- **Europe PMC papers**: 4212
- **Why important**: ALCAM is a cell-adhesion molecule with a high-confidence STRING relationship to L1CAM and a further relationship to CD9 (STRING Keyword Disulfide bond; within-query FDR = 0.0125) (STRING Component Integral component of membrane; within-query FDR = 0.0183) (STRING Keyword Membrane; within-query FDR = 0.0368), (STRING Keyword Transmembrane; within-query FDR = 0.0368). It is annotated for heterophilic cell-cell adhesion, migration, and signaling, is enriched in parathyroid tissue, and shows enhancement in several epithelial and myeloid cell types. Its ovary protein detection and substantial literature make it relevant to a possible adhesion or shared-cell-state interpretation.
- **Conclusion**: Established evidence supports ALCAM as a cell-adhesion and migration protein embedded in a known membrane interaction neighborhood. It is an important marker of the module's surface-interaction component. Its association with the mitochondrial submodule is a co-abundance-based hypothesis, not a demonstrated physical or causal interaction.

## Module 3

**Tissue pair**: ovary and stem_cells  
**Genes (16)**: ACIN1, CXXC1, DYNC1I2, JPT2, PSMC4, PSMD13, CAD, CRYZL1, RCN2, POLR2H, SUPT16H, TP53BP1, YBX3, ZMYND8, TJP1, TJP2

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established single pathway-level annotation. Its structure instead suggests a composite cellular-state module. The strongest coherent feature is a cell-junction and barrier-associated subnetwork centered on TJP1, TJP2, and YBX3, supported by STRING terms (STRING NetworkNeighborAL Claudin, and Maintenance of blood-brain barrier; within-query FDR = 0.0182) and interactions between these genes. A second feature is proteostasis, represented by PSMC4 and PSMD13 and supported by STRING interaction evidence and hu.MAP complexes (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1). Other connected components involve pyrimidine biosynthesis through CAD, transcription and chromatin regulation through SUPT16H, POLR2H, CXXC1, and ZMYND8, intracellular transport through DYNC1I2, and DNA-damage response through TP53BP1. The most defensible interpretation is therefore a shared ovary–stem-cell state involving epithelial or cellular junction organization together with proliferation-associated biosynthesis, protein quality control, genome maintenance, and transcriptional regulation. The junction and apoptosis annotations from STRING are supplementary evidence only and are not globally corrected module-level enrichment results.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only limited secretome representation, and the listed proteins are predominantly intracellular, nuclear, cytosolic, membrane-associated, or junctional. Most genes have low tissue specificity, consistent with broadly expressed cellular machinery rather than a narrowly tissue-restricted program. The module also does not show a strong blood-cell signature: most genes have low immune-cell specificity, with only limited immune-cell enhancement. Consequently, blood contamination is not the leading explanation, although shared cell types cannot be excluded. The HPA single-cell annotations are notably enriched for reproductive, trophoblast, germ-cell, and progenitor-like populations, including spermatocyte, spermatid, trophoblast, and progenitor annotations. This pattern is compatible with a shared cellular state or shared cell-type composition between the sampled tissues. Ovary protein detection is present for many module genes, whereas there is no matching HPA tissue category for stem_cells, so the HPA comparison does not independently validate protein expression in the stem-cell samples.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a well-defined junction subnetwork: TJP1 is linked to TJP2 and YBX3, and TJP2 is also linked to YBX3. STRING also supports the proteasome relationship between PSMC4 and PSMD13, while the POLR2H–SUPT16H relationship supports a transcriptional connection. The supplementary STRING annotations (STRING NetworkNeighborAL Claudin, and Maintenance of blood-brain barrier; within-query FDR = 0.0182) connect TJP1, TJP2, and YBX3 with claudin-associated barrier maintenance, while (STRING RCTM Apoptosis; within-query FDR = 0.0205) connects TJP1, TJP2, PSMC4, PSMD13, and ACIN1 with an apoptosis-related resource. These are supportive annotations, not globally corrected GO or KEGG results. hu.MAP independently places TJP1 and TJP2 together in complexes (hu.MAP huMAP3_06395.1) and (hu.MAP huMAP3_10673.1), and places PSMC4 and PSMD13 together in proteasome-related complexes (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1). TP53BP1 and DYNC1I2 co-occur in (hu.MAP huMAP3_12566.1). However, each hu.MAP complex contains many members outside this module, so the module captures selected components rather than a complete physical complex. Overall, known interactions explain important parts of the network, but not the entire co-abundance structure.

**STRING interactions (score >= 0.7)**: 5 of 120 gene pairs: POLR2H–SUPT16H (0.936); PSMC4–PSMD13 (0.999); TJP1–TJP2 (0.999); TJP1–YBX3 (0.998); TJP2–YBX3 (0.701)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Claudin, and Maintenance of blood-brain barrier (FDR = 0.0182, 3 genes); RCTM Apoptosis (FDR = 0.0205, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06395.1 (TJP1, TJP2; 2/8); huMAP3_10673.1 (TJP1, TJP2; 2/14); huMAP3_05064.1 (PSMC4, PSMD13; 2/31); huMAP3_12566.1 (TP53BP1, DYNC1I2; 2/51); huMAP3_09656.1 (PSMC4, PSMD13; 2/64); huMAP3_13725.1 (PSMC4, PSMD13; 2/69)

### Novelty

The module should not be described as a newly discovered molecular complex or pathway. Several of its relationships are already established through STRING and hu.MAP, especially the TJP1–TJP2 junction relationship and the PSMC4–PSMD13 proteasome relationship. The module may nevertheless represent a novel cross-tissue co-abundance pattern because it combines junctional, proteostatic, biosynthetic, transcriptional, transport, and genome-maintenance genes in a shared ovary–stem-cell context, and most module pairs lack high-confidence STRING support or hu.MAP representation. That observation is suggestive rather than proof of novelty: absence from these resources can reflect incomplete interaction coverage, context dependence, or co-regulation without direct physical binding. Demonstrating novelty would require replication in independent ovary and stem-cell datasets, adjustment for cell-type composition, and comparison with published tissue-specific co-expression modules.

**Hypothesis.** Hypothesis: the module reflects a shared proliferative or progenitor-like cellular state in which junctional architecture is coordinated with biosynthetic capacity, protein turnover, transcriptional control, intracellular transport, and DNA-damage surveillance. TJP1 and TJP2 may mark the structural or epithelial-like component, CAD may support nucleotide production for cell growth, PSMC4 and PSMD13 may maintain proteome quality during increased cellular activity, and TP53BP1 may monitor genome integrity. The observed co-abundance could arise from coordinated regulation within a shared cell population rather than direct physical interaction among all genes. This hypothesis predicts that module activity should track junction integrity, proliferation, proteasome activity, and genome-stress responses, and that the association should weaken after rigorous adjustment for cell-type composition.

### Important genes

#### TJP1

- **Related proteins** (co-abundance neighbors): ZMYND8 (0.84), POLR2H (0.83), CXXC1 (0.83), TJP2 (0.80); STRING partners: TJP2 (0.999), YBX3 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cell Junctions; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_06395.1, huMAP3_10673.1
- **Function (MyGene.info)**: tight junction protein 1. This gene encodes a member of the membrane-associated guanylate kinase (MAGUK) family of proteins, and acts as a tight junction adaptor protein that also regulates adherens junctions. Tight junctions regulate the movement of ions and macromolecules between endothelial and epithelial cells. The multidomain structure of this scaffold protein, including a postsynaptic density 95/disc-large/zona occlu…
- **Diseases (Open Targets)**: dengue disease (0.476); COVID-19 (0.373); skin disorder (0.312); Hypocalcemia (0.264); cataract (0.256)
- **Europe PMC papers**: 6421
- **Why important**: TJP1 is among the strongest network connectors and links the junctional subnetwork to other module components. It has direct STRING relationships with TJP2 and YBX3, participates with TJP2 in hu.MAP complexes (hu.MAP huMAP3_06395.1) and (hu.MAP huMAP3_10673.1), and is annotated as a tight-junction adaptor involved in cell-cell junction assembly, adherens-junction maintenance, actin organization, and cell migration. It is detected in ovary and has cell-type-enhanced HPA annotations in several barrier, neural, and epithelial-like populations. Its disease associations and substantial literature make it the best-established structural anchor of the module.
- **Conclusion**: Established evidence supports TJP1 as a central junctional scaffold and a plausible marker of the module's cell-architecture component. It is not established that TJP1 drives the entire cross-tissue module. Hypothesis: TJP1 abundance may report a coordinated epithelial or progenitor-state program rather than merely local junction assembly.

#### TJP2

- **Related proteins** (co-abundance neighbors): JPT2 (0.85), YBX3 (0.84), TJP1 (0.80); STRING partners: TJP1 (0.999), YBX3 (0.701)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cell Junctions; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_06395.1, huMAP3_10673.1
- **Function (MyGene.info)**: tight junction protein 2. This gene encodes a zonula occluden that is a member of the membrane-associated guanylate kinase homolog family. The encoded protein functions as a component of the tight junction barrier in epithelial and endothelial cells and is necessary for proper assembly of tight junctions. Mutations in this gene have been identified in patients with hypercholanemia, and genomic duplication of a 270 kb regio…
- **Diseases (Open Targets)**: cholestasis, progressive familial intrahepatic, 4 (0.800); hypercholanemia, familial 1 (0.647); autosomal dominant nonsyndromic hearing loss (0.558); progressive familial intrahepatic cholestasis type 2 (0.527); deafness (0.467)
- **Europe PMC papers**: 1748
- **Why important**: TJP2 is a prominent junctional connector with direct STRING links to TJP1 and YBX3 and membership with TJP1 in hu.MAP complexes (hu.MAP huMAP3_06395.1) and (hu.MAP huMAP3_10673.1). Its established functions include tight-junction barrier assembly, homotypic adhesion, and cell-junction organization. It is detected in ovary, has enhanced annotations in several specialized cell types, and has well-documented disease associations involving cholestatic and auditory phenotypes.
- **Conclusion**: Established evidence identifies TJP2 as a second structural anchor that strengthens the interpretation of a junction-associated module component. Its association with the full module remains a co-abundance observation. Hypothesis: coordinated TJP1–TJP2 abundance may indicate remodeling of cell contacts in the shared ovary–stem-cell cellular state.

#### CAD

- **Related proteins** (co-abundance neighbors): DYNC1I2 (0.85), SUPT16H (0.83), YBX3 (0.82), PSMD13 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carbamoyl-phosphate synthetase 2, aspartate transcarbamylase, and dihydroorotase. The de novo synthesis of pyrimidine nucleotides is required for mammalian cells to proliferate. This gene encodes a trifunctional protein which is associated with the enzymatic activities of the first 3 enzymes in the 6-step pathway of pyrimidine biosynthesis: carbamoylphosphate synthetase (CPS II), aspartate transcarbamoylase, and dihydroorotase. This protein is regulated by the mitogen-activated…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 50 (0.660); congenital disorder of glycosylation type I (0.595); infantile epileptic-dyskinetic encephalopathy (0.499); type 2 diabetes mellitus (0.286); urolithiasis (0.283)
- **Europe PMC papers**: 60667
- **Why important**: CAD has the strongest network connectivity in the module and connects the junctional, transcriptional, transport, and proteasome-related portions of the graph. Its established biochemical role is the trifunctional first part of de novo pyrimidine synthesis, a process required for mammalian cell proliferation. It is broadly expressed, detected in ovary, and has a very large literature base, with disease associations including developmental and metabolic disorders.
- **Conclusion**: Established evidence supports CAD as a biosynthetic and proliferation-related component, and its network position makes it a useful bridge gene. No globally significant GO or KEGG result confirms pyrimidine-pathway enrichment for this module. Hypothesis: CAD co-abundance may reflect increased nucleotide demand in a proliferative or progenitor-like population rather than a dedicated pyrimidine module.

#### PSMC4

- **Related proteins** (co-abundance neighbors): TP53BP1 (0.81); STRING partners: PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 4. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.603); mantle cell lymphoma (0.542); neoplasm (0.519); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1065
- **Why important**: PSMC4 is directly linked to PSMD13 by STRING and co-occurs with PSMD13 in multiple hu.MAP proteasome complexes (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1). It is an ATPase component of the proteasome regulatory particle and is annotated for proteasomal protein catabolism, oxidative-stress response, and type-one interferon response. It is detected in ovary and has enhanced HPA annotations in germ-cell, placental, and related populations. Its disease associations and literature support are substantial.
- **Conclusion**: Established evidence supports PSMC4 as part of the proteasome machinery and as a reliable proteostasis marker within the module. The data do not establish that proteasome activity causes the junctional or stem-cell association. Hypothesis: PSMC4 may support proteome quality during the increased biosynthetic and structural demands of the shared cellular state.

#### TP53BP1

- **Related proteins** (co-abundance neighbors): PSMD13 (0.84), PSMC4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_12566.1
- **Function (MyGene.info)**: tumor protein p53 binding protein 1. This gene encodes a protein that functions in the DNA double-strand break repair pathway choice, promoting non-homologous end joining (NHEJ) pathways, and limiting homologous recombination. This protein plays multiple roles in the DNA damage response, including promoting checkpoint signaling following DNA damage, acting as a scaffold for recruitment of DNA damage response proteins to damaged chrom…
- **Diseases (Open Targets)**: neurodegenerative disease (0.367); microcephaly and chorioretinopathy 3 (0.353); alcohol drinking (0.269); urolithiasis (0.269); microcephaly and chorioretinopathy 1 (0.266)
- **Europe PMC papers**: 2200
- **Why important**: TP53BP1 connects to the proteasome-associated part of the module through the co-abundance graph and is included with DYNC1I2 in hu.MAP complex (hu.MAP huMAP3_12566.1). It is an established DNA-damage-response scaffold that promotes checkpoint signaling and non-homologous end joining while limiting homologous recombination. It is detected in ovary, has cell-type-enhanced HPA annotations, and has extensive literature and disease relevance.
- **Conclusion**: Established evidence supports TP53BP1 as a genome-maintenance component that could be important in proliferating or differentiating cells. The module does not establish a direct TP53BP1 interaction with PSMC4 or a causal DNA-damage process. Hypothesis: TP53BP1 co-abundance may indicate coordinated genome surveillance accompanying proliferation and proteostasis demands.

## Module 4

**Tissue pair**: ovary and stem_cells  
**Genes (26)**: ANAPC7, ARFGAP1, BAG3, BYSL, NCAPD2, DIAPH1, DOHH, METTL13, KLHDC4, NAA15, NCDN, NDC80, NSUN2, PHAX, PLS1, POLR2E, SEC24A, SMC2, SMC4, SQSTM1, THUMPD3, TPD52L2, TTI2, UBR5, YAP1, ZNF598

### Function

The strongest interpretation is a chromosome-organization and reproductive cell-cycle module. The globally corrected GO terms consistently identify meiotic cell-cycle activity, chromosome separation, meiotic chromosome condensation, regulation of chromosome condensation, and the condensin complex (9 globally significant GO/KEGG terms, q_global 0.00592–0.0291; see the table). The core signal is carried by SMC2, SMC4, NCAPD2, NDC80, ANAPC7, and NSUN2. SMC2, SMC4, and NCAPD2 are condensin-associated chromosome-structuring proteins, while NDC80 supports kinetochore–microtubule attachment and chromosome segregation, and ANAPC7 is part of the anaphase-promoting complex. NSUN2 links the module to RNA modification and is included in the meiotic-cell-cycle evidence (GO:BP meiotic cell cycle; q_global = 0.00592), (GO:BP meiotic cell cycle process; q_global = 0.0112). The module therefore most plausibly reflects coordinated chromosome condensation, spindle or kinetochore function, and cell-cycle progression in meiotic or other proliferating cells. The remaining genes may represent supporting processes involving RNA maturation, protein quality control, ubiquitination, vesicle trafficking, cytoskeletal organization, and stress or survival responses. These secondary functions should not be treated as globally enriched module functions because they lack globally significant GO/KEGG support.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: HPA identifies only a single secreted gene, and the proteins are mainly intracellular or nuclear. It is also not strongly blood-cell specific overall, because most genes have low immune-cell specificity, although several genes are enhanced in erythrocyte, megakaryocyte, monocyte, or neutrophil progenitors and a smaller subset is enhanced in lymphoid tissue. The frequent HPA cell-type signals for oocytes and hematopoietic progenitors are consistent with a proliferative or germline-related component, but they also warn that shared cell types or differences in cellular composition could contribute to the ovary–stem-cell co-abundance pattern. Most genes have low tissue specificity, so the module is unlikely to be restricted to ovary. Protein detection in ovary supports expression of much of the module there, whereas matching HPA tissue evidence is unavailable for stem cells. Overall, the composition favors a broadly expressed cell-cycle or chromosome-maintenance program with contributions from oocyte-like and progenitor-like populations, rather than a blood-contamination or secreted-protein explanation.

**GO/KEGG enrichment**: 9 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP meiotic cell cycle | 0.00592 | ANAPC7, NCAPD2, NDC80, NSUN2, SMC2, SMC4 |
| GO:BP regulation of chromosome separation | 0.00829 | ANAPC7, NCAPD2, NDC80, SMC2, SMC4 |
| GO:BP positive regulation of chromosome separation | 0.0083 | ANAPC7, NCAPD2, SMC2, SMC4 |
| GO:BP chromosome separation | 0.0112 | ANAPC7, NCAPD2, NDC80, SMC2, SMC4 |
| GO:BP meiotic cell cycle process | 0.0112 | NCAPD2, NDC80, NSUN2, SMC2, SMC4 |
| GO:BP meiotic chromosome condensation | 0.0169 | NCAPD2, SMC2, SMC4 |
| GO:CC condensin complex | 0.0291 | NCAPD2, SMC2, SMC4 |
| GO:BP regulation of chromosome condensation | 0.0291 | NCAPD2, SMC2, SMC4 |
| GO:BP positive regulation of chromosome condensation | 0.0291 | NCAPD2, SMC2, SMC4 |

### STRING and hu.MAP

STRING provides a compact, biologically coherent core. SMC2 and SMC4 have extremely strong mutual support, and both connect to NCAPD2; NDC80 also connects to both SMC proteins. These relationships directly support a condensin and chromosome-segregation interpretation. STRING additionally links BAG3 with SQSTM1, indicating a separate established stress, autophagy, or protein-quality-control relationship. The STRING keyword results for DNA condensation and mitosis (STRING Keyword DNA condensation; within-query FDR = 0.0299), (STRING Keyword Mitosis; within-query FDR = 0.0299) are supplementary and agree with the globally corrected GO findings, but they are not additional global-significance claims. hu.MAP independently places SMC2, NCAPD2, and SMC4 together in several condensin-related or condensin-overlapping complexes (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_14663.1). The repeated recovery of this trio is strong evidence that part of the module reflects a real macromolecular complex rather than an arbitrary co-abundance association. However, most module edges are not represented by high-confidence STRING relationships, and the hu.MAP complexes contain many members absent from the module. Thus, the module combines a known condensin-centered core with peripheral co-abundance relationships whose physical or functional connections remain less established.

**STRING interactions (score >= 0.7)**: 6 of 325 gene pairs: BAG3–SQSTM1 (0.946); NCAPD2–SMC2 (0.999); NCAPD2–SMC4 (0.999); NDC80–SMC2 (0.899); NDC80–SMC4 (0.867); SMC2–SMC4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword DNA condensation (FDR = 0.0299, 3 genes); Keyword Mitosis (FDR = 0.0299, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03084.1 (SMC2, NCAPD2, SMC4; 3/8); huMAP3_14385.1 (SMC2, NCAPD2, SMC4; 3/9); huMAP3_09855.1 (SMC2, NCAPD2, SMC4; 3/10); huMAP3_11457.1 (SMC2, NCAPD2, SMC4; 3/10); huMAP3_14663.1 (SMC2, NCAPD2, SMC4; 3/14)

### Novelty

The biological mechanism represented by the central part of the module is not a new discovery: condensin-associated relationships among SMC2, SMC4, and NCAPD2, and links of NDC80 to chromosome segregation, are already supported by STRING and hu.MAP (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_14663.1). The globally corrected enrichment also recapitulates established chromosome-condensation and meiotic-cell-cycle biology (9 globally significant GO/KEGG terms, q_global 0.00592–0.0291; see the table). The potentially novel result is the tissue-pair-specific co-abundance configuration that joins this condensin core with genes involved in RNA processing, protein quality control, cytoskeletal regulation, trafficking, and stress responses. That configuration could reflect a shared cellular state in ovary and stem cells, but the fact sheet does not establish that it is mechanistically new. Absence of most peripheral relationships from STRING or hu.MAP cannot by itself demonstrate novelty, because those resources emphasize physical interactions and curated complexes rather than every tissue-specific co-expression relationship. The appropriate conclusion is established core biology with a potentially new, but presently unproven, cross-tissue co-abundance context.

**Hypothesis.** Hypothesis: the module marks a conserved proliferative or germline-associated state in which chromosome condensation, kinetochore function, and cell-cycle transitions are coordinated with RNA maturation and cellular stress management. In ovary, this may be particularly relevant to oocyte or meiotic programs; in stem cells, it may reflect a related need for accurate chromosome handling during self-renewal or differentiation. The condensin-centered core could be the mechanistic driver, while NSUN2 and the RNA-processing genes support translation and transcript maturation, and the BAG3–SQSTM1 pair buffers proteotoxic or metabolic stress. This is a testable hypothesis rather than a demonstrated pathway: it would require cell-resolved expression, cell-cycle staging, perturbation of the condensin core, and confirmation that the peripheral genes change with chromosome-segregation status.

### Important genes

#### SMC4

- **Related proteins** (co-abundance neighbors): SMC2 (0.86), PHAX (0.83), SEC24A (0.81), NDC80 (0.80); STRING partners: NCAPD2 (0.999), NDC80 (0.867), SMC2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nuclear speckles, Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_03084.1, huMAP3_14385.1, huMAP3_09855.1, huMAP3_11457.1, huMAP3_14663.1
- **Function (MyGene.info)**: structural maintenance of chromosomes 4. This gene belongs to the 'structural maintenance of chromosomes' (SMC) gene family. Members of this gene family play a role in two changes in chromosome structure during mitotic segregation of chromosomes- chromosome condensation and sister chromatid cohesion. The protein encoded by this gene is likely a subunit of the 13S condensin complex, which is involved in chromosome condensation. A pseudoge…
- **Diseases (Open Targets)**: clonal hematopoiesis (0.233); bone marrow failure syndrome (0.148); hepatocellular carcinoma (0.111); central nervous system cancer (0.107); glioma (0.107)
- **Europe PMC papers**: 1967
- **Why important**: SMC4 is a central hub of the module and has strong STRING support with SMC2, NCAPD2, and NDC80. It appears in every globally corrected GO term (9 globally significant GO/KEGG terms, q_global 0.00592–0.0291; see the table), including the condensin-complex term (GO:CC condensin complex; q_global = 0.0291), and is present in every listed hu.MAP complex (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_14663.1). Its HPA profile includes lymphoid tissue and several progenitor cell types, including erythrocyte and megakaryocyte progenitors. Its established role is as a structural-maintenance-of-chromosomes subunit involved in chromosome condensation and segregation. Its disease associations include clonal hematopoiesis, bone-marrow failure, and cancers, while its literature base is substantial.
- **Conclusion**: Established evidence supports SMC4 as a principal structural component and likely anchor of the module's condensin-centered biology. The co-abundance data support coordinated regulation of this machinery in the two tissues, but do not establish that SMC4 directly regulates the module's peripheral genes.

#### SMC2

- **Related proteins** (co-abundance neighbors): SMC4 (0.86); STRING partners: NCAPD2 (0.999), NDC80 (0.899), SMC4 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_03084.1, huMAP3_14385.1, huMAP3_09855.1, huMAP3_11457.1, huMAP3_14663.1
- **Function (MyGene.info)**: structural maintenance of chromosomes 2. Predicted to enable ATP binding activity; chromatin binding activity; and single-stranded DNA binding activity. Involved in mitotic chromosome condensation. Located in condensed chromosome; cytoplasm; and nuclear lumen. Part of condensin complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: basal cell carcinoma (0.464); ovarian carcinoma (0.383); aortic stenosis (0.380); cancer (0.363); alcohol drinking (0.359)
- **Europe PMC papers**: 2065
- **Why important**: SMC2 is the strongest known partner of SMC4 and has very strong STRING support with NCAPD2. It occurs in every globally corrected GO term (9 globally significant GO/KEGG terms, q_global 0.00592–0.0291; see the table) and in every hu.MAP complex (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_14663.1). HPA shows enhancement in lymphoid tissue and several meiotic or progenitor-like cell types. Its established functions include ATP-dependent chromosome organization, condensin activity, chromosome condensation, and chromosome segregation. It has disease associations including ovarian carcinoma, cancer, and neurodevelopmental disease, and it has a large literature base.
- **Conclusion**: Established evidence identifies SMC2 as a core condensin subunit and one of the most informative markers of the module's chromosome-organization function. Its ovarian disease association makes it particularly relevant to the tissue context, but the module does not by itself show that altered SMC2 causes the observed tissue-pair pattern.

#### NCAPD2

- **Related proteins** (co-abundance neighbors): KLHDC4 (0.92), ANAPC7 (0.85); STRING partners: SMC2 (0.999), SMC4 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_03084.1, huMAP3_14385.1, huMAP3_09855.1, huMAP3_11457.1, huMAP3_14663.1
- **Function (MyGene.info)**: non-SMC condensin I complex subunit D2. Enables histone binding activity. Involved in mitotic chromosome condensation. Located in condensed chromosome; cytosol; and nucleoplasm. Part of condensin complex. Colocalizes with cytoplasm and nuclear chromosome. Implicated in primary autosomal recessive microcephaly. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: microcephaly 21, primary, autosomal recessive (0.592); autosomal recessive primary microcephaly (0.462); neurodegenerative disease (0.376); hereditary disease (0.194); lung adenocarcinoma (0.105)
- **Europe PMC papers**: 623
- **Why important**: NCAPD2 is the non-SMC condensin subunit most consistently connected to the SMC2–SMC4 pair. It appears in every globally corrected GO term (9 globally significant GO/KEGG terms, q_global 0.00592–0.0291; see the table), participates in every hu.MAP complex (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_14663.1), and has strong STRING relationships with both SMC proteins. HPA shows enhancement in lymphoid tissue and multiple hematopoietic progenitor populations. Its established functions include condensin-dependent chromosome condensation and positive regulation of chromosome condensation. It is associated with primary microcephaly and other neurodevelopmental conditions, and it has a substantial literature base.
- **Conclusion**: Established evidence supports NCAPD2 as a core condensin component and a particularly strong explanatory gene for the module. The module may reflect increased demand for condensin function in oocyte-like or progenitor-like cells, but that cellular-state interpretation remains a hypothesis.

#### NDC80

- **Related proteins** (co-abundance neighbors): SMC4 (0.80); STRING partners: SMC2 (0.899), SMC4 (0.867)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NDC80 kinetochore complex component. This gene encodes a component of the NDC80 kinetochore complex. The encoded protein consists of an N-terminal microtubule binding domain and a C-terminal coiled-coiled domain that interacts with other components of the complex. This protein functions to organize and stabilize microtubule-kinetochore interactions and is required for proper chromosome segregation. [provided by RefSeq, Oct 2011].
- **Diseases (Open Targets)**: alcohol drinking (0.466); hemorrhage (0.344); gastric ulcer (0.344); heart conduction disease (0.344); bronchial disorder (0.324)
- **Europe PMC papers**: 3155
- **Why important**: NDC80 connects the condensin core to kinetochore biology through STRING-supported relationships with SMC2 and SMC4. It contributes to the globally corrected meiotic-cell-cycle and chromosome-separation terms (GO:BP meiotic cell cycle; q_global = 0.00592), (GO:BP regulation of chromosome separation; q_global = 0.00829), (GO:BP chromosome separation; q_global = 0.0112), and (GO:BP meiotic cell cycle process; q_global = 0.0112), and its established function is to organize and stabilize microtubule–kinetochore interactions during chromosome segregation. HPA shows enhancement in bone marrow, lymphoid tissue, and several spermatocyte, progenitor, and trophoblast populations. Its literature base is substantial, and its disease associations include hemorrhage and other disorders.
- **Conclusion**: Established evidence supports NDC80 as the module's kinetochore and spindle-segregation component, complementing the chromosome-condensation role of the SMC–NCAPD2 core. Its inclusion strengthens the interpretation of coordinated chromosome segregation, although a direct physical condensin–NDC80 complex is not demonstrated for this module.

#### ANAPC7

- **Related proteins** (co-abundance neighbors): NCAPD2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules, Cytokinetic bridge, Mitotic spindle; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: anaphase promoting complex subunit 7. This gene encodes a tetratricopeptide repeat containing component of the anaphase promoting complex/cyclosome (APC/C), a large E3 ubiquitin ligase that controls cell cycle progression by targeting a number of cell cycle regulators such as B-type cyclins for 26S proteasome-mediated degradation through ubiquitination. The encoded protein is required for proper protein ubiquitination function of APC/…
- **Diseases (Open Targets)**: Ferguson-Bonni neurodevelopmental syndrome (0.475); neurodegenerative disease (0.233); obesity disorder (0.056); schizophrenia (0.040); Abnormality of the skeletal system (0.037)
- **Europe PMC papers**: 354
- **Why important**: ANAPC7 links the module to anaphase-promoting-complex activity and cell-cycle transition control. It contributes to the globally corrected terms for meiotic cell cycle and chromosome separation (4 globally significant GO/KEGG terms, q_global 0.00592–0.0112; see the table), and its HPA localization includes the mitotic spindle, cytokinetic bridge, and microtubules. Its established role is as a subunit of the APC/C ubiquitin ligase, which controls cell-cycle progression through regulated protein degradation. It has disease associations involving neurodevelopment and abnormal skeletal development, with a more modest literature base than the condensin genes. Its network connection to NCAPD2 places it near the chromosome-segregation core.
- **Conclusion**: Established evidence supports ANAPC7 as a cell-cycle-transition component that complements condensin and kinetochore functions. Its module membership suggests coordinated abundance with chromosome machinery, but does not prove direct APC/C control of the other module genes.

#### NSUN2

- **Related proteins** (co-abundance neighbors): DOHH (0.91), PHAX (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP2/Sun RNA methyltransferase 2. This gene encodes a methyltransferase that catalyzes the methylation of cytosine to 5-methylcytosine (m5C) at position 34 of intron-containing tRNA(Leu)(CAA) precursors. This modification is necessary to stabilize the anticodon-codon pairing and correctly translate the mRNA. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Mar…
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.694); hereditary disease (0.518); Intellectual disability (0.489); phenylketonuria (0.470); neurodegenerative disease (0.462)
- **Europe PMC papers**: 2458
- **Why important**: NSUN2 provides a mechanistic bridge from chromosome and meiotic-cell-cycle biology to RNA modification. It contributes to the globally corrected meiotic terms (GO:BP meiotic cell cycle; q_global = 0.00592) and (GO:BP meiotic cell cycle process; q_global = 0.0112) and to the supplementary mitosis term (STRING Keyword Mitosis; within-query FDR = 0.0299). Its established function is cytosine methylation of tRNA and participation in RNA processing and export. HPA describes broad cellular distribution with intracellular and membrane secretome annotation, rather than a secreted-protein role. It has a substantial literature base and disease associations involving intellectual disability and neurodegeneration. Its network links to DOHH and PHAX connect it to RNA maturation and translation-related processes.
- **Conclusion**: Established evidence supports NSUN2 as an RNA-modification factor that may accompany high biosynthetic and proliferative demand. Its connection to the condensin-centered module is biologically plausible but less directly established than the SMC2–SMC4–NCAPD2 relationships, so any role in coordinating RNA metabolism with chromosome segregation remains a hypothesis.

## Module 5

**Tissue pair**: ovary and stem_cells  
**Genes (23)**: ARHGEF2, BICD2, CERT1, CHD4, HBS1L, KLC1, MMTAG2, NLE1, NOP16, PES1, PITPNB, PRRC2A, PRRC2C, PUM1, POLR1A, RRP1B, SH2D4A, DNTTIP2, TRAF2, USP10, UTP4, WDR3, ZC3H4

### Function

The strongest interpretation is a nucleolar preribosome and ribosome-biogenesis module. The primary evidence is the globally corrected enrichment for preribosome (GO:CC preribosome; q_global = 0.0259) and ribosome biogenesis (GO:BP ribosome biogenesis; q_global = 0.0331). (GO:CC preribosome; q_global = 0.0259) identifies DNTTIP2, PES1, RRP1B, UTP4, and WDR3, while (GO:BP ribosome biogenesis; q_global = 0.0331) additionally includes NLE1 and NOP16. This is concordant with the nucleolar or nucleoli-rim localization reported for several members and with the known roles of POLR1A in precursor ribosomal RNA transcription, UTP4 and WDR3 in small-subunit processing, PES1 in large-subunit maturation, and NLE1 in ribosomal assembly. The module therefore most plausibly reflects coordinated ribosomal RNA production, preribosome assembly, and maturation rather than a tissue-specific signaling pathway. No KEGG term is supplied as globally significant, and no within-module GO term passed its correction threshold; the global GO results (GO:CC preribosome; q_global = 0.0259) and (GO:BP ribosome biogenesis; q_global = 0.0331) remain the primary functional evidence.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and the blood-cell evidence is predominantly low immune-cell specificity, with only a limited neutrophil-associated signal involving genes such as USP10 and SH2D4A. The module is therefore more consistent with broadly expressed intracellular machinery than with a blood-derived plasma signature. Cell-type-enhanced annotations include oocytes for several genes and neutrophils for several others, so shared cell types or sample-composition effects cannot be excluded. However, the absence of a dominant blood-cell pattern and the nucleolar localization of the best-supported genes favor a conserved cellular housekeeping or proliferative program. Protein detection in ovary for many members is compatible with the ovary component; the fact sheet provides no matching HPA tissue for stem_cells.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC preribosome | 0.0259 | DNTTIP2, PES1, RRP1B, UTP4, WDR3 |
| GO:BP ribosome biogenesis | 0.0331 | DNTTIP2, NLE1, NOP16, PES1, RRP1B, UTP4, WDR3 |

### STRING and hu.MAP

STRING independently supports the preribosome and ribosome-biogenesis interpretation through (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 0.024). The strongest known relationships form a coherent group around DNTTIP2, UTP4, WDR3, PES1, RRP1B, NLE1, and POLR1A. These relationships indicate that much of the co-abundance structure recapitulates established physical or functional connections rather than being an entirely unexplained correlation pattern. The hu.MAP evidence is more distributed. It places NLE1 with ZC3H4 in (hu.MAP huMAP3_09162.1), UTP4 with HBS1L in (hu.MAP huMAP3_14264.1), and DNTTIP2 with MMTAG2 in (hu.MAP huMAP3_05807.1), while PRRC2A and USP10 recur together across several complexes (hu.MAP huMAP3_08887.1), (hu.MAP huMAP3_10364.1), (hu.MAP huMAP3_10976.1), (hu.MAP huMAP3_11111.1), (hu.MAP huMAP3_14270.1), and (hu.MAP huMAP3_14559.1). These partial overlaps suggest links to RNA handling, translation-associated assemblies, stress-granule biology, and RNA-quality control, but they do not establish that every module member belongs to one physical complex. The STRING and hu.MAP results therefore support a connected ribosome/RNA-processing neighborhood with additional peripheral regulatory branches.

**STRING interactions (score >= 0.7)**: 14 of 253 gene pairs: DNTTIP2–UTP4 (0.989); DNTTIP2–WDR3 (0.99); NLE1–PES1 (0.924); NLE1–POLR1A (0.731); NLE1–RRP1B (0.799); PES1–POLR1A (0.91); PES1–RRP1B (0.984); PES1–UTP4 (0.926); PES1–WDR3 (0.914); POLR1A–UTP4 (0.879); POLR1A–WDR3 (0.948); RRP1B–UTP4 (0.734); RRP1B–WDR3 (0.796); UTP4–WDR3 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 0.024, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08887.1 (PRRC2A, PRRC2C; 2/2); huMAP3_09162.1 (NLE1, ZC3H4; 2/4); huMAP3_10364.1 (PRRC2A, USP10; 2/4); huMAP3_10976.1 (PRRC2A, USP10; 2/12); huMAP3_14264.1 (UTP4, HBS1L; 2/20); huMAP3_11111.1 (PRRC2A, USP10; 2/29); huMAP3_14270.1 (PRRC2A, USP10; 2/47); huMAP3_14559.1 (PRRC2A, USP10; 2/47); huMAP3_05807.1 (DNTTIP2, MMTAG2; 2/81)

### Novelty

The biological function itself should not be presented as a new discovery: ribosome biogenesis, preribosome assembly, and the relationships among several core genes are already represented in GO, STRING, and hu.MAP. What may be novel is the observation that this particular co-abundance configuration is conserved across ovary and stem_cells, especially the combination of a well-supported nucleolar core with peripheral genes involved in RNA regulation, translation, transport, stress-granule biology, and signaling. The fact sheet does not provide an external matched-tissue replication, perturbation experiment, or prior report of this exact module. Consequently, the appropriate conclusion is that the module is a potentially novel cross-tissue co-abundance pattern built largely from established biology, not a newly discovered molecular complex or a proven tissue-specific mechanism. Absence from STRING or hu.MAP alone would not establish novelty.

**Hypothesis.** Hypothesis: in both ovary and stem_cells, a shared demand for ribosome production and translational capacity coordinates a nucleolar preribosome core with post-transcriptional and stress-responsive RNA control. POLR1A may provide the precursor-ribosomal RNA transcriptional input; UTP4, WDR3, DNTTIP2, PES1, RRP1B, NLE1, and NOP16 may support successive preribosome processing and subunit maturation; and PRRC2A, PRRC2C, USP10, PUM1, ZC3H4, and related peripheral genes may tune RNA stability, translation, or stress responses. The shared module could therefore mark a conserved state of biosynthetic readiness or proliferative capacity. The cell-type annotations also motivate a secondary possibility that part of the signal reflects oocyte-associated biology or minor immune-cell admixture. This remains a hypothesis requiring cell-resolved expression, perturbation, and independent tissue replication.

### Important genes

#### WDR3

- **Related proteins** (co-abundance neighbors): USP10 (0.90), CHD4 (0.89); STRING partners: DNTTIP2 (0.99), PES1 (0.914), POLR1A (0.948), RRP1B (0.796), UTP4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 3. This gene encodes a nuclear protein containing 10 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, which usually include a trp-asp at the C-terminal end. Proteins belonging to the WD repeat family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. [provid…
- **Diseases (Open Targets)**: presbycusis (0.335); respiratory tract infectious disorder (0.184); neurodegenerative disease (0.143); preeclampsia (0.120); alcohol drinking (0.098)
- **Europe PMC papers**: 280
- **Why important**: WDR3 is a direct member of both primary globally corrected terms (GO:CC preribosome; q_global = 0.0259) and (GO:BP ribosome biogenesis; q_global = 0.0331) and of the supplementary STRING term (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 0.024). It is nucleolar, has a strong STRING-connected position within the preribosome group, and is annotated for small-subunit ribosomal RNA maturation and biogenesis. Its disease associations include presbycusis, respiratory tract infectious disorder, neurodegenerative disease, preeclampsia, and alcohol drinking. Its literature volume is more limited than that of the most studied regulatory genes, which makes its presence in a coherent cross-tissue module particularly useful for mechanistic follow-up.
- **Conclusion**: Established evidence supports WDR3 as a nucleolar small-subunit biogenesis factor and a core marker of this module. Hypothesis: variation in WDR3 abundance may help report or constrain ribosome-production capacity in both tissues, but the module does not by itself demonstrate that WDR3 drives the shared co-abundance state.

#### UTP4

- **Related proteins** (co-abundance neighbors): MMTAG2 (0.91), PES1 (0.87); STRING partners: DNTTIP2 (0.989), PES1 (0.926), POLR1A (0.879), RRP1B (0.734), WDR3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_14264.1
- **Function (MyGene.info)**: UTP4 small subunit processome component. This gene encodes a WD40-repeat-containing protein that is localized to the nucleolus. Mutation of this gene causes North American Indian childhood cirrhosis, a severe intrahepatic cholestasis that results in transient neonatal jaundice, and progresses to periportal fibrosis and cirrhosis in childhood and adolescence. Alternative splicing results in multiple transcript variants. [provided by RefSe…
- **Diseases (Open Targets)**: hereditary North American Indian childhood cirrhosis (0.420); cardiovascular disorder (0.101); basal cell carcinoma (0.079); hypertensive disorder (0.064); osteosarcoma (0.052)
- **Europe PMC papers**: 214
- **Why important**: UTP4 is present in both primary terms (GO:CC preribosome; q_global = 0.0259) and (GO:BP ribosome biogenesis; q_global = 0.0331) and in (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 0.024). It is nucleolar, is enhanced in oocytes, is detected in ovary, and is strongly connected to the preribosome STRING neighborhood. Its annotated role in small-subunit ribosomal RNA maturation directly matches the inferred function. UTP4 is also associated with North American Indian childhood cirrhosis, cardiovascular disorder, basal cell carcinoma, hypertensive disorder, and osteosarcoma.
- **Conclusion**: Established evidence identifies UTP4 as a small-subunit processome component and a strong molecular marker of the shared nucleolar program. Hypothesis: its oocyte-enhanced annotation may help explain why the module is visible in ovary, although the available data do not show that UTP4 is ovary-specific or causally responsible for conservation across tissues.

#### PES1

- **Related proteins** (co-abundance neighbors): UTP4 (0.87); STRING partners: NLE1 (0.924), POLR1A (0.91), RRP1B (0.984), UTP4 (0.926), WDR3 (0.914)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli, Nucleoli rim, Mitotic chromosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pescadillo ribosomal biogenesis factor 1. This gene encodes a nuclear protein that contains a breast cancer associated gene 1 (BRCA1) C-terminal interaction domain. The encoded protein interacts with BOP1 and WDR12 to form the PeBoW complex, which plays a critical role in cell proliferation via pre-rRNA processing and 60S ribosomal subunit maturation. Expression of this gene may play an important role in breast cancer proliferation and tu…
- **Diseases (Open Targets)**: aortic stenosis (0.137); neoplasm (0.104); head and neck squamous cell carcinoma (0.097); schizophrenia (0.091); neuroblastoma (0.081)
- **Europe PMC papers**: 1080
- **Why important**: PES1 is included in both globally corrected terms (GO:CC preribosome; q_global = 0.0259) and (GO:BP ribosome biogenesis; q_global = 0.0331) and in (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 0.024). It occupies a key STRING position connected to NLE1, POLR1A, RRP1B, UTP4, and WDR3. Its established role in the PeBoW complex, precursor-ribosomal RNA processing, and large-subunit maturation provides a mechanistic bridge between the enrichment result and the known interaction network. PES1 also has substantial literature and associations with neoplasm, head and neck squamous cell carcinoma, schizophrenia, and neuroblastoma.
- **Conclusion**: Established evidence supports PES1 as a core large-subunit biogenesis factor and a central biochemical interpreter of this module. Hypothesis: PES1 abundance may couple ribosome maturation to cell proliferation or biosynthetic demand in the two tissue groups, but the co-abundance data cannot establish a tumor-related or proliferative causal effect.

#### POLR1A

- **Related proteins** (co-abundance neighbors): MMTAG2 (0.95), NOP16 (0.89), USP10 (0.85); STRING partners: NLE1 (0.731), PES1 (0.91), UTP4 (0.879), WDR3 (0.948)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoli fibrillar center; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase I subunit A. The protein encoded by this gene is the largest subunit of the RNA polymerase I complex. The encoded protein represents the catalytic subunit of the complex, which transcribes DNA into ribosomal RNA precursors. Defects in this gene are a cause of the Cincinnati type of acrofacial dysostosis. [provided by RefSeq, May 2016].
- **Diseases (Open Targets)**: choanal atresia-hearing loss-cardiac defects-craniofacial dysmorphism syndrome (0.780); acrofacial dysostosis Cincinnati type (0.723); leukodystrophy, hypomyelinating, 27 (0.459); acrofacial dysostosis (0.372); microtia (0.370)
- **Europe PMC papers**: 555
- **Why important**: POLR1A provides the upstream transcriptional entry point for the inferred pathway because it is the catalytic subunit of RNA polymerase I and transcribes precursor ribosomal RNA. It connects in STRING to NLE1, PES1, UTP4, and WDR3, thereby linking ribosomal RNA production with downstream processing factors. It is nucleolar and detected in ovary. Its established disease associations include Cincinnati type of acrofacial dysostosis, acrofacial dysostosis, hypomyelinating leukodystrophy, and related congenital syndromes.
- **Conclusion**: Established evidence supports POLR1A as the transcriptional component of the ribosome-biogenesis program represented here. Hypothesis: coordinated POLR1A abundance may synchronize precursor-ribosomal RNA production with processing capacity, but the module does not prove transcriptional regulation between POLR1A and the other genes.

#### NLE1

- **Related proteins** (co-abundance neighbors): MMTAG2 (0.88); STRING partners: PES1 (0.924), POLR1A (0.731), RRP1B (0.799)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_09162.1
- **Function (MyGene.info)**: notchless homolog 1. Predicted to be involved in Notch signaling pathway and ribosomal large subunit assembly. Predicted to act upstream of or within several processes, including chordate embryonic development; hematopoietic stem cell homeostasis; and regulation of signal transduction. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.505); lysosomal storage disease (0.198); neoplasm (0.097); non-small cell lung carcinoma (0.074); hepatocellular carcinoma (0.074)
- **Europe PMC papers**: 210
- **Why important**: NLE1 is included in the primary ribosome-biogenesis term (GO:BP ribosome biogenesis; q_global = 0.0331) and the supplementary STRING term (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 0.024). It is nucleolar, connects to PES1, POLR1A, and RRP1B in STRING, and is represented with ZC3H4 in hu.MAP complex (hu.MAP huMAP3_09162.1). Its annotations include ribosomal large-subunit assembly and regulation of Notch signaling, and it is enhanced in oocytes as well as several other cell types. Its disease-oriented resources include neurodegenerative disease, lysosomal storage disease, neoplasm, and several cancer-related associations.
- **Conclusion**: Established evidence supports NLE1 as a ribosome-assembly factor that links the nucleolar core to broader RNA and signaling biology. Hypothesis: NLE1 may be a useful bridge between biosynthetic state and stem-cell or oocyte-associated programs, but the present module cannot determine whether its Notch-related annotation is functionally active in either tissue.

## Module 6

**Tissue pair**: ovary and stem_cells  
**Genes (20)**: ASNS, BOLA2, BOP1, CORO1B, DBR1, DDX21, DHFR, EHMT1, KIF23, MYBBP1A, MED1, MMS19, NOL11, RPAP3, RPP40, RRP1, SRPK1, EPRS1, IARS1, ZNF326

### Function

The module most plausibly represents a coupled nucleolar RNA-processing and translation-support program, with additional links to transcription, RNA splicing, cell-cycle control, and cellular stress. The strongest functional clue is the supplementary STRING rRNA-processing signal (STRING Keyword rRNA processing; within-query FDR = 0.005), involving DDX21, NOL11, RPP40, RRP1, and BOP1. Their annotations support roles in rRNA maturation, ribosome biogenesis, tRNA processing, and nucleolar organization. EPRS1 and IARS1 connect the module to aminoacyl-tRNA charging and translational fidelity, while SRPK1, DBR1, and ZNF326 provide links to RNA splicing. MED1, EHMT1, and MYBBP1A suggest transcriptional and chromatin-regulatory coordination. No GO or KEGG term passed global correction, so the functional interpretation rests on convergent gene annotations, network structure, and the supplementary STRING result rather than on globally significant GO or KEGG enrichment.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and most genes have low tissue specificity and low immune-cell specificity. Thus, contamination by circulating plasma proteins or a broad blood cell signature is not the leading explanation. A small subset has immune-cell enhancement, but the enriched blood-cell categories are heterogeneous rather than forming a coherent blood program. Many genes show cell-type enhancement across diverse epithelial, neural, reproductive, and progenitor populations, which is more consistent with a shared intracellular program or shared cellular state than with one specific tissue identity. Detection of many proteins in ovary supports biological relevance there, whereas the stem-cell comparison has no matching HPA tissue measurement.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a connected core centered on DDX21, BOP1, MYBBP1A, RRP1, and related RNA-processing factors, with additional links from EPRS1 to IARS1 and MED1 and from DDX21 to SRPK1. The supplementary STRING annotation (STRING Keyword rRNA processing; within-query FDR = 0.005) is consistent with rRNA processing, but it is not a globally corrected enrichment result. The module also contains the EPRS1–IARS1 pair in the hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), supporting a known aminoacyl-tRNA synthetase-associated component. These resources show that several relationships are already established, especially the nucleolar RNA-processing connections and the EPRS1–IARS1 complex membership. At the same time, the co-abundance network is relatively sparse and many module gene pairs lack recorded high-confidence STRING or hu.MAP support, so the module should not be treated as a single experimentally established physical complex.

**STRING interactions (score >= 0.7)**: 9 of 190 gene pairs: ASNS–IARS1 (0.804); BOP1–DDX21 (0.838); BOP1–MED1 (0.766); BOP1–MYBBP1A (0.915); BOP1–RRP1 (0.988); DDX21–MYBBP1A (0.963); DDX21–SRPK1 (0.827); EPRS1–IARS1 (0.999); EPRS1–MED1 (0.832)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword rRNA processing (FDR = 0.005, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, IARS1; 2/14); huMAP3_13688.1 (EPRS1, IARS1; 2/14)

### Novelty

The module may be a new tissue-shared co-abundance pattern, but the evidence does not establish a new molecular complex or a new gene function. Its central themes are already biologically recognized: ribosome biogenesis, rRNA processing, aminoacyl-tRNA charging, RNA splicing, transcriptional regulation, and cell-cycle control. Existing STRING links and hu.MAP membership provide prior knowledge for important parts of the network. Conversely, the particular combination of these genes and its conservation between ovary and stem_cells is not shown in the fact sheet to have been previously reported. Absence of an interaction from STRING or hu.MAP cannot demonstrate novelty, so the defensible conclusion is that this is a potentially novel systems-level co-abundance association built largely from known cellular machinery.

**Hypothesis.** Hypothesis: the shared ovary–stem-cell module reflects a coordinated demand for nucleolar RNA maturation, ribosome production, accurate translation, and RNA surveillance in cells with substantial biosynthetic or proliferative activity. In this model, DDX21, BOP1, NOL11, and RRP1 organize or execute rRNA-processing activities; EPRS1 and IARS1 support translational capacity and fidelity; and SRPK1, DBR1, MED1, EHMT1, and related factors couple RNA maturation to splicing, transcription, and cell-state regulation. CORO1B, ASNS, KIF23, and DHFR could represent associated cytoskeletal, metabolic, and proliferative requirements. This remains a hypothesis because co-abundance does not prove physical binding, causal regulation, or a shared cell type.

### Important genes

#### DDX21

- **Related proteins** (co-abundance neighbors): RRP1 (0.88), EPRS1 (0.82), MYBBP1A (0.82), NOL11 (0.81); STRING partners: BOP1 (0.838), MYBBP1A (0.963), SRPK1 (0.827)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 is a central connector in the module and links several nucleolar and RNA-related genes. It has STRING relationships with BOP1, MYBBP1A, SRPK1, and other module members, and it is included in the supplementary rRNA-processing signal (STRING Keyword rRNA processing; within-query FDR = 0.005). Its helicase annotation, nucleolar location, and roles in RNA processing and transcription make it a strong candidate for integrating the module's main functional theme. It also has substantial literature and disease-association support.
- **Conclusion**: Established: DDX21 is an RNA helicase associated with RNA processing, nucleolar biology, and transcriptional regulation, and its recorded network relationships support a central position. Hypothesis: DDX21 may coordinate the shared co-abundance program by coupling rRNA maturation with broader RNA and cell-state regulation.

#### BOP1

- **Related proteins** (co-abundance neighbors): BOLA2; BOLA2B (0.86), CORO1B (0.80); STRING partners: DDX21 (0.838), MED1 (0.766), MYBBP1A (0.915), RRP1 (0.988)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BOP1 ribosomal biogenesis factor. Enables RNA binding activity. Involved in regulation of cell cycle; regulation of signal transduction by p53 class mediator; and ribosomal large subunit biogenesis. Located in chromosome; nucleolus; and nucleoplasm. Part of PeBoW complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.318); cancer (0.090); neoplasm (0.087); polycystic ovary syndrome (0.082); colorectal carcinoma (0.078)
- **Europe PMC papers**: 1064
- **Why important**: BOP1 is a nucleolar ribosome-biogenesis factor and a component of the PeBoW complex. It participates in the supplementary rRNA-processing signal (STRING Keyword rRNA processing; within-query FDR = 0.005) and has known STRING links to DDX21, MYBBP1A, RRP1, and MED1. Its network connections bridge the nucleolar processing core to transcriptional regulation, while its cell-type annotations include progenitor and differentiating populations relevant to the tissue comparison. It has a substantial literature base and disease links including cancer-related associations.
- **Conclusion**: Established: BOP1 has a direct role in large-subunit ribosome biogenesis and rRNA maturation, with multiple known network connections. Hypothesis: BOP1 may be a key execution factor through which biosynthetic demand becomes visible as coordinated module-level abundance.

#### EPRS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.83), RPAP3 (0.83), DDX21 (0.82), ZNF326 (0.81); STRING partners: IARS1 (0.999), MED1 (0.832)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is a highly connected translational component and has a very strong STRING relationship with IARS1. Both genes occur together in hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). EPRS1 encodes a bifunctional aminoacyl-tRNA synthetase involved in glutamyl- and prolyl-tRNA charging, linking the module to protein synthesis rather than only to nucleolar RNA production. Its disease associations include inherited leukodystrophy and developmental phenotypes.
- **Conclusion**: Established: EPRS1 supports aminoacyl-tRNA charging and belongs with IARS1 to known hu.MAP complexes. Hypothesis: EPRS1 may connect increased ribosome biogenesis with the translational capacity needed by ovary and stem-cell populations.

#### NOL11

- **Related proteins** (co-abundance neighbors): MED1 (0.93), DDX21 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleolar protein 11. Enables RNA binding activity. Involved in maturation of SSU-rRNA and positive regulation of transcription of nucleolar large rRNA by RNA polymerase I. Located in nucleolus. Part of t-UTP complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: diabetes mellitus (0.100); type 2 diabetes mellitus (0.100); atrial fibrillation (0.087); ulcerative colitis (0.011); cancer (0.011)
- **Europe PMC papers**: 240
- **Why important**: NOL11 provides a focused link to nucleolar transcription and small-subunit rRNA maturation. It is included in (STRING Keyword rRNA processing; within-query FDR = 0.005) and is connected in the module to MED1 and DDX21, placing it near both the RNA-processing core and a transcriptional regulator. Its ovary protein detection and nucleolar localization further support relevance to the observed tissue-shared pattern, although its literature and disease-association record is more limited than that of the major hubs.
- **Conclusion**: Established: NOL11 participates in SSU-rRNA maturation and nucleolar rRNA transcription. Hypothesis: NOL11 may help couple production of ribosomal precursors to transcriptional control in the shared module.

#### MED1

- **Related proteins** (co-abundance neighbors): MMS19 (0.95), NOL11 (0.93), KIF23 (0.90), DHFR (0.86); STRING partners: BOP1 (0.766), EPRS1 (0.832)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mediator complex subunit 1. The activation of gene transcription is a multistep process that is triggered by factors that recognize transcriptional enhancer sites in DNA. These factors work with co-activators to direct transcriptional initiation by the RNA polymerase II apparatus. The protein encoded by this gene is a subunit of the CRSP (cofactor required for SP1 activation) complex, which, along with TFIID, is required for…
- **Diseases (Open Targets)**: neurodegenerative disease (0.576); lysosomal storage disease (0.491); autoimmune disorder of central nervous system (0.462); Alzheimer disease (0.462); Parkinson disease (0.462)
- **Europe PMC papers**: 4237
- **Why important**: MED1 has the strongest network connectivity in the supplied module and links to BOP1 and EPRS1 through STRING while also connecting to several module genes in the co-abundance graph. As a mediator-complex subunit, it offers a plausible transcriptional interface for a module otherwise rich in nucleolar and translation-related factors. It has extensive literature, broad disease associations, and protein detection in ovary.
- **Conclusion**: Established: MED1 is a transcriptional coactivator and mediator-complex subunit with broad regulatory functions. Hypothesis: MED1 may reflect or help coordinate the transcriptional demand underlying the RNA-processing and biosynthetic state, but the module does not prove a direct MED1 role in ribosome biogenesis.

## Module 7

**Tissue pair**: ovary and stem_cells  
**Genes (28)**: CEP170, CLIP1, CLUH, CMSS1, CNN2, CIAPIN1, DFFA, DHX36, GNL3, GCLM, KRI1, NOLC1, NUDCD1, NUP43, OGFOD1, PAWR, PPP4R1, PSMD9, PYM1, RBM15, RGS10, SCAF11, TUBA1C, CCT5, CCT7, CCT8, TRIP6, ZFR

### Function

The module is most consistent with a nuclear proteostasis and telomere-maintenance program. The primary evidence is the coherent set of globally corrected terms linking positive regulation of telomere maintenance and telomere lengthening, telomerase RNA localization, and protein or RNA localization to the Cajal body (18 globally significant GO/KEGG terms, q_global 0.00227–0.0297; see the table). The chaperonin-containing T-complex annotation (GO:CC chaperonin-containing T-complex; q_global = 0.00995), together with the CCT-related STRING evidence (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 0.0149), indicates that CCT5, CCT7, and CCT8 are a core structural and functional component. GNL3 and DHX36 extend the interpretation toward nucleolar and RNA or nucleic-acid regulation of telomere biology (GO:BP positive regulation of telomere maintenance via telomere lengthening; q_global = 0.00227) (GO:BP positive regulation of telomere maintenance; q_global = 0.00454) (GO:BP regulation of telomere maintenance via telomere lengthening; q_global = 0.00775), (GO:BP regulation of telomere maintenance; q_global = 0.0177), (GO:BP telomere maintenance via telomere lengthening; q_global = 0.0232), (GO:BP positive regulation of chromosome organization; q_global = 0.0297). The sperm–zona pellucida term (GO:BP binding of sperm to zona pellucida; q_global = 0.0348) is supported by the same CCT genes and should be treated as context-dependent annotation rather than evidence that the whole module is a sperm-binding module. Overall, the module likely reflects coordinated protein folding, nuclear-body organization, RNA handling, and maintenance of chromosome ends.

**Cell composition.** This is not a plasma or secreted-protein module: HPA reports no secreted genes. The genes are predominantly low in tissue specificity, with broad cellular representation, so the shared signal is unlikely to be explained by a specialized circulating protein compartment. HPA does not support a strong blood-cell explanation because immune-cell specificity is generally low, although a small subset has immune-cell or bone-marrow-associated enrichment. Several genes are cell-type enhanced in oocytes, spermatogenic cells, trophoblast-related cells, and esophageal cells, suggesting that shared cellular states, proliferative or germline-associated programs, or differences in cell composition could contribute to the ovary–stem-cell conservation. Protein detection in ovary is present for many module genes, while no matching HPA tissue is available for stem_cells; therefore, the stem-cell interpretation should not be inferred from HPA protein detection.

**GO/KEGG enrichment**: 19 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP positive regulation of telomere maintenance via telomere lengthening | 0.00227 | CCT5, CCT7, CCT8, DHX36 |
| GO:BP positive regulation of telomere maintenance | 0.00454 | CCT5, CCT7, CCT8, DHX36, GNL3 |
| GO:BP regulation of telomere maintenance via telomere lengthening | 0.00775 | CCT5, CCT7, CCT8, DHX36 |
| GO:CC chaperonin-containing T-complex | 0.00995 | CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 0.00995 | CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 0.00995 | CCT5, CCT7, CCT8 |
| GO:BP regulation of telomere maintenance | 0.0177 | CCT5, CCT7, CCT8, DHX36, GNL3 |
| GO:BP RNA localization to Cajal body | 0.0203 | CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 0.0203 | CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 0.0203 | CCT5, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 0.0203 | CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 0.0203 | CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 0.0203 | CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 0.0203 | CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 0.0203 | CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING shows well-established relationships among CCT5, CCT7, and CCT8, forming a recognizable CCT chaperonin subnetwork, and supports the connection between CCT7 and TUBA1C (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 0.0149), (STRING RCTM Prefoldin mediated transfer of substrate  to CCT/TriC; within-query FDR = 0.0242) (STRING RCTM Formation of tubulin folding intermediates by CCT/TriC; within-query FDR = 0.0242) (STRING RCTM Folding of actin by CCT/TriC; within-query FDR = 0.0242), (STRING Component Chaperonin-containing T-complex; within-query FDR = 0.037) (STRING NetworkNeighborAL Chaperonin TCP-1, conserved site; within-query FDR = 0.0375) (STRING COMPARTMENTS Chaperonin-containing T-complex; within-query FDR = 0.0397). STRING also supports a GNL3–NOLC1 relationship. These known interactions validate part of the module and indicate that the telomere and Cajal-body enrichment is not based solely on isolated genes. The hu.MAP results independently place CCT5, CCT7, and CCT8 together in several CCT-associated complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). Because the module contains only a partial representation of those larger complexes, the co-abundance pattern may capture coordinated regulation of a CCT subassembly or a shared cellular state rather than a complete physical complex. Most other module edges are not represented by high-confidence STRING interactions or hu.MAP complexes, so the module is a mixed network containing a strongly known CCT core and less-characterized co-abundance links.

**STRING interactions (score >= 0.7)**: 5 of 378 gene pairs: CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999); CCT7–TUBA1C (0.722); GNL3–NOLC1 (0.889)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam TCP-1/cpn60 chaperonin family (FDR = 0.0149, 3 genes); Process Positive regulation of telomere maintenance (FDR = 0.0199, 5 genes); Process Positive regulation of telomere maintenance via telomere lengthening (FDR = 0.0199, 4 genes); Process Positive regulation of protein localization to chromosome, telomeric region (FDR = 0.0199, 4 genes); RCTM Prefoldin mediated transfer of substrate  to CCT/TriC (FDR = 0.0242, 4 genes); RCTM Formation of tubulin folding intermediates by CCT/TriC (FDR = 0.0242, 4 genes); RCTM Folding of actin by CCT/TriC (FDR = 0.0242, 3 genes); Process Positive regulation of establishment of protein localization to telomere (FDR = 0.0331, 3 genes); Process Positive regulation of protein localization to Cajal body (FDR = 0.0335, 3 genes); Process Positive regulation of telomerase RNA localization to Cajal body (FDR = 0.0335, 3 genes); Process Binding of sperm to zona pellucida (FDR = 0.0366, 3 genes); Component Chaperonin-containing T-complex (FDR = 0.037, 3 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site (FDR = 0.0375, 3 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 0.0397, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT8, CCT7; 3/23); huMAP3_06559.1 (CCT5, CCT8, CCT7; 3/25); huMAP3_09191.1 (CCT5, CCT8, CCT7; 3/32); huMAP3_10656.1 (CCT5, CCT8, CCT7; 3/36); huMAP3_14584.1 (CCT5, CCT8, CCT7; 3/61); huMAP3_01951.1 (CCT5, CCT7; 2/8)

### Novelty

The underlying molecular biology is not new: the CCT chaperonin relationships, CCT5–CCT7–CCT8 association, GNL3–NOLC1 interaction, and roles of GNL3 or DHX36 in telomere-related biology are already represented in established resources. Accordingly, the module should not be described as a newly discovered protein complex or as proof of a new direct interaction. A potentially novel aspect is the conserved co-abundance of this partial CCT-centered program between ovary and stem_cells, especially the association with less-connected genes such as RGS10, PAWR, KRI1, and CMSS1. However, the supplied evidence does not establish that this tissue-pair co-abundance pattern has not been reported elsewhere. Its novelty is therefore best regarded as a testable network-level observation rather than a demonstrated new mechanism.

**Hypothesis.** Hypothesis: the module represents a conserved cellular-state program in which CCT-mediated folding supports the assembly or stability of proteins involved in nuclear RNA handling and telomere maintenance, while GNL3 and DHX36 connect nucleolar or RNA-associated regulation to chromosome-end biology. In ovary and stem-cell populations, this program may help maintain proliferative competence, genome stability, and specialized nuclear-body function. RGS10 may act as a co-abundance-based state marker or regulatory bridge linking this nuclear and proteostasis program to broader signaling and cytoskeletal features, but the supplied data do not establish a direct biochemical connection. This hypothesis requires validation through perturbation of the CCT subunits, GNL3, or DHX36 followed by measurement of telomere maintenance, telomerase RNA localization, Cajal-body organization, and cell-state phenotypes.

### Important genes

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT8 (0.89), NOLC1 (0.84); STRING partners: CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is part of the central CCT chaperonin core, has direct high-confidence STRING relationships with CCT7 and CCT8, and appears in every listed globally corrected enrichment term (19 globally significant GO/KEGG terms, q_global 0.00227–0.0348; see the table). It is also present in every listed hu.MAP CCT-associated complex (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). Its established protein-folding role and substantial literature support make it the strongest anchor for interpreting the module.
- **Conclusion**: Established evidence supports CCT5 as a molecular chaperone component underlying the module's CCT and telomere-associated signal. The hypothesis that CCT5 abundance directly controls telomerase RNA localization or telomere maintenance in these tissues remains unproven by co-abundance alone.

#### CCT7

- **Related proteins** (co-abundance neighbors): CCT8 (0.85); STRING partners: CCT5 (0.999), CCT8 (0.999), TUBA1C (0.722)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is directly connected to CCT5 and CCT8 in STRING and to TUBA1C, participates in all listed hu.MAP CCT-associated complexes, and shares the complete globally corrected enrichment profile of the CCT core (19 globally significant GO/KEGG terms, q_global 0.00227–0.0348; see the table). Its known role in folding actin and tubulin provides a plausible bridge between proteostasis, cytoskeletal organization, and cell-state regulation.
- **Conclusion**: Established evidence identifies CCT7 as a core chaperonin component and a likely contributor to the module's conserved biological signal. A tissue-specific role for CCT7 in sustaining telomere or germline-associated states is a hypothesis rather than a demonstrated conclusion.

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT5 (0.89), CCT7 (0.85); STRING partners: CCT5 (0.999), CCT7 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 forms the tightly connected CCT subnetwork with CCT5 and CCT7, is present in all listed hu.MAP CCT complexes, and contributes to every globally corrected term (19 globally significant GO/KEGG terms, q_global 0.00227–0.0348; see the table). HPA places it in an oocyte-enhanced cellular context, while its established function concerns CCT-mediated protein folding and telomerase-related nuclear-body processes.
- **Conclusion**: Established evidence supports CCT8 as a central interpretive gene for the module and as part of a known CCT complex rather than an isolated novel factor. Its apparent relevance to the shared ovary–stem-cell state is biologically plausible but still requires tissue-matched functional testing.

#### GNL3

- **Related proteins** (co-abundance neighbors): NUDCD1 (0.90), TUBA1C (0.87), DHX36 (0.87); STRING partners: NOLC1 (0.889)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein nucleolar 3. The protein encoded by this gene may interact with p53 and may be involved in tumorigenesis. The encoded protein also appears to be important for stem cell proliferation. This protein is found in both the nucleus and nucleolus. Three transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Nov 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.357); Abnormality of the skeletal system (0.264); cataract (0.252); trauma complication (0.245); osteoarthritis (0.155)
- **Europe PMC papers**: 959
- **Why important**: GNL3 links the module to stem-cell proliferation and telomere maintenance in its supplied annotations and contributes to the globally corrected telomere and chromosome-organization terms (GO:BP positive regulation of telomere maintenance; q_global = 0.00454), (GO:BP regulation of telomere maintenance; q_global = 0.0177), (GO:BP positive regulation of chromosome organization; q_global = 0.0297). It is connected to DHX36 and TUBA1C in the module and has a known STRING relationship with NOLC1. Its nucleolar localization and substantial literature make it a stronger mechanistic candidate than genes represented only by generic co-abundance.
- **Conclusion**: Established evidence supports GNL3 as a nucleolar and stem-cell-associated regulator compatible with the telomere-centered interpretation. The possibility that GNL3 coordinates the CCT core with telomere or Cajal-body biology in these tissues is a hypothesis, not a demonstrated direct interaction.

#### DHX36

- **Related proteins** (co-abundance neighbors): GNL3 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAH-box helicase 36. This gene is a member of the DEAH-box family of RNA-dependent NTPases which are named after the conserved amino acid sequence Asp-Glu-Ala-His in motif II. The protein encoded by this gene has been shown to enhance the deadenylation and decay of mRNAs with 3'-UTR AU-rich elements (ARE-mRNA). The protein has also been shown to resolve into single strands the highly stable tetramolecular DNA configur…
- **Diseases (Open Targets)**: neurodegenerative disease (0.522); Abnormality of the skeletal system (0.517); Epiretinal membrane (0.388); degeneration of macula and posterior pole (0.383); retinal disorder (0.372)
- **Europe PMC papers**: 1293
- **Why important**: DHX36 contributes to the globally corrected telomere-maintenance and chromosome-organization terms (GO:BP positive regulation of telomere maintenance via telomere lengthening; q_global = 0.00227) (GO:BP positive regulation of telomere maintenance; q_global = 0.00454) (GO:BP regulation of telomere maintenance via telomere lengthening; q_global = 0.00775), (GO:BP regulation of telomere maintenance; q_global = 0.0177), (GO:BP telomere maintenance via telomere lengthening; q_global = 0.0232), (GO:BP positive regulation of chromosome organization; q_global = 0.0297), connects to GNL3 in the module, and is annotated as an RNA helicase capable of resolving guanine-rich DNA structures. Its cell-type enrichment in spermatogenic and trophoblast-related populations makes it relevant to the reproductive and stem-associated context, while its literature supports a credible nucleic-acid mechanism.
- **Conclusion**: Established evidence supports DHX36 as an RNA and nucleic-acid regulator compatible with telomere biology. Its placement downstream of or in direct cooperation with the CCT subnetwork is a hypothesis requiring biochemical and perturbational validation.

#### RGS10

- **Related proteins** (co-abundance neighbors): CLIP1 (0.89), KRI1 (0.88), GCLM (0.87), NUP43 (0.86), CEP170 (0.86), CIAPIN1 (0.84), CLUH (0.84), PSMD9 (0.82), DFFA (0.82), PAWR (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: regulator of G protein signaling 10. Regulator of G protein signaling (RGS) family members are regulatory molecules that act as GTPase activating proteins (GAPs) for G alpha subunits of heterotrimeric G proteins. RGS proteins are able to deactivate G protein subunits of the Gi alpha, Go alpha and Gq alpha subtypes. They drive G proteins into their inactive GDP-bound forms. Regulator of G protein signaling 10 belongs to this family. A…
- **Diseases (Open Targets)**: hair color (0.310); ovarian carcinoma (0.104); ovarian cancer (0.101); Parkinson disease (0.100); type 2 diabetes mellitus (0.094)
- **Europe PMC papers**: 765
- **Why important**: RGS10 has the strongest network connectivity in the supplied module and links several otherwise weakly connected branches, including CLIP1, KRI1, GCLM, NUP43, CEP170, CIAPIN1, CLUH, and PSMD9. Its established function is regulation of heterotrimeric G-protein signaling, and HPA indicates lymphoid-tissue enhancement with several cell-type contexts. Although it has no globally corrected term, STRING relationship, or hu.MAP complex assignment in this module, its network position makes it a useful candidate for testing how signaling state may influence the CCT-centered program.
- **Conclusion**: Established evidence supports RGS10 as a signaling regulator and a topological connector within the co-abundance network, but not as a proven component of the CCT or telomere machinery. Its role as a signaling-to-nuclear-state bridge is a hypothesis based on network position and should not be treated as established mechanism.

## Module 9

**Tissue pair**: ovary and stem_cells  
**Genes (11)**: FASN, EIF4G1, NIP7, RCC1, RRS1, SF3A1, SURF6, QARS1, TCOF1, TPD52, YTHDF2

### Function

The module is most consistent with a broadly expressed RNA and protein-production program, with contributions from pre-rRNA processing, ribosome biogenesis, pre-mRNA splicing, translation and cell-cycle control. This interpretation is supported by the functions of RRS1, NIP7 and SURF6 in nucleolar ribosome biogenesis, SF3A1 in spliceosome assembly, EIF4G1 in translation initiation, RCC1 in mitotic control, and QARS1 in translation-related tRNA aminoacylation. FASN adds a lipid-biosynthetic and metabolic component, while TCOF1 provides an additional ribosome-biogenesis connection and TPD52 provides a possible cell-population and B-cell-related component. No GO or KEGG term passed global correction. Therefore, this is a biologically coherent interpretation of the gene functions and network, not a claim of statistically significant pathway enrichment. The absence of globally enriched terms does not invalidate the module.

**Cell composition.** The module is not a plasma-protein or secreted-protein module: no member is annotated as secreted. Most members have low tissue specificity and low immune-cell specificity, and protein detection in ovary is common among the genes with available HPA evidence. This favors a broadly expressed cellular program rather than a blood-contamination signature. The module is nevertheless strongly heterogeneous at the single-cell annotation level, with cell-type-enhanced signals involving late spermatids, epithelial cells, B-cells and progenitor-like populations. FASN is tissue-enhanced in adipose tissue, breast and liver, and TPD52 is immune-cell-enhanced in memory B-cells, so sample composition or shared cell states could contribute to part of the co-abundance pattern. HPA provides no matching stem-cell tissue annotation, so the stem-cell interpretation cannot be validated from that tissue-level HPA comparison.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The clearest known interaction-supported core is the nucleolar relationship among NIP7, RRS1 and SURF6. Their STRING links are strong and agree with their annotated roles in ribosome assembly or biogenesis, making this portion of the module more plausibly anchored in known molecular biology. The remaining co-abundance links are not represented by STRING partners in the fact sheet, so they should not be treated as established physical interactions. No hu.MAP complex contains multiple module members. Thus, the module combines a known nucleolar interaction neighborhood with co-abundance relationships that may reflect shared regulation, shared cell state or indirect functional coupling rather than one confirmed multiprotein complex.

**STRING interactions (score >= 0.7)**: 3 of 55 gene pairs: NIP7–RRS1 (0.987); NIP7–SURF6 (0.782); RRS1–SURF6 (0.949)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact conserved ovary and stem-cell co-abundance module may represent a useful new systems-level observation because its full gene combination is not captured as a shared hu.MAP complex and most of its pairwise relationships are not listed as STRING partners. However, it cannot be called a definitively new biological pathway. Several component functions are already established, especially ribosome biogenesis, RNA processing, translation and lipid synthesis, and absence from STRING or hu.MAP alone does not establish novelty. The defensible novelty claim is therefore the cross-tissue co-abundance organization and its apparent coupling of these processes, pending replication and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a shared high-demand biosynthetic cell state in ovary and stem-cell samples. Coordinated nucleolar activity involving RRS1, NIP7, SURF6 and TCOF1 could support ribosome production, while SF3A1 and EIF4G1 could coordinate maturation and translation of transcripts needed for growth or differentiation. RCC1 may connect this state to cell-cycle organization, and FASN could supply lipid biosynthesis required for membrane production or metabolic adaptation. YTHDF2 could contribute post-transcriptional RNA regulation. The network data support coordinated abundance, but do not establish direct regulation, causality or a single physical complex.

### Important genes

#### EIF4G1

- **Related proteins** (co-abundance neighbors): RRS1 (0.87), SF3A1 (0.84), YTHDF2 (0.81), FASN (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 has the strongest network connectivity in the module and links translation initiation to SF3A1, YTHDF2, FASN and RRS1 in the co-abundance graph. Its established role as the EIF4F scaffold makes it a plausible integrator of transcript availability and protein synthesis. It is broadly expressed, detected in ovary, and has extensive literature and disease annotation, so it is both mechanistically informative and experimentally tractable.
- **Conclusion**: Established evidence supports EIF4G1 as a translation-initiation scaffold and a central co-abundance connector. It is a strong candidate module marker. It remains a hypothesis that EIF4G1 drives the shared ovary and stem-cell module rather than merely responding to the same cellular state.

#### RRS1

- **Related proteins** (co-abundance neighbors): EIF4G1 (0.87), TCOF1 (0.84); STRING partners: NIP7 (0.987), SURF6 (0.949)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: regulator of ribosome synthesis 1. Enables 5S rRNA binding activity. Involved in several processes, including mitotic metaphase plate congression; protein localization to nucleolus; and ribosomal large subunit assembly. Located in condensed nuclear chromosome; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.473); post term pregnancy (0.229); breast cancer (0.111); breast carcinoma (0.101); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 1546
- **Why important**: RRS1 connects EIF4G1 and TCOF1 in the module and is part of the strongest known STRING-linked nucleolar neighborhood with NIP7 and SURF6. Its established functions in ribosome biogenesis, large-subunit assembly and nucleolar localization directly support the proposed RNA-production axis. It is detected in ovary and has substantial literature and disease annotation.
- **Conclusion**: Established evidence identifies RRS1 as a biologically plausible anchor for the nucleolar component of the module. The module data support its association with the shared program, but do not show that RRS1 is the upstream controller of the co-abundance pattern.

#### NIP7

- **Related proteins** (co-abundance neighbors): SF3A1 (0.83); STRING partners: RRS1 (0.987), SURF6 (0.782)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleolar pre-rRNA processing protein NIP7. Enables RNA binding activity. Predicted to be involved in ribosomal large subunit biogenesis. Located in cytosol; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.471); COG8-congenital disorder of glycosylation (0.118); liposarcoma (0.035); arthropathy (0.023); chronic obstructive pulmonary disease (0.021)
- **Europe PMC papers**: 392
- **Why important**: NIP7 is directly connected in STRING to RRS1 and SURF6, forming the most coherent known interaction neighborhood in the module. Its annotated role in pre-rRNA processing and large-subunit biogenesis gives it a specific mechanistic link to the nucleolar interpretation. Although its literature is less extensive than that of EIF4G1 or FASN, its functional specificity makes it valuable for testing the module.
- **Conclusion**: Established evidence supports NIP7 as a ribosome-biogenesis component and part of a known nucleolar interaction group. Its centrality to the proposed shared program is a hypothesis that requires perturbation or localization experiments.

#### SF3A1

- **Related proteins** (co-abundance neighbors): SURF6 (0.86), EIF4G1 (0.84), NIP7 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 is one of the more connected genes in the co-abundance graph and links the nucleolar genes NIP7 and SURF6 with EIF4G1. Its established role in U2 snRNP and spliceosome assembly provides the RNA-processing arm of the module. It is detected in ovary and has substantial literature and disease annotation.
- **Conclusion**: Established evidence supports SF3A1 as a core pre-mRNA-splicing factor. Its co-abundance with ribosome-biogenesis and translation genes suggests coordinated RNA handling, but does not demonstrate direct coupling between splicing and nucleolar activity.

#### FASN

- **Related proteins** (co-abundance neighbors): QARS1 (0.88), RCC1 (0.82), EIF4G1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fatty acid synthase. The enzyme encoded by this gene is a multifunctional protein. Its main function is to catalyze the synthesis of palmitate from acetyl-CoA and malonyl-CoA, in the presence of NADPH, into long-chain saturated fatty acids. In some cancer cell lines, this protein has been found to be fused with estrogen receptor-alpha (ER-alpha), in which the N-terminus of FAS is fused in-frame with the C-terminus of …
- **Diseases (Open Targets)**: dengue disease (0.469); autism spectrum disorder (0.333); Parkinson disease (0.295); Epileptic encephalopathy (0.211); neurodegenerative disease (0.205)
- **Europe PMC papers**: 21528
- **Why important**: FASN connects the metabolic branch of the graph to EIF4G1 and also links with QARS1 and RCC1. Its established enzymatic role in palmitate synthesis makes it the clearest metabolic counterpart to the RNA and translation genes. It has extensive literature, strong disease and cancer relevance, and distinctive HPA tissue enhancement in adipose tissue, breast and liver.
- **Conclusion**: Established evidence supports FASN as a lipid-biosynthetic enzyme with a distinctive tissue expression pattern. Its membership may indicate metabolic coupling or sample-specific cell composition; the claim that FASN functionally supports the shared module is a hypothesis.

## Module 10

**Tissue pair**: ovary and stem_cells  
**Genes (6)**: HDGF, HYPK, NUDT5, PFDN6, PSME3IP1, ADSS2

### Function

No GO or KEGG term passed global correction, and there were no supplementary STRING enrichment terms. Therefore, the module does not support a statistically established pathway-level function from enrichment analysis. Its gene annotations instead suggest a possible shared cellular program involving nuclear protein regulation, protein folding and stabilization, nucleotide metabolism, chromatin-related processes, and cell proliferation or survival. PSME3IP1 is the central co-abundance hub, while the other genes connect to it without known high-confidence STRING relationships. These annotations support functional themes, not a formally enriched module function.

**Cell composition.** The module is not predominantly composed of secreted or plasma proteins: only HDGF is annotated as secreted to blood, while the remaining genes are intracellular or nuclear/cytosolic proteins. HPA reports low tissue specificity for every module gene and low immune-cell specificity for every module gene, with no enriched tissue pattern. Cell-type annotations are heterogeneous, including germ-cell, progenitor, glial, neutrophil, Hofbauer-cell, and megakaryocyte-related signals. This argues against a clear ovary-specific program and does not strongly support a blood-cell contamination explanation, although the secreted HDGF signal and the heterogeneous cell-type associations mean sample cellular composition cannot be excluded. Protein detection in ovary is mixed, and there is no matching HPA tissue for stem cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair has a high-confidence STRING interaction, and no hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not corroborated by these protein-interaction or complex resources. The network may reflect coordinated expression, shared regulation, cell-state composition, or incompletely characterized biology rather than a known physical complex. PSME3IP1 is the network hub in the supplied co-abundance graph, but its apparent centrality is not independently supported by STRING or hu.MAP.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unrecognized co-abundance association, because its internal relationships are absent from the supplied STRING and hu.MAP resources and its genes do not form a globally enriched GO or KEGG pathway. However, this is not sufficient to claim a new biological mechanism. The genes themselves have established functions and substantial literature, particularly HDGF, HYPK, NUDT5, PFDN6, and ADSS2. The strongest defensible novelty claim is that their coordinated abundance in the conserved ovary and stem-cell module is not explained by the currently supplied interaction, complex, or enrichment evidence.

**Hypothesis.** Hypothesis: the module reflects a coordinated cellular maintenance state centered on PSME3IP1, coupling protein quality control and stabilization with nuclear regulation, chromatin-associated metabolism, and nucleotide supply. PFDN6 and HYPK could represent protein-folding or protein-stability components; ADSS2 and NUDT5 could support nucleotide and modified-nucleotide homeostasis; HDGF could connect this state to proliferation, differentiation, and chromatin-related regulation. This model is provisional because there is no globally significant enrichment, no STRING support, and no hu.MAP complex containing multiple members. An alternative explanation is coordinated expression caused by shared cell-state or sample-composition effects.

### Important genes

#### PSME3IP1

- **Related proteins** (co-abundance neighbors): PFDN6 (0.83), ADSS2 (0.82), HYPK (0.82), HDGF (0.82), NUDT5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome activator subunit 3 interacting protein 1. Involved in negative regulation of proteasomal protein catabolic process and negative regulation of protein binding activity. Located in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.074); osteoporosis (0.060); arthritic joint disease (0.026); placenta praevia (0.022); Alzheimer disease (0.011)
- **Europe PMC papers**: 18
- **Why important**: PSME3IP1 is the central node in the supplied co-abundance subgraph and is connected to every other module member. Its annotations include negative regulation of proteasomal protein catabolism, negative regulation of protein binding, and spliceosome-related mRNA splicing. It therefore provides the strongest network-based link between the module’s protein-regulatory and nuclear themes. Its literature volume is limited relative to several other members, making the conserved co-abundance association potentially informative.
- **Conclusion**: Established evidence supports PSME3IP1 as the module’s co-abundance hub and as a protein-regulatory nuclear factor. It is reasonable to hypothesize that it coordinates the module, but a direct molecular organizing role is not established because STRING and hu.MAP provide no corroborating relationship.

#### HDGF

- **Related proteins** (co-abundance neighbors): PSME3IP1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparin binding growth factor. This gene encodes a member of the hepatoma-derived growth factor family. The encoded protein has mitogenic and DNA-binding activity and may play a role in cellular proliferation and differentiation. High levels of expression of this gene enhance the growth of many tumors. This gene was thought initially to be located on chromosome X; however, that location has been determined to correspond to a re…
- **Diseases (Open Targets)**: prostate carcinoma (0.394); neurodegenerative disease (0.287); hepatocellular carcinoma (0.115); neoplasm (0.112); non-small cell lung carcinoma (0.111)
- **Europe PMC papers**: 2439
- **Why important**: HDGF combines a direct connection to the network hub with annotations involving chromatin remodeling, transcriptional regulation, nuclear localization, signal transduction, cell division, proliferation, and differentiation. It is detected in ovary and is the only module gene annotated as secreted to blood. It also has the largest literature volume among the module genes and multiple cancer-related disease associations, making it an important biological and interpretive anchor.
- **Conclusion**: Established evidence supports HDGF as a nuclear and potentially secreted growth-related factor associated with proliferation and differentiation. Its participation in the module may indicate a growth or progenitor-state component, but the module data do not establish that HDGF drives the coordinated pattern or that secretion mediates it.

#### HYPK

- **Related proteins** (co-abundance neighbors): PSME3IP1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: huntingtin interacting protein K. Enables protein N-terminus binding activity. Involved in negative regulation of apoptotic process and protein stabilization. Located in cytoplasm; microtubule cytoskeleton; and nucleoplasm. Part of protein-containing complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.226); Huntington disease (0.033); non-alcoholic fatty liver (0.022); diverticular disease (0.019); juvenile Huntington disease (0.014)
- **Europe PMC papers**: 364
- **Why important**: HYPK connects to PSME3IP1 and is annotated with protein folding, protein stabilization, and negative regulation of apoptosis. It occupies a biologically plausible position between proteostasis and cell survival, and it has a substantial literature record with associations involving neurodegenerative and Huntington disease contexts. Its HPA cell-type pattern is group-enriched in several neural and glial populations, emphasizing that the module is not narrowly ovary-specific.
- **Conclusion**: Established evidence supports HYPK as a protein-stability and apoptosis-related factor. Its co-abundance with PSME3IP1 is consistent with a proteostasis interpretation, but any direct role in an ovary or stem-cell maintenance program remains a hypothesis.

#### PFDN6

- **Related proteins** (co-abundance neighbors): PSME3IP1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prefoldin subunit 6. PFDN6 is a subunit of the heteromeric prefoldin complex that chaperones nascent actin (see MIM 102560) and alpha- and beta-tubulin (see MIM 602529 and MIM 191130, respectively) chains pending their transfer to the cytosolic chaperonin containing TCP1 (MIM 186980) (CCT) complex (Hansen et al., 1999 [PubMed 10209023]).[supplied by OMIM, Jul 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.472); colorectal carcinoma (0.074); neoplasm (0.056); hemoglobin D disease (0.046); dehydrated hereditary stomatocytosis (0.043)
- **Europe PMC papers**: 230
- **Why important**: PFDN6 is a prefoldin subunit that participates in chaperoning nascent actin and tubulin for transfer to the cytosolic chaperonin system. It connects to the central PSME3IP1 node and is detected in ovary. Its annotations provide a concrete proteostasis and cytoskeletal-folding mechanism that complements HYPK and the protein-regulatory annotation of PSME3IP1.
- **Conclusion**: Established evidence supports PFDN6 as a component of prefoldin-mediated protein folding and stabilization. Its inclusion is compatible with a shared proteostasis state, but the module does not demonstrate a physical PFDN6–PSME3IP1 interaction or a specialized reproductive function.

#### ADSS2

- **Related proteins** (co-abundance neighbors): PSME3IP1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenylosuccinate synthase 2. This gene encodes the enzyme adenylosuccinate synthetase which catalyzes the first committed step in the conversion of inosine monophosphate to adenosine monophosphate. A pseudogene of this gene is found on chromosome 17.[provided by RefSeq, Nov 2010].
- **Diseases (Open Targets)**: atopic eczema (0.085); respiratory tract infectious disorder (0.077); dermatomycosis (0.062); hyperlipoproteinemia type V (0.056); LCAT deficiency (0.054)
- **Europe PMC papers**: 102
- **Why important**: ADSS2 connects to PSME3IP1 and catalyzes a committed step in AMP biosynthesis. Its annotations also include purine nucleotide biosynthesis, immune-system process, and responses to purine-containing compounds. It contributes a plausible metabolic dimension to a module otherwise rich in protein regulation and chromatin-associated processes, and it is detected in ovary.
- **Conclusion**: Established evidence supports ADSS2 as a purine and AMP-biosynthesis enzyme. Its co-abundance may reflect nucleotide demand in a proliferative or metabolically active cell state, but that interpretation is not proven and should not be presented as pathway enrichment.

#### NUDT5

- **Related proteins** (co-abundance neighbors): PSME3IP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nudix hydrolase 5. This gene belongs to the Nudix (nucleoside diphosphate linked moiety X) hydrolase superfamily. The encoded enzyme catalyzes the hydrolysis of modified nucleoside diphosphates, including ADP-ribose (ADPR) and 8-oxoGua-containing 8-oxo-dADP and 8-oxo-dGDP. Protein-bound ADP ribose can be hazardous to the cell because it can modify some amino acid residues, resulting in the inhibition of ATP-activate…
- **Diseases (Open Targets)**: neurodegenerative disease (0.513); type 2 diabetes mellitus (0.332); coronary artery disorder (0.324); gout (0.315); diabetic neuropathy (0.315)
- **Europe PMC papers**: 847
- **Why important**: NUDT5 connects to PSME3IP1 and hydrolyzes modified nucleoside diphosphates, including ADP-ribose and oxidized guanine-containing nucleotides. Its annotations include nucleotide metabolism, ribose-phosphate metabolism, and chromatin remodeling. This makes it a strong candidate for linking nucleotide quality control with nuclear regulation, and it has a substantial literature record with metabolic, neurological, cardiovascular, and gout-related disease associations.
- **Conclusion**: Established evidence supports NUDT5 as a modified-nucleotide and nucleotide-quality-control enzyme with chromatin-related annotation. Its presence supports a possible metabolic-proteostatic interpretation of the module, but the supplied data do not establish that it functionally cooperates with the other genes.

## Module 11

**Tissue pair**: ovary and stem_cells  
**Genes (12)**: KPNA2, KIF2A, KIFC1, MCM5, MCM7, MAT2A, NASP, AARS1, TXLNA, TXLNG, UBE2C, UBE2T

### Function

The strongest interpretation is a proliferative, chromosome-maintenance and mitotic-cell-state module, with linked protein ubiquitination, nuclear transport, microtubule, and vesicle-trafficking components. The MCM5–MCM7 relationship and the associated hu.MAP complexes support a DNA-replication initiation and replication-fork context, while UBE2C, KIFC1 and KIF2A support mitotic progression, spindle function and chromosome segregation. UBE2T adds a DNA-damage-response and ubiquitin-conjugation connection, and KPNA2 links the module to nuclear import. STRING supplementary terms support cell-cycle and ATP-binding themes (STRING Keyword Cell cycle; within-query FDR = 0.00094) (STRING Keyword ATP-binding; within-query FDR = 0.0072), while the TXLNA–TXLNG pair supports a taxilin/coiled-coil component (STRING Pfam Myosin-like coiled-coil protein; within-query FDR = 0.0479). No GO/KEGG term passed global correction; therefore the functional interpretation rests on the coherent gene-level annotations, network structure, STRING evidence and hu.MAP evidence rather than on a globally significant enrichment term.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly intracellular, including nucleoplasmic, centrosomal and cytosolic proteins. The module is not broadly immune-cell specific, although some genes are enhanced in bone marrow, lymphoid tissue, erythrocyte progenitors, megakaryocyte progenitors, trophoblast populations and other proliferative cell types. This pattern is compatible with a shared proliferative or progenitor-like cell state in ovary and stem-cell samples, and may also reflect shared cellular composition rather than a tissue-exclusive ovarian program. The HPA protein evidence in ovary is incomplete, and there is no matching HPA tissue for the stem-cell sample, so tissue-level absence or presence should be interpreted cautiously.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING contains established high-confidence relationships within several recognizable substructures: MCM5–MCM7 and MCM7–NASP connect replication and histone-handling biology; UBE2C–UBE2T connects ubiquitin-conjugating enzymes; UBE2C–KIFC1 and KIFC1–KPNA2 connect mitotic, motor and nuclear-import biology; and TXLNA–TXLNG supports a taxilin pair. The STRING supplementary cell-cycle and ATP-binding terms (STRING Keyword Cell cycle; within-query FDR = 0.00094) (STRING Keyword ATP-binding; within-query FDR = 0.0072) reinforce, but do not globally validate, the module interpretation. hu.MAP independently recovers the TXLNA–TXLNG pair (hu.MAP huMAP3_02956.1) (hu.MAP huMAP3_13619.1), the KPNA2–KIFC1 nuclear-transport and nuclear-pore context (hu.MAP huMAP3_07479.1) (hu.MAP huMAP3_08226.1) (hu.MAP huMAP3_09825.1) (hu.MAP huMAP3_10000.1) (hu.MAP huMAP3_12581.1), multiple MCM5–MCM7 replication-complex contexts (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1), and an AARS1–UBE2T context (hu.MAP huMAP3_14442.1). These complexes usually contain only a subset of the module members, so the result is best viewed as a co-abundance module assembled from several connected known subcomplexes rather than as one experimentally established physical complex.

**STRING interactions (score >= 0.7)**: 7 of 66 gene pairs: KIFC1–KPNA2 (0.731); KIFC1–UBE2C (0.839); KPNA2–UBE2C (0.806); MCM5–MCM7 (0.999); MCM7–NASP (0.81); TXLNA–TXLNG (0.853); UBE2C–UBE2T (0.794)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Cell cycle (FDR = 0.00094, 7 genes); Keyword ATP-binding (FDR = 0.0072, 8 genes); Pfam Myosin-like coiled-coil protein (FDR = 0.0479, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02956.1 (TXLNA, TXLNG; 2/4); huMAP3_13619.1 (TXLNA, TXLNG; 2/5); huMAP3_07479.1 (KPNA2, KIFC1; 2/6); huMAP3_05529.1 (MCM5, MCM7; 2/6); huMAP3_08226.1 (KPNA2, KIFC1; 2/11); huMAP3_09238.1 (MCM5, MCM7; 2/11); huMAP3_11119.1 (MCM5, MCM7; 2/14); huMAP3_14758.1 (MCM5, MCM7; 2/14); huMAP3_08554.1 (MCM5, MCM7; 2/15); huMAP3_11832.1 (MCM5, MCM7; 2/15); huMAP3_12180.1 (MCM5, MCM7; 2/17); huMAP3_09825.1 (KPNA2, KIFC1; 2/27); huMAP3_10000.1 (KPNA2, KIFC1; 2/44); huMAP3_14442.1 (AARS1, UBE2T; 2/57); huMAP3_12581.1 (KPNA2, KIFC1; 2/58)

### Novelty

The exact cross-tissue co-abundance pattern could be a potentially new systems-level observation, but the module cannot be called a newly discovered molecular complex or pathway. Several of its relationships and subassemblies are already represented in STRING and hu.MAP, especially the MCM, taxilin, nuclear-transport and ubiquitin-related components. Conversely, absence of a complete module-level match in those resources would not prove novelty, because database coverage and complex membership are incomplete and co-abundance is not equivalent to direct physical interaction. The defensible conclusion is that the biological combination and its conservation between ovary and stem cells may merit follow-up, but novelty remains unestablished without comparison to published co-expression modules and independent datasets.

**Hypothesis.** Hypothesis: the shared module marks a proliferative progenitor-like state in which increased genome-replication capacity and histone handling are coordinated with mitotic spindle activity, regulated protein turnover, and nuclear import. MCM5, MCM7 and NASP could support replication and chromatin assembly; UBE2C and UBE2T could coordinate cell-cycle protein turnover and DNA-damage-linked ubiquitination; KIFC1 and KIF2A could organize mitotic microtubules; KPNA2 could control nuclear entry of cell-cycle or replication regulators; and TXLNA/TXLNG could represent a linked trafficking or cytoskeletal regulatory arm. The HPA pattern suggests that this state may be shared by proliferating progenitor or trophoblast-like cells rather than being specific to ovarian tissue. This is a mechanistic model, not a demonstrated causal pathway.

### Important genes

#### MCM7

- **Related proteins** (co-abundance neighbors): NASP (0.84), KPNA2 (0.84); STRING partners: MCM5 (0.999), NASP (0.81)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_09238.1, huMAP3_11119.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 is a central replication-related anchor: it connects to MCM5 and NASP in STRING and appears with MCM5 across multiple hu.MAP replication complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1). Its annotations directly support replication initiation, replication-fork biology and DNA-damage response. It is enhanced in bone marrow and several progenitor or trophoblast cell types, and it has extensive literature support.
- **Conclusion**: Established evidence supports MCM7 as a replication and proliferative-state marker in this module. It is a strong candidate for the module's genome-maintenance axis. It is not established that MCM7 drives the shared ovary–stem-cell co-abundance pattern.

#### UBE2C

- **Related proteins** (co-abundance neighbors): UBE2T (0.84), KIFC1 (0.82); STRING partners: KIFC1 (0.839), KPNA2 (0.806), UBE2T (0.794)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin conjugating enzyme E2 C. The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, ubiquitin-conjugating enzymes, and ubiquitin-protein ligases. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. The encoded protein is required …
- **Diseases (Open Targets)**: neurodegenerative disease (0.497); hepatocellular carcinoma (0.126); non-small cell lung carcinoma (0.125); breast carcinoma (0.120); neoplasm (0.118)
- **Europe PMC papers**: 4459
- **Why important**: UBE2C is a network bridge between the ubiquitin-conjugation and mitotic-motor portions of the module, with STRING relationships to KIFC1, KPNA2 and UBE2T. STRING places it in the supplementary cell-cycle and ATP-binding signals (STRING Keyword Cell cycle; within-query FDR = 0.00094) (STRING Keyword ATP-binding; within-query FDR = 0.0072). Its established functions include mitotic cyclin destruction, mitotic exit and metaphase-to-anaphase regulation. Its bone-marrow and lymphoid-tissue enhancement and its association with proliferative cell types fit the proposed cell-state interpretation, and it has extensive literature support.
- **Conclusion**: Established evidence supports UBE2C as a key cell-cycle and proteostasis component. Its position makes it a plausible integrator of mitotic progression with ubiquitin-dependent turnover, but a causal role in this conserved module remains a hypothesis.

#### KIFC1

- **Related proteins** (co-abundance neighbors): TXLNA (0.84), UBE2C (0.82); STRING partners: KPNA2 (0.731), UBE2C (0.839)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Centrosome; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07479.1, huMAP3_08226.1, huMAP3_09825.1, huMAP3_10000.1, huMAP3_12581.1
- **Function (MyGene.info)**: kinesin family member C1. Predicted to enable microtubule binding activity and minus-end-directed microtubule motor activity. Involved in mitotic metaphase plate congression and mitotic spindle assembly. Located in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.118); neoplasm (0.116); cancer (0.108); triple-negative breast carcinoma (0.107); breast cancer (0.104)
- **Europe PMC papers**: 1342
- **Why important**: KIFC1 links the taxilin arm through TXLNA with the ubiquitin and nuclear-import arms through UBE2C and KPNA2. STRING supports these relationships, and hu.MAP repeatedly places KIFC1 with KPNA2 in nuclear-transport, nuclear-pore and mitosis-associated complexes (hu.MAP huMAP3_07479.1) (hu.MAP huMAP3_08226.1) (hu.MAP huMAP3_09825.1) (hu.MAP huMAP3_10000.1) (hu.MAP huMAP3_12581.1). Its annotations support spindle assembly, metaphase alignment, chromosome segregation and microtubule-based movement. It is enhanced in bone marrow, lymphoid tissue and multiple progenitor or trophoblast populations, with substantial disease and cancer literature.
- **Conclusion**: Established evidence supports KIFC1 as the module's mitotic microtubule connector. Its network position makes it a particularly informative candidate for testing whether the module reflects active mitosis rather than generic housekeeping expression.

#### KPNA2

- **Related proteins** (co-abundance neighbors): UBE2T (0.88), MCM7 (0.84), MCM5 (0.80); STRING partners: KIFC1 (0.731), UBE2C (0.806)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07479.1, huMAP3_08226.1, huMAP3_09825.1, huMAP3_10000.1, huMAP3_12581.1
- **Function (MyGene.info)**: karyopherin subunit alpha 2. The import of proteins into the nucleus is a process that involves at least 2 steps. The first is an energy-independent docking of the protein to the nuclear envelope and the second is an energy-dependent translocation through the nuclear pore complex. Imported proteins require a nuclear localization sequence (NLS) which generally consists of a short region of basic amino acids or 2 such regions s…
- **Diseases (Open Targets)**: severe acute respiratory syndrome (0.462); Orthomyxoviridae infectious disease (0.462); dengue disease (0.462); COVID-19 (0.373); non-alcoholic fatty liver (0.324)
- **Europe PMC papers**: 2442
- **Why important**: KPNA2 has strong module connectivity and links UBE2T, MCM7 and MCM5 in the co-abundance graph. It is represented with KIFC1 in several hu.MAP nuclear-transport and nuclear-pore contexts (hu.MAP huMAP3_07479.1) (hu.MAP huMAP3_08226.1) (hu.MAP huMAP3_09825.1) (hu.MAP huMAP3_10000.1) (hu.MAP huMAP3_12581.1). Its established function in import of nuclear-localization-signal-bearing proteins provides a plausible mechanism for coordinating replication and mitotic regulators. HPA links it to germ-cell and trophoblast populations, and it has substantial literature support.
- **Conclusion**: Established evidence supports KPNA2 as a nuclear-import component that may connect otherwise distinct module arms. Its involvement in coordinating the shared proliferative state is plausible but not demonstrated by the supplied data.

#### UBE2T

- **Related proteins** (co-abundance neighbors): MAT2A (0.92), KPNA2 (0.88), UBE2C (0.84); STRING partners: UBE2C (0.794)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: ubiquitin conjugating enzyme E2 T. The protein encoded by this gene catalyzes the covalent attachment of ubiquitin to protein substrates. Defects in this gene have been associated with Fanconi anemia of complementation group T. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2015].
- **Diseases (Open Targets)**: Fanconi anemia (0.792); myelodysplastic syndrome (0.482); acute myeloid leukemia (0.463); hepatocellular carcinoma (0.125); lung adenocarcinoma (0.117)
- **Europe PMC papers**: 1818
- **Why important**: UBE2T is a highly connected module member linking MAT2A, KPNA2 and UBE2C. STRING supports its relationship with UBE2C (STRING Keyword ATP-binding; within-query FDR = 0.0072), and hu.MAP places UBE2T with AARS1 in a broader protein-associated context (hu.MAP huMAP3_14442.1). Its established functions include ubiquitin conjugation and DNA-damage response, and its disease associations include Fanconi anemia and hematologic disorders. Its progenitor-associated HPA pattern and substantial literature make it relevant to a replication-stress or genome-maintenance interpretation.
- **Conclusion**: Established evidence supports UBE2T as a DNA-repair and ubiquitin-conjugation component. It may couple replication stress to proteostasis in this module, but the specific coupling to the other module members remains a hypothesis.

## Module 12

**Tissue pair**: ovary and stem_cells  
**Genes (5)**: MIER1, METTL3, PXN, PDCL3, SEH1L

### Function

No GO/KEGG term passed global correction, and there are no supplementary STRING enrichment terms. The module therefore does not support a statistically established canonical pathway assignment. Its gene content is functionally heterogeneous: PXN supports focal-adhesion and actin–membrane attachment, PDCL3 is linked to heterotrimeric G-protein regulation and actin organization, SEH1L belongs to the nuclear-pore and mitotic chromosome-alignment machinery, METTL3 catalyzes mRNA N6-adenosine methylation, and MIER1 regulates transcription and chromatin-related processes. The co-abundance pattern is consequently more consistent with a coordinated cellular state involving adhesion or cytoskeletal organization together with nuclear, RNA-processing, and transcriptional regulation than with a demonstrated single pathway.

**Cell composition.** The module is not dominated by classical plasma or secreted proteins, although the HPA summary reports one secreted gene. Most genes have low tissue specificity, so the module is broadly expressed rather than ovary-specific. Several genes show cell-type-enhanced patterns, including neutrophils or neutrophil progenitors, germ-cell populations, oocytes, undifferentiated spermatogonia, and extravillous trophoblasts. One gene is tissue-enhanced in bone marrow, while only one gene is immune-cell enhanced and most have low immune-cell specificity. This pattern raises the possibility that the shared signal reflects common cell states, cellular composition, or blood-related material in samples rather than a dedicated ovary–stem-cell program. HPA protein detection is limited in ovary and unavailable for a matching stem-cell tissue, so tissue-level protein confirmation is incomplete.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, no STRING functional-enrichment term is reported, and no hu.MAP complex contains multiple module members. Thus the co-abundance edges should not be interpreted as established physical interactions or as membership in a known multiprotein complex. Established relationships instead come from the individual annotations: PXN is a focal-adhesion scaffold, PDCL3 is a putative G-protein modulator, SEH1L is a nucleoporin, METTL3 is the catalytic component of the mRNA methyltransferase machinery, and MIER1 is a transcriptional regulator. The absence of database-supported interactions weakens a direct molecular-complex interpretation and favors a model of coordinated regulation or shared cellular-state dependence.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact shared co-abundance configuration may represent a new observation because it is not represented as a known STRING interaction set or hu.MAP complex. However, absence from those resources does not establish biological novelty: the genes have well-established individual functions, and co-abundance can arise from shared cell composition, regulatory state, or technical structure. The lack of globally significant GO/KEGG enrichment also prevents claiming discovery of a new pathway. A novelty claim would require replication in independent ovary and stem-cell datasets, control for cell-type composition and blood contamination, and experimental testing of whether the observed relationships are reproducible and mechanistically connected.

**Hypothesis.** Hypothesis: this module marks a shared, heterogeneous cellular state in which adhesion and cytoskeletal signaling are coordinated with nuclear transport, transcriptional regulation, and RNA methylation. PXN could represent the adhesion-associated readout, while PDCL3 may connect cytoskeletal or signaling behavior to MIER1-dependent transcriptional regulation. METTL3 could modulate the stability or translation of transcripts involved in this state, and SEH1L could reflect accompanying changes in nuclear transport or proliferation. An alternative hypothesis is that the pattern is driven largely by shared cell populations, especially neutrophil-related or germ-cell-related states, rather than by direct regulation among the encoded proteins. These possibilities should be tested by cell-composition adjustment, single-cell or spatial validation, and perturbation of the candidate regulatory genes.

### Important genes

#### PXN

- **Related proteins** (co-abundance neighbors): SEH1L (0.84), METTL3 (0.83), PDCL3 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Focal adhesion sites; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: paxillin. This gene encodes a cytoskeletal protein involved in actin-membrane attachment at sites of cell adhesion to the extracellular matrix (focal adhesion). Alternatively spliced transcript variants encoding different isoforms have been described for this gene. These isoforms exhibit different expression pattern, and have different biochemical, as well as physiological properties (PMID:9054445). [provid…
- **Diseases (Open Targets)**: atrial fibrillation (0.421); Abnormality of the skeletal system (0.342); Dupuytren Contracture (0.283); cardiac arrhythmia (0.275); hypertrophic cardiomyopathy (0.265)
- **Europe PMC papers**: 3057
- **Why important**: PXN is the most connected organizing point in the module, linking SEH1L, METTL3, and PDCL3 in the co-abundance graph. Its established role in focal adhesions, actin–membrane attachment, cell adhesion, migration, and cell spreading gives the module a plausible cytoskeletal and adhesion-related anchor. It is detected in ovary and has cell-type-enhanced HPA patterns involving neutrophils and extravillous trophoblasts. It also has a substantial literature base and disease associations involving structural and cardiac phenotypes.
- **Conclusion**: Established evidence supports PXN as an adhesion and cytoskeletal scaffold and as the principal network connector in this module. It is a plausible marker of the shared cellular state. It is not established that PXN physically regulates the other module genes here; that connection remains a hypothesis.

#### METTL3

- **Related proteins** (co-abundance neighbors): PXN (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methyltransferase 3, N6-adenosine-methyltransferase complex catalytic subunit. This gene encodes the 70 kDa subunit of MT-A which is part of N6-adenosine-methyltransferase. This enzyme is involved in the posttranscriptional methylation of internal adenosine residues in eukaryotic mRNAs, forming N6-methyladenosine. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.537); neoplasm (0.120); colorectal carcinoma (0.120); hepatocellular carcinoma (0.120); gastric cancer (0.118)
- **Europe PMC papers**: 13257
- **Why important**: METTL3 is a catalytic component of the mRNA N6-adenosine-methyltransferase machinery and is annotated for RNA methylation, mRNA processing, DNA-damage response, and spermatogenesis. It connects directly to PXN in the module and shows cell-type-enhanced expression in early spermatids and late primary spermatocytes. METTL3 has a very extensive literature base and broad disease relevance, making it the strongest candidate for post-transcriptional regulation within the module.
- **Conclusion**: Established evidence supports METTL3 as an RNA-modification regulator with relevance to germ-cell biology and gene-expression control. Its co-abundance with PXN does not demonstrate that METTL3 methylates PXN-related transcripts or drives adhesion in this module; that is a testable hypothesis.

#### MIER1

- **Related proteins** (co-abundance neighbors): PDCL3 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MIER1 transcriptional regulator. This gene encodes a protein that was first identified in Xenopus laevis by its role in a mesoderm induction early response (MIER). The encoded protein functions as a transcriptional regulator. Alternatively spliced transcript variants encode multiple isoforms, some of which lack a C-terminal nuclear localization signal. [provided by RefSeq, May 2013].
- **Diseases (Open Targets)**: neurodegenerative disease (0.305); inflammatory bowel disease (0.248); Abnormal pupillary function (0.191); psoriasis (0.167); neoplasm (0.090)
- **Europe PMC papers**: 688
- **Why important**: MIER1 is the transcriptional-regulatory endpoint of the PDCL3–MIER1 branch. It is annotated for negative regulation of RNA polymerase II transcription, chromatin remodeling, regulation of DNA-templated transcription, and positive regulation of canonical NF-kappaB signaling. HPA reports tissue enhancement in bone marrow and cell-type enhancement in neutrophil progenitors and neutrophils, providing a potential explanation for a blood- or myeloid-associated component. Its literature and disease associations support biological relevance beyond this module.
- **Conclusion**: Established evidence supports MIER1 as a transcriptional and chromatin-associated regulator with myeloid-related expression patterns. It could help encode a shared transcriptional state, but the module does not establish that MIER1 controls PXN, PDCL3, or the other genes.

#### PDCL3

- **Related proteins** (co-abundance neighbors): PXN (0.83), MIER1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosducin like 3. This gene encodes a member of the phosducin-like protein family and is a putative modulator of heterotrimeric G proteins. The protein shares extensive amino acid sequence homology with phosducin. Members of the phosducin-like protein family have been shown to bind to the beta-gamma subunits of G proteins. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: ovarian neoplasm (0.353); smoking cessation (0.281); post term pregnancy (0.212); Abnormality of the genital system (0.207); cancer (0.096)
- **Europe PMC papers**: 179
- **Why important**: PDCL3 links PXN to MIER1 and therefore occupies the branch that connects adhesion-associated biology with transcriptional regulation. Its established annotation describes a phosducin-like protein and putative modulator of heterotrimeric G-protein beta-gamma subunits, with links to actin-cytoskeleton organization, angiogenesis, and endothelial proliferation. HPA indicates cell-type enhancement in oocytes and undifferentiated spermatogonia, relevant to the ovary and stem-cell comparison. Although less extensively studied than METTL3 or PXN, it provides a biologically plausible signaling intermediary.
- **Conclusion**: Established evidence supports PDCL3 as a candidate signaling and cytoskeletal regulator with reproductive-cell expression patterns. Its position makes it a useful bridge candidate, but a direct PDCL3-mediated connection between PXN and MIER1 is not established by the supplied data.

#### SEH1L

- **Related proteins** (co-abundance neighbors): PXN (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEH1 like nucleoporin. The protein encoded by this gene is part of a nuclear pore complex, Nup107-160. This protein contains WD repeats and shares 34% amino acid identity with yeast Seh1 and 30% identity with yeast Sec13. All constituents of the Nup107-160 complex, including this protein, specifically localize to kinetochores in mitosis. Two alternatively spliced transcript variants encoding distinct isoforms have been …
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); COVID-19 (0.370); Histiocytosis (0.370)
- **Europe PMC papers**: 416
- **Why important**: SEH1L is connected to PXN and represents a distinct nuclear function within the module. It is a component of the Nup107-160 nuclear-pore complex and is associated with nucleocytoplasmic transport, nuclear-pore organization, and mitotic chromosome alignment. Its inclusion broadens the interpretation from adhesion alone toward coordination of cytoplasmic organization with nuclear transport or proliferative state. It has a substantial literature base and disease associations involving infectious and immune-related conditions.
- **Conclusion**: Established evidence supports SEH1L as a nuclear-pore and mitotic machinery component. Its co-abundance with PXN may reflect a shared cellular state involving adhesion and proliferation or nuclear transport, but no direct molecular relationship between these proteins is demonstrated.
