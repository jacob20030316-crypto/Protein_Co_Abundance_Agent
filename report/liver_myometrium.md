# Conserved co-abundance modules: liver and myometrium

## Module 0

**Tissue pair**: liver and myometrium  
**Genes (10)**: APEX1, ATXN10, DDX39B, HNRNPK, HNRNPL, PSMC2, PTBP1, SAE1, RARS1, CCT8

### Function

The strongest interpretation is a conserved nuclear RNA-processing and mRNA-regulatory module. The globally corrected terms identify ribonucleoprotein granules (GO:CC ribonucleoprotein granule; q_global = 0.03), mRNA metabolic processes (GO:BP mRNA metabolic process; q_global = 0.0473), and regulation of mRNA metabolism (GO:BP regulation of mRNA metabolic process; q_global = 0.0473). These findings are supported by the presence of PTBP1, HNRNPL, HNRNPK, and DDX39B, which are annotated in RNA binding, pre-mRNA processing, splicing, RNA export, and formation or function of heterogeneous nuclear ribonucleoprotein complexes. APEX1 adds a DNA-repair and genome-maintenance component, while SAE1, PSMC2, RARS1, and CCT8 represent possible links to post-translational modification, proteasomal regulation, translation, and protein folding. The latter processes should be regarded as contextual module features rather than the primary functional assignment.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes and low immune-cell specificity throughout the module. All genes have low tissue specificity, which is consistent with broadly expressed intracellular or housekeeping-type biology rather than a liver-specific or myometrium-specific program. Protein detection in both tissues supports technical and biological presence in the paired tissues, but the detection pattern is not uniform across genes. Several genes show cell-type enhancement in neural or reproductive cell categories, yet there is no coherent blood-cell signature. The shared signal therefore more plausibly reflects a conserved intracellular RNA-processing state, cellular composition shared across tissues, or both, rather than blood contamination.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC ribonucleoprotein granule | 0.03 | APEX1, DDX39B, HNRNPK, HNRNPL, PSMC2 |
| GO:BP mRNA metabolic process | 0.0473 | APEX1, DDX39B, HNRNPK, HNRNPL, PTBP1 |
| GO:BP regulation of mRNA metabolic process | 0.0473 | APEX1, HNRNPK, HNRNPL, PTBP1 |

### STRING and hu.MAP

STRING provides established high-confidence relationships within the hnRNP-centered portion of the module: HNRNPK, HNRNPL, and PTBP1 form a tightly connected interaction core, and DDX39B connects to each of these RNA-processing proteins. STRING also supports a relationship between CCT8 and PSMC2. The STRING functional results independently point to nucleoplasm, RNA binding, and an hnRNP/PTBP-related neighborhood (STRING Component Nucleoplasm; within-query FDR = 0.0074), (STRING NetworkNeighborAL Multisystem proteinopathy, and HnRNP-L/PTB; within-query FDR = 0.0125), and (STRING Keyword RNA-binding; within-query FDR = 0.0336). These observations strengthen the interpretation that the co-abundance module contains a real RNA-processing core, although STRING relationships are supplementary and do not establish tissue-specific co-regulation. hu.MAP identifies HNRNPL and HNRNPK together in two large RNA- or hnRNP-associated complexes (hu.MAP huMAP3_10659.1) and (hu.MAP huMAP3_10625.1). The fact that only these members of the module overlap each complex means that the complexes validate the central hnRNP relationship, but do not explain the entire module. The module's co-abundance edges involving SAE1, ATXN10, APEX1, RARS1, and CCT8 should therefore not be treated as already-established physical complexes solely on the basis of the STRING and hu.MAP evidence provided.

