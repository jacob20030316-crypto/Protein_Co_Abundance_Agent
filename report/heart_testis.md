# Conserved co-abundance modules: heart and testis

## Module 0

**Tissue pair**: heart and testis  
**Genes (29)**: YWHAH, ALDH7A1, ANXA2, ANXA4, ANXA5, CLIC1, DDX39B, GSR, GSTP1, HNRNPH1, HNRNPR, IDH1, NME3, OLA1, PARVA, PDXK, PGK1, PNP, ADSL, RTN4, SEC22B, SEPTIN2, SEPTIN7, SEPTIN9, SERPINH1, SNX6, SRSF7, TXNDC5, VIM

### Function

No GO or KEGG term passed global correction, so there is no statistically supported pathway-level annotation for this module. The module is best interpreted as a mixed cellular maintenance and stress-adaptation program rather than as a single canonical pathway. Its network connects cytoskeletal organization through SEPTIN2, SEPTIN7, SEPTIN9, VIM, PARVA and annexins; endoplasmic-reticulum protein folding and trafficking through SERPINH1, TXNDC5, RTN4 and SEC22B; RNA processing through HNRNPH1, HNRNPR, SRSF7 and DDX39B; and redox, intermediary and nucleotide metabolism through GSTP1, GSR, IDH1, ALDH7A1, PGK1, ADSL and PNP. These are coherent cellular functions, but their coexistence and co-abundance should be treated as an interpretation of the gene set and network, not as a globally enriched GO or KEGG result. The high-connectivity genes, especially SERPINH1, SEPTIN2, VIM and TXNDC5, suggest that proteostasis, cytoskeletal organization, intracellular trafficking and adaptation to cellular stress may provide the shared biological context in heart and testis.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: only a small subset is annotated as secreted, and most genes are intracellular. It is also not dominated by blood-cell-enriched genes, because most genes have low immune-cell specificity in HPA. However, the module is compositionally broad and largely low in tissue specificity, with many genes enhanced in particular cell types rather than uniquely characteristic of heart or testis. HPA shows frequent enhancement in trophoblast, epithelial, stromal, vascular, liver-associated, neural and reproductive cell contexts, while several genes are detected in blood-related cell types. This pattern is compatible with a shared intracellular program or shared non-parenchymal cell types, and it does not by itself establish a heart-muscle or germ-cell-specific mechanism. Protein detection is much more complete in testis than in heart, so the heart signal may also be more sensitive to cellular composition, abundance and detection differences.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports several established local relationships rather than a single dense interaction system. The strongest coherent groups are the SEPTIN2–SEPTIN7–SEPTIN9 structural group, the HNRNPH1–HNRNPR–SRSF7–DDX39B RNA-processing group, the GSR–GSTP1 redox relationship, the ADSL–IDH1–PNP metabolic connections, and the ANXA2–ANXA5 membrane-associated relationship. hu.MAP independently supports the septin complex (hu.MAP huMAP3_02362.1), a complex containing ADSL and OLA1 (hu.MAP huMAP3_14442.1), and an RNA-processing complex containing DDX39B and SRSF7 (hu.MAP huMAP3_09943.1). These concordant relationships indicate that parts of the module recover known protein complexes and functional neighborhoods. At the same time, many co-abundant edges lack a corresponding high-confidence STRING or hu.MAP relationship. Thus, the network is not evidence that all module members physically interact; it more likely combines several established submodules linked by abundance covariation or shared cellular state.

**STRING interactions (score >= 0.7)**: 16 of 406 gene pairs: ADSL–IDH1 (0.86); ADSL–PNP (0.725); ANXA2–ANXA5 (0.833); ANXA2–CLIC1 (0.713); DDX39B–HNRNPH1 (0.742); DDX39B–HNRNPR (0.74); DDX39B–SRSF7 (0.905); GSR–GSTP1 (0.952); GSR–IDH1 (0.776); HNRNPH1–HNRNPR (0.947); HNRNPH1–SRSF7 (0.922); HNRNPR–SRSF7 (0.833); IDH1–PGK1 (0.726); SEPTIN2–SEPTIN7 (0.999); SEPTIN2–SEPTIN9 (0.997); SEPTIN7–SEPTIN9 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02362.1 (SEPTIN2, SEPTIN7, SEPTIN9; 3/14); huMAP3_14442.1 (ADSL, OLA1; 2/57); huMAP3_09943.1 (DDX39B, SRSF7; 2/78)

### Novelty

The module should not be described as a completely new molecular pathway. Several of its internal relationships are already established by STRING or hu.MAP, especially the septin assembly, RNA-processing group, redox pair and annexin relationship. The individual genes also have well-established functions and disease associations. A potentially novel aspect is the conservation of their co-abundance as one module across heart and testis, particularly the linkage of cytoskeletal, ER-proteostasis, RNA-processing, redox and metabolic components. However, absence of a complete matching complex in STRING or hu.MAP does not prove novelty, and the lack of globally significant GO or KEGG enrichment prevents a strong claim that this is a newly defined biological pathway. The most defensible conclusion is that the cross-tissue co-abundance pattern is a candidate organizational finding requiring replication and experimental validation.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular resilience program active in structurally specialized and metabolically demanding cells. In this model, septin and vimentin cytoskeletal systems organize membranes and intracellular trafficking; annexins and sorting or vesicle factors support membrane remodeling; SERPINH1 and TXNDC5 maintain ER protein folding and collagen-related proteostasis; RNA-binding and splicing proteins sustain transcript processing; and GSTP1, GSR, IDH1 and related enzymes buffer redox and metabolic stress. Heart and testis may share this program because both require coordinated cytoskeletal architecture, trafficking, protein quality control and oxidative-stress management. An alternative explanation is that the module partly reflects shared stromal, vascular, epithelial or other non-parenchymal cell populations in the sampled tissues. Testing these alternatives would require cell-resolved data, replication across cohorts and perturbation of selected hub or bridge genes.

### Important genes

#### SERPINH1

- **Related proteins** (co-abundance neighbors): VIM (0.91), TXNDC5 (0.90), SEPTIN2 (0.89), HNRNPH1 (0.88), SEPTIN9 (0.86), OLA1 (0.85), SNX6 (0.85), GSTP1 (0.84), YWHAH (0.83), ANXA5 (0.82), DDX39B (0.81), ANXA2 (0.81), IDH1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family H member 1. This gene encodes a member of the serpin superfamily of serine proteinase inhibitors. The encoded protein is localized to the endoplasmic reticulum and plays a role in collagen biosynthesis as a collagen-specific molecular chaperone. Autoantibodies to the encoded protein have been found in patients with rheumatoid arthritis. Expression of this gene may be a marker for cancer, and nucleotide polymo…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 10 (0.714); preterm premature rupture of the membranes (0.559); coronary artery disorder (0.554); myocardial infarction (0.510); Abnormality of the skeletal system (0.474)
- **Europe PMC papers**: 2762
- **Why important**: SERPINH1 is the leading network hub in the supplied ordering and connects VIM, TXNDC5, septins, HNRNPH1, OLA1, SNX6 and GSTP1. Its established function as an ER collagen-specific molecular chaperone links the network to protein folding, unfolded-protein handling and collagen organization. It has substantial literature support and disease associations involving skeletal biology, preterm membrane rupture and cardiovascular disease. HPA places it in the ER, with broad tissue specificity and enhanced expression in several stromal and reproductive cell contexts.
- **Conclusion**: Established evidence supports SERPINH1 as a proteostasis and extracellular-matrix-related hub that may organize part of the module. Its central network position makes it an important candidate driver or marker, but the data do not establish that SERPINH1 causes the cross-tissue co-abundance pattern or that collagen handling is the dominant module function.

#### SEPTIN2

- **Related proteins** (co-abundance neighbors): VIM (0.94), SERPINH1 (0.89), SEPTIN9 (0.89), TXNDC5 (0.88), HNRNPH1 (0.87), PNP (0.86), SNX6 (0.85), GSTP1 (0.85), OLA1 (0.84), SRSF7 (0.83), DDX39B (0.82), SEPTIN7 (0.81); STRING partners: SEPTIN7 (0.999), SEPTIN9 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Actin filaments; IHC detected in heart, testis
- **hu.MAP 3.0**: huMAP3_02362.1
- **Function (MyGene.info)**: septin 2. Enables identical protein binding activity. Predicted to be involved in several processes, including cilium assembly; regulation of exocytosis; and smoothened signaling pathway. Predicted to act upstream of or within regulation of L-glutamate import across plasma membrane and regulation of protein localization. Located in several cellular components, including cytoskeleton; photoreceptor connectin…
- **Diseases (Open Targets)**: hypothyroidism (0.239); squamous cell carcinoma (0.201); ischemic stroke (0.189); coronary artery disorder (0.181); skin cancer (0.181)
- **Europe PMC papers**: 281
- **Why important**: SEPTIN2 is one of the most connected genes in the module and bridges VIM, SERPINH1, TXNDC5, HNRNPH1, PNP and GSTP1. It belongs to the septin structural system and is supported by both STRING relationships with SEPTIN7 and SEPTIN9 and the high-confidence hu.MAP septin complex (hu.MAP huMAP3_02362.1). Its known functions include cytoskeleton organization, cilium assembly, intracellular localization and cytokinesis, with particular relevance to the sperm annulus and membrane architecture.
- **Conclusion**: Established evidence supports SEPTIN2 as a structural organizer and a strong anchor for the module's cytoskeletal interpretation. Its presence in both heart and testis is consistent with a shared architectural program, but the co-abundance data do not demonstrate a tissue-specific septin mechanism or direct regulation of the other module genes.

#### VIM

