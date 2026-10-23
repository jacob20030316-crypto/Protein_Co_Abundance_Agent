# Conserved co-abundance modules: cell line and prostate

## Module 0

**Tissue pair**: cell line and prostate  
**Genes (10)**: BZW2, CARM1, HSP90AA1, MCM5, NAA15, CCT3, TMEM214, VPS35, XPO1, CSE1L

### Function

This is best interpreted as a candidate intracellular cell-state and protein-homeostasis module rather than a securely defined pathway. The genes collectively point to coordination among nuclear transport, protein folding, DNA replication, chromatin regulation, endosomal trafficking, and apoptosis-related processes. BZW2 is the most connected node and links NAA15, MCM5, CSE1L, VPS35, and CARM1, while XPO1 connects nuclear export with NAA15 and TMEM214. MCM5 and HSP90AA1 connect replication-related and chaperone-related biology, and CCT3 provides additional protein-folding support. No GO or KEGG term passed global correction, so the functional interpretation is hypothesis-generating and should not be presented as pathway enrichment. The absence of significant enrichment does not invalidate the co-abundance module.

**Cell composition.** The module does not resemble a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It also does not show a blood-cell signature. Most genes have low tissue specificity, and the blood-cell evidence is generally low immune-cell specificity or absence from immune cells. A smaller subset is enhanced in muscle, tongue, bone marrow, trophoblast, spermatogonial, erythrocyte-progenitor, or ductal cell contexts. Thus, the shared signal is more consistent with broadly expressed intracellular machinery or a shared cellular state than with contamination by circulating proteins or a general immune-cell infiltrate. The tissue and single-cell enrichments may nevertheless indicate contributions from particular cell states in either sample set.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest established pairwise relationships are the STRING interactions between CSE1L and XPO1 and between CCT3 and HSP90AA1. These relationships support a nuclear transport component and a chaperone component, respectively. The module contains no STRING functional-enrichment result, so STRING does not independently establish a common pathway. hu.MAP identifies four complexes containing both XPO1 and CSE1L: (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_09592.1). In each case these are only partial overlaps with much larger complexes, so they support a recurring association of XPO1 and CSE1L but do not show that the entire module is one physical complex. The remaining co-abundance links are not supported by the supplied high-confidence STRING interactions and may reflect coordinated expression, indirect regulation, or shared cell state rather than direct binding.

**STRING interactions (score >= 0.7)**: 2 of 45 gene pairs: CCT3–HSP90AA1 (0.767); CSE1L–XPO1 (0.976)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07170.1 (XPO1, CSE1L; 2/14); huMAP3_09042.1 (XPO1, CSE1L; 2/26); huMAP3_06791.1 (XPO1, CSE1L; 2/31); huMAP3_09592.1 (XPO1, CSE1L; 2/95)

### Novelty

The module may be a new co-abundance observation, but the biological components themselves are not novel. XPO1-CSE1L and CCT3-HSP90AA1 are already supported by STRING, and XPO1-CSE1L recurs in several hu.MAP complexes. Several genes also have well-established functions and substantial literature. The potentially novel aspect is the reproducible co-abundance of this particular combination across cell line and prostate, especially the way BZW2 connects transport, replication, chaperone, trafficking, and chromatin-associated genes. However, absence of additional STRING or hu.MAP relationships cannot establish novelty. A stronger novelty claim would require comparison with published prostate and cell-line coexpression modules, replication in independent cohorts, and testing whether the module predicts a defined phenotype.

**Hypothesis.** Hypothesis: the module reflects a shared proliferative or stress-adaptive intracellular state in which nuclear export and import-related machinery, nascent-protein processing, chaperone capacity, DNA replication competence, chromatin regulation, and membrane or endosomal trafficking are coordinately maintained. In this model, XPO1-CSE1L represents a transport-related anchor, CCT3-HSP90AA1 represents protein-folding capacity, MCM5 represents replication readiness, and BZW2 coordinates several otherwise weakly connected components. This is a mechanistic hypothesis rather than an established pathway assignment; it should be tested with protein-level interaction assays, perturbation of XPO1 or BZW2, cell-cycle and stress measurements, and validation in independent prostate and cell-line datasets.

### Important genes

#### BZW2

- **Related proteins** (co-abundance neighbors): NAA15 (0.85), MCM5 (0.83), CSE1L (0.83), VPS35 (0.81), CARM1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: basic leucine zipper and W2 domains 2. Enables cadherin binding activity. Predicted to be involved in cell differentiation and nervous system development. Located in cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Alzheimer disease (0.212); alopecia areata (0.159); hepatocellular carcinoma (0.089); lung adenocarcinoma (0.082); colorectal carcinoma (0.080)
- **Europe PMC papers**: 382
- **Why important**: BZW2 is the central network connector, linking NAA15, MCM5, CSE1L, VPS35, and CARM1. Its annotation supports regulation of translational initiation and cadherin binding, while HPA places it in cytosol, actin-filament, and plasma-membrane contexts and shows enhancement in muscle and trophoblast-related cell types. It has a substantial literature base and disease associations spanning neurodegenerative and cancer-related indications.
- **Conclusion**: Established evidence supports BZW2 as the strongest organizational candidate within this module and as a regulator associated with translation-related biology. Its role as the coordinator of the module is a hypothesis inferred from co-abundance and network position, not a demonstrated molecular mechanism.

#### XPO1

- **Related proteins** (co-abundance neighbors): NAA15 (0.82), TMEM214 (0.82); STRING partners: CSE1L (0.976)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_07170.1, huMAP3_09042.1, huMAP3_06791.1, huMAP3_09592.1
- **Function (MyGene.info)**: exportin 1. This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSe…
- **Diseases (Open Targets)**: plasma cell myeloma (0.642); B-cell chronic lymphocytic leukemia (0.626); diffuse large B-cell lymphoma (0.602); HIV infectious disease (0.561); neurodegenerative disease (0.522)
- **Europe PMC papers**: 5357
- **Why important**: XPO1 is a nuclear export factor with annotations covering export of proteins, messenger RNA, and ribosomal subunits. It is connected to NAA15 and TMEM214 in the module, has the strongest supplied STRING relationship with CSE1L, and appears with CSE1L in every listed hu.MAP complex (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_09592.1). It is also highly studied and associated with hematologic malignancy, viral infection, and other disease areas.
- **Conclusion**: Established evidence identifies XPO1 as a major nuclear-transport component and the best-supported physical-interaction anchor of the module. It is plausible that altered nuclear export contributes to the shared co-abundance state, but the supplied data do not demonstrate that XPO1 drives the other module genes.

#### MCM5

- **Related proteins** (co-abundance neighbors): BZW2 (0.83), HSP90AA1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: minichromosome maintenance complex component 5. The protein encoded by this gene is structurally very similar to the CDC46 protein from S. cerevisiae, a protein involved in the initiation of DNA replication. The encoded protein is a member of the MCM family of chromatin-binding proteins and can interact with at least two other members of this family. The encoded protein is upregulated in the transition from the G0 to G1/S phase of the cell cycl…
- **Diseases (Open Targets)**: Meier-Gorlin syndrome (0.563); neurodegenerative disease (0.397); lysosomal storage disease (0.362); kidney transplant (0.198); diabetic ketoacidosis (0.129)
- **Europe PMC papers**: 4143
- **Why important**: MCM5 is a core component of the DNA-replication initiation machinery and is annotated in replication initiation, replication-associated repair, and cell-cycle regulation. It connects BZW2 and HSP90AA1, thereby linking the module's central connector to the chaperone branch. HPA detects MCM5 in prostate and shows enhancement in bone marrow and several progenitor or germ-cell contexts. It has a very substantial literature base and disease associations including Meier-Gorlin syndrome.
- **Conclusion**: Established evidence supports MCM5 as a replication-competence marker within the module. Its presence is compatible with a proliferative or progenitor-like cell state, but the module alone cannot establish active DNA replication or a specific cell-cycle phase.

#### HSP90AA1

- **Related proteins** (co-abundance neighbors): CCT3 (0.82), MCM5 (0.81); STRING partners: CCT3 (0.767)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein 90 alpha family class A member 1. The protein encoded by this gene is an inducible molecular chaperone that functions as a homodimer. The encoded protein aids in the proper folding of specific target proteins by use of an ATPase activity that is modulated by co-chaperones. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: cancer (0.643); plasma cell myeloma (0.404); non-small cell lung carcinoma (0.394); dengue disease (0.375); Orthomyxoviridae infectious disease (0.375)
- **Europe PMC papers**: 8215
- **Why important**: HSP90AA1 is an inducible ATP-dependent molecular chaperone involved in folding selected client proteins. It connects MCM5 and CCT3, and its STRING relationship with CCT3 provides independent support for a protein-homeostasis branch. It is broadly expressed, extensively studied, and associated with cancer, plasma-cell myeloma, and host responses to infection.
- **Conclusion**: Established evidence supports HSP90AA1 as a chaperone and stress-responsive component of the module. A coordinated chaperone and replication signal is consistent with proteotoxic or proliferative adaptation, but stress activation itself is not proven by the co-abundance data.

#### CSE1L

- **Related proteins** (co-abundance neighbors): BZW2 (0.83); STRING partners: XPO1 (0.976)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07170.1, huMAP3_09042.1, huMAP3_06791.1, huMAP3_09592.1
- **Function (MyGene.info)**: chromosome segregation 1 like. Proteins that carry a nuclear localization signal (NLS) are transported into the nucleus by the importin-alpha/beta heterodimer. Importin-alpha binds the NLS, while importin-beta mediates translocation through the nuclear pore complex. After translocation, RanGTP binds importin-beta and displaces importin-alpha. Importin-alpha must then be returned to the cytoplasm, leaving the NLS protein behind.…
- **Diseases (Open Targets)**: intelligence (0.293); neurodegenerative disease (0.269); Alzheimer disease (0.199); celiac disease (0.187); autism spectrum disorder (0.178)
- **Europe PMC papers**: 860
- **Why important**: CSE1L is a nuclear-transport factor that recycles importin-alpha after nuclear import. It has the strongest supplied STRING association with XPO1 and shares membership with XPO1 in all listed hu.MAP complexes (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_09592.1). Its annotations support intracellular protein transport, and its cell-type enhancements include spermatocyte and erythrocyte-progenitor contexts. The gene has a meaningful literature base and disease associations involving neurodevelopmental and neurodegenerative conditions.
- **Conclusion**: Established evidence supports CSE1L as the second transport-related anchor and as a known partner of XPO1. Its placement in the module may indicate coordinated nuclear-trafficking demand, but the data do not establish whether this reflects transport activity, cell-cycle state, or an indirect expression program.

## Module 1

**Tissue pair**: cell line and prostate  
**Genes (11)**: ACLY, ACSL3, COG2, COPG2, FLII, CARS1, EPRS1, IARS1, LARS1, RARS1, UTP20