**STRING interactions (score >= 0.7)**: 7 of 45 gene pairs: CCT8–PSMC2 (0.733); DDX39B–HNRNPK (0.808); DDX39B–HNRNPL (0.807); DDX39B–PTBP1 (0.785); HNRNPK–HNRNPL (0.99); HNRNPK–PTBP1 (0.997); HNRNPL–PTBP1 (0.993)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Nucleoplasm (FDR = 0.0074, 9 genes); NetworkNeighborAL Multisystem proteinopathy, and HnRNP-L/PTB (FDR = 0.0125, 3 genes); Keyword RNA-binding (FDR = 0.0336, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10659.1 (HNRNPL, HNRNPK; 2/28); huMAP3_10625.1 (HNRNPL, HNRNPK; 2/57)

### Novelty

The RNA-processing core is not a new molecular idea: the HNRNPK-HNRNPL-PTBP1 relationships, the DDX39B connections, and the hu.MAP hnRNP complexes are already known. The potentially novel aspect is the cross-tissue co-abundance configuration linking this established RNA-processing core with APEX1, SAE1, ATXN10, PSMC2, RARS1, and CCT8 in liver and myometrium. This can be described as a potentially new tissue-pair module or systems-level association, not as discovery of new protein interactions. Absence of some module relationships from STRING or hu.MAP is insufficient to prove novelty, because those resources are incomplete and measure different kinds of evidence. Independent replication, preservation in additional co-abundance datasets, and perturbation or biochemical testing would be needed to establish novelty and mechanistic specificity.

**Hypothesis.** Hypothesis: the shared liver-myometrium signal represents a conserved nuclear RNA-management state in which the HNRNPK-HNRNPL-PTBP1 core organizes or regulates RNA-processing assemblies, DDX39B supports spliceosome assembly and nuclear RNA export, and APEX1 and SAE1 couple RNA metabolism to genome maintenance and post-translational regulation. PSMC2, RARS1, and CCT8 may reflect coordinated demands for proteostasis, translation, and folding. ATXN10 may provide an additional cell-state or cytoskeletal-associated link, but its role in this module is especially uncertain. This is a mechanistic model rather than a demonstrated causal pathway.

### Important genes

#### HNRNPK

- **Related proteins** (co-abundance neighbors): PTBP1 (0.88), HNRNPL (0.81); STRING partners: DDX39B (0.808), HNRNPL (0.99), PTBP1 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, myometrium
- **hu.MAP 3.0**: huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is a central member of the RNA-processing core, connected in STRING to HNRNPL, PTBP1, and DDX39B, and present in both hu.MAP complexes (hu.MAP huMAP3_10659.1) and (hu.MAP huMAP3_10625.1). It contributes to the globally corrected ribonucleoprotein-granule and mRNA-metabolism signals (GO:CC ribonucleoprotein granule; q_global = 0.03), (GO:BP mRNA metabolic process; q_global = 0.0473), and (GO:BP regulation of mRNA metabolic process; q_global = 0.0473). Its established functions include RNA processing, mRNA splicing, and transcriptional regulation. It has substantial literature and disease relevance, including Au-Kline syndrome and neurodevelopmental or neurodegenerative associations.
- **Conclusion**: Established evidence supports HNRNPK as a core structural and regulatory component of the module. It is a strong candidate for an organizing hub, but the fact sheet does not establish that it causes the shared liver-myometrium co-abundance pattern.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): PTBP1 (0.87), PSMC2 (0.83), HNRNPK (0.81); STRING partners: DDX39B (0.807), HNRNPK (0.99), PTBP1 (0.993)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, myometrium
- **hu.MAP 3.0**: huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is a central RNA-binding protein with strong STRING relationships to HNRNPK, PTBP1, and DDX39B, and it is represented in both hu.MAP complexes (hu.MAP huMAP3_10659.1) and (hu.MAP huMAP3_10625.1). It appears in all three globally corrected GO signals (GO:CC ribonucleoprotein granule; q_global = 0.03), (GO:BP mRNA metabolic process; q_global = 0.0473), and (GO:BP regulation of mRNA metabolic process; q_global = 0.0473). Its established annotations include formation, packaging, and processing of mRNA and regulation of RNA splicing. It has a substantial literature base and disease associations involving neuromuscular disease and cancer.
- **Conclusion**: Established evidence identifies HNRNPL as a core RNA-processing component and a plausible physical scaffold for the module's conserved signal. Its precise contribution to liver and myometrium remains a hypothesis.

#### PTBP1

- **Related proteins** (co-abundance neighbors): HNRNPK (0.88), HNRNPL (0.87), SAE1 (0.83); STRING partners: DDX39B (0.785), HNRNPK (0.997), HNRNPL (0.993)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypyrimidine tract binding protein 1. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA-binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.505); dengue disease (0.372); open-angle glaucoma (0.330); glaucoma (0.309); neoplasm (0.116)
- **Europe PMC papers**: 4849
- **Why important**: PTBP1 is among the most connected module genes and links HNRNPK, HNRNPL, and SAE1 in the co-abundance network. It contributes to the globally corrected mRNA-metabolism terms (GO:BP mRNA metabolic process; q_global = 0.0473) and (GO:BP regulation of mRNA metabolic process; q_global = 0.0473) and to the ribonucleoprotein-granule term through the broader module context (GO:CC ribonucleoprotein granule; q_global = 0.03). Its established functions include alternative splicing, mRNA processing, RNA splicing, and regulation of gene expression. It has the deepest literature representation among the highlighted genes and established associations with neurodevelopmental, dengue, glaucoma, and neoplastic disease.
- **Conclusion**: Established evidence supports PTBP1 as a major regulatory hub for RNA processing in this module. Its connection to SAE1 suggests a possible regulatory interface, but that interface is not established as causal by the supplied data.

#### DDX39B

- **Related proteins** (co-abundance neighbors): ATXN10 (0.81); STRING partners: HNRNPK (0.808), HNRNPL (0.807), PTBP1 (0.785)
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nuclear speckles; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 39B. This gene encodes a member of the DEAD box family of RNA-dependent ATPases that mediate ATP hydrolysis during pre-mRNA splicing. The encoded protein is an essential splicing factor required for association of U2 small nuclear ribonucleoprotein with pre-mRNA, and it also plays an important role in mRNA export from the nucleus to the cytoplasm. This gene belongs to a cluster of genes localized in th…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); Alzheimer disease (0.522); Parkinson disease (0.503); lysosomal storage disease (0.503); neurodevelopmental disorder (0.413)
- **Europe PMC papers**: 1037
- **Why important**: DDX39B is the module's annotated RNA helicase and is connected by STRING to HNRNPK, HNRNPL, and PTBP1. It contributes to the globally corrected ribonucleoprotein-granule and mRNA-metabolism terms (GO:CC ribonucleoprotein granule; q_global = 0.03) and (GO:BP mRNA metabolic process; q_global = 0.0473), and STRING supports its nucleoplasmic and RNA-binding context (STRING Component Nucleoplasm; within-query FDR = 0.0074) and (STRING Keyword RNA-binding; within-query FDR = 0.0336). Its established functions include spliceosomal assembly, pre-mRNA splicing, and export of RNA from the nucleus. It has disease associations involving neurodegenerative and neurodevelopmental disorders.
- **Conclusion**: Established evidence supports DDX39B as a functional bridge between RNA helicase activity, splicing, and the hnRNP core. Its apparent cross-tissue co-abundance with ATXN10 is intriguing but remains a hypothesis requiring validation.

#### APEX1