- **Related proteins** (co-abundance neighbors): SEPTIN2 (0.94), TXNDC5 (0.91), SERPINH1 (0.91), HNRNPH1 (0.89), GSTP1 (0.88), SRSF7 (0.87), ANXA2 (0.85), DDX39B (0.81), ADSL (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vimentin. This gene encodes a type III intermediate filament protein. Intermediate filaments, along with microtubules and actin microfilaments, make up the cytoskeleton. The encoded protein is responsible for maintaining cell shape and integrity of the cytoplasm, and stabilizing cytoskeletal interactions. This protein is involved in neuritogenesis and cholesterol transport and functions as an organizer of a…
- **Diseases (Open Targets)**: dengue disease (0.516); early-onset non-syndromic cataract (0.462); early-onset partial cataract (0.458); Developmental cataract (0.435); cataract (0.372)
- **Europe PMC papers**: 86568
- **Why important**: VIM is a prominent network hub linking the septin, ER-proteostasis, RNA-processing, annexin and redox portions of the module. Its established role as a type three intermediate-filament protein provides a mechanistic connection to cell shape, cytoplasmic integrity, attachment, migration and signaling. HPA shows tissue enhancement in blood vessels and cell-type enhancement in fibroblastic, stromal, hepatic and Leydig contexts, which is important when considering cellular composition. VIM also has a very large literature base and multiple disease associations.
- **Conclusion**: Established evidence supports VIM as a plausible structural integrator and as a possible indicator of stromal, vascular or other non-parenchymal contributions. The hypothesis that VIM physically coordinates all connected submodules remains unproven; its high co-abundance connectivity may instead reflect shared cell state or cell composition.

#### TXNDC5

- **Related proteins** (co-abundance neighbors): VIM (0.91), SERPINH1 (0.90), SEPTIN2 (0.88), SRSF7 (0.87), SNX6 (0.87), HNRNPH1 (0.87), OLA1 (0.85), RTN4 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Endoplasmic reticulum; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin domain containing 5. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal endoplasmic reticulum (ER)-signal sequence, three catalytically active thioredoxin domains and a C-terminal ER-retention sequence. Its expression is induced by hypoxia and its role ma…
- **Diseases (Open Targets)**: colorectal carcinoma (0.321); spinal stenosis (0.203); neoplasm (0.096); central nervous system cancer (0.092); glioma (0.091)
- **Europe PMC papers**: 1026
- **Why important**: TXNDC5 is a central network connector between VIM, SERPINH1, SEPTIN2, SRSF7, SNX6, HNRNPH1, OLA1 and RTN4. It is an ER protein-disulfide isomerase with multiple thioredoxin domains and an ER-retention signal, and its expression is induced by hypoxia with a reported role in protection from apoptosis. HPA places it in ER-associated compartments and identifies enhancement in plasma-cell and selected B-cell or plasmacytoid immune contexts, which adds a composition caveat.
- **Conclusion**: Established evidence supports TXNDC5 as an ER folding and redox-proteostasis component that could explain the module's connection to stress adaptation. Its centrality makes it important, but the module does not establish hypoxia, apoptosis protection or an immune-cell origin as the cause of the observed heart–testis conservation.

#### HNRNPH1

- **Related proteins** (co-abundance neighbors): VIM (0.89), SERPINH1 (0.88), SEPTIN2 (0.87), TXNDC5 (0.87), IDH1 (0.85), YWHAH (0.82); STRING partners: DDX39B (0.742), HNRNPR (0.947), SRSF7 (0.922)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein H1. This gene encodes a member of a subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins that complex with heterogeneous nuclear RNA. These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the n…
- **Diseases (Open Targets)**: neurodevelopmental disorder with craniofacial dysmorphism and skeletal defects (0.668); dengue disease (0.462); hereditary disease (0.411); neurodevelopmental disorder (0.400); syndromic intellectual disability (0.370)
- **Europe PMC papers**: 1509
- **Why important**: HNRNPH1 links VIM, SERPINH1, SEPTIN2, TXNDC5, IDH1 and YWHAH in the abundance network. It is an established heterogeneous nuclear ribonucleoprotein involved in pre-mRNA processing, RNA metabolism and regulation of splicing. STRING supports its relationships with DDX39B, HNRNPR and SRSF7, and these partners are also represented in hu.MAP-supported RNA-processing complex (hu.MAP huMAP3_09943.1). Its heart and testis protein detection is consistent with a broadly shared intracellular role.
- **Conclusion**: Established evidence supports HNRNPH1 as a transcript-processing component and as a bridge between the RNA-processing group and other cellular systems. The data support coordinated RNA metabolism as part of the module, but they do not identify particular transcripts, splicing events or a causal role for HNRNPH1 in tissue conservation.

#### GSTP1

- **Related proteins** (co-abundance neighbors): VIM (0.88), YWHAH (0.87), ANXA2 (0.85), SEPTIN2 (0.85), SEPTIN9 (0.84), ANXA5 (0.84), SERPINH1 (0.84), CLIC1 (0.81); STRING partners: GSR (0.952)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutathione S-transferase pi 1. Glutathione S-transferases (GSTs) are a family of enzymes that play an important role in detoxification by catalyzing the conjugation of many hydrophobic and electrophilic compounds with reduced glutathione. Based on their biochemical, immunologic, and structural properties, the soluble GSTs are categorized into 4 main classes: alpha, mu, pi, and theta. This GST family member is a polymorphic gene…
- **Diseases (Open Targets)**: neurodegenerative disease (0.350); breast cancer (0.117); hepatocellular carcinoma (0.115); neoplasm (0.114); posterior cortical atrophy (0.113)
- **Europe PMC papers**: 12759
- **Why important**: GSTP1 is a highly connected redox and stress-associated gene linked to VIM, YWHAH, annexins, septins, SERPINH1 and CLIC1. It has a strong known STRING relationship with GSR and established functions in glutathione conjugation, xenobiotic metabolism and responses to reactive oxygen species. HPA detects the protein in both tissues and shows enhancement in esophageal and epithelial cell contexts. Its extensive literature and disease associations make it a useful marker of cellular stress and detoxification capacity.
- **Conclusion**: Established evidence supports GSTP1 as a redox-protection and detoxification component that may connect oxidative stress to cytoskeletal and membrane-associated proteins. It supports a stress-adaptation interpretation, but the module does not prove that oxidative stress is the initiating signal or that GSTP1 is the causal hub.

## Module 1

**Tissue pair**: heart and testis  
**Genes (25)**: SERPINA1, A1BG, ACADVL, ACO2, ACSS1, ACSL1, AIFM1, SERPINC1, CRAT, CPT2, MLYCD, ETFDH, HPX, HSDL2, LGALS3BP, MCCC1, IMMT, NDUFS1, NNT, DLAT, PDHB, SLC25A12, SDHA, ACAA2, GC

### Function

The best-supported function is mitochondrial acyl-CoA production and utilization, centered on the globally corrected (GO:BP acyl-CoA biosynthetic process; q_global = 0.0442) acyl-CoA biosynthetic process. (GO:BP acyl-CoA biosynthetic process; q_global = 0.0442) links ACSL1 and ACSS1 with MLYCD, DLAT, and PDHB, connecting fatty-acid activation and malonyl-CoA handling with acetyl-CoA generation through pyruvate metabolism. The dense STRING-supported mitochondrial subnetwork further supports coordinated oxidative metabolism, fatty-acid beta-oxidation, respiratory-chain activity, and inner-membrane organization through (STRING Keyword Mitochondrion; within-query FDR = 0.0255), (STRING Keyword Transit peptide; within-query FDR = 0.0255), (STRING Keyword Mitochondrion inner membrane; within-query FDR = 0.0255), (STRING NetworkNeighborAL Mixed, incl. Fatty acid beta-oxidation, and AMP-binding, conserved site; within-query FDR = 0.0349), and (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0367). These STRING annotations are supplementary rather than globally corrected enrichment evidence. The network also contains a distinct plasma-protein component involving HPX, GC, A1BG, SERPINA1, and SERPINC1, so the module is biologically mixed rather than a purely mitochondrial module. No other GO or KEGG term passed global correction.

**Cell composition.** The module is dominated functionally by broadly distributed mitochondrial and metabolic genes, with tissue enhancement often involving heart muscle, skeletal muscle, tongue, or liver and with low immune-cell specificity for most genes. This is compatible with a shared energetic program in heart and testis, both of which show protein detection for most module genes. However, several genes are secreted plasma proteins, including HPX, A1BG, SERPINA1, and SERPINC1, and these proteins are liver-enriched or hepatocyte-enriched in HPA and are not detected in heart or testis tissue by the reported IHC evidence. SERPINA1 has blood-cell enrichment and ACSL1 has neutrophil enrichment, although the overall module has low blood-cell specificity. Thus, part of the shared co-abundance signal could reflect plasma or vascular material, sample composition, or shared non-parenchymal components rather than a heart-testis cell-intrinsic program. The HPA pattern also indicates that tissue specificity is distributed across liver, muscle, tongue, and specialized cell types rather than being uniquely specific to heart and testis.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP acyl-CoA biosynthetic process | 0.0442 | ACSL1, ACSS1, DLAT, MLYCD, PDHB |

### STRING and hu.MAP

STRING supports a coherent mitochondrial metabolism network. Strong relationships connect ACAA2, ACADVL, CPT2, ETFDH, ACSL1, ACSS1, HSDL2, SDHA, ACO2, DLAT, PDHB, and NDUFS1, covering beta-oxidation, acetyl-CoA metabolism, the TCA cycle, and respiratory-chain function. The plasma proteins form a separate known relationship group: HPX connects with GC, SERPINA1, and SERPINC1, while GC also connects with SERPINA1 and SERPINC1. These relationships indicate that much of the module recapitulates established biochemical neighborhoods rather than revealing arbitrary gene associations. hu.MAP independently supports this interpretation. (hu.MAP huMAP3_13468.1) contains the mitochondrial metabolic group including CPT2, ACAA2, CRAT, MCCC1, and ACSS1; (hu.MAP huMAP3_04919.1) through (hu.MAP huMAP3_12248.1) repeatedly recover the DLAT-PDHB pyruvate-dehydrogenase relationship; and (hu.MAP huMAP3_15040.1) together with (hu.MAP huMAP3_10678.1) through (hu.MAP huMAP3_02236.1) captures the plasma-protein group. The overlap with known STRING relationships and hu.MAP complexes supports biological coherence, but it also means the module is not evidence that these proteins physically assemble into one novel complex.

**STRING interactions (score >= 0.7)**: 36 of 300 gene pairs: A1BG–SERPINA1 (0.735); ACAA2–ACADVL (0.983); ACAA2–ACO2 (0.75); ACAA2–ACSL1 (0.788); ACAA2–ACSS1 (0.937); ACAA2–CPT2 (0.822); ACAA2–DLAT (0.892); ACAA2–ETFDH (0.81); ACAA2–HSDL2 (0.918); ACAA2–SDHA (0.753); ACADVL–ACSL1 (0.841); ACADVL–CPT2 (0.995); ACADVL–ETFDH (0.817); ACADVL–HSDL2 (0.787); ACO2–DLAT (0.727); ACO2–NDUFS1 (0.865); ACO2–SDHA (0.975); ACSS1–DLAT (0.942); ACSS1–HSDL2 (0.727); ACSS1–MLYCD (0.866); ACSS1–PDHB (0.861); CPT2–ETFDH (0.758); DLAT–MLYCD (0.854); DLAT–NDUFS1 (0.773); DLAT–PDHB (0.999); DLAT–SDHA (0.852); ETFDH–HSDL2 (0.701); GC–HPX (0.827); GC–SERPINA1 (0.876); GC–SERPINC1 (0.84); HPX–SERPINA1 (0.897); HPX–SERPINC1 (0.762); IMMT–NDUFS1 (0.901); NDUFS1–PDHB (0.809); NDUFS1–SDHA (0.995); PDHB–SDHA (0.731)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Mitochondrion (FDR = 0.0255, 18 genes); Keyword Transit peptide (FDR = 0.0255, 15 genes); Keyword Mitochondrion inner membrane (FDR = 0.0255, 10 genes); NetworkNeighborAL Mixed, incl. Fatty acid beta-oxidation, and AMP-binding, conserved site (FDR = 0.0349, 9 genes); COMPARTMENTS Mitochondrion (FDR = 0.0367, 19 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINC1, SERPINA1, GC, HPX, A1BG; 5/64); huMAP3_13468.1 (CPT2, ACAA2, CRAT, MCCC1, ACSS1; 5/99); huMAP3_10678.1 (SERPINA1, GC, HPX, A1BG; 4/71); huMAP3_08700.1 (SERPINA1, HPX, A1BG; 3/11); huMAP3_07432.1 (SERPINA1, HPX, A1BG; 3/18); huMAP3_07265.1 (SERPINA1, HPX, A1BG; 3/20); huMAP3_09434.1 (SERPINA1, GC, A1BG; 3/33); huMAP3_08395.1 (SERPINA1, HPX, A1BG; 3/43); huMAP3_09531.1 (SERPINA1, HPX, A1BG; 3/47); huMAP3_10101.1 (SERPINA1, HPX, A1BG; 3/49); huMAP3_02236.1 (HPX, A1BG; 2/7); huMAP3_04919.1 (DLAT, PDHB; 2/7); huMAP3_08216.1 (DLAT, PDHB; 2/8); huMAP3_07514.1 (DLAT, PDHB; 2/9); huMAP3_09761.1 (DLAT, PDHB; 2/10); huMAP3_10899.1 (DLAT, PDHB; 2/10); huMAP3_10412.1 (DLAT, PDHB; 2/12); huMAP3_14339.1 (DLAT, PDHB; 2/13); huMAP3_11877.1 (DLAT, PDHB; 2/14); huMAP3_14864.1 (DLAT, PDHB; 2/14); huMAP3_12248.1 (DLAT, PDHB; 2/22); huMAP3_10525.1 (CRAT, MCCC1; 2/33)

### Novelty

The exact heart-testis conserved co-abundance module may be a new systems-level observation, but the underlying biology is not newly established by this fact sheet. Its principal components are known mitochondrial enzymes, respiratory-chain proteins, pyruvate-dehydrogenase components, fatty-acid oxidation proteins, and circulating liver-derived proteins. Many within-module relationships are already represented in STRING and hu.MAP, including the mitochondrial metabolic group, the DLAT-PDHB relationship, and the plasma-protein groups. Therefore, the defensible novelty claim is limited to the tissue-pair co-abundance pattern, its particular combination of metabolic and plasma signals, and its reproducibility across heart and testis. Absence of a complete matching module in STRING or hu.MAP would not by itself establish novelty, because those resources represent physical interactions and complexes rather than this specific tissue-pair co-abundance construction.

**Hypothesis.** Hypothesis: the conserved module reflects a shared high-demand mitochondrial energy program in heart and testis. Coordinated expression of ACSS1, ACSL1, MLYCD, CPT2, ACADVL, ACAA2, CRAT, DLAT, and PDHB could balance acetate and fatty-acyl-CoA entry with pyruvate-derived acetyl-CoA production and beta-oxidation. SDHA, NDUFS1, ACO2, NNT, and IMMT could support electron transport, redox control, TCA-cycle flux, and mitochondrial membrane organization. The co-occurring HPX, GC, A1BG, SERPINA1, and SERPINC1 signal may represent circulating plasma carryover or a shared vascular or extracellular context rather than participation in the same intracellular pathway. This hypothesis should be tested with cell-resolved data, plasma-depletion or vascular-marker controls, and independent heart and testis cohorts.

### Important genes

#### ACSS1

- **Related proteins** (co-abundance neighbors): MCCC1 (0.91), SERPINA1 (0.82), ACADVL (0.81); STRING partners: ACAA2 (0.937), DLAT (0.942), HSDL2 (0.727), MLYCD (0.866), PDHB (0.861)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in heart, testis
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: acyl-CoA synthetase short chain family member 1. This gene encodes a mitochondrial acetyl-CoA synthetase enzyme. A similar protein in mice plays an important role in the tricarboxylic acid cycle by catalyzing the conversion of acetate to acetyl CoA. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Nov 2011].
- **Diseases (Open Targets)**: response to antihypertensive drug (0.284); neurodegenerative disease (0.220); acute myeloid leukemia (0.061); neoplasm (0.048); hepatocellular carcinoma (0.039)
- **Europe PMC papers**: 1022
- **Why important**: ACSS1 is directly present in the primary globally corrected term (GO:BP acyl-CoA biosynthetic process; q_global = 0.0442) and encodes a mitochondrial acetyl-CoA synthetase that converts acetate to acetyl-CoA. It connects the primary enrichment signal to the STRING-supported mitochondrial neighborhood, including ACAA2, DLAT, HSDL2, MLYCD, and PDHB, and it is represented in the mitochondrial hu.MAP complex (hu.MAP huMAP3_13468.1). Its tissue and cell-type pattern includes heart, testis protein detection, choroid plexus enhancement, and Sertoli-cell enhancement. Its disease and literature support are more limited than for highly studied respiratory genes, making it a useful candidate for testing whether acetate utilization contributes to the shared module.
- **Conclusion**: Established: ACSS1 is a mitochondrial acetyl-CoA-producing enzyme and a direct member of (GO:BP acyl-CoA biosynthetic process; q_global = 0.0442), with multiple known metabolic network links. Hypothesis: coordinated ACSS1 abundance may help supply acetyl-CoA during the shared energetic state of heart and testis.

#### SDHA

- **Related proteins** (co-abundance neighbors): NDUFS1 (0.91), CRAT (0.86), ACSL1 (0.84), MLYCD (0.83), IMMT (0.82), AIFM1 (0.80); STRING partners: ACAA2 (0.753), ACO2 (0.975), DLAT (0.852), NDUFS1 (0.995), PDHB (0.731)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate dehydrogenase complex flavoprotein subunit A. This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identi…
- **Diseases (Open Targets)**: mitochondrial complex II deficiency, nuclear type 1 (0.813); pheochromocytoma/paraganglioma syndrome 5 (0.790); dilated cardiomyopathy 1GG (0.768); neurodegeneration with ataxia and late-onset optic atrophy (0.761); gastrointestinal stromal tumor (0.743)
- **Europe PMC papers**: 12756
- **Why important**: SDHA has the strongest network position in the reported module and connects to NDUFS1, CRAT, ACSL1, MLYCD, IMMT, and AIFM1. It is a catalytic component of mitochondrial complex II and links the TCA cycle to respiratory electron transfer. STRING places it in the mitochondrial, transit-peptide, and inner-membrane annotations (STRING Keyword Mitochondrion; within-query FDR = 0.0255), (STRING Keyword Transit peptide; within-query FDR = 0.0255), (STRING Keyword Mitochondrion inner membrane; within-query FDR = 0.0255), and (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0367). HPA shows enhancement in heart muscle and skeletal muscle with protein detection in heart and testis. Its established disease associations include mitochondrial respiratory deficiency, cardiomyopathy, and paraganglioma-related disease, supported by a substantial literature.
- **Conclusion**: Established: SDHA is a central mitochondrial respiratory and TCA-cycle component with strong network connectivity and relevant heart expression. Hypothesis: its position may make it a metabolic integrator linking fatty-acid oxidation with respiratory-chain capacity in this conserved module.

#### CRAT

- **Related proteins** (co-abundance neighbors): ACSL1 (0.88), SDHA (0.86), CPT2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in heart, testis
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1
- **Function (MyGene.info)**: carnitine O-acetyltransferase. This gene encodes carnitine O-acetyltransferase, a member of the carnitine acyltransferase family and a key metabolic pathway enzyme which plays an important role in energy homeostasis and fat metabolism. This enzyme catalyzes the reversible transfer of acyl groups from an acyl-CoA thioester to carnitine and regulates the ratio of acyl-CoA/CoA. It is found in both the mitochondria and the peroxiso…
- **Diseases (Open Targets)**: neurodegeneration with brain iron accumulation 8 (0.499); neurodegeneration with brain iron accumulation (0.341); neurodegenerative disease (0.301); Alzheimer disease (0.252); lysosomal storage disease (0.247)
- **Europe PMC papers**: 4594
- **Why important**: CRAT connects ACSL1, SDHA, and CPT2, thereby bridging acyl-CoA handling, respiratory metabolism, and the carnitine system. It is included in the STRING mitochondrial and fatty-acid-related terms (STRING Keyword Mitochondrion; within-query FDR = 0.0255), (STRING Keyword Mitochondrion inner membrane; within-query FDR = 0.0255), (STRING NetworkNeighborAL Mixed, incl. Fatty acid beta-oxidation, and AMP-binding, conserved site; within-query FDR = 0.0349), and (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0367), and in the metabolic hu.MAP complexes (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1). HPA shows enhancement in skeletal muscle and tongue, including early and late spermatogenic cell types, with detection in both heart and testis. Its established function is reversible transfer of acyl groups between CoA and carnitine, which can regulate the balance between acyl-CoA and free CoA.
- **Conclusion**: Established: CRAT is a carnitine acyltransferase positioned at an interface between fatty-acid metabolism and CoA homeostasis. Hypothesis: CRAT may tune substrate flexibility and protect CoA balance during the energetic demands shared by cardiac and testicular cells.

#### HPX

- **Related proteins** (co-abundance neighbors): LGALS3BP (0.87), GC (0.86), A1BG (0.85); STRING partners: GC (0.827), SERPINA1 (0.897), SERPINC1 (0.762)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_08700.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_02236.1
- **Function (MyGene.info)**: hemopexin. This gene encodes a plasma glycoprotein that binds heme with high affinity. The encoded protein is an acute phase protein that transports heme from the plasma to the liver and may be involved in protecting cells from oxidative stress. [provided by RefSeq, Apr 2009].
- **Diseases (Open Targets)**: panniculitis (0.116); neoplasm (0.107); familial idiopathic steroid-resistant nephrotic syndrome (0.101); hepatocellular carcinoma (0.101); focal segmental glomerulosclerosis (0.097)
- **Europe PMC papers**: 6894
- **Why important**: HPX is important because it exposes the module's non-mitochondrial component. It is a liver- and hepatocyte-enriched secreted plasma glycoprotein that binds heme, transports it to the liver, and may protect against oxidative stress. It connects to GC, A1BG, and LGALS3BP in the co-abundance graph and to GC, SERPINA1, and SERPINC1 in STRING. It is represented across the plasma-protein hu.MAP group (hu.MAP huMAP3_15040.1) and related complexes (hu.MAP huMAP3_10678.1) through (hu.MAP huMAP3_02236.1), while HPA reports no heart or testis IHC detection. Its substantial literature and heme-handling function make it more informative than treating the plasma signal as an unexamined technical artifact.
- **Conclusion**: Established: HPX is a circulating heme-binding protein with known plasma-protein partners and no reported heart or testis tissue detection in this evidence set. Hypothesis: its co-abundance may mark plasma exposure, vascular material, or oxidative stress context rather than an intracellular heart-testis mechanism.

