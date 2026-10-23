# Conserved co-abundance modules: brain and skin

## Module 0

**Tissue pair**: brain and skin  
**Genes (33)**: BZW2, BUB1B, CACNG6, DHX9, EIF3C, HDAC1, HNRNPL, HNRNPR, IGF2BP3, KIF2C, LYAR, MATR3, METTL14, ALPL, PYM1, CAD, RNF2, RPL12, RPL3, RPL6, SF3A1, SF3B3, SMARCA4, SNRNP40, SPIN1, SRRT, QARS1, TCERG1, TRIM27, UTP14A, VASP, WASF2, WDR43

### Function

This is an intracellular RNA and gene-expression module. The strongest primary evidence is for ribonucleoprotein complexes (GO:CC ribonucleoprotein complex; q_global = 0.000205), RNA binding (GO:MF RNA binding; q_global = 0.000433), nucleic-acid binding (GO:MF nucleic acid binding; q_global = 0.000663), gene expression (GO:BP gene expression; q_global = 0.00441), RNA metabolism (GO:BP RNA metabolic process; q_global = 0.0219), and regulation of gene expression (GO:BP regulation of gene expression; q_global = 0.0363). Translation and protein biosynthesis are also supported (GO:BP translation; q_global = 0.0281) (GO:BP protein biosynthetic process; q_global = 0.0281), together with a cytosolic large ribosomal-subunit signal (GO:CC cytosolic large ribosomal subunit; q_global = 0.0169). The gene set therefore combines several related processes: pre-mRNA handling and splicing, RNA binding and surveillance, ribosome biogenesis, translation, and transcriptional or chromatin control. The network contains recognizable functional cores, including ribosomal proteins, spliceosomal components, heterogeneous nuclear ribonucleoproteins, and RNA-processing factors. Its shared brain-skin behavior is best interpreted as conservation of a general intracellular gene-expression program rather than as evidence for a tissue-specific neuronal or epidermal pathway.

**Cell composition.** The module is overwhelmingly composed of intracellular, nuclear, nucleolar, cytosolic, or membrane-associated proteins rather than plasma or secreted proteins. HPA indicates low tissue specificity for most genes, broad protein detection in both brain and skin, and only a single secreted-gene annotation. Blood-cell specificity is generally low, although isolated genes show immune-cell or progenitor-cell enrichment. The presence of cell-type-enhanced genes in neural, epithelial, germ-cell, stromal, and progenitor populations suggests that shared cellular programs may contribute to the signal, but the HPA profile does not support a predominantly blood-derived or plasma-protein module. The broad expression pattern is consistent with a housekeeping-like RNA-processing and protein-production program, while selected genes may reflect proliferative or differentiating cell populations.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC ribonucleoprotein complex | 0.000205 | DHX9, EIF3C, HNRNPL, HNRNPR, RPL12, RPL3, RPL6, SF3A1, SF3B3, SNRNP40, SRRT, UTP14A, WDR43 |
| GO:MF RNA binding | 0.000433 | DHX9, EIF3C, HNRNPL, HNRNPR, IGF2BP3, LYAR, MATR3, METTL14, PYM1, RPL12, RPL3, RPL6, SF3A1, SF3B3, SMARCA4, SNRNP40, SRRT, TCERG1, UTP14A, WDR43 |
| GO:MF nucleic acid binding | 0.000663 | DHX9, EIF3C, HDAC1, HNRNPL, HNRNPR, IGF2BP3, KIF2C, LYAR, MATR3, METTL14, PYM1, RPL12, RPL3, RPL6, SF3A1, SF3B3, SMARCA4, SNRNP40, SRRT, TCERG1, TRIM27, UTP14A, WDR43 |
| GO:BP gene expression | 0.00441 | BZW2, DHX9, EIF3C, HDAC1, HNRNPL, HNRNPR, IGF2BP3, LYAR, MATR3, METTL14, PYM1, QARS1, RNF2, RPL12, RPL3, RPL6, SF3A1, SF3B3, SMARCA4, SNRNP40, SPIN1, SRRT, TCERG1, TRIM27, UTP14A, WDR43 |
| GO:BP macromolecule biosynthetic process | 0.0118 | BZW2, DHX9, EIF3C, HDAC1, HNRNPL, HNRNPR, IGF2BP3, LYAR, MATR3, METTL14, PYM1, QARS1, RNF2, RPL12, RPL3, RPL6, SF3A1, SF3B3, SMARCA4, SNRNP40, SPIN1, SRRT, TCERG1, TRIM27, UTP14A, WDR43 |
| GO:CC cytosolic large ribosomal subunit | 0.0169 | RPL12, RPL3, RPL6 |
| GO:BP RNA metabolic process | 0.0219 | DHX9, HDAC1, HNRNPL, HNRNPR, IGF2BP3, LYAR, METTL14, PYM1, QARS1, RNF2, RPL6, SF3A1, SF3B3, SMARCA4, SNRNP40, SPIN1, SRRT, TCERG1, TRIM27, UTP14A, WDR43 |
| GO:BP negative regulation of RNA metabolic process | 0.0265 | DHX9, HDAC1, HNRNPL, IGF2BP3, LYAR, METTL14, QARS1, RNF2, SMARCA4, TCERG1, TRIM27 |
| GO:BP translation | 0.0281 | BZW2, DHX9, EIF3C, IGF2BP3, METTL14, PYM1, QARS1, RPL12, RPL3, RPL6 |
| GO:BP protein biosynthetic process | 0.0281 | BZW2, DHX9, EIF3C, IGF2BP3, METTL14, PYM1, QARS1, RPL12, RPL3, RPL6 |
| GO:BP regulation of gene expression | 0.0363 | BZW2, DHX9, EIF3C, HDAC1, HNRNPL, IGF2BP3, LYAR, MATR3, METTL14, PYM1, QARS1, RNF2, RPL6, SF3B3, SMARCA4, SPIN1, SRRT, TCERG1, TRIM27, WDR43 |

### STRING and hu.MAP

STRING supports established relationships within the module. Examples include the ribosomal relationships among RPL3, RPL6, and RPL12; the spliceosomal relationships among SF3A1, SF3B3, SNRNP40, and TCERG1; and RNA-associated relationships linking DHX9 with HNRNPL, HNRNPR, MATR3, SRRT, and TCERG1. STRING also connects HDAC1 with SMARCA4, RNF2, and TRIM27, and connects IGF2BP3 with METTL14 and MATR3. These relationships show that substantial parts of the module recapitulate known molecular biology. The supplementary STRING enrichments (15 supplementary STRING terms; within-query FDR 4.18e-05–0.0047) reinforce RNA metabolism, ribonucleoprotein complexes, splicing, translation, and nuclear localization, but they are not additional globally corrected enrichment claims. hu.MAP independently identifies known hnRNP and nuclear RNA-associated complexes containing HNRNPL, HNRNPR, and MATR3 (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1), spliceosomal complexes containing SF3A1, SF3B3, and SNRNP40 (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_04549.1) (hu.MAP huMAP3_06511.1), and a broader RNA-processing complex containing PYM1 and SRRT (hu.MAP huMAP3_11073.1). Thus, the module is not an unexplained collection of genes: much of its structure reflects known complexes and established interactions.

**STRING interactions (score >= 0.7)**: 36 of 528 gene pairs: BUB1B–KIF2C (0.991); BUB1B–RNF2 (0.72); DHX9–HNRNPL (0.901); DHX9–HNRNPR (0.909); DHX9–MATR3 (0.786); DHX9–RPL6 (0.958); DHX9–SF3B3 (0.73); DHX9–SRRT (0.92); DHX9–TCERG1 (0.841); HDAC1–HNRNPL (0.775); HDAC1–RNF2 (0.868); HDAC1–SMARCA4 (0.989); HDAC1–TRIM27 (0.803); HNRNPL–HNRNPR (0.961); HNRNPL–MATR3 (0.757); HNRNPL–SRRT (0.725); HNRNPR–MATR3 (0.714); IGF2BP3–MATR3 (0.735); IGF2BP3–METTL14 (0.829); LYAR–RPL12 (0.806); LYAR–RPL3 (0.833); LYAR–RPL6 (0.836); LYAR–WDR43 (0.718); QARS1–RPL3 (0.749); RPL12–RPL3 (0.999); RPL12–RPL6 (0.999); RPL3–RPL6 (0.999); SF3A1–SF3B3 (0.999); SF3A1–SNRNP40 (0.94); SF3A1–TCERG1 (0.992); SF3B3–SNRNP40 (0.852); SF3B3–TCERG1 (0.977); SNRNP40–TCERG1 (0.973); SRRT–TCERG1 (0.839); UTP14A–WDR43 (0.996); VASP–WASF2 (0.792)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Metabolism of RNA (FDR = 4.18e-05, 15 genes); COMPARTMENTS Nuclear lumen (FDR = 6.17e-05, 20 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 6.52e-05, 12 genes); Keyword Ubl conjugation (FDR = 9.91e-05, 20 genes); Keyword Isopeptide bond (FDR = 9.91e-05, 18 genes); Function RNA binding (FDR = 0.00019, 20 genes); Function Nucleic acid binding (FDR = 0.0002, 23 genes); Process Gene expression (FDR = 0.00023, 21 genes); Component Ribonucleoprotein complex (FDR = 0.0008, 12 genes); RCTM mRNA Splicing - Major Pathway (FDR = 0.00083, 8 genes); RCTM Processing of Capped Intron-Containing Pre-mRNA (FDR = 0.0011, 9 genes); RCTM Formation of a pool of free 40S subunits (FDR = 0.0022, 4 genes); PMID (2020) Bioinformatics Analysis for Multiple Gene Expression Profiles in Sepsis. (FDR = 0.0028, 8 genes); RCTM L13a-mediated translational silencing of Ceruloplasmin expression (FDR = 0.0043, 4 genes); RCTM GTP hydrolysis and joining of the 60S ribosomal subunit (FDR = 0.0047, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07581.1 (HNRNPR, HNRNPL, MATR3; 3/21); huMAP3_10625.1 (HNRNPR, HNRNPL, MATR3; 3/57); huMAP3_08980.1 (SF3B3, SF3A1, SNRNP40; 3/97); huMAP3_05721.1 (HNRNPL, MATR3; 2/6); huMAP3_07225.1 (HNRNPR, HNRNPL; 2/7); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09654.1 (HNRNPR, HNRNPL; 2/13); huMAP3_10659.1 (HNRNPR, HNRNPL; 2/28); huMAP3_04549.1 (SF3B3, SF3A1; 2/52); huMAP3_11073.1 (PYM1, SRRT; 2/67); huMAP3_06511.1 (SF3B3, SF3A1; 2/79)

### Novelty

The individual biological relationships represented here are not new: ribosomal, spliceosomal, hnRNP, RNA-helicase, chromatin, and RNA-modification functions are already established by STRING, hu.MAP, and the gene annotations. Absence of a particular pair from either resource would not prove novelty, because database coverage, assay context, and confidence thresholds are incomplete. The potentially novel aspect is the reproducible co-abundance of these established RNA-processing and translation components as one conserved module across brain and skin. The fact sheet alone does not establish whether this cross-tissue module has previously been reported, so it should be described as a potentially informative conserved organization rather than claimed as a wholly new molecular complex or pathway.

**Hypothesis.** Hypothesis: this module represents a coordinated intracellular gene-expression program that couples RNA production and processing to ribosome assembly and translation. In this model, spliceosomal and hnRNP factors process transcripts, DHX9 and related RNA-binding proteins help remodel or regulate RNA, METTL14 and IGF2BP3 influence transcript modification or handling, ribosomal and initiation factors support protein production, and chromatin regulators such as HDAC1, SMARCA4, RNF2, and TRIM27 tune transcriptional access. The same program could be co-abundant in brain and skin because both tissues require sustained RNA quality control, differentiation-related gene regulation, and protein synthesis. This is a mechanistic model, not proof of direct physical cooperation among every module member. It should be tested with cell-type-resolved data, perturbation experiments, and measurements of splicing, RNA modification, ribosome production, and translation.

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): RPL3 (0.81); STRING partners: HNRNPL (0.901), HNRNPR (0.909), MATR3 (0.786), RPL6 (0.958), SF3B3 (0.73), SRRT (0.92), TCERG1 (0.841)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is a central RNA-associated connector in the module and has established STRING relationships with several hnRNP, spliceosomal, ribosomal, and RNA-effector proteins. It is an RNA helicase with roles in unwinding RNA-containing structures, alternative splicing, transcriptional regulation, and interferon-related gene expression. It appears across nearly all of the primary RNA, gene-expression, and translation terms (10 globally significant GO/KEGG terms, q_global 0.000205–0.0363; see the table) and has a substantial disease and literature record.
- **Conclusion**: Established evidence supports DHX9 as a core RNA-remodeling and gene-expression component of the module. Its central position makes it a plausible integrator of RNA processing and translation, but the co-abundance data do not demonstrate that DHX9 mechanistically drives the shared brain-skin module.

#### SF3A1

- **Related proteins** (co-abundance neighbors): ALPL (0.81), TCERG1 (0.81), RPL3 (0.80); STRING partners: SF3B3 (0.999), SNRNP40 (0.94), TCERG1 (0.992)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_04549.1, huMAP3_06511.1
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 is a spliceosomal factor with a prominent position in the module’s known interaction and complex structure. It has strong STRING relationships with SF3B3, SNRNP40, and TCERG1, and occurs in hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_04549.1) (hu.MAP huMAP3_06511.1). Its annotation directly supports spliceosome assembly, splice-site recognition, and pre-mRNA splicing, while the primary enrichments place it within the ribonucleoprotein, RNA-binding, and gene-expression signals (6 globally significant GO/KEGG terms, q_global 0.000205–0.0219; see the table).
- **Conclusion**: Established evidence identifies SF3A1 as a bona fide spliceosomal anchor within the module. Its conservation between brain and skin may reflect shared dependence on regulated pre-mRNA processing, but tissue-specific splice targets remain a hypothesis.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): RPL3 (0.84), IGF2BP3 (0.82); STRING partners: DHX9 (0.901), HDAC1 (0.775), HNRNPR (0.961), MATR3 (0.757), SRRT (0.725)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_07581.1, huMAP3_10625.1, huMAP3_05721.1, huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_10659.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is a highly connected RNA-binding and nuclear RNA-processing component. It interacts with DHX9, HNRNPR, MATR3, HDAC1, and SRRT in STRING and appears repeatedly in hu.MAP hnRNP complexes (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1). Its established functions include packaging and processing of messenger RNA and regulation of alternative splicing. It contributes to almost every major primary enrichment category involving RNA and gene expression (8 globally significant GO/KEGG terms, q_global 0.000205–0.0363; see the table).
- **Conclusion**: Established evidence supports HNRNPL as a central organizer of nuclear RNA handling and splicing-related interactions. It is a strong candidate for linking the module’s network structure to transcript processing, although the data do not identify which transcripts are functionally affected in brain or skin.

#### RPL3

- **Related proteins** (co-abundance neighbors): HDAC1 (0.86), RPL6 (0.86), SF3B3 (0.84), HNRNPL (0.84), EIF3C (0.84), DHX9 (0.81), RPL12 (0.81), QARS1 (0.81), SF3A1 (0.80); STRING partners: LYAR (0.833), QARS1 (0.749), RPL12 (0.999), RPL6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Cytosol; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein L3. Ribosomes, the complexes that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L3P family of ribosomal proteins and it is located in the cytoplasm. The p…
- **Diseases (Open Targets)**: Duchenne muscular dystrophy (0.506); Orthomyxoviridae infectious disease (0.463); cystic fibrosis (0.389); neuromuscular disease caused by qualitative or quantitative defects of dystrophin (0.323); inflammatory bowel disease (0.308)
- **Europe PMC papers**: 2316
- **Why important**: RPL3 is among the most central genes in the co-abundance subgraph and is embedded in a strongly connected ribosomal cluster with RPL6 and RPL12. It is a component of the large ribosomal subunit and contributes to the primary ribonucleoprotein and translation signals (7 globally significant GO/KEGG terms, q_global 0.000205–0.0281; see the table). Its extensive literature and disease-association record reflect the broad importance of ribosome function.
- **Conclusion**: Established evidence supports RPL3 as the module’s translation-associated structural component. Its presence argues that the module extends beyond splicing into protein production, but it is more likely a readout of ribosome abundance or activity than a brain-skin-specific regulatory driver.

#### METTL14

- **Related proteins** (co-abundance neighbors): SPIN1 (0.81); STRING partners: IGF2BP3 (0.829)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methyltransferase 14, N6-adenosine-methyltransferase non-catalytic subunit. Enables mRNA binding activity. Contributes to mRNA (2'-O-methyladenosine-N6-)-methyltransferase activity. Involved in mRNA metabolic process; negative regulation of hematopoietic progenitor cell differentiation; and positive regulation of translation. Located in nucleoplasm. Part of RNA N6-methyladenosine methyltransferase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.552); clavicle fracture (0.170); shoulder fracture (0.170); liver disorder (0.118); neoplasm (0.118)
- **Europe PMC papers**: 9036
- **Why important**: METTL14 is an RNA-binding component of the mRNA modification machinery and is connected within the module to IGF2BP3 and SPIN1. It is represented in the primary RNA-binding, RNA-metabolism, gene-expression, and translation terms (9 globally significant GO/KEGG terms, q_global 0.000433–0.0363; see the table). Its established roles in mRNA modification, processing, translation, and developmental or disease biology make it a biologically informative bridge between RNA processing and post-transcriptional regulation.
- **Conclusion**: Established evidence supports METTL14 as a regulatory RNA-processing component rather than a generic structural housekeeping protein. A plausible interpretation is that it helps coordinate transcript modification with RNA fate, but the module does not establish altered RNA modification as the cause of the brain-skin co-abundance pattern.

## Module 1

**Tissue pair**: brain and skin  
**Genes (43)**: AAK1, ADD2, AGRN, ANK3, BORCS5, CEP97, C8orf82, C15orf40, CORO1A, EPN2, FOXJ3, RAP1GDS1, GMPR2, GNA13, HDGFL3, HERC1, ITPR2, CSNK1E, CAMK2G, PRPSAP2, LGALSL, LYRM4, MAP1A, MAP1B, RHOT1, MAP2K4, MTX3, NADK2, NMRAL1, OSBPL1A, PCCA, HSPG2, PIP4K2A, PPM1A, PRUNE1, PTBP2, RNF123, LARS2, TLN2, TMEM65, UBR2, VPS50, ZZEF1

### Function

The module does not support a single narrowly defined pathway: no GO/KEGG term passed global correction, and STRING reports no supplementary functional enrichment. Its architecture instead suggests a composite cell-organization program linking membrane and cytoskeletal organization, intracellular trafficking, calcium signaling, mitochondrial metabolism, and stress-responsive signaling. ANK3 occupies the strongest network position and connects membrane organization with MAP1A, HSPG2, RNF123, ZZEF1, and VPS50. The module also contains a coherent microtubule and neuronal-structure component through MAP1A, MAP1B, HDGFL3, and PTBP2; an endocytic and vesicle-trafficking component through AAK1, EPN2, BORCS5, and VPS50; and calcium or signaling components involving ITPR2, CAMK2G, MAP2K4, PPM1A, and RAP1GDS1. PCCA, LARS2, NADK2, RHOT1, MTX3, and LYRM4 provide mitochondrial or metabolic context. The appropriate interpretation is therefore a conserved cellular infrastructure module rather than a proven single biochemical pathway.

**Cell composition.** The module is not predominantly composed of secreted or extracellular proteins: only AGRN and HSPG2 are annotated as secreted to the extracellular matrix. The HPA profile is mixed. Many genes have low tissue specificity, while others show enhancement in brain, bone marrow, liver, retina, blood vessel, skin, or other tissues. There is a notable immune and blood-cell signal, particularly for neutrophils, basophils, eosinophils, platelets, and related cell types; CORO1A is especially consistent with hematopoietic or immune-cell biology. At the same time, oligodendrocyte enrichment is frequent, and several genes have neuronal, glial, membrane, or cytoskeletal annotations. Thus, the shared brain-skin pattern could reflect conserved programs in resident cells, shared vascular or stromal components, or sample-associated blood and immune cells. It should not be interpreted as a brain-skin-specific program without cell-composition adjustment. Protein detection in both tissues is broad for much of the module, but several strongly brain-associated genes are not detected in skin, which further argues for a mixed cellular or compositional explanation rather than uniform expression by the same cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited set of high-confidence known relationships rather than a densely documented interaction system. The strongest links include AGRN-HSPG2, ADD2-ANK3, ANK3-ITPR2, MAP2K4-PPM1A, RAP1GDS1-RHOT1, and PIP4K2A-TLN2, with AAK1-EPN2 also supported. These links independently reinforce extracellular-matrix and membrane anchoring, calcium-linked signaling, stress-kinase regulation, mitochondrial positioning, and phosphoinositide or adhesion biology. hu.MAP provides repeated support for the MAP1A-MAP1B pair across complexes (hu.MAP huMAP3_10774.1), (hu.MAP huMAP3_10983.1), (hu.MAP huMAP3_09907.1), and (hu.MAP huMAP3_10305.1), and supports the AAK1-EPN2 pair in an extensive trafficking complex (hu.MAP huMAP3_12394.1). The PCCA-LARS2 association appears in a mitochondrial metabolic complex (hu.MAP huMAP3_13468.1). Because most module pairs are not represented by high-confidence STRING links and the hu.MAP complexes capture only subsets of the module, the network should be viewed as a co-abundance organization containing several known molecular substructures, not as one experimentally established physical complex.

**STRING interactions (score >= 0.7)**: 7 of 903 gene pairs: AAK1–EPN2 (0.743); ADD2–ANK3 (0.96); AGRN–HSPG2 (0.993); ANK3–ITPR2 (0.922); MAP2K4–PPM1A (0.946); PIP4K2A–TLN2 (0.729); RAP1GDS1–RHOT1 (0.833)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10774.1 (MAP1B, MAP1A; 2/4); huMAP3_10983.1 (MAP1B, MAP1A; 2/4); huMAP3_09907.1 (MAP1B, MAP1A; 2/5); huMAP3_10305.1 (MAP1B, MAP1A; 2/5); huMAP3_12394.1 (EPN2, AAK1; 2/98); huMAP3_13468.1 (PCCA, LARS2; 2/99)

### Novelty

The module is potentially novel as a conserved brain-skin co-abundance pattern, but the data do not establish novelty of the individual molecular interactions. Several component relationships are already known through STRING, including cytoskeletal, extracellular-matrix, signaling, mitochondrial, and trafficking links, while hu.MAP independently recovers MAP1A-MAP1B, AAK1-EPN2, and PCCA-LARS2-containing complexes. The absence of a single matching STRING or hu.MAP entity is therefore compatible with a new cross-tissue co-abundance arrangement, but it is not proof of a new biological mechanism. The absence of globally corrected GO/KEGG enrichment also does not invalidate the module; it indicates that the genes are functionally heterogeneous or that the signal is too distributed for pathway-level enrichment. A stronger novelty claim would require replication in independent brain and skin cohorts, control for cell-type and blood composition, and comparison with published cross-tissue co-expression modules.

**Hypothesis.** Hypothesis: this conserved module represents a cell-architecture and organelle-coordination program that couples membrane-cytoskeleton scaffolding to endocytic recycling, calcium release, mitochondrial positioning, and stress signaling. In neural or glial cells, MAP1A and MAP1B may organize microtubule-dependent structure, while ANK3 and ADD2 connect membrane proteins to the spectrin-actin system. AAK1 and EPN2 may coordinate receptor internalization and vesicle handling, and ITPR2 may provide calcium signals that influence cytoskeletal remodeling and mitochondrial behavior. AGRN and HSPG2 could connect this intracellular program to extracellular-matrix and cell-surface organization. In skin, vascular, stromal, or blood-associated cells, the same co-abundance pattern may be redeployed for adhesion, migration, barrier organization, immune-cell trafficking, or tissue repair. This is a mechanistic model, not an experimentally demonstrated pathway; it predicts that perturbing membrane trafficking or calcium handling should alter cytoskeletal organization and mitochondrial distribution in relevant brain- and skin-derived cell types.

### Important genes

#### ANK3

- **Related proteins** (co-abundance neighbors): HSPG2 (0.86), MAP1A (0.83), RNF123 (0.82), ZZEF1 (0.82), VPS50 (0.81); STRING partners: ADD2 (0.96), ITPR2 (0.922)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ankyrin 3. Ankyrins are a family of proteins that are believed to link the integral membrane proteins to the underlying spectrin-actin cytoskeleton and play key roles in activities such as cell motility, activation, proliferation, contact, and the maintenance of specialized membrane domains. Multiple isoforms of ankyrin with different affinities for various target proteins are expressed in a tissue-specific,…
- **Diseases (Open Targets)**: intellectual disability-hypotonia-spasticity-sleep disorder syndrome (0.726); bipolar disorder (0.536); hereditary disease (0.472); smoking initiation (0.411); smoking cessation (0.391)
- **Europe PMC papers**: 2941
- **Why important**: ANK3 is the central network hub by weighted position and links HSPG2, MAP1A, RNF123, ZZEF1, and VPS50. Its established function is to connect integral membrane proteins with the spectrin-actin cytoskeleton and maintain specialized membrane domains. HPA detects it in both brain and skin, with cell-type enhancement including oligodendrocytes, and the ADD2-ANK3 and ANK3-ITPR2 relationships are supported by STRING. Its disease associations include neurodevelopmental and psychiatric phenotypes, and its literature support is extensive.
- **Conclusion**: Established evidence: ANK3 is the strongest structural connector in this module and has a well-supported membrane-cytoskeleton role. Hypothesis: ANK3 may organize the interface through which calcium signaling, vesicle recycling, and extracellular-matrix cues are integrated across brain and skin cell populations.

#### MAP1A

- **Related proteins** (co-abundance neighbors): ANK3 (0.83), RAP1GDS1 (0.82), TLN2 (0.82), AAK1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_10774.1, huMAP3_10983.1, huMAP3_09907.1, huMAP3_10305.1
- **Function (MyGene.info)**: microtubule associated protein 1A. This gene encodes a protein that belongs to the microtubule-associated protein family. The proteins of this family are thought to be involved in microtubule assembly, which is an essential step in neurogenesis. The product of this gene is a precursor polypeptide that presumably undergoes proteolytic processing to generate the final MAP1A heavy chain and LC2 light chain. Expression of this gene is …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.340); venous thromboembolism (0.238); hereditary disease (0.118); autism spectrum disorder (0.094); urinary bladder cancer (0.075)
- **Europe PMC papers**: 1240
- **Why important**: MAP1A is tissue enriched in brain, is associated with microtubule assembly, axonogenesis, dendrite development, and regulation of microtubule dynamics, and occupies a prominent module position connected to ANK3, RAP1GDS1, TLN2, and AAK1. Together with MAP1B, it is repeatedly recovered in hu.MAP complexes (hu.MAP huMAP3_10774.1), (hu.MAP huMAP3_10983.1), (hu.MAP huMAP3_09907.1), and (hu.MAP huMAP3_10305.1). Its disease associations include neurodevelopmental and autism-related phenotypes, and it has substantial literature support.
- **Conclusion**: Established evidence: MAP1A supplies a strong neuronal microtubule interpretation and is supported by several independent complex records. Hypothesis: MAP1A may be the principal brain-linked structural component of a broader module that is repurposed for membrane trafficking or adhesion in non-neural cells.

#### ITPR2

- **Related proteins** (co-abundance neighbors): HDGFL3 (0.90), PCCA (0.81), BORCS5 (0.81), GMPR2 (0.80); STRING partners: ANK3 (0.922)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum, Mid piece; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inositol 1,4,5-trisphosphate receptor type 2. The protein encoded by this gene belongs to the inositol 1,4,5-triphosphate receptor family, whose members are second messenger intracellular calcium release channels. These proteins mediate a rise in cytoplasmic calcium in response to receptor activated production of inositol triphosphate. Inositol triphosphate receptor-mediated signaling is involved in many processes including cell migration, ce…
- **Diseases (Open Targets)**: isolated anhidrosis with normal sweat glands (0.547); alcohol drinking (0.428); atrial fibrillation (0.394); open-angle glaucoma (0.365); familial hypercholesterolemia (0.333)
- **Europe PMC papers**: 1988
- **Why important**: ITPR2 is a high-position network node connected to HDGFL3, PCCA, BORCS5, GMPR2, and ANK3. Its established function is as an intracellular calcium-release channel activated by inositol trisphosphate, with roles in calcium-mediated signaling, ion transport, migration, division, and neuronal signaling. It is detected in brain and skin and has cell-type enhancement in microglia and several ion-secreting epithelial populations. Its disease associations include anhidrosis, atrial fibrillation, and glaucoma, and it has substantial literature support.
- **Conclusion**: Established evidence: ITPR2 provides a credible calcium-signaling axis within an otherwise structurally and metabolically mixed module. Hypothesis: ITPR2 may couple receptor or adhesion signals to cytoskeletal remodeling and mitochondrial responses, helping explain conservation across neural, epithelial, and vascular contexts.

#### AAK1

- **Related proteins** (co-abundance neighbors): BORCS5 (0.83), MAP1A (0.81); STRING partners: EPN2 (0.743)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Plasma membrane; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: AP2 associated kinase 1. This gene encodes a member of the SNF1 subfamily of serine/threonine protein kinases. Adaptor-related protein complex 2 (AP-2 complexes) functions during receptor-mediated endocytosis to trigger clathrin assembly, interact with membrane-bound receptors, and recruit encodytic accessory factors. The encoded protein interacts with and phosphorylates a subunit of the AP-2 complex, which promotes bindi…
- **Diseases (Open Targets)**: gout (0.466); Parkinson disease (0.265); Alzheimer disease (0.264); neurodegenerative disease (0.261); lysosomal storage disease (0.259)
- **Europe PMC papers**: 1532
- **Why important**: AAK1 connects BORCS5 and MAP1A, is supported by the STRING AAK1-EPN2 relationship, and is included with EPN2 in the hu.MAP trafficking complex (hu.MAP huMAP3_12394.1). Its established function is phosphorylation associated with AP two complexes, clathrin assembly, receptor sorting, and clathrin-dependent endocytosis. It is detected in brain and has disease associations involving neurodegeneration and lysosomal storage, with substantial literature support.
- **Conclusion**: Established evidence: AAK1 is a strong candidate for the module's endocytic and receptor-trafficking component. Hypothesis: AAK1-dependent trafficking may connect membrane-domain organization through ANK3 with microtubule transport through MAP1A and lysosome positioning through BORCS5.

