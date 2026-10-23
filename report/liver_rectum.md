# Conserved co-abundance modules: liver and rectum

## Module 0

**Tissue pair**: liver and rectum  
**Genes (27)**: SLC3A2, AIMP2, CLIC1, DDX5, DDX6, EIF3F, EWSR1, TBRG4, H1-5, HNRNPK, HNRNPL, HNRNPR, NCEH1, NOP56, PSPC1, PTBP1, CAD, RPL6, MRPL48, RPRD1B, RUVBL2, SERPINH1, SUPT16H, SRP68, CCT8, TFRC, TMEM214

### Function

The module is best interpreted as a conserved nuclear RNA and gene-expression machinery module. The primary evidence is the globally corrected enrichment for ribonucleoprotein complex (GO:CC ribonucleoprotein complex; q_global = 0.000208), RNA binding (GO:MF RNA binding; q_global = 0.00156), nucleic-acid binding (GO:MF nucleic acid binding; q_global = 0.00215), gene expression (GO:BP gene expression; q_global = 0.00437), macromolecule biosynthesis (GO:BP macromolecule biosynthetic process; q_global = 0.0103), nucleic-acid biosynthesis and metabolism (GO:BP nucleic acid biosynthetic process; q_global = 0.0108)(GO:BP nucleic acid metabolic process; q_global = 0.0303), RNA biosynthesis (GO:BP RNA biosynthetic process; q_global = 0.0317), and regulation of alternative messenger-RNA splicing through the spliceosome together with pre-messenger-RNA binding (GO:BP regulation of alternative mRNA splicing, via spliceosome; q_global = 0.049)(GO:MF pre-mRNA binding; q_global = 0.049). The genes therefore point to coordinated RNA handling, including ribonucleoprotein assembly, RNA processing and splicing, transcriptional regulation, translation-related functions, and RNA turnover. This is a functional interpretation of the gene composition and network, not evidence that every listed process occurs in the same physical complex or that the module is tissue-specific.

**Cell composition.** The module is dominated by broadly expressed intracellular and nuclear proteins rather than plasma or secreted proteins. HPA reports low tissue specificity for most genes, low immune-cell specificity for nearly all genes, and only a small secreted-gene component. Protein detection is extensive in both liver and rectum. The data therefore do not strongly support a plasma-protein or blood-cell contamination explanation. A limited blood-related contribution cannot be excluded because TFRC is secreted to blood and is enhanced in a non-classical monocyte population, while H1-5 is enriched in bone marrow and lymphoid tissue and in progenitor populations. Several genes also show cell-type-enhanced expression in trophoblast, germ-cell, stromal, epithelial, or erythroid populations, but these patterns are scattered rather than forming a coherent blood-cell signature. Overall, the shared module is more consistent with a broadly expressed housekeeping-like RNA and gene-expression program present in cells from both tissues than with a module driven mainly by circulating material.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC ribonucleoprotein complex | 0.000208 | DDX5, DDX6, EIF3F, HNRNPK, HNRNPL, HNRNPR, MRPL48, NOP56, RPL6, RUVBL2, SRP68 |
| GO:MF RNA binding | 0.00156 | DDX5, DDX6, EWSR1, FASTKD4, H1-5, HNRNPK, HNRNPL, HNRNPR, NOP56, PSPC1, PTBP1, RPL6, SERPINH1, SLC3A2, SRP68, SUPT16H, TFRC |
| GO:MF nucleic acid binding | 0.00215 | DDX5, DDX6, EWSR1, FASTKD4, H1-5, HNRNPK, HNRNPL, HNRNPR, NOP56, PSPC1, PTBP1, RPL6, RUVBL2, SERPINH1, SLC3A2, SRP68, SUPT16H, TFRC |
| GO:BP gene expression | 0.00437 | AIMP2, CCT8, DDX5, DDX6, EIF3F, EWSR1, FASTKD4, H1-5, HNRNPK, HNRNPL, HNRNPR, MRPL48, NOP56, PSPC1, PTBP1, RPL6, RPRD1B, RUVBL2, SERPINH1, SUPT16H, TFRC |
| GO:BP macromolecule biosynthetic process | 0.0103 | AIMP2, CCT8, DDX5, DDX6, EIF3F, EWSR1, FASTKD4, H1-5, HNRNPK, HNRNPL, HNRNPR, MRPL48, NOP56, PSPC1, PTBP1, RPL6, RPRD1B, RUVBL2, SERPINH1, SUPT16H, TFRC |
| GO:BP nucleic acid biosynthetic process | 0.0108 | CCT8, DDX5, EWSR1, FASTKD4, H1-5, HNRNPK, HNRNPL, HNRNPR, NOP56, PSPC1, PTBP1, RPL6, RPRD1B, RUVBL2, SUPT16H |
| GO:BP regulation of nucleobase-containing compound metabolic process | 0.0191 | CCT8, DDX5, EWSR1, FASTKD4, H1-5, HNRNPK, HNRNPL, PSPC1, PTBP1, RPL6, RPRD1B, RUVBL2, SUPT16H, TFRC |
| GO:BP nucleic acid metabolic process | 0.0303 | CCT8, DDX5, EWSR1, FASTKD4, H1-5, HNRNPK, HNRNPL, HNRNPR, NOP56, PSPC1, PTBP1, RPL6, RPRD1B, RUVBL2, SUPT16H, TFRC |
| GO:BP RNA biosynthetic process | 0.0317 | DDX5, EWSR1, FASTKD4, H1-5, HNRNPK, HNRNPL, HNRNPR, NOP56, PSPC1, PTBP1, RPL6, RPRD1B, RUVBL2, SUPT16H |
| GO:BP regulation of alternative mRNA splicing, via spliceosome | 0.049 | DDX5, HNRNPL, PTBP1 |
| GO:MF pre-mRNA binding | 0.049 | DDX5, HNRNPL, PTBP1 |

### STRING and hu.MAP

STRING independently supports nucleic-acid binding (STRING Function Nucleic acid binding; within-query FDR = 0.00025), ribonucleoprotein complexes (STRING Component Ribonucleoprotein complex; within-query FDR = 0.00033)(STRING Keyword Ribonucleoprotein; within-query FDR = 0.0023)(STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.0036), RNA binding (STRING Function RNA binding; within-query FDR = 0.00057), nuclear or nucleoplasmic localization (STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.0031)(STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0036)(STRING Keyword Nucleus; within-query FDR = 0.0054), and RNA-binding or transcription-related keywords (STRING Keyword RNA-binding; within-query FDR = 0.0054)(STRING Keyword Transcription regulation; within-query FDR = 0.0128). The strongest known relationships concentrate around the HNRNPK-HNRNPL-HNRNPR-PTBP1 group, with additional links involving DDX5, DDX6, EWSR1, NOP56, RUVBL2, RPL6, EIF3F, and SRP68. The STRING network therefore recapitulates known RNA-binding and ribonucleoprotein biology rather than providing evidence that all module edges are direct physical interactions. hu.MAP gives especially strong complex-level support for the hnRNP-centered relationships: HNRNPK, HNRNPL, and HNRNPR co-occur in multiple complexes (hu.MAP huMAP3_10659.1)(hu.MAP huMAP3_10625.1), HNRNPL and HNRNPR recur in additional complexes (hu.MAP huMAP3_07225.1)(hu.MAP huMAP3_06093.1)(hu.MAP huMAP3_09654.1)(hu.MAP huMAP3_07581.1), and EWSR1 with PSPC1 occurs in complexes containing SFPQ and NONO (hu.MAP huMAP3_09312.1)(hu.MAP huMAP3_10666.1). The overlap between the co-abundance network, STRING relationships, and hu.MAP complexes supports a real RNA-processing core, while the absence of hu.MAP or high-confidence STRING support for some peripheral genes indicates that the module also contains correlated pathway partners or context-dependent associations.

**STRING interactions (score >= 0.7)**: 17 of 351 gene pairs: CCT8–RPL6 (0.78); CCT8–RUVBL2 (0.776); DDX5–EWSR1 (0.817); DDX5–HNRNPK (0.935); DDX5–HNRNPR (0.844); DDX6–HNRNPK (0.748); EIF3F–RPL6 (0.856); EWSR1–HNRNPK (0.798); EWSR1–HNRNPR (0.786); HNRNPK–HNRNPL (0.99); HNRNPK–HNRNPR (0.962); HNRNPK–PTBP1 (0.997); HNRNPL–HNRNPR (0.961); HNRNPL–PTBP1 (0.993); HNRNPR–PTBP1 (0.875); NOP56–RUVBL2 (0.847); RPL6–SRP68 (0.904)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Nucleic acid binding (FDR = 0.00025, 19 genes); Component Ribonucleoprotein complex (FDR = 0.00033, 11 genes); Function RNA binding (FDR = 0.00057, 17 genes); Keyword Ribonucleoprotein (FDR = 0.0023, 7 genes); COMPARTMENTS Nucleoplasm (FDR = 0.0031, 10 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0036, 12 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 0.0036, 9 genes); Keyword Nucleus (FDR = 0.0054, 17 genes); Keyword RNA-binding (FDR = 0.0054, 9 genes); Keyword Ubl conjugation (FDR = 0.0055, 13 genes); Keyword Transcription regulation (FDR = 0.0128, 7 genes); Keyword Isopeptide bond (FDR = 0.0172, 11 genes); NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex (FDR = 0.0204, 5 genes); NetworkNeighborAL Mixed, incl. Zinc finger, CHHC-type, and Multisystem proteinopathy (FDR = 0.0204, 4 genes); NetworkNeighborAL Multisystem proteinopathy, and HnRNP-L/PTB (FDR = 0.0204, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10659.1 (HNRNPR, HNRNPL, HNRNPK; 3/28); huMAP3_10625.1 (HNRNPR, HNRNPL, HNRNPK; 3/57); huMAP3_09312.1 (EWSR1, PSPC1; 2/4); huMAP3_10666.1 (EWSR1, PSPC1; 2/6); huMAP3_07225.1 (HNRNPR, HNRNPL; 2/7); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09654.1 (HNRNPR, HNRNPL; 2/13); huMAP3_07581.1 (HNRNPR, HNRNPL; 2/21)

### Novelty

The module should not be described as a wholly new molecular complex. Much of its central biology is already established: hnRNP interactions, the DDX5 and RNA-binding relationships, paraspeckle-associated EWSR1-PSPC1 context, and ribonucleoprotein functions are represented in STRING, hu.MAP, and the gene annotations. The potentially novel result is instead the conserved co-abundance configuration shared by liver and rectum, particularly the way established RNA-processing factors are coordinated with less connected genes such as RPRD1B, TMEM214, NCEH1, TBRG4, or tissue-observed metabolic and translation-related components. Database absence for individual edges does not demonstrate novelty, because co-abundance can reflect indirect regulation, shared cell state, or technical and tissue context. The appropriate conclusion is that this is a potentially novel tissue-pair co-abundance association built around largely known RNA and gene-expression machinery, requiring replication and perturbation experiments before being called a new mechanism.

**Hypothesis.** Hypothesis: the conserved module represents a shared cell-intrinsic RNA homeostasis program in liver and rectum. A core formed by DDX5, HNRNPK, HNRNPL, HNRNPR, and PTBP1 may coordinate pre-messenger-RNA binding, alternative splicing, RNA processing, and transcript fate, while PSPC1 may connect this program to paraspeckle or nuclear RNA-retention biology. RPRD1B and SUPT16H could couple RNA processing to RNA polymerase II transcription and chromatin-associated transcriptional control. NOP56, RUVBL2, ribosomal proteins, SRP68, EIF3F, and related genes may link nuclear RNA production to ribosome, mitochondrial, translation, or membrane-targeting demands. This model predicts that perturbing the hnRNP or DDX5-centered core should alter splicing and transcript stability in both tissues, whereas the peripheral genes may modify the response according to cell state. The hypothesis remains unproven by co-abundance alone.

### Important genes

#### DDX5

- **Related proteins** (co-abundance neighbors): PSPC1 (0.89), CAD (0.89), RPRD1B (0.88), TMEM214 (0.86), HNRNPR (0.85), DDX6 (0.84), HNRNPK (0.84), AIMP2 (0.84), NCEH1 (0.83), SUPT16H (0.83), NOP56 (0.83), PTBP1 (0.83), SLC3A2 (0.83), RUVBL2 (0.82); STRING partners: EWSR1 (0.817), HNRNPK (0.935), HNRNPR (0.844)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 is the strongest network hub in the supplied module and connects the hnRNP-centered core with PSPC1, RPRD1B, DDX6, AIMP2, and other module members. It appears in every globally corrected GO term (11 globally significant GO/KEGG terms, q_global 0.000208–0.049; see the table), including the primary splicing and pre-messenger-RNA-binding terms (GO:BP regulation of alternative mRNA splicing, via spliceosome; q_global = 0.049)(GO:MF pre-mRNA binding; q_global = 0.049). Its annotation supports RNA-structure remodeling, transcriptional co-regulation, alternative splicing, and small noncoding-RNA processing. Its STRING links to HNRNPK, HNRNPR, and EWSR1 and its substantial literature volume make it the best anchor for interpreting the module.
- **Conclusion**: Established evidence supports DDX5 as a central RNA-processing and transcriptional regulator in this module. It is plausible that DDX5 helps organize the shared program, but the co-abundance data do not establish that it causally controls the other module genes.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): PTBP1 (0.89), HNRNPR (0.88), RPRD1B (0.87), DDX5 (0.84), TMEM214 (0.83), SLC3A2 (0.83), PSPC1 (0.82), RPL6 (0.82), SUPT16H (0.81), HNRNPL (0.81), NOP56 (0.81); STRING partners: DDX5 (0.935), DDX6 (0.748), EWSR1 (0.798), HNRNPL (0.99), HNRNPR (0.962), PTBP1 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, rectum
- **hu.MAP 3.0**: huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is a highly connected module member and a major bridge among DDX5, DDX6, EWSR1, HNRNPL, HNRNPR, and PTBP1. It participates in the globally corrected ribonucleoprotein, RNA-binding, nucleic-acid-binding, gene-expression, biosynthetic, and nucleic-acid-process terms (9 globally significant GO/KEGG terms, q_global 0.000208–0.0317; see the table). STRING gives particularly strong support for its relationships with HNRNPL, HNRNPR, PTBP1, and DDX5, while hu.MAP places it with HNRNPL and HNRNPR in multiple hnRNP complexes (hu.MAP huMAP3_10659.1)(hu.MAP huMAP3_10625.1). It is broadly expressed and detected in both tissues, reducing concern that its signal is simply a blood-cell artifact.
- **Conclusion**: Established evidence identifies HNRNPK as a core hnRNP and gene-expression component of the module. Its central position makes it a strong candidate mediator, but whether it drives liver-rectum conservation or merely reflects shared RNA-processing activity is a hypothesis.

#### PTBP1