#### SERPINA1

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.83), ACSS1 (0.82); STRING partners: A1BG (0.735), GC (0.876), HPX (0.897)
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_08700.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1
- **Function (MyGene.info)**: serpin family A member 1. The protein encoded by this gene is a serine protease inhibitor belonging to the serpin superfamily whose targets include elastase, plasmin, thrombin, trypsin, chymotrypsin, and plasminogen activator. This protein is produced in the liver, the bone marrow, by lymphocytic and monocytic cells in lymphoid tissue, and by the Paneth cells of the gut. Defects in this gene are associated with chronic obs…
- **Diseases (Open Targets)**: alpha 1-antitrypsin deficiency (0.768); chronic obstructive pulmonary disease (0.690); cirrhosis of liver (0.573); cholelithiasis (0.569); pulmonary emphysema (0.569)
- **Europe PMC papers**: 6526
- **Why important**: SERPINA1 is a secreted liver-derived serine-protease inhibitor and a prominent marker of the module's plasma and immune-adjacent component. It connects to SERPINC1 and ACSS1 in the module and to A1BG, GC, and HPX in STRING. It appears in numerous hu.MAP plasma-protein complexes, including (hu.MAP huMAP3_15040.1) and (hu.MAP huMAP3_10678.1) through (hu.MAP huMAP3_10101.1). HPA identifies liver enrichment, secretion to blood, and enrichment among several myeloid blood-cell classes. Its established disease associations include alpha-one-antitrypsin deficiency, chronic obstructive pulmonary disease, emphysema, and chronic liver disease, with a large literature base.
- **Conclusion**: Established: SERPINA1 is a well-characterized circulating protease inhibitor and plasma-protein network marker. Hypothesis: its presence may indicate blood or vascular contribution to the conserved module and should be controlled before assigning the entire module to heart-testis intracellular metabolism.

## Module 2

**Tissue pair**: heart and testis  
**Genes (5)**: GOT1, ACADM, ATP5F1C, CS, SUCLA2

### Function

This module is most consistent with coordinated mitochondrial energy metabolism in oxidative tissues. CS is the central network hub and represents the tricarboxylic acid cycle; SUCLA2 represents succinyl-CoA synthetase activity within that cycle; ACADM represents mitochondrial fatty-acid beta-oxidation; GOT1 links amino-acid, oxaloacetate, and tricarboxylic-acid metabolism; and ATP5F1C represents the mitochondrial ATP synthase machinery. Together, the gene set suggests coupling of carbon oxidation, intermediary-metabolite exchange, and ATP production. This interpretation is based on the individual gene annotations, the compact network, and the strong STRING-supported relationships. No GO or KEGG term passed global correction. The absence of globally significant enrichment does not invalidate the module, particularly because the module is small and functionally coherent at the level of individual enzymes.

**Cell composition.** The module is not composed of secreted proteins and does not show blood-cell enrichment. All module proteins were detected in both heart and testis, while the HPA profiles emphasize skeletal muscle, tongue, and, for selected genes, heart muscle or liver. Most genes have enhanced specificity for particular cell types, including muscle-associated, epithelial, parietal, hepatic, retinal, and spermatogenic populations, although the module also contains a gene with low cell-type specificity. Thus, the shared heart-testis signal is more plausibly related to oxidative metabolic demand or shared metabolically active cell populations than to plasma contamination or a blood-cell program. The tissue pattern also cautions that the module may reflect abundance of metabolically specialized cells rather than a pathway unique to either organ.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a connected metabolic core involving CS with SUCLA2, GOT1, and ATP5F1C, as well as ACADM with SUCLA2. The strongest-supported relationships include the CS–SUCLA2 and CS–GOT1 links, while ATP5F1C connects to CS and SUCLA2 and ACADM connects to SUCLA2. These relationships are compatible with known mitochondrial energy metabolism, but STRING associations can reflect evidence accumulated from several sources and do not by themselves establish direct physical contact or a single molecular complex. No hu.MAP complex contained multiple module members. Therefore, the network is better interpreted as a functional metabolic neighborhood than as evidence for one defined multiprotein assembly. No STRING functional-enrichment term was reported.

**STRING interactions (score >= 0.7)**: 5 of 10 gene pairs: ACADM–SUCLA2 (0.755); ATP5F1C–CS (0.726); ATP5F1C–SUCLA2 (0.751); CS–GOT1 (0.908); CS–SUCLA2 (0.96)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be presented as a newly discovered biochemical pathway. Its principal genes encode well-established metabolic enzymes, and several of the relationships are already represented in STRING. The lack of a hu.MAP complex does not establish novelty, because absence from a complex resource can reflect coverage, experimental context, or the fact that these proteins participate in pathway-level coordination rather than one stable complex. A potentially novel aspect is the reproducible co-abundance of this metabolic neighborhood across heart and testis, especially the way fatty-acid oxidation, tricarboxylic-acid metabolism, amino-acid-linked carbon transfer, and ATP synthesis co-vary in these tissues. That cross-tissue co-abundance observation remains a hypothesis-generating systems-level result rather than proof of a new interaction or mechanism.

**Hypothesis.** Hypothesis: in metabolically demanding heart and testis cell populations, coordinated abundance of CS, SUCLA2, ACADM, GOT1, and ATP5F1C supports flexible mitochondrial fuel utilization and efficient ATP generation. CS and SUCLA2 may mark tricarboxylic-acid-cycle throughput, ACADM may provide acetyl-CoA and reducing equivalents from medium-chain fatty acids, GOT1 may help balance oxaloacetate and amino-acid-derived carbon, and ATP5F1C may reflect coupling to oxidative phosphorylation. The co-abundance pattern could therefore arise from shared regulation of mitochondrial capacity in oxidative cells, rather than from direct assembly of all module proteins into one complex. This mechanism should be tested with tissue-resolved expression, protein-complex assays, mitochondrial flux measurements, and perturbation of the candidate enzymes.

### Important genes

#### CS

- **Related proteins** (co-abundance neighbors): ATP5F1C (0.87), SUCLA2 (0.85), GOT1 (0.84), ACADM (0.82); STRING partners: ATP5F1C (0.726), GOT1 (0.908), SUCLA2 (0.96)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS is the principal network hub, connecting the other metabolic components and having the strongest weighted connectivity in the module. Its established function is catalysis of citrate formation at the entry point of the tricarboxylic acid cycle. It is mitochondrial, detected in heart and testis, enhanced in skeletal muscle and tongue, and supported by extensive literature. Its disease associations include neurodegenerative and autoimmune neurological disorders in Open Targets, although those associations do not by themselves define the module mechanism.
- **Conclusion**: Established evidence supports CS as the best network anchor and as a marker of mitochondrial oxidative metabolism. The hypothesis that CS coordinates the cross-tissue module is plausible from its hub position and biochemical role, but direct regulatory control over the other genes is not established here.

#### SUCLA2

- **Related proteins** (co-abundance neighbors): ACADM (0.87), CS (0.85); STRING partners: ACADM (0.755), ATP5F1C (0.751), CS (0.96)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase ADP-forming subunit beta. Succinyl-CoA synthetase (SCS) is a mitochondrial matrix enzyme that acts as a heterodimer, being composed of an invariant alpha subunit and a substrate-specific beta subunit. The protein encoded by this gene is an ATP-specific SCS beta subunit that dimerizes with the SCS alpha subunit to form SCS-A, an essential component of the tricarboxylic acid cycle. SCS-A hydrolyzes ATP to convert succinate t…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome, encephalomyopathic form with methylmalonic aciduria (0.816); mitochondrial DNA depletion syndrome, encephalomyopathic form (0.581); neurodegenerative disease (0.485); mitochondrial disease (0.374); disease of peritoneum (0.372)
- **Europe PMC papers**: 1440
- **Why important**: SUCLA2 connects the tricarboxylic-acid-cycle component CS with ACADM and ATP5F1C in the STRING-supported network. It encodes the ATP-specific beta subunit of succinyl-CoA synthetase, linking succinyl-CoA and succinate metabolism to mitochondrial energy handling. It is mitochondrial, detected in both tissues, enriched in skeletal muscle and tongue, and associated with spermatogenic cell types. Its established disease associations include mitochondrial DNA depletion syndromes and other mitochondrial disorders.
- **Conclusion**: Established evidence supports SUCLA2 as a metabolic bridge between carbon-cycle activity and energy production. It is a strong candidate for explaining the shared module, but the co-abundance data do not demonstrate that SUCLA2 physically organizes the network or causes the observed tissue pattern.

#### ACADM

- **Related proteins** (co-abundance neighbors): SUCLA2 (0.87), GOT1 (0.84), CS (0.82); STRING partners: SUCLA2 (0.755)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA dehydrogenase medium chain. This gene encodes the medium-chain specific (C4 to C12 straight chain) acyl-Coenzyme A dehydrogenase. The homotetramer enzyme catalyzes the initial step of the mitochondrial fatty acid beta-oxidation pathway. Defects in this gene cause medium-chain acyl-CoA dehydrogenase deficiency, a disease characterized by hepatic dysfunction, fasting hypoglycemia, and encephalopathy, which can result in infant…
- **Diseases (Open Targets)**: medium chain acyl-CoA dehydrogenase deficiency (0.854); hereditary disease (0.516); rhabdomyolysis (0.370); short chain acyl-CoA dehydrogenase deficiency (0.349); Epileptic spasm (0.333)
- **Europe PMC papers**: 4795
- **Why important**: ACADM contributes the fatty-acid oxidation arm of the module and is connected to SUCLA2 and CS-related network structure. It encodes medium-chain acyl-CoA dehydrogenase, an enzyme catalyzing an early step in mitochondrial beta-oxidation. It is detected in heart and testis and shows enrichment in liver, skeletal muscle, tongue, hepatocytes, parietal cells, and esophageal apical cells. Its disease association with medium-chain acyl-CoA dehydrogenase deficiency is particularly well established, with additional links to rhabdomyolysis and related metabolic phenotypes.
- **Conclusion**: Established evidence supports ACADM as the fuel-substrate component of the module and connects the signal to fatty-acid use. The hypothesis that ACADM supplies carbon or reducing power to the CS-centered network is biochemically coherent, but this dataset does not establish substrate flux or causal coupling.

#### GOT1

- **Related proteins** (co-abundance neighbors): CS (0.84), ACADM (0.84); STRING partners: CS (0.908)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamic-oxaloacetic transaminase 1. Glutamic-oxaloacetic transaminase is a pyridoxal phosphate-dependent enzyme which exists in cytoplasmic and mitochondrial forms, GOT1 and GOT2, respectively.  GOT plays a role in amino acid metabolism and the urea and tricarboxylic acid cycles. The two enzymes are homodimeric and show close homology. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); Parkinson disease (0.375); Alzheimer disease (0.367); lysosomal storage disease (0.356); obesity disorder (0.172)
- **Europe PMC papers**: 3793
- **Why important**: GOT1 is connected to CS in STRING and occupies a position that can link amino-acid metabolism with oxaloacetate and tricarboxylic-acid-cycle chemistry. It encodes a pyridoxal-phosphate-dependent transaminase with cytoplasmic and mitochondrial forms and has established roles in amino-acid metabolism, gluconeogenesis, and aspartate and oxaloacetate handling. It is enhanced in heart muscle, skeletal muscle, and tongue and is associated with late primary spermatocytes and retinal ganglion cells. Its literature and disease associations include neurodegenerative disorders, Parkinson disease, Alzheimer disease, and metabolic phenotypes.
- **Conclusion**: Established evidence supports GOT1 as an intermediary-metabolism and carbon-balancing component. Its participation in a shared mitochondrial program is a reasonable hypothesis, but the supplied evidence does not determine which GOT1 isoform or compartment drives the co-abundance relationship.

#### ATP5F1C

- **Related proteins** (co-abundance neighbors): CS (0.87); STRING partners: CS (0.726), SUCLA2 (0.751)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP synthase F1 subunit gamma. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: late-onset Alzheimers disease (0.350); scleritis (0.189); diaphragm disorder (0.082); glioblastoma (0.044); external ear disorder (0.042)
- **Europe PMC papers**: 306
- **Why important**: ATP5F1C links the metabolic network to ATP synthase and oxidative phosphorylation through its STRING relationships with CS and SUCLA2. It encodes the gamma subunit of the mitochondrial ATP synthase F1 catalytic sector. It is detected in heart and testis and shows tissue and cell-type enhancement in tongue, esophageal suprabasal cells, and parietal cells. Its literature volume is more limited than that of the central metabolic enzymes, but its biochemical role is direct and functionally important; Open Targets also reports associations with neurological and other disorders.
- **Conclusion**: Established evidence supports ATP5F1C as the oxidative-phosphorylation output component of the module. Its peripheral network position suggests that it may report coupling to ATP production rather than define the entire module. Direct functional coupling to the other module proteins remains a hypothesis.

## Module 3

**Tissue pair**: heart and testis  
**Genes (20)**: ADD3, AHNAK, CAND2, CAT, GPS1, HSD17B4, DNM1L, DYNC1H1, EHD4, F13A1, FBLN1, AGL, GSN, GET3, KANK2, MYO1C, PYGB, RTCA, USP5, USO1

### Function

This module does not have a globally significant GO or KEGG term; no GO or KEGG term passed global correction, and STRING functional enrichment was absent. The network therefore supports a cautious, composite interpretation rather than a single established pathway. Its strongest internal structure connects USO1 with intracellular transport machinery and with PYGB, while separate links connect AHNAK, GET3, MYO1C, KANK2, USP5, DYNC1H1, DNM1L, EHD4 and F13A1. The annotated functions span ER-to-Golgi transport, tail-anchored protein insertion, cytoskeletal organization, vesicle and organelle movement, protein deubiquitination, mitochondrial and peroxisomal dynamics, glycogen metabolism, and peroxisomal fatty-acid metabolism. Thus, the most defensible function is a shared cellular-maintenance and trafficking module associated with muscle or germ-cell contexts, not a demonstrated unified biochemical pathway. The absence of enrichment does not invalidate the module.

**Cell composition.** The module is not dominated by secreted or plasma proteins, because only a minority have secreted-protein annotations. Nevertheless, F13A1 is secreted to blood and is associated with macrophages, megakaryocytes and platelets; FBLN1 is secreted to extracellular matrix; and GSN is secreted to blood. These genes could reflect extracellular material, vascular or blood-associated contributions, or sample composition rather than the core intracellular program. Most genes have low immune-cell specificity, although several show immune-cell-enhanced or immune-cell-enriched patterns, including F13A1, CAT, FBLN1, GSN and ADD3. HPA evidence more prominently points to tissue or cell-type heterogeneity: skeletal muscle, tongue, liver, brain, adipose tissue, myonuclei, cardiomyocytes, spermatocytes, spermatids, Leydig cells and several epithelial cell types occur among the annotations. Protein detection is broadly compatible with both heart and testis for much of the module, but several genes are detected in only one tissue or are not detected in either tissue. Overall, the module is neither a simple plasma-protein module nor a uniformly expressed housekeeping module; shared cell types, structural programs, or mixed tissue composition remain plausible explanations.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only two high-confidence within-module relationships: AGL–PYGB and CAT–HSD17B4. These are biologically interpretable, linking glycogen breakdown with AGL and PYGB, and linking catalase with peroxisomal fatty-acid metabolism through CAT and HSD17B4. The absence of other high-confidence STRING edges means that most co-abundance links are not established physical or functional interactions in STRING. hu.MAP repeatedly places AGL and PYGB together in glycogen-related complexes, with the same pair recurring across complexes of differing confidence and composition (hu.MAP huMAP3_08013.1) (hu.MAP huMAP3_06909.1) (hu.MAP huMAP3_01396.1) (hu.MAP huMAP3_08093.1) (hu.MAP huMAP3_10227.1) (hu.MAP huMAP3_09760.1) (hu.MAP huMAP3_13075.1) (hu.MAP huMAP3_11993.1) (hu.MAP huMAP3_12186.1). This convergence supports a real glycogen-metabolism submodule, but the pair represents only a small part of the full module and does not establish that all module members form one complex. No other module members occur in the listed hu.MAP complexes. Together, STRING and hu.MAP support a validated AGL–PYGB metabolic connection and a validated CAT–HSD17B4 association, while the broader module should be interpreted as a co-abundance network rather than a physical complex.

