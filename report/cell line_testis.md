# Conserved co-abundance modules: cell line and testis

## Module 0

**Tissue pair**: cell line and testis  
**Genes (20)**: ACACA, ACSS2, ADD3, AP3D1, ARFGEF1, COG1, DCTN1, EML4, RNMT, MTA2, MYO1C, NAA15, DCN, PYGB, SEC24D, SF3A1, SPTBN1, FARSB, CCT5, CCT8

### Function

No GO or KEGG term passed global correction, so there is no globally significant annotation-based functional enrichment to interpret. STRING functional enrichment was also absent. The network is therefore best viewed as a mixed cellular-state module rather than evidence for one established pathway. Its structure combines a highly connected DCN hub with peripheral genes involved in extracellular-matrix biology, protein folding, vesicle and Golgi trafficking, actin and microtubule organization, RNA processing, translation, and acetyl-CoA or lipid metabolism. The strongest coherent substructures are the CCT5-CCT8 chaperonin pair, the ACSS2-ACACA metabolic link, and the DCTN1-EML4 microtubule-associated link. These relationships support coordinated cellular organization and biosynthetic capacity, but the absence of globally significant GO or KEGG terms means that a more specific pathway assignment would be hypothesis rather than established enrichment.

**Cell composition.** The module is not dominated by plasma or secreted proteins: DCN is the sole gene annotated as secreted to the extracellular matrix. Most genes have low tissue specificity, while many are cell-type enhanced across diverse populations, including adipocytes, neutrophil-lineage cells, neurons, colonocytes, germ-cell populations, and stromal cells. Immune-cell specificity is generally low, with only limited immune enhancement or enrichment. This pattern argues against a simple blood-cell contamination explanation, although the DCN hub and its stromal or fibroblast associations leave shared stromal or extracellular-matrix content as a plausible contributor. HPA protein detection is available for testis but not as a matched cell-line tissue comparison, so the apparent sharing should not be interpreted as proof of identical protein abundance in the two sample groups.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports three particularly clear physical or functional relationships: ACACA with ACSS2, CCT5 with CCT8, and DCTN1 with EML4. The CCT5-CCT8 pair is additionally represented in each of the listed hu.MAP complexes, identified by tags (hu.MAP huMAP3_07938.1), (hu.MAP huMAP3_06559.1), (hu.MAP huMAP3_09191.1), (hu.MAP huMAP3_10656.1), and (hu.MAP huMAP3_14584.1). In every case, the module contributes only a small pair of members to a much larger complex, so these hu.MAP results validate a known chaperonin context rather than defining a module-specific complex. The remaining module genes have no reported STRING partners or hu.MAP complex membership in the supplied evidence. In particular, DCN has no listed STRING or hu.MAP relationship despite being the central co-abundance hub. Thus, the co-abundance edges are not generally equivalent to known physical interactions; they may reflect shared cell composition, shared regulation, or coordinated cellular state.

**STRING interactions (score >= 0.7)**: 3 of 190 gene pairs: ACACA–ACSS2 (0.97); CCT5–CCT8 (0.999); DCTN1–EML4 (0.749)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT8; 2/23); huMAP3_06559.1 (CCT5, CCT8; 2/25); huMAP3_09191.1 (CCT5, CCT8; 2/32); huMAP3_10656.1 (CCT5, CCT8; 2/36); huMAP3_14584.1 (CCT5, CCT8; 2/61)

### Novelty

The module may represent a new cross-context co-abundance pattern, because the supplied data do not identify a previously defined module with this exact combination of genes and the network is not explained by one known complex. However, it is not a new discovery of the individual biology: the CCT chaperonin relationship, acetyl-CoA and lipid enzymes, vesicle-trafficking proteins, cytoskeletal proteins, and DCN extracellular-matrix biology are already established. The lack of STRING or hu.MAP links for many co-abundance pairs does not prove novelty, since those resources emphasize curated or experimentally supported physical and functional relationships rather than every co-regulated abundance pattern. The defensible conclusion is novelty of the integrated co-abundance association is possible, but it requires replication, independent cohorts, and comparison with existing co-expression modules before being called a new biological module.

**Hypothesis.** Hypothesis: this shared module reflects a conserved cellular program coupling extracellular-matrix or stromal context, cytoskeletal and microtubule organization, protein folding, secretory-pathway trafficking, and anabolic carbon metabolism. DCN may mark the cellular context, while the CCT pair supports folding of cytoskeletal or other newly synthesized proteins, ACSS2 and ACACA support acetyl-CoA-dependent lipid anabolism, and the trafficking and cytoskeletal genes support movement and delivery of cellular cargo. In testis, this could be compatible with support of germ-cell or somatic-cell architecture and biosynthetic demand; in cell lines, it could instead reflect a shared growth or culture-state program. This is a mechanistic model, not a conclusion from significant pathway enrichment.

### Important genes

#### DCN

- **Related proteins** (co-abundance neighbors): AP3D1 (0.85), MTA2 (0.85), SF3A1 (0.84), FARSB (0.83), DCTN1 (0.83), EML4 (0.82), CCT5 (0.82), ADD3 (0.82), CCT8 (0.82), RNMT (0.81), ACACA (0.81), PYGB (0.81), SEC24D (0.81), MYO1C (0.80), SPTBN1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: decorin. This gene encodes a member of the small leucine-rich proteoglycan family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature protein. This protein plays a role in collagen fibril assembly. Binding of this protein to multiple cell surface receptors mediates its role in tumor…
- **Diseases (Open Targets)**: congenital stromal corneal dystrophy (0.696); lagophthalmos (0.295); refractive error (0.234); type 2 diabetes mellitus (0.224); hereditary disease (0.193)
- **Europe PMC papers**: 11630
- **Why important**: DCN is the network hub with the broadest connectivity and links genes spanning trafficking, RNA processing, translation, cytoskeletal organization, metabolism, and chaperoning. It is the only secreted extracellular-matrix component in the module, is enhanced in stromal and fibroblast-related cell types, and has an extensive literature including collagen fibril assembly, autophagy, inflammation, angiogenesis, and tumor-suppressive receptor signaling. Its disease associations include congenital stromal corneal dystrophy and metabolic disease. The hub position makes DCN important for interpreting module context, but not proof that DCN physically regulates every neighbor.
- **Conclusion**: Established: DCN is an extracellular-matrix proteoglycan with collagen-assembly and cell-signaling functions and is the central co-abundance gene. Hypothesis: DCN may be a marker of a stromal or matrix-associated cellular state that brings otherwise diverse intracellular genes into the shared module.

#### CCT5

- **Related proteins** (co-abundance neighbors): DCN (0.82); STRING partners: CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is part of the CCT chaperonin, and it has a direct high-confidence STRING relationship with CCT8. Both genes occur together in the listed hu.MAP complexes (hu.MAP huMAP3_07938.1), (hu.MAP huMAP3_06559.1), (hu.MAP huMAP3_09191.1), (hu.MAP huMAP3_10656.1), and (hu.MAP huMAP3_14584.1), providing the clearest complex-level support in the module. CCT5 folds newly synthesized proteins, including actin and tubulin, which connects its established function to the module's cytoskeletal and cell-architecture signals. It also has a disease association with hereditary sensory and autonomic neuropathy with spastic paraplegia.
- **Conclusion**: Established: CCT5 is a CCT chaperonin subunit and its relationship with CCT8 is supported by STRING and hu.MAP. Hypothesis: coordinated CCT5 and CCT8 abundance could buffer protein-folding demand associated with cytoskeletal remodeling or germ-cell development.

#### CCT8

- **Related proteins** (co-abundance neighbors): DCN (0.82), FARSB (0.81); STRING partners: CCT5 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is the partner of CCT5 in the best-supported physical substructure and is represented in all the listed hu.MAP complexes. Its annotated functions include protein folding, protein stabilization, and protein localization. HPA places it in the testis connecting and end regions and in oocyte-enhanced cells, making it particularly relevant to the shared testis context. Its literature and disease associations are more limited than those of the major hub genes, but its network and complex position are unusually informative.
- **Conclusion**: Established: CCT8 is a CCT chaperonin subunit with strong support for partnership with CCT5. Hypothesis: CCT8 may help couple proteostasis to the specialized cytoskeletal or structural requirements of testicular cells, although the module does not establish a testis-specific mechanism.

#### ACSS2

- **Related proteins** (co-abundance neighbors): SEC24D (0.83); STRING partners: ACACA (0.97)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase short chain family member 2. This gene encodes a cytosolic enzyme that catalyzes the activation of acetate for use in lipid synthesis and energy generation. The protein acts as a monomer and produces acetyl-CoA from acetate in a reaction that requires ATP. Expression of this gene is regulated by sterol regulatory element-binding proteins, transcription factors that activate genes required for the synthesis of cholesterol and …
- **Diseases (Open Targets)**: neurodegenerative disease (0.371); orofacial cleft (0.333); autoimmune disorder of central nervous system (0.261); coronary artery disorder (0.152); delusional disorder (0.142)
- **Europe PMC papers**: 2948
- **Why important**: ACSS2 is directly linked to ACACA in STRING and provides a metabolic anchor distinct from the chaperonin substructure. It activates acetate to acetyl-CoA for lipid synthesis and energy generation, while its expression is regulated by sterol regulatory element-binding proteins. HPA reports tissue enhancement in skeletal muscle and cell-type enhancement in several metabolically active cell types, including adipocytes and cardiomyocytes. Its disease associations include neurodegenerative and coronary disorders, and it has substantial literature.
- **Conclusion**: Established: ACSS2 supplies acetyl-CoA from acetate and is linked to ACACA in STRING. Hypothesis: the ACSS2-ACACA pair may indicate coordinated lipid-anabolic or energy-adaptation demands in the shared module, but this cannot be called an enriched metabolic pathway.

#### ACACA

- **Related proteins** (co-abundance neighbors): DCN (0.81); STRING partners: ACSS2 (0.97)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA carboxylase alpha. Acetyl-CoA carboxylase (ACC) is a complex multifunctional enzyme system. ACC is a biotin-containing enzyme which catalyzes the carboxylation of acetyl-CoA to malonyl-CoA, the rate-limiting step in fatty acid synthesis. There are two ACC forms, alpha and beta, encoded by two different genes. ACC-alpha is highly enriched in lipogenic tissues. The enzyme is under long term control at the transcriptio…
- **Diseases (Open Targets)**: neurodegenerative disease (0.550); Alzheimer disease (0.463); lysosomal storage disease (0.460); Parkinson disease (0.460); autoimmune disorder of central nervous system (0.383)
- **Europe PMC papers**: 6268
- **Why important**: ACACA is the complementary member of the STRING-supported ACACA-ACSS2 pair and catalyzes the rate-limiting step in fatty-acid synthesis by producing malonyl-CoA. It is a well-studied metabolic enzyme with extensive literature and disease associations spanning neurodegenerative and lysosomal disorders. Its placement next to ACSS2 gives the module a plausible biochemical connection between acetate activation and fatty-acid biosynthesis, even though the co-abundance graph gives it only a peripheral position.
- **Conclusion**: Established: ACACA performs a central fatty-acid-biosynthetic reaction and has a known STRING relationship with ACSS2. Hypothesis: ACACA and ACSS2 may report a shared anabolic state rather than a direct module-specific regulatory circuit.

## Module 1

**Tissue pair**: cell line and testis  
**Genes (9)**: ACSL3, COPB1, GARS1, SEC24C, DARS2, IARS1, LARS1, RARS1, XPO1

### Function

This is a translation-support module centered on aminoacyl-tRNA charging. The strongest primary evidence is the convergence of (GO:MF aminoacyl-tRNA ligase activity; q_global = 0.000418) through (GO:MF catalytic activity, acting on RNA; q_global = 0.0206) on aminoacyl-tRNA ligase activity, tRNA aminoacylation, amino acid activation, tRNA metabolism, and catalytic activity on RNA. (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 0.000418) independently identifies aminoacyl-tRNA biosynthesis as the corresponding KEGG pathway. The module therefore most directly represents coordinated support for translational fidelity and protein synthesis, rather than a tissue-specific signaling pathway. (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.0222) further supports participation of IARS1, LARS1, and RARS1 in an aminoacyl-tRNA synthetase multienzyme complex. The presence of ACSL3, XPO1, SEC24C, and COPB1 suggests links to lipid activation, nuclear transport, and intracellular vesicle trafficking, but these peripheral annotations do not replace the dominant aminoacylation interpretation.

**Cell composition.** The module is not dominated by plasma proteins, secreted proteins, or blood-cell-enriched genes. HPA reports low immune-cell specificity for all module genes and only one secreted annotation, while the tissue profiles are predominantly low-specificity. Most members are intracellular enzymes or transport and trafficking proteins, consistent with broadly expressed housekeeping-type biology. HPA detects all module proteins in testis, but this does not by itself establish a testis-specific program. The shared signal between cell line and testis is therefore more  plausibly a conserved cellular process, such as translation capacity, than blood contamination or a shared blood-cell composition effect. ACSL3 is the main tissue- and cell-type-enriched exception, with annotations involving parathyroid gland, neutrophils, prostatic glandular cells, and other cell types.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF aminoacyl-tRNA ligase activity | 0.000418 | DARS2, GARS1, IARS1, LARS1, RARS1 |
| GO:BP tRNA aminoacylation for protein translation | 0.000418 | DARS2, GARS1, IARS1, LARS1, RARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 0.000418 | DARS2, GARS1, IARS1, LARS1, RARS1 |
| GO:BP amino acid activation | 0.000418 | DARS2, GARS1, IARS1, LARS1, RARS1 |
| GO:BP tRNA aminoacylation | 0.000418 | DARS2, GARS1, IARS1, LARS1, RARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 0.000418 | DARS2, GARS1, IARS1, LARS1, RARS1 |
| GO:MF catalytic activity, acting on a tRNA | 0.00111 | DARS2, GARS1, IARS1, LARS1, RARS1 |
| GO:MF ligase activity | 0.0015 | ACSL3, DARS2, GARS1, IARS1, LARS1, RARS1 |
| GO:BP tRNA metabolic process | 0.00202 | DARS2, GARS1, IARS1, LARS1, RARS1 |
| GO:MF catalytic activity, acting on RNA | 0.0206 | DARS2, GARS1, IARS1, LARS1, RARS1 |
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 0.0222 | IARS1, LARS1, RARS1 |

### STRING and hu.MAP

STRING strongly supports a pre-existing aminoacyl-tRNA synthetase relationship among DARS2, GARS1, IARS1, LARS1, and RARS1: these genes account for the convergent STRING enrichment in (STRING KEGG Aminoacyl-tRNA biosynthesis; within-query FDR = 5.38e-05) through (STRING NetworkNeighborAL tRNA Aminoacylation; within-query FDR = 0.0034), including tRNA aminoacylation and protein biosynthesis. STRING also supports the COPB1-SEC24C pair, linking coatomer and COPII-related trafficking. The strongest internal relationships are concentrated among IARS1, LARS1, RARS1, and GARS1, with DARS2 connected to several of them. hu.MAP independently places IARS1, LARS1, and RARS1 together in the complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), alongside additional aminoacyl-tRNA synthetases and auxiliary factors. The hu.MAP association of XPO1 and ACSL3 in (hu.MAP huMAP3_09592.1) is broader and less specific because that complex contains many proteins from transport, lipid, membrane, and organelle biology. Thus, the network contains a well-supported synthetase core, a supported trafficking pair, and more tentative peripheral connections.

