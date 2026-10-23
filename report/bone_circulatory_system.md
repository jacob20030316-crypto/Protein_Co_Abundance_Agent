# Conserved co-abundance modules: bone and circulatory_system

## Module 0

**Tissue pair**: bone and circulatory_system  
**Genes (44)**: HIBADH, ALDH16A1, AMPD2, ANXA3, ANXA4, BRI3BP, CCDC167, CNPY3, COPS7A, CSRP1, DDAH2, DNM1L, DUSP3, EGLN1, GSPT2, FAM107B, FAM241B, PTK2, FHOD1, AGL, SLC2A6, GYS1, HEBP1, HK2, IKBIP, ILK, LGALSL, NCKAP1, NECAP1, PFKM, PAICS, PYGB, TRIM21, RPS27L, RSU1, SEC23IP, SHOC2, STOM, STARD3NL, SVIP, DARS2, TMEM179B, VPS13C, XPNPEP1

### Function

The best-supported function is carbohydrate and glycogen metabolism. The globally corrected evidence consists of carbohydrate binding (GO:MF carbohydrate binding; q_global = 0.025) and starch and sucrose metabolism (KEGG Starch and sucrose metabolism - Homo sapiens (human); q_global = 0.0405). The strongest mechanistic core is formed by AGL, GYS1, PYGB, HK2 and PFKM: AGL supports glycogen breakdown, GYS1 supports glycogen synthesis, PYGB supports glycogen mobilization, HK2 initiates glucose utilization, and PFKM supports glycolytic flux. The carbohydrate-binding annotation (GO:MF carbohydrate binding; q_global = 0.025) is broader than a specific pathway assignment, so the most defensible interpretation is coordinated glucose and glycogen handling rather than a narrowly defined molecular process. No other functional theme is globally supported by the enrichment results.

**Cell composition.** This is not primarily a plasma or secreted-protein module: the HPA summary identifies only a single secreted gene, while most genes have low tissue specificity and intracellular or membrane-associated locations. The module nevertheless has a strong cell-composition signal. Many genes are cell-type enhanced, with recurrent enrichment in neutrophils, platelets and megakaryocytes, and several genes are associated with skeletal muscle or other contractile-cell populations. The shared signal between bone and circulatory_system could therefore reflect common blood, platelet, megakaryocyte or vascular-associated cellular contributions in the sampled tissues, superimposed on a genuine intracellular carbohydrate-metabolism program. The absence of matching HPA tissue-level protein measurements for these tissue groups limits direct protein-level interpretation.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF carbohydrate binding | 0.025 | AGL, EGLN1, GYS1, HK2, LGALSL, PFKM |
| KEGG Starch and sucrose metabolism - Homo sapiens (human) | 0.0405 | AGL, GYS1, HK2, PYGB |

### STRING and hu.MAP

STRING provides a coherent, already-known glycogen and glycolysis subnetwork: AGL is linked to GYS1 and PYGB, GYS1 is linked to PYGB, HK2 is linked to PFKM, and PYGB is also linked to PFKM (STRING KEGG Starch and sucrose metabolism; within-query FDR = 0.0215). The ILK–RSU1 relationship is also strongly supported by STRING and represents a separate adhesion-associated branch. hu.MAP independently places AGL, GYS1 and PYGB together across several glycogen-related complexes (hu.MAP huMAP3_10227.1), (hu.MAP huMAP3_09760.1), (hu.MAP huMAP3_13075.1), (hu.MAP huMAP3_11993.1), (hu.MAP huMAP3_12186.1), (hu.MAP huMAP3_08013.1), (hu.MAP huMAP3_06909.1), (hu.MAP huMAP3_01396.1), (hu.MAP huMAP3_08093.1). HK2 and PFKM occur together in a hu.MAP complex (hu.MAP huMAP3_09730.1), while ILK and RSU1 recur together in focal-adhesion-related complexes (hu.MAP huMAP3_06647.1), (hu.MAP huMAP3_04827.1), (hu.MAP huMAP3_09385.1), (hu.MAP huMAP3_11194.1). Thus, part of the module recapitulates established protein relationships and complexes rather than representing an entirely unrecognized interaction system. The remaining co-abundance links are less directly supported by STRING or hu.MAP and may reflect shared regulation, cell composition or tissue-specific coupling rather than physical binding.

**STRING interactions (score >= 0.7)**: 6 of 946 gene pairs: AGL–GYS1 (0.944); AGL–PYGB (0.999); GYS1–PYGB (0.956); HK2–PFKM (0.977); ILK–RSU1 (0.991); PFKM–PYGB (0.736)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Starch and sucrose metabolism (FDR = 0.0215, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10227.1 (PYGB, GYS1, AGL; 3/14); huMAP3_09760.1 (PYGB, GYS1, AGL; 3/15); huMAP3_13075.1 (PYGB, GYS1, AGL; 3/15); huMAP3_11993.1 (PYGB, GYS1, AGL; 3/20); huMAP3_12186.1 (PYGB, GYS1, AGL; 3/23); huMAP3_09730.1 (PFKM, HK2; 2/4); huMAP3_06647.1 (ILK, RSU1; 2/6); huMAP3_04827.1 (ILK, RSU1; 2/7); huMAP3_08013.1 (PYGB, AGL; 2/8); huMAP3_09385.1 (ILK, RSU1; 2/8); huMAP3_06909.1 (PYGB, AGL; 2/9); huMAP3_01396.1 (PYGB, AGL; 2/10); huMAP3_11194.1 (ILK, RSU1; 2/10); huMAP3_08093.1 (PYGB, AGL; 2/12); huMAP3_09592.1 (STARD3NL, BRI3BP; 2/95)

### Novelty

The module should not be described as a wholly new glycogen-metabolism discovery. Its central glycogen relationships are already represented in STRING and hu.MAP, and the relevant genes have established biochemical and disease associations. A potentially novel aspect is the co-abundance organization of this metabolic core with adhesion, membrane, vesicle, oxygen-sensing and blood-cell-associated genes across bone and circulatory_system. However, this is a hypothesis about novelty rather than proof of a new mechanism: absence of a relationship from STRING or hu.MAP does not establish that it is novel, and the module may partly reflect shared cellular composition. The most defensible claim is that the cross-tissue co-abundance context may be under-characterized, while the core molecular functions are established.

**Hypothesis.** Mechanistic hypothesis: a shared population of metabolically active muscle-like, vascular-associated or blood-derived cells contributes a coordinated glucose and glycogen program in both tissue groups. Glycogen synthesis and storage through GYS1, glycogen mobilization through PYGB and AGL, and glucose entry into glycolysis through HK2 and PFKM may be coupled to integrin-associated adhesion and cytoskeletal signaling through ILK and RSU1. Oxygen sensing through EGLN1 and cell-surface or vesicle-associated processes could modulate this program in the local tissue environment. This remains a hypothesis because the enrichment establishes association with carbohydrate metabolism, whereas the cross-tissue cellular source and causal coupling to adhesion signaling are not demonstrated by the supplied data.

### Important genes

#### AGL

- **Related proteins** (co-abundance neighbors): EGLN1 (0.85); STRING partners: GYS1 (0.944), PYGB (0.999)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10227.1, huMAP3_09760.1, huMAP3_13075.1, huMAP3_11993.1, huMAP3_12186.1, huMAP3_08013.1, huMAP3_06909.1, huMAP3_01396.1, huMAP3_08093.1
- **Function (MyGene.info)**: amylo-alpha-1,6-glucosidase and 4-alpha-glucanotransferase. This gene encodes the glycogen debrancher enzyme which is involved in glycogen degradation. This enzyme has two independent catalytic activities which occur at different sites on the protein: a 4-alpha-glucotransferase activity and a amylo-1,6-glucosidase activity. Mutations in this gene are associated with glycogen storage disease although a wide range of enzymatic and clinical variability occurs…
- **Diseases (Open Targets)**: glycogen storage disease III (0.831); disorder of glycogen metabolism (0.768); glycogen storage disease XV (0.608); hereditary disease (0.507); Acute rhabdomyolysis (0.463)
- **Europe PMC papers**: 4441
- **Why important**: AGL is part of the central glycogen-processing core. It appears in the globally supported carbohydrate-binding and starch-and-sucrose terms (GO:MF carbohydrate binding; q_global = 0.025), (KEGG Starch and sucrose metabolism - Homo sapiens (human); q_global = 0.0405), is linked by STRING to GYS1 and PYGB, and recurs with those proteins across multiple hu.MAP complexes (hu.MAP huMAP3_10227.1), (hu.MAP huMAP3_09760.1), (hu.MAP huMAP3_13075.1), (hu.MAP huMAP3_11993.1), (hu.MAP huMAP3_12186.1), (hu.MAP huMAP3_08013.1), (hu.MAP huMAP3_06909.1), (hu.MAP huMAP3_01396.1), (hu.MAP huMAP3_08093.1). Its established glycogen-debranching function and strong association with glycogen storage disease make it a biologically informative anchor for the module.
- **Conclusion**: Established evidence supports AGL as a central glycogen-degradation component and a key marker of the module's metabolic interpretation. The cross-tissue coupling of AGL with adhesion and blood-cell-associated genes is a hypothesis, not an established AGL-specific mechanism here.

#### GYS1

- **Related proteins** (co-abundance neighbors): SEC23IP (0.82); STRING partners: AGL (0.944), PYGB (0.956)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Microtubules, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10227.1, huMAP3_09760.1, huMAP3_13075.1, huMAP3_11993.1, huMAP3_12186.1
- **Function (MyGene.info)**: glycogen synthase 1. The protein encoded by this gene catalyzes the addition of glucose monomers to the growing glycogen molecule through the formation of alpha-1,4-glycoside linkages. Mutations in this gene are associated with muscle glycogen storage disease. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: glycogen storage disease due to muscle and heart glycogen synthase deficiency (0.784); disorder of glycogen metabolism (0.530); neurodegenerative disease (0.440); glycogen storage disease XV (0.382); congenital myasthenic syndrome (0.266)
- **Europe PMC papers**: 1794
- **Why important**: GYS1 is the glycogen-synthesis counterpart to AGL and PYGB. It is present in both globally supported terms (GO:MF carbohydrate binding; q_global = 0.025), (KEGG Starch and sucrose metabolism - Homo sapiens (human); q_global = 0.0405), has strong STRING relationships with AGL and PYGB, and recurs in the same hu.MAP glycogen complexes (hu.MAP huMAP3_10227.1), (hu.MAP huMAP3_09760.1), (hu.MAP huMAP3_13075.1), (hu.MAP huMAP3_11993.1), (hu.MAP huMAP3_12186.1). Its skeletal-muscle and heart-muscle enrichment and established glycogen-storage disease associations make it especially relevant to a module shared with a musculoskeletal tissue.
- **Conclusion**: Established evidence identifies GYS1 as a core glycogen-biosynthetic enzyme and a plausible driver of the module's metabolic signal. It does not by itself establish that glycogen synthesis is the causal process linking bone and circulatory_system.

#### PYGB

- **Related proteins** (co-abundance neighbors): AMPD2 (0.84); STRING partners: AGL (0.999), GYS1 (0.956), PFKM (0.736)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10227.1, huMAP3_09760.1, huMAP3_13075.1, huMAP3_11993.1, huMAP3_12186.1, huMAP3_08013.1, huMAP3_06909.1, huMAP3_01396.1, huMAP3_08093.1
- **Function (MyGene.info)**: glycogen phosphorylase B. The protein encoded by this gene is a glycogen phosphorylase found predominantly in the brain. The encoded protein forms homodimers which can associate into homotetramers, the enzymatically active form of glycogen phosphorylase. The activity of this enzyme is positively regulated by AMP and negatively regulated by ATP, ADP, and glucose-6-phosphate. This enzyme catalyzes the rate-determining step i…
- **Diseases (Open Targets)**: neurodegenerative disease (0.419); prostate carcinoma (0.329); Short stature (0.259); neoplasm (0.102); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 901
- **Why important**: PYGB is a glycogen-phosphorylase component of the globally supported starch-and-sucrose term (KEGG Starch and sucrose metabolism - Homo sapiens (human); q_global = 0.0405). It is linked by STRING to AGL, GYS1 and PFKM, and is included with AGL and GYS1 in multiple hu.MAP complexes (hu.MAP huMAP3_10227.1), (hu.MAP huMAP3_09760.1), (hu.MAP huMAP3_13075.1), (hu.MAP huMAP3_11993.1), (hu.MAP huMAP3_12186.1). Its established role in the rate-limiting step of glycogen degradation gives it strong functional relevance, while its disease and neurological literature provide additional biological context.
- **Conclusion**: Established evidence supports PYGB as a central glycogen-mobilization gene in the module. The association with blood or tissue composition is plausible from the HPA profile but is not proven to be a PYGB-specific effect.

#### HK2

- **Related proteins** (co-abundance neighbors): GSPT2 (0.84); STRING partners: PFKM (0.977)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09730.1
- **Function (MyGene.info)**: hexokinase 2. Hexokinases phosphorylate glucose to produce glucose-6-phosphate, the first step in most glucose metabolism pathways. This gene encodes hexokinase 2, the predominant form found in skeletal muscle. It localizes to the outer membrane of mitochondria. Expression of this gene is insulin-responsive, and studies in rat suggest that it is involved in the increased rate of glycolysis seen in rapidly growi…
- **Diseases (Open Targets)**: neurodegenerative disease (0.541); urolithiasis (0.247); alcohol drinking (0.247); Hypercholesterolemia (0.184); neoplasm (0.120)
- **Europe PMC papers**: 19870
- **Why important**: HK2 connects glucose utilization to the glycogen-associated module. It appears in both globally supported terms (GO:MF carbohydrate binding; q_global = 0.025), (KEGG Starch and sucrose metabolism - Homo sapiens (human); q_global = 0.0405), is linked to PFKM by STRING, and shares a hu.MAP complex with PFKM (hu.MAP huMAP3_09730.1). Its established function as the enzyme initiating glucose phosphorylation, its skeletal-muscle relevance, and its extensive disease literature make it a strong metabolic representative.
- **Conclusion**: Established evidence supports HK2 as a gateway from glucose availability into glycolysis and as part of the module's carbohydrate-metabolism axis. Its co-abundance with platelet- and neutrophil-enhanced genes could reflect cellular composition rather than a novel HK2 pathway in these tissues.

#### PFKM

- **Related proteins** (co-abundance neighbors): NECAP1 (0.83); STRING partners: HK2 (0.977), PYGB (0.736)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09730.1
- **Function (MyGene.info)**: phosphofructokinase, muscle. Three phosphofructokinase isozymes exist in humans: muscle, liver and platelet. These isozymes function as subunits of the mammalian tetramer phosphofructokinase, which catalyzes the phosphorylation of fructose-6-phosphate to fructose-1,6-bisphosphate. Tetramer composition varies depending on tissue type. This gene encodes the muscle-type isozyme. Mutations in this gene have been associated with g…
- **Diseases (Open Targets)**: glycogen storage disease VII (0.819); disorder of glycogen metabolism (0.372); peroxisome biogenesis disorder (0.333); neurodegenerative disease (0.319); anemia (phenotype) (0.288)
- **Europe PMC papers**: 2506
- **Why important**: PFKM is included in the globally supported carbohydrate-binding term (GO:MF carbohydrate binding; q_global = 0.025) and is linked to HK2 and PYGB by STRING. It also occurs with HK2 in hu.MAP complex (hu.MAP huMAP3_09730.1). As the muscle-type phosphofructokinase, it provides a direct connection between glucose phosphorylation and downstream glycolytic commitment, with established relevance to glycogen storage disease.
- **Conclusion**: Established evidence supports PFKM as a glycolytic control point that complements the glycogen enzymes. Its placement in this cross-tissue module suggests coordinated carbohydrate handling, but does not demonstrate that PFKM activity causes the observed co-abundance pattern.

#### ILK

- **Related proteins** (co-abundance neighbors): DUSP3 (0.86), FHOD1 (0.84), GSPT2 (0.84), NECAP1 (0.84), STOM (0.82), RSU1 (0.81); STRING partners: RSU1 (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06647.1, huMAP3_04827.1, huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: integrin linked kinase. This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastas…
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); familial hypertrophic cardiomyopathy (0.194); Abnormality of the cardiovascular system (0.148); Prolonged QT interval (0.118); neoplasm (0.118)
- **Europe PMC papers**: 8401
- **Why important**: ILK is a highly connected member of the non-metabolic branch and is linked to RSU1 by a strong STRING relationship. ILK and RSU1 recur together in several hu.MAP complexes (hu.MAP huMAP3_06647.1), (hu.MAP huMAP3_04827.1), (hu.MAP huMAP3_09385.1), (hu.MAP huMAP3_11194.1). Its established role in integrin-mediated signaling, cell-matrix adhesion and morphogenesis, together with platelet and megakaryocyte enhancement in HPA, makes it important for interpreting why a glycogen-associated module is shared across bone and circulatory_system.
- **Conclusion**: Established evidence supports ILK as an adhesion and cell-interface component that may explain tissue or cellular context around the metabolic core. A direct mechanistic coupling between ILK signaling and the glycogen genes is a hypothesis requiring experimental validation.

## Module 1

**Tissue pair**: bone and circulatory_system  
**Genes (34)**: AACS, ANXA2, ANXA5, ASNS, BLVRB, CBS, TRIP10, NCAPH, DNAAF5, DHX57, EEF1A2, FSCN1, GALE, GNG5, CCDC88A, IMPDH1, KIFBP, MPP2, QPRT, NAMPT, NUDT4, ATIC, SEC23B, SRPK1, TUBB2B, TUBB6, CCT5, CCT3, CCT7, CCT8, TSPYL5, UAP1, UGDH, VCL

### Function

The strongest interpretation is a cytosolic protein-folding and cytoskeletal-support module centered on the CCT/TRiC chaperonin. The primary GO evidence is highly coherent: CCT3, CCT5, CCT7, and CCT8 jointly support the chaperonin-containing T-complex and ATP-dependent protein folding (GO:CC chaperonin-containing T-complex; q_global = 0.000952) (GO:MF ATP-dependent protein folding chaperone; q_global = 0.0343), as well as telomerase-RNA and protein localization to the Cajal body and related telomere-maintenance processes (13 globally significant GO/KEGG terms, q_global 0.000271–0.000952; see the table) (GO:BP positive regulation of telomere maintenance via telomere lengthening; q_global = 0.00224) (4 globally significant GO/KEGG terms, q_global 0.012–0.0178; see the table). The sperm-recognition terms (GO:BP binding of sperm to zona pellucida; q_global = 0.00224) (GO:BP sperm-egg recognition; q_global = 0.00437) are likely indirect or annotation-linked consequences of the same CCT genes rather than evidence that the entire module is a reproductive module. Supplementary STRING results support folding of tubulin and actin, prefoldin-to-CCT substrate transfer, and G-protein-beta folding (8 supplementary STRING terms; within-query FDR 0.00012–0.0049). The remaining genes suggest connected support functions involving microtubules, actin and adhesion, nucleotide and NAD metabolism, glycosaminoglycan precursor production, vesicle trafficking, and RNA or protein regulation. Thus, the module most plausibly reflects proteostasis and cytoskeletal organization, with possible links to proliferative or genome-maintenance state.

**Cell composition.** This does not look like a plasma-protein or secreted-protein module: only NAMPT and ANXA2 are annotated as secreted to blood, and the other genes are predominantly intracellular. It is also not uniformly blood-cell enriched. HPA indicates broadly distributed or tissue-enhanced expression for many genes, with recurrent signals in liver, brain, pancreas, bone marrow, skeletal muscle, and testis. Several genes show enrichment in monocytes, dendritic cells, neutrophils, or progenitor populations, while others are enhanced in cardiomyocytes, neurons, epithelial cells, spermatogenic cells, or muscle. The module may therefore partly reflect shared intracellular programs across heterogeneous cell types, and in circulatory samples some contribution from immune or blood-associated cells is plausible. The absence of matching HPA tissue-protein data for bone and circulatory_system prevents a direct tissue-level protein-expression conclusion.

**GO/KEGG enrichment**: 21 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulation of telomerase RNA localization to Cajal body | 0.000271 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 0.000271 | CCT3, CCT5, CCT7, CCT8 |
| GO:CC chaperonin-containing T-complex | 0.000952 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 0.000952 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to Cajal body | 0.000952 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 0.000952 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 0.000952 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 0.000952 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 0.000952 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 0.000952 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 0.000952 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 0.000952 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 0.000952 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP binding of sperm to zona pellucida | 0.00224 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomere lengthening | 0.00224 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING provides strong prior support for a compact CCT core: CCT3, CCT5, CCT7, and CCT8 are mutually connected, and CCT3 also connects to TUBB2B and TUBB6. STRING additionally supports ATIC with IMPDH1, GALE with UAP1 and UGDH, and ANXA2 with ANXA5. The supplementary pathway results (15 supplementary STRING terms; within-query FDR 0.00012–0.0072) reinforce established chaperonin, tubulin-folding, actin-folding, G-protein-beta-folding, and CCT-domain relationships, but they are not global enrichment evidence. hu.MAP independently places the four CCT genes together in several complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), places TUBB2B and TUBB6 together in multiple tubulin-related complexes (hu.MAP huMAP3_06977.1) (hu.MAP huMAP3_14311.1) (hu.MAP huMAP3_09670.1) (hu.MAP huMAP3_08179.1) (hu.MAP huMAP3_09603.1) (hu.MAP huMAP3_09233.1) (hu.MAP huMAP3_10475.1) (hu.MAP huMAP3_10665.1), and supports smaller groupings involving BLVRB, ATIC, UAP1, UGDH, and NAMPT (hu.MAP huMAP3_14442.1) (hu.MAP huMAP3_12841.1). These relationships indicate that the module contains a genuine known CCT-centered interaction core plus peripheral metabolic, cytoskeletal, and trafficking neighborhoods; they do not establish that all module genes form one physical complex.

