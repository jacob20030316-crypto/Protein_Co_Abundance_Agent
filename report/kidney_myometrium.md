# Conserved co-abundance modules: kidney and myometrium

## Module 0

**Tissue pair**: kidney and myometrium  
**Genes (16)**: ACLY, AP2B1, COPB1, GANAB, HSPH1, HK1, IDE, NAA15, PCNA, PFAS, AARS1, TNPO1, TNPO3, USP5, USO1, XPO1

### Function

This is a broadly expressed intracellular maintenance and trafficking module rather than a narrowly tissue-specialized pathway. Its structure points to coordinated vesicle and Golgi trafficking through USO1 and COPB1, endocytic adaptor activity through AP2B1, nuclear import and export through TNPO1, TNPO3 and XPO1, protein quality control through USP5 and HSPH1, and core metabolic, translational and biosynthetic support through HK1, AARS1, PFAS, ACLY and related genes. These functions are biologically coherent with a shared cellular-state module in kidney and myometrium. However, no GO or KEGG term passed global correction, so the functional interpretation is based on the gene annotations, network structure, and supplementary STRING and hu.MAP evidence rather than a globally significant enrichment result. The STRING armadillo-like and armadillo-type fold signals (STRING InterPro Armadillo-like helical; within-query FDR = 0.0028) (STRING InterPro Armadillo-type fold; within-query FDR = 0.0118) are supplementary and mainly reflect a subset of trafficking and transport proteins.

**Cell composition.** The module is predominantly composed of intracellular, broadly expressed proteins. HPA reports low tissue specificity for most genes, low immune-cell specificity for nearly all genes, and only a small minority of secreted genes. This argues against the module being primarily a plasma-protein or blood-cell contamination signature. A single gene is immune-cell enhanced in neutrophils, while several genes show cell-type enhancement in spermatogenic, erythroid, trophoblast, muscle, pancreatic or other reference cell types. These isolated HPA patterns may reflect shared cellular programs or reference-atlas expression rather than a unified contaminating cell population. Protein detection is complete in kidney and partial in myometrium, supporting biological detectability in the tissues while also indicating that the co-abundance signal should not automatically be interpreted as a myometrium-specific program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides direct high-confidence support for the COPB1-USO1 relationship and for a transportin-exportin subnetwork involving TNPO1, TNPO3 and XPO1. These interactions are consistent with established vesicle trafficking and nucleocytoplasmic transport biology, but they connect only a subset of the module. The STRING armadillo-fold annotations (STRING InterPro Armadillo-like helical; within-query FDR = 0.0028) (STRING InterPro Armadillo-type fold; within-query FDR = 0.0118) are therefore supportive of shared structural features, not globally corrected module enrichment. hu.MAP independently places TNPO1 and TNPO3 together in complexes (hu.MAP huMAP3_09053.1) (hu.MAP huMAP3_11232.1), XPO1 with TNPO1 in (hu.MAP huMAP3_09592.1), USO1 with AP2B1 in (hu.MAP huMAP3_12394.1), and PFAS with HSPH1 in (hu.MAP huMAP3_13774.1). Because each hu.MAP complex contains many members outside this module, the evidence supports reuse of known cellular complexes rather than a newly defined whole-module complex. The remaining module edges may represent co-abundance relationships without direct physical interaction.