### Function

The module is most strongly interpreted as a cytosolic protein-translation and tRNA-charging module. The primary evidence is the coherent set of globally corrected terms for aminoacyl-tRNA ligase activity, tRNA aminoacylation for protein translation, amino acid activation, aminoacyl-tRNA biosynthesis, the aminoacyl-tRNA synthetase multienzyme complex, catalytic activity on tRNA, and tRNA metabolism (10 globally significant GO/KEGG terms, q_global 0.00128–0.0162; see the table). Five module genes, CARS1, EPRS1, IARS1, LARS1, and RARS1, account for the central aminoacylation signal. ACSL3 contributes a broader ligase-related signal, whereas ACLY, FLII, COG2, UTP20, and COPG2 do not have globally significant GO/KEGG annotations in this module. Their presence is therefore better viewed as network context rather than evidence for a second established pathway. The module is consistent with coordinated translational capacity and amino-acid sensing, with possible links to lipid metabolism, Golgi trafficking, actin organization, and ribosome biogenesis.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the annotated proteins are predominantly intracellular, especially cytosolic or nucleoplasmic. It is also not strongly blood-cell enriched. HPA reports low immune-cell specificity for nearly all genes and no enriched blood-cell category. Most genes have low tissue specificity, which is compatible with broadly expressed housekeeping or core-growth functions rather than a prostate-exclusive program. Some cell-type enhancement is present, including prostatic glandular cells for ACSL3, but also salivary acinar cells, pancreatic islet cells, spermatogenic cells, lacrimal acinar cells, adipocytes, epicardial cells, and thyrotrophs. Therefore, the shared cell-line and prostate module is more plausibly a conserved intracellular biosynthetic program or shared cellular-state signal than an artifact caused by blood contamination. HPA protein detection in prostate supports expression of much of the module there, but lack of detection for some genes should not be treated as evidence of absence.

**GO/KEGG enrichment**: 10 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF aminoacyl-tRNA ligase activity | 0.00128 | CARS1, EPRS1, IARS1, LARS1, RARS1 |
| GO:BP tRNA aminoacylation for protein translation | 0.00128 | CARS1, EPRS1, IARS1, LARS1, RARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 0.00128 | CARS1, EPRS1, IARS1, LARS1, RARS1 |
| GO:BP amino acid activation | 0.00128 | CARS1, EPRS1, IARS1, LARS1, RARS1 |
| GO:BP tRNA aminoacylation | 0.00128 | CARS1, EPRS1, IARS1, LARS1, RARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 0.00128 | CARS1, EPRS1, IARS1, LARS1, RARS1 |
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 0.00148 | EPRS1, IARS1, LARS1, RARS1 |
| GO:MF ligase activity | 0.00405 | ACSL3, CARS1, EPRS1, IARS1, LARS1, RARS1 |
| GO:MF catalytic activity, acting on a tRNA | 0.00703 | CARS1, EPRS1, IARS1, LARS1, RARS1 |
| GO:BP tRNA metabolic process | 0.0162 | CARS1, EPRS1, IARS1, LARS1, RARS1 |

### STRING and hu.MAP

STRING independently supports a dense, known relationship structure among the five core synthetase genes. CARS1 connects to EPRS1, IARS1, LARS1, and RARS1, while EPRS1, IARS1, LARS1, and RARS1 show especially strong mutual STRING relationships (14 supplementary STRING terms; within-query FDR 0.00024–0.0033). STRING also supports the aminoacyl-tRNA biosynthesis interpretation, the Rossmann-like fold, class-I synthetase features, cytosolic tRNA aminoacylation, and the synthetase multienzyme complex (14 supplementary STRING terms; within-query FDR 0.00024–0.0033). These relationships indicate that a substantial part of the module recapitulates established biology rather than representing an entirely unknown interaction system. hu.MAP independently places EPRS1, IARS1, LARS1, and RARS1 together in two complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), with additional aminoacyl-tRNA synthetases, auxiliary proteins, and assembly factors. The remaining module genes have weaker or absent STRING and hu.MAP support: COG2 and UTP20 occur in a larger hu.MAP complex (hu.MAP huMAP3_11232.1), while ACLY, FLII, ACSL3, COG2, UTP20, and COPG2 lack the corresponding direct STRING support listed in the fact sheet. Thus, the network contains a well-supported synthetase core plus peripheral co-abundance links that may reflect shared expression, cellular state, or indirect metabolic coupling.

**STRING interactions (score >= 0.7)**: 10 of 55 gene pairs: CARS1–EPRS1 (0.849); CARS1–IARS1 (0.905); CARS1–LARS1 (0.95); CARS1–RARS1 (0.805); EPRS1–IARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–RARS1 (0.999); IARS1–LARS1 (0.999); IARS1–RARS1 (0.999); LARS1–RARS1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Aminoacyl-tRNA biosynthesis (FDR = 0.00024, 5 genes); InterPro Rossmann-like alpha/beta/alpha sandwich fold (FDR = 0.00024, 5 genes); InterPro Aminoacyl-tRNA synthetase, class Ia, anticodon-binding (FDR = 0.00032, 4 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 0.00033, 5 genes); Keyword Ligase (FDR = 0.00033, 6 genes); RCTM Cytosolic tRNA aminoacylation (FDR = 0.00051, 5 genes); NetworkNeighborAL tRNA Aminoacylation (FDR = 0.00066, 5 genes); InterPro Aminoacyl-tRNA synthetase, class I, conserved site (FDR = 0.00079, 4 genes); Function aminoacyl-tRNA ligase activity (FDR = 0.00092, 5 genes); Function Ligase activity (FDR = 0.00095, 6 genes); Component aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.0013, 4 genes); COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.0018, 4 genes); Keyword Protein biosynthesis (FDR = 0.0023, 5 genes); Process tRNA aminoacylation for protein translation (FDR = 0.0033, 5 genes); Process Amide biosynthetic process (FDR = 0.0033, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, IARS1, RARS1, LARS1; 4/14); huMAP3_13688.1 (EPRS1, IARS1, RARS1, LARS1; 4/14); huMAP3_11232.1 (UTP20, COG2; 2/78)

### Novelty

The functional core is not a new molecular function: aminoacyl-tRNA synthetases, cytosolic tRNA charging, and their multisynthetase complexes are already established by the primary annotations, STRING, and hu.MAP. The module may nevertheless represent a new systems-level observation if the coordinated abundance pattern is reproducibly conserved between cell line and prostate and if its peripheral links, particularly those to ACLY, FLII, COG2, UTP20, ACSL3, and COPG2, are not previously described in this tissue-pair context. However, the fact sheet alone cannot establish that the complete module or its cross-tissue conservation has never been reported. Absence of STRING or hu.MAP support for peripheral genes is evidence of limited prior database support, not proof of novelty. The most defensible conclusion is that this is a biologically credible conserved module with a known translation-related core and a potentially novel tissue-pair-specific co-abundance organization.

**Hypothesis.** Hypothesis: the module reflects a conserved biosynthetic state in which cytosolic aminoacyl-tRNA charging is coordinated with cellular growth and protein production. The synthetase core may supply translational fidelity and throughput, while LARS1 may connect amino-acid availability to nutrient-responsive signaling. The association with ACLY and ACSL3 suggests that cytosolic acetyl-CoA and fatty-acyl-CoA metabolism could be coupled to the translational state, whereas UTP20, COG2, COPG2, and FLII may mark linked demands for ribosome production, Golgi trafficking, and cytoskeletal organization. This is a mechanistic model rather than an established physical pathway: co-abundance does not demonstrate direct regulation, complex membership, or causal coupling for the peripheral genes.

### Important genes

#### EPRS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.86), RARS1 (0.85), LARS1 (0.85), ACSL3 (0.82), CARS1 (0.81), COPG2 (0.80); STRING partners: CARS1 (0.849), IARS1 (0.999), LARS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is the most central node by the supplied network measures and connects the synthetase core with ACSL3 and COPG2. It is present in every primary GO/KEGG term (10 globally significant GO/KEGG terms, q_global 0.00128–0.0162; see the table), in the STRING aminoacylation terms (15 supplementary STRING terms; within-query FDR 0.00024–0.0033), and in both relevant hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Its established function is glutamyl- and prolyl-tRNA aminoacylation, and the fact sheet documents a substantial literature and disease-association record.
- **Conclusion**: Established: EPRS1 is a strong anchor for the module's translation and multisynthetase-complex interpretation. Hypothesis: its central network position may make it an organizing or state-reporting node linking translational demand to the peripheral metabolic and trafficking signals.

#### IARS1

- **Related proteins** (co-abundance neighbors): LARS1 (0.94), EPRS1 (0.86), RARS1 (0.84), UTP20 (0.82), ACLY (0.82); STRING partners: CARS1 (0.905), EPRS1 (0.999), LARS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Isoleucine-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family and has been identified as a …
- **Diseases (Open Targets)**: growth retardation, intellectual developmental disorder, hypotonia, and hepatopathy (0.733); Abnormality of the skeletal system (0.332); microcephaly (0.289); Global developmental delay (0.289); Hallux valgus (0.184)
- **Europe PMC papers**: 184
- **Why important**: IARS1 is a highly connected core node and is present in every primary GO/KEGG term (10 globally significant GO/KEGG terms, q_global 0.00128–0.0162; see the table). It has strong STRING relationships with the other core synthetases and occurs in hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Its established role is isoleucyl-tRNA charging and translational fidelity, with documented links to polymyositis or dermatomyositis autoantibodies and developmental disease.
- **Conclusion**: Established: IARS1 provides direct enzymatic support for the aminoacylation interpretation. Hypothesis: its connection to ACLY and UTP20 may indicate coupling between translation, biosynthetic metabolism, and ribosome-production state, but this cannot be inferred as a direct mechanism from co-abundance alone.

#### LARS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.94), EPRS1 (0.85), ACLY (0.83), RARS1 (0.82); STRING partners: CARS1 (0.95), EPRS1 (0.999), IARS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: leucyl-tRNA synthetase 1. This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals w…
- **Diseases (Open Targets)**: infantile liver failure syndrome 1 (0.670); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.510); Global developmental delay (0.119); sensorineural hearing loss disorder (0.119); Generalized-onset seizure (0.118)
- **Europe PMC papers**: 267
- **Why important**: LARS1 is a core synthetase with strong relationships to EPRS1, IARS1, and RARS1, belongs to both relevant hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), and participates in every primary GO/KEGG term (10 globally significant GO/KEGG terms, q_global 0.00128–0.0162; see the table). Its established function is cytosolic leucyl-tRNA charging, and the fact sheet also records amino-acid response annotations, a recognized multisynthetase-complex association, and disease links involving infantile liver failure and developmental phenotypes.
- **Conclusion**: Established: LARS1 is a central enzymatic and complex-associated component of the module. Hypothesis: because leucine is a nutrient signal and LARS1 has amino-acid response annotations, its abundance may help couple amino-acid availability to the translational state represented by the module.