- **Related proteins** (co-abundance neighbors): HNRNPK (0.89), RPRD1B (0.88), TMEM214 (0.87), HNRNPL (0.84), DDX5 (0.83), HNRNPR (0.83), NCEH1 (0.81), PSPC1 (0.80); STRING partners: HNRNPK (0.997), HNRNPL (0.993), HNRNPR (0.875)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypyrimidine tract binding protein 1. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA-binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.505); dengue disease (0.372); open-angle glaucoma (0.330); glaucoma (0.309); neoplasm (0.116)
- **Europe PMC papers**: 4849
- **Why important**: PTBP1 is a central network connector and one of the three genes supporting the globally corrected alternative-splicing and pre-messenger-RNA-binding terms (GO:BP regulation of alternative mRNA splicing, via spliceosome; q_global = 0.049)(GO:MF pre-mRNA binding; q_global = 0.049). Its annotation directly supports RNA splicing, messenger-RNA processing, and regulation of RNA splicing. It has very strong STRING relationships with HNRNPK and HNRNPL and is part of the STRING-supported mRNA-processing and hnRNP-neighbor group (STRING NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex; within-query FDR = 0.0204)(STRING NetworkNeighborAL Multisystem proteinopathy, and HnRNP-L/PTB; within-query FDR = 0.0204). Its broad expression, detection in both tissues, and extensive literature make it a particularly informative functional marker of the module.
- **Conclusion**: Established evidence supports PTBP1 as a core alternative-splicing regulator embedded in the module's hnRNP network. A role in coordinating tissue-shared transcript processing is a reasonable hypothesis, but it requires transcript-level or perturbation evidence.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): SUPT16H (0.88), PSPC1 (0.84), PTBP1 (0.84), RPRD1B (0.83), HNRNPK (0.81); STRING partners: HNRNPK (0.99), HNRNPR (0.961), PTBP1 (0.993)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, rectum
- **hu.MAP 3.0**: huMAP3_10659.1, huMAP3_10625.1, huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_07581.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is a network-connected hnRNP member and one of the genes supporting the globally corrected splicing and pre-messenger-RNA-binding terms (GO:BP regulation of alternative mRNA splicing, via spliceosome; q_global = 0.049)(GO:MF pre-mRNA binding; q_global = 0.049). It appears across the ribonucleoprotein, RNA-binding, nucleic-acid, and gene-expression evidence (9 globally significant GO/KEGG terms, q_global 0.000208–0.0317; see the table). STRING supports very strong connections to HNRNPK, HNRNPR, and PTBP1, and hu.MAP repeatedly places it with HNRNPR and other hnRNP proteins (hu.MAP huMAP3_10659.1)(hu.MAP huMAP3_10625.1)(hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_07581.1). Its established role in messenger-RNA packaging, processing, and splicing makes it a key interpretive gene despite having a more modest direct network position than DDX5 or HNRNPK.
- **Conclusion**: Established evidence supports HNRNPL as a core structural and functional component of the module's RNA-processing machinery. Its contribution to the shared tissue pattern is supported by co-abundance but remains mechanistic inference.

#### PSPC1

- **Related proteins** (co-abundance neighbors): DDX5 (0.89), SUPT16H (0.89), HNRNPR (0.85), HNRNPL (0.84), AIMP2 (0.84), HNRNPK (0.82), RUVBL2 (0.81), DDX6 (0.81), CAD (0.80), PTBP1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, rectum
- **hu.MAP 3.0**: huMAP3_09312.1, huMAP3_10666.1
- **Function (MyGene.info)**: paraspeckle component 1. This gene encodes a nucleolar protein that localizes to punctate subnuclear structures that occur close to splicing speckles, known as paraspeckles. These paraspeckles are composed of RNA-protein structures that include a non-coding RNA, NEAT1/Men epsilon/beta, and the Drosophila Behavior Human Splicing family of proteins, which include the product of this gene and the P54NRB/NONO and PSF/SFPQ pro…
- **Diseases (Open Targets)**: sleep apnea syndrome (0.217); nephrotic syndrome (0.201); squamous cell lung carcinoma (0.196); Hypercholesterolemia (0.148); sleep disorder (0.126)
- **Europe PMC papers**: 1076
- **Why important**: PSPC1 is among the more connected module genes and links the central RNA-processing group to SUPT16H, AIMP2, RUVBL2, DDX6, and the hnRNP proteins. It contributes to the globally corrected RNA-binding and gene-expression terms (8 globally significant GO/KEGG terms, q_global 0.00156–0.0317; see the table). Its annotation places it in paraspeckles and related nuclear RNA-protein structures, and hu.MAP supports complexes containing PSPC1 and EWSR1 together with SFPQ and NONO (hu.MAP huMAP3_09312.1)(hu.MAP huMAP3_10666.1). Unlike several central genes, PSPC1 has no listed high-confidence STRING partner in this module, making its co-abundance connection to the network especially informative but less directly established.
- **Conclusion**: Established evidence supports PSPC1 as a nuclear RNA-protein and paraspeckle-associated component connected to the module's expression machinery. Its role as a bridge between paraspeckle biology and the shared tissue module is a hypothesis rather than a demonstrated causal mechanism.

#### RPRD1B

- **Related proteins** (co-abundance neighbors): DDX5 (0.88), PTBP1 (0.88), SUPT16H (0.87), HNRNPK (0.87), HNRNPR (0.86), HNRNPL (0.83), CLIC1 (0.81), DDX6 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: regulation of nuclear pre-mRNA domain containing 1B. Enables RNA polymerase II complex binding activity and identical protein binding activity. Involved in positive regulation of cell population proliferation; regulation of cell cycle process; and regulation of transcription by RNA polymerase II. Located in nucleoplasm. Part of RNA polymerase II, holoenzyme. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.399); alcohol drinking (0.167); gastric carcinoma (0.153); neoplasm (0.115); colorectal carcinoma (0.101)
- **Europe PMC papers**: 260
- **Why important**: RPRD1B has a substantial module position despite limited external interaction annotation. It connects DDX5, PTBP1, SUPT16H, HNRNPK, HNRNPR, HNRNPL, CLIC1, and DDX6. Its annotation supports RNA polymerase II complex binding, promoter clearance, transcriptional regulation, messenger-RNA three-prime-end processing, and cell-cycle-related regulation. It is tissue-enhanced in liver but detected in both liver and rectum, making it a potentially informative contributor to conservation with a possible liver-associated modulation. Its literature volume is smaller than that of the core hnRNP genes, and it has no listed hu.MAP complex or STRING partner here.
- **Conclusion**: Established evidence supports RPRD1B as a transcription-associated nuclear factor that may connect transcription to RNA maturation. Its placement in this conserved module is suggestive of a coordinating role, but the lack of listed external complex support makes that role a testable hypothesis rather than an established conclusion.

## Module 1

**Tissue pair**: liver and rectum  
**Genes (5)**: ABCF1, COPG2, MAPRE2, POLR2B, SMARCC2

### Function

The module does not map to a statistically supported GO or KEGG function: no GO or KEGG term passed global correction, and there are no supplementary STRING enrichment terms. Its genes nevertheless represent several established intracellular processes: POLR2B supports RNA polymerase II transcription, SMARCC2 supports SWI/SNF chromatin remodeling and transcriptional regulation, ABCF1 is associated with translation and translational initiation, COPG2 supports COPI-dependent Golgi and retrograde vesicle transport, and MAPRE2 supports microtubule organization, spindle assembly, and cell-structure dynamics. The co-abundance topology places POLR2B as the central connector, with links to MAPRE2, COPG2, and SMARCC2, while MAPRE2 also links to ABCF1. Taken together, the most defensible interpretation is a shared basal cellular-maintenance or proliferative-state signal involving transcriptional control, protein synthesis, trafficking, and cytoskeletal organization, rather than a demonstrated single pathway. Because the network is small and lacks enrichment support, this functional interpretation remains integrative and provisional.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and the encoded proteins are intracellular, including nucleoplasmic, cytosolic, or intracellular-transport components. Most genes have low tissue specificity, while one is tissue enhanced in brain. Cell-type enhancement is heterogeneous, involving reproductive, placental, adipocyte, cardiac-associated, immune, retinal, and renal cell annotations rather than one recurring cell population. All genes have low immune-cell specificity, with no enriched blood-cell category reported. This argues against a straightforward blood-contamination or plasma-protein explanation for the shared liver–rectum signal. Protein detection is broadly consistent with the module in both tissues, although one gene is not detected in liver; this supports presence in the sampled tissues but does not establish that every gene is expressed by the same cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, no STRING functional-enrichment term was reported, and no hu.MAP complex contained multiple module members. The observed co-abundance links are therefore not corroborated here as established protein–protein interactions or membership in a known multiprotein complex. Known biology still provides functional context: POLR2B belongs to RNA polymerase II, SMARCC2 belongs to the SWI/SNF chromatin-remodeling system, COPG2 belongs to the COPI coat, ABCF1 is a translation-associated ABC-family protein without transmembrane domains, and MAPRE2 is a microtubule-associated protein related to the EB family. The lack of STRING and hu.MAP support favors an indirect, state-dependent, or transcriptionally coordinated explanation for the co-abundance pattern rather than a single physical complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The specific liver–rectum co-abundance module may be a new data-derived association, because this particular gene grouping is not supported by the reported high-confidence STRING network or by a hu.MAP complex. However, it cannot be called a new biological mechanism on that basis alone. The genes have established, separately characterized roles, the module lacks globally significant GO or KEGG enrichment, and absence from interaction resources can reflect incomplete coverage, context dependence, indirect regulation, or tissue-specific behavior. The strongest novelty claim is therefore the reproducible cross-tissue co-abundance relationship itself, not discovery of a new complex or pathway. Independent replication and perturbation would be needed to establish biological novelty.

**Hypothesis.** Hypothesis: the shared liver–rectum module reflects a conserved intracellular state in which transcriptional output and chromatin accessibility are coordinated with translation, vesicle trafficking, and microtubule organization. POLR2B and SMARCC2 could represent the transcriptional and chromatin-regulatory axis, ABCF1 the protein-synthesis axis, and COPG2 plus MAPRE2 the trafficking and cytoskeletal axes. The module may therefore report a common epithelial or proliferative cellular-maintenance program rather than a direct protein complex. This is a hypothesis, not an established causal model; the absence of enrichment and physical-interaction support means that the direction of regulation, the responsible cell type, and the biological trigger remain unresolved.

### Important genes

#### POLR2B

- **Related proteins** (co-abundance neighbors): COPG2 (0.83), SMARCC2 (0.81), MAPRE2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase II subunit B. This gene encodes the second largest subunit of RNA polymerase II (Pol II), a DNA-dependent RNA polymerase that catalyzes the transcription of DNA into precursors of mRNA, snRNA and microRNA. This subunit and the largest subunit form opposite sides of the center cleft of Pol II. Deletion of the flap loop region of this subunit results in a decrease in the rate of transcriptional elongation. Altern…
- **Diseases (Open Targets)**: HIV infectious disease (0.600); Orthomyxoviridae infectious disease (0.370); dengue disease (0.370); acrocephalosyndactyly (0.370); neurodegenerative disease (0.341)
- **Europe PMC papers**: 589
- **Why important**: POLR2B has the most central network position, connecting to MAPRE2, COPG2, and SMARCC2. Its established function as the second-largest RNA polymerase II subunit makes it the strongest candidate for a transcriptional backbone linking otherwise diverse cellular processes. It has broad tissue and cell-type expression in HPA, is detected in both relevant tissues, and has substantial literature coverage. Its disease associations include infectious and neurodegenerative disease categories, although those associations do not establish relevance to this module.
- **Conclusion**: Established: POLR2B is a core RNA polymerase II component and the network hub of this module. Hypothesis: its centrality may reflect a shared transcriptional state that coordinates the other genes, but the co-abundance data do not show that POLR2B causally regulates them.

#### SMARCC2