**STRING interactions (score >= 0.7)**: 2 of 190 gene pairs: AGL–PYGB (0.999); CAT–HSD17B4 (0.954)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08013.1 (PYGB, AGL; 2/8); huMAP3_06909.1 (PYGB, AGL; 2/9); huMAP3_01396.1 (PYGB, AGL; 2/10); huMAP3_08093.1 (PYGB, AGL; 2/12); huMAP3_10227.1 (PYGB, AGL; 2/14); huMAP3_09760.1 (PYGB, AGL; 2/15); huMAP3_13075.1 (PYGB, AGL; 2/15); huMAP3_11993.1 (PYGB, AGL; 2/20); huMAP3_12186.1 (PYGB, AGL; 2/23)

### Novelty

The module may be a new tissue-pair co-abundance observation, but it cannot be called a newly discovered molecular pathway. Its novelty is supported only in the limited sense that the full combination of genes and cross-tissue co-abundance structure is not represented by the listed STRING or hu.MAP relationships. Absence from those resources alone does not prove novelty, because databases favor well-studied physical interactions and curated complexes, whereas co-abundance can arise from shared regulation, cell composition, organelle state, or correlated tissue abundance. The presence of established AGL–PYGB and CAT–HSD17B4 relationships, together with the absence of global GO or KEGG enrichment and the heterogeneous HPA annotations, argues for novelty as a potentially useful network signature rather than as evidence for a previously unknown complex or pathway.

**Hypothesis.** Hypothesis: in heart and testis, this module may report coordinated cellular maintenance involving intracellular trafficking, cytoskeletal and membrane organization, organelle quality control, and energy-substrate handling. USO1, GET3, DYNC1H1, MYO1C and EHD4 could represent trafficking and motor-related processes; DNM1L and HSD17B4 could reflect mitochondrial or peroxisomal homeostasis; and AGL with PYGB could represent glycogen mobilization. AHNAK, KANK2, ADD3 and GSN could connect these processes to membrane or actin architecture. The shared signal may be driven by common muscle-like or germ-cell structural demands, with additional contribution from blood, vascular, stromal or extracellular components. This is a mechanistic model to test, not an established conclusion from enrichment.

### Important genes

#### USO1

- **Related proteins** (co-abundance neighbors): CAND2 (0.86), MYO1C (0.84), KANK2 (0.83), GET3 (0.82), PYGB (0.82), DYNC1H1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: USO1 vesicle transport factor. The protein encoded by this gene is a peripheral membrane protein which recycles between the cytosol and the Golgi apparatus during interphase. It is regulated by phosphorylation: dephosphorylated protein associates with the Golgi membrane and dissociates from the membrane upon phosphorylation. Ras-associated protein 1 recruits this protein to coat protein complex II (COPII) vesicles during buddin…
- **Diseases (Open Targets)**: psoriatic arthritis (0.184); bipolar disorder (0.150); retinitis pigmentosa (0.085); cone dystrophy (0.076); cone-rod dystrophy (0.076)
- **Europe PMC papers**: 546
- **Why important**: USO1 is the highest-centrality node in the supplied network and connects several otherwise distinct module components, including CAND2, MYO1C, KANK2, GET3, PYGB and DYNC1H1. Its established role in ER-to-Golgi vesicle transport provides a plausible trafficking anchor for the module. HPA describes tissue enhancement in skeletal muscle and cell-type enhancement in myonuclei, with protein detected in testis. Its disease and literature evidence is less extensive than that of several other candidates, making its central network position especially informative.
- **Conclusion**: Established: USO1 is a Golgi-associated vesicle-transport factor and a central co-abundance node with a muscle-related HPA pattern. Hypothesis: USO1 may coordinate the trafficking component of the shared heart–testis module. The network does not establish direct physical interactions between USO1 and its module neighbors.

#### AHNAK

- **Related proteins** (co-abundance neighbors): CAND2 (0.88), GET3 (0.87), HSD17B4 (0.85), FBLN1 (0.85), F13A1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: AHNAK nucleoprotein. The protein encoded by this gene is a large (700 kDa) structural scaffold protein consisting of a central domain with 128 aa repeats. The encoded protein may play a role in such diverse processes as blood-brain barrier formation, cell structure and migration, cardiac calcium channel regulation, and tumor metastasis. A much shorter variant encoding a 17 kDa isoform exists for this gene, and the sho…
- **Diseases (Open Targets)**: Aganglionic megacolon (0.266); neoplasm (0.108); hepatocellular carcinoma (0.093); cancer (0.085); melanoma (0.085)
- **Europe PMC papers**: 2886
- **Why important**: AHNAK is among the more connected nodes and links CAND2, GET3, HSD17B4, FBLN1 and F13A1. Its large structural-scaffold function, plasma-membrane and cytosolic localization, and reported roles in cell structure, migration, membrane repair and cardiac calcium-channel regulation make it a plausible interface between membrane architecture and the heterogeneous extracellular or metabolic signals in the module. It has strong HPA detection in both heart and testis and substantial literature coverage.
- **Conclusion**: Established: AHNAK is a large structural scaffold with documented membrane-related functions and is detected in both relevant tissues. Hypothesis: AHNAK may integrate membrane repair or structural state with trafficking and peroxisomal or extracellular signals. The co-abundance data do not prove that it regulates the other genes.

#### CAND2