#### RARS1

- **Related proteins** (co-abundance neighbors): EPRS1 (0.85), IARS1 (0.84), LARS1 (0.82); STRING partners: CARS1 (0.805), EPRS1 (0.999), IARS1 (0.999), LARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 is part of the densely connected synthetase core, appears in every primary GO/KEGG term (10 globally significant GO/KEGG terms, q_global 0.00128–0.0162; see the table), and is included in both hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Its established function is arginyl-tRNA aminoacylation. The fact sheet also documents associations with hypomyelinating leukodystrophy and other hereditary disease phenotypes, providing substantial biological relevance beyond network connectivity.
- **Conclusion**: Established: RARS1 reinforces that the module represents coordinated cytosolic tRNA charging rather than a single isolated synthetase. Hypothesis: its co-abundance with the other synthetases may reflect concerted control of translational fidelity or demand.

#### ACLY

- **Related proteins** (co-abundance neighbors): FLII (0.84), LARS1 (0.83), IARS1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP citrate lyase. ATP citrate lyase is the primary enzyme responsible for the synthesis of cytosolic acetyl-CoA in many tissues. The enzyme is a tetramer (relative molecular weight approximately 440,000) of apparently identical subunits. It catalyzes the formation of acetyl-CoA and oxaloacetate from citrate and CoA with a concomitant hydrolysis of ATP to ADP and phosphate. The product, acetyl-CoA, serves several im…
- **Diseases (Open Targets)**: familial hypercholesterolemia (0.532); Hypercholesterolemia (0.532); atherosclerosis (0.470); inherited lipid metabolism disorder (0.467); cardiovascular disorder (0.449)
- **Europe PMC papers**: 7957
- **Why important**: ACLY is important because it is a peripheral bridge in the module, connecting to IARS1 and LARS1, while representing a distinct established function: cytosolic acetyl-CoA production from citrate. Its annotations include fatty-acid, cholesterol, and acetyl-CoA biosynthesis, and it has a very large literature and disease-association record. It is not present in the primary GO/KEGG enrichment terms and has no listed STRING or hu.MAP support in this module.
- **Conclusion**: Established: ACLY supplies a plausible metabolic context for the translation-centered core and is expressed in prostate according to the supplied HPA evidence. Hypothesis: the ACLY connection may represent coordination between anabolic carbon flux and protein-synthesis capacity, but it may also be an indirect co-abundance relationship and requires experimental validation.

## Module 2

**Tissue pair**: cell line and prostate  
**Genes (14)**: ACOT9, COG1, HEATR1, NUP85, PDS5B, PRKDC, POLR2B, SEC23A, SEC23B, SUPV3L1, DARS2, VARS1, YARS2, UGGT1

### Function

The strongest functional interpretation is a conserved cellular maintenance module with a mitochondrial RNA-processing and translation component, supported by the globally corrected term (GO:BP mitochondrial RNA metabolic process; q_global = 0.0291), which includes DARS2, SUPV3L1, POLR2B and YARS2. DARS2 and YARS2 are mitochondrial aminoacyl-tRNA synthetases, while SUPV3L1 is a mitochondrial RNA helicase involved in RNA decay and processing. POLR2B connects this signal to core transcription. The network also contains a vesicle-trafficking arm represented by SEC23A and SEC23B, an ER protein-quality-control component represented by UGGT1, Golgi organization represented by COG1, nuclear transport represented by NUP85, chromosome-cohesion and repair represented by PDS5B and PRKDC, and ribosomal RNA biogenesis represented by HEATR1. Thus, the module is biologically heterogeneous but coherent as a shared expression program for housekeeping, genome maintenance, RNA metabolism, protein processing and intracellular trafficking. No additional GO or KEGG term passed global correction. The absence of further enrichment does not invalidate the module.

**Cell composition.** HPA indicates low tissue specificity for all module genes and no recurring enriched tissue pattern. The module is not dominated by plasma or secreted proteins: the HPA summary reports only a single secreted gene, and UGGT1 is annotated as intracellular and membrane associated. Blood-cell specificity is generally low, with no enriched blood-cell pattern, so the module does not strongly resemble a plasma-protein or blood-cell contamination signature. Some genes show cell-type-enhanced signals involving neutrophils, erythrocyte progenitors, cardiomyocytes, epicardial cells, oocytes or spermatids, but these signals are mixed rather than forming a coherent dominant cell-type identity. The broad tissue distribution and functions of the genes are therefore more consistent with a conserved cellular machinery program than with a tissue-specific secretory module. Protein detection in prostate is widespread among the annotated genes, whereas the cell-line comparison has no matching HPA protein data, so protein-level concordance cannot be assessed from HPA.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP mitochondrial RNA metabolic process | 0.0291 | DARS2, POLR2B, SUPV3L1, YARS2 |

### STRING and hu.MAP

STRING provides direct high-confidence support for a mitochondrial aminoacyl-tRNA synthetase cluster through DARS2 with VARS1 and YARS2, and for the SEC23A-SEC23B COPII pair. STRING also links POLR2B with VARS1. These relationships show that parts of the co-abundance module coincide with established molecular associations, although co-abundance edges should not be interpreted as direct physical binding. There is no STRING functional enrichment result. hu.MAP repeatedly identifies SEC23A and SEC23B together in COPII, ER-to-Golgi and trafficking-related complexes (hu.MAP huMAP3_00065.1) through (hu.MAP huMAP3_13535.1) and (hu.MAP huMAP3_12394.1), providing strong complex-level support for the vesicle-trafficking arm. SUPV3L1 and YARS2 co-occur in mitochondrial RNA or mitochondrial ribosome-associated complexes (hu.MAP huMAP3_09113.1) and (hu.MAP huMAP3_06589.1), supporting a mitochondrial RNA and translation-related arm. The hu.MAP association of PRKDC with HEATR1 (hu.MAP huMAP3_09592.1) and the broad complex containing NUP85 and PDS5B (hu.MAP huMAP3_11232.1) is less specific because the module contributes only a small subset of those large complexes. Overall, the external interaction resources validate selected substructures rather than a single complete physical complex.

**STRING interactions (score >= 0.7)**: 5 of 91 gene pairs: DARS2–VARS1 (0.953); DARS2–YARS2 (0.881); POLR2B–VARS1 (0.843); SEC23A–SEC23B (0.949); VARS1–YARS2 (0.878)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00065.1 (SEC23A, SEC23B; 2/4); huMAP3_00707.1 (SEC23A, SEC23B; 2/4); huMAP3_07775.1 (SEC23A, SEC23B; 2/5); huMAP3_06453.1 (SEC23A, SEC23B; 2/6); huMAP3_09282.1 (SEC23A, SEC23B; 2/6); huMAP3_11128.1 (SEC23A, SEC23B; 2/8); huMAP3_11237.1 (SEC23A, SEC23B; 2/12); huMAP3_13535.1 (SEC23A, SEC23B; 2/14); huMAP3_09113.1 (SUPV3L1, YARS2; 2/72); huMAP3_11232.1 (NUP85, PDS5B; 2/78); huMAP3_06589.1 (SUPV3L1, YARS2; 2/79); huMAP3_09592.1 (PRKDC, HEATR1; 2/95); huMAP3_12394.1 (SEC23A, SEC23B; 2/98)

### Novelty

The module should not be presented as a newly discovered molecular complex or as a wholly novel pathway. Its strongest components are established: mitochondrial RNA metabolism, aminoacyl-tRNA synthesis, COPII trafficking, DNA repair, cohesin-associated chromosome control and nuclear transport are well-characterized processes. Several relationships are already represented in STRING, especially the DARS2-VARS1-YARS2 relationships and SEC23A-SEC23B, while hu.MAP repeatedly supports the SEC23A-SEC23B complex. The potentially novel result is the conserved co-abundance organization of these components across cell line and prostate, particularly the way the PRKDC-centered network connects otherwise distinct functional neighborhoods. However, this is a systems-level observation rather than proof of a new biochemical interaction. The absence of some module pairs from STRING or hu.MAP cannot establish novelty, because those resources are incomplete and the co-abundance relationship may reflect shared regulation, cell state or coordinated abundance.

**Hypothesis.** Hypothesis: this module represents a conserved cellular stress and biosynthetic maintenance program that coordinates mitochondrial RNA handling and translation with nuclear genome surveillance, ER-to-Golgi cargo trafficking and protein quality control. PRKDC may act as a network-level marker of the shared proliferative or genome-maintenance state, while the DARS2-SUPV3L1-YARS2 group reflects mitochondrial RNA and translation demand, and the SEC23A-SEC23B group reflects secretory-pathway and membrane-trafficking demand. The observed co-abundance could arise from common transcriptional or post-transcriptional regulation rather than direct interaction between all module members. This hypothesis requires experimental testing through perturbation of the mitochondrial RNA-processing or COPII components, followed by measurement of DNA-repair activity, mitochondrial translation and ER-to-Golgi trafficking.

### Important genes

#### PRKDC

- **Related proteins** (co-abundance neighbors): YARS2 (0.88), DARS2 (0.87), PDS5B (0.85), NUP85 (0.82), SUPV3L1 (0.82), HEATR1 (0.82), SEC23A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: protein kinase, DNA-activated, catalytic subunit. This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to DNA-PKcs deficiency (0.752); neurodegenerative disease (0.548); severe combined immunodeficiency (0.470); combined immunodeficiency (0.464); ovarian neoplasm (0.210)
- **Europe PMC papers**: 12461
- **Why important**: PRKDC is the strongest network hub in the module and connects mitochondrial RNA-related genes, nuclear transport, chromosome organization, HEATR1 and SEC23A. Its established function is the catalytic subunit of DNA-dependent protein kinase, with roles in DNA double-strand-break repair, recombination and innate immune activation. It has extensive literature support and strong disease associations involving DNA-PKcs deficiency and immunodeficiency.
- **Conclusion**: Established evidence supports PRKDC as a central genome-maintenance and repair gene with unusually high network connectivity here. The hypothesis that it coordinates the other functional neighborhoods is not established; its hub status may instead reflect shared cellular state or abundance regulation.

#### DARS2