#### PCCA

- **Related proteins** (co-abundance neighbors): OSBPL1A (0.87), LGALSL (0.81), ITPR2 (0.81), PPM1A (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: propionyl-CoA carboxylase subunit alpha. The protein encoded by this gene is the alpha subunit of the heterodimeric mitochondrial enzyme Propionyl-CoA carboxylase. PCCA encodes the biotin-binding region of this enzyme. Mutations in either PCCA or PCCB (encoding the beta subunit) lead to an enzyme deficiency resulting in propionic acidemia. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by…
- **Diseases (Open Targets)**: propionic acidemia (0.853); hereditary disease (0.487); dilated cardiomyopathy (0.370); neurodegenerative disease (0.357); pontocerebellar hypoplasia type 2D (0.340)
- **Europe PMC papers**: 2633
- **Why important**: PCCA occupies a high network position and connects OSBPL1A, LGALSL, ITPR2, and PPM1A. Its established function is as the biotin-binding alpha subunit of mitochondrial propionyl-CoA carboxylase, linking the module to branched-chain amino-acid and short-chain fatty-acid catabolism. PCCA is detected in brain and skin and is paired with LARS2 in the hu.MAP mitochondrial complex (hu.MAP huMAP3_13468.1). Propionic acidemia is a well-established disease association, and the gene has substantial literature support.
- **Conclusion**: Established evidence: PCCA contributes a genuine mitochondrial metabolic component and is not merely a generic network connector. Hypothesis: mitochondrial substrate processing may be coordinated with calcium signaling and cytoskeletal transport in this conserved module, although the co-abundance data do not demonstrate direct metabolic regulation.

## Module 2

**Tissue pair**: brain and skin  
**Genes (32)**: AAMDC, ACAD8, ADD3, ANKIB1, APC, ARHGEF6, ARHGEF7, BIN1, CASK, DMAP1, DPYSL5, EXOC6, EXOC8, FLOT1, TUBGCP3, GIT1, HMOX2, IRS2, LIPA, PRNP, RAB18, RAB23, RAB34, ARHGAP12, POLR3A, SIRT3, STX6, TATDN1, TRAPPC11, TRIM3, UNC119B, UBAP1

### Function

The module most strongly represents intracellular transport and establishment of protein localization, with a prominent plasma-membrane-bound cell-projection component, supported by the globally corrected terms (GO:BP transport; q_global = 0.0194), (GO:CC plasma membrane bounded cell projection; q_global = 0.0311), and (GO:BP establishment of localization; q_global = 0.038). The genes collectively point to vesicle trafficking, endocytic recycling, exocytosis, membrane organization, cytoskeletal remodeling, and small-GTPase signaling. CASK, STX6, RAB23, RAB18, RAB34, FLOT1, EXOC6, EXOC8, TRAPPC11, and UBAP1 provide complementary evidence for movement of cargo through endosomal, Golgi, lysosomal, and plasma-membrane pathways. ARHGEF6, ARHGEF7, GIT1, ARHGAP12, APC, BIN1, and DPYSL5 connect transport to actin, adhesion, neurite or projection biology, and membrane dynamics. The module therefore appears functionally coherent despite the absence of STRING functional enrichment and despite the absence of within-module term significance after its more limited correction.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module: the HPA summary identifies only one secreted gene, and most proteins are intracellular or membrane-associated. It is also not a uniformly tissue-specific housekeeping module. Most genes have low tissue specificity, while several show enhancement in brain, retina, skeletal muscle, lymphoid tissue, or bone marrow. The module is detected broadly at the protein level in both brain and skin, although a small subset is not detected in one of those tissues. Cell-type enhancement is frequent, especially for neutrophils and neutrophil progenitors, with additional signals in oligodendrocytes, monocytes, macrophages, microglia, and muscle-related cells. Blood-cell specificity is generally low, but the neutrophil and myeloid signals mean that variable immune-cell content could contribute to the shared co-abundance pattern. Thus, a shared cellular trafficking program is plausible, but a blood or myeloid contribution should be considered when interpreting tissue-level measurements.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP transport | 0.0194 | ARHGAP12, ARHGEF7, BIN1, CASK, DMAP1, EXOC6, EXOC8, FLOT1, GIT1, IRS2, LIPA, PRNP, RAB18, RAB23, RAB34, SIRT3, STX6, TRAPPC11, TRIM3, UBAP1, UNC119B |
| GO:CC plasma membrane bounded cell projection | 0.0311 | APC, ARHGEF6, ARHGEF7, BIN1, CASK, DPYSL5, EXOC6, EXOC8, FLOT1, GIT1, PRNP, RAB23, RAB34, TRIM3, UNC119B |
| GO:BP establishment of localization | 0.038 | ARHGAP12, ARHGEF7, BIN1, CASK, DMAP1, EXOC6, EXOC8, FLOT1, GIT1, IRS2, LIPA, PRNP, RAB18, RAB23, RAB34, SIRT3, STX6, TRAPPC11, TRIM3, UBAP1, UNC119B |

### STRING and hu.MAP

STRING provides a small set of high-confidence known relationships rather than a densely connected interaction network. The ARHGEF6–ARHGEF7–GIT1 relationships support a Rac or Rho-linked signaling and adhesion scaffold, while BIN1–DPYSL5 connects membrane or endocytic organization with a neural cytoskeletal protein. EXOC6–EXOC8 is a direct exocyst relationship and strongly supports vesicle tethering and exocytosis. The lack of STRING functional enrichment means that STRING does not independently establish a unified pathway for the whole module, but it does validate selected mechanistic subunits. hu.MAP adds stronger complex-level support: ARHGEF6, ARHGEF7, and GIT1 recur together in several complexes (hu.MAP huMAP3_05415.1), (hu.MAP huMAP3_13927.1), and (hu.MAP huMAP3_14886.1), and EXOC6 with EXOC8 recurs in several exocyst complexes (hu.MAP huMAP3_04054.1), (hu.MAP huMAP3_07009.1), (hu.MAP huMAP3_09839.1), and (hu.MAP huMAP3_12587.1). The TATDN1–SIRT3 pairing in (hu.MAP huMAP3_13468.1) is compatible with a mitochondrial or metabolic branch, but it is less directly connected to the main trafficking scaffold. Overall, the module combines known subcomplexes with co-abundance links that are not established physical interactions.

**STRING interactions (score >= 0.7)**: 5 of 496 gene pairs: ARHGEF6–ARHGEF7 (0.99); ARHGEF6–GIT1 (0.999); ARHGEF7–GIT1 (0.999); BIN1–DPYSL5 (0.872); EXOC6–EXOC8 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05415.1 (ARHGEF7, ARHGEF6, GIT1; 3/8); huMAP3_13927.1 (ARHGEF7, ARHGEF6, GIT1; 3/11); huMAP3_14886.1 (ARHGEF7, ARHGEF6, GIT1; 3/20); huMAP3_04054.1 (EXOC8, EXOC6; 2/10); huMAP3_07009.1 (EXOC8, EXOC6; 2/10); huMAP3_09839.1 (EXOC8, EXOC6; 2/12); huMAP3_12587.1 (EXOC8, EXOC6; 2/14); huMAP3_13468.1 (TATDN1, SIRT3; 2/99)

### Novelty

The module should be described as a potentially new conserved co-abundance configuration, not as a newly discovered molecular complex. Several constituent relationships and functions are already established, especially the ARHGEF6–ARHGEF7–GIT1 scaffold, the EXOC6–EXOC8 exocyst pair, and the trafficking roles of RAB, STX6, CASK, and related proteins. At the same time, most module pairs are not represented by high-confidence STRING links, and only selected subsets map to hu.MAP complexes. This pattern suggests that the novel aspect may be the coordinated brain–skin co-abundance organization and its integration of trafficking, projection biology, cytoskeletal signaling, and metabolic or stress-related genes, rather than discovery of an entirely unknown interaction mechanism. Absence from STRING or hu.MAP alone cannot establish novelty, so independent replication, preservation across cohorts, cell-composition adjustment, and perturbation-based testing would be needed before claiming a new biological module.

**Hypothesis.** Hypothesis: the conserved brain–skin module reflects a shared membrane-trafficking and cell-projection maintenance program. A core involving CASK, STX6, RAB23, RAB18, RAB34, FLOT1, EXOC6, and EXOC8 could coordinate cargo movement, endosomal recycling, Golgi-to-surface delivery, and membrane remodeling. The ARHGEF6–ARHGEF7–GIT1 scaffold could couple this trafficking machinery to Rac or Rho-regulated actin remodeling, adhesion, and projection structure, while BIN1 and DPYSL5 could connect it to endocytosis and neural or cytoskeletal organization. LIPA, SIRT3, HMOX2, and related genes may provide lipid-handling, mitochondrial, or oxidative-stress context. In brain this could support synaptic, glial, and neurite-associated membrane dynamics; in skin it could support epithelial or immune-cell membrane turnover. The hypothesis remains provisional because co-abundance does not demonstrate physical interaction, directionality, or a shared cell type.

### Important genes

#### CASK

- **Related proteins** (co-abundance neighbors): RAB23 (0.87), STX6 (0.86), FLOT1 (0.83), PRNP (0.81), RAB18 (0.81), RAB34 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium/calmodulin dependent serine protein kinase. This gene encodes a calcium/calmodulin-dependent serine protein kinase. The encoded protein is a MAGUK (membrane-associated guanylate kinase) protein family member. These proteins are scaffold proteins and the encoded protein is located at synapses in the brain. Mutations in this gene are associated with FG syndrome 4, intellectual disability and microcephaly with pontine and cerebellar hypoplasia…
- **Diseases (Open Targets)**: syndromic X-linked intellectual disability Najm type (0.829); FG syndrome 4 (0.800); cask-related x-linked intellectual disability (0.667); FG syndrome (0.567); hereditary disease (0.531)
- **Europe PMC papers**: 3838
- **Why important**: CASK is among the most connected genes in the module and links several trafficking-associated neighbors, including RAB23, STX6, FLOT1, PRNP, and RAB18. It is a membrane-associated scaffold located at synapses and is present in all three globally corrected terms (GO:BP transport; q_global = 0.0194), (GO:CC plasma membrane bounded cell projection; q_global = 0.0311), and (GO:BP establishment of localization; q_global = 0.038). Its brain and skin protein detection, synaptic role, and strong disease literature involving intellectual disability and neurodevelopment make it an important anchor for a projection and trafficking interpretation.
- **Conclusion**: Established evidence supports CASK as a membrane-associated scaffold connecting transport machinery to neural cell architecture. It is reasonable to hypothesize that CASK helps organize the shared module in brain and in relevant skin cell populations, but the co-abundance data do not establish that CASK directly regulates the other module members in skin.

#### STX6

- **Related proteins** (co-abundance neighbors): CASK (0.86), ACAD8 (0.84), RAB23 (0.82), TRIM3 (0.81), UBAP1 (0.81), SIRT3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntaxin 6. Enables syntaxin binding activity. Involved in several processes, including Golgi ribbon formation; retrograde transport, endosome to Golgi; and vesicle fusion. Acts upstream of or within endocytic recycling. Located in several cellular components, including early endosome; perinuclear region of cytoplasm; and trans-Golgi network. Part of SNARE complex. [provided by Alliance of Genome Resources, A…
- **Diseases (Open Targets)**: progressive supranuclear palsy (0.372); sporadic Creutzfeld Jacob disease (0.268); alcohol drinking (0.227); menopause (0.166); neoplasm (0.102)
- **Europe PMC papers**: 850
- **Why important**: STX6 is highly connected within the module and is linked to CASK, RAB23, TRIM3, UBAP1, and SIRT3. Its established function in SNARE-dependent vesicle fusion, endosome-to-Golgi retrograde transport, and endocytic recycling directly matches (GO:BP transport; q_global = 0.0194) and (GO:BP establishment of localization; q_global = 0.038). It is detected in brain and skin and has substantial literature supporting a central role in intracellular membrane traffic.
- **Conclusion**: Established evidence identifies STX6 as a strong mechanistic representative of the module's transport function. Its placement suggests that vesicle fusion and recycling may be a core process, while any specific brain–skin regulatory connection remains a hypothesis.

#### GIT1

- **Related proteins** (co-abundance neighbors): APC (0.88), BIN1 (0.85), ANKIB1 (0.84), RAB23 (0.82), TRIM3 (0.81); STRING partners: ARHGEF6 (0.999), ARHGEF7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_05415.1, huMAP3_13927.1, huMAP3_14886.1
- **Function (MyGene.info)**: GIT ArfGAP 1. Enables gamma-tubulin binding activity. Involved in positive regulation of microtubule nucleation and regulation of cytokinesis. Located in several cellular components, including focal adhesion; microtubule cytoskeleton; and mitochondrion. Implicated in attention deficit hyperactivity disorder. Biomarker of Huntington's disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.323); coronary artery disorder (0.237); hereditary disease (0.193); low tension glaucoma (0.173); venous thromboembolism (0.142)
- **Europe PMC papers**: 1678
- **Why important**: GIT1 has a prominent module position and connects APC, BIN1, ANKIB1, RAB23, and TRIM3. It is directly supported by STRING with ARHGEF6 and ARHGEF7 and occurs with those genes in several hu.MAP complexes (hu.MAP huMAP3_05415.1), (hu.MAP huMAP3_13927.1), and (hu.MAP huMAP3_14886.1). It is brain-enhanced, detected in skin, and associated with focal adhesions, microtubule organization, cytokinesis, ARF regulation, and neurodevelopmental or neurodegenerative evidence.
- **Conclusion**: Established evidence supports GIT1 as a bridge between membrane trafficking, cytoskeletal organization, and small-GTPase signaling. The module suggests that this scaffold may coordinate projection or adhesion-related trafficking across brain and skin, but that cross-tissue role is not yet demonstrated.

#### EXOC6

- **Related proteins** (co-abundance neighbors): EXOC8 (0.86); STRING partners: EXOC8 (0.999)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Centrosome, Basal body, Cytosol; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_04054.1, huMAP3_07009.1, huMAP3_09839.1, huMAP3_12587.1
- **Function (MyGene.info)**: exocyst complex component 6. The protein encoded by this gene is highly similar to the Saccharomyces cerevisiae SEC15 gene product, which is essential for vesicular traffic from the Golgi apparatus to the cell surface in yeast. It is one of the components of a multiprotein complex required for exocytosis. The 5' portion of this gene and two neighboring cytochrome p450 genes are included in a deletion that results in an autoso…
- **Diseases (Open Targets)**: pituitary gland disorder (0.358); metabolic syndrome (0.323); type 2 diabetes mellitus (0.317); Abnormality of the skeletal system (0.313); open-angle glaucoma (0.299)
- **Europe PMC papers**: 344
- **Why important**: EXOC6 is paired with EXOC8 in STRING and repeatedly occurs with EXOC8 in hu.MAP exocyst complexes (hu.MAP huMAP3_04054.1), (hu.MAP huMAP3_07009.1), (hu.MAP huMAP3_09839.1), and (hu.MAP huMAP3_12587.1). Its annotated role in exocytosis and Golgi-to-plasma-membrane transport is directly consistent with (GO:BP transport; q_global = 0.0194), (GO:CC plasma membrane bounded cell projection; q_global = 0.0311), and (GO:BP establishment of localization; q_global = 0.038). It is protein-detected in both tissues and shows enhancement in retina and in several cell types including muscle-related and neutrophil-related populations.
- **Conclusion**: Established evidence supports EXOC6 as a component of the exocyst machinery that gives the module a concrete vesicle-tethering mechanism. Its co-abundance with the wider module may indicate coordinated surface delivery, although the remaining links are not proven to be exocyst interactions.

#### ARHGEF7

- **Related proteins** (co-abundance neighbors): TRAPPC11 (0.83), APC (0.82); STRING partners: ARHGEF6 (0.99), GIT1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_05415.1, huMAP3_13927.1, huMAP3_14886.1
- **Function (MyGene.info)**: Rho guanine nucleotide exchange factor 7. This gene encodes a protein that belongs to a family of cytoplasmic proteins that activate the Ras-like family of Rho proteins by exchanging bound GDP for GTP. It forms a complex with the small GTP binding protein Rac1 and recruits Rac1 to membrane ruffles and to focal adhesions. Multiple alternatively spliced transcript variants encoding different isoforms have been observed for this gene. [provi…
- **Diseases (Open Targets)**: diabetes mellitus (0.287); alcohol drinking (0.267); stroke disorder (0.267); ovarian dysfunction (0.261); adolescent idiopathic scoliosis (0.257)
- **Europe PMC papers**: 937
- **Why important**: ARHGEF7 is present in all three primary terms (GO:BP transport; q_global = 0.0194), (GO:CC plasma membrane bounded cell projection; q_global = 0.0311), and (GO:BP establishment of localization; q_global = 0.038), connects to TRAPPC11 and APC in the module, and has strong STRING relationships with ARHGEF6 and GIT1. It recurs with those genes in hu.MAP complexes (hu.MAP huMAP3_05415.1), (hu.MAP huMAP3_13927.1), and (hu.MAP huMAP3_14886.1). Its established ability to activate Rho-family signaling and recruit Rac1 to membrane ruffles and focal adhesions provides a plausible cytoskeletal signaling arm for the transport module.
- **Conclusion**: Established evidence supports ARHGEF7 as a signaling and actin-remodeling connector between membrane localization and cell-projection behavior. A reasonable hypothesis is that it couples trafficking to shape or adhesion changes in brain and skin cells, but the module does not prove the direction of that coupling.

#### RAB23

- **Related proteins** (co-abundance neighbors): CASK (0.87), STX6 (0.82), GIT1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB23, member RAS oncogene family. This gene encodes a small GTPase of the Ras superfamily. Rab proteins are involved in the regulation of diverse cellular functions associated with intracellular membrane trafficking, including autophagy and immune response to bacterial infection. The encoded protein may play a role in central nervous system development by antagonizing sonic hedgehog signaling. Disruption of this gene has been impl…
- **Diseases (Open Targets)**: RAB23-related Carpenter syndrome (0.791); Carpenter syndrome (0.766); coronary artery disorder (0.471); coronary atherosclerosis (0.467); hereditary disease (0.412)
- **Europe PMC papers**: 1213
- **Why important**: RAB23 connects CASK, STX6, and GIT1, placing a small membrane-trafficking GTPase at the interface of the module's scaffold, fusion, and signaling components. It appears in all primary terms (GO:BP transport; q_global = 0.0194), (GO:CC plasma membrane bounded cell projection; q_global = 0.0311), and (GO:BP establishment of localization; q_global = 0.038), is detected in brain and skin, and has established roles in intracellular transport, autophagy, ciliary or developmental signaling, and Carpenter syndrome.
- **Conclusion**: Established evidence supports RAB23 as a biologically meaningful trafficking regulator and a plausible bridge between membrane transport and developmental signaling. Its position supports the hypothesis of coordinated cargo localization in the shared module, but does not establish a tissue-specific mechanism or direct binding to its module neighbors.

## Module 3

**Tissue pair**: brain and skin  
**Genes (38)**: ABLIM1, ADAM10, ALDH4A1, ALDH2, ASAP1, CLIP2, CIT, EIPR1, FMNL2, ABAT, POLR2M, GNL1, HIBCH, HSPA2, IAH1, KIF21A, KLC2, MAP7D1, MADD, MAPRE2, MINK1, ABCC4, MTMR1, NF1, RASAL2, NUMBL, OSBPL2, OTUD7B, PIP4K2B, PRXL2A, REPS1, RAB11FIP5, ARHGAP5, SACS, SORBS2, ALDH5A1, USP8, WDTC1

### Function

The strongest functional interpretation is cell-cell signaling, supported by the only globally corrected GO/KEGG result, (GO:BP cell-cell signaling; q_global = 0.0207). The (GO:BP cell-cell signaling; q_global = 0.0207) genes span signaling regulators, membrane trafficking components, a transporter, and mitochondrial enzymes, suggesting that the module is not a single linear pathway. Its network also connects Ras and MAPK regulation through NF1 and MINK1, membrane proteolysis through ADAM10, endocytic recycling through RAB11FIP5 and EIPR1, cytoskeletal transport through KIF21A, and lipid signaling through MTMR1 and PIP4K2B. The GABA and aldehyde-metabolism genes form a separate, well-supported metabolic neighborhood in STRING. (STRING Component Somatodendritic compartment; within-query FDR = 0.0349) provides supplementary support for a somatodendritic or neuronal trafficking context, but it is not global enrichment evidence. Overall, the module is best viewed as a signaling, membrane-trafficking, cytoskeletal-polarity, and metabolic-support program rather than as a narrowly defined pathway.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: HPA identifies only a small minority as secreted, while many proteins are intracellular, membrane-associated, vesicular, mitochondrial, or cytoskeletal. The expression pattern is heterogeneous, with many genes showing low tissue specificity and others enhanced in brain, liver, kidney, muscle, retina, or epithelial cell types. Brain-associated annotations are frequent, but esophageal epithelial cells, hepatocytes, oligodendrocytes, cardiomyocytes, and neutrophils also recur. Blood-cell associations are present, especially for neutrophils and several lymphoid populations, but the module is not uniformly blood-cell specific. Thus, sample blood contamination or shared vascular or immune content cannot be excluded, yet the HPA profile does not support interpreting the module simply as a plasma-protein or blood-cell module. Protein detection in both brain and skin for most genes is compatible with a shared cellular or intracellular program, although tissue-level protein detection alone does not establish a common cell type.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP cell-cell signaling | 0.0207 | ABAT, ABCC4, ADAM10, ALDH5A1, EIPR1, MINK1, NF1, OSBPL2, RAB11FIP5, USP8 |

### STRING and hu.MAP

STRING provides a small set of high-confidence relationships rather than a dense interaction network. The best-supported neighborhood links ABAT with ALDH2 and ALDH5A1, and links ALDH2 with ALDH4A1, forming a coherent aldehyde and GABA-related metabolic subnetwork. MTMR1 and PIP4K2B provide a separate phosphoinositide-related connection. The supplementary somatodendritic enrichment (STRING Component Somatodendritic compartment; within-query FDR = 0.0349) includes ADAM10, MINK1, NF1, KIF21A, SACS, CIT, USP8, and related genes, supporting neuronal compartment or trafficking relevance but not global significance. hu.MAP independently places NF1 with KIF21A in several related complexes, ABLIM1 with SORBS2 in a cytoskeletal complex, MINK1 with RAB11FIP5 in complexes associated with signaling and trafficking, and REPS1 with NUMBL in an endocytic complex. These overlaps show that parts of the module recover known molecular relationships. However, the hu.MAP complexes contain many members outside the module and generally contribute only pairs of module genes, so they do not establish that the entire co-abundance module is one physical complex.

**STRING interactions (score >= 0.7)**: 4 of 703 gene pairs: ABAT–ALDH2 (0.945); ABAT–ALDH5A1 (0.994); ALDH2–ALDH4A1 (0.85); MTMR1–PIP4K2B (0.724)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Somatodendritic compartment (FDR = 0.0349, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03441.1 (NF1, KIF21A; 2/7); huMAP3_07158.1 (NF1, KIF21A; 2/8); huMAP3_08290.1 (NF1, KIF21A; 2/8); huMAP3_05977.1 (ABLIM1, SORBS2; 2/12); huMAP3_09709.1 (MINK1, RAB11FIP5; 2/57); huMAP3_10333.1 (MINK1, RAB11FIP5; 2/63); huMAP3_12394.1 (REPS1, NUMBL; 2/98)

### Novelty

This is plausibly a new tissue-shared co-abundance finding, but novelty cannot be claimed as established from the supplied evidence alone. The module combines a globally significant cell-cell signaling signature (GO:BP cell-cell signaling; q_global = 0.0207) with neuronal-compartment support (STRING Component Somatodendritic compartment; within-query FDR = 0.0349), metabolic STRING links, and several hu.MAP-supported substructures. That combination may represent a conserved relationship across brain and skin that is not captured by existing interaction databases. Nevertheless, absence of most module pairs from STRING or hu.MAP is not proof of novelty, because those resources emphasize physical or curated relationships and may miss tissue-specific co-regulation, indirect signaling, cell-composition effects, and context-dependent associations. A defensible conclusion is that the module contains novel or under-characterized cross-tissue organization that requires replication, cell-type adjustment, perturbation experiments, and comparison with published co-expression or proteomic modules.

**Hypothesis.** Hypothesis: a shared brain-skin cell program coordinates plasma-membrane signaling with endosomal recycling, cytoskeletal transport, and metabolic protection. In this model, ADAM10-dependent ectodomain processing and NF1-MINK1 regulation tune receptor and MAPK signaling; RAB11FIP5, REPS1, USP8, and EIPR1 regulate recycling and endosomal cargo; KIF21A, SACS, SORBS2, and related cytoskeletal proteins organize polarized transport; and ABAT, ALDH2, ALDH4A1, and ALDH5A1 buffer aldehyde or GABA-related metabolic stress. The shared abundance pattern could therefore reflect a conserved capacity for signaling, trafficking, and stress handling in neural and cutaneous cells, possibly amplified by shared epithelial, vascular, or immune-cell contributions. This is a mechanistic proposal, not a demonstrated causal pathway.

### Important genes

#### MINK1

- **Related proteins** (co-abundance neighbors): MADD (0.88), NF1 (0.85), MTMR1 (0.85), RAB11FIP5 (0.81), ASAP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_09709.1, huMAP3_10333.1
- **Function (MyGene.info)**: misshapen like kinase 1. This gene encodes a serine/threonine kinase belonging to the germinal center kinase (GCK) family. The protein is structurally similar to the kinases that are related to NIK and may belong to a distinct subfamily of NIK-related kinases within the GCK family. Studies of the mouse homolog indicate an up-regulation of expression in the course of postnatal mouse cerebral development and activation of t…
- **Diseases (Open Targets)**: Alzheimer disease (0.326); neurodegenerative disease (0.318); Parkinson disease (0.316); lysosomal storage disease (0.316); obesity disorder (0.301)
- **Europe PMC papers**: 621
- **Why important**: MINK1 is a high-connectivity central node linked to MADD, NF1, MTMR1, RAB11FIP5, and ASAP1. It is the only kinase among the most prominent signaling connectors and is included in both the globally significant cell-cell signaling term (GO:BP cell-cell signaling; q_global = 0.0207) and the supplementary somatodendritic term (STRING Component Somatodendritic compartment; within-query FDR = 0.0349). Its reported MAPK, JNK, cell-matrix adhesion, synaptic, and brain-development functions make it a plausible bridge between signaling, cytoskeletal organization, and neural compartment biology. It also has disease links to neurodegenerative and neurodevelopmental conditions and a substantial literature base.
- **Conclusion**: Established evidence supports MINK1 as a signaling and cytoskeletal regulator with a central position in this module and annotation in (GO:BP cell-cell signaling; q_global = 0.0207) and (STRING Component Somatodendritic compartment; within-query FDR = 0.0349). It is a strong candidate for coordinating the module, but a direct causal role in the brain-skin co-abundance pattern remains a hypothesis.

#### NF1

- **Related proteins** (co-abundance neighbors): MINK1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Plasma membrane; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_03441.1, huMAP3_07158.1, huMAP3_08290.1
- **Function (MyGene.info)**: neurofibromin 1. This gene product appears to function as a negative regulator of the ras signal transduction pathway. Mutations in this gene have been linked to neurofibromatosis type 1, juvenile myelomonocytic leukemia and Watson syndrome. The mRNA for this gene is subject to RNA editing (CGA>UGA->Arg1306Term) resulting in premature translation termination. Alternatively spliced transcript variants encoding diff…
- **Diseases (Open Targets)**: neurofibromatosis type 1 (0.886); neurofibromatosis-Noonan syndrome (0.841); neurofibromatosis (0.819); juvenile myelomonocytic leukemia (0.769); Watson syndrome (0.756)
- **Europe PMC papers**: 30450
- **Why important**: NF1 is a canonical Ras-pathway negative regulator, belongs to (GO:BP cell-cell signaling; q_global = 0.0207), and is connected to MINK1 in the module. It also participates with KIF21A in several hu.MAP complexes (hu.MAP huMAP3_03441.1), (hu.MAP huMAP3_07158.1), and (hu.MAP huMAP3_08290.1), while appearing in the supplementary somatodendritic annotation (STRING Component Somatodendritic compartment; within-query FDR = 0.0349). Its very strong disease evidence for neurofibromatosis and related developmental disorders, together with a large literature base, gives this node unusually well-established biological significance.
- **Conclusion**: Established evidence identifies NF1 as a Ras-signaling brake with relevance to neural development and disease, and the module places it beside MINK1 and KIF21A. The data support a role for Ras-signaling control in the module, but do not prove that NF1 physically binds all co-abundant partners or drives the cross-tissue conservation.

#### ADAM10

- **Related proteins** (co-abundance neighbors): ALDH4A1 (0.82), HIBCH (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ADAM metallopeptidase domain 10. Members of the ADAM family are cell surface proteins with a unique structure possessing both potential adhesion and protease domains. This gene encodes and ADAM family member that cleaves many proteins including TNF-alpha and E-cadherin. Alternate splicing results in multiple transcript variants encoding different proteins that may undergo similar processing. [provided by RefSeq, Feb 2016].
- **Diseases (Open Targets)**: reticulate acropigmentation of Kitamura (0.679); Alzheimer disease 18 (0.621); Alzheimer disease (0.522); dementia (0.415); schizophrenia (0.354)
- **Europe PMC papers**: 11139
- **Why important**: ADAM10 is included in (GO:BP cell-cell signaling; q_global = 0.0207) and (STRING Component Somatodendritic compartment; within-query FDR = 0.0349), is detected in both tissues, and occupies a membrane or vesicular location consistent with regulated ectodomain proteolysis. Its established functions include cleavage of TNF-alpha and E-cadherin, membrane-protein processing, adhesion regulation, and Notch signaling. It therefore provides a biologically meaningful route from the module to intercellular communication and tissue architecture, with extensive literature and disease associations including Alzheimer disease and pigmentation-related disease.
- **Conclusion**: Established evidence supports ADAM10 as a membrane protease involved in signaling and adhesion. Its presence in this module strengthens the cell-cell signaling interpretation, but the co-abundance data do not establish which ADAM10 substrates or signaling outputs are involved in brain or skin.

#### ABAT

- **Related proteins** (co-abundance neighbors): ALDH2 (0.86), PRXL2A (0.85); STRING partners: ALDH2 (0.945), ALDH5A1 (0.994)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 4-aminobutyrate aminotransferase. 4-aminobutyrate aminotransferase (ABAT) is responsible for catabolism of gamma-aminobutyric acid (GABA), an important, mostly inhibitory neurotransmitter in the central nervous system, into succinic semialdehyde. The active enzyme is a homodimer of 50-kD subunits complexed to pyridoxal-5-phosphate. The protein sequence is over 95% similar to the pig protein. GABA is estimated to be present in near…
- **Diseases (Open Targets)**: GABA aminotransaminase deficiency (0.795); infantile spasms (0.568); mitochondrial DNA depletion syndrome (0.542); epilepsy (0.468); Focal impaired awareness seizure (0.466)
- **Europe PMC papers**: 1783
- **Why important**: ABAT is a brain-enhanced mitochondrial enzyme included in (GO:BP cell-cell signaling; q_global = 0.0207). It is connected in STRING to ALDH2 and ALDH5A1, linking the module to a coherent GABA and succinic-semialdehyde metabolic neighborhood. Its known role in GABA catabolism and its associations with GABA aminotransferase deficiency, epilepsy, and infantile spasms give it strong functional and disease relevance. It also provides a metabolic complement to the module's signaling and trafficking components.
- **Conclusion**: Established evidence supports ABAT as a GABA-catabolic mitochondrial enzyme and supports the metabolic subnetwork through its STRING relationships. Its inclusion does not demonstrate that GABA metabolism mechanistically controls the whole module; that connection is a hypothesis.

#### KIF21A

- **Related proteins** (co-abundance neighbors): MADD (0.87), CLIP2 (0.84), FMNL2 (0.84), CIT (0.82), MAPRE2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_03441.1, huMAP3_07158.1, huMAP3_08290.1
- **Function (MyGene.info)**: kinesin family member 21A. This gene encodes a member of the KIF4 subfamily of kinesin-like motor proteins. The encoded protein is characterized by an N-terminal motor domain a coiled-coil stalk domain and a C-terminal WD-40 repeat domain. This protein may be involved in microtubule dependent transport. Mutations in this gene are the cause of congenital fibrosis of extraocular muscles-1. Alternate splicing results in multip…
- **Diseases (Open Targets)**: congenital fibrosis of the extraocular muscles (0.822); arthrogryposis (0.462); hereditary disease (0.416); fetal akinesia deformation sequence (0.370); Abnormality of eye movement (0.340)
- **Europe PMC papers**: 639
- **Why important**: KIF21A is a high-connectivity microtubule motor connected to MADD, CLIP2, FMNL2, CIT, and MAPRE2. It is included in the supplementary somatodendritic term (STRING Component Somatodendritic compartment; within-query FDR = 0.0349) and repeatedly co-occurs with NF1 in hu.MAP complexes (hu.MAP huMAP3_03441.1), (hu.MAP huMAP3_07158.1), and (hu.MAP huMAP3_08290.1). Its established roles in microtubule-dependent transport, polarity, and axonal transport, together with disease associations involving congenital eye-movement disorders and arthrogryposis, make it a strong structural and transport anchor.
- **Conclusion**: Established evidence supports KIF21A as a microtubule transport and polarity factor, and the network supports a relationship to the NF1-MINK1 signaling neighborhood. Its skin absence in the supplied HPA immunohistochemistry record cautions against assuming uniform cellular action in both tissues; a shared abundance association does not by itself prove shared protein function.

## Module 4

**Tissue pair**: brain and skin  
**Genes (7)**: ACACA, ANO10, ASL, ERLIN2, MEAK7, MGST1, MYLK

### Function

No GO or KEGG term passed global multiple-testing correction, and there was no supplementary STRING functional enrichment. Therefore, the module does not support a statistically established single pathway-level function. Its gene annotations nevertheless suggest a mixed cellular program involving membrane and ER lipid organization, calcium-dependent membrane biology, lipid and fatty-acid metabolism, redox and electrophile defense, amino-acid and urea-cycle metabolism, and cytoskeletal contractility. ANO10 is the central network connector, linking MYLK, ACACA, MEAK7, ASL, and ERLIN2, while MEAK7 connects to MGST1. This topology is consistent with coordinated abundance across membrane, metabolic, stress-response, and contractile processes, but it does not establish a common biochemical pathway.

**Cell composition.** The module is not predominantly composed of secreted or plasma proteins: only MGST1 is annotated as secreted, with intracellular and membrane localization, and the remaining proteins are intracellular or membrane-associated. It is also not uniformly blood-cell specific. HPA evidence shows mostly low immune-cell specificity, with individual associations involving neutrophils, basophils, monocytes, myeloid dendritic cells, and megakaryocytes. The tissue pattern is heterogeneous, including liver, adipose tissue, adrenal gland, smooth muscle, and seminal vesicle, while single-cell annotations include hepatocytes, glial and neuronal populations, adipocytes, epithelial cells, and contractile or blood-related cells. All module proteins are detected in skin, whereas two are not detected in the surveyed brain regions. Thus, shared brain-skin co-abundance could reflect broadly detectable cellular programs, shared cell types, or sample-composition effects rather than a brain-skin-specific biological pathway. The liver and hepatocyte signals particularly argue for caution about systemic or metabolic contributions.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module gene pair met the supplied high-confidence STRING interaction threshold, and no STRING functional enrichment was reported. No hu.MAP complex contained at least two module members. The observed co-abundance relationships are therefore not corroborated by curated high-confidence physical interactions or a shared hu.MAP complex. This does not invalidate the module: co-abundance can arise from common regulation, cell composition, tissue state, or indirect metabolic relationships. It does mean that the network should be interpreted as an expression-level association rather than as a demonstrated protein complex or direct interaction network.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is potentially novel as a cross-tissue co-abundance pattern because its exact gene set has no high-confidence STRING pair interactions and no shared hu.MAP complex. However, absence from those resources does not prove biological novelty. Several component functions are already established: ANO10 in membrane ion biology and inherited ataxia, MYLK in actomyosin contractility and vascular disease, ACACA in fatty-acid synthesis and neurodegenerative disease associations, MGST1 in glutathione and lipid-peroxide defense, ASL in the urea cycle and arginine metabolism, MEAK7 in TOR-related signaling, and ERLIN2 in ER lipid-raft biology and ER-associated degradation. The defensible novelty claim is therefore the joint brain-skin co-abundance organization and its specific topology, not the individual gene functions or a newly discovered physical complex.

**Hypothesis.** Hypothesis: the module reflects a coordinated membrane-metabolic stress state shared by selected brain and skin cell populations. ANO10 and ERLIN2 could provide membrane and ER context; ACACA could support lipid supply; MGST1 could buffer lipid-peroxidation or electrophilic stress; MEAK7 could connect nutrient and TOR-related signaling; and MYLK could translate calcium or cellular-state changes into cytoskeletal contractility. ASL may represent linked nitrogen and arginine metabolism. This model is mechanistically plausible from the individual annotations and network placement, but it is not established by the enrichment analysis, STRING, hu.MAP, or the co-abundance data alone. It should be tested using cell-resolved data, replication across cohorts, protein-level measurements, and perturbation of membrane lipid, oxidative-stress, and contractility pathways.

### Important genes

#### ANO10

- **Related proteins** (co-abundance neighbors): MYLK (0.90), ACACA (0.87), MEAK7 (0.81), ASL (0.80), ERLIN2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: anoctamin 10. The transmembrane protein encoded by this gene belongs to the anoctamin family of calcium-activated chloride channels, also known as the transmembrane 16 family. The encoded protein contains eight transmembrane domains with cytosolic N- and C-termini. Defects in this gene may cause autosomal recessive spinocerebellar ataxia-10. Alternative splicing results in multiple transcript variants. [provide…
- **Diseases (Open Targets)**: autosomal recessive spinocerebellar ataxia 10 (0.799); Dorfman-Chanarin disease (0.464); COVID-19 (0.370); autosomal recessive cerebellar ataxia (0.345); Abnormal central motor function (0.340)
- **Europe PMC papers**: 401
- **Why important**: ANO10 is the most connected and strongest hub in the module, linking five other members. It encodes a multi-pass anoctamin-family membrane protein involved in ion transport and is detected in both brain and skin. Its HPA annotation is broadly tissue distributed but enhanced in neutrophil-lineage cells. It has a substantial literature base and established associations with autosomal recessive spinocerebellar ataxia and related disorders, making it the best network-level anchor for interpreting the module.
- **Conclusion**: Established: ANO10 is the module's central co-abundance hub and has membrane ion-transport and neurological disease relevance. Hypothesis: it may coordinate membrane-state signals with lipid, ER, metabolic, and contractile genes in this module; the data do not demonstrate direct physical interactions.

#### ACACA

- **Related proteins** (co-abundance neighbors): ANO10 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA carboxylase alpha. Acetyl-CoA carboxylase (ACC) is a complex multifunctional enzyme system. ACC is a biotin-containing enzyme which catalyzes the carboxylation of acetyl-CoA to malonyl-CoA, the rate-limiting step in fatty acid synthesis. There are two ACC forms, alpha and beta, encoded by two different genes. ACC-alpha is highly enriched in lipogenic tissues. The enzyme is under long term control at the transcriptio…
- **Diseases (Open Targets)**: neurodegenerative disease (0.550); Alzheimer disease (0.463); lysosomal storage disease (0.460); Parkinson disease (0.460); autoimmune disorder of central nervous system (0.383)
- **Europe PMC papers**: 6268
- **Why important**: ACACA is connected directly to ANO10 and encodes the rate-limiting enzyme for malonyl-CoA production and fatty-acid synthesis. It is detected in brain and skin and is enhanced across multiple neural and glial cell types. Its extensive literature and disease associations involving neurodegenerative disorders make it an important metabolic interpretation point.
- **Conclusion**: Established: ACACA supports fatty-acid and lipid biosynthesis and is relevant to neural and neurodegenerative biology. Hypothesis: it may supply lipid remodeling needed for membrane or ER responses represented by ANO10 and ERLIN2, but enrichment and causal coupling are not shown.

#### MGST1

- **Related proteins** (co-abundance neighbors): MEAK7 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Mitochondria; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: microsomal glutathione S-transferase 1. The MAPEG (Membrane Associated Proteins in Eicosanoid and Glutathione metabolism) family consists of six human proteins, two of which are involved in the production of leukotrienes and prostaglandin E, important mediators of inflammation. Other family members, demonstrating glutathione S-transferase and peroxidase activities, are involved in cellular defense against toxic, carcinogenic, and pharma…
- **Diseases (Open Targets)**: adolescent idiopathic scoliosis (0.314); insomnia (0.291); skin disorder (0.250); esophageal adenocarcinoma (0.250); Barrett esophagus (0.249)
- **Europe PMC papers**: 2236
- **Why important**: MGST1 connects to MEAK7 and is tissue enhanced in adipose tissue, adrenal gland, and liver, with hepatocyte and monocyte-related annotations. It participates in glutathione-dependent defense, lipid-hydroperoxide responses, and eicosanoid-related biology. Its substantial literature and relevance to oxidative and inflammatory stress make it important for interpreting the module's possible cellular-state component.
- **Conclusion**: Established: MGST1 is an intracellular membrane-associated defense enzyme linked to redox and lipid-stress biology. Hypothesis: it may couple metabolic or membrane remodeling to protection from oxidative damage in shared brain and skin cell states; the module does not establish that mechanism.

#### ERLIN2

- **Related proteins** (co-abundance neighbors): ANO10 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ER lipid raft associated 2. This gene encodes a member of the SPFH domain-containing family of lipid raft-associated proteins. The encoded protein is localized to lipid rafts of the endoplasmic reticulum and plays a critical role in inositol 1,4,5-trisphosphate (IP3) signaling by mediating ER-associated degradation of activated IP3 receptors. Mutations in this gene are a cause of spastic paraplegia-18 (SPG18). Alternatively …
- **Diseases (Open Targets)**: hereditary spastic paraplegia 18 (0.757); spastic paraplegia 18b, autosomal recessive (0.659); hereditary spastic paraplegia (0.631); cancer (0.587); autosomal dominant complex spastic paraplegia (0.570)
- **Europe PMC papers**: 595
- **Why important**: ERLIN2 is directly connected to the ANO10 hub and is localized to ER lipid rafts. Its annotated functions include ER-associated degradation and regulation of cholesterol and fatty-acid biosynthesis. It is detected in both brain and skin and has established associations with hereditary spastic paraplegia. Although its literature volume is more limited than that of MYLK, its ER position gives it strong mechanistic relevance.
- **Conclusion**: Established: ERLIN2 participates in ER lipid-raft biology, ER-associated degradation, and lipid homeostasis. Hypothesis: it may provide the ER interface linking ANO10-associated membrane biology to ACACA-dependent lipid synthesis and stress defense.

#### MYLK

- **Related proteins** (co-abundance neighbors): ANO10 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin light chain kinase. This gene, a muscle member of the immunoglobulin gene superfamily, encodes myosin light chain kinase which is a calcium/calmodulin dependent enzyme. This kinase phosphorylates myosin regulatory light chains to facilitate myosin interaction with actin filaments to produce contractile activity. This gene encodes both smooth muscle and nonmuscle isoforms. In addition, using a separate promoter in an …
- **Diseases (Open Targets)**: aortic aneurysm, familial thoracic 7 (0.767); familial thoracic aortic aneurysm and aortic dissection (0.710); megacystis-microcolon-intestinal hypoperistalsis syndrome 1 (0.617); megacystis-microcolon-intestinal hypoperistalsis syndrome (0.597); Rare genetic vascular disease (0.483)
- **Europe PMC papers**: 10503
- **Why important**: MYLK is directly connected to ANO10 and has the largest literature volume among the module members. It encodes a calcium-calmodulin-dependent kinase that phosphorylates myosin light chains and promotes actomyosin contraction, migration, and bleb formation. HPA supports smooth-muscle, myoepithelial, hepatic-stellate, platelet, and granulocyte-related expression, and it is detected in skin.
- **Conclusion**: Established: MYLK is a major regulator of contractility and migration with strong vascular and smooth-muscle disease relevance. Hypothesis: its co-abundance with ANO10 may reflect coordinated calcium-sensitive membrane and cytoskeletal remodeling, possibly through shared cell composition rather than direct molecular coupling.

## Module 5

**Tissue pair**: brain and skin  
**Genes (47)**: ACADM, AGO2, ARGLU1, ATXN2, BLOC1S3, CETN2, DHRS1, ECT2, EHMT2, ELP2, ESS2, FGD4, FN1, FKBP15, GRSF1, FECH, HLTF, CHUK, KANK1, PRKAR2B, KIF11, LMO7, MLST8, LEMD3, MYEF2, NCK1, NEK7, NFXL1, NUF2, DHRS7B, PHLDB2, RBPMS, RNASET2, POLR2G, MRPS18B, SELENOO, SMARCAD1, TBC1D4, GTF3C1, GTF3C2, TRMT1, TRUB1, USP10, VPS4B, VWA8, ZFAND5, ZMYM3

### Function

No GO or KEGG term passed global correction, so there is no globally significant pathway assignment for this module. The gene annotations nevertheless suggest a mixed cellular maintenance module rather than a single narrowly defined pathway. Its biological themes include RNA processing and modification, transcription by RNA polymerases, chromatin regulation, mitotic spindle and chromosome organization, cytoskeletal and cell-adhesion control, mitochondrial metabolism, and organelle or vesicle biology. The network is sparse, so these themes should be treated as convergent interpretation of the member genes rather than as a demonstrated unified pathway. The strongest directly supported network relationships include the GTF3C1-GTF3C2 transcription-factor pair, the KIF11-NUF2 mitotic pair, the ECT2 links to KIF11 and NUF2, the KANK1-PHLDB2 cytoskeletal link, and the TRMT1-TRUB1 RNA-modification link.

**Cell composition.** This is not predominantly a plasma or secreted-protein module. FN1 is secreted to blood, and RNASET2 is also secreted to blood, but most members are intracellular proteins located in the nucleus, cytosol, mitochondria, vesicles, membrane, or cytoskeletal compartments. The HPA profile is largely low in tissue specificity, with many proteins detected in both brain and skin, which supports broad cellular expression rather than a strongly brain-specific or skin-specific program. There are, however, substantial signals from liver, skeletal muscle, bone marrow, blood vessels, lymphoid tissue, neutrophils, erythrocyte progenitors, and other specialized cell types. These observations raise the possibility that part of the shared co-abundance reflects common cell populations, vascular or blood-related material, or general cellular composition in the samples. The blood-cell evidence is not dominant across the module, and only a small subset is secreted, so a simple plasma-contamination explanation is insufficient.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited set of established high-confidence relationships: GTF3C1-GTF3C2, KIF11-NUF2, ECT2-KIF11, ECT2-NUF2, KANK1-PHLDB2, and TRMT1-TRUB1. These links provide credible local anchors for transcription, mitosis, cytoskeletal organization, and RNA modification, but most module pairs are not supported by STRING at the stated threshold. hu.MAP provides additional complex-level support. GTF3C1 and GTF3C2 occur together in (hu.MAP huMAP3_10875.1) and (hu.MAP huMAP3_01637.1), with GTF3C1 also represented in (hu.MAP huMAP3_14801.1). SMARCAD1 links to the GTF3C complex in (hu.MAP huMAP3_10875.1) and (hu.MAP huMAP3_14801.1). CETN2 and HLTF co-occur in (hu.MAP huMAP3_14846.1), ZMYM3 and EHMT2 in (hu.MAP huMAP3_11539.1), and PHLDB2 and LMO7 in (hu.MAP huMAP3_09542.1). These complexes indicate that portions of the module overlap known transcriptional, chromatin, DNA-repair, and cytoskeletal assemblies. Because most module genes lack STRING or hu.MAP support, the full module should not be interpreted as one experimentally established complex.

**STRING interactions (score >= 0.7)**: 6 of 1081 gene pairs: ECT2–KIF11 (0.891); ECT2–NUF2 (0.818); GTF3C1–GTF3C2 (0.999); KANK1–PHLDB2 (0.894); KIF11–NUF2 (0.975); TRMT1–TRUB1 (0.824)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10875.1 (GTF3C1, GTF3C2, SMARCAD1; 3/14); huMAP3_01637.1 (GTF3C1, GTF3C2; 2/5); huMAP3_14801.1 (GTF3C1, SMARCAD1; 2/13); huMAP3_14846.1 (CETN2, HLTF; 2/27); huMAP3_11539.1 (ZMYM3, EHMT2; 2/32); huMAP3_09542.1 (PHLDB2, LMO7; 2/38)

### Novelty

The shared brain-skin co-abundance pattern may be a new observation, but the evidence does not establish a new molecular complex or pathway. Several relationships and substructures are already known through STRING and hu.MAP, including the GTF3C transcriptional machinery, the KIF11-NUF2 mitotic machinery, chromatin-associated assemblies containing SMARCAD1, ZMYM3, or EHMT2, and cytoskeletal assemblies involving PHLDB2 or LMO7. Conversely, the absence of many module pairs from STRING or hu.MAP cannot prove novelty because those resources emphasize experimentally characterized interactions and curated complexes rather than co-abundance. The most defensible novelty claim is therefore the reproducible conservation of this particular mixed co-abundance pattern across brain and skin, pending independent replication, control for cell composition, and comparison with published cross-tissue modules.

**Hypothesis.** Hypothesis: the module reflects a shared state of actively maintained, proliferative or remodeling cells in brain and skin, combining chromatin and RNA regulation with cytoskeletal organization, organelle trafficking, and metabolic support. A possible mechanism is that transcriptional and chromatin regulators such as GTF3C1, GTF3C2, SMARCAD1, ZMYM3, and EHMT2 coordinate gene-expression capacity, while KIF11, NUF2, and ECT2 mark mitotic or cytokinetic activity; PHLDB2, LMO7, KANK1, and related proteins connect this state to cell polarity, adhesion, and actin organization. The brain-skin conservation could arise from shared epithelial, vascular, progenitor, or other broadly distributed cell states rather than from a tissue-specific brain-skin pathway. This hypothesis should be tested with cell-type-resolved data, matched sample-quality controls, and perturbation or protein-interaction experiments.

### Important genes

#### ESS2

- **Related proteins** (co-abundance neighbors): TRMT1 (0.87), FN1 (0.85), NEK7 (0.84), ACADM (0.84), VPS4B (0.81), ATXN2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ess-2 spliceosome associated protein. This gene is located within the minimal DGS critical region (MDGCR) thought to contain the gene(s) responsible for a group of developmental disorders. These disorders include DiGeorge syndrome, velocardiofacial syndrome, conotruncal anomaly face syndrome, and some familial or sporadic conotruncal cardiac defects which have been associated with microdeletion of 22q11.2. The encoded protein may be a…
- **Diseases (Open Targets)**: arthropathy (0.097); prostate carcinoma (0.076); Familial prostate cancer (0.076); prostate cancer (0.076); alcohol drinking (0.038)
- **Europe PMC papers**: 173
- **Why important**: ESS2 has the strongest network position in the module and connects RNA-splicing-associated biology with FN1, NEK7, ACADM, VPS4B, and ATXN2. Its annotation supports mRNA splicing and nervous-system development, while its localization and protein detection are compatible with the shared brain-skin signal. Its developmental-disorder context and spliceosome association make it a useful candidate for linking RNA processing to tissue-state variation, although it has no STRING or hu.MAP support here.
- **Conclusion**: Established evidence supports ESS2 as a highly connected spliceosome-associated and development-related member. It is a plausible module coordinator, but its coordinating role in this module remains a hypothesis because the surrounding links are co-abundance links rather than established physical interactions.

#### FN1

- **Related proteins** (co-abundance neighbors): ESS2 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 is the clearest extracellular and composition-sensitive member. It is secreted to blood, is enhanced in blood vessels, liver, and placenta, and is associated with fibroblasts, hepatic stellate cells, and cell-matrix adhesion. It links the module to adhesion, migration, wound healing, coagulation, and extracellular matrix biology, while its direct network connection to ESS2 is strong within the reported subgraph. FN1 also has extensive literature and disease association, making it an important interpretive anchor even though it is peripheral in network degree.
- **Conclusion**: Established evidence supports FN1 as an extracellular-matrix and vascular or stromal marker that could contribute to sample-composition effects. Its presence does not demonstrate that the whole module is extracellular or blood-derived; that broader interpretation is only a hypothesis.

#### GTF3C1

- **Related proteins** (co-abundance neighbors): GTF3C2 (0.82), NCK1 (0.81); STRING partners: GTF3C2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Nucleoli; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_10875.1, huMAP3_01637.1, huMAP3_14801.1
- **Function (MyGene.info)**: general transcription factor IIIC subunit 1. Predicted to contribute to DNA binding activity. Predicted to be involved in 5S class rRNA transcription by RNA polymerase III and transcription initiation from RNA polymerase III promoter. Located in nucleolus and nucleoplasm. Part of transcription factor TFIIIC complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.543); lysosomal storage disease (0.357); alopecia areata (0.352); Abnormal brain morphology (0.266); esophageal atresia/tracheoesophageal fistula (0.259)
- **Europe PMC papers**: 394
- **Why important**: GTF3C1 is a member of the known TFIIIC transcriptional machinery, has a direct STRING relationship with GTF3C2, and appears in (hu.MAP huMAP3_10875.1), (hu.MAP huMAP3_01637.1), and (hu.MAP huMAP3_14801.1). Its annotations support RNA polymerase III initiation and tRNA or five-S-rRNA transcription. Its position connects the module to NCK1 and GTF3C2, while its disease associations include neurodegenerative and brain-related phenotypes.
- **Conclusion**: Established evidence supports GTF3C1 as a bona fide transcriptional-complex component and one of the module's strongest mechanistic anchors. It is reasonable to interpret the GTF3C1-GTF3C2 substructure as known biology, but not to infer that every module member participates in TFIIIC.

#### KIF11

- **Related proteins** (co-abundance neighbors): DHRS7B (0.83), NUF2 (0.82); STRING partners: ECT2 (0.891), NUF2 (0.975)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Mid piece; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 11. This gene encodes a motor protein that belongs to the kinesin-like protein family. Members of this protein family are known to be involved in various kinds of spindle dynamics. The function of this gene product includes chromosome positioning, centrosome separation and establishing a bipolar spindle during cell mitosis. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: microcephaly with or without chorioretinopathy, lymphedema, or intellectual disability (0.821); hereditary disease (0.509); inherited retinal dystrophy (0.507); neurodegenerative disease (0.484); microcephaly (0.412)
- **Europe PMC papers**: 3618
- **Why important**: KIF11 is supported by STRING links to NUF2 and ECT2 and is annotated for spindle organization, centrosome separation, and mitotic chromosome positioning. Its HPA pattern is enhanced in bone marrow and lymphoid tissue and in several progenitor populations, which provides a possible explanation for cell-cycle-related co-abundance in some samples. Its disease associations include microcephaly and neurodevelopmental phenotypes, and its literature base is substantial.
- **Conclusion**: Established evidence supports KIF11 as a mitotic spindle motor and as part of a known local mitotic subnetwork with NUF2 and ECT2. Whether mitotic activity is a central property of the complete brain-skin module, rather than a contribution from particular cell populations, remains unresolved.

#### SMARCAD1

- **Related proteins** (co-abundance neighbors): DHRS7B (0.85), GTF3C2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_10875.1, huMAP3_14801.1
- **Function (MyGene.info)**: SNF2 related chromatin remodeling ATPase with DExD box 1. This gene encodes a member of the SNF subfamily of helicase proteins. The encoded protein plays a critical role in the restoration of heterochromatin organization and propagation of epigenetic patterns following DNA replication by mediating histone H3/H4 deacetylation. Mutations in this gene are associated with adermatoglyphia. Alternatively spliced transcript variants encoding multiple isoforms h…
- **Diseases (Open Targets)**: palmoplantar keratoderma-sclerodactyly syndrome (0.600); absence of fingerprints-congenital milia syndrome (0.580); Adermatoglyphia (0.568); type 2 diabetes mellitus (0.396); isolated congenital adermatoglyphia (0.373)
- **Europe PMC papers**: 708
- **Why important**: SMARCAD1 is a chromatin-remodeling ATPase involved in heterochromatin restoration, DNA-damage processing, and epigenetic pattern propagation. It connects to GTF3C2 in the co-abundance network and appears in hu.MAP complexes (hu.MAP huMAP3_10875.1) and (hu.MAP huMAP3_14801.1). Its disease associations are especially relevant to skin biology, including adermatoglyphia and palmoplantar keratoderma-sclerodactyly syndrome, and it has a meaningful literature base.
- **Conclusion**: Established evidence supports SMARCAD1 as a chromatin and genome-maintenance factor with a particularly strong disease connection to skin development. Its inclusion supports a regulatory and epigenetic component shared by the tissues, but a direct role in coordinating the entire module is still a hypothesis.

## Module 6

**Tissue pair**: brain and skin  
**Genes (40)**: AKAP13, ARID1B, CCS, COMMD10, PDF, DAGLB, MCAT, FNBP1, FOXRED1, GALNS, GAMT, QRSL1, GNAI3, ITSN2, KLC4, MTA3, NFU1, IVNS1ABP, PDCL3, PHF14, PLEKHA5, JUP, PLXNB2, ACP2, PUS1, CTPS2, RBM45, MRPL1, MRPL11, MRPS11, SPTLC2, SSH3, STX18, SUZ12, TCEA1, GTF3C4, MIA3, TIA1, TRAF2, VAMP7

### Function

No GO/KEGG term passed global correction, and STRING reported no functional enrichment. Therefore, the module should not be assigned a formally enriched pathway. Its gene content nevertheless suggests a composite intracellular maintenance program rather than a single canonical pathway. The strongest coherent signals are mitochondrial function and translation, including mitochondrial fatty-acid handling, mitochondrial ribosome components, mitochondrial RNA modification, mitochondrial protein maturation, and respiratory-chain assembly. Additional connected processes include lysosomal glycosaminoglycan degradation, vesicle fusion and transport, endocytosis, sphingolipid metabolism, actin regulation, chromatin remodeling, RNA binding and stress-granule biology, and inflammatory signaling. The absence of a globally significant term does not invalidate the module; it indicates that the genes are functionally heterogeneous or that the module is too diffuse for over-representation enrichment to resolve one dominant annotation.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the HPA summary identifies only a small secreted fraction, and most proteins are intracellular, mitochondrial, nuclear, cytosolic, vesicular, or membrane-associated. Most genes have low tissue specificity, which is compatible with a broadly distributed cellular program. HPA nevertheless shows substantial cell-type enhancement, particularly in epithelial, neutrophil, hepatocyte, platelet, and lymphoid-related populations, with several genes showing monocyte or B-cell associations. Thus, blood or shared immune-cell content could contribute to the cross-tissue signal, but the module is not strongly characterized as an immune-cell module because most genes have low immune-cell specificity. Protein detection in both brain and skin supports genuine presence in the two tissues, although it does not establish that the same cell type drives co-abundance in both.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a limited but biologically coherent set of established relationships. MCAT is connected to MRPS11, while MRPL1, MRPL11, MRPS11, and PDF form a mitochondrial translation and nascent-protein-processing neighborhood. STX18 and VAMP7 form a known SNARE relationship linking ER and vesicular membrane traffic. These interactions support real substructures within the module, but they do not connect all module genes into one established STRING network. hu.MAP independently supports repeated mitochondrial ribosome or mitochondrial RNA-processing associations involving MCAT, MRPL1, MRPL11, MRPS11, RBM45, QRSL1, and PUS1, especially in (hu.MAP huMAP3_07939.1), (hu.MAP huMAP3_09113.1), (hu.MAP huMAP3_09483.1), (hu.MAP huMAP3_06589.1), (hu.MAP huMAP3_13468.1), (hu.MAP huMAP3_02367.1), (hu.MAP huMAP3_04652.1), (hu.MAP huMAP3_06439.1), (hu.MAP huMAP3_06550.1), (hu.MAP huMAP3_08458.1), and (hu.MAP huMAP3_05807.1). It also supports a vesicle or SNARE substructure containing STX18 and VAMP7 in (hu.MAP huMAP3_06458.1), (hu.MAP huMAP3_08929.1), (hu.MAP huMAP3_10587.1), and (hu.MAP huMAP3_13160.1), a lysosomal or extracellular-matrix-related substructure containing PLXNB2 and GALNS in (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), and a chromatin-regulatory association between SUZ12 and MTA3 in (hu.MAP huMAP3_15128.1). The partial overlap with established complexes indicates that parts of the module reflect known molecular machinery, whereas the complete cross-tissue co-abundance configuration is not explained by one documented complex.

**STRING interactions (score >= 0.7)**: 7 of 780 gene pairs: MCAT–MRPS11 (0.926); MRPL1–MRPL11 (0.998); MRPL1–MRPS11 (0.978); MRPL11–MRPS11 (0.997); MRPL11–PDF (0.714); MRPS11–PDF (0.781); STX18–VAMP7 (0.936)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07939.1 (RBM45, MCAT, MRPL1, MRPL11; 4/68); huMAP3_09113.1 (RBM45, MCAT, MRPL1, MRPL11; 4/72); huMAP3_09483.1 (MCAT, MRPL1, MRPL11; 3/74); huMAP3_06589.1 (RBM45, MRPL1, MRPL11; 3/79); huMAP3_13468.1 (FOXRED1, QRSL1, PUS1; 3/99); huMAP3_02367.1 (MRPS11, MCAT; 2/13); huMAP3_04652.1 (MRPL1, MRPL11; 2/30); huMAP3_06458.1 (VAMP7, STX18; 2/41); huMAP3_08929.1 (VAMP7, STX18; 2/44); huMAP3_10587.1 (VAMP7, STX18; 2/45); huMAP3_13160.1 (VAMP7, STX18; 2/49); huMAP3_06439.1 (MRPL1, MRPL11; 2/57); huMAP3_06775.1 (PLXNB2, GALNS; 2/60); huMAP3_06550.1 (MRPL1, MRPL11; 2/62); huMAP3_08458.1 (MRPL1, MRPL11; 2/70); huMAP3_05807.1 (MRPS11, MCAT; 2/81); huMAP3_09327.1 (PLXNB2, GALNS; 2/93); huMAP3_15128.1 (SUZ12, MTA3; 2/96)

### Novelty

The module should not be called a wholly new molecular pathway. Several of its relationships and component functions are already established by STRING and hu.MAP, particularly mitochondrial translation, SNARE-mediated trafficking, lysosomal biology, and chromatin regulation. Conversely, the data do not show that this exact brain-skin co-abundance combination has been previously reported. Absence of a complete module match in STRING or hu.MAP would not prove novelty, because those resources describe physical or curated molecular relationships rather than tissue-pair co-abundance patterns. The defensible conclusion is that this may be a new cross-tissue co-abundance signature assembled from partly known biological components, but its novelty requires comparison with published co-expression, proteomic, and tissue-pair module studies.

**Hypothesis.** Hypothesis: the module reflects a shared cellular stress-adaptation and homeostasis program operating in brain and skin. Mitochondrial translation, respiratory-chain assembly, fatty-acid and sphingolipid metabolism, and oxidative-stress handling may supply energy and protect organelle function, while lysosomal degradation and SNARE-dependent trafficking maintain turnover and membrane transport. Plexin signaling, junctional proteins, actin regulators, and endocytic factors could couple this intracellular state to cell adhesion, migration, epithelial organization, or immune-cell interactions. RNA-binding and chromatin regulators may coordinate the transcriptional and post-transcriptional response. A secondary possibility is that part of the signal reflects shared epithelial or blood-associated cell populations rather than a universal program of resident brain and skin cells. This hypothesis requires validation with cell-resolved data, perturbation experiments, and independent brain-skin cohorts.

### Important genes

#### MCAT

- **Related proteins** (co-abundance neighbors): VAMP7 (0.89), PLXNB2 (0.85), SSH3 (0.84), GALNS (0.82); STRING partners: MRPS11 (0.926)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_07939.1, huMAP3_09113.1, huMAP3_09483.1, huMAP3_02367.1, huMAP3_05807.1
- **Function (MyGene.info)**: malonyl-CoA-acyl carrier protein transacylase. The protein encoded by this gene is found exclusively in the mitochondrion, where it catalyzes the transfer of a malonyl group from malonyl-CoA to the mitochondrial acyl carrier protein. The encoded protein may be part of a fatty acid synthase complex that is more like the type II prokaryotic and plastid complexes rather than the type I human cytosolic complex. Alternative splicing results in mult…
- **Diseases (Open Targets)**: neurodegenerative disease (0.531); optic atrophy 15 (0.417); autosomal recessive optic atrophy (0.370); hereditary optic neuropathy (0.188); prostate carcinoma (0.176)
- **Europe PMC papers**: 2027
- **Why important**: MCAT is among the more connected genes in the module and bridges the mitochondrial and membrane-trafficking portions through links to VAMP7, PLXNB2, SSH3, and GALNS. Its established function is mitochondrial malonyl-group transfer to the mitochondrial acyl carrier protein, with roles in mitochondrial fatty-acid biology and mitochondrial small-ribosomal-subunit assembly. It is also supported by multiple hu.MAP complexes in (hu.MAP huMAP3_07939.1), (hu.MAP huMAP3_09113.1), (hu.MAP huMAP3_09483.1), (hu.MAP huMAP3_13468.1), (hu.MAP huMAP3_02367.1), and (hu.MAP huMAP3_05807.1), and has a substantial disease literature involving optic atrophy and neurodegenerative disease.
- **Conclusion**: Established evidence supports MCAT as a mitochondrial metabolic and assembly factor that helps connect otherwise separate module neighborhoods. Its co-abundance with trafficking and lysosomal genes is intriguing but does not establish a direct biochemical link. Hypothesis: MCAT may mark a shared demand for mitochondrial lipid and energy homeostasis in brain and skin cells.

#### MRPS11

- **Related proteins** (co-abundance neighbors): TRAF2 (0.84), AKAP13 (0.82), GAMT (0.81); STRING partners: MCAT (0.926), MRPL1 (0.978), MRPL11 (0.997), PDF (0.781)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_02367.1, huMAP3_05807.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein S11. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.539); chronic pancreatitis (0.121); subarachnoid hemorrhage (0.102); vascular disorder (0.073); hyperthyroidism (0.065)
- **Europe PMC papers**: 306
- **Why important**: MRPS11 is a central member of the best-supported STRING mitochondrial neighborhood, connecting MCAT, MRPL1, MRPL11, and PDF. It is present in hu.MAP complexes (hu.MAP huMAP3_02367.1) and (hu.MAP huMAP3_05807.1), and its established function is participation in mitochondrial ribosomal protein synthesis. Its placement gives the module a concrete mitochondrial translation axis despite the absence of globally significant GO/KEGG enrichment.
- **Conclusion**: Established evidence supports MRPS11 as a marker of mitochondrial translation and mitoribosome integrity. The co-abundance pattern is consistent with coordinated mitochondrial protein-production capacity, but it does not prove that MRPS11 regulates the other module genes. Its disease associations suggest relevance to neuronal vulnerability, although the module data alone do not connect it to a specific disease mechanism.

#### PLXNB2

- **Related proteins** (co-abundance neighbors): MCAT (0.85), ARID1B (0.81), GNAI3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location None; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: plexin B2. Members of the B class of plexins, such as PLXNB2 are transmembrane receptors that participate in axon guidance and cell migration in response to semaphorins (Perrot et al. (2002) [PubMed 12183458]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Intellectual disability (0.519); amelogenesis imperfecta (0.518); sensorineural hearing loss disorder (0.516); cutaneous melanoma (0.486); neurodegenerative disease (0.455)
- **Europe PMC papers**: 2109
- **Why important**: PLXNB2 is one of the more connected genes and links MCAT and ARID1B to GNAI3. It encodes a plexin receptor involved in semaphorin-responsive axon guidance, cell migration, adhesion, endocytosis, and neuroblast proliferation. HPA shows cell-type enhancement in epithelial populations and enrichment across monocyte and dendritic-cell categories. Its membership with GALNS in (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1) adds a lysosomal or cell-surface context, while its disease associations include neurodevelopmental and cutaneous disorders.
- **Conclusion**: Established evidence supports PLXNB2 as a cell-surface signaling and migration component with relevance to both neural and epithelial biology. Its relationship to the mitochondrial genes is a network-level association rather than an established physical complex. Hypothesis: PLXNB2 may couple cellular metabolic state to adhesion, migration, or endocytic behavior in shared brain-skin cell populations.

#### SPTLC2

- **Related proteins** (co-abundance neighbors): DAGLB (0.82), JUP (0.81), GAMT (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine palmitoyltransferase long chain base subunit 2. This gene encodes a long chain base subunit of serine palmitoyltransferase. Serine palmitoyltransferase, which consists of two different subunits, is the key enzyme in sphingolipid biosynthesis. It catalyzes the pyridoxal-5-prime-phosphate-dependent condensation of L-serine and palmitoyl-CoA to 3-oxosphinganine. Mutations in this gene were identified in patients with hereditary sensory neuropathy …
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy type 1 (0.770); neurodegenerative disease (0.558); Charcot-Marie-Tooth disease (0.490); Riley-Day syndrome (0.462); juvenile amyotrophic lateral sclerosis (0.436)
- **Europe PMC papers**: 1242
- **Why important**: SPTLC2 is the catalytic long-chain-base subunit of serine palmitoyltransferase and therefore provides a direct sphingolipid-biosynthesis interpretation. It connects DAGLB, JUP, and GAMT in the module, linking lipid metabolism with membrane organization and creatine-associated metabolism. HPA shows enhancement in several epithelial and myeloid-related cell types, and its established disease associations include hereditary sensory and autonomic neuropathy and other neurodegenerative conditions.
- **Conclusion**: Established evidence supports SPTLC2 as a biologically important membrane-lipid enzyme relevant to neuronal and epithelial integrity. Its co-abundance with junctional and trafficking-related genes is compatible with coordinated membrane remodeling, but the module does not demonstrate causal regulation. Hypothesis: sphingolipid availability may be one metabolic interface connecting mitochondrial maintenance with tissue-barrier or neuronal-membrane functions.

#### STX18

- **Related proteins** (co-abundance neighbors): PLEKHA5 (0.84); STRING partners: VAMP7 (0.936)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Plasma membrane; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_06458.1, huMAP3_08929.1, huMAP3_10587.1, huMAP3_13160.1
- **Function (MyGene.info)**: syntaxin 18. This gene encodes a member of the syntaxin family of soluble N-ethylmaleimide-sensitive factor attachment protein receptors (SNAREs) which is part of a membrane tethering complex that includes other SNAREs and several peripheral membrane proteins, and is involved in vesicular transport between the endoplasmic reticulum (ER) and the Golgi complex. The encoded protein is important for the organizati…
- **Diseases (Open Targets)**: neurodegenerative disease (0.523); Hyperhidrosis (0.265); trauma complication (0.248); osteoarthritis (0.248); sialolithiasis (0.230)
- **Europe PMC papers**: 330
- **Why important**: STX18 is a component of ER-to-Golgi SNARE machinery and is directly linked to VAMP7 by STRING. It is also present with VAMP7 in the hu.MAP groups (hu.MAP huMAP3_06458.1), (hu.MAP huMAP3_08929.1), (hu.MAP huMAP3_10587.1), and (hu.MAP huMAP3_13160.1). Its established functions include ER membrane organization, retrograde transport, and membrane fusion. HPA detects it in both brain and skin, while its network connection to PLEKHA5 places vesicle transport beside phosphoinositide-related signaling.
- **Conclusion**: Established evidence supports STX18 as a vesicle-trafficking and ER-organization component. The STX18-VAMP7 pair is the clearest trafficking submodule, but its association with mitochondrial and chromatin genes is not independently established here. Hypothesis: coordinated ER, endosomal, and lysosomal trafficking may help cells in both tissues manage organelle turnover and stress adaptation.

#### FOXRED1

- **Related proteins** (co-abundance neighbors): PLEKHA5 (0.90), PUS1 (0.83), PDCL3 (0.82), TIA1 (0.81), TRAF2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: FAD dependent oxidoreductase domain containing 1. This gene encodes a protein that contains a FAD-dependent oxidoreductase domain. The encoded protein is localized to the mitochondria and may function as a chaperone protein required for the function of mitochondrial complex I. Mutations in this gene are associated with mitochondrial complex I deficiency. Alternatively spliced transcript variants have been observed for this gene. [provided by RefS…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.783); mitochondrial complex I deficiency, nuclear type 19 (0.741); Leigh syndrome (0.662); mitochondrial disease (0.646); mitochondrial complex I deficiency, nuclear type 1 (0.630)
- **Europe PMC papers**: 308
- **Why important**: FOXRED1 is among the most connected genes and links PLEKHA5, PUS1, PDCL3, TIA1, and TRAF2. It is a mitochondrial FAD-dependent oxidoreductase-domain protein implicated in complex I assembly and mitochondrial respiratory-chain deficiency. Its HPA profile is broadly distributed and intracellular, and its disease evidence includes mitochondrial complex I deficiency and Leigh syndrome. Unlike several other important genes, it has no recorded STRING partner in this module, making its network placement especially informative as a co-abundance association rather than a known physical interaction.
- **Conclusion**: Established evidence supports FOXRED1 as a mitochondrial respiratory-chain assembly or chaperone-related factor. Its co-abundance with RNA, stress-granule, and inflammatory regulators may indicate coordinated mitochondrial stress biology, but this remains a hypothesis. The lack of STRING and hu.MAP support for its specific module connections argues for experimental validation.

## Module 7

**Tissue pair**: brain and skin  
**Genes (26)**: PRMT7, ANXA6, CAPN1, DPYSL2, HAUS4, HIP1R, KIF3A, LANCL2, LRRC40, NAGK, NBN, NCDN, NCKAP1, NLN, NUDT4, RABGGTA, PIP4K2C, RAB21, SLC27A4, SLK, STXBP1, TACC1, TBC1D17, TMEM222, ATP6V1D, VSNL1

### Function

The module does not support a single statistically established GO or KEGG function: no GO/KEGG term passed global correction. Its biological signal is nevertheless coherent at the level of individual gene annotations and network organization. The strongest interpretation is a membrane-trafficking and cytoskeletal-regulation program with neuronal and epithelial relevance. STXBP1 and VSNL1 connect regulated secretion, calcium-sensitive signaling, and neuronal activity; DPYSL2 links microtubule organization, neuronal development, and synaptic signaling; KIF3A supports kinesin-dependent intracellular and axonal transport, ciliary biology, and protein localization; SLC27A4 supports long-chain fatty-acid transport and is particularly relevant to skin barrier biology; ATP6V1D, RAB21, HIP1R, ANXA6, and TBC1D17 provide additional links to organelle acidification, endocytosis, vesicle traffic, and cytoskeletal organization. Thus, the module is best treated as a cross-tissue cellular logistics and signaling module rather than as proof of one narrowly defined pathway.

**Cell composition.** The module is not composed of secreted proteins, so a plasma-protein explanation is not supported. Most genes have low tissue specificity, while a subset is enhanced or enriched in brain, retina, esophagus, skeletal muscle, or related cell types. HPA detects protein in brain for nearly all assessed genes and in skin for most assessed genes, supporting biological relevance in both tissues but not proving that every gene is produced by the same cell type. The single-cell evidence is dominated by cell-type-enhanced rather than uniformly tissue-restricted expression, with recurrent signals in brain excitatory neurons, other brain neurons, esophageal apical or suprabasal cells, and several epithelial or developmental cell populations. Most genes have low immune-cell specificity, and only a limited subset shows immune-cell enrichment or group enrichment, including monocyte and dendritic-cell patterns for DPYSL2 and NLN. Therefore, the module does not primarily resemble a blood-cell or broadly secreted contamination signature, although shared cell composition and tissue-associated cell states could contribute to its conservation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no supplementary STRING functional enrichment. This means the co-abundance relationships are not recapitulated by the available STRING interaction network at the applied confidence threshold, so they should not be described as established physical interactions. The hu.MAP evidence provides one known complex context, (hu.MAP huMAP3_11626.1), containing STXBP1, VSNL1, and DPYSL2 among the module genes. Those three genes therefore have independent complex-level support for a neuronal or synaptic-related molecular context, while the remaining module relationships are not supported by a listed hu.MAP complex. The absence of STRING support is compatible with co-regulation, shared cell-type abundance, indirect functional coupling, or condition-dependent interactions rather than necessarily indicating biological independence.

**STRING interactions (score >= 0.7)**: 0 of 325 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11626.1 (STXBP1, VSNL1, DPYSL2; 3/42)

### Novelty

The module is potentially novel as a cross-tissue co-abundance pattern, but novelty cannot be established solely from the absence of STRING interactions or the limited hu.MAP overlap. The evidence for a new finding is that the module joins genes from several established processes—neuronal calcium and synaptic biology, microtubule transport, membrane trafficking, lipid handling, organelle acidification, and epithelial or skin biology—without a globally significant GO/KEGG term or a pre-existing STRING network explanation. At the same time, individual components and the (hu.MAP huMAP3_11626.1) complex context are already well characterized, and several genes are broadly expressed. The defensible conclusion is that the coordinated brain–skin abundance pattern may be novel, whereas the underlying gene functions and some molecular relationships are established. Replication in independent brain and skin datasets, control for cell-type composition, and experimental testing of the proposed connections would be required before claiming a newly discovered biological complex or pathway.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of membrane and organelle logistics across neuronal and skin-associated cells. In this model, KIF3A and DPYSL2 organize microtubule-dependent transport, STXBP1 and VSNL1 couple calcium-sensitive signaling to regulated vesicle release, ATP6V1D supports acidification of trafficking and synaptic compartments, and RAB21, HIP1R, ANXA6, and TBC1D17 regulate endosomal, receptor, and cytoskeletal traffic. SLC27A4 could connect this trafficking state to lipid delivery and epidermal barrier physiology, while PRMT7 and PIP4K2C may provide regulatory links through chromatin or phosphoinositide-dependent signaling. The hypothesis is that a shared cellular state involving transport, membrane remodeling, and signaling is measured in both tissues, potentially through related neuronal, epithelial, or other specialized cell populations. This is an inferred mechanism, not an established pathway demonstrated by the enrichment or interaction results.

### Important genes

#### STXBP1

- **Related proteins** (co-abundance neighbors): VSNL1 (0.83), TMEM222 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_11626.1
- **Function (MyGene.info)**: syntaxin binding protein 1. This gene encodes a syntaxin-binding protein. The encoded protein appears to play a role in release of neurotransmitters via regulation of syntaxin, a transmembrane attachment protein receptor. Mutations in this gene have been associated with infantile epileptic encephalopathy-4. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 4 (0.850); genetic developmental and epileptic encephalopathy (0.748); infantile epileptic encephalopathy (0.652); Intellectual disability (0.598); hereditary disease (0.551)
- **Europe PMC papers**: 2334
- **Why important**: STXBP1 is a high-priority anchor because it is tissue-enhanced in brain and retina, is enhanced in brain excitatory neurons and several neuroendocrine cell types, and participates in the (hu.MAP huMAP3_11626.1) hu.MAP complex with VSNL1 and DPYSL2. Its established function includes syntaxin binding, regulation of synaptic vesicle priming, exocytosis, and intracellular protein transport. It also has a strong disease connection to developmental and epileptic encephalopathy and a substantial literature.
- **Conclusion**: Established evidence supports STXBP1 as a neuronal vesicle-release and exocytosis component with major disease relevance. Its membership in this module supports a synaptic or regulated-trafficking interpretation, but the co-abundance data do not establish a direct interaction with the other module genes or show that the module is exclusively neuronal.

#### VSNL1

- **Related proteins** (co-abundance neighbors): NCDN (0.85), STXBP1 (0.83), LANCL2 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11626.1
- **Function (MyGene.info)**: visinin like 1. This gene is a member of the visinin/recoverin subfamily of neuronal calcium sensor proteins. The encoded protein is strongly expressed in granule cells of the cerebellum where it associates with membranes in a calcium-dependent manner and modulates intracellular signaling pathways of the central nervous system by directly or indirectly regulating the activity of adenylyl cyclase. Alternatively sp…
- **Diseases (Open Targets)**: mathematical ability (0.240); ventricular fibrillation (0.235); benign neoplasm (0.214); cholelithiasis (0.202); response to statin (0.126)
- **Europe PMC papers**: 839
- **Why important**: VSNL1 is tissue-enriched in brain and is cell-type-enhanced in both brain neuronal populations and basal keratinocyte or esophageal basal-cell populations, making it especially informative for a brain–skin module. It is a neuronal calcium-sensor family member that modulates intracellular signaling and associates with membranes in a calcium-dependent manner. It is also one of the three module genes represented in the (hu.MAP huMAP3_11626.1) hu.MAP complex and has a substantial literature.
- **Conclusion**: Established evidence supports VSNL1 as a calcium-sensitive signaling regulator with strong neuronal relevance and possible epithelial relevance from HPA cell-type annotations. Its role as a bridge between neuronal and skin biology in this module remains a hypothesis rather than a demonstrated mechanism.

#### DPYSL2

- **Related proteins** (co-abundance neighbors): TMEM222 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Microtubules, Cytosol; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_11626.1
- **Function (MyGene.info)**: dihydropyrimidinase like 2. This gene encodes a member of the collapsin response mediator protein family. Collapsin response mediator proteins form homo- and hetero-tetramers and facilitate neuron guidance, growth and polarity. The encoded protein promotes microtubule assembly and is required for Sema3A-mediated growth cone collapse, and also plays a role in synaptic signaling through interactions with calcium channels. This…
- **Diseases (Open Targets)**: hypertensive disorder (0.431); autosomal dominant non-syndromic intellectual disability (0.370); cardiovascular disorder (0.297); ovarian neoplasm (0.292); glomerulonephritis (0.269)
- **Europe PMC papers**: 1328
- **Why important**: DPYSL2 is tissue-enhanced in brain and cell-type-enhanced in brain neurons, oligodendrocytes, retinal cells, and selected non-neuronal populations. It is a collapsin response mediator protein involved in neuronal guidance, growth, polarity, microtubule assembly, and synaptic signaling. It is a member of the (hu.MAP huMAP3_11626.1) hu.MAP complex with STXBP1 and VSNL1, has a substantial literature, and has reported associations with neurological and intellectual-disability phenotypes.
- **Conclusion**: Established evidence supports DPYSL2 as a cytoskeletal and neuronal-signaling component. Its co-occurrence with STXBP1 and VSNL1 gives the module a credible neuronal structural and synaptic axis, but does not prove that all module edges represent a shared physical complex.

#### KIF3A

- **Related proteins** (co-abundance neighbors): SLC27A4 (0.82), ATP6V1D (0.81), NCKAP1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm, Primary cilium, Basal body, Cytosol; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 3A. Enables protein phosphatase binding activity; small GTPase binding activity; and spectrin binding activity. Involved in protein localization to cell junction and protein transport. Located in centriole and centrosome. Part of kinesin II complex. Colocalizes with spindle microtubule. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.541); ventricular septal defect (0.289); atopic eczema (0.283); alcohol drinking (0.234); asthma (0.225)
- **Europe PMC papers**: 2473
- **Why important**: KIF3A is tissue-enhanced in brain and retina, cell-type-enhanced in excitatory and inhibitory neurons and other specialized cells, and detected in both brain and skin. It is part of the kinesin II complex and has established roles in microtubule-based movement, anterograde axonal transport, intracellular protein localization, cilium assembly, and transport to cellular junctions. Its network position connects the module to SLC27A4, ATP6V1D, and NCKAP1, while its disease literature includes neurodegenerative and epithelial inflammatory contexts.
- **Conclusion**: Established evidence supports KIF3A as a transport and ciliary organizer capable of linking neuronal logistics with epithelial cell biology. Its position makes it a plausible systems-level connector in the module, although the co-abundance network alone cannot determine whether KIF3A drives the shared tissue pattern.

#### SLC27A4

- **Related proteins** (co-abundance neighbors): RABGGTA (0.83), KIF3A (0.82), HIP1R (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 27 member 4. This gene encodes a member of a family of fatty acid transport proteins, which are involved in translocation of long-chain fatty acids cross the plasma membrane. This protein is expressed at high levels on the apical side of mature enterocytes in the small intestine, and appears to be the principal fatty acid transporter in enterocytes. Clinical studies suggest this gene as a candidate gene for th…
- **Diseases (Open Targets)**: ichthyosis prematurity syndrome (0.805); neurodegenerative disease (0.485); hereditary disease (0.471); lamellar ichthyosis (0.414); autosomal recessive disease (0.370)
- **Europe PMC papers**: 947
- **Why important**: SLC27A4 is detected in both brain and skin and is enhanced across several epithelial and absorptive cell types. It is an established long-chain fatty-acid transporter and is strongly relevant to skin biology through its association with ichthyosis prematurity syndrome and other skin-barrier phenotypes. Its module neighbors include KIF3A, RABGGTA, and HIP1R, placing lipid transport alongside vesicle, membrane, and cytoskeletal processes.
- **Conclusion**: Established evidence supports SLC27A4 as a lipid-transport and epithelial-barrier gene with disease relevance. Its presence argues against interpreting the module as purely neuronal and supports a shared membrane or lipid-handling component; whether it mechanistically couples to the neuronal genes is unresolved.

#### PRMT7

- **Related proteins** (co-abundance neighbors): NLN (0.88), ATP6V1D (0.81), RAB21 (0.81), LRRC40 (0.80), CAPN1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein arginine methyltransferase 7. This gene encodes a member of the protein arginine N-methyltransferase family of proteins. The encoded enzyme transfers single methyl groups to arginine residues to generate monomethylarginines on histone proteins as well as other protein substrates. This enzyme plays a role in a wide range of biological processes, including neuronal differentiation, male germ line imprinting, small nuclear ribonu…
- **Diseases (Open Targets)**: short stature-brachydactyly-obesity-global developmental delay syndrome (0.801); hereditary disease (0.510); obesity disorder (0.509); brachydactyly (0.426); fatty liver disease (0.425)
- **Europe PMC papers**: 1274
- **Why important**: PRMT7 has the highest weighted network connectivity in the supplied module and links genes associated with proteolysis, membrane traffic, and cellular regulation. It is an arginine methyltransferase involved in methylation of histone and other protein substrates, with reported roles in neuronal differentiation, snRNP biogenesis, chromatin remodeling, transcriptional regulation, and Wnt signaling. It is detected in both brain and skin and has substantial disease and literature support.
- **Conclusion**: Established evidence supports PRMT7 as a regulatory enzyme capable of influencing gene expression and protein function. Its central network position makes it a candidate upstream coordinator, but there is no direct evidence here that its methyltransferase activity explains the module or controls the other module genes.

## Module 8

**Tissue pair**: brain and skin  
**Genes (32)**: ASF1A, CD2AP, DCAF13, DDX21, EML4, ESF1, FHL2, GCC2, GEMIN4, HOMER3, MYBBP1A, MED6, NCOR1, NLE1, NOL11, NOP2, POLDIP3, PHAX, PAK1IP1, RBM19, POLR1B, IARS1, LARS1, TACC3, TMOD3, TNRC6B, TOX4, TTK, UTP4, UTP6, WDR12, XRCC4

### Function

This is a nucleolar RNA-processing and ribosome-biogenesis module shared by brain and skin. The primary evidence is the globally corrected enrichment for ribosome biogenesis (GO:BP ribosome biogenesis; q_global = 6.26e-06), rRNA metabolic process (GO:BP rRNA metabolic process; q_global = 1.55e-05), rRNA processing (GO:BP rRNA processing; q_global = 4.51e-05), and ribonucleoprotein complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.000127). The nucleolus and related nuclear compartments are also supported by (GO:CC nucleolus; q_global = 0.000534), (GO:CC nuclear lumen; q_global = 0.00312), and (GO:CC nucleoplasm; q_global = 0.012). The module therefore most strongly represents coordinated production, maturation, and assembly of ribosomal RNA and ribonucleoprotein complexes. The broader enrichment for nucleic-acid metabolism, gene expression, and RNA metabolism (GO:BP nucleic acid metabolic process; q_global = 0.0257) (GO:BP gene expression; q_global = 0.0309) (GO:BP RNA metabolic process; q_global = 0.0434) is consistent with this interpretation but is less specific. This is a functional interpretation of co-abundance and does not by itself establish that every listed gene physically participates in one complex.

**Cell composition.** The module is not composed of secreted or plasma proteins: HPA reports no secreted genes, and protein detection is broadly present in both brain and skin. Most genes have low tissue specificity and low immune-cell specificity, arguing against a module defined primarily by a blood-cell or secreted-protein signal. However, HPA reports cell-type-enhanced expression for several genes in specialized populations, including keratinocytes, neuronal and glial populations, progenitors, and reproductive or muscle-related cell types. A small immune-associated component is present, including genes enhanced in neutrophils or other blood-cell populations, but the overall composition is more consistent with a broadly expressed nuclear housekeeping and growth-related program than with blood contamination. The brain-skin conservation may therefore reflect shared cellular demand for ribosome production, while sample cellular composition could still influence the observed co-abundance.

**GO/KEGG enrichment**: 12 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP ribosome biogenesis | 6.26e-06 | DCAF13, DDX21, ESF1, GEMIN4, MYBBP1A, NLE1, NOL11, NOP2, PAK1IP1, UTP4, UTP6, WDR12 |
| GO:BP rRNA metabolic process | 1.55e-05 | DCAF13, DDX21, ESF1, GEMIN4, NOL11, NOP2, PAK1IP1, POLR1B, UTP4, UTP6, WDR12 |
| GO:BP rRNA processing | 4.51e-05 | DCAF13, DDX21, ESF1, GEMIN4, NOL11, NOP2, PAK1IP1, UTP4, UTP6, WDR12 |
| GO:BP ribonucleoprotein complex biogenesis | 0.000127 | DCAF13, DDX21, ESF1, GEMIN4, MYBBP1A, NLE1, NOL11, NOP2, PAK1IP1, UTP4, UTP6, WDR12 |
| GO:CC nucleolus | 0.000534 | CD2AP, DCAF13, DDX21, ESF1, GEMIN4, MYBBP1A, NLE1, NOL11, NOP2, PAK1IP1, POLR1B, RBM19, UTP4, UTP6, WDR12 |
| GO:CC membraneless organelle | 0.000817 | ASF1A, CD2AP, DCAF13, DDX21, EML4, ESF1, FHL2, GEMIN4, LARS1, MYBBP1A, NCOR1, NLE1, NOL11, NOP2, PAK1IP1, PHAX, POLDIP3, POLR1B, RBM19, TACC3, TMOD3, TNRC6B, TOX4, TTK, UTP4, UTP6, WDR12, XRCC4 |
| GO:CC intracellular membraneless organelle | 0.000817 | ASF1A, CD2AP, DCAF13, DDX21, EML4, ESF1, FHL2, GEMIN4, LARS1, MYBBP1A, NCOR1, NLE1, NOL11, NOP2, PAK1IP1, PHAX, POLDIP3, POLR1B, RBM19, TACC3, TMOD3, TNRC6B, TOX4, TTK, UTP4, UTP6, WDR12, XRCC4 |
| GO:CC nuclear lumen | 0.00312 | ASF1A, CD2AP, DCAF13, DDX21, ESF1, FHL2, GCC2, GEMIN4, IARS1, LARS1, MED6, MYBBP1A, NCOR1, NLE1, NOL11, NOP2, PAK1IP1, PHAX, POLDIP3, POLR1B, RBM19, TNRC6B, UTP4, UTP6, WDR12, XRCC4 |
| GO:CC nucleoplasm | 0.012 | ASF1A, DCAF13, DDX21, ESF1, FHL2, GCC2, GEMIN4, IARS1, LARS1, MED6, MYBBP1A, NCOR1, NLE1, NOL11, NOP2, PHAX, POLDIP3, POLR1B, RBM19, TNRC6B, UTP4, UTP6, WDR12, XRCC4 |
| GO:BP nucleic acid metabolic process | 0.0257 | ASF1A, DCAF13, DDX21, ESF1, FHL2, GEMIN4, IARS1, LARS1, MED6, MYBBP1A, NCOR1, NOL11, NOP2, PAK1IP1, PHAX, POLR1B, TNRC6B, TOX4, UTP4, UTP6, WDR12, XRCC4 |
| GO:BP gene expression | 0.0309 | CD2AP, DCAF13, DDX21, ESF1, FHL2, GEMIN4, HOMER3, IARS1, LARS1, MED6, MYBBP1A, NCOR1, NOL11, NOP2, PAK1IP1, PHAX, POLDIP3, POLR1B, TNRC6B, TOX4, UTP4, UTP6, WDR12, XRCC4 |
| GO:BP RNA metabolic process | 0.0434 | DCAF13, DDX21, ESF1, FHL2, GEMIN4, IARS1, LARS1, MED6, MYBBP1A, NCOR1, NOL11, NOP2, PAK1IP1, PHAX, POLR1B, TNRC6B, TOX4, UTP4, UTP6, WDR12 |

### STRING and hu.MAP

STRING provides strong internal support for a coherent ribosome-biogenesis network. The densest relationships connect DCAF13, ESF1, NOL11, UTP4, UTP6, WDR12, NOP2, PAK1IP1, POLR1B, RBM19, MYBBP1A, DDX21, and NLE1, matching the primary GO/KEGG interpretation. STRING functional results independently recover preribosome and ribosome-biogenesis processes (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 3.37e-07) (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 7.26e-07) (STRING Process Ribosome biogenesis; within-query FDR = 3.36e-06), nucleolar localization (STRING COMPARTMENTS Nucleolus; within-query FDR = 1.46e-05), and rRNA processing (STRING Keyword rRNA processing; within-query FDR = 4.39e-05), (STRING Process rRNA metabolic process; within-query FDR = 7.75e-05), and (STRING Process rRNA processing; within-query FDR = 0.00026). These STRING results are supplementary rather than global enrichment evidence. hu.MAP identifies partial overlaps rather than a single complete module: UTP4 and NOL11 recur in several complexes (hu.MAP huMAP3_14364.1), (hu.MAP huMAP3_01743.1), and (hu.MAP huMAP3_14264.1), while IARS1 and LARS1 recur in aminoacyl-tRNA-synthetase complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Thus, the network combines a well-supported nucleolar ribosome-biogenesis core with peripheral links involving translation, RNA handling, chromatin, DNA repair, cytoskeletal, and cell-cycle functions.

**STRING interactions (score >= 0.7)**: 46 of 496 gene pairs: DCAF13–ESF1 (0.853); DCAF13–NLE1 (0.751); DCAF13–NOL11 (0.968); DCAF13–PAK1IP1 (0.828); DCAF13–UTP4 (0.999); DCAF13–UTP6 (0.998); DCAF13–WDR12 (0.898); DDX21–MYBBP1A (0.963); DDX21–NOP2 (0.761); DDX21–POLR1B (0.741); DDX21–WDR12 (0.839); ESF1–NOP2 (0.823); ESF1–PAK1IP1 (0.752); ESF1–UTP4 (0.864); ESF1–UTP6 (0.995); GEMIN4–PHAX (0.764); IARS1–LARS1 (0.999); MYBBP1A–NOP2 (0.864); MYBBP1A–POLR1B (0.947); MYBBP1A–RBM19 (0.813); MYBBP1A–UTP4 (0.923); MYBBP1A–UTP6 (0.754); NLE1–NOP2 (0.748); NLE1–POLR1B (0.784); NLE1–WDR12 (0.859); NOL11–UTP4 (0.999); NOL11–UTP6 (0.957); NOL11–WDR12 (0.78); NOP2–PAK1IP1 (0.833); NOP2–POLR1B (0.879); NOP2–RBM19 (0.796); NOP2–UTP4 (0.753); NOP2–UTP6 (0.756); NOP2–WDR12 (0.975); PAK1IP1–UTP4 (0.827); PAK1IP1–WDR12 (0.869); POLR1B–RBM19 (0.864); POLR1B–UTP4 (0.838); POLR1B–WDR12 (0.86); RBM19–UTP4 (0.856); RBM19–UTP6 (0.793); RBM19–WDR12 (0.902); TACC3–TTK (0.736); UTP4–UTP6 (0.999); UTP4–WDR12 (0.939); UTP6–WDR12 (0.881)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 3.37e-07, 11 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 7.26e-07, 10 genes); Process Ribosome biogenesis (FDR = 3.36e-06, 12 genes); COMPARTMENTS Nucleolus (FDR = 1.46e-05, 14 genes); COMPARTMENTS Intracellular non-membrane-bounded organelle (FDR = 1.46e-05, 25 genes); Keyword Ribosome biogenesis (FDR = 4.39e-05, 7 genes); Keyword rRNA processing (FDR = 4.39e-05, 7 genes); COMPARTMENTS Nuclear lumen (FDR = 5.26e-05, 19 genes); Process rRNA metabolic process (FDR = 7.75e-05, 10 genes); Component Nucleolus (FDR = 9.27e-05, 15 genes); Component Intracellular non-membrane-bounded organelle (FDR = 9.27e-05, 27 genes); Component Nuclear lumen (FDR = 0.00022, 26 genes); Process rRNA processing (FDR = 0.00026, 9 genes); Process ncRNA metabolic process (FDR = 0.00052, 12 genes); Component Nucleoplasm (FDR = 0.00095, 24 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14364.1 (UTP4, NOL11; 2/4); huMAP3_01743.1 (UTP4, NOL11; 2/6); huMAP3_02637.1 (IARS1, LARS1; 2/14); huMAP3_13688.1 (IARS1, LARS1; 2/14); huMAP3_14264.1 (UTP4, NOL11; 2/20)

### Novelty

The module is unlikely to be a wholly unknown molecular program because many of its central genes and relationships are already represented in STRING, and UTP4-NOL11 co-membership is represented in hu.MAP (hu.MAP huMAP3_14364.1), (hu.MAP huMAP3_01743.1), and (hu.MAP huMAP3_14264.1). The strong agreement between co-abundance, globally corrected enrichment, nucleolar localization, and known interaction evidence supports a biologically real ribosome-biogenesis signal rather than an annotation artifact. At the same time, the specific conserved brain-skin co-abundance configuration may still be novel. That claim cannot be established from absence in STRING or hu.MAP alone, because those resources emphasize previously reported physical or functional associations and may not capture tissue-pair co-abundance structure. The appropriate conclusion is that the underlying biology is established, whereas the tissue-shared network organization is a candidate new observation requiring replication in independent cohorts and testing against cell-composition and technical covariates.

**Hypothesis.** Hypothesis: brain and skin cells with sustained renewal, differentiation, or specialized functional demand co-regulate a nucleolar ribosome-production program. A core involving NOL11, UTP4, UTP6, WDR12, DCAF13, NOP2, DDX21, and related factors may coordinate rRNA transcription, processing, and ribosome assembly, while peripheral genes connect this program to translation, chromatin regulation, DNA repair, cytoskeletal organization, and cell-cycle control. The shared module could therefore reflect a conserved response to biosynthetic and proliferative demand across both tissues. This remains a hypothesis: co-abundance does not prove direct physical interaction, causal regulation, or identical cellular origin in brain and skin.

### Important genes

#### NOL11

- **Related proteins** (co-abundance neighbors): POLR1B (0.88), UTP4 (0.87), WDR12 (0.86), ESF1 (0.85), TMOD3 (0.83), PHAX (0.81), NLE1 (0.81); STRING partners: DCAF13 (0.968), UTP4 (0.999), UTP6 (0.957), WDR12 (0.78)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_14364.1, huMAP3_01743.1, huMAP3_14264.1
- **Function (MyGene.info)**: nucleolar protein 11. Enables RNA binding activity. Involved in maturation of SSU-rRNA and positive regulation of transcription of nucleolar large rRNA by RNA polymerase I. Located in nucleolus. Part of t-UTP complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: diabetes mellitus (0.100); type 2 diabetes mellitus (0.100); atrial fibrillation (0.087); ulcerative colitis (0.011); cancer (0.011)
- **Europe PMC papers**: 240
- **Why important**: NOL11 is a central network connector and is present across every globally corrected enrichment category (12 globally significant GO/KEGG terms, q_global 6.26e-06–0.0434; see the table). It is a nucleolar RNA-binding protein involved in small-subunit rRNA maturation and regulation of nucleolar ribosomal-RNA transcription. It is also repeatedly represented in STRING ribosome-biogenesis and nucleolar results (15 supplementary STRING terms; within-query FDR 3.37e-07–0.00095) and in several hu.MAP complexes (hu.MAP huMAP3_14364.1), (hu.MAP huMAP3_01743.1), and (hu.MAP huMAP3_14264.1). Its substantial literature base and disease associations further support it as an informative anchor for the module.
- **Conclusion**: Established evidence identifies NOL11 as a nucleolar ribosome-biogenesis component and a structural anchor of this module. The co-abundance result is consistent with coordinated rRNA production in brain and skin, but does not establish that NOL11 drives the module.

#### UTP4

- **Related proteins** (co-abundance neighbors): NOL11 (0.87); STRING partners: DCAF13 (0.999), ESF1 (0.864), MYBBP1A (0.923), NOL11 (0.999), NOP2 (0.753), PAK1IP1 (0.827), POLR1B (0.838), RBM19 (0.856), UTP6 (0.999), WDR12 (0.939)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_14364.1, huMAP3_01743.1, huMAP3_14264.1
- **Function (MyGene.info)**: UTP4 small subunit processome component. This gene encodes a WD40-repeat-containing protein that is localized to the nucleolus. Mutation of this gene causes North American Indian childhood cirrhosis, a severe intrahepatic cholestasis that results in transient neonatal jaundice, and progresses to periportal fibrosis and cirrhosis in childhood and adolescence. Alternative splicing results in multiple transcript variants. [provided by RefSe…
- **Diseases (Open Targets)**: hereditary North American Indian childhood cirrhosis (0.420); cardiovascular disorder (0.101); basal cell carcinoma (0.079); hypertensive disorder (0.064); osteosarcoma (0.052)
- **Europe PMC papers**: 214
- **Why important**: UTP4 is a core small-subunit processome component with a nucleolar location and functions in rRNA maturation and small-subunit biogenesis. It has very strong STRING support with DCAF13, NOL11, UTP6, WDR12, and other module members, and it recurs in the hu.MAP complexes (hu.MAP huMAP3_14364.1), (hu.MAP huMAP3_01743.1), and (hu.MAP huMAP3_14264.1). UTP4 appears in every globally corrected term (12 globally significant GO/KEGG terms, q_global 6.26e-06–0.0434; see the table), making it one of the clearest links between network structure and functional annotation. Its disease association with childhood liver disease illustrates the importance of impaired ribosome biogenesis in human pathology.
- **Conclusion**: Established evidence places UTP4 in the nucleolar small-subunit processome and strongly supports its membership in the conserved module core. It is a plausible marker of the module, but causality in the brain-skin co-abundance pattern remains untested.

#### DDX21

- **Related proteins** (co-abundance neighbors): NOP2 (0.84), MYBBP1A (0.81), TACC3 (0.81); STRING partners: MYBBP1A (0.963), NOP2 (0.761), POLR1B (0.741), WDR12 (0.839)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 is a nucleolar RNA helicase involved in RNA processing and regulation of ribosomal-RNA transcription. It connects to NOP2, MYBBP1A, and POLR1B in STRING and is represented across the principal ribosome-biogenesis terms (12 globally significant GO/KEGG terms, q_global 6.26e-06–0.0434; see the table). Its HPA profile includes enhancement in basal and suprabasal keratinocytes, providing a biologically relevant link to skin while protein detection is also reported in brain. Its extensive literature and disease associations make it a strong candidate for interpreting regulation or stress responses within the module.
- **Conclusion**: Established evidence supports DDX21 as an RNA-processing and nucleolar regulator that bridges rRNA maturation with transcriptional control. Its keratinocyte association suggests a possible tissue-cellular contribution, but the module does not prove that DDX21 specifically explains the shared brain-skin signal.

#### NOP2

- **Related proteins** (co-abundance neighbors): DDX21 (0.84); STRING partners: DDX21 (0.761), ESF1 (0.823), MYBBP1A (0.864), NLE1 (0.748), PAK1IP1 (0.833), POLR1B (0.879), RBM19 (0.796), UTP4 (0.753), UTP6 (0.756), WDR12 (0.975)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP2 nucleolar protein. Enables RNA binding activity. Involved in positive regulation of cell population proliferation; regulation of signal transduction by p53 class mediator; and ribosomal large subunit assembly. Located in nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.273); nonpapillary renal cell carcinoma (0.097); neoplasm (0.097); cancer (0.091); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 2120
- **Why important**: NOP2 is a nucleolar RNA-binding protein involved in large-subunit assembly, rRNA processing, and maturation of large-subunit rRNA. It is linked by STRING to many core members, including DDX21, NOP2-associated processing factors, POLR1B, UTP4, UTP6, and WDR12, and is present in all primary enrichment categories (12 globally significant GO/KEGG terms, q_global 6.26e-06–0.0434; see the table). HPA reports detection in brain and skin and enhancement across several neuronal and glial cell types. Its large literature volume and links to proliferation and disease make it an important readout of nucleolar biosynthetic activity.
- **Conclusion**: Established evidence supports NOP2 as a central large-subunit rRNA maturation factor with relevance to neural cell populations. Its coordinated abundance may indicate altered ribosome assembly demand, but it should not be interpreted as evidence of a tissue-specific disease mechanism without direct experiments.

#### WDR12

- **Related proteins** (co-abundance neighbors): NOL11 (0.86), PAK1IP1 (0.80); STRING partners: DCAF13 (0.898), DDX21 (0.839), NLE1 (0.859), NOL11 (0.78), NOP2 (0.975), PAK1IP1 (0.869), POLR1B (0.86), RBM19 (0.902), UTP4 (0.939), UTP6 (0.881)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 12. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); poisoning (0.233); non-autoimmune hemolytic anemia (0.214); coronary artery disorder (0.210); myocardial infarction (0.168)
- **Europe PMC papers**: 602
- **Why important**: WDR12 is a WD-repeat protein involved in rRNA processing, ribosome biogenesis, and large-subunit biogenesis. It is connected in STRING to a broad set of module members, including DCAF13, DDX21, NLE1, NOP2, PAK1IP1, POLR1B, RBM19, UTP4, and UTP6. It appears across all globally corrected GO/KEGG categories (12 globally significant GO/KEGG terms, q_global 6.26e-06–0.0434; see the table) and across the STRING ribosome-biogenesis and nucleolar results (15 supplementary STRING terms; within-query FDR 3.37e-07–0.00095). Its network placement and broad functional evidence make it a strong representative of the module's conserved core.
- **Conclusion**: Established evidence identifies WDR12 as a multiprotein-complex component of ribosome biogenesis and supports its role as a core module marker. A mechanistic role in coordinating the brain-skin module is plausible but remains a hypothesis rather than a demonstrated causal function.

## Module 9

**Tissue pair**: brain and skin  
**Genes (46)**: C2orf49, BAZ1A, BPTF, LIG3, ERBIN, HAUS7, HEATR1, KRT18, KRT8, KRI1, LIMA1, MED24, MICALL1, IGF2R, NELFE, NIPBL, NVL, DLAT, PAAF1, PHACTR4, PLBD2, PPHLN1, CDC40, PUM1, RABEPK, RBM28, RBM6, RBM7, UPF3B, POLR1A, PDCD11, RSF1, MRPS22, SAP30, SCAF11, SNAP23, SUN1, THOC1, THOC6, TJAP1, TPX2, TXNL4A, UBR5, YLPM1, ZMYM4, ZNF598

### Function

The module is best interpreted as a conserved nuclear gene-expression and RNA-metabolism module. The primary evidence is the globally corrected enrichment for nuclear protein-containing complexes (GO:CC nuclear protein-containing complex; q_global = 0.00401), nuclear lumen (GO:CC nuclear lumen; q_global = 0.0116), nucleic-acid biosynthesis (GO:BP nucleic acid biosynthetic process; q_global = 0.0164), RNA biosynthesis (GO:BP RNA biosynthetic process; q_global = 0.0254), and related organelle-lumen terms (GO:CC membrane-enclosed lumen; q_global = 0.0309) (GO:CC organelle lumen; q_global = 0.0309) (GO:CC intracellular organelle lumen; q_global = 0.0309), together with nucleic-acid metabolism and nucleobase-containing compound biosynthesis (GO:BP nucleic acid metabolic process; q_global = 0.0473) (GO:BP nucleobase-containing compound biosynthetic process; q_global = 0.0477). The gene content supports several connected activities rather than a single linear pathway: chromatin remodeling and transcriptional regulation, RNA polymerase activity, pre-mRNA splicing and export, RNA surveillance, nucleolar ribosome and rRNA biogenesis, DNA repair, and cell-cycle or spindle control. The STRING results independently support nuclear complexes and the ISWI-type complex (STRING Component Nuclear protein-containing complex; within-query FDR = 0.006), (STRING Component Nuclear lumen; within-query FDR = 0.0088), (STRING Pfam WSTF, HB1, Itc1p, MBD9 motif 1; within-query FDR = 0.0239), and (STRING Component ISWI-type complex; within-query FDR = 0.0488), but are supplementary rather than globally corrected enrichment evidence.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. The HPA evidence places most members in low-tissue-specificity categories, with predominantly nuclear, nucleolar, nucleoplasmic, nuclear-speckle, or nuclear-membrane localizations. Only PLBD2 is annotated as secreted-related, with intracellular and membrane detection. The module therefore does not look like a blood-plasma signature. Most genes also have low immune-cell specificity, although selected members show enhancement in neutrophils or other blood-related cell types, and several show enhancement in proliferative or germ-cell populations. Because nearly all module proteins are detected in both brain and skin, the shared signal is more plausibly a broadly used intracellular program or a shared proliferative, epithelial, or stromal cell-state program than a module dominated by circulating blood cells. Sample cell composition remains a possible contributor.

**GO/KEGG enrichment**: 9 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC nuclear protein-containing complex | 0.00401 | BAZ1A, BPTF, CDC40, HEATR1, MED24, NELFE, NIPBL, NVL, PAAF1, PDCD11, POLR1A, RBM28, RSF1, SAP30, SUN1, THOC1, THOC6, TXNL4A, UPF3B |
| GO:CC nuclear lumen | 0.0116 | BAZ1A, BPTF, CDC40, ERBIN, HAUS7, HEATR1, KRI1, KRT18, KRT8, LIG3, MED24, NELFE, NIPBL, NVL, PAAF1, PDCD11, POLR1A, PPHLN1, PUM1, RBM28, RBM7, RSF1, SAP30, SCAF11, SNAP23, THOC1, THOC6, TPX2, TSLIG2, TXNL4A, UBR5, UPF3B, YLPM1 |
| GO:BP nucleic acid biosynthetic process | 0.0164 | BAZ1A, BPTF, CDC40, HEATR1, KRI1, LIG3, MED24, NELFE, NIPBL, NVL, PAAF1, PDCD11, POLR1A, PPHLN1, PUM1, RBM28, RBM6, RBM7, RSF1, SAP30, SCAF11, THOC1, THOC6, TSLIG2, TXNL4A, UPF3B |
| GO:BP RNA biosynthetic process | 0.0254 | BAZ1A, BPTF, CDC40, HEATR1, KRI1, MED24, NELFE, NIPBL, NVL, PAAF1, PDCD11, POLR1A, PPHLN1, PUM1, RBM28, RBM6, RBM7, RSF1, SAP30, SCAF11, THOC1, THOC6, TSLIG2, TXNL4A, UPF3B |
| GO:CC membrane-enclosed lumen | 0.0309 | BAZ1A, BPTF, CDC40, DLAT, ERBIN, HAUS7, HEATR1, IGF2R, KRI1, KRT18, KRT8, LIG3, MED24, MRPS22, NELFE, NIPBL, NVL, PAAF1, PDCD11, PLBD2, POLR1A, PPHLN1, PUM1, RBM28, RBM7, RSF1, SAP30, SCAF11, SNAP23, THOC1, THOC6, TPX2, TSLIG2, TXNL4A, UBR5, UPF3B, YLPM1 |
| GO:CC organelle lumen | 0.0309 | BAZ1A, BPTF, CDC40, DLAT, ERBIN, HAUS7, HEATR1, IGF2R, KRI1, KRT18, KRT8, LIG3, MED24, MRPS22, NELFE, NIPBL, NVL, PAAF1, PDCD11, PLBD2, POLR1A, PPHLN1, PUM1, RBM28, RBM7, RSF1, SAP30, SCAF11, SNAP23, THOC1, THOC6, TPX2, TSLIG2, TXNL4A, UBR5, UPF3B, YLPM1 |
| GO:CC intracellular organelle lumen | 0.0309 | BAZ1A, BPTF, CDC40, DLAT, ERBIN, HAUS7, HEATR1, IGF2R, KRI1, KRT18, KRT8, LIG3, MED24, MRPS22, NELFE, NIPBL, NVL, PAAF1, PDCD11, PLBD2, POLR1A, PPHLN1, PUM1, RBM28, RBM7, RSF1, SAP30, SCAF11, SNAP23, THOC1, THOC6, TPX2, TSLIG2, TXNL4A, UBR5, UPF3B, YLPM1 |
| GO:BP nucleic acid metabolic process | 0.0473 | BAZ1A, BPTF, CDC40, HEATR1, KRI1, LIG3, MED24, NELFE, NIPBL, NVL, PAAF1, PDCD11, POLR1A, PPHLN1, PUM1, RBM28, RBM6, RBM7, RSF1, SAP30, SCAF11, THOC1, THOC6, TSLIG2, TXNL4A, UBR5, UPF3B, YLPM1 |
| GO:BP nucleobase-containing compound biosynthetic process | 0.0477 | BAZ1A, BPTF, CDC40, DLAT, HEATR1, KRI1, LIG3, MED24, NELFE, NIPBL, NVL, PAAF1, PDCD11, POLR1A, PPHLN1, PUM1, RBM28, RBM6, RBM7, RSF1, SAP30, SCAF11, THOC1, THOC6, TSLIG2, TXNL4A, UPF3B |

### STRING and hu.MAP

STRING contains a coherent but incomplete set of established relationships. Strong links connect the BAZ1A–BPTF–RSF1 chromatin-remodeling group, NIPBL with BPTF and RSF1, HEATR1 with KRI1, PDCD11, POLR1A, and RBM28, CDC40 with TXNL4A and UPF3B, THOC1 with THOC6, and KRT8 with KRT18. These links indicate that parts of the co-abundance module recapitulate known molecular complexes or functional neighborhoods, especially chromatin remodeling, nucleolar RNA processing, splicing, and epithelial intermediate filaments. The many module pairs without high-confidence STRING links show that the co-abundance network is broader than a catalog of direct physical interactions and may include indirect, shared-regulation, or cell-state relationships. hu.MAP provides partial support for RNA-processing and RNA-binding assemblies involving YLPM1, RBM6, and PPHLN1 (hu.MAP huMAP3_08625.1) (hu.MAP huMAP3_01533.1) (hu.MAP huMAP3_09569.1) (hu.MAP huMAP3_07030.1) (hu.MAP huMAP3_08950.1) (hu.MAP huMAP3_09973.1) (hu.MAP huMAP3_10643.1) (hu.MAP huMAP3_09895.1) (hu.MAP huMAP3_09778.1) (hu.MAP huMAP3_10098.1) (hu.MAP huMAP3_14523.1), the SUN1–BAZ1A group (hu.MAP huMAP3_08267.1) (hu.MAP huMAP3_10419.1), THOC1–THOC6 assemblies (hu.MAP huMAP3_04932.1) (hu.MAP huMAP3_09184.1) and (hu.MAP huMAP3_12548.1) (hu.MAP huMAP3_09101.1) (hu.MAP huMAP3_10299.1), spliceosomal CDC40–TXNL4A assemblies (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_13482.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1), and chromatin or DNA-repair assemblies containing RSF1, BAZ1A, BPTF, SAP30, KRT18, or LIG3 (hu.MAP huMAP3_13854.1) (hu.MAP huMAP3_11539.1) (hu.MAP huMAP3_12711.1) and (hu.MAP huMAP3_13482.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1) (hu.MAP huMAP3_09943.1) (hu.MAP huMAP3_15128.1). These are partial overlaps, so they support modular organization without proving that the entire co-abundance module is one physical complex.

**STRING interactions (score >= 0.7)**: 20 of 1035 gene pairs: BAZ1A–BPTF (0.935); BAZ1A–RSF1 (0.907); BPTF–NIPBL (0.806); BPTF–RSF1 (0.918); CDC40–TXNL4A (0.825); CDC40–UPF3B (0.816); HEATR1–KRI1 (0.758); HEATR1–PDCD11 (0.999); HEATR1–POLR1A (0.938); HEATR1–RBM28 (0.793); KRI1–PDCD11 (0.797); KRT18–KRT8 (0.999); NIPBL–RSF1 (0.72); NIPBL–SCAF11 (0.73); NVL–POLR1A (0.74); NVL–RBM28 (0.902); PDCD11–POLR1A (0.985); PDCD11–RBM28 (0.976); POLR1A–RBM28 (0.738); THOC1–THOC6 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Nuclear protein-containing complex (FDR = 0.006, 18 genes); Keyword Phosphoprotein (FDR = 0.0083, 44 genes); Component Nuclear lumen (FDR = 0.0088, 32 genes); Component Intracellular organelle lumen (FDR = 0.0195, 36 genes); Keyword Isopeptide bond (FDR = 0.02, 18 genes); Pfam WSTF, HB1, Itc1p, MBD9 motif 1 (FDR = 0.0239, 3 genes); Keyword Nucleus (FDR = 0.0299, 29 genes); COMPARTMENTS Nucleus (FDR = 0.038, 32 genes); Component ISWI-type complex (FDR = 0.0488, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08625.1 (YLPM1, RBM6, PPHLN1; 3/6); huMAP3_01533.1 (YLPM1, RBM6, PPHLN1; 3/7); huMAP3_09569.1 (YLPM1, RBM6, PPHLN1; 3/9); huMAP3_07030.1 (YLPM1, RBM6, PPHLN1; 3/10); huMAP3_08950.1 (YLPM1, RBM6, PPHLN1; 3/10); huMAP3_09973.1 (YLPM1, RBM6, PPHLN1; 3/10); huMAP3_10643.1 (YLPM1, RBM6, PPHLN1; 3/13); huMAP3_09895.1 (YLPM1, RBM6, PPHLN1; 3/14); huMAP3_09778.1 (YLPM1, RBM6, PPHLN1; 3/16); huMAP3_10098.1 (YLPM1, RBM6, PPHLN1; 3/17); huMAP3_14523.1 (YLPM1, RBM6, PPHLN1; 3/33); huMAP3_08267.1 (SUN1, BAZ1A; 2/3); huMAP3_10419.1 (SUN1, BAZ1A; 2/4); huMAP3_02281.1 (YLPM1, PPHLN1; 2/5); huMAP3_06755.1 (YLPM1, PPHLN1; 2/6); huMAP3_09844.1 (YLPM1, PPHLN1; 2/6); huMAP3_09463.1 (RBM6, PPHLN1; 2/7); huMAP3_06354.1 (YLPM1, RBM6; 2/7); huMAP3_08096.1 (YLPM1, RBM6; 2/9); huMAP3_04932.1 (THOC6, THOC1; 2/14); huMAP3_09184.1 (THOC6, THOC1; 2/14); huMAP3_10307.1 (ZNF598, C2orf49; 2/20); huMAP3_12548.1 (THOC6, THOC1; 2/21); huMAP3_09101.1 (THOC6, THOC1; 2/22); huMAP3_10299.1 (THOC6, THOC1; 2/22); huMAP3_10631.1 (ZNF598, C2orf49; 2/28); huMAP3_11111.1 (ZNF598, C2orf49; 2/29); huMAP3_13854.1 (LIG3, RSF1; 2/29); huMAP3_11539.1 (ZMYM4, RSF1; 2/32); huMAP3_12711.1 (KRT18, RSF1; 2/35); huMAP3_10789.1 (THOC6, THOC1; 2/37); huMAP3_14270.1 (ZNF598, C2orf49; 2/47); huMAP3_14559.1 (ZNF598, C2orf49; 2/47); huMAP3_08501.1 (CDC40, TXNL4A; 2/47); huMAP3_13482.1 (SAP30, BPTF; 2/50); huMAP3_09504.1 (CDC40, TXNL4A; 2/51); huMAP3_09945.1 (CDC40, TXNL4A; 2/61); huMAP3_09943.1 (THOC6, THOC1; 2/78); huMAP3_15128.1 (SAP30, BPTF; 2/96)

### Novelty

The module is plausibly a new systems-level finding, but not because its individual genes or all of its relationships are novel. Several relationships and complexes are already represented in STRING and hu.MAP, including chromatin-remodeling, nucleolar, RNA-export, spliceosomal, DNA-repair, and keratin-related components. What may be new is the conserved brain–skin co-abundance organization that links these otherwise distinct nuclear, RNA-processing, chromatin, cytoskeletal, and epithelial components. The evidence supports novelty at the level of cross-tissue co-abundance architecture and module interpretation, not a claim that the proteins or complexes themselves were previously unknown. Absence of a relationship from STRING or hu.MAP should not be treated as proof of novelty.

**Hypothesis.** Hypothesis: in both brain and skin, a shared cellular state coordinates chromatin accessibility and transcription with RNA maturation, export, surveillance, and ribosome production, while coupling these processes to cell-cycle, cytoskeletal, nuclear-envelope, and epithelial-barrier functions. NIPBL, BAZ1A, BPTF, and RSF1 could organize the chromatin and long-range transcriptional layer; THOC1, THOC6, CDC40, TXNL4A, RBM6, and RBM7 could coordinate RNA processing and export; NVL, HEATR1, POLR1A, PDCD11, RBM28, and KRI1 could support nucleolar and ribosome-biogenesis demands. PPHLN1, KRT8, KRT18, SUN1, and ERBIN could connect this nuclear program to epithelial integrity, nuclear mechanics, and cell-state remodeling. This is a mechanistic model generated from co-abundance and annotations, not proof of direct regulation or physical assembly.

### Important genes

#### NVL

- **Related proteins** (co-abundance neighbors): NIPBL (0.90), RSF1 (0.85), THOC6 (0.83), ZMYM4 (0.82), YLPM1 (0.82), ZNF598 (0.81), NELFE (0.81), RBM7 (0.81), UBR5 (0.81); STRING partners: POLR1A (0.74), RBM28 (0.902)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nuclear VCP like. This gene encodes a member of the AAA (ATPases associated with diverse cellular activities) superfamily. Multiple transcript variants encoding different isoforms have been found for this gene. Two encoded proteins, described as major and minor isoforms, have been localized to distinct regions of the nucleus. The largest encoded protein (major isoform) has been localized to the nucleolus and shown …
- **Diseases (Open Targets)**: neurodegenerative disease (0.459); Parkinson disease (0.370); lysosomal storage disease (0.370); Alzheimer disease (0.370); glioblastoma (0.263)
- **Europe PMC papers**: 717
- **Why important**: NVL is the most centrally connected member in the supplied module ranking and links chromatin, RNA-processing, RNA-binding, and nucleolar-associated genes. It appears in every globally corrected GO term (9 globally significant GO/KEGG terms, q_global 0.00401–0.0477; see the table) and in multiple supplementary STRING terms (5 supplementary STRING terms; within-query FDR 0.006–0.02), (STRING Keyword Nucleus; within-query FDR = 0.0299), and (STRING COMPARTMENTS Nucleus; within-query FDR = 0.038). Its nucleolar localization and annotation in ribosome biogenesis and rRNA processing give it a strong functional bridge between the module's nucleolar and broader nuclear programs. Its disease links include neurodegenerative and Parkinson disease categories, and it has substantial literature.
- **Conclusion**: Established evidence supports NVL as a central nuclear and nucleolar RNA or ribosome-biogenesis component. It is a strong candidate for coordinating the module, but co-abundance does not establish that NVL regulates the other genes.

#### BAZ1A

- **Related proteins** (co-abundance neighbors): ZMYM4 (0.84), KRT8 (0.83), RBM7 (0.81), SCAF11 (0.81); STRING partners: BPTF (0.935), RSF1 (0.907)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_08267.1, huMAP3_10419.1
- **Function (MyGene.info)**: bromodomain adjacent to zinc finger domain 1A. The BAZ1A gene encodes the accessory subunit of the ATP-dependent chromatin assembly factor (ACF), a member of the ISWI ('imitation switch') family of chromatin remodeling complexes (summarized by Racki et al., 2009 [PubMed 20033039]).[supplied by OMIM, Apr 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); non-small cell lung carcinoma (0.405); lung adenocarcinoma (0.395); hypothyroidism (0.391); psoriasis (0.346)
- **Europe PMC papers**: 666
- **Why important**: BAZ1A is present in all globally corrected GO terms (9 globally significant GO/KEGG terms, q_global 0.00401–0.0477; see the table), occupies the module's chromatin-remodeling neighborhood, and has strong STRING links to BPTF and RSF1. STRING also identifies the WSTF-related motif and ISWI-type complex (STRING Pfam WSTF, HB1, Itc1p, MBD9 motif 1; within-query FDR = 0.0239) and (STRING Component ISWI-type complex; within-query FDR = 0.0488), while hu.MAP places BAZ1A with SUN1 (hu.MAP huMAP3_08267.1) (hu.MAP huMAP3_10419.1). HPA detects it in brain and skin and shows enhancement in bone marrow and neutrophil-related cell types. Its established functions include nucleosome assembly, chromatin remodeling, and transcriptional regulation, with reported neurodevelopmental, neurodegenerative, and psoriasis associations.
- **Conclusion**: Established evidence supports BAZ1A as a chromatin-remodeling anchor of the module. Its brain and skin co-detection is compatible with a shared transcriptional or chromatin state, whereas any specific role in generating the conserved co-abundance pattern remains a hypothesis.

#### NIPBL

- **Related proteins** (co-abundance neighbors): NVL (0.90), ERBIN (0.86), C2orf49 (0.81), SCAF11 (0.80); STRING partners: BPTF (0.806), RSF1 (0.72), SCAF11 (0.73)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NIPBL cohesin loading factor. This gene encodes the homolog of the Drosophila melanogaster Nipped-B gene product and fungal Scc2-type sister chromatid cohesion proteins. The Drosophila protein facilitates enhancer-promoter communication of remote enhancers and plays a role in developmental regulation. It is also homologous to a family of chromosomal adherins with broad roles in sister chromatid cohesion, chromosome condensatio…
- **Diseases (Open Targets)**: Cornelia de Lange syndrome (0.864); hereditary disease (0.544); Dislocated radial head (0.462); Intellectual disability (0.384); low grade glioma (0.370)
- **Europe PMC papers**: 2494
- **Why important**: NIPBL connects the central NVL neighborhood with BPTF, RSF1, SCAF11, ERBIN, and C2orf49, and is supported by STRING links to BPTF, RSF1, and SCAF11. It is present in every globally corrected GO term (9 globally significant GO/KEGG terms, q_global 0.00401–0.0477; see the table). Its established cohesin-loading and chromatin-remodeling functions provide a mechanistic route from nuclear organization to enhancer-promoter communication and transcription. It has a strong disease association with Cornelia de Lange syndrome and additional developmental and intellectual-disability associations.
- **Conclusion**: Established evidence supports NIPBL as a chromatin-organization and developmental regulator that could connect the module's transcriptional and structural layers. The module does not demonstrate that cohesin loading is the cause of the brain–skin co-abundance pattern.

#### THOC1

- **Related proteins** (co-abundance neighbors): TXNL4A (0.82), POLR1A (0.82); STRING partners: THOC6 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_04932.1, huMAP3_09184.1, huMAP3_12548.1, huMAP3_09101.1, huMAP3_10299.1, huMAP3_10789.1, huMAP3_09943.1
- **Function (MyGene.info)**: THO complex subunit 1. HPR1 is part of the TREX (transcription/export) complex, which includes TEX1 (MIM 606929), THO2 (MIM 300395), ALY (MIM 604171), and UAP56 (MIM 142560).[supplied by OMIM, Nov 2010]
- **Diseases (Open Targets)**: neurodegenerative disease (0.409); hearing loss, autosomal dominant 86 (0.362); alcohol drinking (0.231); urolithiasis (0.231); immune system disorder (0.226)
- **Europe PMC papers**: 804
- **Why important**: THOC1 is part of the THOC1–THOC6 edge and is supported by a very strong STRING relationship with THOC6. Both genes recur across several hu.MAP assemblies (hu.MAP huMAP3_04932.1) (hu.MAP huMAP3_09184.1), (hu.MAP huMAP3_12548.1) (hu.MAP huMAP3_09101.1) (hu.MAP huMAP3_10299.1), (hu.MAP huMAP3_10789.1), and (hu.MAP huMAP3_09943.1). THOC1 appears in all globally corrected GO terms (9 globally significant GO/KEGG terms, q_global 0.00401–0.0477; see the table), is localized to nuclear speckles, and has established roles in the TREX complex and mRNA export. Its literature includes associations with neurodegenerative disease and developmental or hearing-related disorders.
- **Conclusion**: Established evidence supports THOC1 as an RNA-export and transcription-to-processing connector. Its position in the module makes it a plausible integrator of co-abundant RNA-handling processes, but a direct brain–skin-specific export mechanism is not established.

#### PPHLN1

- **Related proteins** (co-abundance neighbors): C2orf49 (0.87), KRI1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_08625.1, huMAP3_01533.1, huMAP3_09569.1, huMAP3_07030.1, huMAP3_08950.1, huMAP3_09973.1, huMAP3_10643.1, huMAP3_09895.1, huMAP3_09778.1, huMAP3_10098.1, huMAP3_14523.1, huMAP3_02281.1, huMAP3_06755.1, huMAP3_09844.1, huMAP3_09463.1
- **Function (MyGene.info)**: periphilin 1. The protein encoded by this gene is one of the several proteins that become sequentially incorporated into the cornified cell envelope during the terminal differentiation of keratinocyte at the outer layers of epidermis. This protein interacts with periplakin, which is known as a precursor of the cornified cell envelope. The cellular localization pattern and insolubility of this protein suggest th…
- **Diseases (Open Targets)**: alcohol drinking (0.252); actinic keratosis (0.247); stroke disorder (0.224); hypothyroidism (0.224); systemic lupus erythematosus (0.211)
- **Europe PMC papers**: 360
- **Why important**: PPHLN1 is repeatedly represented in hu.MAP RNA-binding and RNA-associated assemblies (hu.MAP huMAP3_08625.1) (hu.MAP huMAP3_01533.1) (hu.MAP huMAP3_09569.1) (hu.MAP huMAP3_07030.1) (hu.MAP huMAP3_08950.1) (hu.MAP huMAP3_09973.1) (hu.MAP huMAP3_10643.1) (hu.MAP huMAP3_09895.1) (hu.MAP huMAP3_09778.1) (hu.MAP huMAP3_10098.1) (hu.MAP huMAP3_14523.1) and (hu.MAP huMAP3_02281.1) (hu.MAP huMAP3_06755.1) (hu.MAP huMAP3_09844.1) (hu.MAP huMAP3_09463.1) (hu.MAP huMAP3_06354.1) (hu.MAP huMAP3_08096.1), despite lacking high-confidence STRING partners. It is present in most globally corrected GO terms except the first nuclear-complex term (8 globally significant GO/KEGG terms, q_global 0.0116–0.0477; see the table). Its established function links it to terminal keratinocyte differentiation, the cornified cell envelope, epithelial integrity, and heterochromatin-associated gene regulation. HPA detects it in both brain and skin, and its disease associations include actinic keratosis and systemic lupus erythematosus.
- **Conclusion**: Established evidence supports PPHLN1 as an epithelial-differentiation and nuclear gene-regulation connector, with particularly relevant biology for skin. Its repeated hu.MAP representation suggests an RNA-associated neighborhood, but the co-abundance data do not establish a direct physical complex or explain why the same signal is present in brain.

## Module 10

**Tissue pair**: brain and skin  
**Genes (12)**: BABAM1, CDC73, EP300, MVB12A, METTL3, PCF11, PHC2, POLR2A, SIN3A, SIRT1, TRIM24, TOP2A

### Function

The primary evidence supports a nuclear gene-regulatory module centered on chromatin, RNA polymerase II transcription, chromosome organization, nucleic-acid metabolism, and rhythmic biology. The globally corrected terms include circadian rhythm and rhythmic process (GO:BP circadian rhythm; q_global = 0.000838) (GO:BP rhythmic process; q_global = 0.00297), chromatin binding (GO:MF chromatin binding; q_global = 0.012), DNA-templated and RNA polymerase II transcription (GO:BP DNA-templated transcription; q_global = 0.0244) (GO:BP transcription by RNA polymerase II; q_global = 0.0323), chromosome and euchromatin (GO:CC chromosome; q_global = 0.0306) (GO:CC euchromatin; q_global = 0.0483), nucleic-acid metabolism (GO:BP nucleic acid metabolic process; q_global = 0.0394), protein destabilization (GO:BP protein destabilization; q_global = 0.0368), and hemopoiesis (GO:BP hemopoiesis; q_global = 0.00264). The overlap between the circadian terms and the SIRT1, EP300, METTL3, SIN3A, and TOP2A group is coherent with the supplementary STRING results for biological rhythms (STRING Keyword Biological rhythms; within-query FDR = 8.95e-05) (STRING WikiPathways Circadian rhythm genes; within-query FDR = 0.00017) (STRING Process Rhythmic process; within-query FDR = 0.009). Overall, this is best interpreted as a transcriptional and chromatin-control module with a rhythmic component, rather than as a narrowly tissue-specific structural module.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and the proteins detected in brain and skin are predominantly nuclear. Most genes have low tissue specificity, while many are cell-type enhanced. The HPA signals include neutrophils and neutrophil progenitors, with additional signals in lymphoid tissue, choroid plexus epithelial cells, germ-cell populations, and proliferative or progenitor populations. PHC2 has immune-cell enrichment for neutrophils, and TOP2A is enhanced in lymphoid tissue and in T-reg cells. These observations make a shared cellular-composition or blood-associated contribution plausible, particularly for the hemopoiesis term (GO:BP hemopoiesis; q_global = 0.00264), although the low overall immune-cell specificity and the coherent nuclear annotations argue against treating the entire module as a blood-cell signature. Protein detection in both brain and skin supports biological presence in both tissues, but co-abundance may still partly reflect shared cell types or cell-state composition.

**GO/KEGG enrichment**: 10 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP circadian rhythm | 0.000838 | EP300, METTL3, SIN3A, SIRT1, TOP2A |
| GO:BP hemopoiesis | 0.00264 | BABAM1, CDC73, EP300, METTL3, SIN3A, SIRT1, TOP2A |
| GO:BP rhythmic process | 0.00297 | EP300, METTL3, SIN3A, SIRT1, TOP2A |
| GO:MF chromatin binding | 0.012 | EP300, PHC2, SIN3A, SIRT1, TOP2A, TRIM24 |
| GO:BP DNA-templated transcription | 0.0244 | CDC73, EP300, PCF11, PHC2, POLR2A, SIN3A, SIRT1, TOP2A, TRIM24 |
| GO:CC chromosome | 0.0306 | CDC73, EP300, PHC2, POLR2A, SIN3A, SIRT1, TOP2A, TRIM24 |
| GO:BP transcription by RNA polymerase II | 0.0323 | CDC73, EP300, PCF11, POLR2A, SIN3A, SIRT1, TOP2A, TRIM24 |
| GO:BP protein destabilization | 0.0368 | CDC73, EP300, SIRT1 |
| GO:BP nucleic acid metabolic process | 0.0394 | BABAM1, CDC73, EP300, METTL3, PCF11, PHC2, POLR2A, SIN3A, SIRT1, TOP2A, TRIM24 |
| GO:CC euchromatin | 0.0483 | POLR2A, SIRT1, TRIM24 |

### STRING and hu.MAP

Several module relationships are already strongly supported by STRING: CDC73 with POLR2A, PCF11 with POLR2A, EP300 with SIRT1, EP300 with SIN3A, and SIN3A with SIRT1. These links independently reinforce a connected transcription, transcription-termination, and chromatin-regulatory system. STRING enrichment also supports nucleoplasm, chromatin binding, nuclear protein-containing complexes, RNA polymerase II transcription, and biological rhythms (8 supplementary STRING terms; within-query FDR 8.95e-05–0.0147), but these are supplementary evidence rather than globally corrected enrichment. hu.MAP provides additional established complex context for PCF11 with CDC73 (hu.MAP huMAP3_12111.1) and for CDC73 with POLR2A in RNA polymerase and transcription-associated complexes (hu.MAP huMAP3_09843.1) (hu.MAP huMAP3_11092.1). The hu.MAP complexes contain many additional complex members not present in this module, so the module is a partial projection of larger known assemblies rather than a complete new complex. The remaining co-abundance edges, especially those involving BABAM1, PHC2, MVB12A, TRIM24, and METTL3, are not all represented by high-confidence STRING or hu.MAP relationships and may reflect co-regulation, context dependence, or indirect association.

**STRING interactions (score >= 0.7)**: 5 of 66 gene pairs: CDC73–POLR2A (0.999); EP300–SIN3A (0.816); EP300–SIRT1 (0.972); PCF11–POLR2A (0.952); SIN3A–SIRT1 (0.8)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Biological rhythms (FDR = 8.95e-05, 5 genes); WikiPathways Circadian rhythm genes (FDR = 0.00017, 5 genes); COMPARTMENTS Nucleoplasm (FDR = 0.00031, 9 genes); Function Chromatin binding (FDR = 0.00037, 7 genes); Keyword Nucleus (FDR = 0.0012, 12 genes); PMID (2019) The Histone Deacetylase SIRT6 Restrains Transcription Elongation via Promoter-Proximal Pausing. (FDR = 0.0032, 5 genes); RCTM SUMOylation of transcription cofactors (FDR = 0.0066, 3 genes); Keyword Ubl conjugation (FDR = 0.0071, 9 genes); Process Positive regulation of nucleobase-containing compound metabolic process (FDR = 0.009, 9 genes); Process Rhythmic process (FDR = 0.009, 5 genes); Keyword Isopeptide bond (FDR = 0.0102, 8 genes); Component Chromosome (FDR = 0.0104, 8 genes); Component Nuclear protein-containing complex (FDR = 0.0109, 8 genes); RCTM RNA Polymerase II Transcription (FDR = 0.014, 7 genes); Process Transcription by RNA polymerase II (FDR = 0.0147, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12111.1 (PCF11, CDC73; 2/16); huMAP3_09843.1 (POLR2A, CDC73; 2/29); huMAP3_11092.1 (POLR2A, CDC73; 2/65)

### Novelty

The biological functions and several physical or functional relationships in this module are established, so the module should not be presented as a newly discovered transcriptional complex or circadian pathway. A potentially novel aspect is the conservation of this particular co-abundance neighborhood across brain and skin, especially the combination of rhythmic regulators, chromatin factors, RNA polymerase machinery, DNA-repair or checkpoint-associated factors, and cell-state-linked genes. However, the supplied evidence does not establish that this cross-tissue co-abundance pattern is new. Absence of a relationship from STRING or hu.MAP is not evidence of novelty, and the module may represent a tissue-shared expression program assembled from known pathways. Novelty would require comparison with prior cross-tissue co-expression modules, independent cohorts, and perturbation or longitudinal data.

**Hypothesis.** Hypothesis: this conserved brain-skin module reflects a shared nuclear state in which circadian regulation and chromatin remodeling coordinate RNA polymerase II transcription, RNA processing, DNA topology, and genome maintenance. SIRT1, EP300, and SIN3A may form a regulatory core that links activating and repressing chromatin control, while POLR2A, CDC73, and PCF11 connect that state to transcriptional elongation, termination, and messenger-RNA processing. METTL3 may couple the state to RNA methylation and rhythmic post-transcriptional regulation, while TOP2A and BABAM1 may report cell-cycle, chromosome, and DNA-repair demands. The hemopoietic and neutrophil-associated signals could indicate that part of the observed conservation arises from shared immune or progenitor-cell composition rather than identical regulation within mature brain and skin cells. This hypothesis should be tested by cell-type-resolved analysis, adjustment for blood-cell abundance, and perturbation of the proposed regulatory core.

### Important genes

#### SIRT1

- **Related proteins** (co-abundance neighbors): SIN3A (0.85), BABAM1 (0.83), CDC73 (0.81), POLR2A (0.81); STRING partners: EP300 (0.972), SIN3A (0.8)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sirtuin 1. This gene encodes a member of the sirtuin family of proteins, homologs to the yeast Sir2 protein. Members of the sirtuin family are characterized by a sirtuin core domain and grouped into four classes. The functions of human sirtuins have not yet been determined; however, yeast sirtuin proteins are known to regulate epigenetic gene silencing and suppress recombination of rDNA. Studies suggest that…
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); atrial fibrillation (0.336); hypertensive disorder (0.204); tooth disorder (0.200); type 2 diabetes mellitus (0.140)
- **Europe PMC papers**: 55588
- **Why important**: SIRT1 has the strongest network centrality in the supplied subgraph and connects to SIN3A, BABAM1, CDC73, and POLR2A. It occurs in every globally corrected enrichment term (10 globally significant GO/KEGG terms, q_global 0.000838–0.0483; see the table), including rhythmic process, chromatin binding, transcription, chromosome, euchromatin, and protein destabilization. Its STRING links to EP300 and SIN3A, nuclear localization, detection in brain and skin, disease associations involving neurodegenerative disease and metabolic or cardiovascular phenotypes, and very large literature volume make it the most informative candidate for the module's regulatory core.
- **Conclusion**: Established evidence supports SIRT1 as a central nuclear regulator linking chromatin, transcription, DNA repair, and rhythmic biology in this module. It is a strong candidate driver or marker of the shared program, but co-abundance alone does not establish that SIRT1 causally controls the other module genes.

#### EP300

- **Related proteins** (co-abundance neighbors): TRIM24 (0.82), SIN3A (0.80), METTL3 (0.80); STRING partners: SIN3A (0.816), SIRT1 (0.972)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EP300 lysine acetyltransferase. This gene encodes the adenovirus E1A-associated cellular p300 transcriptional co-activator protein. It functions as histone acetyltransferase that regulates transcription via chromatin remodeling and is important in the processes of cell proliferation and differentiation. It mediates cAMP-gene regulation by binding specifically to phosphorylated CREB protein. This gene has also been identified as …
- **Diseases (Open Targets)**: Rubinstein-Taybi syndrome due to EP300 haploinsufficiency (0.797); Menke-Hennekam syndrome 2 (0.677); cancer (0.601); Rubinstein-Taybi syndrome (0.585); hereditary disease (0.551)
- **Europe PMC papers**: 17204
- **Why important**: EP300 is a highly connected module member linking TRIM24, SIN3A, and METTL3, and it has strong STRING support with SIRT1 and SIN3A. It appears in nearly all of the globally corrected terms, including rhythmic biology, chromatin binding, transcription, chromosome organization, and protein destabilization (9 globally significant GO/KEGG terms, q_global 0.000838–0.0394; see the table). Its established lysine-acetyltransferase and transcriptional co-activator functions, brain and skin detection, disease associations including Rubinstein-Taybi syndrome and cancer, and substantial literature volume give it major mechanistic and biomedical importance.
- **Conclusion**: Established evidence identifies EP300 as a chromatin and transcriptional co-regulator that plausibly connects the module's rhythmic and gene-expression signals. Its causal role in this specific brain-skin co-abundance module remains a hypothesis rather than a demonstrated fact.

#### SIN3A

- **Related proteins** (co-abundance neighbors): SIRT1 (0.85), EP300 (0.80); STRING partners: EP300 (0.816), SIRT1 (0.8)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SIN3 transcription regulator family member A. The protein encoded by this gene is a transcriptional regulatory protein. It contains paired amphipathic helix (PAH) domains, which are important for protein-protein interactions and may mediate repression by the Mad-Max complex. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: chromosome 15q24 deletion syndrome (0.748); SIN3A-related intellectual disability syndrome (0.618); syndromic intellectual disability (0.554); hereditary disease (0.537); neurodegenerative disease (0.430)
- **Europe PMC papers**: 5349
- **Why important**: SIN3A is connected to SIRT1 and EP300 in the module and by STRING, placing it within the best-supported regulatory core. It appears in the rhythmic, hemopoietic, chromatin, transcription, chromosome, and nucleic-acid-related global terms (8 globally significant GO/KEGG terms, q_global 0.000838–0.0394; see the table). Its known transcriptional repression and chromatin-associated functions, neuronal differentiation annotation, brain and skin detection, association with SIN3A-related intellectual disability and neurodegenerative disease, and substantial literature volume make it important for interpreting the neural and chromatin dimensions of the module.
- **Conclusion**: Established evidence supports SIN3A as a transcriptional and chromatin regulator that helps explain the module's coherent nuclear architecture. The observed association with rhythmic biology is supported at the module level, but direct rhythmic regulation by SIN3A in these tissues is not established here.

#### CDC73

- **Related proteins** (co-abundance neighbors): SIRT1 (0.81); STRING partners: POLR2A (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_12111.1, huMAP3_09843.1, huMAP3_11092.1
- **Function (MyGene.info)**: cell division cycle 73. This gene encodes a tumor suppressor that is involved in transcriptional and post-transcriptional control pathways. The protein is a component of the the PAF protein complex, which associates with the RNA polymerase II subunit POLR2A and with a histone methyltransferase complex. This protein appears to facilitate the association of 3' mRNA processing factors with actively-transcribed chromatin. Mu…
- **Diseases (Open Targets)**: hyperparathyroidism 2 with jaw tumors (0.810); parathyroid gland carcinoma (0.802); familial isolated hyperparathyroidism (0.738); hyperparathyroidism (0.599); hereditary neoplastic syndrome (0.555)
- **Europe PMC papers**: 2210
- **Why important**: CDC73 connects to SIRT1 in the co-abundance network, has a very strong STRING relationship with POLR2A, and occurs in all three hu.MAP complexes reported for the module (hu.MAP huMAP3_12111.1) (hu.MAP huMAP3_09843.1) (hu.MAP huMAP3_11092.1). It contributes to globally corrected transcription, chromosome, nucleic-acid, hemopoietic, and protein-destabilization terms (6 globally significant GO/KEGG terms, q_global 0.00264–0.0394; see the table). Its established role in the PAF-associated transcriptional and post-transcriptional machinery, tumor-suppressor function, and strong disease associations with hyperparathyroidism and jaw tumors make it an important bridge between the module's transcriptional and disease-relevant interpretations.
- **Conclusion**: Established evidence supports CDC73 as a transcription-associated and messenger-RNA-processing component that anchors the module to known polymerase and PAF-related complexes. Its co-abundance with rhythmic regulators does not by itself prove that CDC73 participates in circadian control.

#### POLR2A

- **Related proteins** (co-abundance neighbors): SIRT1 (0.81); STRING partners: CDC73 (0.999), PCF11 (0.952)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09843.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase II subunit A. This gene encodes the largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene contains a carboxy terminal domain composed of heptapeptide repeats that are essential for polymerase activity. These repeats contain serine and threonine residues that are phosphorylated in actively transcribing RNA polymerase. In addition, …
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and variable intellectual and behavioral abnormalities (0.738); HIV infectious disease (0.600); hereditary disease (0.479); syndromic intellectual disability (0.462); Orthomyxoviridae infectious disease (0.374)
- **Europe PMC papers**: 4546
- **Why important**: POLR2A is the largest subunit of RNA polymerase II and is connected to CDC73 and PCF11 by strong STRING relationships. It appears in the globally corrected transcription, chromosome, nucleic-acid, and euchromatin terms (5 globally significant GO/KEGG terms, q_global 0.0244–0.0483; see the table), and it participates with CDC73 in multiple hu.MAP complexes (hu.MAP huMAP3_09843.1) (hu.MAP huMAP3_11092.1). Its detection-related and tissue-enhancement evidence, together with associations involving neurodevelopmental and hereditary disorders, makes it a direct molecular anchor for the module's transcriptional interpretation.
- **Conclusion**: Established evidence supports POLR2A as the core transcriptional machinery represented by this module and provides a concrete explanation for its RNA polymerase II and chromosome annotations. The module does not show that POLR2A is specifically regulated by the brain-skin conservation.

## Module 11

**Tissue pair**: brain and skin  
**Genes (8)**: CNN2, POLA1, HUS1, MAN2A1, MAD2L1, MED20, SLC16A3, SMC2

### Function

The module is most consistent with a genome-maintenance and proliferative-cell program, centered on DNA replication initiation, the mitotic spindle checkpoint, DNA-damage checkpoint activity, chromosome condensation, and transcriptional regulation. POLA1, MAD2L1, HUS1, and SMC2 provide the strongest functional coherence through replication, checkpoint, repair, and chromosome-organization roles. MED20, SLC16A3, MAN2A1, and CNN2 suggest additional links to transcriptional control, lactate and pyruvate transport, Golgi glycan maturation, and actin organization. No GO or KEGG term passed global correction, so this interpretation is based on the individual gene annotations and network structure rather than statistically significant pathway enrichment. The sparse network and absence of STRING functional enrichment argue for a biologically mixed module rather than a single fully resolved pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: all members have no secreted-gene annotation. It is also not broadly dominated by immune-cell-specific genes, although HPA evidence points toward cell-type-associated expression involving erythrocyte progenitors, neutrophils, lymphoid tissue, bone marrow, oligodendrocytes, and several proliferative or reproductive cell types. Most members have low tissue specificity, while several show cell-type enhancement. Protein detection in both brain and skin for multiple members supports shared detectability, but the HPA pattern also raises the possibility that the conserved co-abundance signal reflects shared proliferative, vascular, stromal, or blood-associated cell populations rather than a brain-and-skin-specific mechanism. SLC16A3 has immune-cell enhancement in neutrophils, whereas CNN2 is associated with neutrophil-lineage cell types; this warrants attention to cellular composition and possible blood-cell or infiltrating-cell contributions.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports two high-confidence pairwise relationships within the module: MAD2L1 with SMC2 and POLA1 with SMC2. These links connect checkpoint or chromosome-segregation biology with DNA replication machinery, but they do not establish a complete physical complex containing all module members. hu.MAP identifies complex C1, containing POLA1 and MAD2L1 among the module genes, with POLA2 and C15orf39 outside the module. Thus, part of the module recapitulates known molecular relationships, especially around POLA1, MAD2L1, and SMC2. MAN2A1, SLC16A3, MED20, HUS1, and CNN2 lack reported within-module STRING or hu.MAP support in the supplied evidence, so their co-abundance links should be treated as statistical or contextual associations rather than established physical interactions.

**STRING interactions (score >= 0.7)**: 2 of 28 gene pairs: MAD2L1–SMC2 (0.754); POLA1–SMC2 (0.864)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05779.1 (POLA1, MAD2L1; 2/4)

### Novelty

The module should not be described as a wholly new molecular complex. Its POLA1-MAD2L1 relationship is represented in hu.MAP, and its POLA1-SMC2 and MAD2L1-SMC2 relationships are supported by STRING. The potentially novel aspect is the cross-tissue co-abundance configuration that combines this partial genome-maintenance core with MAN2A1, SLC16A3, MED20, HUS1, and CNN2 in brain and skin. However, absence of the latter relationships from STRING or hu.MAP does not prove novelty: it may reflect context dependence, co-regulation, cell-type composition, incomplete database coverage, or indirect biology. The appropriate conclusion is that the brain-skin module is a potentially novel systems-level association built partly from known interactions, requiring independent validation.

**Hypothesis.** Hypothesis: the module reflects a shared proliferative or stress-response state present in selected cell populations of brain and skin. In this model, POLA1 supports replication initiation, HUS1 monitors DNA damage, MAD2L1 coordinates spindle checkpoint control, and SMC2 organizes chromosomes during cell division. MED20 could provide transcriptional coordination, while SLC16A3 could support the metabolic demands of cells relying on lactate and pyruvate transport. MAN2A1 and CNN2 may represent tissue or cell-state-specific interfaces involving Golgi glycan processing and cytoskeletal organization. The apparent conservation could therefore arise from a shared repair, regeneration, or cell-cycle-associated state, potentially influenced by cellular admixture, rather than from a single brain-skin-specific biochemical complex. This is a hypothesis, not an established causal mechanism.

### Important genes

#### POLA1

- **Related proteins** (co-abundance neighbors): MAN2A1 (0.87), MED20 (0.83), MAD2L1 (0.81); STRING partners: SMC2 (0.864)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_05779.1
- **Function (MyGene.info)**: DNA polymerase alpha 1, catalytic subunit. This gene encodes the catalytic subunit of DNA polymerase, which together with a regulatory and two primase subunits, forms the DNA polymerase alpha complex. The catalytic subunit plays an essential role in the initiation of DNA replication. [provided by RefSeq, Mar 2010].
- **Diseases (Open Targets)**: X-linked reticulate pigmentary disorder (0.747); X-linked intellectual disability, van Esch type (0.731); acute lymphoblastic leukemia (0.598); non-small cell lung carcinoma (0.593); B-cell chronic lymphocytic leukemia (0.590)
- **Europe PMC papers**: 1674
- **Why important**: POLA1 is the highest-connectivity gene in the module and links MAN2A1, MED20, and MAD2L1. It encodes the catalytic subunit of DNA polymerase alpha, which is essential for replication initiation and primer synthesis. It is detected in both brain and skin, is represented in hu.MAP complex C1, has a substantial literature base, and has disease associations including X-linked reticulate pigmentary disorder, X-linked intellectual disability, and hematologic malignancy.
- **Conclusion**: Established evidence supports POLA1 as a central replication-related hub and as a plausible anchor of the module. The hypothesis that POLA1 drives the shared brain-skin co-abundance pattern, rather than merely marking a proliferative cell state, remains untested.

#### SMC2

- **Related proteins** (co-abundance neighbors): HUS1 (0.81), MAD2L1 (0.80); STRING partners: MAD2L1 (0.754), POLA1 (0.864)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: structural maintenance of chromosomes 2. Predicted to enable ATP binding activity; chromatin binding activity; and single-stranded DNA binding activity. Involved in mitotic chromosome condensation. Located in condensed chromosome; cytoplasm; and nuclear lumen. Part of condensin complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: basal cell carcinoma (0.464); ovarian carcinoma (0.383); aortic stenosis (0.380); cancer (0.363); alcohol drinking (0.359)
- **Europe PMC papers**: 2065
- **Why important**: SMC2 is connected to HUS1 and MAD2L1 and has high-confidence STRING relationships with both MAD2L1 and POLA1. It is a component of the condensin complex and participates in chromosome condensation, chromosome organization, chromosome segregation, cerebral cortex development, and B-cell differentiation. It is detected in both brain and skin and shows enhancement in lymphoid tissue and several progenitor populations.
- **Conclusion**: Established evidence identifies SMC2 as the principal bridge between replication or checkpoint genes and chromosome architecture in this module. Its placement supports a cell-division or genome-organization interpretation, while any specific role in coordinated brain-skin biology is still hypothetical.

#### MAD2L1

- **Related proteins** (co-abundance neighbors): POLA1 (0.81), SMC2 (0.80); STRING partners: SMC2 (0.754)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05779.1
- **Function (MyGene.info)**: mitotic arrest deficient 2 like 1. MAD2L1 is a component of the mitotic spindle assembly checkpoint that prevents the onset of anaphase until all chromosomes are properly aligned at the metaphase plate.  MAD2L1 is related to the MAD2L2 gene located on chromosome 1.  A MAD2 pseudogene has been mapped to chromosome 14. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: alcohol drinking (0.433); cornea transplantation (0.342); connective tissue disorder (0.314); hypotensive disorder (0.294); Tietze syndrome (0.294)
- **Europe PMC papers**: 3856
- **Why important**: MAD2L1 is a core spindle-assembly-checkpoint component, connects POLA1 with SMC2, participates in hu.MAP complex C1, and has the largest literature base among the module genes. Its HPA profile is enhanced in bone marrow and lymphoid tissue and in multiple progenitor or differentiating cell types, consistent with a role in dividing-cell populations.
- **Conclusion**: Established evidence supports MAD2L1 as a key mitotic-checkpoint marker and as part of the known POLA1-associated molecular context. The hypothesis that its co-abundance reflects active checkpoint engagement in brain and skin requires direct cellular and functional testing.

#### HUS1

- **Related proteins** (co-abundance neighbors): SMC2 (0.81), CNN2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HUS1 checkpoint clamp component. The protein encoded by this gene is a component of an evolutionarily conserved, genotoxin-activated checkpoint complex that is involved in the cell cycle arrest in response to DNA damage. This protein forms a heterotrimeric complex with checkpoint proteins RAD9 and RAD1. In response to DNA damage, the trimeric complex interacts with another protein complex consisting of checkpoint protein RAD17 an…
- **Diseases (Open Targets)**: severe acute respiratory syndrome (0.144); COVID-19 (0.144); Alzheimer disease (0.073); endometriosis (0.052); toxic encephalopathy (0.043)
- **Europe PMC papers**: 1763
- **Why important**: HUS1 is connected to SMC2 and CNN2 and encodes a component of the DNA-damage checkpoint clamp with RAD9 and RAD1. Its annotations include DNA-damage checkpoint signaling, DNA repair, telomere maintenance, homologous recombination, and nucleotide-excision repair. It is detected in both brain and skin and is enhanced in esophageal apical cells and late spermatids, while having a substantial literature base.
- **Conclusion**: Established evidence supports HUS1 as the module's clearest DNA-damage-response component and gives biological plausibility to a genome-stress interpretation. The proposed connection between HUS1 and the tissue-pair conservation is a hypothesis that could reflect repair or regeneration states.

#### SLC16A3

- **Related proteins** (co-abundance neighbors): MAN2A1 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 16 member 3. Lactic acid and pyruvate transport across plasma membranes is catalyzed by members of the proton-linked monocarboxylate transporter (MCT) family, which has been designated solute carrier family-16. Each MCT appears to have slightly different substrate and inhibitor specificities and transport kinetics, which are related to the metabolic requirements of the tissues in which it is found. The MCTs, w…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.208); neoplasm (0.118); lung adenocarcinoma (0.113); glioblastoma (0.108); cancer (0.106)
- **Europe PMC papers**: 2423
- **Why important**: SLC16A3 is the module's membrane transporter and connects MAN2A1 to the rest of the network through the MAN2A1-SLC16A3 edge. It transports lactate and pyruvate across the plasma membrane, is detected in both brain and skin, and shows enhancement in skeletal muscle, neutrophils, and several epithelial or trophoblast cell types. Its disease associations include glioblastoma and other neoplastic conditions, and it has a substantial literature base.
- **Conclusion**: Established evidence supports SLC16A3 as a metabolic-context gene rather than a demonstrated member of the nuclear replication machinery. Its presence suggests that metabolic state may accompany the genome-maintenance program, but the hypothesis that lactate or pyruvate flux organizes the entire module is not established.

## Module 12

**Tissue pair**: brain and skin  
**Genes (14)**: CRELD2, EED, MCM2, MCM4, MCM6, MCM7, MSH2, NUP205, PALM2AKAP2, PUS7, RAI14, SRSF5, TWSG1, ZNF787

### Function

The module is best interpreted as a nuclear DNA replication and genome-maintenance module. The primary evidence is exceptionally coherent: the MCM2–MCM4–MCM6–MCM7 subset supports the MCM complex and CMG complex (GO:CC MCM complex; q_global = 1.23e-05) (GO:CC CMG complex; q_global = 0.000158), DNA replication initiation and its regulation (4 globally significant GO/KEGG terms, q_global 0.000158–0.016; see the table), multiple DNA-helicase activities (8 globally significant GO/KEGG terms, q_global 0.00051–0.0132; see the table), and the DNA-replication pathway (KEGG DNA replication - Homo sapiens (human); q_global = 0.00581). The same core also supports break-induced replication, homologous recombination, DNA recombination, and double-strand-break repair (4 globally significant GO/KEGG terms, q_global 5.67e-05–0.0429; see the table). MSH2 extends this interpretation toward DNA mismatch repair and damage surveillance, although the globally corrected terms involving MSH2 are broader DNA-binding, DNA-repair, recombination, and telomeric-region terms rather than a dedicated mismatch-repair term (6 globally significant GO/KEGG terms, q_global 0.00051–0.0429; see the table). The isomerase term (GO:MF isomerase activity; q_global = 0.0447) is less specific and should not drive the interpretation. Overall, this is a replication-fork and genome-integrity module rather than a brain- or skin-specific signaling module.

**Cell composition.** The proteins are predominantly intracellular and nuclear rather than plasma or secreted proteins. HPA places most genes at low tissue specificity, with several enhanced in bone marrow or lymphoid tissue and frequent enhancement in erythrocyte, megakaryocyte, and monocyte progenitors. Most genes have low immune-cell specificity, with only PALM2AKAP2 marked as immune-cell enhanced and RAI14 not detected in immune cells. TWSG1 is secreted with unknown location, while CRELD2 has intracellular and membrane localization; these are minority features rather than evidence that the module is a secreted-protein module. Detection in brain and skin is widespread for the module, but MCM2 and MCM7 are not detected in brain by the stated HPA protein assay, so the shared brain–skin pattern should not automatically be interpreted as a specialized neuronal or cutaneous program. The progenitor-enrichment pattern raises the possibility that part of the shared signal reflects proliferating or progenitor-like cells, or sample-composition effects, rather than a tissue-specific function. It does not by itself invalidate the module.

**GO/KEGG enrichment**: 26 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC MCM complex | 1.23e-05 | MCM2, MCM4, MCM6, MCM7 |
| GO:BP double-strand break repair via break-induced replication | 5.67e-05 | MCM2, MCM4, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication initiation | 0.000158 | MCM2, MCM4, MCM6, MCM7 |
| GO:CC CMG complex | 0.000158 | MCM2, MCM4, MCM6, MCM7 |
| GO:CC DNA replication preinitiation complex | 0.000235 | MCM2, MCM4, MCM6, MCM7 |
| GO:MF single-stranded DNA binding | 0.00051 | MCM2, MCM4, MCM6, MCM7, MSH2 |
| GO:BP regulation of DNA-templated DNA replication | 0.000804 | MCM2, MCM4, MCM6, MCM7 |
| GO:BP DNA replication initiation | 0.00321 | MCM2, MCM4, MCM6, MCM7 |
| GO:MF four-way junction helicase activity | 0.00321 | MCM2, MCM4, MCM6, MCM7 |
| GO:MF forked DNA-dependent helicase activity | 0.00321 | MCM2, MCM4, MCM6, MCM7 |
| GO:MF ATP-dependent activity, acting on DNA | 0.00368 | MCM2, MCM4, MCM6, MCM7, MSH2 |
| GO:MF double-stranded DNA helicase activity | 0.00377 | MCM2, MCM4, MCM6, MCM7 |
| GO:MF 3'-5' DNA helicase activity | 0.00377 | MCM2, MCM4, MCM6, MCM7 |
| GO:MF single-stranded 3'-5' DNA helicase activity | 0.00377 | MCM2, MCM4, MCM6, MCM7 |
| KEGG DNA replication - Homo sapiens (human) | 0.00581 | MCM2, MCM4, MCM6, MCM7 |

### STRING and hu.MAP

STRING provides strong, mutually reinforcing support for the known MCM core: MCM2, MCM4, MCM6, and MCM7 are densely connected at very high confidence, and the supplementary enrichment identifies the MCM complex, MCM domains, the CMG complex, DNA unwinding, and replication-stress biology (15 supplementary STRING terms; within-query FDR 2.57e-05–0.00069). The weaker MCM7–MSH2 link is consistent with a possible connection between replication and repair, but it is not equivalent to membership of MSH2 in the MCM core. hu.MAP independently places the MCM2–MCM4–MCM6–MCM7 group in several complexes, including MCM-core and broader replisome or replication-stress assemblies (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_08848.1). These complexes include expected partners such as MCM3, MCM5, MCMBP, CDC45, GINS proteins, TIMELESS, TIPIN, and CLSPN. Thus, the network is substantially supported by previously known physical or functional relationships, especially for the MCM quartet. EED, TWSG1, ZNF787, RAI14, SRSF5, NUP205, PUS7, PALM2AKAP2, and CRELD2 lack the listed STRING or hu.MAP support, so their co-abundance links should be treated as correlations requiring validation rather than established physical interactions.

**STRING interactions (score >= 0.7)**: 7 of 91 gene pairs: MCM2–MCM4 (0.999); MCM2–MCM6 (0.999); MCM2–MCM7 (0.999); MCM4–MCM6 (0.999); MCM4–MCM7 (0.999); MCM6–MCM7 (0.999); MCM7–MSH2 (0.71)
**STRING functional enrichment (supplementary, within-query FDR)**: Component MCM complex (FDR = 2.57e-05, 4 genes); COMPARTMENTS MCM complex (FDR = 2.81e-05, 4 genes); InterPro MCM domain (FDR = 4.69e-05, 4 genes); InterPro Mini-chromosome maintenance, conserved site (FDR = 4.69e-05, 4 genes); InterPro MCM N-terminal domain (FDR = 4.69e-05, 4 genes); InterPro Mini-chromosome maintenance protein (FDR = 4.69e-05, 4 genes); InterPro MCM OB domain (FDR = 4.69e-05, 4 genes); InterPro MCM, AAA-lid domain (FDR = 4.69e-05, 4 genes); Component CMG complex (FDR = 7.21e-05, 4 genes); COMPARTMENTS CMG complex (FDR = 7.9e-05, 4 genes); RCTM Unwinding of DNA (FDR = 0.00021, 4 genes); COMPARTMENTS MCM core complex (FDR = 0.00035, 3 genes); Process Double-strand break repair via break-induced replication (FDR = 0.00042, 4 genes); Process Regulation of DNA-templated DNA replication initiation (FDR = 0.00046, 4 genes); RCTM Activation of ATR in response to replication stress (FDR = 0.00069, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06061.1 (MCM4, MCM7, MCM2, MCM6; 4/5); huMAP3_05529.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_07113.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_14758.1 (MCM4, MCM7, MCM2, MCM6; 4/14); huMAP3_08554.1 (MCM4, MCM7, MCM2, MCM6; 4/15); huMAP3_11832.1 (MCM4, MCM7, MCM2, MCM6; 4/15); huMAP3_12180.1 (MCM4, MCM7, MCM2, MCM6; 4/17); huMAP3_09860.1 (MCM4, MCM2, MCM6; 3/4); huMAP3_00154.1 (MCM4, MCM2, MCM6; 3/5); huMAP3_11119.1 (MCM4, MCM7, MCM6; 3/14); huMAP3_09466.1 (MCM4, MCM2, MCM6; 3/23); huMAP3_10862.1 (MCM4, MCM2, MCM6; 3/33); huMAP3_14306.1 (MCM4, MCM2, MCM6; 3/55); huMAP3_02602.1 (MCM4, MCM6; 2/2); huMAP3_08848.1 (MCM4, MCM6; 2/15)

### Novelty

The molecular function of the central MCM group is not a new discovery: the globally corrected enrichment, STRING relationships, and hu.MAP complexes all agree with an established replication machinery. The potentially novel aspect is the observation that this replication-and-repair program is conserved as a co-abundance module across brain and skin. The fact sheet does not establish whether this cross-tissue module has been reported previously, and absence from the listed resources for several peripheral genes cannot prove novelty. A defensible claim is therefore that the cross-tissue co-abundance organization may be a new systems-level observation, while the underlying MCM complex and its replication role are established. Novelty would require comparison with prior brain–skin co-abundance studies, independent cohorts, cell-composition controls, and experimental interaction or perturbation data.

**Hypothesis.** Hypothesis: the conserved brain–skin module reflects coordinated activity or abundance of a replication-fork and genome-surveillance program in proliferating progenitor or renewing cell populations shared across the two tissues. The MCM2–MCM4–MCM6–MCM7 core could mark licensing and helicase activity, while MSH2 could couple replication-associated lesions to repair surveillance. EED, PUS7, SRSF5, NUP205, and the less-characterized peripheral genes may reflect chromatin, RNA-processing, nuclear-transport, or cell-state dependencies that accompany this program, but the present data do not establish direct biochemical links. TWSG1 and PALM2AKAP2 could instead indicate a distinct extracellular or membrane-associated cell-state component connected through co-abundance. This hypothesis should be tested by cell-type deconvolution, replication and DNA-damage assays, perturbation of the MCM core, and validation in independent brain and skin datasets.

### Important genes

#### MCM6

- **Related proteins** (co-abundance neighbors): MCM4 (0.89), MCM2 (0.88), MCM7 (0.88), TWSG1 (0.82), EED (0.80); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_11119.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 6. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: lactose intolerance (0.246); neurodegenerative disease (0.225); obesity disorder (0.166); nervous system disorder (0.141); systemic lupus erythematosus (0.140)
- **Europe PMC papers**: 3766
- **Why important**: MCM6 has the strongest network position in the module and connects the four-gene MCM core with TWSG1 and EED. It participates in every primary enrichment term listed for the module (26 globally significant GO/KEGG terms, q_global 1.23e-05–0.0467; see the table), is supported by all listed STRING MCM annotations (15 supplementary STRING terms; within-query FDR 2.57e-05–0.00069), and occurs across the hu.MAP complexes (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_08848.1). Its annotation identifies it as an essential MCM replication factor involved in replication initiation, fork formation, and break-induced replication. It is detected in both brain and skin and shows enhancement in lymphoid and hematopoietic progenitor contexts. Its disease-association evidence is broad rather than diagnostic, and the literature support is substantial.
- **Conclusion**: Established: MCM6 is a central replication-helicase component and the strongest integrative anchor of this module. Hypothesis: its high co-abundance centrality may make it a useful marker of shared proliferative or replication-stress states across brain and skin, but this cannot be separated from cell-composition effects using the supplied evidence.

#### MCM2

- **Related proteins** (co-abundance neighbors): MCM6 (0.88), MCM7 (0.87), TWSG1 (0.80); STRING partners: MCM4 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a core member of the MCM and CMG machinery, has strong STRING support with MCM4, MCM6, and MCM7, and appears in nearly all listed hu.MAP assemblies involving the MCM group (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1). It contributes to the complete primary replication and repair signature (26 globally significant GO/KEGG terms, q_global 1.23e-05–0.0467; see the table). Its annotated role in replication initiation and fork formation gives the module a direct mechanistic entry point. It has extensive literature support and disease associations involving hearing loss and developmental phenotypes. HPA enhancement in bone marrow and lymphoid tissue, together with progenitor enrichment, is consistent with a replication-linked cell-state signal.
- **Conclusion**: Established: MCM2 is a core replication-licensing factor that strongly supports the module's functional interpretation. Hypothesis: its presence in the shared tissue module may report renewal or progenitor activity rather than a specialized function of mature neural or skin cells.

#### MCM4

- **Related proteins** (co-abundance neighbors): MCM6 (0.89), MCM7 (0.86), MSH2 (0.80); STRING partners: MCM2 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_11119.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 4. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication rel…
- **Diseases (Open Targets)**: primary immunodeficiency with natural-killer cell deficiency and adrenal insufficiency (0.714); X-linked adrenal hypoplasia congenita (0.185); lung adenocarcinoma (0.112); microcephaly (0.111); neoplasm (0.102)
- **Europe PMC papers**: 4082
- **Why important**: MCM4 is a core MCM and CMG component with strong STRING links to MCM2, MCM6, and MCM7 and broad representation across the hu.MAP complexes (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_08848.1). It contributes to all primary enrichment themes assigned to the MCM quartet, including replication initiation, helicase activity, recombination, and double-strand-break repair (26 globally significant GO/KEGG terms, q_global 1.23e-05–0.0467; see the table). Its annotated function in replication-fork formation and DNA replication is direct and well established. It is detected in both brain and skin, is enhanced in bone marrow, and has substantial literature and disease-association support, including developmental and immune-related phenotypes.
- **Conclusion**: Established: MCM4 is a central, previously characterized replication-machinery component that validates the module's core interpretation. Hypothesis: MCM4 abundance may be sensitive to replication stress or proliferative demand in shared renewing cell populations, but the co-abundance data do not demonstrate that causal relationship.

#### MCM7

- **Related proteins** (co-abundance neighbors): MCM6 (0.88), MCM2 (0.87), MCM4 (0.86); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM6 (0.999), MSH2 (0.71)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_11119.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 completes the strongly connected MCM quartet and has high-confidence STRING links to MCM2, MCM4, and MCM6, plus a weaker link to MSH2. It is represented in multiple hu.MAP replication complexes (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_11119.1) and participates in nearly all primary enrichment terms associated with replication, helicase activity, recombination, and repair (24 globally significant GO/KEGG terms, q_global 1.23e-05–0.0447; see the table). Its established annotation includes replication initiation, fork elongation, and DNA-damage response. It is enhanced in bone marrow and several progenitor or basal-cell populations, with extensive literature and disease-association support.
- **Conclusion**: Established: MCM7 is a core replication helicase component and reinforces the biological reality of the MCM-centered module. Hypothesis: its connection to MSH2 may indicate coordination between replication and mismatch or damage surveillance, but the available interaction evidence is insufficient to establish a direct functional complex.

#### MSH2

- **Related proteins** (co-abundance neighbors): NUP205 (0.82), MCM4 (0.80); STRING partners: MCM7 (0.71)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutS homolog 2. This locus is frequently mutated in hereditary nonpolyposis colon cancer (HNPCC). When cloned, it was discovered to be a human homolog of the E. coli mismatch repair gene mutS, consistent with the characteristic alterations in microsatellite sequences (RER+ phenotype) found in HNPCC. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: Lynch syndrome (0.891); colorectal cancer (0.776); mismatch repair cancer syndrome (0.775); Muir-Torre syndrome (0.752); mismatch repair cancer syndrome 1 (0.740)
- **Europe PMC papers**: 22581
- **Why important**: MSH2 is the module's clearest repair-surveillance gene. It contributes to the globally corrected single-stranded-DNA-binding, DNA-recombination, double-strand-break-repair, telomeric-region, and DNA-catalytic-activity terms (6 globally significant GO/KEGG terms, q_global 0.00051–0.0429; see the table). Its annotated role in mismatch repair and DNA damage tolerance is well established, it has the strongest disease-association evidence in the module through Lynch syndrome and related mismatch-repair cancer syndromes, and it has extensive literature support. In the network it links MCM4 to NUP205, while STRING supplies a weaker MCM7 connection. HPA detects it in brain and skin and shows progenitor-associated cell-type enhancement.
- **Conclusion**: Established: MSH2 supplies a credible genome-surveillance and repair context around the MCM replication core. Hypothesis: MSH2 may couple replication-fork stress to repair processes in the shared module, but its peripheral network position and limited listed complex evidence argue against claiming that it is a core MCM component.

## Module 13

**Tissue pair**: brain and skin  
**Genes (5)**: EXOC3, GNAI1, NCS1, TUBB2A, VPS11

### Function

The module is most consistent with a membrane-proximal signaling and vesicle-trafficking program that links inhibitory G-protein regulation, calcium sensing, exocytosis, microtubule organization, and endosome or lysosome transport. The primary enrichment evidence is (GO:MF cyclase regulator activity; q_global = 0.0206), cyclase regulator activity, supported by GNAI1 and NCS1. GNAI1 can inhibit adenylate cyclase through heterotrimeric G-protein signaling, while NCS1 regulates calcium-sensitive signaling, receptor phosphorylation, secretory granules, and synaptic plasticity. EXOC3 provides a plausible exocytic-vesicle component, VPS11 provides endosomal and lysosomal trafficking context, and TUBB2A provides a microtubule-based transport and structural context. The four-edge subgraph is compact and chain-like rather than a densely interconnected canonical complex. No STRING functional-enrichment term was reported. The absence of additional enriched terms does not invalidate the module, but it limits the breadth of pathway inference.

**Cell composition.** This is not a plasma or secreted-protein module: none of its members is annotated as secreted. It is also not predominantly a blood-cell module. HPA profiles show strong brain representation, including brain-enhanced or brain-enriched genes, and protein detection in both brain and skin for nearly all members with available data. Cell-type annotations span neuronal and glial populations as well as keratinocyte populations, with several genes enhanced in brain excitatory neurons, oligodendrocytes, basal keratinocytes, or suprabasal keratinocytes. GNAI1 has an immune-cell-enriched annotation in NK cells and EXOC3 has an immune-cell-enhanced annotation in eosinophils, so immune-cell composition cannot be excluded entirely. However, the absence of secreted proteins and the presence of neuronal, glial, and keratinocyte annotations favor a shared cell-biological program or shared cell types over a simple plasma-protein signal. EXOC3 and VPS11 are broadly expressed, housekeeping-like trafficking components, which may also contribute to cross-tissue preservation.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF cyclase regulator activity | 0.0206 | GNAI1, NCS1 |

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module members, and no STRING enrichment term was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not independently supported here as established physical interactions or membership in a known multiprotein complex. This does not show that the relationships are biologically false: co-abundance can reflect coordinated regulation, shared cell types, indirect pathway coupling, or technical and compositional effects. The strongest functional convergence is between GNAI1 and NCS1 through (GO:MF cyclase regulator activity; q_global = 0.0206), while EXOC3, VPS11, and TUBB2A supply trafficking and cytoskeletal context without database-confirmed pairwise support.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module-level configuration appears unusual and is not already represented by a matching STRING network or hu.MAP complex. That supports novelty as a co-abundance observation, especially because it joins G-protein and calcium regulation with exocytosis, endosomal trafficking, and microtubules. It should not be called a wholly new biological pathway: the individual functions and disease associations of the genes are established, and the absence of STRING or hu.MAP support alone cannot prove novelty. The most defensible claim is that this particular cross-tissue co-abundance arrangement is a candidate novel association requiring validation in independent cohorts, cell-type-resolved data, and perturbation experiments.

**Hypothesis.** Hypothesis: in neuronal, glial, and keratinocyte-related cell populations, coordinated abundance of GNAI1 and NCS1 may tune receptor-linked cyclic-AMP and calcium signaling, while EXOC3, VPS11, and TUBB2A couple that signaling state to vesicle docking, endosomal or lysosomal routing, and microtubule-dependent intracellular transport. The shared brain-skin module may therefore represent a conserved secretory and membrane-trafficking state rather than a physical complex. A testable prediction is that perturbing GNAI1 or NCS1 will alter exocytic or endosomal trafficking phenotypes involving EXOC3 and VPS11, with dependence on the microtubule network involving TUBB2A. This is a mechanistic hypothesis, not an established interaction inferred from the supplied databases.

### Important genes

#### GNAI1

- **Related proteins** (co-abundance neighbors): TUBB2A (0.82), EXOC3 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Centrosome, Principal piece; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein subunit alpha i1. Guanine nucleotide binding proteins are heterotrimeric signal-transducing molecules consisting of alpha, beta, and gamma subunits. The alpha subunit binds guanine nucleotide, can hydrolyze GTP, and can interact with other proteins. The protein encoded by this gene represents the alpha subunit of an inhibitory complex. The encoded protein is part of a complex that responds to beta-adrenergic signal…
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia, impaired speech, and behavioral abnormalities (0.745); polycystic ovary syndrome (0.470); hereditary disease (0.412); complex neurodevelopmental disorder (0.370); neurodegenerative disease (0.323)
- **Europe PMC papers**: 1376
- **Why important**: GNAI1 has a high network position, connects directly to EXOC3 and TUBB2A, and is one of the genes supporting the primary globally corrected term (GO:MF cyclase regulator activity; q_global = 0.0206). Its established function as an inhibitory heterotrimeric G-protein alpha subunit provides the clearest entry point from the module into receptor signaling and adenylate-cyclase regulation. It has broad disease relevance, including neurodevelopmental and neurodegenerative associations, and substantial literature support.
- **Conclusion**: Established evidence supports GNAI1 as a signaling regulator and as a central connector between signaling, exocytosis, and microtubule context in this module. It is a leading candidate driver of the module's signaling interpretation. The proposed role in coordinating the other module members remains a hypothesis because neither STRING nor hu.MAP confirms those relationships.

#### NCS1

- **Related proteins** (co-abundance neighbors): EXOC3 (0.81), VPS11 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neuronal calcium sensor 1. This gene is a member of the neuronal calcium sensor gene family, which encode calcium-binding proteins expressed predominantly in neurons. The protein encoded by this gene regulates G protein-coupled receptor phosphorylation in a calcium-dependent manner and can substitute for calmodulin. The protein is associated with secretory granules and modulates synaptic transmission and synaptic plasticity…
- **Diseases (Open Targets)**: alcohol drinking (0.355); neurodegenerative disease (0.283); insomnia (0.252); benign chondrogenic neoplasm (0.186); bilirubin metabolism disease (0.143)
- **Europe PMC papers**: 713
- **Why important**: NCS1 has a high network position, connects to EXOC3 and VPS11, and is the other member supporting (GO:MF cyclase regulator activity; q_global = 0.0206). Its established calcium-sensor function, association with secretory granules, regulation of receptor phosphorylation, and role in synaptic transmission provide a mechanistic bridge between calcium signaling and vesicle biology. HPA annotations favor brain excitatory neurons and other neural cell types, and the gene has substantial disease and literature relevance.
- **Conclusion**: Established evidence supports NCS1 as the strongest calcium-sensitive and neuron-linked component of the module. Its co-abundance with EXOC3 and VPS11 is compatible with coordinated secretion and intracellular trafficking, but a direct regulatory chain among these proteins is only a hypothesis.

#### EXOC3

- **Related proteins** (co-abundance neighbors): NCS1 (0.81), GNAI1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exocyst complex component 3. The protein encoded by this gene is a component of the exocyst complex, a multiple protein complex essential for targeting exocytic vesicles to specific docking sites on the plasma membrane. Though best characterized in yeast, the component proteins and functions of exocyst complex have been demonstrated to be highly conserved in higher eukaryotes. At least eight components of the exocyst complex,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); hypospadias (0.172); hemorrhoid (0.156); Abnormality of the skeletal system (0.048); diabetes mellitus (0.038)
- **Europe PMC papers**: 362
- **Why important**: EXOC3 is the most connective structural bridge in the subgraph, linking both GNAI1 and NCS1. Its established role as an exocyst complex component places it at the interface of vesicle docking, plasma-membrane delivery, exocytosis, and cytoskeletal remodeling. Its broad tissue and cell-type profile makes it a plausible conserved trafficking component, while its disease associations add biological relevance despite the lack of primary enrichment support.
- **Conclusion**: Established evidence supports EXOC3 as a vesicle-targeting and exocytic component that can connect the module's signaling genes to cellular transport. Its central network placement makes it an important integrator, but the module does not establish that EXOC3 physically binds GNAI1 or NCS1.

#### VPS11

- **Related proteins** (co-abundance neighbors): NCS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS11 core subunit of CORVET and HOPS complexes. Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene encodes the human homolog of yeast class C Vps11 protein. The mammalian class C Vps proteins are predominantly associated with late…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 12 (0.723); neurodegenerative disease (0.527); POLR-related leukodystrophy (0.527); dystonia 32 (0.410); VPS11-related neurological disorder (0.370)
- **Europe PMC papers**: 849
- **Why important**: VPS11 is connected to NCS1 and is an established core component of the CORVET and HOPS trafficking systems, with roles in endosome organization, intracellular protein transport, and endosome-to-lysosome delivery. Its neural cell-type annotations and associations with leukodystrophy, neurodegeneration, and VPS11-related neurological disease make it particularly informative for the brain component of the module.
- **Conclusion**: Established evidence supports VPS11 as the endosomal and lysosomal trafficking arm of the module. Its association with NCS1 suggests a plausible shared trafficking state, but a specific NCS1-VPS11 mechanism is not established by the supplied interaction resources.

#### TUBB2A

- **Related proteins** (co-abundance neighbors): GNAI1 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tubulin beta 2A class IIa. Microtubules, key participants in processes such as mitosis and intracellular transport, are composed of heterodimers of alpha- and beta-tubulins. The protein encoded by this gene is a beta-tubulin. Defects in this gene are associated with complex cortical dysplasia with other brain malformations-5. Two transcript variants encoding distinct isoforms have been found for this gene. [provided by RefS…
- **Diseases (Open Targets)**: complex cortical dysplasia with other brain malformations 5 (0.749); Genetic central nervous system malformation (0.730); breast cancer (0.616); breast carcinoma (0.606); non-small cell lung carcinoma (0.606)
- **Europe PMC papers**: 1594
- **Why important**: TUBB2A is a terminal network member connected to GNAI1 and is an established beta-tubulin involved in microtubule organization, intracellular transport, neuronal migration, and cerebral-cortex development. It is brain-enriched, detected in brain and skin, and strongly relevant to cortical malformation and other neurological disease. Its substantial literature support makes it an important structural and disease-linked anchor even though it does not support (GO:MF cyclase regulator activity; q_global = 0.0206).
- **Conclusion**: Established evidence supports TUBB2A as the microtubule and neuronal-development component of the module. Its placement is compatible with cytoskeletal support for trafficking, but the inferred coupling to GNAI1-mediated signaling and the other module members remains a hypothesis.

## Module 14

**Tissue pair**: brain and skin  
**Genes (5)**: GANAB, PDIA4, PSMC6, RSL1D1, TXNDC5

### Function

The most coherent interpretation is an endoplasmic-reticulum protein quality-control and secretory-protein maturation module, with a broader proteostasis component. PDIA4 and TXNDC5 are ER thiol-disulfide enzymes involved in protein folding, secretion, and ER-stress responses; GANAB participates in glucosidase-II-mediated N-glycan processing and quality control; and PSMC6 is a proteasome ATPase linked to proteasomal degradation and ER-associated degradation. RSL1D1 connects the module to nucleolar and chromosome-associated RNA-binding functions and regulation of apoptosis, senescence, and protein localization. The direct functional enrichment support is supplementary STRING evidence: (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0144) links GANAB, TXNDC5, and PDIA4 to protein processing in the ER, while (STRING InterPro Disulphide isomerase; within-query FDR = 0.0222) and (STRING Pfam Thioredoxin; within-query FDR = 0.0429) support disulfide-isomerase and thioredoxin-related activity for TXNDC5 and PDIA4. No GO/KEGG term passed global correction, so there is no globally significant GO/KEGG enrichment to report. The lack of a globally significant term does not invalidate the module, especially given the small and functionally mixed gene set.

**Cell composition.** All module proteins were detected by HPA in both brain and skin, and every gene has low tissue specificity. The module therefore does not appear to represent a brain- or skin-restricted program. Several members are intracellular or membrane-associated rather than classical freely secreted proteins, although HPA classifies PDIA4, GANAB, and TXNDC5 as intracellular and membrane proteins and identifies multiple cell-type or blood-cell associations. TXNDC5 is group-enriched in choroid plexus epithelial cells and plasma cells and is also group-enriched in memory B cells, naive B cells, and plasmacytoid dendritic cells. PDIA4 has enhanced expression in plasma cells and other specialized cell types, while GANAB, PSMC6, and RSL1D1 have more limited or low cell-type specificity. These observations raise the possibility that part of the shared brain-skin signal reflects broadly distributed proteostasis biology, shared cell populations, or blood and immune-cell contribution rather than a tissue-specific mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING identifies one high-confidence pair within the module, GANAB-PDIA4, and this pair also has support in both listed hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). The STRING supplementary enrichment terms (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0144), (STRING InterPro Disulphide isomerase; within-query FDR = 0.0222), and (STRING Pfam Thioredoxin; within-query FDR = 0.0429) are concordant with an ER folding, glycan-processing, and thioredoxin interpretation, but they are not global corrections across all module tests and should not be treated as globally significant enrichment. hu.MAP independently places PDIA4 and GANAB in two large complexes, providing convergent evidence that their association is embedded in known protein-processing machinery. RSL1D1 and PSMC6 have no listed STRING partners or hu.MAP complexes, and TXNDC5 has no listed interaction or complex evidence in these resources. Thus, the network contains a known ER-processing core surrounded by more weakly characterized co-abundance links, rather than a fully documented physical complex.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: GANAB–PDIA4 (0.717)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Protein processing in endoplasmic reticulum (FDR = 0.0144, 3 genes); InterPro Disulphide isomerase (FDR = 0.0222, 2 genes); Pfam Thioredoxin (FDR = 0.0429, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (PDIA4, GANAB; 2/60); huMAP3_09327.1 (PDIA4, GANAB; 2/93)

### Novelty

This module should not be called a wholly new molecular complex or a newly discovered pathway. The GANAB-PDIA4 relationship is already represented in STRING and in both listed hu.MAP complexes, and the ER quality-control interpretation is consistent with established gene functions. The potentially novel aspect is the co-abundance configuration shared by brain and skin, particularly the connection of the established ER-processing core with RSL1D1, PSMC6, and TXNDC5 in these tissues. However, absence of the latter genes from the listed STRING or hu.MAP evidence does not prove novelty: it may reflect tissue-level co-regulation, indirect biology, incomplete interaction coverage, or sample-composition effects. Independent replication, perturbation, and comparison with existing tissue co-expression studies would be required to establish a new finding.

**Hypothesis.** Hypothesis: in both brain and skin, a shared cellular state involving synthesis and maturation of secretory or membrane proteins coordinates ER disulfide-bond formation, N-glycan quality control, and disposal of misfolded proteins. PDIA4 and TXNDC5 could provide thiol-disulfide processing, GANAB could assist glycan trimming, and PSMC6 could connect unresolved ER clients to proteasomal degradation. RSL1D1 may mark a linked nucleolar or stress-responsive program that coordinates protein localization, survival, or senescence rather than being a direct member of the ER machinery. A competing explanation is that the apparent shared module is driven partly by broadly expressed housekeeping proteins and plasma-cell, immune-cell, or other shared-cell contributions. This hypothesis should be tested by cell-type-aware analysis, assessment of secretory-load and ER-stress markers, and experimental testing of the GANAB-PDIA4, PDIA4-TXNDC5, and RSL1D1-linked relationships.

### Important genes

#### PDIA4

- **Related proteins** (co-abundance neighbors): GANAB (0.85), RSL1D1 (0.80); STRING partners: GANAB (0.717)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 is the most informative core gene for the ER interpretation: it connects directly to GANAB and RSL1D1 in the module, is the shared member of both hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), and is the STRING partner of GANAB. Its established function is ER protein folding and thiol-disulfide interchange, with roles in protein secretion and ER-stress response. It also anchors all three supplementary STRING terms (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0144), (STRING InterPro Disulphide isomerase; within-query FDR = 0.0222), and (STRING Pfam Thioredoxin; within-query FDR = 0.0429) and has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports PDIA4 as a central ER proteostasis component and as the strongest functional anchor of this module. It is plausible, but not established, that its co-abundance with the other genes reflects coordinated ER quality control in brain and skin.

#### GANAB

- **Related proteins** (co-abundance neighbors): PDIA4 (0.85); STRING partners: PDIA4 (0.717)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: glucosidase II alpha subunit. This gene encodes the alpha subunit of glucosidase II and a member of the glycosyl hydrolase 31 family of proteins. The heterodimeric enzyme glucosidase II plays a role in protein folding and quality control by cleaving glucose residues from immature glycoproteins in the endoplasmic reticulum. Expression of the encoded protein is elevated in lung tumor tissue and in response to UV irradiation. Mut…
- **Diseases (Open Targets)**: polycystic kidney disease 3 with or without polycystic liver disease (0.792); autosomal dominant polycystic liver disease (0.515); autosomal dominant polycystic kidney disease (0.470); Biliary tract abnormality (0.438); COVID-19 (0.370)
- **Europe PMC papers**: 1240
- **Why important**: GANAB is directly connected to PDIA4, is present in both hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), and contributes to the supplementary ER-processing signal (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0144). Its established role as the alpha subunit of glucosidase II places it in ER N-glycan processing and glycoprotein quality control. It also has strong disease associations involving autosomal-dominant polycystic kidney and liver disease and a substantial literature.
- **Conclusion**: Established evidence supports GANAB as the glycan-processing counterpart of the PDIA4 folding arm. The module data support a coordinated relationship between these functions, but do not establish a new GANAB mechanism in brain or skin.

#### TXNDC5

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Endoplasmic reticulum; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin domain containing 5. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal endoplasmic reticulum (ER)-signal sequence, three catalytically active thioredoxin domains and a C-terminal ER-retention sequence. Its expression is induced by hypoxia and its role ma…
- **Diseases (Open Targets)**: colorectal carcinoma (0.321); spinal stenosis (0.203); neoplasm (0.096); central nervous system cancer (0.092); glioma (0.091)
- **Europe PMC papers**: 1026
- **Why important**: TXNDC5 provides an independent ER thioredoxin-family signal and contributes with PDIA4 to the supplementary disulfide-isomerase and thioredoxin terms (STRING InterPro Disulphide isomerase; within-query FDR = 0.0222) and (STRING Pfam Thioredoxin; within-query FDR = 0.0429), as well as the ER-processing term (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0144). Its established functions include ER protein folding and negative regulation of apoptosis, with induction by hypoxia. HPA additionally associates it with choroid plexus epithelial cells, plasma cells, and selected blood-cell populations, making it important for interpreting possible cell-composition effects.
- **Conclusion**: Established evidence supports TXNDC5 as a biologically relevant ER folding and stress component. Its co-abundance with this module is consistent with a shared proteostasis state, but the lack of listed STRING or hu.MAP support means that a direct physical connection to the module is unproven.

#### PSMC6

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 6. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.606); mantle cell lymphoma (0.542); neoplasm (0.528); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 748
- **Why important**: PSMC6 is important because it supplies a proteasomal and ER-associated-degradation interpretation that is distinct from the ER folding enzymes. Its established annotation places it in the ATPase ring of the proteasome and in proteasomal protein catabolism, oxidative-stress response, and ER-associated degradation. It is linked to plasma-cell myeloma, other neoplastic conditions, HIV-related disease, and amyloidosis, and has a substantial literature. Its module link is to RSL1D1 rather than to the known GANAB-PDIA4 pair.
- **Conclusion**: Established evidence supports PSMC6 as a proteostasis disposal component. The hypothesis that it functionally couples this module to ER-associated degradation is biologically reasonable, but the module and interaction evidence do not demonstrate that coupling.

#### RSL1D1

- **Related proteins** (co-abundance neighbors): PSMC6 (0.83), TXNDC5 (0.81), PDIA4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in brain, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal L1 domain containing 1. Enables mRNA 3'-UTR binding activity and mRNA 5'-UTR binding activity. Involved in regulation of apoptotic process and regulation of cellular senescence. Acts upstream of or within regulation of protein localization. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: adolescent idiopathic scoliosis (0.219); hepatocellular carcinoma (0.099); neoplasm (0.099); colorectal carcinoma (0.096); insomnia (0.078)
- **Europe PMC papers**: 381
- **Why important**: RSL1D1 has the strongest network connectivity in the module and links PSMC6, TXNDC5, and PDIA4, making it the principal network bridge between the ER-associated genes and the proteasome-associated gene. Its established annotations concern mRNA untranslated-region binding, nucleolar and chromosome localization, protein localization, apoptosis, and cellular senescence. It has no listed STRING partner, no listed hu.MAP complex, and no listed enrichment term, but it has a substantial literature and disease associations including adolescent idiopathic scoliosis and several neoplastic conditions.
- **Conclusion**: Established evidence supports RSL1D1 as a nucleolar and regulatory protein with a broad stress and cell-state context. Its bridge position suggests a possible regulatory link between proteostasis and RNA or cell-survival programs, but that link is a hypothesis rather than an established molecular interaction.

## Module 15

**Tissue pair**: brain and skin  
**Genes (7)**: PSMC2, PAICS, CCT5, CCT3, CCT7, CCT8, CSE1L

### Function

The strongest interpretation is a conserved intracellular proteostasis and protein-folding module centered on the chaperonin-containing T-complex. The core signal is formed by CCT3, CCT5, CCT7, and CCT8, which jointly support the globally corrected chaperonin-containing T-complex and ATP-dependent protein-folding annotations (GO:CC chaperonin-containing T-complex; q_global = 2.53e-07), (GO:MF ATP-dependent protein folding chaperone; q_global = 4.4e-05), (GO:CC protein folding chaperone complex; q_global = 0.000114), (GO:MF protein folding chaperone; q_global = 0.000314), (GO:MF unfolded protein binding; q_global = 0.00115), (GO:BP protein stabilization; q_global = 0.0128), and (GO:BP protein folding; q_global = 0.0151). The same core also carries globally corrected annotations for RNA and protein localization to Cajal bodies, telomerase-RNA localization, telomere maintenance, DNA biosynthetic processes, and nuclear organization (11 globally significant GO/KEGG terms, q_global 2.53e-07–2.06e-06; see the table), (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 4.03e-06), (GO:BP regulation of telomere maintenance via telomerase; q_global = 3.31e-05), (4 globally significant GO/KEGG terms, q_global 5.67e-05–0.000114; see the table), (GO:BP telomere maintenance via telomere lengthening; q_global = 0.000167), (GO:BP regulation of DNA biosynthetic process; q_global = 0.000314), (GO:BP positive regulation of telomere maintenance; q_global = 0.000547), (GO:BP regulation of telomere maintenance; q_global = 0.00196), (5 globally significant GO/KEGG terms, q_global 0.00289–0.00667; see the table), (GO:BP RNA localization; q_global = 0.0209), (GO:BP positive regulation of DNA metabolic process; q_global = 0.0242), and (GO:BP regulation of chromosome organization; q_global = 0.0363). These latter annotations should be interpreted cautiously: they are biologically compatible with CCT-dependent folding or stabilization of nuclear and telomere-associated factors, but the co-abundance module alone does not establish a direct telomerase mechanism. The fertilization and cell-recognition annotations (GO:BP binding of sperm to zona pellucida; q_global = 4.03e-06), (GO:BP sperm-egg recognition; q_global = 6.92e-06), (GO:BP cell-cell recognition; q_global = 3.31e-05), (GO:BP cell recognition; q_global = 0.000272), (GO:BP single fertilization; q_global = 0.000314), and (GO:BP fertilization; q_global = 0.000779) are globally corrected but are less coherent with the principal intracellular chaperone interpretation and may reflect annotation connectivity or shared gene membership. PSMC2 adds a proteasomal ATPase/protein-quality-control component, CSE1L adds nuclear transport, and PAICS adds purine biosynthesis, suggesting peripheral links to protein turnover, nuclear trafficking, and biosynthetic capacity rather than a single complete pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and all module genes have low immune-cell specificity. All genes have low tissue specificity, with protein detected in brain and skin for nearly the entire module; CSE1L is detected in skin but not brain in the supplied HPA evidence. Several genes show cell-type-enhanced patterns involving germ-cell populations, erythrocyte progenitors, trophoblasts, or esophageal basal cells, while the module as a whole lacks a dominant enriched tissue or blood-cell signature. Thus, the brain-skin conservation is more consistent with broadly deployed intracellular proteostasis and nuclear functions, or with shared cellular stress and differentiation states, than with a plasma-protein or blood-contamination explanation. The cell-type-enhanced observations remain a possible source of sample-composition effects and should not be treated as evidence for a tissue-specific brain-skin mechanism.

**GO/KEGG enrichment**: 49 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chaperonin-containing T-complex | 2.53e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 2.53e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 2.53e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 8.62e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 8.62e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to Cajal body | 2.06e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 2.06e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 2.06e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 2.06e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 2.06e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 2.06e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 2.06e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP binding of sperm to zona pellucida | 4.03e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 4.03e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP sperm-egg recognition | 6.92e-06 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING supports a well-known CCT core: CCT3, CCT5, CCT7, and CCT8 are mutually connected, and CCT8 additionally connects with PSMC2. STRING independently annotates the CCT/TCP-1 chaperonin family, the chaperonin-containing T-complex, actin folding, and cellular proteostasis (11 supplementary STRING terms; within-query FDR 4.31e-07–1.73e-06). The lymphoblast tissue annotation (STRING TISSUES Lymphoblast; within-query FDR = 5.14e-09) is supplementary and does not establish that the module is blood-derived. The sperm-recognition and telomere-related STRING annotations (STRING Process Binding of sperm to zona pellucida; within-query FDR = 5.77e-06) (STRING Process Positive regulation of telomere maintenance via telomerase; within-query FDR = 5.77e-06) (STRING Process Positive regulation of establishment of protein localization to telomere; within-query FDR = 5.77e-06) agree with the corresponding GO membership but do not supersede the primary global correction framework. hu.MAP repeatedly places CCT3, CCT5, CCT7, and CCT8 together in several complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), with additional partners including TCP1, other CCT subunits, tubulin-related proteins, trafficking factors, and regulatory proteins. PAICS, PSMC2, and CSE1L have no hu.MAP complex with another module member in the supplied results; PSMC2 has a STRING link to CCT8, whereas PAICS and CSE1L lack listed STRING partners. Overall, the network is strongly anchored in an already established CCT complex, with weaker peripheral associations.

**STRING interactions (score >= 0.7)**: 7 of 21 gene pairs: CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999); CCT8–PSMC2 (0.733)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Lymphoblast (FDR = 5.14e-09, 7 genes); Pfam TCP-1/cpn60 chaperonin family (FDR = 4.31e-07, 4 genes); Component Chaperonin-containing T-complex (FDR = 5.07e-07, 4 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 5.55e-07, 4 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 9.27e-07, 4 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 9.27e-07, 4 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 9.27e-07, 4 genes); InterPro GroEL-like apical domain superfamily (FDR = 9.27e-07, 4 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 9.27e-07, 4 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 9.27e-07, 4 genes); RCTM Folding of actin by CCT/TriC (FDR = 1.3e-06, 4 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis (FDR = 1.73e-06, 4 genes); Process Binding of sperm to zona pellucida (FDR = 5.77e-06, 4 genes); Process Positive regulation of telomere maintenance via telomerase (FDR = 5.77e-06, 4 genes); Process Positive regulation of establishment of protein localization to telomere (FDR = 5.77e-06, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8)

### Novelty

This is not a new discovery of the CCT complex or of the physical relationships among its core subunits: those relationships are directly supported by STRING (11 supplementary STRING terms; within-query FDR 4.31e-07–1.73e-06) and multiple hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). The potentially novel result is the reproducible co-abundance of a CCT-centered module across the brain-skin tissue pair, together with its peripheral association with PSMC2, PAICS, and CSE1L. The supplied evidence does not establish whether that cross-tissue module has been reported previously, and absence of a PAICS- or CSE1L-containing hu.MAP complex does not prove novelty. The most defensible conclusion is therefore that the module represents a potentially context-specific systems-level observation built from a well-established molecular core, rather than a newly discovered protein complex or pathway.

**Hypothesis.** Hypothesis: in both brain and skin, a shared cellular state increases demand for CCT-mediated folding and stabilization of newly synthesized, cytoskeletal, and nuclear proteins. CCT3, CCT5, CCT7, and CCT8 could form the core proteostasis signal; CSE1L could couple that state to nuclear protein transport, PSMC2 could couple it to ubiquitin-dependent proteasomal clearance, and PAICS could reflect the biosynthetic capacity needed to sustain protein and nucleotide production. The globally corrected Cajal-body and telomere annotations suggest a testable possibility that CCT activity influences the folding, localization, or stability of telomere-associated factors, but this is a hypothesis rather than an established direct mechanism. Testing should examine module preservation across purified cell types, CCT-complex abundance and activity, nuclear-body localization, proteasome activity, and telomere-related readouts while controlling for cellular composition.

### Important genes

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT5 (0.93), CCT7 (0.91), CCT3 (0.85), PSMC2 (0.82); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999), PSMC2 (0.733)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is the strongest network hub in the supplied module and connects the CCT core to PSMC2. It participates in every globally corrected enrichment term listed for the module, is detected in both brain and skin, and has extensive literature support. STRING places it in the established CCT interaction core (11 supplementary STRING terms; within-query FDR 4.31e-07–1.73e-06), while hu.MAP places it with the other CCT subunits across multiple complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1).
- **Conclusion**: Established: CCT8 is a central subunit of the CCT chaperonin system and a principal marker of the module's proteostasis function. Hypothesis: its connection to PSMC2 may couple folding capacity to proteasomal quality control in the shared brain-skin state.

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT8 (0.93), CCT7 (0.88), CCT3 (0.84), PAICS (0.82); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is a highly connected core member linked to CCT3, CCT7, and CCT8, and it occurs in all supplied hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It has globally corrected annotations for chaperone activity, protein folding, protein stabilization, Cajal-body localization, and telomere maintenance (12 globally significant GO/KEGG terms, q_global 2.53e-07–2.06e-06; see the table), (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 4.03e-06), (GO:MF ATP-dependent protein folding chaperone; q_global = 4.4e-05), (GO:CC protein folding chaperone complex; q_global = 0.000114), (GO:MF protein folding chaperone; q_global = 0.000314), (GO:MF unfolded protein binding; q_global = 0.00115), and (7 globally significant GO/KEGG terms, q_global 0.0128–0.0463; see the table). The supplied disease evidence includes hereditary sensory and autonomic neuropathy with spastic paraplegia and neurodegenerative disease, making it especially relevant to a brain-containing module.
- **Conclusion**: Established: CCT5 is a core CCT chaperone subunit with disease-linked relevance to neuronal proteostasis. Hypothesis: variation in CCT5-dependent folding could influence the vulnerability of brain and skin cells to proteotoxic or differentiation-associated stress.