- **Related proteins** (co-abundance neighbors): AHNAK (0.88), USO1 (0.86), USP5 (0.85), RTCA (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nuclear bodies; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cullin associated and neddylation dissociated 2 (putative). Predicted to enable TBP-class protein binding activity. Predicted to be involved in SCF complex assembly; positive regulation of transcription, DNA-templated; and protein ubiquitination. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: atrial fibrillation (0.568); cardiac arrhythmia (0.488); cardiomyopathy (0.477); heart failure (0.462); atrial flutter (0.414)
- **Europe PMC papers**: 369
- **Why important**: CAND2 is a central connector among AHNAK, USO1, USP5 and RTCA. HPA associates it with skeletal muscle, tongue, cardiomyocytes, myonuclei and several neuronal cell types, and detects it in both heart and testis. Its annotated links to SCF complex assembly, ubiquitination and transcriptional regulation provide a possible regulatory layer connecting protein turnover with the module's transport and structural processes. It also has notable associations with atrial fibrillation, cardiomyopathy, heart failure and related cardiac phenotypes.
- **Conclusion**: Established: CAND2 is a network connector with muscle and cardiomyocyte-related HPA evidence and annotations involving ubiquitination and SCF assembly. Hypothesis: it may help couple protein stability or transcriptional regulation to the shared tissue state. A causal role in the module is not demonstrated.

#### AGL

- **Related proteins** (co-abundance neighbors): GPS1 (0.86); STRING partners: PYGB (0.999)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_08013.1, huMAP3_06909.1, huMAP3_01396.1, huMAP3_08093.1, huMAP3_10227.1, huMAP3_09760.1, huMAP3_13075.1, huMAP3_11993.1, huMAP3_12186.1
- **Function (MyGene.info)**: amylo-alpha-1,6-glucosidase and 4-alpha-glucanotransferase. This gene encodes the glycogen debrancher enzyme which is involved in glycogen degradation. This enzyme has two independent catalytic activities which occur at different sites on the protein: a 4-alpha-glucotransferase activity and a amylo-1,6-glucosidase activity. Mutations in this gene are associated with glycogen storage disease although a wide range of enzymatic and clinical variability occurs…
- **Diseases (Open Targets)**: glycogen storage disease III (0.831); disorder of glycogen metabolism (0.768); glycogen storage disease XV (0.608); hereditary disease (0.507); Acute rhabdomyolysis (0.463)
- **Europe PMC papers**: 4441
- **Why important**: AGL is the strongest metabolic anchor because it has a direct high-confidence STRING relationship with PYGB and occurs with PYGB across the listed hu.MAP complexes (hu.MAP huMAP3_08013.1) (hu.MAP huMAP3_06909.1) (hu.MAP huMAP3_01396.1) (hu.MAP huMAP3_08093.1) (hu.MAP huMAP3_10227.1) (hu.MAP huMAP3_09760.1) (hu.MAP huMAP3_13075.1) (hu.MAP huMAP3_11993.1) (hu.MAP huMAP3_12186.1). It encodes the glycogen debrancher enzyme and is associated with glycogen-storage disease and glycogen-metabolism disorders. HPA gives AGL a group-enriched skeletal-muscle and tongue pattern and myonuclear cell-type enhancement, although protein is detected in testis rather than heart in the supplied evidence.
- **Conclusion**: Established: AGL participates in glycogen degradation, is linked to glycogen-storage disease, and forms a supported metabolic pair with PYGB in STRING and hu.MAP. Hypothesis: the AGL–PYGB pair may reflect shared regulation of glycogen availability in the heart–testis module. This pair does not establish that the remaining genes participate directly in glycogen metabolism.

#### PYGB

- **Related proteins** (co-abundance neighbors): USO1 (0.82); STRING partners: AGL (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, testis
- **hu.MAP 3.0**: huMAP3_08013.1, huMAP3_06909.1, huMAP3_01396.1, huMAP3_08093.1, huMAP3_10227.1, huMAP3_09760.1, huMAP3_13075.1, huMAP3_11993.1, huMAP3_12186.1
- **Function (MyGene.info)**: glycogen phosphorylase B. The protein encoded by this gene is a glycogen phosphorylase found predominantly in the brain. The encoded protein forms homodimers which can associate into homotetramers, the enzymatically active form of glycogen phosphorylase. The activity of this enzyme is positively regulated by AMP and negatively regulated by ATP, ADP, and glucose-6-phosphate. This enzyme catalyzes the rate-determining step i…
- **Diseases (Open Targets)**: neurodegenerative disease (0.419); prostate carcinoma (0.329); Short stature (0.259); neoplasm (0.102); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 901
- **Why important**: PYGB is the direct STRING partner of AGL and recurs with AGL in every listed hu.MAP complex (hu.MAP huMAP3_08013.1) (hu.MAP huMAP3_06909.1) (hu.MAP huMAP3_01396.1) (hu.MAP huMAP3_08093.1) (hu.MAP huMAP3_10227.1) (hu.MAP huMAP3_09760.1) (hu.MAP huMAP3_13075.1) (hu.MAP huMAP3_11993.1) (hu.MAP huMAP3_12186.1). It catalyzes the rate-determining step of glycogen degradation, making it complementary to AGL's debranching activity. HPA detects PYGB protein in both heart and testis, while its network connection to USO1 places the glycogen pair near the module's trafficking component. Its disease and literature evidence is more focused than that of some structural candidates.
- **Conclusion**: Established: PYGB is a glycogen-phosphorylase enzyme with a supported AGL relationship and detection in both tissues. Hypothesis: PYGB may connect glycogen mobilization to intracellular trafficking or cell-state regulation through the USO1-associated co-abundance pattern. The data do not show a direct PYGB–USO1 physical interaction.

#### HSD17B4

- **Related proteins** (co-abundance neighbors): AHNAK (0.85), MYO1C (0.82), GET3 (0.81); STRING partners: CAT (0.954)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Peroxisomes; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydroxysteroid 17-beta dehydrogenase 4. The protein encoded by this gene is a bifunctional enzyme that is involved in the peroxisomal beta-oxidation pathway for fatty acids. It also acts as a catalyst for the formation of 3-ketoacyl-CoA intermediates from both straight-chain and 2-methyl-branched-chain fatty acids. Defects in this gene that affect the peroxisomal fatty acid beta-oxidation activity are a cause of D-bifunctional protein d…
- **Diseases (Open Targets)**: d-bifunctional protein deficiency (0.830); Perrault syndrome 1 (0.761); Perrault syndrome (0.736); hereditary disease (0.488); hearing loss disorder (0.370)
- **Europe PMC papers**: 1624
- **Why important**: HSD17B4 is connected in the module to AHNAK, MYO1C and GET3 and has a high-confidence STRING relationship with CAT. It is a peroxisomal bifunctional enzyme involved in fatty-acid beta-oxidation and steroid metabolism, with disease associations including D-bifunctional protein deficiency and Perrault syndrome. HPA shows liver enhancement, hepatocyte and alveolar-cell enhancement, and protein detection in both heart and testis. Its position provides a metabolic contrast to the glycogen-centered AGL–PYGB pair.
- **Conclusion**: Established: HSD17B4 is a peroxisomal fatty-acid metabolism enzyme with a supported CAT relationship and relevant inherited-disease associations. Hypothesis: the CAT–HSD17B4 pair may report coordinated peroxisomal redox and lipid-metabolic state within the shared module. The network does not establish that this peroxisomal process is the dominant function of the module.

## Module 4

**Tissue pair**: heart and testis  
**Genes (15)**: ALDH3A2, ASPH, ATP1A1, MTHFD1, CISD2, CYRIB, DSTN, DNM2, FKBP3, HEBP1, EPHX1, MESD, PANK4, SCARB2, TFRC

### Function

No GO/KEGG term passed global correction, and STRING supplied no supplementary enriched term; therefore the module should not be assigned a single statistically established pathway. Its structure instead suggests a heterogeneous cellular maintenance module linking membrane trafficking and endocytosis through DNM2, ion-gradient and membrane physiology through ATP1A1, iron uptake and endosomal biology through TFRC and SCARB2, one-carbon metabolism through MTHFD1, cytoskeletal regulation through DSTN and CYRIB, and endoplasmic-reticulum, calcium or proteostasis-related functions through ASPH, CISD2, MESD and FKBP3. The strongest within-module connectivity is centered on DNM2 and CYRIB, with additional bridging through MTHFD1, ASPH and ATP1A1. This pattern is more consistent with coordinated cellular homeostasis, membrane remodeling, intracellular trafficking and metabolic support than with a narrowly defined pathway. These functional interpretations are gene-level annotations and network-based inferences, not globally significant enrichment claims.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only TFRC is annotated as secreted to blood, while MESD is intracellular and membrane-associated, and the remaining genes are not annotated as secreted. It is also not uniformly blood-cell enriched. Most genes have low immune-cell specificity, although SCARB2, TFRC, ASPH, CYRIB and related genes show selected immune or myeloid-cell signals. HPA shows a mixture of tissue-enhanced and low-specificity genes, including liver, adipose, parathyroid, bone-marrow and blood-vessel signals, together with cell-type signals from cardiomyocytes, late spermatids, hepatocytes, erythrocyte progenitors, neutrophils and several epithelial or vascular populations. Protein detection is broad in both heart and testis, which supports biological presence in the paired tissues, but the HPA pattern also means that shared cell types, vascular components, blood contamination or common cellular programs could contribute to the conserved co-abundance signal. The module therefore should not be interpreted as exclusively heart-specific or testis-specific.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, between SCARB2 and TFRC. This supports a known connection involving endosomal or lysosomal membrane biology and iron-receptor trafficking, but it does not establish the whole co-abundance module as a known physical complex. hu.MAP identifies FKBP3 and MESD together in C1 and C2. In each case, the module contributes only a small subset of the broader reported complex, so these results support possible shared protein-folding, trafficking or regulatory context rather than membership of the entire module in either complex. The absence of additional STRING or hu.MAP relationships indicates that most module edges are not currently represented by these resources; it may reflect co-regulation, tissue composition, indirect biology, context dependence or incomplete interaction coverage.

**STRING interactions (score >= 0.7)**: 1 of 105 gene pairs: SCARB2–TFRC (0.917)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13998.1 (FKBP3, MESD; 2/23); huMAP3_14982.1 (FKBP3, MESD; 2/28)

### Novelty

The module may be a novel tissue-pair co-abundance observation, because most of its within-module relationships are not represented as high-confidence STRING interactions or as shared hu.MAP complex membership. However, it is not a newly discovered biological system: the individual genes have established functions, disease associations and substantial literature, and the SCARB2-TFRC relationship is already known. The defensible novelty claim is therefore limited to the particular conserved co-abundance pattern in heart and testis, not to the genes, their functions, or a newly proven physical complex. Its novelty would require validation in independent cohorts, control for blood and cell-type composition, and ideally experimental testing of the inferred connections.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular stress-and-transport program present in relevant heart and testis cell populations. DNM2 and ATP1A1 could organize membrane remodeling, endocytosis and electrochemical homeostasis; TFRC and SCARB2 could couple iron uptake to endosomal or lysosomal handling; MTHFD1 could provide one-carbon metabolic capacity for biosynthetic demand; and ASPH, CISD2, FKBP3, MESD, CYRIB and DSTN could connect calcium, organelle, protein-folding, cytoskeletal and trafficking responses. This is a mechanistic model rather than an established pathway assignment. An alternative explanation is that the signal partly reflects shared vascular, immune, epithelial or other cellular composition across the two tissues.

### Important genes

#### DNM2

- **Related proteins** (co-abundance neighbors): ALDH3A2 (0.89), ATP1A1 (0.86), MTHFD1 (0.85), CYRIB (0.84), ASPH (0.81), HEBP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 2. Dynamins represent one of the subfamilies of GTP-binding proteins. These proteins share considerable sequence similarity over the N-terminal portion of the molecule, which contains the GTPase domain. Dynamins are associated with microtubules. They have been implicated in cell processes such as endocytosis and cell motility, and in alterations of the membrane that accompany certain activities such …
- **Diseases (Open Targets)**: autosomal dominant centronuclear myopathy (0.844); Charcot-Marie-Tooth disease dominant intermediate B (0.830); fetal akinesia-cerebral and retinal hemorrhage syndrome (0.739); autosomal dominant Charcot-Marie-Tooth disease type 2M (0.715); centronuclear myopathy (0.692)
- **Europe PMC papers**: 2412
- **Why important**: DNM2 is the most connected node in the module and links ALDH3A2, ATP1A1, MTHFD1, CYRIB, ASPH and HEBP1. Its established role in GTPase-dependent membrane remodeling, endocytosis, vesicle transport and cytoskeletal processes gives it a plausible organizing role. It is detected in both heart and testis and has extensive literature and strong disease associations involving centronuclear myopathy and Charcot-Marie-Tooth disease.
- **Conclusion**: Established: DNM2 is a central network node with well-supported roles in endocytosis, vesicle handling and cytoskeletal biology, and it is relevant to muscle and neuromuscular disease. Hypothesis: DNM2 may act as a structural or regulatory anchor for the shared membrane-trafficking component of this module.

#### MTHFD1

- **Related proteins** (co-abundance neighbors): ASPH (0.91), DNM2 (0.85), TFRC (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methylenetetrahydrofolate dehydrogenase, cyclohydrolase and formyltetrahydrofolate synthetase 1. This gene encodes a protein that possesses three distinct enzymatic activities, 5,10-methylenetetrahydrofolate dehydrogenase, 5,10-methenyltetrahydrofolate cyclohydrolase and 10-formyltetrahydrofolate synthetase. Each of these activities catalyzes one of three sequential reactions in the interconversion of 1-carbon derivatives of tetrahydrofolate, which are substrates for methionine, thymidylate, …
- **Diseases (Open Targets)**: combined immunodeficiency and megaloblastic anemia with or without hyperhomocysteinemia (0.773); severe combined immunodeficiency (0.473); neural tube defects, folate-sensitive (0.414); isolated spina bifida (0.376); atrial fibrillation (0.332)
- **Europe PMC papers**: 1939
- **Why important**: MTHFD1 connects ASPH, DNM2 and TFRC and is annotated as a trifunctional enzyme in folate-mediated one-carbon metabolism supporting methionine, thymidylate and purine synthesis. Its HPA profile includes cardiomyocytes, erythrocyte progenitors and hepatocytes, and it has substantial literature plus associations with combined immunodeficiency, megaloblastic anemia, neural-tube defects and atrial fibrillation.
- **Conclusion**: Established: MTHFD1 supplies core biosynthetic and one-carbon metabolic functions and is expressed in cell types relevant to both tissues. Hypothesis: its co-abundance may indicate metabolic support for membrane turnover, iron-dependent cellular activity or tissue maintenance rather than a specific folate-enrichment module.

#### ATP1A1

- **Related proteins** (co-abundance neighbors): DNM2 (0.86), CYRIB (0.84), PANK4 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 is a connected membrane node linking DNM2, CYRIB and PANK4. Its established Na+/K+-ATPase function maintains sodium and potassium gradients required for osmoregulation, transport and electrical excitability. It is relevant to muscle and cardiac physiology, is detected in testis, and has extensive literature and disease associations including cardiac and neuromuscular conditions.
- **Conclusion**: Established: ATP1A1 is a core ion-homeostasis and plasma-membrane protein with clear relevance to excitable tissues. Hypothesis: it may connect the module's membrane-trafficking signal to the electrochemical demands of heart and testis cells.

#### TFRC

- **Related proteins** (co-abundance neighbors): MTHFD1 (0.82), ASPH (0.80); STRING partners: SCARB2 (0.917)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes, Lysosomes; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transferrin receptor. This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: TFRC-related combined immunodeficiency (0.623); type 2 diabetes mellitus (0.518); mucopolysaccharidosis type 2 (0.490); diabetes mellitus (0.471); diabetic retinopathy (0.343)
- **Europe PMC papers**: 14164
- **Why important**: TFRC links MTHFD1 and ASPH and is the member of the module with a high-confidence STRING relationship, namely SCARB2-TFRC. Its established function is receptor-mediated iron uptake through endocytosis, with roles in iron homeostasis, hypoxia response and erythropoiesis. HPA places it in endosomes and lysosomes, detects it in both tissues, and shows signals in erythrocyte progenitors, macrophages and monocytes. It also has the largest literature volume among the selected genes and disease associations involving immunodeficiency and diabetes-related conditions.
- **Conclusion**: Established: TFRC is a biologically well-supported iron-uptake and endocytic component, and its relationship with SCARB2 is independently represented in STRING. Hypothesis: TFRC may provide a functional bridge between iron availability, endosomal trafficking and the metabolic demands represented by MTHFD1.

#### SCARB2

- **Related proteins** (co-abundance neighbors): ALDH3A2 (0.89); STRING partners: TFRC (0.917)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: scavenger receptor class B member 2. The protein encoded by this gene is a type III glycoprotein that is located primarily in limiting membranes of lysosomes and endosomes. Earlier studies in mice and rat suggested that this protein may participate in membrane transportation and the reorganization of endosomal/lysosomal compartment. The protein deficiency in mice was reported to impair cell membrane transport processes and cause pelv…
- **Diseases (Open Targets)**: action myoclonus-renal failure syndrome (0.779); progressive myoclonus epilepsy (0.647); hereditary disease (0.470); self-limited epilepsy with centrotemporal spikes (0.416); Unverricht-Lundborg syndrome (0.381)
- **Europe PMC papers**: 1732
- **Why important**: SCARB2 is directly connected to ALDH3A2 in the co-abundance network and has the module's high-confidence STRING relationship with TFRC. It is an endosomal and lysosomal membrane protein annotated in receptor-mediated endocytosis, autophagy, lysosomal targeting and glycolipid catabolism. HPA shows broad myeloid and mononuclear-phagocyte signals, while protein is detected in both heart and testis. Its established disease associations include action myoclonus-renal failure syndrome and progressive myoclonus epilepsy.
- **Conclusion**: Established: SCARB2 is a lysosomal and endosomal trafficking protein with an independently supported relationship to TFRC. Hypothesis: SCARB2 may mark a lysosome-endosome arm of the shared module, potentially influenced by phagocytic or myeloid-cell contribution rather than by the parenchymal cells alone.

## Module 5

**Tissue pair**: heart and testis  
**Genes (35)**: ANXA6, BLVRA, CAPN1, CBR1, CKAP4, CSRP1, DYNC1I2, DHX9, DPYSL2, EZR, FERMT2, FLNA, FLNB, HNRNPK, HNRNPL, HSPA8, IMPDH2, IQGAP1, ITGB1, CAMK2D, LGALS3, MATR3, PDCD6IP, PGM2, PLS3, RO60, SEC23A, SPTBN1, WARS1, TAGLN2, TKT, TLN1, VPS35, WDR1, XRCC6

### Function

The module is best interpreted as a conserved cell-adhesion and actin-cytoskeleton organization program. The primary evidence is the global enrichment of actin filament-based process (GO:BP actin filament-based process; q_global = 0.00233), actin cytoskeleton organization (GO:BP actin cytoskeleton organization; q_global = 0.00285), actin filament binding (GO:MF actin filament binding; q_global = 0.0065), focal adhesion and cell-substrate junction (GO:CC focal adhesion; q_global = 0.0168) (GO:CC cell-substrate junction; q_global = 0.0168), anchoring junction (GO:CC anchoring junction; q_global = 0.0233), cortical cytoskeleton organization (GO:BP cortical cytoskeleton organization; q_global = 0.0274), leading edge membrane (GO:CC leading edge membrane; q_global = 0.0274), and regulation of protein localization to the cell periphery (GO:BP positive regulation of protein localization to cell periphery; q_global = 0.0106) (GO:BP regulation of protein localization to cell periphery; q_global = 0.047). The vesicle and cytosol terms (GO:CC vesicle; q_global = 0.0239) (GO:CC cytosol; q_global = 0.0378) indicate that membrane trafficking and cytosolic protein organization accompany this adhesion-cytoskeletal program. The module therefore appears to connect integrin-based adhesion and cortical actin with vesicle movement, cell-shape control, and intracellular organization. RNA-binding and metabolic proteins are also present, but their presence does not override the coherent adhesion and cytoskeletal signal.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module: the HPA summary reports only a small secreted component, with LGALS3 explicitly secreted to blood, while most proteins are intracellular or membrane-associated. Most genes have low tissue specificity, and many are detected in both heart and testis, consistent with a broadly deployed cellular program rather than a uniquely heart-specific or testis-specific pathway. The HPA single-cell data show enrichment in epithelial cells, megakaryocytes, platelets, and several vascular or stromal populations. Several genes also show monocyte or myeloid-cell enrichment, although most genes have low immune-cell specificity. Thus, the shared module could reflect a genuine adhesion and cytoskeletal program in resident cells, but contribution from shared vascular, epithelial, platelet, or other cellular populations should be considered. The heart and testis protein-detection results support broad detectability overall, but gene-level differences such as absent heart detection for ITGB1, EZR, TLN1, FLNA, and related proteins warrant caution about cell composition and measurement effects.

**GO/KEGG enrichment**: 16 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP actin filament-based process | 0.00233 | CAMK2D, CSRP1, EZR, FERMT2, FLNA, FLNB, IQGAP1, ITGB1, PDCD6IP, PLS3, SPTBN1, TAGLN2, TLN1, WDR1 |
| GO:BP actin cytoskeleton organization | 0.00285 | CSRP1, EZR, FERMT2, FLNA, FLNB, IQGAP1, ITGB1, PDCD6IP, PLS3, SPTBN1, TAGLN2, TLN1, WDR1 |
| GO:MF actin filament binding | 0.0065 | EZR, FERMT2, FLNA, FLNB, IQGAP1, PLS3, SPTBN1, TAGLN2, TLN1, WDR1 |
| GO:BP positive regulation of protein localization to cell periphery | 0.0106 | EZR, ITGB1, LGALS3, SPTBN1, VPS35 |
| GO:CC focal adhesion | 0.0168 | ANXA6, CAPN1, CSRP1, EZR, FERMT2, FLNA, FLNB, HNRNPK, HSPA8, IQGAP1, ITGB1, PDCD6IP, TLN1 |
| GO:CC cell-substrate junction | 0.0168 | ANXA6, CAPN1, CSRP1, EZR, FERMT2, FLNA, FLNB, HNRNPK, HSPA8, IQGAP1, ITGB1, PDCD6IP, TLN1 |
| GO:CC anchoring junction | 0.0233 | ANXA6, CAPN1, CSRP1, EZR, FERMT2, FLNA, FLNB, HNRNPK, HSPA8, IQGAP1, ITGB1, PDCD6IP, TLN1, WDR1 |
| GO:CC vesicle | 0.0239 | ANXA6, BLVRA, CAMK2D, CAPN1, CBR1, CKAP4, CSRP1, DPYSL2, DYNC1I2, EZR, FLNA, FLNB, HNRNPK, HNRNPL, HSPA8, IMPDH2, IQGAP1, ITGB1, LGALS3, PDCD6IP, PGM2, SEC23A, SPTBN1, TAGLN2, TKT, TLN1, VPS35, WARS1, WDR1, XRCC6 |
| GO:MF protein-containing complex binding | 0.0246 | DHX9, EZR, FERMT2, FLNA, FLNB, HSPA8, IQGAP1, ITGB1, LGALS3, PLS3, SPTBN1, TAGLN2, TLN1, WDR1, XRCC6 |
| GO:MF actin binding | 0.0268 | EZR, FERMT2, FLNA, FLNB, IQGAP1, ITGB1, PLS3, SPTBN1, TAGLN2, TLN1, WDR1 |
| GO:BP cortical cytoskeleton organization | 0.0274 | EZR, IQGAP1, PDCD6IP, TLN1, WDR1 |
| GO:CC leading edge membrane | 0.0274 | EZR, FERMT2, ITGB1, SPTBN1, TLN1 |
| GO:CC actin cytoskeleton | 0.0313 | DHX9, EZR, FERMT2, FLNA, FLNB, HNRNPK, IQGAP1, PDCD6IP, PLS3, SPTBN1, TAGLN2, WDR1 |
| GO:BP cytoskeleton organization | 0.0361 | CSRP1, DPYSL2, EZR, FERMT2, FLNA, FLNB, IQGAP1, ITGB1, PDCD6IP, PLS3, SPTBN1, TAGLN2, TLN1, WDR1 |
| GO:CC cytosol | 0.0378 | BLVRA, CAMK2D, CAPN1, CBR1, DHX9, DPYSL2, DYNC1I2, EZR, FERMT2, FLNA, FLNB, HSPA8, IMPDH2, IQGAP1, LGALS3, PDCD6IP, PGM2, PLS3, RO60, SEC23A, SPTBN1, TAGLN2, TKT, TLN1, VPS35, WARS1, WDR1, XRCC6 |

### STRING and hu.MAP

STRING supports a known interaction backbone rather than an isolated statistical co-abundance pattern. The strongest and most coherent relationships connect the integrin and adhesion machinery, including ITGB1 with FLNA, FLNB, TLN1, FERMT2, and LGALS3; the actin-associated scaffold group involving FLNA, FLNB, TLN1, IQGAP1, EZR, and WDR1; and the RNA-processing group involving DHX9, HNRNPK, HNRNPL, MATR3, HSPA8, and XRCC6. The PGM2-TKT relationship provides a metabolic submodule. STRING functional terms independently support cytosol, vesicles, focal adhesion, anchoring junction, actin cytoskeleton, and actin-filament binding (11 supplementary STRING terms; within-query FDR 0.00051–0.0183), but these are supplementary and do not replace the global GO evidence. hu.MAP provides additional support for an RNA-binding complex centered on HNRNPL, MATR3, and HNRNPK (hu.MAP huMAP3_10625.1), smaller HNRNP-containing complexes (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10659.1), a PLS3-EZR complex (hu.MAP huMAP3_10281.1), ITGB1-LGALS3 complexes (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1), and a WDR1-SPTBN1 complex (hu.MAP huMAP3_09165.1). Together, these results indicate that the module contains several established interaction substructures linked by the abundance network.

**STRING interactions (score >= 0.7)**: 30 of 595 gene pairs: CAPN1–TLN1 (0.77); DHX9–HNRNPK (0.939); DHX9–HNRNPL (0.901); DHX9–HSPA8 (0.703); DHX9–MATR3 (0.786); DHX9–XRCC6 (0.819); EZR–FLNA (0.761); EZR–IQGAP1 (0.938); EZR–TLN1 (0.797); FERMT2–FLNA (0.852); FERMT2–FLNB (0.757); FERMT2–ITGB1 (0.796); FERMT2–TLN1 (0.705); FLNA–FLNB (0.979); FLNA–IQGAP1 (0.952); FLNA–ITGB1 (0.993); FLNA–TLN1 (0.998); FLNA–WDR1 (0.874); FLNB–ITGB1 (0.939); FLNB–TLN1 (0.995); HNRNPK–HNRNPL (0.99); HNRNPK–HSPA8 (0.791); HNRNPK–MATR3 (0.923); HNRNPK–XRCC6 (0.738); HNRNPL–MATR3 (0.757); IQGAP1–TLN1 (0.893); ITGB1–LGALS3 (0.931); ITGB1–TLN1 (0.999); PGM2–TKT (0.953); TLN1–WDR1 (0.744)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Cytosol (FDR = 0.00051, 27 genes); Keyword Cytoplasm (FDR = 0.00068, 28 genes); Keyword Phosphoprotein (FDR = 0.00078, 34 genes); Component Cytosol (FDR = 0.0092, 29 genes); Component Vesicle (FDR = 0.0092, 30 genes); Component Focal adhesion (FDR = 0.0101, 13 genes); TISSUES Integument (FDR = 0.0102, 21 genes); Keyword Host-virus interaction (FDR = 0.0108, 10 genes); COMPARTMENTS Anchoring junction (FDR = 0.0126, 13 genes); Component Actin cytoskeleton (FDR = 0.0155, 11 genes); Component Anchoring junction (FDR = 0.0155, 14 genes); Function Actin filament binding (FDR = 0.0164, 10 genes); TISSUES Skin (FDR = 0.017, 17 genes); TISSUES Organism form (FDR = 0.018, 24 genes); Component Cytoskeleton (FDR = 0.0183, 16 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10625.1 (HNRNPL, MATR3, HNRNPK; 3/57); huMAP3_05721.1 (HNRNPL, MATR3; 2/6); huMAP3_10281.1 (PLS3, EZR; 2/9); huMAP3_07581.1 (HNRNPL, MATR3; 2/21); huMAP3_10503.1 (ITGB1, LGALS3; 2/27); huMAP3_10659.1 (HNRNPL, HNRNPK; 2/28); huMAP3_09165.1 (WDR1, SPTBN1; 2/39); huMAP3_10980.1 (ITGB1, LGALS3; 2/44); huMAP3_09336.1 (ITGB1, LGALS3; 2/50)

### Novelty

The module should not be described as a newly discovered adhesion pathway. Its central components and many of its relationships are already established in STRING, hu.MAP, gene annotations, and the literature, especially the ITGB1-FLNA-FLNB-TLN1 adhesion scaffold and the HNRNP-MATR3 RNA-processing group. The potentially novel result is the conserved co-abundance organization of these components across heart and testis, including the coupling of adhesion, actin remodeling, vesicle biology, RNA regulation, and metabolism in one cross-tissue module. However, database coverage is incomplete and the module may partly reflect shared cell populations, including vascular, epithelial, platelet, or stromal cells. Therefore the appropriate conclusion is a potentially novel cross-tissue network context, not a proven new molecular complex or a new biological mechanism. Validation should test whether the co-abundance structure persists after cell-type deconvolution and whether the proposed links are present in the same cells.

**Hypothesis.** Mechanistic hypothesis: in shared vascular, epithelial, germ-cell-associated, or other adherent cell populations of heart and testis, an ITGB1-centered adhesion apparatus recruits TLN1, FLNA, FLNB, FERMT2, EZR, IQGAP1, and PLS3 to organize cortical actin and focal or anchoring junctions. CAMK2D and calcium-sensitive membrane regulators may tune this scaffold, while PDCD6IP, SEC23A, DYNC1I2, VPS35, and related proteins coordinate vesicle trafficking and recycling. In parallel, the HNRNPL-HNRNPK-MATR3-DHX9-RNA-binding group may regulate the transcripts needed to maintain this structural state, and TKT with PGM2 may support the associated metabolic demand. This is a hypothesis because the co-abundance data and annotations establish association and plausibility, not direct physical coupling or causal regulation in heart and testis.

### Important genes

#### ITGB1

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.94), PLS3 (0.91), RO60 (0.86), PDCD6IP (0.86), CAPN1 (0.86), EZR (0.85), TLN1 (0.84), TKT (0.82); STRING partners: FERMT2 (0.796), FLNA (0.993), FLNB (0.939), LGALS3 (0.931), TLN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10503.1, huMAP3_10980.1, huMAP3_09336.1
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is a central adhesion node in the module and is connected to the actin and focal-adhesion machinery through FLNA, FLNB, TLN1, FERMT2, EZR, and LGALS3 in STRING. It contributes to nearly all of the primary adhesion, actin, junction, vesicle, and peripheral-localization terms (12 globally significant GO/KEGG terms, q_global 0.00233–0.047; see the table). Its established function as an integrin subunit links extracellular recognition to intracellular cytoskeletal organization, and its disease associations include inflammatory and immune-related disorders. It is also represented in several hu.MAP integrin-galectin complexes (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1).
- **Conclusion**: Established evidence identifies ITGB1 as a core molecular anchor for the module's adhesion interpretation. The cross-tissue module may reflect shared integrin-dependent organization, but the lack of HPA protein detection in the sampled heart and testis argues that cell-type composition and assay sensitivity must be resolved before assigning it a universal role in both tissues.

#### EZR

- **Related proteins** (co-abundance neighbors): ANXA6 (0.88), PGM2 (0.88), ITGB1 (0.85), PDCD6IP (0.84), DPYSL2 (0.83), CAMK2D (0.82), TKT (0.82); STRING partners: FLNA (0.761), IQGAP1 (0.938), TLN1 (0.797)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_10281.1
- **Function (MyGene.info)**: ezrin. The cytoplasmic peripheral membrane protein encoded by this gene functions as a protein-tyrosine kinase substrate in microvilli. As a member of the ERM protein family, this protein serves as an intermediate between the plasma membrane and the actin cytoskeleton. This protein plays a key role in cell surface structure adhesion, migration and organization, and it has been implicated in various human…
- **Diseases (Open Targets)**: hair color (0.477); non-small cell lung carcinoma (0.397); lung adenocarcinoma (0.382); autosomal recessive non-syndromic intellectual disability (0.370); glaucoma (0.347)
- **Europe PMC papers**: 4982
- **Why important**: EZR has broad participation across the primary terms, including actin organization, actin binding, focal adhesion, cortical cytoskeleton, leading edge membrane, vesicles, and peripheral protein localization (16 globally significant GO/KEGG terms, q_global 0.00233–0.047; see the table). It occupies a connecting position between membrane-associated proteins and actin, with STRING relationships to IQGAP1, FLNA, and TLN1, and it is part of the hu.MAP PLS3-EZR complex (hu.MAP huMAP3_10281.1). Its established function as an ERM-family linker provides a direct mechanistic bridge between plasma membrane structure, adhesion, migration, and actin.
- **Conclusion**: Established evidence supports EZR as a structural integrator of membrane and cortical actin processes in this module. Its testis detection but absence of heart detection in HPA means that the shared network signal may depend on particular cell populations rather than uniform expression throughout both organs.

#### FLNA

- **Related proteins** (co-abundance neighbors): TLN1 (0.90), CSRP1 (0.88), CKAP4 (0.85), IQGAP1 (0.84), RO60 (0.83); STRING partners: EZR (0.761), FERMT2 (0.852), FLNB (0.979), IQGAP1 (0.952), ITGB1 (0.993), TLN1 (0.998), WDR1 (0.874)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is a major scaffold node with extensive links to TLN1, FLNB, ITGB1, IQGAP1, EZR, FERMT2, and WDR1 in STRING. It is represented across the primary actin, focal-adhesion, junction, vesicle, and cytoskeletal terms (11 globally significant GO/KEGG terms, q_global 0.00233–0.0378; see the table). Its established function is to crosslink actin and connect it to membrane glycoproteins and receptor complexes. Its disease associations include several skeletal and neurodevelopmental syndromes, and its literature support is substantial.
- **Conclusion**: Established evidence makes FLNA a plausible mechanical scaffold and an important contributor to the module's adhesion-cytoskeleton core. The co-abundance data do not establish that FLNA drives the module or that its disease mechanisms operate in the heart-testis context.

#### CAMK2D

- **Related proteins** (co-abundance neighbors): MATR3 (0.87), ANXA6 (0.85), RO60 (0.85), IMPDH2 (0.84), EZR (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Primary cilium tip, Primary cilium transition zone, Principal piece; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium/calmodulin dependent protein kinase II delta. The product of this gene belongs to the serine/threonine protein kinase family and to the Ca(2+)/calmodulin-dependent protein kinase subfamily. Calcium signaling is crucial for several aspects of plasticity at glutamatergic synapses. In mammalian cells, the enzyme is composed of four different chains: alpha, beta, gamma, and delta. The product of this gene is a delta chain. Alternative splicing re…
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.632); atrial fibrillation (0.556); CAMK2D-related neurodevelopmental disorder and dilated cardiomyopathy (0.503); heart conduction disease (0.449); heart failure (0.438)
- **Europe PMC papers**: 2254
- **Why important**: CAMK2D provides a tissue-relevant regulatory connection because HPA marks it as heart-muscle enhanced and detects it in cardiomyocytes, myonuclei, and Sertoli cells. It contributes to actin filament-based process, vesicle biology, cytosol, and peripheral protein localization (4 globally significant GO/KEGG terms, q_global 0.00233–0.047; see the table), and it has a central position among the module's links to MATR3, ANXA6, RO60, IMPDH2, and EZR. Its established calcium/calmodulin-dependent kinase function and roles in membrane depolarization and heart contraction make it a plausible signal-dependent regulator. Its disease associations include atrial fibrillation, heart failure, conduction disease, and a cardiomyopathy-related disorder.
- **Conclusion**: Established evidence supports CAMK2D as a biologically important calcium-responsive regulator that may connect contractile or membrane signaling to the structural module. Its contribution to the shared module beyond the heart remains a hypothesis, despite HPA evidence in Sertoli cells.

#### MATR3

- **Related proteins** (co-abundance neighbors): HNRNPL (0.95), RO60 (0.89), XRCC6 (0.87), HNRNPK (0.87), CAMK2D (0.87), IMPDH2 (0.87), TKT (0.84), DHX9 (0.82), SPTBN1 (0.82), PDCD6IP (0.80); STRING partners: DHX9 (0.786), HNRNPK (0.923), HNRNPL (0.757)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, testis
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_05721.1, huMAP3_07581.1
- **Function (MyGene.info)**: matrin 3. This gene encodes a nuclear matrix protein, which is proposed to stabilize certain messenger RNA species. Mutations of this gene are associated with distal myopathy 2, which often includes vocal cord and pharyngeal weakness. Alternatively spliced transcript variants, including read-through transcripts composed of the upstream small nucleolar RNA host gene 4 (non-protein coding) and matrin 3 gene s…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.735); distal myopathy with vocal cord weakness (0.569); neurodegenerative disease (0.529); distal myopathy (0.384); hereditary disease (0.193)
- **Europe PMC papers**: 1756
- **Why important**: MATR3 is one of the most highly connected genes in the co-abundance graph and links the RNA-associated part of the module to RO60, HNRNPL, HNRNPK, DHX9, XRCC6, CAMK2D, IMPDH2, and TKT. It is represented in multiple hu.MAP RNA-binding complexes (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07581.1), and STRING supports its relationships with HNRNPK, HNRNPL, and DHX9. Its established function as a nuclear matrix and RNA-associated protein, together with its association with distal myopathy and neuromuscular disease, is relevant to a module shared by a contractile organ and a reproductive organ.
- **Conclusion**: Established evidence supports MATR3 as a key RNA-processing or nuclear-organization component that may explain why the module includes a coherent RNA-binding subnetwork. Its connection to the actin-adhesion program is inferred from network structure and co-abundance, not demonstrated as a direct causal pathway.

## Module 6

**Tissue pair**: heart and testis  
**Genes (20)**: HSPA5, CAPN2, CAP2, EIF3C, EIF3L, GPD2, HSP90AA1, LTA4H, ATIC, SUN2, FARSB, KARS1, QARS1, RARS1, CCT5, CCT3, CCT7, CCT8, XPO1, XPNPEP1

### Function

The module is best interpreted as a conserved intracellular protein-homeostasis and biosynthetic-support module. Its strongest primary evidence is ATP-dependent protein folding chaperone activity and protein folding (GO:MF ATP-dependent protein folding chaperone; q_global = 0.000188) (GO:MF protein folding chaperone; q_global = 0.0016) (GO:BP protein folding; q_global = 0.0458), with a coherent chaperonin-containing T-complex formed by CCT3, CCT5, CCT7, and CCT8 (GO:CC chaperonin-containing T-complex; q_global = 0.00392). These four CCT subunits occupy the central, highly connected part of the network and are supported by known STRING relationships (5 supplementary STRING terms; within-query FDR 0.0024–0.0238) and multiple hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). The module also contains a translation-support arm consisting of EIF3C, EIF3L, RARS1, FARSB, QARS1, and KARS1, consistent with protein metabolism and translation-related evidence (GO:BP protein metabolic process; q_global = 0.00157) (STRING Keyword Protein biosynthesis; within-query FDR = 0.008) (STRING Keyword Aminoacyl-tRNA synthetase; within-query FDR = 0.0247) (STRING Process Translation; within-query FDR = 0.0262) (STRING Process tRNA aminoacylation for protein translation; within-query FDR = 0.0262). The telomere, chromosome-organization, DNA-biosynthetic, and Cajal-body terms (32 globally significant GO/KEGG terms, q_global 0.000241–0.0411; see the table) are globally corrected primary evidence, but they are driven largely by the shared CCT3-CCT5-CCT7-CCT8-HSP90AA1 annotation pattern and should be interpreted as functional annotations of this chaperone-centered system rather than proof that the whole module is a dedicated telomere machine. The sperm-egg recognition terms (GO:BP binding of sperm to zona pellucida; q_global = 0.0322) (GO:BP sperm-egg recognition; q_global = 0.0322) are also globally corrected, but their overlap is restricted to the CCT subunits and may reflect annotation or cell-state associations rather than a complete reproductive pathway. Overall, the network supports coordinated folding, translation, protein localization, and stress-adaptive maintenance of cellular proteins.

**Cell composition.** This is not primarily a plasma, secreted-protein, or blood-cell module. The HPA summary reports only a small secreted component, low immune-cell specificity for nearly all genes, and protein detection in both heart and testis for most members. Most genes have low tissue specificity, so the shared signal is compatible with broadly expressed intracellular housekeeping machinery rather than a heart-specific or testis-specific secretome. At the same time, several genes show cell-type-enhanced patterns relevant to germ-cell or reproductive compartments, including late primary spermatocytes, early or late spermatids, oocytes, epididymal cells, and testis-associated cells. CAP2 is tissue-enhanced in skeletal muscle and detected in heart, while KARS1 is enhanced in cardiomyocytes and late spermatogenic cells. These observations support a combination of broadly required proteostasis and translation machinery with contributions from shared specialized cell states. The data do not support interpreting the module as primarily caused by blood contamination.

**GO/KEGG enrichment**: 42 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF ATP-dependent protein folding chaperone | 0.000188 | CCT3, CCT5, CCT7, CCT8, HSP90AA1, HSPA5 |
| GO:BP RNA-templated DNA biosynthetic process | 0.000241 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP telomere maintenance via telomerase | 0.000241 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP telomere maintenance via telomere lengthening | 0.000241 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP regulation of telomere maintenance via telomerase | 0.000241 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP positive regulation of telomere maintenance via telomerase | 0.000241 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP regulation of telomere maintenance via telomere lengthening | 0.000241 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP positive regulation of telomere maintenance via telomere lengthening | 0.000241 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP regulation of DNA biosynthetic process | 0.000241 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP positive regulation of DNA biosynthetic process | 0.000241 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP regulation of telomere maintenance | 0.00096 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP positive regulation of telomere maintenance | 0.00096 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP regulation of chromosome organization | 0.00096 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP DNA biosynthetic process | 0.00096 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP positive regulation of chromosome organization | 0.00096 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |

### STRING and hu.MAP

STRING provides strong prior support for the central CCT relationship: CCT3, CCT5, CCT7, and CCT8 are mutually connected, and they connect to HSP90AA1 and HSPA5 (5 supplementary STRING terms; within-query FDR 0.0024–0.0238). STRING also supports a translation-related subnetwork involving EIF3C- EIF3L and the aminoacyl-tRNA synthetases FARSB, KARS1, QARS1, and RARS1 (4 supplementary STRING terms; within-query FDR 0.008–0.0262). The direct STRING interaction list therefore confirms that important portions of the module reproduce established protein-protein relationships rather than representing entirely unexplored pairings. hu.MAP independently identifies repeated complexes containing the four CCT subunits (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), a complex containing QARS1, RARS1, and KARS1 (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), and complexes containing EIF3C and EIF3L (hu.MAP huMAP3_01276.1) (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1). The LTA4H-ATIC-XPNPEP1 grouping is represented in hu.MAP (hu.MAP huMAP3_14442.1), although those genes have weaker or absent STRING support within the supplied evidence. Thus, the module appears to join several known complexes and interaction neighborhoods through co-abundance, while some cross-complex links remain network-level associations rather than established physical interactions.

**STRING interactions (score >= 0.7)**: 22 of 190 gene pairs: ATIC–CCT7 (0.881); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT3–HSP90AA1 (0.767); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT5–HSP90AA1 (0.868); CCT5–HSPA5 (0.727); CCT7–CCT8 (0.999); CCT7–EIF3C (0.728); CCT7–HSP90AA1 (0.849); CCT7–HSPA5 (0.783); CCT8–HSP90AA1 (0.823); CCT8–HSPA5 (0.701); EIF3C–EIF3L (0.999); FARSB–KARS1 (0.813); FARSB–RARS1 (0.706); HSP90AA1–HSPA5 (0.968); KARS1–QARS1 (0.999); KARS1–RARS1 (0.999); QARS1–RARS1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Protein folding chaperone (FDR = 0.0024, 6 genes); Function ATP-dependent protein folding chaperone (FDR = 0.0043, 5 genes); Pfam TCP-1/cpn60 chaperonin family (FDR = 0.0069, 4 genes); Keyword Protein biosynthesis (FDR = 0.008, 6 genes); Function Unfolded protein binding (FDR = 0.0134, 6 genes); Process Peptide metabolic process (FDR = 0.0175, 8 genes); Process Toxin transport (FDR = 0.0175, 5 genes); Process Positive regulation of DNA biosynthetic process (FDR = 0.0175, 5 genes); Keyword ATP-binding (FDR = 0.0238, 10 genes); Keyword Chaperone (FDR = 0.0238, 6 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 0.0247, 4 genes); Keyword Cytoplasm (FDR = 0.0247, 16 genes); Process Translation (FDR = 0.0262, 6 genes); Process tRNA aminoacylation for protein translation (FDR = 0.0262, 4 genes); Process Binding of sperm to zona pellucida (FDR = 0.0262, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_02637.1 (QARS1, RARS1, KARS1; 3/14); huMAP3_13688.1 (QARS1, RARS1, KARS1; 3/14); huMAP3_14442.1 (LTA4H, ATIC, XPNPEP1; 3/57); huMAP3_01276.1 (EIF3C, EIF3L; 2/17); huMAP3_13175.1 (EIF3C, EIF3L; 2/20); huMAP3_11246.1 (EIF3C, EIF3L; 2/24)

### Novelty

The module is not a wholly new protein complex: its CCT core, EIF3C-EIF3L pair, and aminoacyl-tRNA synthetase group are already represented in STRING and hu.MAP (STRING Function Protein folding chaperone; within-query FDR = 0.0024) (STRING Function ATP-dependent protein folding chaperone; within-query FDR = 0.0043) (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 0.0069) (STRING Keyword Protein biosynthesis; within-query FDR = 0.008) (STRING Function Unfolded protein binding; within-query FDR = 0.0134) (STRING Keyword Aminoacyl-tRNA synthetase; within-query FDR = 0.0247) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1) (hu.MAP huMAP3_01276.1) (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1). The likely novelty is instead the conserved co-abundance organization of these known components across heart and testis, together with their observed connection to SUN2, XPO1, HSP90AA1, HSPA5, metabolic enzymes, and cytoskeletal or proteolytic components. Absence of some edges from STRING or hu.MAP does not establish novelty, because those resources capture physical interactions or curated complexes rather than every tissue-level co-abundance relationship. Accordingly, this should be described as a potentially novel cross-tissue regulatory or abundance module built partly from established molecular machinery, not as a newly discovered molecular complex.

**Hypothesis.** Hypothesis: in both heart and testis, a shared demand for high-throughput protein production, folding, localization, and quality control produces coordinated abundance of the CCT chaperonin, HSP90AA1-HSPA5 chaperones, translation-initiation factors, and aminoacyl-tRNA synthetases. The CCT core may help maintain folding-competent actin, tubulin, and other client proteins, while EIF3C-EIF3L and the tRNA synthetase group support translation. SUN2 and XPO1 could connect this proteostasis-translation state to nuclear organization and nucleocytoplasmic trafficking, consistent with the nuclear-localization evidence (GO:BP protein localization to nucleus; q_global = 0.00326) (GO:BP positive regulation of protein localization to nucleus; q_global = 0.0275) (GO:BP regulation of protein localization to nucleus; q_global = 0.0411). The telomere and Cajal-body annotations suggest a possible additional role in maintaining nuclear RNA and chromosome-associated processes, but this mechanistic extension requires experimental testing and should not be treated as established for the complete module.

### Important genes

#### CCT3

- **Related proteins** (co-abundance neighbors): EIF3C (0.93), HSP90AA1 (0.91), CCT8 (0.91), CCT7 (0.90), RARS1 (0.87), FARSB (0.85), CCT5 (0.85), QARS1 (0.82), HSPA5 (0.81); STRING partners: CCT5 (0.999), CCT7 (0.999), CCT8 (0.999), HSP90AA1 (0.767)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in heart, testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a highly connected hub and belongs to every listed CCT-centered hu.MAP complex (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It participates in all globally corrected module terms (42 globally significant GO/KEGG terms, q_global 0.000188–0.0458; see the table), including chaperone activity, protein folding, telomere-related annotations, nuclear and Cajal-body localization, chromosome organization, and sperm-egg recognition. Its established function is as a subunit of the ATP-dependent CCT chaperonin that folds proteins such as actin and tubulin. It has substantial literature support and disease associations including neurodevelopmental and neurodegenerative conditions and atrial fibrillation.
- **Conclusion**: Established: CCT3 is a central structural and functional component of the module's chaperonin core. Hypothesis: variation in CCT3 abundance may influence the shared heart-testis module by changing folding capacity and indirectly affecting nuclear or telomere-associated processes.

#### CCT5

- **Related proteins** (co-abundance neighbors): EIF3C (0.92), FARSB (0.89), CCT7 (0.88), RARS1 (0.88), SUN2 (0.88), XPO1 (0.85), CCT3 (0.85), HSP90AA1 (0.84), CCT8 (0.83); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999), HSP90AA1 (0.868), HSPA5 (0.727)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is a highly connected CCT hub with repeated STRING support and membership in the principal hu.MAP CCT complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It contributes to every globally corrected term in the supplied analysis (42 globally significant GO/KEGG terms, q_global 0.000188–0.0458; see the table). Its established role is ATP-dependent folding of newly synthesized proteins within TRiC, and it shows cell-type enhancement in late primary spermatocytes. It has substantial literature volume and disease associations including hereditary sensory and autonomic neuropathy with spastic paraplegia and neurodegenerative disease.
- **Conclusion**: Established: CCT5 is a core chaperonin component and a plausible contributor to protein-folding capacity in both tissues. Hypothesis: its reproductive-cell enhancement may help explain why this broadly expressed chaperone module is conserved in testis as well as heart.

#### HSP90AA1

- **Related proteins** (co-abundance neighbors): EIF3C (0.92), CCT3 (0.91), CCT7 (0.85), CCT5 (0.84), CCT8 (0.82); STRING partners: CCT3 (0.767), CCT5 (0.868), CCT7 (0.849), CCT8 (0.823), HSPA5 (0.968)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein 90 alpha family class A member 1. The protein encoded by this gene is an inducible molecular chaperone that functions as a homodimer. The encoded protein aids in the proper folding of specific target proteins by use of an ATPase activity that is modulated by co-chaperones. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: cancer (0.643); plasma cell myeloma (0.404); non-small cell lung carcinoma (0.394); dengue disease (0.375); Orthomyxoviridae infectious disease (0.375)
- **Europe PMC papers**: 8215
- **Why important**: HSP90AA1 connects strongly to the CCT subunits and HSPA5 in STRING and is a major bridge between the CCT core and stress-responsive chaperone biology (5 supplementary STRING terms; within-query FDR 0.0024–0.0238). It contributes to the globally corrected chaperone, protein-folding, DNA-biosynthetic, telomere, chromosome-organization, and nuclear-localization terms (28 globally significant GO/KEGG terms, q_global 0.000188–0.0458; see the table). Its established function is an inducible ATP-dependent molecular chaperone that stabilizes specific client proteins. It has extensive literature support and disease associations including cancer, plasma-cell myeloma, and infectious disease.
- **Conclusion**: Established: HSP90AA1 is a major proteostasis and stress-response component linked to the CCT core. Hypothesis: HSP90AA1 may buffer tissue-specific stress while coordinating folding of clients connected to nuclear maintenance, but the module does not by itself establish a direct telomere mechanism.

#### EIF3C

- **Related proteins** (co-abundance neighbors): CCT8 (0.95), XPNPEP1 (0.93), CCT3 (0.93), HSP90AA1 (0.92), CCT5 (0.92), ATIC (0.91), CCT7 (0.90), HSPA5 (0.89), LTA4H (0.84); STRING partners: CCT7 (0.728), EIF3L (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, testis
- **hu.MAP 3.0**: huMAP3_01276.1, huMAP3_13175.1, huMAP3_11246.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C is among the most connected genes in the module and links the CCT hub to EIF3L, XPNPEP1, ATIC, HSP90AA1, and multiple CCT subunits. It is present in the protein-metabolism primary term (GO:BP protein metabolic process; q_global = 0.00157) and in STRING translation and protein-biosynthesis terms (STRING Keyword Protein biosynthesis; within-query FDR = 0.008) (STRING Keyword Cytoplasm; within-query FDR = 0.0247) (STRING Process Translation; within-query FDR = 0.0262). Its established function is as a subunit of the eukaryotic translation-initiation factor complex, supporting formation of the cytoplasmic translation-initiation complex. It is represented in several hu.MAP eIF3 complexes (hu.MAP huMAP3_01276.1) (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1) and has substantial literature volume and cancer-related disease associations.
- **Conclusion**: Established: EIF3C supplies a translation-initiation anchor that complements the chaperone core. Hypothesis: coordinated EIF3C and CCT abundance may couple synthesis of new proteins to their immediate folding and quality control in heart and testis.

#### KARS1

- **Related proteins** (co-abundance neighbors): HSPA5 (0.84); STRING partners: FARSB (0.813), QARS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, testis
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: lysyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. Lysyl-tRNA synthetase is a homodimer localized to the cytoplasm which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Alternatively spliced transcript variants encoding different…
- **Diseases (Open Targets)**: leukoencephalopathy, progressive, infantile-onset, with or without deafness (0.753); deafness, congenital, and adult-onset progressive leukoencephalopathy (0.714); autosomal recessive nonsyndromic hearing loss 89 (0.685); Charcot-Marie-Tooth disease recessive intermediate B (0.670); deafness (0.534)
- **Europe PMC papers**: 232
- **Why important**: KARS1 is part of the aminoacyl-tRNA synthetase cluster supported by STRING and hu.MAP (STRING Keyword Protein biosynthesis; within-query FDR = 0.008) (STRING Keyword Aminoacyl-tRNA synthetase; within-query FDR = 0.0247) (STRING Process Translation; within-query FDR = 0.0262) (STRING Process tRNA aminoacylation for protein translation; within-query FDR = 0.0262) (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), and it is connected in the module to HSPA5. Its established function is lysine-tRNA charging for translation, with additional reported immune-related functions. HPA shows enhancement in cardiomyocytes and late primary or late spermatogenic cells, directly matching the two tissues represented by the conserved module. It has disease associations including progressive leukoencephalopathy and hereditary hearing disorders.
- **Conclusion**: Established: KARS1 represents the translation-supply arm of the module and has tissue-relevant cell-type evidence in cardiomyocytes and spermatogenic cells. Hypothesis: KARS1 may help couple the biosynthetic demands of these energetically and developmentally specialized cells to chaperone-mediated protein maturation.

## Module 8

**Tissue pair**: heart and testis  
**Genes (5)**: L2HGDH, NDUFA9, NDUFS2, NDUFS4, NDUFV1

### Function

This is a mitochondrial oxidative-phosphorylation module centered on respiratory-chain complex I. The strongest primary evidence is the globally corrected enrichment for NADH dehydrogenase activity and the NADH dehydrogenase and respiratory-chain complexes (GO:MF NADH dehydrogenase (ubiquinone) activity; q_global = 0.00508) (GO:CC NADH dehydrogenase complex; q_global = 0.00508) (GO:CC respiratory chain complex I; q_global = 0.00508), together with mitochondrial electron transfer from NADH to ubiquinone (GO:BP mitochondrial electron transport, NADH to ubiquinone; q_global = 0.00642). The same four genes also support proton-motive-force-driven ATP synthesis, aerobic and respiratory electron transport, and ATP biosynthesis (7 globally significant GO/KEGG terms, q_global 0.0191–0.0293; see the table), while the transporter terms (GO:MF oxidoreduction-driven active transmembrane transporter activity; q_global = 0.0163), (GO:MF primary active transmembrane transporter activity; q_global = 0.0333), and (GO:MF active monoatomic ion transmembrane transporter activity; q_global = 0.0333) are consistent with proton translocation by respiratory complex I. The KEGG endocannabinoid-signaling and non-alcoholic-fatty-liver-disease terms (KEGG Retrograde endocannabinoid signaling - Homo sapiens (human); q_global = 0.00642), (KEGG Non-alcoholic fatty liver disease - Homo sapiens (human); q_global = 0.0222) should be interpreted as pathway-context annotations rather than evidence that the module is specifically an endocannabinoid or liver module. L2HGDH is not included in any globally corrected GO/KEGG term, but its mitochondrial location and role in oxidation of L-2-hydroxyglutarate to alpha-ketoglutarate indicate a possible metabolic connection to the respiratory network. Overall, the module most plausibly reports coordinated mitochondrial complex I abundance and respiratory capacity in heart and testis.

**Cell composition.** The module is not composed of plasma or secreted proteins: all module proteins are mitochondrial and the secreted-gene count is zero. It is also not predominantly blood-cell enriched. HPA assigns low immune-cell specificity to most genes, with only L2HGDH showing immune-cell enhancement in basophils. All module proteins are detected in both heart muscle and testis, supporting genuine representation in both tissues rather than absence caused by limited protein detection. Most genes have low tissue specificity, while NDUFS2 is tissue enhanced in skeletal muscle and tongue and L2HGDH is tissue enhanced in kidney. Cell-type annotations are heterogeneous, including late spermatids, parietal cells, photoreceptors, and proximal tubule cells. Thus, the shared heart–testis signal is more consistent with a broadly distributed mitochondrial energy-demand program, potentially accentuated by tissue-specific cellular composition, than with a blood or secreted-protein artifact.

**GO/KEGG enrichment**: 20 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF NADH dehydrogenase (ubiquinone) activity | 0.00508 | NDUFA9, NDUFS2, NDUFS4, NDUFV1 |
| GO:CC NADH dehydrogenase complex | 0.00508 | NDUFA9, NDUFS2, NDUFS4, NDUFV1 |
| GO:CC respiratory chain complex I | 0.00508 | NDUFA9, NDUFS2, NDUFS4, NDUFV1 |
| GO:BP mitochondrial electron transport, NADH to ubiquinone | 0.00642 | NDUFA9, NDUFS2, NDUFS4, NDUFV1 |
| KEGG Retrograde endocannabinoid signaling - Homo sapiens (human) | 0.00642 | NDUFA9, NDUFS2, NDUFS4, NDUFV1 |
| GO:MF oxidoreduction-driven active transmembrane transporter activity | 0.0163 | NDUFA9, NDUFS2, NDUFS4, NDUFV1 |
| GO:BP proton motive force-driven mitochondrial ATP synthesis | 0.0191 | NDUFA9, NDUFS2, NDUFS4, NDUFV1 |
| GO:BP proton motive force-driven ATP synthesis | 0.0222 | NDUFA9, NDUFS2, NDUFS4, NDUFV1 |
| KEGG Non-alcoholic fatty liver disease - Homo sapiens (human) | 0.0222 | NDUFA9, NDUFS2, NDUFS4, NDUFV1 |
| GO:BP aerobic electron transport chain | 0.0256 | NDUFA9, NDUFS2, NDUFS4, NDUFV1 |
| GO:BP ATP synthesis coupled electron transport | 0.0256 | NDUFA9, NDUFS2, NDUFS4, NDUFV1 |
| GO:BP mitochondrial ATP synthesis coupled electron transport | 0.0256 | NDUFA9, NDUFS2, NDUFS4, NDUFV1 |
| GO:BP ATP biosynthetic process | 0.0293 | NDUFA9, NDUFS2, NDUFS4, NDUFV1 |
| GO:MF primary active transmembrane transporter activity | 0.0333 | NDUFA9, NDUFS2, NDUFS4, NDUFV1 |
| GO:MF active monoatomic ion transmembrane transporter activity | 0.0333 | NDUFA9, NDUFS2, NDUFS4, NDUFV1 |

### STRING and hu.MAP

STRING reports very strong pairwise relationships among the four complex I genes NDUFA9, NDUFS2, NDUFS4, and NDUFV1, forming a densely connected known interaction core. STRING supplementary enrichment independently links these genes to NADH dehydrogenase activity and complex I deficiency (STRING NetworkNeighborAL NADH dehydrogenase (ubiquinone) activity; within-query FDR = 0.0013), (STRING DISEASES Mitochondrial complex I deficiency; within-query FDR = 0.0023), while the phenotype terms involving neurological, visual, cardiac, and leukodystrophy features (11 supplementary STRING terms; within-query FDR 0.003–0.0031) are consistent with the established multisystem consequences of mitochondrial dysfunction but are not globally corrected module evidence. hu.MAP identifies the same four genes together in multiple complex I assemblies (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1), with smaller overlapping complex-I assemblies also containing three of them (hu.MAP huMAP3_08132.1), (hu.MAP huMAP3_02819.1). This convergence indicates that the central subgraph is a known physical and functional complex rather than an incidental co-abundance association. L2HGDH has no STRING partner and no hu.MAP complex assignment in the supplied data; its connection to NDUFV1 is therefore less established and may represent metabolic co-regulation, indirect association, or a tissue-specific abundance relationship.

**STRING interactions (score >= 0.7)**: 6 of 10 gene pairs: NDUFA9–NDUFS2 (0.999); NDUFA9–NDUFS4 (0.999); NDUFA9–NDUFV1 (0.999); NDUFS2–NDUFS4 (0.999); NDUFS2–NDUFV1 (0.999); NDUFS4–NDUFV1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Retrograde endocannabinoid signaling (FDR = 0.0013, 4 genes); NetworkNeighborAL NADH dehydrogenase (ubiquinone) activity (FDR = 0.0013, 4 genes); DISEASES Mitochondrial complex I deficiency (FDR = 0.0023, 4 genes); KEGG Non-alcoholic fatty liver disease (FDR = 0.0023, 4 genes); HPO Progressive cerebellar ataxia (FDR = 0.003, 4 genes); HPO Intellectual disability, severe (FDR = 0.003, 5 genes); HPO Abnormal CNS myelination (FDR = 0.003, 5 genes); HPO Strabismus (FDR = 0.0031, 5 genes); HPO Pigmentary retinopathy (FDR = 0.0031, 4 genes); HPO Nystagmus (FDR = 0.0031, 5 genes); HPO Optic atrophy (FDR = 0.0031, 5 genes); HPO Emotional lability (FDR = 0.0031, 4 genes); HPO Hypertrichosis (FDR = 0.0031, 4 genes); HPO Ventricular septal defect (FDR = 0.0031, 4 genes); HPO Leukodystrophy (FDR = 0.0031, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14018.1 (NDUFS4, NDUFS2, NDUFV1, NDUFA9; 4/48); huMAP3_06397.1 (NDUFS4, NDUFS2, NDUFV1, NDUFA9; 4/49); huMAP3_09982.1 (NDUFS4, NDUFS2, NDUFV1, NDUFA9; 4/49); huMAP3_09567.1 (NDUFS4, NDUFS2, NDUFV1, NDUFA9; 4/52); huMAP3_14878.1 (NDUFS4, NDUFS2, NDUFV1, NDUFA9; 4/53); huMAP3_08132.1 (NDUFS4, NDUFS2, NDUFV1; 3/24); huMAP3_02819.1 (NDUFS4, NDUFV1, NDUFA9; 3/34)

### Novelty

The module’s central biological interpretation is not a new discovery: the four-gene complex I core is already strongly represented in STRING and hu.MAP, and the individual genes have extensive prior literature and disease annotation. The potentially novel aspect is the conserved co-abundance configuration shared by heart and testis, especially the inclusion of L2HGDH alongside the complex I core. However, absence of L2HGDH from STRING or hu.MAP does not establish novelty, because those resources capture selected physical interactions and curated or inferred complexes rather than every tissue-specific co-expression relationship. A defensible conclusion is that this is a biologically credible replication or tissue-contextualization of a known mitochondrial complex I program, with a testable but presently unproven L2HGDH-linked extension rather than a wholly new molecular complex.

**Hypothesis.** Hypothesis: in both heart and testis, cellular energy demand or mitochondrial remodeling coordinately regulates complex I abundance and L-2-hydroxyglutarate metabolism. NDUFA9, NDUFS2, NDUFS4, and NDUFV1 could form the respiratory-chain backbone that supports NADH oxidation, proton translocation, and ATP production, while L2HGDH could couple carbon-metabolite oxidation to the available mitochondrial redox state. The direct complex I relationships are established by STRING and hu.MAP, but the functional coupling between L2HGDH and this complex-I module remains a hypothesis that should be tested with tissue-resolved expression, protein-complex, metabolite, and respiratory-flux measurements.

Web sources: https://www.ahajournals.org/doi/10.1161/CIRCRESAHA.118.314284; https://pmc.ncbi.nlm.nih.gov/articles/PMC7699753/; https://pmc.ncbi.nlm.nih.gov/articles/PMC9805526/; https://www.frontiersin.org/journals/molecular-biosciences/articles/10.3389/fmolb.2021.798353/full; https://pubmed.ncbi.nlm.nih.gov/36462614/

### Important genes

#### NDUFV1

- **Related proteins** (co-abundance neighbors): L2HGDH (0.87), NDUFS4 (0.86), NDUFS2 (0.85); STRING partners: NDUFA9 (0.999), NDUFS2 (0.999), NDUFS4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, testis
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1, huMAP3_08132.1, huMAP3_02819.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit V1. The mitochondrial respiratory chain provides energy to cells via oxidative phosphorylation and consists of four membrane-bound electron-transporting protein complexes (I-IV) and an ATP synthase (complex V). This gene encodes a 51 kDa subunit of the NADH:ubiquinone oxidoreductase complex I; a large complex with at least 45 nuclear and mitochondrial encoded subunits that liberates electrons from NAD…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.788); mitochondrial complex I deficiency, nuclear type 4 (0.724); mitochondrial complex I deficiency, nuclear type 1 (0.685); Leigh syndrome (0.635); type 2 diabetes mellitus (0.609)
- **Europe PMC papers**: 4567
- **Why important**: NDUFV1 is the most central gene in the co-abundance subgraph and connects to L2HGDH as well as the other complex I members. It encodes the complex I core subunit carrying the NADH-binding site and is present in every globally corrected functional term (20 globally significant GO/KEGG terms, q_global 0.00508–0.0424; see the table). It is also present in every listed hu.MAP complex (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1) (hu.MAP huMAP3_08132.1) (hu.MAP huMAP3_02819.1) and has strong STRING relationships with the other core genes. Its extensive literature and disease associations with complex I deficiency and Leigh syndrome make it the strongest anchor for the module’s respiratory interpretation.
- **Conclusion**: Established evidence supports NDUFV1 as a central NADH-entry and complex I component that explains much of the module’s function. Its link to L2HGDH is an observed network association, but a direct biochemical or regulatory connection between the two proteins is not established by the supplied evidence.

#### NDUFS2

- **Related proteins** (co-abundance neighbors): NDUFA9 (0.86), NDUFV1 (0.85); STRING partners: NDUFA9 (0.999), NDUFS4 (0.999), NDUFV1 (0.999)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, testis
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1, huMAP3_08132.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S2. The protein encoded by this gene is a core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (complex I). Mammalian mitochondrial complex I is composed of at least 43 different subunits, 7 of which are encoded by the mitochondrial genome, and the rest are the products of nuclear genes. The iron-sulfur protein fraction of complex I is made up of 7 subunits, including this g…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.758); mitochondrial complex I deficiency, nuclear type 6 (0.665); type 2 diabetes mellitus (0.608); mitochondrial disease (0.596); Parkinson disease (0.588)
- **Europe PMC papers**: 1723
- **Why important**: NDUFS2 is a core complex I subunit in the iron-sulfur protein fraction and participates in electron transfer toward ubiquinone. It is one of the four genes in every primary globally corrected term (20 globally significant GO/KEGG terms, q_global 0.00508–0.0424; see the table), has strong STRING connections to all other complex-I members in the module, and occurs in six hu.MAP assemblies (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1) (hu.MAP huMAP3_08132.1). Its established associations with complex I deficiency, mitochondrial disease, Parkinson disease, and diabetes provide substantial disease relevance.
- **Conclusion**: Established evidence supports NDUFS2 as a core catalytic and structural contributor to complex I electron transfer. The heart–testis co-abundance pattern is consistent with shared respiratory demand, but the module does not by itself demonstrate tissue-specific regulation or a disease mechanism in either tissue.

#### NDUFS4

- **Related proteins** (co-abundance neighbors): NDUFV1 (0.86); STRING partners: NDUFA9 (0.999), NDUFS2 (0.999), NDUFV1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, testis
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1, huMAP3_08132.1, huMAP3_02819.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit S4. This gene encodes an nuclear-encoded accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (complex I, or NADH:ubiquinone oxidoreductase). Complex I removes electrons from NADH and passes them to the electron acceptor ubiquinone. Mutations in this gene can cause mitochondrial complex I deficiencies such as Leigh syndrome. Alternative splicing results in multiple tran…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.800); Leigh syndrome (0.775); mitochondrial complex I deficiency, nuclear type 1 (0.721); type 2 diabetes mellitus (0.689); diabetes mellitus (0.662)
- **Europe PMC papers**: 2283
- **Why important**: NDUFS4 is a complex I accessory subunit with a prominent position in the known interaction network and membership in all listed hu.MAP assemblies (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1) (hu.MAP huMAP3_08132.1) (hu.MAP huMAP3_02819.1). It participates in every globally corrected GO/KEGG term (20 globally significant GO/KEGG terms, q_global 0.00508–0.0424; see the table), and literature links it to complex I stability, assembly, complex I deficiency, and Leigh syndrome. Its abundance therefore may report not only respiratory-chain presence but also integrity of the assembled complex.
- **Conclusion**: Established evidence supports NDUFS4 as an important complex I assembly or stability-related component whose disruption can impair mitochondrial respiration. It is reasonable to hypothesize that coordinated NDUFS4 abundance helps maintain the module, but the co-abundance data do not prove that NDUFS4 controls the other genes.