- **Related proteins** (co-abundance neighbors): POLR2B (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SWI/SNF related BAF chromatin remodeling complex subunit C2. The protein encoded by this gene is a member of the SWI/SNF family of proteins, whose members display helicase and ATPase activities and which are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI and contains a predicted leucine zipper motif typical …
- **Diseases (Open Targets)**: Coffin-Siris syndrome 8 (0.720); Intellectual disability (0.564); Coffin-Siris syndrome (0.503); hereditary disease (0.468); Global developmental delay (0.463)
- **Europe PMC papers**: 1300
- **Why important**: SMARCC2 connects directly to POLR2B and provides a complementary chromatin-regulatory explanation for the module. It is a component of the ATP-dependent SWI/SNF remodeling system and is annotated for chromatin remodeling and regulation of RNA polymerase II transcription. It has the largest literature volume among the module genes and strong disease associations involving Coffin–Siris syndrome and developmental disability. It is detected in both tissues and has low tissue and immune specificity.
- **Conclusion**: Established: SMARCC2 participates in chromatin remodeling and transcriptional regulation. Hypothesis: coordinated SMARCC2 and POLR2B abundance could mark a shared transcriptional or differentiation state in liver and rectum, but no direct module-specific interaction is established.

#### MAPRE2

- **Related proteins** (co-abundance neighbors): ABCF1 (0.86), POLR2B (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: microtubule associated protein RP/EB family member 2. The protein encoded by this gene shares significant homology to the adenomatous polyposis coli (APC) protein-binding EB1 gene family. This protein is a microtubule-associated protein that is necessary for spindle symmetry during mitosis. It is thought to play a role in the tumorigenesis of colorectal cancers and the proliferative control of normal cells. Alternative splicing of this gene results i…
- **Diseases (Open Targets)**: multiple benign circumferential skin creases on limbs (0.746); skin creases, congenital symmetric circumferential, 2 (0.697); neurodegenerative disease (0.464); Brugada syndrome (0.388); developmental disability (0.340)
- **Europe PMC papers**: 475
- **Why important**: MAPRE2 is the second network connector: it links ABCF1 to POLR2B and has the strongest direct co-abundance edge in the module. Its established functions include microtubule organization, spindle assembly, and regulation of cell migration-related processes. The annotation specifically notes a possible role in colorectal tumorigenesis and proliferative control of normal cells, which is relevant to a rectal tissue context. It is tissue enhanced in brain, detected in rectum but not liver by the reported HPA immunohistochemistry, and has substantial literature coverage.
- **Conclusion**: Established: MAPRE2 is a microtubule-associated protein with roles in spindle and cytoskeletal organization. Hypothesis: MAPRE2 may connect transcriptional state to cell architecture or proliferation in this shared module, but the apparent cross-tissue association should not be interpreted as proof of a colorectal cancer mechanism.

#### ABCF1

- **Related proteins** (co-abundance neighbors): MAPRE2 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP binding cassette subfamily F member 1. The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the GCN20 subfamily. Unlike other members of the superfamily, this protein lac…
- **Diseases (Open Targets)**: urinary bladder cancer (0.074); urinary bladder carcinoma (0.074); lung adenocarcinoma (0.048); hepatocellular carcinoma (0.036); glioblastoma (0.033)
- **Europe PMC papers**: 964
- **Why important**: ABCF1 is the peripheral partner attached to MAPRE2 and contributes a translation-related axis distinct from the transcriptional and cytoskeletal annotations. It is an ABC-family protein lacking the transmembrane domains typical of many transporters and is annotated for translation, translational initiation, inflammatory response, and ribosome biogenesis. It is detected in both tissues, has heterogeneous cell-type enhancement, low immune specificity, and substantial literature coverage. Its disease associations include several cancer categories, but the reported association strengths are not evidence that it drives this module.
- **Conclusion**: Established: ABCF1 is an intracellular translation-associated ABC-family protein. Hypothesis: its co-abundance with MAPRE2 may indicate coupling between protein synthesis and cytoskeletal or proliferative state, but there is no evidence here for a direct ABCF1–MAPRE2 complex.

#### COPG2

- **Related proteins** (co-abundance neighbors): POLR2B (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coat protein complex I subunit gamma 2. Predicted to enable structural molecule activity. Involved in intra-Golgi vesicle-mediated transport. Part of COPI vesicle coat. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.410); skin neoplasm (0.327); Alzheimer disease (0.253); alcohol drinking (0.252); stroke disorder (0.252)
- **Europe PMC papers**: 389
- **Why important**: COPG2 is directly connected to the central POLR2B node and introduces intracellular trafficking into the module. It is a component of the COPI coat and is annotated for Golgi-to-endoplasmic-reticulum retrograde transport, intra-Golgi transport, and vesicle-mediated transport. It is detected in both tissues, has low tissue and immune specificity, and shows cell-type enhancement in adipocyte-, epicardial-, and thyrotroph-associated annotations. Its literature volume is more limited than that of the other selected genes, which makes its presence potentially informative but less independently characterized.
- **Conclusion**: Established: COPG2 contributes to COPI vesicle-coat function and intracellular transport. Hypothesis: its association with POLR2B may reflect a broader cellular-maintenance or secretory-pathway state, but the data do not demonstrate transcriptional control of COPG2 or a physical COPG2–POLR2B interaction.

## Module 2

**Tissue pair**: liver and rectum  
**Genes (39)**: ACIN1, AFDN, AP3D1, ATAD3A, CNOT1, COPB1, CASK, CTNND1, CACYBP, DNM1L, EIF3L, GAR1, GARS1, GTF2I, GMPS, NUP155, NUP160, NUP93, ALDH18A1, PCNA, PSMG1, UPF1, MRPL13, PDCD11, SNRPA1, SCFD1, SEC63, SNRPD1, SPATS2L, U2SURP, SRP72, SRRT, DARS1, LARS1, CCT7, TNPO1, SNRNP200, UMPS, TJP2

### Function

The module is most strongly associated with coordinated gene-expression machinery, especially ribonucleoprotein complexes, nuclear protein-containing complexes, RNA metabolism, and nucleocytoplasmic transport. These conclusions are supported by the globally corrected terms (GO:CC ribonucleoprotein complex; q_global = 0.00642) through (GO:BP macromolecule biosynthetic process; q_global = 0.0499), including ribonucleoprotein complex, nuclear protein-containing complex, gene expression, nucleocytoplasmic transport, RNA metabolic process, nucleic-acid metabolic process, and macromolecule biosynthetic process. The convergence of spliceosomal, nucleolar, nuclear-pore, translation-related, and RNA-surveillance genes indicates a broad post-transcriptional gene-expression program rather than a narrowly specialized metabolic pathway. The module also contains genes involved in cell junctions, vesicle traffic, mitochondrial organization, and amino-acid or nucleotide metabolism, suggesting that the RNA-centered signal is embedded in general cellular maintenance and epithelial-cell physiology.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a single secreted gene, and the module is largely composed of intracellular proteins located in the nucleus, nucleoplasm, nucleoli, cytosol, nuclear membrane, endoplasmic reticulum, Golgi, mitochondria, or cell junctions. Most genes have low tissue specificity, and most have low immune-cell specificity. Therefore, a blood-contamination explanation is not favored by the HPA summary, although a small immune-cell contribution cannot be excluded because a few genes are immune-cell enhanced, enriched, or group enriched. The shared liver–rectum signal is more consistent with broadly expressed cellular machinery, potentially contributed by common epithelial or other shared cell types, than with a plasma-protein module. HPA protein detection in both tissues is also widespread across the module, supporting biological presence in the sampled tissues but not proving coordinated regulation.

**GO/KEGG enrichment**: 8 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC ribonucleoprotein complex | 0.00642 | EIF3L, GAR1, MRPL13, PDCD11, SNRNP200, SNRPA1, SNRPD1, SRP72, SRRT, U2SURP, UPF1 |
| GO:CC nuclear protein-containing complex | 0.00981 | ACIN1, GAR1, NUP155, NUP160, NUP93, PCNA, PDCD11, SNRNP200, SNRPA1, SNRPD1, U2SURP, UPF1 |
| GO:BP gene expression | 0.0201 | ACIN1, AFDN, AP3D1, CASK, CCT7, CNOT1, CTNND1, DARS1, DNM1L, EIF3L, GAR1, GARS1, GTF2I, LARS1, MRPL13, NUP155, NUP160, NUP93, PCNA, PDCD11, SNRNP200, SNRPA1, SNRPD1, SRRT, U2SURP, UPF1 |
| KEGG Nucleocytoplasmic transport - Homo sapiens (human) | 0.0256 | ACIN1, NUP155, NUP160, NUP93, TNPO1, UPF1 |
| GO:BP RNA metabolic process | 0.0331 | ACIN1, AP3D1, CASK, CNOT1, CTNND1, DARS1, GAR1, GARS1, GTF2I, LARS1, NUP155, PCNA, PDCD11, SNRNP200, SNRPA1, SNRPD1, SRRT, U2SURP, UPF1 |
| GO:CC protein-containing complex | 0.0361 | ACIN1, AFDN, AP3D1, CACYBP, CCT7, CNOT1, COPB1, CTNND1, DARS1, DNM1L, EIF3L, GAR1, LARS1, MRPL13, NUP155, NUP160, NUP93, PCNA, PDCD11, PSMG1, SEC63, SNRNP200, SNRPA1, SNRPD1, SPATS2L, SRP72, SRRT, U2SURP, UPF1 |
| GO:BP nucleic acid metabolic process | 0.044 | ACIN1, AP3D1, CASK, CCT7, CNOT1, CTNND1, DARS1, GAR1, GARS1, GTF2I, LARS1, NUP155, PCNA, PDCD11, SNRNP200, SNRPA1, SNRPD1, SRRT, U2SURP, UPF1 |
| GO:BP macromolecule biosynthetic process | 0.0499 | ACIN1, AFDN, AP3D1, CASK, CCT7, CNOT1, CTNND1, DARS1, DNM1L, EIF3L, GAR1, GARS1, GTF2I, LARS1, MRPL13, NUP155, NUP160, NUP93, PCNA, PDCD11, SNRNP200, SNRPA1, SNRPD1, SRRT, U2SURP, UPF1 |

### STRING and hu.MAP

STRING provides direct or highly supported relationships within several coherent subgroups. The strongest known interaction cluster contains SNRNP200, SNRPA1, SNRPD1, and U2SURP, consistent with spliceosomal snRNP machinery. NUP155, NUP160, and NUP93 form a nuclear-pore subgroup, with TNPO1 providing a transport-related connection. DARS1, GARS1, and LARS1 are linked through aminoacyl-tRNA-synthetase relationships, while AFDN, CTNND1, and TJP2 form a cell-junction subgroup. Additional STRING links connect mitochondrial or nucleotide-related genes and protein-folding or proteasome-associated genes. These relationships support that the co-abundance module contains real biological neighborhoods rather than only unrelated correlated genes. hu.MAP independently supports the spliceosomal complex through (hu.MAP huMAP3_08980.1) and (hu.MAP huMAP3_06511.1), the nucleoporin-associated complexes through (hu.MAP huMAP3_07789.1), (hu.MAP huMAP3_09042.1), and (hu.MAP huMAP3_12581.1), the aminoacyl-tRNA-synthetase complexes through (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), the SRRT–ACIN1 RNA-processing complexes through (hu.MAP huMAP3_10564.1), (hu.MAP huMAP3_09621.1), (hu.MAP huMAP3_11073.1), and (hu.MAP huMAP3_09943.1), and additional mixed complexes through (hu.MAP huMAP3_14442.1) and (hu.MAP huMAP3_11232.1). Because many hu.MAP complexes contribute only a small subset of their members, the module appears to combine several known complexes and functional neighborhoods rather than represent one intact physical complex.

**STRING interactions (score >= 0.7)**: 23 of 741 gene pairs: AFDN–CTNND1 (0.998); AFDN–TJP2 (0.999); ALDH18A1–GMPS (0.909); CCT7–PSMG1 (0.922); CNOT1–SNRNP200 (0.748); COPB1–SCFD1 (0.729); DARS1–GARS1 (0.772); DARS1–LARS1 (0.996); GAR1–GMPS (0.823); GARS1–LARS1 (0.895); GMPS–UMPS (0.802); MRPL13–PDCD11 (0.935); MRPL13–PSMG1 (0.893); NUP155–NUP160 (0.994); NUP155–NUP93 (0.999); NUP160–NUP93 (0.991); NUP160–TNPO1 (0.718); SEC63–SNRNP200 (0.733); SNRNP200–SNRPA1 (0.999); SNRNP200–SNRPD1 (0.999); SNRPA1–SNRPD1 (0.999); SNRPA1–U2SURP (0.934); SNRPD1–U2SURP (0.744)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Metabolism of RNA (FDR = 0.00047, 14 genes); Process RNA metabolic process (FDR = 0.0101, 15 genes); RCTM Processing of Capped Intron-Containing Pre-mRNA (FDR = 0.0138, 9 genes); Process Gene expression (FDR = 0.0183, 18 genes); Process Nucleic acid metabolic process (FDR = 0.0183, 16 genes); Keyword Nucleus (FDR = 0.0238, 21 genes); Keyword Isopeptide bond (FDR = 0.0238, 15 genes); Keyword Ubl conjugation (FDR = 0.0454, 15 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (SNRNP200, SNRPA1, SNRPD1; 3/97); huMAP3_07789.1 (UMPS, NUP93; 2/7); huMAP3_02637.1 (DARS1, LARS1; 2/14); huMAP3_13688.1 (DARS1, LARS1; 2/14); huMAP3_09042.1 (UMPS, NUP93; 2/26); huMAP3_10564.1 (SRRT, ACIN1; 2/37); huMAP3_09621.1 (SRRT, ACIN1; 2/56); huMAP3_14442.1 (GARS1, GMPS; 2/57); huMAP3_12581.1 (NUP155, NUP160; 2/58); huMAP3_11073.1 (SRRT, ACIN1; 2/67); huMAP3_09943.1 (SRRT, ACIN1; 2/78); huMAP3_11232.1 (NUP160, TNPO1; 2/78); huMAP3_06511.1 (SNRPA1, SNRPD1; 2/79)

### Novelty

This module should not be claimed as a newly discovered molecular complex or as a wholly novel pathway. Its central components and several internal relationships are already established by STRING and hu.MAP, especially spliceosomal proteins, nucleoporins, aminoacyl-tRNA synthetases, and RNA-processing factors. The potentially novel aspect is the conserved co-abundance pattern across liver and rectum and the particular combination of RNA processing, nuclear transport, translation support, epithelial junction, trafficking, and cellular-maintenance genes. Absence of some genes from STRING or hu.MAP does not establish novelty, because those resources emphasize experimentally or computationally supported physical interactions and may not capture tissue-specific co-abundance. The appropriate conclusion is that the cross-tissue module is a potentially informative systems-level association built largely from known biology, requiring independent replication and comparison with existing tissue co-expression modules before it can be called a new finding.

**Hypothesis.** Hypothesis: the module reflects a shared epithelial-cell state in liver and rectum in which high demand for gene expression and protein production is coordinated with RNA processing, nuclear export and import, translation, secretory-pathway handling, and maintenance of cell–cell junctions. In this model, spliceosomal and RNA-surveillance components regulate transcript maturation, nucleoporins and TNPO1 control traffic across the nuclear envelope, aminoacyl-tRNA synthetases and translation factors support protein synthesis, and AFDN, CTNND1, and TJP2 maintain epithelial architecture. The observed co-abundance may therefore represent coordinated cellular homeostasis in common tissue-resident cell types rather than direct physical interaction among every module member. This remains a hypothesis because co-abundance does not establish causality, directionality, or a single shared cell type.

### Important genes

#### SNRNP200

- **Related proteins** (co-abundance neighbors): U2SURP (0.90), TJP2 (0.89), NUP160 (0.88), CNOT1 (0.88), GAR1 (0.88), SEC63 (0.87), AP3D1 (0.86), ALDH18A1 (0.85), SRP72 (0.85), GTF2I (0.85), CTNND1 (0.84), CCT7 (0.82), LARS1 (0.82), UPF1 (0.82), ACIN1 (0.82), COPB1 (0.81), SNRPD1 (0.80); STRING partners: CNOT1 (0.748), SEC63 (0.733), SNRPA1 (0.999), SNRPD1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is among the more central genes in the module and connects to U2SURP, CNOT1, NUP160, GAR1, SEC63, AP3D1, and other module members. It is a U5 snRNP-specific RNA helicase and appears in every primary global term (GO:CC ribonucleoprotein complex; q_global = 0.00642) through (GO:BP macromolecule biosynthetic process; q_global = 0.0499) as well as every supplementary STRING term (STRING RCTM Metabolism of RNA; within-query FDR = 0.00047) through (STRING Keyword Ubl conjugation; within-query FDR = 0.0454). Its direct STRING links to SNRPA1 and SNRPD1 and its membership in hu.MAP complex (hu.MAP huMAP3_08980.1) provide convergent evidence for a spliceosomal core. It has substantial literature and established disease associations involving retinal degeneration.
- **Conclusion**: Established evidence supports SNRNP200 as a central spliceosomal and RNA-processing component of the module. Its network position makes it a plausible integrator of the RNA-processing signal, but the data do not show that SNRNP200 drives the cross-tissue co-abundance pattern or that it specifically explains liver–rectum conservation.

#### SNRPA1

- **Related proteins** (co-abundance neighbors): ALDH18A1 (0.85), UMPS (0.82), NUP155 (0.81), SEC63 (0.80); STRING partners: SNRNP200 (0.999), SNRPD1 (0.999), U2SURP (0.934)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, rectum
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_06511.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein polypeptide A'. Enables RNA binding activity. Involved in mRNA splicing, via spliceosome and spermatogenesis. Located in nuclear speck. Part of U2-type catalytic step 2 spliceosome and U2-type precatalytic spliceosome. Implicated in connective tissue disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.538); dengue disease (0.370); phosphorus metabolism disease (0.196); hypotensive disorder (0.196); cancer (0.087)
- **Europe PMC papers**: 520
- **Why important**: SNRPA1 is a core U2-type spliceosomal factor with strong module connectivity to SNRNP200, SNRPD1, U2SURP, and other genes. It is represented in (GO:CC ribonucleoprotein complex; q_global = 0.00642) through (GO:BP macromolecule biosynthetic process; q_global = 0.0499) and (STRING RCTM Metabolism of RNA; within-query FDR = 0.00047) through (STRING Keyword Ubl conjugation; within-query FDR = 0.0454), has very strong STRING relationships with SNRNP200 and SNRPD1, and occurs in hu.MAP complexes (hu.MAP huMAP3_08980.1) and (hu.MAP huMAP3_06511.1). Its established functions include snRNP assembly, pre-spliceosome assembly, and mRNA splicing, while its disease associations and literature support make it a well-characterized representative of the module's primary functional signal.
- **Conclusion**: Established evidence identifies SNRPA1 as a core spliceosomal marker and a strong representative of the module's RNA-processing axis. A specific tissue-selective splicing program is a plausible interpretation but is not demonstrated by the supplied data.

#### NUP155

- **Related proteins** (co-abundance neighbors): SRP72 (0.87), SRRT (0.86), DNM1L (0.85), CTNND1 (0.81), SNRPA1 (0.81), ALDH18A1 (0.81), GMPS (0.80), DARS1 (0.80), EIF3L (0.80); STRING partners: NUP160 (0.994), NUP93 (0.999)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 155. Nucleoporins are proteins that play an important role in the assembly and functioning of the nuclear pore complex (NPC) which regulates the movement of macromolecules across the nuclear envelope (NE). The protein encoded by this gene plays a role in the fusion of NE vesicles and formation of the double membrane NE. The protein may also be involved in cardiac physiology and may be associated with t…
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); atrial fibrillation (0.470); familial atrial fibrillation (0.390)
- **Europe PMC papers**: 944
- **Why important**: NUP155 is a highly connected nuclear-envelope component linked to NUP160 and NUP93 by STRING and represented in hu.MAP complex (hu.MAP huMAP3_12581.1). It occurs in the primary nuclear-complex, gene-expression, nucleocytoplasmic-transport, RNA-metabolism, and biosynthetic terms (GO:CC nuclear protein-containing complex; q_global = 0.00981) through (GO:BP macromolecule biosynthetic process; q_global = 0.0499), and in all listed supplementary STRING terms. Its established functions include nuclear-pore organization, RNA export, and protein import. It also has extensive disease relevance, including atrial-fibrillation associations.
- **Conclusion**: Established evidence supports NUP155 as the principal nuclear-pore component connecting RNA processing with nucleocytoplasmic transport in this module. It provides a mechanistic bridge between the spliceosomal subgroup and broader gene-expression machinery, but the module does not establish altered nuclear transport in either tissue.

#### UPF1

- **Related proteins** (co-abundance neighbors): ACIN1 (0.86), U2SURP (0.85), AP3D1 (0.84), SNRNP200 (0.82), ALDH18A1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UPF1 RNA helicase and ATPase. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons.…
- **Diseases (Open Targets)**: Intellectual disability (0.437); Global developmental delay (0.426); High anterior hairline (0.425); Frontal bossing (0.425); Hypertelorism (0.425)
- **Europe PMC papers**: 4252
- **Why important**: UPF1 is included in all primary global terms (GO:CC ribonucleoprotein complex; q_global = 0.00642) through (GO:BP macromolecule biosynthetic process; q_global = 0.0499) and most supplementary RNA and gene-expression terms. It connects to ACIN1, U2SURP, AP3D1, SNRNP200, and ALDH18A1 in the module network. Its established function in mRNA export and nonsense-mediated decay links transcript processing to quality control after export. It has a substantial literature and documented associations with intellectual disability and developmental phenotypes.
- **Conclusion**: Established evidence supports UPF1 as an RNA-surveillance and export factor that broadens the module beyond spliceosome assembly. Its presence is consistent with coordinated transcript maturation and quality control, but the data do not demonstrate altered nonsense-mediated decay or a causal role in tissue-specific physiology.

#### CTNND1

- **Related proteins** (co-abundance neighbors): SRP72 (0.86), U2SURP (0.86), GTF2I (0.85), AP3D1 (0.85), SNRNP200 (0.84), CNOT1 (0.84), GAR1 (0.83), ACIN1 (0.83), NUP160 (0.83), ALDH18A1 (0.82), TJP2 (0.82), NUP155 (0.81), SEC63 (0.80); STRING partners: AFDN (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin delta 1. This gene encodes a member of the Armadillo protein family, which function in adhesion between cells and signal transduction. Multiple translation initiation codons and alternative splicing result in many different isoforms being translated. Not all of the full-length natures of the described transcript variants have been determined. Read-through transcription also exists between this gene and the…
- **Diseases (Open Targets)**: blepharocheilodontic syndrome (0.724); listeriosis (0.526); cleft lip (0.510); hereditary disease (0.415); exudative vitreoretinopathy (0.376)
- **Europe PMC papers**: 3021
- **Why important**: CTNND1 is one of the more connected module genes and links the RNA-centered neighborhood with AFDN, TJP2, CNOT1, GTF2I, AP3D1, and several spliceosome-associated genes. It is present in the global gene-expression, RNA-metabolism, nucleic-acid, and biosynthetic terms (GO:BP gene expression; q_global = 0.0201) and (GO:BP RNA metabolic process; q_global = 0.0331) through (GO:BP macromolecule biosynthetic process; q_global = 0.0499). Its established role in cadherin-mediated cell adhesion and signal transduction, its plasma-membrane localization, its detection in both liver and rectum, and its disease literature make it an important tissue-architecture representative.
- **Conclusion**: Established evidence supports CTNND1 as a cell-adhesion and signaling component that may connect epithelial architecture to the module's intracellular gene-expression program. The proposed bridge between junctional state and RNA-processing abundance is a hypothesis, not a demonstrated causal mechanism.

#### TJP2

- **Related proteins** (co-abundance neighbors): AP3D1 (0.90), SNRNP200 (0.89), SEC63 (0.86), SRP72 (0.86), SRRT (0.84), LARS1 (0.83), CTNND1 (0.82), ALDH18A1 (0.81), EIF3L (0.80); STRING partners: AFDN (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cell Junctions; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tight junction protein 2. This gene encodes a zonula occluden that is a member of the membrane-associated guanylate kinase homolog family. The encoded protein functions as a component of the tight junction barrier in epithelial and endothelial cells and is necessary for proper assembly of tight junctions. Mutations in this gene have been identified in patients with hypercholanemia, and genomic duplication of a 270 kb regio…
- **Diseases (Open Targets)**: cholestasis, progressive familial intrahepatic, 4 (0.800); hypercholanemia, familial 1 (0.647); autosomal dominant nonsyndromic hearing loss (0.558); progressive familial intrahepatic cholestasis type 2 (0.527); deafness (0.467)
- **Europe PMC papers**: 1748
- **Why important**: TJP2 is a cell-junction component detected in both tissues and is strongly connected in STRING to AFDN. Within the co-abundance network it links to AP3D1, SNRNP200, SEC63, SRP72, SRRT, LARS1, CTNND1, and ALDH18A1. Its established function is maintenance and assembly of tight-junction barriers, with disease associations involving cholestasis, hypercholanemia, and hearing loss. Although it is not present in the primary GO or KEGG terms, it provides important tissue-contextual evidence for an epithelial component.
- **Conclusion**: Established evidence supports TJP2 as an epithelial-barrier marker and a plausible context gene for the shared liver–rectum module. Its connection to RNA-processing genes is currently an association in this dataset; it should not be interpreted as proof that tight-junction regulation controls the RNA machinery.

## Module 3

**Tissue pair**: liver and rectum  
**Genes (37)**: ACLY, AP3B1, CLTC, DHX9, EIF3C, ERMP1, FDFT1, FUS, MACROH2A1, HSPH1, HSP90AA1, EIF4G1, IPO4, LBR, LMNB1, MATR3, MYBBP1A, MOGS, SNU13, PRKDC, RPL12, RSL1D1, SF3A1, SF3B3, IARS1, KARS1, MARS1, VARS1, CCT5, CCT3, TMEM11, TOMM40, TXLNA, EFTUD2, VDAC2, VIL1, XRCC6

### Function

The module is best interpreted as a conserved nuclear gene-expression and RNA-processing module, with linked support for translation, protein-RNA complex assembly, DNA metabolism, and macromolecule biosynthesis. The primary evidence is the coordinated enrichment for nucleic acid binding (GO:MF nucleic acid binding; q_global = 0.00012), RNA binding (GO:MF RNA binding; q_global = 0.00021), macromolecule biosynthetic process (GO:BP macromolecule biosynthetic process; q_global = 0.00432), gene expression (GO:BP gene expression; q_global = 0.00594), ribonucleoprotein complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.00817), protein-RNA complex assembly (GO:BP protein-RNA complex assembly; q_global = 0.04), and protein-RNA complex organization (GO:BP protein-RNA complex organization; q_global = 0.0491). The DNA-related terms (GO:BP positive regulation of DNA metabolic process; q_global = 0.0322) and (GO:BP regulation of DNA metabolic process; q_global = 0.0411) suggest coupling to genome maintenance rather than a purely translational program. The gene composition supports a broad information-processing program involving spliceosomal proteins, RNA helicases, translation factors, aminoacyl-tRNA synthetases, ribosomal proteins, chaperones, chromatin-associated proteins, and DNA-repair proteins. This is a coherent functional interpretation, although enrichment alone does not establish that every member acts in one physical complex.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary identifies only one secreted gene, while nearly all members are intracellular and most have low tissue specificity. Protein detection is broad in both liver and rectum, supporting a shared cellular program rather than a liver-specific or rectum-specific secretory signature. HPA also shows low immune-cell specificity for most genes, so the module is not best explained as a blood-cell module. Nevertheless, several members have enhanced or enriched signals in neutrophils, erythrocyte progenitors, lymphoid or bone-marrow tissue, and reproductive cell types. Those signals, together with the STRING tissue associations for lymphocytes, leukemia cells, and reproductive tissues (8 supplementary STRING terms; within-query FDR 0.0007–0.0012), indicate that cellular composition and proliferative state could contribute to the observed co-abundance. VIL1 provides a limited epithelial or intestinal component, but it is not sufficient to redefine the whole module.

**GO/KEGG enrichment**: 12 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleic acid binding | 0.00012 | CCT3, CCT5, CLTC, DHX9, EFTUD2, EIF3C, EIF4G1, FUS, HSP90AA1, IARS1, KARS1, LBR, LMNB1, MACROH2A1, MARS1, MATR3, MYBBP1A, PRKDC, RPL12, RSL1D1, SF3A1, SF3B3, SNU13, XRCC6 |
| GO:MF RNA binding | 0.00021 | CCT3, CCT5, CLTC, DHX9, EFTUD2, EIF3C, EIF4G1, FUS, HSP90AA1, IARS1, KARS1, LBR, MARS1, MATR3, MYBBP1A, PRKDC, RPL12, RSL1D1, SF3A1, SF3B3, SNU13, XRCC6 |
| GO:BP macromolecule biosynthetic process | 0.00432 | AP3B1, CCT3, CCT5, CLTC, DHX9, EFTUD2, EIF3C, EIF4G1, FUS, HSP90AA1, HSPH1, IARS1, KARS1, LBR, LMNB1, MACROH2A1, MARS1, MATR3, MOGS, MYBBP1A, PRKDC, RPL12, SF3A1, SF3B3, SNU13, VARS1, XRCC6 |
| GO:BP gene expression | 0.00594 | AP3B1, CCT3, CCT5, DHX9, EFTUD2, EIF3C, EIF4G1, FUS, HSP90AA1, HSPH1, IARS1, KARS1, LBR, LMNB1, MACROH2A1, MARS1, MATR3, MOGS, MYBBP1A, PRKDC, RPL12, SF3A1, SF3B3, SNU13, VARS1, XRCC6 |
| GO:BP ribonucleoprotein complex biogenesis | 0.00817 | DHX9, EIF3C, HSP90AA1, MYBBP1A, PRKDC, SF3A1, SF3B3, SNU13 |
| GO:BP positive regulation of macromolecule biosynthetic process | 0.0158 | AP3B1, CCT3, CCT5, DHX9, EIF3C, EIF4G1, FUS, HSP90AA1, HSPH1, KARS1, MACROH2A1, MARS1, MYBBP1A, PRKDC, SF3B3, XRCC6 |
| GO:CC intracellular protein-containing complex | 0.0294 | CCT3, CCT5, DHX9, EIF4G1, IARS1, KARS1, MARS1, PRKDC, SF3B3, XRCC6 |
| GO:BP positive regulation of DNA metabolic process | 0.0322 | CCT3, CCT5, DHX9, FUS, HSP90AA1, PRKDC |
| GO:BP positive regulation of biosynthetic process | 0.0351 | AP3B1, CCT3, CCT5, DHX9, EIF3C, EIF4G1, FUS, HSP90AA1, HSPH1, KARS1, MACROH2A1, MARS1, MYBBP1A, PRKDC, SF3B3, XRCC6 |
| GO:BP protein-RNA complex assembly | 0.04 | DHX9, EIF3C, HSP90AA1, PRKDC, SF3A1, SF3B3 |
| GO:BP regulation of DNA metabolic process | 0.0411 | CCT3, CCT5, DHX9, FUS, HSP90AA1, PRKDC, SF3B3 |
| GO:BP protein-RNA complex organization | 0.0491 | DHX9, EIF3C, HSP90AA1, PRKDC, SF3A1, SF3B3 |

### STRING and hu.MAP

STRING supports a structured network rather than an arbitrary gene set. Strong known relationships include the CCT3-CCT5 chaperonin pair, the DHX9-FUS-MATR3 RNA-associated group, the EFTUD2-SF3A1-SF3B3-SNU13 spliceosomal group, the EIF3C-EIF4G1 translation-initiation pair, the IARS1-KARS1-MARS1-VARS1 aminoacyl-tRNA synthetase group, the LBR-LMNB1 nuclear-envelope pair, and the PRKDC-XRCC6 DNA-repair pair. The HSP90AA1-HSPH1 chaperone relationship and the TOMM40-VDAC2 mitochondrial relationship add supporting submodules. hu.MAP independently recovers spliceosomal assemblies (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_04549.1), aminoacyl-tRNA synthetase assemblies (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), CCT assemblies (hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1), translation-initiation assemblies (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1), and a DNA-repair or membrane-associated assembly containing PRKDC and VDAC2 (hu.MAP huMAP3_09592.1). These results indicate that many edges reflect established molecular machinery. They do not prove that the entire co-abundance module is one biochemical complex; instead, the module appears to connect several interacting information-processing systems.

**STRING interactions (score >= 0.7)**: 37 of 666 gene pairs: AP3B1–CLTC (0.756); CCT3–CCT5 (0.999); CCT3–HSP90AA1 (0.767); CCT5–HSP90AA1 (0.868); DHX9–FUS (0.87); DHX9–MATR3 (0.786); DHX9–PRKDC (0.74); DHX9–SF3B3 (0.73); DHX9–XRCC6 (0.819); EFTUD2–HSP90AA1 (0.715); EFTUD2–KARS1 (0.704); EFTUD2–RPL12 (0.752); EFTUD2–SF3A1 (0.999); EFTUD2–SF3B3 (0.999); EFTUD2–SNU13 (0.998); EIF3C–EIF4G1 (0.99); FUS–MATR3 (0.91); HSP90AA1–HSPH1 (0.938); HSP90AA1–PRKDC (0.733); HSP90AA1–TOMM40 (0.722); IARS1–KARS1 (0.999); IARS1–MARS1 (0.999); IARS1–VARS1 (0.9); KARS1–MARS1 (0.999); KARS1–RPL12 (0.709); KARS1–VARS1 (0.978); LBR–LMNB1 (0.999); MACROH2A1–XRCC6 (0.769); MARS1–VARS1 (0.902); MYBBP1A–RSL1D1 (0.831); PRKDC–XRCC6 (0.999); RPL12–SNU13 (0.731); RSL1D1–SNU13 (0.893); SF3A1–SF3B3 (0.999); SF3A1–SNU13 (0.994); SF3B3–SNU13 (0.994); TOMM40–VDAC2 (0.873)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Brain (FDR = 3.97e-05, 35 genes); Function Nucleic acid binding (FDR = 8.13e-05, 24 genes); Function RNA binding (FDR = 8.13e-05, 22 genes); TISSUES Female reproductive gland (FDR = 0.0007, 25 genes); TISSUES Male reproductive system (FDR = 0.00081, 24 genes); TISSUES Female reproductive system (FDR = 0.00081, 35 genes); TISSUES Lymphocyte (FDR = 0.00081, 14 genes); TISSUES Leukemia cell (FDR = 0.00081, 16 genes); TISSUES Blood cancer cell (FDR = 0.0009, 17 genes); TISSUES Urogenital system (FDR = 0.0011, 36 genes); TISSUES Male reproductive gland (FDR = 0.0012, 23 genes); Process Positive regulation of macromolecule biosynthetic process (FDR = 0.0025, 15 genes); TISSUES Lymphoblast (FDR = 0.0027, 9 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0037, 15 genes); COMPARTMENTS Nucleoplasm (FDR = 0.006, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (SNU13, EFTUD2, SF3B3, SF3A1; 4/97); huMAP3_02637.1 (IARS1, MARS1, KARS1; 3/14); huMAP3_13688.1 (IARS1, MARS1, KARS1; 3/14); huMAP3_06511.1 (SNU13, SF3B3, SF3A1; 3/79); huMAP3_01951.1 (CCT5, CCT3; 2/8); huMAP3_13175.1 (EIF4G1, EIF3C; 2/20); huMAP3_07938.1 (CCT5, CCT3; 2/23); huMAP3_11246.1 (EIF4G1, EIF3C; 2/24); huMAP3_06559.1 (CCT5, CCT3; 2/25); huMAP3_09191.1 (CCT5, CCT3; 2/32); huMAP3_10656.1 (CCT5, CCT3; 2/36); huMAP3_04549.1 (SF3B3, SF3A1; 2/52); huMAP3_14584.1 (CCT5, CCT3; 2/61); huMAP3_09592.1 (VDAC2, PRKDC; 2/95)

### Novelty

The module should not be called a wholly new molecular complex. Many of its strongest relationships and subgroups are already represented in STRING and hu.MAP, and its dominant functions are established cellular processes. Its potentially novel aspect is the conserved co-abundance of these linked systems across liver and rectum, especially the coordinated connection of spliceosome, RNA surveillance or remodeling, translation, chaperoning, chromatin or nuclear-envelope biology, and DNA repair. Absence of hu.MAP or STRING support for some individual genes is not evidence of novelty, because those databases are incomplete and because co-abundance does not require direct physical interaction. A defensible conclusion is that this is a potentially informative tissue-shared regulatory signature, but novelty as a biological mechanism requires validation in independent cohorts, cell-composition adjustment, perturbation experiments, and comparison with previously reported cross-tissue expression modules.

**Hypothesis.** Hypothesis: the module represents a shared cellular maintenance state in which active RNA processing and translation are coordinated with proteostasis and genome surveillance. A possible mechanism is that DHX9, FUS, MATR3, EFTUD2, SF3A1, SF3B3, and SNU13 organize or remodel RNA-processing machinery; EIF3C, EIF4G1, RPL12, and the aminoacyl-tRNA synthetases support productive translation; CCT3, CCT5, HSP90AA1, and HSPH1 buffer the resulting proteotoxic load; and PRKDC, XRCC6, MACROH2A1, LBR, and LMNB1 couple this state to DNA repair, chromatin, and nuclear architecture. The conserved signal may therefore reflect a common requirement for transcriptional, post-transcriptional, and proteostatic homeostasis in cells present in both tissues. This remains a hypothesis: the data establish co-abundance and functional coherence, not causal direction or a single unified pathway.

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.93), PRKDC (0.93), SF3B3 (0.91), CLTC (0.89), EFTUD2 (0.89), IPO4 (0.89), SF3A1 (0.88), CCT3 (0.88), MATR3 (0.87), ERMP1 (0.87), RPL12 (0.85), LBR (0.84), CCT5 (0.83), IARS1 (0.83), VARS1 (0.83), XRCC6 (0.82), FUS (0.81), MARS1 (0.80), KARS1 (0.80), EIF3C (0.80); STRING partners: FUS (0.87), MATR3 (0.786), PRKDC (0.74), SF3B3 (0.73), XRCC6 (0.819)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is the strongest network hub in the supplied ranking and is present in every globally corrected GO term (12 globally significant GO/KEGG terms, q_global 0.00012–0.0491; see the table). It is an RNA helicase that unwinds RNA and DNA-RNA structures, participates in alternative splicing and transcriptional regulation, and connects the module to FUS, MATR3, PRKDC, SF3B3, and XRCC6 through STRING. Its disease associations include developmental and neurodegenerative disorders, and its literature base is substantial.
- **Conclusion**: Established evidence supports DHX9 as a central RNA and nucleic-acid-processing component of the module. Its network position and broad annotation make it a plausible coordinator of the RNA-processing and genome-maintenance signals. It is not established that DHX9 drives the cross-tissue co-abundance pattern; that causal role is a hypothesis.

#### PRKDC

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.93), DHX9 (0.93), MYBBP1A (0.92), SF3A1 (0.88), ERMP1 (0.88), IARS1 (0.87), IPO4 (0.87), EIF3C (0.86), XRCC6 (0.86), CLTC (0.84), VARS1 (0.84), MARS1 (0.84), CCT3 (0.83), SF3B3 (0.83), LBR (0.81), KARS1 (0.81), CCT5 (0.80); STRING partners: DHX9 (0.74), HSP90AA1 (0.733), XRCC6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, rectum
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: protein kinase, DNA-activated, catalytic subunit. This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to DNA-PKcs deficiency (0.752); neurodegenerative disease (0.548); severe combined immunodeficiency (0.470); combined immunodeficiency (0.464); ovarian neoplasm (0.210)
- **Europe PMC papers**: 12461
- **Why important**: PRKDC is a highly connected module member present in every globally corrected GO term (12 globally significant GO/KEGG terms, q_global 0.00012–0.0491; see the table). It encodes the catalytic subunit of DNA-dependent protein kinase and is linked to DNA double-strand-break repair, recombination, telomere maintenance, innate immune activation, and ribonucleoprotein biogenesis. It has a strong STRING relationship with XRCC6 and additional links to DHX9 and HSP90AA1, while hu.MAP places it in the membrane-associated complex (hu.MAP huMAP3_09592.1). It has extensive literature and clinically important immunodeficiency associations.
- **Conclusion**: Established evidence supports PRKDC as the module's principal DNA-repair and genome-surveillance anchor, while its participation in the broader RNA and biosynthetic signature is supported by enrichment and network context. The data do not demonstrate that DNA damage initiates the module or that PRKDC directly regulates all of its members.

#### SF3B3

- **Related proteins** (co-abundance neighbors): DHX9 (0.91), EFTUD2 (0.88), RSL1D1 (0.88), CCT3 (0.87), IPO4 (0.87), RPL12 (0.87), IARS1 (0.85), AP3B1 (0.85), HSPH1 (0.84), CLTC (0.83), FUS (0.83), PRKDC (0.83), CCT5 (0.82), MARS1 (0.81), VARS1 (0.81), EIF4G1 (0.81); STRING partners: DHX9 (0.73), EFTUD2 (0.999), SF3A1 (0.999), SNU13 (0.994)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Nucleoli rim; IHC detected in liver, rectum
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_06511.1, huMAP3_04549.1
- **Function (MyGene.info)**: splicing factor 3b subunit 3. This gene encodes subunit 3 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); dengue disease (0.370); cervical cancer (0.189); cervical carcinoma (0.189); prostate cancer (0.111)
- **Europe PMC papers**: 965
- **Why important**: SF3B3 is a high-ranking network member and is present in nearly all globally corrected terms, including RNA binding, ribonucleoprotein biogenesis, and protein-RNA organization (11 globally significant GO/KEGG terms, q_global 0.00012–0.0491; see the table). It is a core component of the SF3B spliceosomal machinery and has direct STRING links to EFTUD2, SF3A1, SNU13, and DHX9. Its membership in several hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_04549.1) provides orthogonal support. It also has disease associations involving neurodegeneration and cancer.
- **Conclusion**: Established evidence identifies SF3B3 as a central spliceosomal component and one of the clearest physical-complex anchors in the module. It supports the interpretation that RNA splicing is a real component of the shared signal. The data do not establish tissue-specific splice isoforms or a disease-specific splicing mechanism.