**STRING interactions (score >= 0.7)**: 14 of 561 gene pairs: ANXA2–ANXA5 (0.833); ATIC–CCT7 (0.881); ATIC–IMPDH1 (0.979); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT3–TUBB2B (0.71); CCT3–TUBB6 (0.716); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999); GALE–UAP1 (0.886); GALE–UGDH (0.984); UAP1–UGDH (0.733)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Formation of tubulin folding intermediates by CCT/TriC (FDR = 0.00012, 6 genes); RCTM Chaperonin-mediated protein folding (FDR = 0.00012, 7 genes); RCTM Prefoldin mediated transfer of substrate  to CCT/TriC (FDR = 0.00015, 6 genes); RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding (FDR = 0.00015, 5 genes); Pfam TCP-1/cpn60 chaperonin family (FDR = 0.0017, 4 genes); RCTM Folding of actin by CCT/TriC (FDR = 0.0017, 4 genes); RCTM Association of TriC/CCT with target proteins during biosynthesis (FDR = 0.0035, 4 genes); Component Chaperonin-containing T-complex (FDR = 0.0049, 4 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 0.0053, 4 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 0.0072, 4 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 0.0072, 4 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 0.0072, 4 genes); InterPro GroEL-like apical domain superfamily (FDR = 0.0072, 4 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 0.0072, 4 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 0.0072, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_14442.1 (BLVRB, ATIC, UAP1; 3/57); huMAP3_12841.1 (UGDH, NAMPT; 2/10); huMAP3_06977.1 (TUBB6, TUBB2B; 2/12); huMAP3_14311.1 (TUBB6, TUBB2B; 2/16); huMAP3_09670.1 (TUBB6, TUBB2B; 2/23); huMAP3_08179.1 (TUBB6, TUBB2B; 2/24); huMAP3_09603.1 (TUBB6, TUBB2B; 2/24); huMAP3_09233.1 (TUBB6, TUBB2B; 2/34); huMAP3_10475.1 (TUBB6, TUBB2B; 2/39); huMAP3_10665.1 (TUBB6, TUBB2B; 2/42)

### Novelty

The CCT-centered portion is not a new molecular interaction finding because it is strongly represented in STRING and hu.MAP. The module-level co-abundance pattern across bone and circulatory_system may nevertheless be a potentially new systems-level observation, particularly because the module combines the established CCT core with genes involved in metabolism, cytoskeleton, vesicles, immune-associated cell types, and tissue-diverse programs. Novelty should be stated cautiously: the fact sheet does not provide a comparison with previously reported cross-tissue co-abundance modules, and absence of prior STRING or hu.MAP relationships would not by itself prove novelty. The most defensible claim is that the shared co-abundance organization may be novel, whereas its central molecular machinery is established.

**Hypothesis.** Hypothesis: a shared cellular-state program in bone and circulatory_system coordinates CCT/TRiC-dependent folding of actin, tubulin, and other client proteins with cytoskeletal remodeling, vesicle or membrane organization, and metabolic support. In blood-associated samples, variation in monocyte, dendritic-cell, neutrophil, platelet, or progenitor composition could generate part of the shared signal. The CCT core may help maintain cytoskeletal and nuclear-body functions, while NAMPT, CBS, purine-pathway genes, glycosaminoglycan-related enzymes, annexins, and adhesion proteins represent context-dependent metabolic and structural outputs. This hypothesis requires validation by cell-composition adjustment, independent cohorts, protein-level assays, and perturbation of CCT or selected peripheral genes.

### Important genes

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT8 (0.89), CCT7 (0.83), CCT3 (0.82); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is a central member of the CCT/TRiC core, is connected to CCT3, CCT7, and CCT8 in STRING, and occurs in multiple hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It belongs to every primary GO term (21 globally significant GO/KEGG terms, q_global 0.000271–0.0343; see the table) and every supplementary STRING term (15 supplementary STRING terms; within-query FDR 0.00012–0.0072). Its established function is ATP-dependent folding of proteins including actin and tubulin, and it has a disease association with hereditary sensory and autonomic neuropathy with spastic paraplegia. Its literature support is substantial relative to most peripheral module genes.
- **Conclusion**: Established evidence identifies CCT5 as a core chaperonin component and a strong functional anchor for the module. It is reasonable to hypothesize that CCT5 abundance tracks proteostasis and cytoskeletal-client folding in the shared tissue program, but the co-abundance data do not show that CCT5 drives the module.

#### CCT3

- **Related proteins** (co-abundance neighbors): ATIC (0.87), CCT5 (0.82); STRING partners: CCT5 (0.999), CCT7 (0.999), CCT8 (0.999), TUBB2B (0.71), TUBB6 (0.716)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is part of the same highly supported CCT core, appears in hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), and connects in STRING to the other CCT subunits and to TUBB2B and TUBB6. It is present in all primary GO terms (21 globally significant GO/KEGG terms, q_global 0.000271–0.0343; see the table) and all supplementary CCT and substrate-folding terms (15 supplementary STRING terms; within-query FDR 0.00012–0.0072). Its established role is ATP-dependent molecular chaperoning of actin, tubulin, and other unfolded proteins. Disease associations include a neurodevelopmental disorder and neurodegenerative disease.
- **Conclusion**: Established evidence supports CCT3 as a core structural and functional component of the module. Its tubulin-linked STRING relationships make it a plausible bridge between chaperoning and cytoskeletal organization, but that bridge remains a mechanistic hypothesis rather than a demonstrated tissue-specific causal pathway.

#### CCT7

- **Related proteins** (co-abundance neighbors): CCT5 (0.83), CCT8 (0.81); STRING partners: ATIC (0.881), CCT3 (0.999), CCT5 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is a member of the four-subunit CCT core, has strong STRING relationships with CCT3, CCT5, and CCT8, and occurs in hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It contributes to every primary GO term (21 globally significant GO/KEGG terms, q_global 0.000271–0.0343; see the table) and every supplementary CCT-related term (15 supplementary STRING terms; within-query FDR 0.00012–0.0072). Its established functions include protein folding, stabilization, and support of telomerase-RNA or protein localization to the Cajal body. Open Targets associations include myocardial infarction and preeclampsia, which are relevant to circulatory biology but do not establish a tissue mechanism.
- **Conclusion**: Established evidence makes CCT7 a core module marker and a plausible indicator of proteostasis state. Its disease associations motivate investigation in circulatory phenotypes, but they should not be interpreted as evidence that this module causes those diseases.

#### NAMPT

