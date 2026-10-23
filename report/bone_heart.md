# Conserved co-abundance modules: bone and heart

## Module 0

**Tissue pair**: bone and heart  
**Genes (34)**: YWHAH, ALDH1B1, ANXA1, ANXA2, ANXA3, ANXA5, CLIC1, EIF3L, EZR, GANAB, SHMT2, GSTP1, HPRT1, HSP90AA1, IMPDH2, PKM, LDHA, PGK1, PSMC4, PSMB3, PSMD13, ADSL, SEPTIN11, SEPTIN2, SEPTIN7, SEPTIN9, SUN2, DARS1, CCT5, CCT3, CCT7, CCT8, USO1, XPO1

### Function

The strongest interpretation is a conserved intracellular proteostasis and cell-organization module. Primary evidence comes from the globally corrected globally significant GO/KEGG terms: the CCT subunits CCT3, CCT5, CCT7, and CCT8, together with HSP90AA1, are associated with DNA biosynthetic regulation and telomere maintenance (13 globally significant GO/KEGG terms, q_global 0.00482–0.0192; see the table), (GO:BP telomere maintenance; q_global = 0.0488) (GO:BP regulation of chromosome organization; q_global = 0.0488) (GO:BP positive regulation of chromosome organization; q_global = 0.0488). The same CCT subunits form the chaperonin-containing T-complex (GO:CC chaperonin-containing T-complex; q_global = 0.0415) and are linked to nuclear and Cajal-body protein localization, including telomerase RNA localization (7 globally significant GO/KEGG terms, q_global 0.0415–0.0415; see the table). A second established component is the septin cytoskeleton, represented by SEPTIN2, SEPTIN7, SEPTIN9, and SEPTIN11 (GO:CC septin ring; q_global = 0.0415) (GO:CC septin complex; q_global = 0.0415) (GO:CC septin cytoskeleton; q_global = 0.0415). Thus, the module is not best described as a single specialized pathway: it combines protein folding and quality control, nuclear or telomere-associated organization, cytoskeletal structure, proteasomal turnover, energy metabolism, and membrane-associated processes. The telomere interpretation is supported by enrichment, but it should not be taken to mean that every module gene directly regulates telomeres.

**Cell composition.** The module is predominantly intracellular rather than a plasma-protein or secreted-protein module. The HPA summary reports low tissue specificity for most genes, low immune-cell specificity for most genes, and only a small secreted subset. This argues against interpreting the shared bone-heart signal primarily as blood-cell contamination, although ANXA1 and ANXA2 are secreted to blood and several genes show associations with megakaryocytes, platelets, monocytes, or other specialized cell types. The HPA tissue pattern is heterogeneous, with enrichment represented in skeletal muscle, esophagus, blood vessel, liver, and other tissues, while many genes are broadly expressed. Heart protein detection is present for a substantial portion of the measured genes, including CCT3, CCT7, CCT8, ADSL, PSMC4, PKM, GSTP1, YWHAH, PSMD13, PSMB3, IMPDH2, CLIC1, PGK1, ALDH1B1, SUN2, and XPO1. This supports genuine cellular machinery shared by bone and heart, but the broad expression profile means that the module may reflect common cell-state or housekeeping programs rather than a bone-heart-specific mechanism.

**GO/KEGG enrichment**: 27 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA-templated DNA biosynthetic process | 0.00482 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP telomere maintenance via telomerase | 0.00482 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP telomere maintenance via telomere lengthening | 0.00482 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP regulation of telomere maintenance via telomerase | 0.00482 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP positive regulation of telomere maintenance via telomerase | 0.00482 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP regulation of telomere maintenance via telomere lengthening | 0.00482 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP positive regulation of telomere maintenance via telomere lengthening | 0.00482 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP regulation of DNA biosynthetic process | 0.00482 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP positive regulation of DNA biosynthetic process | 0.00482 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP sexual reproduction | 0.00826 | CCT3, CCT5, CCT7, CCT8, PSMD13, SEPTIN2, SEPTIN7, SUN2 |
| GO:BP regulation of telomere maintenance | 0.0192 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP positive regulation of telomere maintenance | 0.0192 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP DNA biosynthetic process | 0.0192 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:CC chaperonin-containing T-complex | 0.0415 | CCT3, CCT5, CCT7, CCT8 |
| GO:CC septin ring | 0.0415 | SEPTIN11, SEPTIN2, SEPTIN7, SEPTIN9 |

### STRING and hu.MAP

STRING provides strong internal support for several physically or functionally coherent substructures. CCT3, CCT5, CCT7, and CCT8 are tightly connected, and each is connected to HSP90AA1, establishing a chaperone-centered core. SEPTIN2, SEPTIN7, SEPTIN9, and SEPTIN11 form a strongly connected septin group. PSMB3, PSMC4, and PSMD13 form a proteasome-associated group, while LDHA, PGK1, and PKM form a glycolytic group; ADSL, HPRT1, and IMPDH2 support a purine-metabolism connection. Additional links connect the chaperone, membrane, annexin, cytoskeletal, metabolic, and proteasomal portions, so the co-abundance graph is more integrated than a collection of unrelated annotations. hu.MAP independently recovers the septin complex (hu.MAP huMAP3_02362.1), multiple CCT-containing complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), proteasome assemblies containing PSMB3, PSMC4, and PSMD13 (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) (hu.MAP huMAP3_05064.1), and a complex containing PKM and ADSL (hu.MAP huMAP3_14442.1). These findings show that much of the network reflects known molecular complexes. The STRING tissue enrichments (15 supplementary STRING terms; within-query FDR 0.0037–0.0168) are supplementary and point toward broadly expressed, hematopoietic, epithelial, metabolic, and proliferative cellular programs; they are not global enrichment evidence.

**STRING interactions (score >= 0.7)**: 35 of 561 gene pairs: ADSL–HPRT1 (0.935); ADSL–IMPDH2 (0.879); ADSL–SHMT2 (0.909); ANXA1–ANXA2 (0.989); ANXA2–ANXA5 (0.833); ANXA2–CLIC1 (0.713); ANXA2–EZR (0.725); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT3–HSP90AA1 (0.767); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT5–HSP90AA1 (0.868); CCT7–CCT8 (0.999); CCT7–HSP90AA1 (0.849); CCT7–IMPDH2 (0.758); CCT8–HSP90AA1 (0.823); CLIC1–EZR (0.715); EZR–HSP90AA1 (0.954); HPRT1–IMPDH2 (0.967); HPRT1–PGK1 (0.83); HSP90AA1–PGK1 (0.713); LDHA–PGK1 (0.923); LDHA–PKM (0.997); PGK1–PKM (0.936); PSMB3–PSMC4 (0.999); PSMB3–PSMD13 (0.999); PSMC4–PSMD13 (0.999); SEPTIN11–SEPTIN2 (0.999); SEPTIN11–SEPTIN7 (0.999); SEPTIN11–SEPTIN9 (0.996); SEPTIN2–SEPTIN7 (0.999); SEPTIN2–SEPTIN9 (0.997); SEPTIN7–SEPTIN9 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Lymphoblast (FDR = 0.0037, 13 genes); TISSUES Alimentary canal (FDR = 0.0084, 23 genes); TISSUES Ascites (FDR = 0.0084, 7 genes); TISSUES Respiratory system (FDR = 0.0084, 22 genes); TISSUES Blood cancer cell (FDR = 0.0084, 17 genes); TISSUES Bone marrow cancer cell (FDR = 0.0084, 9 genes); TISSUES Leukemia cell (FDR = 0.0084, 16 genes); TISSUES Internal male genital organ (FDR = 0.0084, 20 genes); TISSUES Embryonic structure (FDR = 0.0094, 23 genes); TISSUES Hematopoietic system (FDR = 0.0094, 24 genes); TISSUES Liver (FDR = 0.0094, 30 genes); TISSUES Lung (FDR = 0.0094, 19 genes); TISSUES Female reproductive gland (FDR = 0.0104, 22 genes); TISSUES Lymphoid tissue (FDR = 0.0118, 16 genes); TISSUES Skin (FDR = 0.0168, 16 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02362.1 (SEPTIN2, SEPTIN7, SEPTIN11, SEPTIN9; 4/14); huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_09656.1 (PSMC4, PSMB3, PSMD13; 3/64); huMAP3_13725.1 (PSMC4, PSMB3, PSMD13; 3/69); huMAP3_05064.1 (PSMC4, PSMD13; 2/31); huMAP3_14442.1 (PKM, ADSL; 2/57)

### Novelty

The individual molecular relationships are not a new discovery: the CCT chaperonin, HSP90AA1, septin assemblies, proteasome components, glycolytic enzymes, annexins, and purine enzymes are already supported by STRING or hu.MAP. The potentially novel result is the reproducible co-abundance organization of these established systems in a module conserved across bone and heart. However, the fact sheet does not establish novelty against all published co-expression, proteomic, tissue-specific, or disease modules. Absence of hu.MAP or STRING support for some individual edges would not prove novelty, because those resources catalog physical or functional evidence rather than this particular cross-tissue co-abundance pattern. The appropriate conclusion is that the module is a potentially novel cross-tissue systems-level association built from largely established molecular machinery, requiring independent cohorts and comparison with existing bone, heart, proteostasis, cytoskeletal, and cell-composition modules before claiming a new biological mechanism.

**Hypothesis.** Hypothesis: the shared bone-heart module reflects a coordinated cellular maintenance state in which CCT and HSP90AA1 preserve folding and assembly of cytoskeletal and nuclear proteins, septins organize membrane and cytoskeletal architecture, and proteasomal and metabolic components remove damaged proteins while supplying energy and nucleotide precursors. In this state, chaperone activity could support nuclear-body and telomerase-related organization, consistent with (13 globally significant GO/KEGG terms, q_global 0.00482–0.0192; see the table) and (10 globally significant GO/KEGG terms, q_global 0.0415–0.0488; see the table), while septin, annexin, ezrin, and SUN2 components could couple cytoskeletal structure to membrane and nuclear organization. The hypothesis is that bone and heart share this stress-sensitive proteostasis and structural-maintenance program because both require durable architecture and continuous protein-quality control. This is a mechanistic model, not proof of direct regulation by the module; it should be tested by cell-type-resolved measurements, perturbation of the CCT or septin systems, and assessment of proteostasis, cytoskeletal integrity, and telomere-associated readouts.

### Important genes

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT3 (0.97), HSP90AA1 (0.93), CCT7 (0.92), DARS1 (0.90), IMPDH2 (0.90), EIF3L (0.88), EZR (0.86), GANAB (0.85), ADSL (0.85), ANXA5 (0.85), ANXA2 (0.84), PSMC4 (0.84), PGK1 (0.84), SEPTIN7 (0.84), SEPTIN2 (0.84), PSMD13 (0.83), CCT5 (0.83); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999), HSP90AA1 (0.823)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is the leading network connector in the module and links the CCT core to HSP90AA1, DARS1, IMPDH2, EIF3L, EZR, and GANAB. It participates in every primary CCT-associated enrichment group, including telomere maintenance, Cajal-body localization, DNA biosynthetic regulation, and the chaperonin-containing T-complex (9 globally significant GO/KEGG terms, q_global 0.00482–0.00482; see the table), (4 globally significant GO/KEGG terms, q_global 0.0192–0.0415; see the table), (10 globally significant GO/KEGG terms, q_global 0.0415–0.0488; see the table). Its membership in several hu.MAP CCT-containing complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1), heart detection by HPA, and substantial literature support make it a strong representative of the module core.
- **Conclusion**: Established: CCT8 is a core CCT chaperonin subunit and a central connector in this module, with direct support from STRING, hu.MAP, HPA, and primary enrichment. Hypothesis: CCT8 may help couple protein folding to the nuclear and telomere-associated features of the shared bone-heart state.

#### HSP90AA1

- **Related proteins** (co-abundance neighbors): CCT8 (0.93), CCT3 (0.91), PGK1 (0.88), ANXA5 (0.88), ANXA2 (0.88), GANAB (0.88), CCT5 (0.87), SEPTIN9 (0.86), EIF3L (0.85), CCT7 (0.85), PSMD13 (0.84), GSTP1 (0.83), CLIC1 (0.82), DARS1 (0.82), ADSL (0.81); STRING partners: CCT3 (0.767), CCT5 (0.868), CCT7 (0.849), CCT8 (0.823), EZR (0.954), PGK1 (0.713)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein 90 alpha family class A member 1. The protein encoded by this gene is an inducible molecular chaperone that functions as a homodimer. The encoded protein aids in the proper folding of specific target proteins by use of an ATPase activity that is modulated by co-chaperones. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: cancer (0.643); plasma cell myeloma (0.404); non-small cell lung carcinoma (0.394); dengue disease (0.375); Orthomyxoviridae infectious disease (0.375)
- **Europe PMC papers**: 8215
- **Why important**: HSP90AA1 is a highly connected chaperone hub linking the CCT group to glycolytic, annexin, membrane, and ezrin-associated components. It contributes to all primary telomere and DNA-biosynthetic enrichment groups that contain the chaperone core (13 globally significant GO/KEGG terms, q_global 0.00482–0.0192; see the table), (GO:BP telomere maintenance; q_global = 0.0488) (GO:BP regulation of chromosome organization; q_global = 0.0488) (GO:BP positive regulation of chromosome organization; q_global = 0.0488). Its STRING links to CCT proteins, EZR, and PGK1 support integration between proteostasis and structural or metabolic processes. It has extensive disease and literature representation, making it an important biological and translational anchor.
- **Conclusion**: Established: HSP90AA1 is a molecular chaperone and a major network bridge, with support from primary enrichment and STRING. Hypothesis: HSP90AA1 may buffer stress-related protein-folding demands in both tissues and thereby help maintain the broader module state.

#### SEPTIN7

- **Related proteins** (co-abundance neighbors): PSMC4 (0.93), EIF3L (0.87), SEPTIN9 (0.87), GANAB (0.86), SEPTIN2 (0.84), CCT8 (0.84), SUN2 (0.82), CCT7 (0.80); STRING partners: SEPTIN11 (0.999), SEPTIN2 (0.999), SEPTIN9 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02362.1
- **Function (MyGene.info)**: septin 7. This gene encodes a protein that is highly similar to the CDC10 protein of Saccharomyces cerevisiae. The protein also shares similarity with Diff 6 of Drosophila and with H5 of mouse. Each of these similar proteins, including the yeast CDC10, contains a GTP-binding motif. The yeast CDC10 protein is a structural component of the 10 nm filament which lies inside the cytoplasmic membrane and is essen…
- **Diseases (Open Targets)**: glaucoma (0.366); bone fracture (0.264); fracture of pelvis (0.264); open-angle glaucoma (0.262); male reproductive system disorder (0.260)
- **Europe PMC papers**: 304
- **Why important**: SEPTIN7 is part of the fully represented septin group and is connected to SEPTIN2, SEPTIN9, SEPTIN11, SUN2, PSMC4, EIF3L, and the CCT system. The septin complex and septin cytoskeleton are primary globally corrected annotations (GO:CC septin ring; q_global = 0.0415) (GO:CC septin complex; q_global = 0.0415) (GO:CC septin cytoskeleton; q_global = 0.0415), and the septin group is recovered as hu.MAP complex (hu.MAP huMAP3_02362.1) and by strong STRING relationships. Its annotations connect cytoskeletal organization, cytokinesis, cilium assembly, and cell shape to the otherwise chaperone-centered module. Its disease associations include bone fracture and glaucoma, providing tissue-relevant context, although these associations do not establish a causal role here.
- **Conclusion**: Established: SEPTIN7 is a structural component of a known septin complex and defines a genuine cytoskeletal arm of the module. Hypothesis: SEPTIN7 may transmit the shared proteostasis state into membrane, cytoskeletal, or nuclear organization in bone and heart cells.