#### CCT3

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.91), EFTUD2 (0.88), DHX9 (0.88), SF3B3 (0.87), SF3A1 (0.87), SNU13 (0.85), RPL12 (0.84), MYBBP1A (0.84), ACLY (0.83), PRKDC (0.83), FUS (0.82), CCT5 (0.81), IPO4 (0.81), MATR3 (0.80); STRING partners: CCT5 (0.999), HSP90AA1 (0.767)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver, rectum
- **hu.MAP 3.0**: huMAP3_01951.1, huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a highly connected member present in most globally corrected terms, including nucleic acid binding, biosynthetic regulation, intracellular complexes, and DNA-metabolism regulation (9 globally significant GO/KEGG terms, q_global 0.00012–0.0411; see the table). It is a subunit of the CCT chaperonin that folds proteins such as actin and tubulin. Its near-maximal STRING relationship with CCT5 and multiple hu.MAP CCT-related complexes (hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) establish a well-supported proteostasis component. It also has substantial literature and associations with neurodevelopmental and neurodegenerative conditions.
- **Conclusion**: Established evidence supports CCT3 as the proteostasis and protein-folding anchor that links the module's biosynthetic activity to management of newly synthesized proteins. Its co-abundance may reflect general cellular workload rather than a specialized liver-rectum mechanism.