- **Related proteins** (co-abundance neighbors): PRKDC (0.87), UGGT1 (0.81), NUP85 (0.81); STRING partners: VARS1 (0.953), YARS2 (0.881)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 2, mitochondrial. The protein encoded by this gene belongs to the class-II aminoacyl-tRNA synthetase family. It is a mitochondrial enzyme that specifically aminoacylates aspartyl-tRNA. Mutations in this gene are associated with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation (LBSL). [provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: leukoencephalopathy with brain stem and spinal cord involvement-high lactate syndrome (0.843); neurodegenerative disease (0.527); hereditary disease (0.518); hypertensive disorder (0.425); Cerebral cortical atrophy (0.425)
- **Europe PMC papers**: 796
- **Why important**: DARS2 is a bridge between the central PRKDC neighborhood and the mitochondrial RNA-related cluster, and it has high-confidence STRING relationships with VARS1 and YARS2. It is a mitochondrial aspartyl-tRNA synthetase and is directly included in the globally significant mitochondrial RNA metabolic process term (GO:BP mitochondrial RNA metabolic process; q_global = 0.0291). Its disease association with leukoencephalopathy and lactate elevation provides strong functional relevance, with a substantial body of literature.
- **Conclusion**: Established evidence supports DARS2 as a key marker of mitochondrial gene-expression and translation capacity in the module. A direct role for DARS2 in coordinating nuclear repair or vesicle trafficking is only a hypothesis based on co-abundance and network placement.

#### YARS2

- **Related proteins** (co-abundance neighbors): PRKDC (0.88); STRING partners: DARS2 (0.881), VARS1 (0.878)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_09113.1, huMAP3_06589.1
- **Function (MyGene.info)**: tyrosyl-tRNA synthetase 2. This gene encodes a mitochondrial protein that catalyzes the attachment of tyrosine to tRNA(Tyr). Mutations in this gene are associated with myopathy with lactic acidosis and sideroblastic anemia type 2 (MLASA2). [provided by RefSeq, Jan 2011].
- **Diseases (Open Targets)**: myopathy, lactic acidosis, and sideroblastic anemia (0.794); mitochondrial disease (0.509); neurodegenerative disease (0.478); hereditary disease (0.452); pericarditis (0.214)
- **Europe PMC papers**: 430
- **Why important**: YARS2 is included in (GO:BP mitochondrial RNA metabolic process; q_global = 0.0291), participates in the mitochondrial aminoacyl-tRNA synthetase STRING cluster with DARS2 and VARS1, and appears with SUPV3L1 in hu.MAP mitochondrial complexes (hu.MAP huMAP3_09113.1) and (hu.MAP huMAP3_06589.1). It encodes mitochondrial tyrosyl-tRNA synthetase and is associated with myopathy, lactic acidosis and sideroblastic anemia. Its literature volume is meaningful and its disease annotation directly supports the importance of mitochondrial translation.
- **Conclusion**: Established evidence supports YARS2 as a functional anchor of the mitochondrial RNA and translation component. The broader interpretation that its coordinated abundance links mitochondrial translation to prostate cellular state remains a hypothesis.

#### SEC23A

- **Related proteins** (co-abundance neighbors): VARS1 (0.82), PRKDC (0.80); STRING partners: SEC23B (0.949)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_00065.1, huMAP3_00707.1, huMAP3_07775.1, huMAP3_06453.1, huMAP3_09282.1, huMAP3_11128.1, huMAP3_11237.1, huMAP3_13535.1, huMAP3_12394.1
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A is the representative of a strongly supported trafficking substructure: it is paired with SEC23B in STRING and recurs across multiple hu.MAP COPII and ER-trafficking complexes (hu.MAP huMAP3_00065.1) through (hu.MAP huMAP3_13535.1) and (hu.MAP huMAP3_12394.1). Its established function is COPII-coated vesicle budding, cargo loading and ER-to-Golgi transport. It has substantial literature support and disease associations including craniolenticulosutural dysplasia.
- **Conclusion**: Established evidence supports SEC23A as the principal marker of the module's ER export and vesicle-trafficking arm. The hypothesis that this trafficking arm is mechanistically coupled to the mitochondrial and DNA-repair components is not demonstrated by the available interaction evidence.

#### SUPV3L1

- **Related proteins** (co-abundance neighbors): PRKDC (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_09113.1, huMAP3_06589.1
- **Function (MyGene.info)**: Suv3 like RNA helicase. Enables helicase activity; nucleic acid binding activity; and protein homodimerization activity. Involved in several processes, including mitochondrial RNA metabolic process; mitochondrion morphogenesis; and positive regulation of mitochondrial RNA catabolic process. Located in mitochondrial nucleoid and nucleus. Part of mitochondrial degradosome. [provided by Alliance of Genome Resources, Apr 202…
- **Diseases (Open Targets)**: neurodegenerative disease (0.541); response to vaccine (0.276); neoplasm (0.041); gestational diabetes (0.036); seasonal allergic rhinitis (0.025)
- **Europe PMC papers**: 275
- **Why important**: SUPV3L1 is one of the genes contributing to (GO:BP mitochondrial RNA metabolic process; q_global = 0.0291) and forms a hu.MAP association with YARS2 in mitochondrial RNA and ribosome-related complexes (hu.MAP huMAP3_09113.1) and (hu.MAP huMAP3_06589.1). It encodes a mitochondrial RNA helicase involved in mitochondrial RNA catabolism, RNA processing and mitochondrial nucleoid functions. Its literature volume is more limited than that of PRKDC or SEC23A, which makes its recurrence in the globally significant module especially informative.
- **Conclusion**: Established evidence supports SUPV3L1 as a mechanistically relevant mitochondrial RNA-processing component rather than a generic network passenger. Its possible role as a mediator between mitochondrial RNA quality control and the wider module is a hypothesis requiring direct perturbation and biochemical validation.

## Module 3

**Tissue pair**: cell line and prostate  
**Genes (9)**: ATP13A1, DHX36, EIF4G1, LRBA, NUP160, NUP93, QARS1, TBL2, SNRNP200

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent. The gene identities and network structure instead point to a broadly expressed intracellular gene-expression and protein-homeostasis module. SNRNP200 supports spliceosomal RNA processing; NUP93 and NUP160 support nucleocytoplasmic transport and nuclear-pore organization; EIF4G1 and QARS1 support translation; DHX36 supports RNA and nucleic-acid metabolism; ATP13A1 supports membrane-protein quality control and ion transport; LRBA is associated with vesicle-related intracellular organization; and TBL2 has annotations involving unfolded-protein, glucose-starvation, and hypoxia responses. These annotations are functionally diverse, so the module should not be assigned a single established pathway. Its strongest interpretation is coordinated cellular maintenance involving RNA processing, nuclear-cytoplasmic exchange, translation, and proteostasis.

**Cell composition.** The module is not plasma-derived, secreted, or blood-cell enriched according to HPA: all genes have low immune-cell specificity and none is secreted. Most genes have low tissue specificity, which is compatible with broadly expressed housekeeping-type biology. Several genes show cell-type enhancement, especially in spermatids, while TBL2 is tissue enhanced in testis. The prostate protein evidence is mixed, with detection for several genes and lack of detection or missing data for others. The shared signal therefore appears more consistent with conserved intracellular biology or shared cellular composition than with a blood or secreted-protein artifact. The spermatid-related HPA pattern is notable but does not establish that spermatids caused the module in the sampled tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship within the module is between NUP160 and NUP93. This is consistent with their shared role in the nuclear pore complex and provides direct external support for a nuclear-transport component. The remaining co-abundance relationships are not represented by high-confidence STRING links in the supplied results. No hu.MAP complex contains multiple module members. Thus, the co-abundance network is not a direct reconstruction of a known physical complex. It may combine direct nuclear-pore biology with correlated regulation of RNA processing, translation, membrane quality control, and stress responses.

**STRING interactions (score >= 0.7)**: 1 of 36 gene pairs: NUP160–NUP93 (0.991)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is a potentially interesting co-abundance association, but it cannot be called a newly discovered molecular complex or a novel pathway. The absence of broad STRING and hu.MAP support means that most of the observed relationships are not already established as physical interactions in those resources, yet database absence alone does not prove novelty. The strongest established part is the NUP160-NUP93 relationship. A defensible novelty claim is therefore limited to the particular cross-tissue co-abundance pattern and its possible coordination of otherwise distinct cellular processes. Independent replication, preservation in additional cohorts, and experimental testing of the noncanonical edges would be required.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular-maintenance state in which spliceosome activity, nuclear-pore transport, translation initiation, aminoacylation, RNA helicase activity, membrane-protein quality control, vesicle organization, and stress adaptation rise and fall together. SNRNP200 may provide a central co-abundance hub linking RNA processing to several of these processes, while the NUP160-NUP93 pair represents a structurally grounded nuclear-transport submodule. The spermatid-associated HPA pattern could indicate contribution from a specialized transcriptional or translational state, but this remains a hypothesis rather than an established explanation. The network does not demonstrate that these proteins physically assemble into one complex.

### Important genes

#### SNRNP200

- **Related proteins** (co-abundance neighbors): EIF4G1 (0.81), NUP160 (0.81), DHX36 (0.81), NUP93 (0.81), ATP13A1 (0.80), LRBA (0.80), TBL2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 has the strongest network position, connecting to most other module members. It is a core U5 small nuclear ribonucleoprotein component and a DEXH-box RNA helicase involved in spliceosomal assembly and conformational change. Its broad tissue pattern supports a general cellular role, while its extensive literature and established retinal-disease associations make it a biologically well-characterized anchor for the module.
- **Conclusion**: Established evidence supports SNRNP200 as a central spliceosome component and the principal network hub. It is reasonable to hypothesize that its abundance tracks a broader RNA-processing state, but the supplied data do not establish that SNRNP200 mechanistically drives the other module genes.

#### NUP93

- **Related proteins** (co-abundance neighbors): EIF4G1 (0.83), SNRNP200 (0.81), ATP13A1 (0.80); STRING partners: NUP160 (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 occupies an internally connected position and forms the module's strongest STRING-supported relationship with NUP160. It is a nucleoporin involved in the nuclear pore complex, nucleocytoplasmic transport, nuclear-envelope organization, messenger-RNA export, and nuclear import. Its disease associations include nephrotic syndromes and infectious-disease annotations, giving it substantial biological and clinical relevance.
- **Conclusion**: Established evidence supports NUP93 as a nuclear-pore and transport protein and supports its relationship with NUP160. Its co-abundance with spliceosomal, translational, and quality-control genes may indicate coordinated gene-expression infrastructure, but that broader linkage remains inferential.

#### NUP160

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.81); STRING partners: NUP93 (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 160. NUP160 is 1 of up to 60 proteins that make up the 120-MD nuclear pore complex, which mediates nucleoplasmic transport.[supplied by OMIM, Apr 2004]
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.527); neurodegenerative disease (0.469); Alzheimer disease (0.429)
- **Europe PMC papers**: 812
- **Why important**: NUP160 is the partner of NUP93 in the only high-confidence STRING interaction detected within the module. It is a component of the nuclear pore complex with roles in messenger-RNA export and nuclear import and export. Its network degree is limited, but its direct external interaction and clear molecular function make it important for identifying the nuclear-transport component of the module.
- **Conclusion**: Established evidence supports NUP160 as a nuclear-pore constituent and supports its partnership with NUP93. The module-level interpretation that this pair marks coordinated nuclear transport is plausible, whereas any proposed connection to SNRNP200 or the other genes is a hypothesis based on co-abundance.

#### EIF4G1

- **Related proteins** (co-abundance neighbors): NUP93 (0.83), QARS1 (0.82), SNRNP200 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 connects translation-related biology with the network through links to NUP93, QARS1, and SNRNP200. It is a scaffold of the EIF4F complex and supports cap-dependent recruitment of messenger RNA to ribosomes and translational initiation. It has substantial literature and disease annotations involving neurodegenerative and other disorders, making it a strong representative of the module's translational component.
- **Conclusion**: Established evidence supports EIF4G1 as a translation-initiation scaffold. Its association with nuclear-pore and spliceosomal genes may reflect coordinated demand for RNA handling and protein synthesis, but the fact sheet does not show a direct physical complex connecting all of these proteins.

#### DHX36

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAH-box helicase 36. This gene is a member of the DEAH-box family of RNA-dependent NTPases which are named after the conserved amino acid sequence Asp-Glu-Ala-His in motif II. The protein encoded by this gene has been shown to enhance the deadenylation and decay of mRNAs with 3'-UTR AU-rich elements (ARE-mRNA). The protein has also been shown to resolve into single strands the highly stable tetramolecular DNA configur…
- **Diseases (Open Targets)**: neurodegenerative disease (0.522); Abnormality of the skeletal system (0.517); Epiretinal membrane (0.388); degeneration of macula and posterior pole (0.383); retinal disorder (0.372)
- **Europe PMC papers**: 1293
- **Why important**: DHX36 is linked to the central SNRNP200 hub and contributes RNA-helicase and nucleic-acid metabolism functions. It can promote decay of messenger RNAs containing AU-rich elements and resolve stable guanine-rich DNA structures; its annotations also include spermatogenesis and regulation of translation. Its cell-type pattern includes early and late spermatids, matching a notable HPA feature of the module, and it has substantial literature and disease associations.
- **Conclusion**: Established evidence supports DHX36 as an RNA-dependent NTPase with roles in RNA regulation and nucleic-acid structure resolution. Its spermatid-associated expression and connection to SNRNP200 support a possible RNA-processing interpretation, but they do not prove that the module is spermatid-specific or that DHX36 controls the network.

## Module 4

**Tissue pair**: cell line and prostate  
**Genes (6)**: CHD4, DDX21, DHX9, RSL1D1, POLR2A, RRP12

### Function

The module is most consistent with a coordinated nuclear gene-expression and RNA-maturation program. Its genes include RNA helicases, a chromatin-remodeling ATPase, a ribosome-biogenesis factor, a nucleolar regulatory protein, and the largest subunit of RNA polymerase II. The strongest internal structure links DHX9 with DDX21, RSL1D1, and RRP12; connects RRP12 with RSL1D1; and links CHD4 with POLR2A. These relationships support a functional axis spanning RNA processing, preribosome maturation, chromatin regulation, and transcription. However, no GO or KEGG term passed global correction, so this interpretation is based on gene functions, network structure, and supplementary STRING evidence rather than statistically significant GO or KEGG enrichment. STRING supports helicase-related biology (STRING SMART DEAD-like helicases superfamily; within-query FDR = 0.0034), (STRING SMART Helicase superfamily c-terminal domain; within-query FDR = 0.0034), (STRING Keyword Helicase; within-query FDR = 0.0149), (STRING InterPro Helicase, C-terminal; within-query FDR = 0.0221), (STRING InterPro Helicase superfamily 1/2, ATP-binding domain; within-query FDR = 0.0221), transcription (STRING Keyword Transcription; within-query FDR = 0.049), nuclear localization (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0105), and preribosome or ribosome-biogenesis associations (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 0.0325), (STRING NetworkNeighborAL Mixed, incl. Preribosome, large subunit precursor, and Maturation of LSU-rRNA; within-query FDR = 0.0406).

**Cell composition.** The module is composed entirely of intracellular or nuclear proteins, with no secreted genes. Most members have low tissue specificity and low immune-cell specificity, arguing against a module that is primarily a plasma-protein or blood-cell signature. RRP12 is enriched in bone marrow and skeletal muscle and is enhanced in neutrophil-related populations, while POLR2A is tissue enhanced in lymphoid tissue. Several genes show cell-type enhancement in neural or epithelial populations, and DDX21 shows enhancement in keratinocytes. The prostate protein data detect DHX9, CHD4, DDX21, and RSL1D1, whereas RRP12 and POLR2A lack protein detection there. Overall, the shared signal is more plausibly a conserved intracellular program or shared cell-state component than contamination by secreted proteins, although cell composition and proliferative or transcriptional state could contribute.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING contains established high-confidence relationships for DDX21 with DHX9 and RSL1D1, DHX9 with POLR2A, and RRP12 with RSL1D1. The supplementary STRING annotations also connect DDX21, DHX9, and CHD4 to helicase-related domains (STRING SMART DEAD-like helicases superfamily; within-query FDR = 0.0034), (STRING SMART Helicase superfamily c-terminal domain; within-query FDR = 0.0034), (STRING Keyword Helicase; within-query FDR = 0.0149), (STRING InterPro Helicase, C-terminal; within-query FDR = 0.0221), (STRING InterPro Helicase superfamily 1/2, ATP-binding domain; within-query FDR = 0.0221), connect RRP12 and RSL1D1 to preribosome and large-subunit maturation biology (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 0.0325), (STRING NetworkNeighborAL Mixed, incl. Preribosome, large subunit precursor, and Maturation of LSU-rRNA; within-query FDR = 0.0406), and place the full module in nuclear or chromosomal contexts (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0105), (STRING Component Chromosome; within-query FDR = 0.0167). These known links support biological coherence but do not establish that every co-abundance edge is a direct physical interaction. No hu.MAP complex contains at least two module members, so there is no independent hu.MAP support for a shared stable complex. The module therefore appears to combine related nuclear processes and interaction neighborhoods rather than represent one demonstrated multiprotein complex.

**STRING interactions (score >= 0.7)**: 4 of 15 gene pairs: DDX21–DHX9 (0.908); DDX21–RSL1D1 (0.81); DHX9–POLR2A (0.781); RRP12–RSL1D1 (0.97)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART DEAD-like helicases superfamily (FDR = 0.0034, 3 genes); SMART Helicase superfamily c-terminal domain (FDR = 0.0034, 3 genes); Keyword Ubl conjugation (FDR = 0.0086, 6 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0105, 6 genes); Keyword Helicase (FDR = 0.0149, 3 genes); Component Chromosome (FDR = 0.0167, 5 genes); InterPro Helicase, C-terminal (FDR = 0.0221, 3 genes); InterPro Helicase superfamily 1/2, ATP-binding domain (FDR = 0.0221, 3 genes); PMID (2017) SIRT7-dependent deacetylation of CDK9 activates RNA polymerase II transcription. (FDR = 0.0232, 4 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 0.0325, 3 genes); Keyword Isopeptide bond (FDR = 0.036, 5 genes); NetworkNeighborAL Mixed, incl. Preribosome, large subunit precursor, and Maturation of LSU-rRNA (FDR = 0.0406, 2 genes); Keyword Transcription (FDR = 0.049, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be called a wholly new molecular pathway. Its component functions and several relationships are already established through STRING, and the genes have substantial prior literature, especially DHX9, CHD4, DDX21, and POLR2A. Nevertheless, the conserved co-abundance association between cell line and prostate may be a new systems-level observation, particularly because no hu.MAP complex jointly captures the module and no GO or KEGG term passes global correction. The appropriate claim is therefore a potentially novel cross-tissue co-abundance configuration built from largely known nuclear biology, not discovery of previously unknown gene functions or interactions. Absence from hu.MAP or from particular STRING links is insufficient by itself to establish novelty.

**Hypothesis.** Hypothesis: the module reflects a coordinated nuclear state in which RNA helicases and nucleolar factors support RNA processing and ribosome maturation while chromatin remodeling and RNA polymerase II activity regulate transcriptional output. DHX9 and DDX21 may form a helicase-centered RNA-processing interface, RRP12 and RSL1D1 may represent a nucleolar or preribosome-related branch, and CHD4 with POLR2A may connect chromatin state to transcription. The shared abundance pattern in cell line and prostate could therefore arise when cells maintain high demand for transcription, RNA maturation, and growth-associated nuclear organization. This is a mechanistic hypothesis, not a demonstrated causal pathway; the co-abundance data do not prove direct binding, directionality, or coordinated regulation.

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): DDX21 (0.86), RSL1D1 (0.85), RRP12 (0.83); STRING partners: DDX21 (0.908), POLR2A (0.781)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 has the strongest network position, connecting DDX21, RSL1D1, and RRP12, and it is the only module member that bridges the helicase-centered and nucleolar branches. Established annotations describe ATP-dependent unwinding of RNA and DNA-RNA complexes, nuclear and cytoplasmic localization, transcriptional regulation, alternative splicing, and regulation of RNA polymerase II transcription. It has extensive literature and disease associations including intellectual developmental disorder and neurodegenerative disease. STRING supports its links with DDX21 and POLR2A and repeatedly places it in helicase, transcription, nuclear, and chromatin-related supplementary categories (STRING SMART DEAD-like helicases superfamily; within-query FDR = 0.0034), (STRING SMART Helicase superfamily c-terminal domain; within-query FDR = 0.0034), (STRING Keyword Ubl conjugation; within-query FDR = 0.0086), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0105), (STRING Keyword Helicase; within-query FDR = 0.0149), (STRING Component Chromosome; within-query FDR = 0.0167), (STRING InterPro Helicase, C-terminal; within-query FDR = 0.0221), (STRING InterPro Helicase superfamily 1/2, ATP-binding domain; within-query FDR = 0.0221), (STRING PMID (2017) SIRT7-dependent deacetylation of CDK9 activates RNA polymerase II transcription.; within-query FDR = 0.0232), (STRING Keyword Isopeptide bond; within-query FDR = 0.036), (STRING Keyword Transcription; within-query FDR = 0.049).
- **Conclusion**: Established evidence supports DHX9 as the principal integrative RNA-processing and transcriptional hub of the module. It is reasonable to hypothesize that DHX9 helps couple RNA metabolism to transcription in this co-abundance program, but the module does not establish that DHX9 drives the association or directly binds every connected member.

#### DDX21

- **Related proteins** (co-abundance neighbors): DHX9 (0.86); STRING partners: DHX9 (0.908), RSL1D1 (0.81)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 is a nucleolar and mitotic-chromosome protein with a direct high-confidence STRING relationship to DHX9 and an additional relationship to RSL1D1. Its established functions include RNA structural remodeling, ribosome and spliceosome assembly, transcriptional regulation, chromatin remodeling, and regulation of RNA polymerase I and II-associated processes. It has substantial literature and disease associations involving neurodegenerative and malignant conditions. The supplementary STRING evidence repeatedly identifies DDX21 in helicase, transcription, nuclear, chromosomal, and preribosome-related contexts (STRING SMART DEAD-like helicases superfamily; within-query FDR = 0.0034), (STRING SMART Helicase superfamily c-terminal domain; within-query FDR = 0.0034), (STRING Keyword Ubl conjugation; within-query FDR = 0.0086), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0105), (STRING Keyword Helicase; within-query FDR = 0.0149), (STRING Component Chromosome; within-query FDR = 0.0167), (STRING InterPro Helicase, C-terminal; within-query FDR = 0.0221), (STRING InterPro Helicase superfamily 1/2, ATP-binding domain; within-query FDR = 0.0221), (STRING PMID (2017) SIRT7-dependent deacetylation of CDK9 activates RNA polymerase II transcription.; within-query FDR = 0.0232), (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 0.0325), (STRING Keyword Isopeptide bond; within-query FDR = 0.036), (STRING Keyword Transcription; within-query FDR = 0.049).
- **Conclusion**: Established evidence supports DDX21 as a nucleolar RNA-processing and transcriptional regulator that provides a biological rationale for the module. Its position is peripheral in the measured subgraph, so a role as a central organizer remains a hypothesis rather than a conclusion from this network alone.

#### RRP12

- **Related proteins** (co-abundance neighbors): DHX9 (0.83), CHD4 (0.81); STRING partners: RSL1D1 (0.97)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal RNA processing 12 homolog. Enables RNA binding activity. Predicted to be involved in rRNA processing. Located in cytosol; nucleolus; and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.435); bilateral striopallidodentate calcinosis (0.370); colorectal carcinoma (0.079); hepatocellular carcinoma (0.075); neoplasm (0.067)
- **Europe PMC papers**: 367
- **Why important**: RRP12 links DHX9 with CHD4 in the module and has a high-confidence STRING relationship with RSL1D1. It is annotated as an RNA-binding ribosome-biogenesis factor involved in rRNA processing and is located in the nucleolus among other reported cellular locations. Its HPA profile is distinctive within the module, with enrichment in bone marrow and skeletal muscle and enhancement in monocyte and neutrophil-related populations. STRING supplementary evidence specifically supports preribosome, ribosome-biogenesis, large-subunit precursor, and maturation biology (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 0.0325), (STRING NetworkNeighborAL Mixed, incl. Preribosome, large subunit precursor, and Maturation of LSU-rRNA; within-query FDR = 0.0406).
- **Conclusion**: Established evidence supports RRP12 as the clearest indicator of a ribosome-biogenesis or rRNA-processing component. Its blood and bone-marrow associations raise the possibility that sample cell composition contributes to its co-abundance, but the lack of broad immune specificity and the nuclear composition of the module argue against reducing the entire module to a blood signature.