- **Related proteins** (co-abundance neighbors): SAE1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apurinic/apyrimidinic endodeoxyribonuclease 1. The APEX gene encodes the major AP endonuclease in human cells. It encodes the APEX endonuclease, a DNA repair enzyme with apurinic/apyrimidinic (AP) activity. Such AP activity sites occur frequently in DNA molecules by spontaneous hydrolysis, by DNA damaging agents or by DNA glycosylases that remove specific abnormal bases. The AP sites are the most frequent pre-mutagenic lesions that can prevent…
- **Diseases (Open Targets)**: neurodegenerative disease (0.464); Galloway-Mowat syndrome (0.429); hereditary disease (0.161); neoplasm (0.118); non-small cell lung carcinoma (0.115)
- **Europe PMC papers**: 2928
- **Why important**: APEX1 contributes to all three globally corrected GO signals (GO:CC ribonucleoprotein granule; q_global = 0.03), (GO:BP mRNA metabolic process; q_global = 0.0473), and (GO:BP regulation of mRNA metabolic process; q_global = 0.0473), is connected to SAE1 in the module network, and is detected in both tissues. Its established function is central to base-excision DNA repair and genome maintenance, with additional annotations involving telomere maintenance. It has a substantial literature and disease associations involving neurodegenerative disease, Galloway-Mowat syndrome, and cancer.
- **Conclusion**: Established evidence supports APEX1 as a genome-maintenance factor that is co-abundant with the module's RNA-processing program. A functional coupling between RNA metabolism and DNA repair is a reasonable hypothesis, but it is not demonstrated by the enrichment or interaction evidence alone.

## Module 1

**Tissue pair**: liver and myometrium  
**Genes (7)**: BPNT1, EPS15L1, ATIC, NARS1, YARS1, CCT5, NAE1

### Function

The module does not have a globally significant GO or KEGG enrichment: no globally significant GO/KEGG term passed global correction. Its gene-level annotations instead point to a broad intracellular maintenance program combining translation, protein folding, protein modification, nucleotide and purine metabolism, and vesicle or endosomal biology. The strongest coherent biological interpretation is cellular proteostasis and biosynthetic support rather than a tissue-specific pathway. YARS1 and NARS1 are aminoacyl-tRNA synthetases, CCT5 is a chaperonin subunit, NAE1 supports NEDD8 activation, BPNT1 participates in nucleotide and phosphoinositide-related metabolism, and ATIC catalyses terminal steps of de novo purine synthesis. Because the module is a small co-abundance subgraph and lacks globally significant enrichment, this functional interpretation should be regarded as convergent gene-level evidence rather than pathway-level proof.

**Cell composition.** The module is not composed of plasma or secreted proteins: all genes have no secretome designation. HPA reports low tissue specificity for every gene and low immune-cell specificity for every gene, with no frequent enriched blood-cell category. Protein detection is present for most genes in both liver and myometrium, while CCT5 is not detected in either of those tissues in the stated HPA immunohistochemistry summary. The single-cell annotations are heterogeneous, including intestinal epithelial cells, myonuclei, neutrophils, spermatogenic cells, and trophoblasts, rather than identifying one shared cell type. Thus the module does not strongly support a plasma-protein or blood-contamination explanation, but its broad tissue profile means that shared cellular housekeeping or general biosynthetic activity remains plausible.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, between NARS1 and YARS1, supporting a known connection between two translation-related aminoacyl-tRNA synthetases. No other within-module STRING partners are reported at the stated threshold, and STRING functional enrichment is absent. hu.MAP supports recurrent co-membership of NARS1 and YARS1 in (hu.MAP huMAP3_10302.1) and (hu.MAP huMAP3_10115.1), while (hu.MAP huMAP3_14442.1) supports co-membership of YARS1 and ATIC. These complexes also contain many proteins outside the module, so they establish that selected pairs participate in known larger molecular assemblies but do not demonstrate that the entire module is one physical complex. The network edges beyond the NARS1-YARS1 relationship should therefore be interpreted primarily as co-abundance associations.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: NARS1–YARS1 (0.966)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10302.1 (NARS1, YARS1; 2/9); huMAP3_10115.1 (NARS1, YARS1; 2/14); huMAP3_14442.1 (ATIC, YARS1; 2/57)

### Novelty

The module is unlikely to represent a previously established single complex or canonical pathway, because only the NARS1-YARS1 relationship is directly supported by STRING, the other within-module relationships lack reported STRING support, and the hu.MAP overlaps are partial and distributed across larger complexes. However, this does not prove that the liver-myometrium co-abundance pattern is novel: individual genes, gene functions, and pairwise complex memberships are already known, and absence from STRING or hu.MAP is not evidence of biological novelty. The defensible conclusion is that the tissue-pair module may be a novel cross-tissue co-abundance configuration built from largely established intracellular functions, but its novelty requires independent replication and comparison with published tissue co-expression studies.

**Hypothesis.** Hypothesis: in both liver and myometrium, a shared level of general cellular activity coordinates translation capacity, folding of newly produced proteins, NEDD8-dependent protein regulation, nucleotide and purine supply, and membrane-trafficking support. The central position of YARS1 and NAE1, together with the NARS1-YARS1 known interaction and the NARS1-YARS1 and YARS1-ATIC hu.MAP overlaps, suggests a biosynthetic and proteostasis coordination axis. This is a hypothesis based on network structure and gene functions, not a demonstrated physical pathway or causal mechanism.

### Important genes

#### YARS1