#### FUS

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.86), RPL12 (0.84), SF3B3 (0.83), LBR (0.82), CCT3 (0.82), HSPH1 (0.82), DHX9 (0.81), EIF4G1 (0.81), TOMM40 (0.80), AP3B1 (0.80); STRING partners: DHX9 (0.87), MATR3 (0.91)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FUS RNA binding protein. This gene encodes a multifunctional protein component of the heterogeneous nuclear ribonucleoprotein (hnRNP) complex. The hnRNP complex is involved in pre-mRNA splicing and the export of fully processed mRNA to the cytoplasm. This protein belongs to the FET family of RNA-binding proteins which have been implicated in cellular processes that include regulation of gene expression, maintenance of gen…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.710); sporadic amyotrophic lateral sclerosis (0.683); frontotemporal dementia with motor neuron disease (0.667); essential tremor (0.557); juvenile amyotrophic lateral sclerosis (0.527)
- **Europe PMC papers**: 19869
- **Why important**: FUS is a central RNA-binding protein with links to DHX9 and MATR3 in STRING and connections across the module to spliceosomal, translational, chaperone, and nuclear proteins. It appears in the primary terms for nucleic acid binding, RNA binding, gene expression, positive biosynthetic regulation, DNA-metabolism regulation, and protein-RNA organization (8 globally significant GO/KEGG terms, q_global 0.00012–0.0491; see the table). FUS participates in pre-mRNA splicing, mRNA export, gene regulation, and genome integrity, and it has a large literature base with strong amyotrophic lateral sclerosis and frontotemporal dementia associations.
- **Conclusion**: Established evidence supports FUS as an integrative RNA-processing and nuclear gene-regulation component. Its presence strengthens the interpretation of a coordinated RNA and genome-maintenance program. Disease links do not imply that this module is pathological or that FUS dysfunction explains the tissue association.

## Module 4

**Tissue pair**: liver and rectum  
**Genes (7)**: ACSL3, CSTF3, NDUFAF4, PFDN6, PSMD13, TBL2, TPD52L2

### Function

This is a heterogeneous intracellular co-abundance module rather than a module with a demonstrated single pathway. Its genes span pre-mRNA three-prime-end processing through CSTF3, protein folding and complex assembly through PFDN6, proteasome-associated protein turnover through PSMD13, mitochondrial complex I assembly through NDUFAF4, long-chain fatty-acyl-CoA metabolism through ACSL3, and stress, vesicle, or proliferation-related biology through TBL2 and TPD52L2. No GO or KEGG term passed global correction, and there are no supplementary STRING enrichment terms. The most defensible interpretation is coordinated variation in fundamental RNA-processing, proteostasis, lipid, mitochondrial, and cellular-maintenance programs, rather than a proven unified biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of its genes is annotated as secreted. All genes have low blood-cell specificity, so the module is not evidently a blood-cell signature. Most genes have low tissue specificity, while several show reproductive or other cell-type-enhanced patterns, including oocytes, spermatocyte or spermatid populations, and selected epithelial or neural cell types. Two genes are tissue-enhanced in testis or parathyroid gland. Protein detection is generally compatible with presence in liver and rectum, although detection is not uniform across the two tissues. These findings favor a broadly intracellular module that may reflect shared cellular composition or a common cell state in the sampled tissues, rather than a liver-rectum-specific secreted program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The co-abundance network contains a connected chain-like structure centered on CSTF3, with additional links through PFDN6 and PSMD13 toward NDUFAF4. However, none of the possible gene pairs has a high-confidence STRING interaction in the supplied evidence, and no STRING functional-enrichment term is available. No hu.MAP complex contains at least two module members. Thus, the module edges are observations of coordinated abundance, not established physical interactions or membership in a known multiprotein complex. The annotations suggest several plausible cellular processes, but the network does not independently validate a single molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The conserved liver-rectum co-abundance pattern may represent a new systems-level association, because the supplied network is not recovered as a high-confidence STRING interaction network or as a shared hu.MAP complex. Nevertheless, absence from STRING or hu.MAP does not establish biological novelty: co-abundance can arise from regulation, cell composition, indirect coupling, or technical and sampling effects, and known annotations exist for each gene individually. The appropriate conclusion is that the cross-tissue co-abundance configuration is potentially novel and currently unvalidated, not that the underlying gene functions or relationships are newly discovered.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular resource-management state present in liver and rectum, in which RNA maturation, chaperone-assisted folding, proteasome activity, mitochondrial respiratory-chain assembly, and lipid activation vary together. CSTF3 may mark the central abundance axis, while proteostasis and mitochondrial genes may respond to cellular protein and energetic demand; ACSL3 and TPD52L2 could connect this state to lipid handling and vesicular or proliferative biology. The cell-type-enhanced HPA patterns also raise the alternative hypothesis that shared or variable cell populations generate part of the signal. This hypothesis requires validation with independent cohorts, cell-composition adjustment, and targeted measurements of transcript processing, proteasome activity, mitochondrial function, and lipid metabolism.

### Important genes

#### CSTF3

- **Related proteins** (co-abundance neighbors): TBL2 (0.84), ACSL3 (0.83), TPD52L2 (0.83), PFDN6 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cleavage stimulation factor subunit 3. The protein encoded by this gene is one of three (including CSTF1 and CSTF2) cleavage stimulation factors that combine to form the cleavage stimulation factor complex (CSTF). This complex is involved in the polyadenylation and 3' end cleavage of pre-mRNAs. The encoded protein functions as a homodimer and interacts directly with both CSTF1 and CSTF2 in the CSTF complex. Alternative splicing results…
- **Diseases (Open Targets)**: dengue disease (0.370); Hydrocephalus (0.192); retinitis pigmentosa (0.085); early-onset non-syndromic cataract (0.084); early-onset zonular cataract (0.080)
- **Europe PMC papers**: 477
- **Why important**: CSTF3 is the most connected node in the co-abundance subgraph and therefore the strongest network anchor. Its established function in the cleavage stimulation factor complex directly links it to pre-mRNA three-prime-end cleavage and polyadenylation. It is detected in both liver and rectum, has low tissue specificity, and has substantial literature coverage. Its disease associations in the supplied evidence include dengue disease, hydrocephalus, and inherited eye disorders.
- **Conclusion**: Established evidence supports CSTF3 as an RNA-processing gene and the principal network anchor. It is reasonable to use CSTF3 as a marker of the module, but there is no evidence that it physically binds the other module members or causally organizes their co-abundance. Its role as the driver of the cross-tissue module remains a hypothesis.

#### ACSL3

- **Related proteins** (co-abundance neighbors): CSTF3 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 3. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme is highly expressed…
- **Diseases (Open Targets)**: prostate adenocarcinoma (0.370); acute myeloid leukemia (0.313); neurodegenerative disease (0.300); ovarian dysfunction (0.253); Abnormality of the skeletal system (0.215)
- **Europe PMC papers**: 2930
- **Why important**: ACSL3 links the module to long-chain fatty-acid activation, lipid biosynthesis, fatty-acid degradation, and very-low-density-lipoprotein particle assembly. It is connected directly to CSTF3, is detected in both tissues, and has the largest literature presence among the listed genes. The supplied disease and trait associations include prostate adenocarcinoma, acute myeloid leukemia, neurodegenerative disease, and ovarian dysfunction.
- **Conclusion**: Established evidence supports ACSL3 as a lipid-metabolism enzyme with broad disease relevance. Its membership suggests that lipid handling may be part of the cellular state represented by the module, but the data do not establish that ACSL3 is functionally coupled to CSTF3 or that lipid metabolism explains the entire module.

#### PSMD13

- **Related proteins** (co-abundance neighbors): PFDN6 (0.81), NDUFAF4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 is positioned between PFDN6 and NDUFAF4 in the co-abundance subgraph, providing a bridge between protein-folding and mitochondrial-associated module components. It is a non-ATPase subunit of the proteasome regulatory machinery and is annotated for ubiquitin-dependent protein catabolism, oxidative-stress response, and type-one-interferon response. It has broad disease associations including plasma-cell myeloma, mantle-cell lymphoma, neurodegenerative disease, neoplasm, and HIV infection.
- **Conclusion**: Established evidence supports PSMD13 as a proteasome-associated component involved in regulated protein turnover and stress-related biology. Its network position makes it a plausible indicator of proteostasis demand, but there is no STRING or hu.MAP evidence here for a physical complex with the neighboring module genes.

#### NDUFAF4