- **Related proteins** (co-abundance neighbors): FSCN1 (0.83), CBS (0.80), ASNS (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12841.1
- **Function (MyGene.info)**: nicotinamide phosphoribosyltransferase. This gene encodes a protein that catalyzes the condensation of nicotinamide with 5-phosphoribosyl-1-pyrophosphate to yield nicotinamide mononucleotide, one step in the biosynthesis of nicotinamide adenine dinucleotide. The protein belongs to the nicotinic acid phosphoribosyltransferase (NAPRTase) family and is thought to be involved in many important biological processes, including metabolism, str…
- **Diseases (Open Targets)**: neurodegenerative disease (0.322); asthma (0.259); esophageal squamous cell carcinoma (0.174); Genu varum (0.172); Genu valgum (0.172)
- **Europe PMC papers**: 8350
- **Why important**: NAMPT links the module to NAD biosynthesis, stress response, inflammation, and cell signaling. It is tissue-enhanced in lymphoid tissue, cell-type enriched in neutrophils, and secreted to blood according to HPA, making it especially relevant to the circulatory context. It connects in the module to FSCN1, CBS, and ASNS and appears in hu.MAP complex (hu.MAP huMAP3_12841.1). It also has a substantial literature base and disease associations spanning inflammatory, metabolic, and neurodegenerative contexts.
- **Conclusion**: Established evidence supports NAMPT as a metabolic and inflammatory-context gene that may help explain why the module is shared with circulatory_system. A role as a circulating or immune-cell-linked modulator of the CCT and cytoskeletal program is plausible, but the co-abundance network does not establish secretion-mediated regulation or causality.

#### ANXA2

- **Related proteins** (co-abundance neighbors): EEF1A2 (0.83), ANXA5 (0.82); STRING partners: ANXA5 (0.833)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A2. This gene encodes a member of the annexin family. Members of this calcium-dependent phospholipid-binding protein family play a role in the regulation of cellular growth and in signal transduction pathways. This protein functions as an autocrine factor which heightens osteoclast formation and bone resorption. This gene has three pseudogenes located on chromosomes 4, 9 and 10, respectively. Multiple…
- **Diseases (Open Targets)**: neurodegenerative disease (0.443); Alzheimer disease (0.312); Parkinson disease (0.298); lysosomal storage disease (0.289); benign urinary system neoplasm (0.270)
- **Europe PMC papers**: 12966
- **Why important**: ANXA2 is a membrane-associated calcium-dependent phospholipid-binding protein with roles in vesicle budding, adhesion, receptor recycling, angiogenesis, and osteoclast formation. It is secreted to blood and shows blood enrichment across several immune-cell categories in HPA. Its direct STRING relationship with ANXA5 is established, and its module neighbors include EEF1A2 and ANXA5. Its literature volume is high, and its functions are relevant to both bone remodeling and vascular or blood-associated biology.
- **Conclusion**: Established evidence supports ANXA2 as a plausible tissue-interface and cell-composition marker linking membrane dynamics, adhesion, and bone resorption. Its placement in this module may reflect a shared structural or immune-associated state, but a direct functional connection to the CCT core remains hypothetical.

#### FSCN1

- **Related proteins** (co-abundance neighbors): CBS (0.94), MPP2 (0.87), NAMPT (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fascin actin-bundling protein 1. This gene encodes a member of the fascin family of actin-binding proteins. Fascin proteins organize F-actin into parallel bundles, and are required for the formation of actin-based cellular protrusions. The encoded protein plays a critical role in cell migration, motility, adhesion and cellular interactions. Expression of this gene is known to be regulated by several microRNAs, and overexpression …
- **Diseases (Open Targets)**: ankylosing spondylitis (0.355); Alzheimer disease (0.179); hypothyroidism (0.164); neoplasm (0.118); breast cancer (0.116)
- **Europe PMC papers**: 4005
- **Why important**: FSCN1 is an actin-bundling protein required for cellular protrusions, migration, motility, adhesion, and cell interactions. It is connected in the module to CBS, MPP2, and NAMPT and is immune-cell enhanced in myeloid dendritic cells. Its extensive literature and disease associations, including neoplasm and ankylosing spondylitis, make it an informative peripheral structural gene. It provides a functional link from the CCT-supported actin-folding evidence to actin organization and cell movement.
- **Conclusion**: Established evidence supports FSCN1 as a cytoskeletal remodeling and migration factor that may contextualize the module's shared tissue signal. Its connection to the CCT core is indirect in the supplied data, so any model in which CCT activity controls FSCN1-dependent migration is a hypothesis requiring direct testing.

## Module 2

**Tissue pair**: bone and circulatory_system  
**Genes (23)**: APOBEC3C, COX16, CMC1, FMC1, GATC, GOLGA7, LANCL2, MAGEB2, MGST1, NDUFA6, NUSAP1, PPIL3, PFN2, MRPL27, MRPL45, MRPL55, MRPS18B, MRPS23, SCD, BNIP1, SYNJ2BP, UBE4B, UPP1

### Function

The strongest interpretation is a mitochondrial protein-synthesis and respiratory-capacity module. (KEGG Ribosome - Homo sapiens (human); q_global = 0.045) is the only GO/KEGG term that passed global correction and identifies ribosome biology through MRPL27, MRPL45, MRPL55, MRPS18B, and MRPS23. The mitochondrial interpretation is supported, but only supplementarily, by (STRING Keyword Mitochondrion; within-query FDR = 0.0014) through (STRING Component Mitochondrial protein-containing complex; within-query FDR = 0.0365), which connect the module to mitochondria, mitochondrial membranes, mitochondrial ribosomes, mitochondrial translation, and respiratory-chain functions. Additional module genes support adjacent biology: NDUFA6 contributes to respiratory-chain complex I, COX16 and CMC1 to complex IV assembly, FMC1 to ATP synthase assembly, GATC to mitochondrial translation and translational fidelity, and MGST1 to oxidant and lipid-hydroperoxide handling. The sparse co-abundance graph contains a coherent mitochondrial-ribosomal core plus peripheral metabolic, membrane, trafficking, and cell-structure genes. Thus, the module most plausibly reflects coordinated mitochondrial translation and oxidative-energy maintenance, rather than a single narrowly defined pathway.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: HPA identifies only one secreted gene, and the listed proteins are overwhelmingly intracellular. It is also not strongly blood-cell enriched. Most genes have low tissue specificity and low immune-cell specificity, although individual genes show enrichment in particular tissues or cell types, including adipose tissue, liver, brain, reproductive cells, hepatocytes, and selected immune populations. The presence of NUSAP1 in bone marrow and lymphoid tissue, and CMC1 in NK cells, warrants attention to cellular composition, but the overall HPA pattern does not support a predominantly blood-cell-driven explanation. HPA provides no matching tissue-level protein data for either named tissue, so tissue-specific protein localization cannot be assessed from this summary. A shared abundance signal may therefore reflect broadly expressed mitochondrial machinery, with contributions from differing cell mixtures in bone and circulatory-system samples.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Ribosome - Homo sapiens (human) | 0.045 | MRPL27, MRPL45, MRPL55, MRPS18B, MRPS23 |

### STRING and hu.MAP

STRING contains a dense, high-confidence set of known relationships among the five mitochondrial ribosomal proteins represented in (KEGG Ribosome - Homo sapiens (human); q_global = 0.045), especially the links joining MRPL27, MRPL45, MRPL55, MRPS18B, and MRPS23. STRING also provides a more limited known link between GATC and NDUFA6, while several mitochondrial genes are connected by the supplementary functional network annotations (STRING Keyword Mitochondrion; within-query FDR = 0.0014), (STRING Component Mitochondrial membrane; within-query FDR = 0.0044), (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.009), (STRING Component Mitochondrion; within-query FDR = 0.0115), (STRING Component Mitochondrial inner membrane; within-query FDR = 0.0358), and (STRING Component Mitochondrial protein-containing complex; within-query FDR = 0.0365). These observations show that the central ribosomal signal is biologically credible and substantially recapitulates established mitochondrial-ribosome relationships. hu.MAP independently places MRPL27 and MRPL55 together in several large mitochondrial-complex contexts (hu.MAP huMAP3_06439.1) through (hu.MAP huMAP3_06589.1), and MRPS18B with MRPS23 in (hu.MAP huMAP3_05807.1). However, each hu.MAP complex contributes only a small subset of its members to this module. The network therefore combines a known mitochondrial ribosomal core with module-specific co-abundance links that are not uniformly supported by physical complex membership.

**STRING interactions (score >= 0.7)**: 11 of 253 gene pairs: GATC–NDUFA6 (0.709); MRPL27–MRPL45 (0.953); MRPL27–MRPL55 (0.941); MRPL27–MRPS18B (0.849); MRPL27–MRPS23 (0.884); MRPL45–MRPL55 (0.841); MRPL45–MRPS18B (0.954); MRPL45–MRPS23 (0.895); MRPL55–MRPS18B (0.885); MRPL55–MRPS23 (0.881); MRPS18B–MRPS23 (0.983)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Mitochondrion (FDR = 0.0014, 13 genes); Component Mitochondrial membrane (FDR = 0.0044, 10 genes); Component Mitochondrial ribosome (FDR = 0.006, 5 genes); COMPARTMENTS Mitochondrion (FDR = 0.009, 13 genes); COMPARTMENTS Mitochondrial ribosome (FDR = 0.0096, 5 genes); Keyword Ribosomal protein (FDR = 0.0098, 5 genes); Component Ribosomal subunit (FDR = 0.0113, 5 genes); Component Mitochondrion (FDR = 0.0115, 13 genes); NetworkNeighborAL Organellar ribosome (FDR = 0.0266, 5 genes); RCTM Mitochondrial translation initiation (FDR = 0.0307, 5 genes); RCTM Mitochondrial translation elongation (FDR = 0.0307, 5 genes); RCTM Mitochondrial translation termination (FDR = 0.0307, 5 genes); Component Mitochondrial inner membrane (FDR = 0.0358, 7 genes); Component Mitochondrial protein-containing complex (FDR = 0.0365, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06439.1 (MRPL55, MRPL27; 2/57); huMAP3_06550.1 (MRPL55, MRPL27; 2/62); huMAP3_07939.1 (MRPL55, MRPL27; 2/68); huMAP3_08458.1 (MRPL55, MRPL27; 2/70); huMAP3_09113.1 (MRPL55, MRPL27; 2/72); huMAP3_09483.1 (MRPL55, MRPL27; 2/74); huMAP3_06589.1 (MRPL55, MRPL27; 2/79); huMAP3_05807.1 (MRPS23, MRPS18B; 2/81)

### Novelty

The mitochondrial-ribosomal core is not a new molecular interaction finding: its central relationships are already represented in STRING and hu.MAP, and the relevant gene functions are established. The potentially novel aspect is the coordinated co-abundance of this mitochondrial translation core with MGST1, BNIP1, SYNJ2BP, NDUFA6, SCD, LANCL2, UPP1, and other peripheral genes specifically across the bone and circulatory-system tissue pair. That claim remains provisional because the fact sheet does not provide an independent replication, perturbation experiment, clinical association, or comparison with published cross-tissue modules. Absence of STRING or hu.MAP support for peripheral edges is not evidence of novelty; it may reflect context-dependent regulation, incomplete databases, or correlations caused by cell composition. The appropriate conclusion is a potentially distinctive tissue-pair co-abundance pattern built around a well-established mitochondrial program, not a demonstrated new molecular complex or pathway.

**Hypothesis.** Hypothesis: in both bone and circulatory-system samples, variation in cellular energetic demand or mitochondrial abundance coordinately raises mitochondrial translation through the (KEGG Ribosome - Homo sapiens (human); q_global = 0.045) ribosomal core and couples it to respiratory-chain assembly and electron transport through NDUFA6, COX16, CMC1, and FMC1. MGST1 and SCD may mark accompanying lipid-handling and oxidative-stress states, while BNIP1 and SYNJ2BP may connect organelle maintenance or membrane trafficking with the mitochondrial program. This could represent a shared mitochondrial state across the two tissues, but it could alternatively arise from broadly expressed housekeeping machinery or differences in cell-type mixture. Testing this hypothesis requires replication across samples, adjustment for cellular composition, and experimental assessment of mitochondrial translation and respiratory function.

### Important genes

#### MRPL45

- **Related proteins** (co-abundance neighbors): GATC (0.85), SYNJ2BP (0.84), NDUFA6 (0.82), MGST1 (0.81), BNIP1 (0.81); STRING partners: MRPL27 (0.953), MRPL55 (0.841), MRPS18B (0.954), MRPS23 (0.895)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial ribosomal protein L45. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.498); lysosomal storage disease (0.325); Alzheimer disease (0.325); Parkinson disease (0.325); prostate carcinoma (0.198)
- **Europe PMC papers**: 238
- **Why important**: MRPL45 is the most connected gene in the module and bridges the mitochondrial-ribosomal core to GATC, SYNJ2BP, NDUFA6, MGST1, and BNIP1. It is present in (KEGG Ribosome - Homo sapiens (human); q_global = 0.045) and in every listed mitochondrial STRING enrichment (STRING Keyword Mitochondrion; within-query FDR = 0.0014) through (STRING Component Mitochondrial protein-containing complex; within-query FDR = 0.0365). Its mitochondrial location and established role as a mitochondrial large-subunit ribosomal protein make it a strong structural anchor. The literature record is substantial, and disease associations include neurodegenerative and lysosomal-storage disorders.
- **Conclusion**: Established: MRPL45 is a central mitochondrial-ribosomal component and a plausible marker of the module's core program. Hypothesis: its network position may make it a useful bridge between mitochondrial translation and the module's membrane or stress-related periphery, but the co-abundance data do not establish a direct regulatory role.

#### MRPL27

- **Related proteins** (co-abundance neighbors): MRPS23 (0.85), MGST1 (0.81), CMC1 (0.81); STRING partners: MRPL45 (0.953), MRPL55 (0.941), MRPS18B (0.849), MRPS23 (0.884)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06439.1, huMAP3_06550.1, huMAP3_07939.1, huMAP3_08458.1, huMAP3_09113.1, huMAP3_09483.1, huMAP3_06589.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein L27. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.519); cholangiocarcinoma (0.075); neoplasm (0.045); systemic-onset juvenile idiopathic arthritis (0.020); chronic obstructive pulmonary disease (0.016)
- **Europe PMC papers**: 258
- **Why important**: MRPL27 is highly connected to the mitochondrial-ribosomal core and to MGST1 and CMC1. It is part of (KEGG Ribosome - Homo sapiens (human); q_global = 0.045), all of the listed mitochondrial STRING enrichments, and the hu.MAP contexts (hu.MAP huMAP3_06439.1) through (hu.MAP huMAP3_06589.1). Its annotation as a mitochondrial large-subunit ribosomal protein gives direct functional support to the module interpretation. Its literature record is substantial and includes associations with neurodegenerative disease and other disorders.
- **Conclusion**: Established: MRPL27 is a well-supported component of the module's mitochondrial-ribosome subnetwork. Hypothesis: its association with MGST1 and CMC1 may indicate coupling between mitochondrial protein synthesis, respiratory-chain maintenance, and redox handling, although the peripheral links are not established physical interactions here.

#### MRPS18B

- **Related proteins** (co-abundance neighbors): COX16 (0.88), MRPS23 (0.88), NUSAP1 (0.80); STRING partners: MRPL27 (0.849), MRPL45 (0.954), MRPL55 (0.885), MRPS23 (0.983)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05807.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein S18B. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.537); tuberculosis (0.023); systemic-onset juvenile idiopathic arthritis (0.016); oral cavity squamous cell carcinoma (0.011); breast cancer (0.009)
- **Europe PMC papers**: 311
- **Why important**: MRPS18B is a mitochondrial small-subunit ribosomal protein, belongs to (KEGG Ribosome - Homo sapiens (human); q_global = 0.045), and participates in the strongly connected mitochondrial-ribosomal STRING core. It also links to COX16 and NUSAP1 within the co-abundance graph and shares a hu.MAP context with MRPS23 in (hu.MAP huMAP3_05807.1). Its mitochondrial localization, translation annotation, disease associations, and established literature make it informative despite its more focused network position.
- **Conclusion**: Established: MRPS18B supports the interpretation that the module contains coordinated mitochondrial translation machinery. Hypothesis: its connection to COX16 could reflect coupling between translation and complex IV assembly, but this relationship is inferred from co-abundance and is not demonstrated as a direct interaction.