#### ADSL

- **Related proteins** (co-abundance neighbors): LDHA (0.91), CCT7 (0.88), PKM (0.88), PSMD13 (0.88), PSMC4 (0.86), CCT8 (0.85), YWHAH (0.84), HPRT1 (0.84), GSTP1 (0.83), CCT5 (0.83), ANXA5 (0.83), HSP90AA1 (0.81); STRING partners: HPRT1 (0.935), IMPDH2 (0.879), SHMT2 (0.909)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: adenylosuccinate lyase. The protein encoded by this gene belongs to the lyase 1 family. It is an essential enzyme involved in purine metabolism, and catalyzes two non-sequential reactions in the de novo purine biosynthetic pathway: the conversion of succinylaminoimidazole carboxamide ribotide (SAICAR) to aminoimidazole carboxamide ribotide (AICAR) and the conversion of adenylosuccinate (S-AMP) to adenosine monophosphate …
- **Diseases (Open Targets)**: adenylosuccinate lyase deficiency (0.852); neurodegenerative disease (0.528); hereditary disease (0.486); Intellectual disability (0.464); Epileptic encephalopathy (0.462)
- **Europe PMC papers**: 1131
- **Why important**: ADSL is a relatively central connector between glycolytic genes, purine-metabolism genes, CCT proteins, proteasome components, and YWHAH. Its enzyme function in de novo purine biosynthesis is supported by the supplied annotation, and its links to HPRT1 and IMPDH2 are strong STRING relationships. ADSL and PKM are represented together in a hu.MAP complex (hu.MAP huMAP3_14442.1), while ADSL is tissue-group enriched in skeletal muscle and tongue and detected in heart by HPA. Its disease association with adenylosuccinase deficiency gives it clear biological importance even though it is not among the genes driving the primary GO enrichment.
- **Conclusion**: Established: ADSL provides a metabolic and nucleotide-supply component that is connected to the structural and proteostasis portions of the module. Hypothesis: purine availability may help coordinate energy-intensive protein quality control and structural maintenance in the shared bone-heart cell state.

#### ANXA2

- **Related proteins** (co-abundance neighbors): CCT5 (0.88), HSP90AA1 (0.88), CCT8 (0.84), ANXA5 (0.83), CCT7 (0.82), CCT3 (0.82), GSTP1 (0.81); STRING partners: ANXA1 (0.989), ANXA5 (0.833), CLIC1 (0.713), EZR (0.725)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A2. This gene encodes a member of the annexin family. Members of this calcium-dependent phospholipid-binding protein family play a role in the regulation of cellular growth and in signal transduction pathways. This protein functions as an autocrine factor which heightens osteoclast formation and bone resorption. This gene has three pseudogenes located on chromosomes 4, 9 and 10, respectively. Multiple…
- **Diseases (Open Targets)**: neurodegenerative disease (0.443); Alzheimer disease (0.312); Parkinson disease (0.298); lysosomal storage disease (0.289); benign urinary system neoplasm (0.270)
- **Europe PMC papers**: 12966
- **Why important**: ANXA2 is a membrane-associated, secreted-to-blood annexin that connects ANXA1, ANXA5, CLIC1, EZR, HSP90AA1, and the CCT group in STRING. Its HPA profile shows tissue enhancement in esophagus and group enrichment across several blood-cell types, so it is important both as a possible structural signaling component and as a marker requiring composition-aware interpretation. The supplied functional annotation links ANXA2 to angiogenesis, membrane-raft assembly, receptor recycling, vesicle budding, and cell adhesion, while the literature volume is extensive. Its role in heightening osteoclast formation and bone resorption makes it especially relevant to the bone side of the tissue pair, but no direct heart-specific mechanism is established here.
- **Conclusion**: Established: ANXA2 is a membrane and vesicle-associated connector with known annexin interactions and a plausible bone-relevant function. Caution: its secreted-to-blood and blood-cell-associated profile means part of its module signal could reflect extracellular or cellular composition. Hypothesis: ANXA2 may link cell-surface remodeling and vesicle trafficking to the intracellular chaperone and cytoskeletal program.

## Module 1

**Tissue pair**: bone and heart  
**Genes (26)**: GOT2, ACADVL, ACO2, SLC25A4, AIFM1, ALDH2, ATP5PB, ATP5F1A, ATP5F1C, CS, COQ9, DHRS4, ETFA, HSDL2, AK4, L2HGDH, NDUFA10, NDUFV1, DLAT, PDHB, SDHA, SPRYD4, SUCLG1, SUCLG2, ACAT1, ACAA2

### Function

This is a mitochondrial oxidative-energy and central-carbon-metabolism module. The primary evidence is exceptionally coherent: every module gene is included in the mitochondrion cellular-component term (GO:CC mitochondrion; q_global = 1.12e-05), while many genes support precursor-metabolite and energy generation (GO:BP generation of precursor metabolites and energy; q_global = 4.46e-05), the mitochondrial matrix (GO:CC mitochondrial matrix; q_global = 0.000103), small-molecule metabolism (GO:BP small molecule metabolic process; q_global = 0.0003), oxidation of organic compounds (GO:BP energy derivation by oxidation of organic compounds; q_global = 0.000827), cellular and aerobic respiration (GO:BP cellular respiration; q_global = 0.0011) (GO:BP aerobic respiration; q_global = 0.00193), broad metabolic pathways (KEGG Metabolic pathways - Homo sapiens (human); q_global = 0.00368), the citrate cycle (KEGG Citrate cycle (TCA cycle) - Homo sapiens (human); q_global = 0.00582), the tricarboxylic acid cycle (GO:BP tricarboxylic acid cycle; q_global = 0.021), and carbon metabolism (KEGG Carbon metabolism - Homo sapiens (human); q_global = 0.0369). The gene content spans fatty-acid oxidation, pyruvate entry into acetyl-CoA, the TCA cycle, respiratory complexes, ATP synthase, adenine-nucleotide exchange, and related mitochondrial redox reactions. Thus, the most defensible interpretation is coordinated mitochondrial fuel oxidation and oxidative phosphorylation capacity rather than a narrowly specialized signaling pathway. The globally significant GO/KEGG terms are the globally corrected evidence; the STRING terms are concordant supplementary evidence.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and the genes are predominantly intracellular mitochondrial proteins or enzymes. It is also not strongly blood-cell enriched, because most genes have low immune-cell specificity, with only a small minority showing immune or blood-cell enrichment. The HPA pattern instead points to metabolically active tissues and cell types, especially tongue, liver, skeletal muscle, heart muscle, hepatocytes, and muscle-lineage cells. Heart protein detection is widespread among the module genes, whereas bone has no matching HPA tissue protein assessment. The shared bone-heart signal could therefore reflect a conserved mitochondrial energy program in resident metabolically active cells, particularly muscle-like or other energetically demanding cells, rather than blood contamination. At the same time, the frequent liver, digestive, and tongue associations indicate that the module is not uniquely bone- or heart-specific and may partly represent a broadly reused tissue-metabolic program.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrion | 1.12e-05 | ACAA2, ACADVL, ACAT1, ACO2, AIFM1, AK4, ALDH2, ATP5F1A, ATP5F1C, ATP5PB, COQ9, CS, DHRS4, DLAT, ETFA, GOT2, HSDL2, L2HGDH, NDUFA10, NDUFV1, PDHB, SDHA, SLC25A4, SPRYD4, SUCLG1, SUCLG2 |
| GO:BP generation of precursor metabolites and energy | 4.46e-05 | ACADVL, ACAT1, ACO2, AK4, ATP5F1A, ATP5F1C, ATP5PB, COQ9, CS, DLAT, ETFA, NDUFA10, NDUFV1, PDHB, SDHA, SLC25A4, SUCLG1, SUCLG2 |
| GO:CC mitochondrial matrix | 0.000103 | ACAA2, ACADVL, ACAT1, ACO2, AK4, ALDH2, ATP5F1A, ATP5F1C, ATP5PB, CS, DLAT, ETFA, GOT2, NDUFA10, PDHB, SDHA, SUCLG1, SUCLG2 |
| GO:BP small molecule metabolic process | 0.0003 | ACAA2, ACADVL, ACAT1, ACO2, AK4, ALDH2, ATP5F1A, ATP5F1C, ATP5PB, COQ9, CS, DHRS4, DLAT, ETFA, GOT2, L2HGDH, NDUFA10, NDUFV1, PDHB, SDHA, SUCLG1, SUCLG2 |
| GO:BP energy derivation by oxidation of organic compounds | 0.000827 | ACADVL, ACO2, AK4, ATP5F1A, ATP5F1C, ATP5PB, COQ9, CS, DLAT, ETFA, NDUFA10, NDUFV1, PDHB, SDHA, SUCLG1, SUCLG2 |
| GO:BP cellular respiration | 0.0011 | ACO2, AK4, ATP5F1A, ATP5F1C, ATP5PB, COQ9, CS, DLAT, ETFA, NDUFA10, NDUFV1, PDHB, SDHA, SUCLG1, SUCLG2 |
| GO:BP aerobic respiration | 0.00193 | ACO2, AK4, ATP5F1A, ATP5F1C, ATP5PB, COQ9, CS, DLAT, NDUFA10, NDUFV1, PDHB, SDHA, SUCLG1, SUCLG2 |
| KEGG Metabolic pathways - Homo sapiens (human) | 0.00368 | ACAA2, ACADVL, ACAT1, ACO2, AK4, ALDH2, ATP5F1A, ATP5F1C, ATP5PB, CS, DHRS4, DLAT, GOT2, L2HGDH, NDUFA10, NDUFV1, PDHB, SDHA, SUCLG1, SUCLG2 |
| KEGG Citrate cycle (TCA cycle) - Homo sapiens (human) | 0.00582 | ACO2, CS, DLAT, PDHB, SDHA, SUCLG1, SUCLG2 |
| GO:BP tricarboxylic acid cycle | 0.021 | ACO2, CS, DLAT, PDHB, SDHA, SUCLG1, SUCLG2 |
| KEGG Carbon metabolism - Homo sapiens (human) | 0.0369 | ACAT1, ACO2, CS, DLAT, GOT2, PDHB, SDHA, SUCLG1, SUCLG2 |

### STRING and hu.MAP

STRING provides strong prior support for a connected mitochondrial metabolic network. Known relationships link citrate synthase with aconitase, pyruvate-dehydrogenase components, succinate dehydrogenase, aminotransferase, and succinate-CoA ligase; connect fatty-acid oxidation enzymes with electron-transfer flavoprotein; and connect respiratory-chain proteins with ATP-synthase components. The STRING functional categories independently support mitochondrial localization, matrix membership, respiration, TCA-cycle activity, and oxidation of organic compounds (15 supplementary STRING terms; within-query FDR 4.03e-07–0.0026), but these are supplementary and are not global multiple-testing evidence. hu.MAP provides more specific complex-level support: ATP5F1A, ATP5F1C, and ATP5PB recur together in ATP-synthase complexes (hu.MAP huMAP3_09307.1) (hu.MAP huMAP3_11095.1) (hu.MAP huMAP3_08716.1) (hu.MAP huMAP3_07476.1) (hu.MAP huMAP3_05994.1) (hu.MAP huMAP3_08393.1) (hu.MAP huMAP3_09775.1); DLAT and PDHB recur in pyruvate-dehydrogenase-related complexes (hu.MAP huMAP3_04919.1) (hu.MAP huMAP3_08216.1) (hu.MAP huMAP3_07514.1) (hu.MAP huMAP3_09761.1) (hu.MAP huMAP3_10899.1) (hu.MAP huMAP3_10412.1) (hu.MAP huMAP3_14339.1) (hu.MAP huMAP3_11877.1) (hu.MAP huMAP3_14864.1) (hu.MAP huMAP3_12248.1); ACADVL and DHRS4 recur in several smaller complexes (hu.MAP huMAP3_08580.1) (hu.MAP huMAP3_02431.1) (hu.MAP huMAP3_11915.1) (hu.MAP huMAP3_10506.1); and NDUFA10 with NDUFV1 recur in complex-I-related assemblies (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1). These observations indicate that the co-abundance module is substantially grounded in known mitochondrial pathways and partial physical complexes, rather than being an entirely unexplained association. The module is broader than any single complex and appears to combine multiple interacting energy systems.