- **Related proteins** (co-abundance neighbors): PSMD13 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase complex assembly factor 4. NADH:ubiquinone oxidoreductase (complex I) catalyzes the transfer of electrons from NADH to ubiquinone (coenzyme Q) in the first step of the mitochondrial respiratory chain, resulting in the translocation of protons across the inner mitochondrial membrane. This gene encodes a complex I assembly factor. Mutations in this gene are a cause of mitochondrial complex I deficiency. [provided by RefSeq, O…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.714); type 2 diabetes mellitus (0.607); mitochondrial disease (0.597); diabetes mellitus (0.578); mitochondrial complex I deficiency, nuclear type 15 (0.568)
- **Europe PMC papers**: 378
- **Why important**: NDUFAF4 connects to PSMD13 and represents the mitochondrial arm of the module. It is a complex I assembly factor, and mutations are associated with mitochondrial complex I deficiency. It is detected in both liver and rectum and has supplied disease associations involving mitochondrial complex I deficiency, mitochondrial disease, and diabetes mellitus.
- **Conclusion**: Established evidence supports NDUFAF4 as a mitochondrial respiratory-chain assembly factor and a disease-relevant gene. Its presence supports an energetic or mitochondrial-maintenance component in the module, but the co-abundance data do not demonstrate that mitochondrial complex I assembly is the module's primary function.

#### PFDN6

- **Related proteins** (co-abundance neighbors): CSTF3 (0.82), PSMD13 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prefoldin subunit 6. PFDN6 is a subunit of the heteromeric prefoldin complex that chaperones nascent actin (see MIM 102560) and alpha- and beta-tubulin (see MIM 602529 and MIM 191130, respectively) chains pending their transfer to the cytosolic chaperonin containing TCP1 (MIM 186980) (CCT) complex (Hansen et al., 1999 [PubMed 10209023]).[supplied by OMIM, Jul 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.472); colorectal carcinoma (0.074); neoplasm (0.056); hemoglobin D disease (0.046); dehydrated hereditary stomatocytosis (0.043)
- **Europe PMC papers**: 230
- **Why important**: PFDN6 links CSTF3 to PSMD13 and is annotated as a prefoldin subunit that assists folding of nascent actin and tubulin before transfer to the cytosolic chaperonin system. It has cell-type-enhanced expression in reproductive cell populations, low tissue specificity, and a disease association with neurodegenerative disease and colorectal carcinoma among the supplied evidence.
- **Conclusion**: Established evidence supports PFDN6 as a protein-folding and cytoskeletal-chaperoning component. Its bridging position makes it a plausible proteostasis-related connector in the module, while the reproductive cell-type enrichment means that cell composition could contribute to its co-abundance. A direct mechanistic bridge between prefoldin activity and the other module processes is not established.

## Module 5

**Tissue pair**: liver and rectum  
**Genes (26)**: AIMP1, ALG2, CCAR1, DIAPH1, ADAR, MAN2A1, NSUN2, NUP62, NUP85, NUP98, P4HA1, PPP6R3, RBM39, RPA3, RPL9, SAE1, SDF2L1, CTTN, SRP54, TCEA1, TIMM44, TMOD3, TRIM25, XPO1, XRN2, ZW10

### Function

The strongest interpretation is a conserved nuclear RNA-handling and nucleocytoplasmic-transport module. The primary evidence is the global enrichment of nuclear export (GO:BP nuclear export; q_global = 0.00717), RNA export from the nucleus (GO:BP RNA export from nucleus; q_global = 0.0125), and mRNA transport (GO:BP mRNA transport; q_global = 0.0349). NSUN2, NUP62, NUP85, NUP98, and XPO1 form the central export-associated gene set, while ADAR links RNA editing to nuclear export (GO:BP nuclear export; q_global = 0.00717). The spindle annotation (GO:CC spindle; q_global = 0.0367) indicates a related cell-division or nuclear-architecture component involving CTTN, DIAPH1, NSUN2, NUP62, NUP85, and ZW10, but it is less specific than the RNA-export signal. STRING supplementary results support RNA metabolism and nuclear localization (STRING RCTM Metabolism of RNA; within-query FDR = 0.0093) (STRING COMPARTMENTS Nucleus; within-query FDR = 0.0185) (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0201), with additional cell-cycle and chromosome-segregation themes (4 supplementary STRING terms; within-query FDR 0.0313–0.0313). Overall, the module most plausibly reflects coordinated expression of nuclear pore, RNA processing, RNA export, and selected mitotic functions.

**Cell composition.** This does not appear to be primarily a plasma-protein or secreted-protein module. Most genes have low tissue specificity, and nearly all are detected at the protein level in rectum, with broad detection in liver. The HPA data show that only a minority are secreted, including AIMP1, whereas most proteins are intracellular or membrane-associated. The module is therefore more consistent with broadly expressed cellular machinery than with a liver-specific or rectum-specific secretome. HPA does, however, show cell-type enrichment for several genes, especially neutrophil-associated genes such as ADAR, XRN2, NUP98, CTTN, and DIAPH1, as well as platelet-associated DIAPH1 and related cell-type signals. This raises the possibility that part of the shared signal reflects common cell populations or variable blood content in tissue samples, although the aggregate HPA summary indicates low immune-cell specificity for most genes. AIMP1 is secreted to blood and could provide a circulating or vascular contribution, but it is not sufficient to characterize the whole module as plasma-derived.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP nuclear export | 0.00717 | ADAR, NSUN2, NUP62, NUP85, NUP98, XPO1 |
| GO:BP RNA export from nucleus | 0.0125 | NSUN2, NUP62, NUP85, NUP98, XPO1 |
| GO:BP mRNA transport | 0.0349 | NSUN2, NUP62, NUP85, NUP98, XPO1 |
| GO:CC spindle | 0.0367 | CTTN, DIAPH1, NSUN2, NUP62, NUP85, ZW10 |

### STRING and hu.MAP

Several relationships are already well established. STRING directly supports the nucleoporin core through NUP62-NUP85, NUP62-NUP98, NUP85-NUP98, and links involving XPO1. The CCAR1-RBM39 relationship and the RPL9-SRP54 relationship are also supported. These interactions mean that the module is not merely a collection of genes with correlated abundance: part of it recapitulates known nuclear-pore and RNA-related machinery. hu.MAP independently places NUP62, NUP98, and NUP85 together in a large nuclear-pore complex (hu.MAP huMAP3_12581.1), with additional complexes containing NUP62 and NUP98 (hu.MAP huMAP3_05948.1) (hu.MAP huMAP3_03647.1) (hu.MAP huMAP3_06369.1) (hu.MAP huMAP3_10000.1). ADAR and NSUN2 co-occur in a hu.MAP complex (hu.MAP huMAP3_12301.1), and ZW10 with NUP85 appears in another complex (hu.MAP huMAP3_11232.1). The network's strongest known relationships are therefore concentrated in the nucleoporin core, while many peripheral module edges lack direct STRING or hu.MAP support and may represent co-abundance, indirect regulation, shared cellular state, or tissue-composition effects.

**STRING interactions (score >= 0.7)**: 7 of 325 gene pairs: CCAR1–RBM39 (0.875); NUP62–NUP85 (0.995); NUP62–NUP98 (0.998); NUP62–XPO1 (0.869); NUP85–NUP98 (0.999); NUP98–XPO1 (0.968); RPL9–SRP54 (0.98)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Metabolism of RNA (FDR = 0.0093, 10 genes); COMPARTMENTS Nucleus (FDR = 0.0185, 18 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0201, 11 genes); RCTM Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal (FDR = 0.0313, 4 genes); RCTM Late Phase of HIV Life Cycle (FDR = 0.0313, 5 genes); RCTM Cell Cycle (FDR = 0.0313, 7 genes); RCTM Rev-mediated nuclear export of HIV RNA (FDR = 0.0313, 4 genes); RCTM Influenza Infection (FDR = 0.0313, 5 genes); RCTM NEP/NS2 Interacts with the Cellular Export Machinery (FDR = 0.0313, 4 genes); RCTM RHO GTPase Effectors (FDR = 0.0313, 6 genes); RCTM Resolution of Sister Chromatid Cohesion (FDR = 0.0313, 4 genes); RCTM SUMOylation (FDR = 0.0313, 4 genes); RCTM Regulation of HSF1-mediated heat shock response (FDR = 0.0313, 4 genes); RCTM RHO GTPases Activate Formins (FDR = 0.0313, 5 genes); RCTM Cell Cycle Checkpoints (FDR = 0.0313, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12581.1 (NUP62, NUP98, NUP85; 3/58); huMAP3_05948.1 (NUP62, NUP98; 2/5); huMAP3_03647.1 (NUP62, NUP98; 2/6); huMAP3_06369.1 (NUP62, NUP98; 2/12); huMAP3_12301.1 (ADAR, NSUN2; 2/26); huMAP3_10000.1 (NUP62, NUP98; 2/44); huMAP3_11232.1 (ZW10, NUP85; 2/78)

### Novelty

The module should not be described as a newly discovered molecular complex. Its central interpretation is consistent with established nuclear-pore, exportin, RNA-processing, and mitotic biology, and several relationships are already present in STRING and hu.MAP. Nevertheless, the conserved co-abundance of this particular gene combination across liver and rectum may be a useful systems-level observation. Its possible novelty lies in the tissue-pair-specific co-abundance organization and in the connection of the established nuclear-export core with genes involved in RNA modification, cytoskeletal organization, endoplasmic-reticulum or Golgi biology, mitochondrial import, and extracellular signaling. That claim remains hypothesis-generating rather than a demonstration of a new pathway. Absence of an interaction in STRING or hu.MAP cannot establish novelty, especially because co-abundance edges may reflect regulation, cell composition, or context-dependent interactions.

**Hypothesis.** Hypothesis: this shared module represents a coordinated state in which active RNA production, processing, modification, and export are coupled to nuclear-pore function and cell-cycle or structural remodeling in liver and rectum. The NUP62-NUP85-NUP98-XPO1 core could organize the export component, while NSUN2 and ADAR could influence the processing or modification state of exported RNA. XRN2 and RBM39 may connect transcriptional termination, RNA turnover, and splicing-related regulation. The spindle and cytoskeletal genes could reflect coupling of nuclear transport to proliferative or epithelial structural states. AIMP1, SDF2L1, TRIM25, and the cell-type-enriched genes may indicate additional contributions from stress, immune, vascular, or tissue-associated cells. This model should be tested with cell-resolved expression, tissue-composition adjustment, perturbation of nuclear export, and direct measurement of RNA-processing or transport phenotypes.

### Important genes

#### NUP62

- **Related proteins** (co-abundance neighbors): XPO1 (0.87), MAN2A1 (0.87), AIMP1 (0.86), NSUN2 (0.86), ZW10 (0.85); STRING partners: NUP85 (0.995), NUP98 (0.998), XPO1 (0.869)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in liver, rectum
- **hu.MAP 3.0**: huMAP3_12581.1, huMAP3_05948.1, huMAP3_03647.1, huMAP3_06369.1, huMAP3_10000.1
- **Function (MyGene.info)**: nucleoporin 62. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. The protein encoded by this gene is a member of the FG-repeat containing nucleoporins and is localized to the nuclear pore ce…
- **Diseases (Open Targets)**: infantile bilateral striatal necrosis (0.609); familial infantile bilateral striatal necrosis (0.590); HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.529)
- **Europe PMC papers**: 1582
- **Why important**: NUP62 is a central network gene and a member of the nuclear pore central plug. It participates in all primary nuclear-export terms (4 globally significant GO/KEGG terms, q_global 0.00717–0.0367; see the table), has direct STRING relationships with NUP85, NUP98, and XPO1, and occurs in several hu.MAP complexes (hu.MAP huMAP3_12581.1) (hu.MAP huMAP3_05948.1) (hu.MAP huMAP3_03647.1) (hu.MAP huMAP3_06369.1) (hu.MAP huMAP3_10000.1). Its annotation directly supports nucleocytoplasmic transport, RNA export, protein import, and mitotic functions. It is detected in both tissues and has substantial literature and disease annotation, making it a strong molecular anchor for the module.
- **Conclusion**: Established evidence supports NUP62 as a core structural and functional component of the module's nuclear-export machinery. It is plausible, but not established, that NUP62 abundance helps couple RNA export to the shared cellular state in liver and rectum.

#### NUP98

- **Related proteins** (co-abundance neighbors): CTTN (0.82), DIAPH1 (0.81); STRING partners: NUP62 (0.998), NUP85 (0.999), XPO1 (0.968)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12581.1, huMAP3_05948.1, huMAP3_03647.1, huMAP3_06369.1, huMAP3_10000.1
- **Function (MyGene.info)**: nucleoporin 98 and 96 precursor. Nuclear pore complexes (NPCs) regulate the transport of macromolecules between the nucleus and cytoplasm, and are composed of many polypeptide subunits, many of which belong to the nucleoporin family. This gene belongs to the nucleoporin gene family and encodes a 186 kDa precursor protein that undergoes autoproteolytic cleavage to generate a 98 kDa nucleoporin and 96 kDa nucleoporin. The 98 kDa nu…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); acute myeloid leukemia (0.399); lung carcinoma (0.376)
- **Europe PMC papers**: 4839
- **Why important**: NUP98 is a high-connectivity member of the known nucleoporin core. It participates in the primary nuclear-export, RNA-export, and mRNA-transport terms (GO:BP nuclear export; q_global = 0.00717) (GO:BP RNA export from nucleus; q_global = 0.0125) (GO:BP mRNA transport; q_global = 0.0349), has very strong STRING links to NUP62, NUP85, and XPO1, and appears across multiple hu.MAP nuclear-pore complexes (hu.MAP huMAP3_12581.1) (hu.MAP huMAP3_05948.1) (hu.MAP huMAP3_03647.1) (hu.MAP huMAP3_06369.1) (hu.MAP huMAP3_10000.1). Its functions include RNA export, nucleocytoplasmic transport, nuclear-pore organization, and nuclear periphery tethering. Its extensive literature and associations with viral disease and malignancy also make it biologically important.
- **Conclusion**: Established evidence identifies NUP98 as a core export and nuclear-pore component rather than a module-specific novel factor. Its inclusion supports a genuine transport-related interpretation, while its cell-state or disease relevance in these tissues remains to be tested.

#### NSUN2

- **Related proteins** (co-abundance neighbors): NUP62 (0.86), PPP6R3 (0.84), P4HA1 (0.84), XRN2 (0.83), ADAR (0.82), AIMP1 (0.82), TIMM44 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, rectum
- **hu.MAP 3.0**: huMAP3_12301.1
- **Function (MyGene.info)**: NOP2/Sun RNA methyltransferase 2. This gene encodes a methyltransferase that catalyzes the methylation of cytosine to 5-methylcytosine (m5C) at position 34 of intron-containing tRNA(Leu)(CAA) precursors. This modification is necessary to stabilize the anticodon-codon pairing and correctly translate the mRNA. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Mar…
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.694); hereditary disease (0.518); Intellectual disability (0.489); phenylketonuria (0.470); neurodegenerative disease (0.462)
- **Europe PMC papers**: 2458
- **Why important**: NSUN2 has the strongest network position in the module and appears in every primary term (4 globally significant GO/KEGG terms, q_global 0.00717–0.0367; see the table). Its established functions include RNA methylation, tRNA modification, rRNA processing, mRNA processing, and regulation of mRNA export. It connects the nucleoporin neighborhood to XRN2, ADAR, and other module genes, and it shares a hu.MAP complex with ADAR (hu.MAP huMAP3_12301.1). Its large literature base and disease associations support its importance beyond simple network centrality.
- **Conclusion**: Established evidence supports NSUN2 as the principal bridge between RNA modification or processing and nuclear export in this module. The hypothesis that NSUN2-dependent RNA modification drives the shared co-abundance pattern is not established by these data and requires functional testing.

#### XPO1