**STRING interactions (score >= 0.7)**: 9 of 36 gene pairs: COPB1–SEC24C (0.714); DARS2–IARS1 (0.807); DARS2–RARS1 (0.728); GARS1–IARS1 (0.97); GARS1–LARS1 (0.895); GARS1–RARS1 (0.892); IARS1–LARS1 (0.999); IARS1–RARS1 (0.999); LARS1–RARS1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Aminoacyl-tRNA biosynthesis (FDR = 5.38e-05, 5 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 8.07e-05, 5 genes); Keyword Ligase (FDR = 8.07e-05, 6 genes); Function aminoacyl-tRNA ligase activity (FDR = 0.00022, 5 genes); Function Ligase activity (FDR = 0.00022, 6 genes); NetworkNeighborAL tRNA Aminoacylation (FDR = 0.00028, 5 genes); RCTM tRNA Aminoacylation (FDR = 0.00035, 5 genes); Keyword Protein biosynthesis (FDR = 0.00036, 5 genes); Process tRNA aminoacylation for protein translation (FDR = 0.001, 5 genes); RCTM Cytosolic tRNA aminoacylation (FDR = 0.002, 4 genes); Process Amide biosynthetic process (FDR = 0.0023, 6 genes); NetworkNeighborAL tRNA Aminoacylation (FDR = 0.0034, 4 genes); Component aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.022, 3 genes); InterPro Aminoacyl-tRNA synthetase, class Ia, anticodon-binding (FDR = 0.0223, 3 genes); InterPro Aminoacyl-tRNA synthetase, class I, conserved site (FDR = 0.0281, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (IARS1, RARS1, LARS1; 3/14); huMAP3_13688.1 (IARS1, RARS1, LARS1; 3/14); huMAP3_09592.1 (XPO1, ACSL3; 2/95)

### Novelty

The module should not be described as a newly discovered aminoacyl-tRNA synthetase complex or as evidence for previously unknown protein relationships. Its central biology is already represented in STRING and hu.MAP, and the primary enrichment terms are canonical. The potentially new observation is the coordinated co-abundance of this established translation-related core with the peripheral genes in the shared cell-line and testis context. That cross-context co-abundance pattern may be biologically informative, but novelty cannot be established from this fact sheet alone. Absence of hu.MAP or STRING support for individual peripheral edges is not evidence that those relationships are novel; it may reflect incomplete coverage, indirect co-regulation, or context-dependent association.

**Hypothesis.** Hypothesis: the module reflects a conserved increase or decrease in cellular translational capacity, in which coordinated expression of cytosolic aminoacyl-tRNA synthetases helps maintain accurate tRNA charging while mitochondrial DARS2 links the program to organelle protein synthesis and metabolic state. The association with XPO1 may reflect coupling to RNA and ribosome-related nuclear export, whereas SEC24C and COPB1 may reflect the broader biosynthetic and membrane-trafficking demands of cells with altered protein production. ACSL3 could connect this state to fatty-acid activation, but that connection remains a testable hypothesis rather than an established property of the core module.

### Important genes

#### IARS1

- **Related proteins** (co-abundance neighbors): LARS1 (0.94), DARS2 (0.86), RARS1 (0.83), SEC24C (0.81); STRING partners: DARS2 (0.807), GARS1 (0.97), LARS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Isoleucine-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family and has been identified as a …
- **Diseases (Open Targets)**: growth retardation, intellectual developmental disorder, hypotonia, and hepatopathy (0.733); Abnormality of the skeletal system (0.332); microcephaly (0.289); Global developmental delay (0.289); Hallux valgus (0.184)
- **Europe PMC papers**: 184
- **Why important**: IARS1 is a central core member with strong connections to DARS2, GARS1, LARS1, and RARS1. It appears in every primary enrichment category from (GO:MF aminoacyl-tRNA ligase activity; q_global = 0.000418) through (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.0222), every relevant STRING enrichment from (STRING KEGG Aminoacyl-tRNA biosynthesis; within-query FDR = 5.38e-05) through (STRING InterPro Aminoacyl-tRNA synthetase, class I, conserved site; within-query FDR = 0.0281), and both synthetase complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Its established function is isoleucyl-tRNA charging and participation in translational fidelity. The gene is associated with developmental and skeletal abnormalities and has been implicated as an autoantibody target in polymyositis and dermatomyositis. Its literature volume is more limited than that of the best-studied peripheral genes, which makes its repeated network and complex support especially important.
- **Conclusion**: Established conclusion: IARS1 is a core molecular marker of the module's aminoacylation function and likely contributes directly to its translation-related signal. Hypothesis: variation in IARS1 abundance could help tune translational fidelity in both cell-line and testis contexts, but the co-abundance data do not demonstrate causality.

#### LARS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.94), DARS2 (0.82); STRING partners: GARS1 (0.895), IARS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: leucyl-tRNA synthetase 1. This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals w…
- **Diseases (Open Targets)**: infantile liver failure syndrome 1 (0.670); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.510); Global developmental delay (0.119); sensorineural hearing loss disorder (0.119); Generalized-onset seizure (0.118)
- **Europe PMC papers**: 267
- **Why important**: LARS1 is embedded in the synthetase core, has a strong connection to IARS1, and is present in (GO:MF aminoacyl-tRNA ligase activity; q_global = 0.000418) through (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.0222), (STRING KEGG Aminoacyl-tRNA biosynthesis; within-query FDR = 5.38e-05) through (STRING InterPro Aminoacyl-tRNA synthetase, class I, conserved site; within-query FDR = 0.0281), and (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). It is an established cytosolic leucine-tRNA synthetase and a component of the multisynthetase complex, with a known interaction through its C-terminal domain with arginyl-tRNA synthetase. Its disease associations include infantile liver failure syndrome and additional developmental and neurological phenotypes. Its literature volume is substantial enough to support a mature functional interpretation.
- **Conclusion**: Established conclusion: LARS1 is a core component of the translation and amino acid sensing machinery represented by this module. Hypothesis: its presence may couple leucine-responsive cellular state to translational output, although the module does not prove that leucine sensing drives the observed co-abundance.

#### RARS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.83); STRING partners: DARS2 (0.728), GARS1 (0.892), IARS1 (0.999), LARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 is part of the densely supported synthetase core and occurs in all primary enrichment terms, all listed STRING functional enrichments, and both hu.MAP synthetase complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). It encodes the cytosolic arginyl-tRNA synthetase and has established associations with leukodystrophy and other hereditary neurological disease. Although its direct module connectivity is peripheral relative to IARS1, LARS1, and DARS2, its repeated STRING and complex support makes it a strong biological anchor.
- **Conclusion**: Established conclusion: RARS1 reinforces that the module represents a coordinated aminoacyl-tRNA synthetase program rather than an isolated pair of correlated genes. Hypothesis: RARS1 abundance may contribute to translational robustness in the shared cell-line and testis state, but this requires perturbation or functional validation.

#### DARS2