#### CCT7

- **Related proteins** (co-abundance neighbors): CCT8 (0.91), CCT5 (0.88), CSE1L (0.80); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is a highly connected CCT-core gene, detected in brain and skin and present in all supplied hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It shares the module's globally corrected chaperone, protein-folding, nuclear-localization, and telomere-related annotations (12 globally significant GO/KEGG terms, q_global 2.53e-07–2.06e-06; see the table), (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 4.03e-06), (GO:MF ATP-dependent protein folding chaperone; q_global = 4.4e-05), (GO:CC protein folding chaperone complex; q_global = 0.000114), (GO:MF protein folding chaperone; q_global = 0.000314), (GO:MF unfolded protein binding; q_global = 0.00115), and (7 globally significant GO/KEGG terms, q_global 0.0128–0.0463; see the table). Its disease associations include neurodegenerative disease and other systemic conditions, and its HPA cell-type enhancements include several germ-cell populations, indicating broad biological deployment rather than a uniquely brain-specific role.
- **Conclusion**: Established: CCT7 is a core component of the conserved CCT proteostasis signal. Hypothesis: CCT7 abundance may report a shared demand for folding of cytoskeletal or nuclear proteins during tissue maintenance and differentiation.

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT8 (0.85), CCT5 (0.84); STRING partners: CCT5 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in brain, skin
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a core CCT member connected to CCT5 and CCT8 and present in every supplied hu.MAP complex (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It contributes to all globally corrected terms attributed to the four-subunit CCT core, including ATP-dependent folding, protein stabilization, Cajal-body localization, and telomere maintenance (12 globally significant GO/KEGG terms, q_global 2.53e-07–2.06e-06; see the table), (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 4.03e-06), (GO:MF ATP-dependent protein folding chaperone; q_global = 4.4e-05), (GO:CC protein folding chaperone complex; q_global = 0.000114), (GO:MF protein folding chaperone; q_global = 0.000314), (GO:MF unfolded protein binding; q_global = 0.00115), and (7 globally significant GO/KEGG terms, q_global 0.0128–0.0463; see the table). It has the largest literature volume among the core genes in the fact sheet and disease associations involving neurodevelopmental and neurodegenerative conditions.
- **Conclusion**: Established: CCT3 is a well-supported structural and functional anchor of the module's CCT interpretation. Hypothesis: CCT3 may help transmit changes in cellular folding demand into nuclear protein-localization or chromosome-organization phenotypes.