#### MRPS23

- **Related proteins** (co-abundance neighbors): MRPS18B (0.88), MRPL27 (0.85); STRING partners: MRPL27 (0.884), MRPL45 (0.895), MRPL55 (0.881), MRPS18B (0.983)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05807.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein S23. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.495); combined oxidative phosphorylation deficiency 46 (0.399); tendon sheath disorder (0.307); gout (0.204); liver disorder (0.186)
- **Europe PMC papers**: 362
- **Why important**: MRPS23 is part of the globally supported ribosome signal (KEGG Ribosome - Homo sapiens (human); q_global = 0.045) and forms very strong STRING relationships with MRPS18B and the mitochondrial large-subunit proteins. It also participates in (hu.MAP huMAP3_05807.1). Its mitochondrial location and translation annotation directly reinforce the core functional interpretation. The literature includes mitochondrial disease and neurodegenerative associations, making it relevant to energetic and cellular-stress biology.
- **Conclusion**: Established: MRPS23 is a known mitochondrial-ribosome component and a robust marker of the module's conserved core. Hypothesis: coordinated MRPS23 abundance may report altered mitochondrial translational capacity across the two tissues, but it does not by itself identify the initiating stimulus.

#### NDUFA6

- **Related proteins** (co-abundance neighbors): BNIP1 (0.86), MRPL45 (0.82); STRING partners: GATC (0.709)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, End piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit A6. This gene encodes a member of the LYR family of proteins that contain a highly conserved tripeptide (LYR) motif near the N-terminus. The encoded protein is an accessory subunit of NADH: ubiquinone oxidorerductase (Complex I), which is the largest enzyme of the mitochondrial membrane respiratory chain. Complex I functions in electron transfer from NADH to the respiratory chain. [provided by RefSeq,…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 33 (0.709); type 2 diabetes mellitus (0.609); mitochondrial complex I deficiency (0.601); diabetes mellitus (0.578); neurodegenerative disease (0.567)
- **Europe PMC papers**: 1085
- **Why important**: NDUFA6 connects the mitochondrial-ribosomal neighborhood to respiratory-chain biology through its module edges with MRPL45 and BNIP1 and its known STRING relationship with GATC. Its annotation identifies it as a complex I accessory and assembly factor, and it appears in supplementary mitochondrial and inner-membrane terms (STRING Keyword Mitochondrion; within-query FDR = 0.0014), (STRING Component Mitochondrial membrane; within-query FDR = 0.0044), (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.009), (STRING Component Mitochondrion; within-query FDR = 0.0115), (STRING Component Mitochondrial inner membrane; within-query FDR = 0.0358), and (STRING Component Mitochondrial protein-containing complex; within-query FDR = 0.0365). It has a substantial literature record and disease associations involving complex I deficiency, diabetes, and neurodegenerative disease.
- **Conclusion**: Established: NDUFA6 provides the clearest link from the module's translation core to mitochondrial electron transport and respiratory-chain assembly. Hypothesis: it may help explain why the same co-abundance module is observed in tissues with differing energetic requirements, but causality and tissue specificity remain untested.

## Module 3

**Tissue pair**: bone and circulatory_system  
**Genes (26)**: ACIN1, AP1M1, AP3D1, ARL3, CCDC137, CCAR1, CDK5RAP3, CSTF3, DDX24, EML4, SQLE, FLOT1, GLYR1, H1-1, LACTB, LIMA1, MCU, NCBP3, PPP1R9B, PDLIM2, PAK1IP1, RBMXL1, SMARCA2, SMARCC2, TFAM, TTC9C

### Function

No GO or KEGG term passed global correction, so the module should not be assigned a formally enriched pathway function. The gene composition nevertheless suggests a mixed intracellular maintenance program rather than a bone- or circulation-specific pathway. One component involves nuclear RNA metabolism, including RNA binding, splicing, mRNA three-prime-end processing, RNA export, and nucleolar functions, represented especially by CCDC137, RBMXL1, CSTF3, ACIN1, NCBP3, and PAK1IP1. A second component involves chromatin organization and transcriptional regulation, represented by SMARCA2, SMARCC2, GLYR1, and H1-1. Additional connected genes implicate vesicle trafficking, actin organization, mitochondrial regulation, and microtubule biology. Thus, the most defensible interpretation is a broadly expressed cellular homeostasis module with linked RNA-processing, chromatin, trafficking, cytoskeletal, and mitochondrial components, rather than a single confirmed biological pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, supporting a broadly expressed or housekeeping-like component. Cell-type-enhanced genes are diverse, including neutrophils, reproductive cell types, epithelial cells, neural cells, and other specialized populations, rather than forming a coherent bone or circulatory cell signature. Only a small minority show immune-cell enhancement, and the overall blood-cell specificity is low. Therefore, contamination by circulating proteins is unlikely to explain the module, although shared cellular populations or general cellular-state variation in the sampled tissues could contribute. HPA protein detection is unavailable for the queried bone and circulatory-system tissue labels, so tissue-level protein confirmation cannot be made.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The high-confidence STRING evidence is sparse and consists of three pairwise relationships: ACIN1 with NCBP3, AP1M1 with AP3D1, and SMARCA2 with SMARCC2. These relationships support specific local biological links involving RNA-related nuclear functions, adaptor-mediated trafficking, and the SWI/SNF chromatin-remodeling machinery, but they do not support a densely connected protein-interaction complex for the whole module. The hu.MAP evidence independently recapitulates several local relationships. ARL3 and EML4 occur together in huMAP complex (hu.MAP huMAP3_14884.1); SMARCA2 and SMARCC2 occur together in two related chromatin-remodeling complexes (hu.MAP huMAP3_11470.1) and (hu.MAP huMAP3_03221.1); PPP1R9B and LIMA1 occur together in an actin-associated complex (hu.MAP huMAP3_09542.1); and NCBP3 and ACIN1 occur together in an RNA-processing-associated complex (hu.MAP huMAP3_09943.1). In every case, only a small subset of the larger reference complex is represented, so these findings support known local machinery rather than a complete shared complex. The absence of STRING functional enrichment further argues against overinterpreting the module as a single established pathway.

**STRING interactions (score >= 0.7)**: 3 of 325 gene pairs: ACIN1–NCBP3 (0.717); AP1M1–AP3D1 (0.877); SMARCA2–SMARCC2 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14884.1 (ARL3, EML4; 2/10); huMAP3_11470.1 (SMARCA2, SMARCC2; 2/27); huMAP3_03221.1 (SMARCA2, SMARCC2; 2/28); huMAP3_09542.1 (PPP1R9B, LIMA1; 2/38); huMAP3_09943.1 (NCBP3, ACIN1; 2/78)

### Novelty

The module-level co-abundance pattern may be a new observation because the supplied resources establish only a few local physical or complex relationships and do not provide evidence that all module genes form a previously recognized biological unit. However, it cannot be called definitively novel from these data alone. Several edges correspond to known STRING relationships, and the hu.MAP matches show that parts of the module belong to established RNA-processing, chromatin-remodeling, cytoskeletal, and trafficking machinery. The appropriate conclusion is that the cross-tissue co-abundance organization is potentially novel, while its component molecular processes are largely established. Lack of STRING or hu.MAP coverage for the remaining relationships is evidence of limited prior support, not proof of biological novelty.

**Hypothesis.** Hypothesis: the conserved bone–circulatory-system module reflects coordinated abundance of broadly expressed intracellular machinery that couples RNA and chromatin regulation to cell structural maintenance, vesicle trafficking, mitochondrial activity, and survival responses. In shared or variable cell populations, coordinated regulation of RNA processing and chromatin state could influence expression of genes required for cytoskeletal remodeling, vesicle handling, mitochondrial calcium and metabolism, and apoptosis. The module may therefore represent a general cellular-state program preserved across the two tissue groups rather than a specialized extracellular or blood-borne signaling pathway. This hypothesis requires validation by cell-resolved expression, perturbation, and protein-level measurements.

### Important genes

#### CCDC137

- **Related proteins** (co-abundance neighbors): H1-1 (0.89), LIMA1 (0.85), RBMXL1 (0.85), ACIN1 (0.83), CSTF3 (0.81), NCBP3 (0.81), PPP1R9B (0.80), GLYR1 (0.80), DDX24 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coiled-coil domain containing 137. Enables RNA binding activity. Located in chromosome and fibrillar center. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.105); myopia (0.100); neoplasm (0.094); colorectal carcinoma (0.075); urinary bladder carcinoma (0.074)
- **Europe PMC papers**: 148
- **Why important**: CCDC137 is the most connected hub in the supplied co-abundance subgraph and links genes involved in nuclear RNA biology, chromatin-associated functions, and structural processes. Its annotation supports RNA binding and a nucleolar or fibrillar-center location, while its connections include ACIN1, NCBP3, CSTF3, RBMXL1, H1-1, LIMA1, PPP1R9B, and GLYR1. It has disease associations spanning neoplasm and several other conditions, but its direct mechanistic characterization is more limited than that of the better-studied genes in the module.
- **Conclusion**: Established evidence supports CCDC137 as a network hub associated with nuclear RNA-related biology. It is a strong marker of the module's coordinated expression architecture, but whether it actively organizes the module or merely tracks a shared cellular state remains unresolved.

#### SMARCA2

- **Related proteins** (co-abundance neighbors): GLYR1 (0.82), TFAM (0.80); STRING partners: SMARCC2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11470.1, huMAP3_03221.1
- **Function (MyGene.info)**: SWI/SNF related BAF chromatin remodeling complex subunit ATPase 2. The protein encoded by this gene is a member of the SWI/SNF family of proteins and is highly similar to the brahma protein of Drosophila. Members of this family have helicase and ATPase activities and are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/…
- **Diseases (Open Targets)**: intellectual disability-sparse hair-brachydactyly syndrome (0.854); blepharophimosis-impaired intellectual development syndrome (0.694); hereditary disease (0.527); Intellectual disability (0.501); blepharophimosis - intellectual disability syndrome (0.434)
- **Europe PMC papers**: 3654
- **Why important**: SMARCA2 is a catalytic ATPase subunit of the SWI/SNF chromatin-remodeling machinery. It is directly paired with SMARCC2 by STRING and appears with SMARCC2 in huMAP complexes (hu.MAP huMAP3_11470.1) and (hu.MAP huMAP3_03221.1). Its network links GLYR1 and TFAM, connecting chromatin regulation with mitochondrial and transcriptional biology. It has extensive literature and strong disease associations involving intellectual-developmental syndromes.
- **Conclusion**: Established evidence identifies SMARCA2 as a bona fide chromatin-remodeling component with a known relationship to SMARCC2. Its presence supports a transcriptional or chromatin-regulatory axis within the module. It does not establish that this module specifically controls bone or circulatory biology.

#### SMARCC2

- **Related proteins** (co-abundance neighbors): RBMXL1 (0.85); STRING partners: SMARCA2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11470.1, huMAP3_03221.1
- **Function (MyGene.info)**: SWI/SNF related BAF chromatin remodeling complex subunit C2. The protein encoded by this gene is a member of the SWI/SNF family of proteins, whose members display helicase and ATPase activities and which are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI and contains a predicted leucine zipper motif typical …
- **Diseases (Open Targets)**: Coffin-Siris syndrome 8 (0.720); Intellectual disability (0.564); Coffin-Siris syndrome (0.503); hereditary disease (0.468); Global developmental delay (0.463)
- **Europe PMC papers**: 1300
- **Why important**: SMARCC2 is a structural subunit of SWI/SNF chromatin-remodeling complexes and forms the strongest supplied STRING relationship with SMARCA2. Its membership in huMAP complexes (hu.MAP huMAP3_11470.1) and (hu.MAP huMAP3_03221.1) provides convergent complex-level support. It is associated with chromatin remodeling, transcriptional regulation, cell differentiation, and developmental disease, and therefore supplies a well-established mechanistic anchor for the chromatin component.
- **Conclusion**: Established evidence supports SMARCC2 as part of the same chromatin-remodeling machinery as SMARCA2. Its co-abundance with other module genes may reflect coordinated regulation of cellular transcriptional state, but a tissue-specific regulatory role remains a hypothesis.

#### CSTF3

- **Related proteins** (co-abundance neighbors): CCAR1 (0.89), AP3D1 (0.83), CDK5RAP3 (0.81), CCDC137 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cleavage stimulation factor subunit 3. The protein encoded by this gene is one of three (including CSTF1 and CSTF2) cleavage stimulation factors that combine to form the cleavage stimulation factor complex (CSTF). This complex is involved in the polyadenylation and 3' end cleavage of pre-mRNAs. The encoded protein functions as a homodimer and interacts directly with both CSTF1 and CSTF2 in the CSTF complex. Alternative splicing results…
- **Diseases (Open Targets)**: dengue disease (0.370); Hydrocephalus (0.192); retinitis pigmentosa (0.085); early-onset non-syndromic cataract (0.084); early-onset zonular cataract (0.080)
- **Europe PMC papers**: 477
- **Why important**: CSTF3 is a recognized component of the cleavage stimulation factor complex that performs pre-mRNA three-prime-end cleavage and polyadenylation. It is connected in the module to CCDC137, CCAR1, AP3D1, and CDK5RAP3, thereby bridging RNA processing with trafficking-associated and regulatory genes. Its disease and literature record is substantial, including associations with neurological and developmental conditions.
- **Conclusion**: Established evidence supports CSTF3 as a core mRNA-processing factor. Its position suggests that RNA maturation may be a meaningful component of the module's shared biology, although the co-abundance data do not show that CSTF3 directly regulates the other module genes.