- **Related proteins** (co-abundance neighbors): IARS1 (0.86), LARS1 (0.82), XPO1 (0.80), ACSL3 (0.80), GARS1 (0.80); STRING partners: IARS1 (0.807), RARS1 (0.728)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 2, mitochondrial. The protein encoded by this gene belongs to the class-II aminoacyl-tRNA synthetase family. It is a mitochondrial enzyme that specifically aminoacylates aspartyl-tRNA. Mutations in this gene are associated with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation (LBSL). [provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: leukoencephalopathy with brain stem and spinal cord involvement-high lactate syndrome (0.843); neurodegenerative disease (0.527); hereditary disease (0.518); hypertensive disorder (0.425); Cerebral cortical atrophy (0.425)
- **Europe PMC papers**: 796
- **Why important**: DARS2 has the broadest network connectivity in the module and links the synthetase core to ACSL3 and XPO1 as well as to other aminoacylation genes. It is included in (GO:MF aminoacyl-tRNA ligase activity; q_global = 0.000418) through (GO:MF catalytic activity, acting on RNA; q_global = 0.0206) and in the main STRING aminoacylation enrichments (STRING KEGG Aminoacyl-tRNA biosynthesis; within-query FDR = 5.38e-05) through (STRING Process Amide biosynthetic process; within-query FDR = 0.0023). Its established function is mitochondrial aspartyl-tRNA synthetase activity, connecting the module to mitochondrial translation. Mutations are associated with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation, and it has a substantial literature base.
- **Conclusion**: Established conclusion: DARS2 is the key mitochondrial and network-bridging component of the module. Hypothesis: DARS2 may couple mitochondrial protein synthesis or energetic state to the cytosolic synthetase program, but the observed edges do not establish a direct regulatory mechanism.

#### GARS1

- **Related proteins** (co-abundance neighbors): DARS2 (0.80); STRING partners: IARS1 (0.97), LARS1 (0.895), RARS1 (0.892)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycyl-tRNA synthetase 1. This gene encodes glycyl-tRNA synthetase, one of the aminoacyl-tRNA synthetases that charge tRNAs with their cognate amino acids. The encoded enzyme is an (alpha)2 dimer which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Two transcript variants encoding different isoforms ha…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease type 2D (0.790); neuronopathy, distal hereditary motor, type 5A (0.729); neuronopathy, distal hereditary motor, type 5 (0.698); spinal muscular atrophy, infantile, James type (0.649); Charcot-Marie-Tooth disease type 2 (0.565)
- **Europe PMC papers**: 302
- **Why important**: GARS1 is a glycine-tRNA synthetase and is repeatedly supported by (GO:MF aminoacyl-tRNA ligase activity; q_global = 0.000418) through (GO:MF catalytic activity, acting on RNA; q_global = 0.0206) and (STRING KEGG Aminoacyl-tRNA biosynthesis; within-query FDR = 5.38e-05) through (STRING NetworkNeighborAL tRNA Aminoacylation; within-query FDR = 0.0034). STRING places it in strong relationships with IARS1, LARS1, and RARS1, making it an important member of the synthetase core even though its direct co-abundance connectivity in the displayed module is limited. It has established associations with Charcot-Marie-Tooth disease and several hereditary motor neuron or neuronopathy phenotypes, as well as autoimmune relevance through polymyositis and dermatomyositis. Its literature volume supports extensive prior biological knowledge.
- **Conclusion**: Established conclusion: GARS1 independently confirms the module's translation-related identity and its known synthetase network. Hypothesis: coordinated GARS1 abundance may help preserve balanced charging across amino acids, but balance across synthetases cannot be inferred from co-abundance alone.

## Module 2

**Tissue pair**: cell line and testis  
**Genes (15)**: AKAP4, CFAP20, SLC25A10, EFHC1, ELAPOR1, GK2, AK7, NUP188, MT-ND4, NUP35, UQCRC2, RUVBL2, SCCPDH, CCT6B, SLC25A19

### Function

The module is best interpreted as a sperm- and motile-cilium-associated program involving flagellar structure, cilium movement, and cellular motility. Globally corrected GO evidence supports flagellated sperm motility, sperm motility, motile cilium, and cilium-dependent cell motility (6 globally significant GO/KEGG terms, q_global 0.0209–0.038; see the table). AKAP4, CFAP20, EFHC1, and GK2 recur across the sperm-motility terms, while AK7 also contributes to the motile-cilium term (GO:CC motile cilium; q_global = 0.0303). Other module genes represent supporting processes, including mitochondrial respiration, metabolite transport, protein folding, nuclear transport, and autophagy-related biology. These ancillary annotations may reflect the energetic, proteostatic, and developmental requirements of differentiating germ cells or ciliated cells. No KEGG term is provided as primary evidence.

**Cell composition.** The module contains no secreted genes according to HPA, so it is not primarily a plasma or secreted-protein module. Its HPA profile is strongly compatible with testicular germ-cell and ciliated-cell biology. Late spermatids, late primary spermatocytes, and early spermatids are frequent enriched cell types, and testis is the most frequent enriched tissue. AKAP4, GK2, CCT6B, and RUVBL2 show testis-enriched or testis-enhanced patterns, while EFHC1, AK7, and CFAP20 are associated with ciliated cell types. Some genes have immune-cell annotations, including basophil, neutrophil, NK-cell, and plasmacytoid dendritic cell associations, but the overall pattern is more consistent with germ-cell and ciliated-cell composition than with blood contamination. Several genes have low or broad tissue specificity, indicating that shared housekeeping or organelle functions may also contribute. HPA protein detection is available for most genes in testis, but the cell-line comparison has no matching HPA tissue evidence, so HPA cannot determine the source of the cell-line signal.

**GO/KEGG enrichment**: 6 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP flagellated sperm motility | 0.0209 | AKAP4, CFAP20, EFHC1, GK2 |
| GO:BP sperm motility | 0.0209 | AKAP4, CFAP20, EFHC1, GK2 |
| GO:CC motile cilium | 0.0303 | AK7, AKAP4, CFAP20, EFHC1, GK2 |
| GO:BP cilium or flagellum-dependent cell motility | 0.038 | AKAP4, CFAP20, EFHC1, GK2 |
| GO:BP cilium-dependent cell motility | 0.038 | AKAP4, CFAP20, EFHC1, GK2 |
| GO:BP cilium movement involved in cell motility | 0.038 | AKAP4, CFAP20, EFHC1, GK2 |

### STRING and hu.MAP

The network is sparse and does not correspond to one established protein complex. STRING supports CFAP20–EFHC1, linking two genes with ciliary or sperm-motility relevance. It also supports MT-ND4–UQCRC2, consistent with a mitochondrial respiratory-chain relationship, and NUP188–NUP35, consistent with a nuclear-pore relationship. STRING reports no functional enrichment for the module, and hu.MAP reports no complex containing multiple module members. Thus, some relationships are already known, but most co-abundance edges are not supported by the supplied physical-interaction or complex resources. The module may combine a ciliary or sperm-motility core with mitochondrial, nuclear-transport, chaperone, and metabolic context rather than representing one canonical complex.

**STRING interactions (score >= 0.7)**: 3 of 105 gene pairs: CFAP20–EFHC1 (0.908); MT-ND4–UQCRC2 (0.953); NUP188–NUP35 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a plausible biological module, but it should not be described as a newly discovered molecular complex. The globally corrected GO results provide convergent evidence for sperm-motility and motile-cilium biology (6 globally significant GO/KEGG terms, q_global 0.0209–0.038; see the table), and the HPA profile independently agrees with spermatogenic and ciliated-cell biology. Conversely, limited STRING support, absence of a hu.MAP complex, and inclusion of mitochondrial, nuclear-pore, metabolic, and chaperone genes argue against claiming that the complete gene set is an established pathway. Absence from STRING or hu.MAP alone does not prove novelty. A cautious interpretation is that this may be a new tissue-pair or context-specific co-abundance association organized around a known spermatogenic or ciliary program. Independent replication and comparison with published sperm and cilia modules would be needed to establish novelty.

**Hypothesis.** Hypothesis: the module reflects a coordinated program in differentiating germ cells or related ciliated cells that couples axoneme assembly and motility regulation to energy supply, calcium-sensitive control, protein folding, nuclear transport, and metabolite handling. AKAP4, CFAP20, EFHC1, and AK7 may represent the motility-facing component, while mitochondrial genes may support the energy demands of movement and CCT6B, nucleoporins, and transport proteins may support maturation and cellular organization. The co-abundance pattern may therefore arise because these processes are activated together during spermatid differentiation or ciliated-cell specialization. This is a mechanistic hypothesis and does not establish direct physical interaction among all module members.

### Important genes

#### EFHC1

- **Related proteins** (co-abundance neighbors): RUVBL2 (0.94), GK2 (0.92), UQCRC2 (0.81), SCCPDH (0.81), NUP188 (0.81); STRING partners: CFAP20 (0.908)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Mid piece, Principal piece, End piece; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EF-hand domain containing 1. This gene encodes an EF-hand-containing calcium binding protein. The encoded protein likely plays a role in calcium homeostasis. Mutations in this gene have been associated with susceptibility to juvenile myoclonic epilepsy and juvenile absence epilepsy. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: juvenile myoclonic epilepsy (0.764); Abnormality of the skeletal system (0.351); chronic obstructive pulmonary disease (0.316); lower respiratory tract disorder (0.286); Generalized non-motor (absence) seizure (0.281)
- **Europe PMC papers**: 464
- **Why important**: EFHC1 has the strongest network position in the module and connects to both motility-relevant and broader cellular genes. It appears in every globally corrected GO term (6 globally significant GO/KEGG terms, q_global 0.0209–0.038; see the table), has a direct STRING relationship with CFAP20, and is detected in testis with enrichment across several ciliated epithelial cell types. Its EF-hand calcium-binding annotation provides a plausible connection to calcium-sensitive control of ciliary or flagellar movement. It also has substantial literature and disease associations involving juvenile epilepsy and ciliary or respiratory disorders.
- **Conclusion**: Established evidence supports EFHC1 as a central co-abundance marker and as a biologically plausible ciliary or flagellar motility gene (6 globally significant GO/KEGG terms, q_global 0.0209–0.038; see the table). Its calcium-homeostasis role and disease associations are established annotations. Whether EFHC1 directly organizes the other module genes in this tissue-pair context remains a hypothesis.

#### AKAP4

- **Related proteins** (co-abundance neighbors): ELAPOR1 (0.86), NUP35 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Principal piece; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: A-kinase anchoring protein 4. The A-kinase anchor proteins (AKAPs) are a group of structurally diverse proteins, which have the common function of binding to the regulatory subunit of protein kinase A (PKA) and confining the holoenzyme to discrete locations within the cell. This gene encodes a member of the AKAP family. The encoded protein is localized to the sperm flagellum and may be involved in the regulation of sperm motil…
- **Diseases (Open Targets)**: non-syndromic male infertility due to sperm motility disorder (0.395); spinal muscular atrophy (0.326); Atrophy/Degeneration affecting the central nervous system (0.303); motor neuron disorder (0.303); Reduced sperm motility (0.123)
- **Europe PMC papers**: 735
- **Why important**: AKAP4 is testis-enriched, localized to the sperm principal piece, and annotated as a sperm-flagellum AKAP involved in regulation of sperm motility. It appears in every globally corrected GO term (6 globally significant GO/KEGG terms, q_global 0.0209–0.038; see the table) and has disease associations related to reduced sperm motility and male infertility. Its network connectivity is limited, but its functional specificity makes it a strong biological anchor for the module.
- **Conclusion**: Established evidence identifies AKAP4 as a sperm-flagellar scaffold and a compelling marker of the module's motility interpretation (6 globally significant GO/KEGG terms, q_global 0.0209–0.038; see the table). Its co-abundance with the other genes may reflect shared spermatid differentiation or flagellar specialization. Direct interaction with the full module is not established by the supplied STRING or hu.MAP results.

#### CFAP20

- **Related proteins** (co-abundance neighbors): AK7 (0.80); STRING partners: EFHC1 (0.908)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Principal piece; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cilia and flagella associated protein 20. Enables RNA binding activity. Involved in several processes, including positive regulation of feeding behavior; protein polyglutamylation; and regulation of cell motility. Located in centriole; ciliary basal body; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: retinitis pigmentosa (0.474); Hematuria (0.033); gastric ulcer (0.033); hemorrhage (0.033); Alzheimer disease (0.025)
- **Europe PMC papers**: 135
- **Why important**: CFAP20 is annotated for sperm axoneme assembly, cilium assembly, protein polyglutamylation, regulation of ciliary beat frequency, and flagellated sperm motility. It contributes to every globally corrected GO term (6 globally significant GO/KEGG terms, q_global 0.0209–0.038; see the table), is expressed in spermatogenic cell types, and has a direct high-confidence STRING relationship with EFHC1. Its more limited literature volume relative to several established genes makes it a potentially informative and less extensively characterized module component.
- **Conclusion**: Established evidence supports CFAP20 as a cilia- and sperm-axoneme-associated gene that reinforces the module's primary interpretation (6 globally significant GO/KEGG terms, q_global 0.0209–0.038; see the table). The EFHC1 relationship provides direct interaction support for part of the module. Its possible role as a connector between axoneme assembly and the remaining metabolic or transport genes is a hypothesis.

#### AK7

- **Related proteins** (co-abundance neighbors): NUP35 (0.84), UQCRC2 (0.82), SLC25A19 (0.82), CFAP20 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cytosol, Principal piece; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenylate kinase 7. This gene encodes a member of the adenylate kinase family of enzymes. The encoded enzyme is a phosphotransferase that catalyzes the reversible phosphorylation of adenine nucleotides. This enzyme plays a role in energy homeostasis of the cell. Alternative splicing results in multiple transcript variants. Mutations in the mouse gene are associated with primary ciliary dyskinesia. [provided by RefSeq…
- **Diseases (Open Targets)**: spermatogenic failure 27 (0.504); non-syndromic male infertility due to sperm motility disorder (0.382); neurodegenerative disease (0.300); metabolic disease (0.198); glomerulonephritis (0.192)
- **Europe PMC papers**: 842
- **Why important**: AK7 occupies a relatively central network position and connects the motility-associated portion of the module with nucleoporin, mitochondrial, and metabolite-transport genes. It contributes to the globally corrected motile-cilium term (GO:CC motile cilium; q_global = 0.0303), is enriched in ciliated epithelial cell types, and is annotated as an adenylate kinase involved in cellular energy homeostasis. Its disease associations include spermatogenic failure and sperm-motility disorder, while the supplied annotation also links the gene to primary ciliary dyskinesia in an animal model.
- **Conclusion**: Established evidence supports AK7 as an energy-homeostasis enzyme with ciliary and reproductive relevance, and its network position makes it a plausible bridge between motility and cellular energetics (GO:CC motile cilium; q_global = 0.0303). A direct role in coordinating the other module members in human testis or cell line remains unproven.

#### UQCRC2

- **Related proteins** (co-abundance neighbors): AK7 (0.82), EFHC1 (0.81); STRING partners: MT-ND4 (0.953)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase core protein 2. The protein encoded by this gene is located in the mitochondrion, where it is part of the ubiquinol-cytochrome c reductase complex (also known as complex III). This complex constitutes a part of the mitochondrial respiratory chain. Defects in this gene are a cause of mitochondrial complex III deficiency nuclear type 5. [provided by RefSeq, Jul 2015].
- **Diseases (Open Targets)**: mitochondrial complex III deficiency (0.732); neurodegenerative disease (0.423); mitochondrial disease (0.312); gastric cancer (0.085); adrenoleukodystrophy (0.075)
- **Europe PMC papers**: 3297
- **Why important**: UQCRC2 contributes a mitochondrial respiratory-chain component to a module otherwise dominated by ciliary and spermatogenic signals. It has a STRING relationship with MT-ND4 and co-abundance connections to AK7 and EFHC1. Its established role in complex III and oxidative phosphorylation makes it relevant to the energy demands of sperm or ciliated-cell movement. It also has substantial literature and disease evidence concerning mitochondrial complex deficiency.
- **Conclusion**: Established evidence supports UQCRC2 as a mitochondrial respiration gene and as part of a known respiratory-chain relationship with MT-ND4. Its inclusion may indicate energetic support for motility-related cells, but that linkage is inferential; the supplied evidence does not show that UQCRC2 directly regulates sperm flagellar function.

## Module 3

**Tissue pair**: cell line and testis  
**Genes (16)**: AP3B1, DHX9, DPP3, DYNC1H1, EIF3C, EXOC4, FLII, EIF4G1, KIFBP, LTA4H, PRKDC, RO60, SRP72, SNRNP200, VPS33A, VPS35

### Function

The module most strongly indicates coordinated RNA and protein production machinery, centered on positive regulation of translation (GO:BP positive regulation of translation; q_global = 0.022) and ribonucleoprotein complexes (GO:CC ribonucleoprotein complex; q_global = 0.0369). EIF3C and EIF4G1 support translation initiation, while DHX9, SNRNP200, RO60, SRP72 and PRKDC contribute to RNA handling, spliceosomal or ribonucleoprotein biology, and related nuclear functions. The network also contains cytoskeletal, vesicle-trafficking and organelle-positioning genes, including DYNC1H1, EXOC4, VPS35, VPS33A and AP3B1. Thus, the best-supported interpretation is a translation and RNA-processing module embedded in broader intracellular transport and structural organization. The sparse connectivity means that this is a functional co-abundance pattern rather than evidence that all genes form one physical complex.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It also does not resemble a blood-cell contamination module, because every gene has low immune-cell specificity and no blood-cell enrichment is reported. Most genes have low tissue specificity, consistent with broadly expressed cellular machinery rather than a narrowly tissue-restricted program. The module is nevertheless compatible with shared cellular processes in cell line and testis, and the widespread testis protein detection supports biological presence in testis rather than an annotation artifact. Cell-type-enhanced annotations include neuronal, glial, photoreceptor, spermatid, oocyte and other specialized cell types, but these are distributed across different genes and do not establish one common cell type. The module may therefore reflect conserved housekeeping-like RNA, translation, transport and cytoskeletal activity, with additional relevance to germ-cell biology.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP positive regulation of translation | 0.022 | DHX9, EIF3C, EIF4G1, PRKDC |
| GO:CC ribonucleoprotein complex | 0.0369 | DHX9, EIF3C, PRKDC, RO60, SNRNP200, SRP72 |

### STRING and hu.MAP

The strongest known STRING relationship is EIF3C–EIF4G1, directly supporting a translation-initiation connection. EIF4G1 also connects to VPS35, linking translation-associated machinery with retromer-related trafficking. DHX9 connects with FLII, PRKDC and SNRNP200, providing known links among RNA helicase, DNA-repair or RNA-associated kinase, spliceosomal and actin-remodeling biology. The STRING ribonucleoprotein enrichments (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.00096) and (STRING Component Ribonucleoprotein complex; within-query FDR = 0.0029) are concordant with the globally corrected GO terms but remain supplementary evidence rather than global significance. hu.MAP independently places EIF3C and EIF4G1 together in two translation-related complexes (hu.MAP huMAP3_13175.1) and (hu.MAP huMAP3_11246.1), although each complex contains many additional members not present in the module. No hu.MAP complex is reported for the other module genes. Overall, known physical or complex-level support is concentrated in the translation and RNA-associated subset; the remaining co-abundance links should not be interpreted as established direct molecular interactions.

**STRING interactions (score >= 0.7)**: 5 of 120 gene pairs: DHX9–FLII (0.772); DHX9–PRKDC (0.74); DHX9–SNRNP200 (0.784); EIF3C–EIF4G1 (0.99); EIF4G1–VPS35 (0.899)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Ribonucleoprotein complex (FDR = 0.00096, 7 genes); Component Ribonucleoprotein complex (FDR = 0.0029, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13175.1 (EIF4G1, EIF3C; 2/20); huMAP3_11246.1 (EIF4G1, EIF3C; 2/24)

### Novelty

The supplied evidence does not establish that this is a completely new biological mechanism. Several components and relationships are already well known, especially the EIF3C–EIF4G1 translation connection, the EIF3C/EIF4G1 hu.MAP complexes, and the DHX9–SNRNP200 and DHX9–PRKDC STRING relationships. Conversely, the particular conserved co-abundance combination spanning translation initiation, RNA processing, cytoskeletal transport and vesicle machinery is not represented as a single known hu.MAP complex, and most module pairings lack high-confidence STRING support. This makes the module potentially novel as a cross-tissue co-abundance organization, but not demonstrably novel as a molecular pathway. Absence from STRING or hu.MAP alone is insufficient to claim discovery; validation in independent cohorts, perturbation experiments or comparison with published co-expression modules would be needed.

**Hypothesis.** Hypothesis: cell line and testis share a coordinated cellular state in which increased demand for translation and RNA maturation is coupled to intracellular transport, organelle positioning and vesicle handling. EIF3C and EIF4G1 could represent the translation-initiation arm, DHX9 and SNRNP200 the RNA-processing arm, and DYNC1H1, VPS35, EXOC4, VPS33A and AP3B1 the transport and trafficking arm. In testis, this coordination could support specialized germ-cell differentiation and the intense remodeling of cellular architecture, while in cell line it could reflect a more general proliferative or biosynthetic state. This is a mechanistic model, not evidence of a single physical supercomplex or of direct regulation among all module members.

### Important genes

#### DYNC1H1

- **Related proteins** (co-abundance neighbors): EXOC4 (0.85), EIF3C (0.83), EIF4G1 (0.82), SRP72 (0.82), VPS33A (0.81), FLII (0.80), AP3B1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 1 heavy chain 1. Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polyp…
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy without contractures (0.816); intellectual disability, autosomal dominant 13 (0.815); Charcot-Marie-Tooth disease axonal type 2O (0.799); autosomal dominant non-syndromic intellectual disability (0.634); hereditary disease (0.545)
- **Europe PMC papers**: 1731
- **Why important**: DYNC1H1 is the principal network hub by weighted connectivity and links translation-associated genes, SRP72, vesicle-trafficking components and the actin-remodeling protein FLII. Its established function as a cytoplasmic dynein motor connects the module to microtubule-based movement, organelle transport, protein sorting and spindle dynamics. It also has extensive literature and strong disease associations involving neurodevelopmental and peripheral nerve disorders.
- **Conclusion**: Established evidence supports DYNC1H1 as the module's transport and microtubule-organizing anchor. Its high network position makes it important for module architecture, but the data do not establish that dynein directly drives the translation or ribonucleoprotein associations. A testable hypothesis is that dynein-dependent transport helps coordinate the localization of biosynthetic or germ-cell machinery.

#### EIF3C

- **Related proteins** (co-abundance neighbors): KIFBP (0.83), DYNC1H1 (0.83); STRING partners: EIF4G1 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_13175.1, huMAP3_11246.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C is supported by both globally corrected terms, positive regulation of translation (GO:BP positive regulation of translation; q_global = 0.022) and ribonucleoprotein complex (GO:CC ribonucleoprotein complex; q_global = 0.0369). It is a component of the eukaryotic translation-initiation factor complex, has a direct high-confidence STRING relationship with EIF4G1, and occurs with EIF4G1 in both hu.MAP complexes (hu.MAP huMAP3_13175.1) and (hu.MAP huMAP3_11246.1). Its cell-type annotations include several neural cell types, and it has substantial literature.
- **Conclusion**: Established evidence identifies EIF3C as a central translation-initiation marker and one of the strongest functional interpreters of the module. The co-abundance pattern supports coordinated translation machinery, but it does not prove altered translational activity or a testis-specific role. Its specialized-cell annotations make a context-dependent contribution plausible, but this remains a hypothesis.

#### EIF4G1

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.82), SNRNP200 (0.82); STRING partners: EIF3C (0.99), VPS35 (0.899)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_13175.1, huMAP3_11246.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 is a translation-initiation scaffold and is included in the globally corrected positive-regulation-of-translation term (GO:BP positive regulation of translation; q_global = 0.022) and the supplementary STRING ribonucleoprotein terms (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.00096) and (STRING Component Ribonucleoprotein complex; within-query FDR = 0.0029). It forms the strongest reported STRING pair with EIF3C, connects to VPS35, and is present with EIF3C in both hu.MAP complexes (hu.MAP huMAP3_13175.1) and (hu.MAP huMAP3_11246.1). It has extensive literature and disease associations including Parkinson disease and neurodegenerative disease.
- **Conclusion**: Established evidence supports EIF4G1 as the translation-initiation counterpart to EIF3C and as a bridge toward trafficking through VPS35. The module does not show that EIF4G1 activity is increased or that it physically couples translation to retromer function here. A coordinated biosynthetic and trafficking state is therefore a reasonable hypothesis rather than a demonstrated mechanism.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): PRKDC (0.88), EIF4G1 (0.82), DHX9 (0.80); STRING partners: DHX9 (0.784)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is a core U5 snRNP component and RNA helicase involved in spliceosome assembly and conformational remodeling. It is present in the globally corrected ribonucleoprotein term (GO:CC ribonucleoprotein complex; q_global = 0.0369) and in both supplementary STRING ribonucleoprotein annotations (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.00096) and (STRING Component Ribonucleoprotein complex; within-query FDR = 0.0029). Its STRING links to DHX9 and PRKDC place it within the module's RNA-associated core, and it has strong literature and established retinal-disease associations.
- **Conclusion**: Established evidence supports SNRNP200 as the principal spliceosomal and RNA-processing representative. Its connections to DHX9 and PRKDC are consistent with coordinated RNA and nuclear maintenance functions, but do not establish a novel spliceosome–DNA-repair complex. Its testis detection and germ-cell context make specialized RNA processing a plausible hypothesis.

#### DHX9

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.80); STRING partners: FLII (0.772), PRKDC (0.74), SNRNP200 (0.784)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is included in both globally corrected terms (GO:BP positive regulation of translation; q_global = 0.022) and (GO:CC ribonucleoprotein complex; q_global = 0.0369) and is a multifunctional RNA helicase involved in RNA and DNA–RNA unwinding, transcriptional regulation and alternative splicing. It has STRING relationships with SNRNP200, PRKDC and FLII, thereby connecting the RNA-processing signal to nuclear maintenance and cytoskeletal remodeling. It has extensive literature and associations with developmental, neurodegenerative and infectious-disease biology.
- **Conclusion**: Established evidence supports DHX9 as a multifunctional RNA-processing bridge within the module. The data justify interpreting it as part of the RNA and ribonucleoprotein component, but not as proof that it mediates the observed co-abundance relationships. Its broad molecular roles make it a plausible coordinator of the proposed biosynthetic state, pending experimental testing.

#### VPS35