#### NDUFA9

- **Related proteins** (co-abundance neighbors): NDUFS2 (0.86); STRING partners: NDUFS2 (0.999), NDUFS4 (0.999), NDUFV1 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, testis
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1, huMAP3_02819.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit A9. The encoded protein is a subunit of the hydrophobic protein fraction of the NADH:ubiquinone oxidoreductase (complex I), the first enzyme complex in the electron transport chain located in the inner mitochondrial membrane. A pseudogene has been identified on chromosome 12. [provided by RefSeq, May 2010].
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 26 (0.660); mitochondrial complex I deficiency (0.621); type 2 diabetes mellitus (0.607); Parkinson disease (0.579); diabetes mellitus (0.579)
- **Europe PMC papers**: 2098
- **Why important**: NDUFA9 is a mitochondrial complex I subunit represented in every primary globally corrected term (20 globally significant GO/KEGG terms, q_global 0.00508–0.0424; see the table), strongly connected in STRING, and present in six hu.MAP assemblies (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1), (hu.MAP huMAP3_02819.1). Literature describes a role in stabilizing interactions between complex I modules, and disease associations include complex I deficiency, Parkinson disease, and diabetes. Its HPA annotation of late-spermatid enrichment is especially relevant to the testis component, while its detection in both tissues supports the shared-module interpretation.
- **Conclusion**: Established evidence supports NDUFA9 as a structural and functional complex I component. Its late-spermatid annotation suggests a possible testis-specific emphasis, but it does not establish that NDUFA9 explains the conservation of the entire module between heart and testis.