**STRING interactions (score >= 0.7)**: 81 of 325 gene pairs: ACAA2–ACADVL (0.983); ACAA2–ACAT1 (0.963); ACAA2–ACO2 (0.75); ACAA2–CS (0.946); ACAA2–DLAT (0.892); ACAA2–ETFA (0.858); ACAA2–HSDL2 (0.918); ACAA2–SDHA (0.753); ACAA2–SUCLG1 (0.912); ACAA2–SUCLG2 (0.88); ACADVL–ETFA (0.877); ACADVL–HSDL2 (0.787); ACAT1–CS (0.977); ACAT1–DLAT (0.949); ACAT1–ETFA (0.821); ACAT1–HSDL2 (0.909); ACAT1–SDHA (0.762); ACAT1–SUCLG1 (0.907); ACAT1–SUCLG2 (0.867); ACO2–ALDH2 (0.751); ACO2–ATP5F1A (0.884); ACO2–CS (0.999); ACO2–DLAT (0.727); ACO2–GOT2 (0.753); ACO2–NDUFA10 (0.747); ACO2–NDUFV1 (0.944); ACO2–SDHA (0.975); ACO2–SLC25A4 (0.706); ACO2–SUCLG1 (0.929); ACO2–SUCLG2 (0.735); AK4–ATP5F1C (0.722); ATP5F1A–ATP5F1C (0.999); ATP5F1A–ATP5PB (0.999); ATP5F1A–CS (0.94); ATP5F1A–DLAT (0.8); ATP5F1A–ETFA (0.786); ATP5F1A–NDUFA10 (0.759); ATP5F1A–NDUFV1 (0.958); ATP5F1A–PDHB (0.81); ATP5F1A–SDHA (0.972); ATP5F1A–SLC25A4 (0.868); ATP5F1A–SUCLG1 (0.853); ATP5F1C–ATP5PB (0.999); ATP5F1C–CS (0.726); ATP5F1C–ETFA (0.715); ATP5F1C–NDUFA10 (0.919); ATP5F1C–NDUFV1 (0.949); ATP5F1C–PDHB (0.913); ATP5F1C–SDHA (0.75); ATP5F1C–SUCLG1 (0.934); ATP5F1C–SUCLG2 (0.728); ATP5PB–NDUFV1 (0.731); ATP5PB–SDHA (0.755); CS–DLAT (0.996); CS–GOT2 (0.952); CS–L2HGDH (0.931); CS–NDUFV1 (0.724); CS–PDHB (0.941); CS–SDHA (0.984); CS–SLC25A4 (0.852); CS–SUCLG1 (0.929); CS–SUCLG2 (0.948); DLAT–PDHB (0.999); DLAT–SDHA (0.852); DLAT–SUCLG1 (0.99); DLAT–SUCLG2 (0.967); ETFA–PDHB (0.728); ETFA–SDHA (0.706); ETFA–SUCLG1 (0.956); GOT2–SDHA (0.981); NDUFA10–NDUFV1 (0.999); NDUFA10–SDHA (0.793); NDUFA10–SUCLG1 (0.836); NDUFV1–PDHB (0.738); NDUFV1–SDHA (0.999); NDUFV1–SUCLG1 (0.836); PDHB–SDHA (0.731); PDHB–SUCLG1 (0.821); SDHA–SUCLG1 (0.999); SDHA–SUCLG2 (0.997); SUCLG1–SUCLG2 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transit peptide (FDR = 4.03e-07, 21 genes); COMPARTMENTS Mitochondrion (FDR = 4.43e-07, 25 genes); Keyword Mitochondrion (FDR = 2.77e-06, 23 genes); Component Mitochondrion (FDR = 3.15e-06, 25 genes); Process Generation of precursor metabolites and energy (FDR = 7.12e-05, 18 genes); Component Mitochondrial matrix (FDR = 0.00015, 17 genes); Process Small molecule metabolic process (FDR = 0.00017, 22 genes); RCTM The citric acid (TCA) cycle and respiratory electron transport (FDR = 0.00024, 14 genes); Process Energy derivation by oxidation of organic compounds (FDR = 0.00026, 15 genes); Process Cellular respiration (FDR = 0.00026, 14 genes); Process Aerobic respiration (FDR = 0.00031, 13 genes); KEGG Metabolic pathways (FDR = 0.00044, 20 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.0023, 15 genes); Keyword Tricarboxylic acid cycle (FDR = 0.0025, 7 genes); KEGG Citrate cycle (TCA cycle) (FDR = 0.0026, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09307.1 (ATP5PB, ATP5F1A, ATP5F1C; 3/35); huMAP3_11095.1 (ATP5PB, ATP5F1A, ATP5F1C; 3/45); huMAP3_08580.1 (ACADVL, DHRS4; 2/2); huMAP3_02431.1 (ACADVL, DHRS4; 2/3); huMAP3_11915.1 (ACADVL, DHRS4; 2/3); huMAP3_10506.1 (ACADVL, DHRS4; 2/4); huMAP3_04919.1 (DLAT, PDHB; 2/7); huMAP3_08216.1 (DLAT, PDHB; 2/8); huMAP3_07514.1 (DLAT, PDHB; 2/9); huMAP3_09761.1 (DLAT, PDHB; 2/10); huMAP3_10899.1 (DLAT, PDHB; 2/10); huMAP3_10412.1 (DLAT, PDHB; 2/12); huMAP3_14339.1 (DLAT, PDHB; 2/13); huMAP3_11877.1 (DLAT, PDHB; 2/14); huMAP3_14864.1 (DLAT, PDHB; 2/14); huMAP3_08716.1 (ATP5PB, ATP5F1C; 2/15); huMAP3_07476.1 (ATP5PB, ATP5F1C; 2/18); huMAP3_05994.1 (ATP5PB, ATP5F1C; 2/19); huMAP3_08393.1 (ATP5PB, ATP5F1C; 2/19); huMAP3_09775.1 (ATP5PB, ATP5F1C; 2/21); huMAP3_12248.1 (DLAT, PDHB; 2/22); huMAP3_02819.1 (NDUFA10, NDUFV1; 2/34); huMAP3_14018.1 (NDUFA10, NDUFV1; 2/48); huMAP3_06397.1 (NDUFA10, NDUFV1; 2/49); huMAP3_09982.1 (NDUFA10, NDUFV1; 2/49); huMAP3_09567.1 (NDUFA10, NDUFV1; 2/52); huMAP3_14878.1 (NDUFA10, NDUFV1; 2/53)

### Novelty

The module should not be called a wholly new mitochondrial pathway. Its principal function, localization, and several relationships are already well established by the globally corrected GO/KEGG results, STRING links, and hu.MAP complexes. Nevertheless, the conserved co-abundance organization across bone and heart may still be a novel systems-level observation, because the supplied evidence does not establish that this exact tissue-pair module, its exact membership, or its cross-tissue coordination has previously been reported. Absence of a complete module match in STRING or hu.MAP would not by itself prove novelty, since those resources represent curated or experimentally supported interactions rather than tissue-pair co-abundance modules. The appropriate conclusion is therefore conditional novelty: potentially new as a bone-heart co-abundance configuration, but not new as a mitochondrial energy program.

**Hypothesis.** Hypothesis: the module represents a shared energetic adaptation in bone and heart cells that coordinates substrate entry, TCA-cycle flux, electron transfer, proton-gradient use, and ATP production. In this model, pyruvate dehydrogenase and fatty-acid oxidation supply acetyl-CoA and reducing equivalents; the TCA cycle and succinate dehydrogenase process these substrates; complex-I-related proteins and associated electron-transfer machinery support respiratory electron flow; ATP synthase and adenine-nucleotide transport couple the gradient to cytosolic ATP availability. The co-abundance of these components could help maintain energy-demanding cellular functions in both tissues. This remains a hypothesis because co-abundance and database relationships do not demonstrate physical co-assembly, flux, causality, or cell-type identity in the sampled tissues.

### Important genes

#### ACO2

- **Related proteins** (co-abundance neighbors): GOT2 (0.95), ATP5F1A (0.89), SLC25A4 (0.86), CS (0.86), SUCLG1 (0.85), ACAT1 (0.82), ETFA (0.82); STRING partners: ACAA2 (0.75), ALDH2 (0.751), ATP5F1A (0.884), CS (0.999), DLAT (0.727), GOT2 (0.753), NDUFA10 (0.747), NDUFV1 (0.944), SDHA (0.975), SLC25A4 (0.706), SUCLG1 (0.929), SUCLG2 (0.735)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aconitase 2. The protein encoded by this gene belongs to the aconitase/IPM isomerase family. It is an enzyme that catalyzes the interconversion of citrate to isocitrate via cis-aconitate in the second step of the TCA cycle. This protein is encoded in the nucleus and functions in the mitochondrion. It was found to be one of the mitochondrial matrix proteins that are preferentially degraded by the serine proteas…
- **Diseases (Open Targets)**: infantile cerebellar-retinal degeneration (0.814); optic atrophy 9 (0.693); autosomal dominant optic atrophy, classic form (0.619); optic atrophy (0.601); mitochondrial disease (0.505)
- **Europe PMC papers**: 3559
- **Why important**: ACO2 is among the most central module genes by weighted network position and connects GOT2, ATP5F1A, SLC25A4, CS, SUCLG1, ACAT1, and ETFA. It appears in every primary GO/KEGG term (11 globally significant GO/KEGG terms, q_global 1.12e-05–0.0369; see the table), is a mitochondrial TCA-cycle enzyme, has heart-muscle and skeletal-muscle tissue enhancement with heart protein detection, and has substantial disease and literature support involving mitochondrial and optic-atrophy disorders.
- **Conclusion**: Established evidence supports ACO2 as a core TCA-cycle and mitochondrial-energy component of this module. Its network centrality and broad primary-term coverage make it a strong anchor gene. It is not established that ACO2 organizes the module or drives the bone-heart conservation; that causal role is a hypothesis.

#### CS

- **Related proteins** (co-abundance neighbors): GOT2 (0.88), ETFA (0.86), ACO2 (0.86), ATP5F1A (0.82); STRING partners: ACAA2 (0.946), ACAT1 (0.977), ACO2 (0.999), ATP5F1A (0.94), ATP5F1C (0.726), DLAT (0.996), GOT2 (0.952), L2HGDH (0.931), NDUFV1 (0.724), PDHB (0.941), SDHA (0.984), SLC25A4 (0.852), SUCLG1 (0.929), SUCLG2 (0.948)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS is a canonical entry-point enzyme for the TCA cycle and has extensive literature support. It has strong STRING connectivity to many module enzymes, including ACO2, DLAT, GOT2, SDHA, SUCLG1, and SUCLG2, and is included in every primary GO/KEGG term (11 globally significant GO/KEGG terms, q_global 1.12e-05–0.0369; see the table). HPA shows skeletal-muscle and tongue tissue enhancement, low immune specificity, mitochondrial localization, and heart protein detection.
- **Conclusion**: Established evidence identifies CS as a highly informative biochemical marker of mitochondrial oxidative metabolism and TCA-cycle participation in the module. Its high literature volume strengthens functional confidence, but its presence does not prove that TCA flux is increased in either tissue.

#### SDHA

- **Related proteins** (co-abundance neighbors): HSDL2 (0.86), AIFM1 (0.83); STRING partners: ACAA2 (0.753), ACAT1 (0.762), ACO2 (0.975), ATP5F1A (0.972), ATP5F1C (0.75), ATP5PB (0.755), CS (0.984), DLAT (0.852), ETFA (0.706), GOT2 (0.981), NDUFA10 (0.793), NDUFV1 (0.999), PDHB (0.731), SUCLG1 (0.999), SUCLG2 (0.997)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate dehydrogenase complex flavoprotein subunit A. This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identi…
- **Diseases (Open Targets)**: mitochondrial complex II deficiency, nuclear type 1 (0.813); pheochromocytoma/paraganglioma syndrome 5 (0.790); dilated cardiomyopathy 1GG (0.768); neurodegeneration with ataxia and late-onset optic atrophy (0.761); gastrointestinal stromal tumor (0.743)
- **Europe PMC papers**: 12756
- **Why important**: SDHA links TCA-cycle metabolism with respiratory electron transport as a catalytic subunit of succinate dehydrogenase. It is included in every primary term (11 globally significant GO/KEGG terms, q_global 1.12e-05–0.0369; see the table), has extensive STRING connections across the module, and is strongly connected to ACO2, ATP synthase components, CS, GOT2, NDUFV1, and SUCLG proteins. HPA shows heart-muscle and skeletal-muscle enhancement, mitochondrial localization, and heart protein detection. Its disease associations include respiratory-chain deficiency, cardiomyopathy, and neurodegenerative conditions.
- **Conclusion**: Established evidence supports SDHA as a bridge between the TCA cycle and the respiratory chain, making it central to the proposed module function. The module is consistent with coordinated oxidative metabolism, but does not establish SDHA dysfunction or altered succinate oxidation in the samples.

#### DLAT

- **Related proteins** (co-abundance neighbors): HSDL2 (0.91), GOT2 (0.81), ACAA2 (0.81); STRING partners: ACAA2 (0.892), ACAT1 (0.949), ACO2 (0.727), ATP5F1A (0.8), CS (0.996), PDHB (0.999), SDHA (0.852), SUCLG1 (0.99), SUCLG2 (0.967)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_04919.1, huMAP3_08216.1, huMAP3_07514.1, huMAP3_09761.1, huMAP3_10899.1, huMAP3_10412.1, huMAP3_14339.1, huMAP3_11877.1, huMAP3_14864.1, huMAP3_12248.1
- **Function (MyGene.info)**: dihydrolipoamide S-acetyltransferase. This gene encodes component E2 of the multi-enzyme pyruvate dehydrogenase complex (PDC). PDC resides in the inner mitochondrial membrane and catalyzes the conversion of pyruvate to acetyl coenzyme A. The protein product of this gene, dihydrolipoamide acetyltransferase, accepts acetyl groups formed by the oxidative decarboxylation of pyruvate and transfers them to coenzyme A. Dihydrolipoamide acety…
- **Diseases (Open Targets)**: pyruvate dehydrogenase E2 deficiency (0.792); pyruvate decarboxylase deficiency (0.711); dystonic disorder (0.374); hereditary disease (0.341); neurodegenerative disease (0.322)
- **Europe PMC papers**: 3481
- **Why important**: DLAT is the E2 component of the pyruvate dehydrogenase complex and links pyruvate catabolism to acetyl-CoA production and the TCA cycle. It has strong STRING relationships with CS, PDHB, SUCLG1, SUCLG2, and other metabolic proteins, and appears in the pyruvate-dehydrogenase-related hu.MAP complexes (hu.MAP huMAP3_04919.1) (hu.MAP huMAP3_08216.1) (hu.MAP huMAP3_07514.1) (hu.MAP huMAP3_09761.1) (hu.MAP huMAP3_10899.1) (hu.MAP huMAP3_10412.1) (hu.MAP huMAP3_14339.1) (hu.MAP huMAP3_11877.1) (hu.MAP huMAP3_14864.1) (hu.MAP huMAP3_12248.1). It is included in all primary GO/KEGG terms (11 globally significant GO/KEGG terms, q_global 1.12e-05–0.0369; see the table), shows cardiomyocyte enrichment at the single-cell level, and has heart protein detection. Its disease associations include pyruvate-dehydrogenase E2 deficiency.
- **Conclusion**: Established evidence supports DLAT as a mechanistic gateway from carbohydrate-derived pyruvate into mitochondrial oxidation. Its network and complex evidence make it important for interpreting the module as an integrated pathway. The data do not demonstrate that pyruvate is the dominant substrate in bone or heart.

#### SLC25A4

- **Related proteins** (co-abundance neighbors): ACO2 (0.86), NDUFA10 (0.86); STRING partners: ACO2 (0.706), ATP5F1A (0.868), CS (0.852)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 25 member 4. This gene is a member of the mitochondrial carrier subfamily of solute carrier protein genes. The product of this gene functions as a gated pore that translocates ADP from the cytoplasm into the mitochondrial matrix and ATP from the mitochondrial matrix into the cytoplasm. The protein forms a homodimer embedded in the inner mitochondria membrane. Mutations in this gene have been shown to result in…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome 12B (cardiomyopathic type), autosomal recessive (0.783); mitochondrial DNA depletion syndrome 12A (cardiomyopathic type), autosomal dominant (0.776); progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal dominant 2 (0.775); Sengers syndrome (0.620); neurodegenerative disease (0.528)
- **Europe PMC papers**: 1754
- **Why important**: SLC25A4 is the mitochondrial ADP/ATP carrier and therefore provides a direct link between oxidative phosphorylation inside mitochondria and cellular nucleotide demand. It has heart-muscle, skeletal-muscle, and tongue group enrichment, heart protein detection, and disease associations involving cardiomyopathy, mitochondrial DNA depletion, external ophthalmoplegia, and Sengers syndrome. Within the module it connects ACO2 and NDUFA10 and has STRING support with ATP5F1A and CS. It is included in the primary mitochondrion and energy-generation terms (GO:CC mitochondrion; q_global = 1.12e-05) (GO:BP generation of precursor metabolites and energy; q_global = 4.46e-05).
- **Conclusion**: Established evidence supports SLC25A4 as a functionally important output interface for mitochondrial ATP production, especially relevant to heart and muscle biology. Its relatively limited network connectivity does not make it a global module hub, but its transport role gives it high mechanistic importance. A direct effect on tissue energy supply remains a hypothesis.

## Module 2

**Tissue pair**: bone and heart  
**Genes (34)**: ACO1, ANXA7, CAPN1, CAPN2, CBR1, CNDP2, CSRP1, DSTN, DNM1L, DPYSL2, DYNC1H1, EHD4, GSN, GSR, IDH1, ILK, LTA4H, NEXN, OLA1, PALLD, PDLIM1, PFKP, PLS3, ATIC, PYGB, RSU1, RTCA, FARSB, QARS1, RARS1, USP5, VPS35, WDR1, XPNPEP1

### Function

No GO or KEGG term passed global correction, and STRING reported no supplementary functional enrichment. Therefore, the module does not support a statistically established single pathway annotation. Its gene-level biology nevertheless points to a composite intracellular program involving actin and cytoskeletal organization, adhesion and mechanotransduction, proteolysis, intracellular trafficking, energy and redox metabolism, and protein synthesis. The network contains coherent known pairs and complexes for calpain activity (hu.MAP huMAP3_03767.1) (hu.MAP huMAP3_08670.1) (hu.MAP huMAP3_09127.1) (hu.MAP huMAP3_09328.1) (hu.MAP huMAP3_10242.1), (hu.MAP huMAP3_13615.1) (hu.MAP huMAP3_14229.1) (hu.MAP huMAP3_04827.1) (hu.MAP huMAP3_11557.1) (hu.MAP huMAP3_12716.1) (hu.MAP huMAP3_12926.1), (hu.MAP huMAP3_11557.1) (hu.MAP huMAP3_12716.1) (hu.MAP huMAP3_12926.1), integrin-linked adhesion (hu.MAP huMAP3_06647.1), (hu.MAP huMAP3_04827.1), (hu.MAP huMAP3_09385.1), (hu.MAP huMAP3_11194.1), actin turnover (hu.MAP huMAP3_11076.1), aminoacyl-tRNA synthetases (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1), and IDH1–PLS3 association (hu.MAP huMAP3_02650.1). This is best interpreted as a cellular maintenance and structural-stress module rather than evidence for one specific biological pathway.

**Cell composition.** The module is not dominated by secreted proteins: HPA identifies only GSN as secreted to blood, while the other genes are intracellular or membrane-associated. It is also not strongly immune-cell specific overall, although several members show platelet, megakaryocyte, smooth-muscle, vascular, or selected leukocyte enrichment. A large majority of genes have cell-type-enhanced expression, whereas tissue specificity is mixed, with many genes having low tissue specificity and others enhanced in heart muscle, blood vessel, skeletal muscle, brain, liver, intestine, or esophagus. Heart protein detection is widespread among the measured genes, but bone protein detection has no matching HPA tissue data. The platelet and megakaryocyte signals, together with the blood-cell annotations, mean that residual blood, vascular cells, or shared stromal and contractile cell types could contribute to the conserved bone–heart co-abundance pattern. Conversely, the presence of heart-muscle, actin, adhesion, and cytoskeletal genes also supports a genuine tissue-cellular component rather than a purely plasma-protein signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited set of already known or biologically plausible relationships: the strongest examples are ACO1–IDH1, CAPN1–CAPN2, ILK–RSU1, QARS1–RARS1, and the links involving VPS35, DNM1L, WDR1, DSTN, FARSB, and OLA1. These interactions indicate that parts of the co-abundance module recapitulate established molecular machinery rather than defining entirely unconnected proteins. hu.MAP independently supports repeated calpain complexes containing CAPN1 and CAPN2 (hu.MAP huMAP3_03767.1) (hu.MAP huMAP3_08670.1) (hu.MAP huMAP3_09127.1) (hu.MAP huMAP3_09328.1) (hu.MAP huMAP3_10242.1), (hu.MAP huMAP3_13615.1) (hu.MAP huMAP3_14229.1) (hu.MAP huMAP3_04827.1) (hu.MAP huMAP3_11557.1) (hu.MAP huMAP3_12716.1) (hu.MAP huMAP3_12926.1), adhesion complexes containing ILK and RSU1 (hu.MAP huMAP3_06647.1), (hu.MAP huMAP3_04827.1), (hu.MAP huMAP3_09385.1), (hu.MAP huMAP3_11194.1), the actin-regulatory pair WDR1 and DSTN (hu.MAP huMAP3_11076.1), aminoacyl-tRNA synthetase complexes containing QARS1 and RARS1 (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1), and complexes containing PLS3 with IDH1 (hu.MAP huMAP3_02650.1), or PLS3 with the broader multiprotein assembly (hu.MAP huMAP3_14442.1), (hu.MAP huMAP3_10900.1). Thus, the module has several known molecular substructures, but these relationships do not establish that all module members form one physical complex or one unified pathway.

**STRING interactions (score >= 0.7)**: 11 of 561 gene pairs: ACO1–IDH1 (0.998); ANXA7–VPS35 (0.785); CAPN1–CAPN2 (0.978); DNM1L–VPS35 (0.9); DSTN–WDR1 (0.794); FARSB–OLA1 (0.702); FARSB–RARS1 (0.706); GSR–IDH1 (0.776); ILK–RSU1 (0.991); OLA1–RARS1 (0.747); QARS1–RARS1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (PDLIM1, LTA4H, PLS3, ATIC, XPNPEP1, OLA1; 6/57); huMAP3_02650.1 (IDH1, PLS3; 2/2); huMAP3_03767.1 (CAPN1, CAPN2; 2/3); huMAP3_08670.1 (CAPN1, CAPN2; 2/4); huMAP3_09127.1 (CAPN1, CAPN2; 2/5); huMAP3_09328.1 (CAPN1, CAPN2; 2/6); huMAP3_10242.1 (CAPN1, CAPN2; 2/6); huMAP3_10900.1 (IDH1, PLS3; 2/6); huMAP3_06647.1 (ILK, RSU1; 2/6); huMAP3_13615.1 (CAPN1, CAPN2; 2/7); huMAP3_14229.1 (CAPN1, CAPN2; 2/7); huMAP3_04827.1 (ILK, RSU1; 2/7); huMAP3_11557.1 (CAPN1, CAPN2; 2/8); huMAP3_12716.1 (CAPN1, CAPN2; 2/8); huMAP3_12926.1 (CAPN1, CAPN2; 2/8); huMAP3_09385.1 (ILK, RSU1; 2/8); huMAP3_11076.1 (WDR1, DSTN; 2/10); huMAP3_11194.1 (ILK, RSU1; 2/10); huMAP3_02637.1 (QARS1, RARS1; 2/14); huMAP3_13688.1 (QARS1, RARS1; 2/14)

### Novelty

The conserved co-abundance module may represent a new systems-level observation, but the fact sheet does not establish a new molecular complex or a new pathway. Several internal relationships are already represented in STRING and hu.MAP, especially calpain, adhesion, actin-regulatory, aminoacylation, and IDH1-related assemblies. The absence of global GO or KEGG enrichment and the absence of STRING functional enrichment further argue against claiming a newly discovered canonical pathway. A cautious conclusion is that the potentially novel feature is the coordinated abundance of these partly known cellular components across bone and heart. Demonstrating novelty would require comparison with prior bone–heart co-abundance modules, independent cohorts, cell-composition-adjusted analyses, and experimental validation; absence from a database alone would not prove novelty.

**Hypothesis.** Hypothesis: this module reflects a shared structural-stress and cellular-maintenance state in bone and heart. In this model, PLS3, NEXN, PDLIM1, PALLD, DSTN, WDR1, ILK, and RSU1 coordinate actin organization, adhesion, and force transmission; CAPN1 and CAPN2 remodel cytoskeletal or adhesion proteins in a calcium-responsive manner; VPS35 and DNM1L support membrane and organelle trafficking; and IDH1, GSR, ACO1, PYGB, and PFKP help maintain metabolic and redox capacity. The aminoacylation and purine-biosynthesis genes could reflect the protein-production and energetic demands of cells experiencing structural turnover. The platelet, vascular, and blood-cell signatures raise an alternative or complementary hypothesis that shared vascular or residual blood-cell composition contributes substantially to the apparent cross-tissue conservation. These mechanisms are hypotheses, not conclusions supported by globally significant enrichment.

### Important genes

#### PLS3

- **Related proteins** (co-abundance neighbors): CAPN1 (0.89), WDR1 (0.89), ATIC (0.87), DPYSL2 (0.87), GSR (0.87), DYNC1H1 (0.87), OLA1 (0.85), IDH1 (0.83), XPNPEP1 (0.82), PFKP (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cytosol; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_14442.1, huMAP3_02650.1, huMAP3_10900.1
- **Function (MyGene.info)**: plastin 3. Plastins are a family of actin-binding proteins that are conserved throughout eukaryote evolution and expressed in most tissues of higher eukaryotes. In humans, two ubiquitous plastin isoforms (L and T) have been identified. Plastin 1 (otherwise known as Fimbrin) is a third distinct plastin isoform which is specifically expressed at high levels in the small intestine. The L isoform is expressed on…
- **Diseases (Open Targets)**: X-linked osteoporosis with fractures (0.727); congenital diaphragmatic hernia (0.553); osteoporosis (0.477); hernia, anterior diaphragmatic (0.380); postmenopausal osteoporosis (0.341)
- **Europe PMC papers**: 1365
- **Why important**: PLS3 is among the most connected genes in the module and links CAPN1, WDR1, ATIC, DPYSL2, GSR, DYNC1H1, OLA1, and IDH1. Its established function is actin-filament bundling and actin-network formation, and it is represented in hu.MAP assemblies (hu.MAP huMAP3_14442.1), (hu.MAP huMAP3_02650.1), and (hu.MAP huMAP3_10900.1). HPA shows blood-vessel enhancement, heart detection, and selected vascular or immune-cell associations. Its disease associations include X-linked osteoporosis with fractures and osteoporosis, making it particularly relevant to the bone–heart comparison.
- **Conclusion**: Established evidence supports PLS3 as a structural actin organizer and a plausible bridge between bone-related phenotypes and vascular or cardiac cellular architecture. It is a strong module anchor. It is not established that PLS3 drives the shared tissue module; its centrality could also reflect shared cell composition.

#### CAPN1

- **Related proteins** (co-abundance neighbors): ATIC (0.90), VPS35 (0.90), PLS3 (0.89), OLA1 (0.88), RARS1 (0.88), WDR1 (0.87), USP5 (0.86), CAPN2 (0.85), RTCA (0.84), IDH1 (0.83), NEXN (0.82), XPNPEP1 (0.81); STRING partners: CAPN2 (0.978)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_03767.1, huMAP3_08670.1, huMAP3_09127.1, huMAP3_09328.1, huMAP3_10242.1, huMAP3_13615.1, huMAP3_14229.1, huMAP3_11557.1, huMAP3_12716.1, huMAP3_12926.1
- **Function (MyGene.info)**: calpain 1. The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpa…
- **Diseases (Open Targets)**: Autosomal recessive spastic paraplegia type 76 (0.781); Alzheimer disease (0.383); neurodegenerative disease (0.326); hereditary spastic paraplegia 11 (0.266); hereditary disease (0.193)
- **Europe PMC papers**: 1869
- **Why important**: CAPN1 has high network connectivity and links structural, metabolic, trafficking, and translation-associated members. It forms a high-confidence STRING relationship with CAPN2 and appears together with CAPN2 across many hu.MAP calpain complexes (hu.MAP huMAP3_03767.1) (hu.MAP huMAP3_08670.1) (hu.MAP huMAP3_09127.1) (hu.MAP huMAP3_09328.1) (hu.MAP huMAP3_10242.1), (hu.MAP huMAP3_13615.1) (hu.MAP huMAP3_14229.1) (hu.MAP huMAP3_04827.1) (hu.MAP huMAP3_11557.1) (hu.MAP huMAP3_12716.1) (hu.MAP huMAP3_12926.1). Its established function is calcium-activated intracellular proteolysis, with roles in cytoskeletal remodeling and cellular signaling. It has a substantial literature base and disease associations including autosomal recessive spastic paraplegia and neurodegenerative disease.
- **Conclusion**: Established evidence supports CAPN1 as a proteolytic remodeling component that could connect calcium-dependent stress responses to cytoskeletal turnover. Its repeated complex support makes it an important mechanistic candidate, but the co-abundance data do not demonstrate calpain activation or direct action in bone and heart.

#### NEXN

- **Related proteins** (co-abundance neighbors): XPNPEP1 (0.82), CAPN1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nexilin F-actin binding protein. This gene encodes a filamentous actin-binding protein that may function in cell adhesion and migration. Mutations in this gene have been associated with dilated cardiomyopathy, also known as CMD1CC. Alternatively spliced transcript variants have been described.[provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: dilated cardiomyopathy 1CC (0.792); hypertrophic cardiomyopathy 20 (0.746); familial isolated dilated cardiomyopathy (0.667); hypertrophic cardiomyopathy (0.584); cardiomyopathy, dilated, 2M (0.565)
- **Europe PMC papers**: 1090
- **Why important**: NEXN is specifically enhanced in heart muscle and skeletal muscle, detected in heart, and enhanced in cardiomyocytes and myonuclei. It encodes an F-actin-binding protein involved in adhesion and cytoskeletal organization. Its disease associations include dilated and hypertrophic cardiomyopathy, with a meaningful literature base. Although its network connectivity is limited, its tissue relevance and disease specificity make it more informative biologically than connectivity alone would suggest.
- **Conclusion**: Established evidence supports NEXN as a heart- and muscle-relevant structural component. It strengthens the interpretation that at least part of the module may reflect contractile or adhesive cell biology. Whether NEXN participates in a shared bone–heart mechanism rather than marking the heart contribution remains unresolved.

#### IDH1

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.88), GSR (0.86), QARS1 (0.85), PLS3 (0.83), CAPN1 (0.83), WDR1 (0.81), FARSB (0.80), XPNPEP1 (0.80); STRING partners: ACO1 (0.998), GSR (0.776)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02650.1, huMAP3_10900.1
- **Function (MyGene.info)**: isocitrate dehydrogenase (NADP(+)) 1. Isocitrate dehydrogenases catalyze the oxidative decarboxylation of isocitrate to 2-oxoglutarate. These enzymes belong to two distinct subclasses, one of which utilizes NAD(+) as the electron acceptor and the other NADP(+). Five isocitrate dehydrogenases have been reported: three NAD(+)-dependent isocitrate dehydrogenases, which localize to the mitochondrial matrix, and two NADP(+)-dependent isoci…
- **Diseases (Open Targets)**: acute myeloid leukemia (0.779); Ollier disease (0.672); glioblastoma (0.657); cholangiocarcinoma (0.652); glioma (0.637)
- **Europe PMC papers**: 29424
- **Why important**: IDH1 is connected to DPYSL2, GSR, QARS1, PLS3, CAPN1, WDR1, FARSB, and XPNPEP1, and it has known STRING relationships with ACO1 and GSR. It is represented in hu.MAP complexes with PLS3 (hu.MAP huMAP3_02650.1) and (hu.MAP huMAP3_10900.1). Its established function includes cytosolic isocitrate metabolism and NADPH regeneration, linking metabolism to redox control. It has very extensive literature coverage and disease associations including acute myeloid leukemia, Ollier disease, glioblastoma, cholangiocarcinoma, and glioma.
- **Conclusion**: Established evidence supports IDH1 as a metabolic and redox node that could supply resilience during structural or energetic stress. Its network position links metabolic and cytoskeletal portions of the module. The data do not establish altered IDH1 catalysis, an oncogenic IDH1 state, or a causal role in the bone–heart conservation.

#### ILK

- **Related proteins** (co-abundance neighbors): RSU1 (0.81); STRING partners: RSU1 (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_06647.1, huMAP3_04827.1, huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: integrin linked kinase. This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastas…
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); familial hypertrophic cardiomyopathy (0.194); Abnormality of the cardiovascular system (0.148); Prolonged QT interval (0.118); neoplasm (0.118)
- **Europe PMC papers**: 8401
- **Why important**: ILK has limited direct network connectivity but forms a very strong STRING relationship with RSU1 and is repeatedly present with RSU1 in hu.MAP adhesion-related complexes (hu.MAP huMAP3_06647.1), (hu.MAP huMAP3_04827.1), (hu.MAP huMAP3_09385.1), and (hu.MAP huMAP3_11194.1). Its established function is integrin-linked signaling at focal adhesions, including cell-matrix adhesion and morphogenesis. HPA detects it in heart and shows associations with smooth-muscle cells, megakaryocytes, and platelets. Its disease associations include familial hypertrophic cardiomyopathy and cardiovascular abnormalities, while its literature coverage is substantial.
- **Conclusion**: Established evidence supports ILK as an adhesion and mechanotransduction component that could connect matrix interactions with cardiac or vascular structure. It is important because a low-connectivity node can still mark a well-defined biological subcomplex. A causal role in the conserved module remains hypothetical.

## Module 3

**Tissue pair**: bone and heart  
**Genes (5)**: ACOT9, HACL2, JUP, SCO1, TRAP1

### Function

No GO/KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The available evidence instead suggests a mixed co-abundance signature linking mitochondrial and lipid-related biology with cellular stress handling and epithelial or cardiac cell-junction biology. ACOT9 is the most connected node and is annotated for acyl-CoA and fatty-acid metabolism; HACL2 is annotated for fatty-acid alpha-oxidation; SCO1 supports cytochrome-c-oxidase assembly and copper homeostasis; TRAP1 is a mitochondrial chaperone associated with stress responses and regulation of respiration; and JUP is a desmosomal and intermediate-junction component. These annotations are biologically compatible with a shared tissue-state or cell-composition signal, but they do not establish a single pathway or direct protein complex.

**Cell composition.** The module is not dominated by secreted or plasma proteins, since none of its genes is secreted. Most genes have low tissue specificity, while JUP is tissue enhanced in esophagus and skin. All genes have cell-type-enhanced HPA annotations, with signals involving epithelial populations, trophoblasts, and selected immune populations. The module is therefore compatible with shared cell-type or sample-composition effects across bone and heart. However, it is not uniformly blood-cell enriched: most genes have low immune-cell specificity, whereas JUP has group-enriched blood-cell expression. HPA protein detection is reported for most module genes in heart muscle, while no matching HPA bone tissue result is available, so the bone interpretation remains particularly dependent on the co-abundance data rather than direct protein validation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no hu.MAP complex containing multiple module members. Thus, the co-abundance edges are not corroborated here as established physical or functional protein interactions. The absence of STRING or hu.MAP support argues against interpreting this module as a known molecular complex. It does not invalidate the co-abundance pattern, because co-abundance can reflect shared regulation, cell composition, organelle state, or indirect biological coupling rather than direct binding.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears to be a potentially novel co-abundance association rather than a demonstrated new molecular complex. The lack of multi-member STRING and hu.MAP support means the precise combination of ACOT9, HACL2, SCO1, TRAP1, and JUP is not represented as an established interaction module in the supplied resources. Nevertheless, absence from those resources alone cannot prove novelty: the individual genes have prior functional annotations, disease associations, and literature, and the observed association may arise from shared cell types or a tissue-state effect. A stronger novelty claim would require replication in independent bone and heart datasets, control for cell composition, and comparison with published co-expression or proteomic modules.

**Hypothesis.** Hypothesis: the module may reflect a shared mitochondrial-metabolic and cellular-junction state present in particular cell populations sampled from bone and heart. In this model, ACOT9 and HACL2 represent lipid-processing activity, SCO1 and TRAP1 represent mitochondrial respiratory-chain assembly and stress adaptation, and JUP represents the structural or epithelial-like junctional component. The apparent linkage could be indirect, produced by coordinated abundance within a shared cell population or by tissue stress, rather than by direct interaction among the proteins. This hypothesis should be tested by cell-type deconvolution, replication at the protein level, and examination of whether mitochondrial, lipid, and junctional signals covary within the same cells.

### Important genes

#### ACOT9

- **Related proteins** (co-abundance neighbors): HACL2 (0.83), TRAP1 (0.82), JUP (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA thioesterase 9. The protein encoded by this gene is a mitochondrial acyl-CoA thioesterase of unknown function. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2010].
- **Diseases (Open Targets)**: rotator cuff syndrome (0.163); shoulder impingement syndrome (0.162); hepatocellular carcinoma (0.039); laryngeal squamous cell carcinoma (0.016); neoplasm (0.013)
- **Europe PMC papers**: 322
- **Why important**: ACOT9 is the most connected node in the module and links the lipid-metabolism annotations to both mitochondrial and structural members of the network. It is annotated as a mitochondrial acyl-CoA thioesterase involved in fatty-acid and acyl-CoA metabolism. Its HPA profile is broadly expressed with cell-type enhancement in cDCs, monocytes, and neutrophils, making it informative both biologically and for assessing cell-composition effects. It has a substantial literature and disease-association record.
- **Conclusion**: Established evidence supports ACOT9 as the network hub and as a lipid-metabolism gene. It is a plausible organizing marker for the module, but the data do not establish that it directly regulates the other module genes. Its immune-cell-associated HPA pattern also means that an abundance or composition effect remains plausible.

#### SCO1

- **Related proteins** (co-abundance neighbors): HACL2 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: synthesis of cytochrome C oxidase 1. Mammalian cytochrome c oxidase (COX) catalyzes the transfer of reducing equivalents from cytochrome c to molecular oxygen and pumps protons across the inner mitochondrial membrane. In yeast, 2 related COX assembly genes, SCO1 and SCO2 (synthesis of cytochrome c oxidase), enable subunits 1 and 2 to be incorporated into the holoprotein. This gene is the human homolog to the yeast SCO1 gene. [provide…
- **Diseases (Open Targets)**: mitochondrial complex IV deficiency, nuclear type 4 (0.782); leigh syndrome due to mitochondrial complex iv deficiency (0.583); mitochondrial complex IV deficiency, nuclear-type (0.543); neurodegenerative disease (0.484); mitochondrial disease (0.372)
- **Europe PMC papers**: 1293
- **Why important**: SCO1 provides the clearest respiratory-chain interpretation in the module. It is annotated for cytochrome-c-oxidase assembly and intracellular copper homeostasis, has a direct co-abundance connection to HACL2, and is detected in heart muscle by HPA. Its disease associations are strongly centered on mitochondrial complex IV deficiency and related mitochondrial disease, and it has extensive literature.
- **Conclusion**: Established evidence supports SCO1 as a mitochondrial respiratory-chain assembly factor with clinically relevant mitochondrial disease associations. Its presence supports a mitochondrial component of the module, but the single co-abundance connection and lack of STRING or hu.MAP support do not demonstrate a physical SCO1-containing complex with the other module members.

#### TRAP1

- **Related proteins** (co-abundance neighbors): ACOT9 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TNF receptor associated protein 1. This gene encodes a mitochondrial chaperone protein that is member of the heat shock protein 90 (HSP90) family. The encoded protein has ATPase activity and interacts with tumor necrosis factor type I. This protein may function in regulating cellular stress responses. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jan 2013].
- **Diseases (Open Targets)**: congenital anomaly of kidney and urinary tract (0.643); VACTERL/vater association (0.492); atrial fibrillation (0.467); neurodegenerative disease (0.372); Blindness (0.338)
- **Europe PMC papers**: 2586
- **Why important**: TRAP1 is a mitochondrial HSP ninety-family chaperone and one of the module members connected to ACOT9. Its annotations involve protein folding, cellular respiration, reactive oxygen species, apoptosis, and stress responses. It is detected in heart muscle, has disease associations including atrial fibrillation and neurodegenerative disease, and has extensive literature.
- **Conclusion**: Established evidence supports TRAP1 as a mitochondrial stress and proteostasis regulator. It strengthens the interpretation that the module may report mitochondrial stress or respiratory state. Whether TRAP1 is mechanistically linked to ACOT9 in this module is unresolved, because the relationship is co-abundance-based and lacks corroboration from STRING or hu.MAP.

#### JUP

- **Related proteins** (co-abundance neighbors): ACOT9 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cell Junctions; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: junction plakoglobin. This gene encodes a major cytoplasmic protein which is the only known constituent common to submembranous plaques of both desmosomes and intermediate junctions. This protein forms distinct complexes with cadherins and desmosomal cadherins and is a member of the catenin family since it contains a distinct repeating amino acid motif called the armadillo repeat. Mutation in this gene has been associa…
- **Diseases (Open Targets)**: Naxos disease (0.784); arrhythmogenic right ventricular dysplasia 12 (0.755); arrhythmogenic right ventricular cardiomyopathy (0.597); lethal acantholytic epidermolysis bullosa (0.383); familial isolated arrhythmogenic ventricular dysplasia, biventricular form (0.370)
- **Europe PMC papers**: 3429
- **Why important**: JUP is a structural junctional protein and the only module member with tissue-enhanced HPA expression, particularly in esophagus and skin. It is a constituent of desmosomal and intermediate-junction plaques, is involved in cell adhesion and desmosome assembly, and is associated with Naxos disease and arrhythmogenic right ventricular cardiomyopathy. It is connected to ACOT9 in the module and has the largest literature record among the listed genes.
- **Conclusion**: Established evidence supports JUP as a cell-adhesion and junctional component with important cardiac and epithelial disease relevance. Its inclusion may indicate a structural or cell-type component of the shared signal, but it is not evidence that the module is a desmosomal complex. Its blood-cell enrichment in HPA also warrants explicit control for cellular composition.

#### HACL2

- **Related proteins** (co-abundance neighbors): SCO1 (0.86), ACOT9 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 2-hydroxyacyl-CoA lyase 2. The protein encoded by this gene shares similarity with several thiamine pyrophosphate-binding proteins identified in bacteria, yeast, and plants. The highest degree of similarity is found with bacterial acetolactate synthases (AHAS), which are enzymes that catalyze the first step in branched-chain amino acid biosynthesis. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: male infertility (0.025); COVID-19 (0.020); tuberculosis (0.018); hepatocellular carcinoma (0.018); lung adenocarcinoma (0.015)
- **Europe PMC papers**: 107
- **Why important**: HACL2 connects ACOT9 to SCO1 and is annotated for fatty-acid alpha-oxidation, providing a metabolic bridge within the module. Its HPA cell-type-enhanced pattern includes enterocytes, esophageal apical cells, trophoblasts, and melanocytes, which emphasizes that its abundance may be cell-population dependent. It has a smaller literature and disease-association record than the other selected genes, but its network position and metabolic annotation make it important for interpreting the module.
- **Conclusion**: Established evidence supports HACL2 as a fatty-acid alpha-oxidation enzyme and as a connecting node between ACOT9 and SCO1 in the co-abundance graph. The proposed connection between lipid oxidation and mitochondrial respiratory biology is a hypothesis rather than a demonstrated biochemical relationship in this module.

## Module 4

**Tissue pair**: bone and heart  
**Genes (10)**: ADD3, DHX9, DDX39B, MACROH2A1, H4C1, HNRNPH1, HNRNPL, HNRNPR, LMNB2, MATR3

### Function

The module is best interpreted as a conserved nuclear RNA-processing and pre-mRNA-splicing program. The primary enrichment evidence identifies spliceosomal RNA splicing and related mRNA-processing processes through the same five genes (GO:BP RNA splicing, via transesterification reactions; q_global = 0.000849), (GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 0.000849), (GO:BP mRNA splicing, via spliceosome; q_global = 0.000849), (GO:BP mRNA processing; q_global = 0.00229), (GO:BP RNA splicing; q_global = 0.00229), (GO:BP mRNA metabolic process; q_global = 0.01), (GO:BP RNA processing; q_global = 0.0174). All module genes are assigned to the nuclear lumen (GO:CC nuclear lumen; q_global = 0.00222), and the module also shows enrichment for ribonucleoprotein complexes (GO:CC ribonucleoprotein complex; q_global = 0.0223). The pattern is therefore consistent with coordinated regulation of RNA maturation, RNA-binding, spliceosome function, and associated nuclear organization. The chromatin and nuclear-envelope genes suggest that the module also connects RNA processing with nuclear structure, but the strongest functional conclusion is RNA processing rather than chromatin regulation.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity and low immune-cell specificity, and their annotations predominantly describe broadly distributed nuclear proteins. Thus, the shared bone-heart signal is more consistent with a general nuclear housekeeping or cell-state program than with a tissue-specific extracellular pathway. The HPA data show protein detection for every listed gene in heart, while there is no matching HPA tissue result for bone, so the cross-tissue interpretation should not be taken as direct evidence of equivalent protein abundance in bone. Several genes have cell-type-enhanced annotations, including neural and progenitor populations, and H4C1 has tissue and blood-cell enrichment annotations. These observations leave open a contribution from shared cell types or sample composition, but the absence of secreted genes and the low overall immune specificity argue against a simple plasma or blood-cell module explanation.

**GO/KEGG enrichment**: 9 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA splicing, via transesterification reactions | 0.000849 | DDX39B, DHX9, HNRNPH1, HNRNPL, HNRNPR |
| GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile | 0.000849 | DDX39B, DHX9, HNRNPH1, HNRNPL, HNRNPR |
| GO:BP mRNA splicing, via spliceosome | 0.000849 | DDX39B, DHX9, HNRNPH1, HNRNPL, HNRNPR |
| GO:CC nuclear lumen | 0.00222 | ADD3, DDX39B, DHX9, H4C1, HNRNPH1, HNRNPL, HNRNPR, LMNB2, MACROH2A1, MATR3 |
| GO:BP mRNA processing | 0.00229 | DDX39B, DHX9, HNRNPH1, HNRNPL, HNRNPR |
| GO:BP RNA splicing | 0.00229 | DDX39B, DHX9, HNRNPH1, HNRNPL, HNRNPR |
| GO:BP mRNA metabolic process | 0.01 | DDX39B, DHX9, HNRNPH1, HNRNPL, HNRNPR |
| GO:BP RNA processing | 0.0174 | DDX39B, DHX9, HNRNPH1, HNRNPL, HNRNPR |
| GO:CC ribonucleoprotein complex | 0.0223 | DDX39B, DHX9, HNRNPH1, HNRNPL, HNRNPR |

### STRING and hu.MAP

STRING supports a coherent known interaction core among DDX39B, DHX9, HNRNPH1, HNRNPL, HNRNPR, and MATR3. The strongest connectivity is concentrated among RNA helicase and heterogeneous nuclear ribonucleoprotein genes, matching the primary GO evidence. STRING also links H4C1 with MACROH2A1, providing a separate chromatin-associated connection, while ADD3 and LMNB2 are less connected peripheral members. The STRING functional results are supplementary and reinforce nuclear-lumen, nucleoplasmic, RNA-binding, mRNA-splicing, and mRNA-processing interpretations (15 supplementary STRING terms; within-query FDR 1.17e-06–0.0066); they are not additional globally corrected enrichment evidence. hu.MAP independently places HNRNPR, HNRNPL, and MATR3 together in several RNA-binding and mRNA-processing complexes (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1). MACROH2A1 and H4C1 co-occur in a chromatin and histone-related complex (hu.MAP huMAP3_10862.1). These resources indicate that much of the module reflects previously known molecular relationships and complexes, rather than an entirely uncharacterized interaction system.

**STRING interactions (score >= 0.7)**: 15 of 45 gene pairs: DDX39B–DHX9 (0.962); DDX39B–HNRNPH1 (0.742); DDX39B–HNRNPL (0.807); DDX39B–HNRNPR (0.74); DHX9–HNRNPH1 (0.878); DHX9–HNRNPL (0.901); DHX9–HNRNPR (0.909); DHX9–MATR3 (0.786); H4C1–MACROH2A1 (0.943); HNRNPH1–HNRNPL (0.982); HNRNPH1–HNRNPR (0.947); HNRNPH1–MATR3 (0.911); HNRNPL–HNRNPR (0.961); HNRNPL–MATR3 (0.757); HNRNPR–MATR3 (0.714)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Nuclear lumen (FDR = 1.17e-06, 9 genes); Component Nuclear lumen (FDR = 0.00043, 10 genes); NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex (FDR = 0.00051, 5 genes); COMPARTMENTS Nucleoplasm (FDR = 0.00055, 6 genes); SMART RNA recognition motif (FDR = 0.00083, 4 genes); RCTM mRNA Splicing - Major Pathway (FDR = 0.0011, 5 genes); NetworkNeighborAL Mixed, incl. CRD-mediated mRNA stabilization, and Zinc finger, CHHC-type (FDR = 0.0013, 4 genes); Keyword Isopeptide bond (FDR = 0.0015, 8 genes); Keyword Ubl conjugation (FDR = 0.0023, 8 genes); Keyword RNA-binding (FDR = 0.0045, 5 genes); Keyword mRNA splicing (FDR = 0.0047, 4 genes); WikiPathways mRNA processing (FDR = 0.0047, 4 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 0.005, 5 genes); Component Nuclear chromosome (FDR = 0.0052, 4 genes); COMPARTMENTS Chromatin (FDR = 0.0066, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07581.1 (HNRNPR, HNRNPL, MATR3; 3/21); huMAP3_10625.1 (HNRNPR, HNRNPL, MATR3; 3/57); huMAP3_05721.1 (HNRNPL, MATR3; 2/6); huMAP3_07225.1 (HNRNPR, HNRNPL; 2/7); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09654.1 (HNRNPR, HNRNPL; 2/13); huMAP3_10659.1 (HNRNPR, HNRNPL; 2/28); huMAP3_10862.1 (MACROH2A1, H4C1; 2/33)

### Novelty

The exact conserved co-abundance module may still be a new observation in the bone-heart comparison, but the available evidence does not establish it as a newly discovered molecular complex or pathway. Its central relationships are already represented in STRING, and several of its RNA-binding proteins occur together in hu.MAP complexes. The module is also composed largely of broadly expressed nuclear and RNA-processing proteins, which makes convergence through a shared housekeeping program plausible. Absence of some genes from hu.MAP or STRING cannot by itself demonstrate novelty. A defensible conclusion is that the tissue-pair co-abundance pattern may be novel, whereas the principal biological machinery represented by the module is established.

**Hypothesis.** Hypothesis: bone and heart samples share a coordinated nuclear gene-expression state in which spliceosomal RNA processing, RNA export, nuclear organization, and chromatin context are regulated together. HNRNPL, HNRNPR, HNRNPH1, DHX9, and DDX39B may form the functional RNA-processing core, with MATR3 helping organize or stabilize associated RNA-protein assemblies. LMNB2, MACROH2A1, and H4C1 could couple this RNA-processing state to nuclear-envelope or chromatin features, while ADD3 may reflect a cell-structural or cell-composition contribution. This hypothesis predicts coordinated changes in splicing and RNA maturation in the relevant bone and heart cell populations, but the fact sheet does not establish causality or tissue-specific regulation.

### Important genes

#### HNRNPL

- **Related proteins** (co-abundance neighbors): MATR3 (0.96), HNRNPH1 (0.87), DHX9 (0.84), HNRNPR (0.84), MACROH2A1 (0.84), LMNB2 (0.83), H4C1; H4C2; H4C3; H4C4; H4C5; H4C6; H4C8; H4C9; H4C11; H4C12; H4C13; H4C14; H4C15; H4C16 (0.82); STRING partners: DDX39B (0.807), DHX9 (0.901), HNRNPH1 (0.982), HNRNPR (0.961), MATR3 (0.757)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_07581.1, huMAP3_10625.1, huMAP3_05721.1, huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_10659.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is the most connected module member and links the principal RNA-binding proteins with MATR3, MACROH2A1, LMNB2, and the histone-related edge. It participates in every primary GO term (9 globally significant GO/KEGG terms, q_global 0.000849–0.0223; see the table) and is included in the STRING mRNA-processing and spliceosomal evidence (15 supplementary STRING terms; within-query FDR 1.17e-06–0.0066). Its annotation describes a stable heterogeneous nuclear ribonucleoprotein component involved in mRNA packaging, processing, function, and alternative splicing. It also has extensive literature and disease associations, making it a strong integrative marker of the module.
- **Conclusion**: Established evidence supports HNRNPL as a central RNA-processing scaffold and a plausible core marker of this module. Its network position and annotations support a functional role in coordinating RNA-protein assemblies. A specific bone-heart regulatory role remains a hypothesis rather than an established conclusion.

#### DHX9

- **Related proteins** (co-abundance neighbors): HNRNPL (0.84), ADD3 (0.82), MATR3 (0.81); STRING partners: DDX39B (0.962), HNRNPH1 (0.878), HNRNPL (0.901), HNRNPR (0.909), MATR3 (0.786)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is a highly connected RNA helicase linked to DDX39B, HNRNPH1, HNRNPL, HNRNPR, and MATR3 in STRING. It appears in every primary GO term (9 globally significant GO/KEGG terms, q_global 0.000849–0.0223; see the table), and its annotation provides a biochemical mechanism through ATP-dependent unwinding of RNA and DNA-RNA structures, alternative splicing, transcriptional regulation, and nuclear export. It also has the largest literature footprint among the listed genes and disease associations spanning developmental and neurodegenerative conditions.
- **Conclusion**: Established evidence supports DHX9 as an enzymatic RNA-processing component that could help drive the module's spliceosomal and RNA-export functions. Its links to osteoblast differentiation and transcriptional regulation make tissue relevance plausible, but the co-abundance data do not prove that DHX9 controls the module in bone or heart.

#### MATR3

- **Related proteins** (co-abundance neighbors): HNRNPL (0.96), HNRNPR (0.89), DHX9 (0.81), MACROH2A1 (0.81); STRING partners: DHX9 (0.786), HNRNPH1 (0.911), HNRNPL (0.757), HNRNPR (0.714)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_07581.1, huMAP3_10625.1, huMAP3_05721.1
- **Function (MyGene.info)**: matrin 3. This gene encodes a nuclear matrix protein, which is proposed to stabilize certain messenger RNA species. Mutations of this gene are associated with distal myopathy 2, which often includes vocal cord and pharyngeal weakness. Alternatively spliced transcript variants, including read-through transcripts composed of the upstream small nucleolar RNA host gene 4 (non-protein coding) and matrin 3 gene s…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.735); distal myopathy with vocal cord weakness (0.569); neurodegenerative disease (0.529); distal myopathy (0.384); hereditary disease (0.193)
- **Europe PMC papers**: 1756
- **Why important**: MATR3 is a connected bridge between the heterogeneous nuclear ribonucleoprotein core and DHX9, and it occurs with HNRNPL and HNRNPR in several hu.MAP complexes (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_05721.1). It contributes to the nuclear-lumen primary evidence (GO:CC nuclear lumen; q_global = 0.00222) and to the corresponding STRING nuclear and RNA-processing evidence (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 1.17e-06), (STRING Component Nuclear lumen; within-query FDR = 0.00043), (STRING NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex; within-query FDR = 0.00051), (STRING SMART RNA recognition motif; within-query FDR = 0.00083). Its annotation describes a nuclear matrix protein proposed to stabilize messenger RNAs, and its disease associations include distal myopathy and amyotrophic lateral sclerosis, giving it particular relevance to muscle and neuromuscular biology.
- **Conclusion**: Established evidence supports MATR3 as a nuclear RNA-associated structural or stabilizing component of the module. Its heart detection and muscle-related disease biology make it a compelling candidate for tissue-relevant interpretation, although a direct role in the shared bone-heart program remains unproven.

#### DDX39B

- **Related proteins** (co-abundance neighbors): HNRNPR (0.88), HNRNPH1 (0.86), LMNB2 (0.81); STRING partners: DHX9 (0.962), HNRNPH1 (0.742), HNRNPL (0.807), HNRNPR (0.74)
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nuclear speckles; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 39B. This gene encodes a member of the DEAD box family of RNA-dependent ATPases that mediate ATP hydrolysis during pre-mRNA splicing. The encoded protein is an essential splicing factor required for association of U2 small nuclear ribonucleoprotein with pre-mRNA, and it also plays an important role in mRNA export from the nucleus to the cytoplasm. This gene belongs to a cluster of genes localized in th…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); Alzheimer disease (0.522); Parkinson disease (0.503); lysosomal storage disease (0.503); neurodevelopmental disorder (0.413)
- **Europe PMC papers**: 1037
- **Why important**: DDX39B is connected to the principal RNA-binding core and has a particularly strong STRING relationship with DHX9. It appears in every primary GO term (9 globally significant GO/KEGG terms, q_global 0.000849–0.0223; see the table). Its annotation identifies it as an ATPase required for spliceosomal association with pre-mRNA and for export of mature mRNA from the nucleus. Its nuclear-speckle localization and disease associations involving neurodegeneration and developmental disorders further support its importance as a mechanistic RNA-processing gene.
- **Conclusion**: Established evidence supports DDX39B as a spliceosome-associated helicase and mRNA-export factor within the module. It is a plausible rate-limiting or coordinating component, but the current evidence does not establish altered DDX39B activity or a causal tissue-specific effect.

#### HNRNPR

- **Related proteins** (co-abundance neighbors): MATR3 (0.89), DDX39B (0.88), MACROH2A1 (0.87), HNRNPL (0.84), HNRNPH1 (0.84); STRING partners: DDX39B (0.74), DHX9 (0.909), HNRNPH1 (0.947), HNRNPL (0.961), MATR3 (0.714)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_07581.1, huMAP3_10625.1, huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_10659.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR is a central connected heterogeneous nuclear ribonucleoprotein and occurs in the primary splicing and RNA-processing terms (9 globally significant GO/KEGG terms, q_global 0.000849–0.0223; see the table). It participates in multiple hu.MAP complexes with HNRNPL and MATR3 (hu.MAP huMAP3_07581.1), (hu.MAP huMAP3_10625.1), (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1), and STRING places it in the dense RNA-binding interaction core. Its annotation identifies a spliceosome C-complex component involved in pre-mRNA processing and transport, while its disease associations include developmental, skeletal, and brain abnormalities.
- **Conclusion**: Established evidence supports HNRNPR as a core spliceosomal and RNA-transport factor that helps define the module's molecular identity. Its skeletal and developmental disease associations make it biologically relevant to the tissue pair, but they do not demonstrate that this module mediates those diseases.

## Module 5

**Tissue pair**: bone and heart  
**Genes (20)**: AHNAK, ANXA6, ASPH, CAP2, CLTC, DNM2, EIF3C, FLNA, FLNB, GPD2, IQGAP1, PSMC6, PSMC2, RAN, RUVBL2, SEC22B, KARS1, TKT, TLN1, TLN2

### Function

The module most plausibly represents a shared cellular infrastructure program linking cytoskeletal adhesion, membrane trafficking, protein synthesis, proteasomal quality control, and intermediary metabolism. Its network is organized around EIF3C, with additional connectivity through the talin–filamin–IQGAP1 adhesion scaffold, clathrin and dynamin trafficking, and the PSMC proteasome ATPases. This is an integrative interpretation rather than a claim of a single pathway. No GO or KEGG term passed global correction. There were also no supplementary STRING functional-enrichment terms, so the functional inference rests on the annotated genes, the network architecture, and the physical-interaction evidence.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a single secreted gene, and the genes are predominantly intracellular or membrane-associated. Most genes have low tissue specificity, while many are cell-type enhanced, particularly in neutrophils or neutrophil progenitors, with additional signals in adipocytes, vascular cells, muscle-related cells, and other specialized cell types. This makes the module compatible with a shared cellular or stromal component in bone and heart, but it also raises the possibility that part of the cross-tissue signal reflects common cell types or blood-related material rather than a bone–heart-specific program. The HPA blood-cell summary does not show broad immune specificity for most genes, arguing against interpreting the entire module as a blood-cell module. Heart protein detection is present for many genes, whereas matching HPA bone protein data are unavailable, so the protein-level comparison between the tissues remains limited.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a coherent adhesion and cytoskeletal subnetwork involving FLNA, FLNB, TLN1, TLN2, and IQGAP1, as well as a clathrin–dynamin relationship involving CLTC and DNM2. It also supports the PSMC2–PSMC6 proteasome relationship and a weaker connection between GPD2 and PSMC2. These are established molecular relationships, not newly demonstrated interactions by this module. hu.MAP independently places TLN1 and TLN2 in (hu.MAP huMAP3_01307.1), FLNB and AHNAK in (hu.MAP huMAP3_05674.1), and PSMC2 with PSMC6 in (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1). Because the hu.MAP complexes contain many members outside the module, the module appears to sample components from several known complexes rather than reproduce a complete single complex. The remaining co-abundance links, especially those connecting translation, trafficking, metabolism, and proteostasis components, should be regarded as network associations rather than confirmed physical interactions.

**STRING interactions (score >= 0.7)**: 11 of 190 gene pairs: CLTC–DNM2 (0.911); FLNA–FLNB (0.979); FLNA–IQGAP1 (0.952); FLNA–TLN1 (0.998); FLNA–TLN2 (0.996); FLNB–TLN1 (0.995); FLNB–TLN2 (0.995); GPD2–PSMC2 (0.739); IQGAP1–TLN1 (0.893); PSMC2–PSMC6 (0.999); TLN1–TLN2 (0.968)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01307.1 (TLN1, TLN2; 2/4); huMAP3_05674.1 (FLNB, AHNAK; 2/12); huMAP3_05064.1 (PSMC2, PSMC6; 2/31); huMAP3_09656.1 (PSMC2, PSMC6; 2/64); huMAP3_13725.1 (PSMC2, PSMC6; 2/69)

### Novelty

The exact cross-tissue co-abundance module appears potentially novel as an observation, because the supplied evidence shows a mixed network assembled across several established cellular systems rather than a named canonical complex or pathway. A search for the gene combination with a bone–heart co-abundance context did not identify an exact previously reported module. However, this does not establish biological novelty: many component relationships are already known through STRING and hu.MAP, and the genes have substantial prior literature. The defensible claim is therefore that the shared bone–heart co-abundance organization may be new, while its component biology is largely established. Independent replication, tissue-cell deconvolution, and comparison with published co-expression resources would be needed before calling the module a novel biological mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated maintenance of mechanically active or adherent cells in bone and heart. A talin–filamin–IQGAP1 cytoskeletal scaffold could couple integrin-linked adhesion and cell shape to clathrin–dynamin membrane turnover, while SEC22B and related trafficking machinery support membrane and secretory-system flux. EIF3C and KARS1 could sustain local protein production, PSMC2 and PSMC6 could remove damaged or misfolded proteins, and TKT, GPD2, and ASPH could support metabolic and calcium-handling demands. Shared abundance of this infrastructure could arise from common vascular, stromal, muscle-associated, or blood-related cellular contributors in the two tissues. This is a mechanistic hypothesis, not an experimentally established pathway for this module.

### Important genes

#### TLN1

- **Related proteins** (co-abundance neighbors): PSMC6 (0.90), FLNA (0.86), IQGAP1 (0.84), EIF3C (0.84), CLTC (0.82); STRING partners: FLNA (0.998), FLNB (0.995), IQGAP1 (0.893), TLN2 (0.968)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_01307.1
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 is a central network connector within the adhesion-associated part of the module and links strongly to FLNA, FLNB, IQGAP1, TLN2, and other module hubs. Its established functions include integrin activation, cell adhesion, actin organization, cell junction assembly, and cell migration. HPA places it in focal adhesion sites and identifies vascular and megakaryocyte or platelet-related enrichment. It is also represented in hu.MAP complex (hu.MAP huMAP3_01307.1) and has extensive disease and literature annotation, including hypertrophic cardiomyopathy among its Open Targets associations.
- **Conclusion**: Established evidence supports TLN1 as a structural and signaling anchor for cell adhesion and force transmission. Its position makes it a strong candidate for organizing the module, but the module alone does not prove that TLN1 drives the shared bone–heart pattern. A plausible hypothesis is that TLN1 couples tissue mechanical state to coordinated membrane trafficking and proteostasis.

#### FLNA

- **Related proteins** (co-abundance neighbors): TKT (0.87), TLN1 (0.86), PSMC6 (0.81); STRING partners: FLNB (0.979), IQGAP1 (0.952), TLN1 (0.998), TLN2 (0.996)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is a well-studied actin-crosslinking and membrane-receptor scaffold with strong STRING relationships to FLNB, TLN1, TLN2, and IQGAP1. It occupies the adhesion and cytoskeletal core of the network and is tissue enhanced in blood vessels, with cell-type enhancement in several structural and vascular-associated populations. Its established roles in cell shape, migration, integrin-linked signaling, and platelet-related processes connect the module to both skeletal and cardiovascular cellular biology. It also has extensive disease and literature evidence.
- **Conclusion**: Established evidence supports FLNA as a major cytoskeletal integrator and a biologically important member of the module. The shared co-abundance signal may reflect coordinated structural remodeling, but it does not demonstrate a bone–heart-specific FLNA mechanism. The strongest hypothesis is that FLNA helps couple adhesion and cytoskeletal state to the other module processes.

#### PSMC2

- **Related proteins** (co-abundance neighbors): EIF3C (0.86), KARS1 (0.85), SEC22B (0.85), RAN (0.81), DNM2 (0.81); STRING partners: GPD2 (0.739), PSMC6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is a proteasome regulatory ATPase and a network bridge between EIF3C, KARS1, SEC22B, RAN, DNM2, and the PSMC6 proteasome component. It is supported by STRING and by hu.MAP complexes (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1). Its annotations include ubiquitin-dependent proteolysis, oxidative-stress response, and proteasomal protein catabolism, while its disease associations include plasma cell myeloma and amyloidosis. Its literature volume is substantial.
- **Conclusion**: Established evidence supports PSMC2 as a proteostasis component that can connect protein quality control with broader cellular stress responses. Its module position supports a coordinating role, but there is no evidence here that proteasome activity is specifically altered in bone or heart. The hypothesis is that PSMC2 helps maintain the protein-quality demands imposed by adhesion, trafficking, and mechanical stress.

#### EIF3C

- **Related proteins** (co-abundance neighbors): CLTC (0.93), AHNAK (0.87), PSMC2 (0.86), RAN (0.84), TKT (0.84), TLN1 (0.84), SEC22B (0.83), PSMC6 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C has the strongest apparent network centrality in the module and connects translation initiation with trafficking, proteasome components, RAN, TKT, and talin-associated structure. Its established function is as a subunit of the eukaryotic translation-initiation complex, supporting cytoplasmic translation and positive regulation of translation. HPA describes broad tissue distribution with heart detection and low immune specificity. Its extensive literature and cancer-related Open Targets associations make it a well-characterized but biologically broad candidate.
- **Conclusion**: Established evidence supports EIF3C as a general translational-support hub rather than a tissue-specific marker. Its central position suggests that coordinated protein synthesis may help explain the module, but co-abundance does not establish translational activation. The hypothesis is that EIF3C links increased production of structural, trafficking, and quality-control proteins within shared active cells.

#### TKT

- **Related proteins** (co-abundance neighbors): FLNA (0.87), RAN (0.85), EIF3C (0.84), IQGAP1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transketolase. This gene encodes a thiamine-dependent enzyme which plays a role in the channeling of excess sugar phosphates to glycolysis in the pentose phosphate pathway. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: transketolase deficiency (0.663); neurodegenerative disease (0.409); cardiomyopathy (0.382); alcohol drinking (0.261); urolithiasis (0.259)
- **Europe PMC papers**: 3981
- **Why important**: TKT connects the adhesion-associated network to RAN, EIF3C, and IQGAP1 and provides a metabolic dimension through the non-oxidative pentose-phosphate pathway. HPA identifies tissue enhancement in bone marrow and cell-type enhancement across several metabolically active or epithelial populations, with blood-cell group enrichment. Its established function in sugar-phosphate channeling and its extensive literature, together with an Open Targets association with cardiomyopathy, make it relevant to cellular biosynthetic and stress demands.
- **Conclusion**: Established evidence supports TKT as a metabolic support enzyme that can provide carbon-flow flexibility for biosynthesis and redox-related demands. The module does not show that pentose-phosphate activity is enriched, because no GO or KEGG term passed global correction. The hypothesis is that TKT contributes metabolic support to cells simultaneously maintaining cytoskeletal remodeling, translation, and protein quality control.

## Module 6

**Tissue pair**: bone and heart  
**Genes (18)**: AIMP2, ARPC1B, ARL3, BCAM, MTHFD1, DYNC1I2, SORD, FKBP3, FKBP4, NES, PARVA, PDCD6IP, PGM2, PNP, RNH1, NANS, SNX6, SRSF7

### Function

No GO or KEGG term passed global correction, and STRING reports no supplementary functional enrichment. The module therefore should not be assigned a narrowly defined pathway on enrichment evidence alone. Its gene annotations and network structure instead suggest a heterogeneous intracellular maintenance module involving vesicle and endosomal trafficking, cytoskeletal organization, microtubule-based transport, carbohydrate and nucleotide metabolism, RNA handling, protein-complex assembly, and cell adhesion. PDCD6IP is the principal network hub and connects genes spanning these processes, while NANS, RNH1, ARL3, and DYNC1I2 form a connected intracellular transport and metabolic neighborhood. This is more consistent with coordinated cellular state or composition than with a single established biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only a minority gene is annotated as secreted, while the remainder are intracellular, membrane-associated, vesicular, cytoskeletal, or nuclear proteins. Most genes have low tissue specificity, although several show tissue enhancement in skeletal muscle, liver, blood vessel, retina, lymphoid tissue, or heart muscle. Most genes are cell-type enhanced, with recurring HPA signals in esophageal epithelial cells, trophoblast populations, megakaryocytes, and podocytes. Blood-cell specificity is generally low, with only limited signals involving basophils, eosinophils, MAIT T cells, or immune-related cell types. Thus, a simple blood contamination explanation is not strongly supported, but shared cellular composition or broadly expressed housekeeping-like programs could contribute to the bone-heart association. HPA protein detection is available for heart but not for a matching bone tissue, limiting direct tissue-level interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship is PGM2--PNP, supporting a known connection between carbohydrate-related metabolism and purine nucleoside salvage within the module. The hu.MAP evidence consists of (hu.MAP huMAP3_14624.1), in which ARPC1B and SORD occur among a larger complex, but only these module members are represented; this is partial complex overlap rather than evidence that the whole module is one complex. The absence of additional STRING or hu.MAP relationships indicates that most co-abundance links are not established physical interactions in these resources. Consequently, the network likely captures coordinated abundance, shared regulation, cell-state effects, or indirect biology rather than a single known protein complex.

**STRING interactions (score >= 0.7)**: 1 of 153 gene pairs: PGM2–PNP (0.84)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14624.1 (ARPC1B, SORD; 2/14)

### Novelty

The conserved bone-heart co-abundance pattern may be a novel tissue-pair association because most of its gene relationships are not represented as high-confidence STRING interactions or as a shared hu.MAP complex. However, database absence alone cannot establish novelty. The lack of globally significant GO or KEGG enrichment, the heterogeneous annotations, and the limited known interaction support argue against claiming discovery of a new coherent pathway. The strongest defensible novelty claim is that these genes show a previously unvalidated coordinated abundance pattern across bone and heart, which requires replication, cell-composition adjustment, and experimental testing.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular resilience and remodeling state present in cellular populations contributing to bone and heart samples. In this model, PDCD6IP-associated vesicle and membrane-trafficking processes are coordinated with ARL3 and DYNC1I2-dependent transport, RNH1-mediated control of ribonuclease activity and angiogenic signaling, PGM2 and PNP carbohydrate and purine metabolism, and actin or adhesion machinery represented by ARPC1B and related genes. This could support organelle transport, cytoskeletal remodeling, macromolecule turnover, and metabolic adaptation in cells present in both tissues. The hypothesis is not established by enrichment or interaction evidence and should be tested with cell-resolved expression, protein measurements, and perturbation of the hub-associated processes.

### Important genes

#### PDCD6IP

- **Related proteins** (co-abundance neighbors): ARL3 (0.90), PGM2 (0.88), RNH1 (0.87), DYNC1I2 (0.86), FKBP4 (0.86), SRSF7 (0.85), NANS (0.85), SORD (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 6 interacting protein. This gene encodes a protein that functions within the ESCRT pathway in the abscission stage of cytokinesis, in intralumenal endosomal vesicle formation, and in enveloped virus budding. Studies using mouse cells have shown that overexpression of this protein can block apoptosis. In addition, the product of this gene binds to the product of the PDCD6 gene, a protein required for apoptosis, in a calc…
- **Diseases (Open Targets)**: HIV infectious disease (0.463); anthrax infection (0.462); alcohol drinking (0.388); autosomal recessive primary microcephaly (0.386); microcephaly 29, primary, autosomal recessive (0.383)
- **Europe PMC papers**: 1668
- **Why important**: PDCD6IP is the most central node in the supplied co-abundance graph and connects transport, metabolic, RNA-associated, and cytoskeletal neighbors. Its established functions in ESCRT-dependent cytokinetic abscission, intralumenal vesicle formation, and enveloped virus budding make it a plausible organizer of a membrane-trafficking state. It has extensive literature relative to most module genes and disease associations involving infection and primary microcephaly.
- **Conclusion**: Established evidence supports PDCD6IP as a vesicle- and ESCRT-related intracellular protein and as the network hub. It is a strong candidate for coordinating the module, but a causal role in the bone-heart association remains a hypothesis.

#### NANS

- **Related proteins** (co-abundance neighbors): ARL3 (0.88), PGM2 (0.87), RNH1 (0.87), DYNC1I2 (0.86), PDCD6IP (0.85), NES (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-acetylneuraminate synthase. This gene encodes an enzyme that functions in the biosynthetic pathways of sialic acids. In vitro, the encoded protein uses N-acetylmannosamine 6-phosphate and mannose 6-phosphate as substrates to generate phosphorylated forms of N-acetylneuraminic acid (Neu5Ac) and 2-keto-3-deoxy-D-glycero-D-galacto-nononic acid (KDN), respectively; however, it exhibits much higher activity toward the Neu5Ac phos…
- **Diseases (Open Targets)**: spondyloepimetaphyseal dysplasia, Genevieve type (0.799); neurodegenerative disease (0.501); hereditary disease (0.192); neoplasm (0.067); mental disorder (0.056)
- **Europe PMC papers**: 2339
- **Why important**: NANS is one of the more highly connected module genes and links PDCD6IP with ARL3, PGM2, RNH1, DYNC1I2, and NES. Its established enzymatic role in sialic-acid biosynthesis provides a plausible metabolic component that could influence glycoprotein or membrane biology. It has substantial literature and a strong disease association with spondyloepimetaphyseal dysplasia, which is relevant to skeletal biology.
- **Conclusion**: Established evidence supports NANS as a sialic-acid biosynthetic enzyme with skeletal disease relevance. Its position in the module supports coordinated metabolic regulation, but does not establish that altered sialylation drives the shared bone-heart pattern.

#### RNH1

- **Related proteins** (co-abundance neighbors): PGM2 (0.90), PDCD6IP (0.87), NANS (0.87), ARPC1B (0.85), AIMP2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribonuclease/angiogenin inhibitor 1. Placental ribonuclease inhibitor (PRI) is a member of a family of proteinaceous cytoplasmic RNase inhibitors that occur in many tissues and bind to both intracellular and extracellular RNases (summarized by Lee et al., 1988 [PubMed 3219362]). In addition to control of intracellular RNases, the inhibitor may have a role in the regulation of angiogenin (MIM 105850). Ribonuclease inhibitor, of 50,000…
- **Diseases (Open Targets)**: encephalitis, acute, infection-induced, susceptibility to, 12 (0.327); hypothyroidism (0.250); Encephalopathy (0.185); psoriasis (0.129); cancer (0.082)
- **Europe PMC papers**: 994
- **Why important**: RNH1 is a highly connected intermediary linking PDCD6IP, NANS, PGM2, ARPC1B, and AIMP2. It is an intracellular ribonuclease inhibitor with reported roles in RNA stability, cell migration, angiogenesis, and regulation of Arp2/3-mediated actin nucleation. Its detection in heart and its connections to both actin-related and metabolic genes make it informative for interpreting the module as a cellular remodeling program. It has a substantial literature and disease associations involving encephalitis, encephalopathy, psoriasis, and cancer.
- **Conclusion**: Established evidence supports RNH1 in ribonuclease control and broader cytoskeletal or angiogenic regulation. Its central position makes it a plausible integrator, but the proposed role in bone-heart co-abundance is inferential.

#### PGM2

- **Related proteins** (co-abundance neighbors): RNH1 (0.90), PDCD6IP (0.88), NANS (0.87); STRING partners: PNP (0.84)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglucomutase 2. Enables phosphopentomutase activity. Predicted to be involved in carbohydrate metabolic process and deoxyribose phosphate catabolic process. Predicted to act upstream of or within glucose metabolic process. Located in extracellular exosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: intracranial subdural hematoma (0.216); Cerebral degeneration (0.190); malignant renal pelvis neoplasm (0.188); respiratory system disorder (0.188); lung adenocarcinoma (0.079)
- **Europe PMC papers**: 1479
- **Why important**: PGM2 connects the central PDCD6IP-NANS-RNH1 neighborhood to PNP through the only high-confidence STRING relationship in the module. Its annotated functions include carbohydrate metabolism, glycogen metabolism, and purine nucleoside salvage-related biology. The STRING-supported relationship gives PGM2 greater interpretive importance than its network position alone would provide, although its literature and disease evidence are less extensive than those of PNP or PDCD6IP.
- **Conclusion**: Established evidence supports PGM2 as a metabolic enzyme and supports its functional association with PNP in STRING. The module may coordinate carbohydrate and purine metabolism, but this remains a mechanistic interpretation rather than a demonstrated pathway.

#### PNP

- **Related proteins** (co-abundance neighbors): AIMP2 (0.84); STRING partners: PGM2 (0.84)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: purine nucleoside phosphorylase. This gene encodes an enzyme which reversibly catalyzes the phosphorolysis of purine nucleosides. The enzyme is trimeric, containing three identical subunits. Mutations which result in nucleoside phosphorylase deficiency result in defective T-cell (cell-mediated) immunity but can also affect B-cell immunity and antibody responses. Neurologic disorders may also be apparent in patients with immune de…
- **Diseases (Open Targets)**: purine nucleoside phosphorylase deficiency (0.815); severe combined immunodeficiency (0.632); combined immunodeficiency (0.468); T-B- severe combined immunodeficiency (0.462); T-B+ severe combined immunodeficiency (0.462)
- **Europe PMC papers**: 13792
- **Why important**: PNP is the partner of PGM2 in the only high-confidence STRING interaction and has a well-established role in purine nucleoside phosphorolysis. Its deficiency causes severe immune abnormalities, giving it a strong disease and mechanistic evidence base. Although it has limited direct connectivity in the co-abundance graph, its STRING relationship and extensive literature make it an important anchor for the nucleotide-metabolism interpretation.
- **Conclusion**: Established evidence supports PNP in purine salvage and immune-system biology, with a strong disease connection. Its involvement in this bone-heart module may indicate metabolic coordination or shared cellular composition, but the tissue-pair-specific interpretation is unproven.

#### ARPC1B

- **Related proteins** (co-abundance neighbors): RNH1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14624.1
- **Function (MyGene.info)**: actin related protein 2/3 complex subunit 1B. This gene encodes one of seven subunits of the human Arp2/3 protein complex. This subunit is a member of the SOP2 family of proteins and is most similar to the protein encoded by gene ARPC1A. The similarity between these two proteins suggests that they both may function as p41 subunit of the human Arp2/3 complex that has been implicated in the control of actin polymerization in cells. It is possib…
- **Diseases (Open Targets)**: platelet abnormalities with eosinophilia and immune-mediated inflammatory disease (0.771); combined immunodeficiency (0.429); autoimmune disorder of central nervous system (0.397); cutaneous leishmaniasis (0.370); immunodeficiency disease (0.346)
- **Europe PMC papers**: 1334
- **Why important**: ARPC1B is the module representative of the Arp2/3 actin-nucleation machinery and participates with SORD in the partial hu.MAP complex (hu.MAP huMAP3_14624.1). Its HPA profile is enhanced in lymphoid tissue and several myeloid or trophoblast-related cell types, and its disease associations include platelet, immune, and immunodeficiency phenotypes. Although it has limited network connectivity here, it provides a concrete cytoskeletal and cell-type-associated interpretation that complements RNH1 and PDCD6IP.
- **Conclusion**: Established evidence supports ARPC1B as an Arp2/3 complex subunit involved in actin polymerization and immune or platelet biology. Its presence does not prove that the complete module is an actin complex, but it supports cytoskeletal remodeling as one component of the hypothesis.

## Module 7

**Tissue pair**: bone and heart  
**Genes (17)**: ALDH3A2, APMAP, HSPA5, CKAP4, HSD17B4, DHRS7, FKBP2, EPHX1, ITGB1, MESD, PITRM1, RAB8A, RTN4, SCARB2, SERPINH1, TFRC, TXNDC5

### Function

The strongest interpretation is an endoplasmic-reticulum and endomembrane proteostasis module. The primary evidence is the globally significant enrichment for organelle subcompartments, endoplasmic reticulum, endoplasmic-reticulum membrane, and the nuclear-envelope–endoplasmic-reticulum membrane network (5 globally significant GO/KEGG terms, q_global 0.00401–0.027; see the table). The same genes include ER chaperones and folding factors such as HSPA5, SERPINH1, TXNDC5, FKBP2, CKAP4 and MESD, together with proteins involved in ER shape, membrane trafficking, endosomal or lysosomal handling, and lipid or aldehyde metabolism. RAB8A, TFRC and SCARB2 suggest a trafficking and recycling component, while ALDH3A2, EPHX1, DHRS7 and HSD17B4 suggest metabolic support. Thus, the module is best viewed as a conserved cellular infrastructure program for ER protein folding and membrane trafficking, with associated stress, quality-control and metabolic functions. The STRING enrichments (7 supplementary STRING terms; within-query FDR 0.00028–0.0255) support this interpretation but are supplementary rather than independent global enrichment evidence.

**Cell composition.** This is not predominantly a plasma-protein module: most annotated proteins are intracellular or membrane-associated, and several are localized to the ER, endosomes, lysosomes, mitochondria or peroxisomes. Nevertheless, the module is not tissue-specific in a simple bone–heart sense. HPA reports low tissue specificity for most genes, with tissue-enhanced signals particularly in liver and, for DHRS7, skeletal muscle. Many genes are cell-type enhanced, including signals in hepatocytes, neutrophils, monocytes, basophils, plasmacytoid dendritic cells, trophoblasts and other cell types. SCARB2, TFRC, RTN4, TXNDC5, RAB8A and other members have immune or blood-cell-associated HPA signals. TFRC is annotated as secreted to blood, and the module contains several genes with secretome annotations, but this does not make the whole module a plasma-protein module. The shared signal could therefore reflect broadly expressed cellular machinery, shared stromal or vascular components, or variable blood and immune cell content in the samples. Heart protein detection is mixed, and the absence of matching HPA bone tissue data limits tissue-level interpretation.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC organelle subcompartment | 0.00401 | ALDH3A2, CKAP4, DHRS7, EPHX1, FKBP2, HSPA5, RAB8A, RTN4, SCARB2 |
| GO:CC endoplasmic reticulum | 0.00648 | ALDH3A2, CKAP4, DHRS7, EPHX1, FKBP2, HSPA5, MESD, RTN4, SCARB2, SERPINH1, TXNDC5 |
| GO:CC endoplasmic reticulum membrane | 0.0191 | ALDH3A2, CKAP4, DHRS7, EPHX1, FKBP2, HSPA5, RTN4, SCARB2 |
| GO:CC endoplasmic reticulum subcompartment | 0.0191 | ALDH3A2, CKAP4, DHRS7, EPHX1, FKBP2, HSPA5, RTN4, SCARB2 |
| GO:CC nuclear outer membrane-endoplasmic reticulum membrane network | 0.027 | ALDH3A2, CKAP4, DHRS7, EPHX1, FKBP2, HSPA5, RTN4, SCARB2 |

### STRING and hu.MAP

STRING provides a small but coherent set of high-confidence known relationships. HSPA5 connects with SERPINH1 and TXNDC5, matching an ER folding and redox interpretation. ITGB1 connects with SCARB2 and TFRC, while RAB8A connects with TFRC; the SCARB2–TFRC relationship links endosomal or lysosomal trafficking to iron-receptor recycling. These relationships support parts of the module, but most module pairs are not represented as high-confidence STRING interactions. hu.MAP contributes two complexes with module-member pairs: EPHX1 with DHRS7 (hu.MAP huMAP3_15113.1), and TFRC with CKAP4 (hu.MAP huMAP3_10725.1). Because each complex contains only a small subset of the module and has many members outside it, these findings support partial physical or functional connections rather than a single established complex. Overall, the network appears to combine known ER, trafficking and membrane relationships with coordinated abundance relationships that are not yet fully represented in interaction databases.

**STRING interactions (score >= 0.7)**: 6 of 136 gene pairs: HSPA5–SERPINH1 (0.747); HSPA5–TXNDC5 (0.798); ITGB1–SCARB2 (0.719); ITGB1–TFRC (0.838); RAB8A–TFRC (0.891); SCARB2–TFRC (0.917)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Endoplasmic reticulum (FDR = 0.00028, 9 genes); Component Endoplasmic reticulum (FDR = 0.0026, 11 genes); Component Organelle subcompartment (FDR = 0.0026, 9 genes); Component Endoplasmic reticulum membrane (FDR = 0.0036, 8 genes); Component Endomembrane system (FDR = 0.0059, 14 genes); COMPARTMENTS Endoplasmic reticulum (FDR = 0.0096, 9 genes); Keyword Signal (FDR = 0.0255, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15113.1 (EPHX1, DHRS7; 2/53); huMAP3_10725.1 (TFRC, CKAP4; 2/59)

### Novelty

The module should not be called a wholly new molecular pathway. Its component functions and several relationships are well established, especially ER chaperoning by HSPA5, collagen-related folding by SERPINH1, thiol-disulfide processing by TXNDC5, receptor trafficking involving TFRC and RAB8A, and endolysosomal function involving SCARB2. However, the specific conserved co-abundance module shared by bone and heart may represent a new systems-level observation, because only part of its structure is captured by STRING and hu.MAP and the module combines ER proteostasis with trafficking and metabolic genes. That possibility remains provisional: database absence does not prove novelty, and the shared signal could arise from cell composition or broadly expressed housekeeping machinery. Independent replication, adjustment for blood and immune-cell content, and testing in purified bone and cardiac cell populations would be needed to establish novelty and tissue specificity.

**Hypothesis.** Hypothesis: in both bone and heart, a shared cellular-stress and secretory-load state coordinates ER folding, disulfide-bond processing, ER membrane organization, endosomal recycling and lysosomal delivery. HSPA5, SERPINH1, TXNDC5 and FKBP2 could maintain folding and quality control; CKAP4, RTN4 and MESD could organize or traffic membrane and receptor cargo; and the SCARB2, TFRC and RAB8A axis could couple endolysosomal processing with recycling. Metabolic genes such as ALDH3A2, EPHX1, DHRS7 and HSD17B4 may buffer lipid, aldehyde or related metabolic stress. This model predicts that the module will track secretory or proteotoxic stress and membrane trafficking activity, but does not by itself establish direct regulation or a common physical complex.

### Important genes

#### HSPA5

- **Related proteins** (co-abundance neighbors): SCARB2 (0.89), TXNDC5 (0.87), CKAP4 (0.85), HSD17B4 (0.82); STRING partners: SERPINH1 (0.747), TXNDC5 (0.798)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is the most connected module member and occurs in every primary GO term (5 globally significant GO/KEGG terms, q_global 0.00401–0.027; see the table) and every listed STRING enrichment (7 supplementary STRING terms; within-query FDR 0.00028–0.0255). Its established function as an ER HSP seventy chaperone and regulator of ER homeostasis gives the module a clear mechanistic anchor. It also has direct STRING support with SERPINH1 and TXNDC5 and the largest literature volume among the selected genes, together with disease associations involving stress, neurodegeneration and neoplasia.
- **Conclusion**: Established: HSPA5 is a central ER proteostasis factor and a strong candidate driver or marker of the module. Hypothesis: variation in HSPA5 abundance may organize the shared module response to secretory or proteotoxic stress in bone and heart.

#### SERPINH1

- **Related proteins** (co-abundance neighbors): TXNDC5 (0.91), RTN4 (0.85), TFRC (0.84), CKAP4 (0.82); STRING partners: HSPA5 (0.747)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family H member 1. This gene encodes a member of the serpin superfamily of serine proteinase inhibitors. The encoded protein is localized to the endoplasmic reticulum and plays a role in collagen biosynthesis as a collagen-specific molecular chaperone. Autoantibodies to the encoded protein have been found in patients with rheumatoid arthritis. Expression of this gene may be a marker for cancer, and nucleotide polymo…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 10 (0.714); preterm premature rupture of the membranes (0.559); coronary artery disorder (0.554); myocardial infarction (0.510); Abnormality of the skeletal system (0.474)
- **Europe PMC papers**: 2762
- **Why important**: SERPINH1 is highly connected and links the ER folding neighborhood to RTN4 and TFRC, while also connecting to HSPA5 and TXNDC5 in STRING. Its established role as a collagen-specific ER chaperone is especially relevant to bone matrix production and potentially to cardiac extracellular-matrix maintenance. It is represented in primary ER evidence (GO:CC endoplasmic reticulum; q_global = 0.00648) and in several supplementary STRING terms. Its disease associations include osteogenesis imperfecta, skeletal abnormality, coronary artery disorder and myocardial infarction.
- **Conclusion**: Established: SERPINH1 provides a biologically plausible bridge between ER proteostasis and collagen assembly. Hypothesis: it may help explain why this cellular module is conserved across matrix-producing bone cells and cardiac tissue, although the co-abundance data do not prove a shared collagen-specific mechanism.

#### SCARB2

- **Related proteins** (co-abundance neighbors): HSPA5 (0.89), PITRM1 (0.87), ALDH3A2 (0.86); STRING partners: ITGB1 (0.719), TFRC (0.917)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: scavenger receptor class B member 2. The protein encoded by this gene is a type III glycoprotein that is located primarily in limiting membranes of lysosomes and endosomes. Earlier studies in mice and rat suggested that this protein may participate in membrane transportation and the reorganization of endosomal/lysosomal compartment. The protein deficiency in mice was reported to impair cell membrane transport processes and cause pelv…
- **Diseases (Open Targets)**: action myoclonus-renal failure syndrome (0.779); progressive myoclonus epilepsy (0.647); hereditary disease (0.470); self-limited epilepsy with centrotemporal spikes (0.416); Unverricht-Lundborg syndrome (0.381)
- **Europe PMC papers**: 1732
- **Why important**: SCARB2 is a connected endolysosomal membrane protein and is present in all primary GO terms (5 globally significant GO/KEGG terms, q_global 0.00401–0.027; see the table). It connects to HSPA5, PITRM1 and ALDH3A2 in the module and has strong STRING links to TFRC and ITGB1. Its established functions include lysosomal and endosomal membrane transport, receptor-mediated endocytosis, autophagy and glycolipid catabolism. HPA also shows strong blood-cell-associated signals, making it important both mechanistically and as a possible cell-composition indicator.
- **Conclusion**: Established: SCARB2 supports an endolysosomal and trafficking arm of the module. Hypothesis: its association with the ER-centered genes may reflect coordinated cargo quality control or autophagic handling, but may alternatively reflect myeloid or other blood-cell admixture.

#### TFRC

- **Related proteins** (co-abundance neighbors): MESD (0.89), SERPINH1 (0.84), RAB8A (0.83); STRING partners: ITGB1 (0.838), RAB8A (0.891), SCARB2 (0.917)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes, Lysosomes; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_10725.1
- **Function (MyGene.info)**: transferrin receptor. This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: TFRC-related combined immunodeficiency (0.623); type 2 diabetes mellitus (0.518); mucopolysaccharidosis type 2 (0.490); diabetes mellitus (0.471); diabetic retinopathy (0.343)
- **Europe PMC papers**: 14164
- **Why important**: TFRC is a highly connected trafficking node linking MESD, SERPINH1 and RAB8A in the module. STRING independently supports links with ITGB1, RAB8A and SCARB2, and hu.MAP places TFRC with CKAP4 (hu.MAP huMAP3_10725.1). Its established function is receptor-mediated iron uptake, with roles in erythropoiesis, hypoxia response, intracellular iron homeostasis and endocytosis. Its blood and monocyte-associated HPA signals make it particularly informative for distinguishing a tissue-intrinsic signal from blood or immune-cell contribution.
- **Conclusion**: Established: TFRC is a plausible trafficking and iron-homeostasis interface within the module. Hypothesis: the shared module may respond to iron demand or hypoxic stress, but the TFRC signal could also be driven by erythroid or monocyte-related sample composition.

#### MESD

- **Related proteins** (co-abundance neighbors): TFRC (0.89), RTN4 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mesoderm development LRP chaperone. Predicted to enable low-density lipoprotein particle receptor binding activity. Involved in ossification and protein folding. Located in endoplasmic reticulum. Implicated in osteogenesis imperfecta type 20. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: osteogenesis imperfecta, type 20 (0.713); osteogenesis imperfecta (0.463); Abnormality of the skeletal system (0.416); osteogenesis imperfecta type 2 (0.370); Hernia of the abdominal wall (0.190)
- **Europe PMC papers**: 405
- **Why important**: MESD occupies a strategically informative position between TFRC and RTN4 in the co-abundance network and is represented in the primary ER term (GO:CC endoplasmic reticulum; q_global = 0.00648) and multiple supplementary ER and signal terms. Its established role as an ER chaperone for LDL-receptor-family proteins, with functions in protein folding, ossification and Wnt signaling, connects ER quality control to bone biology. Its disease associations include osteogenesis imperfecta and skeletal abnormalities, despite a more limited literature base than the major hubs.
- **Conclusion**: Established: MESD supplies a bone-relevant ER folding and receptor-maturation link. Hypothesis: MESD may couple matrix or Wnt-related receptor handling to the broader conserved module in bone and heart, but this proposed coupling requires direct functional testing.
