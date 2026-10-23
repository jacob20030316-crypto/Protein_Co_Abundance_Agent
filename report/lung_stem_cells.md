# Conserved co-abundance modules: lung and stem_cells

## Module 0

**Tissue pair**: lung and stem_cells  
**Genes (26)**: HIBADH, ASL, MTHFD1L, CD276, PDSS2, TSFM, EHMT2, EXOC6B, FUCA2, H6PD, GALNT7, QRSL1, L2HGDH, LYRM4, MGME1, MOSPD2, NEXN, OCIAD1, PIK3C2A, PDP1, PIGS, CARS2, EARS2, YARS2, TAMM41, TRIOBP

### Function

The module is most consistent with mitochondrial metabolism and mitochondrial gene expression, especially mitochondrial translation, aminoacyl-tRNA charging, respiratory-chain support, mitochondrial genome maintenance, and related metabolic processes. This interpretation is supported by the concentration of mitochondrial annotations and by the supplementary STRING terms concerning mitochondria, mitochondrial disease, combined oxidative phosphorylation deficiency, mitochondrial translation, and associated metabolic phenotypes. However, no GO or KEGG term passed global correction, so these annotations do not constitute globally significant enrichment. The network also contains genes involved in pyruvate entry into metabolism, coenzyme Q synthesis, cardiolipin synthesis, iron-sulfur cluster biology, amino-acid metabolism, and mitochondrial folate metabolism. Thus, the module appears functionally coherent but biologically broad rather than a narrowly defined pathway.

**Cell composition.** This is not primarily a plasma or secreted-protein module: only FUCA2 is described as secreted to blood, while H6PD is described as intracellular and membrane-associated. Most genes have low tissue specificity and low immune-cell specificity, and the module is not dominated by blood-cell markers. A few genes show cell-type-enhanced patterns involving cardiomyocytes, oligodendrocytes, trophoblast-related cells, and other differentiated cell types, but these patterns are distributed across different cell types rather than defining a single shared population. HPA detects most of the module proteins in lung, whereas there is no matching HPA tissue for stem cells. The shared signal therefore could reflect a broadly expressed mitochondrial program present in both tissues, with possible contributions from shared cell states, rather than a blood-contamination signature. The liver and heart-muscle tissue enhancements of selected genes should be treated as compositional context, not proof that the module originates from either tissue.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a concentrated set of known or database-supported relationships among the mitochondrial translation genes CARS2, EARS2, YARS2, TSFM, and QRSL1. These include links among mitochondrial aminoacyl-tRNA synthetases, the translation elongation factor TSFM, and the mitochondrial glutaminyl-tRNA amidotransferase subunit QRSL1. STRING supplementary annotations also connect many module genes with mitochondrial disease, oxidative phosphorylation deficiency, mitochondrial localization, transit peptides, protein biosynthesis, and metabolic phenotypes. These are supporting evidence and are not globally corrected module-enrichment results. hu.MAP identifies one complex containing TSFM, MTHFD1L, QRSL1, and PDP1. The complex has many additional proteins, so the module captures a subset of a broader mitochondrial metabolic and translation-associated complex rather than reproducing the complete complex. Most other module edges are not represented in the supplied STRING or hu.MAP results; this may reflect database coverage, indirect co-abundance relationships, or tissue-specific regulation. The network therefore combines a well-supported mitochondrial translation core with peripheral metabolic, trafficking, cytoskeletal, glycosylation, and signaling genes.