#### CHD4

- **Related proteins** (co-abundance neighbors): POLR2A (0.82), RRP12 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromodomain helicase DNA binding protein 4. The product of this gene belongs to the SNF2/RAD54 helicase family. It represents the main component of the nucleosome remodeling and deacetylase complex and plays an important role in epigenetic transcriptional repression. Patients with dermatomyositis develop antibodies against this protein. Somatic mutations in this gene are associated with serous endometrial tumors. Alternative splicing result…
- **Diseases (Open Targets)**: Sifrim-Hitz-Weiss syndrome (0.810); neurodegenerative disease (0.551); hereditary disease (0.505); endometrial cancer (0.470); uterine carcinosarcoma (0.439)
- **Europe PMC papers**: 3617
- **Why important**: CHD4 connects POLR2A and RRP12 and is a principal component of the nucleosome remodeling and deacetylase complex. Established functions include chromatin remodeling, epigenetic transcriptional repression, homologous-recombination repair, and regulation of gene expression and cell fate. It has extensive literature and disease associations including Sifrim-Hitz-Weiss syndrome, neurodegenerative disease, endometrial cancer, and uterine carcinosarcoma. STRING places CHD4 with DHX9 and DDX21 in helicase-related supplementary categories and with POLR2A in a transcription-associated context (STRING SMART DEAD-like helicases superfamily; within-query FDR = 0.0034), (STRING SMART Helicase superfamily c-terminal domain; within-query FDR = 0.0034), (STRING Keyword Ubl conjugation; within-query FDR = 0.0086), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0105), (STRING Keyword Helicase; within-query FDR = 0.0149), (STRING Component Chromosome; within-query FDR = 0.0167), (STRING InterPro Helicase, C-terminal; within-query FDR = 0.0221), (STRING InterPro Helicase superfamily 1/2, ATP-binding domain; within-query FDR = 0.0221), (STRING PMID (2017) SIRT7-dependent deacetylation of CDK9 activates RNA polymerase II transcription.; within-query FDR = 0.0232), (STRING Keyword Isopeptide bond; within-query FDR = 0.036), (STRING Keyword Transcription; within-query FDR = 0.049).
- **Conclusion**: Established evidence supports CHD4 as the chromatin-regulatory arm of the module and provides a plausible bridge between chromatin state and RNA production. The proposed coupling to RRP12 and the broader RNA-maturation program is a hypothesis based on co-abundance and network placement, not a demonstrated CHD4-specific mechanism here.

