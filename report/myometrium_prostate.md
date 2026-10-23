# Conserved co-abundance modules: myometrium and prostate

## Module 0

**Tissue pair**: myometrium and prostate  
**Genes (16)**: PGD, ADK, APEX1, ATXN10, DCPS, DDX39B, GOLGA7, HNRNPF, HNRNPK, PCNA, PTBP1, GART, PFAS, RBBP4, SAE1, XPO5

### Function

The module most strongly supports coordinated nuclear RNA metabolism, especially pre-mRNA splicing, RNA processing, and RNA export. PTBP1, HNRNPK, HNRNPF, and DDX39B form a coherent RNA-processing component supported by the supplementary STRING annotations for mRNA splicing and RNA binding (STRING Keyword mRNA splicing; within-query FDR = 0.0219)(STRING Keyword RNA-binding; within-query FDR = 0.0241), together with strong STRING links among these proteins. A second component connects DNA replication and repair with nucleotide production: PCNA, APEX1, RBBP4, GART, PFAS, and ADK. The PFAS–GART relationship and their shared hu.MAP complexes support a purine-biosynthetic submodule (hu.MAP huMAP3_03291.1)(hu.MAP huMAP3_00676.1). These are functional clues only: no GO or KEGG term passed global correction. The module may therefore represent coordinated expression of constitutive RNA-processing, genome-maintenance, and nucleotide-supply machinery rather than one narrowly defined pathway.

**Cell composition.** The module consists of intracellular, non-secreted proteins rather than plasma or secreted proteins. Most genes have low tissue specificity and low immune-cell specificity in HPA. Protein detection is broad in prostate and substantial in myometrium, supporting expression in both sampled tissues. Some genes show enrichment in bone marrow, liver, esophageal cells, neutrophils, erythrocyte progenitors, or other specialized cell types, particularly PGD, PCNA, PFAS, DCPS, and GOLGA7. This leaves open a contribution from shared cell populations or sample composition, but the module is not predominantly blood-cell enriched according to the overall HPA profile. Its broadly expressed nuclear and metabolic proteins also suggest that shared cellular requirements may contribute more than tissue-specific biology.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a known RNA-processing subnetwork involving PTBP1, HNRNPK, HNRNPF, and DDX39B, with supplementary annotations for mRNA splicing and RNA binding (STRING Keyword mRNA splicing; within-query FDR = 0.0219)(STRING Keyword RNA-binding; within-query FDR = 0.0241). STRING also supports APEX1 with PCNA, PCNA with RBBP4, and PFAS with GART. hu.MAP independently places PFAS and GART together in two complexes (hu.MAP huMAP3_03291.1)(hu.MAP huMAP3_00676.1), with FASN in one complex and FASN plus PTGR2 in the other. HNRNPF and HNRNPK occur together in a larger RNA-associated complex (hu.MAP huMAP3_14523.1), while APEX1 and PGD occur together in a broad complex (hu.MAP huMAP3_14442.1). These resources therefore support several established functional neighborhoods more strongly than one unified physical complex. Co-abundance edges not represented in STRING or hu.MAP may reflect shared regulation, tissue composition, indirect biology, or relationships that remain unmeasured.

**STRING interactions (score >= 0.7)**: 9 of 120 gene pairs: APEX1–PCNA (0.864); DDX39B–HNRNPF (0.736); DDX39B–HNRNPK (0.808); DDX39B–PTBP1 (0.785); GART–PFAS (0.999); HNRNPF–HNRNPK (0.971); HNRNPF–PTBP1 (0.942); HNRNPK–PTBP1 (0.997); PCNA–RBBP4 (0.714)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword mRNA splicing (FDR = 0.0219, 5 genes); Keyword Repressor (FDR = 0.0241, 4 genes); Keyword RNA-binding (FDR = 0.0241, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03291.1 (PFAS, GART; 2/3); huMAP3_00676.1 (PFAS, GART; 2/4); huMAP3_14523.1 (HNRNPF, HNRNPK; 2/33); huMAP3_14442.1 (APEX1, PGD; 2/57)

### Novelty

The module should not be described as a wholly new molecular pathway. Its principal components recapitulate established biology: hnRNP-mediated RNA processing, DDX39B-linked splicing and export, PCNA-associated genome maintenance, and the PFAS–GART purine-biosynthesis relationship. Potential novelty lies in the reproducible co-abundance of these neighborhoods across myometrium and prostate, if this cross-tissue pattern has not previously been reported. Absence of a relationship from STRING or hu.MAP does not establish novelty, because those resources emphasize supported physical associations and may not capture co-regulation. A defensible novelty claim requires independent replication, comparison with published tissue co-expression networks, and testing whether the pattern persists after controlling for cell composition and general housekeeping or proliferative signals.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular state in which active RNA processing and export are coupled to nucleotide production and genome-maintenance capacity needed for transcription, replication, and repair. PTBP1, HNRNPK, HNRNPF, and DDX39B could coordinate processing and export of transcripts, while PCNA, APEX1, RBBP4, GART, PFAS, and ADK could support DNA synthesis, repair, chromatin handling, and purine availability. The cross-tissue co-abundance may arise from common stromal or epithelial cellular programs, or from shared cell types, rather than from a myometrium–prostate-specific pathway. This is a mechanistic hypothesis, not established causal evidence.

### Important genes

#### PTBP1

- **Related proteins** (co-abundance neighbors): HNRNPK (0.88), SAE1 (0.84), PGD (0.84), GOLGA7 (0.83), ADK (0.82), ATXN10 (0.82); STRING partners: DDX39B (0.785), HNRNPF (0.942), HNRNPK (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypyrimidine tract binding protein 1. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA-binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.505); dengue disease (0.372); open-angle glaucoma (0.330); glaucoma (0.309); neoplasm (0.116)
- **Europe PMC papers**: 4849
- **Why important**: PTBP1 is the strongest network hub and connects the RNA-processing neighborhood with several genes outside the tight hnRNP cluster. Its established functions include pre-mRNA processing, alternative splicing, RNA metabolism, and regulation of RNA splicing. It is supported by all supplementary STRING annotations (STRING Keyword mRNA splicing; within-query FDR = 0.0219)(STRING Keyword Repressor; within-query FDR = 0.0241)(STRING Keyword RNA-binding; within-query FDR = 0.0241) and has extensive literature coverage and disease associations.
- **Conclusion**: Established evidence identifies PTBP1 as a broadly expressed nuclear RNA-processing regulator and the central connectivity point of the module. It is an important marker of the RNA-processing component. It is not established that PTBP1 causally drives the cross-tissue co-abundance or links RNA processing to purine metabolism; that connection remains hypothetical.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): PTBP1 (0.88), DDX39B (0.86), GOLGA7 (0.82); STRING partners: DDX39B (0.808), HNRNPF (0.971), PTBP1 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: huMAP3_14523.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is a highly connected member of the hnRNP cluster and has strong STRING relationships with PTBP1, HNRNPF, and DDX39B. Its annotations support RNA binding, mRNA splicing, RNA processing, transcriptional regulation, and negative regulation of gene expression. It also belongs to a hu.MAP RNA-associated complex (hu.MAP huMAP3_14523.1) and has substantial disease and literature support.
- **Conclusion**: Established evidence places HNRNPK at the intersection of RNA processing and transcriptional regulation within the module. Its network position and independent complex support make it a strong representative of the conserved RNA-processing program. A direct role in coordinating the metabolic genes is not demonstrated.

#### DDX39B

- **Related proteins** (co-abundance neighbors): HNRNPK (0.86); STRING partners: HNRNPF (0.736), HNRNPK (0.808), PTBP1 (0.785)
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nuclear speckles; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 39B. This gene encodes a member of the DEAD box family of RNA-dependent ATPases that mediate ATP hydrolysis during pre-mRNA splicing. The encoded protein is an essential splicing factor required for association of U2 small nuclear ribonucleoprotein with pre-mRNA, and it also plays an important role in mRNA export from the nucleus to the cytoplasm. This gene belongs to a cluster of genes localized in th…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); Alzheimer disease (0.522); Parkinson disease (0.503); lysosomal storage disease (0.503); neurodevelopmental disorder (0.413)
- **Europe PMC papers**: 1037
- **Why important**: DDX39B links spliceosomal assembly, mRNA splicing, and mRNA export. It is connected in STRING to PTBP1, HNRNPK, and HNRNPF and contributes to the supplementary mRNA-splicing and RNA-binding signals (STRING Keyword mRNA splicing; within-query FDR = 0.0219)(STRING Keyword RNA-binding; within-query FDR = 0.0241). Its nuclear-speckle localization is compatible with this role.
- **Conclusion**: Established evidence supports DDX39B as a core RNA-processing and export factor that reinforces the module interpretation. Its inclusion does not prove that the module controls transcript export in either tissue, because the data are co-abundance and interaction evidence rather than perturbation evidence.

#### PCNA

- **Related proteins** (co-abundance neighbors): XPO5 (0.90), ADK (0.88), PFAS (0.86); STRING partners: APEX1 (0.864), RBBP4 (0.714)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proliferating cell nuclear antigen. The protein encoded by this gene is found in the nucleus and is a cofactor of DNA polymerase delta. The encoded protein acts as a homotrimer and helps increase the processivity of leading strand synthesis during DNA replication. In response to DNA damage, this protein is ubiquitinated and is involved in the RAD6-dependent DNA repair pathway. Two transcript variants encoding the same protein have b…
- **Diseases (Open Targets)**: ataxia-telangiectasia-like disorder (0.497); neurodegenerative disease (0.188); neoplasm (0.118); diabetes mellitus (0.116); hepatocellular carcinoma (0.113)
- **Europe PMC papers**: 61820
- **Why important**: PCNA links the module to DNA replication and repair and connects to XPO5, ADK, and PFAS in the co-abundance network. It also has strong STRING relationships with APEX1 and RBBP4. HPA identifies tissue enhancement in bone marrow and several proliferative or progenitor-cell contexts, making PCNA informative for possible cell-state or proliferation contributions.
- **Conclusion**: Established evidence supports PCNA as a genome-maintenance and replication-associated component and as a possible bridge between the RNA-processing and metabolic neighborhoods. Its presence may indicate shared proliferative or biosynthetic demand, but the module does not establish that proliferation is its primary driver.

#### GART

- **Related proteins** (co-abundance neighbors): ADK (0.82); STRING partners: PFAS (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: huMAP3_03291.1, huMAP3_00676.1
- **Function (MyGene.info)**: phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase. The protein encoded by this gene is a trifunctional polypeptide. It has phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase activity which is required for de novo purine biosynthesis. This enzyme is highly conserved in vertebrates. Alternative splicing of this gene results in two transcript variants encoding different isoforms.…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.606); mesothelioma (0.584); malignant pleural mesothelioma (0.557); adenocarcinoma (0.486); anaplastic lung carcinoma (0.462)
- **Europe PMC papers**: 1890
- **Why important**: GART is a multifunctional enzyme in de novo purine biosynthesis and forms a strong STRING pair with PFAS. Both genes occur together in two hu.MAP complexes (hu.MAP huMAP3_03291.1)(hu.MAP huMAP3_00676.1), giving this metabolic submodule independent interaction and complex support. GART is detected in both sampled tissues and has disease associations involving several cancers.
- **Conclusion**: Established evidence supports GART as a representative of purine-production capacity within the module and supports its relationship to PFAS. It is not established that purine synthesis is coordinated with the hnRNP genes by one physical complex; that interpretation is based on co-abundance and remains provisional.

#### PGD

- **Related proteins** (co-abundance neighbors): PTBP1 (0.84), HNRNPF (0.84); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: phosphogluconate dehydrogenase. 6-phosphogluconate dehydrogenase is the second dehydrogenase in the pentose phosphate shunt. Deficiency of this enzyme is generally asymptomatic, and the inheritance of this disorder is autosomal dominant. Hemolysis results from combined deficiency of 6-phosphogluconate dehydrogenase and 6-phosphogluconolactonase suggesting a synergism of the two enzymopathies. Several transcript variants encoding…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); Abnormality of the skeletal system (0.329); autoimmune disorder of central nervous system (0.246); smoking behavior (0.245); essential hypertension (0.199)
- **Europe PMC papers**: 8652
- **Why important**: PGD contributes a distinct metabolic and cell-composition perspective. It is a pentose-phosphate-shunt enzyme involved in NADPH regeneration and is associated in HPA with bone marrow, esophageal, and multiple blood-cell contexts. Its co-abundance links to PTBP1 and HNRNPF connect it to the RNA-processing neighborhood, although STRING does not provide corresponding interactions for those links.
- **Conclusion**: Established evidence supports PGD as a pentose-phosphate and redox-associated enzyme and as the gene most suggestive of possible blood-cell or progenitor-cell contribution. Its position may reflect coordinated metabolic demand or shared cellular composition rather than direct interaction with hnRNP proteins. It is therefore important for testing whether cell mixture contributes to the module.