#### ACIN1

- **Related proteins** (co-abundance neighbors): CCDC137 (0.83); STRING partners: NCBP3 (0.717)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09943.1
- **Function (MyGene.info)**: apoptotic chromatin condensation inducer 1. Apoptosis is defined by several morphologic nuclear changes, including chromatin condensation and nuclear fragmentation. This gene encodes a nuclear protein that induces apoptotic chromatin condensation after activation by caspase-3, without inducing DNA fragmentation. This protein has also been shown to be a component of a splicing-dependent multiprotein exon junction complex (EJC) that is deposi…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); adolescent idiopathic scoliosis (0.090); hepatocellular carcinoma (0.076); acute lymphoblastic leukemia (0.074); pancreatic neoplasm (0.045)
- **Europe PMC papers**: 894
- **Why important**: ACIN1 combines a direct STRING relationship with NCBP3 and membership with NCBP3 in huMAP complex (hu.MAP huMAP3_09943.1). It is a nuclear apoptosis-associated protein that also participates in splicing-related exon-junction biology, and its annotations include RNA splicing, apoptotic chromatin condensation, and regulation of monocyte differentiation. Its network connection to the hub CCDC137 makes it informative for the interface between RNA processing and cell survival.
- **Conclusion**: Established evidence supports ACIN1 as a nuclear RNA- and apoptosis-related factor with independent STRING and huMAP support for its relationship to NCBP3. Its connection to a broader survival or differentiation program in bone and circulation is plausible but remains unproven.

#### AP3D1

- **Related proteins** (co-abundance neighbors): CSTF3 (0.83), CCAR1 (0.80); STRING partners: AP1M1 (0.877)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor related protein complex 3 subunit delta 1. The protein encoded by this gene is a subunit of the AP3 adaptor-like complex, which is not clathrin-associated, but is associated with the golgi region, as well as more peripheral structures. The AP-3 complex facilitates the budding of vesicles from the golgi membrane, and may be directly involved in trafficking to lysosomes. This subunit is implicated in intracellular biogenesis and trafficking …
- **Diseases (Open Targets)**: Hermansky-Pudlak syndrome 10 (0.584); Hermansky-Pudlak syndrome 2 (0.455); Hermansky-Pudlak syndrome (0.432); Alzheimer disease (0.421); lysosomal storage disease (0.417)
- **Europe PMC papers**: 637
- **Why important**: AP3D1 is a subunit of the AP-3 adaptor complex, which participates in Golgi-derived vesicle formation and intracellular or lysosomal trafficking. It has a direct STRING relationship with AP1M1 and is connected in the co-abundance network to CSTF3 and CCAR1, linking vesicle biology with nuclear regulatory genes. Its disease associations include Hermansky–Pudlak and lysosomal-storage disorders, providing clinically relevant support for its trafficking function.
- **Conclusion**: Established evidence supports AP3D1 as a vesicle-trafficking component and confirms its relationship with AP1M1. Its presence suggests that intracellular transport may accompany the module's nuclear regulatory program, but the data do not establish a specific platelet, bone, or circulatory mechanism.

## Module 4

**Tissue pair**: bone and circulatory_system  
**Genes (30)**: AFG2A, AP1G2, ATXN10, CWF19L1, MTHFD1L, CASP7, EFL1, EXOC6B, FDFT1, FBXL18, TUBGCP2, IDE, KIF23, PPFIA1, MAGED1, MED23, MSI2, NFS1, NR2C2AP, DBT, PDPR, PNPO, PPP6R3, GINS1, PSMF1, ELAC2, SLC12A2, SIN3B, SMN1, TCP11L1

### Function

No GO/KEGG term passed global correction, so the module does not support a single statistically established pathway-level annotation. The network instead suggests a composite cellular-maintenance program involving proteostasis and regulated protein turnover through FBXL18, cell division and microtubule organization through KIF23 and associated genes, mitochondrial metabolism through MTHFD1L and PDPR, intracellular trafficking through EXOC6B, and apoptosis through CASP7. These processes are connected only by the co-abundance structure; they should not be treated as a formally enriched biological pathway. The sparse, hub-and-spoke topology is compatible with coordinated cellular state, but it is not evidence of direct physical interaction among the genes.

**Cell composition.** The module is not dominated by plasma or secreted proteins: HPA identifies only a small secreted component, and most genes have low immune-cell specificity. Most genes have low tissue specificity, while a substantial subset is cell-type enhanced across diverse populations, including cardiomyocytes, oligodendrocytes, reproductive cell types, erythrocyte progenitors, and other specialized cells. The presence of genes enhanced in blood vessel, heart muscle, lymphoid tissue, and bone marrow is compatible with contributions from shared vascular, marrow, or other cellular states, but the HPA summary does not support interpreting the module as a simple blood-cell or plasma-protein signature. HPA provides no matching protein-detection evidence for either named tissue, so tissue-level protein validation is unavailable.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no STRING interactions among the module genes at the supplied high-confidence threshold, and STRING functional enrichment is absent. Thus, STRING provides no established direct interaction network for this module. hu.MAP supplies partial complex-level support. MTHFD1L, PDPR, and ELAC2 occur together in complex (hu.MAP huMAP3_13468.1), while MTHFD1L and PDPR also occur together in (hu.MAP huMAP3_10525.1). These observations support a pre-existing mitochondrial or metabolic complex context for part of the module, but the module contains only a small subset of each complex and hu.MAP does not connect the remaining genes into one physical assembly. The co-abundance relationships therefore extend beyond currently catalogued protein-complex membership.

**STRING interactions (score >= 0.7)**: 0 of 435 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (MTHFD1L, PDPR, ELAC2; 3/99); huMAP3_10525.1 (MTHFD1L, PDPR; 2/33)

### Novelty

The shared co-abundance pattern is potentially novel because it is not recapitulated by a high-confidence STRING interaction network or by a globally significant GO/KEGG annotation, while only a limited substructure is represented in hu.MAP complexes (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1). However, this is not proof of a new molecular complex or pathway. Lack of STRING or hu.MAP support can reflect incomplete interaction coverage, context dependence, tissue composition, indirect regulation, or correlated cell states. The defensible conclusion is that the cross-tissue co-abundance module is a potentially new systems-level observation whose biological mechanism remains to be validated.

**Hypothesis.** Hypothesis: the module reflects a coordinated cellular adaptation shared by bone-associated and circulatory-system-associated samples rather than a single lineage-specific pathway. Mitochondrial metabolic capacity, proteostasis, cytoskeletal remodeling, vesicle trafficking, and controlled cell turnover may vary together across the contributing cells. MTHFD1L and PDPR could mark the metabolic component, FBXL18 could organize proteasomal regulation and link several module branches, KIF23 could reflect proliferative or cytoskeletal state, EXOC6B could reflect trafficking and cardiomyocyte-associated cellular organization, and CASP7 could report regulated apoptotic potential. This hypothesis predicts that module activity will track cellular composition or physiological state and should be tested with independent tissue cohorts, cell-composition adjustment, protein measurements, and perturbation experiments.

### Important genes

#### FBXL18

- **Related proteins** (co-abundance neighbors): PPFIA1 (0.91), AFG2A (0.89), SLC12A2 (0.86), EXOC6B (0.85), KIF23 (0.84), CASP7 (0.83), MTHFD1L (0.82), TUBGCP2 (0.81), PSMF1 (0.81), GINS1 (0.81), ATXN10 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: F-box and leucine rich repeat protein 18. The protein encoded by this gene is a member of a family of proteins that contain an approximately 40-amino acid F-box motif. This motif is important for interaction with SKP1 and for targeting some proteins for degradation. The encoded protein has been shown to control the cellular level of FBXL7, a protein that induces mitotic arrest, by targeting it for polyubiquitylation and proteasomal degrad…
- **Diseases (Open Targets)**: neurodegenerative disease (0.320); adolescent idiopathic scoliosis (0.214); Abnormality of the skeletal system (0.212); diabetic ketoacidosis (0.204); Crohn disease (0.080)
- **Europe PMC papers**: 209
- **Why important**: FBXL18 is the strongest network hub in the supplied subgraph and connects proteostasis-related biology with cell-cycle, transport, apoptosis, and metabolic neighbors. Its F-box function provides an established mechanism for substrate targeting and proteasomal degradation, and the fact sheet links it to regulation of apoptotic processes. It has disease associations spanning neurodegeneration and skeletal-system abnormalities, although its literature volume is more limited than that of several other selected genes. Its central network position makes it an important candidate for organizing the module's co-abundance signal.
- **Conclusion**: Established evidence supports FBXL18 as an F-box protein involved in regulated protein degradation and apoptosis-related control, with a prominent position in this module. It is a plausible module coordinator, but the co-abundance data do not establish that FBXL18 directly regulates the other module genes. Its coordinating role is therefore a hypothesis requiring perturbational validation.

#### KIF23

- **Related proteins** (co-abundance neighbors): MAGED1 (0.87), PDPR (0.84), FBXL18 (0.84), MED23 (0.82), CWF19L1 (0.81), DBT (0.81), MSI2 (0.81), EXOC6B (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 23. The protein encoded by this gene is a member of kinesin-like protein family. This family includes microtubule-dependent molecular motors that transport organelles within cells and move chromosomes during cell division. This protein has been shown to cross-bridge antiparallel microtubules and drive microtubule movement in vitro. Alternate splicing of this gene results in multiple transcript variant…
- **Diseases (Open Targets)**: congenital dyserythropoietic anemia type 3 (0.735); hypertensive disorder (0.436); neurodegenerative disease (0.370); cardiovascular disorder (0.302); essential hypertension (0.302)
- **Europe PMC papers**: 2136
- **Why important**: KIF23 is one of the principal network hubs and has extensive literature support. Its established functions in kinesin-dependent microtubule movement, mitotic spindle organization, and cytokinesis provide a coherent cellular interpretation for its links to MAGED1, FBXL18, EXOC6B, and other module members. HPA enhancement in bone marrow and lymphoid tissue, including erythrocyte progenitors, is especially relevant to the tissue pair, and disease associations include congenital dyserythropoietic anemia and cardiovascular or hypertensive disorders.
- **Conclusion**: Established evidence supports KIF23 as a cell-division and microtubule-regulation gene with relevant marrow-associated expression. It may indicate proliferative or cytoskeletal state in the shared module, but it does not prove that the entire module is a proliferation program because no GO/KEGG term passed global correction.

#### MTHFD1L

- **Related proteins** (co-abundance neighbors): FDFT1 (0.86), FBXL18 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1
- **Function (MyGene.info)**: methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 1 like. The protein encoded by this gene is involved in the synthesis of tetrahydrofolate (THF) in the mitochondrion. THF is important in the de novo synthesis of purines and thymidylate and in the regeneration of methionine from homocysteine. Several transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Jun 2011].
- **Diseases (Open Targets)**: Alzheimer disease (0.343); Abnormality of refraction (0.315); refractive error (0.312); COVID-19 (0.296); severe acute respiratory syndrome (0.295)
- **Europe PMC papers**: 1180
- **Why important**: MTHFD1L is a network connector and is present in both hu.MAP complexes (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1), where it occurs with PDPR and, in (hu.MAP huMAP3_13468.1), ELAC2. Its established mitochondrial tetrahydrofolate-related function links one part of the module to formate and one-carbon metabolism. HPA reports tissue enhancement in blood vessel and cell-type enhancement in several vascular or cardiac-associated populations, while disease associations include neurodegenerative and vascular-relevant conditions. Its network and complex context make it a strong anchor for the metabolic interpretation.
- **Conclusion**: Established evidence supports MTHFD1L as a mitochondrial one-carbon-metabolism enzyme and as part of the partial hu.MAP context represented by (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1). It may connect metabolic state to the shared bone–circulatory co-abundance pattern, but the module does not establish a direct metabolic pathway enrichment or a causal role for MTHFD1L.

#### PDPR

- **Related proteins** (co-abundance neighbors): KIF23 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1
- **Function (MyGene.info)**: pyruvate dehydrogenase phosphatase regulatory subunit. Pyruvate dehydrogenase complex (PDC) catalyzes the oxidative decarboxylation of pyruvate and links glycolysis to the tricarboxylic acid cycle and fatty acid synthesis. The dephosphorylation and reactivation of PDC is catalyzed by pyruvate dehydrogenase phosphatase (PDP). The dimeric PDP has a catalytic subunit and a regulatory subunit. This gene encodes the FAD-containing regulatory subunit of PDP…
- **Diseases (Open Targets)**: osteoarthritis, hip (0.288); total joint arthroplasty (0.285); osteoarthritis, knee (0.285); viral pneumonia (0.262); Alzheimer disease (0.223)
- **Europe PMC papers**: 326
- **Why important**: PDPR is a member of both hu.MAP complexes (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1) and is linked in the module to KIF23. Its established role as a regulatory subunit of pyruvate dehydrogenase phosphatase connects mitochondrial pyruvate utilization with acetyl-CoA production and broader cellular energy state. The fact sheet also reports associations with osteoarthritis and joint-related outcomes, which are relevant to bone biology, although its literature volume is more limited than that of KIF23 or CASP7.
- **Conclusion**: Established evidence supports PDPR as a mitochondrial regulator of pyruvate dehydrogenase activity and as part of the partial complexes (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1). Its placement suggests that energy metabolism may contribute to the module, but a direct connection between PDPR and the bone–circulatory shared phenotype remains a hypothesis.

#### EXOC6B