#### L2HGDH

- **Related proteins** (co-abundance neighbors): NDUFV1 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in heart, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: L-2-hydroxyglutarate dehydrogenase. This gene encodes L-2-hydroxyglutarate dehydrogenase, a FAD-dependent enzyme that oxidizes L-2-hydroxyglutarate to alpha-ketoglutarate in a variety of mammalian tissues. Mutations in this gene cause L-2-hydroxyglutaric aciduria, a rare autosomal recessive neurometabolic disorder resulting in moderate to severe cognitive disability. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: L-2-hydroxyglutaric aciduria (0.823); neurodegenerative disease (0.514); hereditary disease (0.452); gout (0.376); lysosomal storage disease (0.370)
- **Europe PMC papers**: 521
- **Why important**: L2HGDH is the module’s distinctive metabolic gene and the only member absent from the globally corrected GO/KEGG overlaps and from the supplied STRING and hu.MAP relationships. It encodes a mitochondrial FAD-dependent enzyme that converts L-2-hydroxyglutarate to alpha-ketoglutarate and is associated with L-2-hydroxyglutaric aciduria and neurometabolic disease. Its observed co-abundance link to the highly central NDUFV1, together with mitochondrial localization and detection in both tissues, makes it important for testing whether the module extends beyond a canonical complex I signature.
- **Conclusion**: Established evidence supports L2HGDH as a mitochondrial metabolite-oxidizing enzyme with a distinct disease association. Its functional coupling to complex I in this module is presently a hypothesis: the supplied data support co-abundance, not direct physical interaction, shared pathway membership, or causal regulation.