- **Related proteins** (co-abundance neighbors): NUP62 (0.87); STRING partners: NUP62 (0.869), NUP98 (0.968)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exportin 1. This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSe…
- **Diseases (Open Targets)**: plasma cell myeloma (0.642); B-cell chronic lymphocytic leukemia (0.626); diffuse large B-cell lymphoma (0.602); HIV infectious disease (0.561); neurodegenerative disease (0.522)
- **Europe PMC papers**: 5357
- **Why important**: XPO1 is the module's exportin and directly mediates transport of nuclear-export-signal-bearing cargo. It participates in the primary nuclear-export, RNA-export, and mRNA-transport terms (GO:BP nuclear export; q_global = 0.00717) (GO:BP RNA export from nucleus; q_global = 0.0125) (GO:BP mRNA transport; q_global = 0.0349), and has STRING support with NUP62 and NUP98. Its functions include export of ribosomal subunits, mRNA, and proteins, as well as regulation of cell-cycle and transcriptional regulators. Its broad literature and disease associations make it a particularly interpretable functional marker.
- **Conclusion**: Established evidence supports XPO1 as a key effector of the module's export interpretation. It is reasonable to hypothesize that altered XPO1 activity could affect the module's cellular phenotype, but co-abundance alone does not establish altered transport flux or causality.

#### ADAR

- **Related proteins** (co-abundance neighbors): AIMP1 (0.87), RBM39 (0.83), NSUN2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in liver, rectum
- **hu.MAP 3.0**: huMAP3_12301.1
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR provides a mechanistic link between RNA editing and nuclear RNA handling. It is included in the primary nuclear-export term (GO:BP nuclear export; q_global = 0.00717), connects in the module network to NSUN2, AIMP1, and RBM39, and shares a hu.MAP complex with NSUN2 (hu.MAP huMAP3_12301.1). Its established functions include adenosine-to-inosine RNA editing, RNA processing, nuclear transport-related biology, and antiviral response. It also has a particularly substantial literature base and strong disease associations involving inherited interferonopathy and dyschromatosis.
- **Conclusion**: Established evidence supports ADAR as an RNA-processing and editing component that complements the nuclear-export core. Its possible role in shaping the exported RNA species represented by the module is a hypothesis, not a conclusion from the co-abundance data.

## Module 6

**Tissue pair**: liver and rectum  
**Genes (41)**: PRMT5, ATP1B1, CD2AP, CNPY3, DDX46, DSP, DNAJB1, DPP3, TUFM, EML4, ERO1A, FLNB, GFPT1, COLGALT1, HYOU1, EIF4E, LRBA, MAL2, EEF1E1, NRDC, NTPCR, NUP107, NUP205, NUP210, PRPF4, PRRC1, PSMC2, GART, ATIC, RCC1, MRPS22, SEC24C, EPRS1, QARS1, RARS1, TECR, TM9SF2, TRAP1, TTLL12, UGGT1, ZC3HAV1

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established pathway assignment from enrichment. Its gene content instead points to a broadly expressed cellular infrastructure program spanning translation, RNA processing, nuclear transport, protein folding and quality control, vesicle trafficking, mitochondrial function, cytoskeletal organization, and nucleotide metabolism. The strongest coherent subnetworks are the aminoacyl-tRNA synthetase assembly represented by EEF1E1, EPRS1, QARS1 and RARS1 in (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), nuclear pore components involving NUP107 and NUP210 in (hu.MAP huMAP3_07492.1), (hu.MAP huMAP3_09710.1) and (hu.MAP huMAP3_12581.1), spliceosomal factors involving PRMT5, PRPF4 and DDX46 in (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1), and endoplasmic-reticulum quality-control components involving NTPCR and UGGT1 in (hu.MAP huMAP3_08545.1). These observations support a shared cellular maintenance and proteostasis program rather than a narrowly specialized liver or rectal pathway.

**Cell composition.** The module is not dominated by secreted or plasma proteins: only a minority are annotated as secreted, and most are intracellular or membrane-associated. HPA data show predominantly low tissue specificity and generally low immune-cell specificity, with protein detection in both liver and rectum for most genes. Therefore, the module is unlikely to be explained simply by a plasma-protein signal or a strong blood-cell admixture. Nevertheless, the HPA single-cell annotations are heterogeneous, with recurrent signals in esophageal epithelial cells, spermatogenic cells, trophoblasts, and selected myeloid or lymphoid populations. NUP210 is tissue enhanced in bone marrow and lymphoid tissue, while COLGALT1 has myeloid and macrophage-associated annotations and CD2AP is immune-cell enhanced. These features warrant checking cellular composition and epithelial or stromal admixture, but they do not establish that blood contamination drives the shared module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports several established relationships within the module. The aminoacyl-tRNA synthetase cluster is strongly connected through EEF1E1, EPRS1, QARS1 and RARS1; ATIC is linked to GART, GART to GFPT1, and NUP107 is linked to NUP205 and NUP210. Additional STRING-supported relationships connect DNAJB1 with HYOU1, TRAP1 and TTLL12, UGGT1 with HYOU1, MRPS22 with TUFM, and SEC24C with PRRC1. hu.MAP independently supports the aminoacyl-tRNA synthetase complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), spliceosomal assemblies (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1), the UGGT1-containing complex (hu.MAP huMAP3_08545.1), nuclear-pore assemblies (hu.MAP huMAP3_07492.1), (hu.MAP huMAP3_09710.1) and (hu.MAP huMAP3_12581.1), COPII-related complexes (hu.MAP huMAP3_11237.1) and (hu.MAP huMAP3_13535.1), and complexes containing ATIC with TRAP1 (hu.MAP huMAP3_14442.1). Thus, part of the network reflects known molecular complexes and physical or functional associations. The remaining co-abundance links are not automatically direct physical interactions; they may reflect shared abundance control, cellular state, or common cell-type composition.

**STRING interactions (score >= 0.7)**: 20 of 820 gene pairs: ATIC–EML4 (0.807); ATIC–GART (0.999); DNAJB1–HYOU1 (0.765); DNAJB1–TRAP1 (0.704); DNAJB1–TTLL12 (0.797); EEF1E1–EPRS1 (0.999); EEF1E1–QARS1 (0.996); EEF1E1–RARS1 (0.996); EPRS1–GART (0.752); EPRS1–QARS1 (0.999); EPRS1–RARS1 (0.999); GART–GFPT1 (0.897); HYOU1–UGGT1 (0.791); MRPS22–TUFM (0.988); NUP107–NUP205 (0.999); NUP107–NUP210 (0.988); NUP107–RCC1 (0.759); NUP205–NUP210 (0.991); PRRC1–SEC24C (0.728); QARS1–RARS1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EEF1E1, EPRS1, QARS1, RARS1; 4/14); huMAP3_13688.1 (EEF1E1, EPRS1, QARS1, RARS1; 4/14); huMAP3_06511.1 (PRMT5, PRPF4, DDX46; 3/79); huMAP3_08980.1 (PRMT5, PRPF4, DDX46; 3/97); huMAP3_08545.1 (NTPCR, UGGT1; 2/5); huMAP3_07492.1 (NUP107, NUP210; 2/10); huMAP3_11237.1 (SEC24C, PRRC1; 2/12); huMAP3_09710.1 (NUP107, NUP210; 2/13); huMAP3_13535.1 (SEC24C, PRRC1; 2/14); huMAP3_14442.1 (ATIC, TRAP1; 2/57); huMAP3_12581.1 (RCC1, NUP107; 2/58)

### Novelty

This module should not be claimed as a new molecular complex or a newly discovered pathway. Several of its densest relationships are already represented in STRING and hu.MAP, especially the aminoacyl-tRNA synthetase, spliceosome, nuclear-pore, ER-quality-control, COPII, and purine-metabolism components. A potentially novel aspect is the cross-tissue co-abundance pattern linking these established cellular systems in liver and rectum, but novelty cannot be established from the supplied evidence alone. The lack of a STRING interaction or hu.MAP assignment for some genes is not evidence of novelty. A defensible novelty claim would require comparison against prior liver and rectal co-abundance modules, independent cohorts, preservation testing, and preferably experimental validation.

**Hypothesis.** Hypothesis: the module represents a conserved cellular stress-adaptation and biosynthetic-capacity program shared by liver and rectal tissue. Coordinated abundance of aminoacyl-tRNA synthetases and translation-associated proteins may support protein production; DDX46, PRPF4 and PRMT5 may support RNA maturation; NUP107 and NUP210 may couple nucleocytoplasmic transport to gene-expression demands; UGGT1, DNAJB1 and HYOU1 may maintain ER and general proteostasis; and SEC24C, LRBA and related trafficking proteins may support intracellular cargo movement. Mitochondrial and nucleotide-biosynthetic components could provide energy and precursor support. This is a mechanistic model rather than a demonstrated causal pathway. It could arise from a conserved epithelial or parenchymal maintenance state, a shared stress response, or coordinated differences in cell composition.

### Important genes

#### LRBA

- **Related proteins** (co-abundance neighbors): CD2AP (0.90), PSMC2 (0.86), EML4 (0.85), DDX46 (0.85), SEC24C (0.84), EPRS1 (0.83), RARS1 (0.83), TRAP1 (0.83), RCC1 (0.83), ZC3HAV1 (0.82), TM9SF2 (0.81), UGGT1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LPS responsive beige-like anchor protein. The protein encoded by this gene is a member of the WDL-BEACH-WD (WBW) gene family. Its expression is induced in B cells and macrophages by bacterial lipopolysaccharides (LPS). The encoded protein associates with protein kinase A and may be involved in leading intracellular vesicles to activated receptor complexes, which aids in the secretion and/or membrane deposition of immune effector molecules…
- **Diseases (Open Targets)**: combined immunodeficiency due to LRBA deficiency (0.815); colobomatous microphthalmia-rhizomelic dysplasia syndrome (0.525); cholelithiasis (0.509); immunodeficiency disease (0.431); gallstones (0.419)
- **Europe PMC papers**: 1561
- **Why important**: LRBA is the strongest network hub in the supplied module and connects proteins from translation, trafficking, cytoskeletal, proteostasis and nuclear-related neighborhoods. It is detected in both tissues, is localized to the Golgi apparatus, and has established links to vesicle delivery and immune-effector secretion. Its disease associations include LRBA deficiency and common variable immunodeficiency, while its substantial literature volume makes it one of the best-characterized genes in the module.
- **Conclusion**: Established evidence supports LRBA as a central intracellular trafficking and immune-effector regulator with broad cellular relevance. Its hub position suggests that it may organize or report the shared module state, but the co-abundance data do not prove that LRBA regulates the other module genes.

#### RARS1

- **Related proteins** (co-abundance neighbors): HYOU1 (0.87), SEC24C (0.85), NUP210 (0.84), LRBA (0.83), QARS1 (0.83), EPRS1 (0.83), DDX46 (0.82), PSMC2 (0.82), MAL2 (0.82), PRPF4 (0.81), EML4 (0.81); STRING partners: EEF1E1 (0.996), EPRS1 (0.999), QARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver, rectum
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 is a prominent connector in the module and participates with EEF1E1, EPRS1 and QARS1 in the hu.MAP aminoacyl-tRNA synthetase complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), with corresponding STRING support. It is detected in both tissues and has established functions in arginyl-tRNA aminoacylation and translation. Its disease associations include hypomyelinating leukodystrophy and related hereditary disorders.
- **Conclusion**: Established evidence identifies RARS1 as a translation-supporting aminoacyl-tRNA synthetase embedded in a known multienzyme complex. Its module abundance likely reflects translational capacity or cellular maintenance, while any broader role in coordinating ER, nuclear-pore or trafficking processes remains a hypothesis.

#### DDX46

- **Related proteins** (co-abundance neighbors): EPRS1 (0.85), QARS1 (0.85), LRBA (0.85), FLNB (0.83), UGGT1 (0.83), EML4 (0.82), RARS1 (0.82), DSP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in liver, rectum
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: DEAD-box helicase 46. This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribu…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); dengue disease (0.370); Hypercholesterolemia (0.203); lung adenocarcinoma (0.074); osteosarcoma (0.053)
- **Europe PMC papers**: 592
- **Why important**: DDX46 occupies a connecting position between the translation-associated genes and proteins involved in ER quality control, epithelial structure and cytoskeletal organization. It is represented in the spliceosomal hu.MAP complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1), is localized to nuclear speckles, and has established roles in mRNA splicing and U2-type prespliceosome assembly. Its disease and infection associations and substantial literature support its biological relevance beyond a purely structural network role.
- **Conclusion**: Established evidence supports DDX46 as an RNA-helicase and spliceosome-associated factor. Its position suggests that RNA processing may be coordinated with the other cellular maintenance processes in the module, but the data do not establish DDX46 as the causal bridge.

#### NUP210

- **Related proteins** (co-abundance neighbors): EPRS1 (0.86), EIF4E (0.85), RARS1 (0.84), TTLL12 (0.83), EML4 (0.83), ATP1B1 (0.81), GFPT1 (0.81), GART (0.81); STRING partners: NUP107 (0.988), NUP205 (0.991)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver, rectum
- **hu.MAP 3.0**: huMAP3_07492.1, huMAP3_09710.1
- **Function (MyGene.info)**: nucleoporin 210. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. The protein encoded by this gene is a membrane-spanning glycoprotein that is a major component of the nuclear pore complex. M…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.536); COVID-19 (0.407); Histiocytosis (0.370)
- **Europe PMC papers**: 642
- **Why important**: NUP210 is a network connector linked to translation-associated genes, metabolic genes and other nucleoporins. It has strong STRING relationships with NUP107 and NUP205 and appears in the hu.MAP nuclear-pore complexes (hu.MAP huMAP3_07492.1) and (hu.MAP huMAP3_09710.1). It is detected in both tissues, is tissue enhanced in bone marrow and lymphoid tissue, and has established functions as a membrane-spanning nuclear-pore component involved in nucleocytoplasmic transport. Its disease associations include viral disease and histiocytosis.
- **Conclusion**: Established evidence supports NUP210 as part of the nuclear pore complex and as a plausible marker of transport and gene-expression capacity. The bone-marrow and lymphoid annotations suggest a possible cell-composition contribution, but the predominantly low immune-cell specificity of the module argues against treating that explanation as proven.

#### DNAJB1

- **Related proteins** (co-abundance neighbors): RCC1 (0.89), TM9SF2 (0.83), ATP1B1 (0.82), EPRS1 (0.81), UGGT1 (0.81); STRING partners: HYOU1 (0.765), TRAP1 (0.704), TTLL12 (0.797)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DnaJ heat shock protein family (Hsp40) member B1. This gene encodes a member of the DnaJ or Hsp40 (heat shock protein 40 kD) family of proteins. DNAJ family members are characterized by a highly conserved amino acid stretch called the 'J-domain' and function as one of the two major classes of molecular chaperones involved in a wide range of cellular events, such as protein folding and oligomeric protein complex assembly. The encoded protein is a …
- **Diseases (Open Targets)**: fibrolamellar hepatocellular carcinoma (0.377); hepatocellular adenoma (0.370); bile duct adenocarcinoma (0.370); hepatocellular carcinoma (0.290); hepatoblastoma (0.281)
- **Europe PMC papers**: 2924
- **Why important**: DNAJB1 connects several module neighborhoods, including HYOU1, TRAP1, TTLL12, ATP1B1, EPRS1 and UGGT1. STRING supports its relationships with HYOU1, TRAP1 and TTLL12, while its established function is as an HSP40-family molecular chaperone that promotes HSP70 ATPase activity, protein folding and responses to unfolded proteins. It is detected in both tissues and has a substantial disease and literature record, including associations with liver neoplasia.
- **Conclusion**: Established evidence supports DNAJB1 as a proteostasis and stress-response factor. Its position and links to ER and mitochondrial chaperones make it a strong candidate marker of the proposed cellular stress-adaptation state, but a causal role in generating the cross-tissue co-abundance pattern remains hypothetical.

## Module 7

**Tissue pair**: liver and rectum  
**Genes (6)**: COL6A1, COL6A2, COL6A3, LAMA5, LAMC1, HSPG2

### Function