- **Related proteins** (co-abundance neighbors): FBXL18 (0.85), PPP6R3 (0.82), NR2C2AP (0.82), KIF23 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exocyst complex component 6B. This gene encodes a protein which is a part of the evolutionarily conserved exocyst, a multimeric protein complex necessary for exocytosis, which in turn, is crucial for cell growth, polarity and migration. Disruption of this gene may be associated with phenotypes exhibiting multiple symptoms including intellectual disability and developmental delay (DD). [provided by RefSeq, Jun 2016].
- **Diseases (Open Targets)**: spondyloepimetaphyseal dysplasia with joint laxity, type 3 (0.679); neurodegenerative disease (0.540); rectosigmoid junction neoplasm (0.277); muscular dystrophy (0.255); prostatitis (0.229)
- **Europe PMC papers**: 284
- **Why important**: EXOC6B occupies a connected position between FBXL18, KIF23, PPP6R3, and NR2C2AP. Its established role in the exocyst complex links it to exocytosis, cell polarity, membrane trafficking, and cell growth. HPA reports enhancement in heart muscle and cardiomyocytes, making it particularly informative for the circulatory-system side of the module. Its disease associations include skeletal developmental abnormalities and muscular or neurodevelopmental conditions.
- **Conclusion**: Established evidence supports EXOC6B as an exocyst-associated trafficking factor with heart- and cardiomyocyte-relevant HPA expression. It may represent a trafficking or cellular-architecture component of the module, but the absence of STRING support means that the inferred links to the other module genes are co-abundance relationships rather than established physical interactions.

#### CASP7

- **Related proteins** (co-abundance neighbors): PSMF1 (0.90), NR2C2AP (0.86), FBXL18 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caspase 7. This gene encodes a member of the cysteine-aspartic acid protease (caspase) family. Sequential activation of caspases plays a central role in the execution-phase of cell apoptosis. Caspases exist as inactive proenzymes which undergo proteolytic processing at conserved aspartic residues to produce two subunits, large and small, that dimerize to form the active enzyme. The precursor of the encoded p…
- **Diseases (Open Targets)**: cataract (0.609); Age-related cataract (0.334); lens disorder (0.330); neurodegenerative disease (0.294); glaucoma (0.279)
- **Europe PMC papers**: 3507
- **Why important**: CASP7 has a highly studied role as an executioner caspase in apoptosis and is connected in the module to PSMF1, NR2C2AP, and FBXL18. Its extensive literature and disease associations provide strong biological interpretability. HPA describes intracellular and membrane-associated localization and cell-type enhancement in gastrointestinal epithelial populations, while the network places CASP7 at an interface between proteostasis, nuclear regulation, and the module hub.
- **Conclusion**: Established evidence supports CASP7 as an apoptosis effector and protease. Its presence may indicate regulated cell turnover or stress-related state in the samples, but it does not establish that apoptosis is the primary function of the complete module, especially because no globally significant GO/KEGG term was detected.

## Module 5

**Tissue pair**: bone and circulatory_system  
**Genes (48)**: AKR1D1, AKAP12, CALD1, CAPRIN1, CCDC9B, CD44, CEBPB, CMBL, DPH2, EMC10, ERBIN, GPAT3, GPN1, HIP1, IGF2BP3, KDSR, LDLR, MBNL1, METTL15, MVD, OCC1, PLGRKT, PPIE, PXMP2, NRAS, MRPL1, RRAS, MRPS11, MRPS22, TMEM97, SMTN, SPAG5, CTTN, STX7, CCDC59, TST, TMEM70, TPM1, TPX2, TRMT61A, TXNL4B, UTP6, UTRN, VAC14, XTBD1, ZC3H4, ZNF185, SLC30A7

### Function

This module does not support a single formally enriched GO or KEGG function: no GO/KEGG term passed global correction, and there were no supplementary STRING enrichment terms. The gene set is heterogeneous but converges on several related biological themes. A prominent branch involves actin cytoskeleton, contractility, adhesion, and vascular or smooth-muscle biology, represented by CALD1, TPM1, SMTN, CTTN, UTRN, and RRAS. Other branches involve lipid and cholesterol metabolism, mitochondrial translation or energy-related processes, RNA processing, vesicle trafficking, and cell-cycle or spindle functions. CEBPB is the principal co-abundance hub and links contractile, cytoskeletal, mitochondrial, and signaling-associated genes. The most defensible interpretation is therefore a mixed structural and cellular-state module rather than a narrowly defined pathway. The functional interpretation is suggestive and network-supported, not established by enrichment statistics.

**Cell composition.** The module is not dominated by plasma or secreted proteins; only a small subset has secretome annotation, including CD44 and EMC10. It is also not uniformly tissue-specific: many genes have low tissue specificity, while others are enhanced in skeletal muscle, liver, kidney, blood vessel, or lymphoid tissue. HPA single-cell evidence shows broad cell-type enhancement, with recurring signals in neutrophils, basophils, monocytes, trophoblast-related cells, muscle-related cells, and epithelial populations. Several genes have immune-cell enhancement or enrichment, including CEBPB, CALD1, CD44, HIP1, STX7, and related module members. This pattern argues that the shared bone and circulatory_system signal may partly reflect common vascular, stromal, smooth-muscle, immune, or blood-associated cell populations in the sampled tissues. It does not establish that the module is a circulating-protein module, and the absence of matching HPA protein data for the two tissue labels limits tissue-level protein interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a small set of established high-confidence relationships within the module. The contractile pair CALD1–TPM1 is known, as are the mitochondrial ribosomal relationships METTL15–MRPS11, METTL15–MRPS22, MRPL1–MRPS11, MRPL1–MRPS22, and MRPS11–MRPS22. SPAG5–TPX2 is an established spindle-associated relationship. These interactions support real local subnetworks, especially contractile cytoskeletal and mitochondrial translation subnetworks, but they do not validate the entire co-abundance module as one physical complex. hu.MAP independently supports several partial complexes: GPAT3, SLC30A7, and TMEM70 occur in (hu.MAP huMAP3_06247.1); CALD1 and CTTN occur in (hu.MAP huMAP3_06395.1) and (hu.MAP huMAP3_10673.1); RRAS and OCC1 occur in (hu.MAP huMAP3_12303.1) and (hu.MAP huMAP3_12658.1); and MRPS22 and MRPS11 occur in (hu.MAP huMAP3_05954.1). Because each complex contains only a subset of the module members, the hu.MAP evidence favors multiple embedded molecular systems rather than one unified complex. The co-abundance edges that lack STRING or hu.MAP support should be interpreted as expression-state relationships or possible indirect associations, not established physical interactions.

**STRING interactions (score >= 0.7)**: 7 of 1128 gene pairs: CALD1–TPM1 (0.869); METTL15–MRPS11 (0.878); METTL15–MRPS22 (0.866); MRPL1–MRPS11 (0.978); MRPL1–MRPS22 (0.933); MRPS11–MRPS22 (0.998); SPAG5–TPX2 (0.854)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06247.1 (GPAT3, SLC30A7, TMEM70; 3/65); huMAP3_06395.1 (CALD1, CTTN; 2/8); huMAP3_10673.1 (CALD1, CTTN; 2/14); huMAP3_12303.1 (RRAS, OCC1; 2/22); huMAP3_05954.1 (MRPS22, MRPS11; 2/28); huMAP3_12658.1 (RRAS, OCC1; 2/32)

### Novelty

The module may be novel as a cross-tissue co-abundance pattern, but the fact sheet does not establish a new molecular mechanism. Several internal relationships are already known through STRING or hu.MAP, and many component genes have well-established individual functions. What may be new is the specific combination and coordinated abundance pattern across bone and circulatory_system, particularly the juxtaposition of contractile or vascular genes with lipid, mitochondrial, RNA-processing, and immune-associated signals. Absence of a complete STRING or hu.MAP representation cannot by itself demonstrate novelty. The most cautious conclusion is that this is a potentially novel tissue-pair association built from partly familiar biological subnetworks, requiring replication, cell-composition adjustment, and independent experimental validation.

**Hypothesis.** Hypothesis: the module reflects a shared vascular or stromal cellular state present in bone and circulatory_system, with variable contributions from smooth-muscle-like, endothelial-associated, immune, and blood-cell populations. In this model, CEBPB-linked transcriptional state is co-abundant with actin-contractile machinery involving CALD1, TPM1, SMTN, and CTTN; RRAS-associated signaling connects this state to vascular homeostasis, adhesion, migration, and angiogenesis; lipid handling and mitochondrial protein synthesis provide metabolic support for the state. CD44 and vesicle-trafficking genes could couple adhesion and inflammatory cell interactions to tissue remodeling. This is a hypothesis rather than an established pathway assignment, because global enrichment was absent and the module contains several disconnected molecular systems.

### Important genes

#### CEBPB

- **Related proteins** (co-abundance neighbors): TXNL4B (0.90), CCDC59 (0.89), CALD1 (0.87), TPM1 (0.85), SMTN (0.85), CTTN (0.81), TMEM70 (0.80), NRAS (0.80), MRPL1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CCAAT enhancer binding protein beta. This intronless gene encodes a transcription factor that contains a basic leucine zipper (bZIP) domain. The encoded protein functions as a homodimer but can also form heterodimers with CCAAT/enhancer-binding proteins alpha, delta, and gamma. Activity of this protein is important in the regulation of genes involved in immune and inflammatory responses, among other processes. The use of alternative …
- **Diseases (Open Targets)**: neurodegenerative disease (0.536); type 2 diabetes mellitus (0.402); diabetes mellitus (0.370); autoimmune disorder of central nervous system (0.370); bile duct disorder (0.328)
- **Europe PMC papers**: 9284
- **Why important**: CEBPB is the central network hub and connects genes involved in cytoskeletal structure, contractility, signaling, and cellular metabolism. Its established role as a bZIP transcription factor regulating immune and inflammatory gene programs fits the recurrent neutrophil and monocyte-related HPA signal. It has extensive literature and disease-linked evidence, making it a strong anchor for interpreting the module's cellular-state component even though it has no STRING or hu.MAP relationship within this module.
- **Conclusion**: Established evidence supports CEBPB as an inflammatory and transcriptional regulator with a central position in this co-abundance network. It is plausible that CEBPB marks a shared immune, vascular, or stromal state, but the module does not demonstrate that CEBPB directly regulates the other module genes here.

#### CALD1

- **Related proteins** (co-abundance neighbors): GPN1 (0.88), CEBPB (0.87), DPH2 (0.82); STRING partners: TPM1 (0.869)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Actin filaments; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06395.1, huMAP3_10673.1
- **Function (MyGene.info)**: caldesmon 1. This gene encodes a calmodulin- and actin-binding protein that plays an essential role in the regulation of smooth muscle and nonmuscle contraction. The conserved domain of this protein possesses the binding activities to Ca(2+)-calmodulin, actin, tropomyosin, myosin, and phospholipids. This protein is a potent inhibitor of the actin-tropomyosin activated myosin MgATPase, and serves as a mediating…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.499); diaphragmatic hernia (0.447); glaucoma (0.405); diverticular disease (0.393); open-angle glaucoma (0.390)
- **Europe PMC papers**: 3386
- **Why important**: CALD1 is connected to the module hub CEBPB and participates in the contractile cytoskeletal branch. Its established actin-, calmodulin-, tropomyosin-, and myosin-related functions are reinforced by the STRING relationship with TPM1 and hu.MAP membership in (hu.MAP huMAP3_06395.1) and (hu.MAP huMAP3_10673.1) with CTTN. Its skeletal-system disease associations and immune-cell enrichment make it relevant to both the tissue pair and the possible cell-composition explanation.
- **Conclusion**: Established evidence supports CALD1 as a structural regulator of smooth-muscle and nonmuscle contraction and as part of a known contractile subnetwork. Its role as a mediator linking inflammatory state to bone–circulatory remodeling remains a hypothesis.

#### RRAS

- **Related proteins** (co-abundance neighbors): HIP1 (0.84), GPAT3 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12303.1, huMAP3_12658.1
- **Function (MyGene.info)**: RAS related. The protein encoded by this gene is a small GTPase involved in diverse processes including angiogenesis, vascular homeostasis and regeneration, cell adhesion, and neuronal axon guidance. Mutations in this gene are found in many invasive cancers. [provided by RefSeq, Jul 2015].
- **Diseases (Open Targets)**: Noonan syndrome (0.424); Noonan syndrome and Noonan-related syndrome (0.370); hypertensive disorder (0.324); neurodegenerative disease (0.288); hereditary disease (0.266)
- **Europe PMC papers**: 1607
- **Why important**: RRAS links the module to vascular biology through established functions in angiogenesis, endothelial migration, vascular homeostasis, polarity, and adhesion. It connects to HIP1 and GPAT3 in the co-abundance graph and appears with OCC1 in hu.MAP complexes (hu.MAP huMAP3_12303.1) and (hu.MAP huMAP3_12658.1). Its HPA enhancement in blood vessel and monocyte-related populations strengthens its relevance to a shared circulatory and stromal signal.
- **Conclusion**: Established evidence supports RRAS as a vascular and cell-adhesion-associated small GTPase with a biologically plausible position in this module. The claim that it coordinates the whole module, or directly links its contractile and metabolic branches, is not established.

#### CD44

- **Related proteins** (co-abundance neighbors): UTP6 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD44 molecule (IN blood group). The protein encoded by this gene is a cell-surface glycoprotein involved in cell-cell interactions, cell adhesion and migration. It is a receptor for hyaluronic acid (HA) and can also interact with other ligands, such as osteopontin, collagens, and matrix metalloproteinases (MMPs). This protein participates in a wide variety of cellular functions including lymphocyte activation, recirculation and …
- **Diseases (Open Targets)**: nephrolithiasis, calcium oxalate (0.523); calcium oxalate urolithiasis (0.521); uterine corpus leiomyoma (0.480); systemic lupus erythematosus (0.467); autoimmune disease (0.330)
- **Europe PMC papers**: 102058
- **Why important**: CD44 is a highly studied cell-surface adhesion and migration receptor with established roles in hyaluronan interaction, hematopoiesis, lymphocyte trafficking, inflammation, and cell-matrix adhesion. It connects to UTP6 in the module and is annotated as secreted to blood, while its single-cell profile includes monocytes, neutrophils, dendritic cells, and mast cells. Its extensive literature and autoimmune and renal disease associations make it especially informative for distinguishing tissue biology from blood-cell or immune-cell contribution.
- **Conclusion**: Established evidence supports CD44 as a cell-interaction and immune-trafficking marker that could contribute to the shared tissue signal. Its presence does not prove that the module is secreted or circulating, and its mechanistic connection to the other subnetworks remains hypothetical.

#### TMEM70