- **Related proteins** (co-abundance neighbors): CCT5 (0.86), EPS15L1 (0.85), NAE1 (0.83); STRING partners: NARS1 (0.966)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver, myometrium
- **hu.MAP 3.0**: huMAP3_10302.1, huMAP3_10115.1, huMAP3_14442.1
- **Function (MyGene.info)**: tyrosyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Tyrosyl-tRNA synthetase belongs to the class I tRNA synthetase family. Cytokine activities have also been observ…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease dominant intermediate C (0.739); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset 2 (0.707); hereditary disease (0.509); Charcot-Marie-Tooth disease (0.418); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset (0.333)
- **Europe PMC papers**: 215
- **Why important**: YARS1 has a highly connected position in the module and links CCT5, EPS15L1, and NAE1. It is a tyrosyl-tRNA synthetase with an established role in tyrosyl-tRNA aminoacylation and protein translation. It is the module member participating in all listed hu.MAP overlaps, and it forms the sole reported high-confidence STRING pair with NARS1. Its disease associations include Charcot-Marie-Tooth disease and multisystem neurodevelopmental disorders, while its literature volume is substantial.
- **Conclusion**: Established evidence supports YARS1 as a central translation-related connector and as the best-supported network anchor. It is plausible, but unproven, that YARS1 helps link the module's biosynthetic processes.

#### NAE1

- **Related proteins** (co-abundance neighbors): NARS1 (0.86), BPNT1 (0.83), YARS1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NEDD8 activating enzyme E1 subunit 1. The protein encoded by this gene binds to the beta-amyloid precursor protein. Beta-amyloid precursor protein is a cell surface protein with signal-transducing properties, and it is thought to play a role in the pathogenesis of Alzheimer's disease. In addition, the encoded protein can form a heterodimer with UBE1C and bind and activate NEDD8, a ubiquitin-like protein. This protein is required for c…
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and ischiopubic hypoplasia (0.576); neurodegenerative disease (0.533); acute myeloid leukemia (0.347); myelodysplastic syndrome (0.345); chronic myelomonocytic leukemia (0.286)
- **Europe PMC papers**: 798
- **Why important**: NAE1 has a highly connected position, linking NARS1, BPNT1, and YARS1. It is the NEDD8 activating enzyme E1 subunit and is annotated for protein neddylation, cell-cycle checkpoint signalling, and regulation of apoptosis. It has disease associations involving neurodevelopment, neurodegeneration, acute myeloid leukemia, and myelodysplastic syndrome, with a substantial literature volume.
- **Conclusion**: Established evidence supports NAE1 as the module's principal protein-regulatory and ubiquitin-like modification component. Its connection to translation and nucleotide-related genes suggests coordination, but the co-abundance data do not establish that NAE1 regulates the other module genes.

#### NARS1

- **Related proteins** (co-abundance neighbors): NAE1 (0.86), ATIC (0.81); STRING partners: YARS1 (0.966)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver, myometrium
- **hu.MAP 3.0**: huMAP3_10302.1, huMAP3_10115.1
- **Function (MyGene.info)**: asparaginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids.  Asparaginyl-tRNA synthetase is localized to the cytoplasm and belongs to the class II family of tRNA synthetases.  The N-terminal domain represents the signature sequence for the eukaryotic asparaginyl-tRNA synthetases. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, impaired language, and gait abnormalities (0.762); neurodevelopmental disorder with microcephaly, impaired language, epilepsy, and gait abnormalities (0.679); neurodevelopmental disorder (0.567); complex neurodevelopmental disorder (0.462); developmental disability (0.340)
- **Europe PMC papers**: 216
- **Why important**: NARS1 is an asparaginyl-tRNA synthetase involved in translation and asparaginyl-tRNA aminoacylation. It connects NAE1 and ATIC, forms the reported high-confidence STRING relationship with YARS1, and occurs with YARS1 in (hu.MAP huMAP3_10302.1) and (hu.MAP huMAP3_10115.1). Its disease associations are dominated by neurodevelopmental disorders, and it has an established literature base.
- **Conclusion**: Established evidence supports NARS1 as a translation-related bridge between the YARS1-containing complexes and ATIC. Its bridge-like position is consistent with a biosynthetic interpretation, but does not prove direct physical coupling to ATIC in this tissue module.

#### ATIC

- **Related proteins** (co-abundance neighbors): NARS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver, myometrium
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: 5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase. This gene encodes a bifunctional protein that catalyzes the last two steps of the de novo purine biosynthetic pathway. The N-terminal domain has phosphoribosylaminoimidazolecarboxamide formyltransferase activity, and the C-terminal domain has IMP cyclohydrolase activity. A mutation in this gene results in AICA-ribosiduria. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: AICA-ribosiduria (0.708); cancer (0.571); Intellectual disability (0.463); lung adenocarcinoma (0.390); anaplastic large cell lymphoma (0.374)
- **Europe PMC papers**: 5200
- **Why important**: ATIC is the least connected member of the network but is functionally distinctive: it catalyses the last two steps of de novo purine biosynthesis and is associated with AICA-ribosiduria, cancer, and intellectual disability. It participates in (hu.MAP huMAP3_14442.1) with YARS1 and has a large literature volume. Its presence adds a nucleotide-supply dimension that is not captured by the aminoacylation genes alone.
- **Conclusion**: Established evidence supports ATIC as the module's purine-biosynthesis representative and as a partial complex-overlap partner of YARS1. Its inclusion supports a biosynthetic interpretation, while its functional connection to the remaining module is a hypothesis.

#### CCT5