## Module 1

**Tissue pair**: myometrium and prostate  
**Genes (12)**: GOT2, ATP5F1A, ATP5F1B, CS, FH, IDH3A, PPA2, NDUFS2, DDOST, UQCRC1, STT3A, VDAC2

### Function

This is a mitochondrial energy-metabolism module. The strongest primary evidence is enrichment for mitochondrial matrix (GO:CC mitochondrial matrix; q_global = 0.000291), aerobic and cellular respiration (GO:BP aerobic respiration; q_global = 0.00133)(GO:BP cellular respiration; q_global = 0.00297), oxidative phosphorylation (KEGG Oxidative phosphorylation - Homo sapiens (human); q_global = 0.004), energy derivation by oxidation of organic compounds (GO:BP energy derivation by oxidation of organic compounds; q_global = 0.00761), generation of precursor metabolites and energy (GO:BP generation of precursor metabolites and energy; q_global = 0.0202), broad metabolic pathways (KEGG Metabolic pathways - Homo sapiens (human); q_global = 0.0243), and respiratory chain complex (GO:CC respiratory chain complex; q_global = 0.0428). The gene composition supports a coherent pathway spanning the tricarboxylic acid cycle, respiratory-chain electron transfer, ATP synthase, mitochondrial phosphate handling, and metabolite transport. The reactive-oxygen-species and diabetic-cardiomyopathy pathway terms (KEGG Chemical carcinogenesis - reactive oxygen species - Homo sapiens (human); q_global = 0.0181)(KEGG Diabetic cardiomyopathy - Homo sapiens (human); q_global = 0.0207) should be interpreted as pathway-context associations rather than evidence that the module specifically causes either disease. The ion-transporter term (GO:MF monoatomic ion transmembrane transporter activity; q_global = 0.03) is consistent with mitochondrial membrane and metabolite-transfer biology. Overall, the module most plausibly represents coordinated mitochondrial oxidative metabolism and ATP-generating capacity shared by myometrium and prostate.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins: HPA reports no secreted genes. It is also unlikely to be a blood-cell contamination signature, because nearly all genes have low immune-cell specificity and only IDH3A is immune-cell enhanced in plasmacytoid dendritic cells. Instead, the profile is enriched for tissue-associated and muscle-related expression, especially skeletal muscle, tongue, and heart muscle, with additional liver and choroid-plexus associations. Most proteins are detected in prostate and many are detected in myometrium, although several genes show tissue-specific detection differences between the two tissues. This pattern is compatible with a shared oxidative metabolic program in metabolically active resident cells or smooth-muscle-related cells, rather than a plasma or blood-cell artifact. The HPA results also indicate that the module is not uniformly tissue-specific, so shared cellular metabolism remains a plausible explanation.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrial matrix | 0.000291 | ATP5F1A, ATP5F1B, CS, FH, GOT2, IDH3A, NDUFS2, PPA2, VDAC2 |
| GO:BP aerobic respiration | 0.00133 | ATP5F1A, ATP5F1B, CS, FH, IDH3A, NDUFS2, UQCRC1 |
| GO:BP cellular respiration | 0.00297 | ATP5F1A, ATP5F1B, CS, FH, IDH3A, NDUFS2, UQCRC1 |
| KEGG Oxidative phosphorylation - Homo sapiens (human) | 0.004 | ATP5F1A, ATP5F1B, NDUFS2, PPA2, UQCRC1 |
| GO:BP energy derivation by oxidation of organic compounds | 0.00761 | ATP5F1A, ATP5F1B, CS, FH, IDH3A, NDUFS2, UQCRC1 |
| KEGG Chemical carcinogenesis - reactive oxygen species - Homo sapiens (human) | 0.0181 | ATP5F1A, ATP5F1B, NDUFS2, UQCRC1, VDAC2 |
| GO:BP generation of precursor metabolites and energy | 0.0202 | ATP5F1A, ATP5F1B, CS, FH, IDH3A, NDUFS2, UQCRC1 |
| KEGG Diabetic cardiomyopathy - Homo sapiens (human) | 0.0207 | ATP5F1A, ATP5F1B, NDUFS2, UQCRC1, VDAC2 |
| KEGG Metabolic pathways - Homo sapiens (human) | 0.0243 | ATP5F1A, ATP5F1B, CS, DDOST, FH, GOT2, IDH3A, NDUFS2, STT3A, UQCRC1 |
| GO:MF monoatomic ion transmembrane transporter activity | 0.03 | ATP5F1A, ATP5F1B, NDUFS2, UQCRC1, VDAC2 |
| GO:CC respiratory chain complex | 0.0428 | ATP5F1A, ATP5F1B, NDUFS2, UQCRC1 |

### STRING and hu.MAP

STRING provides strong, biologically coherent support for the module. ATP5F1A and ATP5F1B are strongly connected to one another and to respiratory and tricarboxylic-acid-cycle genes; NDUFS2 and UQCRC1 form a particularly strong respiratory-chain connection; CS connects the ATP-synthase and respiratory components with FH, GOT2, and IDH3A; and DDOST-STT3A is a distinct, well-supported oligosaccharyltransferase relationship. The STRING functional results independently support mitochondrial matrix, mitochondrion, aerobic respiration, the tricarboxylic acid cycle, respiratory electron transport, and oxidative phosphorylation (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 1.01e-05)(STRING Keyword Transit peptide; within-query FDR = 3.62e-05)(STRING Component Mitochondrial matrix; within-query FDR = 3.73e-05)(STRING RCTM The citric acid (TCA) cycle and respiratory electron transport; within-query FDR = 9.44e-05)(STRING Keyword Mitochondrion; within-query FDR = 0.00011)(STRING Process Aerobic respiration; within-query FDR = 0.00024)(STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.00071)(STRING KEGG Oxidative phosphorylation; within-query FDR = 0.0012)(STRING Component Mitochondrion; within-query FDR = 0.0045). These are supplementary confirmations, not replacements for global GO/KEGG correction. hu.MAP identifies ATP5F1A and ATP5F1B in several ATP-synthase-related complexes (hu.MAP huMAP3_08750.1)(hu.MAP huMAP3_09307.1)(hu.MAP huMAP3_11095.1), NDUFS2 and UQCRC1 in respiratory-chain complexes (hu.MAP huMAP3_14018.1)(hu.MAP huMAP3_09982.1), and VDAC2 with STT3A in a broader membrane and organelle-associated complex (hu.MAP huMAP3_09592.1). The module therefore contains recognizable fragments of established complexes, but hu.MAP captures only subsets of those complexes, not a complete novel complex.

**STRING interactions (score >= 0.7)**: 25 of 66 gene pairs: ATP5F1A–ATP5F1B (0.999); ATP5F1A–CS (0.94); ATP5F1A–FH (0.793); ATP5F1A–IDH3A (0.855); ATP5F1A–NDUFS2 (0.98); ATP5F1A–PPA2 (0.857); ATP5F1A–UQCRC1 (0.97); ATP5F1A–VDAC2 (0.715); ATP5F1B–CS (0.917); ATP5F1B–NDUFS2 (0.97); ATP5F1B–PPA2 (0.798); ATP5F1B–UQCRC1 (0.969); ATP5F1B–VDAC2 (0.758); CS–FH (0.993); CS–GOT2 (0.952); CS–IDH3A (0.925); CS–NDUFS2 (0.772); CS–UQCRC1 (0.71); DDOST–STT3A (0.999); FH–GOT2 (0.979); FH–IDH3A (0.864); GOT2–IDH3A (0.889); GOT2–NDUFS2 (0.802); GOT2–UQCRC1 (0.718); NDUFS2–UQCRC1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Mitochondrial matrix (FDR = 1.01e-05, 9 genes); Keyword Transit peptide (FDR = 3.62e-05, 9 genes); Component Mitochondrial matrix (FDR = 3.73e-05, 9 genes); RCTM The citric acid (TCA) cycle and respiratory electron transport (FDR = 9.44e-05, 7 genes); Keyword Mitochondrion (FDR = 0.00011, 10 genes); PMID (2019) A Pathogen and a Non-pathogen Spotted Fever Group Rickettsia Trigger Differential Proteome Signatures in Macrophages. (FDR = 0.00022, 8 genes); Process Aerobic respiration (FDR = 0.00024, 7 genes); COMPARTMENTS Mitochondrion (FDR = 0.00071, 10 genes); TISSUES Left ventricle (FDR = 0.001, 6 genes); PMID (2015) Evidence of Mitochondrial Dysfunction within the Complex Genetic Etiology of Schizophrenia. (FDR = 0.001, 8 genes); TISSUES Connective tissue (FDR = 0.0011, 9 genes); KEGG Oxidative phosphorylation (FDR = 0.0012, 5 genes); KEGG Metabolic pathways (FDR = 0.0014, 10 genes); TISSUES Atrium (FDR = 0.0015, 5 genes); Component Mitochondrion (FDR = 0.0045, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08750.1 (ATP5F1B, ATP5F1A; 2/12); huMAP3_09307.1 (ATP5F1B, ATP5F1A; 2/35); huMAP3_11095.1 (ATP5F1B, ATP5F1A; 2/45); huMAP3_14018.1 (NDUFS2, UQCRC1; 2/48); huMAP3_09982.1 (NDUFS2, UQCRC1; 2/49); huMAP3_09592.1 (VDAC2, STT3A; 2/95)

### Novelty

The functional interpretation is strongly established rather than novel: oxidative phosphorylation, the tricarboxylic acid cycle, respiratory-chain activity, and ATP synthase are well-known biological systems, and many of the pairwise relationships are already represented in STRING or hu.MAP. The potentially new observation is the conserved co-abundance of this particular combination across myometrium and prostate, including the joint organization of central mitochondrial metabolism with the smaller endoplasmic-reticulum glycosylation branch. However, the supplied evidence does not establish that this cross-tissue module is a new molecular mechanism. Absence of some genes from hu.MAP or absence of a recorded complex for a gene pair cannot by itself demonstrate novelty. A defensible conclusion is that the module is a potentially tissue-pair-specific network-level observation built largely from established mitochondrial biology, requiring comparison with published cross-tissue co-abundance modules and independent cohorts before being called a new finding.

**Hypothesis.** Hypothesis: in both myometrium and prostate, a shared resident-cell metabolic state coordinately increases mitochondrial substrate oxidation and respiratory-chain activity, thereby supporting ATP production and metabolite exchange. CS, FH, GOT2, and IDH3A may provide connected tricarboxylic-acid-cycle and amino-acid flux, while NDUFS2 and UQCRC1 support electron transfer and ATP5F1A with ATP5F1B supports proton-motive-force-driven ATP synthesis. PPA2 and VDAC2 may couple phosphate and metabolite handling to mitochondrial energetic and membrane functions. The DDOST-STT3A pair may reflect parallel protein-processing demand or organelle coordination rather than a core component of the oxidative-phosphorylation machinery. This hypothesis predicts that the module will track mitochondrial respiratory capacity in the relevant resident cell populations, but co-abundance alone does not establish causal regulation or physical interaction.

### Important genes

#### CS

- **Related proteins** (co-abundance neighbors): GOT2 (0.86), DDOST (0.84), FH (0.83), IDH3A (0.83), ATP5F1A (0.82), ATP5F1B (0.82), NDUFS2 (0.82); STRING partners: ATP5F1A (0.94), ATP5F1B (0.917), FH (0.993), GOT2 (0.952), IDH3A (0.925), NDUFS2 (0.772), UQCRC1 (0.71)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS is the most connected gene in the module and links ATP synthase, tricarboxylic-acid-cycle enzymes, amino-acid metabolism, and respiratory-chain components in the co-abundance graph. It is a mitochondrial matrix citrate-synthase enzyme and appears in many globally significant energy and metabolism terms (GO:CC mitochondrial matrix; q_global = 0.000291)(GO:BP aerobic respiration; q_global = 0.00133)(GO:BP cellular respiration; q_global = 0.00297)(GO:BP energy derivation by oxidation of organic compounds; q_global = 0.00761)(GO:BP generation of precursor metabolites and energy; q_global = 0.0202)(KEGG Metabolic pathways - Homo sapiens (human); q_global = 0.0243). Its extensive literature and disease associations make it a well-established marker of mitochondrial oxidative capacity rather than a speculative driver.
- **Conclusion**: Established evidence supports CS as a central metabolic anchor and a strong indicator of coordinated mitochondrial oxidative metabolism. It is reasonable to hypothesize that CS helps organize the metabolic side of the module, but the network does not prove that CS regulates the other genes.

#### ATP5F1A

- **Related proteins** (co-abundance neighbors): STT3A (0.89), ATP5F1B (0.84), DDOST (0.83), CS (0.82), FH (0.82); STRING partners: ATP5F1B (0.999), CS (0.94), FH (0.793), IDH3A (0.855), NDUFS2 (0.98), PPA2 (0.857), UQCRC1 (0.97), VDAC2 (0.715)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: huMAP3_08750.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit alpha. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, using an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic po…
- **Diseases (Open Targets)**: mitochondrial complex V (ATP synthase) deficiency, nuclear type 4A (0.655); mitochondrial proton-transporting ATP synthase complex deficiency (0.648); mitochondrial complex V (ATP synthase) deficiency, nuclear type 4B (0.532); hereditary disease (0.394); Mitochondrial encephalopathy (0.371)
- **Europe PMC papers**: 822
- **Why important**: ATP5F1A has a highly connected position and links ATP5F1B, CS, FH, NDUFS2, PPA2, UQCRC1, and VDAC2 through STRING. It is a catalytic-core subunit of mitochondrial ATP synthase and participates in every globally significant GO/KEGG term listed for this module (GO:CC mitochondrial matrix; q_global = 0.000291) through (GO:CC respiratory chain complex; q_global = 0.0428). It is also represented in several hu.MAP ATP-synthase-related complexes (hu.MAP huMAP3_08750.1)(hu.MAP huMAP3_09307.1)(hu.MAP huMAP3_11095.1) and has established mitochondrial complex disease associations.
- **Conclusion**: Established evidence identifies ATP5F1A as a core ATP-production component and a major bridge between respiratory metabolism and energy output. Its centrality makes it a useful representative of module function, while any claim that it drives the shared tissue program remains a hypothesis.

#### NDUFS2

- **Related proteins** (co-abundance neighbors): CS (0.82); STRING partners: ATP5F1A (0.98), ATP5F1B (0.97), CS (0.772), GOT2 (0.802), UQCRC1 (0.999)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_09982.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S2. The protein encoded by this gene is a core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (complex I). Mammalian mitochondrial complex I is composed of at least 43 different subunits, 7 of which are encoded by the mitochondrial genome, and the rest are the products of nuclear genes. The iron-sulfur protein fraction of complex I is made up of 7 subunits, including this g…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.758); mitochondrial complex I deficiency, nuclear type 6 (0.665); type 2 diabetes mellitus (0.608); mitochondrial disease (0.596); Parkinson disease (0.588)
- **Europe PMC papers**: 1723
- **Why important**: NDUFS2 is a core subunit of mitochondrial complex I and is present across the primary respiration, oxidative-phosphorylation, respiratory-chain, and metabolic terms (GO:CC mitochondrial matrix; q_global = 0.000291) through (GO:CC respiratory chain complex; q_global = 0.0428). It has strong STRING relationships with ATP5F1A, ATP5F1B, UQCRC1, GOT2, and CS, and appears in respiratory-chain hu.MAP complexes (hu.MAP huMAP3_14018.1)(hu.MAP huMAP3_09982.1). Its disease associations include complex-I deficiency and Parkinson disease, giving it both mechanistic and clinical relevance.
- **Conclusion**: Established evidence supports NDUFS2 as the complex-I and electron-entry representative of the module. The module may reflect coordinated control of electron transport and ATP synthesis, but the co-abundance data do not establish whether NDUFS2 is limiting, regulated, or causative.