#### POLR2A

- **Related proteins** (co-abundance neighbors): CHD4 (0.82); STRING partners: DHX9 (0.781)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase II subunit A. This gene encodes the largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene contains a carboxy terminal domain composed of heptapeptide repeats that are essential for polymerase activity. These repeats contain serine and threonine residues that are phosphorylated in actively transcribing RNA polymerase. In addition, …
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and variable intellectual and behavioral abnormalities (0.738); HIV infectious disease (0.600); hereditary disease (0.479); syndromic intellectual disability (0.462); Orthomyxoviridae infectious disease (0.374)
- **Europe PMC papers**: 4546
- **Why important**: POLR2A is the largest subunit of RNA polymerase II and contains the carboxyl-terminal repeat domain required for polymerase activity and regulated transcription. It connects to CHD4 in the module and has a high-confidence STRING relationship with DHX9. It is annotated in transcription initiation, elongation-related polymerase activity, transcription termination, and regulation of DNA-templated transcription. POLR2A also has extensive literature and disease associations involving neurodevelopmental and infectious disease contexts. STRING supplementary evidence places it in nuclear, chromosomal, transcriptional, and SIRT7-dependent RNA polymerase II-related evidence (STRING Keyword Ubl conjugation; within-query FDR = 0.0086), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0105), (STRING Component Chromosome; within-query FDR = 0.0167), (STRING PMID (2017) SIRT7-dependent deacetylation of CDK9 activates RNA polymerase II transcription.; within-query FDR = 0.0232), (STRING Keyword Transcription; within-query FDR = 0.049).
- **Conclusion**: Established evidence supports POLR2A as the core transcriptional output component of the module. Its connection to helicase and chromatin factors is biologically plausible, but the co-abundance pattern does not show whether transcriptional activity causes the module or is merely a shared consequence of cellular state.

## Module 6

**Tissue pair**: cell line and prostate  
**Genes (10)**: COPB1, DDX6, FAM91A1, NUDCD1, DIS3, SEC24A, SEC24C, TBC1D24, UBE4B, VPS45

### Function

The module most plausibly reflects intracellular membrane trafficking, especially endoplasmic-reticulum-to-Golgi transport, vesicle formation, cargo handling, and associated RNA and protein quality-control processes. The strongest mechanistic signal comes from SEC24A and SEC24C, which are COPII components, together with COPB1, a coatomer subunit involved in Golgi-associated vesicle transport. DDX6, DIS3, and UBE4B add RNA turnover, translation repression, and ubiquitin-dependent protein quality-control functions, while VPS45 and TBC1D24 are compatible with vesicle sorting and membrane trafficking. No GO or KEGG term passed global correction, so the functional interpretation is hypothesis-generating and is based on gene functions, network structure, STRING supplementary terms, and hu.MAP relationships rather than globally significant GO or KEGG enrichment. The supplementary STRING terms (STRING Keyword Cytoplasmic vesicle; within-query FDR = 0.0144) and (STRING Keyword ER-Golgi transport; within-query FDR = 0.0325) support cytoplasmic vesicle biology and ER-Golgi transport, respectively.

**Cell composition.** The module is not dominated by plasma proteins, secreted proteins, or blood-cell-enriched genes. HPA reports no secreted genes, generally low tissue specificity, generally low immune-cell specificity, and no recurrent enriched blood-cell category. Most proteins are detected in prostate, whereas the cell-line protein comparison has no informative matching HPA tissue result. The broadly expressed profile suggests that the shared signal may represent a conserved intracellular housekeeping or trafficking program rather than a prostate-specific secretory program. Cell-type-enhanced observations in spermatids, cardiomyocytes, esophageal apical cells, plasma cells, neutrophils, podocytes, and neural or renal cell types indicate that some components can vary with cellular composition, but they do not establish a blood-derived explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING directly supports a compact trafficking-centered core. COPB1 connects with SEC24A, SEC24C, and NUDCD1, and SEC24A connects very strongly with SEC24C. The supplementary STRING annotations (STRING Keyword Cytoplasmic vesicle; within-query FDR = 0.0144) and (STRING Keyword ER-Golgi transport; within-query FDR = 0.0325) involve COPB1, SEC24A, SEC24C, FAM91A1, and TBC1D24, reinforcing vesicle and ER-Golgi biology, but these are not global multiple-testing evidence. The hu.MAP results (hu.MAP huMAP3_06453.1) through (hu.MAP huMAP3_12394.1) repeatedly place SEC24A and SEC24C together in complexes containing SEC23 and other SEC24 paralogs, providing independent support for a COPII-related module core. The remaining module edges, especially those involving DDX6, UBE4B, VPS45, DIS3, FAM91A1, and TBC1D24, are not extensively represented by high-confidence STRING or hu.MAP evidence in this fact sheet. Thus, the network combines a known vesicle-trafficking backbone with less established co-abundance links to RNA metabolism, ubiquitin regulation, and trafficking adaptors.