- **Related proteins** (co-abundance neighbors): EXOC4 (0.85), RO60 (0.81); STRING partners: EIF4G1 (0.899)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS35 retromer complex component. This gene belongs to a group of vacuolar protein sorting (VPS) genes. The encoded protein is a component of a large multimeric complex, termed the retromer complex, involved in retrograde transport of proteins from endosomes to the trans-Golgi network. The close structural similarity between the yeast and human proteins that make up this complex suggests a similarity in function. Expression studie…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.743); neurodegenerative disease (0.553); young-onset Parkinson disease (0.503); Parkinson disease (0.482); Parkinson disease, dominant (0.370)
- **Europe PMC papers**: 3611
- **Why important**: VPS35 is a retromer component involved in endosome-to-Golgi retrograde transport, lysosome organization and protein transport. It connects in the module to EXOC4 and RO60 and has a strong STRING relationship with EIF4G1, providing the clearest link between translation-associated genes and membrane-trafficking machinery. It has extensive literature and notable associations with Parkinson disease and neurodegenerative disease.
- **Conclusion**: Established evidence supports VPS35 as a trafficking representative and as a plausible interface between protein production and intracellular cargo handling. The module does not establish that retromer activity regulates translation or RNA processing. Its importance is therefore interpretive and network-based, while the proposed translation–trafficking coupling remains hypothetical.

## Module 4

**Tissue pair**: cell line and testis  
**Genes (6)**: APOA1, DDAH1, FLNB, NCDN, TES, TKT

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING functional enrichment. The module therefore has no statistically established pathway-level function from enrichment analysis. Its network is organized around APOA1, which is connected to every other module member, while the remaining genes form a set of individual links to APOA1 rather than a densely interconnected network. The gene annotations span HDL-mediated lipid transport and cholesterol efflux through APOA1, nitric-oxide and methylarginine regulation through DDAH1, actin-cytoskeleton and signal-transduction functions through FLNB, LIM-domain and growth-regulatory functions through TES, neuronal plasticity-related functions through NCDN, and pentose-phosphate metabolism through TKT. Taken together, the module does not support a single established molecular pathway; it is more consistent with a heterogeneous co-abundance pattern centered on APOA1.

**Cell composition.** This is not predominantly a secreted-protein module: only APOA1 is identified as secreted to blood. APOA1 is liver-enriched, associated with enterocytes and hepatocytes, and is not detected by testis immunohistochemistry, so its abundance could reflect circulating or sample-composition effects rather than a testis-intrinsic program. The other genes are intracellular or membrane-associated and have diverse tissue or cell-type associations, including kidney, brain, seminal vesicle, bone marrow, alveolar cells, neurons, spermatids, and several immune-cell categories. The module is therefore not a coherent blood-cell signature overall, although TKT has broad myeloid and other blood-cell enrichment and APOA1 has immune-cell enhancement in plasmacytoid dendritic cells. The HPA profile supports substantial cellular and tissue heterogeneity, with most members showing cell-type-enhanced expression, rather than a broadly expressed housekeeping composition. The shared signal could consequently reflect overlapping cell populations, sample composition, or a context-dependent abundance relationship in addition to a biological program shared by the cell-line and testis datasets.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported for any pair of module genes, and no hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not corroborated here as established physical protein interactions or as membership in a known multiprotein complex. The APOA1-centered topology should be interpreted as a statistical abundance relationship, not as evidence that APOA1 directly binds DDAH1, FLNB, TES, NCDN, or TKT. Known biology remains available at the individual-gene level: APOA1 participates in HDL and cholesterol handling, DDAH1 regulates methylarginines and nitric-oxide biology, FLNB links signaling to the actin cytoskeleton, TES contains LIM domains involved in protein interactions and growth regulation, NCDN is associated with neuronal signaling and plasticity, and TKT functions in the non-oxidative pentose-phosphate pathway. These annotations explain plausible independent contributors to the abundance pattern but do not establish a shared complex or pathway.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module-level co-abundance observation may be a new association in this dataset, because neither STRING nor hu.MAP provides an external network or complex that reproduces it. However, absence from those resources does not prove novelty: it may reflect tissue context, abundance correlation rather than physical interaction, incomplete database coverage, or a statistical association among proteins with unrelated primary functions. The individual genes and their functions are already well established, especially APOA1, TES, TKT, FLNB, and DDAH1, so the defensible novelty claim concerns the particular cross-context co-abundance pattern rather than discovery of new gene functions or a new protein complex. Independent replication, control for cell composition and circulating proteins, and validation in testis-relevant material would be needed before treating the module as a novel biological mechanism.

**Hypothesis.** Hypothesis: the module represents a context-dependent abundance program assembled from several biological sources rather than a single physical pathway. A circulating or extracellular APOA1-related component may covary with cellular states involving cytoskeletal remodeling through FLNB and TES, nitric-oxide regulation through DDAH1, metabolic flux through TKT, and neuronal or other lineage-associated biology through NCDN. In testis, some of the signal may be contributed by testis-detected intracellular proteins and cell-type composition, whereas APOA1 may reflect extracellular carryover or shared media and sample conditions. This hypothesis predicts that the APOA1 relationships will weaken after adjustment for extracellular protein abundance and cell composition, while any genuine intracellular program should show reproducible relationships among the relevant tissue or cell types.

### Important genes

#### APOA1

- **Related proteins** (co-abundance neighbors): DDAH1 (0.88), FLNB (0.84), TES (0.84), NCDN (0.84), TKT (0.82); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is the hub of the module, connected to every other member with the strongest aggregate network position. It encodes the major HDL protein component, promotes cholesterol efflux, and supports lecithin-cholesterol acyltransferase activity. It is liver-enriched, secreted to blood, associated with enterocytes and hepatocytes, has extensive disease and literature evidence, and is not detected in testis by immunohistochemistry. Its centrality makes it the main candidate for driving the module statistically, while its extracellular biology makes sample composition a major alternative explanation.
- **Conclusion**: Established: APOA1 is the network hub and a circulating lipid-transport protein with strong independent biological support. Conclusion: it is the best marker of the module's statistical organization, but the data do not establish APOA1 as a direct mechanistic regulator of the other genes.

#### TES

- **Related proteins** (co-abundance neighbors): APOA1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: testin LIM domain protein. Cancer-associated chromosomal changes often involve regions containing fragile sites. This gene maps to a common fragile site on chromosome 7q31.2 designated FRA7G. This gene is similar to mouse Testin, a testosterone-responsive gene encoding a Sertoli cell secretory protein containing three LIM domains. LIM domains are double zinc-finger motifs that mediate protein-protein interactions between tr…
- **Diseases (Open Targets)**: open-angle glaucoma (0.490); glaucoma (0.440); placenta praevia (0.258); spinal cord injury (0.246); Joint stiffness (0.173)
- **Europe PMC papers**: 32609
- **Why important**: TES is directly linked to APOA1 and has a tissue-enhanced association with seminal vesicle and cell-type-enhanced associations including early spermatids. Its LIM domains mediate interactions with transcriptional, cytoskeletal, and signaling proteins, and its annotation includes negative regulation of cell proliferation. It has the largest literature volume among the listed module genes and established disease associations involving glaucoma and other conditions.
- **Conclusion**: Established: TES is a LIM-domain protein with cytoskeletal and growth-regulatory relevance and a reproductive-tissue-related expression signal. Conclusion: TES is a strong candidate for a testis-relevant component of the module, but its edge to APOA1 is co-abundance evidence rather than demonstrated molecular interaction.

#### TKT

- **Related proteins** (co-abundance neighbors): APOA1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transketolase. This gene encodes a thiamine-dependent enzyme which plays a role in the channeling of excess sugar phosphates to glycolysis in the pentose phosphate pathway. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: transketolase deficiency (0.663); neurodegenerative disease (0.409); cardiomyopathy (0.382); alcohol drinking (0.261); urolithiasis (0.259)
- **Europe PMC papers**: 3981
- **Why important**: TKT is linked to the APOA1 hub and encodes a thiamine-dependent enzyme in the non-oxidative pentose-phosphate pathway. It is tissue-enhanced in bone marrow and has group-enriched blood-cell associations across multiple myeloid populations, while also being detected in testis. Its metabolic function, disease association with transketolase deficiency, and substantial literature support make it a plausible indicator of metabolic or cellular-composition effects.
- **Conclusion**: Established: TKT provides a defined metabolic function and has bone-marrow and myeloid-associated expression evidence. Conclusion: TKT could reflect altered metabolic demand or the contribution of blood-related cells, but the module does not establish that its metabolic activity is coordinated mechanistically with APOA1.

#### DDAH1

- **Related proteins** (co-abundance neighbors): APOA1 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dimethylarginine dimethylaminohydrolase 1. This gene belongs to the dimethylarginine dimethylaminohydrolase (DDAH) gene family. The encoded enzyme plays a role in nitric oxide generation by regulating cellular concentrations of methylarginines, which in turn inhibit nitric oxide synthase activity. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: aortic stenosis (0.372); osteoarthritis, knee (0.272); medical procedure (0.272); Alzheimer disease (0.257); seborrheic keratosis (0.240)
- **Europe PMC papers**: 1290
- **Why important**: DDAH1 is the only module member directly linked to APOA1 besides the other peripheral members and is detected in testis. It regulates methylarginine concentrations, nitric-oxide generation, systemic blood pressure, vascular permeability, and related arginine metabolism. Its kidney-enhanced and several specialized cell-type-enhanced associations provide a biologically distinct vascular and signaling dimension, with established disease links and a substantive literature base.
- **Conclusion**: Established: DDAH1 is an enzyme regulating nitric-oxide biology and arginine-related processes. Conclusion: it is a plausible marker of vascular or signaling state in the module, but there is no evidence here for a direct DDAH1–APOA1 biochemical connection.

#### FLNB

- **Related proteins** (co-abundance neighbors): APOA1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin B. This gene encodes a member of the filamin family. The encoded protein interacts with glycoprotein Ib alpha as part of the process to repair vascular injuries. The platelet glycoprotein Ib complex includes glycoprotein Ib alpha, and it binds the actin cytoskeleton. Mutations in this gene have been found in several conditions: atelosteogenesis type 1 and type 3; boomerang dysplasia; autosomal domina…
- **Diseases (Open Targets)**: Larsen syndrome (0.829); spondylocarpotarsal synostosis syndrome (0.775); atelosteogenesis type I (0.763); atelosteogenesis type III (0.756); Boomerang dysplasia (0.723)
- **Europe PMC papers**: 2274
- **Why important**: FLNB is linked to APOA1 and encodes a filamin-family cytoskeletal protein involved in actin organization and signal transduction. It is detected in testis, has low tissue specificity, and has cell-type associations that include trophoblast, pancreatic, prostatic, and urothelial populations. Its extensive developmental-disease associations, including Larsen syndrome and skeletal dysplasias, support a well-established structural role.
- **Conclusion**: Established: FLNB is a cytoskeletal and signaling protein with strong developmental and skeletal-disease evidence. Conclusion: FLNB may report a structural or cell-state component of the module, but the co-abundance edge does not demonstrate an APOA1–FLNB interaction or a shared complex.

## Module 5

**Tissue pair**: cell line and testis  
**Genes (20)**: ARSA, ASRGL1, CTSL, CLU, CPTP, SORD, DNAI2, DPCD, ECM1, FUNDC2, GSTM3, HSPA2, DNALI1, PRKACG, LIPT2, MAN2C1, NME8, PSMB3, SPA17, LTF

### Function

The module is best interpreted as a motile-cilium and sperm-flagellum program. The primary evidence is the globally corrected enrichment for cilium movement (GO:BP cilium movement; q_global = 0.000815), motile cilium (GO:CC motile cilium; q_global = 0.0105), sperm flagellum (GO:CC sperm flagellum; q_global = 0.0254), and the nine-plus-two motile-cilium structure (GO:CC 9+2 motile cilium; q_global = 0.0321). The shared signal is especially coherent for axonemal structure and movement: DNAI2, DNALI1, NME8, DPCD, SORD, GSTM3, and SPA17 recur across these terms. DNAI2 and DNALI1 are dynein components, NME8 is implicated in outer dynein arms and ciliary function, and DPCD is associated with generation and maintenance of ciliated cells. SORD, GSTM3, and SPA17 may represent metabolic, stress-protection, or sperm-surface components associated with the same biological state rather than core axonemal machinery. The STRING enrichments (7 supplementary STRING terms; within-query FDR 0.0034–0.0281) independently support motile cilium, sperm flagellum, cilium, and cilium movement, while the sparse high-confidence STRING edges identify a particularly coherent DNAI2–DNALI1–NME8 relationship and a separate CLU–LTF relationship. Overall, the module most plausibly reflects coordinated ciliated-cell and spermatogenic differentiation with emphasis on motility apparatus formation and function.

**Cell composition.** This is not primarily a plasma-protein or broadly expressed housekeeping module. HPA shows strong reproductive and ciliated-cell specificity: testis is the most frequent enriched tissue, and late primary spermatocytes, early spermatids, and late spermatids are the most frequent enriched cell types. Fallopian-tube ciliated cells and related ciliated epithelial populations are also represented. Most genes have testis protein detection, whereas LTF and CLU are secreted proteins and ECM1 is secreted to the extracellular matrix; these are a minority of the module. Several genes have immune-cell annotations, but the module is not dominated by blood-cell specificity, and four genes are not detected in immune cells. LTF and CLU could reflect extracellular or blood-associated material in some samples, so sample composition should still be considered, but the HPA pattern strongly favors a genuine ciliated and spermatogenic cell-state signal rather than a generic blood contamination explanation.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP cilium movement | 0.000815 | DNAI2, DNALI1, DPCD, NME8, SORD, SPA17 |
| GO:CC motile cilium | 0.0105 | DNAI2, DNALI1, GSTM3, NME8, SORD, SPA17 |
| GO:CC sperm flagellum | 0.0254 | DNAI2, DNALI1, GSTM3, NME8, SPA17 |
| GO:CC 9+2 motile cilium | 0.0321 | DNAI2, DNALI1, GSTM3, NME8, SPA17 |

### STRING and hu.MAP

STRING provides three high-confidence relationships among the module genes. DNAI2 connects strongly to DNALI1 and NME8, directly reinforcing an axonemal dynein interpretation; CLU connects strongly to LTF, supporting a separate extracellular or secreted-protein association. The absence of STRING edges for many other module pairs means that the co-abundance network contains relationships not represented as established STRING physical or functional links, but it does not by itself demonstrate novel biology. hu.MAP identifies PRKACG and SPA17 together in four complexes (hu.MAP huMAP3_07046.1) (hu.MAP huMAP3_11135.1) (hu.MAP huMAP3_13352.1) (hu.MAP huMAP3_14681.1), each containing broader PKA, AKAP, and sperm-associated components. These complexes support a possible PKA-organizing or sperm-signaling context, but only a small subset of each complex is represented in the module, so they should not be interpreted as complete complexes assembled from this module. The combined evidence suggests a compact established axonemal core plus a broader differentiation, signaling, proteostasis, metabolic, and extracellular context.