#### UQCRC1

- **Related proteins** (co-abundance neighbors): ATP5F1B (0.84), VDAC2 (0.82), STT3A (0.82); STRING partners: ATP5F1A (0.97), ATP5F1B (0.969), CS (0.71), GOT2 (0.718), NDUFS2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_09982.1
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase core protein 1. Enables ubiquitin protein ligase binding activity. Predicted to be involved in oxidative phosphorylation. Predicted to act upstream of or within mitochondrial electron transport, ubiquinol to cytochrome c. Located in mitochondrion. Implicated in Alzheimer's disease. Biomarker of Alzheimer's disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: parkinsonism with polyneuropathy (0.642); neurodegenerative disease (0.569); Parkinson disease (0.521); Alzheimer disease (0.519); lysosomal storage disease (0.498)
- **Europe PMC papers**: 1860
- **Why important**: UQCRC1 connects ATP synthase, NDUFS2, VDAC2, CS, and GOT2 in STRING and is included in the primary respiration, oxidative-phosphorylation, respiratory-chain, and metabolic terms (GO:BP aerobic respiration; q_global = 0.00133)(GO:BP cellular respiration; q_global = 0.00297)(KEGG Oxidative phosphorylation - Homo sapiens (human); q_global = 0.004)(GO:BP energy derivation by oxidation of organic compounds; q_global = 0.00761)(KEGG Chemical carcinogenesis - reactive oxygen species - Homo sapiens (human); q_global = 0.0181)(GO:BP generation of precursor metabolites and energy; q_global = 0.0202)(KEGG Diabetic cardiomyopathy - Homo sapiens (human); q_global = 0.0207)(KEGG Metabolic pathways - Homo sapiens (human); q_global = 0.0243)(GO:MF monoatomic ion transmembrane transporter activity; q_global = 0.03)(GO:CC respiratory chain complex; q_global = 0.0428). It is a core protein associated with electron transfer from ubiquinol to cytochrome c and is represented in hu.MAP respiratory-chain complexes (hu.MAP huMAP3_14018.1)(hu.MAP huMAP3_09982.1). Its substantial literature and neurodegenerative-disease associations reinforce its importance.
- **Conclusion**: Established evidence supports UQCRC1 as a respiratory-chain connector that helps join electron transport with the broader mitochondrial module. Its position suggests a useful interface gene, but a specific regulatory role in the myometrium–prostate conservation is not demonstrated.

#### FH

- **Related proteins** (co-abundance neighbors): CS (0.83), ATP5F1A (0.82); STRING partners: ATP5F1A (0.793), CS (0.993), GOT2 (0.979), IDH3A (0.864)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fumarate hydratase. The protein encoded by this gene is an enzymatic component of the tricarboxylic acid (TCA) cycle, or Krebs cycle, and catalyzes the formation of L-malate from fumarate. It exists in both a cytosolic form and an N-terminal extended form, differing only in the translation start site used. The N-terminal extended form is targeted to the mitochondrion, where the removal of the extension generates the …
- **Diseases (Open Targets)**: hereditary leiomyomatosis and renal cell cancer (0.838); fumaric aciduria (0.820); hereditary neoplastic syndrome (0.580); Multiple cutaneous leiomyomas (0.575); neurodegenerative disease (0.482)
- **Europe PMC papers**: 42469
- **Why important**: FH is a tricarboxylic-acid-cycle enzyme with a strong connection to CS and additional STRING relationships with GOT2 and IDH3A. It appears in the mitochondrial-matrix and energy-related primary terms (GO:CC mitochondrial matrix; q_global = 0.000291)(GO:BP aerobic respiration; q_global = 0.00133)(GO:BP cellular respiration; q_global = 0.00297)(GO:BP energy derivation by oxidation of organic compounds; q_global = 0.00761)(GO:BP generation of precursor metabolites and energy; q_global = 0.0202)(KEGG Metabolic pathways - Homo sapiens (human); q_global = 0.0243). It has extensive literature and well-established associations with hereditary leiomyomatosis and renal cell cancer, fumaric aciduria, and hereditary neoplastic syndromes, making it especially relevant to muscle and tumor biology.
- **Conclusion**: Established evidence supports FH as a metabolic-flux component whose inclusion strengthens the interpretation of the module as a coordinated tricarboxylic-acid-cycle and respiratory program. Its disease links make it biologically important, but they do not show that this module is pathogenic in either tissue.

## Module 2

**Tissue pair**: myometrium and prostate  
**Genes (5)**: ACLY, IDE, USP5, USO1, XPO7

### Function

The module does not support a single statistically established pathway assignment: no GO/KEGG term passed global correction, and STRING functional enrichment was absent. Its gene-level annotations instead suggest a coordinated intracellular maintenance program combining vesicle and Golgi trafficking through USO1, nucleocytoplasmic transport through XPO7, ubiquitin-chain disassembly and protein-stability control through USP5, peptide proteolysis and insulin-related signaling through IDE, and cytosolic acetyl-CoA, fatty-acid and cholesterol biosynthesis through ACLY. The co-abundance structure is a connected chain-like network linking USO1 with XPO7 and IDE, and linking XPO7 with USP5 and IDE with ACLY. This supports a broad relationship between intracellular transport, protein turnover, peptide handling and metabolic state rather than a narrowly defined canonical pathway.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only IDE has a secretome annotation, and it is described as secreted in other tissues. All genes have low immune-cell specificity, with no enriched blood-cell category, so the module does not resemble a blood-cell contamination signature on the available HPA evidence. Most genes have low tissue specificity, while USO1 is tissue enhanced in skeletal muscle and cell-type enhanced in myonuclei; USP5 is cell-type enhanced in late primary spermatocytes and syncytiotrophoblasts, and ACLY is cell-type enhanced in pancreatic islet cells. These scattered cell-type associations do not define a shared myometrium–prostate cell type. Protein detection is asymmetric between tissues: USO1 and IDE are detected in myometrium, whereas USO1, XPO7, USP5 and ACLY are detected in prostate. Thus the module may reflect a shared intracellular state or differences in tissue composition, but the HPA summary does not support a dominant blood or secreted-protein explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair reached the stated high-confidence STRING interaction threshold, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. Therefore the observed co-abundance links should not be interpreted as established direct protein–protein interactions or as membership in a known multiprotein complex. The network may capture coordinated expression, indirect regulation, shared cellular state, or tissue-composition effects. The absence of STRING and hu.MAP support also means that the apparent USO1–XPO7–USP5 and USO1–IDE–ACLY chains are module-level statistical relationships rather than validated physical assemblies.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears to be a potentially novel co-abundance combination rather than a previously established molecular complex or pathway module. The case for novelty is based on the specific cross-tissue module structure together with the absence of high-confidence STRING links, the absence of a shared hu.MAP complex, and the lack of globally significant GO/KEGG enrichment. Those absences do not prove biological novelty: each component has established functions, disease associations and substantial literature, and co-abundance may arise from shared regulation or cellular context. The strongest defensible conclusion is that the integrated module-level relationship is not already explained by the interaction and complex resources examined, but it requires independent replication and perturbation to establish novelty.

**Hypothesis.** Hypothesis: in both myometrium and prostate, a shared intracellular resource state may coordinate secretory-pathway trafficking, nuclear transport, ubiquitin-system maintenance, peptide degradation and cytosolic carbon allocation. USO1 could couple secretory-pathway organization with the abundance of transport-related proteins; XPO7 could influence nuclear–cytoplasmic distribution; USP5 could regulate the stability of selected proteins; IDE could alter peptide signaling; and ACLY could connect nutrient or citrate availability to lipid and cholesterol biosynthesis. The co-abundance pattern may therefore reflect coordinated adaptation to cellular trafficking, proteostasis and metabolic demand rather than a direct physical complex. This is a hypothesis, not an established mechanism, and should be tested by replication across cohorts, cell-type-aware analysis and perturbation of the candidate genes.

Web sources: https://www.broadinstitute.org/publications/broad1373766

### Important genes

#### USO1