- **Related proteins** (co-abundance neighbors): YARS1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is a chaperonin-containing TCP1 subunit that participates in ATP-dependent folding of proteins such as actin and tubulin. It is directly connected to YARS1 in the module and has the largest literature volume among the listed genes. Its disease associations include hereditary sensory and autonomic neuropathy with spastic paraplegia and neurodegenerative disease.
- **Conclusion**: Established evidence supports CCT5 as the module's protein-folding component and as a link from translation capacity to proteostasis. Its absence from the stated liver and myometrium immunohistochemistry detections warrants caution when interpreting its tissue-level contribution.

## Module 2

**Tissue pair**: liver and myometrium  
**Genes (10)**: CAPZB, CNOT1, CASK, TUFM, HSPH1, PCNA, PFAS, TCEA1, XPO1, CSE1L

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. The module therefore does not support a single statistically established pathway assignment. Its gene composition instead suggests coordinated cellular maintenance involving several processes: nuclear transport through XPO1 and CSE1L, proteostasis through HSPH1, purine synthesis and replication-associated activity through PFAS and PCNA, transcriptional elongation through TCEA1, mRNA regulation through CNOT1, actin dynamics through CAPZB, mitochondrial translation through TUFM, and intracellular scaffolding or transport through CASK. The sparse network is better interpreted as a coordinated cellular-state signature than as proof of one physical biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: no member is annotated as secreted. Most genes have low tissue specificity, and most are detected at the protein level in both liver and myometrium, although some members are not detected in one or both tissues. Several genes show enhanced specificity for particular cell types, with erythrocyte progenitors recurring among the enriched cell types; PCNA also has tissue-enhanced expression in bone marrow. Blood-cell specificity is generally low, but isolated immune-cell enrichment or enhancement is present. This pattern does not establish a blood cell-derived module, yet it raises the possibility that shared cell composition, proliferative activity, or hematopoietic contamination contributes to the cross-tissue co-abundance. The cell-type annotations also include spermatogenic, epithelial, monocyte, oligodendrocyte-progenitor, and ductal-cell signals, so the HPA evidence is heterogeneous rather than tissue-specific.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The best-supported STRING relationship is XPO1-CSE1L, which is a high-confidence known interaction. CAPZB-CNOT1 is also present but is weaker by comparison. No other STRING interaction among the module members passed the supplied threshold, and STRING functional enrichment was absent. hu.MAP independently places XPO1 and CSE1L together in several complexes (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_09592.1), providing convergent support for a nuclear-transport-related substructure. PFAS and HSPH1 co-occur in a hu.MAP complex (hu.MAP huMAP3_13774.1), but only as a subset of a much larger complex, so this does not by itself establish a direct interaction. The remaining module relationships are not represented by the supplied high-confidence STRING or hu.MAP evidence. Thus, the network contains a validated XPO1-CSE1L core, a supported CAPZB-CNOT1 association, and additional co-abundance links that may reflect shared regulation rather than direct binding.

**STRING interactions (score >= 0.7)**: 2 of 45 gene pairs: CAPZB–CNOT1 (0.708); CSE1L–XPO1 (0.976)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07170.1 (XPO1, CSE1L; 2/14); huMAP3_09042.1 (XPO1, CSE1L; 2/26); huMAP3_06791.1 (XPO1, CSE1L; 2/31); huMAP3_13774.1 (PFAS, HSPH1; 2/33); huMAP3_09592.1 (XPO1, CSE1L; 2/95)

### Novelty

The shared liver-myometrium co-abundance pattern may be a new systems-level observation, but it cannot be called a newly discovered molecular complex. Parts of it are already known: XPO1-CSE1L is supported by STRING and repeatedly represented in hu.MAP (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_09592.1), while CAPZB-CNOT1 is also represented in STRING. The other co-abundance connections lack supplied support in STRING or hu.MAP, but absence from those resources does not prove novelty because databases are incomplete and co-abundance does not imply direct physical interaction. The defensible novelty claim is therefore limited to the cross-tissue module-level association and its particular combination of nuclear transport, proteostasis, replication, RNA regulation, cytoskeletal, and mitochondrial genes. Replication in independent cohorts, cell-composition adjustment, and experimental testing would be required before assigning biological novelty or mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared cellular stress and growth-maintenance state present in both tissues. In this model, XPO1-CSE1L supports regulated nuclear-cytoplasmic transport, HSPH1 buffers proteotoxic stress, PFAS supplies purine-pathway activity for biosynthetic and replication demand, PCNA and TCEA1 mark DNA synthesis and transcriptional activity, and CNOT1-CAPZB connect RNA turnover with cytoskeletal organization. TUFM may represent accompanying mitochondrial translational demand. A competing hypothesis is that the pattern is partly generated by shared minor cell populations or proliferative and stress-related cell states rather than by a unified pathway. This hypothesis is not established by the absent global enrichment results and should be tested with cell-resolved expression, covariate-adjusted replication, and perturbation of the proposed core genes.

### Important genes

#### XPO1

- **Related proteins** (co-abundance neighbors): HSPH1 (0.88), CSE1L (0.85); STRING partners: CSE1L (0.976)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_07170.1, huMAP3_09042.1, huMAP3_06791.1, huMAP3_09592.1
- **Function (MyGene.info)**: exportin 1. This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSe…
- **Diseases (Open Targets)**: plasma cell myeloma (0.642); B-cell chronic lymphocytic leukemia (0.626); diffuse large B-cell lymphoma (0.602); HIV infectious disease (0.561); neurodegenerative disease (0.522)
- **Europe PMC papers**: 5357
- **Why important**: XPO1 is a central member of the best-supported substructure: it is linked to HSPH1 and CSE1L in the co-abundance network, has a high-confidence STRING interaction with CSE1L, and appears with CSE1L in several hu.MAP complexes (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_09592.1). Its established function is export of NES-containing proteins and several RNA classes, with effects on transcriptional and signaling regulators. It has extensive literature and disease associations including plasma-cell myeloma, chronic lymphocytic leukemia, diffuse large B-cell lymphoma, HIV-related disease, and neurodegenerative disease.
- **Conclusion**: Established: XPO1 is the strongest mechanistically anchored candidate for a nuclear-transport component of the module and is supported by both network and complex evidence. Hypothesis: its co-abundance with HSPH1 and the broader module may indicate coordinated stress-responsive nucleocytoplasmic trafficking, but the tissue-level mechanism remains unproven.