**STRING interactions (score >= 0.7)**: 3 of 190 gene pairs: CLU–LTF (0.993); DNAI2–DNALI1 (0.983); DNAI2–NME8 (0.981)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Motile cilium (FDR = 0.0034, 6 genes); COMPARTMENTS Motile cilium (FDR = 0.0054, 5 genes); Component Sperm flagellum (FDR = 0.0069, 5 genes); Component Cilium (FDR = 0.0077, 7 genes); Process Cilium movement (FDR = 0.0189, 5 genes); COMPARTMENTS Cilium (FDR = 0.0234, 6 genes); COMPARTMENTS Sperm flagellum (FDR = 0.0281, 4 genes); Component Cell surface (FDR = 0.041, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07046.1 (PRKACG, SPA17; 2/17); huMAP3_11135.1 (PRKACG, SPA17; 2/26); huMAP3_13352.1 (PRKACG, SPA17; 2/30); huMAP3_14681.1 (PRKACG, SPA17; 2/31)

### Novelty

The module is not wholly new in biological interpretation: the cilium and sperm-flagellum functions, the DNAI2–DNALI1–NME8 relationships, and the PRKACG–SPA17 complex context are already supported by curated annotations, STRING, hu.MAP, and gene literature. Its potentially novel contribution is the coordinated co-abundance of this established ciliary and spermatogenic machinery with genes such as HSPA2, ASRGL1, LIPT2, FUNDC2, SORD, and selected extracellular proteins across the cell-line and testis tissue pair. That claim remains a hypothesis rather than proof of novelty. Lack of representation in STRING or hu.MAP cannot establish that the module is new, and the fact sheet does not provide an external matched-module comparison, perturbation experiment, or independent replication. The defensible conclusion is that this is a biologically coherent module with a potentially novel cross-context co-abundance organization, not a demonstrably unprecedented pathway.

**Hypothesis.** Hypothesis: the module marks a coordinated differentiation state in which spermatogenic or ciliated cells build and maintain a motile nine-plus-two axoneme while coupling axonemal assembly to cAMP–PKA signaling, proteostasis, redox and metabolic support, and extracellular surface interactions. In this model, DNAI2, DNALI1, NME8, and DPCD form the motility and assembly axis; PRKACG and SPA17 provide a sperm-associated signaling or anchoring context; HSPA2 supports protein folding during differentiation; and SORD, GSTM3, LIPT2, and FUNDC2 help meet metabolic or stress-related demands. CLU and LTF may represent extracellular or sample-context components rather than obligatory members of the axonemal machinery. This model should be tested by cell-type-resolved expression, protein localization, perturbation of the dynein or PKA-associated genes, and measurement of ciliary or sperm motility.

### Important genes

#### DNAI2

- **Related proteins** (co-abundance neighbors): DPCD (0.94), CLU (0.82); STRING partners: DNALI1 (0.983), NME8 (0.981)
- **HPA**: Group enriched; Group enriched; blood Immune cell enriched; location Connecting piece, Mid piece; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein axonemal intermediate chain 2. The protein encoded by this gene belongs to the dynein intermediate chain family, and is part of the dynein complex of respiratory cilia and sperm flagella. Mutations in this gene are associated with primary ciliary dyskinesia type 9. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene. [provided by RefSeq, Mar 2010].
- **Diseases (Open Targets)**: Kartagener Syndrome (0.758); bronchiectasis (0.370); Alzheimer disease (0.257); poisoning (0.257); lysosomal storage disease (0.254)
- **Europe PMC papers**: 580
- **Why important**: DNAI2 is a central anchor of the module's established ciliary interpretation. It has direct STRING relationships with DNALI1 and NME8, appears in every primary GO term (4 globally significant GO/KEGG terms, q_global 0.000815–0.0321; see the table), and is also present across the relevant STRING enrichments. It encodes a dynein intermediate-chain protein involved in respiratory cilia and sperm flagella, and its mutations are associated with primary ciliary dyskinesia type nine and Kartagener syndrome. Its network position is more modest than the highest-degree genes, but its direct high-confidence links and disease relevance make it a mechanistically informative connector.
- **Conclusion**: Established evidence supports DNAI2 as a core axonemal and motility gene in this module. The module-level data support coordinated abundance with other ciliary genes, but do not establish that DNAI2 controls the entire module or that its disease associations explain the cross-context co-abundance.

#### DNALI1

- **Related proteins** (co-abundance neighbors): HSPA2 (0.94), ASRGL1 (0.91), FUNDC2 (0.90), LTF (0.87), SORD (0.86), PSMB3 (0.80); STRING partners: DNAI2 (0.983)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Primary cilium, Mid piece, Principal piece, End piece; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein axonemal light intermediate chain 1. This gene is the human homolog of the Chlamydomonas inner dynein arm gene, p28. The precise function of this gene is not known, however, it is a potential candidate for immotile cilia syndrome (ICS). Ultrastructural defects of the inner dynein arms are seen in patients with ICS. Immotile mutant strains of Chlamydomonas, a biflagellated algae, exhibit similar defects. [provided by RefSeq, Jul 2008]…
- **Diseases (Open Targets)**: spermatogenic failure 83 (0.414); non-syndromic male infertility due to sperm motility disorder (0.387); open-angle glaucoma (0.309); asthma (0.115); lower respiratory tract disorder (0.104)
- **Europe PMC papers**: 497
- **Why important**: DNALI1 has one of the strongest network positions, with the highest listed degree and weighted strength, and it connects to several module genes including DNAI2 and SORD. It occurs in every primary GO term (4 globally significant GO/KEGG terms, q_global 0.000815–0.0321; see the table), has a direct high-confidence STRING edge to DNAI2, and is annotated as a dynein axonemal light intermediate chain and a candidate for immotile cilia syndrome. Its HPA pattern links testis, spermatogenic cells, and multiple ciliated epithelial populations.
- **Conclusion**: Established evidence identifies DNALI1 as a likely structural component of the module's conserved motile-cilium program. Its ciliary disease relevance makes it a strong candidate for functional testing, but the co-abundance network alone does not prove that DNALI1 is a regulatory hub or that its links outside the known dynein relationship are physical interactions.

#### NME8

- **Related proteins** (co-abundance neighbors): GSTM3 (0.87), LIPT2 (0.87); STRING partners: DNAI2 (0.981)
- **HPA**: Group enriched; Group enriched; blood Immune cell enhanced; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NME/NM23 family member 8. This gene encodes a protein with an N-terminal thioredoxin domain and three C-terminal nucleoside diphosphate kinase (NDK) domains, but the NDK domains are thought to be catalytically inactive. The sea urchin ortholog of this gene encodes a component of sperm outer dynein arms, and the protein is implicated in ciliary function. Mutations in this gene are implicated in primary ciliary dyskinesia ty…
- **Diseases (Open Targets)**: Kartagener Syndrome (0.424); neurodegenerative disease (0.274); Alzheimer disease (0.258); dementia (0.236); sign or symptom (0.204)
- **Europe PMC papers**: 510
- **Why important**: NME8 appears in every primary GO term (4 globally significant GO/KEGG terms, q_global 0.000815–0.0321; see the table) and in the principal STRING cilium and sperm-flagellum enrichments. It has a direct high-confidence relationship with DNAI2 and is implicated in sperm outer dynein arms, ciliary function, and primary ciliary dyskinesia type six. HPA places it in testis and differentiating spermatogenic cell types, making it a strong bridge between the ciliary and reproductive interpretations.
- **Conclusion**: Established evidence supports NME8 as part of the conserved ciliary and sperm-motility machinery represented by the module. Its disease and structural annotations make it biologically important, while the module does not establish whether NME8 abundance is causal for the broader co-abundance pattern.

#### SPA17

- **Related proteins** (co-abundance neighbors): PRKACG (0.90), CTSL (0.85), CLU (0.85), GSTM3 (0.84), HSPA2 (0.84), ASRGL1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Golgi apparatus, Principal piece; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07046.1, huMAP3_11135.1, huMAP3_13352.1, huMAP3_14681.1
- **Function (MyGene.info)**: sperm autoantigenic protein 17. This gene encodes a protein present at the cell surface. The N-terminus has sequence similarity to human cAMP-dependent protein kinase A (PKA) type II alpha regulatory subunit (RIIa) while the C-terminus has an IQ calmodulin-binding motif. The central portion of the protein has carbohydrate binding motifs and likely functions in cell-cell adhesion. The protein was initially characterized by its in…
- **Diseases (Open Targets)**: irritable bowel syndrome (0.252); neurodegenerative disease (0.225); familial long QT syndrome (0.085); neoplasm (0.082); cancer (0.077)
- **Europe PMC papers**: 373
- **Why important**: SPA17 has a high network position and links to PRKACG, HSPA2, GSTM3, ASRGL1, and CLU. It appears in every primary GO term (4 globally significant GO/KEGG terms, q_global 0.000815–0.0321; see the table) and all listed STRING enrichment categories, although it has no direct STRING partner in the supplied network. HPA supports testis and fallopian-tube enrichment and spermatogenic cell-type association. Its annotations connect sperm flagellum and cilium movement with sperm–zona-pellucida binding, cell adhesion, and a calmodulin- and PKA-related molecular context. Its presence with PRKACG in the hu.MAP complexes (hu.MAP huMAP3_07046.1) (hu.MAP huMAP3_11135.1) (hu.MAP huMAP3_13352.1) (hu.MAP huMAP3_14681.1) adds a signaling-organizing dimension.
- **Conclusion**: Established evidence supports SPA17 as an important sperm-associated and cilium-related module member, with a plausible interface between motility, surface interaction, and signaling. The proposed role as an organizer linking axonemal function to PKA or adhesion is a hypothesis because the supplied data do not demonstrate those interactions directly.

#### PRKACG

- **Related proteins** (co-abundance neighbors): SPA17 (0.90), MAN2C1 (0.87), ECM1 (0.86), ARSA (0.85), CPTP (0.84); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07046.1, huMAP3_11135.1, huMAP3_13352.1, huMAP3_14681.1
- **Function (MyGene.info)**: protein kinase cAMP-activated catalytic subunit gamma. Cyclic AMP-dependent protein kinase (PKA) consists of two catalytic subunits and a regulatory subunit dimer. This gene encodes the gamma form of its catalytic subunit. The gene is intronless and is thought to be a retrotransposon derived from the gene for the alpha form of the PKA catalytic subunit. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: platelet-type bleeding disorder 19 (0.503); Rare hemorrhagic disorder due to a constitutional platelet anomaly (0.462); neurodegenerative disease (0.241); nephrolithiasis (0.183); lymphoma (0.037)
- **Europe PMC papers**: 665
- **Why important**: PRKACG has a relatively strong network position and is the only module gene with testis tissue enrichment in the supplied HPA summary. It is associated with differentiating spermatogenic cells, connects in the module to SPA17, MAN2C1, ECM1, ARSA, and CPTP, and occurs with SPA17 in four hu.MAP complexes (hu.MAP huMAP3_07046.1) (hu.MAP huMAP3_11135.1) (hu.MAP huMAP3_13352.1) (hu.MAP huMAP3_14681.1) containing PKA and AKAP components. Its function as a cAMP-dependent protein-kinase catalytic subunit provides a plausible signaling mechanism for coordinating sperm-cell differentiation or motility, although it is not in any primary GO term.
- **Conclusion**: Established evidence supports PRKACG as a testis-enriched PKA catalytic subunit embedded in a sperm-associated complex context, but not as a member of the core cilium-enrichment signal. Its role in regulating this module's motility program is a hypothesis that requires biochemical interaction and perturbation evidence.

#### HSPA2

- **Related proteins** (co-abundance neighbors): DNALI1 (0.94), SPA17 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Flagellar centriole, Annulus; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 2. Enables disordered domain specific binding activity; enzyme binding activity; and unfolded protein binding activity. Involved in negative regulation of inclusion body assembly and protein refolding. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: glaucoma (0.294); open-angle glaucoma (0.278); hypothyroidism (0.122); non-small cell lung carcinoma (0.100); neoplasm (0.094)
- **Europe PMC papers**: 2107
- **Why important**: HSPA2 is connected to the high-position DNALI1 and SPA17 nodes and is detected in testis, with enrichment in early and late primary spermatocytes and other relevant developmental cell types. It is a chaperone involved in unfolded-protein binding, protein refolding, meiotic nuclear division, spermatogenesis, and spermatid development. Although it is not in the primary GO terms and has no supplied STRING edge, its strong literature volume and established spermatogenic and proteostasis functions make it important for interpreting how the module could support assembly of complex ciliary structures.
- **Conclusion**: Established evidence supports HSPA2 as a spermatogenic proteostasis factor associated with module genes that participate in ciliary and sperm functions. Its proposed role in maintaining or assembling the motility apparatus is a hypothesis rather than a demonstrated direct mechanism.

## Module 6

**Tissue pair**: cell line and testis  
**Genes (9)**: ATP13A1, DOCK7, NSF, NUP93, RNF123, SUN2, CARS1, QARS1, VPS13A

### Function

This is a heterogeneous intracellular cell-biological module rather than a clearly defined canonical pathway. Its genes collectively relate to nuclear pore function and nucleocytoplasmic transport through NUP93, vesicle trafficking and receptor recycling through NSF, nuclear positioning and cytoskeletal coupling through SUN2, membrane and organelle trafficking through VPS13A and ATP13A1, ubiquitin-dependent protein turnover through RNF123, cytoskeletal and neuronal polarization processes through DOCK7, and protein synthesis through CARS1 and QARS1. No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for the module. The globally significant GO/KEGG evidence therefore does not support assigning a single established biochemical function. The gene annotations and the co-abundance structure are most consistent with a shared intracellular maintenance program involving transport, protein handling, nuclear organization, and translation, with substantial uncertainty about whether these processes are mechanistically coupled.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not strongly blood-cell enriched, because nearly all genes have low immune-cell specificity and only DOCK7 is immune-cell enhanced in myeloid dendritic cells. Most genes have low tissue specificity, while a smaller subset is tissue enhanced in brain, skeletal muscle, or tongue. Cell-type enhancement is common, including reproductive, neural, epithelial, cardiac-associated, and muscle-associated cell types. Testis protein detection is available for nearly all genes and is positive for nearly all of those with data, while the cell-line protein summary has no informative matching HPA tissue result. The shared module could therefore reflect broadly expressed intracellular machinery that is especially detectable in testis, but cell-type composition or testis-specific cellular states may also contribute. The HPA pattern does not support a simple blood-contamination explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship within the module is between CARS1 and QARS1. This is biologically plausible because both are aminoacyl-tRNA synthetases involved in translation, but the isolated pair does not establish that the entire module is a translation complex. STRING reports no supplementary functional enrichment. No hu.MAP complex contains multiple module members. NUP93 is the principal network connector, linking several otherwise weakly connected branches, while NSF connects the nuclear-envelope-related and trafficking-related portion of the graph. The sparse STRING support and absence of a hu.MAP complex indicate that much of the co-abundance structure is not explained by already catalogued physical complexes. The network may represent coordinated expression or shared cellular-state regulation rather than one stable multiprotein assembly.

**STRING interactions (score >= 0.7)**: 1 of 36 gene pairs: CARS1–QARS1 (0.838)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact co-abundance module may be a new observation in this tissue-pair analysis, because it lacks a matching hu.MAP complex, has only one supported within-module STRING interaction, and has no globally significant GO or KEGG enrichment. However, these facts do not prove biological novelty. Most member genes have established individual functions, disease associations, and literature, and the module combines familiar processes such as nuclear transport, vesicle trafficking, translation, ubiquitin-mediated turnover, and cytoskeletal organization. A defensible conclusion is that the specific cross-context co-abundance pattern is potentially novel, whereas the component biology is largely established. Independent replication, preservation testing, and comparison with published co-expression modules would be required to claim a genuinely new biological mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated demand for intracellular proteostasis and trafficking during specialized testis or cell-line cellular states. In this model, NUP93 and SUN2 couple nuclear transport and nuclear-envelope organization, NSF and VPS13A support membrane and organelle trafficking, ATP13A1 handles mislocalized membrane proteins, RNF123 contributes selective protein turnover, and CARS1 with QARS1 supports translation. DOCK7 may connect this program to cytoskeletal remodeling and cell polarization. The hypothesis predicts that the module should track cellular remodeling, transport burden, or differentiation state rather than a single physical complex. It remains speculative because the module lacks globally significant enrichment, has sparse known physical interactions, and does not contain a hu.MAP complex.

### Important genes

#### NUP93

- **Related proteins** (co-abundance neighbors): DOCK7 (0.87), QARS1 (0.84), RNF123 (0.83), NSF (0.81), ATP13A1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 is the central network connector and has the strongest weighted network position in the module. Its established function in the nuclear pore complex links nucleocytoplasmic transport, nuclear-envelope organization, nuclear pore assembly, and messenger RNA export. It is detected in testis, shows cell-type enhancement in oocytes and retinal bipolar cells, and has extensive literature and disease associations including nephrotic syndrome and steroid-resistant nephrotic syndrome.
- **Conclusion**: Established evidence supports NUP93 as the principal structural and transport-related anchor of the module. It is a strong candidate for coordinating the module's nuclear-transport interpretation. It is not established that NUP93 physically organizes the other module members, because STRING lists no supported partners for it within this module and hu.MAP lists no relevant complex. Any role as the upstream coordinator is therefore a hypothesis.

#### NSF

- **Related proteins** (co-abundance neighbors): DOCK7 (0.83), SUN2 (0.82), NUP93 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-ethylmaleimide sensitive factor, vesicle fusing ATPase. Enables PDZ domain binding activity and ionotropic glutamate receptor binding activity. Involved in intracellular protein transport; positive regulation of protein catabolic process; and positive regulation of receptor recycling. Located in Golgi apparatus; cytosol; and plasma membrane. Implicated in developmental and epileptic encephalopathy. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy 96 (0.561); neurodegenerative disease (0.529); atrial fibrillation (0.310); Abnormality of the skeletal system (0.303); androgenetic alopecia (0.300)
- **Europe PMC papers**: 65784
- **Why important**: NSF is a central connector linking DOCK7, SUN2, and NUP93. Its established role as a vesicle-fusing ATPase in intracellular transport, exocytosis, intra-Golgi trafficking, and receptor recycling provides a mechanistic bridge between membrane trafficking and the nuclear or cytoskeletal portions of the module. It is tissue enhanced in brain, enriched across several neural and renal cell types, detected in testis, and has very extensive literature together with disease associations including developmental and epileptic encephalopathy.
- **Conclusion**: Established evidence supports NSF as a major intracellular trafficking component and a biologically important connector in the co-abundance network. Its position makes it a plausible integrator of transport-related cellular demand. A direct functional connection between NSF and the other module genes is not established by the supplied interaction resources.

#### CARS1

- **Related proteins** (co-abundance neighbors): VPS13A (0.81); STRING partners: QARS1 (0.838)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cysteinyl-tRNA synthetase 1. This gene encodes a class 1 aminoacyl-tRNA synthetase, cysteinyl-tRNA synthetase. Each of the twenty aminoacyl-tRNA synthetases catalyzes the aminoacylation of a specific tRNA or tRNA isoaccepting family with the cognate amino acid. This gene is one of several located near the imprinted gene domain on chromosome 11p15.5, an important tumor-suppressor gene region. Alterations in this region have be…
- **Diseases (Open Targets)**: microcephaly, developmental delay, and brittle hair syndrome (0.674); cancer (0.471); lung carcinoma (0.371); kidney neoplasm (0.371); trichothiodystrophy (0.370)
- **Europe PMC papers**: 306
- **Why important**: CARS1 is one half of the only high-confidence STRING interaction in the module, pairing with QARS1. It encodes cysteinyl-tRNA synthetase and therefore directly supports accurate protein translation. It is enhanced in early spermatids and late primary spermatocytes, detected in testis, has disease associations involving microcephaly and developmental delay, and has a meaningful literature base despite being less studied than the central network genes.
- **Conclusion**: Established evidence supports CARS1 as a translation-related component with particular relevance to spermatogenic cell states. Its STRING relationship with QARS1 strengthens the interpretation of a local aminoacylation or protein-synthesis signal. It is not established that this translation pair mechanistically drives the whole module; that broader connection remains a hypothesis.

#### QARS1

- **Related proteins** (co-abundance neighbors): NUP93 (0.84); STRING partners: CARS1 (0.838)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutaminyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. In metazoans, 9 aminoacyl-tRNA synthetases specific for glutamine (gln), glutamic acid (glu), and 7 other amino …
- **Diseases (Open Targets)**: diffuse cerebral and cerebellar atrophy - intractable seizures - progressive microcephaly syndrome (0.794); hereditary disease (0.415); intellectual disability, autosomal dominant 43 (0.340); microcephaly (0.298); attention deficit-hyperactivity disorder (0.111)
- **Europe PMC papers**: 253
- **Why important**: QARS1 is the partner of CARS1 in the only high-confidence STRING relationship within the module. Its established function is glutaminyl-tRNA aminoacylation and protein translation. It is enhanced in early and late spermatids as well as other specialized cell types, is detected in testis, and is associated with neurodevelopmental disease including progressive microcephaly and intractable seizures.
- **Conclusion**: Established evidence supports QARS1 as a translation and aminoacylation component that may explain part of the testis-associated co-abundance signal, especially alongside CARS1. The CARS1-QARS1 relationship is the clearest known molecular link in the module. Whether this pair is coordinated with nuclear transport, trafficking, or cytoskeletal genes through a shared mechanism is not established.

#### SUN2

- **Related proteins** (co-abundance neighbors): NSF (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Sad1 and UNC84 domain containing 2. SUN1 (MIM 607723) and SUN2 are inner nuclear membrane (INM) proteins that play a major role in nuclear-cytoplasmic connection by formation of a 'bridge' across the nuclear envelope, known as the LINC complex, via interaction with the conserved luminal KASH domain of nesprins (e.g., SYNE1; MIM 608441) located in the outer nuclear membrane (ONM). The LINC complex provides a direct connection between…
- **Diseases (Open Targets)**: dengue disease (0.370); mirror movements 3 (0.333); Emery-Dreifuss muscular dystrophy (0.208); cervical carcinoma (0.204); HIV-1 infection (0.098)
- **Europe PMC papers**: 1766
- **Why important**: SUN2 connects the nuclear membrane to the cytoskeleton through the LINC complex and is involved in nuclear migration, centrosome localization, and cell migration. It links directly to NSF in the module, is detected in testis, and shows cell-type enhancement in epicardial, esophageal apical, and oligodendrocyte populations. Its disease associations include Emery-Dreifuss muscular dystrophy, and its literature supports an established role in nuclear positioning and mechanical coupling.
- **Conclusion**: Established evidence supports SUN2 as the module's nuclear-envelope and mechanotransduction-related component. Its presence provides a plausible route by which intracellular trafficking and cytoskeletal remodeling could be coordinated with nuclear organization. A direct SUN2-mediated mechanism connecting the full module is not demonstrated by the supplied STRING or hu.MAP evidence.

## Module 7

**Tissue pair**: cell line and testis  
**Genes (8)**: BBS1, CLYBL, COG8, GFPT1, HOOK1, IFT57, IFT81, PIP4K2C

### Function

The module is most consistent with a cilia- and intracellular-trafficking-related co-abundance program, with a particularly coherent signal for intraflagellar transport and ciliopathy biology. The strongest functional interpretation comes from the convergence of IFT81, IFT57, and BBS1 in the supplementary STRING annotations (5 supplementary STRING terms; within-query FDR 0.0368–0.0489), together with the known IFT57–IFT81 relationship and their shared membership in hu.MAP complexes (hu.MAP huMAP3_05411.1) and (hu.MAP huMAP3_13817.1). However, no GO or KEGG term passed global correction, so the ciliary interpretation is supportive rather than a globally significant enrichment result. The remaining genes point to connected cellular processes including microtubule and organelle transport, Golgi trafficking, membrane lipid metabolism, carbohydrate metabolism, and autophagy.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity and low immune-cell specificity, which argues against a module driven primarily by blood contamination or a shared immune cell population. The HPA single-cell patterns nevertheless include ciliated, neural, epithelial, and spermatogenic cell types, with recurrent signals in ependymal cells and spermatids. Two genes are tissue enhanced in liver or retina, while the proteins are predominantly detected in testis. Thus, the cell-line/testis sharing may reflect a broad intracellular program that is especially visible in testicular cells with cilia, flagellar, or specialized trafficking biology, rather than a secreted or blood-derived program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The established interaction evidence is concentrated rather than widespread. STRING reports the IFT57–IFT81 pair as a high-confidence interaction, and both genes occur together in hu.MAP complexes (hu.MAP huMAP3_05411.1) and (hu.MAP huMAP3_13817.1). These complexes contain additional intraflagellar-transport components, supporting the interpretation that the pair is part of a recognized ciliary transport assembly. BBS1 is functionally linked to the same ciliopathy theme through the supplementary STRING terms (5 supplementary STRING terms; within-query FDR 0.0368–0.0489), but it has no listed STRING partner and no listed hu.MAP complex in this module. The other module genes also have no listed STRING partners or hu.MAP complexes. Consequently, the co-abundance network is not simply a catalogue of known physical interactions; it combines one established IFT interaction and complex membership with broader expression covariation around BBS1.

**STRING interactions (score >= 0.7)**: 1 of 28 gene pairs: IFT57–IFT81 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Ciliopathy (FDR = 0.0368, 3 genes); WikiPathways Genes related to primary cilium development (based on CRISPR) (FDR = 0.0383, 3 genes); WikiPathways Ciliopathies (FDR = 0.0383, 3 genes); WikiPathways Bardet-Biedl syndrome (FDR = 0.0383, 3 genes); NetworkNeighborAL Intraciliary transport particle, and Bardet-Biedl syndrome 18 (FDR = 0.0489, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05411.1 (IFT81, IFT57; 2/17); huMAP3_13817.1 (IFT81, IFT57; 2/20)

### Novelty

The module should not be called a wholly new ciliary complex or a newly discovered physical interaction. The IFT57–IFT81 relationship, their hu.MAP complex membership, and the association of BBS1 with ciliopathy biology are already established by the provided resources. A potentially novel aspect is the tissue-pair-specific co-abundance configuration that places BBS1 at the center of a small module linking recognized ciliary genes with HOOK1, COG8, GFPT1, PIP4K2C, and CLYBL. That observation is hypothesis-generating, not proof of a new pathway: most edges lack listed STRING or hu.MAP support, and absence from those resources does not establish novelty.

**Hypothesis.** Hypothesis: in cell line and testis, coordinated abundance of BBS1 with IFT57 and IFT81 marks a ciliary or flagellar trafficking state, while the accompanying genes modulate the membrane, Golgi, cytoskeletal, metabolic, and autophagic environment needed to assemble or maintain that structure. BBS1 may act as the expression-linked hub connecting the core intraflagellar-transport signal to these peripheral processes. This mechanism is plausible from the annotations and network structure, but it requires direct validation by localization, perturbation, and physical-interaction experiments.

### Important genes

#### BBS1

- **Related proteins** (co-abundance neighbors): CLYBL (0.84), IFT57 (0.84), HOOK1 (0.84), GFPT1 (0.82), IFT81 (0.81), COG8 (0.81), PIP4K2C (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Midbody; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Bardet-Biedl syndrome 1. Mutations in this gene have been observed in patients with the major form (type 1) of Bardet-Biedl syndrome. The encoded protein may play a role in eye, limb, cardiac and reproductive system development. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: Bardet-Biedl syndrome 1 (0.828); Bardet-Biedl syndrome (0.774); retinitis pigmentosa (0.694); inherited retinal dystrophy (0.560); hereditary disease (0.506)
- **Europe PMC papers**: 2029
- **Why important**: BBS1 is the weighted-degree hub connected to every other module gene, making it the central network organizer. Its annotations include cilium assembly, photoreceptor maintenance, intracellular protein localization, and Bardet-Biedl syndrome, while the supplementary STRING results repeatedly place it with IFT81 and IFT57 in ciliopathy-related terms (5 supplementary STRING terms; within-query FDR 0.0368–0.0489). It also has the largest literature volume among the selected genes.
- **Conclusion**: Established evidence supports BBS1 as the module's central ciliary-disease anchor. It is reasonable to hypothesize that its abundance tracks the broader ciliary state, but the co-abundance edges do not establish that BBS1 directly regulates the other genes.

#### IFT81

- **Related proteins** (co-abundance neighbors): BBS1 (0.81); STRING partners: IFT57 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_05411.1, huMAP3_13817.1
- **Function (MyGene.info)**: intraflagellar transport 81. The protein encoded by this gene, together with IFT74, forms a tubulin-binding module of intraflagellar transport complex B. This module is involved in transport of tubulin within the cilium, and the encoded protein is required for ciliogenesis. Mutations in this gene are a cause of short-rib polydactyly syndromes. [provided by RefSeq, Dec 2016].
- **Diseases (Open Targets)**: short-rib thoracic dysplasia 19 with or without polydactyly (0.691); short rib dysplasia (0.554); short rib-polydactyly syndrome (0.528); inherited retinal dystrophy (0.456); atrial fibrillation (0.398)
- **Europe PMC papers**: 527
- **Why important**: IFT81 is a recognized intraflagellar-transport component that forms a tubulin-binding module with IFT74 and is required for ciliogenesis. It is annotated for intraciliary transport, cilium assembly, spermatogenesis, and smoothened signaling, and is associated with short-rib polydactyly syndromes and inherited retinal disease. It is also one half of the only listed high-confidence STRING pair and appears in both hu.MAP complexes (hu.MAP huMAP3_05411.1) and (hu.MAP huMAP3_13817.1).
- **Conclusion**: Established evidence identifies IFT81 as a core mechanistic marker of ciliary transport and a plausible driver of the module's biological interpretation. Its co-abundance with the peripheral genes remains an association rather than evidence that those genes function in the same physical complex.

#### IFT57

- **Related proteins** (co-abundance neighbors): BBS1 (0.84); STRING partners: IFT81 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus, Primary cilium, Basal body, Mid piece; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_05411.1, huMAP3_13817.1
- **Function (MyGene.info)**: intraflagellar transport 57. Predicted to enable DNA binding activity. Acts upstream of or within activation of cysteine-type endopeptidase activity involved in apoptotic process; apoptotic process; and regulation of apoptotic process. Predicted to be located in ciliary basal body. Predicted to be part of axoneme and intraciliary transport particle B. Predicted to be active in Golgi apparatus; centrosome; and cilium. Implicat…
- **Diseases (Open Targets)**: orofaciodigital syndrome 18 (0.540); Bardet-Biedl syndrome (0.459); orofaciodigital syndrome (0.372); hypothyroidism (0.371); malnutrition (0.273)
- **Europe PMC papers**: 600
- **Why important**: IFT57 is annotated as part of the axoneme, basal body, and intraciliary transport particle, with roles in anterograde transport and cilium assembly. It is associated with orofaciodigital syndrome and Bardet-Biedl syndrome, belongs to both hu.MAP complexes (hu.MAP huMAP3_05411.1) and (hu.MAP huMAP3_13817.1), and forms the strongest listed STRING interaction with IFT81. Its spermatid and ciliated-cell expression patterns are particularly relevant to the testis-shared module.
- **Conclusion**: Established evidence supports IFT57 as a core ciliary and spermatogenic component that reinforces the IFT interpretation. The module data support coordinated abundance with IFT81 and BBS1, but do not demonstrate a causal role for IFT57 in the module's peripheral associations.

#### HOOK1

- **Related proteins** (co-abundance neighbors): BBS1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hook microtubule tethering protein 1. This gene encodes a member of the hook family of coiled-coil proteins, which bind to microtubules and organelles through their N- and C-terminal domains, respectively. The encoded protein localizes to discrete punctuate subcellular structures, and interacts with several members of the Rab GTPase family involved in endocytosis. It is thought to link endocytic membrane trafficking to the microtubule…
- **Diseases (Open Targets)**: neurodegenerative disease (0.475); hypothyroidism (0.244); ulcerative colitis (0.217); dementia (0.216); autoimmune thyroid disease (0.200)
- **Europe PMC papers**: 774
- **Why important**: HOOK1 provides a mechanistic bridge between the ciliary-centered signal and the cytoskeleton and membrane-trafficking systems. It binds microtubules and organelles, participates in endosome and lysosome organization, and is annotated for cytoskeleton-dependent intracellular transport. Its HPA pattern includes early and late spermatids and retina, and it is connected directly to the BBS1 hub in the co-abundance graph.
- **Conclusion**: Established evidence supports HOOK1 as a trafficking and cytoskeletal context gene that could be relevant to specialized testicular cells. Its possible role in ciliary transport within this module is a hypothesis, because the provided resources do not list a direct HOOK1 interaction with the IFT components.

#### COG8

- **Related proteins** (co-abundance neighbors): BBS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: component of oligomeric golgi complex 8. This gene encodes a protein that is a component of the conserved oligomeric Golgi (COG) complex, a multiprotein complex that plays a structural role in the Golgi apparatus, and is involved in intracellular membrane trafficking and glycoprotein modification. Mutations in this gene cause congenital disorder of glycosylation, type IIh, a disease that is characterized by under-glycosylated serum prote…
- **Diseases (Open Targets)**: COG8-congenital disorder of glycosylation (0.788); neurodegenerative disease (0.430); Alzheimer disease (0.387); Parkinson disease (0.387); lysosomal storage disease (0.387)
- **Europe PMC papers**: 359
- **Why important**: COG8 represents the Golgi-trafficking arm of the module. It is a component of the conserved oligomeric Golgi complex involved in membrane trafficking and glycoprotein modification, and mutations cause a congenital disorder of glycosylation. It is connected to BBS1 in the module and has Golgi localization and testis detection in the HPA evidence, providing a plausible trafficking context for the ciliary genes.
- **Conclusion**: Established evidence supports COG8 as a Golgi and glycosylation gene that may explain part of the module's intracellular trafficking context. A direct functional coupling between COG8 and the ciliary machinery is only a hypothesis from their shared abundance pattern and is not established by the listed STRING or hu.MAP evidence.

## Module 8

**Tissue pair**: cell line and testis  
**Genes (10)**: CAPZA2, HEBP1, IAH1, IST1, OLA1, OSTF1, PHYHD1, RAB18, MRPS22, VTA1

### Function

No GO or KEGG term passed global correction, and STRING supplied no supplementary enrichment. The module is therefore best interpreted as a mixed cellular-maintenance module rather than as a statistically established pathway. Its genes collectively point to intracellular trafficking and vesicle biology through VTA1, IST1, and RAB18; mitochondrial protein synthesis through MRPS22; actin-filament regulation through CAPZA2; ATPase and centrosome-related biology through OLA1; and possible enzymatic, heme-related, or lipid-associated functions through PHYHD1, IAH1, and HEBP1. The star-like co-abundance structure, with PHYHD1 connected to the other members, indicates that PHYHD1 is the principal expression-level organizer, but co-abundance does not by itself establish direct physical interaction or a single biochemical pathway. The absence of globally significant enrichment should be treated as limited pathway resolution, not as evidence that the module is false.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. All members have low tissue specificity, which is compatible with broadly distributed expression, although this does not establish a housekeeping module. Most genes show cell-type-enhanced rather than tissue-specific patterns, with signals distributed across neutrophils, esophageal apical cells, breast lactating cells, spermatogenic cells, endometrial glandular cells, and other cell types. Immune-cell specificity is low for nearly all members, with only PHYHD1 marked as immune-cell enriched in plasmacytoid dendritic cells. Thus, a simple blood-contamination explanation is not supported, although shared cell-type composition could contribute to the co-abundance pattern. In testis, protein detection is reported for nearly all members, whereas the supplied cell-line HPA protein comparison has no informative tissue match. The spermatocyte and spermatid signals make a testis-associated cellular program plausible, but the broad and heterogeneous HPA pattern argues against assigning the module exclusively to germ cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports only the high-confidence IST1–VTA1 relationship. This is biologically coherent because IST1 is an ESCRT-associated factor and VTA1 participates in multivesicular-body sorting and ESCRT-III disassembly. No other module pair is reported by STRING at the supplied threshold, and no hu.MAP complex contains at least two module members. Therefore, most edges in the co-abundance network are expression relationships without corresponding curated physical-interaction support. The known IST1–VTA1 pair provides a real vesicle-trafficking anchor, but it does not validate the entire module as one established complex.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: IST1–VTA1 (0.996)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact co-abundance module may represent a new systems-level association, because it combines a PHYHD1-centered co-abundance structure with only one known STRING pair and no multi-member hu.MAP complex. However, novelty cannot be concluded solely from absence in STRING or hu.MAP: those resources emphasize physical interactions and curated complexes, whereas co-abundance can reflect shared regulation, cell state, compartmental activity, or cell composition. The defensible conclusion is that this exact cross-context module is potentially novel and is not already explained by a recognized protein complex or canonical enriched pathway. Direct comparison with prior co-abundance studies and independent replication would be required before calling it a definitively new biological discovery.

**Hypothesis.** Hypothesis: the module reflects a coordinated intracellular quality-control and remodeling state in which vesicle and endosomal trafficking, membrane or lipid handling, mitochondrial translational capacity, ATP-dependent cellular maintenance, and cytoskeletal organization vary together. PHYHD1 may mark or help organize this state at the expression level, while the IST1–VTA1 pair supplies a mechanistic vesicle-sorting component and RAB18 links the model to organelle and lipid-droplet trafficking. In testis, this state could support the high membrane, organelle, and structural demands of differentiating germ cells; in cell line samples, it may instead reflect a shared cellular state. This remains a hypothesis because global enrichment is absent, most network edges lack known physical-interaction support, and the HPA cell-type signals are heterogeneous.

### Important genes

#### PHYHD1

- **Related proteins** (co-abundance neighbors): IAH1 (0.88), MRPS22 (0.87), HEBP1 (0.84), OSTF1 (0.84), CAPZA2 (0.83), VTA1 (0.83), OLA1 (0.81), RAB18 (0.81), IST1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phytanoyl-CoA dioxygenase domain containing 1. Enables 2-oxoglutarate-dependent dioxygenase activity. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypercholesterolemia, familial, 1 (0.333); Abnormality of the gastrointestinal tract (0.102); oculocutaneous albinism type 6 (0.074); vitiligo (0.074); acroleukopathy, symmetric (0.074)
- **Europe PMC papers**: 219
- **Why important**: PHYHD1 is the network hub, connected to every other module member with the greatest weighted centrality in the supplied graph. It is annotated as a phytanoyl-CoA dioxygenase-domain-containing protein with putative two-oxoglutarate-dependent dioxygenase activity, but it has no STRING partners, no hu.MAP placement, and no globally significant GO or KEGG annotation in this module. Its HPA profile is broadly distributed but includes several enhanced cell types and an immune-cell-enriched plasmacytoid dendritic-cell signal. Its literature and disease-association record is substantial enough to make it a useful entry point, while the limited interaction annotation makes it especially informative for testing whether the hub is regulatory or merely a co-abundance marker.
- **Conclusion**: Established evidence supports PHYHD1 as the expression-level hub and as a candidate dioxygenase-related protein; it does not establish PHYHD1 as the physical scaffold of the module. My conclusion is that PHYHD1 is the most important discovery candidate and should be experimentally tested for regulation of the other module genes or for association with the inferred cellular state. Any causal role remains hypothetical.

#### VTA1

- **Related proteins** (co-abundance neighbors): PHYHD1 (0.83); STRING partners: IST1 (0.996)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Vesicles, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vesicle trafficking 1. C6ORF55 encodes a protein involved in trafficking of the multivesicular body, an endosomal compartment involved in sorting membrane proteins for degradation in lysosomes (Ward et al., 2005 [PubMed 15644320]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: HIV infectious disease (0.462); Abnormality of the skeletal system (0.267); Menorrhagia (0.251); COVID-19 (0.192); severe acute respiratory syndrome (0.190)
- **Europe PMC papers**: 1165
- **Why important**: VTA1 is important because it forms the only high-confidence STRING interaction within the module, with IST1. Its annotation directly connects it to multivesicular-body assembly, membrane-protein sorting, macroautophagy, and ESCRT-III complex disassembly. It is detected in testis and has a comparatively large literature and disease-association record, although it has no hu.MAP complex containing another module member.
- **Conclusion**: Established evidence supports VTA1 as a vesicle-trafficking and ESCRT-related component and supports its physical relationship with IST1. The conclusion that VTA1 contributes to the broader module is plausible but not proven, because its connection to PHYHD1 and the remaining genes is co-abundance rather than demonstrated interaction.

#### IST1

- **Related proteins** (co-abundance neighbors): PHYHD1 (0.80); STRING partners: VTA1 (0.996)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IST1 factor associated with ESCRT-III. This gene encodes a protein with MIT-interacting motifs that interacts with components of endosomal sorting complexes required for transport (ESCRT). ESCRT functions in vesicle budding, such as that which occurs during membrane abscission in cytokinesis. There is a pseudogene for this gene on chromosome 19. Alternatively spliced transcript variants encoding multiple isoforms have been observed for…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); major depressive disorder (0.364); atrial fibrillation (0.210); Hypercholesterolemia (0.170); abdominal aortic aneurysm (0.153)
- **Europe PMC papers**: 709
- **Why important**: IST1 is the partner of VTA1 in the sole high-confidence STRING pair. It is an ESCRT-associated factor involved in intracellular protein localization, protein transport, multivesicular-body assembly, proteolysis-related regulation, and cell division. Its vesicular localization, testis detection, neutrophil-enhanced signal, and substantial literature make it a strong mechanistic anchor for the trafficking interpretation.
- **Conclusion**: Established evidence supports IST1 as an ESCRT-linked trafficking factor and supports its relationship with VTA1. My conclusion is that IST1 provides the strongest evidence for a vesicle-remodeling component within the module, but its role in coordinating mitochondrial, actin, or enzymatic members remains a hypothesis.

#### RAB18

- **Related proteins** (co-abundance neighbors): PHYHD1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB18, member RAS oncogene family. The protein encoded by this gene is a member of a family of Ras-related small GTPases that regulate membrane trafficking in organelles and transport vesicles. Knockdown studies is zebrafish suggest that this protein may have a role in eye and brain development. Mutations in this gene are associated with Warburg micro syndrome type 3. Alternatively spliced transcript variants have been found for th…
- **Diseases (Open Targets)**: Warburg micro syndrome (0.815); neurodegenerative disease (0.496); cerebral atherosclerosis (0.275); malunion fracture (0.239); adolescent idiopathic scoliosis (0.229)
- **Europe PMC papers**: 2168
- **Why important**: RAB18 is a small GTPase associated with organelle and transport-vesicle trafficking, intracellular protein transport, lipid-droplet organization, sterol homeostasis, and eye and brain development. It has the largest literature and a clear disease association with Warburg micro syndrome among the module members. Its enhanced signals in breast lactating and esophageal apical cells, together with testis protein detection, are consistent with involvement in specialized cells with substantial membrane and secretory demands.
- **Conclusion**: Established evidence supports RAB18 as a regulator of membrane and organelle trafficking with disease relevance. My conclusion is that RAB18 could connect the module's vesicle biology to lipid and organelle remodeling, but the supplied data do not show that RAB18 physically interacts with PHYHD1, VTA1, or IST1.

#### MRPS22

- **Related proteins** (co-abundance neighbors): PHYHD1 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial ribosomal protein S22. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: hypotonia with lactic acidemia and hyperammonemia (0.787); 46 XX gonadal dysgenesis (0.631); neurodegenerative disease (0.525); androgenetic alopecia (0.507); hereditary disease (0.495)
- **Europe PMC papers**: 448
- **Why important**: MRPS22 encodes a mitochondrial small-subunit ribosomal protein and is annotated with mitochondrial translation. It is enhanced in late primary spermatocytes, detected in testis, and has a substantial literature and disease-association record, including links to mitochondrial and gonadal phenotypes. Its presence broadens the module beyond endosomal trafficking and suggests that organelle protein-synthesis capacity may covary with the trafficking state.
- **Conclusion**: Established evidence supports MRPS22 as a mitochondrial translation factor with relevance to mitochondrial and reproductive phenotypes. My conclusion is that MRPS22 is an important marker of a possible organelle-demand component, but linking it mechanistically to the vesicle and cytoskeletal genes is presently a hypothesis rather than an established pathway.

## Module 9

**Tissue pair**: cell line and testis  
**Genes (12)**: CNOT1, DDX6, GYS1, MAPK14, MOV10, PTPN23, SKIC2, THOP1, TNPO1, UBE4B, ATP6V1H, WASHC4

### Function

The most coherent interpretation is a post-transcriptional RNA regulation and RNA-quality-control module, centered on the CNOT1–DDX6–MOV10 connection. CNOT1 is a CCR4-NOT complex subunit involved in mRNA deadenylation, translation repression, and P-body assembly; DDX6 is a P-body RNA helicase involved in decapping, mRNA degradation, translation suppression, and microRNA-mediated silencing; and MOV10 is an RNA helicase involved in RNA binding, antiviral defense, transposable-element silencing, and post-transcriptional regulation. SKIC2 provides a further RNA-decay and ribosome-rescue interpretation. The remaining genes connect this core to protein ubiquitination, nuclear transport, endosomal and lysosomal processes, kinase signaling, peptide processing, and glycogen metabolism. No GO or KEGG term passed global correction, so those databases do not provide a globally significant functional annotation for this module. The functional interpretation is therefore based on the gene functions and network structure rather than on enrichment significance.

**Cell composition.** This does not resemble a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and most have low immune-cell specificity, which is compatible with broadly expressed cellular machinery rather than a tissue-restricted secretome. There is nevertheless a cell-type signal involving neutrophil and neutrophil progenitor annotations, with MAPK14 showing group enrichment in myeloid cells. GYS1 is group-enriched in heart muscle, skeletal muscle, and tongue, and several other genes have cell-type-enhanced annotations across diverse cell types. Thus, the shared cell-line/testis pattern is more plausibly a conserved intracellular program, or a shared cell-state component, than a blood-contamination signature; cellular admixture cannot be excluded from the HPA summary alone. Protein detection in testis is reported for nearly all genes with available results, while cell-line protein detection has no informative matching tissue result.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides strong prior support for a compact RNA-regulatory core: CNOT1 and DDX6 are linked, and DDX6 and MOV10 are also linked. The supplementary STRING annotations place CNOT1, DDX6, MOV10, and MAPK14 in the reported pronephros tissue category (STRING TISSUES Pronephros; within-query FDR = 0.0293), and place CNOT1, MOV10, and DDX6 in the P-body compartment category (STRING COMPARTMENTS P-body; within-query FDR = 0.0451). These are supplementary within-query STRING findings, not globally corrected enrichment results. The module network contains additional high-weight co-abundance links, but STRING does not provide prior partners for several of those genes. hu.MAP reports no complex containing multiple module members. Accordingly, the module partly recapitulates known RNA-processing relationships, while its broader co-abundance structure is not explained by a previously catalogued complex.

**STRING interactions (score >= 0.7)**: 2 of 66 gene pairs: CNOT1–DDX6 (0.999); DDX6–MOV10 (0.746)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Pronephros (FDR = 0.0293, 4 genes); COMPARTMENTS P-body (FDR = 0.0451, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is not established as an entirely new molecular mechanism, because the CNOT1–DDX6–MOV10 relationships and the P-body interpretation have prior STRING support, and the individual gene functions are well documented. However, the conserved co-abundance association across cell line and testis, the connection of the RNA-regulatory core to SKIC2, UBE4B, TNPO1, PTPN23, WASHC4, ATP6V1H, THOP1, MAPK14, and GYS1, and the lack of a corresponding multi-member hu.MAP complex may represent a useful systems-level finding. It should be described as a potentially novel module-level organization, not as proof of a novel physical complex or a newly discovered pathway. Absence from STRING or hu.MAP alone is insufficient to establish novelty.

**Hypothesis.** Hypothesis: in both cell-line and testis contexts, a conserved RNA-quality-control program coordinates helicase-dependent RNA surveillance and post-transcriptional silencing with CNOT1-mediated deadenylation and DDX6 P-body activity. SKIC2 may extend this program toward exonucleolytic mRNA decay and rescue of stalled ribosomes. UBE4B, PTPN23, ATP6V1H, and THOP1 could connect RNA turnover to protein quality control, endosomal or lysosomal handling, and cytosolic peptide processing, while TNPO1 and MAPK14 could provide nuclear-transport and stress or inflammatory signaling links. GYS1 may reflect metabolic state or a cell-state-specific co-abundance connection rather than a direct component of the RNA machinery. This mechanistic model requires validation by perturbation, localization, and physical-interaction experiments.

### Important genes

#### DDX6

- **Related proteins** (co-abundance neighbors): THOP1 (0.82), MOV10 (0.80); STRING partners: CNOT1 (0.999), MOV10 (0.746)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytoplasmic bodies; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 6. This gene encodes a member of the DEAD box protein family. The protein is an RNA helicase found in P-bodies and stress granules, and functions in translation suppression and mRNA degradation. It is required for microRNA-induced gene silencing. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: intellectual developmental disorder with impaired language and dysmorphic facies (0.650); Intellectual disability (0.555); neurodegenerative disease (0.459); lung carcinoma (0.371); Global developmental delay (0.371)
- **Europe PMC papers**: 3002
- **Why important**: DDX6 is a direct bridge between the RNA-regulatory interpretation and the observed network: it connects to MOV10 and THOP1 and has STRING links to CNOT1 and MOV10. Its established functions include P-body localization, mRNA decapping and degradation, translation repression, microRNA-mediated silencing, and spermatogenesis. It also has the largest literature volume among the selected RNA-core genes.
- **Conclusion**: Established: DDX6 is a strong mechanistic anchor for RNA turnover and P-body biology in this module. Hypothesis: its co-abundance with the other module members reflects coordinated RNA-quality-control activity in testis and cell line rather than merely shared expression.

#### CNOT1

- **Related proteins** (co-abundance neighbors): WASHC4 (0.85), MOV10 (0.82), PTPN23 (0.80); STRING partners: DDX6 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CCR4-NOT transcription complex subunit 1. Enables armadillo repeat domain binding activity; molecular adaptor activity; and nuclear receptor binding activity. Contributes to poly(A)-specific ribonuclease activity. Involved in several processes, including negative regulation of signal transduction; positive regulation of cytoplasmic mRNA processing body assembly; and regulation of gene expression. Located in P-body and cytosol. Part of CCR…
- **Diseases (Open Targets)**: holoprosencephaly 12 with or without pancreatic agenesis (0.749); Vissers-Bodmer syndrome (0.697); hereditary disease (0.515); complex neurodevelopmental disorder (0.474); neurodegenerative disease (0.471)
- **Europe PMC papers**: 1262
- **Why important**: CNOT1 is the highest-confidence scaffold for the deadenylation and translation-control interpretation. It connects to MOV10, PTPN23, and WASHC4, has a STRING relationship with DDX6, and is a core CCR4-NOT complex subunit involved in mRNA deadenylation, P-body assembly, and negative regulation of translation. Its disease associations include holoprosencephaly and neurodevelopmental disorders.
- **Conclusion**: Established: CNOT1 can mechanistically support the module's post-transcriptional regulatory interpretation. Hypothesis: the module may coordinate CCR4-NOT activity with endosomal and RNA-helicase processes through the CNOT1 neighborhood.

#### MOV10

- **Related proteins** (co-abundance neighbors): PTPN23 (0.83), SKIC2 (0.83), CNOT1 (0.82), UBE4B (0.80), DDX6 (0.80); STRING partners: DDX6 (0.746)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Mov10 RNA helicase. Enables 5'-3' RNA helicase activity and RNA binding activity. Involved in defense response to virus; negative regulation of transposition, RNA-mediated; and posttranscriptional regulation of gene expression. Located in P-body and cytosol. Implicated in hypertension. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.516); cancer (0.467); Thrombocytopenia (0.364); open-angle glaucoma (0.344); hypertensive disorder (0.329)
- **Europe PMC papers**: 1449
- **Why important**: MOV10 has one of the strongest and most central positions in the module, linking PTPN23, SKIC2, CNOT1, UBE4B, and DDX6. It is an RNA helicase involved in antiviral defense, transposable-element silencing, microRNA-mediated regulation, and spermatogenesis. It appears in both supplementary STRING categories (STRING TISSUES Pronephros; within-query FDR = 0.0293) and (STRING COMPARTMENTS P-body; within-query FDR = 0.0451), and has substantial literature and disease-association support.
- **Conclusion**: Established: MOV10 is a plausible central RNA-regulatory connector supported by both network position and prior interaction evidence. Hypothesis: MOV10 may couple RNA silencing to protein or endosomal quality-control processes represented by neighboring genes.

#### SKIC2

- **Related proteins** (co-abundance neighbors): GYS1 (0.87), UBE4B (0.84), TNPO1 (0.83), ATP6V1H (0.83), MOV10 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SKI2 subunit of superkiller complex. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: trichohepatoenteric syndrome (0.745); immunodeficiency 57 (0.340); hereditary disease (0.195); African iron overload (0.059); maple syrup urine disease (0.058)
- **Europe PMC papers**: 360
- **Why important**: SKIC2 has the strongest network position in the module and connects the RNA-centered genes to GYS1, UBE4B, TNPO1, and ATP6V1H. Its annotation supports nuclear-transcribed mRNA catabolism, nonsense-mediated and nonstop decay, and rescue of stalled cytosolic ribosomes. It therefore supplies a complementary RNA-decay mechanism to the CNOT1–DDX6–MOV10 core.
- **Conclusion**: Established: SKIC2 supports an mRNA surveillance and ribosome-quality-control interpretation. Hypothesis: its broad network connectivity may indicate coordination between RNA decay and cellular stress or metabolic state, although the module does not establish direct binding.

#### MAPK14

- **Related proteins** (co-abundance neighbors): UBE4B (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Nuclear speckles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitogen-activated protein kinase 14. The protein encoded by this gene is a member of the MAP kinase family. MAP kinases act as an integration point for multiple biochemical signals, and are involved in a wide variety of cellular processes such as proliferation, differentiation, transcription regulation and development. This kinase is activated by various environmental stresses and proinflammatory cytokines. The activation requires it…
- **Diseases (Open Targets)**: neurodegenerative disease (0.464); autoimmune disorder of central nervous system (0.459); Alzheimer disease (0.337); Parkinson disease (0.316); lysosomal storage disease (0.303)
- **Europe PMC papers**: 8074
- **Why important**: MAPK14 is the module's most notable signaling and cell-composition marker. It is connected to UBE4B, has supplementary STRING support in (STRING TISSUES Pronephros; within-query FDR = 0.0293), and is HPA-group-enriched in monocyte progenitors, neutrophil progenitors, and neutrophils, including blood-cell annotations. Its established functions include stress- and cytokine-responsive MAPK signaling, transcriptional regulation, and inflammatory responses.
- **Conclusion**: Established: MAPK14 may report a stress or myeloid-associated component of the co-abundance pattern. Hypothesis: MAPK14 could modulate RNA-quality-control activity indirectly through stress signaling, but the present network does not demonstrate such causality.

#### GYS1

- **Related proteins** (co-abundance neighbors): SKIC2 (0.87), TNPO1 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Microtubules, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycogen synthase 1. The protein encoded by this gene catalyzes the addition of glucose monomers to the growing glycogen molecule through the formation of alpha-1,4-glycoside linkages. Mutations in this gene are associated with muscle glycogen storage disease. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: glycogen storage disease due to muscle and heart glycogen synthase deficiency (0.784); disorder of glycogen metabolism (0.530); neurodegenerative disease (0.440); glycogen storage disease XV (0.382); congenital myasthenic syndrome (0.266)
- **Europe PMC papers**: 1794
- **Why important**: GYS1 is a biologically informative peripheral member because it is group-enriched in heart muscle, skeletal muscle, and tongue and is associated with glycogen metabolism and glycogen-storage disease. It connects to SKIC2 and TNPO1, linking metabolic storage to the RNA-decay and nuclear-transport side of the module. Its disease associations are particularly relevant to muscle and heart biology.
- **Conclusion**: Established: GYS1 marks a metabolic and muscle-associated dimension of the module. Hypothesis: its co-abundance may reflect energetic state or cell-state coupling to RNA surveillance, rather than GYS1 being a core component of the P-body machinery.

## Module 10

**Tissue pair**: cell line and testis  
**Genes (7)**: FGA, FGG, NCKAP1, SRP68, TARS1, CCT7, TKFC

### Function

The module does not have a GO or KEGG term that passed global correction, so no pathway-level enrichment can be claimed. Its strongest biological signal is a fibrinogen-associated extracellular and coagulation context, supported only as supplementary evidence by the SMART fibrinogen-family terms (STRING SMART Fibrinogen alpha/beta chain family; within-query FDR = 0.0295) and (STRING SMART Fibrinogen-related domains (FReDs); within-query FDR = 0.0309). FGA and FGG form the only high-confidence STRING interaction, and both occur together across the hu.MAP complexes (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1). The remaining co-abundance structure connects FGA with SRP68 and CCT7, SRP68 with TARS1 and TKFC, and TARS1 with NCKAP1. These genes represent protein targeting, translation, chaperoning, carbohydrate and glycerol metabolism, and actin-regulatory processes rather than a single established molecular pathway. Thus, the most defensible interpretation is a mixed module combining a fibrinogen or secreted-protein signal with broadly expressed intracellular protein-handling and cellular-physiology genes.

**Cell composition.** The module is not predominantly composed of immune-cell-enriched genes, because the HPA summary reports low immune-cell specificity or no immune-cell detection for the genes. FGA and FGG are secreted blood proteins with liver and hepatocyte enrichment, making them plausible indicators of plasma carryover, vascular material, or shared extracellular protein abundance rather than testis-cell biology. The other genes are nonsecreted intracellular proteins and are mostly broadly expressed, although SRP68, TARS1, NCKAP1, CCT7, and TKFC are detected in testis and some show testis or germ-cell-related HPA patterns. The contrast between the liver or hepatocyte signal for the fibrinogen genes and the testis detection of several intracellular genes argues against treating the entire module as a testis-specific program. It may instead reflect mixed cellular composition, extracellular protein contamination or transport, and a shared protein-abundance background.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

Known molecular support is concentrated in the FGA–FGG pair: STRING reports this interaction with very high confidence, and the pair is repeatedly represented in hu.MAP complexes (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1). Those complexes contain many other plasma, coagulation, complement, transport, and acute-phase proteins, so their presence supports a known fibrinogen-associated extracellular network but does not establish that the complete module is one physical complex. SRP68, TARS1, NCKAP1, CCT7, and TKFC have no listed STRING partners within this module and no listed hu.MAP complexes. Therefore, the co-abundance edges involving those genes are not independently validated here as physical interactions. The network may capture correlated expression, shared sample composition, or indirect cellular processes rather than direct protein binding.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: FGA–FGG (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Fibrinogen alpha/beta chain family (FDR = 0.0295, 2 genes); SMART Fibrinogen-related domains (FReDs) (FDR = 0.0309, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02242.1 (FGA, FGG; 2/9); huMAP3_08224.1 (FGA, FGG; 2/21); huMAP3_09434.1 (FGA, FGG; 2/33); huMAP3_08395.1 (FGA, FGG; 2/43); huMAP3_09531.1 (FGA, FGG; 2/47); huMAP3_10101.1 (FGA, FGG; 2/49); huMAP3_15040.1 (FGA, FGG; 2/64); huMAP3_10678.1 (FGA, FGG; 2/71)

### Novelty

The module as a complete biological unit should not be called a new fibrinogen complex or a newly discovered interaction network. The FGA–FGG relationship is already known from STRING, and the repeated hu.MAP representation of this pair places it in established plasma-protein complexes. The other module edges are not represented by the supplied STRING or hu.MAP evidence, but database absence does not prove that they are novel or nonexistent. A cautious conclusion is that the co-abundance combination may be a new tissue-pair observation, while its strongest biochemical component is established and its broader mechanistic interpretation remains unvalidated. The lack of globally significant GO or KEGG enrichment further limits claims of a newly defined pathway, without making the module itself false.

**Hypothesis.** Hypothesis: the shared cell-line and testis module may arise from a mixture of extracellular fibrinogen abundance and intracellular protein-production or quality-control activity. In this model, FGA and FGG reflect hepatocyte-derived or plasma-associated material, while SRP68 could mark synthesis and endoplasmic-reticulum targeting of secreted proteins; CCT7 could support folding of newly produced proteins; TARS1 could reflect translational capacity; and TKFC or NCKAP1 could contribute metabolic or cytoskeletal context. The observed co-abundance could therefore reflect coordinated sample composition or proteostasis around secreted-protein handling rather than direct assembly of all module proteins. This hypothesis requires validation with cell-type-resolved data, plasma-depletion or contamination controls, and targeted protein or RNA measurements.

### Important genes

#### FGA

- **Related proteins** (co-abundance neighbors): FGG (0.89), SRP68 (0.82), CCT7 (0.82); STRING partners: FGG (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02242.1, huMAP3_08224.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: fibrinogen alpha chain. This gene encodes the alpha subunit of the coagulation factor fibrinogen, which is a component of the blood clot. Following vascular injury, the encoded preproprotein is proteolytically processed by thrombin during the conversion of fibrinogen to fibrin. Mutations in this gene lead to several disorders, including dysfibrinogenemia, hypofibrinogenemia, afibrinogenemia and renal amyloidosis. Alterna…
- **Diseases (Open Targets)**: familial dysfibrinogenemia (0.789); familial visceral amyloidosis (0.765); congenital afibrinogenemia (0.757); familial hypodysfibrinogenemia (0.659); congenital fibrinogen deficiency (0.619)
- **Europe PMC papers**: 7516
- **Why important**: FGA has the strongest network position in the module and connects the fibrinogen signal to SRP68 and CCT7, in addition to its direct STRING relationship with FGG. It encodes the fibrinogen alpha chain, a secreted blood-clot component involved in coagulation, platelet activation, cell-matrix adhesion, plasminogen activation, and fibrinolysis. HPA assigns it to liver and hepatocytes and identifies it as secreted to blood. It is extensively studied and is associated with familial dysfibrinogenemia, afibrinogenemia, hypofibrinogenemia, and related fibrinogen disorders.
- **Conclusion**: Established evidence supports FGA as the principal extracellular and coagulation-related anchor of the module, not as evidence for a testis-specific function. Its central position may reflect correlation with secreted-protein handling or sample-derived plasma material. A direct functional bridge from FGA to the intracellular module members remains a hypothesis.

#### FGG

- **Related proteins** (co-abundance neighbors): FGA (0.89); STRING partners: FGA (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02242.1, huMAP3_08224.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: fibrinogen gamma chain. The protein encoded by this gene is the gamma component of fibrinogen, a blood-borne glycoprotein comprised of three pairs of nonidentical polypeptide chains. Following vascular injury, fibrinogen is cleaved by thrombin to form fibrin which is the most abundant component of blood clots. In addition, various cleavage products of fibrinogen and fibrin regulate cell adhesion and spreading, display va…
- **Diseases (Open Targets)**: familial dysfibrinogenemia (0.787); congenital afibrinogenemia (0.753); congenital fibrinogen deficiency (0.617); familial hypodysfibrinogenemia (0.597); cancer (0.596)
- **Europe PMC papers**: 4006
- **Why important**: FGG is the direct STRING partner of FGA and the second module member represented across all listed hu.MAP complexes. It encodes the fibrinogen gamma chain, participates in fibrin formation, and has reported roles in cell adhesion, platelet activation, plasminogen activation, protein secretion, and related extracellular signaling. HPA assigns it to liver and hepatocytes and identifies it as secreted to blood. It has substantial literature and disease associations involving congenital fibrinogen deficiency and dysfibrinogenemia.
- **Conclusion**: Established evidence identifies FGG as a genuine fibrinogen component and the best-supported molecular relationship in the module through its FGA pairing. Its module membership is therefore biologically credible, but it does not establish that the intracellular neighbors are part of the same fibrinogen complex. The shared abundance may reflect extracellular material or coordinated secretory context.

#### SRP68

- **Related proteins** (co-abundance neighbors): TARS1 (0.84), FGA (0.82), TKFC (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal recognition particle 68. This gene encodes a subunit of the signal recognition particle (SRP). The SRP is a ribonucleoprotein complex that transports secreted and membrane proteins to the endoplasmic reticulum for processing. The complex includes a 7S RNA and six protein subunits. The encoded protein is the 68kDa component of the SRP, and forms a heterodimer with the 72kDa subunit that is required for SRP function. Altern…
- **Diseases (Open Targets)**: neurodegenerative disease (0.347); neutropenia, severe congenital, 10, autosomal recessive (0.333); COVID-19 (0.155); metabolic syndrome (0.074); atrial septal defect (0.073)
- **Europe PMC papers**: 440
- **Why important**: SRP68 is a network bridge linking FGA to TARS1 and TKFC. It encodes a signal-recognition-particle subunit involved in signal-sequence recognition and co-translational targeting of proteins to the endoplasmic reticulum, making it mechanistically relevant to production of secreted proteins. HPA reports testis detection and enhanced expression in selected cell types, while also describing low tissue specificity. Its literature base is smaller than that of the fibrinogen genes, and the supplied STRING and hu.MAP data provide no independent interaction support.
- **Conclusion**: Established evidence supports SRP68 as a plausible protein-targeting component whose function is compatible with the fibrinogen-related signal. The proposed connection between SRP68 and FGA may indicate coordinated secretory activity, but the co-abundance edge is not established as a direct physical interaction. Its role in this module should therefore be considered mechanistically plausible rather than demonstrated.

#### CCT7

- **Related proteins** (co-abundance neighbors): FGA (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 connects directly to FGA and encodes a subunit of the CCT or TRiC chaperonin, which folds proteins including actin and tubulin. HPA reports enhancement in early spermatids, late primary spermatocytes, and late spermatids, and testis protein detection. This gives CCT7 particular relevance to the cell-line and testis comparison, although its low tissue specificity and lack of STRING or hu.MAP support within the module argue against a specialized fibrinogen complex. It has a substantial literature base and reported associations including myocardial infarction, preeclampsia, neurodegenerative disease, and hepatocellular carcinoma.
- **Conclusion**: Established evidence supports CCT7 as a protein-folding factor with a notable germ-cell expression context. Its co-abundance with FGA could reflect shared protein-production or proteostasis conditions, but no direct connection to fibrinogen is established. A testis-related chaperone interpretation is plausible, yet it should not be presented as the definitive function of the whole module.