**STRING interactions (score >= 0.7)**: 4 of 45 gene pairs: COPB1–NUDCD1 (0.71); COPB1–SEC24A (0.724); COPB1–SEC24C (0.714); SEC24A–SEC24C (0.995)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Cytoplasmic vesicle (FDR = 0.0144, 5 genes); Keyword ER-Golgi transport (FDR = 0.0325, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06453.1 (SEC24A, SEC24C; 2/6); huMAP3_09282.1 (SEC24A, SEC24C; 2/6); huMAP3_11128.1 (SEC24A, SEC24C; 2/8); huMAP3_11237.1 (SEC24A, SEC24C; 2/12); huMAP3_13535.1 (SEC24A, SEC24C; 2/14); huMAP3_12394.1 (SEC24A, SEC24C; 2/98)

### Novelty

This should not be called a wholly new molecular pathway. The SEC24A-SEC24C relationship, their shared COPII complex context, and COPB1-associated vesicle biology are established by STRING and hu.MAP. However, the particular cross-context co-abundance module may still be a new systems-level observation because it joins this trafficking core with DDX6, UBE4B, VPS45, DIS3, FAM91A1, TBC1D24, and NUDCD1 in a conserved cell-line and prostate pattern. Absence of many module pairs from STRING or hu.MAP does not prove novelty; it more cautiously indicates that the observed co-abundance organization is not fully captured by existing interaction or complex resources. Validation in independent cohorts, at the protein level, and with cell-composition controls would be needed before claiming a novel biological complex or pathway.

**Hypothesis.** Mechanistic hypothesis: a conserved intracellular trafficking state links COPII cargo selection and ER-to-Golgi export through SEC24A and SEC24C with COPB1-mediated Golgi vesicle cycling. VPS45, FAM91A1, and TBC1D24 may connect this transport state to later sorting, tethering, or Rab-regulated membrane events, while DDX6, DIS3, and UBE4B may coordinate RNA turnover and protein-quality control as cells maintain trafficking capacity. The co-abundance pattern could therefore reflect coordinated proteostasis and membrane transport rather than a single discrete complex. This remains a hypothesis: the fact sheet supports the trafficking core, but does not establish direct physical binding among all module members or causal regulation between the RNA, ubiquitin, and vesicle components.

### Important genes

#### SEC24C

- **Related proteins** (co-abundance neighbors): DDX6 (0.83), COPB1 (0.82); STRING partners: COPB1 (0.714), SEC24A (0.995)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_06453.1, huMAP3_09282.1, huMAP3_11128.1, huMAP3_11237.1, huMAP3_13535.1, huMAP3_12394.1
- **Function (MyGene.info)**: SEC24 homolog C, COPII component. The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec24p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The product of this gene may play a role in shaping the vesicle, as well as in cargo selection and concentration.…
- **Diseases (Open Targets)**: 22q11.2 deletion syndrome (0.370); neurodegenerative disease (0.369); Alzheimer disease (0.281); lysosomal storage disease (0.274); Parkinson disease (0.274)
- **Europe PMC papers**: 693
- **Why important**: SEC24C is central to the best-supported biological interpretation. It is a COPII component involved in cargo loading and ER-to-Golgi transport, has direct STRING links to COPB1 and SEC24A, and appears with SEC24A across the hu.MAP complexes (hu.MAP huMAP3_06453.1) through (hu.MAP huMAP3_12394.1). Its vesicle localization and prostate detection are consistent with the module context. Its literature volume is substantial, and its disease associations include neurodegenerative and lysosomal disorders.
- **Conclusion**: Established evidence supports SEC24C as a core ER-export and cargo-selection anchor of the module. It is a strong candidate for representing the conserved trafficking component. Whether its co-abundance with the RNA and ubiquitin regulators reflects functional coupling remains a hypothesis.

#### SEC24A

- **Related proteins** (co-abundance neighbors): COPB1 (0.83), DDX6 (0.81); STRING partners: COPB1 (0.724), SEC24C (0.995)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center, Vesicles; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_06453.1, huMAP3_09282.1, huMAP3_11128.1, huMAP3_11237.1, huMAP3_13535.1, huMAP3_12394.1
- **Function (MyGene.info)**: SEC24 homolog A, COPII component. The protein encoded by this gene belongs to a family of proteins that are homologous to yeast Sec24. This protein is a component of coat protein II (COPII)-coated vesicles that mediate protein transport from the endoplasmic reticulum. COPII acts in the cytoplasm to promote the transport of secretory, plasma membrane, and vacuolar proteins from the endoplasmic reticulum to the golgi complex. Altern…
- **Diseases (Open Targets)**: Graves disease (0.218); hyperlipoproteinemia type V (0.071); combined low LDL and fibrinogen (0.069); Hyperlipoproteinemia type 1 (0.062); apolipoprotein c-III deficiency (0.062)
- **Europe PMC papers**: 808
- **Why important**: SEC24A is one of the most informative module genes because it is a COPII cargo component with functions in ER-to-Golgi transport and vesicle cargo loading. It has a very strong STRING relationship with SEC24C, direct links to COPB1, and repeated co-membership with SEC24C in hu.MAP complexes (hu.MAP huMAP3_06453.1) through (hu.MAP huMAP3_12394.1). It is detected in prostate and has disease associations involving lipoprotein and fibrinogen biology, making it relevant to secretory and cargo-transport processes.
- **Conclusion**: Established evidence identifies SEC24A as a second core trafficking anchor and supports a SEC24A-SEC24C COPII-centered interpretation. Its association with the other module genes should be treated as coordinated regulation or co-abundance until experimentally demonstrated.

#### COPB1

- **Related proteins** (co-abundance neighbors): SEC24A (0.83), SEC24C (0.82), DIS3 (0.81); STRING partners: NUDCD1 (0.71), SEC24A (0.724), SEC24C (0.714)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus, Vesicles, Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coat protein complex I subunit beta 1. This gene encodes a protein subunit of the coatomer complex associated with non-clathrin coated vesicles. The coatomer complex, also known as the coat protein complex 1, forms in the cytoplasm and is recruited to the Golgi by activated guanosine triphosphatases. Once at the Golgi membrane, the coatomer complex may assist in the movement of protein and lipid components back to the endoplasmic retic…
- **Diseases (Open Targets)**: Baralle-Macken syndrome (0.598); Alzheimer disease (0.463); Parkinson disease (0.462); neurodegenerative disease (0.462); lysosomal storage disease (0.462)
- **Europe PMC papers**: 565
- **Why important**: COPB1 has a high network position and connects the module’s COPII-related genes with the broader coatomer and Golgi transport system. Its known role in COPI vesicles, retrograde ER-Golgi transport, and intra-Golgi transport is consistent with the STRING supplementary terms (STRING Keyword Cytoplasmic vesicle; within-query FDR = 0.0144) and (STRING Keyword ER-Golgi transport; within-query FDR = 0.0325). It directly links to SEC24A, SEC24C, and NUDCD1 in STRING, and is localized to the Golgi, vesicles, and cytosol. Its literature base is substantial and includes neurological and lysosomal disease associations.
- **Conclusion**: Established evidence supports COPB1 as a bridge between COPII-linked export and Golgi or retrograde vesicle cycling. Its connection to NUDCD1 is less established functionally and should not be interpreted as a defined complex without further evidence.

#### DDX6

- **Related proteins** (co-abundance neighbors): UBE4B (0.87), VPS45 (0.84), TBC1D24 (0.83), SEC24C (0.83), NUDCD1 (0.82), SEC24A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytoplasmic bodies; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 6. This gene encodes a member of the DEAD box protein family. The protein is an RNA helicase found in P-bodies and stress granules, and functions in translation suppression and mRNA degradation. It is required for microRNA-induced gene silencing. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: intellectual developmental disorder with impaired language and dysmorphic facies (0.650); Intellectual disability (0.555); neurodegenerative disease (0.459); lung carcinoma (0.371); Global developmental delay (0.371)
- **Europe PMC papers**: 3002
- **Why important**: DDX6 has the strongest network position in the module and connects to UBE4B, VPS45, TBC1D24, SEC24C, NUDCD1, and SEC24A. It is an RNA helicase associated with P-bodies and stress granules and functions in translation suppression, microRNA-mediated silencing, and mRNA degradation. Its literature volume is very large relative to most module members, and its disease associations include developmental and neurodegenerative disorders.
- **Conclusion**: Established evidence supports DDX6 as an RNA fate and translational-control factor that may broaden the module beyond membrane trafficking. Its central co-abundance position makes it an important integrator, but the fact sheet does not establish that DDX6 directly regulates the SEC24 or COPB1 trafficking machinery.

#### VPS45

- **Related proteins** (co-abundance neighbors): DDX6 (0.84), UBE4B (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vacuolar protein sorting 45 homolog. Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene is a member of the Sec1 domain family, and shows a high degree of sequence similarity to mouse, rat and yeast Vps45. The exact func…
- **Diseases (Open Targets)**: congenital neutropenia-myelofibrosis-nephromegaly syndrome (0.787); severe congenital neutropenia (0.549); neurodegenerative disease (0.462); COVID-19 (0.371); hereditary disease (0.192)
- **Europe PMC papers**: 811
- **Why important**: VPS45 links to DDX6 and UBE4B and is annotated for intracellular protein sorting and vesicle-mediated transport. Its association with early and late spermatids and its prostate detection fit a conserved transport-related program, while its disease associations include severe congenital neutropenia and a congenital neutropenia-myelofibrosis-nephromegaly syndrome. It also has a substantial literature base.
- **Conclusion**: Established evidence supports VPS45 as a vesicle-sorting component and provides a plausible connection between trafficking and disease-relevant cellular homeostasis. Its specific mechanistic relationship to DDX6 and UBE4B in this module is a hypothesis rather than an established complex.

## Module 7

**Tissue pair**: cell line and prostate  
**Genes (10)**: COPS3, DYNC1H1, EIF3C, KIFBP, PSMD13, RPL9, RPS27L, PSAT1, SRP72, XAB2

### Function

The module does not support a single statistically established GO or KEGG function because no term passed global correction. Its strongest interpretable signal is a mixed cellular gene-expression and proteostasis program: translation initiation and ribosomal activity are represented by EIF3C, RPS27L, and RPL9; proteasome or ubiquitin-system components are represented by PSMD13 and COPS3; cotranslational membrane targeting is represented by SRP72; and intracellular transport or cytoskeletal functions are represented by DYNC1H1 and KIFBP. The STRING supplementary terms support these interpretations through proteasome or PCI-domain associations (STRING SMART Motif in proteasome subunits, Int-6, Nip-1 and TRIP-15; within-query FDR = 0.003) (STRING InterPro Proteasome component (PCI) domain; within-query FDR = 0.0318), free forty-S subunit formation and translational processes (STRING RCTM Formation of a pool of free 40S subunits; within-query FDR = 0.0265) (STRING RCTM L13a-mediated translational silencing of Ceruloplasmin expression; within-query FDR = 0.0312) (STRING RCTM GTP hydrolysis and joining of the 60S ribosomal subunit; within-query FDR = 0.0312), SRP-dependent membrane targeting (STRING RCTM SRP-dependent cotranslational protein targeting to membrane; within-query FDR = 0.0312), and regulation of SLIT or ROBO expression (STRING RCTM Regulation of expression of SLITs and ROBOs; within-query FDR = 0.0348). These are supportive annotations rather than globally corrected enrichment. The network is therefore best interpreted as a weakly connected, mixed housekeeping and protein-handling module rather than a coherent specialized pathway.

**Cell composition.** All module genes have HPA annotations, and none are secreted proteins. Most have low tissue specificity and low immune-cell specificity, arguing against a plasma-protein or broad blood-cell contamination explanation. Many genes are nevertheless cell-type enhanced, with recurring HPA associations involving oocytes, gastric chief cells, ependymal cells, and oligodendrocyte-related populations. The tissue-enhanced genes include brain, kidney, liver, and pancreas associations, but these are distributed across different genes rather than defining one tissue program. Protein detection is reported for several genes in prostate, while cell-line protein detection has no informative matching HPA tissue result. Overall, the composition is more consistent with broadly used intracellular machinery, with possible contributions from shared cell states or cell types, than with a secreted or immune-cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports only a limited subset of the observed co-abundance relationships. The strongest known links involve RPL9 with RPS27L and SRP72, and EIF3C with RPS27L. The supplementary STRING terms connect EIF3C, RPS27L, and RPL9 to translation-related processes, and connect COPS3, EIF3C, and PSMD13 to PCI-domain or proteasome-associated functions (STRING SMART Motif in proteasome subunits, Int-6, Nip-1 and TRIP-15; within-query FDR = 0.003) through (STRING RCTM Regulation of expression of SLITs and ROBOs; within-query FDR = 0.0348). These results indicate that some members participate in known translation, SRP, and proteasome-related biology. However, most module gene pairs are not supported by high-confidence STRING links, and no hu.MAP complex contains multiple module members. Thus, the module is not a well-established physical complex; it is primarily a co-abundance association with a few known molecular relationships.

**STRING interactions (score >= 0.7)**: 3 of 45 gene pairs: EIF3C–RPS27L (0.748); RPL9–RPS27L (0.991); RPL9–SRP72 (0.878)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Motif in proteasome subunits, Int-6, Nip-1 and TRIP-15 (FDR = 0.003, 3 genes); RCTM Formation of a pool of free 40S subunits (FDR = 0.0265, 3 genes); RCTM L13a-mediated translational silencing of Ceruloplasmin expression (FDR = 0.0312, 3 genes); RCTM SRP-dependent cotranslational protein targeting to membrane (FDR = 0.0312, 3 genes); RCTM GTP hydrolysis and joining of the 60S ribosomal subunit (FDR = 0.0312, 3 genes); InterPro Proteasome component (PCI) domain (FDR = 0.0318, 3 genes); RCTM Regulation of expression of SLITs and ROBOs (FDR = 0.0348, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module cannot be declared a new biological mechanism from the available evidence. Its component functions are largely established: translation, ribosomal activity, SRP-dependent targeting, proteasome regulation, RNA processing, and microtubule-based transport are well-known processes. The absence of a matching hu.MAP complex and the limited STRING connectivity mean that the particular cross-tissue co-abundance arrangement may be data-derived and potentially interesting, but absence from these resources does not prove novelty. The most defensible conclusion is that the module may represent a previously unreported association pattern, while its individual molecular functions are not novel and its mechanistic unity remains unproven.

**Hypothesis.** Hypothesis: the conserved cell-line and prostate co-abundance pattern reflects a shared intracellular protein-production and quality-control state. In this model, EIF3C, RPS27L, and RPL9 mark coordinated translational capacity; SRP72 links translation to cotranslational membrane targeting; PSMD13 and COPS3 connect the state to proteasome and ubiquitin-system regulation; and DYNC1H1, KIFBP, and XAB2 reflect transport, cytoskeletal organization, and RNA-processing requirements. PSAT1 may indicate accompanying metabolic support through serine biosynthesis and stress adaptation. The observed module could therefore arise when cells coordinate synthesis, targeting, trafficking, and turnover of proteins, but this remains a hypothesis because global GO or KEGG enrichment is absent, physical-complex support is limited, and several edges are not corroborated by STRING or hu.MAP.

### Important genes

#### EIF3C

- **Related proteins** (co-abundance neighbors): PSAT1 (0.85), RPL9; RPL9P7; RPL9P8; RPL9P9 (0.85), PSMD13 (0.83), KIFBP (0.81); STRING partners: RPS27L (0.748)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C has the highest weighted network connectivity in the module and links the network to PSAT1, proteasome-associated members, KIFBP, and the ribosomal or translational portion of the module. Its established function is as a subunit of the eukaryotic translation-initiation factor complex, with roles in translation initiation and positive regulation of translation. It is supported by several supplementary STRING annotations involving translation and PCI-domain or proteasome-related motifs (STRING SMART Motif in proteasome subunits, Int-6, Nip-1 and TRIP-15; within-query FDR = 0.003) (STRING RCTM Formation of a pool of free 40S subunits; within-query FDR = 0.0265) (STRING RCTM L13a-mediated translational silencing of Ceruloplasmin expression; within-query FDR = 0.0312) (STRING RCTM GTP hydrolysis and joining of the 60S ribosomal subunit; within-query FDR = 0.0312) (STRING InterPro Proteasome component (PCI) domain; within-query FDR = 0.0318), has prostate protein detection, and has substantial literature coverage. Its disease and neoplasm associations further support biological importance, although they do not establish a role in this module.
- **Conclusion**: Established evidence supports EIF3C as a central translation-initiation component and a major network anchor. Its connection to proteasome-related genes is compatible with coordinated protein production and quality control. A module-specific role linking translation initiation to proteostasis is plausible, but remains a hypothesis rather than a demonstrated mechanism.

#### DYNC1H1

- **Related proteins** (co-abundance neighbors): XAB2 (0.83), COPS3 (0.82), PSMD13 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 1 heavy chain 1. Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polyp…
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy without contractures (0.816); intellectual disability, autosomal dominant 13 (0.815); Charcot-Marie-Tooth disease axonal type 2O (0.799); autosomal dominant non-syndromic intellectual disability (0.634); hereditary disease (0.545)
- **Europe PMC papers**: 1731
- **Why important**: DYNC1H1 has high network connectivity and bridges XAB2, COPS3, and PSMD13, thereby connecting transport biology with RNA-processing and protein-quality-control components. It encodes the heavy chain of cytoplasmic dynein, a molecular motor involved in intracellular transport, organelle movement, spindle dynamics, and retrograde axonal transport. It is tissue enhanced in brain and has extensive literature and strong disease associations involving motor-neuron and neurodevelopmental disorders. Its STRING partner list does not independently support the module edges, so its importance comes primarily from network position and established function.
- **Conclusion**: Established evidence supports DYNC1H1 as a major intracellular transport and cytoskeletal component. Its placement may indicate that transport requirements accompany the translational and proteostasis state, but the module does not establish a direct physical or regulatory connection between DYNC1H1 and the other members.

#### PSMD13

- **Related proteins** (co-abundance neighbors): EIF3C (0.83), DYNC1H1 (0.82), SRP72 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 is a highly connected module member linking EIF3C, DYNC1H1, and SRP72. It encodes a non-ATPase subunit of the twenty-six S proteasome and is associated with ubiquitin-dependent protein catabolism, oxidative-stress responses, and proteasome regulation. Its membership in the supplementary PCI-domain and proteasome-related STRING terms (STRING SMART Motif in proteasome subunits, Int-6, Nip-1 and TRIP-15; within-query FDR = 0.003) (STRING InterPro Proteasome component (PCI) domain; within-query FDR = 0.0318), prostate protein detection, and disease associations involving plasma-cell malignancy, lymphoma, neurodegeneration, and neoplasia make it an important proteostasis marker.
- **Conclusion**: Established evidence supports PSMD13 as the module's clearest proteasome-related representative. Its network position suggests coordination between protein degradation and synthesis or targeting, but the absence of a multi-member hu.MAP complex means that a unified proteasome complex cannot be claimed for this module.

#### PSAT1

- **Related proteins** (co-abundance neighbors): EIF3C (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoserine aminotransferase 1. This gene encodes a member of the class-V pyridoxal-phosphate-dependent aminotransferase family. The encoded protein is a phosphoserine aminotransferase and decreased expression may be associated with schizophrenia. Mutations in this gene are also associated with phosphoserine aminotransferase deficiency. Alternative splicing results in multiple transcript variants. Pseudogenes of this gene have b…
- **Diseases (Open Targets)**: Neu-Laxova syndrome 2 (0.809); PSAT deficiency (0.745); Neu-Laxova syndrome (0.634); neurometabolic disorder due to serine deficiency (0.437); type 2 diabetes mellitus (0.419)
- **Europe PMC papers**: 3221
- **Why important**: PSAT1 is a network bridge to EIF3C and adds a metabolic dimension that is not represented by the translation and proteasome genes alone. It encodes phosphoserine aminotransferase, participates in L-serine biosynthesis, and has annotations related to pyridoxine biosynthesis, mechanical-stimulus response, and negative regulation of ferroptosis. It is tissue enhanced in several organs, including brain, kidney, liver, and pancreas, is immune-cell enhanced in T-reg cells, has strong disease associations involving serine deficiency and neurometabolic disorders, and has extensive literature coverage.
- **Conclusion**: Established evidence supports PSAT1 as a serine-metabolism and stress-response enzyme rather than a core translation or proteasome component. Its connection to EIF3C could indicate metabolic support for protein synthesis or stress adaptation, but that interpretation is a module-level hypothesis and is not confirmed by global enrichment.

#### SRP72

- **Related proteins** (co-abundance neighbors): PSMD13 (0.81); STRING partners: RPL9 (0.878)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal recognition particle 72. This gene encodes the 72 kDa subunit of the signal recognition particle (SRP), a ribonucleoprotein complex that mediates the targeting of secretory proteins to the endoplasmic reticulum (ER). The SRP complex consists of a 7S RNA and 6 protein subunits: SRP9, SRP14, SRP19, SRP54, SRP68, and SRP72, that are bound to the 7S RNA as monomers or heterodimers. SRP has at least 3 distinct functions that c…
- **Diseases (Open Targets)**: autosomal dominant aplasia and myelodysplasia (0.641); neurodegenerative disease (0.416); intracranial subdural hematoma (0.280); type 2 diabetes mellitus (0.044); oropharynx cancer (0.032)
- **Europe PMC papers**: 696
- **Why important**: SRP72 is connected to PSMD13 in the co-abundance network and to RPL9 in STRING. It is a component of the signal-recognition particle, which mediates recognition of signal sequences, translational arrest, and cotranslational targeting of proteins to the endoplasmic reticulum. The supplementary STRING annotation for SRP-dependent cotranslational membrane targeting (STRING RCTM SRP-dependent cotranslational protein targeting to membrane; within-query FDR = 0.0312) directly supports this functional interpretation. It has prostate protein detection and disease associations involving aplasia or myelodysplasia and neurodegenerative disease.
- **Conclusion**: Established evidence supports SRP72 as the module's membrane-targeting component. Its placement beside translation and proteasome-related genes is consistent with coordinated synthesis, delivery, and turnover of proteins, but the data do not establish that these processes are physically assembled into one complex.