**STRING interactions (score >= 0.7)**: 4 of 120 gene pairs: COPB1–USO1 (0.869); TNPO1–TNPO3 (0.974); TNPO1–XPO1 (0.868); TNPO3–XPO1 (0.764)
**STRING functional enrichment (supplementary, within-query FDR)**: InterPro Armadillo-like helical (FDR = 0.0028, 6 genes); InterPro Armadillo-type fold (FDR = 0.0118, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09053.1 (TNPO1, TNPO3; 2/25); huMAP3_13774.1 (PFAS, HSPH1; 2/33); huMAP3_11232.1 (TNPO1, TNPO3; 2/78); huMAP3_09592.1 (XPO1, TNPO1; 2/95); huMAP3_12394.1 (USO1, AP2B1; 2/98)

### Novelty

The module appears to be a potentially new tissue-pair co-abundance observation, but not a newly established molecular pathway. Several of its strongest relationships are already represented by STRING or hu.MAP, and the component genes have well-described housekeeping, trafficking, transport, metabolic or proteostasis functions. The absence of a complete module match in the supplied interaction resources would not prove novelty, because co-abundance can arise from shared regulation, cell composition, indirect biochemical coupling or technical covariance. A defensible novelty claim is therefore limited to the particular coordinated pattern observed across kidney and myometrium; mechanistic novelty and tissue-specific novelty remain unproven without replication, independent cohorts, perturbation, and comparison with other tissue pairs.

**Hypothesis.** Hypothesis: this shared module reflects a coordinated intracellular resource-management state in which vesicle and Golgi traffic, endocytosis, nuclear transport, protein quality control, glucose and lipid metabolism, purine synthesis, and DNA replication are jointly adjusted across kidney and myometrium. USP5 and HSPH1 could help maintain proteome quality, USO1, COPB1 and AP2B1 could coordinate membrane cargo movement, and TNPO1, TNPO3 and XPO1 could couple cytoplasmic trafficking to nuclear regulation. The module may therefore report a common demand for protein processing and cellular transport rather than a tissue-specific biological pathway. This remains a hypothesis because the module lacks globally significant GO or KEGG enrichment and because co-abundance does not establish direction, causality or physical interaction.

### Important genes

#### USP5

- **Related proteins** (co-abundance neighbors): XPO1 (0.90), USO1 (0.85), AARS1 (0.83), GANAB (0.80), HSPH1 (0.80), HK1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin specific peptidase 5. Ubiquitin (see MIM 191339)-dependent proteolysis is a complex pathway of protein metabolism implicated in such diverse cellular functions as maintenance of chromatin structure, receptor function, and degradation of abnormal proteins. A late step of the process involves disassembly of the polyubiquitin chains on degraded proteins into ubiquitin monomers. USP5 disassembles branched polyubiquitin cha…
- **Diseases (Open Targets)**: neurodegenerative disease (0.532); neoplasm (0.116); hepatocellular carcinoma (0.110); non-small cell lung carcinoma (0.109); cancer (0.104)
- **Europe PMC papers**: 1576
- **Why important**: USP5 is the strongest network hub in the supplied subgraph and connects the trafficking-related genes with AARS1, GANAB, HSPH1 and HK1. Its established function is deubiquitination and disassembly of branched polyubiquitin chains, linking the module to protein turnover and proteostasis. It has substantial literature coverage and disease associations including neurodegenerative disease and neoplasia. Its HPA profile is broadly expressed, with detection in kidney but not myometrium.
- **Conclusion**: Established evidence supports USP5 as a central proteostasis and ubiquitin-processing component with an important coordinating position in this module. It is plausible that USP5 helps couple protein quality control to trafficking and metabolism, but the co-abundance data do not establish that it regulates the other module genes.

#### TNPO1

- **Related proteins** (co-abundance neighbors): TNPO3 (0.85), NAA15 (0.82), AARS1 (0.82); STRING partners: TNPO3 (0.974), XPO1 (0.868)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, myometrium
- **hu.MAP 3.0**: huMAP3_09053.1, huMAP3_11232.1, huMAP3_09592.1
- **Function (MyGene.info)**: transportin 1. This gene encodes the beta subunit of the karyopherin receptor complex which interacts with nuclear localization signals to target nuclear proteins to the nucleus. The karyopherin receptor complex is a heterodimer of an alpha subunit which recognizes the nuclear localization signal and a beta subunit which docks the complex at nucleoporins. Alternate splicing of this gene results in several transc…
- **Diseases (Open Targets)**: atrial fibrillation (0.415); neurodegenerative disease (0.370); hypothyroidism (0.320); injury (0.198); bladder calculus (0.183)
- **Europe PMC papers**: 822
- **Why important**: TNPO1 is connected to TNPO3, NAA15 and AARS1 and is present in multiple hu.MAP complexes (hu.MAP huMAP3_09053.1) (hu.MAP huMAP3_11232.1) (hu.MAP huMAP3_09592.1). Its established role is karyopherin-mediated nuclear import, making it a plausible bridge between cytoplasmic cellular state and nuclear regulation. It also has disease associations including atrial fibrillation and neurodegenerative disease, with a substantial literature base.
- **Conclusion**: Established evidence supports TNPO1 as a nuclear transport component and as one of the best-supported physical-network anchors in the module. Its participation in the shared tissue module may indicate coordinated nucleocytoplasmic transport, but a tissue-specific regulatory role is not demonstrated.

#### USO1

- **Related proteins** (co-abundance neighbors): USP5 (0.85), IDE (0.83), AARS1 (0.82); STRING partners: COPB1 (0.869)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: USO1 vesicle transport factor. The protein encoded by this gene is a peripheral membrane protein which recycles between the cytosol and the Golgi apparatus during interphase. It is regulated by phosphorylation: dephosphorylated protein associates with the Golgi membrane and dissociates from the membrane upon phosphorylation. Ras-associated protein 1 recruits this protein to coat protein complex II (COPII) vesicles during buddin…
- **Diseases (Open Targets)**: psoriatic arthritis (0.184); bipolar disorder (0.150); retinitis pigmentosa (0.085); cone dystrophy (0.076); cone-rod dystrophy (0.076)
- **Europe PMC papers**: 546
- **Why important**: USO1 has a relatively central position in the module and links USP5, IDE and AARS1. It is annotated to ER-to-Golgi vesicle transport and Golgi vesicle fusion. STRING supports its relationship with COPB1, the supplementary armadillo-fold terms include USO1 (STRING InterPro Armadillo-like helical; within-query FDR = 0.0028) (STRING InterPro Armadillo-type fold; within-query FDR = 0.0118), and hu.MAP places it with AP2B1 in a trafficking complex (hu.MAP huMAP3_12394.1). Its HPA profile includes skeletal-muscle and myonuclear enhancement, although its tissue specificity is not broadly restricted.
- **Conclusion**: Established evidence supports USO1 as a strong candidate for the module's vesicle-transport axis. The network suggests coordination between Golgi trafficking and proteostasis, but whether USO1 is a driver rather than a correlated component remains a hypothesis.

#### IDE

- **Related proteins** (co-abundance neighbors): COPB1 (0.85), USO1 (0.83), ACLY (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in kidney, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin degrading enzyme. This gene encodes a zinc metallopeptidase that degrades intracellular insulin, and thereby terminates insulins activity, as well as participating in intercellular peptide signalling by degrading diverse peptides such as glucagon, amylin, bradykinin, and kallidin. The preferential affinity of this enzyme for insulin results in insulin-mediated inhibition of the degradation of other peptides such as…
- **Diseases (Open Targets)**: diabetes mellitus (0.307); type 2 diabetes mellitus (0.287); diabetic retinopathy (0.146); diabetic eye disease (0.144); brain cancer (0.142)
- **Europe PMC papers**: 19876
- **Why important**: IDE connects COPB1, USO1 and ACLY, thereby linking trafficking-associated genes with peptide degradation and cytosolic metabolism. Its established functions include degradation of insulin and other peptides, proteolysis, ubiquitin recycling and antigen processing. It has extensive literature coverage and disease associations involving diabetes, diabetic complications and neurodegenerative biology. It is detected in both kidney and myometrium and is described as secreted in other tissues.
- **Conclusion**: Established evidence supports IDE as a multifunctional protease that could connect metabolic signaling with intracellular protein handling. Its position makes it biologically informative for the module, but the data do not show that insulin or extracellular peptide signaling explains the shared co-abundance pattern.

#### PCNA

- **Related proteins** (co-abundance neighbors): PFAS (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proliferating cell nuclear antigen. The protein encoded by this gene is found in the nucleus and is a cofactor of DNA polymerase delta. The encoded protein acts as a homotrimer and helps increase the processivity of leading strand synthesis during DNA replication. In response to DNA damage, this protein is ubiquitinated and is involved in the RAD6-dependent DNA repair pathway. Two transcript variants encoding the same protein have b…
- **Diseases (Open Targets)**: ataxia-telangiectasia-like disorder (0.497); neurodegenerative disease (0.188); neoplasm (0.118); diabetes mellitus (0.116); hepatocellular carcinoma (0.113)
- **Europe PMC papers**: 61820
- **Why important**: PCNA is connected to PFAS and is a canonical nuclear factor for DNA replication, mismatch repair and DNA-damage responses. It has exceptionally extensive literature coverage, disease associations involving genome maintenance and neoplasia, and HPA enhancement in several proliferative or progenitor cell types including erythroid and germ-cell populations. Its detection in both tissues supports the possibility that the module includes a proliferative or repair-related component.
- **Conclusion**: Established evidence supports PCNA as a DNA-replication and repair marker whose presence may indicate replication or stress-related cellular activity. A proliferative interpretation of the entire module is not justified because PCNA is only one peripheral module member and no globally significant enrichment supports that conclusion.

#### HSPH1

- **Related proteins** (co-abundance neighbors): USP5 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_13774.1
- **Function (MyGene.info)**: heat shock protein family H (Hsp110) member 1. This gene encodes a member of the heat shock protein 70 family of proteins. The encoded protein functions as a nucleotide exchange factor for the molecular chaperone heat shock cognate 71 kDa protein (Hsc70). In addition, this protein plays a distinct but related role as a holdase that inhibits the aggregation of misfolded proteins, including the cystic fibrosis transmembrane conductance regulator…
- **Diseases (Open Targets)**: Parkinson disease (0.205); Phenotypic abnormality (0.187); hypertensive disorder (0.131); neoplasm (0.104); major depressive disorder (0.096)
- **Europe PMC papers**: 2050
- **Why important**: HSPH1 is connected to USP5 and participates with PFAS in hu.MAP complex (hu.MAP huMAP3_13774.1). Its established function is as an HSP seventy-family nucleotide-exchange factor and holdase that limits aggregation of misfolded proteins. It has disease and stress-related annotations and a substantial literature base. Its HPA pattern is broadly expressed with cell-type enhancement in several epithelial or immune-associated reference populations.
- **Conclusion**: Established evidence supports HSPH1 as a proteostasis and stress-response component that complements USP5. Its inclusion supports a protein-quality-control interpretation, but the module does not demonstrate that unfolded-protein stress is the initiating process in either tissue.

## Module 1

**Tissue pair**: kidney and myometrium  
**Genes (7)**: ATXN10, DDX39B, HNRNPK, EIF5, METAP2, PTBP1, SARS1

### Function

The module most plausibly reflects a broadly expressed intracellular gene-expression and protein-production program, centered on RNA processing, pre-mRNA splicing, nuclear RNA export, translation initiation, and nascent-protein processing. This interpretation is based on the annotated functions of PTBP1, HNRNPK, DDX39B, EIF5, SARS1, and METAP2, together with the direct network links among the RNA-associated genes. No GO or KEGG term passed global correction, so the functional interpretation remains gene-level and network-based rather than enrichment-confirmed.

**Cell composition.** All module proteins are detected in both kidney and myometrium, and all have low tissue specificity. None is secreted, and the module does not show blood-cell specificity. The profile therefore argues against a plasma-protein or blood-contamination explanation. Its broad expression and intracellular locations instead suggest a housekeeping-like program that could reflect shared basal cellular activity, although the cell-type information provides limited support for a narrowly defined tissue or cell population. DDX39B has group-enriched expression in several neural cell types, while EIF5 and METAP2 show cell-type-enhanced expression in late spermatids and erythrocyte progenitors respectively; these isolated observations do not establish the module as neural, germ-cell, or erythroid.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known relationship is between HNRNPK and PTBP1, with additional high-confidence links connecting DDX39B to each of them. These relationships support a real RNA-processing-associated core within the co-abundance module. The module also contains network links from PTBP1 to ATXN10 and SARS1, from HNRNPK to EIF5, and from ATXN10 to METAP2, but those relationships are not represented as STRING interactions in the supplied evidence. No hu.MAP complex contains multiple module members. Thus, the network is partly supported by known pairwise associations but does not correspond to a documented shared multiprotein complex.

**STRING interactions (score >= 0.7)**: 3 of 21 gene pairs: DDX39B–HNRNPK (0.808); DDX39B–PTBP1 (0.785); HNRNPK–PTBP1 (0.997)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should be regarded as a potentially interesting cross-tissue co-abundance observation rather than a demonstrated new biological complex or pathway. Its strongest internal relationships are already known, and the genes are broadly expressed with established roles in basic RNA and protein metabolism. The absence of a hu.MAP complex or additional STRING interactions does not prove novelty. A stronger novelty claim would require comparison with published kidney and myometrium co-abundance modules, independent cohorts, expression quantitative trait or perturbation data, and experimental testing of the proposed cross-tissue coordination.

**Hypothesis.** Hypothesis: the shared kidney–myometrium module represents coordinated variation in a basal RNA-handling and protein-synthesis state. PTBP1 and HNRNPK may form an RNA-regulatory core, with DDX39B supporting spliceosome assembly and nuclear RNA export, while EIF5, SARS1, and METAP2 support translation initiation, tRNA charging, and processing of newly synthesized proteins. ATXN10 may connect this state to cell-structure or cell-cycle-related functions. This is a mechanistic hypothesis, not an established pathway assignment, because global enrichment was absent and the module lacks a shared hu.MAP complex.

### Important genes

#### PTBP1

- **Related proteins** (co-abundance neighbors): HNRNPK (0.88), ATXN10 (0.82), SARS1 (0.82), DDX39B (0.81); STRING partners: DDX39B (0.785), HNRNPK (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypyrimidine tract binding protein 1. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA-binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.505); dengue disease (0.372); open-angle glaucoma (0.330); glaucoma (0.309); neoplasm (0.116)
- **Europe PMC papers**: 4849
- **Why important**: PTBP1 is the highest-connectivity node in the module and links the RNA-associated core to ATXN10 and SARS1 as well as to HNRNPK and DDX39B. Its established functions include regulation of alternative splicing, mRNA processing, RNA splicing, and gene expression. It is broadly expressed, detected in both tissues, and has substantial literature coverage. Its disease associations include neurodevelopmental disorder, dengue disease, and glaucoma.
- **Conclusion**: Established evidence supports PTBP1 as the principal network hub and a plausible regulator of shared RNA-processing variation. It is not established that PTBP1 drives the module or that the module alters any particular splice isoform; those claims remain hypotheses.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): PTBP1 (0.88), EIF5 (0.83); STRING partners: DDX39B (0.808), PTBP1 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is directly connected to PTBP1 and EIF5 and has the strongest supplied STRING relationship with PTBP1. It is a nucleoplasmic heterogeneous nuclear ribonucleoprotein involved in RNA processing, spliceosomal mRNA splicing, transcriptional regulation, and signal transduction. It is detected in both tissues, broadly expressed, associated with several human disease categories, and has substantial literature coverage.
- **Conclusion**: Established evidence supports HNRNPK as an RNA-processing and transcriptional regulatory component that reinforces the module's intracellular gene-expression interpretation. Its specific causal role in the kidney–myometrium co-abundance pattern is unproven.

#### DDX39B

- **Related proteins** (co-abundance neighbors): PTBP1 (0.81); STRING partners: HNRNPK (0.808), PTBP1 (0.785)
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nuclear speckles; IHC detected in kidney, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 39B. This gene encodes a member of the DEAD box family of RNA-dependent ATPases that mediate ATP hydrolysis during pre-mRNA splicing. The encoded protein is an essential splicing factor required for association of U2 small nuclear ribonucleoprotein with pre-mRNA, and it also plays an important role in mRNA export from the nucleus to the cytoplasm. This gene belongs to a cluster of genes localized in th…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); Alzheimer disease (0.522); Parkinson disease (0.503); lysosomal storage disease (0.503); neurodevelopmental disorder (0.413)
- **Europe PMC papers**: 1037
- **Why important**: DDX39B provides a functionally coherent connection to the PTBP1–HNRNPK core through its known relationships with both proteins. It is an RNA-dependent ATPase required for U2 small nuclear ribonucleoprotein association with pre-mRNA, spliceosomal activity, and nuclear mRNA export. It is detected in both tissues and has disease associations spanning neurodegenerative and neurodevelopmental disorders.
- **Conclusion**: Established evidence supports DDX39B as a strong candidate for the splicing and RNA-export component of the module. The neural cell-type expression pattern does not demonstrate that neural cells generate the tissue-level module, and any such attribution remains uncertain.

#### METAP2

- **Related proteins** (co-abundance neighbors): ATXN10 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in kidney, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionyl aminopeptidase 2. The protein encoded by this gene is a member of the methionyl aminopeptidase family. The encoded protein functions both by protecting the alpha subunit of eukaryotic initiation factor 2 from inhibitory phosphorylation and by removing the amino-terminal methionine residue from nascent proteins. Increased expression of this gene is associated with various forms of cancer, and the anti-cancer drugs f…
- **Diseases (Open Targets)**: neurodegenerative disease (0.521); autoimmune disorder of central nervous system (0.316); obesity disorder (0.305); Prader-Willi syndrome (0.279); Polyphagia (0.259)
- **Europe PMC papers**: 828
- **Why important**: METAP2 connects to ATXN10 and supplies a complementary protein-biogenesis function. It removes amino-terminal methionine from nascent proteins and regulates translation initiation through effects on the alpha subunit of eukaryotic initiation factor two. It is detected in both tissues, has documented links to protein processing and translational regulation, and is associated with cancer and several other disease categories.
- **Conclusion**: Established evidence supports METAP2 as a plausible downstream protein-maturation component accompanying the RNA-processing genes. The module does not establish that METAP2 activity is coordinated mechanistically with PTBP1 or DDX39B, so that connection is hypothetical.

#### EIF5

- **Related proteins** (co-abundance neighbors): HNRNPK (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 5. Eukaryotic translation initiation factor-5 (EIF5) interacts with the 40S initiation complex to promote hydrolysis of bound GTP with concomitant joining of the 60S ribosomal subunit to the 40S initiation complex. The resulting functional 80S ribosomal initiation complex is then active in peptidyl transfer and chain elongations (summary by Si et al., 1996 [PubMed 8663286]).[supplied by OMIM, May 201…
- **Diseases (Open Targets)**: knee fracture (0.219); hair color (0.161); Abnormality of the skeletal system (0.103); liver disorder (0.088); hypertensive disorder (0.079)
- **Europe PMC papers**: 1989
- **Why important**: EIF5 is connected to HNRNPK in the module and represents the translation-initiation arm of the proposed function. It promotes GTP hydrolysis during joining of translation subunits and supports formation and regulation of the cytoplasmic translation-initiation complex. It is detected in both tissues and has broad literature coverage, although its network position is peripheral.
- **Conclusion**: Established evidence supports EIF5 as a translation-related component that may explain co-abundance with RNA-processing factors. Its peripheral position and lack of a documented shared complex make a direct mechanistic role in the module uncertain.

## Module 2

**Tissue pair**: kidney and myometrium  
**Genes (11)**: CAPN2, DNM1L, GARS1, HSP90AB2P, HSP90AA1, HSPA8, MOGS, CTPS1, SEC23A, TARS1, VPS35

### Function

The strongest functional interpretation is a conserved proteostasis and intracellular trafficking module centered on endoplasmic-reticulum protein processing. The primary evidence is (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0121), in which CAPN2, HSP90AA1, HSPA8, MOGS, and SEC23A jointly support the KEGG protein-processing-in-the-endoplasmic-reticulum pathway. The biological roles of these genes are complementary: MOGS performs early N-linked oligosaccharide processing in the ER, SEC23A supports COPII vesicle budding and ER-to-Golgi transport, and HSP90AA1 and HSPA8 provide chaperone activity for protein folding. CAPN2 adds calcium-regulated intracellular proteolysis. The remaining genes suggest supporting cellular processes rather than a second equally strong pathway: GARS1 and TARS1 support translation through tRNA aminoacylation, CTPS1 supports nucleotide and phospholipid precursor synthesis, VPS35 supports endosomal-to-Golgi trafficking, and DNM1L supports mitochondrial and peroxisomal dynamics. Thus, the module is best viewed as a proteostasis, secretory-trafficking, and organelle-maintenance program rather than a narrowly defined enzyme complex. The testis and perinuclear-region results (STRING TISSUES Testis; within-query FDR = 0.003) and (STRING Component Perinuclear region of cytoplasm; within-query FDR = 0.0239) are supplementary and consistent with broad intracellular organization, but they are not primary globally corrected enrichment evidence.

**Cell composition.** This does not look like a plasma-protein or blood-cell module. HPA reports low immune-cell specificity for the annotated genes and no recurrent enriched blood-cell type. It also is not dominated by secreted proteins: the component genes are mainly intracellular, cytosolic, ER, endosomal, or organellar proteins, with only a single secreted-gene annotation in the module summary. Most annotated genes have low tissue specificity, which is consistent with broadly expressed housekeeping or core-cellular functions. HPA protein detection is stronger in kidney than in myometrium for this module, while several proteins are detected in both tissues. The lack of tissue-specific enrichment and the presence of translation, chaperone, trafficking, and nucleotide-biosynthesis genes mean that shared abundance may reflect common cellular infrastructure or shared cell states rather than a kidney- or myometrium-specific lineage program. The isolated single-cell enrichments should not be interpreted as evidence that the whole module represents those cell types.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human) | 0.0121 | CAPN2, HSP90AA1, HSPA8, MOGS, SEC23A |

### STRING and hu.MAP

STRING supports only a limited set of direct high-confidence relationships within the module: DNM1L with VPS35, GARS1 with TARS1, and HSP90AA1 with HSPA8. These relationships are biologically interpretable as links involving organelle and endosomal dynamics, a glycyl- and threonyl-tRNA-synthetase pair, and a chaperone pair. STRING supplementary enrichment independently recapitulates the ER protein-processing signal (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0019) and also points to testis-associated and perinuclear annotations (STRING TISSUES Testis; within-query FDR = 0.003) and (STRING Component Perinuclear region of cytoplasm; within-query FDR = 0.0239). However, most module pairs are not established STRING relationships, so the co-abundance graph should not be treated as a physical interaction network. No hu.MAP complex contains multiple module members. Together, these results support a partially known functional neighborhood assembled from several cellular systems, but they do not demonstrate one pre-existing multiprotein complex.

**STRING interactions (score >= 0.7)**: 3 of 55 gene pairs: DNM1L–VPS35 (0.9); GARS1–TARS1 (0.909); HSP90AA1–HSPA8 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Protein processing in endoplasmic reticulum (FDR = 0.0019, 5 genes); TISSUES Testis (FDR = 0.003, 9 genes); Component Perinuclear region of cytoplasm (FDR = 0.0239, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The pathway interpretation is not itself a new biological concept, because ER protein processing, chaperoning, glycosylation, COPII transport, translation, and organelle dynamics are established functions. The module-level observation may nevertheless be a new co-abundance finding: it combines these processes across kidney and myometrium, while showing only a limited set of known STRING relationships and no multi-member hu.MAP complex. Absence from STRING or hu.MAP cannot establish novelty, because those resources emphasize physical interactions or curated complexes rather than tissue-pair co-abundance. A defensible claim is therefore that this is a potentially novel tissue-shared co-abundance configuration of largely known proteins, requiring replication in independent cohorts and comparison with published kidney and myometrium proteomic networks before being called a new biological module.

**Hypothesis.** Mechanistic hypothesis: shared cellular stress or protein-flux demands in kidney and myometrium increase coordination between ER quality control, glycoprotein maturation, ER-to-Golgi export, chaperone-assisted folding, and selective intracellular turnover. In this model, MOGS and SEC23A handle maturation and export, HSP90AA1 and HSPA8 stabilize client proteins, CAPN2 provides regulated proteolytic remodeling, and VPS35 and DNM1L connect trafficking with organelle maintenance. GARS1, TARS1, and CTPS1 may supply the translation and nucleotide or membrane-building capacity needed to sustain this response. This is a hypothesis derived from co-abundance and functional annotations, not proof of direct physical cooperation or causal regulation.

### Important genes

#### HSP90AA1

- **Related proteins** (co-abundance neighbors): HSP90AB2P (0.91), TARS1 (0.84), CTPS1 (0.84); STRING partners: HSPA8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein 90 alpha family class A member 1. The protein encoded by this gene is an inducible molecular chaperone that functions as a homodimer. The encoded protein aids in the proper folding of specific target proteins by use of an ATPase activity that is modulated by co-chaperones. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: cancer (0.643); plasma cell myeloma (0.404); non-small cell lung carcinoma (0.394); dengue disease (0.375); Orthomyxoviridae infectious disease (0.375)
- **Europe PMC papers**: 8215
- **Why important**: HSP90AA1 is a central chaperone-associated node in the module and is directly linked in STRING to HSPA8. It is one of the genes in the primary ER protein-processing evidence (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0121) and also appears in the supplementary STRING annotations (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0019), (STRING TISSUES Testis; within-query FDR = 0.003), and (STRING Component Perinuclear region of cytoplasm; within-query FDR = 0.0239). Its established function is ATP-regulated folding of specific client proteins, and it has extensive disease and literature coverage, including cancer and infectious-disease associations.
- **Conclusion**: Established evidence supports HSP90AA1 as a major proteostasis component and a plausible anchor of the module. It is reasonable to hypothesize that its abundance tracks folding demand in the shared tissue state, but the data do not establish that HSP90AA1 drives the module or that its clients are directly responsible for the tissue pairing.

#### HSPA8

- **Related proteins** (co-abundance neighbors): GARS1 (0.88), TARS1 (0.84), HSP90AB2P (0.80); STRING partners: HSP90AA1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Flagellar centriole, Annulus; IHC detected in kidney, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 8. This gene encodes a member of the heat shock protein 70 family, which contains both heat-inducible and constitutively expressed members. This protein belongs to the latter group, which are also referred to as heat-shock cognate proteins. It functions as a chaperone, and binds to nascent polypeptides to facilitate correct folding. It also functions as an ATPase in the disassembly of clathrin-coated…
- **Diseases (Open Targets)**: dengue disease (0.505); systemic lupus erythematosus (0.375); smoking initiation (0.199); Lennox-Gastaut syndrome (0.118); neoplasm (0.105)
- **Europe PMC papers**: 6937
- **Why important**: HSPA8 is among the more connected genes in the module, links to GARS1, TARS1, and HSP90AB2P, and has a high-confidence STRING relationship with HSP90AA1. It is included in (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0121) and in the supplementary ER, testis, and perinuclear annotations (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0019), (STRING TISSUES Testis; within-query FDR = 0.003), and (STRING Component Perinuclear region of cytoplasm; within-query FDR = 0.0239). Its established functions include constitutive chaperoning, folding of nascent polypeptides, response to unfolded proteins, and ATP-dependent disassembly of clathrin-coated vesicles. It has extensive literature and disease-association coverage.
- **Conclusion**: Established evidence places HSPA8 at the interface of protein folding and membrane-trafficking quality control. Its network position makes it a strong marker of the module's cellular state, while any causal role in the kidney–myometrium conservation remains hypothetical.

#### SEC23A

- **Related proteins** (co-abundance neighbors): HSP90AB2P (0.80), VPS35 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A is a primary-evidence gene in (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0121) and is connected in the module to HSP90AB2P and VPS35. It encodes a COPII component required for ER-to-Golgi transport, vesicle budding, and cargo loading, giving it a direct mechanistic link to the module's strongest pathway interpretation. It has established disease associations involving craniofacial and skeletal development and has substantial literature coverage.
- **Conclusion**: Established evidence supports SEC23A as the module's principal secretory-trafficking component. Its co-abundance with chaperones and ER glycan processing machinery is compatible with coordinated handling of newly folded cargo, but direct regulation among these genes is not demonstrated.

#### MOGS

- **Related proteins** (co-abundance neighbors): GARS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosyl-oligosaccharide glucosidase. This gene encodes the first enzyme in the N-linked oligosaccharide processing pathway. The enzyme cleaves the distal alpha-1,2-linked glucose residue from the Glc(3)-Man(9)-GlcNAc(2) oligosaccharide precursor. This protein is located in the lumen of the endoplasmic reticulum. Defects in this gene are a cause of type IIb congenital disorder of glycosylation (CDGIIb). Two transcript variants encodin…
- **Diseases (Open Targets)**: MOGS-congenital disorder of glycosylation (0.818); congenital disorder of glycosylation (0.374); congenital disorder of glycosylation type II (0.370); severe acute respiratory syndrome (0.370); SRD5A3-congenital disorder of glycosylation (0.370)
- **Europe PMC papers**: 987
- **Why important**: MOGS is one of the primary-evidence genes in (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0121) and is located in the ER lumen, where it performs an early step in N-linked oligosaccharide processing. It connects in the module to GARS1 and is also represented in supplementary ER and testis annotations (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0019) and (STRING TISSUES Testis; within-query FDR = 0.003). Its congenital-disorder associations provide a clear link between the encoded activity and protein-glycosylation homeostasis, and it has substantial literature coverage.
- **Conclusion**: Established evidence identifies MOGS as a specific biochemical contributor to ER glycoprotein maturation. It strengthens the interpretation that the module involves secretory-protein quality control, although its single network connection means it is more likely a pathway-specific component than a graph-wide hub.

#### CAPN2

- **Related proteins** (co-abundance neighbors): GARS1 (0.83), TARS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Connecting piece, Mid piece; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calpain 2. The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpa…
- **Diseases (Open Targets)**: Alzheimer disease (0.389); urolithiasis (0.288); alcohol drinking (0.288); aortic stenosis (0.141); neoplasm (0.105)
- **Europe PMC papers**: 1796
- **Why important**: CAPN2 is among the more connected module genes and is included in (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0121). It links to GARS1 and TARS1 and appears in supplementary ER and perinuclear annotations (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0019) and (STRING Component Perinuclear region of cytoplasm; within-query FDR = 0.0239). Its established function as a calcium-activated intracellular cysteine protease provides a potential remodeling or quality-control arm alongside chaperoning and ER export. It has extensive disease and literature coverage, including associations with neurodegenerative disease, urolithiasis, and neoplasia.
- **Conclusion**: Established evidence supports CAPN2 as a regulated intracellular proteolysis component that broadens the module beyond folding and trafficking. Its participation in the shared module could reflect calcium- or mechanical-state regulation, but that mechanistic connection is a hypothesis rather than a demonstrated causal pathway.

## Module 3

**Tissue pair**: kidney and myometrium  
**Genes (12)**: DBNL, DDX6, EPS15L1, GMPS, PSMC2, SF3A1, RARS1, CCT3, CCT7, CCT8, THOP1, TSG101

### Function

The strongest functional interpretation is a conserved intracellular proteostasis and RNA or protein-processing module centered on the CCT chaperonin complex. CCT3, CCT7, and CCT8 account for all of the globally corrected GO evidence (19 globally significant GO/KEGG terms, q_global 0.0067–0.0236; see the table). These terms support chaperonin-containing T-complex membership, ATP-dependent protein folding, protein localization to nuclear and Cajal bodies, telomerase-RNA localization, and telomere maintenance. The CCT annotations are biologically coherent with the supplied gene descriptions for CCT3, CCT7, and CCT8, which identify them as subunits of the TRiC or CCT folding machine. The sperm-binding and sperm–egg recognition terms (GO:BP binding of sperm to zona pellucida; q_global = 0.0138) and (GO:BP sperm-egg recognition; q_global = 0.0236) should be interpreted cautiously: they are carried by the same CCT genes and do not by themselves establish a reproductive-tissue-specific function. The remaining genes suggest connected support processes involving translation, RNA processing, mRNA turnover, proteasomal degradation, vesicle or endosomal trafficking, and purine biosynthesis. Overall, the module is best viewed as a protein-folding and cellular quality-control core with links to RNA metabolism and macromolecular turnover, rather than as a narrowly tissue-specific pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It also does not show a blood-cell-enriched composition, because every gene has low immune-cell specificity and no enriched blood-cell category is reported. Most genes have low tissue specificity, and several are detected in kidney and myometrium, which is compatible with broadly expressed intracellular housekeeping or core-cellular machinery. The module nevertheless contains cell-type-enhanced signals for germ-cell populations, oocytes, myonuclei, neutrophils, syncytiotrophoblasts, epithelial cells, and hepatocyte-lineage cells. GMPS is tissue-enhanced in testis and is cell-type enhanced in spermatogenic populations, while CCT7 and related genes also show spermatogenic cell-type enhancement. These observations may reflect shared cellular programs or mixed-cell composition, but they do not support a blood-contamination explanation and do not establish that the module is specific to reproductive tissue.

**GO/KEGG enrichment**: 19 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chaperonin-containing T-complex | 0.0067 | CCT3, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 0.0067 | CCT3, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 0.0067 | CCT3, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 0.0067 | CCT3, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 0.0067 | CCT3, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 0.0067 | CCT3, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 0.0067 | CCT3, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 0.0067 | CCT3, CCT7, CCT8 |
| GO:BP binding of sperm to zona pellucida | 0.0138 | CCT3, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 0.0138 | CCT3, CCT7, CCT8 |
| GO:BP RNA localization to Cajal body | 0.0138 | CCT3, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 0.0138 | CCT3, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 0.0138 | CCT3, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 0.0138 | CCT3, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomere lengthening | 0.0138 | CCT3, CCT7, CCT8 |

### STRING and hu.MAP

STRING provides very strong direct support for a CCT subnetwork: CCT3, CCT7, and CCT8 are mutually connected with near-maximal reported confidence (9 supplementary STRING terms; within-query FDR 0.0046–0.0215) and (STRING NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis; within-query FDR = 0.0385) (STRING RCTM Folding of actin by CCT/TriC; within-query FDR = 0.0404) (STRING RCTM Association of TriC/CCT with target proteins during biosynthesis; within-query FDR = 0.0428). STRING also links CCT8 with PSMC2 and links GMPS with RARS1. The supplementary STRING results independently reinforce the CCT or TCP-1 family, the chaperonin-containing T-complex, ATP hydrolysis, cellular proteostasis, and actin folding (13 supplementary STRING terms; within-query FDR 0.0046–0.0428). The CCT triad is represented in several hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), alongside additional CCT subunits, TCP1, tubulin-related proteins, prefoldin-associated proteins, and regulatory proteins. This means that the central CCT relationships are established physical or functional associations, not newly inferred edges. By contrast, the other module connections are less strongly supported by the supplied external resources: EPS15L1, DBNL, TSG101, DDX6, SF3A1, GMPS, RARS1, THOP1, and PSMC2 do not form a broad hu.MAP-supported complex within this module, and several have no listed STRING partner. The network therefore appears to contain a well-established CCT core plus peripheral or tissue-dependent co-abundance links.

**STRING interactions (score >= 0.7)**: 5 of 66 gene pairs: CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT7–CCT8 (0.999); CCT8–PSMC2 (0.733); GMPS–RARS1 (0.872)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam TCP-1/cpn60 chaperonin family (FDR = 0.0046, 3 genes); Component Chaperonin-containing T-complex (FDR = 0.0164, 3 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 0.0169, 3 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 0.0215, 3 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 0.0215, 3 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 0.0215, 3 genes); InterPro GroEL-like apical domain superfamily (FDR = 0.0215, 3 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 0.0215, 3 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 0.0215, 3 genes); Function ATP hydrolysis activity (FDR = 0.0249, 5 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis (FDR = 0.0385, 3 genes); RCTM Folding of actin by CCT/TriC (FDR = 0.0404, 3 genes); RCTM Association of TriC/CCT with target proteins during biosynthesis (FDR = 0.0428, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT3, CCT8, CCT7; 3/23); huMAP3_06559.1 (CCT3, CCT8, CCT7; 3/25); huMAP3_09191.1 (CCT3, CCT8, CCT7; 3/32); huMAP3_10656.1 (CCT3, CCT8, CCT7; 3/36); huMAP3_14584.1 (CCT3, CCT8, CCT7; 3/61); huMAP3_01951.1 (CCT3, CCT7; 2/8)

### Novelty

The module should not be described as a newly discovered CCT complex. Its central CCT3–CCT7–CCT8 relationships are already strongly represented in STRING and repeatedly represented in hu.MAP (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). The globally corrected enrichment is also a coherent recovery of a well-known chaperonin function rather than evidence that the individual CCT interactions are novel. A potentially novel aspect could be the reproducible co-abundance of this CCT core with the particular peripheral genes in a conserved kidney–myometrium module, especially the links involving EPS15L1, DDX6, GMPS, SF3A1, RARS1, THOP1, and PSMC2. However, absence of those links from STRING or hu.MAP does not prove novelty: it may reflect context dependence, incomplete interaction databases, indirect regulation, shared cell composition, or technical co-abundance. The appropriate conclusion is that the module represents a new tissue-pair-level organization or observation of largely established cellular machinery, with novelty requiring independent replication and perturbation testing.

**Hypothesis.** Hypothesis: in both kidney and myometrium, a shared intracellular demand for proteome maintenance couples CCT-mediated folding with RNA handling, translation control, proteasomal turnover, and vesicle-associated trafficking. The CCT3–CCT7–CCT8 core may fold or stabilize cytoskeletal and other newly synthesized proteins, while PSMC2 could connect this activity to proteasome-dependent quality control. RARS1 may link translation capacity to the chaperone core, and SF3A1 and DDX6 may connect it to pre-mRNA processing and cytoplasmic mRNA turnover. EPS15L1, DBNL, and TSG101 could represent an endocytic or vesicle-trafficking branch, whereas GMPS and THOP1 may reflect nucleotide supply and cytosolic peptide processing. This is a mechanistic model, not an established pathway demonstrated by the co-abundance data; direct interaction, perturbation, and cell-composition-controlled experiments are needed.

### Important genes

#### CCT8

- **Related proteins** (co-abundance neighbors): RARS1 (0.87), CCT3 (0.82), THOP1 (0.82); STRING partners: CCT3 (0.999), CCT7 (0.999), PSMC2 (0.733)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is a central network connector, linking the CCT core to RARS1 and THOP1 while also connecting to CCT3, CCT7, and PSMC2 in STRING. It participates in every globally corrected enrichment term (19 globally significant GO/KEGG terms, q_global 0.0067–0.0236; see the table) and every listed STRING functional category (13 supplementary STRING terms; within-query FDR 0.0046–0.0428). Its annotation identifies it as the theta subunit of the ATP-dependent CCT folding complex, with functions in protein folding, protein stabilization, and telomerase-related RNA localization. It has extensive literature coverage and cancer-related Open Targets associations.
- **Conclusion**: Established: CCT8 is a core component and network bridge of the module’s chaperonin-centered machinery. Hypothesis: its bridging position may help couple protein folding to translation, peptide processing, and proteasomal quality control in the shared tissue context.

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT7 (0.89), CCT8 (0.82); STRING partners: CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in kidney, myometrium
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a member of the tightly supported CCT3–CCT7–CCT8 subnetwork, appears in every primary enrichment term (19 globally significant GO/KEGG terms, q_global 0.0067–0.0236; see the table), and is represented in all listed hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). Its supplied annotation directly supports ATP-dependent folding of actin, tubulin, and other unfolded polypeptides. It has extensive literature coverage and disease associations involving neurodevelopmental, neurodegenerative, skeletal, autoimmune, and cardiac conditions.
- **Conclusion**: Established: CCT3 provides strong molecular evidence that the module contains a bona fide CCT or TRiC folding component. Hypothesis: variation in CCT3 abundance could influence the folding capacity of shared kidney and myometrial cell populations, but the co-abundance result does not establish causality.

#### CCT7

- **Related proteins** (co-abundance neighbors): CCT3 (0.89); STRING partners: CCT3 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney, myometrium
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 completes the highly supported CCT triad with CCT3 and CCT8, contributes to every primary enrichment term (19 globally significant GO/KEGG terms, q_global 0.0067–0.0236; see the table), and is present in all listed hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). Its supplied function is ATP-dependent chaperonin-mediated folding of proteins including actin and tubulin. It has substantial literature coverage and reported associations with myocardial infarction, preeclampsia, neurodegeneration, and hepatocellular carcinoma. Its spermatogenic cell-type enhancement is relevant when interpreting the reproductive-cell signals in the module.
- **Conclusion**: Established: CCT7 is an essential interpretive member of the module’s established chaperonin core. Hypothesis: its reproductive-cell enrichment may contribute to the observed cross-tissue signal, but it could also reflect a broadly deployed folding program rather than reproductive specialization.

#### PSMC2

- **Related proteins** (co-abundance neighbors): RARS1 (0.84), SF3A1 (0.83); STRING partners: CCT8 (0.733)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in kidney, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 occupies a bridge position between RARS1 and SF3A1 in the module and has a STRING connection to CCT8. Its annotation identifies it as an ATPase subunit of the nineteen-S proteasome regulator, with roles in ubiquitin-dependent proteolysis and oxidative-stress response. It is also included in the supplementary ATP-hydrolysis category (STRING Function ATP hydrolysis activity; within-query FDR = 0.0249). Its literature coverage is substantial and its disease associations include plasma-cell myeloma, lymphoma, neoplasm, HIV infection, and amyloidosis.
- **Conclusion**: Established: PSMC2 supplies a plausible proteasomal quality-control link adjacent to the CCT core. Hypothesis: PSMC2 may connect chaperone-assisted folding with selective removal of damaged or misfolded proteins in this module.

#### DDX6

- **Related proteins** (co-abundance neighbors): GMPS (0.81), EPS15L1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytoplasmic bodies; IHC detected in kidney, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 6. This gene encodes a member of the DEAD box protein family. The protein is an RNA helicase found in P-bodies and stress granules, and functions in translation suppression and mRNA degradation. It is required for microRNA-induced gene silencing. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: intellectual developmental disorder with impaired language and dysmorphic facies (0.650); Intellectual disability (0.555); neurodegenerative disease (0.459); lung carcinoma (0.371); Global developmental delay (0.371)
- **Europe PMC papers**: 3002
- **Why important**: DDX6 connects GMPS with EPS15L1 in the module and contributes to the supplementary ATP-hydrolysis category (STRING Function ATP hydrolysis activity; within-query FDR = 0.0249). Its supplied annotation places it in P-bodies and stress granules, where it supports mRNA decapping, deadenylation-dependent decay, translation suppression, microRNA-mediated silencing, and spermatogenesis. It has broad literature coverage and disease associations involving intellectual disability, neurodegeneration, lung carcinoma, and developmental delay.
- **Conclusion**: Established: DDX6 represents an RNA-regulatory and translational-control component rather than a demonstrated member of the CCT complex. Hypothesis: DDX6 may couple cellular stress or translational suppression to the proteostasis program represented by the CCT core.

#### GMPS

- **Related proteins** (co-abundance neighbors): SF3A1 (0.87), DDX6 (0.81); STRING partners: RARS1 (0.872)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: guanosine monophosphate synthase. In the de novo synthesis of purine nucleotides, IMP is the branch point metabolite at which point the pathway diverges to the synthesis of either guanine or adenine nucleotides. In the guanine nucleotide pathway, there are 2 enzymes involved in converting IMP to GMP, namely IMP dehydrogenase (IMPD1), which catalyzes the oxidation of IMP to XMP, and GMP synthetase, which catalyzes the amination of …
- **Diseases (Open Targets)**: rheumatoid arthritis (0.277); nephrotic syndrome (0.259); lupus nephritis (0.259); rhabdomyosarcoma (0.247); hepatocellular carcinoma (0.237)
- **Europe PMC papers**: 5161
- **Why important**: GMPS is a network connector between SF3A1 and DDX6 and has a STRING association with RARS1. Its established biochemical role is GMP production within de novo purine biosynthesis, providing a direct link to nucleotide metabolism. It is tissue-enhanced in testis and cell-type enhanced in early and late spermatogenic populations. It has the largest literature volume among the module genes in the supplied evidence and disease associations including rheumatoid arthritis, nephrotic syndrome, lupus nephritis, rhabdomyosarcoma, and hepatocellular carcinoma.
- **Conclusion**: Established: GMPS contributes a nucleotide-biosynthetic branch and is the clearest tissue-enhanced gene in the module. Hypothesis: its association with RNA-processing and translation-related genes may reflect coordinated nucleotide and macromolecule production, or may partly reflect shared spermatogenic-cell composition.

## Module 4

**Tissue pair**: kidney and myometrium  
**Genes (8)**: HDGF, NIBAN2, PAK2, SEPTIN9, YARS1, CCT5, TRIM25, NAE1

### Function

This module does not support a single statistically established GO or KEGG function, because no GO or KEGG term passed global correction. Its structure instead suggests a loosely connected combination of intracellular protein homeostasis, cytoskeletal signaling, cell-cycle or proliferation control, transcriptional regulation, and stress or innate-immune responses. CCT5 is a network hub associated with the CCT protein-folding machinery; PAK2 links signaling to cytoskeletal reorganization; SEPTIN9 is associated with cytokinesis and cytoskeletal organization; HDGF has mitogenic and transcription-related functions; TRIM25 contributes to RNA sensing, ubiquitination, and antiviral innate immunity; YARS1 supports protein translation and can have cytokine activity in a processed form; NIBAN2 and NAE1 provide additional links to transcriptional, apoptotic, cell-cycle, and neddylation biology. These annotations are functional context rather than evidence of significant enrichment for the module as a whole.

**Cell composition.** The module is not predominantly composed of secreted or plasma proteins: only HDGF is annotated as secreted to blood, while the other members are intracellular or membrane-associated. The HPA profile shows broadly distributed tissue expression for most genes, with NIBAN2 tissue-enhanced in esophagus. Several genes have cell-type-enhanced or cell-type-enriched patterns involving neutrophils, erythrocyte progenitors, megakaryocytes, monocytes, urothelial cells, reproductive-lineage cells, and esophageal apical cells. TRIM25 has immune-cell-enhanced expression in neutrophils, and NIBAN2 has immune-cell-enhanced expression in classical monocytes. Therefore, the shared kidney–myometrium signal could partly reflect common cell populations, immune or blood-related contributions, or broadly expressed cellular programs rather than a tissue-specific kidney–myometrium mechanism. Protein detection is complete in kidney but more variable in myometrium, so transcript co-abundance should not automatically be interpreted as uniform protein-level activity.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship was present among the module genes, and no hu.MAP complex contained multiple module members. Thus, the observed co-abundance links are not supported here by the queried STRING physical or functional network and are not explained by a known hu.MAP complex. This does not disprove biological coordination: co-abundance can arise from shared regulation, cell composition, tissue state, or indirect pathway relationships. It does mean that the module should be treated as a data-derived association pattern rather than a validated protein-interaction complex.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a new co-abundance observation, but it cannot be claimed as a newly discovered biological pathway. The absence of STRING and hu.MAP support reduces evidence that this exact gene combination is an already recognized interaction module. However, each component has established biology and substantial literature, and several pairwise functional connections are plausible from known gene roles even though they were not recovered by the specified databases. The lack of globally significant GO or KEGG enrichment further argues against presenting the module as a previously defined canonical pathway. Independent replication, cell-composition adjustment, tissue-specific validation, and protein-level testing would be needed before calling it a novel conserved mechanism.

**Hypothesis.** Hypothesis: the conserved co-abundance pattern reflects a shared cellular stress-and-remodeling state present in kidney and myometrium. In this model, CCT5 supports folding of proteins required for cellular structure and signaling; PAK2 and SEPTIN9 coordinate cytoskeletal remodeling and cell behavior; HDGF and NIBAN2 influence transcription, proliferation, or survival; NAE1 contributes to neddylation and cell-cycle control; YARS1 reflects translational capacity and possibly stress signaling; and TRIM25 contributes an innate-immune or antiviral response. The apparent conservation may be generated by a common mixture of resident structural cells and low-level blood or immune-cell contributions rather than by direct physical interaction among all module proteins. This is a hypothesis, not an established causal mechanism.

### Important genes

#### CCT5

- **Related proteins** (co-abundance neighbors): YARS1 (0.86), PAK2 (0.82), HDGF (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 has the strongest network position in the module and connects to YARS1, PAK2, and HDGF. It is a subunit of the CCT or TRiC chaperonin complex, which folds actin, tubulin, and other proteins. Its protein-folding role provides a plausible upstream support function for the signaling and cytoskeletal proteins represented in the module. It also has extensive literature and disease associations involving hereditary sensory and autonomic neuropathy and neurodegenerative disease.
- **Conclusion**: Established evidence supports CCT5 as a broadly expressed intracellular chaperone subunit and as a central co-abundance connector. It is reasonable to hypothesize that CCT5 marks proteostasis demand in the shared module, but the fact sheet does not establish that CCT5 drives the other genes or that the complete CCT complex is enriched in these tissues.

#### HDGF

- **Related proteins** (co-abundance neighbors): NAE1 (0.81), SEPTIN9 (0.81), CCT5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparin binding growth factor. This gene encodes a member of the hepatoma-derived growth factor family. The encoded protein has mitogenic and DNA-binding activity and may play a role in cellular proliferation and differentiation. High levels of expression of this gene enhance the growth of many tumors. This gene was thought initially to be located on chromosome X; however, that location has been determined to correspond to a re…
- **Diseases (Open Targets)**: prostate carcinoma (0.394); neurodegenerative disease (0.287); hepatocellular carcinoma (0.115); neoplasm (0.112); non-small cell lung carcinoma (0.111)
- **Europe PMC papers**: 2439
- **Why important**: HDGF is one of the most connected genes and links NAE1, SEPTIN9, and CCT5. It has documented mitogenic, DNA-binding, chromatin-remodeling, transcriptional, and cell-division-related functions, and it is detected in both kidney and myometrium. Its annotation as secreted to blood also makes it relevant to the possibility that part of the shared signal has an extracellular or blood-associated component. HDGF has substantial literature and disease associations involving cancer and neurodegenerative disease.
- **Conclusion**: Established evidence supports HDGF as a growth- and transcription-associated protein with both intracellular localization and blood secretion annotation. Its network position makes it an important integrator candidate, but the module does not demonstrate that HDGF mediates tissue remodeling or acts as a circulating driver here.

#### PAK2

- **Related proteins** (co-abundance neighbors): CCT5 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: p21 (RAC1) activated kinase 2. The p21 activated kinases (PAK) are critical effectors that link Rho GTPases to cytoskeleton reorganization and nuclear signaling. The PAK proteins are a family of serine/threonine kinases that serve as targets for the small GTP binding proteins, CDC42 and RAC1, and have been implicated in a wide range of biological activities. The protein encoded by this gene is activated by proteolytic cleavage …
- **Diseases (Open Targets)**: Knobloch syndrome 2 (0.525); Knobloch syndrome (0.454); HIV infectious disease (0.370); atrial fibrillation (0.210); ovarian carcinoma (0.175)
- **Europe PMC papers**: 3704
- **Why important**: PAK2 is connected to the CCT5 hub and is a serine/threonine kinase that links RAC1 and CDC42 signaling to cytoskeletal reorganization and nuclear signaling. It is also associated with cell migration, phosphorylation, stress responses, and apoptosis. Its functional position makes it a plausible bridge between protein homeostasis and tissue-cell structural behavior, and it has a substantial literature base.
- **Conclusion**: Established evidence supports PAK2 as a regulator of Rho-family GTPase-dependent signaling, cytoskeletal organization, migration, and apoptosis. The module supports its consideration as a signaling component, but does not establish a specific PAK2-dependent mechanism in kidney or myometrium.

#### TRIM25

- **Related proteins** (co-abundance neighbors): SEPTIN9 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tripartite motif containing 25. The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein is an RNA binding protein, functions as a ubiquitin E3 ligase and is involved in multiple cellular processes, including regulation of antiviral innate immunity. [provided by RefSeq, S…
- **Diseases (Open Targets)**: dengue disease (0.463); COVID-19 (0.376); severe acute respiratory syndrome (0.372); neoplasm (0.108); hepatocellular carcinoma (0.106)
- **Europe PMC papers**: 4363
- **Why important**: TRIM25 is a functionally distinctive member of the module. It is an RNA-binding ubiquitin E3 ligase involved in cytoplasmic pattern-recognition receptor signaling, antiviral innate immunity, protein ubiquitination, and oxidative-stress responses. Its cell-type annotation includes neutrophils and monocytes, and it has the largest literature volume among the listed genes, with disease associations involving viral infection and cancer. Although it has only a peripheral network connection through SEPTIN9, that connection may identify an immune or stress-related branch of the module.
- **Conclusion**: Established evidence supports TRIM25 as an innate-immune and ubiquitin-regulatory protein with blood-cell-related expression features. A blood or immune contribution to the module is plausible, but the fact sheet does not show that antiviral signaling is the dominant module function or that TRIM25 physically interacts with SEPTIN9.

#### SEPTIN9

- **Related proteins** (co-abundance neighbors): TRIM25 (0.88), HDGF (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in kidney, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: septin 9. This gene is a member of the septin family involved in cytokinesis and cell cycle control. This gene is a candidate for the ovarian tumor suppressor gene. Mutations in this gene cause hereditary neuralgic amyotrophy, also known as neuritis with brachial predilection. A chromosomal translocation involving this gene on chromosome 17 and the MLL gene on chromosome 11 results in acute myelomonocytic l…
- **Diseases (Open Targets)**: neuralgic amyotrophy (0.564); hypertensive disorder (0.496); cataract (0.437); essential hypertension (0.426); alcohol drinking (0.420)
- **Europe PMC papers**: 748
- **Why important**: SEPTIN9 connects TRIM25 and HDGF and is associated with cytoskeleton organization, cytokinesis, intracellular protein localization, and non-motile cilium assembly. It is detected in both kidney and myometrium and is localized to actin filaments. Its position links the possible immune or stress branch represented by TRIM25 with the growth and structural branch represented by HDGF, while its disease associations include hereditary neuralgic amyotrophy and leukemia-related biology.
- **Conclusion**: Established evidence supports SEPTIN9 as a cytoskeletal and cytokinesis-related protein. Its placement in the module is consistent with a structural-remodeling component, but the co-abundance data do not establish a direct SEPTIN9-mediated connection between innate immunity and tissue remodeling.