This is a conserved extracellular-matrix and basement-membrane module. Every module gene occurs in the globally corrected ECM-receptor interaction and extracellular-matrix structural-constituent terms (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 3.11e-07) and (GO:MF extracellular matrix structural constituent; q_global = 2.81e-06), as well as the external encapsulating structure and extracellular-matrix cellular-component terms (GO:CC external encapsulating structure; q_global = 4.42e-06) and (GO:CC extracellular matrix; q_global = 4.42e-06). The module combines a collagen type VI trimer formed by COL6A1, COL6A2, and COL6A3 with laminin components LAMA5 and LAMC1 and the heparan-sulfate proteoglycan HSPG2. The collagen, laminin, and proteoglycan annotations are therefore concordant rather than driven by a single isolated gene. Focal adhesion, integrin signaling, and PI3K-Akt pathway enrichment (KEGG PI3K-Akt signaling pathway - Homo sapiens (human); q_global = 8.6e-05), (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.000351), and (KEGG Integrin signaling - Homo sapiens (human); q_global = 0.000351) supports a role in coupling the matrix to cell adhesion and signaling. The human papillomavirus and protein-digestion pathways (KEGG Human papillomavirus infection - Homo sapiens (human); q_global = 0.000351) and (KEGG Protein digestion and absorption - Homo sapiens (human); q_global = 0.0183) are best treated as pathway-map overlaps, not as evidence that the module is specifically viral or digestive.

**Cell composition.** All genes are annotated as secreted to the extracellular matrix, so this is not a housekeeping-like intracellular module and is not predominantly a plasma-protein module. HPA evidence strongly points toward stromal and mesenchymal sources: fibro-adipogenic progenitors, fibroblasts, hepatic stellate cells, and smooth-muscle-related cells recur across the annotations. Most genes are not detected in immune cells, with COL6A2 the main exception because it has group-enriched blood-cell annotation. Thus, a blood-cell explanation is not favored. The shared liver-rectum signal is more plausibly related to conserved stromal, vascular, smooth-muscle, or matrix-producing cell populations, although sample composition cannot be excluded. HPA protein detection is stronger in rectum than liver, while several genes are not detected by liver immunohistochemistry; this may reflect abundance, assay sensitivity, spatial sampling, or differences between transcript and protein measurements rather than absence of the module in liver.

**GO/KEGG enrichment**: 17 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG ECM-receptor interaction - Homo sapiens (human) | 3.11e-07 | COL6A1, COL6A2, COL6A3, HSPG2, LAMA5, LAMC1 |
| GO:MF extracellular matrix structural constituent | 2.81e-06 | COL6A1, COL6A2, COL6A3, HSPG2, LAMA5, LAMC1 |
| GO:CC external encapsulating structure | 4.42e-06 | COL6A1, COL6A2, COL6A3, HSPG2, LAMA5, LAMC1 |
| GO:CC extracellular matrix | 4.42e-06 | COL6A1, COL6A2, COL6A3, HSPG2, LAMA5, LAMC1 |
| KEGG PI3K-Akt signaling pathway - Homo sapiens (human) | 8.6e-05 | COL6A1, COL6A2, COL6A3, LAMA5, LAMC1 |
| KEGG Focal adhesion - Homo sapiens (human) | 0.000351 | COL6A1, COL6A2, COL6A3, LAMA5, LAMC1 |
| KEGG Integrin signaling - Homo sapiens (human) | 0.000351 | COL6A1, COL6A2, COL6A3, LAMA5, LAMC1 |
| KEGG Human papillomavirus infection - Homo sapiens (human) | 0.000351 | COL6A1, COL6A2, COL6A3, LAMA5, LAMC1 |
| GO:MF structural molecule activity | 0.00211 | COL6A1, COL6A2, COL6A3, HSPG2, LAMA5, LAMC1 |
| GO:CC basement membrane | 0.0025 | COL6A1, HSPG2, LAMA5, LAMC1 |
| GO:MF extracellular matrix structural constituent conferring tensile strength | 0.00782 | COL6A1, COL6A2, COL6A3 |
| KEGG Protein digestion and absorption - Homo sapiens (human) | 0.0183 | COL6A1, COL6A2, COL6A3 |
| GO:CC collagen trimer | 0.0229 | COL6A1, COL6A2, COL6A3 |
| GO:CC collagen type VI trimer | 0.0316 | COL6A1, COL6A3 |
| GO:CC collagen beaded filament | 0.0316 | COL6A1, COL6A3 |

### STRING and hu.MAP

STRING supports two coherent molecular subassemblies: the very strong COL6A1-COL6A2-COL6A3 collagen relationship and the strong LAMA5-LAMC1 laminin relationship. HSPG2 connects to the collagen group through STRING and to LAMC1 through an additional high-confidence relationship. STRING functional results independently reproduce ECM, collagen formation, cell adhesion, ECM-receptor interaction, PI3K-Akt, and focal-adhesion themes (STRING KEGG ECM-receptor interaction; within-query FDR = 1.37e-08) through (STRING PMID (2023) Deciphering the Kidney Matrisome: Identification and Quantification of Renal Extracellular Matrix Proteins in Healthy Mice.; within-query FDR = 2.66e-05). These relationships indicate that the network is biologically coherent and contains established physical or functional associations, rather than being an arbitrary co-abundance cluster. No hu.MAP complex contains multiple module members. That absence means the module is not represented there as a detected multi-member protein complex; it does not negate extracellular assembly, matrix organization, or pathway-level cooperation.

**STRING interactions (score >= 0.7)**: 5 of 15 gene pairs: COL6A1–COL6A2 (0.998); COL6A1–COL6A3 (0.994); COL6A2–COL6A3 (0.994); HSPG2–LAMC1 (0.82); LAMA5–LAMC1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG ECM-receptor interaction (FDR = 1.37e-08, 6 genes); RCTM ECM proteoglycans (FDR = 4.17e-08, 6 genes); RCTM Degradation of the extracellular matrix (FDR = 1e-07, 6 genes); Keyword Extracellular matrix (FDR = 2.88e-07, 6 genes); Function Extracellular matrix structural constituent (FDR = 3.04e-07, 6 genes); NetworkNeighborAL Collagen formation, and Protein complex involved in cell adhesion (FDR = 4.15e-07, 6 genes); COMPARTMENTS Collagen-containing extracellular matrix (FDR = 6.45e-07, 6 genes); COMPARTMENTS External encapsulating structure (FDR = 6.51e-07, 6 genes); KEGG PI3K-Akt signaling pathway (FDR = 3.48e-06, 5 genes); PMID (2021) The Extracellular Matrix Environment of Clear Cell Renal Cell Carcinoma Determines Cancer Associated Fibroblast Growth. (FDR = 8.71e-06, 6 genes); PMID (2019) Quantitative proteomic profiling of extracellular matrix and site-specific collagen post-translational modifications in an in vitro model of lung fibrosis. (FDR = 9.27e-06, 6 genes); WikiPathways PI3K-Akt signaling pathway (FDR = 1.15e-05, 5 genes); KEGG Focal adhesion (FDR = 1.28e-05, 5 genes); KEGG Human papillomavirus infection (FDR = 1.28e-05, 5 genes); PMID (2023) Deciphering the Kidney Matrisome: Identification and Quantification of Renal Extracellular Matrix Proteins in Healthy Mice. (FDR = 2.66e-05, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The biological components and many of their relationships are established, so the module should not be claimed as a newly discovered ECM pathway. The collagen type VI triad, laminin pair, and proteoglycan connections are supported by STRING and by established gene descriptions. A potentially novel aspect is the conserved co-abundance of this particular ECM combination across liver and rectum, especially because hu.MAP does not report a shared multi-member complex. However, the FACT SHEET does not provide an external comparison set, replication analysis, or prior tissue-pair module catalogue. Therefore the defensible conclusion is that the module may represent a new tissue-level co-abundance pattern, but novelty of the underlying biology is not established.

**Hypothesis.** Hypothesis: matrix-producing stromal cells in liver and rectum co-secrete a coordinated extracellular scaffold composed of collagen type VI, laminin, and perlecan. Collagen type VI could provide a beaded structural network, while laminin and HSPG2 could organize basement-membrane and interstitial-matrix interfaces and present or modulate cell-surface signals. Integrin-linked adhesion and PI3K-Akt enrichment suggests that variation in scaffold abundance may influence adhesion, migration, survival, or differentiation of neighboring cells. This is a mechanistic hypothesis derived from the annotations and network structure, not a demonstrated causal mechanism.

### Important genes

#### COL6A3

- **Related proteins** (co-abundance neighbors): COL6A2 (0.89), COL6A1 (0.88), LAMC1 (0.81), HSPG2 (0.81); STRING partners: COL6A1 (0.994), COL6A2 (0.994)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 3 chain. This gene encodes the alpha-3 chain, one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The alpha-3 chain of type VI collagen is much larger than the alpha-1 and -2 chains. This difference in size is largely due to an increase in the number of subdomains, similar to von Willebrand Factor type A domains, that are found in the amino termin…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy (0.766); dystonia 27 (0.764); Bethlem myopathy (0.758); Bethlem myopathy 1C (0.747); Bethlem myopathy 1A (0.718)
- **Europe PMC papers**: 5386
- **Why important**: COL6A3 is the most connected module member in the supplied network and links the collagen subgroup with LAMC1 and HSPG2. It encodes the alpha-three chain of collagen type VI, including von-Willebrand-factor-A-like domains, and appears across nearly all primary ECM, collagen, basement-membrane, and pathway terms (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 3.11e-07) through (GO:CC von-Willerbrand-factor-A-domain-rich collagen trimer; q_global = 0.0316). It has strong fibroblast, fibro-adipogenic-progenitor, and hepatic-stellate-cell relevance, extensive literature, and disease associations including Bethlem myopathy and Ullrich congenital muscular dystrophy.
- **Conclusion**: Established evidence supports COL6A3 as a central structural and connective-tissue component of the module. Its network position makes it a strong candidate for organizing cross-talk between collagen VI and laminin or proteoglycan compartments. A regulatory or signaling role beyond structural assembly remains a hypothesis.

#### COL6A1

- **Related proteins** (co-abundance neighbors): COL6A2 (0.96), HSPG2 (0.90), COL6A3 (0.88); STRING partners: COL6A2 (0.998), COL6A3 (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is a core member of the collagen type VI triad and is connected to COL6A2, COL6A3, and HSPG2. It contributes to every broad ECM structural annotation and to the collagen, basement-membrane, focal-adhesion, and integrin-related evidence (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 3.11e-07) through (GO:CC von-Willerbrand-factor-A-domain-rich collagen trimer; q_global = 0.0316). Its description identifies collagen VI as a major microfibrillar structural component, and it has extensive literature and strong disease associations with Bethlem myopathy and Ullrich congenital muscular dystrophy.
- **Conclusion**: Established evidence supports COL6A1 as an indispensable structural subunit of the collagen VI portion of the module. Its co-abundance is likely to report matrix production or remodeling by stromal cells. Direct control of PI3K-Akt or tissue-specific signaling is not established by this dataset.

#### COL6A2

- **Related proteins** (co-abundance neighbors): COL6A1 (0.96), COL6A3 (0.89), HSPG2 (0.84); STRING partners: COL6A1 (0.998), COL6A3 (0.994)
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 2 chain. This gene encodes one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The product of this gene contains several domains similar to von Willebrand Factor type A domains. These domains have been shown to bind extracellular matrix proteins, an interaction that explains the importance of this collagen in organizing matrix components. Mutation…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy 1B (0.770); Bethlem myopathy (0.755); Ullrich congenital muscular dystrophy (0.743); Bethlem myopathy 1B (0.723); Bethlem myopathy 1A (0.713)
- **Europe PMC papers**: 4115
- **Why important**: COL6A2 completes the collagen VI heterotrimer and has strong network links to COL6A1, COL6A3, and HSPG2. It is included in the primary ECM and collagen terms (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 3.11e-07) through (GO:CC extracellular matrix; q_global = 4.42e-06) and (GO:MF structural molecule activity; q_global = 0.00211) through (GO:CC collagen trimer; q_global = 0.0229). Its von-Willebrand-factor-A-like domains are described as mediating interactions with other extracellular-matrix proteins. It is associated with Bethlem myopathy and Ullrich congenital muscular dystrophy, while its HPA profile also provides the only notable group-enriched blood-cell signal in the module.
- **Conclusion**: Established evidence supports COL6A2 as a structural and matrix-organizing collagen VI component. The blood-cell annotation should be monitored as a possible minor confounder, but the overall module composition favors stromal ECM biology. Its specific contribution to the liver-rectum shared signal remains unresolved.

#### HSPG2

- **Related proteins** (co-abundance neighbors): COL6A1 (0.90), COL6A2 (0.84), COL6A3 (0.81); STRING partners: LAMC1 (0.82)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in liver, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 encodes perlecan, a large multidomain proteoglycan that cross-links extracellular-matrix and cell-surface molecules. It connects to all three collagen VI genes in the supplied network and to LAMC1 in STRING, and it is present in the primary ECM and basement-membrane terms (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 3.11e-07) through (GO:CC extracellular matrix; q_global = 4.42e-06) and (GO:MF structural molecule activity; q_global = 0.00211) through (GO:CC basement membrane; q_global = 0.0025). Its HPA annotation highlights blood vessels, hepatic stellate cells, fibro-adipogenic progenitors, and extracellular-matrix secretion. It also has disease associations including Schwartz-Jampel syndrome and dyssegmental dysplasia.
- **Conclusion**: Established evidence supports HSPG2 as the matrix-interface and signaling-permissive proteoglycan component of the module. Its ability to bind matrix and cell-surface molecules makes it a plausible bridge between scaffold structure and adhesion signaling. A specific causal role in the shared tissue pattern is a hypothesis.

#### LAMC1

- **Related proteins** (co-abundance neighbors): COL6A3 (0.81), LAMA5 (0.80); STRING partners: HSPG2 (0.82), LAMA5 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Plasma membrane; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit gamma 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: Fuchs' endothelial dystrophy (0.487); prostate carcinoma (0.467); colorectal cancer (0.447); eye disorder (0.434); benign colon neoplasm (0.427)
- **Europe PMC papers**: 4227
- **Why important**: LAMC1 is the laminin gamma chain and forms the strong STRING-supported laminin relationship with LAMA5. It also connects the laminin subgroup to COL6A3 and HSPG2 in the module network. Laminins are major noncollagenous basement-membrane constituents involved in adhesion, migration, differentiation, and signaling, and LAMC1 occurs in the primary ECM, basement-membrane, focal-adhesion, and integrin-related terms (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 3.11e-07) through (GO:CC basement membrane; q_global = 0.0025). It has extensive literature and reported associations with colorectal cancer and other disorders.
- **Conclusion**: Established evidence supports LAMC1 as a basement-membrane and adhesion-associated organizer that complements collagen VI and perlecan. Its position suggests a plausible interface between structural matrix and cell signaling, but the network does not establish directionality or causation.

#### LAMA5

- **Related proteins** (co-abundance neighbors): LAMC1 (0.80); STRING partners: LAMC1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit alpha 5. This gene encodes one of the vertebrate laminin alpha chains. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins are composed of 3 non identical chains: l…
- **Diseases (Open Targets)**: nephrotic syndrome, IIa 26 (0.761); bent bone dysplasia syndrome 2 (0.563); colorectal cancer (0.491); LAMA5-related multisystemic syndrome (0.475); polyp of colon (0.467)
- **Europe PMC papers**: 2881
- **Why important**: LAMA5 is the laminin alpha chain paired with LAMC1 and is present in the primary ECM-receptor, structural ECM, focal-adhesion, integrin, and PI3K-Akt terms (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 3.11e-07) through (GO:MF structural molecule activity; q_global = 0.00211). Its described functions include cell adhesion, integrin-mediated signaling, migration, and regulation of adhesion and migration. HPA places it in several specialized epithelial and stromal-associated cell types, and it has reported associations with colorectal cancer, colon polyps, and LAMA5-related multisystemic disease.
- **Conclusion**: Established evidence supports LAMA5 as the laminin ligand-side component of the basement-membrane and adhesion module. Its co-abundance with LAMC1 may mark coordinated laminin production in matrix-producing cells. Any disease-specific or tissue-specific signaling effect remains a hypothesis.