- **Related proteins** (co-abundance neighbors): CEBPB (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06247.1
- **Function (MyGene.info)**: transmembrane protein 70. This gene likely encodes a mitochondrial membrane protein. The encoded protein may play a role in biogenesis of mitochondrial ATP synthase. Mutations in this gene have been associated with neonatal mitochondrial encephalocardiomyopathy due to ATP synthase deficiency. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: mitochondrial complex V (ATP synthase) deficiency, nuclear type 2 (0.811); mitochondrial disease (0.597); mitochondrial proton-transporting ATP synthase complex deficiency (0.588); hereditary disease (0.413); cardiomyopathy (0.371)
- **Europe PMC papers**: 490
- **Why important**: TMEM70 is tissue-enriched in skeletal muscle, is mitochondrial, and is annotated in mitochondrial ATP synthase assembly and respiratory-chain-related processes. It occurs with GPAT3 and SLC30A7 in hu.MAP complex (hu.MAP huMAP3_06247.1) and is connected to the central CEBPB node in the co-abundance graph. Its established association with mitochondrial ATP synthase deficiency and cardiomyopathy makes it relevant to the energy demands of muscle, vascular, or remodeling-associated cells.
- **Conclusion**: Established evidence supports TMEM70 as a mitochondrial ATP synthase biogenesis factor and a marker of an energy-related component of the module. The proposed coupling of mitochondrial capacity to the contractile or vascular state is a mechanistic hypothesis, not a demonstrated property of this module.

## Module 6

**Tissue pair**: bone and circulatory_system  
**Genes (7)**: CANX, MT-CO2, HSD17B4, DDOST, RAB5C, TUSC3, VDAC2

### Function

The strongest functional interpretation is an endoplasmic-reticulum protein maturation module centered on N-linked glycosylation and glycoprotein quality control. (GO:CC oligosaccharyltransferase complex; q_global = 0.0412) identifies the oligosaccharyltransferase complex through DDOST and TUSC3, providing the only globally corrected GO/KEGG evidence. DDOST is an oligosaccharyltransferase component that transfers high-mannose oligosaccharides to nascent proteins, while TUSC3 is an ER oligosaccharyltransferase component also associated with protein glycosylation. CANX provides a compatible ER folding and quality-control function. The STRING results are consistent with this interpretation through the supplementary oligosaccharyltransferase and spike-protein-maturation terms (STRING RCTM Maturation of spike protein; within-query FDR = 0.0044) and (STRING COMPARTMENTS Oligosaccharyltransferase complex; within-query FDR = 0.0436). The remaining genes suggest linked organelle physiology rather than a single uniformly annotated pathway: MT-CO2 and VDAC2 relate to mitochondrial respiration and membrane function, RAB5C to endosomal transport, and HSD17B4 to peroxisomal fatty-acid metabolism. Thus, the module is best interpreted as an ER glycoprotein-processing core embedded in a broader organelle homeostasis program, rather than as evidence that every member performs N-linked glycosylation.

**Cell composition.** The module contains no secreted genes, so it does not resemble a plasma-protein or secreted-protein module. HPA indicates generally low tissue specificity for most members, with tissue enhancement for MT-CO2 in heart muscle and HSD17B4 in liver. Most genes show cell-type enhancement rather than strong tissue restriction, including hepatocytes, trophoblast populations, spermatogenic cells and other specialized cell types. Immune-cell specificity is generally low; HSD17B4 is immune-cell enhanced in basophils, whereas TUSC3 is not detected in immune cells. These findings argue against a simple blood-cell-enriched explanation, although shared cellular composition or broadly active organelle programs could contribute to the bone and circulatory_system co-abundance signal. HPA provides no matching bone or circulatory_system protein-detection evidence, so tissue-specific protein localization cannot be established from this dataset.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC oligosaccharyltransferase complex | 0.0412 | DDOST, TUSC3 |

### STRING and hu.MAP

The known physical or functional core is DDOST with TUSC3, supported by a very strong STRING relationship and by both hu.MAP complexes (hu.MAP huMAP3_09893.1) and (hu.MAP huMAP3_10071.1). Those complexes include additional oligosaccharyltransferase-associated or ER components, including DAD1, STT3B, LMF2 and related ER membrane factors, which reinforces the interpretation of an ER glycosylation complex. CANX is also connected to DDOST by STRING and supplies a biologically coherent ER folding-quality-control link. The supplementary STRING terms for organelle membrane (STRING COMPARTMENTS Organelle membrane; within-query FDR = 0.0129), macrophage proteome signatures (STRING PMID (2019) A Pathogen and a Non-pathogen Spotted Fever Group Rickettsia Trigger Differential Proteome Signatures in Macrophages.; within-query FDR = 0.0148) and spike-protein maturation (STRING RCTM Maturation of spike protein; within-query FDR = 0.0044) provide contextual support but are not globally corrected module-level enrichment evidence. The other module members do not have reported high-confidence STRING partners or hu.MAP complexes within the supplied results, so their inclusion is primarily based on co-abundance and compatible organelle annotations rather than established physical interaction.

**STRING interactions (score >= 0.7)**: 2 of 21 gene pairs: CANX–DDOST (0.886); DDOST–TUSC3 (0.998)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Maturation of spike protein (FDR = 0.0044, 3 genes); COMPARTMENTS Organelle membrane (FDR = 0.0129, 7 genes); PMID (2019) A Pathogen and a Non-pathogen Spotted Fever Group Rickettsia Trigger Differential Proteome Signatures in Macrophages. (FDR = 0.0148, 5 genes); COMPARTMENTS Oligosaccharyltransferase complex (FDR = 0.0436, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09893.1 (DDOST, TUSC3; 2/5); huMAP3_10071.1 (DDOST, TUSC3; 2/10)

### Novelty

This module should not be described as a newly discovered molecular complex. The DDOST-TUSC3 relationship, their participation in hu.MAP complexes, and the CANX-DDOST relationship are already established in interaction or complex resources. The potentially novel aspect is the conserved co-abundance of this ER-centered core with MT-CO2, VDAC2, RAB5C and HSD17B4 across bone and circulatory_system. That cross-tissue network organization is not directly established by the supplied databases, but it requires validation because co-abundance can reflect shared cell composition, organelle state or coordinated stress responses. The absence of STRING or hu.MAP relationships for some edges does not prove that those relationships are novel. Overall, the module is a potentially interesting tissue-pair co-abundance observation built around a known glycosylation core, not evidence of a wholly new pathway.

**Hypothesis.** Hypothesis: in both bone and circulatory_system, variation in secretory-cell or other metabolically active cell populations may coordinate ER glycoprotein maturation with mitochondrial, peroxisomal and endosomal maintenance. DDOST and TUSC3 could form the functional anchor for nascent-protein glycosylation, with CANX supporting folding and quality control. Coupling of this ER program to MT-CO2 and VDAC2 could reflect changes in respiratory capacity or mitochondrial membrane state, while RAB5C could reflect altered trafficking and HSD17B4 could reflect lipid-handling or metabolic adaptation. This hypothesis is consistent with the network structure and annotations, but the supplied evidence does not demonstrate direct regulation, physical interaction among all members, or a bone-specific or circulatory-specific mechanism.

### Important genes

#### TUSC3

- **Related proteins** (co-abundance neighbors): MT-CO2 (0.87), RAB5C (0.87), CANX (0.84), VDAC2 (0.83), DDOST (0.82), HSD17B4 (0.82); STRING partners: DDOST (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09893.1, huMAP3_10071.1
- **Function (MyGene.info)**: tumor suppressor candidate 3. This gene encodes a protein that has been associated with several biological functions including cellular magnesium uptake, protein glycosylation and embryonic development. This protein localizes to the endoplasmic reticulum and acts as a component of the oligosaccharyl transferase complex which is responsible for N-linked protein glycosylation. This gene is a candidate tumor suppressor gene. Homo…
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.648); dengue disease (0.505); Intellectual disability (0.499); hereditary disease (0.486); Abnormality of the skeletal system (0.468)
- **Europe PMC papers**: 1002
- **Why important**: TUSC3 is the strongest network anchor in the module, connecting to every other member in the co-abundance subgraph. It is one of the two genes in the globally significant oligosaccharyltransferase term (GO:CC oligosaccharyltransferase complex; q_global = 0.0412), participates in both hu.MAP complexes (hu.MAP huMAP3_09893.1) and (hu.MAP huMAP3_10071.1), and has a high-confidence STRING relationship with DDOST. Its established functions include ER localization, protein N-linked glycosylation, magnesium transport and embryonic development. It also has disease associations involving autosomal recessive intellectual disability and skeletal-system abnormality, together with substantial literature coverage.
- **Conclusion**: Established evidence supports TUSC3 as the central ER glycosylation-related member and the principal network organizer. A role in coordinating the other organelle programs is a hypothesis from its network position, not an established molecular function of this module.

#### DDOST

- **Related proteins** (co-abundance neighbors): TUSC3 (0.82); STRING partners: CANX (0.886), TUSC3 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09893.1, huMAP3_10071.1
- **Function (MyGene.info)**: dolichyl-diphosphooligosaccharide--protein glycosyltransferase non-catalytic subunit. This gene encodes a component of the oligosaccharyltransferase complex which catalyzes the transfer of high-mannose oligosaccharides to asparagine residues on nascent polypeptides in the lumen of the rough endoplasmic reticulum. The protein complex co-purifies with ribosomes. The product of this gene is also implicated in the processing of advanced glycation endproducts (AGEs), which form from non…
- **Diseases (Open Targets)**: DDOST-congenital disorder of glycosylation (0.734); young-onset Parkinson disease (0.561); neurodegenerative disease (0.539); dengue disease (0.505); congenital disorder of glycosylation (0.373)
- **Europe PMC papers**: 685
- **Why important**: DDOST is directly represented in the globally significant oligosaccharyltransferase term (GO:CC oligosaccharyltransferase complex; q_global = 0.0412). It has the strongest supplied STRING relationship with TUSC3, an additional relationship with CANX, and membership in both hu.MAP complexes (hu.MAP huMAP3_09893.1) and (hu.MAP huMAP3_10071.1). Its established function is as a non-catalytic oligosaccharyltransferase-complex component involved in transfer of oligosaccharides to nascent proteins in the ER. It is associated with congenital disorders of glycosylation and neurodegenerative disease and has a substantial literature base.
- **Conclusion**: Established evidence makes DDOST a core molecular component of the module’s ER glycoprotein-processing interpretation. Its possible contribution to cross-organelle coordination or tissue-pair conservation remains a hypothesis.

#### CANX

- **Related proteins** (co-abundance neighbors): TUSC3 (0.84); STRING partners: DDOST (0.886)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX links the network anchor TUSC3 to an established ER quality-control function and has a high-confidence STRING relationship with DDOST. Its annotations support calnexin-mediated folding and assembly of newly synthesized N-linked glycoproteins, retention of misfolded proteins and ER-associated degradation. It appears in the supplementary spike-protein-maturation and organelle-membrane terms (STRING RCTM Maturation of spike protein; within-query FDR = 0.0044) and (STRING COMPARTMENTS Organelle membrane; within-query FDR = 0.0129). It is associated with neurodegenerative and viral infectious diseases and has broad literature coverage.
- **Conclusion**: Established evidence supports CANX as a compatible ER folding and quality-control partner of the glycosylation core. Any claim that CANX drives the conserved bone and circulatory_system co-abundance pattern is a hypothesis rather than a demonstrated mechanism.

#### HSD17B4

- **Related proteins** (co-abundance neighbors): TUSC3 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Peroxisomes; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydroxysteroid 17-beta dehydrogenase 4. The protein encoded by this gene is a bifunctional enzyme that is involved in the peroxisomal beta-oxidation pathway for fatty acids. It also acts as a catalyst for the formation of 3-ketoacyl-CoA intermediates from both straight-chain and 2-methyl-branched-chain fatty acids. Defects in this gene that affect the peroxisomal fatty acid beta-oxidation activity are a cause of D-bifunctional protein d…
- **Diseases (Open Targets)**: d-bifunctional protein deficiency (0.830); Perrault syndrome 1 (0.761); Perrault syndrome (0.736); hereditary disease (0.488); hearing loss disorder (0.370)
- **Europe PMC papers**: 1624
- **Why important**: HSD17B4 is connected to the module hub by co-abundance and is the only member with tissue enhancement in liver and immune-cell enhancement in basophils according to the supplied HPA summary. It has established peroxisomal beta-oxidation and fatty-acid metabolic functions, is associated with D-bifunctional protein deficiency and Perrault syndrome, and has substantial literature coverage. Its presence broadens the module beyond ER glycosylation toward lipid and organelle metabolism.
- **Conclusion**: Established evidence supports HSD17B4 as a peroxisomal metabolic component that may mark cellular metabolic state. Its functional coupling to the ER glycosylation core in this tissue pair is a hypothesis based on co-abundance, not a known complex relationship.

#### MT-CO2

- **Related proteins** (co-abundance neighbors): TUSC3 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome c oxidase subunit II. Contributes to cytochrome-c oxidase activity. Predicted to be involved in mitochondrial electron transport, cytochrome c to oxygen and positive regulation of vasoconstriction. Located in mitochondrial inner membrane. Part of respiratory chain complex IV. Biomarker of Huntington's disease and stomach cancer. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: mitochondrial complex IV deficiency, nuclear-type (0.726); mitochondrial disease (0.707); MELAS syndrome (0.662); leigh syndrome due to mitochondrial complex iv deficiency (0.536); MERRF syndrome (0.516)
- **Europe PMC papers**: 47751
- **Why important**: MT-CO2 is tissue enhanced in heart muscle and is cell-type enhanced in enterocytes, colonocytes and hepatocytes. It encodes a subunit of mitochondrial respiratory-chain complex four and contributes to electron transport, oxygen reduction and coupled ATP synthesis. It has extensive literature coverage and disease associations involving mitochondrial complex deficiencies, MELAS syndrome and related mitochondrial disease. Its co-abundance link to TUSC3 connects the ER-centered core to mitochondrial energy metabolism.
- **Conclusion**: Established evidence supports MT-CO2 as a mitochondrial respiratory component and a plausible marker of energetic state. Its participation in a coordinated ER-mitochondrial module is a hypothesis; the supplied interaction resources do not establish a direct physical relationship with the other module members.

## Module 7

**Tissue pair**: bone and circulatory_system  
**Genes (5)**: MCM2, MCM4, MCM5, MCM6, MCM7

### Function

This is a highly coherent MCM helicase and DNA-replication module. Every module gene is represented in the globally corrected GO/KEGG evidence for the MCM complex, replication-initiation regulation, DNA replication, helicase activity, DNA-repair processes, cell-cycle replication, homologous recombination, and the human DNA-replication pathway (53 globally significant GO/KEGG terms, q_global 3.48e-10–0.0231; see the table). The strongest interpretation is coordinated expression of the MCM2–MCM7 replicative helicase, rather than a generic cell-cycle signal. The enrichment is especially compelling because the genes collectively define the same physical replication machinery and all module genes contribute to the central MCM-complex evidence (GO:CC MCM complex; q_global = 3.48e-10), (GO:CC DNA replication preinitiation complex; q_global = 2.01e-08), (GO:CC CMG complex; q_global = 2.01e-08), (KEGG DNA replication - Homo sapiens (human); q_global = 4.42e-07). The break-induced replication and DNA-damage-response terms (GO:BP double-strand break repair via break-induced replication; q_global = 4.49e-09), (GO:BP double-strand break repair via homologous recombination; q_global = 2.94e-05), (GO:BP DNA repair; q_global = 0.00218), (GO:BP DNA damage response; q_global = 0.00795) support a role in replication-associated genome maintenance, although they do not establish that this module specifically measures DNA damage in the sampled tissues.

**Cell composition.** The module is composed entirely of nuclear MCM components, not plasma or secreted proteins. HPA places the proteins in the nucleoplasm and reports no secreted genes. All module genes are tissue-enhanced or cell-type-enhanced, with recurring enrichment in bone marrow and lymphoid tissue and in erythrocyte, megakaryocyte, and monocyte progenitor populations. HPA assigns low immune-cell specificity and does not identify enriched mature blood-cell populations. Thus, the shared bone–circulatory_system signal is unlikely to be a plasma-protein module. It may instead reflect proliferating or progenitor-like hematopoietic cells, or another shared cell population, in the profiled samples. HPA has no matching tissue-level protein-detection result for either named tissue, so the tissue-level protein evidence is unavailable rather than negative.

**GO/KEGG enrichment**: 53 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC MCM complex | 3.48e-10 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication initiation | 1.61e-09 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP double-strand break repair via break-induced replication | 4.49e-09 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication | 4.49e-09 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC DNA replication preinitiation complex | 2.01e-08 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC CMG complex | 2.01e-08 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP DNA replication initiation | 1.87e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF four-way junction helicase activity | 3.47e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF forked DNA-dependent helicase activity | 3.47e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF double-stranded DNA helicase activity | 4.42e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF 3'-5' DNA helicase activity | 4.42e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded 3'-5' DNA helicase activity | 4.42e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| KEGG DNA replication - Homo sapiens (human) | 4.42e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded DNA helicase activity | 1.13e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA replication | 1.38e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |

### STRING and hu.MAP

STRING reports very strong relationships among every possible pair of module genes, and its supplementary annotations place all genes in the MCM complex, MCM domains, the CMG complex, DNA unwinding, pre-replicative-complex activation, replication-initiation regulation, and replication-stress responses (15 supplementary STRING terms; within-query FDR 5.27e-10–8.84e-09). These STRING relationships are already known molecular associations and strongly support that the co-abundance pattern tracks a real replicative-helicase complex rather than an incidental correlation. hu.MAP independently places the module genes in multiple complexes containing the MCM helicase and, in broader assemblies, MCM3, CDC45, GINS proteins, TIMELESS, TIPIN, CLSPN, and MCMBP (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_08848.1). The repeated recovery of the same module genes across these complexes supports a core-complex interpretation, while the absent partner genes indicate that the module is a partial expression-defined representation of larger replisome assemblies. The module-network topology is compact and internally connected: MCM5 is the most connected module member, MCM6 links MCM4 and MCM5, and MCM2 and MCM7 connect through MCM5 and each other. This topology is consistent with coordinated abundance of a known protein complex, not evidence that the co-abundance edges themselves are novel physical interactions.

**STRING interactions (score >= 0.7)**: 10 of 10 gene pairs: MCM2–MCM4 (0.999); MCM2–MCM5 (0.999); MCM2–MCM6 (0.999); MCM2–MCM7 (0.999); MCM4–MCM5 (0.999); MCM4–MCM6 (0.999); MCM4–MCM7 (0.999); MCM5–MCM6 (0.999); MCM5–MCM7 (0.999); MCM6–MCM7 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component MCM complex (FDR = 5.27e-10, 5 genes); COMPARTMENTS MCM complex (FDR = 5.61e-10, 5 genes); InterPro MCM domain (FDR = 7.69e-10, 5 genes); InterPro Mini-chromosome maintenance, conserved site (FDR = 7.69e-10, 5 genes); InterPro MCM N-terminal domain (FDR = 7.69e-10, 5 genes); InterPro Mini-chromosome maintenance protein (FDR = 7.69e-10, 5 genes); InterPro MCM OB domain (FDR = 7.69e-10, 5 genes); InterPro MCM, AAA-lid domain (FDR = 7.69e-10, 5 genes); Component CMG complex (FDR = 2.09e-09, 5 genes); COMPARTMENTS CMG complex (FDR = 2.23e-09, 5 genes); Process Double-strand break repair via break-induced replication (FDR = 6.05e-09, 5 genes); Process Regulation of DNA-templated DNA replication initiation (FDR = 6.05e-09, 5 genes); RCTM Unwinding of DNA (FDR = 6.19e-09, 5 genes); RCTM Activation of the pre-replicative complex (FDR = 6.76e-09, 5 genes); RCTM Activation of ATR in response to replication stress (FDR = 8.84e-09, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05529.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/6); huMAP3_14758.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/14); huMAP3_08554.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_11832.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_12180.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/17); huMAP3_06061.1 (MCM4, MCM7, MCM2, MCM6; 4/5); huMAP3_07113.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_11119.1 (MCM4, MCM5, MCM7, MCM6; 4/14); huMAP3_09860.1 (MCM4, MCM2, MCM6; 3/4); huMAP3_00154.1 (MCM4, MCM2, MCM6; 3/5); huMAP3_09466.1 (MCM4, MCM2, MCM6; 3/23); huMAP3_10862.1 (MCM4, MCM2, MCM6; 3/33); huMAP3_14306.1 (MCM4, MCM2, MCM6; 3/55); huMAP3_02602.1 (MCM4, MCM6; 2/2); huMAP3_09238.1 (MCM5, MCM7; 2/11); huMAP3_08848.1 (MCM4, MCM6; 2/15)