#### HSPH1

- **Related proteins** (co-abundance neighbors): XPO1 (0.88), CNOT1 (0.85), TUFM (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_13774.1
- **Function (MyGene.info)**: heat shock protein family H (Hsp110) member 1. This gene encodes a member of the heat shock protein 70 family of proteins. The encoded protein functions as a nucleotide exchange factor for the molecular chaperone heat shock cognate 71 kDa protein (Hsc70). In addition, this protein plays a distinct but related role as a holdase that inhibits the aggregation of misfolded proteins, including the cystic fibrosis transmembrane conductance regulator…
- **Diseases (Open Targets)**: Parkinson disease (0.205); Phenotypic abnormality (0.187); hypertensive disorder (0.131); neoplasm (0.104); major depressive disorder (0.096)
- **Europe PMC papers**: 2050
- **Why important**: HSPH1 is one of the most connected and strongest nodes in the module, linking XPO1, CNOT1, and TUFM. It is a nucleotide-exchange factor for HSC seventy-one and also acts as a holdase that limits aggregation of misfolded proteins. It has a hu.MAP association with PFAS (hu.MAP huMAP3_13774.1), extensive literature, and reported relationships to protein folding, stress, unfolded-protein responses, immune regulation, cancer, Parkinson disease, hypertensive disorder, and major depressive disorder.
- **Conclusion**: Established: HSPH1 is a plausible proteostasis and stress-response anchor with a prominent network position. Hypothesis: it may couple proteotoxic buffering to nuclear transport and mitochondrial translation in the shared tissue state, but the supplied evidence does not show that these proteins form one functional machine.

#### PFAS

- **Related proteins** (co-abundance neighbors): PCNA (0.85), TCEA1 (0.83), CAPZB (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_13774.1
- **Function (MyGene.info)**: phosphoribosylformylglycinamidine synthase. Purines are necessary for many cellular processes, including DNA replication, transcription, and energy metabolism. Ten enzymatic steps are required to synthesize inosine monophosphate (IMP) in the de novo pathway of purine biosynthesis. The enzyme encoded by this gene catalyzes the fourth step of IMP biosynthesis. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: dyskeratosis congenita (0.520); Coats plus syndrome (0.455); neurodegenerative disease (0.187); hereditary disease (0.174); retinal disorder (0.118)
- **Europe PMC papers**: 3393
- **Why important**: PFAS is a prominent connector joining PCNA, TCEA1, and CAPZB. Its established biochemical role is the fourth enzymatic step of de novo purine biosynthesis, making it relevant to nucleotide supply for DNA replication, transcription, and energy metabolism. It is represented with HSPH1 in hu.MAP (hu.MAP huMAP3_13774.1), has substantial literature, and has disease associations including dyskeratosis congenita and Coats plus syndrome.
- **Conclusion**: Established: PFAS provides the clearest metabolic rationale for a biosynthetic or proliferative component of the module. Hypothesis: its covariance with PCNA and TCEA1 may reflect increased nucleotide demand during replication or transcription, although no globally corrected enrichment supports that interpretation.

#### PCNA

- **Related proteins** (co-abundance neighbors): PFAS (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proliferating cell nuclear antigen. The protein encoded by this gene is found in the nucleus and is a cofactor of DNA polymerase delta. The encoded protein acts as a homotrimer and helps increase the processivity of leading strand synthesis during DNA replication. In response to DNA damage, this protein is ubiquitinated and is involved in the RAD6-dependent DNA repair pathway. Two transcript variants encoding the same protein have b…
- **Diseases (Open Targets)**: ataxia-telangiectasia-like disorder (0.497); neurodegenerative disease (0.188); neoplasm (0.118); diabetes mellitus (0.116); hepatocellular carcinoma (0.113)
- **Europe PMC papers**: 61820
- **Why important**: PCNA is the principal replication-associated node connected to PFAS and has a very large literature base. It is an established DNA polymerase delta processivity factor and participates in DNA replication, mismatch repair, chromatin organization, and DNA-damage responses. HPA annotates tissue enhancement in bone marrow and cell-type enhancement in several proliferative or developing populations. Its disease associations include ataxia-telangiectasia-like disorder, neurodegenerative disease, diabetes mellitus, and hepatocellular carcinoma.
- **Conclusion**: Established: PCNA marks replication and repair capacity and gives the PFAS-linked branch a specific cellular interpretation. Hypothesis: PCNA may indicate a shared proliferative or repair-demand state across the tissues, but it could also reflect a minor proliferating population rather than the bulk tissue.

#### CNOT1

- **Related proteins** (co-abundance neighbors): CAPZB (0.86), HSPH1 (0.85); STRING partners: CAPZB (0.708)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CCR4-NOT transcription complex subunit 1. Enables armadillo repeat domain binding activity; molecular adaptor activity; and nuclear receptor binding activity. Contributes to poly(A)-specific ribonuclease activity. Involved in several processes, including negative regulation of signal transduction; positive regulation of cytoplasmic mRNA processing body assembly; and regulation of gene expression. Located in P-body and cytosol. Part of CCR…
- **Diseases (Open Targets)**: holoprosencephaly 12 with or without pancreatic agenesis (0.749); Vissers-Bodmer syndrome (0.697); hereditary disease (0.515); complex neurodevelopmental disorder (0.474); neurodegenerative disease (0.471)
- **Europe PMC papers**: 1262
- **Why important**: CNOT1 is a network connector between CAPZB and HSPH1 and is the scaffold subunit of the CCR4-NOT complex. Its established functions include mRNA deadenylation-dependent decay, regulation of gene expression, P-body assembly, and translational control. It is detected in both liver and myometrium, has disease associations including holoprosencephaly with or without pancreatic agenesis and Vissers-Bodmer syndrome, and has a substantial literature base.
- **Conclusion**: Established: CNOT1 supplies a credible post-transcriptional regulatory component and is supported by the CAPZB-CNOT1 STRING relationship. Hypothesis: CNOT1 may help coordinate stress-induced mRNA remodeling with HSPH1 and actin-associated regulation, but this proposed coupling is not demonstrated by the supplied interaction resources.

## Module 3

**Tissue pair**: liver and myometrium  
**Genes (8)**: DDX5, DNM1L, GARS1, HSP90AB2P, HSP90AA1, SERPINH1, TARS1, VPS35

### Function

The module does not have a globally significant GO or KEGG enrichment, so its function should be inferred cautiously from gene identities and network structure rather than assigned from enrichment. The genes collectively point to broadly conserved intracellular maintenance processes: protein folding and chaperoning through HSP90AA1, HSP90AB2P, and SERPINH1; protein synthesis through the aminoacyl-tRNA synthetases GARS1 and TARS1; RNA processing and regulation through DDX5; mitochondrial and peroxisomal dynamics through DNM1L; and endosomal protein trafficking through VPS35. The subgraph is therefore most consistent with a cellular proteostasis, translation, RNA-processing, organelle-maintenance, and intracellular-trafficking program rather than a narrowly specialized tissue pathway. The relatively sparse direct connectivity also argues against treating the module as a single established molecular complex.

**Cell composition.** The HPA profile does not support a blood-derived explanation: the genes have low immune-cell specificity and no enriched blood-cell pattern. It also does not support a module dominated by secreted plasma proteins; only a minority are classified as secreted, while the annotated proteins are mainly intracellular, cytosolic, nuclear, endoplasmic-reticulum, or endosomal. Most genes have low tissue specificity and low cell-type specificity, which is compatible with broadly expressed housekeeping or stress-responsive biology. The liver and myometrium detection pattern is therefore more consistent with shared cellular maintenance requirements than with a tissue-exclusive program. SERPINH1 has cell-type-enhanced annotation in stromal and trophoblast-related populations, while HSP90AA1 has cell-type-enhanced annotation in ductal populations, but these observations do not establish that such cell types caused the shared module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a direct relationship between DNM1L and VPS35 and a direct relationship between GARS1 and TARS1. The supplementary STRING tissue result (STRING TISSUES Testis; within-query FDR = 0.0068) links most of the module to a testis-associated tissue annotation, but this is not global GO/KEGG evidence and should not be interpreted as proof of a testis-specific function. The remaining module connections are weaker or are not represented as high-confidence STRING interactions. No hu.MAP complex contains multiple module members. Thus, the module combines some known pairwise relationships with a broader co-abundance pattern that is not currently represented as an established multiprotein complex.

**STRING interactions (score >= 0.7)**: 2 of 28 gene pairs: DNM1L–VPS35 (0.9); GARS1–TARS1 (0.909)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Testis (FDR = 0.0068, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a new co-abundance association, but it should not be called a newly discovered molecular pathway. The presence of known relationships, especially DNM1L with VPS35 and GARS1 with TARS1, indicates that parts of the module recover established biology. Conversely, the absence of a hu.MAP complex and the limited set of high-confidence STRING links mean that the complete liver–myometrium co-abundance configuration is not directly supported as a previously catalogued complex. Absence from STRING or hu.MAP alone does not prove novelty. The most defensible conclusion is that the tissue-shared co-abundance organization is potentially novel, while its component functions are largely established.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular quality-control and resource-management state present in liver and myometrium. Chaperone activity and collagen-related folding through HSP90 proteins and SERPINH1 could help maintain proteome and extracellular-matrix protein production; GARS1 and TARS1 could represent translational demand; DDX5 could couple RNA processing to that demand; and DNM1L together with VPS35 could connect organelle dynamics and endosomal trafficking. The observed co-abundance may therefore arise when cells coordinate protein production, folding, trafficking, and organelle maintenance. This remains a hypothesis because the module lacks globally significant GO/KEGG enrichment and lacks a hu.MAP complex containing multiple members.

### Important genes

#### DNM1L

- **Related proteins** (co-abundance neighbors): HSP90AB2P (0.88); STRING partners: VPS35 (0.9)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 1L. This gene encodes a member of the dynamin superfamily of GTPases. The encoded protein mediates mitochondrial and peroxisomal division, and is involved in developmentally regulated apoptosis and programmed necrosis. Dysfunction of this gene is implicated in several neurological disorders, including Alzheimer's disease. Mutations in this gene are associated with the autosomal dominant disorder, ence…
- **Diseases (Open Targets)**: encephalopathy, lethal, due to defective mitochondrial peroxisomal fission 1 (0.815); autosomal dominant optic atrophy, classic form (0.721); neurodegenerative disease (0.531); encephalopathy due to mitochondrial and peroxisomal fission defect (0.455); hereditary disease (0.451)
- **Europe PMC papers**: 3015
- **Why important**: DNM1L provides a strong functional anchor for organelle maintenance because it mediates mitochondrial and peroxisomal fission and is involved in apoptosis-related processes. It is connected in the module to HSP90AB2P and has a known STRING relationship with VPS35. Its extensive literature and disease associations involving mitochondrial and peroxisomal fission make it an important interpretive bridge between proteostasis and organelle biology.
- **Conclusion**: Established evidence supports DNM1L as an organelle-dynamics gene with relevant neurological disease associations and a known relationship to VPS35. Its participation in a shared liver–myometrium maintenance program is plausible but remains an interpretation of the co-abundance pattern, not a demonstrated tissue-specific mechanism.

#### VPS35

- **Related proteins** (co-abundance neighbors): TARS1 (0.86); STRING partners: DNM1L (0.9)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS35 retromer complex component. This gene belongs to a group of vacuolar protein sorting (VPS) genes. The encoded protein is a component of a large multimeric complex, termed the retromer complex, involved in retrograde transport of proteins from endosomes to the trans-Golgi network. The close structural similarity between the yeast and human proteins that make up this complex suggests a similarity in function. Expression studie…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.743); neurodegenerative disease (0.553); young-onset Parkinson disease (0.503); Parkinson disease (0.482); Parkinson disease, dominant (0.370)
- **Europe PMC papers**: 3611
- **Why important**: VPS35 is the central retromer component represented in the module and connects to TARS1 in the co-abundance graph and to DNM1L in STRING. Its established role in endosomal-to-trans-Golgi retrograde transport and lysosome-related organization gives the module a protein-trafficking dimension. Its substantial literature and Parkinson disease associations further support its biological importance.
- **Conclusion**: Established evidence supports VPS35 as a retromer and endosomal-trafficking factor with disease relevance. The link between trafficking, translation, and organelle dynamics in this module is a hypothesis rather than an experimentally established joint pathway.

#### GARS1

- **Related proteins** (co-abundance neighbors): TARS1 (0.87), HSP90AB2P (0.85), HSP90AA1 (0.81); STRING partners: TARS1 (0.909)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycyl-tRNA synthetase 1. This gene encodes glycyl-tRNA synthetase, one of the aminoacyl-tRNA synthetases that charge tRNAs with their cognate amino acids. The encoded enzyme is an (alpha)2 dimer which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Two transcript variants encoding different isoforms ha…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease type 2D (0.790); neuronopathy, distal hereditary motor, type 5A (0.729); neuronopathy, distal hereditary motor, type 5 (0.698); spinal muscular atrophy, infantile, James type (0.649); Charcot-Marie-Tooth disease type 2 (0.565)
- **Europe PMC papers**: 302
- **Why important**: GARS1 has a relatively prominent position in the module and connects HSP90AB2P, HSP90AA1, and TARS1. It encodes glycyl-tRNA synthetase, making it a direct marker of translational capacity, and it forms the strongest represented STRING pair with TARS1 (STRING TISSUES Testis; within-query FDR = 0.0068). Its associations with inherited motor-neuron and peripheral-nerve disorders and its substantial literature make it an informative functional representative.
- **Conclusion**: Established evidence supports GARS1 as a glycyl-tRNA synthetase involved in protein translation and as a gene associated with several neurological disorders. Its co-abundance with chaperones may indicate coordinated translational and folding demand, but that coordination is not proven by the supplied data.

#### SERPINH1

- **Related proteins** (co-abundance neighbors): HSP90AB2P (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family H member 1. This gene encodes a member of the serpin superfamily of serine proteinase inhibitors. The encoded protein is localized to the endoplasmic reticulum and plays a role in collagen biosynthesis as a collagen-specific molecular chaperone. Autoantibodies to the encoded protein have been found in patients with rheumatoid arthritis. Expression of this gene may be a marker for cancer, and nucleotide polymo…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 10 (0.714); preterm premature rupture of the membranes (0.559); coronary artery disorder (0.554); myocardial infarction (0.510); Abnormality of the skeletal system (0.474)
- **Europe PMC papers**: 2762
- **Why important**: SERPINH1 contributes a distinct endoplasmic-reticulum and extracellular-matrix angle. It is a collagen-specific molecular chaperone, is linked to collagen fibril organization, and is cell-type enhanced in stromal and trophoblast-related populations in HPA. Its position beside HSP90AB2P and its disease associations involving connective tissue and pregnancy-related phenotypes make it important for interpreting the module beyond generic translation.
- **Conclusion**: Established evidence supports SERPINH1 as an endoplasmic-reticulum collagen chaperone with connective-tissue and reproductive disease relevance. Its presence may indicate matrix-production or folding demand in myometrium, but it does not establish that the whole module is a collagen pathway.

#### DDX5

- **Related proteins** (co-abundance neighbors): HSP90AB2P (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in liver, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 adds nuclear RNA biology to a module otherwise rich in protein-folding, translation, trafficking, and organelle functions. It is an RNA helicase and adaptor involved in RNA structure remodeling, transcriptional regulation, splicing, and small noncoding-RNA processing. Its extensive literature and cancer-related disease associations make it an important candidate for linking transcript processing with downstream proteome maintenance.
- **Conclusion**: Established evidence supports DDX5 as a multifunctional RNA-processing and transcriptional regulator. Its role in this module is most reasonably interpreted as a possible upstream coordinator of cellular state, while any direct regulatory connection to the other module members remains hypothetical.