**STRING interactions (score >= 0.7)**: 6 of 325 gene pairs: CARS2–EARS2 (0.838); CARS2–YARS2 (0.843); EARS2–QRSL1 (0.908); EARS2–TSFM (0.704); EARS2–YARS2 (0.909); TSFM–YARS2 (0.822)
**STRING functional enrichment (supplementary, within-query FDR)**: DISEASES Inherited metabolic disorder (FDR = 0.00043, 13 genes); Keyword Primary mitochondrial disease (FDR = 0.001, 7 genes); Keyword Mitochondrion (FDR = 0.0013, 13 genes); DISEASES Combined oxidative phosphorylation deficiency (FDR = 0.0018, 5 genes); DISEASES Mitochondrial metabolism disease (FDR = 0.0026, 7 genes); Keyword Transit peptide (FDR = 0.0103, 9 genes); HPO Abnormality of acid-base homeostasis (FDR = 0.0111, 9 genes); HPO Decreased activity of mitochondrial complex IV (FDR = 0.0111, 4 genes); HPO Decreased activity of mitochondrial complex III (FDR = 0.0111, 4 genes); COMPARTMENTS Mitochondrion (FDR = 0.0144, 13 genes); Keyword Protein biosynthesis (FDR = 0.0237, 5 genes); Component Mitochondrion (FDR = 0.0274, 14 genes); Component Mitochondrial matrix (FDR = 0.0274, 9 genes); Keyword Ligase (FDR = 0.0433, 5 genes); HPO Increased serum lactate (FDR = 0.0467, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (TSFM, MTHFD1L, QRSL1, PDP1; 4/99)

### Novelty

The underlying biology is not a wholly new finding. Mitochondrial translation, oxidative phosphorylation deficiency, coenzyme Q synthesis, mitochondrial genome maintenance, iron-sulfur biology, and related metabolic functions are already established for several module genes and are represented in STRING and hu.MAP evidence. The absence of many individual relationships from these resources does not prove novelty. A potentially new aspect is the specific co-abundance configuration shared by lung and stem cells, particularly the way mitochondrial translation genes are connected to metabolic, membrane, cytoskeletal, and cell-state genes. That module-level tissue-pair observation cannot be established as novel from the supplied evidence alone; it would require comparison with published co-abundance networks, independent cohorts, and replication across datasets.

**Hypothesis.** Hypothesis: the module represents a shared mitochondrial capacity program that coordinates production and maintenance of respiratory-chain components with substrate metabolism and organelle quality control in lung and stem-cell contexts. In this model, mitochondrial tRNA charging and translation through CARS2, EARS2, YARS2, TSFM, and QRSL1 support respiratory-chain protein synthesis; LYRM4 supports iron-sulfur cluster biology; PDSS2 and TAMM41 support respiratory-chain lipid and coenzyme Q-related functions; and L2HGDH, HIBADH, PDP1, H6PD, ASL, and MTHFD1L connect mitochondrial activity to carbon, amino-acid, and folate metabolism. The peripheral genes may reflect coupling to membrane trafficking, glycosylation, adhesion, signaling, or cell differentiation. This is a mechanistic hypothesis generated from co-abundance and annotations, not evidence of direct physical interaction or causal regulation.

### Important genes

#### CARS2

- **Related proteins** (co-abundance neighbors): LYRM4 (0.91), HIBADH (0.80); STRING partners: EARS2 (0.838), YARS2 (0.843)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cysteinyl-tRNA synthetase 2, mitochondrial. This gene encodes a putative member of the class I family of aminoacyl-tRNA synthetases. These enzymes play a critical role in protein biosynthesis by charging tRNAs with their cognate amino acids. This protein is encoded by the nuclear genome but is likely to be imported to the mitochondrion where it is thought to catalyze the ligation of cysteine to tRNA molecules. A splice-site mutation in this…
- **Diseases (Open Targets)**: Combined oxidative phosphorylation defect type 27 (0.757); neurodegenerative disease (0.550); hereditary disease (0.471); mitochondrial disease (0.416); atrial fibrillation (0.389)
- **Europe PMC papers**: 441
- **Why important**: CARS2 is a mitochondrial cysteinyl-tRNA synthetase and sits within the STRING-supported mitochondrial translation cluster with EARS2 and YARS2. It is connected to nearly all of the supplementary mitochondrial disease and oxidative-phosphorylation annotations, and its disease associations include combined oxidative phosphorylation defect and mitochondrial disease. Its established function and strong literature support make it a central marker of the module's mitochondrial translation interpretation.
- **Conclusion**: Established evidence supports CARS2 as a mitochondrial protein-biosynthesis component and a disease-relevant indicator of oxidative-phosphorylation dysfunction. The module supports coordinated regulation of CARS2 with other mitochondrial translation genes, but does not establish a new CARS2 interaction or a causal role in the lung or stem-cell context.

#### EARS2

- **Related proteins** (co-abundance neighbors): MGME1 (0.84), QRSL1 (0.84); STRING partners: CARS2 (0.838), QRSL1 (0.908), TSFM (0.704), YARS2 (0.909)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamyl-tRNA synthetase 2, mitochondrial. This gene encodes a member of the class I family of aminoacyl-tRNA synthetases. These enzymes play a critical role in protein biosynthesis by charging tRNAs with their cognate amino acids. This protein is encoded by the nuclear genome but is likely to be imported to the mitochondrion where it is thought to catalyze the ligation of glutamate to tRNA molecules. Mutations in this gene have been assoc…
- **Diseases (Open Targets)**: leukoencephalopathy-thalamus and brainstem anomalies-high lactate syndrome (0.828); hereditary disease (0.470); mitochondrial disease (0.408); Leigh syndrome (0.371); epilepsy (0.371)
- **Europe PMC papers**: 384
- **Why important**: EARS2 is a mitochondrial glutamyl-tRNA synthetase and has STRING-supported relationships with CARS2, YARS2, TSFM, and QRSL1. It is present across the supplementary mitochondrial, mitochondrial-disease, and oxidative-phosphorylation evidence, while its disease associations include a mitochondrial leukoencephalopathy with high lactate and combined oxidative phosphorylation deficiency. Its position links the translation-related portion of the network to the QRSL1 and TSFM relationships.
- **Conclusion**: Established evidence supports EARS2 as a mitochondrial tRNA-charging gene with disease relevance. Its co-abundance with the other translation genes is consistent with a shared mitochondrial translation program, but the supplied data do not show that EARS2 mechanistically regulates the other module members.

#### TSFM

- **Related proteins** (co-abundance neighbors): HIBADH (0.84), L2HGDH (0.82); STRING partners: EARS2 (0.704), YARS2 (0.822)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: Ts translation elongation factor, mitochondrial. This gene encodes a mitochondrial translation elongation factor. The encoded protein is an enzyme that catalyzes the exchange of guanine nucleotides on the translation elongation factor Tu during the elongation step of mitchondrial protein translation. Mutations in this gene are associated with combined oxidative phosphorylation deficiency-3 syndrome. Alternate splicing results in multiple transcr…
- **Diseases (Open Targets)**: fatal mitochondrial disease due to combined oxidative phosphorylation defect type 3 (0.795); steroid-resistant nephrotic syndrome (0.474); hereditary disease (0.414); mitochondrial disease (0.372); neurodegenerative disease (0.370)
- **Europe PMC papers**: 484
- **Why important**: TSFM is the mitochondrial translation elongation factor in the module and is represented in the hu.MAP complex with MTHFD1L, QRSL1, and PDP1. It has STRING-supported links to EARS2 and YARS2 and appears across the supplementary mitochondrial disease, oxidative-phosphorylation, transit-peptide, and mitochondrial translation evidence. Its role is complementary to the aminoacyl-tRNA synthetases, making it an important functional bridge within the mitochondrial translation interpretation.
- **Conclusion**: Established evidence supports TSFM as a core mitochondrial translation factor associated with combined oxidative-phosphorylation deficiency. The module suggests coordinated regulation of translation elongation with tRNA charging and metabolic functions, but does not demonstrate that the hu.MAP complex is assembled in either tissue.

#### QRSL1

- **Related proteins** (co-abundance neighbors): L2HGDH (0.87), EARS2 (0.84); STRING partners: EARS2 (0.908)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: glutaminyl-tRNA amidotransferase subunit QRSL1. Enables glutaminyl-tRNA synthase (glutamine-hydrolyzing) activity. Involved in glutaminyl-tRNAGln biosynthesis via transamidation and mitochondrial translation. Located in mitochondrion. Part of glutamyl-tRNA(Gln) amidotransferase complex. Implicated in combined oxidative phosphorylation deficiency 40. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: combined oxidative phosphorylation deficiency 40 (0.752); neurodegenerative disease (0.462); vascular disorder (0.362); hereditary disease (0.193); choreatic disease (0.118)
- **Europe PMC papers**: 212
- **Why important**: QRSL1 is a mitochondrial glutaminyl-tRNA amidotransferase subunit involved in mitochondrial translation and belongs to the hu.MAP complex identified in the module. It has a strong STRING relationship with EARS2 and is connected to the supplementary mitochondrial disease and oxidative-phosphorylation evidence. Its blood-cell group enrichment in HPA is worth noting, but the broader module is not blood-cell dominated, so QRSL1 should not by itself be interpreted as evidence of blood contamination.
- **Conclusion**: Established evidence supports QRSL1 as a mitochondrial translation component and disease-associated gene. Its network placement supports a translation-centered module core, while the HPA blood-cell pattern remains a compositional consideration rather than a demonstrated explanation for the whole module.

#### L2HGDH

- **Related proteins** (co-abundance neighbors): QRSL1 (0.87), LYRM4 (0.84), TSFM (0.82), HIBADH (0.82), FUCA2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: L-2-hydroxyglutarate dehydrogenase. This gene encodes L-2-hydroxyglutarate dehydrogenase, a FAD-dependent enzyme that oxidizes L-2-hydroxyglutarate to alpha-ketoglutarate in a variety of mammalian tissues. Mutations in this gene cause L-2-hydroxyglutaric aciduria, a rare autosomal recessive neurometabolic disorder resulting in moderate to severe cognitive disability. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: L-2-hydroxyglutaric aciduria (0.823); neurodegenerative disease (0.514); hereditary disease (0.452); gout (0.376); lysosomal storage disease (0.370)
- **Europe PMC papers**: 521
- **Why important**: L2HGDH has the strongest network position in the supplied subgraph and connects several mitochondrial or metabolic genes, including QRSL1, LYRM4, TSFM, HIBADH, and FUCA2. It encodes the enzyme that converts L-2-hydroxyglutarate to alpha-ketoglutarate and is associated with L-2-hydroxyglutaric aciduria and neurodegenerative disease. Its established metabolic function provides a bridge between the mitochondrial translation cluster and broader carbon metabolism.
- **Conclusion**: Established evidence supports L2HGDH as a mitochondrial metabolic enzyme with a clear inherited neurometabolic disease association. Its central network position suggests that metabolic state may be coupled to the mitochondrial translation program, but this coupling is a hypothesis rather than proof of direct biochemical regulation.

#### LYRM4

- **Related proteins** (co-abundance neighbors): PDP1 (0.94), CARS2 (0.91), L2HGDH (0.84), H6PD (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LYR motif containing 4. The protein encoded by this gene is found in both mitochondria and the nucleus, where it binds cysteine desulfurase and helps free inorganic sulfur for Fe/S clusters. Disruption of this gene negatively impacts mitochondrial and cytosolic iron homeostasis. [provided by RefSeq, Sep 2016].
- **Diseases (Open Targets)**: combined oxidative phosphorylation deficiency 19 (0.684); severe neonatal lactic acidosis due to NFS1-ISD11 complex deficiency (0.619); severe acute respiratory syndrome (0.197); COVID-19 (0.197); placental retention (0.163)
- **Europe PMC papers**: 445
- **Why important**: LYRM4 connects PDP1, CARS2, L2HGDH, and H6PD in the co-abundance network and is repeatedly represented in the supplementary mitochondrial disease and mitochondrial compartment evidence. Its established function in cysteine-desulfurase-associated iron-sulfur cluster assembly provides a mechanistic link between mitochondrial metabolism, respiratory-chain competence, and the translation-associated genes. It also has disease associations involving oxidative-phosphorylation deficiency and severe lactic acidosis.
- **Conclusion**: Established evidence supports LYRM4 as an iron-sulfur cluster biology factor relevant to mitochondrial function. Its placement suggests that iron-sulfur maturation may be coordinated with mitochondrial translation and energy metabolism in the shared module, but the co-abundance data do not establish direct regulation or causality.

## Module 1

**Tissue pair**: lung and stem_cells  
**Genes (36)**: SLC3A2, SLC1A5, ACSL3, AGPS, CANX, CKAP4, CYP51A1, TBRG4, HACL2, ITGA6, MKI67, PRKCA, MAVS, MED20, MAPK15, SLC16A3, MTX1, MYEF2, NCEH1, ORC4, PDE12, PNPLA6, PMS1, RAB3B, RDH11, RTN4, SMARCA1, SMARCD1, HM13, SPTLC1, TFRC, TIMM50, TMEM33, TOP2A, TYSND1, VAMP7

### Function

The best-supported function is an endoplasmic-reticulum and organelle-membrane program, with particular emphasis on the ER membrane, ER subcompartments, and the nuclear-envelope–ER membrane network. This interpretation is based on the globally corrected primary terms (5 globally significant GO/KEGG terms, q_global 0.00357–0.0498; see the table); these terms substantially overlap in genes and should not be treated as independent biological discoveries. The module also contains a coherent lipid and membrane-metabolism component: ACSL3 activates long-chain fatty acids, SPTLC1 initiates sphingolipid biosynthesis, CYP51A1 participates in cholesterol biosynthesis, HACL2 is associated with fatty-acid alpha-oxidation, PNPLA6 with phosphatidylcholine metabolism, and AGPS with ether-lipid biosynthesis. CANX supports ER protein folding and quality control, while VAMP7 supports vesicle traffic and fusion. A smaller branch links mitochondrial signaling, proliferation, chromatin, transport, and innate antiviral signaling, so the module should not be reduced to a single pathway. The supplementary STRING terms (11 supplementary STRING terms; within-query FDR 3.09e-07–0.0491) reinforce a membrane and ER interpretation, but they are supplementary rather than globally corrected primary evidence. No GO or KEGG biological-process term passed global correction; the globally significant evidence is concentrated in cellular-component terms.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the HPA summary identifies only a small secreted component, and most genes have low tissue specificity with many cell-type enhancements. Protein detection in lung is broad across the module, whereas there is no matching HPA tissue for stem_cells, so shared abundance may partly reflect common cellular composition or a general membrane program rather than a stem-cell-specific mechanism. HPA points to several potentially admixed cell contexts, including neutrophils, trophoblast-related cells, late spermatids, and esophageal apical cells. Immune-cell specificity is mostly low, but several genes are immune-cell enhanced, including CKAP4, SLC16A3, TFRC, and ITGA6, while neutrophil-associated signals occur for ACSL3, TMEM33, and SLC16A3. Thus blood or shared cell types cannot be excluded, especially in heterogeneous lung material, but the module is not convincingly explained as a blood-only or secreted-protein signature. The HPA pattern also supports a broadly expressed housekeeping-like membrane and organelle component.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC endoplasmic reticulum membrane | 0.00357 | ACSL3, CANX, CKAP4, CYP51A1, HACL2, HM13, NCEH1, PNPLA6, RDH11, RTN4, SPTLC1, TMEM33, VAMP7 |
| GO:CC endoplasmic reticulum subcompartment | 0.00357 | ACSL3, CANX, CKAP4, CYP51A1, HACL2, HM13, NCEH1, PNPLA6, RDH11, RTN4, SPTLC1, TMEM33, VAMP7 |
| GO:CC nuclear outer membrane-endoplasmic reticulum membrane network | 0.00431 | ACSL3, CANX, CKAP4, CYP51A1, HACL2, HM13, NCEH1, PNPLA6, RDH11, RTN4, SPTLC1, TMEM33, VAMP7 |
| GO:CC organelle membrane | 0.0171 | ACSL3, AGPS, CANX, CKAP4, CYP51A1, HACL2, HM13, MAVS, MTX1, NCEH1, PNPLA6, PRKCA, RAB3B, RDH11, RTN4, SLC16A3, SLC3A2, SPTLC1, TFRC, TIMM50, TMEM33, VAMP7 |
| GO:CC organelle subcompartment | 0.0498 | ACSL3, CANX, CKAP4, CYP51A1, HACL2, HM13, NCEH1, PNPLA6, RDH11, RTN4, SPTLC1, TMEM33, VAMP7 |

### STRING and hu.MAP

Direct high-confidence STRING support is sparse and localized. The established pairs are AGPS–TYSND1, MKI67–TOP2A, and SLC1A5–SLC3A2. The last pair directly supports amino-acid transport, while the MKI67–TOP2A pair marks a proliferation-associated branch and AGPS–TYSND1 connects ether-lipid biosynthesis with peroxisomal protein processing. There are no listed STRING partners for many of the ER-centered genes, so co-abundance should not be interpreted as a catalogue of physical interactions. hu.MAP provides convergent but partial complex-level support: ACSL3, TMEM33, and HM13 co-occur in several ER or membrane-oriented complexes (hu.MAP huMAP3_08167.1), (hu.MAP huMAP3_09592.1), (hu.MAP huMAP3_07410.1), and (hu.MAP huMAP3_06247.1); HACL2 and ACSL3 co-occur in (hu.MAP huMAP3_02404.1) and (hu.MAP huMAP3_10153.1); and TFRC with CKAP4 occurs in (hu.MAP huMAP3_10725.1). However, each complex contains many members outside the module, and confidence varies. Collectively, STRING and hu.MAP support selected known relationships and an ER/membrane neighborhood, but they do not establish one complete physical complex spanning the module.

**STRING interactions (score >= 0.7)**: 3 of 630 gene pairs: AGPS–TYSND1 (0.881); MKI67–TOP2A (0.993); SLC1A5–SLC3A2 (0.894)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transmembrane helix (FDR = 3.09e-07, 20 genes); Component Intrinsic component of membrane (FDR = 3.74e-05, 21 genes); Component Integral component of membrane (FDR = 8.59e-05, 20 genes); Keyword Signal-anchor (FDR = 0.00048, 7 genes); Keyword Membrane (FDR = 0.00084, 23 genes); Keyword Endoplasmic reticulum (FDR = 0.0015, 12 genes); Component Endoplasmic reticulum membrane (FDR = 0.0018, 12 genes); Component Organelle membrane (FDR = 0.003, 21 genes); Component Melanosome (FDR = 0.0171, 5 genes); COMPARTMENTS Endoplasmic reticulum (FDR = 0.042, 12 genes); Component Endoplasmic reticulum (FDR = 0.0491, 13 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08167.1 (ACSL3, TMEM33, HM13; 3/24); huMAP3_09592.1 (ACSL3, TMEM33, HM13; 3/95); huMAP3_02404.1 (HACL2, ACSL3; 2/4); huMAP3_10153.1 (HACL2, ACSL3; 2/10); huMAP3_07410.1 (TMEM33, HM13; 2/35); huMAP3_10725.1 (TFRC, CKAP4; 2/59); huMAP3_06247.1 (TMEM33, HM13; 2/65)

### Novelty

The module is not established as a wholly new molecular pathway: its central themes involve well-known ER membrane biology, lipid metabolism, vesicle trafficking, amino-acid transport, mitochondrial signaling, and cell proliferation. Several individual relationships and complexes are already represented by STRING or hu.MAP, as shown by the pairs and complexes above. Nevertheless, the lung–stem_cells co-abundance organization may be a new systems-level observation, particularly because the module combines an ER lipid and membrane core with mitochondrial, transport, and proliferation branches. That claim remains a hypothesis rather than proof of novelty: absence of a relationship from STRING or hu.MAP cannot demonstrate that it is novel, and co-abundance does not prove direct molecular interaction. Establishing novelty would require comparison with prior tissue-pair module studies and independent replication.

**Hypothesis.** Mechanistic hypothesis: shared cellular stress or biosynthetic demand in lung and stem-cell samples co-regulates an ER-centered membrane homeostasis program. ACSL3, SPTLC1, CYP51A1, PNPLA6, and AGPS could coordinate fatty-acyl, sphingolipid, sterol, phosphatidylcholine, and ether-lipid handling; TMEM33 and HM13 could couple ER topology, ER-stress responses, and intramembrane processing; CANX could maintain folding quality; and VAMP7 could route membrane cargo. SLC1A5–SLC3A2 may provide nutrient transport, while MAVS and the mitochondrial branch may reflect stress or innate immune signaling. The proliferation-linked MKI67–TOP2A edge may represent a cell-state admixture or a regenerative component rather than the core mechanism. This model predicts that perturbing ER membrane lipid handling should alter ER morphology, protein quality control, and vesicle traffic together, but it requires experimental testing and should not be treated as established by co-abundance alone.

### Important genes

#### ACSL3

- **Related proteins** (co-abundance neighbors): HACL2 (0.87), SMARCD1 (0.87), CKAP4 (0.85), TMEM33 (0.84), SLC1A5 (0.82), CANX (0.81), HM13 (0.81), TBRG4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_08167.1, huMAP3_09592.1, huMAP3_02404.1, huMAP3_10153.1
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 3. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme is highly expressed…
- **Diseases (Open Targets)**: prostate adenocarcinoma (0.370); acute myeloid leukemia (0.313); neurodegenerative disease (0.300); ovarian dysfunction (0.253); Abnormality of the skeletal system (0.215)
- **Europe PMC papers**: 2930
- **Why important**: ACSL3 is the strongest network hub in the supplied module and is present in every primary global term (5 globally significant GO/KEGG terms, q_global 0.00357–0.0498; see the table). It links HACL2, CKAP4, TMEM33, SLC1A5, CANX, HM13, SMARCD1, and TBRG4, thereby connecting the ER membrane core to lipid metabolism, transport, and nuclear or mitochondrial branches. Its established function is long-chain fatty-acyl-CoA formation for lipid biosynthesis and fatty-acid degradation, and it appears in several hu.MAP complexes (hu.MAP huMAP3_08167.1) (hu.MAP huMAP3_09592.1) (hu.MAP huMAP3_02404.1) (hu.MAP huMAP3_10153.1). It has substantial literature and disease-association coverage, including cancer, neurodegenerative disease, and ovarian dysfunction.
- **Conclusion**: Established: ACSL3 is a central co-abundance organizer with a documented lipid-metabolic function and repeated ER/membrane complex annotation. Hypothesis: it may be a metabolic anchor that couples ER membrane composition to the other module branches; the network does not establish that it physically regulates all of them.

#### TMEM33

- **Related proteins** (co-abundance neighbors): ACSL3 (0.84), RAB3B (0.84), SLC16A3 (0.83), HACL2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_08167.1, huMAP3_09592.1, huMAP3_07410.1, huMAP3_06247.1
- **Function (MyGene.info)**: transmembrane protein 33. Involved in positive regulation of endoplasmic reticulum unfolded protein response; regulation of endoplasmic reticulum tubular network organization; and response to endoplasmic reticulum stress. Located in endoplasmic reticulum membrane; melanosome; and nuclear envelope. Is integral component of endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: squamous cell carcinoma (0.156); thrombophilia (0.100); neoplasm (0.089); lung adenocarcinoma (0.080); cervical squamous cell carcinoma (0.077)
- **Europe PMC papers**: 338
- **Why important**: TMEM33 is connected to ACSL3, RAB3B, SLC16A3, and HACL2 and is present in every primary global term (5 globally significant GO/KEGG terms, q_global 0.00357–0.0498; see the table). Its documented functions include ER tubular-network organization and positive regulation of IRE1- and PERK-mediated unfolded-protein responses. It recurs with ACSL3 and HM13 in multiple hu.MAP complexes (hu.MAP huMAP3_08167.1), (hu.MAP huMAP3_09592.1), (hu.MAP huMAP3_07410.1), and (hu.MAP huMAP3_06247.1), despite having no listed STRING partner. Its literature volume is smaller than that of the major hubs, which makes it potentially informative for a less-characterized ER mechanism; disease associations include several neoplastic conditions.
- **Conclusion**: Established: TMEM33 is an ER-membrane and ER-stress-related component with repeated complex-level support and a strategically placed position in the module. Hypothesis: it could coordinate ER shape and stress signaling with lipid remodeling and monocarboxylate transport, but that coupling is not directly demonstrated here.

#### CANX

- **Related proteins** (co-abundance neighbors): SPTLC1 (0.83), CKAP4 (0.82), ACSL3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX connects ACSL3, SPTLC1, and CKAP4 and occurs in every primary global term (5 globally significant GO/KEGG terms, q_global 0.00357–0.0498; see the table). It is an ER molecular chaperone involved in calcium-dependent folding and quality control of newly synthesized glycoproteins, including ER-associated degradation. It also appears in the supplementary ER and membrane terms (STRING Keyword Transmembrane helix; within-query FDR = 3.09e-07) (STRING Component Intrinsic component of membrane; within-query FDR = 3.74e-05) (STRING Component Integral component of membrane; within-query FDR = 8.59e-05) and (7 supplementary STRING terms; within-query FDR 0.00084–0.0491), and has substantial literature and disease-association coverage, including neurodegenerative and viral-disease contexts. Its lung protein detection and broadly low tissue specificity make it a plausible general cellular-state marker as well as a mechanistic component.
- **Conclusion**: Established: CANX supports the ER protein-quality-control interpretation and is positioned at the interface between lipid-related genes and the ER structural branch. Hypothesis: its co-abundance may report increased folding load or membrane remodeling in the shared cell state, but the data do not distinguish cause from consequence.

#### VAMP7

- **Related proteins** (co-abundance neighbors): AGPS (0.85), NCEH1 (0.83), TFRC (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vesicle associated membrane protein 7. This gene encodes a transmembrane protein that is a member of the soluble N-ethylmaleimide-sensitive factor attachment protein receptor (SNARE) family. The encoded protein localizes to late endosomes and lysosomes and is involved in the fusion of transport vesicles to their target membranes. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Jun 2010].
- **Diseases (Open Targets)**: neoplasm (0.083); gastric cancer (0.076); breast cancer (0.048); acute myeloid leukemia (0.042); hypospadias (0.039)
- **Europe PMC papers**: 1776
- **Why important**: VAMP7 connects AGPS, NCEH1, and TFRC and is present in every primary global term (5 globally significant GO/KEGG terms, q_global 0.00357–0.0498; see the table). It is a documented SNARE-family vesicle-fusion protein involved in ER-to-Golgi transport, endosome-to-lysosome transport, exocytosis, and phagocytic engulfment. It is repeatedly represented in the supplementary membrane and ER terms (8 supplementary STRING terms; within-query FDR 3.09e-07–0.003) and (STRING COMPARTMENTS Endoplasmic reticulum; within-query FDR = 0.042) (STRING Component Endoplasmic reticulum; within-query FDR = 0.0491). Its network position links lipid metabolism and ER lipid handling to vesicular trafficking and iron-receptor trafficking, while its literature and disease-association record is substantial.
- **Conclusion**: Established: VAMP7 provides a credible trafficking arm of the ER and organelle-membrane program. Hypothesis: coordinated VAMP7 abundance could translate ER membrane remodeling into altered cargo delivery or lysosomal handling, but no direct module-specific cargo mechanism is shown.

#### SPTLC1

- **Related proteins** (co-abundance neighbors): CANX (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine palmitoyltransferase long chain base subunit 1. This gene encodes a member of the class-II pyridoxal-phosphate-dependent aminotransferase family. The encoded protein is the long chain base subunit 1 of serine palmitoyltransferase. Serine palmitoyltransferase converts L-serine and palmitoyl-CoA to 3-oxosphinganine with pyridoxal 5'-phosphate and is the key enzyme in sphingolipid biosynthesis. Mutations in this gene were identified in patients wi…
- **Diseases (Open Targets)**: neuropathy, hereditary sensory and autonomic, type 1A (0.702); hereditary sensory and autonomic neuropathy type 1 (0.667); amyotrophic lateral sclerosis 27, juvenile (0.632); Charcot-Marie-Tooth disease (0.582); hereditary sensory and autonomic neuropathy type 2 (0.462)
- **Europe PMC papers**: 1351
- **Why important**: SPTLC1 is an ER-localized, primary sphingolipid-biosynthesis enzyme and is present in every primary global term (5 globally significant GO/KEGG terms, q_global 0.00357–0.0498; see the table). It connects to CANX in the module and is represented across the supplementary membrane and ER terms (STRING Keyword Transmembrane helix; within-query FDR = 3.09e-07) (STRING Component Intrinsic component of membrane; within-query FDR = 3.74e-05) (STRING Component Integral component of membrane; within-query FDR = 8.59e-05) and (7 supplementary STRING terms; within-query FDR 0.00084–0.0491). Its established role in the first step of sphingolipid biosynthesis gives the module a biochemical entry point for membrane-lipid remodeling, and its disease associations include hereditary sensory neuropathy and related neurological disorders. Its literature volume is substantial.
- **Conclusion**: Established: SPTLC1 supplies strong biochemical support for an ER lipid-homeostasis interpretation and has clinically established disease relevance. Hypothesis: sphingolipid flux may be one of the signals coupling membrane composition to ER quality control and vesicle traffic in the shared module; co-abundance alone cannot establish altered enzymatic flux.

## Module 2

**Tissue pair**: lung and stem_cells  
**Genes (33)**: GOT2, ACADVL, AKAP1, ASPH, ATP5F1C, COQ8B, HSD17B11, DNAJC10, GFM1, ETFA, GALNT2, HSPA13, EPHX1, IKBIP, LAMTOR3, MFN1, MGAT2, MPDU1, NDUFAF7, NFU1, NT5DC2, PDIA5, PITRM1, CDC40, RBM15B, RPL26L1, RNF213, STX7, DARS2, IARS2, MIA3, METTL1, UXS1

### Function

The strongest interpretation is a mitochondrial maintenance and energy-metabolism module, with linked mitochondrial translation, respiratory-chain assembly, fatty-acid oxidation, iron-sulfur cluster handling, and mitochondrial protein processing. This interpretation is supported by DARS2, IARS2, GFM1, NDUFAF7, NFU1, ETFA, ACADVL, PITRM1, ATP5F1C, MFN1, AKAP1, and COQ8B, together with the STRING mitochondrial and transit-peptide signals (STRING Keyword Transit peptide; within-query FDR = 0.0075) and (STRING Keyword Mitochondrion; within-query FDR = 0.0286). A secondary arm involves ER and Golgi protein maturation, glycosylation, vesicle traffic, and quality control, represented by MGAT2, MPDU1, UXS1, GALNT2, DNAJC10, PDIA5, HSPA13, STX7, MIA3, and HSD17B11. No GO/KEGG term passed global correction, so these pathway interpretations should be regarded as convergent functional evidence rather than globally significant GO/KEGG enrichment.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module: the proteins are predominantly intracellular, with mitochondrial, ER, Golgi, lysosomal, nucleoplasmic, and cytosolic localizations, and only a small minority are annotated in the secretome. Most genes have low tissue specificity, and lung protein detection is widespread across the module. The HPA data nevertheless indicate cell-type structure, including neutrophil, plasma-cell, hepatocyte, and germ-cell associations, while immune-cell specificity is low for most genes. Thus the shared lung and stem-cell signal could reflect a broadly used metabolic program, but contributions from shared cell types or sample-composition effects, particularly myeloid or other specialized cell populations, cannot be excluded. HPA has no matching stem-cell tissue entry, so the tissue-level comparison is not independently confirmed by HPA protein detection in stem cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited set of high-confidence, biologically coherent relationships. The ACADVL–ETFA relationship links very-long-chain fatty-acid oxidation to electron transfer, DARS2–IARS2 links mitochondrial aminoacyl-tRNA synthetases, and ATP5F1C connects to ETFA, GFM1, NDUFAF7, and RPL26L1. GFM1 also connects to RPL26L1. These known relationships support a mitochondrial translation and oxidative-energy component, but the sparse STRING connectivity means that most co-abundance edges are not established physical or functional interactions. hu.MAP provides complementary support: C1 joins DARS2, NDUFAF7, GFM1, NT5DC2, and IARS2 within a broad mitochondrial and metabolic complex, while C2 and C3 independently reinforce the DARS2–IARS2–GFM1 mitochondrial translation-related core. C4 links MGAT2 and HSD17B11 in a separate glycosylation and lipid-associated complex. Collectively, the databases support several known submodules rather than a single experimentally established complex containing all module genes.

**STRING interactions (score >= 0.7)**: 7 of 528 gene pairs: ACADVL–ETFA (0.877); ATP5F1C–ETFA (0.715); ATP5F1C–GFM1 (0.77); ATP5F1C–NDUFAF7 (0.825); ATP5F1C–RPL26L1 (0.713); DARS2–IARS2 (0.895); GFM1–RPL26L1 (0.791)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transit peptide (FDR = 0.0075, 11 genes); Keyword Mitochondrion (FDR = 0.0286, 13 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (DARS2, NDUFAF7, GFM1, NT5DC2, IARS2; 5/99); huMAP3_10525.1 (DARS2, GFM1, IARS2; 3/33); huMAP3_09668.1 (DARS2, IARS2; 2/8); huMAP3_08424.1 (MGAT2, HSD17B11; 2/9)

### Novelty

The conserved co-abundance module may represent a new systems-level observation, because the supplied evidence shows a cross-tissue pattern combining mitochondrial maintenance with ER/Golgi glycoprotein processing, and the complete module is not presented as an already defined STRING or hu.MAP complex. However, it cannot be called a definitively new biological pathway. Several component relationships and functions are already established in STRING, hu.MAP, gene annotations, and disease literature, whereas the co-abundance organization and its conservation between lung and stem cells are the potentially novel features. Absence of a complete match in STRING or hu.MAP is not evidence by itself for novelty.

**Hypothesis.** Hypothesis: this module reflects coordinated cellular demand for mitochondrial proteostasis and biosynthetic capacity. Mitochondrial translation, respiratory-chain assembly, iron-sulfur cluster maturation, fatty-acid oxidation, and ATP production may be co-regulated with ER/Golgi glycosylation and quality control so that cells can maintain energy production while synthesizing, folding, trafficking, and modifying proteins. The lung and stem-cell conservation could indicate a shared requirement for metabolic flexibility and organelle quality control, although the HPA cell-type patterns leave open the alternative explanation that shared cell populations contribute substantially to the signal. This hypothesis requires validation by cell-resolved expression, perturbation, and measurements of mitochondrial respiration and protein-processing capacity.

### Important genes

#### DARS2

- **Related proteins** (co-abundance neighbors): GOT2 (0.84), CDC40 (0.84), IKBIP (0.83), IARS2 (0.81), NT5DC2 (0.81); STRING partners: IARS2 (0.895)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1, huMAP3_09668.1
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 2, mitochondrial. The protein encoded by this gene belongs to the class-II aminoacyl-tRNA synthetase family. It is a mitochondrial enzyme that specifically aminoacylates aspartyl-tRNA. Mutations in this gene are associated with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation (LBSL). [provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: leukoencephalopathy with brain stem and spinal cord involvement-high lactate syndrome (0.843); neurodegenerative disease (0.527); hereditary disease (0.518); hypertensive disorder (0.425); Cerebral cortical atrophy (0.425)
- **Europe PMC papers**: 796
- **Why important**: DARS2 is the strongest network connector in the supplied ranking and links mitochondrial translation to several otherwise separate parts of the module. It participates in hu.MAP complexes C1, C2, and C3, has the known STRING relationship with IARS2, and is included in both supplementary mitochondrial signals (STRING Keyword Transit peptide; within-query FDR = 0.0075) and (STRING Keyword Mitochondrion; within-query FDR = 0.0286). Its established function is mitochondrial aspartyl-tRNA aminoacylation, and its disease association with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation gives the gene direct clinical relevance. The literature volume is substantial.
- **Conclusion**: Established: DARS2 is a mitochondrial translation factor and a central connector of the module's mitochondrial subnetwork. Hypothesis: variation in DARS2 abundance may help couple mitochondrial translation capacity to respiratory and biosynthetic demands in the shared lung and stem-cell state.

#### GFM1

- **Related proteins** (co-abundance neighbors): ETFA (0.81); STRING partners: ATP5F1C (0.77), RPL26L1 (0.791)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1
- **Function (MyGene.info)**: G elongation factor mitochondrial 1. Eukaryotes contain two protein translational systems, one in the cytoplasm and one in the mitochondria. Mitochondrial translation is crucial for maintaining mitochondrial function and mutations in this system lead to a breakdown in the respiratory chain-oxidative phosphorylation system and to impaired maintenance of mitochondrial DNA. This gene encodes one of the mitochondrial translation elongati…
- **Diseases (Open Targets)**: hepatoencephalopathy due to combined oxidative phosphorylation defect type 1 (0.822); neurodegenerative disease (0.463); combined oxidative phosphorylation deficiency (0.451); hereditary disease (0.341); Leigh syndrome (0.313)
- **Europe PMC papers**: 1380
- **Why important**: GFM1 is a mitochondrial translation elongation factor, is represented in hu.MAP complexes C1 and C2, and has STRING relationships with ATP5F1C and RPL26L1. Its position connects mitochondrial protein synthesis with ATP-production machinery and a translation-associated protein. GFM1 is associated with combined oxidative-phosphorylation defects, hepatoencephalopathy, and Leigh syndrome, and it has a substantial literature base.
- **Conclusion**: Established: GFM1 provides a mechanistic link between mitochondrial translation and respiratory-chain function. Hypothesis: its co-abundance with ATP5F1C and other mitochondrial factors may mark coordinated regulation of mitochondrial gene-expression output and oxidative phosphorylation.

#### ETFA

- **Related proteins** (co-abundance neighbors): ACADVL (0.83), PITRM1 (0.81), GFM1 (0.81); STRING partners: ACADVL (0.877), ATP5F1C (0.715)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein subunit alpha. ETFA participates in catalyzing the initial step of the mitochondrial fatty acid beta-oxidation. It shuttles electrons between primary flavoprotein dehydrogenases and the membrane-bound electron transfer flavoprotein ubiquinone oxidoreductase. Defects in electron-transfer-flavoprotein have been implicated in type II glutaricaciduria in which multiple acyl-CoA dehydrogenase deficiencies result in l…
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.834); glutaric aciduria (0.756); hereditary disease (0.469); multiple acyl-CoA dehydrogenase deficiency, mild type (0.370); multiple acyl-CoA dehydrogenase deficiency, severe neonatal type (0.370)
- **Europe PMC papers**: 1433
- **Why important**: ETFA is part of the mitochondrial electron-transfer system and supports fatty-acid beta-oxidation. It has a direct STRING relationship with ACADVL and additional relationships with ATP5F1C and GFM1, placing it at the interface of lipid-derived electron transfer, ATP production, and mitochondrial translation. Its HPA profile includes liver and hepatocyte associations, and its established disease links include multiple acyl-CoA dehydrogenase deficiency and glutaric aciduria. It has a substantial literature volume.
- **Conclusion**: Established: ETFA is a functionally supported oxidative-metabolism component and helps explain the module's connection to fatty-acid utilization. Hypothesis: ETFA may report the energetic substrate flexibility of the shared cellular state rather than define a lung-specific mechanism.

#### NFU1

- **Related proteins** (co-abundance neighbors): MPDU1 (0.87), UXS1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NFU1 iron-sulfur cluster scaffold. This gene encodes a protein that is localized to mitochondria and plays a critical role in iron-sulfur cluster biogenesis. The encoded protein assembles and transfers 4Fe-4S clusters to target apoproteins including succinate dehydrogenase and lipoic acid synthase. Mutations in this gene are a cause of multiple mitochondrial dysfunctions syndrome-1, and pseudogenes of this gene are located on the s…
- **Diseases (Open Targets)**: multiple mitochondrial dysfunctions syndrome 1 (0.813); spastic paraplegia 93, autosomal recessive (0.589); neurodegenerative disease (0.559); osteoarthritis, hip (0.377); multiple mitochondrial dysfunctions syndrome 2 (0.373)
- **Europe PMC papers**: 581
- **Why important**: NFU1 is connected to MPDU1 and UXS1 in the co-abundance graph and appears in both supplementary mitochondrial STRING signals (STRING Keyword Transit peptide; within-query FDR = 0.0075) and (STRING Keyword Mitochondrion; within-query FDR = 0.0286). Its established role is iron-sulfur cluster assembly and transfer to mitochondrial target proteins, making it relevant to respiratory-chain competence. NFU1 is associated with multiple mitochondrial dysfunctions syndrome and related neurodegenerative conditions. Although its direct network connectivity is limited, its biochemical role is highly informative for interpreting the mitochondrial arm.
- **Conclusion**: Established: NFU1 supports mitochondrial cofactor maturation and is consistent with a respiratory and protein-quality-control interpretation. Hypothesis: NFU1 may function as a vulnerability point that couples mitochondrial cofactor supply to the broader module.

#### MGAT2

- **Related proteins** (co-abundance neighbors): DNAJC10 (0.88), MFN1 (0.85), STX7 (0.84), MIA3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_08424.1
- **Function (MyGene.info)**: alpha-1,6-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase. The product of this gene is a Golgi enzyme catalyzing an essential step in the conversion of oligomannose to complex N-glycans. The enzyme has the typical glycosyltransferase domains: a short N-terminal cytoplasmic domain, a hydrophobic non-cleavable signal-anchor domain, and a C-terminal catalytic domain. Mutations in this gene may lead to carbohydrate-deficient glycoprotein syndrome, type II. Th…
- **Diseases (Open Targets)**: MGAT2-congenital disorder of glycosylation (0.785); Kartagener Syndrome (0.511); congenital disorder of glycosylation (0.371); COVID-19 (0.370); congenital disorder of glycosylation type II (0.370)
- **Europe PMC papers**: 828
- **Why important**: MGAT2 is a relatively well-connected gene in the module and is the module's clearest bridge to the Golgi glycosylation arm. It connects to DNAJC10, MFN1, STX7, and MIA3, and is represented with HSD17B11 in hu.MAP complex C4. Its established function is a Golgi glycosyltransferase required for conversion of oligomannose to complex N-glycans. HPA associates it with hepatocytes and plasma cells, and disease evidence includes MGAT2-related and other congenital glycosylation disorders. Its literature volume is substantial.
- **Conclusion**: Established: MGAT2 identifies a genuine glycoprotein-processing component distinct from the core mitochondrial translation machinery. Hypothesis: its co-abundance with mitochondrial genes may reflect coordination between energy supply and secretory or membrane-protein maturation, or may partly reflect shared cell-type composition.

## Module 3

**Tissue pair**: lung and stem_cells  
**Genes (32)**: SLC33A1, FDXR, GLA, ALG1, ANTXR1, APAF1, ATP13A1, BPTF, CLPB, COG8, LIG3, DPP9, DSG2, FLOT1, IQGAP2, LBR, LGALS8, MGAT1, NBAS, NDUFS1, NKRF, NPC1, PARD3, PCNP, PHF3, PHIP, RNASEH2B, RRBP1, STX6, USP25, WASHC4, ERCC4

### Function

No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The gene annotations instead suggest a heterogeneous intracellular-maintenance module with emphasis on membrane and vesicle trafficking, Golgi-to-ER and endosomal transport, glycoprotein processing, cell adhesion and polarity, cytoskeletal organization, proteostasis, mitochondrial function, and DNA repair. The network is sparse and contains several locally coherent pairs or short chains rather than a single demonstrated biochemical pathway. The strongest functional interpretation is therefore coordinated cellular infrastructure and stress-resilience biology, not a specific pathway. The lung and stem-cell sharing may reflect broadly expressed cellular machinery or shared cell populations rather than a tissue-specific program.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the HPA summary identifies only a small minority as secreted, and most genes have low tissue specificity. The module is therefore compatible with broadly expressed housekeeping-like cellular machinery. Nevertheless, HPA shows a noticeable immune and blood-cell signal, especially involving neutrophils, neutrophil progenitors, basophils, dendritic-cell populations, and related myeloid cells. Several genes are also enhanced in hematopoietic or reproductive cell types, while a smaller subset is enriched in skeletal muscle, testis, adrenal gland, blood vessel, bone marrow, or lymphoid tissue. Most module proteins are detected in lung, whereas HPA has no matching stem-cell tissue category for protein detection. Thus, shared blood or immune-cell composition, or another shared cell type, should be considered before interpreting the module as a lung–stem-cell intrinsic program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only limited direct support for a unified physical network. The known high-confidence relationships are COG8–STX6 and NBAS–STX6. These support a connection between Golgi organization, vesicle traffic, and the NBAS-associated transport machinery, but they do not establish interactions across the whole module. hu.MAP identifies FLOT1–DSG2 in complexes C1 and C2, linking membrane organization with cell-junction biology. It identifies NBAS–STX6 in complexes C3 through C6, supporting their participation in vesicle-fusion and trafficking-related assemblies. However, each hu.MAP complex contains many members outside this module, and only a small subset of each complex is represented here. The STRING and hu.MAP evidence therefore supports selected mechanistic islands, not a single experimentally established multiprotein complex containing the module.

**STRING interactions (score >= 0.7)**: 2 of 496 gene pairs: COG8–STX6 (0.862); NBAS–STX6 (0.79)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08718.1 (FLOT1, DSG2; 2/17); huMAP3_09165.1 (FLOT1, DSG2; 2/39); huMAP3_06458.1 (NBAS, STX6; 2/41); huMAP3_08929.1 (NBAS, STX6; 2/44); huMAP3_10587.1 (NBAS, STX6; 2/45); huMAP3_13160.1 (NBAS, STX6; 2/49)

### Novelty

The co-abundance pattern may be a new observation, but the module cannot be claimed as a newly discovered biological pathway. Its individual components and several relationships are already well established, including NBAS and STX6 in trafficking biology, COG8 in the conserved oligomeric Golgi complex, FLOT1 in membrane organization, DSG2 in desmosomes, and the DNA-repair and glycosylation functions represented by other members. Conversely, the sparse STRING connectivity, absence of STRING functional enrichment, lack of globally significant GO or KEGG terms, and partial rather than complete hu.MAP coverage argue against a previously recognized coherent module. The appropriate conclusion is that this is a candidate tissue-shared co-abundance pattern whose novelty lies mainly in its specific lung–stem-cell association and composition, requiring replication, cell-composition adjustment, and experimental validation.

**Hypothesis.** Hypothesis: the module reflects coordinated cellular logistics in a shared epithelial, progenitor, or immune-associated population, coupling Golgi and ER trafficking with endosomal recycling, membrane-junction organization, glycoprotein processing, proteostasis, and responses to cellular stress. NBAS, COG8, and STX6 could form a trafficking-centered axis; FLOT1, DSG2, PARD3, and IQGAP2 could connect membrane organization, polarity, adhesion, and cytoskeletal remodeling; and genes such as SLC33A1, ATP13A1, NPC1, and GLA could contribute to organelle and lipid-handling demands. The apparent association with DNA repair, mitochondrial maintenance, and apoptosis may represent supporting stress-management processes or may arise from mixed cell composition. This hypothesis predicts that the module will be strongest in defined cell populations rather than uniformly across all lung and stem-cell samples, and that its co-abundance will weaken after controlling for immune or blood-cell abundance.

### Important genes

#### NBAS

- **Related proteins** (co-abundance neighbors): COG8 (0.90), NPC1 (0.88), USP25 (0.88), SLC33A1 (0.86), RNASEH2B (0.81); STRING partners: STX6 (0.79)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_06458.1, huMAP3_08929.1, huMAP3_10587.1, huMAP3_13160.1
- **Function (MyGene.info)**: NBAS subunit of NRZ tethering complex. This gene encodes a protein with two leucine zipper domains, a ribosomal protein S14 signature domain and a Sec39 like domain. The protein is thought to be involved in Golgi-to-ER transport. Mutations in this gene are associated with short stature, optic nerve atrophy, and Pelger-Huet anomaly. [provided by RefSeq, Oct 2012].
- **Diseases (Open Targets)**: infantile liver failure syndrome 2 (0.817); short stature-optic atrophy-Pelger-Huët anomaly syndrome (0.793); infantile liver failure (0.548); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.546); hereditary optic neuropathy (0.421)
- **Europe PMC papers**: 2184
- **Why important**: NBAS has the strongest network position in the supplied subgraph and connects to COG8, NPC1, USP25, SLC33A1, and RNASEH2B. Its established role in the NRZ tethering complex and Golgi-to-ER retrograde transport provides a plausible anchor for the trafficking interpretation. It has direct STRING support with STX6 and appears with STX6 in hu.MAP complexes C3 through C6. Its disease associations include infantile liver failure and short stature–optic atrophy–Pelger-Huet anomaly syndrome, and its substantial literature supports a comparatively well-characterized role.
- **Conclusion**: Established evidence supports NBAS as a central trafficking and ER–Golgi maintenance gene with disease relevance. It is a strong candidate driver or marker of the module's trafficking component. It remains unproven that NBAS organizes the entire co-abundance module; that broader role is a hypothesis.

#### STX6

- **Related proteins** (co-abundance neighbors): IQGAP2 (0.85); STRING partners: COG8 (0.862), NBAS (0.79)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_06458.1, huMAP3_08929.1, huMAP3_10587.1, huMAP3_13160.1
- **Function (MyGene.info)**: syntaxin 6. Enables syntaxin binding activity. Involved in several processes, including Golgi ribbon formation; retrograde transport, endosome to Golgi; and vesicle fusion. Acts upstream of or within endocytic recycling. Located in several cellular components, including early endosome; perinuclear region of cytoplasm; and trans-Golgi network. Part of SNARE complex. [provided by Alliance of Genome Resources, A…
- **Diseases (Open Targets)**: progressive supranuclear palsy (0.372); sporadic Creutzfeld Jacob disease (0.268); alcohol drinking (0.227); menopause (0.166); neoplasm (0.102)
- **Europe PMC papers**: 850
- **Why important**: STX6 provides the clearest bridge between the network and external interaction resources. It is a Golgi and endosomal SNARE involved in vesicle fusion, endocytic recycling, and retrograde transport. It has high-confidence STRING relationships with COG8 and NBAS and is paired with NBAS in multiple hu.MAP complexes. Its HPA profile includes neutrophil enhancement, which also makes it relevant to the possibility of shared immune-cell composition.
- **Conclusion**: Established evidence supports STX6 as a vesicle-trafficking and membrane-fusion component that links several independently observed module relationships. Its co-abundance with the broader module may represent coordinated trafficking biology, but it could also partly reflect the abundance of neutrophil-associated or other shared cell populations.

#### FLOT1

- **Related proteins** (co-abundance neighbors): PHIP (0.81), NKRF (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_08718.1, huMAP3_09165.1
- **Function (MyGene.info)**: flotillin 1. This gene encodes an protein that localizes to the caveolae, which are small domains on the inner cell membranes. This protein plays a role in vesicle trafficking and cell morphology. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016].
- **Diseases (Open Targets)**: neurodegenerative disease (0.332); gastric cancer (0.101); hepatocellular carcinoma (0.101); neoplasm (0.097); lung adenocarcinoma (0.093)
- **Europe PMC papers**: 3298
- **Why important**: FLOT1 connects the module's transcriptional and trafficking-associated branches through PHIP and NKRF and is represented in hu.MAP complexes C1 and C2 with DSG2. Its established functions include caveolar or membrane-domain organization, vesicle trafficking, cell morphology, receptor internalization, and junction assembly. HPA associates it with neutrophils and late spermatids, while its lung protein detection supports the relevance of the lung observation.
- **Conclusion**: Established evidence supports FLOT1 as a membrane-organization and trafficking component. Its relationship with DSG2 is consistent with a membrane-junction submodule. Whether FLOT1 links this junctional branch causally to the NBAS–STX6 trafficking branch is a hypothesis rather than a demonstrated mechanism.

#### DSG2

- **Related proteins** (co-abundance neighbors): PARD3 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cell Junctions; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_08718.1, huMAP3_09165.1
- **Function (MyGene.info)**: desmoglein 2. This gene encodes a member of the desmoglein family and cadherin cell adhesion molecule superfamily of proteins. Desmogleins are calcium-binding transmembrane glycoprotein components of desmosomes, cell-cell junctions between epithelial, myocardial, and other cell types. The encoded preproprotein is proteolytically processed to generate the mature glycoprotein. This gene is present in a gene clust…
- **Diseases (Open Targets)**: arrhythmogenic right ventricular dysplasia 10 (0.812); arrhythmogenic right ventricular cardiomyopathy (0.781); dilated cardiomyopathy 1BB (0.714); familial isolated dilated cardiomyopathy (0.615); Abnormality of the cardiovascular system (0.552)
- **Europe PMC papers**: 3811
- **Why important**: DSG2 is the module's clearest epithelial junction and adhesion marker. It is a desmosomal cadherin involved in cell–cell adhesion and epithelial organization, and it connects to PARD3 in the co-abundance graph. Its membership with FLOT1 in hu.MAP complexes C1 and C2 supports a membrane-architecture interpretation. DSG2 also has established associations with arrhythmogenic and dilated cardiomyopathies, indicating substantial disease and functional relevance.
- **Conclusion**: Established evidence supports DSG2 as a cell-junction and epithelial-architecture gene. It could indicate epithelial or barrier-cell representation in the shared samples. A direct role for DSG2 in coordinating the module's intracellular trafficking machinery is not established and should remain a hypothesis.

#### SLC33A1

- **Related proteins** (co-abundance neighbors): NBAS (0.86), DPP9 (0.84), ATP13A1 (0.83), WASHC4 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 33 member 1. The protein encoded by this gene is required for the formation of O-acetylated (Ac) gangliosides. The encoded protein is predicted to contain 6 to 10 transmembrane domains, and a leucine zipper motif in transmembrane domain III. Defects in this gene have been reported to cause spastic paraplegia autosomal dominant type 42 (SPG42) in one Chinese family, but not in similar patients of European desce…
- **Diseases (Open Targets)**: Huppke-Brendel syndrome (0.721); hereditary spastic paraplegia 42 (0.632); Spastic paraplegia (0.479); neurodegenerative disease (0.463); hereditary spastic paraplegia (0.414)
- **Europe PMC papers**: 476
- **Why important**: SLC33A1 occupies a relatively central position among the module's local links, connecting NBAS with DPP9, ATP13A1, and WASHC4. It is a vesicular and cytosolic transporter implicated in acetyl-CoA transmembrane transport and formation of O-acetylated gangliosides. Its low tissue specificity and neural or glial cell-type enhancements support a broadly distributed organelle-maintenance role rather than a lung-specific marker. Disease associations include Huppke–Brendel syndrome and hereditary spastic paraplegia.
- **Conclusion**: Established evidence supports SLC33A1 as a membrane-transport and lipid or ganglioside-related component that could complement the module's trafficking interpretation. The evidence does not establish that its co-abundance with NBAS or the other genes reflects a shared acetyl-CoA pathway; that connection is a hypothesis.

#### COG8

- **Related proteins** (co-abundance neighbors): NBAS (0.90); STRING partners: STX6 (0.862)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: component of oligomeric golgi complex 8. This gene encodes a protein that is a component of the conserved oligomeric Golgi (COG) complex, a multiprotein complex that plays a structural role in the Golgi apparatus, and is involved in intracellular membrane trafficking and glycoprotein modification. Mutations in this gene cause congenital disorder of glycosylation, type IIh, a disease that is characterized by under-glycosylated serum prote…
- **Diseases (Open Targets)**: COG8-congenital disorder of glycosylation (0.788); neurodegenerative disease (0.430); Alzheimer disease (0.387); Parkinson disease (0.387); lysosomal storage disease (0.387)
- **Europe PMC papers**: 359
- **Why important**: COG8 is directly connected to NBAS in the module and to STX6 in STRING. Its established role in the conserved oligomeric Golgi complex, Golgi organization, retrograde transport, vesicle recycling, and glycoprotein modification provides a strong mechanistic link between the module graph and Golgi biology. Its disease association with a congenital disorder of glycosylation further demonstrates the physiological importance of this function.
- **Conclusion**: Established evidence supports COG8 as a Golgi trafficking and glycoprotein-processing component and as a plausible partner in the NBAS–STX6 trafficking axis. It strengthens the interpretation of a localized trafficking submodule, but does not demonstrate that all module genes participate in the same Golgi complex.

## Module 4

**Tissue pair**: lung and stem_cells  
**Genes (5)**: ACY1, CPVL, EML2, TP53I3, TST

### Function

No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The gene set is functionally heterogeneous but suggests a possible convergence of epithelial metabolic activity, mitochondrial sulfur and toxicant handling, amino-acid salvage, cytoskeletal regulation, and stress or cell-death biology. Established gene-level annotations include mitochondrial sulfurtransferase and ribosomal-RNA transport functions for TST, amino-acid catabolism and salvage for ACY1, microtubule regulation for EML2, protease-related activity for CPVL, and p53-linked oxidative-stress and apoptotic associations for TP53I3. These annotations support a cautious cellular-state interpretation rather than a defined pathway. The co-abundance structure is centered on CPVL, with links to TST, EML2, and TP53I3, while EML2 also links to ACY1.

**Cell composition.** The module is not predominantly secreted or plasma-protein based: only CPVL has an intracellular and membrane secretome classification, and the other genes are not classified as secreted. The HPA profile instead points toward tissue- and cell-type-restricted expression. Several genes are associated with intestinal or epithelial populations, especially enterocytes, colonocytes, and esophageal apical cells. Two genes have immune-cell-enhanced profiles involving myeloid dendritic cells or monocytes, while most genes have low immune-cell specificity. This pattern does not support a simple blood-contamination explanation, although shared epithelial or myeloid cell composition could contribute to the lung and stem-cell co-abundance signal. Protein detection in lung for most members supports lung relevance, whereas the lack of a matching HPA stem-cell tissue category limits interpretation in stem cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the possible gene pairs, no STRING functional-enrichment result was reported, and no hu.MAP complex contained multiple module members. Therefore, the observed co-abundance edges are not corroborated here by known physical interactions or a shared catalogued complex. The strongest edge pattern is an observational expression relationship centered on CPVL, not evidence that CPVL physically binds the connected proteins. The absence of STRING or hu.MAP support also means that any proposed common mechanism remains provisional.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a previously unreported tissue-pair co-abundance pattern because the module has no matching high-confidence STRING interactions, no reported STRING enrichment, and no multi-member hu.MAP complex. However, those absences do not establish biological novelty. The constituent genes have established individual functions, disease associations, and substantial literature, and the module may reflect shared epithelial, metabolic, stress-response, or immune-cell composition rather than a new molecular complex. A stronger novelty claim would require replication in independent lung and stem-cell datasets, adjustment for cell-type composition, and comparison with published co-expression modules.

**Hypothesis.** Hypothesis: this module reflects a conserved cellular-state program in which epithelial or progenitor-like cells coordinate amino-acid salvage, mitochondrial sulfur and toxicant processing, cytoskeletal organization, and oxidative-stress or p53-linked responses. CPVL may mark the central co-abundance state, with TST contributing mitochondrial redox and sulfur handling, ACY1 contributing amino-acid salvage, EML2 contributing cytoskeletal regulation, and TP53I3 contributing stress-linked apoptosis. The HPA cell-type pattern raises an alternative hypothesis that the signal is driven partly by shared epithelial populations, with a smaller contribution from myeloid cells. These are hypotheses from co-abundance and annotations, not demonstrated causal interactions.

### Important genes

#### CPVL

- **Related proteins** (co-abundance neighbors): TST (0.82), EML2 (0.81), TP53I3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carboxypeptidase vitellogenic like. The protein encoded by this gene is a carboxypeptidase and bears strong sequence similarity to serine carboxypeptidases. Carboxypeptidases are a large class of proteases that act to cleave a single amino acid from the carboxy termini of proteins or peptides. The exact function of this protein, however, has not been determined. [provided by RefSeq, Jan 2017].
- **Diseases (Open Targets)**: basal cell carcinoma (0.553); skin neoplasm (0.547); skin cancer (0.534); hypothyroidism (0.510); non-melanoma skin carcinoma (0.488)
- **Europe PMC papers**: 621
- **Why important**: CPVL is the network hub in this module, connecting TST, EML2, and TP53I3. Its annotated carboxypeptidase-like function provides a plausible proteolytic or peptide-processing component, although its exact function remains undetermined. HPA places it in lymphoid and choroid-plexus-associated tissue profiles and in myeloid and macrophage-related cell types, while detecting its protein in lung. Its disease associations include skin neoplasms and hypothyroidism, and its literature volume is substantial.
- **Conclusion**: Established: CPVL is the central co-abundance node and has carboxypeptidase-like and immune-cell-associated annotations. Hypothesis: CPVL may coordinate peptide processing with the metabolic or stress-related state represented by neighboring genes. The network position does not prove that it regulates the other module members.

#### TST

- **Related proteins** (co-abundance neighbors): CPVL (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thiosulfate sulfurtransferase. This is one of two neighboring genes encoding similar proteins that each contain two rhodanese domains. The encoded protein is localized to the mitochondria and catalyzes the conversion of thiosulfate and cyanide to thiocyanate and sulfite. In addition, the protein interacts with 5S ribosomal RNA and facilitates its import into the mitochondria. Alternative splicing results in multiple transcript …
- **Diseases (Open Targets)**: neurodegenerative disease (0.356); atopic eczema (0.306); severe acute respiratory syndrome (0.287); COVID-19 (0.287); tuberculosis (0.105)
- **Europe PMC papers**: 14284
- **Why important**: TST connects directly to CPVL and has a mitochondrial location. Its established activities include conversion of thiosulfate and cyanide to thiocyanate and sulfite, sulfur-related catabolism, response to toxic substances, and mitochondrial ribosomal-RNA import. HPA associates it with liver and several epithelial populations, including enterocytes, colonocytes, and esophageal apical cells, and detects its protein in lung. It has the largest literature volume among the module genes and disease associations involving neurodegenerative disease, atopic eczema, severe acute respiratory syndrome, and COVID nineteen.
- **Conclusion**: Established: TST is a mitochondrial sulfurtransferase with toxicant-response and mitochondrial RNA-related functions. Hypothesis: TST may represent a mitochondrial detoxification or redox component of the shared module. Its direct co-abundance with CPVL is not evidence of a physical interaction.

#### ACY1

- **Related proteins** (co-abundance neighbors): EML2 (0.81); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aminoacylase 1. This gene encodes a cytosolic, homodimeric, zinc-binding enzyme that catalyzes the hydrolysis of acylated L-amino acids to L-amino acids and an acyl group, and has been postulated to function in the catabolism and salvage of acylated amino acids. This gene is located on chromosome 3p21.1, a region reduced to homozygosity in small-cell lung cancer (SCLC), and its expression has been reported to be …
- **Diseases (Open Targets)**: aminoacylase 1 deficiency (0.810); Intellectual disability (0.466); hereditary disease (0.452); toxic encephalopathy (0.370); inborn aminoacylase deficiency (0.266)
- **Europe PMC papers**: 719
- **Why important**: ACY1 is an enzyme involved in hydrolysis of acylated amino acids and proposed amino-acid salvage, and it is connected to EML2 in the module. HPA describes group-enriched expression in intestine, kidney, and liver and enrichment in colonocytes and enterocytes, with no lung protein detection. Its disease associations include aminoacylase deficiency and intellectual disability, and the fact sheet notes reduced or absent expression in small-cell lung cancer models. These features make it relevant to metabolic state and possible epithelial lineage composition.
- **Conclusion**: Established: ACY1 supports amino-acid metabolism and salvage and has strong intestinal and renal tissue associations. Hypothesis: ACY1 may indicate a differentiated epithelial metabolic program within the shared module. The absence of lung protein detection cautions against interpreting it as a uniformly active lung protein.

#### EML2

- **Related proteins** (co-abundance neighbors): CPVL (0.81), ACY1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EMAP like 2. Enables microtubule binding activity. Involved in negative regulation of microtubule polymerization and regulation of microtubule nucleation. Colocalizes with mitotic spindle. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.445); Abnormality of the skeletal system (0.299); cervical carcinoma (0.289); type 2 diabetes mellitus (0.232); diabetes mellitus (0.195)
- **Europe PMC papers**: 326
- **Why important**: EML2 occupies an intermediate network position, linking CPVL to ACY1. Its established molecular functions include microtubule binding, regulation of microtubule nucleation, inhibition of microtubule polymerization, and association with the mitotic spindle. HPA reports low tissue specificity and cell-type enhancement in rod photoreceptors and syncytiotrophoblasts, with lung protein detection. Its disease associations include neurodegenerative disease, skeletal abnormality, cervical carcinoma, and diabetes-related conditions.
- **Conclusion**: Established: EML2 contributes to cytoskeletal and microtubule regulation. Hypothesis: EML2 may connect epithelial metabolic state to cell architecture or proliferative organization. The module does not establish that its cytoskeletal function is the driver of the shared co-abundance pattern.

#### TP53I3

- **Related proteins** (co-abundance neighbors): CPVL (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tumor protein p53 inducible protein 3. The protein encoded by this gene is similar to oxidoreductases, which are enzymes involved in cellular responses to oxidative stresses and irradiation. This gene is induced by the tumor suppressor p53 and is thought to be involved in p53-mediated cell death. It contains a p53 consensus binding site in its promoter region and a downstream pentanucleotide microsatellite sequence. P53 has been shown …
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.094); lung adenocarcinoma (0.083); metastatic malignant neoplasm in the lymph nodes (0.061); acute pancreatitis (0.052); hypertensive disorder (0.049)
- **Europe PMC papers**: 789
- **Why important**: TP53I3 connects to the CPVL hub and is annotated as a p53-inducible protein related to oxidoreductases. Its established associations include oxidative-stress biology, reactive oxygen species production, and apoptosis. HPA places it in esophageal tissue and in several epithelial cell types, including enterocytes and esophageal apical and suprabasal cells, and detects its protein in lung. Its disease associations include non-small-cell lung carcinoma and lung adenocarcinoma, although the reported disease-association strengths are modest.
- **Conclusion**: Established: TP53I3 is linked to p53-mediated stress and cell-death biology and is relevant to lung cancer annotations. Hypothesis: TP53I3 may mark a stress-responsive component of the module that accompanies metabolic and mitochondrial activity. Co-abundance with CPVL does not demonstrate direct p53 regulation of the entire module.

## Module 5

**Tissue pair**: lung and stem_cells  
**Genes (23)**: ADAM9, ATP1A1, COQ8A, CTTNBP2NL, EXD2, FKBP14, FKBP9, FNDC3A, GIT2, PIGK, HSP90AB4P, IFIT5, KIF14, MED6, MTA2, NUCB2, SCYL3, MRPS23, SCFD2, TM9SF2, USP33, VPS45, WDR44

### Function

This is a heterogeneous intracellular homeostasis and trafficking module rather than a sharply defined pathway. Its strongest biological signals are vesicle-mediated transport, vesicle docking, Golgi and endosomal organization, cytoskeletal and microtubule processes, protein folding, deubiquitination, membrane transport, transcriptional regulation, mitochondrial activity, and innate immune signaling. These themes are supported by the annotations of SCFD2, VPS45, WDR44, TM9SF2, FKBP14, FKBP9, USP33, ATP1A1, IFIT5, MTA2, COQ8A, and related genes. However, no GO or KEGG term passed global correction, so these annotations provide biological context rather than statistically validated module enrichment. The sparse network and mixed annotations are consistent with a co-abundance program reflecting several linked aspects of cellular maintenance rather than one narrowly specialized function.

**Cell composition.** The module does not appear to be dominated by plasma proteins, broadly secreted proteins, or blood-cell markers. Most annotated genes have low tissue specificity, and most have low immune-cell specificity. A minority show immune or myeloid associations, including CTTNBP2NL, GIT2, FNDC3A, FKBP9, and ADAM9, while KIF14 is enhanced in bone marrow and lymphoid tissue. Five genes are annotated as secreted or potentially secreted, including NUCB2 and ADAM9, but this is not the prevailing composition. Lung protein detection is widespread among the annotated genes, whereas the stem-cell comparison has no matching HPA tissue dataset. The shared signal is therefore more plausibly related to broadly distributed cellular programs, with possible contributions from epithelial, stromal, and occasional immune cell populations, than to simple blood contamination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no high-confidence interactions among the module genes and no supplementary STRING enrichment. This argues against interpreting the co-abundance edges as established physical interactions. hu.MAP provides the main external support: SCFD2 and VPS45 co-occur in complexes (hu.MAP huMAP3_06458.1), (hu.MAP huMAP3_08929.1), (hu.MAP huMAP3_10587.1), and (hu.MAP huMAP3_13160.1). Those complexes contain many vesicle, SNARE, syntaxin, and vesicle-fusion components, consistent with intracellular transport and docking. The fact that only SCFD2 and VPS45 from the module occur in those large complexes means the hu.MAP evidence supports a vesicle-trafficking anchor, not a complete physical complex formed by the whole module. The remaining edges may represent coordinated expression, indirect regulation, shared cell composition, or technical covariance rather than direct molecular binding.

**STRING interactions (score >= 0.7)**: 0 of 253 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06458.1 (SCFD2, VPS45; 2/41); huMAP3_08929.1 (SCFD2, VPS45; 2/44); huMAP3_10587.1 (SCFD2, VPS45; 2/45); huMAP3_13160.1 (SCFD2, VPS45; 2/49)

### Novelty

This module should not be called a newly discovered molecular complex or a newly established pathway. The lack of STRING interactions and the absence of globally significant GO or KEGG enrichment make a strong novelty claim inappropriate. Its potentially new aspect is the cross-tissue co-abundance pattern linking vesicle trafficking genes with deubiquitination, chromatin regulation, mitochondrial function, membrane transport, and innate immune genes in lung and stem-cell samples. That pattern is hypothesis-generating, but it requires replication in independent cohorts, control for cell composition, and experimental or perturbational testing before it can be considered a novel biological mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-maintenance state in which vesicle docking and intracellular transport are coordinated with protein quality control, cytoskeletal organization, membrane ion homeostasis, transcriptional regulation, and stress or innate immune responsiveness. SCFD2 and VPS45 may provide a trafficking-related backbone, while USP33, FKBP14, FKBP9, and MTA2 could connect trafficking to protein modification, folding, and transcriptional state. In lung, this state may be expressed across epithelial and other resident cells, with occasional myeloid contributions. The observed co-abundance could also arise partly from shared cell types or sample composition, so this mechanism remains provisional.

### Important genes

#### VPS45

- **Related proteins** (co-abundance neighbors): FNDC3A (0.89), USP33 (0.82), SCYL3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_06458.1, huMAP3_08929.1, huMAP3_10587.1, huMAP3_13160.1
- **Function (MyGene.info)**: vacuolar protein sorting 45 homolog. Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene is a member of the Sec1 domain family, and shows a high degree of sequence similarity to mouse, rat and yeast Vps45. The exact func…
- **Diseases (Open Targets)**: congenital neutropenia-myelofibrosis-nephromegaly syndrome (0.787); severe congenital neutropenia (0.549); neurodegenerative disease (0.462); COVID-19 (0.371); hereditary disease (0.192)
- **Europe PMC papers**: 811
- **Why important**: VPS45 is a highly connected module member and links directly to FNDC3A, USP33, and SCYL3. Its established role is in vacuolar protein sorting and vesicle-mediated transport. It is the clearest trafficking-related anchor in the module and is present with SCFD2 in all listed hu.MAP complexes (hu.MAP huMAP3_06458.1), (hu.MAP huMAP3_08929.1), (hu.MAP huMAP3_10587.1), and (hu.MAP huMAP3_13160.1). Its association with severe congenital neutropenia and related disease makes it relevant to cellular trafficking and immune-cell biology. Its literature support is substantial relative to most module members.
- **Conclusion**: Established evidence supports VPS45 as an intracellular trafficking component and as one of the module's best-supported structural anchors through hu.MAP. It is plausible, but not proven, that VPS45 helps organize the shared co-abundance state.

#### SCFD2

- **Related proteins** (co-abundance neighbors): MED6 (0.85), USP33 (0.84), EXD2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_06458.1, huMAP3_08929.1, huMAP3_10587.1, huMAP3_13160.1
- **Function (MyGene.info)**: sec1 family domain containing 2. Predicted to enable syntaxin binding activity. Predicted to be involved in intracellular protein transport and vesicle docking involved in exocytosis. Predicted to be active in plasma membrane and secretory granule. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: open-angle glaucoma (0.407); insomnia (0.289); deficiency anemia (0.285); Pancreatic pseudocyst (0.271); male reproductive organ cancer (0.239)
- **Europe PMC papers**: 201
- **Why important**: SCFD2 connects to USP33, MED6, and EXD2 and is the other module member repeatedly represented with VPS45 in hu.MAP complexes (hu.MAP huMAP3_06458.1), (hu.MAP huMAP3_08929.1), (hu.MAP huMAP3_10587.1), and (hu.MAP huMAP3_13160.1). Its predicted syntaxin-binding activity and predicted roles in vesicle docking and exocytosis make it particularly informative for interpreting the trafficking component. Its lung protein detection and low tissue specificity fit a broadly distributed cellular process, while its disease associations provide additional biomedical relevance despite limited direct mechanistic characterization.
- **Conclusion**: Established evidence supports SCFD2 as a predicted vesicle-docking and syntaxin-related factor with complex-level support from hu.MAP. Its role as a central coordinator of this module is a reasonable hypothesis, but the co-abundance data do not establish direct interaction or causality.

#### USP33

- **Related proteins** (co-abundance neighbors): KIF14 (0.90), FKBP14 (0.88), SCFD2 (0.84), VPS45 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin specific peptidase 33. This gene encodes a deubiquinating enzyme important in a variety of processes, including Slit-dependent cell migration and beta-2 adrenergic receptor signaling. The protein is negatively regulated through ubiquitination by von Hippel-Lindau tumor protein (VHL). Alternative splicing results in multiple transcript variants and protein isoforms. [provided by RefSeq, Jun 2012].
- **Diseases (Open Targets)**: neoplasm (0.098); lung cancer (0.087); lung carcinoma (0.087); pancreatic ductal adenocarcinoma (0.087); lymphoid neoplasm (0.086)
- **Europe PMC papers**: 729
- **Why important**: USP33 has one of the strongest network positions in the module and connects the trafficking-related genes VPS45 and SCFD2 with KIF14 and FKBP14. It encodes a deubiquitinating enzyme involved in protein deubiquitination, cell migration, axon guidance, and regulation of G protein-coupled receptor signaling. Its Golgi and nucleoplasmic localization provides a possible bridge between membrane trafficking and regulatory signaling. It also has a comparatively large literature base and disease links involving neoplasia and lung cancer.
- **Conclusion**: Established evidence supports USP33 as a regulatory deubiquitinase with roles in migration and receptor signaling. Its placement near trafficking genes suggests a possible regulatory bridge in the module, but the module does not demonstrate that USP33 controls VPS45 or SCFD2.

#### ATP1A1

- **Related proteins** (co-abundance neighbors): COQ8A (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 is the module's clearest membrane ion-homeostasis marker. It encodes the sodium-potassium pump alpha subunit and is annotated in sodium and potassium transport, electrochemical-gradient maintenance, and osmosensory signaling. Its connection to COQ8A links membrane physiology to mitochondrial and respiratory-chain biology. HPA identifies lung detection and enhancement in alveolar type one cells, making it especially relevant to the lung context. It also has extensive disease literature involving cardiac, neurological, and electrolyte-related disorders.
- **Conclusion**: Established evidence supports ATP1A1 as a core membrane homeostasis protein with direct relevance to lung epithelial physiology. Its inclusion may indicate that the module captures a broader cellular state rather than only vesicle trafficking; any connection to the other module components remains inferential.

#### FKBP14

- **Related proteins** (co-abundance neighbors): USP33 (0.88), CTTNBP2NL (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FKBP prolyl isomerase 14. The protein encoded by this gene is a member of the FK506-binding protein family of peptidyl-prolyl cis-trans isomerases. The encoded protein is found in the lumen of the endoplasmic reticulum, where it is thought to accelerate protein folding. Defects in this gene are a cause of a type of Ehlers-Danlos syndrome (EDS). Both a protein-coding variant and noncoding variants are transcribed from this …
- **Diseases (Open Targets)**: Ehlers-Danlos syndrome, kyphoscoliotic type, 2 (0.764); Abnormality of the cardiovascular system (0.515); Hypotonia (0.362); Pes valgus (0.333); Thoracolumbar scoliosis (0.333)
- **Europe PMC papers**: 475
- **Why important**: FKBP14 connects USP33 with CTTNBP2NL and encodes an endoplasmic-reticulum-associated peptidyl-prolyl isomerase involved in protein folding. Its disease association with kyphoscoliotic Ehlers-Danlos syndrome provides strong evidence that altered protein maturation and connective-tissue biology can have organism-level consequences. Its low immune specificity and intracellular or membrane secretome annotation argue against interpreting it as a blood-derived secreted marker.
- **Conclusion**: Established evidence supports FKBP14 as a protein-folding factor with a clear inherited disease connection. Within this module it may represent a proteostasis arm linked to trafficking and cytoskeletal regulation, but that integrative role is a hypothesis.

## Module 6

**Tissue pair**: lung and stem_cells  
**Genes (25)**: AFG2B, ANXA7, ATXN2L, C5orf22, CFAP298, DCAF7, FTO, GALK1, GAR1, LMO7, NUP43, OSBPL11, PAPSS1, PARG, PXN, PDRG1, PIK3C3, PPP4R1, PSMC2, CRYZL1, ROCK1, POLR2D, CTTN, TOR1AIP2, TTC5

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established pathway assignment from enrichment. The individual gene annotations and network structure instead suggest a mixed cellular program involving nuclear gene expression and stress or damage responses, intracellular membrane and lipid handling, cytoskeletal adhesion, and epithelial or ciliary biology. POLR2D, TTC5, PDRG1, AFG2B, PARG, and PSMC2 support transcriptional, protein-quality, DNA-damage, and proteostasis processes, whereas OSBPL11 and PIK3C3 support lipid transfer, endosomal organization, and autophagy. CTTN, PXN, LMO7, ROCK1, and PPP4R1 support actin organization, adhesion, migration, and signaling. The sparse network and lack of globally significant enrichment argue against calling this a single definitive biochemical pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and lung protein detection is common among the genes with available data, supporting a broadly expressed cellular component rather than a lung-exclusive secretory program. At the same time, cell-type enhancement is frequent, especially for esophageal apical cells, neutrophils, late primary spermatocytes, respiratory ciliated cells, and astrocytes. Several genes show immune-cell enhancement or enrichment, including CTTN, PXN, PPP4R1, ROCK1, C5orf22, and PAPSS1, with neutrophil and basophil signals particularly recurrent. This raises the possibility that the shared lung and stem_cells module partly reflects common epithelial or ciliated cell states and, depending on sample composition, some blood or immune-cell contribution. The HPA evidence does not by itself establish contamination or a particular cell mixture.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, CTTN-PXN, linking cortactin and paxillin in a focal-adhesion and actin-associated context. This is consistent with the individual annotations for cell adhesion, actin organization, substrate attachment, and migration, and it is the clearest already-known physical or functional connection in the module. No STRING functional-enrichment result was reported. hu.MAP identifies partial overlap with three complexes. GALK1 and TTC5 occur together in (hu.MAP huMAP3_10665.1), while POLR2D and PDRG1 occur together in (hu.MAP huMAP3_14318.1) and (hu.MAP huMAP3_11092.1). These overlaps connect the module to broader multiprotein assemblies involving metabolic, transcriptional, RNA-polymerase-associated, and protein-folding machinery, but only a small subset of members from each complex is present. Thus, the hu.MAP evidence supports isolated complex membership rather than a complete assembled complex represented by the module.

**STRING interactions (score >= 0.7)**: 1 of 300 gene pairs: CTTN–PXN (0.997)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10665.1 (GALK1, TTC5; 2/42); huMAP3_14318.1 (POLR2D, PDRG1; 2/58); huMAP3_11092.1 (POLR2D, PDRG1; 2/65)

### Novelty

The module may be a novel co-abundance pattern, but the evidence does not justify claiming a newly discovered biological pathway or a new molecular interaction. The CTTN-PXN relationship is already represented in STRING, and the POLR2D-PDRG1 and GALK1-TTC5 overlaps are represented in hu.MAP. Most other within-module relationships are not supported by these reference resources, but absence from STRING or hu.MAP does not prove that they are novel or direct. The strongest defensible conclusion is that this particular cross-tissue co-abundance organization appears potentially under-characterized, while its component functions and some of its relationships are established. Demonstrating novelty would require comparison with published co-expression modules, independent tissue cohorts, cell-type-resolved data, and replication in an external dataset.

**Hypothesis.** Hypothesis: this module represents a shared epithelial or progenitor-cell state in which transcriptional and proteostatic capacity is coordinated with membrane-lipid trafficking, autophagy, cytoskeletal adhesion, and ciliary or cell-surface organization. In lung, the signal could be contributed by respiratory ciliated or alveolar epithelial cells and possibly immune cells; in stem_cells, it could reflect a common proliferative, differentiation, or stress-adaptation state rather than a lung-specific function. A possible mechanistic axis is that cellular stress or changing membrane composition engages OSBPL11 and PIK3C3-dependent membrane and autophagy processes, while TTC5, POLR2D, PDRG1, and associated nuclear machinery adjust gene expression and protein handling, and CTTN-PXN with ROCK1 and LMO7 coordinates adhesion and actin remodeling. This is a testable model, not an enrichment-supported conclusion.

### Important genes

#### POLR2D

- **Related proteins** (co-abundance neighbors): AFG2B (0.84), TTC5 (0.81), CFAP298 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase II subunit D. This gene encodes the fourth largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. In yeast, this polymerase subunit is associated with the polymerase under suboptimal growth conditions and may have a stress protective role. A sequence for a ribosomal pseudogene is contained within the 3' untranslated region of the transcript from this gene.…
- **Diseases (Open Targets)**: HIV infectious disease (0.600); acrocephalosyndactyly (0.370); dengue disease (0.370); Orthomyxoviridae infectious disease (0.370); Alzheimer disease (0.235)
- **Europe PMC papers**: 361
- **Why important**: POLR2D is a core RNA polymerase II subunit and occupies a bridge in the module between AFG2B, TTC5, and CFAP298. It is present in the two hu.MAP assemblies (hu.MAP huMAP3_14318.1) and (hu.MAP huMAP3_11092.1), which independently connect it to broad transcriptional machinery. Its annotation supports transcription initiation and elongation, while its lung detection and association with late spermatocytes and late spermatids suggest that its co-abundance may track a differentiated or highly regulated cellular state. Its literature volume is substantial relative to many less-characterized module members.
- **Conclusion**: Established evidence supports POLR2D as a transcriptional machinery component and as a connector to hu.MAP complexes (hu.MAP huMAP3_14318.1) and (hu.MAP huMAP3_11092.1). It is reasonable to hypothesize that POLR2D helps couple the module to cell-state-dependent transcription, but the co-abundance data do not establish that it regulates the other module genes.

#### TTC5

- **Related proteins** (co-abundance neighbors): PAPSS1 (0.85), ROCK1 (0.82), ATXN2L (0.82), POLR2D (0.81), FTO (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_10665.1
- **Function (MyGene.info)**: tetratricopeptide repeat domain 5. Predicted to enable DNA binding activity and chromatin binding activity. Predicted to be involved in DNA repair. Predicted to act upstream of or within positive regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder with cerebral atrophy and variable facial dysmorphism (0.739); autosomal recessive non-syndromic intellectual disability (0.370); neurodevelopmental disorder (0.370); Neurodevelopmental delay (0.118); autosomal recessive spondylocostal dysostosis (0.075)
- **Europe PMC papers**: 767
- **Why important**: TTC5 has a relatively central position in the module and connects PAPSS1, ROCK1, ATXN2L, POLR2D, and FTO. Its annotations support DNA-damage response, chromatin or DNA binding, regulation of gene expression, and RNA metabolism. It also participates in hu.MAP complex (hu.MAP huMAP3_10665.1) with GALK1. The combination of network connectivity, nuclear localization, lung detection, respiratory ciliated-cell enhancement, and substantial literature makes TTC5 a plausible state-regulatory gene rather than a passive marker.
- **Conclusion**: Established evidence supports roles for TTC5 in DNA-damage-related and transcription-associated processes, with membership in (hu.MAP huMAP3_10665.1). The idea that TTC5 coordinates stress responses with ciliary or epithelial state in this module remains a hypothesis requiring perturbation or cell-state-resolved validation.

#### OSBPL11

- **Related proteins** (co-abundance neighbors): DCAF7 (0.86), AFG2B (0.85), C5orf22 (0.82), PIK3C3 (0.81), GAR1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: oxysterol binding protein like 11. This gene encodes a member of the oxysterol-binding protein (OSBP) family, a group of intracellular lipid receptors. Like most members, the encoded protein contains an N-terminal pleckstrin homology domain and a highly conserved C-terminal OSBP-like sterol-binding domain. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.444); COVID-19 (0.282); severe acute respiratory syndrome (0.282); ovarian neoplasm (0.156); circadian rhythm sleep disorder (0.138)
- **Europe PMC papers**: 203
- **Why important**: OSBPL11 is among the more connected genes and links AFG2B, DCAF7, C5orf22, PIK3C3, and GAR1. Its established annotation as an intracellular sterol and phospholipid-transfer protein gives the module a plausible membrane-lipid component. It is tissue enhanced in skeletal muscle and tongue and cell-type enhanced in several metabolically or structurally specialized cell types, including neutrophils. Its literature volume is meaningful, although the module contains no direct STRING or hu.MAP relationship for OSBPL11.
- **Conclusion**: Established evidence supports OSBPL11 in phospholipid transfer, lipid homeostasis, and lysosomal membrane organization. It is a strong candidate for linking membrane composition to the module, but its proposed coordination with PIK3C3 or cytoskeletal genes is currently a hypothesis based on co-abundance and annotation rather than demonstrated interaction.

#### PIK3C3

- **Related proteins** (co-abundance neighbors): PDRG1 (0.83), OSBPL11 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphatidylinositol 3-kinase catalytic subunit type 3. Enables 1-phosphatidylinositol-3-kinase activity. Involved in early endosome to late endosome transport and regulation of cytokinesis. Acts upstream of or within autophagy and protein lipidation. Located in autolysosome; late endosome; and midbody. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.544); alcohol drinking (0.474); COVID-19 (0.470); obesity disorder (0.452); type 2 diabetes mellitus (0.384)
- **Europe PMC papers**: 3625
- **Why important**: PIK3C3 connects OSBPL11 with PDRG1 and has a well-established role in endosome organization, autophagy, autophagosome assembly, and lysosomal targeting. It is broadly expressed by HPA and detected in lung, making it compatible with a general cellular maintenance program rather than a plasma or secreted signal. Its extensive literature and disease relevance make it one of the best-supported mechanistic anchors in the module, despite its limited local connectivity.
- **Conclusion**: Established evidence supports PIK3C3 as an endosomal and autophagy regulator. Its placement next to OSBPL11 is consistent with a possible lipid-trafficking-to-autophagy connection, but the module does not demonstrate that this pathway is the principal driver of the shared lung and stem_cells signal.

#### CTTN

- **Related proteins** (co-abundance neighbors): CRYZL1 (0.81), TOR1AIP2 (0.80); STRING partners: PXN (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Plasma membrane; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cortactin. This gene is overexpressed in breast cancer and squamous cell carcinomas of the head and neck. The encoded protein is localized in the cytoplasm and in areas of the cell-substratum contacts. This gene has two roles: (1) regulating the interactions between components of adherens-type junctions and (2) organizing the cytoskeleton and cell adhesion structures of epithelia and carcinoma cells. During …
- **Diseases (Open Targets)**: drug allergy (0.349); placenta praevia (0.265); response to antihypertensive drug (0.260); gallbladder disorder (0.258); non-autoimmune hemolytic anemia (0.240)
- **Europe PMC papers**: 2395
- **Why important**: CTTN is the module member with the clearest high-confidence STRING relationship, partnering with PXN. Its established functions include actin cytoskeleton organization, adherens-junction regulation, receptor-mediated endocytosis, and epithelial adhesion structures. It is cell-type enhanced in epithelial and neural populations and immune-cell enhanced in basophils and neutrophils. Its substantial literature, lung detection, and connection to CRYZL1 and TOR1AIP2 make it an informative marker of the module's structural and adhesion-related component.
- **Conclusion**: Established evidence supports CTTN as an actin- and adhesion-associated protein, and supports its relationship with PXN. It is plausible that CTTN-PXN captures a shared adhesion or migration state across tissues, but the module cannot distinguish epithelial remodeling from immune-cell-associated cytoskeletal activity.

#### PXN

- **Related proteins** (co-abundance neighbors): CRYZL1 (0.82); STRING partners: CTTN (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Focal adhesion sites; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: paxillin. This gene encodes a cytoskeletal protein involved in actin-membrane attachment at sites of cell adhesion to the extracellular matrix (focal adhesion). Alternatively spliced transcript variants encoding different isoforms have been described for this gene. These isoforms exhibit different expression pattern, and have different biochemical, as well as physiological properties (PMID:9054445). [provid…
- **Diseases (Open Targets)**: atrial fibrillation (0.421); Abnormality of the skeletal system (0.342); Dupuytren Contracture (0.283); cardiac arrhythmia (0.275); hypertrophic cardiomyopathy (0.265)
- **Europe PMC papers**: 3057
- **Why important**: PXN provides the paired partner to CTTN in the only high-confidence STRING relationship reported within the module. Paxillin is an established focal-adhesion scaffold involved in actin-membrane attachment, cell adhesion, migration, spreading, and signal-complex assembly. Its enhancement in extravillous trophoblasts and neutrophils, immune-cell enhancement, and lung detection make it relevant to both structural and cell-migration interpretations. Its literature volume is substantial and its annotation is directly compatible with the CTTN connection.
- **Conclusion**: Established evidence supports PXN as a focal-adhesion and signaling scaffold, with a known relationship to CTTN. The most defensible module-level interpretation is that this pair marks an adhesion or motility-associated substructure; whether it is central to the shared tissue module or reflects a particular cell type remains unresolved.

## Module 7

**Tissue pair**: lung and stem_cells  
**Genes (26)**: AGO2, ANAPC1, ARHGEF1, ASCC3, TP53BP2, BOD1L1, RNF40, CDKN2AIP, CCDC25, SPECC1, DIAPH1, GCC2, INTS4, PPFIBP1, LRBA, MKLN1, NCOR1, PHACTR4, RBM27, RNF31, RPTOR, SCAF8, SMG8, TMA16, TXNRD2, URB2

### Function

The module does not have any GO or KEGG term passing global correction; therefore no pathway is established as significantly enriched. Its genes instead point to a broad regulatory program spanning cell-cycle control and ubiquitin-dependent proteolysis through ANAPC1, RNA surveillance and ribosome biogenesis through SMG8, URB2, TMA16 and related genes, transcriptional and chromatin regulation through NCOR1, RNF40 and SCAF8, DNA-damage responses through CDKN2AIP, ASCC3 and BOD1L1, and cytoskeletal, adhesion and Rho signaling through DIAPH1, PHACTR4, ARHGEF1 and MKLN1. Additional links to mTOR regulation, mitochondrial redox control, vesicle trafficking and immune signaling are present in the annotations. Thus, the most defensible interpretation is a mixed cellular-maintenance and stress-response module rather than a single canonical pathway. The sparse co-abundance graph hu.MAP supports coordinated expression, but does not by itself establish a physical or biochemical complex.

**Cell composition.** The module is not dominated by plasma or secreted proteins: no member is annotated as secreted. Most genes have low tissue specificity, and lung protein detection is widespread among the members, whereas there is no matching HPA tissue for stem cells. Many members are cell-type enhanced, including genes associated with neutrophils, hematopoietic stem cells, lymphoid cells, brain cell types, reproductive cells and muscle-related cells. Most genes have low immune-cell specificity, with a smaller subset showing immune-cell enhancement or enrichment. This argues against a strongly blood-cell-specific module, although shared cell types, sample cellular composition, or broadly expressed housekeeping and regulatory programs could contribute to its recurrence in lung and stem-cell data. The lymphoid- and brain-enhanced tissue annotations are notable but do not define the module as lung-specific or stem-cell-specific.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional-enrichment result is available, and none of the possible within-module gene pairs reaches the supplied STRING interaction threshold. No hu.MAP complex contains multiple module members. Consequently, the co-abundance relationships are not supported here by high-confidence known protein-protein interactions or by a known multiprotein complex. This favors an interpretation as coordinated regulation, shared cellular state, or indirect network coupling rather than a single established molecular machine. The absence of STRING or hu.MAP support is evidence of limited prior network annotation, not evidence that the co-abundance signal is false.

**STRING interactions (score >= 0.7)**: 0 of 325 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may represent a previously unreported co-abundance pattern, because the supplied resources show no high-confidence STRING interactions, no multi-member hu.MAP complex, no STRING enrichment, and no globally significant GO or KEGG term. However, these observations do not prove biological novelty. Several members have well-established individual functions and substantial literature, and a sparse co-abundance module can arise from shared expression state, cell composition, or indirect regulation. The appropriate conclusion is that the joint module-level finding appears under-annotated and potentially novel, but requires independent replication, preservation testing, cell-composition adjustment, and validation at the transcript or protein level before being called a new biological mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-maintenance state in which proliferative or progenitor-like cells coordinate proteostasis, RNA quality control, DNA-damage handling, cytoskeletal remodeling and nutrient or redox responses. ANAPC1, SMG8, URB2 and related genes could represent the regulatory and biosynthetic core, while RNF31, ARHGEF1, DIAPH1, PHACTR4, MKLN1 and LRBA could connect that core to inflammatory signaling, membrane trafficking and cytoskeletal adaptation. In lung, this state could be expressed by epithelial, stromal or immune-associated cells; in stem-cell material, it could reflect progenitor maintenance or differentiation state. This is a testable hypothesis, not an established pathway assignment, because the module lacks globally significant enrichment and known physical-complex support.

### Important genes

#### ANAPC1

- **Related proteins** (co-abundance neighbors): ASCC3 (0.90), TMA16 (0.87), RNF31 (0.86), SMG8 (0.86), ARHGEF1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: anaphase promoting complex subunit 1. This gene encodes a subunit of the anaphase-promoting complex. This complex is an E3 ubiquitin ligase that regulates progression through the metaphase to anaphase portion of the cell cycle by ubiquitinating proteins which targets them for degradation. [provided by RefSeq, Dec 2011].
- **Diseases (Open Targets)**: Rothmund-Thomson syndrome type 1 (0.776); Rothmund-Thomson syndrome (0.375); Splenomegaly (0.271); Alzheimer disease (0.249); injury (0.248)
- **Europe PMC papers**: 575
- **Why important**: ANAPC1 has the strongest network position in the supplied module, linking the module to ASCC3, TMA16, RNF31, SMG8 and ARHGEF1. Its established role as a subunit of the anaphase-promoting complex connects the module to mitotic progression, regulated protein degradation and cell-cycle control. It also has substantial literature and an association with Rothmund-Thomson syndrome in the supplied disease evidence.
- **Conclusion**: Established evidence supports ANAPC1 as a plausible structural and functional anchor for cell-cycle and ubiquitin-dependent regulation. It is reasonable to treat it as a module anchor, but the co-abundance data do not establish that the other members physically assemble with the anaphase-promoting complex.

#### SMG8

- **Related proteins** (co-abundance neighbors): BOD1L1 (0.87), ANAPC1 (0.86), CCDC25 (0.85), LRBA (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SMG8 nonsense mediated mRNA decay factor. Involved in nuclear-transcribed mRNA catabolic process, nonsense-mediated decay and regulation of protein kinase activity. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Alzahrani-Kuwahara syndrome (0.730); microcephaly (0.483); Short stature (0.483); Intellectual disability (0.483); Abnormal facial shape (0.483)
- **Europe PMC papers**: 261
- **Why important**: SMG8 is among the more connected genes and links BOD1L1, ANAPC1, CCDC25 and LRBA. Its established role in nonsense-mediated decay and regulation of protein kinase activity provides a direct route from the module to RNA quality control and post-transcriptional regulation. The supplied evidence also links it to a neurodevelopmental syndrome, microcephaly, short stature and intellectual disability.
- **Conclusion**: Established evidence supports SMG8 as a candidate RNA-surveillance component of the module. A role as a bridge between RNA quality control and cell-cycle or stress regulation is a plausible interpretation, but it remains a hypothesis because no enriched term or physical interaction confirms that bridge here.

#### RNF31

- **Related proteins** (co-abundance neighbors): ANAPC1 (0.86), ARHGEF1 (0.82), SPECC1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ring finger protein 31. The protein encoded by this gene contains a RING finger, a motif present in a variety of functionally distinct proteins and known to be involved in protein-DNA and protein-protein interactions. The encoded protein is the E3 ubiquitin-protein ligase component of the linear ubiquitin chain assembly complex. Two transcript variants encoding different isoforms have been found for this gene. [provided …
- **Diseases (Open Targets)**: autoinflammatory syndrome with pyogenic bacterial infection and amylopectinosis (0.508); immunodeficiency 115 with autoinflammation (0.506); neurodegenerative disease (0.480); polyglucosan body myopathy 1 with or without immunodeficiency (0.443); Short stature (0.323)
- **Europe PMC papers**: 788
- **Why important**: RNF31 connects ANAPC1, ARHGEF1 and SPECC1 and has a central position within a subnetwork that combines ubiquitin regulation, Rho-linked signaling and cytoskeletal biology. It is an E3 ubiquitin-ligase component of the linear ubiquitin-chain assembly complex and is annotated in receptor signaling, antibacterial defense and canonical NF-kappaB activation. Its disease associations include immunodeficiency and autoinflammatory syndromes, and it has substantial literature.
- **Conclusion**: Established evidence supports RNF31 as the strongest candidate for an immune-signaling and ubiquitin-regulatory interface in this module. Its connection to the cell-cycle and cytoskeletal genes may indicate indirect coordination, but a unified inflammatory mechanism is not demonstrated by the supplied network.

#### LRBA

- **Related proteins** (co-abundance neighbors): NCOR1 (0.86), SMG8 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LPS responsive beige-like anchor protein. The protein encoded by this gene is a member of the WDL-BEACH-WD (WBW) gene family. Its expression is induced in B cells and macrophages by bacterial lipopolysaccharides (LPS). The encoded protein associates with protein kinase A and may be involved in leading intracellular vesicles to activated receptor complexes, which aids in the secretion and/or membrane deposition of immune effector molecules…
- **Diseases (Open Targets)**: combined immunodeficiency due to LRBA deficiency (0.815); colobomatous microphthalmia-rhizomelic dysplasia syndrome (0.525); cholelithiasis (0.509); immunodeficiency disease (0.431); gallstones (0.419)
- **Europe PMC papers**: 1561
- **Why important**: LRBA links SMG8 with NCOR1 and is relevant to vesicle positioning, mitophagy and phagophore assembly-site localization. Its supplied annotation describes induction in B cells and macrophages by bacterial lipopolysaccharide and involvement in intracellular vesicle routing to activated receptor complexes. LRBA deficiency is associated with common variable immunodeficiency and related immune disease, and LRBA has the largest literature volume among the selected immune-relevant candidates.
- **Conclusion**: Established evidence supports LRBA as a vesicle-trafficking and immune-homeostasis component. Its presence could reflect an immune or stress-related cellular state shared across samples, but it does not establish that the module is blood-derived, especially because most members have low immune-cell specificity.

#### DIAPH1

- **Related proteins** (co-abundance neighbors): TP53BP2 (0.82), PHACTR4 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: diaphanous related formin 1. This gene is a homolog of the Drosophila diaphanous gene, and has been linked to autosomal dominant, fully penetrant, nonsyndromic sensorineural progressive low-frequency hearing loss. Actin polymerization involves proteins known to interact with diaphanous protein in Drosophila and mouse. It has therefore been speculated that this gene may have a role in the regulation of actin polymerization in …
- **Diseases (Open Targets)**: progressive microcephaly-seizures-cortical blindness-developmental delay syndrome (0.771); autosomal dominant nonsyndromic hearing loss 1 (0.755); DIAPH1-related sensorineural hearing loss-thrombocytopenia syndrome (0.462); deafness (0.458); Global developmental delay (0.435)
- **Europe PMC papers**: 2166
- **Why important**: DIAPH1 connects TP53BP2 and PHACTR4, providing a compact bridge between actin regulation, apoptosis-related signaling and membrane or cytoskeletal organization. It is annotated in actin filament polymerization and cytoskeleton organization, is enhanced in neutrophils and platelets, and has substantial disease evidence involving hearing loss, thrombocytopenia and developmental disorders.
- **Conclusion**: Established evidence supports DIAPH1 as a cytoskeletal and cell-shape component that could connect the module to migration or adhesion. A role in coupling cytoskeletal remodeling to the module's RNA, ubiquitin and stress-regulatory genes is a hypothesis requiring perturbation or cellular localization experiments.

## Module 8

**Tissue pair**: lung and stem_cells  
**Genes (8)**: AGRN, AKAP17A, CAV1, COL1A2, COL4A1, COL6A1, EHD2, LAMB2

### Function

The module is best interpreted as an extracellular-matrix and basement-membrane organization module. The primary evidence is exceptionally coherent: ECM-receptor interaction (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 3.14e-05), basement-membrane organization (GO:BP basement membrane organization; q_global = 5.69e-05), extracellular-matrix structural constituent activity (GO:MF extracellular matrix structural constituent; q_global = 6.84e-05), extracellular matrix and external encapsulating structure (GO:CC external encapsulating structure; q_global = 0.000193) (GO:CC extracellular matrix; q_global = 0.000193), and extracellular-matrix organization (GO:BP extracellular matrix organization; q_global = 0.000546) (GO:BP extracellular structure organization; q_global = 0.000546) (GO:BP external encapsulating structure organization; q_global = 0.000546) all pass global correction. Focal adhesion, integrin signaling, and PI3K-Akt signaling (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.000816) (KEGG Integrin signaling - Homo sapiens (human); q_global = 0.00927) (KEGG PI3K-Akt signaling pathway - Homo sapiens (human); q_global = 0.0167) suggest that the matrix is not merely structural but may regulate cell adhesion and intracellular signaling. The collagen-trimer, tensile-strength, growth-factor-binding, and platelet-derived growth-factor-binding terms (5 globally significant GO/KEGG terms, q_global 0.00154–0.038; see the table) support a matrix scaffold capable of influencing tissue mechanics and receptor signaling. The neuromuscular-junction term (GO:BP neuromuscular junction development; q_global = 0.00825) is compatible with shared basement-membrane and synaptic-organizing functions but should not be taken to mean that the module is specifically a neuromuscular-junction module. The protein-digestion and absorption and infection-related pathway terms (KEGG Protein digestion and absorption - Homo sapiens (human); q_global = 0.0215) (KEGG Human papillomavirus infection - Homo sapiens (human); q_global = 0.0436) are likely secondary pathway annotations arising from shared collagen and matrix genes rather than the central biological interpretation. STRING supplementary results independently reinforce ECM, collagen-containing matrix, integrin interactions, focal adhesion, and PI3K-Akt themes (15 supplementary STRING terms; within-query FDR 2.06e-06–0.0011).

**Cell composition.** The module is dominated by secreted extracellular-matrix or basement-membrane proteins, including LAMB2, COL1A2, COL4A1, COL6A1, and AGRN. This composition is consistent with a stromal, vascular, perivascular, fibroblast-like, or epithelial-supporting matrix program rather than a blood-cell program. HPA single-cell evidence particularly points toward hepatic stellate cells, pericytes, peritubular myoid cells, vascular smooth muscle cells, and stromal populations. Most genes are not detected in immune cells, although CAV1 has blood-cell group enrichment and AKAP17A has immune-cell enhancement; these observations do not by themselves establish blood contamination. Protein detection in lung is broad, while there is no matching HPA tissue category for stem_cells. The shared module could therefore reflect a conserved matrix-producing or matrix-interacting cell population present in both sample groups, with a contribution from vascular or stromal cell composition, rather than a function unique to stem cells. The secretion and extracellular-matrix localization of much of the module also makes sample composition and extracellular carryover important considerations.

**GO/KEGG enrichment**: 24 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG ECM-receptor interaction - Homo sapiens (human) | 3.14e-05 | AGRN, COL1A2, COL4A1, COL6A1, LAMB2 |
| GO:BP basement membrane organization | 5.69e-05 | CAV1, COL4A1, COL6A1, LAMB2 |
| GO:MF extracellular matrix structural constituent | 6.84e-05 | AGRN, COL1A2, COL4A1, COL6A1, LAMB2 |
| GO:CC external encapsulating structure | 0.000193 | AGRN, COL1A2, COL4A1, COL6A1, LAMB2 |
| GO:CC extracellular matrix | 0.000193 | AGRN, COL1A2, COL4A1, COL6A1, LAMB2 |
| GO:BP extracellular matrix organization | 0.000546 | CAV1, COL1A2, COL4A1, COL6A1, LAMB2 |
| GO:BP extracellular structure organization | 0.000546 | CAV1, COL1A2, COL4A1, COL6A1, LAMB2 |
| GO:BP external encapsulating structure organization | 0.000546 | CAV1, COL1A2, COL4A1, COL6A1, LAMB2 |
| KEGG Focal adhesion - Homo sapiens (human) | 0.000816 | CAV1, COL1A2, COL4A1, COL6A1, LAMB2 |
| GO:CC basement membrane | 0.00145 | AGRN, COL4A1, COL6A1, LAMB2 |
| GO:MF platelet-derived growth factor binding | 0.00154 | COL1A2, COL4A1, COL6A1 |
| GO:CC complex of collagen trimers | 0.00671 | COL1A2, COL4A1, COL6A1 |
| GO:BP neuromuscular junction development | 0.00825 | AGRN, COL4A1, LAMB2 |
| GO:MF extracellular matrix structural constituent conferring tensile strength | 0.00825 | COL1A2, COL4A1, COL6A1 |
| KEGG Integrin signaling - Homo sapiens (human) | 0.00927 | COL1A2, COL4A1, COL6A1, LAMB2 |

### STRING and hu.MAP

STRING provides direct high-confidence support for the collagen relationships COL1A2-COL4A1, COL1A2-COL6A1, and COL4A1-COL6A1, forming a collagen-centered interaction core. STRING also supports CAV1-EHD2, linking caveolar membrane organization to the matrix-associated program. The STRING enrichment results (15 supplementary STRING terms; within-query FDR 2.06e-06–0.0011) reproduce the ECM, collagen, focal-adhesion, integrin, growth-factor-binding, and PI3K-Akt interpretations, but they remain supplementary rather than global module-wide significance evidence. The co-abundance network additionally connects LAMB2 with EHD2, CAV1, AGRN, and COL6A1, and connects CAV1 with AKAP17A; these relationships are not all represented by high-confidence STRING edges. No hu.MAP complex contains multiple module members. Thus, the module is supported more strongly as a coordinated extracellular and membrane-associated biological program than as a known intracellular multiprotein complex. Known collagen interactions validate part of the network, while the remaining co-abundance links may reflect shared cell type, matrix deposition, membrane organization, or correlated regulation rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 4 of 28 gene pairs: CAV1–EHD2 (0.786); COL1A2–COL4A1 (0.757); COL1A2–COL6A1 (0.875); COL4A1–COL6A1 (0.832)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG ECM-receptor interaction (FDR = 2.06e-06, 5 genes); RCTM ECM proteoglycans (FDR = 9.18e-06, 5 genes); Keyword Extracellular matrix (FDR = 1.07e-05, 5 genes); PMID (2023) Data-independent acquisition and quantification of extracellular matrix from human lung in chronic inflammation-associated carcinomas. (FDR = 2.98e-05, 6 genes); KEGG Focal adhesion (FDR = 4.03e-05, 5 genes); WikiPathways miRNA targets in ECM and membrane receptors (FDR = 5.52e-05, 4 genes); COMPARTMENTS External encapsulating structure (FDR = 0.0001, 5 genes); COMPARTMENTS Collagen-containing extracellular matrix (FDR = 0.0001, 5 genes); RCTM Integrin cell surface interactions (FDR = 0.00042, 4 genes); RCTM Non-integrin membrane-ECM interactions (FDR = 0.00042, 4 genes); Component Collagen-containing extracellular matrix (FDR = 0.00059, 5 genes); Function Extracellular matrix structural constituent (FDR = 0.001, 4 genes); KEGG PI3K-Akt signaling pathway (FDR = 0.001, 4 genes); Function Platelet-derived growth factor binding (FDR = 0.0011, 3 genes); RCTM NCAM1 interactions (FDR = 0.0011, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The broad biological function is not a new discovery: basement membranes, collagens, laminins, agrin, caveolin, focal adhesions, and integrin signaling are established biology, and several collagen relationships are already represented in STRING. The absence of a hu.MAP complex does not establish novelty, because hu.MAP is primarily evidence for defined intracellular complexes and is not expected to capture all extracellular-matrix assemblies. The potentially novel aspect is the conservation of this particular co-abundance pattern across lung and stem_cells, especially the combination of the LAMB2-centered links with the collagen core, CAV1, EHD2, AGRN, and AKAP17A. That claim remains provisional because co-abundance can arise from shared cell composition or coordinated extracellular deposition. Replication in independent cohorts, cell-type-resolved analysis, protein-level validation, and comparison with existing tissue-specific co-expression modules would be required before calling the shared module a new biological mechanism.

**Hypothesis.** Hypothesis: the module represents a conserved stromal or vascular-support program in which collagen-rich matrix is assembled with type IV collagen, type VI collagen, type I collagen, laminin beta two, and agrin, while caveolin one and EHD2 organize membrane signaling and endocytic or caveolar responses. This matrix may engage integrins and growth-factor-binding interactions to regulate adhesion, cytoskeletal organization, PI3K-Akt signaling, tissue mechanics, and differentiation in lung and stem-cell-associated contexts. The apparent conservation may reflect a common pericyte, smooth-muscle, fibroblast, or related matrix-interacting cell state. This is a mechanistic hypothesis, not proof of direct binding among all module members or proof that the program originates from the same cell type in both tissues.

### Important genes

#### LAMB2

- **Related proteins** (co-abundance neighbors): EHD2 (0.86), CAV1 (0.84), AGRN (0.82), COL6A1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit beta 2. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: LAMB2-related infantile-onset nephrotic syndrome (0.808); Pierson syndrome (0.797); nephrotic syndrome (0.496); eye disorder (0.434); synaptic congenital myasthenic syndrome (0.381)
- **Europe PMC papers**: 2504
- **Why important**: LAMB2 has the strongest network position in the module and links the ECM-associated genes with CAV1, EHD2, and AGRN. It is a laminin basement-membrane component and appears across many primary ECM, basement-membrane, focal-adhesion, integrin, and PI3K-Akt terms (15 globally significant GO/KEGG terms, q_global 3.14e-05–0.049; see the table). HPA places it in extracellular matrix secretion and shows lung protein detection, while disease associations include Pierson syndrome and LAMB2-related nephrotic disease. Its substantial literature supports an established role in basement-membrane architecture and adhesion.
- **Conclusion**: Established evidence supports LAMB2 as a central basement-membrane scaffold and a plausible organizer of the module's ECM-receptor interpretation. It is reasonable to hypothesize that its co-abundance with CAV1, EHD2, and AGRN marks coordinated matrix-membrane signaling, but the network does not prove that LAMB2 physically binds every linked gene in this module.

#### COL6A1

- **Related proteins** (co-abundance neighbors): COL1A2 (0.88), COL4A1 (0.82), LAMB2 (0.81); STRING partners: COL1A2 (0.875), COL4A1 (0.832)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is a highly connected collagen gene and is directly supported by STRING links to COL1A2 and COL4A1. It contributes to nearly all of the primary ECM, collagen, focal-adhesion, integrin, growth-factor-binding, and related terms (24 globally significant GO/KEGG terms, q_global 3.14e-05–0.049; see the table). HPA associates it with stromal, fibroblast-like, and perivascular cell types and with secretion to extracellular matrix. Its disease associations include Bethlem myopathy, Ullrich congenital muscular dystrophy, and collagen-six-related myopathy, with extensive literature on collagen VI biology.
- **Conclusion**: Established evidence identifies COL6A1 as a structural and disease-relevant core of the collagen network. Its position supports a role in matrix architecture and tissue mechanics. A specific causal role in the lung-stem-cell shared state remains a hypothesis requiring perturbation or cell-type-resolved validation.

#### COL4A1

- **Related proteins** (co-abundance neighbors): COL6A1 (0.82); STRING partners: COL1A2 (0.757), COL6A1 (0.832)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type IV alpha 1 chain. This gene encodes a type IV collagen alpha protein. Type IV collagen proteins are integral components of basement membranes. This gene shares a bidirectional promoter with a paralogous gene on the opposite strand. The protein consists of an amino-terminal 7S domain, a triple-helix forming collagenous domain, and a carboxy-terminal non-collagenous domain. It functions as part of a heterotrimer and …
- **Diseases (Open Targets)**: brain small vessel disease 1 with or without ocular anomalies (0.841); autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome (0.804); microangiopathy and leukoencephalopathy, pontine, autosomal dominant (0.729); schizencephaly (0.695); retinal arterial tortuosity (0.693)
- **Europe PMC papers**: 9069
- **Why important**: COL4A1 is a central basement-membrane collagen and is connected by STRING to COL1A2 and COL6A1. It appears in essentially the complete primary ECM interpretation, including basement-membrane organization, collagen trimers, growth-factor binding, focal adhesion, integrin signaling, and PI3K-Akt signaling (24 globally significant GO/KEGG terms, q_global 3.14e-05–0.049; see the table). HPA shows lung detection and enrichment in vascular, stromal, adipocyte, and trophoblast-associated cell types. Its disease associations include small-vessel brain disease, retinal arterial tortuosity, and related vascular disorders, supporting a major role in basement-membrane and vascular integrity.
- **Conclusion**: Established evidence supports COL4A1 as a key basement-membrane and vascular-matrix component that can explain the module's structural and signaling annotations. The shared module may indicate coordinated vascular or perivascular matrix biology, but that cell-of-origin interpretation is still a hypothesis.

#### COL1A2

- **Related proteins** (co-abundance neighbors): COL6A1 (0.88); STRING partners: COL4A1 (0.757), COL6A1 (0.875)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type I alpha 2 chain. This gene encodes the pro-alpha2 chain of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIB, recessive Ehlers-Danlos syndrome Classi…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 2 (0.845); osteogenesis imperfecta type 3 (0.830); osteogenesis imperfecta type 4 (0.820); Ehlers-Danlos syndrome, cardiac valvular type (0.777); osteogenesis imperfecta type 1 (0.770)
- **Europe PMC papers**: 67901
- **Why important**: COL1A2 is the type I collagen alpha-two chain and is directly connected to the collagen core through COL6A1 and COL4A1. It contributes to ECM-receptor interaction, extracellular-matrix structure, focal adhesion, integrin and PI3K-Akt signaling, collagen-trimer and tensile-strength annotations, and growth-factor-binding terms (21 globally significant GO/KEGG terms, q_global 3.14e-05–0.049; see the table). HPA shows tissue enhancement in connective and smooth-muscle-associated tissues and stromal cell enrichment. Its extensive literature and strong disease associations include osteogenesis imperfecta and Ehlers-Danlos syndromes.
- **Conclusion**: Established evidence makes COL1A2 a major fibrillar-matrix component and a strong indicator of connective-tissue or stromal biology. Its presence supports matrix deposition as a core interpretation rather than a generic housekeeping explanation. Whether it drives the shared lung-stem-cell co-abundance pattern or simply reports matrix-producing cell abundance remains unresolved.

#### CAV1

- **Related proteins** (co-abundance neighbors): LAMB2 (0.84), AKAP17A (0.82); STRING partners: EHD2 (0.786)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caveolin 1. The scaffolding protein encoded by this gene is the main component of the caveolae plasma membranes found in most cell types. The protein links integrin subunits to the tyrosine kinase FYN, an initiating step in coupling integrins to the Ras-ERK pathway and promoting cell cycle progression. The gene is a tumor suppressor gene candidate and a negative regulator of the Ras-p42/44 mitogen-activated k…
- **Diseases (Open Targets)**: congenital generalized lipodystrophy type 3 (0.661); pulmonary hypertension, primary, 3 (0.626); partial lipodystrophy, congenital cataracts, and neurodegeneration syndrome (0.615); atrial fibrillation (0.581); glaucoma (0.528)
- **Europe PMC papers**: 19537
- **Why important**: CAV1 provides a membrane-signaling counterpart to the secreted matrix genes. It connects in the module to LAMB2 and AKAP17A and has a STRING relationship with EHD2. It contributes to basement-membrane organization, extracellular-matrix organization, focal adhesion, and extracellular-structure terms (5 globally significant GO/KEGG terms, q_global 5.69e-05–0.000816; see the table). HPA detects it in lung and associates it with alveolar type one cells, hepatic stellate cells, and other specialized cell populations; it also shows blood-cell enrichment that should be considered when assessing sample composition. Its disease associations include pulmonary hypertension and lipodystrophy, and it has a very extensive literature.
- **Conclusion**: Established evidence supports CAV1 as a caveolar scaffold that can connect matrix adhesion to membrane signaling, hypoxia responses, endothelial behavior, and cytoskeletal regulation. Its inclusion strengthens a matrix-receptor signaling interpretation, but its blood-cell enrichment means that cell-composition effects should be excluded before assigning a lung-specific mechanism.

## Module 9

**Tissue pair**: lung and stem_cells  
**Genes (22)**: ALDH1A1, ASCC2, ATP2B4, BCAT2, BIN1, CASP6, SPECC1L, PROCR, GNB4, GBP1, HAUS7, IDE, MAN1B1, MOGS, APIP, NME3, PON2, SKIC3, SARS2, UBA6, ATP6V0A1, TCIRG1

### Function

The module does not support a single statistically established GO or KEGG function: no globally significant GO/KEGG term passed global correction, and STRING reported no supplementary enrichment. Its genes instead suggest a heterogeneous combination of intracellular organelle acidification, membrane ion handling, glycoprotein processing, immune signaling, apoptosis, protein quality control, and metabolism. The strongest coherent biological signal is the presence of TCIRG1 and ATP6V0A1, both components of vacuolar H+-ATPase-related machinery, supported by their high-confidence STRING relationship and their recurrence in multiple hu.MAP complexes (hu.MAP huMAP3_07558.1) through (hu.MAP huMAP3_10511.1) and (hu.MAP huMAP3_12042.1). MOGS and MAN1B1 provide a separate endoplasmic-reticulum glycan-processing connection, supported by STRING. GBP1 and CASP6 occur together in hu.MAP complexes (hu.MAP huMAP3_15160.1) and (hu.MAP huMAP3_12098.1), but this does not establish a direct functional relationship. Overall, the module is better interpreted as a cross-tissue co-abundance pattern linking vesicular acidification and trafficking-related biology with cell-state, stress, immune, and metabolic components rather than as a validated canonical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins. HPA indicates that most genes have low immune-cell specificity, while only a minority show immune-cell enhancement, enrichment, or group enrichment. A small subset has secretome annotations, including PON2 and IDE, but the majority are intracellular, membrane-associated, cytosolic, nuclear, mitochondrial, endoplasmic-reticulum, or vesicular proteins. The module therefore does not strongly resemble a blood-cell or circulating-protein contamination signature. HPA instead shows mixed tissue and cell-type associations, including neural and glial populations, epithelial and stromal populations, smooth muscle, liver-associated cells, and selected immune cells. This heterogeneity is compatible with shared cellular programs or sample-composition effects, but it does not identify a single shared cell type. Protein detection in lung is broad among the genes with available data, whereas there is no matching HPA tissue for stem_cells, so the stem-cell side cannot be assessed by direct HPA protein detection.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING identifies a high-confidence relationship between ATP6V0A1 and TCIRG1 and another strong relationship between MOGS and MAN1B1. These links provide established molecular support for a vacuolar acidification component and an ER glycan-processing component, respectively. The absence of STRING links for the remaining module pairs means that most co-abundance edges are not independently supported as known physical or functional interactions; they may represent shared regulation, cell composition, indirect biology, or context-specific association. hu.MAP provides partial complex support. TCIRG1 and ATP6V0A1 recur together across several V-ATPase-related complexes (hu.MAP huMAP3_07558.1) through (hu.MAP huMAP3_10511.1) and (hu.MAP huMAP3_12042.1), while ATP2B4 and PROCR recur together in (hu.MAP huMAP3_09336.1) and (hu.MAP huMAP3_11349.1). GBP1 and CASP6 recur together in (hu.MAP huMAP3_15160.1) and (hu.MAP huMAP3_12098.1). Because each hu.MAP result contains only a small subset of the corresponding complex, these observations support local molecular anchors rather than a complete physical complex for the whole module.

**STRING interactions (score >= 0.7)**: 2 of 231 gene pairs: ATP6V0A1–TCIRG1 (0.96); MAN1B1–MOGS (0.852)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15160.1 (GBP1, CASP6; 2/5); huMAP3_12098.1 (GBP1, CASP6; 2/6); huMAP3_07558.1 (TCIRG1, ATP6V0A1; 2/8); huMAP3_05805.1 (TCIRG1, ATP6V0A1; 2/21); huMAP3_09477.1 (TCIRG1, ATP6V0A1; 2/26); huMAP3_10516.1 (TCIRG1, ATP6V0A1; 2/31); huMAP3_10511.1 (TCIRG1, ATP6V0A1; 2/35); huMAP3_09336.1 (ATP2B4, PROCR; 2/50); huMAP3_12042.1 (TCIRG1, ATP6V0A1; 2/56); huMAP3_11349.1 (ATP2B4, PROCR; 2/78)

### Novelty

The cross-tissue co-abundance module may be a new systems-level observation, but the supplied evidence does not establish that it is a new biological mechanism. Its strongest relationships are already known through STRING and hu.MAP, and the component genes have substantial prior functional and disease literature. Conversely, the sparse network, lack of globally significant GO or KEGG terms, lack of STRING enrichment, and heterogeneous annotations argue against claiming discovery of a previously unknown pathway. A defensible conclusion is that the novelty lies, if anywhere, in the specific co-abundance combination across lung and stem_cells and its reproducibility, not in the individual gene functions or the established protein interactions. Demonstrating novelty would require replication in independent cohorts, preservation of the module across analytical choices, and comparison with published cross-tissue co-expression or proteomic modules.

**Hypothesis.** Hypothesis: the module reflects coordinated variation in vesicular and lysosomal acidification together with membrane calcium handling and ER glycoprotein processing, embedded within a broader cell-state program involving innate immune tone, apoptosis, proteostasis, and intermediary metabolism. In lung, this could arise from coordinated activity or abundance of epithelial, stromal, vascular, and resident immune-related cell populations; in stem_cells, it could reflect a shared requirement for organelle trafficking, protein maturation, and cell-state remodeling. The TCIRG1–ATP6V0A1 and MOGS–MAN1B1 relationships are mechanistic anchors, while the remaining edges should currently be treated as candidate regulatory or compositional links. This hypothesis should be tested by measuring V-ATPase activity, organelle acidity, ER glycan processing, calcium flux, and cell-type-resolved expression or protein abundance rather than inferred from co-abundance alone.

### Important genes

#### TCIRG1

- **Related proteins** (co-abundance neighbors): NME3 (0.91), ATP2B4 (0.91), SKIC3 (0.90), ATP6V0A1 (0.88), UBA6 (0.83), MOGS (0.82), BCAT2 (0.81); STRING partners: ATP6V0A1 (0.96)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_07558.1, huMAP3_05805.1, huMAP3_09477.1, huMAP3_10516.1, huMAP3_10511.1, huMAP3_12042.1
- **Function (MyGene.info)**: T cell immune regulator 1, ATPase H+ transporting V0 subunit a3. This gene encodes a subunit of a large protein complex known as a vacuolar H+-ATPase (V-ATPase). The protein complex acts as a pump to move protons across the membrane. This movement of protons helps regulate the pH of cells and their surrounding environment. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, and recepto…
- **Diseases (Open Targets)**: autosomal recessive osteopetrosis (0.770); autosomal recessive osteopetrosis 1 (0.751); osteopetrosis (0.554); chronic kidney disease (0.451); dysosteosclerosis (0.442)
- **Europe PMC papers**: 1274
- **Why important**: TCIRG1 is the strongest network anchor in the module and connects the V-ATPase-related signal to several otherwise disparate genes. It has a high-confidence STRING relationship with ATP6V0A1 and appears with ATP6V0A1 in multiple hu.MAP complexes (hu.MAP huMAP3_07558.1) through (hu.MAP huMAP3_10511.1) and (hu.MAP huMAP3_12042.1). Its established function in vacuolar and lysosomal acidification, protein sorting, receptor-mediated endocytosis, and autophagy gives the module a plausible organelle-acidification axis. Its osteopetrosis associations and substantial literature volume also provide strong disease and experimental context.
- **Conclusion**: Established evidence supports TCIRG1 as a V-ATPase-related hub and a key mechanistic anchor of the module. It is plausible, but not established, that variation in TCIRG1 abundance contributes to coordinated organelle-acidification biology across the two tissues.

#### ATP6V0A1

- **Related proteins** (co-abundance neighbors): TCIRG1 (0.88), PROCR (0.87), APIP (0.81); STRING partners: TCIRG1 (0.96)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_07558.1, huMAP3_05805.1, huMAP3_09477.1, huMAP3_10516.1, huMAP3_10511.1, huMAP3_12042.1
- **Function (MyGene.info)**: ATPase H+ transporting V0 subunit a1. This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 d…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy 104 (0.712); neurodevelopmental disorder with epilepsy and brain atrophy (0.696); Seizure (0.420); hereditary disease (0.414); developmental disability (0.370)
- **Europe PMC papers**: 854
- **Why important**: ATP6V0A1 is directly connected to TCIRG1 and also links to PROCR and APIP in the co-abundance network. It has a high-confidence STRING relationship with TCIRG1 and recurs with TCIRG1 across several hu.MAP V-ATPase-related complexes (hu.MAP huMAP3_07558.1) through (hu.MAP huMAP3_10511.1) and (hu.MAP huMAP3_12042.1). Its established roles in vacuolar, lysosomal, and endosomal acidification, autophagy, and synaptic vesicle lumen acidification make it central to interpreting the vesicular component. Its neurological disease associations add biological relevance, although they do not establish a role in this module.
- **Conclusion**: Established evidence identifies ATP6V0A1 as a V-ATPase subunit with strong support from network and complex data. The module-level claim that it coordinates acidification with the other module processes remains a hypothesis.

#### ATP2B4

- **Related proteins** (co-abundance neighbors): TCIRG1 (0.91), CASP6 (0.83), GNB4 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Primary cilium; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_09336.1, huMAP3_11349.1
- **Function (MyGene.info)**: ATPase plasma membrane Ca2+ transporting 4. The protein encoded by this gene belongs to the family of P-type primary ion transport ATPases characterized by the formation of an aspartyl phosphate intermediate during the reaction cycle. These enzymes remove bivalent calcium ions from eukaryotic cells against very large concentration gradients and play a critical role in intracellular calcium homeostasis. The mammalian plasma membrane calcium …
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.393); malaria (0.367); chronic venous hypertension (0.222); male infertility (0.208); prostate cancer (0.114)
- **Europe PMC papers**: 1568
- **Why important**: ATP2B4 connects TCIRG1, CASP6, and GNB4 and is supported by hu.MAP complexes containing ATP2B4 and PROCR (hu.MAP huMAP3_09336.1) and (hu.MAP huMAP3_11349.1). Its established role is plasma-membrane calcium export and intracellular calcium homeostasis. The HPA association with alveolar, smooth-muscle, and epithelial cell types makes it particularly relevant to lung biology. Its disease and literature record is substantial, providing context for calcium-dependent signaling and cellular stress.
- **Conclusion**: Established evidence supports ATP2B4 as a calcium-homeostasis component and a useful bridge between the acidification-associated anchor and signaling or apoptotic genes. It is not established that calcium handling is a defining function of the entire module.

#### MOGS

- **Related proteins** (co-abundance neighbors): TCIRG1 (0.82), MAN1B1 (0.80); STRING partners: MAN1B1 (0.852)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosyl-oligosaccharide glucosidase. This gene encodes the first enzyme in the N-linked oligosaccharide processing pathway. The enzyme cleaves the distal alpha-1,2-linked glucose residue from the Glc(3)-Man(9)-GlcNAc(2) oligosaccharide precursor. This protein is located in the lumen of the endoplasmic reticulum. Defects in this gene are a cause of type IIb congenital disorder of glycosylation (CDGIIb). Two transcript variants encodin…
- **Diseases (Open Targets)**: MOGS-congenital disorder of glycosylation (0.818); congenital disorder of glycosylation (0.374); congenital disorder of glycosylation type II (0.370); severe acute respiratory syndrome (0.370); SRD5A3-congenital disorder of glycosylation (0.370)
- **Europe PMC papers**: 987
- **Why important**: MOGS forms the module's clearest ER glycan-processing pair with MAN1B1, supported by STRING. Its established function is removal of glucose from N-linked oligosaccharide precursors during ER glycoprotein processing, and defects cause congenital glycosylation disease. This provides a mechanistic connection to protein maturation and quality control that is distinct from the V-ATPase signal. Its HPA annotation indicates low tissue and immune specificity, which is consistent with a broadly distributed cellular process rather than a blood-specific marker.
- **Conclusion**: Established evidence supports MOGS as an ER glycoprotein-processing component and as part of a known relationship with MAN1B1. The proposed connection between this process and the module's acidification or cell-state signals is a hypothesis.

#### GBP1

- **Related proteins** (co-abundance neighbors): GNB4 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_15160.1, huMAP3_12098.1
- **Function (MyGene.info)**: guanylate binding protein 1. Guanylate binding protein expression is induced by interferon. Guanylate binding proteins are characterized by their ability to specifically bind guanine nucleotides (GMP, GDP, and GTP) and are distinguished from the GTP-binding proteins by the presence of 2 binding motifs rather than 3. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: bacterial infectious disease (0.528); Orthomyxoviridae infectious disease (0.374); neurodegenerative disease (0.302); muscular disease (0.195); neoplasm (0.116)
- **Europe PMC papers**: 3935
- **Why important**: GBP1 contributes an interferon-inducible innate immune dimension and is associated with antibacterial, antiprotozoal, calcium-signaling, and T-cell regulatory functions in the supplied annotations. It appears with CASP6 in hu.MAP complexes (hu.MAP huMAP3_15160.1) and (hu.MAP huMAP3_12098.1), while its network connection to GNB4 provides a link to signaling. Its substantial literature volume and infectious-disease associations make it an informative indicator of immune-state biology, although HPA does not show strong general blood-cell specificity for the module.
- **Conclusion**: Established evidence supports GBP1 as an interferon-responsive immune effector. Its presence does not prove that the module is an immune module; it may instead report a context-dependent or cell-composition component of the shared co-abundance pattern.

#### PROCR

- **Related proteins** (co-abundance neighbors): ATP6V0A1 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09336.1, huMAP3_11349.1
- **Function (MyGene.info)**: protein C receptor. The protein encoded by this gene is a receptor for activated protein C, a serine protease activated by and involved in the blood coagulation pathway. The encoded protein is an N-glycosylated type I membrane protein that enhances the activation of protein C. Mutations in this gene have been associated with venous thromboembolism and myocardial infarction, as well as with late fetal loss during preg…
- **Diseases (Open Targets)**: venous thromboembolism (0.548); coronary artery disorder (0.546); deep vein thrombosis (0.510); pulmonary embolism (0.502); ischemic stroke (0.482)
- **Europe PMC papers**: 3131
- **Why important**: PROCR links directly to ATP6V0A1 in the module and occurs with ATP2B4 in hu.MAP complexes (hu.MAP huMAP3_09336.1) and (hu.MAP huMAP3_11349.1). Its established function is as the endothelial protein C receptor involved in regulation of coagulation. HPA associates it with stromal, progenitor, trophoblast, and selected immune cell types, while the supplied disease associations include thromboembolic and vascular disorders. Its lack of lung protein detection is important context and cautions against assuming that the module represents uniform abundance in lung tissue.
- **Conclusion**: Established evidence supports PROCR as a vascular, coagulation-related receptor and as a local network bridge. Its contribution to the shared lung–stem-cell module is uncertain and may reflect a specific cell population or sample-composition effect rather than a universal tissue program.

## Module 10

**Tissue pair**: lung and stem_cells  
**Genes (32)**: ANO6, AP3B1, ARHGEF12, CDKAL1, CDK5RAP3, DAGLB, EIF2AK4, ERLIN2, FN3K, HS1BP3, HDHD2, HIKESHI, ITPR3, MPHOSPH6, NIPBL, DBT, OSBPL1A, PLXNB2, PMM2, PPIL2, PTPN23, RAB32, RBBP9, STT3A, SWAP70, TAF5, TBCE, TMED8, UFD1, VPS50, VPS53, WASF2

### Function

No GO/KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The gene-level evidence instead points to a mixed intracellular trafficking, membrane signaling, calcium-handling, cytoskeletal, and cellular stress program. ITPR3 and ERLIN2 connect calcium release with endoplasmic-reticulum regulation; PLXNB2, ARHGEF12, WASF2, and SWAP70 support receptor-linked Rho or actin signaling; VPS50, VPS53, TMED8, AP3B1, and PTPN23 support vesicle transport and endosomal recycling; and EIF2AK4 supports translational suppression during amino-acid, glucose, or viral stress. The sparse, chain-like network suggests coordinated co-abundance of several cellular systems rather than a single established biochemical pathway. These functional interpretations are hypothesis-generating because the enrichment analysis did not identify a globally significant GO/KEGG theme.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only one gene is annotated as secreted, and most proteins are intracellular or membrane-associated. HPA shows broadly low tissue specificity for most genes, while many genes are cell-type enhanced in diverse populations, including alveolar cells, glia, spermatids, epithelial cells, and selected immune cells. Most genes have low immune-cell specificity, although several show enrichment or enhancement in basophils, monocytes, dendritic cells, plasmacytoid dendritic cells, or B cells. Protein detection in lung is widespread among the module genes, whereas there is no matching HPA tissue for stem cells. Thus, the shared lung–stem-cell module is unlikely to be explained simply by a plasma-protein signal or a uniform blood-cell signature, but sample cell composition and broadly expressed cellular programs remain plausible contributors.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides limited direct support. The known high-confidence relationship between ARHGEF12 and PLXNB2 links Rho signaling with a plexin receptor, and the relationship between VPS50 and VPS53 supports a vesicle-trafficking connection. No STRING functional-enrichment result was available, so STRING does not establish a pathway-level interpretation. hu.MAP independently places VPS50 and VPS53 together in the partial complexes C1 and C2, consistent with EARP or GARP-related trafficking machinery. STT3A and CDKAL1 occur together as a small subset of the much larger complex C3, but this does not imply that the entire complex is represented by the module. The known interactions and complex memberships validate selected local relationships, while the many remaining module edges lack corresponding STRING or hu.MAP support.

**STRING interactions (score >= 0.7)**: 2 of 496 gene pairs: ARHGEF12–PLXNB2 (0.994); VPS50–VPS53 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03896.1 (VPS53, VPS50; 2/7); huMAP3_13708.1 (VPS53, VPS50; 2/8); huMAP3_09592.1 (STT3A, CDKAL1; 2/95)

### Novelty

The specific co-abundance module may be a new systems-level observation, because it combines several biologically distinct processes and is not recapitulated by a globally significant GO/KEGG or STRING enrichment result. However, novelty cannot be claimed solely from sparse STRING coverage or absence from hu.MAP: those resources record physical or curated molecular relationships, whereas co-abundance can arise from shared regulation, cell composition, or coordinated state changes. The defensible conclusion is that the module-level association appears insufficiently characterized by the cited databases, but its biological novelty and causality require replication in independent lung and stem-cell datasets, cell-type-aware analysis, and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a coordinated membrane-to-organelle adaptation program shared by selected lung and stem-cell populations. Plexin-linked signaling through PLXNB2 and ARHGEF12 may influence Rho-dependent cytoskeletal state, while ITPR3 and ERLIN2 regulate endoplasmic-reticulum calcium dynamics. VPS50 and VPS53 may help route receptors and cargo through recycling or retrograde trafficking, and EIF2AK4 may couple nutrient or cellular stress to reduced translation. In this model, the module represents a cell-state program integrating surface signaling, calcium control, vesicle traffic, and stress adaptation rather than a single canonical pathway. This is a mechanistic hypothesis, not an established conclusion from the enrichment results.

### Important genes

#### ITPR3

- **Related proteins** (co-abundance neighbors): PMM2 (0.84), DBT (0.81), WASF2 (0.81), ERLIN2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inositol 1,4,5-trisphosphate receptor type 3. This gene encodes a receptor for inositol 1,4,5-trisphosphate, a second messenger that mediates the release of intracellular calcium. The receptor contains a calcium channel at the C-terminus and the ligand-binding site at the N-terminus. Knockout studies in mice suggest that type 2 and type 3 inositol 1,4,5-trisphosphate receptors play a key role in exocrine secretion underlying energy metabolism…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease, demyelinating, type 1J (0.656); immunodeficiency 133 with ectodermal dysplasia with or without peripheral neuropathy (0.532); type 1 diabetes mellitus (0.496); rheumatoid arthritis (0.454); chronic hepatitis B virus infection (0.443)
- **Europe PMC papers**: 2080
- **Why important**: ITPR3 is among the more connected genes in the module and links to PMM2, DBT, WASF2, and ERLIN2. It encodes an intracellular calcium-release channel, has cell-type-enhanced expression in both alveolar populations, and is connected to calcium signaling and exocrine secretion in the supplied annotations. Its position provides a plausible bridge between membrane signaling, endoplasmic-reticulum function, and cytoskeletal remodeling. It also has substantial literature and disease associations involving neuropathy, immunodeficiency, diabetes, and inflammatory disease.
- **Conclusion**: Established evidence supports ITPR3 as a calcium-release component with lung-relevant alveolar expression and a central position in this module. It is plausible, but not established, that ITPR3-mediated calcium signaling coordinates the other module processes.

#### PLXNB2

- **Related proteins** (co-abundance neighbors): ARHGEF12 (0.90), RAB32 (0.84), DAGLB (0.81); STRING partners: ARHGEF12 (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plexin B2. Members of the B class of plexins, such as PLXNB2 are transmembrane receptors that participate in axon guidance and cell migration in response to semaphorins (Perrot et al. (2002) [PubMed 12183458]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Intellectual disability (0.519); amelogenesis imperfecta (0.518); sensorineural hearing loss disorder (0.516); cutaneous melanoma (0.486); neurodegenerative disease (0.455)
- **Europe PMC papers**: 2109
- **Why important**: PLXNB2 is a membrane receptor with connections to ARHGEF12, RAB32, and DAGLB. The direct STRING relationship with ARHGEF12 is the strongest supported signaling link in the module. PLXNB2 is cell-type enhanced in alveolar cells and shows enrichment across several monocyte and dendritic-cell populations. Its known roles in semaphorin responses, cell migration, adhesion, receptor-mediated endocytosis, and neurodevelopment make it a strong candidate for connecting extracellular cues to the module’s trafficking and cytoskeletal features.
- **Conclusion**: Established evidence supports PLXNB2 as a signaling and trafficking receptor, with lung and selected immune-cell relevance and a known relationship to ARHGEF12. Its role as an upstream organizer of the entire module remains a hypothesis.

#### ARHGEF12

- **Related proteins** (co-abundance neighbors): PLXNB2 (0.90), CDK5RAP3 (0.84), NIPBL (0.82), SWAP70 (0.81); STRING partners: PLXNB2 (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho guanine nucleotide exchange factor 12. Rho GTPases play a fundamental role in numerous cellular processes that are initiated by extracellular stimuli working through G protein-coupled receptors. The encoded protein may form a complex with G proteins and stimulate Rho-dependent signals. This protein has been observed to form a myeloid/lymphoid fusion partner in acute myeloid leukemia. Three transcript variants encoding different isoform…
- **Diseases (Open Targets)**: glaucoma (0.524); open-angle glaucoma (0.511); lymphoid neoplasm (0.370); lung carcinoma (0.370); Chordoid Meningioma (0.370)
- **Europe PMC papers**: 923
- **Why important**: ARHGEF12 is a relatively connected node linked to PLXNB2, CDK5RAP3, NIPBL, and SWAP70. It encodes a Rho guanine-nucleotide exchange factor, placing it near actin organization, small-GTPase signaling, and receptor-driven cellular responses. Its direct STRING relationship with PLXNB2 gives the module a supported receptor-to-Rho signaling connection. It has substantial literature and disease associations involving glaucoma, lymphoid neoplasia, and lung carcinoma.
- **Conclusion**: Established evidence supports ARHGEF12 as a regulator of Rho-dependent signaling and as a known partner of PLXNB2. It may help translate receptor activity into cytoskeletal or migration changes in the shared module, but the co-abundance data do not prove that direction of regulation.

#### VPS50

- **Related proteins** (co-abundance neighbors): HDHD2 (0.85), RBBP9 (0.82); STRING partners: VPS53 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_03896.1, huMAP3_13708.1
- **Function (MyGene.info)**: VPS50 subunit of EARP/GARPII complex. Enables SNARE binding activity. Acts upstream of or within endocytic recycling. Located in recycling endosome. Part of EARP complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, seizures, and neonatal cholestasis (0.601); placenta praevia (0.227); malnutrition (0.223); macular degeneration (0.186); glomerulonephritis (0.184)
- **Europe PMC papers**: 99
- **Why important**: VPS50 participates in endocytic recycling and retrograde endosome-to-Golgi transport and is connected in the module to HDHD2 and RBBP9. It has a direct STRING relationship with VPS53 and appears with VPS53 in the hu.MAP complexes C1 and C2. This convergence of independent interaction resources makes VPS50 an important anchor for the module’s vesicle-trafficking component. Its disease associations include a neurodevelopmental disorder involving microcephaly, seizures, and cholestasis.
- **Conclusion**: Established evidence supports VPS50 as a component of EARP or GARP-related recycling machinery and confirms a relationship with VPS53. A role for VPS50 in coordinating receptor recycling with calcium or Rho signaling is a hypothesis.

#### VPS53

- **Related proteins** (co-abundance neighbors): OSBPL1A (0.81); STRING partners: VPS50 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_03896.1, huMAP3_13708.1
- **Function (MyGene.info)**: VPS53 subunit of GARP complex. This gene encodes a protein with sequence similarity to the yeast Vps53p protein. Vps53p is involved in retrograde vesicle trafficking in late Golgi. [provided by RefSeq, Jul 2008]
- **Diseases (Open Targets)**: pontocerebellar hypoplasia type 2E (0.732); progressive cerebello-cerebral atrophy (0.656); prostate carcinoma (0.539); neurodegenerative disease (0.528); prostate cancer (0.480)
- **Europe PMC papers**: 504
- **Why important**: VPS53 is a Golgi and vesicle-associated component of GARP-related retrograde trafficking. Although it has limited local connectivity in the co-abundance graph, its relationship with VPS50 is strongly supported by STRING and by the hu.MAP complexes C1 and C2. It therefore provides unusually strong complex-level support within an otherwise sparsely validated network. VPS53 also has established associations with pontocerebellar hypoplasia, progressive cerebello-cerebral atrophy, and neurodegenerative disease.
- **Conclusion**: Established evidence supports VPS53 as a vesicle-trafficking factor that forms a supported module subunit with VPS50. Its participation in a broader lung–stem-cell stress or signaling program is plausible but not demonstrated.

## Module 11

**Tissue pair**: lung and stem_cells  
**Genes (33)**: AP1M1, AP3D1, ARMC8, BAG3, BCLAF1, BRIX1, COG1, CRNKL1, COPS3, CACYBP, EIF2B2, EXOC4, GNL3, GRIPAP1, KLC1, NAA10, NCK1, OCRL, PDCD6IP, PTGR1, RCC1, MRPL10, SCAF11, PSAT1, SMAP, SRP54, STK3, VARS2, TXNRD1, UBLCP1, GGCX, VPS33A, YTHDF2

### Function

No GO/KEGG term passed global correction, and there was no supplementary STRING functional enrichment. Therefore, the module should not be assigned a single statistically established pathway. Its genes nevertheless converge on general cellular maintenance in proliferative or differentiating cells: nucleolar ribosome production and stem-cell proliferation through GNL3 and BRIX1; RNA processing through SCAF11, BCLAF1 and related nuclear factors; vesicle, endosomal and lysosomal trafficking through VPS33A, OCRL, AP-complex components, COG1 and EXOC4; and cellular stress, redox and protein-quality control through TXNRD1, BAG3 and CACYBP. The sparse co-abundance graph links these processes only weakly, so the most defensible interpretation is a broad growth, biosynthetic and trafficking program rather than a discrete pathway.

**Cell composition.** The module is predominantly composed of broadly expressed, low-tissue-specificity genes, with many genes having low immune-cell specificity. It is therefore not mainly a plasma-protein, secreted-protein or blood-cell module, and a blood-contamination explanation is not favored by the HPA summary. Most module proteins are detected in lung, whereas there is no directly matching HPA tissue category for stem_cells. A minority of genes show tissue or cell-type enhancement in liver, brain, skeletal muscle, bone marrow, intestine and several specialized reproductive or epithelial cell types. This heterogeneous pattern is more compatible with a shared housekeeping, proliferative or cell-state program than with a lung-specific secretory function. The single secreted gene does not support a secreted-protein interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The high-confidence STRING evidence is limited to a small set of pairwise relationships. The strongest known links connect BRIX1 with GNL3, and GNL3 with RCC1, while AP1M1 is linked with AP3D1 and BCLAF1 with SCAF11. These relationships support parts of the nucleolar, cell-cycle, vesicle-trafficking and RNA-processing interpretation, but they do not establish one unified physical complex for the whole module. hu.MAP provides additional partial complex support: VPS33A and CACYBP co-occur in huMAP3_12433.1 and huMAP3_12945.1 (hu.MAP huMAP3_12433.1) (hu.MAP huMAP3_12945.1), while OCRL and AP1M1 co-occur in the large trafficking-related huMAP3_12394.1 complex (hu.MAP huMAP3_12394.1). Because each hu.MAP match contains only a small subset of the relevant complex, the module appears to combine several known cellular subsystems rather than represent a single canonical complex.

**STRING interactions (score >= 0.7)**: 4 of 528 gene pairs: AP1M1–AP3D1 (0.877); BCLAF1–SCAF11 (0.72); BRIX1–GNL3 (0.98); GNL3–RCC1 (0.743)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12433.1 (VPS33A, CACYBP; 2/11); huMAP3_12945.1 (VPS33A, CACYBP; 2/12); huMAP3_12394.1 (OCRL, AP1M1; 2/98)

### Novelty

This is not demonstrated to be a wholly new molecular mechanism. Several of its relationships and functions are already established by STRING, hu.MAP, curated gene annotations and disease literature. The potentially novel observation is the coordinated co-abundance of these otherwise separate processes across lung and stem_cells. However, the graph is sparse, global enrichment is absent, and there is no direct evidence here that the cross-tissue module has been independently reported. Accordingly, it is best described as a potentially novel tissue-pair association or systems-level module, not as proof of a new pathway. Absence from STRING or hu.MAP would not by itself establish novelty.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular state in which proliferating or differentiating cells coordinate ribosome biogenesis, RNA maturation, mitochondrial and cytosolic protein production, redox protection, and membrane-trafficking capacity. GNL3 and BRIX1 may mark the biosynthetic and nucleolar component; VPS33A and OCRL may connect that state to endosomal and lysosomal trafficking; and TXNRD1 may help buffer the oxidative burden associated with growth and protein synthesis. This model predicts that module activity will track cell proliferation or differentiation and proteostatic demand rather than a lung-specific extracellular function. It remains a hypothesis because no globally significant enrichment or direct causal experiment is provided.

### Important genes

#### GNL3

- **Related proteins** (co-abundance neighbors): TXNRD1 (0.84), PSAT1 (0.82), AP3D1 (0.81), EXOC4 (0.81); STRING partners: BRIX1 (0.98), RCC1 (0.743)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein nucleolar 3. The protein encoded by this gene may interact with p53 and may be involved in tumorigenesis. The encoded protein also appears to be important for stem cell proliferation. This protein is found in both the nucleus and nucleolus. Three transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Nov 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.357); Abnormality of the skeletal system (0.264); cataract (0.252); trauma complication (0.245); osteoarthritis (0.155)
- **Europe PMC papers**: 959
- **Why important**: GNL3 is a network-central connector associated with TXNRD1, PSAT1, AP3D1 and EXOC4, and it has a high-confidence STRING relationship with BRIX1 plus an additional relationship with RCC1. Its established annotations include nucleolar localization, stem-cell division, stem-cell population maintenance, proliferation and telomere maintenance. It therefore provides an important bridge between the module's nucleolar, proliferative and trafficking-related signals. Its literature is substantial, and its disease associations include neurodegenerative and skeletal abnormalities.
- **Conclusion**: Established evidence supports GNL3 as a nucleolar and stem-cell maintenance factor that is central to this module's interpretation. It is plausible, but unproven, that GNL3 helps couple biosynthetic growth demands to the other module processes.

#### BRIX1

- **Related proteins** (co-abundance neighbors): BAG3 (0.85), YTHDF2 (0.85), AP3D1 (0.84), KLC1 (0.83), UBLCP1 (0.82), RCC1 (0.80); STRING partners: GNL3 (0.98)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Mitotic chromosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biogenesis of ribosomes BRX1. Enables RNA binding activity. Predicted to be involved in ribosomal large subunit assembly. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: colorectal cancer (0.077); cancer (0.077); colorectal carcinoma (0.074); deficiency anemia (0.065); sialolithiasis (0.060)
- **Europe PMC papers**: 251
- **Why important**: BRIX1 has the strongest network connectivity in the module and connects to BAG3, YTHDF2, AP3D1, KLC1, UBLCP1 and RCC1. Its established function is ribosomal large-subunit assembly and rRNA processing, with nucleolar and mitotic-chromosome localization. Its high-confidence STRING relationship with GNL3 gives direct support to a ribosome-biogenesis submodule. It also has a substantial literature base and reported links to cancer and deficiency anemia.
- **Conclusion**: Established evidence identifies BRIX1 as a strong marker of ribosome production and proliferative biosynthetic capacity. Its central network position supports its use as an anchor gene, but the data do not show that BRIX1 drives the cross-tissue co-abundance pattern.

#### VPS33A

- **Related proteins** (co-abundance neighbors): STK3 (0.89), SCAF11 (0.85), COG1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12433.1, huMAP3_12945.1
- **Function (MyGene.info)**: VPS33A core subunit of CORVET and HOPS complexes. This gene encodes a tethering protein and a core subunit of the homotypic fusion and protein sorting (HOPS) complex. The HOPS complex and a second endosomal tethering complex called the class C core vacuole/endosome tethering (CORVET) complex, perform diverse functions in endocytosis including membrane tethering, RabGTPase interaction, activation and proofreading of synaptic-soluble N-ethylmaleimi…
- **Diseases (Open Targets)**: mucopolysaccharidosis-plus syndrome (0.752); neurodegenerative disease (0.496); COVID-19 (0.370); placental abruption (0.198); retinitis pigmentosa (0.097)
- **Europe PMC papers**: 912
- **Why important**: VPS33A connects the module to STK3, SCAF11 and COG1 and is represented in two hu.MAP complexes with CACYBP (hu.MAP huMAP3_12433.1) (hu.MAP huMAP3_12945.1). Its established function as a CORVET and HOPS core subunit supports endosomal tethering, intracellular transport, endosome-to-lysosome transport and membrane fusion. It has substantial disease literature, including mucopolysaccharidosis-plus syndrome and neurodegenerative disease.
- **Conclusion**: Established evidence supports VPS33A as the clearest endolysosomal trafficking component of the module. Its presence alongside nucleolar and redox genes supports a shared cellular-maintenance interpretation, while any direct role in coupling trafficking to stem-cell state remains hypothetical.

#### OCRL

- **Related proteins** (co-abundance neighbors): STK3 (0.88), SMAP (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Microtubules, Primary cilium; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: OCRL inositol polyphosphate-5-phosphatase. This gene encodes an inositol polyphosphate 5-phosphatase. This protein is involved in regulating membrane trafficking and is located in numerous subcellular locations including the trans-Golgi network, clathrin-coated vesicles and, endosomes and the plasma membrane. This protein may also play a role in primary cilium formation. Mutations in this gene cause oculocerebrorenal syndrome of Lowe and a…
- **Diseases (Open Targets)**: oculocerebrorenal syndrome (0.864); Dent disease type 2 (0.814); Dent disease (0.740); nephrocalcinosis (0.469); hypercholesterolemia, familial, 1 (0.333)
- **Europe PMC papers**: 1458
- **Why important**: OCRL links STK3 with SMAP in the module and occurs with AP1M1 in a hu.MAP trafficking complex (hu.MAP huMAP3_12394.1). Its established enzymatic role in inositol-phosphate and phosphoinositide metabolism, together with localization to the trans-Golgi network, clathrin-coated vesicles, endosomes and primary cilia, gives it strong mechanistic relevance to membrane trafficking. Its disease associations with oculocerebrorenal syndrome and Dent disease are well established.
- **Conclusion**: Established evidence supports OCRL as a membrane-trafficking and phosphoinositide-regulation component. The module does not establish a new OCRL disease mechanism, but its co-abundance with VPS33A and adaptor machinery makes altered endosomal organization a reasonable hypothesis.

#### TXNRD1

- **Related proteins** (co-abundance neighbors): GNL3 (0.84), PTGR1 (0.83), NCK1 (0.82), COPS3 (0.82), CACYBP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin reductase 1. The protein encoded by this gene belongs to the pyridine nucleotide-disulfide oxidoreductase family, and is a member of the thioredoxin (Trx) system. Three thioredoxin reductase (TrxR) isozymes are found in mammals. TrxRs are selenocysteine-containing flavoenzymes, which reduce thioredoxins, as well as other substrates, and play a key role in redox homoeostasis. This gene encodes an ubiquitously e…
- **Diseases (Open Targets)**: acute promyelocytic leukemia (0.588); neoplasm (0.397); brain cancer (0.371); acute myeloid leukemia (0.370); arthritic joint disease (0.370)
- **Europe PMC papers**: 4293
- **Why important**: TXNRD1 is among the most connected genes and links GNL3 with PTGR1, NCK1, COPS3 and CACYBP. Its established function in the thioredoxin system, selenium metabolism, cellular redox homeostasis and oxidant detoxification supplies a plausible stress-buffering component for a biosynthetically active cell state. It has extensive literature and broad disease associations, including hematologic malignancy, cancer and inflammatory disease.
- **Conclusion**: Established evidence supports TXNRD1 as a broadly expressed redox-homeostasis factor rather than a tissue-specific marker. Its network position suggests coordination between redox control and growth-related processes, but the direction and causality of that relationship are not demonstrated.

#### BCLAF1

- **Related proteins** (co-abundance neighbors): MRPL10 (0.87), STK3 (0.81); STRING partners: SCAF11 (0.72)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BCL2 associated transcription factor 1. This gene encodes a transcriptional repressor that interacts with several members of the BCL2 family of proteins. Overexpression of this protein induces apoptosis, which can be suppressed by co-expression of BCL2 proteins. The protein localizes to dot-like structures throughout the nucleus, and redistributes to a zone near the nuclear envelope in cells undergoing apoptosis. Multiple transcript var…
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); Pulmonary artery atresia (0.416); acute myeloid leukemia (0.357); bronchial disorder (0.288); Vertigo (0.253)
- **Europe PMC papers**: 1702
- **Why important**: BCLAF1 connects MRPL10 with STK3 and has a known STRING relationship with SCAF11. Its established annotations include transcriptional repression, apoptosis, DNA-damage response and mRNA stabilization, while its nuclear-speckle localization places it near RNA-processing machinery. It has a substantial literature and reported associations with hematologic, neurologic and bronchial disorders.
- **Conclusion**: Established evidence supports BCLAF1 as a nuclear RNA-regulatory and stress-response component. Its position may connect mitochondrial translation, RNA processing and apoptosis within the module, but that integrative role is a hypothesis rather than an established mechanism.

## Module 12

**Tissue pair**: lung and stem_cells  
**Genes (11)**: APMAP, CLN6, DSTN, ITGA3, ITGAV, ITGB1, PGM1, RAB21, RIF1, MRPL45, SORBS1

### Function

This is a cell–extracellular-matrix adhesion module centered on integrin receptors. The strongest primary evidence is the globally corrected enrichment for fibronectin binding (GO:MF fibronectin binding; q_global = 0.00367), integrin complex (GO:CC integrin complex; q_global = 0.00736), C-X3-C chemokine binding (GO:MF C-X3-C chemokine binding; q_global = 0.0227), the integrin alpha3-beta1 and alphav-beta1 complexes (GO:CC integrin alpha3-beta1 complex; q_global = 0.0227) (GO:CC integrin alphav-beta1 complex; q_global = 0.0227), extracellular-matrix binding (GO:MF extracellular matrix binding; q_global = 0.0232), and adhesion-associated protein complexes (GO:CC protein complex involved in cell adhesion; q_global = 0.0276). The cardiomyopathy pathway terms (KEGG Hypertrophic cardiomyopathy - Homo sapiens (human); q_global = 0.0377) (KEGG Dilated cardiomyopathy - Homo sapiens (human); q_global = 0.0377) (KEGG Arrhythmogenic right ventricular cardiomyopathy - Homo sapiens (human); q_global = 0.0433) should be interpreted as evidence for integrin-linked adhesion and mechanotransduction rather than as evidence that the module specifically represents heart disease. The module therefore most plausibly reflects coordinated cell-substrate attachment, extracellular-matrix sensing, migration, and downstream cytoskeletal signaling. The remaining genes may represent connected trafficking, actin, metabolic, mitochondrial, nuclear, or lysosomal context rather than a single additional enriched process. No GO or KEGG term beyond the listed globally significant GO/KEGG terms should be treated as globally significant.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes, and the proteins are mainly intracellular or membrane-associated. It is also not strongly blood-cell specific, with generally low immune-cell specificity and only limited enrichment involving basophils. HPA instead indicates broad or cell-type-enhanced expression, with recurring signals in podocytes, myonuclei, hepatocytes, and vascular or epithelial populations. Blood-vessel enhancement occurs for SORBS1 and DSTN, while several integrins are enhanced in alveolar, podocyte, urothelial, or related epithelial cells. Thus, the shared lung–stem_cells signal is more consistent with a conserved adhesion or shared cell-state program than with a plasma-protein or general blood-contamination module, although cell-type composition remains a possible contributor. Lung protein detection is present for much of the module, whereas HPA provides no matching stem-cell tissue category.

**GO/KEGG enrichment**: 10 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF fibronectin binding | 0.00367 | ITGA3, ITGAV, ITGB1 |
| GO:CC integrin complex | 0.00736 | ITGA3, ITGAV, ITGB1 |
| GO:MF C-X3-C chemokine binding | 0.0227 | ITGAV, ITGB1 |
| GO:CC integrin alpha3-beta1 complex | 0.0227 | ITGA3, ITGB1 |
| GO:CC integrin alphav-beta1 complex | 0.0227 | ITGAV, ITGB1 |
| GO:MF extracellular matrix binding | 0.0232 | ITGA3, ITGAV, ITGB1 |
| GO:CC protein complex involved in cell adhesion | 0.0276 | ITGA3, ITGAV, ITGB1 |
| KEGG Hypertrophic cardiomyopathy - Homo sapiens (human) | 0.0377 | ITGA3, ITGAV, ITGB1 |
| KEGG Dilated cardiomyopathy - Homo sapiens (human) | 0.0377 | ITGA3, ITGAV, ITGB1 |
| KEGG Arrhythmogenic right ventricular cardiomyopathy - Homo sapiens (human) | 0.0433 | ITGA3, ITGAV, ITGB1 |

### STRING and hu.MAP

STRING supports a compact, biologically coherent integrin core: ITGA3–ITGB1 and ITGAV–ITGB1 are very strong known associations, ITGA3–ITGAV is also supported, and ITGB1–RAB21 links the receptor core to integrin trafficking. STRING functional results independently support integrin function, fibronectin binding, integrin-mediated adhesion, extracellular-matrix interaction, and the cardiomyopathy pathway annotations (15 supplementary STRING terms; within-query FDR 0.0026–0.0279); these are supplementary and not global enrichment evidence. hu.MAP places ITGA3 and ITGB1 together in several integrin or adhesion-related complexes (hu.MAP huMAP3_06815.1) (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1), with partners including other integrin subunits, galectins, adhesion molecules, phosphatases, and membrane-trafficking proteins. The fact that only ITGA3 and ITGB1 from this module occur in those complexes means the complex evidence strongly validates the integrin core but does not establish that the entire module is one physical complex. The absence of STRING or hu.MAP support for several peripheral genes indicates limited database connectivity, not biological irrelevance.

**STRING interactions (score >= 0.7)**: 4 of 55 gene pairs: ITGA3–ITGAV (0.968); ITGA3–ITGB1 (0.999); ITGAV–ITGB1 (0.999); ITGB1–RAB21 (0.815)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Integrin (FDR = 0.0026, 3 genes); WikiPathways Integrin-mediated cell adhesion (FDR = 0.0038, 4 genes); Function Fibronectin binding (FDR = 0.0044, 3 genes); KEGG Hypertrophic cardiomyopathy (FDR = 0.007, 3 genes); KEGG Arrhythmogenic right ventricular cardiomyopathy (FDR = 0.007, 3 genes); KEGG Dilated cardiomyopathy (FDR = 0.007, 3 genes); Component Integrin complex (FDR = 0.0084, 3 genes); InterPro Integrin domain superfamily (FDR = 0.0109, 3 genes); NetworkNeighborAL Integrin domain superfamily (FDR = 0.0115, 3 genes); WikiPathways Arrhythmogenic right ventricular cardiomyopathy (FDR = 0.0116, 3 genes); KEGG ECM-receptor interaction (FDR = 0.0124, 3 genes); KEGG Small cell lung cancer (FDR = 0.0141, 3 genes); Function Extracellular matrix binding (FDR = 0.0175, 3 genes); Component Integrin alpha3-beta1 complex (FDR = 0.0266, 2 genes); COMPARTMENTS Integrin complex (FDR = 0.0279, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06815.1 (ITGB1, ITGA3; 2/5); huMAP3_10503.1 (ITGB1, ITGA3; 2/27); huMAP3_10980.1 (ITGB1, ITGA3; 2/44); huMAP3_09336.1 (ITGB1, ITGA3; 2/50)

### Novelty

The integrin-centered function is not a new biological concept: integrin complexes, fibronectin binding, cell-matrix adhesion, and integrin trafficking are established biology, and the central ITGA3–ITGB1 and ITGAV–ITGB1 relationships are already represented in STRING and hu.MAP. What may be novel is the specific conserved co-abundance arrangement linking this integrin core with APMAP, SORBS1, RAB21, CLN6, DSTN, PGM1, MRPL45, and RIF1 across lung and stem_cells. However, the fact sheet does not provide a literature or independent-cohort comparison demonstrating that this exact module has not been reported. Therefore the defensible conclusion is that the module is a potentially novel cross-tissue co-abundance configuration built around a well-established adhesion program, not a claim of a wholly novel pathway.

**Hypothesis.** Hypothesis: a conserved cell-surface adhesion state coordinates ITGA3 and ITGAV with ITGB1 to sense extracellular matrix, especially fibronectin-related cues, while SORBS1 and DSTN connect adhesion to focal-adhesion and actin remodeling, and RAB21 regulates receptor trafficking. APMAP may mark a membrane-associated cellular state, while CLN6, PGM1, MRPL45, and RIF1 may capture linked lysosomal, metabolic, mitochondrial, or proliferative demands of cells maintaining adhesion and remodeling. In lung, this could support epithelial or vascular attachment and repair; in stem_cells, it could contribute to niche interaction and cell-state maintenance. The peripheral links are hypotheses generated by co-abundance and should be tested with cell-type-resolved perturbation, localization, and physical-interaction experiments.

### Important genes

#### ITGB1

- **Related proteins** (co-abundance neighbors): ITGAV (0.82), ITGA3 (0.81), MRPL45 (0.80); STRING partners: ITGA3 (0.999), ITGAV (0.999), RAB21 (0.815)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06815.1, huMAP3_10503.1, huMAP3_10980.1, huMAP3_09336.1
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is the central receptor subunit in the module’s strongest network relationships, connecting both ITGA3 and ITGAV and also linking to RAB21. It is present in every primary integrin-related GO/KEGG term (10 globally significant GO/KEGG terms, q_global 0.00367–0.0433; see the table), every STRING functional category (15 supplementary STRING terms; within-query FDR 0.0026–0.0279), and all listed hu.MAP complexes (hu.MAP huMAP3_06815.1) (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1). Its established functions include cell adhesion, cell-matrix adhesion, angiogenesis, phagocytosis, and cell-defense processes, and it has extensive disease and literature support.
- **Conclusion**: Established evidence identifies ITGB1 as the principal structural and functional hub of the module. It is reasonable to hypothesize that coordinated ITGB1 abundance is a major driver of the shared adhesion signal, but co-abundance alone does not establish receptor activation or a causal role in either tissue.

#### ITGA3

- **Related proteins** (co-abundance neighbors): ITGB1 (0.81); STRING partners: ITGAV (0.968), ITGB1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_06815.1, huMAP3_10503.1, huMAP3_10980.1, huMAP3_09336.1
- **Function (MyGene.info)**: integrin subunit alpha 3. The gene encodes a member of the integrin alpha chain family of proteins. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain that function as cell surface adhesion molecules. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha 3 subunit. This subunit joins with a beta 1 subunit to form an …
- **Diseases (Open Targets)**: epidermolysis bullosa, junctional 7, with interstitial lung disease and nephrotic syndrome (0.807); neurodegenerative disease (0.503); junctional epidermolysis bullosa (0.372); junctional epidermolysis bullosa Herlitz type (0.370); epidermolysis bullosa simplex 4, localized or generalized intermediate, autosomal recessive (0.370)
- **Europe PMC papers**: 4167
- **Why important**: ITGA3 forms the strongly supported alpha3-beta1 integrin complex with ITGB1 and is present in the primary fibronectin-binding, integrin-complex, extracellular-matrix, adhesion-complex, and cardiomyopathy terms (8 globally significant GO/KEGG terms, q_global 0.00367–0.0433; see the table). It is supported by STRING (15 supplementary STRING terms; within-query FDR 0.0026–0.0279) and hu.MAP (hu.MAP huMAP3_06815.1) (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1), is expressed in alveolar and other epithelial or podocyte cell types, and has a notable association with junctional epidermolysis bullosa with interstitial lung disease and nephrotic syndrome.
- **Conclusion**: Established evidence supports ITGA3 as the lung-relevant alpha receptor partner that anchors the module to epithelial and basement-membrane adhesion biology. Its disease associations make defective adhesion a biologically credible interpretation, while any specific role in stem-cell maintenance remains a hypothesis.

#### ITGAV

- **Related proteins** (co-abundance neighbors): ITGB1 (0.82), APMAP (0.80); STRING partners: ITGA3 (0.968), ITGB1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha V. The product of this gene belongs to the integrin alpha chain family. Integrins are heterodimeric integral membrane proteins composed of an alpha subunit and a beta subunit that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha V subunit. This subunit associates with beta 1, beta 3, beta…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); myocardial infarction (0.396); angina pectoris (0.371); Recurrent thrombophlebitis (0.370); intermediate coronary syndrome (0.370)
- **Europe PMC papers**: 5475
- **Why important**: ITGAV is the second alpha integrin in the module and forms a strong STRING-supported relationship with ITGB1 and ITGA3. It contributes to the primary fibronectin-binding, C-X3-C chemokine-binding, alphav-beta1-complex, extracellular-matrix, adhesion-complex, and cardiomyopathy terms (9 globally significant GO/KEGG terms, q_global 0.00367–0.0433; see the table), as well as most corresponding STRING categories (14 supplementary STRING terms; within-query FDR 0.0026–0.0279). Its established functions include cell-matrix adhesion, angiogenesis, vasculogenesis, and calcium-linked signaling.
- **Conclusion**: Established evidence indicates that ITGAV broadens the module from a single alpha3-beta1 receptor to a more flexible integrin signaling program. The module may therefore encode shared matrix sensing rather than one exclusive receptor complex; which ITGAV heterodimer is functionally active in either tissue is unresolved.

#### RAB21

- **Related proteins** (co-abundance neighbors): SORBS1 (0.84); STRING partners: ITGB1 (0.815)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB21, member RAS oncogene family. This gene belongs to the Rab family of monomeric GTPases, which are involved in the control of cellular membrane traffic. The encoded protein plays a role in the targeted trafficking of integrins via its association with integrin alpha tails. As a consequence, the encoded protein is involved in the regulation of cell adhesion and migration. Expression of this gene is associated with a poor prognos…
- **Diseases (Open Targets)**: neurodegenerative disease (0.469); small intestine neuroendocrine neoplasm (0.095); neoplasm (0.085); posterior cortical atrophy (0.074); nonpapillary renal cell carcinoma (0.065)
- **Europe PMC papers**: 999
- **Why important**: RAB21 connects the adhesion core to membrane trafficking through its STRING relationship with ITGB1 and is linked in the module network to SORBS1. Its documented function includes targeted integrin trafficking, regulation of cell adhesion and migration, receptor-mediated endocytosis, and membrane transport. Its network position makes it a mechanistically informative peripheral gene despite not appearing in the primary GO/KEGG terms.
- **Conclusion**: Established evidence supports RAB21 as a plausible trafficking regulator of integrin localization and turnover. Its participation in the shared module is consistent with coordinated receptor recycling, but the specific direction and tissue consequences of that regulation are hypotheses.

#### SORBS1

- **Related proteins** (co-abundance neighbors): RAB21 (0.84), APMAP (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Focal adhesion sites; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sorbin and SH3 domain containing 1. This gene encodes a CBL-associated protein which functions in the signaling and stimulation of insulin. Mutations in this gene may be associated with human disorders of insulin resistance. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.454); atrial fibrillation (0.394); urinary system disorder (0.381); uterine corpus leiomyoma (0.351); hypertensive disorder (0.345)
- **Europe PMC papers**: 1367
- **Why important**: SORBS1 links to RAB21 and APMAP in the module and is the only module gene represented in the STRING integrin-mediated adhesion term beyond the three core integrin subunits (STRING WikiPathways Integrin-mediated cell adhesion; within-query FDR = 0.0038). It localizes to focal adhesion sites and has established associations with cytoskeleton organization, cell-matrix and cell-substrate adhesion, stress-fiber assembly, and insulin signaling. HPA shows blood-vessel enhancement and cell-type enhancement in adipocytes, astrocytes, and cardiomyocytes, while Open Targets includes cardiovascular and metabolic disease associations.
- **Conclusion**: Established evidence supports SORBS1 as a scaffold connecting integrin signaling to cytoskeletal organization and metabolic signaling. Its co-abundance with the integrin core suggests a candidate adapter role in the shared module, but direct physical coupling in lung or stem_cells has not been demonstrated here.

## Module 13

**Tissue pair**: lung and stem_cells  
**Genes (21)**: ARMH3, CDK1, CMSS1, COMMD8, COX6C, DDX41, EXOSC2, EXOSC3, KAT7, PPP1R12A, NUP214, NUP85, PLOD2, CRYZ, RCL1, SUN1, THOC1, TPX2, USP19, VTA1, ZMYM4

### Function

This module does not have a globally significant GO/KEGG enrichment term: no term passed global correction, so the functional interpretation must come from the gene annotations and network structure rather than enrichment statistics. The most coherent interpretation is a mixed nuclear and proliferative cell-state module. CDK1 and TPX2 support mitotic kinase activity, spindle assembly, and cell-cycle progression; EXOSC2, EXOSC3, and RCL1 support nuclear RNA processing, ribosome biogenesis, and RNA surveillance; THOC1 supports messenger-RNA export; and NUP85 with NUP214 supports nucleocytoplasmic transport. SUN1 adds a nuclear-envelope and nuclear-anchorage component, while DDX41 contributes RNA helicase activity and cGAS/STING-related biology. The sparse network contains several biologically interpretable substructures rather than one demonstrated pathway, so this is best viewed as a coordinated cellular state involving proliferation, RNA handling, and nuclear organization.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins: the HPA summary identifies only a single secreted gene, and the genes are predominantly intracellular or nuclear. Most genes have low tissue specificity and low immune-cell specificity, which is consistent with broadly expressed cellular machinery rather than a specialized blood or immune program. Nevertheless, HPA shows recurrent enrichment in erythrocyte progenitors and other proliferative or developmental cell types, with additional signals in bone marrow, lymphoid tissue, testis, liver, and kidney. CDK1 and TPX2 are enhanced in bone marrow and lymphoid tissue and in erythrocyte progenitors, while NUP214 is group-enriched in classical monocytes and neutrophils. Thus, sample composition or shared proliferative cell types could contribute to the lung and stem-cell concordance, but the evidence does not support describing this as a plasma-protein or broadly blood-cell module. Lung protein detection is present for many genes, whereas the stem-cell comparison has no matching HPA tissue.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a limited but informative set of known relationships. The strongest connections include EXOSC2 with EXOSC3, NUP214 with NUP85, and CDK1 with TPX2; additional links connect EXOSC2 and EXOSC3 with RCL1 and connect CDK1 with PPP1R12A. These relationships independently support an exosome or ribosome-processing substructure, a nuclear-pore substructure, and a mitotic substructure. hu.MAP also places EXOSC2 and EXOSC3 together in two exosome-related complexes (hu.MAP huMAP3_05382.1) (hu.MAP huMAP3_14264.1), NUP214 and NUP85 in a nuclear-pore complex (hu.MAP huMAP3_12581.1), TPX2 and DDX41 in a complex (hu.MAP huMAP3_13567.1), and THOC1 with DDX41 in an RNA-processing or export-associated complex (hu.MAP huMAP3_09943.1). However, each hu.MAP overlap contains only a small subset of the larger complex, so these are supporting links rather than proof that the entire module is one physical complex. The remaining co-abundance edges lack listed STRING or hu.MAP support and may represent co-regulation, shared cell-state dependence, or context-specific associations.

**STRING interactions (score >= 0.7)**: 6 of 210 gene pairs: CDK1–PPP1R12A (0.745); CDK1–TPX2 (0.952); EXOSC2–EXOSC3 (0.999); EXOSC2–RCL1 (0.744); EXOSC3–RCL1 (0.763); NUP214–NUP85 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13567.1 (DDX41, TPX2; 2/10); huMAP3_05382.1 (EXOSC2, EXOSC3; 2/18); huMAP3_14264.1 (EXOSC2, EXOSC3; 2/20); huMAP3_12581.1 (NUP214, NUP85; 2/58); huMAP3_09943.1 (THOC1, DDX41; 2/78)

### Novelty

The module should not be called a wholly new molecular complex or a newly discovered pathway. Several of its relationships are already established in STRING, and multiple gene pairs map to known hu.MAP complexes, especially the exosome-related, nuclear-pore, and RNA-processing assemblies. A potentially novel aspect is the co-abundance of these partially connected components across lung and stem-cell samples, particularly the combination of mitotic, RNA-processing, nuclear-transport, and nuclear-envelope genes. That dataset-level combination may be a new observation, but novelty cannot be established from absence of database links alone. Independent replication, comparison with published co-expression modules, and testing across additional tissues or cohorts would be needed to support a claim of novelty.

**Hypothesis.** Hypothesis: this shared module reflects a proliferative and developmentally plastic cell state in which increased cell-cycle activity is coupled to the RNA-processing, RNA-export, and nuclear-organization capacity required for rapid growth or differentiation. CDK1 and TPX2 may mark mitotic demand; EXOSC2, EXOSC3, and RCL1 may support processing and quality control of transcripts and ribosomal RNA; THOC1 and the nucleoporins may coordinate transcript export and nucleocytoplasmic transport; and SUN1 may link nuclear organization to cell mechanics or migration. The recurrent HPA signal in erythrocyte progenitors and other progenitor-like populations suggests that shared proliferative cell types or sample composition could help generate the cross-tissue module. This is a mechanistic hypothesis, not a demonstrated causal model.

### Important genes

#### CDK1

- **Related proteins** (co-abundance neighbors): EXOSC3 (0.85); STRING partners: PPP1R12A (0.745), TPX2 (0.952)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cyclin dependent kinase 1. The protein encoded by this gene is a member of the Ser/Thr protein kinase family. This protein is a catalytic subunit of the highly conserved protein kinase complex known as M-phase promoting factor (MPF), which is essential for G2/M phase transitions of eukaryotic cell cycle. Mitotic cyclins stably associate with this protein and function as regulatory subunits. The kinase activity of this prote…
- **Diseases (Open Targets)**: neurodegenerative disease (0.535); Alzheimer disease (0.526); Parkinson disease (0.523); lysosomal storage disease (0.512); prostatitis (0.404)
- **Europe PMC papers**: 33995
- **Why important**: CDK1 is the clearest proliferative anchor of the module. It is a catalytic component of the M-phase-promoting kinase system and is annotated for G two/M transition, DNA replication, DNA repair, chromatin remodeling, and microtubule organization. It has a direct STRING relationship with TPX2 and an additional relationship with PPP1R12A, linking the module to mitotic spindle control and cytoskeletal regulation. Its HPA profile is enhanced in bone marrow, lymphoid tissue, and erythrocyte progenitors, making it especially relevant to the possibility that the module reflects proliferating progenitor cells. Its extensive literature and disease annotation make its function well established.
- **Conclusion**: Established evidence supports CDK1 as a marker and likely functional contributor to cell-cycle activity in the module. It is plausible, but not proven, that CDK1-centered proliferation helps organize the cross-tissue co-abundance pattern.

#### TPX2

- **Related proteins** (co-abundance neighbors): PPP1R12A (0.81); STRING partners: CDK1 (0.952)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_13567.1
- **Function (MyGene.info)**: TPX2 microtubule nucleation factor. Enables importin-alpha family protein binding activity and protein kinase binding activity. Involved in activation of protein kinase activity; microtubule cytoskeleton organization; and negative regulation of microtubule depolymerization. Located in intercellular bridge; mitotic spindle; and nucleoplasm. Colocalizes with spindle pole. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.124); neoplasm (0.117); breast carcinoma (0.116); non-small cell lung carcinoma (0.112); breast cancer (0.110)
- **Europe PMC papers**: 4216
- **Why important**: TPX2 is an important mitotic and spindle-associated gene. It is annotated for microtubule nucleation, spindle assembly, spindle organization, kinase activation, and prevention of microtubule depolymerization. Its STRING relationship with CDK1 and its membership with DDX41 in hu.MAP complex (hu.MAP huMAP3_13567.1) connect the proliferative portion of the module to the broader nuclear and RNA-associated network. HPA enhancement in bone marrow, lymphoid tissue, testis, and erythrocyte progenitors is compatible with active division and developmental programs. TPX2 also has substantial literature volume and cancer-related annotations.
- **Conclusion**: Established evidence supports TPX2 as a spindle and mitotic component that reinforces the CDK1 interpretation. A role for TPX2 in integrating the module’s proliferative and developmental signals remains a hypothesis.

#### EXOSC3

- **Related proteins** (co-abundance neighbors): CDK1 (0.85), CMSS1 (0.83), USP19 (0.82); STRING partners: EXOSC2 (0.999), RCL1 (0.763)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_05382.1, huMAP3_14264.1
- **Function (MyGene.info)**: exosome component 3. This gene encodes a non-catalytic component of the human exosome, a complex with 3'-5' exoribonuclease activity that plays a role in numerous RNA processing and degradation activities. Related pseudogenes of this gene are found on chromosome 19 and 21. Alternatively spliced transcript variants encoding different isoforms have been described. [provided by RefSeq, Jun 2012].
- **Diseases (Open Targets)**: pontocerebellar hypoplasia type 1 (0.763); pontocerebellar hypoplasia (0.607); neurodegenerative disease (0.528); hereditary disease (0.414); pontocerebellar hypoplasia type 1A (0.370)
- **Europe PMC papers**: 2616
- **Why important**: EXOSC3 is a core RNA-processing representative and has direct STRING relationships with EXOSC2 and RCL1. It is included in two hu.MAP complexes (hu.MAP huMAP3_05382.1) (hu.MAP huMAP3_14264.1), both containing broader exosome-associated membership. Its annotations cover nuclear RNA degradation, RNA processing, and maturation of ribosomal RNA. The gene has a well-developed literature and strong disease associations involving pontocerebellar hypoplasia. Its HPA profile is broadly expressed, with enhancement in several neural cell types, rather than indicating a secreted or immune-specific protein.
- **Conclusion**: Established evidence supports EXOSC3 as part of the module’s RNA surveillance and ribosome-processing component. The co-abundance pattern may indicate increased RNA-processing demand in the shared cellular state, but it does not establish altered exosome activity.

#### NUP214

- **Related proteins** (co-abundance neighbors): NUP85 (0.81); STRING partners: NUP85 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 214. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene is a member of the FG-repeat-containing nucleoporins. The protein encoded by this gene is localized to the cytoplas…
- **Diseases (Open Targets)**: familial acute necrotizing encephalopathy (0.664); Orthomyxoviridae infectious disease (0.543); HIV infectious disease (0.542); viral infectious disease (0.527); Global developmental delay (0.435)
- **Europe PMC papers**: 2712
- **Why important**: NUP214 represents the nuclear-transport arm of the module and forms a very strong STRING relationship with NUP85. Both genes occur together in hu.MAP complex (hu.MAP huMAP3_12581.1). NUP214 is a nucleoporin involved in RNA export, protein import and export, and nucleocytoplasmic transport. Its HPA profile is enhanced in testis and group-enriched in classical monocytes and neutrophils, providing a possible connection to developmental and hematopoietic sample states. It also has substantial literature and disease associations involving infection and developmental disorders.
- **Conclusion**: Established evidence supports NUP214 as a nuclear-pore component whose co-abundance with NUP85 is biologically credible. Its possible contribution to shared progenitor or immune-cell states is plausible from HPA evidence but remains untested in this module.

#### DDX41

- **Related proteins** (co-abundance neighbors): ARMH3 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_13567.1, huMAP3_09943.1
- **Function (MyGene.info)**: DEAD-box helicase 41. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of the DEAD box protein family …
- **Diseases (Open Targets)**: DDX41-related hematologic malignancy predisposition syndrome (0.801); myelodysplastic syndrome (0.718); acute myeloid leukemia (0.704); myelodysplastic syndrome with excess blasts (0.584); myeloid leukemia (0.556)
- **Europe PMC papers**: 2217
- **Why important**: DDX41 links RNA metabolism with innate immune signaling. It is an RNA helicase associated with mRNA splicing, cell proliferation, differentiation, apoptosis, and cGAS/STING signaling. It appears in hu.MAP complexes (hu.MAP huMAP3_13567.1) and (hu.MAP huMAP3_09943.1), connecting it to TPX2 and THOC1, respectively, although the module does not contain the full complexes. DDX41 has substantial literature and particularly strong disease associations with myeloid malignancy predisposition and acute myeloid leukemia. Its HPA cell-type enhancement in extravillous trophoblasts and esophageal suprabasal cells does not by itself establish a blood origin.
- **Conclusion**: Established evidence supports DDX41 as a biologically important RNA-helicase and innate-immune regulator. Its position may help connect RNA processing, differentiation, and stress or immune signaling, but that integrative role is a hypothesis rather than a demonstrated property of this module.

## Module 15

**Tissue pair**: lung and stem_cells  
**Genes (5)**: ATP1B3, CCDC90B, ERCC2, LSM6, TM9SF1

### Function

No GO or KEGG term passed global correction, and there was no STRING functional enrichment, so the module does not support a single statistically established pathway-level function. Its genes instead suggest a mixed cellular program spanning transcription-coupled DNA repair and RNA polymerase II regulation through ERCC2, pre-mRNA processing and RNA turnover through LSM6, membrane and vesicle localization through TM9SF1, maintenance of plasma-membrane sodium and potassium gradients through ATP1B3, and mitochondrial localization through CCDC90B. The co-abundance pattern is therefore best interpreted as a coordinated cellular-state signal rather than proof of one common biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: all genes are non-secreted according to the HPA summary. All genes have low tissue specificity, and the proteins are detected in lung. The module also has low immune-cell specificity, with no frequent enriched blood-cell category, arguing against a simple blood-cell or plasma-protein contamination explanation. The cell-type annotations are heterogeneous and include reproductive cell types, neural and glial populations, epithelial or progenitor populations, lactotrophs, vascular smooth muscle cells, and monocytes. Thus, shared abundance may reflect broadly distributed cellular machinery or a shared cell-state component rather than a lung-specific lineage program; the absence of matching HPA tissue data for stem cells limits direct tissue comparison.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction or STRING enrichment was reported, so the module is not supported by established STRING interaction connectivity. The only reported complex relationship is huMAP complex (hu.MAP huMAP3_06791.1), which contains TM9SF1 and ATP1B3 among a larger complex whose other members are not in the module. This provides limited support for a known physical or functional neighborhood involving those membrane-associated proteins, but it does not establish that all module genes form one complex. ERCC2, CCDC90B, and LSM6 have no reported huMAP membership in the supplied evidence.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06791.1 (TM9SF1, ATP1B3; 2/31)

### Novelty

A shared lung and stem-cell co-abundance module with this exact gene combination may be a new observation, because the supplied resources show no STRING network and only partial huMAP overlap. However, absence from STRING or huMAP does not prove novelty: co-abundance is a different type of evidence from curated physical interaction, and sparse networks can arise from limited coverage, context dependence, or correlation structure. The defensible conclusion is that the cross-tissue co-abundance pattern is a candidate novel association requiring replication and independent validation, not an established new molecular complex or pathway.

**Hypothesis.** Hypothesis: a shared cellular state in lung and stem-cell samples coordinately changes several broadly expressed maintenance systems, linking ERCC2-dependent genome transcription and repair, LSM6-dependent RNA processing, TM9SF1-associated membrane or lysosomal trafficking, ATP1B3-supported ion-gradient maintenance, and CCDC90B-associated mitochondrial function. ERCC2 is the strongest network-centered integrator in this hypothesis, while the remaining genes may represent parallel responses to cellular stress or biosynthetic demand rather than direct physical partners. This hypothesis should be tested by replication across cohorts, cell-composition adjustment, perturbation of the candidate genes, and measurement of DNA-repair, RNA-splicing, membrane-trafficking, ion-homeostasis, and mitochondrial phenotypes.

### Important genes

#### ERCC2

- **Related proteins** (co-abundance neighbors): CCDC90B (0.88), TM9SF1 (0.83), ATP1B3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ERCC excision repair 2, TFIIH core complex helicase subunit. The nucleotide excision repair pathway is a mechanism to repair damage to DNA. The protein encoded by this gene is involved in transcription-coupled nucleotide excision repair and is an integral member of the basal transcription factor BTF2/TFIIH complex. The gene product has ATP-dependent DNA helicase activity and belongs to the RAD3/XPD subfamily of helicases. Defects in this gene can result in …
- **Diseases (Open Targets)**: xeroderma pigmentosum group D (0.842); trichothiodystrophy 1, photosensitive (0.821); cerebrooculofacioskeletal syndrome 2 (0.788); trichothiodystrophy (0.745); xeroderma pigmentosum (0.698)
- **Europe PMC papers**: 4325
- **Why important**: ERCC2 is the most connected and strongest node in the module. It encodes a TFIIH-associated ATP-dependent helicase involved in transcription-coupled and nucleotide-excision repair and in RNA polymerase II transcriptional regulation. Its disease associations include xeroderma pigmentosum group D, trichothiodystrophy, and cerebrooculofacioskeletal syndrome, and it has extensive literature support. Its central network position makes it the principal candidate for integrating the module, although its links are co-abundance links rather than demonstrated physical interactions.
- **Conclusion**: Established: ERCC2 has a well-supported role in genome repair and transcription and is the module hub. Conclusion: it is the strongest biological anchor for a cellular maintenance or stress interpretation, but the module does not establish that ERCC2 mechanistically controls the other genes.

#### TM9SF1

- **Related proteins** (co-abundance neighbors): ERCC2 (0.83), LSM6 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_06791.1
- **Function (MyGene.info)**: transmembrane 9 superfamily member 1. Predicted to be involved in protein localization to membrane. Predicted to be located in autophagosome membrane; cytoplasmic vesicle; and lysosomal membrane. Predicted to be integral component of membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); breast cancer (0.081); gastric cancer (0.076); acute respiratory distress syndrome (0.074); systemic lupus erythematosus (0.074)
- **Europe PMC papers**: 194
- **Why important**: TM9SF1 connects ERCC2 and LSM6 in the co-abundance graph and is the only gene besides ATP1B3 represented in huMAP complex (hu.MAP huMAP3_06791.1). It is a Golgi-localized transmembrane protein predicted to participate in membrane localization and to occur in autophagosomal, vesicular, and lysosomal membranes. Its literature volume is more limited than that of ERCC2, and reported disease associations include neurodegenerative disease and acute respiratory distress syndrome.
- **Conclusion**: Established: TM9SF1 is a membrane-trafficking candidate with partial complex support from (hu.MAP huMAP3_06791.1). Conclusion: it could connect membrane quality control with the broader cellular-state signal, but a direct relationship to ERCC2 or LSM6 remains a hypothesis.

#### LSM6

- **Related proteins** (co-abundance neighbors): TM9SF1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LSM6 homolog, U6 small nuclear RNA and mRNA degradation associated. Sm-like proteins were identified in a variety of organisms based on sequence homology with the Sm protein family (see SNRPD2; MIM 601061). Sm-like proteins contain the Sm sequence motif, which consists of 2 regions separated by a linker of variable length that folds as a loop. The Sm-like proteins are thought to form a stable heteromer present in tri-snRNP particles, which are important for pre-mR…
- **Diseases (Open Targets)**: neurodegenerative disease (0.560); Alzheimer disease (0.527); lysosomal storage disease (0.526); Parkinson disease (0.526); attention deficit-hyperactivity disorder (0.373)
- **Europe PMC papers**: 414
- **Why important**: LSM6 is linked to TM9SF1 and has a defined role in spliceosomal small nuclear ribonucleoprotein assembly, pre-mRNA splicing, and mRNA decapping or degradation. Its disease-association record includes neurodegenerative and lysosomal-storage conditions, and it has a substantial literature base. It provides an RNA-processing dimension that complements the transcription and repair role of ERCC2.
- **Conclusion**: Established: LSM6 participates in RNA processing and RNA turnover. Conclusion: its co-abundance with TM9SF1 may indicate a shared cellular state affecting RNA and membrane homeostasis, but no direct molecular bridge is demonstrated.

#### ATP1B3

- **Related proteins** (co-abundance neighbors): ERCC2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_06791.1
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit beta 3. The protein encoded by this gene belongs to the family of Na+/K+ and H+/K+ ATPases beta chain proteins, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a vari…
- **Diseases (Open Targets)**: congestive heart failure (0.600); atrial fibrillation (0.595); heart failure (0.578); cardiovascular disorder (0.551); cardiac arrhythmia (0.503)
- **Europe PMC papers**: 805
- **Why important**: ATP1B3 is connected to ERCC2 and is the second module member in huMAP complex (hu.MAP huMAP3_06791.1). As a beta subunit of the sodium and potassium ATPase, it supports plasma-membrane ion gradients, sodium-coupled transport, and electrical or osmotic homeostasis. It has a comparatively substantial literature record and disease associations involving heart failure, atrial fibrillation, and cardiovascular disorders. Its plasma-membrane localization supplies a distinct physiological output for the module.
- **Conclusion**: Established: ATP1B3 is an ion-homeostasis and membrane-transport component with partial huMAP support. Conclusion: it is a plausible readout of cellular energetic or membrane stress, but the co-abundance data do not show that it is regulated by ERCC2.

#### CCDC90B

- **Related proteins** (co-abundance neighbors): ERCC2 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coiled-coil domain containing 90B. Located in mitochondrion. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: refractive error (0.270); smoking initiation (0.249); poisoning (0.236); trauma complication (0.236); placental abruption (0.225)
- **Europe PMC papers**: 129
- **Why important**: CCDC90B is the peripheral module node connected to ERCC2 and is annotated as mitochondrial. It has comparatively sparse functional annotation and a smaller literature base than the other selected genes, which makes it valuable as a less-characterized candidate rather than as an established pathway marker. Its cell-type annotations include germ-cell states and esophageal apical cells, while HPA reports low tissue specificity and lung detection.
- **Conclusion**: Established: CCDC90B is a mitochondrial coiled-coil protein and a peripheral co-abundance partner of ERCC2. Conclusion: it may report mitochondrial involvement in the shared cellular state, but any role in DNA repair, RNA processing, or membrane homeostasis is presently hypothetical.

## Module 16

**Tissue pair**: lung and stem_cells  
**Genes (7)**: ATAD1, FOXRED1, DDOST, PNKP, OXCT1, SMCHD1, TMEM126A

### Function

The module does not support a single statistically established GO or KEGG function: no GO or KEGG term passed global correction, and there were no supplementary STRING enrichment terms. Its gene-level evidence instead suggests a mixed intracellular maintenance program. FOXRED1 and TMEM126A point toward mitochondrial respiratory-chain complex I assembly and mitochondrial protein quality control; OXCT1 supports mitochondrial ketone-body utilization; ATAD1 supports extraction of mislocalized mitochondrial membrane proteins; DDOST supports endoplasmic-reticulum protein N-linked glycosylation; and PNKP and SMCHD1 support DNA repair and chromatin regulation. The sparse co-abundance structure therefore appears more consistent with coordinated cellular proteostasis, energy metabolism, and genome maintenance than with a validated canonical pathway. This interpretation is a hypothesis rather than a globally enriched functional annotation.

**Cell composition.** The module is composed entirely of intracellular proteins, with no secreted genes. HPA evidence indicates that most genes have low tissue specificity and low immune-cell specificity, arguing against a predominantly plasma-protein or blood-cell module. The genes show diverse cell-type associations, including reproductive, epithelial, adrenal, gastric progenitor, plasma-cell, and neutrophil populations, rather than a single shared cell type. SMCHD1 is immune-cell enriched in neutrophils and could reflect a neutrophil-related component, but the remainder of the HPA profile does not support a strong blood-contamination explanation. OXCT1 is tissue enhanced in heart muscle, while the other genes are broadly distributed. Protein detection in lung is mixed, and there is no matching HPA tissue evidence for stem cells, so the shared co-abundance pattern should not be interpreted as evidence that all genes are uniformly expressed in both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was detected among the module genes, and no hu.MAP complex contained multiple module members. Thus, the co-abundance links are not independently supported here by known physical or functional associations in those resources. The apparent network hub is FOXRED1, which connects to OXCT1, PNKP, TMEM126A, and SMCHD1 in the co-abundance graph, while ATAD1 connects to OXCT1 and DDOST. These links may represent coordinated expression, indirect biology, shared cellular state, or technical structure rather than direct molecular binding. The absence of STRING and hu.MAP support limits claims of a pre-existing protein complex but does not invalidate the co-abundance signal.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a new tissue-pair co-abundance observation because the exact module pattern is not supported by the supplied STRING or hu.MAP resources and no established shared complex is evident. However, it cannot be called a definitively novel biological module from resource absence alone. Several component functions are already established, including complex I assembly, ketone-body catabolism, mitochondrial protein dislocation, DNA repair, chromatin regulation, and endoplasmic-reticulum glycosylation. The defensible novelty claim is therefore the coordinated lung–stem-cell co-abundance of this particular combination, not discovery of new functions or new physical interactions.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in which mitochondrial respiratory capacity, mitochondrial protein quality control, nutrient-dependent energy metabolism, endoplasmic-reticulum protein maturation, and DNA or chromatin repair are co-regulated in lung and stem-cell samples. FOXRED1 and TMEM126A may form the mitochondrial respiratory-quality-control axis, with OXCT1 and ATAD1 representing metabolic and membrane-proteostasis components, while PNKP, SMCHD1, and DDOST capture genome-maintenance and protein-maturation demands. This model predicts coordinated changes in mitochondrial function, proteotoxic stress handling, and DNA damage responses, but the current evidence does not establish direct molecular coupling or causality.

### Important genes

#### FOXRED1

- **Related proteins** (co-abundance neighbors): OXCT1 (0.86), PNKP (0.84), TMEM126A (0.83), SMCHD1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FAD dependent oxidoreductase domain containing 1. This gene encodes a protein that contains a FAD-dependent oxidoreductase domain. The encoded protein is localized to the mitochondria and may function as a chaperone protein required for the function of mitochondrial complex I. Mutations in this gene are associated with mitochondrial complex I deficiency. Alternatively spliced transcript variants have been observed for this gene. [provided by RefS…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.783); mitochondrial complex I deficiency, nuclear type 19 (0.741); Leigh syndrome (0.662); mitochondrial disease (0.646); mitochondrial complex I deficiency, nuclear type 1 (0.630)
- **Europe PMC papers**: 308
- **Why important**: FOXRED1 has the strongest network position and connects the mitochondrial, DNA-repair, and chromatin-associated portions of the module. Its established role as a mitochondrial FAD-dependent oxidoreductase and proposed complex I chaperone is directly relevant to the mitochondrial annotations of TMEM126A. It is associated with mitochondrial complex I deficiency and Leigh syndrome and has a substantial literature base.
- **Conclusion**: Established evidence supports FOXRED1 as the leading candidate for a mitochondrial respiratory-chain component of the module. Its hub position suggests a coordinating role in the co-abundance pattern, but it does not prove that FOXRED1 physically regulates the other genes.

#### TMEM126A

- **Related proteins** (co-abundance neighbors): FOXRED1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transmembrane protein 126A. The protein encoded by this gene is a mitochondrial membrane protein of unknown function. Defects in this gene are a cause of optic atrophy type 7 (OPA7). Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2011].
- **Diseases (Open Targets)**: autosomal recessive optic atrophy, OPA7 type (0.710); autosomal recessive optic atrophy (0.464); optic atrophy (0.439); Leber hereditary optic neuropathy (0.375); hereditary optic atrophy (0.375)
- **Europe PMC papers**: 278
- **Why important**: TMEM126A is directly connected to FOXRED1 in the module and has annotations for mitochondrial inner-membrane protein insertion, complex I assembly, and mitochondrial protein quality control. Its disease associations with optic atrophy provide strong biological evidence that mitochondrial dysfunction is clinically relevant. Its literature volume is more limited than that of the major repair genes, making the module context particularly informative.
- **Conclusion**: Established evidence supports TMEM126A as a mitochondrial assembly or quality-control component that reinforces the FOXRED1-centered interpretation. Its participation in this shared module is plausible, but the co-abundance data do not establish a new TMEM126A interaction.

#### OXCT1

- **Related proteins** (co-abundance neighbors): FOXRED1 (0.86), ATAD1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3-oxoacid CoA-transferase 1. This gene encodes a member of the 3-oxoacid CoA-transferase gene family. The encoded protein is a homodimeric mitochondrial matrix enzyme that plays a central role in extrahepatic ketone body catabolism by catalyzing the reversible transfer of coenzyme A from succinyl-CoA to acetoacetate. Mutations in this gene are associated with succinyl CoA:3-oxoacid CoA transferase deficiency. [provided by Ref…
- **Diseases (Open Targets)**: succinyl-CoA:3-ketoacid CoA transferase deficiency (0.827); mitochondrial disease (0.370); neurodegenerative disease (0.355); supraventricular ectopy (0.268); Ketonuria (0.242)
- **Europe PMC papers**: 1212
- **Why important**: OXCT1 is a network connector between FOXRED1 and ATAD1 and encodes the mitochondrial enzyme responsible for extrahepatic ketone-body catabolism. Its heart-muscle tissue enhancement and association with a defined metabolic deficiency make it the clearest metabolic component of the module. It also has a comparatively extensive literature base.
- **Conclusion**: Established evidence supports OXCT1 as an energy-metabolism component and a plausible link between mitochondrial respiratory function and nutrient utilization. Its network position supports coordination with the mitochondrial genes, but it remains uncertain whether this reflects a shared metabolic state or direct regulation.

#### ATAD1

- **Related proteins** (co-abundance neighbors): DDOST (0.83), OXCT1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoli rim; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase family AAA domain containing 1. Predicted to enable ATP binding activity and transmembrane protein dislocase activity. Involved in extraction of mislocalized protein from mitochondrial outer membrane. Located in mitochondrial outer membrane and peroxisomal membrane. Implicated in hyperekplexia 4. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hyperekplexia 4 (0.637); hereditary hyperekplexia (0.596); neurodegenerative disease (0.503); spondyloepimetaphyseal dysplasia, PAPSS2 type (0.486); placenta praevia (0.215)
- **Europe PMC papers**: 345
- **Why important**: ATAD1 connects OXCT1 with DDOST and has an established role in extracting mislocalized proteins from the mitochondrial outer membrane, with an additional peroxisomal-membrane location. Its connection to both a mitochondrial metabolic gene and an endoplasmic-reticulum glycosylation gene makes it informative for a broader proteostasis interpretation. It also has disease associations involving hyperekplexia and a moderate literature base.
- **Conclusion**: Established evidence supports ATAD1 as a membrane-proteostasis component that could connect mitochondrial quality control with broader protein handling. Its bridging position is suggestive, but the module does not demonstrate that ATAD1 mechanistically links OXCT1 and DDOST.

#### PNKP

- **Related proteins** (co-abundance neighbors): FOXRED1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polynucleotide kinase 3'-phosphatase. This locus represents a gene involved in DNA repair. In response to ionizing radiation or oxidative damage, the protein encoded by this locus catalyzes 5' phosphorylation and 3' dephosphorylation of nucleic acids. Mutations at this locus have been associated with microcephaly, seizures, and developmental delay.[provided by RefSeq, Sep 2010].
- **Diseases (Open Targets)**: Ataxia-oculomotor apraxia type 4 (0.802); microcephaly, seizures, and developmental delay (0.800); genetic developmental and epileptic encephalopathy (0.710); spinocerebellar ataxia, autosomal recessive, with axonal neuropathy 2 (0.652); Charcot-Marie-Tooth disease type 2B2 (0.618)
- **Europe PMC papers**: 2922
- **Why important**: PNKP is connected to the FOXRED1 hub and encodes a DNA-end processing enzyme involved in single-strand break repair, base-excision repair, and repair after oxidative damage. Its strong disease associations with neurodevelopmental and ataxia syndromes and its extensive literature make it an important genome-maintenance marker. Its presence broadens the module beyond metabolism.
- **Conclusion**: Established evidence supports PNKP as a DNA-repair component whose inclusion may indicate a cellular state involving oxidative or replication-associated stress. The link to the mitochondrial portion is a hypothesis based on co-abundance and shared stress biology, not an established direct interaction.

#### SMCHD1

- **Related proteins** (co-abundance neighbors): FOXRED1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enriched; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: structural maintenance of chromosomes flexible hinge domain containing 1. This gene encodes a protein which contains a hinge region domain found in members of the SMC (structural maintenance of chromosomes) protein family. [provided by RefSeq, Dec 2011].
- **Diseases (Open Targets)**: facioscapulohumeral muscular dystrophy 2 (0.806); arhinia, choanal atresia, and microphthalmia (0.775); facioscapulohumeral muscular dystrophy (0.764); Hyposmia - nasal and ocular hypoplasia - hypogonadotropic hypogonadism (0.689); Arrhinia - choanal atresia - microphthalmia (0.666)
- **Europe PMC papers**: 1156
- **Why important**: SMCHD1 is connected to FOXRED1 and is annotated for chromosome organization, X-chromosome inactivation, and DNA-repair regulation. HPA identifies it as immune-cell enriched in neutrophils, making it important for evaluating whether a cell-composition signal contributes to the module. Its associations with facioscapulohumeral muscular dystrophy and developmental craniofacial disorders, together with substantial literature, make it biologically consequential despite its peripheral network position.
- **Conclusion**: Established evidence supports SMCHD1 as a chromatin and genome-regulation component and raises the possibility of a neutrophil-related contribution in some samples. Its relationship to the mitochondrial genes is not established; the co-abundance link may reflect cellular state or composition rather than shared molecular machinery.

## Module 17

**Tissue pair**: lung and stem_cells  
**Genes (30)**: ATRX, BECN1, DGKA, DOCK11, ERCC1, FRYL, H1-2, H1-4, HYCC1, IDH3A, KIF2A, KNTC1, MGST1, MYOF, NAA35, NEDD1, NIF3L1, URB1, PANK4, PRPF39, GINS1, RBM7, POLR2A, STEEP1, SUCLA2, TRMT6, XIAP, XPO6, ZC3HAV1, ZMYM3

### Function

This is a heterogeneous co-abundance module rather than a module with a demonstrated single pathway function. No GO or KEGG term passed global correction, so the annotations cannot support a statistically established pathway assignment. The gene-level evidence spans apoptosis and autophagy through XIAP and BECN1, mitotic microtubule activity through KIF2A and KNTC1, DNA repair through ERCC1, and mitochondrial energy metabolism through SUCLA2. These themes may reflect coordinated cellular state, proliferation, stress handling, or mixed cell composition rather than one biochemical process. The module is therefore best interpreted as a potentially shared lung and stem-cell cellular-state module with several connected functional axes, not as a validated pathway-enrichment module.

**Cell composition.** The module contains no secreted genes, arguing against a plasma-protein or secretome explanation. HPA indicates broadly distributed expression for most genes, with many showing low tissue specificity and low immune-cell specificity. At the same time, the tissue and single-cell annotations repeatedly point toward bone marrow, lymphoid tissue, hematopoietic progenitors, megakaryocytic or erythroid progenitors, neutrophil-related cells, and other specialized cell types. This pattern raises the possibility that the shared signal partly reflects hematopoietic or other shared-cell contributions in the samples, although it is not uniformly blood-cell enriched. Protein detection in lung is widespread among the annotated genes, whereas HPA has no matching stem-cell tissue for direct protein comparison. The module should therefore not be described as lung-specific or stem-cell-specific.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The high-confidence STRING evidence is sparse and consists of the listed BECN1–XIAP, H1-2–H1-4, and IDH3A–SUCLA2 relationships. These links support a few biologically plausible local connections: apoptosis or autophagy-related regulation, linker-histone association, and mitochondrial tricarboxylic-acid-cycle coupling. Most co-abundance edges do not have a corresponding high-confidence STRING interaction, so the network is not simply a reconstruction of known physical interactions. hu.MAP provides repeated support for KNTC1 and XPO6 appearing together in complexes (hu.MAP huMAP3_08298.1), (hu.MAP huMAP3_09114.1), (hu.MAP huMAP3_10202.1), (hu.MAP huMAP3_10287.1), and (hu.MAP huMAP3_11232.1), and for ATRX and ZMYM3 appearing together in (hu.MAP huMAP3_11539.1). H1-4 and ZC3HAV1 occur together in (hu.MAP huMAP3_05807.1). However, each listed complex contains only a small subset of this module, so the complex evidence supports local substructures rather than one unified complex. Overall, STRING and hu.MAP indicate several known relationships embedded within a largely unconnected co-abundance pattern.

**STRING interactions (score >= 0.7)**: 3 of 435 gene pairs: BECN1–XIAP (0.867); H1-2–H1-4 (0.826); IDH3A–SUCLA2 (0.972)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08298.1 (KNTC1, XPO6; 2/24); huMAP3_09114.1 (KNTC1, XPO6; 2/30); huMAP3_11539.1 (ATRX, ZMYM3; 2/32); huMAP3_10202.1 (KNTC1, XPO6; 2/52); huMAP3_10287.1 (KNTC1, XPO6; 2/53); huMAP3_11232.1 (KNTC1, XPO6; 2/78); huMAP3_05807.1 (H1-4, ZC3HAV1; 2/81)

### Novelty

The module should be regarded as a potentially novel cross-tissue co-abundance pattern, but not as a proven new biological complex or pathway. Its novelty is supported by the unusual combination of apoptosis or autophagy, mitosis, chromatin, RNA processing, mitochondrial metabolism, membrane trafficking, and immune-associated genes, together with the sparse STRING interaction coverage and the fact that hu.MAP support is limited to small subsets. Nevertheless, absence from STRING or hu.MAP alone does not establish discovery: co-abundance can arise from shared cell composition, common regulation, technical effects, or indirect cellular state. A credible novelty claim would require replication in independent lung and stem-cell datasets, preservation after cell-composition adjustment, and experimental or perturbational validation.

**Hypothesis.** Hypothesis: this module may represent a shared proliferative and stress-adaptation state in lung-associated and stem-cell-associated samples. In this model, KIF2A and KNTC1 mark mitotic and chromosome-segregation demands; ERCC1 and chromatin-associated genes support genome maintenance; XIAP and BECN1 balance survival, apoptosis, autophagy, and stress responses; and SUCLA2 with IDH3A supports mitochondrial metabolic capacity. The observed co-abundance could therefore arise when cells require simultaneous genome protection, cell-cycle control, organelle metabolism, and survival signaling. An alternative hypothesis is that the pattern is driven partly by shared hematopoietic or progenitor-cell contamination or representation, given the HPA annotations. These are hypotheses rather than conclusions from enrichment, because no GO or KEGG term achieved global significance.

### Important genes

#### XIAP

- **Related proteins** (co-abundance neighbors): H1-2 (0.90), KIF2A (0.88), PRPF39 (0.84), ATRX (0.83), ZC3HAV1 (0.82); STRING partners: BECN1 (0.867)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: X-linked inhibitor of apoptosis. This gene encodes a protein that belongs to a family of apoptotic suppressor proteins. Members of this family share a conserved motif termed, baculovirus IAP repeat, which is necessary for their anti-apoptotic function. This protein functions through binding to tumor necrosis factor receptor-associated factors TRAF1 and TRAF2 and inhibits apoptosis induced by menadione, a potent inducer of free ra…
- **Diseases (Open Targets)**: X-linked lymphoproliferative syndrome (0.814); neurodegenerative disease (0.556); inflammatory bowel disease (0.478); hereditary disease (0.469); Splenomegaly (0.464)
- **Europe PMC papers**: 16708
- **Why important**: XIAP has a central position in the co-abundance network and connects to BECN1, KIF2A, ATRX, ZC3HAV1, and PRPF39. Its established anti-apoptotic function provides a plausible survival-related anchor for a module that also contains autophagy, DNA-damage, and antiviral genes. It has extensive literature and disease associations including X-linked lymphoproliferative syndrome, inflammatory bowel disease, splenomegaly, and neurodegenerative disease.
- **Conclusion**: Established evidence supports XIAP as an apoptosis and inflammatory-signaling regulator and as an important network hub. It is plausible, but not demonstrated, that XIAP coordinates the other module processes in lung or stem cells; the co-abundance pattern alone does not establish such regulation.

#### BECN1

- **Related proteins** (co-abundance neighbors): NEDD1 (0.91), HYCC1 (0.86), SUCLA2 (0.82), KIF2A (0.81); STRING partners: XIAP (0.867)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: beclin 1. This gene encodes a protein that regulates autophagy, a catabolic process of degradation induced by starvation. The encoded protein is a component of the phosphatidylinositol-3-kinase (PI3K) complex which mediates vesicle-trafficking processes. This protein is thought to play a role in multiple cellular processes, including tumorigenesis, neurodegeneration and apoptosis. Alternative splicing resul…
- **Diseases (Open Targets)**: neurodegenerative disease (0.552); COVID-19 (0.482); dengue disease (0.380); severe acute respiratory syndrome (0.371); lysosomal storage disease (0.284)
- **Europe PMC papers**: 17940
- **Why important**: BECN1 is a highly connected module gene linked to NEDD1, HYCC1, SUCLA2, KIF2A, and XIAP. Its established role in autophagosome assembly, mitophagy, lysosomal targeting, and hypoxia response makes it a strong candidate for connecting cellular stress handling with mitochondrial and cytoskeletal processes. It has extensive literature and disease associations including neurodegenerative disease, viral disease, and lysosomal storage disease.
- **Conclusion**: Established evidence identifies BECN1 as an autophagy and vesicle-trafficking regulator with relevance to cellular stress. A role for BECN1 in coupling autophagy to the other module branches is a reasonable hypothesis, but it is not shown by the absence of globally significant enrichment.

#### KIF2A

- **Related proteins** (co-abundance neighbors): XIAP (0.88), STEEP1 (0.86), BECN1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Centrosome, Basal body, Annulus; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 2A. The protein encoded by this gene is a plus end-directed motor required for normal mitotic progression. The encoded protein is required for normal spindle activity during mitosis and is necessary for normal brain development. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2011].
- **Diseases (Open Targets)**: Genetic central nervous system malformation (0.749); neurodegenerative disease (0.403); ovarian neoplasm (0.342); diabetes mellitus (0.307); major depressive disorder (0.302)
- **Europe PMC papers**: 1206
- **Why important**: KIF2A occupies a central local position linking XIAP, STEEP1, and BECN1. Its established function in mitotic spindle activity, microtubule depolymerization, chromosome segregation, and cell migration gives the module a direct cell-cycle and cytoskeletal component. It has disease associations involving central nervous system malformation, neurodegenerative disease, ovarian neoplasm, and diabetes.
- **Conclusion**: Established evidence supports KIF2A as a mitotic microtubule motor and regulator of cell division. Its co-abundance with survival and autophagy genes may indicate a coordinated proliferative state, but that interpretation remains a hypothesis.

#### ERCC1

- **Related proteins** (co-abundance neighbors): KNTC1 (0.87), GINS1 (0.85), PANK4 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ERCC excision repair 1, endonuclease non-catalytic subunit. The product of this gene functions in the nucleotide excision repair pathway, and is required for the repair of DNA lesions such as those induced by UV light or formed by electrophilic compounds including cisplatin. The encoded protein forms a heterodimer with the XPF endonuclease (also known as ERCC4), and the heterodimeric endonuclease catalyzes the 5' incision in the process of excising the DNA…
- **Diseases (Open Targets)**: COFS syndrome (0.745); Cockayne syndrome (0.648); liver disorder (0.535); kidney failure (0.535); hepatorenal syndrome (0.534)
- **Europe PMC papers**: 8981
- **Why important**: ERCC1 links KNTC1, GINS1, and PANK4, placing DNA repair near genes involved in chromosome segregation and replication. It is an established component of nucleotide-excision repair and also participates in recombinational and other DNA-repair processes. Its disease associations include Cockayne syndrome, cerebro-oculo-facio-skeletal syndrome, liver disorder, and kidney failure, and it has substantial literature.
- **Conclusion**: Established evidence supports ERCC1 as a genome-maintenance factor. Its network placement is consistent with a module involving replication and chromosome integrity, but it does not prove that DNA repair is the dominant function of the whole module.

#### SUCLA2

- **Related proteins** (co-abundance neighbors): MYOF (0.82), BECN1 (0.82), IDH3A (0.81); STRING partners: IDH3A (0.972)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase ADP-forming subunit beta. Succinyl-CoA synthetase (SCS) is a mitochondrial matrix enzyme that acts as a heterodimer, being composed of an invariant alpha subunit and a substrate-specific beta subunit. The protein encoded by this gene is an ATP-specific SCS beta subunit that dimerizes with the SCS alpha subunit to form SCS-A, an essential component of the tricarboxylic acid cycle. SCS-A hydrolyzes ATP to convert succinate t…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome, encephalomyopathic form with methylmalonic aciduria (0.816); mitochondrial DNA depletion syndrome, encephalomyopathic form (0.581); neurodegenerative disease (0.485); mitochondrial disease (0.374); disease of peritoneum (0.372)
- **Europe PMC papers**: 1440
- **Why important**: SUCLA2 connects MYOF, BECN1, and IDH3A, creating a local mitochondrial-metabolic bridge between the autophagy-related and energy-metabolism portions of the network. It is an established ATP-specific succinyl-CoA synthetase subunit in the tricarboxylic acid cycle and is associated with mitochondrial DNA depletion syndromes, mitochondrial disease, and neurodegenerative disease. Its direct STRING relationship with IDH3A is especially consistent with a known mitochondrial metabolic neighborhood.
- **Conclusion**: Established evidence supports SUCLA2 as a mitochondrial energy-metabolism component with important disease relevance. The proposed connection between mitochondrial metabolism and autophagy in this module is biologically plausible, but the module data do not establish causal metabolic coupling.

#### KNTC1

- **Related proteins** (co-abundance neighbors): ERCC1 (0.87), NAA35 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_08298.1, huMAP3_09114.1, huMAP3_10202.1, huMAP3_10287.1, huMAP3_11232.1
- **Function (MyGene.info)**: kinetochore associated 1. This gene encodes a protein that is one of many involved in mechanisms to ensure proper chromosome segregation during cell division. Experimental evidence indicated that the encoded protein functioned in a similar manner to that of the Drosophila rough deal protein. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.314); osteoarthritis, knee (0.278); osteoarthritis (0.264); preeclampsia (0.178); total knee arthroplasty (0.148)
- **Europe PMC papers**: 576
- **Why important**: KNTC1 is connected to ERCC1 and NAA35 in the module and repeatedly appears with XPO6 in hu.MAP complexes (hu.MAP huMAP3_08298.1), (hu.MAP huMAP3_09114.1), (hu.MAP huMAP3_10202.1), (hu.MAP huMAP3_10287.1), and (hu.MAP huMAP3_11232.1). Its established role in kinetochore assembly, spindle-checkpoint signaling, chromosome segregation, and mitotic exit makes it a strong indicator of cell-division control. HPA also associates it with bone marrow and several hematopoietic progenitor populations, which is relevant to the possible cell-composition explanation.
- **Conclusion**: Established evidence supports KNTC1 as a mitotic chromosome-segregation factor and as part of recurring complex-level relationships with XPO6. Its presence may reflect proliferative progenitor cells, a true shared cell-cycle state, or both; distinguishing these explanations requires cell-composition-aware replication.

## Module 18

**Tissue pair**: lung and stem_cells  
**Genes (6)**: BLOC1S5, NCDN, NXN, PAK2, PSMC6, SNX2

### Function

The module does not support a single established pathway-level function. No GO or KEGG term passed global correction, and there were no supplementary STRING enrichment terms. Its network is a hub-and-spoke structure centered on BLOC1S5, with PSMC6, NCDN, NXN, SNX2, and PAK2 each connected to that hub but not to one another. The annotations suggest several related cellular themes rather than one confirmed process: vesicle and endosomal trafficking through BLOC1S5 and SNX2, neuronal projection and synaptic regulation through BLOC1S5 and NCDN, redox and Wnt regulation through NXN, proteasomal proteostasis through PSMC6, and cytoskeletal or signaling regulation through PAK2. These annotations are hypothesis-generating rather than enrichment-based evidence. The most defensible interpretation is a co-abundance pattern involving intracellular trafficking and vesicle-associated biology, potentially combined with cell-state, differentiation, or tissue-composition effects.

**Cell composition.** This is not a plasma-protein or secreted-protein module: no member is annotated as secreted. It is also not broadly blood-cell dominated. Most members have low tissue specificity and low immune-cell specificity, while one member is immune-cell enhanced in memory and naive B cells and another is not detected in immune cells. The HPA profile is mixed: one gene is tissue enriched in brain, one is tissue enhanced in skeletal muscle, and all members show some cell-type enhancement, including neuronal, alveolar, endothelial, trophoblast, B-cell, and neutrophil populations. Five proteins are detected in lung, whereas NCDN is not detected there by immunohistochemistry. There is no matching HPA tissue category for stem_cells. Therefore, the shared module is more consistent with a mixed intracellular program or shared cell-state composition than with a circulating protein signal. The neuronal and muscle associations also warrant caution about interpreting the module as lung-specific.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and no supplementary STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated here by known high-confidence physical or functional interactions, and the module should not be presented as an established protein complex. The absence of STRING or hu.MAP support does not invalidate the co-abundance pattern; it indicates that the observed coordination may reflect regulation at the transcript or protein-abundance level, shared cell composition, indirect biology, or interactions not represented in those resources.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a new cross-tissue co-abundance association, because the particular grouping is not supported by the supplied STRING or hu.MAP evidence. However, it cannot be called a new biological complex or definitively novel mechanism. Several component functions and disease links are already established, and the lack of database support alone is not proof of novelty. A stronger novelty claim would require replication in independent lung and stem-cell datasets, control for cell-type composition, testing of the edge reproducibility, and experimental validation of coordinated regulation or physical interaction.

**Hypothesis.** Hypothesis: a shared intracellular trafficking and stress-adaptation state coordinates BLOC1S5 with endosomal sorting, redox/Wnt regulation, proteasomal turnover, neuronal or differentiation-associated processes, and cytoskeletal signaling across lung and stem-cell samples. BLOC1S5 may act as the central abundance marker of this state, while NXN, SNX2, PSMC6, NCDN, and PAK2 report different downstream aspects of vesicle handling, redox control, proteostasis, cell differentiation, and signaling. This remains a hypothesis because there is no globally significant GO or KEGG term, no STRING enrichment, no high-confidence STRING interaction among the members, and no multi-member hu.MAP complex.

### Important genes

#### BLOC1S5

- **Related proteins** (co-abundance neighbors): PSMC6 (0.90), NCDN (0.90), NXN (0.86), SNX2 (0.84), PAK2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biogenesis of lysosomal organelles complex 1 subunit 5. This gene encodes a component of BLOC-1 (biogenesis of lysosome-related organelles complex 1). Components of this complex are involved in the biogenesis of organelles such as melanosomes and platelet-dense granules. A mouse model for Hermansky-Pudlak Syndrome is mutated in the murine version of this gene. Alternative splicing results in multiple transcript variants. Read-through transcription exis…
- **Diseases (Open Targets)**: Hermansky-Pudlak syndrome 11 (0.662); Hermansky-Pudlak syndrome (0.461); lysosomal storage disease (0.451); Alzheimer disease (0.451); Parkinson disease (0.451)
- **Europe PMC papers**: 173
- **Why important**: BLOC1S5 is the network hub, directly connected to every other member in the module. Its established role as a component of BLOC-one and in lysosome-related organelle biogenesis provides the clearest mechanistic anchor for the module, with links to vesicle-mediated transport, melanosome organization, and anterograde axonal transport. It is detected in lung, has vesicle localization, and has disease associations including Hermansky-Pudlak syndrome and lysosomal storage disease. Its literature volume is substantial relative to several other members.
- **Conclusion**: Established: BLOC1S5 is the central co-abundance node and has a documented role in organelle and vesicle biogenesis. Hypothesis: it may be the principal coordinator or marker of the shared module state. The network does not establish that it directly regulates the other members.

#### SNX2

- **Related proteins** (co-abundance neighbors): BLOC1S5 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sorting nexin 2. This gene belongs to the sorting nexin family whose members contain the phosphoinositide-binding phox (PX) domain. The encoded protein is a component of the retromer complex which plays a role in protein sorting in the endocytic pathway. This protein may form oligomeric complexes with other family members. Alternate splicing results in multiple transcript variants of this gene. Pseudogenes associa…
- **Diseases (Open Targets)**: diverticular disease (0.368); anxiety (0.364); chronic obstructive pulmonary disease (0.362); malnutrition (0.315); migraine disorder (0.311)
- **Europe PMC papers**: 852
- **Why important**: SNX2 is directly linked to the hub and is an endosomal protein that participates in retromer-associated intracellular and retrograde transport. It is detected in lung and is immune-cell enhanced in memory and naive B cells, making it informative for both trafficking biology and possible sample-composition effects. It has a substantial literature base and a disease association with chronic obstructive pulmonary disease among other conditions.
- **Conclusion**: Established: SNX2 has a documented role in endosomal protein sorting and transport, and its abundance is coordinated with BLOC1S5 in this module. Hypothesis: SNX2 may connect the module to receptor recycling or endosomal remodeling in lung or stem-cell-associated cells. The data do not show that B-cell abundance caused the module.

#### NXN

- **Related proteins** (co-abundance neighbors): BLOC1S5 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoredoxin. This gene encodes a member of the thioredoxin superfamily, a group of small, multifunctional redox-active proteins. Members of this family are characterized by a conserved active motif called the thioredoxin fold that catalyzes disulfide bond formation and isomerization. The encoded protein acts a redox-dependent regulator of the Wnt signaling pathway and is involved in cell growth and differentia…
- **Diseases (Open Targets)**: robinow syndrome, autosomal recessive 2 (0.607); Robinow syndrome (0.599); colorectal cancer (0.400); autosomal recessive Robinow syndrome (0.381); polyp of colon (0.341)
- **Europe PMC papers**: 1006
- **Why important**: NXN is directly connected to the hub and encodes a thioredoxin-superfamily redox regulator. Its documented functions include Wnt regulation, cellular oxidant detoxification, protein-ubiquitination regulation, and growth or differentiation processes. It is tissue enhanced in skeletal muscle, detected in lung, absent from immune-cell detection, and has a large literature volume. Its disease associations include Robinow syndrome and colorectal cancer.
- **Conclusion**: Established: NXN is a redox and signaling regulator with relevance to Wnt biology and differentiation. Hypothesis: NXN may provide a redox-sensitive link between trafficking, differentiation, and cellular stress in the shared module. The co-abundance data do not establish Wnt pathway activation.

#### NCDN

- **Related proteins** (co-abundance neighbors): BLOC1S5 (0.90); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neurochondrin. This gene encodes a leucine-rich cytoplasmic protein, which is highly similar to a mouse protein that negatively regulates Ca/calmodulin-dependent protein kinase II phosphorylation and may be essential for spatial learning processes. Several alternatively spliced transcript variants of this gene have been described. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodevelopmental disorder with infantile epileptic spasms (0.670); epilepsy (0.430); Intellectual disability (0.416); autosomal recessive non-syndromic intellectual disability (0.370); neurodegenerative disease (0.212)
- **Europe PMC papers**: 301
- **Why important**: NCDN is directly connected to the hub and is tissue enriched in brain, with cell-type enhancement across neuronal populations. Its documented functions include neuron projection development, synaptic plasticity regulation, and postsynaptic neurotransmitter receptor internalization. It has disease associations involving epilepsy, neurodevelopmental disorders, and intellectual disability, together with a substantial literature base. Its lack of lung immunohistochemical detection makes it particularly relevant when considering cell composition or indirect co-abundance.
- **Conclusion**: Established: NCDN is associated with neuronal cytoplasmic and synaptic biology and is coordinated with BLOC1S5 in the module. Hypothesis: NCDN may mark a shared differentiation or vesicle-trafficking state rather than contribute a lung-specific neuronal function. This interpretation requires independent cell-composition analysis.

#### PAK2

- **Related proteins** (co-abundance neighbors): BLOC1S5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: p21 (RAC1) activated kinase 2. The p21 activated kinases (PAK) are critical effectors that link Rho GTPases to cytoskeleton reorganization and nuclear signaling. The PAK proteins are a family of serine/threonine kinases that serve as targets for the small GTP binding proteins, CDC42 and RAC1, and have been implicated in a wide range of biological activities. The protein encoded by this gene is activated by proteolytic cleavage …
- **Diseases (Open Targets)**: Knobloch syndrome 2 (0.525); Knobloch syndrome (0.454); HIV infectious disease (0.370); atrial fibrillation (0.210); ovarian carcinoma (0.175)
- **Europe PMC papers**: 3704
- **Why important**: PAK2 is directly connected to the hub and is a serine-threonine kinase activated by RAC1 and CDC42. Its established functions include cytoskeletal reorganization, nuclear signaling, protein phosphorylation, cell migration, and apoptosis-related regulation. It is detected in lung, shows neutrophil cell-type enhancement, has extensive literature coverage among the module members, and has disease associations spanning vascular, infectious, and neoplastic conditions.
- **Conclusion**: Established: PAK2 is a signaling kinase with roles in cytoskeletal dynamics, migration, and stress or apoptotic responses. Hypothesis: PAK2 may translate the shared module state into changes in cell shape, motility, or survival. The module does not demonstrate PAK2 activation or a direct interaction with BLOC1S5.

## Module 19

**Tissue pair**: lung and stem_cells  
**Genes (11)**: BOP1, CCDC86, CDC73, DDX21, DDX56, ADAR, MYBBP1A, NOL11, NUP42, RIOX2, UTP15

### Function

The module is strongly characterized as a nucleolar ribosome-biogenesis and ribonucleoprotein-processing program. The primary evidence is the globally corrected enrichment for ribonucleoprotein complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.000132), positive regulation and transcription by RNA polymerase I (GO:BP positive regulation of transcription by RNA polymerase I; q_global = 0.000352) (GO:BP regulation of transcription by RNA polymerase I; q_global = 0.000748) (GO:BP transcription by RNA polymerase I; q_global = 0.00771), ribosome biogenesis (GO:BP ribosome biogenesis; q_global = 0.000389), the nucleolus (GO:CC nucleolus; q_global = 0.000533), rRNA processing and rRNA metabolism (GO:BP rRNA processing; q_global = 0.0224) (GO:BP rRNA metabolic process; q_global = 0.0361), nuclear protein-containing complexes (GO:CC nuclear protein-containing complex; q_global = 0.0277), and RNA binding (GO:MF RNA binding; q_global = 0.0392). The convergence of these independent biological-process, cellular-component, and molecular-function terms supports a coherent interpretation rather than a term-specific annotation artifact. The genes span small-subunit and large-subunit ribosome maturation, rRNA processing, nucleolar transcriptional regulation, RNA helicase activity, RNA editing, and nucleocytoplasmic transport. STRING enrichment is concordant but supplementary; its ribosome-biogenesis, rRNA-processing, nucleolar, and preribosome results reinforce the primary GO interpretation without being treated as global significance.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It is also not blood-cell enriched, because every gene has low immune-cell specificity and no enriched blood-cell category is reported. Most genes have low tissue specificity, consistent with a broadly expressed, housekeeping-like nucleolar program. Some cell-type-enhanced signals occur in epithelial, germ-cell, muscle, cardiomyocyte, oligodendrocyte-progenitor, and neutrophil categories, but they do not establish a blood-derived explanation. The shared lung and stem-cell signal therefore more plausibly reflects a conserved cellular growth, RNA-production, and ribosome-assembly state, while variation in the relevant cell populations remains a possible contributor.

**GO/KEGG enrichment**: 10 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP ribonucleoprotein complex biogenesis | 0.000132 | ADAR, BOP1, DDX21, DDX56, MYBBP1A, NOL11, RIOX2, UTP15 |
| GO:BP positive regulation of transcription by RNA polymerase I | 0.000352 | DDX21, MYBBP1A, NOL11, UTP15 |
| GO:BP ribosome biogenesis | 0.000389 | BOP1, DDX21, DDX56, MYBBP1A, NOL11, RIOX2, UTP15 |
| GO:CC nucleolus | 0.000533 | ADAR, BOP1, CCDC86, DDX21, DDX56, MYBBP1A, NOL11, RIOX2, UTP15 |
| GO:BP regulation of transcription by RNA polymerase I | 0.000748 | DDX21, MYBBP1A, NOL11, UTP15 |
| GO:BP transcription by RNA polymerase I | 0.00771 | DDX21, MYBBP1A, NOL11, UTP15 |
| GO:BP rRNA processing | 0.0224 | BOP1, DDX21, DDX56, NOL11, UTP15 |
| GO:CC nuclear protein-containing complex | 0.0277 | ADAR, BOP1, CDC73, DDX21, MYBBP1A, NOL11, NUP42, UTP15 |
| GO:BP rRNA metabolic process | 0.0361 | BOP1, DDX21, DDX56, NOL11, UTP15 |
| GO:MF RNA binding | 0.0392 | ADAR, BOP1, CCDC86, DDX21, DDX56, MYBBP1A, NOL11, NUP42, UTP15 |

### STRING and hu.MAP

The strongest known STRING relationships connect BOP1 with DDX21, DDX56, MYBBP1A, and UTP15; connect DDX21 with MYBBP1A; connect DDX56 with MYBBP1A; connect MYBBP1A with UTP15; and connect NOL11 with UTP15. These links form a recognizable nucleolar ribosome-biogenesis core within the co-abundance graph and support biological coherence, although STRING relationships can reflect transferred or functionally inferred evidence rather than direct physical interaction. The hu.MAP evidence independently places UTP15 and NOL11 together in a t-UTP-associated complex (hu.MAP huMAP3_01743.1) and in a broader RNA-processing and exosome-associated complex (hu.MAP huMAP3_14264.1). The fact that only these shared members are represented in those complexes, while several other module genes lack matching hu.MAP complexes, suggests a module combining a known core with additional functionally coordinated nucleolar factors rather than a fully resolved single complex.

**STRING interactions (score >= 0.7)**: 8 of 55 gene pairs: BOP1–DDX21 (0.838); BOP1–DDX56 (0.963); BOP1–MYBBP1A (0.915); BOP1–UTP15 (0.797); DDX21–MYBBP1A (0.963); DDX56–MYBBP1A (0.838); MYBBP1A–UTP15 (0.784); NOL11–UTP15 (0.986)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Ribosome biogenesis (FDR = 1.62e-06, 6 genes); Process Ribonucleoprotein complex biogenesis (FDR = 2.28e-06, 9 genes); COMPARTMENTS Nucleolus (FDR = 7.24e-06, 9 genes); Keyword rRNA processing (FDR = 9.23e-05, 5 genes); Component Nucleolus (FDR = 0.00012, 9 genes); Process Ribosome biogenesis (FDR = 0.00021, 7 genes); Process Positive regulation of transcription by RNA polymerase I (FDR = 0.00037, 4 genes); COMPARTMENTS Nuclear lumen (FDR = 0.00039, 10 genes); Keyword Nucleus (FDR = 0.0033, 11 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 0.0142, 5 genes); Process rRNA processing (FDR = 0.017, 5 genes); Process ncRNA processing (FDR = 0.017, 6 genes); Component Nuclear lumen (FDR = 0.0225, 11 genes); COMPARTMENTS Nucleus (FDR = 0.0228, 11 genes); COMPARTMENTS B-WICH complex (FDR = 0.0228, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01743.1 (UTP15, NOL11; 2/6); huMAP3_14264.1 (UTP15, NOL11; 2/20)

### Novelty

The functional theme itself is not a new biological discovery: ribosome biogenesis, nucleolar localization, rRNA processing, and several pairwise relationships are already supported by GO, STRING, hu.MAP, and the gene-specific annotations. The potentially novel result is the conserved co-abundance configuration observed across lung and stem_cells, particularly the coordinated inclusion of the t-UTP-associated genes with nucleolar helicases, ribosome-assembly factors, RNA-editing machinery, and nuclear transport components. However, the fact sheet does not provide an external co-abundance comparison, perturbation experiment, or independent replication, so this should be described as a potentially novel systems-level association rather than a proven new complex or mechanism. Absence of hu.MAP or STRING evidence for some edges is not evidence of novelty.

**Hypothesis.** Mechanistic hypothesis: this module represents a shared nucleolar biosynthetic state in which increased demand for ribosome production coordinates rRNA transcription, processing, and assembly with RNA remodeling and quality control. UTP15 and NOL11 may provide a t-UTP-associated small-subunit maturation axis, while BOP1 supports large-subunit maturation, DDX21 and DDX56 remodel structured RNA, and MYBBP1A couples nucleolar transcriptional regulation to ribosome production. ADAR and NUP42 may connect this core to RNA-editing and nucleocytoplasmic transport. In lung and stem-cell populations, this coordinated state could support proliferation, differentiation, or tissue maintenance; this is a hypothesis requiring perturbation and cell-composition-aware validation, not an established causal mechanism.

### Important genes

#### UTP15

- **Related proteins** (co-abundance neighbors): MYBBP1A (0.85), DDX56 (0.83), ADAR (0.82), RIOX2 (0.82), BOP1 (0.81); STRING partners: BOP1 (0.797), MYBBP1A (0.784), NOL11 (0.986)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_01743.1, huMAP3_14264.1
- **Function (MyGene.info)**: UTP15 small subunit processome component. Enables RNA binding activity. Involved in positive regulation of rRNA processing and positive regulation of transcription by RNA polymerase I. Located in endoplasmic reticulum and fibrillar center. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.354); Parkinson disease (0.251); Alzheimer disease (0.251); lysosomal storage disease (0.251); male reproductive organ cancer (0.114)
- **Europe PMC papers**: 234
- **Why important**: UTP15 has the most central network position in the module, with the greatest connectivity and links to MYBBP1A, DDX56, ADAR, RIOX2, and BOP1. It appears in every globally significant GO term (10 globally significant GO/KEGG terms, q_global 0.000132–0.0392; see the table), is linked by STRING to the ribosome-biogenesis core, and is present in both hu.MAP complexes (hu.MAP huMAP3_01743.1) (hu.MAP huMAP3_14264.1). Its annotation as a small-subunit processome component, RNA-binding factor, and regulator of rRNA processing makes it a strong integrative marker of the module. Its disease-associated evidence is broad and its literature volume is substantial, supporting biological relevance while also indicating that the gene is not an unstudied candidate.
- **Conclusion**: Established evidence supports UTP15 as a central small-subunit ribosome-biogenesis and rRNA-processing component that anchors the module. It is a strong candidate for a driver or sensitive readout of the shared nucleolar state, but causality in lung or stem_cells is not established.

#### NOL11

- **Related proteins** (co-abundance neighbors): DDX56 (0.85); STRING partners: UTP15 (0.986)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_01743.1, huMAP3_14264.1
- **Function (MyGene.info)**: nucleolar protein 11. Enables RNA binding activity. Involved in maturation of SSU-rRNA and positive regulation of transcription of nucleolar large rRNA by RNA polymerase I. Located in nucleolus. Part of t-UTP complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: diabetes mellitus (0.100); type 2 diabetes mellitus (0.100); atrial fibrillation (0.087); ulcerative colitis (0.011); cancer (0.011)
- **Europe PMC papers**: 240
- **Why important**: NOL11 participates in every globally significant GO term (10 globally significant GO/KEGG terms, q_global 0.000132–0.0392; see the table), is linked very strongly to UTP15 in STRING, and is represented with UTP15 in both hu.MAP complexes (hu.MAP huMAP3_01743.1) (hu.MAP huMAP3_14264.1). Its annotation places it in the nucleolus, the t-UTP complex, small-subunit rRNA maturation, and positive regulation of nucleolar large-rRNA transcription. Although its direct co-abundance connectivity is limited, its functional specificity and complex evidence make it an important biochemical anchor.
- **Conclusion**: Established evidence identifies NOL11 as a nucleolar RNA-binding and rRNA-maturation factor connected to the t-UTP-associated core. Its coordinated abundance with UTP15 is mechanistically plausible, but the module does not by itself demonstrate that NOL11 controls the entire program.

#### DDX21

- **Related proteins** (co-abundance neighbors): NUP42 (0.89), MYBBP1A (0.82); STRING partners: BOP1 (0.838), MYBBP1A (0.963)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 has broad representation across all globally significant GO terms (10 globally significant GO/KEGG terms, q_global 0.000132–0.0392; see the table) and connects the module to both MYBBP1A and BOP1 through STRING evidence. It is a nucleolar-rim RNA helicase associated with RNA-structure remodeling, ribosome and spliceosome assembly, transcriptional regulation, and cell-growth-related processes. It also has the largest literature volume among the module's nucleolar core factors and has disease associations spanning neurodegenerative and cancer-related categories.
- **Conclusion**: Established evidence supports DDX21 as an RNA-remodeling and nucleolar regulatory factor that could coordinate rRNA processing with transcriptional control. Its network placement makes it a plausible integrator, but whether it is causal for the cross-tissue co-abundance pattern remains untested.

#### BOP1

- **Related proteins** (co-abundance neighbors): UTP15 (0.81); STRING partners: DDX21 (0.838), DDX56 (0.963), MYBBP1A (0.915), UTP15 (0.797)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BOP1 ribosomal biogenesis factor. Enables RNA binding activity. Involved in regulation of cell cycle; regulation of signal transduction by p53 class mediator; and ribosomal large subunit biogenesis. Located in chromosome; nucleolus; and nucleoplasm. Part of PeBoW complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.318); cancer (0.090); neoplasm (0.087); polycystic ovary syndrome (0.082); colorectal carcinoma (0.078)
- **Europe PMC papers**: 1064
- **Why important**: BOP1 is connected in STRING to DDX21, DDX56, MYBBP1A, and UTP15 and is represented in the primary ribosome-biogenesis and nucleolar terms (7 globally significant GO/KEGG terms, q_global 0.000132–0.0392; see the table). Its annotation as a PeBoW-complex component and large-subunit maturation factor supplies a complementary large-subunit axis to the UTP15-NOL11 small-subunit axis. It also has extensive literature and disease-related associations, and its HPA profile includes tissue and cell-type enhancement without immune-cell specificity.
- **Conclusion**: Established evidence supports BOP1 as a large-subunit ribosome-assembly factor that helps explain why the module spans multiple stages of ribosome production. Its co-abundance with small-subunit and RNA-helicase factors suggests coordinated assembly demand, but does not prove direct physical cooperation among all module members.

#### ADAR

- **Related proteins** (co-abundance neighbors): UTP15 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR contributes to the globally significant ribonucleoprotein-biogenesis, nucleolar, nuclear-complex, and RNA-binding terms (4 globally significant GO/KEGG terms, q_global 0.000132–0.0392; see the table). Unlike the core ribosome-assembly genes, it provides a distinct RNA-editing and double-stranded-RNA remodeling function and is annotated in RNA processing, nucleocytoplasmic transport, and antiviral response. Its very extensive literature and strong disease associations, including inherited interferonopathy-related conditions, make it biologically important even though it has only a single high-confidence module edge.
- **Conclusion**: Established evidence supports ADAR as an RNA-editing enzyme that is coordinated with the nucleolar program in this module. Its inclusion may reflect broader RNA-processing or stress-state coupling rather than a canonical ribosome-biogenesis complex; that interpretation is a hypothesis requiring experimental testing.

## Module 20

**Tissue pair**: lung and stem_cells  
**Genes (29)**: CCNT1, CHORDC1, CMC2, CSTB, DCUN1D5, FKBP4, GEMIN5, GET3, HIP1, KIF3A, METAP2, MED30, MICALL1, MYCBP, NELFA, NUP98, PDCL3, PIH1D1, PSME3IP1, PPIL1, CAD, RBM10, DPF2, SMARCE1, SUPT16H, TLE3, XRN2, ZCCHC8, ZGPAT

### Function

The module is best interpreted as a nuclear gene-regulatory and RNA-processing module. The primary global evidence supports molecular adaptor activity and protein-macromolecule adaptor activity (GO:MF molecular adaptor activity; q_global = 0.0309) (GO:MF protein-macromolecule adaptor activity; q_global = 0.049), together with DNA-templated transcription (GO:BP DNA-templated transcription; q_global = 0.0362). Its genes include transcriptional elongation and pausing factors such as CCNT1, NELFA and SUPT16H; chromatin-remodeling factors such as DPF2 and SMARCE1; transcriptional regulatory proteins such as MED30, TLE3 and ZGPAT; RNA-processing factors such as RBM10, GEMIN5, XRN2 and ZCCHC8; and nuclear transport or assembly factors such as NUP98 and PIH1D1. The STRING supplementary terms for the nucleus, nuclear lumen and transcription regulation (4 supplementary STRING terms; within-query FDR 0.0064–0.0153) are concordant, but remain supplementary rather than primary evidence. No KEGG-specific term was supplied. Overall, the module appears to represent coordinated regulation of transcription, chromatin accessibility, RNA maturation and macromolecular assembly rather than a tissue-specific metabolic pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the fact sheet reports no secreted genes. It is also not predominantly blood-cell enriched. Most genes have low tissue specificity and low immune-cell specificity, although selected genes show enrichment in neutrophils, basophils, erythrocyte progenitors or other cell types. The broad expression pattern and nuclear or cytosolic localization are more consistent with broadly used cellular machinery or a shared cell-state program than with a specialized lung secretory program. HPA protein detection in lung is frequent among the tested genes, while there is no matching HPA tissue category for stem cells. The cell-type enrichments involving reproductive, esophageal, neural and marrow populations suggest that some co-abundance may reflect shared cell states or general regulatory activity, but they do not by themselves establish blood contamination or a specific contaminating cell population.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF molecular adaptor activity | 0.0309 | CCNT1, DPF2, FKBP4, HIP1, MED30, MICALL1, MYCBP, NELFA, NUP98, PIH1D1, SMARCE1, TLE3 |
| GO:BP DNA-templated transcription | 0.0362 | CCNT1, DPF2, FKBP4, MED30, MYCBP, NELFA, NUP98, PIH1D1, PPIL1, RBM10, SMARCE1, SUPT16H, TLE3, XRN2, ZGPAT |
| GO:MF protein-macromolecule adaptor activity | 0.049 | CCNT1, DPF2, FKBP4, HIP1, MED30, MICALL1, MYCBP, NUP98, PIH1D1, SMARCE1, TLE3 |

### STRING and hu.MAP

Known physical or functional support is limited but informative. STRING reports a high-confidence CCNT1–NELFA relationship, a very high-confidence DPF2–SMARCE1 relationship, and a further PPIL1–PSME3IP1 relationship. These links independently support transcriptional elongation, chromatin remodeling and RNA or protein-processing components within the module, but they account for only a small part of the module and do not establish one complete physical complex. hu.MAP provides stronger complex-level context for DPF2 and SMARCE1 as members of related SWI/SNF or BAF chromatin-remodeling assemblies (hu.MAP huMAP3_11470.1) (hu.MAP huMAP3_03221.1). ZGPAT and GEMIN5 occur together in large spliceosome or snRNP-associated complexes (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_08980.1), although each complex contains many members outside the module. Thus, the network combines several known functional assemblies rather than representing a single fully resolved complex. The co-abundance structure may therefore capture coordinated activity across interacting nuclear systems, while the sparse STRING connectivity cautions against claiming direct physical interaction among most module members.

**STRING interactions (score >= 0.7)**: 3 of 406 gene pairs: CCNT1–NELFA (0.939); DPF2–SMARCE1 (0.999); PPIL1–PSME3IP1 (0.804)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Nucleus (FDR = 0.0064, 24 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0115, 16 genes); Keyword Nucleus (FDR = 0.0153, 22 genes); Keyword Transcription regulation (FDR = 0.0153, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11470.1 (DPF2, SMARCE1; 2/27); huMAP3_03221.1 (DPF2, SMARCE1; 2/28); huMAP3_06511.1 (ZGPAT, GEMIN5; 2/79); huMAP3_08980.1 (ZGPAT, GEMIN5; 2/97)

### Novelty

The module should not be called a newly discovered molecular complex. Several of its relationships and functional groupings are already established by STRING and hu.MAP, and the broad transcription, chromatin and RNA-processing functions are well known. At the same time, the specific conserved co-abundance pattern shared by lung and stem_cells may represent a new systems-level observation because the supplied evidence does not identify a prior study of this exact module or tissue pair. Absence from STRING or hu.MAP is not evidence of novelty; it mainly indicates that many within-module co-abundance relationships are not curated as physical interactions. A defensible novelty claim is therefore limited to the integrated co-abundance association and its conservation across the two tissue groups, which would require independent cohorts, cell-composition controls and perturbation or time-course validation.

**Hypothesis.** Hypothesis: this module coordinates a permissive nuclear state in which chromatin remodeling, transcriptional elongation, RNA processing and nucleocytoplasmic transport are coupled to support cell maintenance or state transitions shared between lung and stem-cell populations. DPF2–SMARCE1 may provide chromatin-remodeling context, CCNT1–NELFA may couple transcriptional elongation with pausing control, and NUP98, GEMIN5, RBM10, XRN2 and ZCCHC8 may connect transcription to RNA export, maturation and turnover. PIH1D1 may help organize protein complexes or pre-ribosomal and snoRNP-related processes. This model predicts coordinated changes in nascent transcription, chromatin accessibility and RNA-processing outputs when the module is perturbed, but the co-abundance data alone do not establish directionality, causality or a single shared complex.

### Important genes

#### CCNT1

- **Related proteins** (co-abundance neighbors): XRN2 (0.81), MYCBP (0.81), ZCCHC8 (0.81), PDCL3 (0.81), PPIL1 (0.80); STRING partners: NELFA (0.939)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cyclin T1. This gene encodes a member of the highly conserved cyclin C subfamily. The encoded protein tightly associates with cyclin-dependent kinase 9, and is a major subunit of positive transcription elongation factor b (p-TEFb). In humans, there are multiple forms of positive transcription elongation factor b, which may include one of several different cyclins along with cyclin-dependent kinase 9. The com…
- **Diseases (Open Targets)**: HIV infectious disease (0.595); neurodegenerative disease (0.370); acute myeloid leukemia (0.226); Insulin resistance (0.076); congenital fibrosis of the extraocular muscles (0.054)
- **Europe PMC papers**: 870
- **Why important**: CCNT1 is a central regulatory anchor in the module’s transcriptional interpretation: it participates in all primary enriched terms (GO:MF molecular adaptor activity; q_global = 0.0309) (GO:BP DNA-templated transcription; q_global = 0.0362) (GO:MF protein-macromolecule adaptor activity; q_global = 0.049), is connected to several module genes, and has the strongest curated STRING relationship in the module through NELFA. Its established role as cyclin T1 in positive transcription elongation and its substantial literature and disease-association record make it a strong candidate for linking module abundance to transcriptional output.
- **Conclusion**: Established evidence supports CCNT1 as a transcriptional-elongation regulator and a plausible network anchor. The hypothesis that its abundance drives the coordinated lung–stem-cell module remains untested; co-abundance does not show that CCNT1 is the upstream regulator.

#### DPF2

- **Related proteins** (co-abundance neighbors): PDCL3 (0.86), CAD (0.84), ZGPAT (0.82), CMC2 (0.80); STRING partners: SMARCE1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_11470.1, huMAP3_03221.1
- **Function (MyGene.info)**: double PHD fingers 2. The protein encoded by this gene is a member of the d4 domain family, characterized by a zinc finger-like structural motif. This protein functions as a transcription factor which is necessary for the apoptotic response following deprivation of survival factors. It likely serves a regulatory role in rapid hematopoietic cell growth and turnover. This gene is considered a candidate gene for multiple …
- **Diseases (Open Targets)**: Coffin-Siris syndrome (0.774); neurodegenerative disease (0.552); hereditary disease (0.468); Intellectual disability (0.371); lysosomal storage disease (0.370)
- **Europe PMC papers**: 835
- **Why important**: DPF2 is included in every primary enriched term (GO:MF molecular adaptor activity; q_global = 0.0309) (GO:BP DNA-templated transcription; q_global = 0.0362) (GO:MF protein-macromolecule adaptor activity; q_global = 0.049), occupies a relatively connected position in the module, and has a very high-confidence STRING relationship with SMARCE1. It is also the module’s clearest link to the SWI/SNF or BAF chromatin-remodeling complexes represented by hu.MAP (hu.MAP huMAP3_11470.1) (hu.MAP huMAP3_03221.1). Its established roles in chromatin remodeling, transcriptional regulation and apoptosis, together with strong disease associations, give it substantial mechanistic importance.
- **Conclusion**: Established evidence supports DPF2 as a chromatin-associated transcriptional regulator and as part of known remodeling complexes. It is reasonable to hypothesize that DPF2 helps explain the module’s shared regulatory state, but the module does not prove that DPF2 mediates the cross-tissue conservation.

#### SMARCE1

- **Related proteins** (co-abundance neighbors): PIH1D1 (0.83), MICALL1 (0.82); STRING partners: DPF2 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_11470.1, huMAP3_03221.1
- **Function (MyGene.info)**: SWI/SNF related BAF chromatin remodeling complex subunit E1. The protein encoded by this gene is part of the large ATP-dependent chromatin remodeling complex SWI/SNF, which is required for transcriptional activation of genes normally repressed by chromatin. The encoded protein, either alone or when in the SWI/SNF complex, can bind to 4-way junction DNA, which is thought to mimic the topology of DNA as it enters or exits the nucleosome. The protein contains …
- **Diseases (Open Targets)**: familial meningioma (0.750); Coffin-Siris syndrome (0.748); hereditary neoplastic syndrome (0.550); neurodegenerative disease (0.526); meningioma (0.521)
- **Europe PMC papers**: 1702
- **Why important**: SMARCE1 is present in every primary enriched term (GO:MF molecular adaptor activity; q_global = 0.0309) (GO:BP DNA-templated transcription; q_global = 0.0362) (GO:MF protein-macromolecule adaptor activity; q_global = 0.049), is linked to DPF2 by the strongest STRING relationship in the module, and is represented with DPF2 in related hu.MAP chromatin-remodeling complexes (hu.MAP huMAP3_11470.1) (hu.MAP huMAP3_03221.1). Its HMG-domain-containing SWI/SNF-associated function and strong disease literature make it an important structural and regulatory counterpart to DPF2.
- **Conclusion**: Established evidence supports SMARCE1 as a chromatin-remodeling and transcriptional regulator with a known relationship to DPF2. A coordinated DPF2–SMARCE1 contribution to the module is plausible, but the co-abundance graph cannot determine whether their complex is active in both tissue groups.

#### NUP98

- **Related proteins** (co-abundance neighbors): CMC2 (0.87), GEMIN5 (0.83), PIH1D1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 98 and 96 precursor. Nuclear pore complexes (NPCs) regulate the transport of macromolecules between the nucleus and cytoplasm, and are composed of many polypeptide subunits, many of which belong to the nucleoporin family. This gene belongs to the nucleoporin gene family and encodes a 186 kDa precursor protein that undergoes autoproteolytic cleavage to generate a 98 kDa nucleoporin and 96 kDa nucleoporin. The 98 kDa nu…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); acute myeloid leukemia (0.399); lung carcinoma (0.376)
- **Europe PMC papers**: 4839
- **Why important**: NUP98 has a comparatively connected position and bridges CMC2, GEMIN5 and PIH1D1 in the module. It occurs in all primary enriched terms (GO:MF molecular adaptor activity; q_global = 0.0309) (GO:BP DNA-templated transcription; q_global = 0.0362) (GO:MF protein-macromolecule adaptor activity; q_global = 0.049) and is consistent with the supplementary nuclear and transcription-regulation evidence (4 supplementary STRING terms; within-query FDR 0.0064–0.0153). Its established functions in nuclear pore organization, RNA export, protein import and transcriptional tethering provide a mechanistic connection between nuclear transport and gene regulation. It also has extensive literature and disease associations, including lung and hematologic relevance.
- **Conclusion**: Established evidence supports NUP98 as a nuclear transport and gene-regulatory factor. Its module position suggests a possible bridge between transcriptional machinery and RNA or protein trafficking, but that bridging role is a hypothesis rather than a demonstrated physical interaction.

#### PIH1D1

- **Related proteins** (co-abundance neighbors): DCUN1D5 (0.86), SMARCE1 (0.83), MED30 (0.83), NUP98 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PIH1 domain containing 1. Enables several functions, including RNA polymerase I core promoter sequence-specific DNA binding activity; enzyme binding activity; and phosphoprotein binding activity. Involved in several processes, including box C/D snoRNP assembly; positive regulation of signal transduction; and regulation of cellular protein metabolic process. Located in cytoplasm and nucleolus. Part of R2TP complex and pre-s…
- **Diseases (Open Targets)**: neurodegenerative disease (0.437); mood disorder (0.059); depressive disorder (0.043); mental disorder (0.032); breast cancer (0.022)
- **Europe PMC papers**: 285
- **Why important**: PIH1D1 is present in every primary enriched term (GO:MF molecular adaptor activity; q_global = 0.0309) (GO:BP DNA-templated transcription; q_global = 0.0362) (GO:MF protein-macromolecule adaptor activity; q_global = 0.049) and connects DCUN1D5, SMARCE1, MED30 and NUP98 in the co-abundance network. Its established participation in the R2TP and pre-snoRNP systems, together with roles in snoRNP assembly, rRNA processing, protein stabilization and chromatin-related processes, makes it a candidate organizer connecting transcriptional and RNA-processing functions. Its disease and literature record is meaningful while remaining less extensive than that of the best-studied module members.
- **Conclusion**: Established evidence supports PIH1D1 as a protein-complex and RNA-biogenesis regulator. Its network position supports a hypothesis that it coordinates nuclear assembly processes with chromatin or transcriptional machinery, but this proposed integration has not been demonstrated by the supplied data.

## Module 21

**Tissue pair**: lung and stem_cells  
**Genes (5)**: FHL2, NIP7, PPP6R3, DARS1, TAB2

### Function

The module does not have a globally significant GO or KEGG annotation: no globally significant GO/KEGG term passed global correction. Its organization is therefore more informative than pathway enrichment. TAB2 is the central connector in the observed co-abundance subgraph, linking FHL2, NIP7, and DARS1, while NIP7 also links to PPP6R3. The gene annotations suggest a mixed module rather than a single established pathway: TAB2 supports MAP3K7/TAK1-linked inflammatory and NF-kappaB/MAPK signaling; FHL2 is associated with LIM-domain, focal-adhesion, transcriptional, apoptotic, and cardiac-development functions; NIP7 supports nucleolar pre-rRNA processing and ribosomal large-subunit biogenesis; PPP6R3 regulates signal-transduction phosphatase activity; and DARS1 supports translation through aspartyl-tRNA aminoacylation. These annotations support a tentative connection among inflammatory signaling, cell-structural or developmental state, signal-transduction control, and cellular protein-production capacity, but they do not establish one coherent pathway. The absence of enriched GO/KEGG terms is not evidence that the module is false.

**Cell composition.** All module genes have HPA protein detection in lung, and none is annotated as secreted. Most have low tissue specificity and low immune-cell specificity, while one gene, FHL2, is tissue-group enriched and is associated with several specialized cell types, including cardiomyocytes, ciliated cells, trophoblast populations, and Leydig cells. TAB2 shows cell-type enhancement in microglia and neutrophils, and NIP7 shows enhancement in esophageal basal and gastric progenitor cells. The HPA profile does not support a plasma-protein or broadly blood-cell-derived module. It is more consistent with intracellular proteins expressed across tissues, with possible contributions from shared or specialized cell states. Because HPA has no matching stem-cell tissue entry, the stem-cell interpretation is limited by unequal tissue reference coverage.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported for any possible gene pair, and no supplementary STRING functional-enrichment term was reported. No hu.MAP complex contained multiple module members. Thus the co-abundance relationships are not corroborated here by known physical or functional interaction resources. The lack of database support argues against calling this an established molecular complex, but it does not negate coordinated expression or prove that the relationships are novel biological interactions.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a previously unrecognized co-abundance pattern, because the module has no reported STRING interaction support, no multi-member hu.MAP complex, and no globally significant GO or KEGG term. However, those absences alone do not establish a new biological mechanism. The genes individually have substantial prior annotation and literature, especially TAB2 and FHL2, so the likely novelty is the particular cross-functional co-abundance relationship in lung and stem-cell samples rather than discovery of unknown genes or functions. The available web search identified broad lung regeneration and stem-cell literature, but not a publication establishing this exact five-gene module; this is suggestive rather than definitive evidence of novelty.

**Hypothesis.** Hypothesis: the module reflects a coordinated intracellular state in which TAB2-linked inflammatory or stress-responsive signaling is coupled to FHL2-associated adhesion and developmental regulation, while PPP6R3 tunes signal-transduction phosphatase activity and NIP7 plus DARS1 maintain the ribosome and translation capacity needed for cell-state change or repair. In lung, this could arise from shared activation or remodeling states among epithelial, stromal, or immune-associated cells, and its apparent conservation in stem cells could reflect a general cellular transition program rather than a lung-specific pathway. This hypothesis requires validation by independent cohorts, cell-resolved data, perturbation experiments, and direct testing of the predicted regulatory relationships.

### Important genes

#### TAB2

- **Related proteins** (co-abundance neighbors): FHL2 (0.83), NIP7 (0.82), DARS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TGF-beta activated kinase 1 (MAP3K7) binding protein 2. The protein encoded by this gene is an activator of MAP3K7/TAK1, which is required for for the IL-1 induced activation of nuclear factor kappaB and MAPK8/JNK. This protein forms a kinase complex with TRAF6, MAP3K7 and TAB1, and it thus serves as an adaptor that links MAP3K7 and TRAF6. This protein, along with TAB1 and MAP3K7, also participates in the signal transduction induced by TNFSF11/RANKl th…
- **Diseases (Open Targets)**: congenital heart defects, multiple types, 2 (0.704); congenital heart malformation (0.555); hereditary disease (0.509); chromosome 6q24-q25 deletion syndrome (0.462); autoimmune disorder of central nervous system (0.391)
- **Europe PMC papers**: 3951
- **Why important**: TAB2 is the central network connector in the module and links the signaling-associated branch to FHL2, NIP7, and DARS1. Its established role as a MAP3K7/TAK1 adaptor connecting TRAF6 to inflammatory NF-kappaB and JNK signaling gives it the strongest mechanistic bridge between the module and stress, cytokine, or tissue-injury responses. It also has extensive literature and disease links involving congenital heart abnormalities and immune or inflammatory biology.
- **Conclusion**: Established evidence supports TAB2 as an inflammatory signal-transduction adaptor and as the most plausible organizing gene in this co-abundance pattern. It is a reasonable mechanistic anchor, but the module does not establish that TAB2 directly regulates the other members.

#### FHL2

- **Related proteins** (co-abundance neighbors): TAB2 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Actin filaments, Focal adhesion sites; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: four and a half LIM domains 2. This gene encodes a member of the four-and-a-half-LIM-only protein family. Family members contain two highly conserved, tandemly arranged, zinc finger domains with four highly conserved cysteines binding a zinc atom in each zinc finger. This protein is thought to have a role in the assembly of extracellular membranes. Also, this gene is down-regulated during transformation of normal myoblasts to r…
- **Diseases (Open Targets)**: familial isolated dilated cardiomyopathy (0.372); alcohol drinking (0.367); seasonal allergic rhinitis (0.307); stroke disorder (0.240); poisoning (0.215)
- **Europe PMC papers**: 2785
- **Why important**: FHL2 is directly connected to TAB2 and is the most distinctive HPA composition signal in the module, with tissue enrichment in heart muscle and ovary and enhancement across several specialized cell types. Its focal-adhesion and actin-associated localization, cardiac-development annotations, transcriptional effects, and links to cardiomyopathy make it relevant to structural remodeling and differentiated cell state. Its substantial literature volume supports a well-established biological context.
- **Conclusion**: Established evidence supports FHL2 as a context-dependent structural and transcriptional regulator with developmental and cardiac relevance. Its co-abundance with TAB2 may indicate coordinated remodeling or cell-state signaling, but a direct TAB2-FHL2 pathway is a hypothesis rather than a demonstrated relationship here.

#### NIP7

- **Related proteins** (co-abundance neighbors): TAB2 (0.82), PPP6R3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleolar pre-rRNA processing protein NIP7. Enables RNA binding activity. Predicted to be involved in ribosomal large subunit biogenesis. Located in cytosol; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.471); COG8-congenital disorder of glycosylation (0.118); liposarcoma (0.035); arthropathy (0.023); chronic obstructive pulmonary disease (0.021)
- **Europe PMC papers**: 392
- **Why important**: NIP7 occupies the bridge position between TAB2 and PPP6R3 in the observed subgraph. It is annotated to nucleolar pre-rRNA processing and ribosomal large-subunit biogenesis, providing a plausible link from signaling or cell-state change to biosynthetic capacity. Its nucleolar localization and enhancement in progenitor-like gastrointestinal cell types are relevant to proliferative or regenerative states, although its literature volume is much smaller than that of TAB2 or FHL2.
- **Conclusion**: Established evidence supports NIP7 as a ribosome-biogenesis factor. Its placement in this module suggests a possible coupling of signal state to protein-production capacity, but there is no enrichment or interaction evidence demonstrating that role in lung or stem cells.

#### PPP6R3

- **Related proteins** (co-abundance neighbors): NIP7 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase 6 regulatory subunit 3. Protein phosphatase regulatory subunits, such as SAPS3, modulate the activity of protein phosphatase catalytic subunits by restricting substrate specificity, recruiting substrates, and determining the intracellular localization of the holoenzyme. SAPS3 is a regulatory subunit for the protein phosphatase-6 catalytic subunit (PPP6C; MIM 612725) (Stefansson and Brautigan, 2006 [PubMed 16769727]).[sup…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.383); hair color (0.341); bone fracture (0.253); Pathologic fracture (0.190); obesity disorder (0.185)
- **Europe PMC papers**: 243
- **Why important**: PPP6R3 is connected to NIP7 and encodes a regulatory subunit of protein phosphatase six, which can influence substrate selection and intracellular localization of the phosphatase holoenzyme. Its annotation to regulation of signal transduction makes it a plausible modulator of the signaling branch, while its nucleoplasmic, plasma-membrane, and cytosolic locations are compatible with broad intracellular regulation. Its disease and literature support are more limited than those for TAB2 and FHL2.
- **Conclusion**: Established evidence supports PPP6R3 as a signal-transduction phosphatase regulator. Within this module it may provide signal damping or context control, but the co-abundance data do not identify its substrates or prove functional coupling to NIP7.

#### DARS1

- **Related proteins** (co-abundance neighbors): TAB2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 1. This gene encodes a member of a multienzyme complex that functions in mediating the attachment of amino acids to their cognate tRNAs. The encoded protein ligates L-aspartate to tRNA(Asp). Mutations in this gene have been found in patients showing hypomyelination with brainstem and spinal cord involvement and leg spasticity. Alternative splicing results in multiple transcript variants. [provided by…
- **Diseases (Open Targets)**: hypomyelination with brain stem and spinal cord involvement and leg spasticity (0.773); atrial fibrillation (0.268); Abnormal brain morphology (0.266); tooth hard tissue disease (0.226); Pancreatic pseudocyst (0.225)
- **Europe PMC papers**: 238
- **Why important**: DARS1 is connected to TAB2 and supplies a clear translation-related function through aspartyl-tRNA aminoacylation. Its role in protein synthesis and protein-containing complex assembly could support the increased biosynthetic demands of activated, differentiating, or repairing cells. Its disease association with hypomyelination and spasticity demonstrates functional importance, although its literature volume is comparatively limited and no module-level annotation supports a specific lung mechanism.
- **Conclusion**: Established evidence supports DARS1 as an essential translation factor with neurological disease relevance. In this module it is best interpreted as a possible indicator of biosynthetic state, not as evidence that the module is a translation pathway.

## Module 22

**Tissue pair**: lung and stem_cells  
**Genes (5)**: GOLPH3L, MAPK14, MYLK, P3H3, RAPH1

### Function

No GO or KEGG term passed global multiple-testing correction, and there was no supplementary STRING enrichment; therefore the module does not have a statistically established pathway assignment from enrichment analysis. Its gene annotations and topology instead suggest a possible interface between actin-dependent cell mechanics, smooth-muscle or nonmuscle contractility, Golgi trafficking, extracellular-matrix collagen processing, and stress or inflammatory signaling. RAPH1 and MYLK connect through the module network, while GOLPH3L links RAPH1 to MAPK14 and MYLK links to P3H3. These co-abundance relationships support a coordinated cellular-state interpretation, not proof of direct biochemical interaction.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: only P3H3 has intracellular-and-membrane secretome annotation, and the other genes are not annotated as secreted. The module is also not uniformly immune-cell enriched. MYLK is enhanced in basophils and neutrophils, MAPK14 is enriched in monocyte and neutrophil progenitor states and in basophils and neutrophils, whereas RAPH1 and P3H3 are not detected in immune cells and GOLPH3L has low immune-cell specificity. HPA tissue patterns are mixed, including smooth muscle, liver, seminal vesicle, and low-specificity expression, with cell-type enrichment in several unrelated cell populations. Thus, blood contamination or shared immune cells could contribute to part of the lung signal, especially for MYLK and MAPK14, but the module is not adequately described as a blood-cell module. HPA protein detection supports lung detection for RAPH1, MAPK14, and P3H3, while MYLK was not detected in lung and there is no matching HPA stem-cell tissue.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. Consequently, the co-abundance edges are not corroborated here by known high-confidence physical interactions or a shared annotated complex. The absence of STRING and hu.MAP support means the network may capture coordinated expression, indirect regulation, cell composition, or context-specific biology rather than a stable molecular complex. It does not by itself invalidate the module or prove that the relationships are biologically novel.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a context-specific co-abundance pattern because it combines genes from cytoskeletal regulation, Golgi trafficking, collagen processing, and MAPK signaling without a globally enriched GO or KEGG term, and it has no corroborating high-confidence STRING interaction or hu.MAP complex. However, these observations are insufficient to call it a new biological mechanism: the constituent genes and their functions are already established, and lack of database representation can reflect incomplete coverage, tissue context, indirect regulation, or limited power. The defensible conclusion is that the specific lung and stem-cell co-abundance configuration is a candidate novel observation requiring replication and independent validation, not that the underlying biology is newly discovered.

**Hypothesis.** Hypothesis: the module reflects a shared structural and stress-responsive cellular state in which RAPH1-associated actin remodeling and MYLK-dependent contractility are coordinated with GOLPH3L-dependent Golgi trafficking, P3H3-linked collagen maturation, and MAPK14 stress or inflammatory signaling. In lung, this could arise from a mixture of structural or smooth-muscle-related cells and immune-associated cells; in stem-cell samples, it could reflect a comparable differentiation, adhesion, matrix-remodeling, or stress state. This is a mechanistic hypothesis rather than an established pathway assignment, because enrichment, STRING, and complex evidence do not independently support it.

### Important genes

#### MYLK

- **Related proteins** (co-abundance neighbors): RAPH1 (0.82), P3H3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin light chain kinase. This gene, a muscle member of the immunoglobulin gene superfamily, encodes myosin light chain kinase which is a calcium/calmodulin dependent enzyme. This kinase phosphorylates myosin regulatory light chains to facilitate myosin interaction with actin filaments to produce contractile activity. This gene encodes both smooth muscle and nonmuscle isoforms. In addition, using a separate promoter in an …
- **Diseases (Open Targets)**: aortic aneurysm, familial thoracic 7 (0.767); familial thoracic aortic aneurysm and aortic dissection (0.710); megacystis-microcolon-intestinal hypoperistalsis syndrome 1 (0.617); megacystis-microcolon-intestinal hypoperistalsis syndrome (0.597); Rare genetic vascular disease (0.483)
- **Europe PMC papers**: 10503
- **Why important**: MYLK is a central network connector, linked to RAPH1 and P3H3, and encodes a calcium-calmodulin-dependent kinase that enables actomyosin contractility. Its annotations include smooth-muscle contraction, cell migration, and muscle development. HPA links it to smooth muscle, several contractile or stromal cell types, megakaryocytes, platelets, basophils, and neutrophils. It has extensive literature and strong disease associations involving thoracic aortic aneurysm and related vascular disease, making it the best-established mechanical and vascular anchor of the module.
- **Conclusion**: Established evidence supports MYLK as a contractility and migration gene with substantial vascular and smooth-muscle relevance. Its presence may help explain a structural-cell component of the module, although its immune-cell enrichment also makes sample composition a plausible contributor. It is not established that MYLK directly drives the other module relationships.

#### MAPK14

- **Related proteins** (co-abundance neighbors): GOLPH3L (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Nuclear speckles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitogen-activated protein kinase 14. The protein encoded by this gene is a member of the MAP kinase family. MAP kinases act as an integration point for multiple biochemical signals, and are involved in a wide variety of cellular processes such as proliferation, differentiation, transcription regulation and development. This kinase is activated by various environmental stresses and proinflammatory cytokines. The activation requires it…
- **Diseases (Open Targets)**: neurodegenerative disease (0.464); autoimmune disorder of central nervous system (0.459); Alzheimer disease (0.337); Parkinson disease (0.316); lysosomal storage disease (0.303)
- **Europe PMC papers**: 8074
- **Why important**: MAPK14 is the signaling endpoint connected to GOLPH3L and is a stress- and cytokine-responsive MAP kinase involved in signal integration, transcriptional regulation, chemotaxis, and inflammatory responses. HPA specifically associates it with monocyte progenitors, neutrophil progenitors, neutrophils, basophils, and lung detection. Its extensive literature and disease associations make it the strongest candidate for linking the module to inflammatory or environmental stress states.
- **Conclusion**: Established evidence supports MAPK14 as a stress and inflammatory signaling hub, and HPA supports an immune-associated contribution in lung. Its co-abundance with GOLPH3L could indicate coordinated signaling and trafficking, but no direct interaction or module-level pathway enrichment establishes that mechanism.

#### RAPH1

- **Related proteins** (co-abundance neighbors): GOLPH3L (0.85), MYLK (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nuclear bodies, Plasma membrane; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Ras association (RalGDS/AF-6) and pleckstrin homology domains 1. This gene encodes a protein that belongs to the Mig10/Rap1-interacting adaptor molecule/Lamellipodin family of adapter proteins, which function in cell migration. Members of this family contain pleckstrin-homology domains, Ras-association domains, and proline-rich C-termini. The protein encoded by this gene regulates actin dynamics through interaction with Ena/Vasodilator proteins as well as direc…
- **Diseases (Open Targets)**: neurodegenerative disease (0.524); coronary artery disorder (0.469); bone Paget disease (0.316); osteoarthritis (0.283); coronary atherosclerosis (0.279)
- **Europe PMC papers**: 370
- **Why important**: RAPH1 has the highest network connectivity jointly with GOLPH3L and connects to both GOLPH3L and MYLK. It is an adaptor containing Ras-association and pleckstrin-homology domains that regulates actin dynamics, filamentous-actin organization, and cell migration. It is detected in lung, is not detected in immune cells by HPA, and has substantial literature plus associations with vascular, skeletal, and neurodegenerative disease.
- **Conclusion**: Established evidence supports RAPH1 as a plausible cytoskeletal and migration coordinator that could connect contractile and trafficking-related signals. Its non-immune HPA profile argues against interpreting the entire module as blood-derived. Whether RAPH1 is a functional driver of this shared co-abundance state remains a hypothesis.

#### GOLPH3L

- **Related proteins** (co-abundance neighbors): RAPH1 (0.85), MAPK14 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: golgi phosphoprotein 3 like. The Golgi complex plays a key role in the sorting and modification of proteins exported from the endoplasmic reticulum. The protein encoded by this gene is localized at the Golgi stack and may have a regulatory role in Golgi trafficking. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: pericarditis (0.116); inflammatory bowel disease (0.094); Crohn disease (0.082); ovarian carcinoma (0.078); breast cancer (0.077)
- **Europe PMC papers**: 217
- **Why important**: GOLPH3L is a network connector between RAPH1 and MAPK14 and is annotated to Golgi organization, Golgi-to-plasma-membrane transport, vesicle budding, protein secretion, and protein targeting to the Golgi. Its low tissue specificity and esophageal apical-cell enrichment suggest a broadly relevant epithelial or trafficking context rather than a uniquely lung-specific role. Although its literature volume is more limited than that of MYLK or MAPK14, its position provides a coherent trafficking link within the module.
- **Conclusion**: Established evidence supports GOLPH3L as a Golgi-trafficking regulator and a plausible bridge between membrane trafficking and signaling. The module data do not establish that it couples Golgi transport to MAPK14 activity or RAPH1-mediated actin remodeling, so that connection remains hypothetical.

#### P3H3

- **Related proteins** (co-abundance neighbors): MYLK (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prolyl 3-hydroxylase 3. The protein encoded by this gene belongs to the leprecan family of proteoglycans, which function as collagen prolyl hydroxylases that are required for proper collagen biosynthesis, folding and assembly. This protein, like other family members, is thought to reside in the endoplasmic reticulum. Epigenetic inactivation of this gene is associated with breast and other cancers, suggesting that it may …
- **Diseases (Open Targets)**: severe acute respiratory syndrome (0.259); COVID-19 (0.259); osteoarthritis, knee (0.092); epidermolysis bullosa simplex 2E, with migratory circinate erythema (0.066); exfoliative ichthyosis (0.062)
- **Europe PMC papers**: 221
- **Why important**: P3H3 is connected to MYLK and encodes a collagen prolyl hydroxylase-family protein involved in collagen biosynthesis, collagen metabolism, and peptidyl-lysine hydroxylation. It is detected in lung, has intracellular-and-membrane secretome annotation, and is enriched in several cell types including peritubular myoid cells. Its disease annotations include respiratory viral disease, osteoarthritis, and epithelial fragility, while its literature volume is more limited than that of the major signaling and contractility genes.
- **Conclusion**: Established evidence supports P3H3 as an extracellular-matrix and collagen-processing candidate that could connect tissue structure to MYLK-associated contractility. Its lung detection makes it relevant to the tissue pair, but the module does not establish altered collagen processing or a direct MYLK–P3H3 mechanism.

## Module 23

**Tissue pair**: lung and stem_cells  
**Genes (6)**: KATNB1, MED8, NELFE, NUDT4, PCYT2, TRMT5

### Function

The module does not have any GO or KEGG term passing global multiple-testing correction, so its function cannot be assigned from enrichment statistics. Gene-level annotations instead suggest a mixed nuclear and cytosolic program involving transcriptional regulation, RNA polymerase transcription pausing and initiation, tRNA methylation, phospholipid synthesis, microtubule regulation, and intracellular diphosphoinositol-polyphosphate signaling. The co-abundance graph is sparse, with MED8 as the main connectivity center linking NELFE, PCYT2, and TRMT5, while TRMT5 connects to KATNB1 and NELFE connects to NUDT4. This pattern supports a coordinated expression module, but not a single established biochemical pathway.

**Cell composition.** The module is not dominated by secreted or plasma proteins: no member is annotated as secreted, and all members have low immune-cell specificity. Most members have low tissue specificity, indicating a largely broadly expressed or housekeeping-like component rather than a lung-specific program. The HPA single-cell annotations show recurrent enrichment or enhancement in spermatid and spermatocyte populations, with additional annotations involving ciliated cells, oocytes, syncytiotrophoblasts, cardiomyocytes, pituicytes, and Schwann cells. PCYT2 is tissue enhanced in liver and testis. All members are detected at the protein level in lung, whereas there is no matching HPA tissue assessment for stem cells. Thus, the shared module is unlikely to be explained primarily by blood contamination, but it could reflect broad cellular machinery or shared specialized cell-state programs rather than a lung-and-stem-cell-specific mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional-enrichment term is reported. None of the possible within-module gene pairs meets the supplied STRING interaction threshold, and no hu.MAP complex contains multiple module members. Therefore, the co-abundance relationships are not supported here by high-confidence known physical interactions or a shared curated complex. The direct co-abundance links should be interpreted as expression-level relationships, potentially reflecting shared regulation, cellular state, or indirect biology rather than demonstrated protein binding.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may represent a previously unrecognized co-abundance combination, because its members do not form a reported high-confidence STRING interaction set and do not share a reported hu.MAP complex. However, those absences do not establish biological novelty. Each gene has established molecular functions and disease or literature connections, and the module combines several well-characterized processes. The defensible conclusion is that the cross-tissue co-abundance pattern is potentially novel, whereas the individual genes and most of their functions are not novel. Confirmation would require independent datasets, cell-composition controls, and experimental testing of coordinated regulation.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in which transcriptional output and RNA processing are coordinated with biosynthetic and cytoskeletal demands. MED8 and NELFE could represent a transcriptional regulatory axis; TRMT5 could couple that state to tRNA and mitochondrial RNA-modification requirements; PCYT2 could support membrane phospholipid production; NUDT4 could regulate intracellular signaling through diphosphoinositol-polyphosphate turnover; and KATNB1 could adjust microtubule organization. The repeated single-cell annotations involving germ-cell and ciliated-cell states make a specialized differentiation or structural-cell-state explanation plausible, but this remains a hypothesis rather than an enrichment-supported mechanism.

### Important genes

#### MED8

- **Related proteins** (co-abundance neighbors): NELFE (0.91), PCYT2 (0.87), TRMT5 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mediator complex subunit 8. This gene encodes a protein component of the mediator complex, which aids in transcriptional activation through interaction with RNA polymerase II and gene-specific transcription factors. The encoded protein may also function in ubiquitin ligation and protein degradation. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.537); hypertensive disorder (0.095); hepatocellular carcinoma (0.085); neoplasm (0.080); central nervous system cancer (0.075)
- **Europe PMC papers**: 693
- **Why important**: MED8 is the central network connector in the module, linking the transcription-associated genes NELFE and TRMT5 with PCYT2. Its established mediator-complex function places it at the interface of gene-specific transcription factors and RNA polymerase transcription, with additional annotations involving transcription initiation, elongation, and ubiquitination. It has broad tissue specificity, nuclear localization, lung protein detection, disease associations including neurodegenerative disease and neoplasm, and substantial literature support.
- **Conclusion**: Established evidence supports MED8 as the strongest candidate for coordinating the transcriptional part of the module. It is plausible that its network position reflects shared transcriptional regulation, but the co-abundance data do not prove that MED8 physically binds the other module members.

#### NELFE

- **Related proteins** (co-abundance neighbors): MED8 (0.91), NUDT4 (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: negative elongation factor complex member E. The protein encoded by this gene is part of a complex termed negative elongation factor (NELF) which represses RNA polymerase II transcript elongation. This protein bears similarity to nuclear RNA-binding proteins; however, it has not been demonstrated that this protein binds RNA. The protein contains a tract of alternating basic and acidic residues, largely arginine (R) and aspartic acid (D). The…
- **Diseases (Open Targets)**: HIV infectious disease (0.592); neurodegenerative disease (0.385); iridocyclitis (0.341); ankylosing spondylitis (0.304); gastric cancer (0.089)
- **Europe PMC papers**: 390
- **Why important**: NELFE connects MED8 with NUDT4 and is an established member of the negative elongation factor complex. Its annotated functions include transcriptional pausing and regulation of RNA polymerase transcription. It is nuclear, detected in lung, enriched in late spermatids at the single-cell level, associated with several diseases including HIV infection and neurodegenerative disease, and supported by a substantial literature.
- **Conclusion**: Established evidence supports NELFE as a plausible transcriptional-state marker and a bridge between the module's nuclear and signaling-related components. Its role as a mechanistic driver of this particular lung and stem-cell module remains unproven.

#### TRMT5

- **Related proteins** (co-abundance neighbors): KATNB1 (0.91), MED8 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tRNA methyltransferase 5. tRNAs contain as many as 13 or 14 nucleotides that are modified posttranscriptionally by enzymes that are highly specific for particular nucleotides in the tRNA structure. TRMT5 methylates the N1 position of guanosine-37 (G37) in selected tRNAs using S-adenosyl methionine (Brule et al., 2004 [PubMed 15248782]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Combined oxidative phosphorylation defect type 26 (0.765); neurodegenerative disease (0.503); mitochondrial disease (0.372); hereditary disease (0.193); Intellectual disability (0.118)
- **Europe PMC papers**: 275
- **Why important**: TRMT5 connects MED8 with KATNB1 and encodes a tRNA methyltransferase responsible for guanine modification in selected tRNAs, including mitochondrial tRNAs. It is nucleoplasmic and nucleolar, detected in lung, and shows cell-type enhancement in early spermatids, late primary spermatocytes, and late spermatids. Its disease associations include combined oxidative-phosphorylation defects, mitochondrial disease, neurodegenerative disease, and intellectual disability, with established literature support.
- **Conclusion**: Established evidence makes TRMT5 a strong candidate for linking RNA modification and mitochondrial state to the module. The proposed connection to transcriptional and cytoskeletal co-abundance is a hypothesis, not a demonstrated physical or causal relationship.

#### PCYT2

- **Related proteins** (co-abundance neighbors): MED8 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphate cytidylyltransferase 2, ethanolamine. This gene encodes an enzyme that catalyzes the formation of CDP-ethanolamine from CTP and phosphoethanolamine in the Kennedy pathway of phospholipid synthesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010].
- **Diseases (Open Targets)**: spastic paraplegia 82, autosomal recessive (0.771); complex hereditary spastic paraplegia (0.554); neurodegenerative disease (0.542); Global developmental delay (0.462); Intellectual disability (0.462)
- **Europe PMC papers**: 4199
- **Why important**: PCYT2 is directly connected to MED8 and catalyzes a key step in the Kennedy pathway for phosphatidylethanolamine and phospholipid synthesis. It is the module member with tissue-enhanced annotation in liver and testis and is enriched in late spermatids. It is detected in lung, has disease associations including hereditary spastic paraplegia and neurodegenerative disease, and has the largest literature record among the listed genes.
- **Conclusion**: Established evidence supports PCYT2 as the strongest membrane-biosynthesis candidate and a plausible indicator of cellular structural demand. Its link to MED8 is an expression relationship in this module, not evidence that PCYT2 directly regulates transcription.

#### KATNB1

- **Related proteins** (co-abundance neighbors): TRMT5 (0.91); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: katanin regulatory subunit B1. Microtubules, polymers of alpha and beta tubulin subunits, form the mitotic spindle of a dividing cell and help to organize membranous organelles during interphase. Katanin is a heterodimer that consists of a 60 kDa ATPase (p60 subunit A 1) and an 80 kDa accessory protein (p80 subunit B 1). The p60 subunit acts to sever and disassemble microtubules, while the p80 subunit targets the enzyme to the …
- **Diseases (Open Targets)**: microlissencephaly (0.657); lissencephaly spectrum disorders (0.503); hereditary disease (0.415); Norman-Roberts syndrome (0.370); placenta praevia (0.171)
- **Europe PMC papers**: 274
- **Why important**: KATNB1 is connected to TRMT5 and encodes the regulatory subunit of katanin, a complex that targets microtubule-severing activity and supports microtubule organization. Its single-cell annotations include early spermatids, late primary spermatocytes, fallopian-tube ciliated cells, and respiratory ciliated cells, which provides a biologically relevant structural context for lung and differentiated-cell states. It is associated with lissencephaly-spectrum and related hereditary disorders and has established literature support.
- **Conclusion**: Established evidence supports KATNB1 as the module's cytoskeletal and cell-architecture component. The shared ciliated and germ-cell annotations make it relevant to a differentiation-state hypothesis, but they do not establish that KATNB1 drives the module.

#### NUDT4

- **Related proteins** (co-abundance neighbors): NELFE (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nudix hydrolase 4. The protein encoded by this gene regulates the turnover of diphosphoinositol polyphosphates. The turnover of these high-energy diphosphoinositol polyphosphates represents a molecular switching activity with important regulatory consequences. Molecular switching by diphosphoinositol polyphosphates may contribute to regulating intracellular trafficking. Several alternatively spliced transcript varia…
- **Diseases (Open Targets)**: open-angle glaucoma (0.280); knee fracture (0.217); shoulder fracture (0.196); clavicle fracture (0.196); diabetes mellitus (0.142)
- **Europe PMC papers**: 338
- **Why important**: NUDT4 connects to NELFE and encodes a Nudix hydrolase involved in turnover of diphosphoinositol polyphosphates and related intracellular signaling molecules. It is cytosolic, detected in lung, and has cell-type-enhanced annotations in cardiomyocytes, pituicytes, and Schwann cells. Its disease associations include glaucoma, fractures, and diabetes, and it has established literature support.
- **Conclusion**: Established evidence supports NUDT4 as a signaling and metabolic-regulation candidate at the edge of the module. Its connection to NELFE may reflect coordinated cellular state or signaling feedback, but no direct molecular interaction is established by the supplied evidence.