### Novelty

The molecular function and physical complex are not new findings: MCM2, MCM4, MCM5, MCM6, and MCM7 are established components of the replication machinery, and their relationships are represented in STRING and hu.MAP (15 supplementary STRING terms; within-query FDR 5.27e-10–8.84e-09), (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_08848.1). A potentially new aspect is the identification of this coherent MCM submodule as conserved across the bone and circulatory_system co-abundance profiles. That tissue-pair observation should be described as a context-specific network finding rather than a newly discovered complex or mechanism. The shared signal could be driven by common proliferative progenitor-cell composition, particularly given the HPA enrichment pattern, so novelty would require validation in independent cohorts, cell-composition-adjusted analyses, and comparison with existing tissue co-expression resources. Absence of an exact tissue-pair module from STRING or hu.MAP would not by itself establish novelty.

**Hypothesis.** Hypothesis: the conserved module reflects the abundance of proliferating progenitor or precursor cells shared by bone-associated and circulatory-system samples. In those cells, coordinated expression of the MCM helicase supports licensing and unwinding of replication origins, replication-fork progression, and protection or repair of stressed replication forks. The HPA enrichment in hematopoietic progenitor populations makes a cell-composition or proliferative-state explanation plausible, while the replication and repair annotations provide the molecular mechanism. This hypothesis predicts that module abundance should track proliferation markers and progenitor-cell fractions, and that its apparent tissue conservation should weaken after appropriate adjustment for those factors.

### Important genes

#### MCM5

- **Related proteins** (co-abundance neighbors): MCM6 (0.88), MCM7 (0.88), MCM2 (0.83); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 5. The protein encoded by this gene is structurally very similar to the CDC46 protein from S. cerevisiae, a protein involved in the initiation of DNA replication. The encoded protein is a member of the MCM family of chromatin-binding proteins and can interact with at least two other members of this family. The encoded protein is upregulated in the transition from the G0 to G1/S phase of the cell cycl…
- **Diseases (Open Targets)**: Meier-Gorlin syndrome (0.563); neurodegenerative disease (0.397); lysosomal storage disease (0.362); kidney transplant (0.198); diabetic ketoacidosis (0.129)
- **Europe PMC papers**: 4143
- **Why important**: MCM5 is the most connected member of the module subgraph and connects to MCM2, MCM6, and MCM7. It participates in all of the principal globally corrected MCM, replication, helicase, and repair annotations (50 globally significant GO/KEGG terms, q_global 3.48e-10–0.0183; see the table), is included in the core STRING and hu.MAP complexes (15 supplementary STRING terms; within-query FDR 5.27e-10–8.84e-09), (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1), (hu.MAP huMAP3_11119.1), (hu.MAP huMAP3_09238.1), and has a substantial literature record. MyGene describes it as an MCM-family chromatin-binding protein involved in the transition toward S phase and cell-cycle regulation. HPA links it particularly to bone marrow and several progenitor populations.
- **Conclusion**: Established evidence supports MCM5 as a highly connected core component of the replicative helicase and a strong marker of the module's proliferative program. It is a useful network anchor, but the available evidence does not show that MCM5 uniquely drives the shared tissue signal. The progenitor-cell interpretation remains a hypothesis.

#### MCM2

- **Related proteins** (co-abundance neighbors): MCM5 (0.83), MCM7 (0.82); STRING partners: MCM4 (0.999), MCM5 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a core MCM component with direct STRING relationships to every other module gene and broad representation across the hu.MAP complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1), (hu.MAP huMAP3_06061.1), (hu.MAP huMAP3_07113.1), (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1). It contributes to every major globally corrected functional theme, including replication initiation, helicase activity, DNA repair, and the KEGG DNA-replication pathway (50 globally significant GO/KEGG terms, q_global 3.48e-10–0.0183; see the table) and (GO:BP cell cycle DNA replication initiation; q_global = 0.0231) (GO:BP nuclear cell cycle DNA replication initiation; q_global = 0.0231) (GO:BP mitotic DNA replication initiation; q_global = 0.0231). It has the largest literature volume among the module genes in the supplied evidence and is enhanced in bone marrow and lymphoid tissue as well as several progenitor populations.
- **Conclusion**: Established evidence identifies MCM2 as a central, extensively studied replication-initiation component and a strong representative of the module. Its tissue and cell-type pattern is compatible with a progenitor-associated explanation, but it cannot distinguish that explanation from a general proliferative-state signal.

#### MCM6

- **Related proteins** (co-abundance neighbors): MCM4 (0.90), MCM5 (0.88); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 6. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: lactose intolerance (0.246); neurodegenerative disease (0.225); obesity disorder (0.166); nervous system disorder (0.141); systemic lupus erythematosus (0.140)
- **Europe PMC papers**: 3766
- **Why important**: MCM6 has strong connections to MCM4 and MCM5 in the module and is represented across the broadest set of hu.MAP assemblies listed for the module, including assemblies containing the MCM, CMG, and replisome-associated proteins (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_08848.1). It contributes to all major globally corrected MCM and DNA-replication terms, including mitotic DNA replication (GO:BP mitotic DNA replication; q_global = 0.000859), (GO:BP nuclear DNA replication; q_global = 0.00363), (GO:BP cell cycle DNA replication; q_global = 0.00445). MyGene describes its role in the pre-replication complex, replication-fork formation, and recruitment of replication proteins. HPA associates it with lymphoid tissue and hematopoietic progenitor populations.
- **Conclusion**: Established evidence supports MCM6 as a core structural and functional component of the replication machinery and a bridge to larger replisome assemblies. Its HPA pattern strengthens the progenitor or proliferative-state hypothesis, but does not prove that MCM6 has a tissue-specific function in bone or circulation.

#### MCM7

- **Related proteins** (co-abundance neighbors): MCM5 (0.88), MCM2 (0.82); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM6 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 is a core MCM helicase component, connects directly to MCM2 and MCM5 in the module, and is present in the principal STRING and hu.MAP MCM and CMG assemblies (15 supplementary STRING terms; within-query FDR 5.27e-10–8.84e-09), (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1), (hu.MAP huMAP3_09238.1). It contributes to the globally corrected replication, helicase, DNA-repair, and DNA-damage-response evidence (34 globally significant GO/KEGG terms, q_global 3.48e-10–0.000753; see the table), (15 globally significant GO/KEGG terms, q_global 0.00138–0.0183; see the table). MyGene describes its role in replication initiation, fork elongation, and DNA-damage response. It is enhanced in bone marrow and in erythrocyte and megakaryocyte progenitor populations, and it has a substantial literature record.
- **Conclusion**: Established evidence supports MCM7 as a core replication-fork and genome-maintenance component. Its cell-type pattern is consistent with the module reflecting proliferative progenitors in the sampled tissues. A specific MCM7-mediated mechanism distinguishing bone from circulatory tissue is not established by the supplied data.

#### MCM4

- **Related proteins** (co-abundance neighbors): MCM6 (0.90); STRING partners: MCM2 (0.999), MCM5 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 4. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication rel…
- **Diseases (Open Targets)**: primary immunodeficiency with natural-killer cell deficiency and adrenal insufficiency (0.714); X-linked adrenal hypoplasia congenita (0.185); lung adenocarcinoma (0.112); microcephaly (0.111); neoplasm (0.102)
- **Europe PMC papers**: 4082
- **Why important**: MCM4 is the least connected member of the module subgraph but remains essential to the interpretation because it is directly connected to MCM6 and appears with all module genes in the central MCM-complex and replication-initiation evidence (34 globally significant GO/KEGG terms, q_global 3.48e-10–0.000753; see the table). It is included in nearly all listed hu.MAP MCM and replisome-related assemblies (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_08848.1). MyGene identifies it as a conserved MCM protein involved in replication initiation and fork elongation. HPA associates it with bone marrow and erythrocyte and megakaryocyte progenitors. Its disease associations include natural-killer-cell deficiency with adrenal insufficiency and other developmental or neoplastic conditions in the supplied Open Targets evidence.
- **Conclusion**: Established evidence supports MCM4 as an indispensable core member whose lower module connectivity reflects the observed co-abundance topology, not lack of biological importance. Its progenitor-associated expression and disease links make it relevant for follow-up, but they do not establish a disease mechanism for this tissue-pair module.