- **Related proteins** (co-abundance neighbors): XPO7 (0.85), IDE (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: USO1 vesicle transport factor. The protein encoded by this gene is a peripheral membrane protein which recycles between the cytosol and the Golgi apparatus during interphase. It is regulated by phosphorylation: dephosphorylated protein associates with the Golgi membrane and dissociates from the membrane upon phosphorylation. Ras-associated protein 1 recruits this protein to coat protein complex II (COPII) vesicles during buddin…
- **Diseases (Open Targets)**: psoriatic arthritis (0.184); bipolar disorder (0.150); retinitis pigmentosa (0.085); cone dystrophy (0.076); cone-rod dystrophy (0.076)
- **Europe PMC papers**: 546
- **Why important**: USO1 is a central connector in the module, linking XPO7 and IDE, and has the highest weighted connectivity in the supplied network. Its established function is COPII-associated endoplasmic-reticulum-to-Golgi vesicle transport and Golgi vesicle fusion. HPA describes tissue enhancement in skeletal muscle and cell-type enhancement in myonuclei, while the gene has a moderate literature base and reported disease associations including psoriatic arthritis and retinal dystrophies.
- **Conclusion**: Established evidence supports USO1 as the strongest trafficking-related anchor of the module. It is a plausible organizing marker for a shared intracellular transport state, but there is no evidence here that it physically binds the other module members or drives the cross-tissue association.

#### XPO7

- **Related proteins** (co-abundance neighbors): USO1 (0.85), USP5 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exportin 7. The transport of protein and large RNAs through the nuclear pore complexes (NPC) is an energy-dependent and regulated process. The import of proteins with a nuclear localization signal (NLS) is accomplished by recognition of one or more clusters of basic amino acids by the importin-alpha/beta complex; see MIM 600685 and MIM 602738. The small GTPase RAN (MIM 601179) plays a key role in NLS-dependen…
- **Diseases (Open Targets)**: atrial fibrillation (0.474); neurodegenerative disease (0.471); substance-related disorder (0.353); Alzheimer disease (0.351); Parkinson disease (0.351)
- **Europe PMC papers**: 450
- **Why important**: XPO7 is a connector between USO1 and USP5 and is annotated for nuclear and nucleocytoplasmic transport. Its disease associations include atrial fibrillation and neurodegenerative disorders. The web literature also reports an XPO7–NPAT axis in acute myeloid leukemia, including context-dependent effects of XPO7 depletion, which provides external evidence that XPO7 can influence cellular growth and nuclear regulation. Its literature volume is substantial, although less extensive than that of IDE or ACLY in this module.
- **Conclusion**: Established evidence supports XPO7 as a transport regulator with disease-relevant nuclear functions. Its position makes it a plausible bridge between trafficking and protein-regulatory processes, but the leukemia findings cannot be assumed to apply to myometrium or prostate.

#### IDE

- **Related proteins** (co-abundance neighbors): USO1 (0.83), ACLY (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin degrading enzyme. This gene encodes a zinc metallopeptidase that degrades intracellular insulin, and thereby terminates insulins activity, as well as participating in intercellular peptide signalling by degrading diverse peptides such as glucagon, amylin, bradykinin, and kallidin. The preferential affinity of this enzyme for insulin results in insulin-mediated inhibition of the degradation of other peptides such as…
- **Diseases (Open Targets)**: diabetes mellitus (0.307); type 2 diabetes mellitus (0.287); diabetic retinopathy (0.146); diabetic eye disease (0.144); brain cancer (0.142)
- **Europe PMC papers**: 19876
- **Why important**: IDE connects USO1 with ACLY and is the most extensively studied gene in the module according to the supplied literature summary. It is a zinc metallopeptidase that degrades insulin and other peptides, participates in insulin-receptor-related biology, and has roles in proteolysis and antigen processing. Its disease associations prominently include diabetes, diabetic complications and brain cancer. HPA reports low tissue specificity, secretome annotation in other tissues, and protein detection in myometrium but not prostate.
- **Conclusion**: Established evidence supports IDE as a biologically important peptide-processing and metabolic-signaling enzyme. Its cross-tissue co-abundance with ACLY may indicate a shared metabolic state, but the tissue-asymmetric protein detection and lack of interaction evidence make a direct IDE–ACLY mechanism uncertain.

#### USP5

- **Related proteins** (co-abundance neighbors): XPO7 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin specific peptidase 5. Ubiquitin (see MIM 191339)-dependent proteolysis is a complex pathway of protein metabolism implicated in such diverse cellular functions as maintenance of chromatin structure, receptor function, and degradation of abnormal proteins. A late step of the process involves disassembly of the polyubiquitin chains on degraded proteins into ubiquitin monomers. USP5 disassembles branched polyubiquitin cha…
- **Diseases (Open Targets)**: neurodegenerative disease (0.532); neoplasm (0.116); hepatocellular carcinoma (0.110); non-small cell lung carcinoma (0.109); cancer (0.104)
- **Europe PMC papers**: 1576
- **Why important**: USP5 is the endpoint connected to XPO7 and contributes a protein-quality-control interpretation through deubiquitination, ubiquitin recycling and regulation of protein stability. It has cell-type-enhanced HPA annotations in late primary spermatocytes and syncytiotrophoblasts, and disease associations involving neurodegenerative disease and cancer. Its literature volume exceeds that of USO1 and XPO7 but is smaller than that of IDE and ACLY.
- **Conclusion**: Established evidence supports USP5 as a regulator of ubiquitin-dependent protein homeostasis. Its inclusion is consistent with a proteostasis component in the module, but neither the module data nor the interaction resources establish that XPO7 controls USP5 in these tissues.

#### ACLY

- **Related proteins** (co-abundance neighbors): IDE (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP citrate lyase. ATP citrate lyase is the primary enzyme responsible for the synthesis of cytosolic acetyl-CoA in many tissues. The enzyme is a tetramer (relative molecular weight approximately 440,000) of apparently identical subunits. It catalyzes the formation of acetyl-CoA and oxaloacetate from citrate and CoA with a concomitant hydrolysis of ATP to ADP and phosphate. The product, acetyl-CoA, serves several im…
- **Diseases (Open Targets)**: familial hypercholesterolemia (0.532); Hypercholesterolemia (0.532); atherosclerosis (0.470); inherited lipid metabolism disorder (0.467); cardiovascular disorder (0.449)
- **Europe PMC papers**: 7957
- **Why important**: ACLY is the metabolic endpoint connected to IDE and encodes the primary cytosolic source of acetyl-CoA from citrate. Its established functions include fatty-acid and cholesterol biosynthesis, and its disease associations include hypercholesterolemia, atherosclerosis and broader lipid-metabolism disorders. HPA places it in the cytosol, with cell-type enhancement in pancreatic islet cells and protein detection in prostate but not myometrium. It has an extensive literature base.
- **Conclusion**: Established evidence supports ACLY as a major link between central carbon metabolism and lipid biosynthesis. Its module relationship with IDE supports a possible shared metabolic-expression state, but it does not demonstrate coordinated enzymatic activity or a direct functional partnership.

## Module 3

**Tissue pair**: myometrium and prostate  
**Genes (11)**: HSPA5, DNM1L, GARS1, HSP90AB2P, HSP90AA1, HSPA8, REXO2, PDIA4, SEC23A, TARS1, VPS35

### Function

The best-supported function is endoplasmic-reticulum protein quality control and secretory-pathway handling. The primary evidence is global enrichment for protein processing in the endoplasmic reticulum (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0225), protein refolding (GO:BP protein refolding; q_global = 0.0454), and antigen processing and presentation (KEGG Antigen processing and presentation - Homo sapiens (human); q_global = 0.0454). The core chaperone group HSP90AA1, HSPA5, and HSPA8 supports refolding and protection of unfolded proteins, while PDIA4 supports ER disulfide-bond formation and protein folding. SEC23A adds ER-to-Golgi COPII vesicle budding and cargo transport. The remaining genes suggest connections to translation, endosomal recycling, mitochondrial organization, and RNA surveillance, but these peripheral functions are not globally enriched module functions.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module, and the HPA summary does not indicate blood-cell enrichment: the annotated genes have low immune-cell specificity and no recurrent enriched blood-cell category. Most genes have low tissue specificity, consistent with broadly distributed cellular machinery rather than a myometrium- or prostate-specific program. The module therefore could reflect a shared intracellular state or shared cell biology in the two tissues more readily than tissue-specific identity. Cell-type-enhanced signals include epididymal principal cells, trophoblast populations, and plasma cells, but these do not establish that the module is driven by those cell types in the sampled tissues. Protein detection is generally stronger in prostate than myometrium, although the module is detected in both tissues and several members are detected in both.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human) | 0.0225 | HSP90AA1, HSPA5, HSPA8, PDIA4, SEC23A |
| GO:BP protein refolding | 0.0454 | HSP90AA1, HSPA5, HSPA8 |
| KEGG Antigen processing and presentation - Homo sapiens (human) | 0.0454 | HSP90AA1, HSPA5, HSPA8 |

### STRING and hu.MAP

STRING provides a dense, high-confidence chaperone and ER-folding core: HSP90AA1 connects strongly with HSPA5 and HSPA8, and HSPA5 connects strongly with HSPA8 and PDIA4. STRING also supports the ER-processing and antigen-presentation interpretations (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0042) and (STRING KEGG Antigen processing and presentation; within-query FDR = 0.0101), but these are supplementary rather than globally corrected evidence. Additional known STRING relationships connect GARS1 with TARS1 and DNM1L with VPS35, while SEC23A has high-confidence links to VPS35, REXO2, HSP90AA1, and DNM1L in the supplied network. Thus, the module combines a well-supported chaperone/ER-folding neighborhood with more weakly integrated translation, trafficking, mitochondrial, and RNA-surveillance links. No hu.MAP complex contains at least two module members, so the module is not validated as a known hu.MAP complex. The STRING relationships support biological coherence, but they do not by themselves prove that the co-abundance pattern has a common physical complex.

**STRING interactions (score >= 0.7)**: 6 of 55 gene pairs: DNM1L–VPS35 (0.9); GARS1–TARS1 (0.909); HSP90AA1–HSPA5 (0.968); HSP90AA1–HSPA8 (0.999); HSPA5–HSPA8 (0.983); HSPA5–PDIA4 (0.99)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Protein processing in endoplasmic reticulum (FDR = 0.0042, 5 genes); KEGG Antigen processing and presentation (FDR = 0.0101, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be described as a wholly new molecular pathway: its central chaperone and ER-folding relationships are already represented in STRING, and the constituent genes have established cellular functions. At the same time, the specific co-abundance configuration shared by myometrium and prostate may be a new tissue-pair observation, because no hu.MAP complex was identified and the module combines several established interaction neighborhoods rather than corresponding to one documented complex. The supplied evidence is insufficient to establish publication-level novelty. Absence from hu.MAP or absence of a particular STRING edge is not proof of novelty; novelty would require comparison with prior tissue co-abundance studies and independent replication.

**Hypothesis.** Hypothesis: the shared module represents a conserved intracellular protein homeostasis program operating across myometrial and prostatic cells. Increased coordination of ER chaperones and PDIA4 could help fold and assemble secretory or membrane proteins, while SEC23A could route their cargo from ER to Golgi. HSP90AA1 and HSPA8 may connect this ER-centered response to cytosolic folding, and the links to VPS35, DNM1L, and REXO2 may couple protein trafficking with endosomal, mitochondrial, and RNA-quality-control processes. The antigen-presentation enrichment may reflect shared chaperone biology rather than a specific immune-cell infiltrate, given the low immune-cell specificity in HPA. This hypothesis requires validation using cell-composition data, perturbation of ER proteostasis, and independent cohorts from both tissues.

### Important genes

#### HSPA5

- **Related proteins** (co-abundance neighbors): PDIA4 (0.94), TARS1 (0.85); STRING partners: HSP90AA1 (0.968), HSPA8 (0.983), PDIA4 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is a central member of the globally supported ER-processing, protein-refolding, and antigen-presentation signals (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0225), (GO:BP protein refolding; q_global = 0.0454), (KEGG Antigen processing and presentation - Homo sapiens (human); q_global = 0.0454). It is annotated as an ER HSP70 chaperone and master regulator of ER homeostasis, connects strongly to PDIA4, HSPA8, and HSP90AA1 in STRING, and has the largest literature volume among the listed genes.
- **Conclusion**: Established evidence supports HSPA5 as a principal ER proteostasis anchor of the module. It is reasonable to hypothesize that its co-abundance marks shared folding or ER-stress capacity, but the data do not establish that HSPA5 drives the module or that pathological ER stress is present.

#### HSP90AA1

- **Related proteins** (co-abundance neighbors): HSPA8 (0.88), SEC23A (0.84), GARS1 (0.82), HSP90AB2P (0.82); STRING partners: HSPA5 (0.968), HSPA8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein 90 alpha family class A member 1. The protein encoded by this gene is an inducible molecular chaperone that functions as a homodimer. The encoded protein aids in the proper folding of specific target proteins by use of an ATPase activity that is modulated by co-chaperones. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: cancer (0.643); plasma cell myeloma (0.404); non-small cell lung carcinoma (0.394); dengue disease (0.375); Orthomyxoviridae infectious disease (0.375)
- **Europe PMC papers**: 8215
- **Why important**: HSP90AA1 is a highly connected chaperone linked to HSPA5 and HSPA8, and it is present in all primary enriched terms (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0225), (GO:BP protein refolding; q_global = 0.0454), (KEGG Antigen processing and presentation - Homo sapiens (human); q_global = 0.0454). Its annotation supports ATP-dependent folding of specific client proteins, and its extensive literature and disease associations make it a strong biological and interpretive anchor.
- **Conclusion**: Established evidence supports HSP90AA1 as the cytosolic chaperone bridge between the ER-focused core and broader protein-folding machinery. A possible interpretation is that the module coordinates client-protein handling across cellular compartments, but tissue-specific client proteins are not identified here.

#### HSPA8

- **Related proteins** (co-abundance neighbors): HSP90AA1 (0.88), PDIA4 (0.81); STRING partners: HSP90AA1 (0.999), HSPA5 (0.983)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Flagellar centriole, Annulus; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 8. This gene encodes a member of the heat shock protein 70 family, which contains both heat-inducible and constitutively expressed members. This protein belongs to the latter group, which are also referred to as heat-shock cognate proteins. It functions as a chaperone, and binds to nascent polypeptides to facilitate correct folding. It also functions as an ATPase in the disassembly of clathrin-coated…
- **Diseases (Open Targets)**: dengue disease (0.505); systemic lupus erythematosus (0.375); smoking initiation (0.199); Lennox-Gastaut syndrome (0.118); neoplasm (0.105)
- **Europe PMC papers**: 6937
- **Why important**: HSPA8 is a constitutive HSP70 chaperone present in all primary enriched terms (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0225), (GO:BP protein refolding; q_global = 0.0454), (KEGG Antigen processing and presentation - Homo sapiens (human); q_global = 0.0454). It has strong STRING relationships with HSP90AA1 and HSPA5 and is annotated in protein folding, unfolded-protein response, and clathrin-coated-vesicle disassembly. Its broad expression and substantial literature support make it important for interpreting the module as general cellular proteostasis rather than a tissue-specific marker.
- **Conclusion**: Established evidence supports HSPA8 as a constitutive folding and trafficking component of the module. Its broad cellular role favors a shared housekeeping or stress-capacity explanation, although the co-abundance data alone cannot distinguish basal activity from stress induction.

#### PDIA4

- **Related proteins** (co-abundance neighbors): HSPA5 (0.94), HSPA8 (0.81), TARS1 (0.81); STRING partners: HSPA5 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 is part of the primary ER-processing signal (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0225) and the STRING supporting signal (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0042). It is an ER protein-disulfide isomerase with multiple thioredoxin domains, supports protein folding and secretion, and connects strongly to HSPA5 and HSPA8. Its HPA cell-type signals include epididymal principal cells, trophoblast populations, hepatocytes, and plasma cells, making it relevant to secretory-cell biology while not proving a blood-cell origin.
- **Conclusion**: Established evidence supports PDIA4 as the ER oxidative-folding and secretory-pathway component of the module. A plausible hypothesis is that it helps translate chaperone coordination into maturation of disulfide-containing proteins, but the specific client proteins and direction of regulation remain unknown.

#### SEC23A

- **Related proteins** (co-abundance neighbors): VPS35 (0.90), REXO2 (0.88), HSP90AA1 (0.84), DNM1L (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A is the highest weighted-degree gene in the module and is present in the primary ER-processing term (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0225). Its annotation directly supports COPII-coated vesicle budding, cargo loading, and ER-to-Golgi transport. It links the chaperone core to VPS35, REXO2, HSP90AA1, and DNM1L in the module network and has a substantial literature base plus a documented association with craniolenticulosutural dysplasia.
- **Conclusion**: Established evidence supports SEC23A as a trafficking connector that extends the module beyond folding into secretory cargo export. It may coordinate disposal or delivery of properly folded proteins, but the network does not demonstrate that SEC23A physically binds every linked module member.

## Module 4

**Tissue pair**: myometrium and prostate  
**Genes (10)**: CACYBP, FKBP3, HNRNPH1, LYRM7, MANF, SNU13, RAN, RBM39, SCP2, CTTN

### Function

The module does not support a single statistically established GO or KEGG function because no term passed global correction. Its composition instead suggests a mixed intracellular program involving nuclear transport and cell-cycle support through RAN, RNA processing and splicing through HNRNPH1, RBM39, and SNU13, mitochondrial respiratory-chain complex III assembly through LYRM7, lipid and steroid metabolism through SCP2, protein folding and stress protection through MANF and FKBP3, and cytoskeletal or adhesion organization through CACYBP and CTTN. The co-abundance pattern therefore appears more consistent with coordination of general cellular maintenance processes than with a specific pathway. These functional interpretations are gene-level annotations, not enrichment claims.

**Cell composition.** The module is not dominated by secreted or plasma proteins: only MANF is annotated as secreted to blood, while the other genes are intracellular. The HPA profile also does not indicate a predominantly blood-cell module, because most genes have low immune-cell specificity and only a small subset shows immune-cell enhancement. Most genes are cell-type enhanced rather than broadly uniform, with recurring associations involving germ-cell populations and several epithelial or trophoblast populations. Several genes have low tissue specificity and are detected in both myometrium and prostate, which is compatible with a shared intracellular or cellular-composition signal rather than a tissue-specific secretory program. The shared module could still reflect common cell states or cell types in the two tissues, but the available HPA evidence does not support interpreting it primarily as blood contamination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and no hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not corroborated by the supplied physical or functional interaction resources. The network nevertheless contains plausible functional neighborhoods: RAN connects several genes involved in nuclear or cellular maintenance, LYRM7 is connected to SCP2 and SNU13, and CACYBP is connected to FKBP3 and CTTN. These relationships should be regarded as co-abundance structure rather than established molecular interactions. The lack of STRING and hu.MAP support weakens claims of a pre-existing protein complex but does not invalidate the module.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a previously unreported tissue-pair co-abundance pattern, but the fact sheet does not establish that it is a new biological mechanism. The genes themselves have well-described individual functions, whereas the particular combination across myometrium and prostate lacks support from the supplied STRING, hu.MAP, and enrichment results. Therefore, the cautious conclusion is that the module is a potentially novel cross-tissue co-abundance association, not a demonstrated novel pathway. Its novelty requires independent replication, assessment against published co-expression resources, and experimental or perturbational validation.

**Hypothesis.** Hypothesis: the module reflects a shared cellular maintenance state present in myometrium and prostate, in which nuclear transport and RNA processing are coordinated with mitochondrial respiratory-chain assembly, lipid or steroid handling, protein-folding protection, and cytoskeletal remodeling. RAN, HNRNPH1, RBM39, and SNU13 could represent the nuclear RNA and transport component; LYRM7 and SCP2 could represent mitochondrial and lipid-metabolic support; MANF and FKBP3 could buffer proteostatic stress; and CACYBP with CTTN could connect this state to cytoskeletal or adhesion remodeling. This is a mechanistic model derived from gene functions and network placement, not an established pathway demonstrated by enrichment or protein-interaction evidence.

### Important genes

#### RAN

- **Related proteins** (co-abundance neighbors): CACYBP (0.84), LYRM7 (0.83), HNRNPH1 (0.81), SCP2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAN, member RAS oncogene family. RAN (ras-related nuclear protein) is a small GTP binding protein belonging to the RAS superfamily that is essential for the translocation of RNA and proteins through the nuclear pore complex. The RAN protein is also involved in control of DNA synthesis and cell cycle progression. Nuclear localization of RAN requires the presence of regulator of chromosome condensation 1 (RCC1). Mutations in RAN di…
- **Diseases (Open Targets)**: HIV infectious disease (0.565); Orthomyxoviridae infectious disease (0.376); pemphigus foliaceus (0.298); neurodegenerative disease (0.270); Genu valgum (0.136)
- **Europe PMC papers**: 133080
- **Why important**: RAN has the strongest apparent network centrality in the module and links multiple otherwise separate neighborhoods. Its established functions include nuclear import and export, ribosomal subunit export, DNA synthesis, and cell-cycle progression. Its extensive literature makes it a strong anchor for interpreting the module as involving broad nuclear and proliferative maintenance rather than a specialized tissue pathway.
- **Conclusion**: Established evidence supports RAN as a central regulator of nucleocytoplasmic transport and cell-cycle-related processes. The hypothesis that it organizes the observed module is plausible from its network position, but the co-abundance data do not demonstrate direct regulation of the other module genes.

#### LYRM7

- **Related proteins** (co-abundance neighbors): SCP2 (0.86), SNU13 (0.85), RAN (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LYR motif containing 7. Inner mitochondrial membrane complex III (CIII) is the main enzyme complex in the mitochondrial respiratory chain, and Rieske Fe-S protein (UQCRFS1) is the last catalytic subunit added to the complex. The protein encoded by this gene is a nuclear-encoded mitochondrial matrix protein that stabilizes UQCRFS1 and chaperones it to the CIII complex. Defects in this gene are a cause of mitochondrial com…
- **Diseases (Open Targets)**: mitochondrial complex III deficiency (0.788); mitochondrial disease (0.371); mitochondrial complex III deficiency nuclear type 1 (0.340); psoriasis (0.317); inflammatory bowel disease (0.313)
- **Europe PMC papers**: 265
- **Why important**: LYRM7 is a highly connected member of the mitochondrial and RNA-processing neighborhood and is detected in both myometrium and prostate. It stabilizes or chaperones a component of mitochondrial respiratory-chain complex III, and its disease associations include mitochondrial complex III deficiency. Its more limited literature volume compared with RAN makes the cross-tissue co-abundance signal potentially informative.
- **Conclusion**: Established evidence supports LYRM7 as a mitochondrial complex III assembly factor. It may indicate shared respiratory or energy-management demands in the two tissues, but the module does not establish that mitochondrial activity is the dominant module function.

#### SCP2

- **Related proteins** (co-abundance neighbors): LYRM7 (0.86), MANF (0.85), RAN (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Peroxisomes; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sterol carrier protein 2. This gene encodes two proteins: sterol carrier protein X (SCPx) and sterol carrier protein 2 (SCP2), as a result of transcription initiation from 2 independently regulated promoters. The transcript initiated from the proximal promoter encodes the longer SCPx protein, and the transcript initiated from the distal promoter encodes the shorter SCP2 protein, with the 2 proteins sharing a common C-termi…
- **Diseases (Open Targets)**: sterol carrier protein 2 deficiency (0.708); spermatogenic failure (0.191); stroke disorder (0.187); alcohol drinking (0.186); leukodystrophy (0.119)
- **Europe PMC papers**: 2268
- **Why important**: SCP2 occupies a connecting position between LYRM7, MANF, and RAN and is detected in both tissues. It encodes sterol-carrier proteins involved in peroxisomal lipid handling, fatty-acid oxidation, steroid biosynthesis, and bile-acid metabolism. Its disease association with sterol carrier protein deficiency and its substantial literature support make it an important metabolic representative of the module.
- **Conclusion**: Established evidence supports SCP2 in lipid, sterol, and peroxisomal metabolism. A contribution to shared steroid or lipid handling in myometrium and prostate is a reasonable hypothesis, but tissue-level metabolic flux is not established by this module.

#### HNRNPH1

- **Related proteins** (co-abundance neighbors): RBM39 (0.88), RAN (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein H1. This gene encodes a member of a subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins that complex with heterogeneous nuclear RNA. These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the n…
- **Diseases (Open Targets)**: neurodevelopmental disorder with craniofacial dysmorphism and skeletal defects (0.668); dengue disease (0.462); hereditary disease (0.411); neurodevelopmental disorder (0.400); syndromic intellectual disability (0.370)
- **Europe PMC papers**: 1509
- **Why important**: HNRNPH1 connects to RAN and RBM39 and represents a nuclear RNA-processing branch of the module. It is a broadly expressed RNA-binding protein involved in pre-mRNA processing and splicing, is detected in both tissues, and has substantial literature coverage. Its presence alongside RBM39 and SNU13 gives the module a coherent gene-expression and RNA-maturation dimension even though no enrichment term passed global correction.
- **Conclusion**: Established evidence supports HNRNPH1 as an RNA-processing and splicing factor. It may mark coordinated post-transcriptional regulation in the shared cellular state, but the data do not identify which transcripts or splicing events are involved.

#### CACYBP

- **Related proteins** (co-abundance neighbors): FKBP3 (0.85), CTTN (0.85), RAN (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcyclin binding protein. The protein encoded by this gene is a calcyclin binding protein. It may be involved in calcium-dependent ubiquitination and subsequent proteosomal degradation of target proteins. It probably serves as a molecular bridge in ubiquitin E3 complexes and participates in the ubiquitin-mediated degradation of beta-catenin. Two alternatively spliced transcript variants encoding different isoforms have bee…
- **Diseases (Open Targets)**: esophageal disorder (0.358); gastroesophageal reflux disease (0.291); Abnormality of the skeletal system (0.262); mood disorder (0.202); major depressive disorder (0.202)
- **Europe PMC papers**: 835
- **Why important**: CACYBP links RAN to FKBP3 and CTTN, placing it at the intersection of protein turnover, calcium-responsive biology, and cytoskeletal organization. It can participate in ubiquitin-related degradation and beta-catenin regulation, and its annotations include calcium response and cell differentiation. Its intermediate literature volume and bridging network position make it useful for connecting the nuclear-maintenance interpretation to structural and proteostatic processes.
- **Conclusion**: Established evidence supports CACYBP as a protein-interaction and degradation-associated factor with links to calcium-responsive and developmental processes. Its role as a mediator of the proposed module-wide state remains hypothetical because neither the interaction resources nor enrichment analysis confirms it.

## Module 5

**Tissue pair**: myometrium and prostate  
**Genes (5)**: DDX6, EIF4G1, MAT2A, MYG1, RBM12

### Function

The module most plausibly represents coordinated regulation of RNA fate and cellular gene expression. DDX6 contributes mRNA decay, decapping, translation suppression, microRNA-mediated silencing, and P-body assembly. EIF4G1 contributes cap-dependent translation initiation. RBM12 contributes RNA-splicing regulation, while MYG1 contributes mitochondrial RNA metabolism, rRNA processing, and mRNA processing. MAT2A contributes S-adenosylmethionine production, linking the module to cellular methyl-donor metabolism. No GO or KEGG term passed global correction, so these gene-level annotations are functional context rather than globally significant enrichment. There is also no supplementary STRING functional-enrichment result.

**Cell composition.** The module is not composed of plasma proteins, secreted proteins, or blood-cell-enriched proteins. All members are intracellular and non-secreted, and all have low immune-cell specificity. Most members also have low tissue specificity, consistent with broadly used cellular machinery rather than a strongly restricted tissue program. HPA detects protein in both queried tissues for most members. MAT2A is tissue-enhanced in pancreas and cell-type-enhanced in smooth muscle but is not detected by HPA in the queried tissues. These observations argue against a simple blood-contamination explanation and are more compatible with shared intracellular biology or shared cell-state composition.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only reported high-confidence STRING relationship is DDX6–EIF4G1. This connects an RNA-decay and translation-suppression factor with a translation-initiation scaffold. The remaining module edges lack reported high-confidence STRING support, and no hu.MAP complex contains multiple module members. Thus, one part of the module recapitulates a known molecular relationship, while the other co-abundance links may reflect indirect regulation, shared expression control, cellular state, or relationships absent from these databases. The module is not established as one physical multiprotein complex.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: DDX6–EIF4G1 (0.857)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The specific conserved co-abundance pattern across myometrium and prostate is a candidate context-specific finding, but it cannot be called a wholly new molecular mechanism. The DDX6–EIF4G1 relationship is already known, and the individual functions of the genes are established to varying degrees. The supplied STRING and hu.MAP results do not validate the full combination as a known complex or pathway. However, absence from those resources alone does not prove novelty. Independent replication and perturbation experiments are needed.

**Hypothesis.** Hypothesis: a shared cellular state in myometrium and prostate coordinates DDX6-linked mRNA repression or decay, EIF4G1-linked translation initiation, RBM12-linked RNA processing, and MYG1-linked mitochondrial or ribosomal RNA metabolism, while MAT2A-linked methyl-donor availability modulates the broader gene-expression state. The genes may therefore co-abundance without forming one physical complex. This predicts coordinated changes in RNA stability, translation, RNA processing, and methylation-sensitive cellular programs, but the prediction is not established by the fact sheet.

### Important genes

#### DDX6

- **Related proteins** (co-abundance neighbors): EIF4G1 (0.87), MYG1 (0.84), MAT2A (0.84); STRING partners: EIF4G1 (0.857)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytoplasmic bodies; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 6. This gene encodes a member of the DEAD box protein family. The protein is an RNA helicase found in P-bodies and stress granules, and functions in translation suppression and mRNA degradation. It is required for microRNA-induced gene silencing. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: intellectual developmental disorder with impaired language and dysmorphic facies (0.650); Intellectual disability (0.555); neurodegenerative disease (0.459); lung carcinoma (0.371); Global developmental delay (0.371)
- **Europe PMC papers**: 3002
- **Why important**: DDX6 has the most central network position, connecting EIF4G1, MYG1, and MAT2A. Its established roles in P-body assembly, mRNA decay, decapping, translation suppression, and microRNA-mediated silencing make it the clearest integrator of the module. It is also the member participating in the reported high-confidence STRING relationship and has substantial literature and disease-association evidence.
- **Conclusion**: Established evidence supports DDX6 as a central RNA-regulatory factor and as a known partner of EIF4G1. It is a strong candidate organizing gene, but co-abundance and network position do not establish that DDX6 drives the conserved tissue-pair pattern.

#### EIF4G1

- **Related proteins** (co-abundance neighbors): DDX6 (0.87), RBM12 (0.85); STRING partners: DDX6 (0.857)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 connects DDX6 and RBM12, placing translation initiation between RNA turnover and RNA processing. Its established role as an EIF4F scaffold gives the module a translational axis. It also has substantial literature and disease-association evidence.
- **Conclusion**: Established evidence supports EIF4G1 as a translation-initiation scaffold and confirms its high-confidence relationship with DDX6. Coordinated translation and mRNA turnover are plausible interpretations, but a specific functional change in the shared tissue state remains unproven.

#### MAT2A

- **Related proteins** (co-abundance neighbors): DDX6 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionine adenosyltransferase 2A. The protein encoded by this gene catalyzes the production of S-adenosylmethionine (AdoMet) from methionine and ATP. AdoMet is the key methyl donor in cellular processes. [provided by RefSeq, Jun 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.545); familial thoracic aortic aneurysm and aortic dissection (0.416); autoimmune disorder of central nervous system (0.340); prostate carcinoma (0.252); Abnormality of the cardiovascular system (0.192)
- **Europe PMC papers**: 2615
- **Why important**: MAT2A connects to DDX6 and contributes a metabolic dimension through S-adenosylmethionine production. Its annotations include methionine response and TORC1 regulation. It is cell-type-enhanced in smooth muscle and has supplied disease-association evidence involving prostate carcinoma, although HPA does not detect it in the queried tissues.
- **Conclusion**: Established evidence supports MAT2A as a methyl-donor biosynthesis enzyme linked to nutrient and growth signaling. A connection between metabolic state and RNA or translation control is a hypothesis, not demonstrated module function. The HPA detection discrepancy warrants validation.

#### MYG1

- **Related proteins** (co-abundance neighbors): DDX6 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MYG1 exonuclease. Predicted to enable nuclease activity. Predicted to be involved in nucleic acid phosphodiester bond hydrolysis. Predicted to act upstream of or within locomotory exploration behavior. Located in mitochondrion and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: triple-A syndrome (0.333); vitiligo (0.090); lung adenocarcinoma (0.074); breast carcinoma (0.037); breast cancer (0.037)
- **Europe PMC papers**: 183
- **Why important**: MYG1 connects to DDX6 and contributes mitochondrial RNA metabolism, rRNA processing, and mRNA processing annotations. Its low tissue specificity suggests broadly used nucleic-acid-processing biology rather than a tissue-exclusive function. Its more limited literature base makes it useful for testing whether the module represents a novel regulatory association.
- **Conclusion**: Established evidence supports MYG1 as a nucleic-acid-processing factor. A role linking RNA surveillance or processing to DDX6-centered regulation is plausible, but the relationship lacks independent high-confidence STRING or complex support and remains hypothetical.

## Module 6

**Tissue pair**: myometrium and prostate  
**Genes (12)**: GMPS, PAK2, PSMC4, PSMC2, PSMD13, SF3A1, KARS1, RARS1, CCT3, CCT7, CCT8, THOP1

### Function

The module is best interpreted as a conserved intracellular proteostasis and biosynthetic-support module. The strongest primary evidence is enrichment for intracellular protein-containing complexes (GO:CC intracellular protein-containing complex; q_global = 0.00116), ATP and adenyl-ribonucleotide binding (GO:MF ATP binding; q_global = 0.00699), (GO:MF adenyl ribonucleotide binding; q_global = 0.00732), (GO:MF adenyl nucleotide binding; q_global = 0.0275), the chaperonin-containing T-complex (GO:CC chaperonin-containing T-complex; q_global = 0.0106), and the proteasome regulatory and accessory complexes (GO:CC proteasome regulatory particle; q_global = 0.0216), (GO:CC proteasome accessory complex; q_global = 0.0216). The CCT3-CCT7-CCT8 component supports ATP-dependent folding of newly synthesized proteins, while PSMC2, PSMC4 and PSMD13 support ubiquitin-dependent proteasomal processing. GMPS contributes purine nucleotide biosynthesis, and KARS1 and RARS1 contribute aminoacyl-tRNA charging. The CCT-associated telomerase, Cajal-body, sperm-recognition and DNA-biosynthesis annotations (7 globally significant GO/KEGG terms, q_global 0.0106–0.0106; see the table), (GO:BP binding of sperm to zona pellucida; q_global = 0.0216), (6 globally significant GO/KEGG terms, q_global 0.0216–0.0216; see the table), (4 globally significant GO/KEGG terms, q_global 0.0369–0.0369; see the table) should be treated cautiously: they are driven by the same CCT genes and do not by themselves demonstrate that these processes are active in myometrium or prostate. Overall, the most defensible interpretation is coordinated protein folding, protein quality control, translation support and nucleotide metabolism, rather than a tissue-specific signaling pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a limited secretome signal, and the listed proteins are predominantly intracellular. It is also not blood-cell enriched by HPA, because all module genes have low immune-cell specificity and no enriched blood-cell category is reported. Most genes have low tissue specificity, consistent with broadly expressed housekeeping or core cellular machinery. At the same time, many genes show cell-type-enhanced expression in germ-cell populations, especially spermatids and primary spermatocytes, with additional signals in syncytiotrophoblasts and neutrophils. This creates a plausible cell-composition or shared-cell-state contribution, although the HPA evidence does not establish that the myometrium-prostate module is caused by blood contamination. Protein detection is generally stronger in prostate than in myometrium for several members, but the module includes proteins detected in both tissues, including PSMC4, SF3A1, CCT7, PSMC2, CCT3 and KARS1.

**GO/KEGG enrichment**: 25 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC intracellular protein-containing complex | 0.00116 | CCT3, CCT7, CCT8, KARS1, PSMC2, PSMC4, PSMD13, RARS1 |
| GO:MF ATP binding | 0.00699 | CCT3, CCT7, CCT8, GMPS, KARS1, PAK2, PSMC2, PSMC4, RARS1 |
| GO:MF adenyl ribonucleotide binding | 0.00732 | CCT3, CCT7, CCT8, GMPS, KARS1, PAK2, PSMC2, PSMC4, RARS1 |
| GO:CC chaperonin-containing T-complex | 0.0106 | CCT3, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 0.0106 | CCT3, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 0.0106 | CCT3, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 0.0106 | CCT3, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 0.0106 | CCT3, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 0.0106 | CCT3, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 0.0106 | CCT3, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 0.0106 | CCT3, CCT7, CCT8 |
| GO:CC proteasome regulatory particle | 0.0216 | PSMC2, PSMC4, PSMD13 |
| GO:BP binding of sperm to zona pellucida | 0.0216 | CCT3, CCT7, CCT8 |
| GO:CC proteasome accessory complex | 0.0216 | PSMC2, PSMC4, PSMD13 |
| GO:BP positive regulation of telomere maintenance via telomerase | 0.0216 | CCT3, CCT7, CCT8 |

### STRING and hu.MAP

STRING supports several established physical or functional relationships. CCT3, CCT7 and CCT8 form a very strongly supported CCT/TRiC clique, with CCT8 also linking to PSMC2. PSMC2, PSMC4 and PSMD13 form a strongly supported proteasome-associated group. GMPS, KARS1 and RARS1 are connected through a nucleotide and aminoacyl-tRNA-synthetase-associated neighborhood, with especially strong support for the KARS1-RARS1 relationship. The STRING supplementary terms are consistent with ATP binding, ATP hydrolysis, CCT-mediated folding, proteasome-mediated regulation and antigen-processing-related degradation (15 supplementary STRING terms; within-query FDR 0.00071–0.013), but these are not global enrichment evidence. hu.MAP independently places CCT3, CCT7 and CCT8 in several CCT-containing complexes (hu.MAP huMAP3_07938.1), (hu.MAP huMAP3_06559.1), (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1), (hu.MAP huMAP3_01951.1), and places PSMC2, PSMC4 and PSMD13 in proteasome complexes (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1). RARS1 and KARS1 also recur together in aminoacyl-tRNA-synthetase complexes (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1). Thus, much of the internal structure reflects known complexes rather than previously unknown physical interactions. SF3A1, PAK2 and THOP1 have no reported high-confidence STRING partners or qualifying hu.MAP complexes in this fact sheet, so their module links are more appropriately viewed as co-abundance relationships than established direct physical interactions.

**STRING interactions (score >= 0.7)**: 10 of 66 gene pairs: CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT7–CCT8 (0.999); CCT8–PSMC2 (0.733); GMPS–KARS1 (0.835); GMPS–RARS1 (0.872); KARS1–RARS1 (0.999); PSMC2–PSMC4 (0.999); PSMC2–PSMD13 (0.999); PSMC4–PSMD13 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword ATP-binding (FDR = 0.00071, 9 genes); Function ATP binding (FDR = 0.0034, 9 genes); Pfam TCP-1/cpn60 chaperonin family (FDR = 0.0066, 3 genes); RCTM Regulation of activated PAK-2p34 by proteasome mediated degradation (FDR = 0.0069, 4 genes); Function ATP hydrolysis activity (FDR = 0.0088, 5 genes); RCTM TCR signaling (FDR = 0.0096, 4 genes); RCTM Fc epsilon receptor (FCERI) signaling (FDR = 0.0096, 4 genes); RCTM Signaling by ROBO receptors (FDR = 0.0096, 4 genes); RCTM Folding of actin by CCT/TriC (FDR = 0.0096, 3 genes); RCTM Association of TriC/CCT with target proteins during biosynthesis (FDR = 0.0096, 3 genes); RCTM C-type lectin receptors (CLRs) (FDR = 0.0096, 4 genes); RCTM MAPK6/MAPK4 signaling (FDR = 0.0096, 4 genes); RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding (FDR = 0.0096, 3 genes); RCTM Host Interactions of HIV factors (FDR = 0.0122, 4 genes); RCTM Antigen processing: Ubiquitination & Proteasome degradation (FDR = 0.013, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT3, CCT8, CCT7; 3/23); huMAP3_06559.1 (CCT3, CCT8, CCT7; 3/25); huMAP3_05064.1 (PSMC2, PSMC4, PSMD13; 3/31); huMAP3_09191.1 (CCT3, CCT8, CCT7; 3/32); huMAP3_10656.1 (CCT3, CCT8, CCT7; 3/36); huMAP3_14584.1 (CCT3, CCT8, CCT7; 3/61); huMAP3_09656.1 (PSMC2, PSMC4, PSMD13; 3/64); huMAP3_13725.1 (PSMC2, PSMC4, PSMD13; 3/69); huMAP3_01951.1 (CCT3, CCT7; 2/8); huMAP3_02637.1 (RARS1, KARS1; 2/14); huMAP3_13688.1 (RARS1, KARS1; 2/14)

### Novelty

The module should not be presented as discovery of a new CCT complex, proteasome complex, aminoacyl-tRNA-synthetase complex or molecular function, because those relationships are already represented by STRING and hu.MAP (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) (hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). Its potentially novel aspect is the coordinated co-abundance of these established intracellular systems across myometrium and prostate. However, the fact sheet alone does not establish that this tissue-pair module has not been reported previously, and absence of a relationship from STRING or hu.MAP would not prove novelty. The appropriate conclusion is therefore qualified: the module-level cross-tissue co-abundance pattern may be a new observation, whereas its main molecular components and several internal relationships are established biology.

**Hypothesis.** Hypothesis: a shared cellular state in myometrium and prostate increases demand for synthesis, folding, remodeling and selective removal of proteins, producing coordinated abundance of CCT chaperonins, proteasome components, aminoacyl-tRNA synthetases and purine-biosynthetic machinery. CCT-mediated folding may support cytoskeletal or other newly synthesized proteins, while proteasomal turnover removes damaged or regulated proteins; GMPS and the tRNA synthetases may provide nucleotide and translational capacity for this response. The germ-cell-enriched HPA pattern raises an alternative or additional hypothesis that the signal partly reflects a shared rare-cell or cell-state component rather than a universal program of smooth-muscle and prostate cells. These hypotheses require validation with cell-resolved expression, sample-level module scores, histology, and perturbation of chaperonin or proteasome activity; the co-abundance data do not establish causality.

### Important genes

#### CCT8

- **Related proteins** (co-abundance neighbors): PSMD13 (0.88), RARS1 (0.87), PSMC4 (0.87), THOP1 (0.83), CCT3 (0.82); STRING partners: CCT3 (0.999), CCT7 (0.999), PSMC2 (0.733)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 has the strongest weighted network position in the module and connects the CCT group with proteasome-, synthetase- and peptidase-associated members. It is part of the highly supported CCT3-CCT7-CCT8 complex in STRING and hu.MAP, and it contributes to the globally corrected intracellular-complex, ATP-binding, chaperonin and Cajal-body-related annotations (11 globally significant GO/KEGG terms, q_global 0.00116–0.0106; see the table), (GO:BP binding of sperm to zona pellucida; q_global = 0.0216), (11 globally significant GO/KEGG terms, q_global 0.0216–0.0369; see the table). Its established function is as a CCT chaperonin subunit involved in folding and protein stabilization. It also has extensive literature and cancer-related disease associations in the supplied resources.
- **Conclusion**: Established conclusion: CCT8 is a central marker of the module's CCT-dependent proteostasis arm. Hypothesis: its network position may make it an important coupling point between protein folding and the broader quality-control program, but the co-abundance pattern does not show that CCT8 regulates the other genes.

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT7 (0.86), CCT8 (0.82); STRING partners: CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a member of the same strongly supported CCT/TRiC complex as CCT7 and CCT8 and is connected to both of those partners in the module. It contributes to essentially the full set of CCT-driven globally corrected annotations, including intracellular complex, ATP binding, chaperonin-containing T-complex and the Cajal-body and telomerase-related terms (11 globally significant GO/KEGG terms, q_global 0.00116–0.0106; see the table), (GO:BP binding of sperm to zona pellucida; q_global = 0.0216), (11 globally significant GO/KEGG terms, q_global 0.0216–0.0369; see the table). Its established role is ATP-dependent folding of proteins such as actin and tubulin. It has the largest literature volume among the listed genes and supplied disease associations spanning neurodevelopmental, neurodegenerative and other disorders.
- **Conclusion**: Established conclusion: CCT3 is a well-supported representative of the module's core chaperonin machinery. Hypothesis: coordinated CCT3 abundance may indicate increased folding capacity or cytoskeletal-protein handling in the shared tissue state, but it does not prove a telomerase or sperm-recognition function in these tissues.

#### PSMC4

- **Related proteins** (co-abundance neighbors): PSMD13 (0.88), CCT8 (0.87), KARS1 (0.83); STRING partners: PSMC2 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 4. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.603); mantle cell lymphoma (0.542); neoplasm (0.519); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1065
- **Why important**: PSMC4 occupies a connected position between the proteasome group and other module components and has strong STRING links to PSMC2 and PSMD13. It belongs to the proteasome complexes represented by hu.MAP (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1) and contributes to the globally corrected intracellular-complex, ATP-binding and proteasome regulatory-complex annotations (GO:CC intracellular protein-containing complex; q_global = 0.00116), (GO:MF ATP binding; q_global = 0.00699), (GO:MF adenyl ribonucleotide binding; q_global = 0.00732), (GO:CC proteasome regulatory particle; q_global = 0.0216), (GO:CC proteasome accessory complex; q_global = 0.0216), (GO:MF adenyl nucleotide binding; q_global = 0.0275). Its established function is an ATPase subunit of the proteasome regulatory particle, supporting ubiquitin-dependent protein catabolism and stress-related protein quality control. It has substantial literature and disease associations involving hematologic malignancy, neoplasm and other conditions.
- **Conclusion**: Established conclusion: PSMC4 anchors the module's proteasomal degradation arm. Hypothesis: its co-abundance with CCT components may reflect coupling between folding capacity and disposal of misfolded proteins, but this coupling is not demonstrated as a direct regulatory interaction.

#### PSMD13

- **Related proteins** (co-abundance neighbors): PSMC4 (0.88), CCT8 (0.88); STRING partners: PSMC2 (0.999), PSMC4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 is tightly connected to PSMC2 and PSMC4 in STRING and is present with them in proteasome complexes (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1). It contributes to the globally corrected intracellular-complex, proteasome-regulatory-particle and proteasome-accessory-complex annotations (GO:CC intracellular protein-containing complex; q_global = 0.00116), (GO:CC proteasome regulatory particle; q_global = 0.0216), (GO:CC proteasome accessory complex; q_global = 0.0216). Its established role is as a non-ATPase component of the proteasome regulatory machinery, with functions related to ubiquitin-dependent proteolysis and oxidative-stress response. The supplied resources also associate it with malignancy, neurodegenerative disease and HIV-related disease, and provide substantial literature coverage.
- **Conclusion**: Established conclusion: PSMD13 reinforces that the proteasome signal is a genuine complex-level feature rather than a single-gene annotation. Hypothesis: PSMD13 may help define the proteasome-centered branch of the shared module, but no causal role in the myometrium-prostate co-abundance pattern is established.

#### PAK2

- **Related proteins** (co-abundance neighbors): CCT7 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: p21 (RAC1) activated kinase 2. The p21 activated kinases (PAK) are critical effectors that link Rho GTPases to cytoskeleton reorganization and nuclear signaling. The PAK proteins are a family of serine/threonine kinases that serve as targets for the small GTP binding proteins, CDC42 and RAC1, and have been implicated in a wide range of biological activities. The protein encoded by this gene is activated by proteolytic cleavage …
- **Diseases (Open Targets)**: Knobloch syndrome 2 (0.525); Knobloch syndrome (0.454); HIV infectious disease (0.370); atrial fibrillation (0.210); ovarian carcinoma (0.175)
- **Europe PMC papers**: 3704
- **Why important**: PAK2 is a peripheral module member connected to CCT7 and is included in the globally corrected ATP- and adenyl-ribonucleotide-binding terms (GO:MF ATP binding; q_global = 0.00699), (GO:MF adenyl ribonucleotide binding; q_global = 0.00732), (GO:MF adenyl nucleotide binding; q_global = 0.0275). Its established function is a RAC and CDC42-responsive serine/threonine kinase linking Rho-GTPase activity to cytoskeletal reorganization, nuclear signaling, migration and apoptotic regulation. STRING supplementary relationships connect it with proteasome-associated regulation and several receptor or MAPK signaling categories (STRING RCTM Regulation of activated PAK-2p34 by proteasome mediated degradation; within-query FDR = 0.0069), (STRING RCTM TCR signaling; within-query FDR = 0.0096) (STRING RCTM Fc epsilon receptor (FCERI) signaling; within-query FDR = 0.0096) (STRING RCTM Signaling by ROBO receptors; within-query FDR = 0.0096), (STRING RCTM C-type lectin receptors (CLRs); within-query FDR = 0.0096), (STRING RCTM MAPK6/MAPK4 signaling; within-query FDR = 0.0096), (STRING RCTM Host Interactions of HIV factors; within-query FDR = 0.0122), but these remain supplementary evidence. PAK2 also has substantial literature and disease associations including Knobloch syndrome, HIV infection and ovarian carcinoma.
- **Conclusion**: Established conclusion: PAK2 provides a plausible cytoskeletal and signaling interface for an otherwise largely housekeeping-like module. Hypothesis: PAK2 may link CCT-dependent folding to actin or cytoskeletal remodeling in the shared tissue state, but the single co-abundance edge and supplementary STRING annotations do not establish that mechanism.

## Module 7

**Tissue pair**: myometrium and prostate  
**Genes (10)**: HSPH1, PAFAH1B3, PSMC6, ADSS2, UPF1, SEC23IP, SEC24C, UBA6, XPO1, CSE1L

### Function

The module is most consistent with a broadly expressed intracellular proteostasis and RNA-protein trafficking program, rather than a tissue-specific pathway. Its genes span nuclear transport, mRNA surveillance, protein folding, ubiquitin-dependent regulation, proteasomal degradation, and endoplasmic-reticulum-to-Golgi vesicle trafficking. The strongest co-abundance hubs are XPO1, CSE1L, and HSPH1, with UPF1 providing a bridge to SEC24C and SEC23IP. However, no GO or KEGG term passed global correction, so the proposed function is an interpretation of the gene annotations and network architecture, not a globally significant enrichment result. The absence of a globally enriched term does not invalidate the module.

**Cell composition.** The module does not resemble a plasma-protein or secreted-protein module: the HPA summary identifies no secreted genes. All genes have low tissue specificity, and most have low immune-cell specificity; one is not detected in immune cells. Therefore, the shared signal is unlikely to be explained primarily by plasma contamination or a blood-cell-enriched population. Six genes show cell-type-enhanced expression, but the enhanced cell types are heterogeneous and include epithelial, reproductive, pancreatic duct, and monocyte-related populations rather than a single shared cell type. The pattern is more compatible with broadly distributed cellular machinery, possibly modulated by differences in cellular composition or cellular stress. Protein detection is more frequent in prostate than myometrium, while several genes remain undetected in one or both tissues, so transcript co-abundance should not be equated with uniform protein abundance.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only two high-confidence relationships within the module: CSE1L with XPO1, and SEC23IP with SEC24C. These support a nuclear transport submodule and a COPII vesicle-trafficking submodule, respectively. STRING reports no supplementary functional enrichment. hu.MAP independently places SEC23IP with SEC24C in several COPII-related complexes (hu.MAP huMAP3_07775.1), (hu.MAP huMAP3_09282.1), (hu.MAP huMAP3_11128.1), and (hu.MAP huMAP3_13535.1), while XPO1 with CSE1L recurs in complexes (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_09592.1). These complex memberships show that parts of the module correspond to known molecular assemblies, although each complex contains many proteins outside the module. HSPH1, UPF1, UBA6, PSMC6, PAFAH1B3, and ADSS2 do not have an in-module STRING or hu.MAP relationship in the supplied evidence. Thus, the co-abundance network extends beyond currently catalogued physical interactions and should not be interpreted as a single established protein complex.

**STRING interactions (score >= 0.7)**: 2 of 45 gene pairs: CSE1L–XPO1 (0.976); SEC23IP–SEC24C (0.737)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07775.1 (SEC24C, SEC23IP; 2/5); huMAP3_09282.1 (SEC24C, SEC23IP; 2/6); huMAP3_11128.1 (SEC24C, SEC23IP; 2/8); huMAP3_13535.1 (SEC24C, SEC23IP; 2/14); huMAP3_07170.1 (XPO1, CSE1L; 2/14); huMAP3_09042.1 (XPO1, CSE1L; 2/26); huMAP3_06791.1 (XPO1, CSE1L; 2/31); huMAP3_09592.1 (XPO1, CSE1L; 2/95)

### Novelty

The molecular functions represented here are established, and the XPO1-CSE1L and SEC23IP-SEC24C relationships are already supported by STRING, with the latter also represented in multiple hu.MAP complexes. Consequently, the module is not a discovery of a new interaction or a new biochemical pathway. The potentially novel result is the coordinated co-abundance of these otherwise distinct transport, proteostasis, and RNA-quality-control components across myometrium and prostate. That observation may be new in this tissue-pair context, but novelty cannot be established definitively from the fact sheet alone. The absence of additional STRING or hu.MAP relationships is evidence of limited prior interaction support, not proof that the co-abundance pattern or its mechanism is novel.

**Hypothesis.** Hypothesis: the shared module reflects a coordinated cellular-maintenance state in which nuclear transport and RNA surveillance are coupled to proteostasis and secretory-pathway capacity. Increased XPO1-CSE1L activity could track movement of nuclear cargo, while UPF1 could link mRNA export and surveillance to the broader program. HSPH1, UBA6, and PSMC6 could represent handling, modification, and removal of damaged or misfolded proteins. SEC24C and SEC23IP could represent parallel adjustment of ER export and vesicle formation. In both tissues, this state might arise from common smooth-muscle or epithelial cellular demands, differentiation, or stress rather than from a tissue-specific secreted or immune process. This is a mechanistic hypothesis requiring validation by protein-level measurements, perturbation, and direct testing of whether the module changes with ER stress, proteotoxic stress, or altered nuclear export.

### Important genes

#### XPO1

- **Related proteins** (co-abundance neighbors): CSE1L (0.89), HSPH1 (0.85), UBA6 (0.83), PSMC6 (0.82); STRING partners: CSE1L (0.976)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: huMAP3_07170.1, huMAP3_09042.1, huMAP3_06791.1, huMAP3_09592.1
- **Function (MyGene.info)**: exportin 1. This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSe…
- **Diseases (Open Targets)**: plasma cell myeloma (0.642); B-cell chronic lymphocytic leukemia (0.626); diffuse large B-cell lymphoma (0.602); HIV infectious disease (0.561); neurodegenerative disease (0.522)
- **Europe PMC papers**: 5357
- **Why important**: XPO1 is one of the principal network hubs and is directly connected to CSE1L, HSPH1, UBA6, and PSMC6. Its established function is export of nuclear cargo, including RNA and regulatory proteins, and its annotations include ribosomal subunit export, mRNA export, and regulation of transcriptional signaling. It also has extensive literature coverage and disease associations involving hematologic malignancy, HIV infection, and neurodegenerative disease. Its recurring hu.MAP association with CSE1L (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_09592.1) reinforces the importance of the nuclear-transport component.
- **Conclusion**: Established evidence supports XPO1 as a central nuclear-export component and a strong marker of the module's intracellular transport axis. It is plausible, but not established, that variation in XPO1 activity helps coordinate the other module processes across the two tissues.

#### CSE1L

- **Related proteins** (co-abundance neighbors): XPO1 (0.89), PAFAH1B3 (0.85), PSMC6 (0.84), ADSS2 (0.80); STRING partners: XPO1 (0.976)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07170.1, huMAP3_09042.1, huMAP3_06791.1, huMAP3_09592.1
- **Function (MyGene.info)**: chromosome segregation 1 like. Proteins that carry a nuclear localization signal (NLS) are transported into the nucleus by the importin-alpha/beta heterodimer. Importin-alpha binds the NLS, while importin-beta mediates translocation through the nuclear pore complex. After translocation, RanGTP binds importin-beta and displaces importin-alpha. Importin-alpha must then be returned to the cytoplasm, leaving the NLS protein behind.…
- **Diseases (Open Targets)**: intelligence (0.293); neurodegenerative disease (0.269); Alzheimer disease (0.199); celiac disease (0.187); autism spectrum disorder (0.178)
- **Europe PMC papers**: 860
- **Why important**: CSE1L has hub-level network connectivity and the strongest supplied STRING relationship, with XPO1. Its established role in recycling importin-alpha after nuclear import makes it a functional complement to XPO1 rather than an unrelated correlate. It also connects to PAFAH1B3, PSMC6, and ADSS2 in the co-abundance network, potentially linking nuclear transport with proteostasis and metabolism. Its literature volume is substantial, and the HPA profile indicates broad tissue distribution with reproductive-cell enhancements.
- **Conclusion**: Established evidence supports CSE1L as the nuclear-transport partner most directly anchoring the module. The broader connections to proteasomal, lipid-related, and purine-related genes remain co-abundance associations and should not be treated as proven physical or regulatory interactions.

#### HSPH1

- **Related proteins** (co-abundance neighbors): XPO1 (0.85), SEC24C (0.85), UBA6 (0.84), UPF1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family H (Hsp110) member 1. This gene encodes a member of the heat shock protein 70 family of proteins. The encoded protein functions as a nucleotide exchange factor for the molecular chaperone heat shock cognate 71 kDa protein (Hsc70). In addition, this protein plays a distinct but related role as a holdase that inhibits the aggregation of misfolded proteins, including the cystic fibrosis transmembrane conductance regulator…
- **Diseases (Open Targets)**: Parkinson disease (0.205); Phenotypic abnormality (0.187); hypertensive disorder (0.131); neoplasm (0.104); major depressive disorder (0.096)
- **Europe PMC papers**: 2050
- **Why important**: HSPH1 is a highly connected module hub linking XPO1, SEC24C, UBA6, and UPF1. Its established function as a chaperone-associated nucleotide exchange factor and holdase provides a direct proteostasis interpretation for this position. It is annotated for protein folding, unfolded-protein response, and stress response, has substantial literature coverage, and has been associated with cancer and other disease contexts. Its HPA cell-type enhancements are heterogeneous, which argues against assigning the module to one specific cell population.
- **Conclusion**: Established evidence supports HSPH1 as a plausible proteostasis hub within the module. Its position suggests that cellular stress or protein-folding demand may connect the nuclear and vesicle-trafficking components, but that coupling is a hypothesis rather than a demonstrated mechanism.

#### SEC24C

- **Related proteins** (co-abundance neighbors): UPF1 (0.86), HSPH1 (0.85); STRING partners: SEC23IP (0.737)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in myometrium, prostate
- **hu.MAP 3.0**: huMAP3_07775.1, huMAP3_09282.1, huMAP3_11128.1, huMAP3_13535.1
- **Function (MyGene.info)**: SEC24 homolog C, COPII component. The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec24p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The product of this gene may play a role in shaping the vesicle, as well as in cargo selection and concentration.…
- **Diseases (Open Targets)**: 22q11.2 deletion syndrome (0.370); neurodegenerative disease (0.369); Alzheimer disease (0.281); lysosomal storage disease (0.274); Parkinson disease (0.274)
- **Europe PMC papers**: 693
- **Why important**: SEC24C is the module member with the clearest COPII vesicle-trafficking evidence. It is connected to UPF1 and HSPH1, has a STRING relationship with SEC23IP, and recurs with SEC23IP across hu.MAP complexes (hu.MAP huMAP3_07775.1), (hu.MAP huMAP3_09282.1), (hu.MAP huMAP3_11128.1), and (hu.MAP huMAP3_13535.1). Its established functions include COPII-coated vesicle cargo loading and ER-to-Golgi transport. It is detected in both myometrium and prostate by HPA, making it especially relevant to a shared tissue-pair module.
- **Conclusion**: Established evidence supports SEC24C as the anchor of a vesicle-trafficking submodule. Its connection to the nuclear surveillance and chaperone-related genes is supported by co-abundance but is not yet established as a direct molecular pathway.

#### SEC23IP

- **Related proteins** (co-abundance neighbors): UPF1 (0.84); STRING partners: SEC24C (0.737)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_07775.1, huMAP3_09282.1, huMAP3_11128.1, huMAP3_13535.1
- **Function (MyGene.info)**: SEC23 interacting protein. This gene encodes a member of the phosphatidic acid preferring-phospholipase A1 family. The encoded protein is localized to endoplasmic reticulum exit sites and plays a critical role in ER-Golgi transport as part of the multimeric coat protein II complex. An orthologous gene in frogs is required for normal neural crest cell development, suggesting that this gene may play a role in Waardenburg synd…
- **Diseases (Open Targets)**: Parkinson disease (0.409); type 2 diabetes mellitus (0.372); cardiomyopathy (0.326); diabetes mellitus (0.294); Genu valgum (0.269)
- **Europe PMC papers**: 265
- **Why important**: SEC23IP is a direct partner of SEC24C in STRING and appears with SEC24C in multiple hu.MAP COPII-related complexes (hu.MAP huMAP3_07775.1), (hu.MAP huMAP3_09282.1), (hu.MAP huMAP3_11128.1), and (hu.MAP huMAP3_13535.1). Its established localization at ER exit sites and role in COPII-mediated ER-to-Golgi transport make it an important functional representative of the vesicle-trafficking arm. It also has annotations involving Golgi organization and the endomembrane system, along with disease associations involving Parkinson disease, diabetes, and cardiomyopathy.
- **Conclusion**: Established evidence supports SEC23IP as a bona fide component of the module's ER-export machinery. Its co-abundance with UPF1 and the broader module may indicate coordination between secretory-pathway capacity and RNA or proteostasis control, but this cross-process relationship remains hypothetical.
