# Conserved co-abundance modules: liver and ovary

## Module 0

**Tissue pair**: liver and ovary  
**Genes (7)**: ABCF1, GAR1, EIF4G1, NUP155, SF3A1, STT3A, ZFR

### Function

The module does not support a single, statistically validated GO or KEGG function: no GO/KEGG term passed global correction, and there were no supplementary STRING enrichment terms. Its constituent annotations instead point to coordinated intracellular gene-expression and protein-homeostasis processes. EIF4G1 supports cap-dependent translation initiation; ABCF1 is linked to translation and translational initiation; SF3A1 supports spliceosome assembly and pre-mRNA splicing; GAR1 supports snoRNA-guided rRNA pseudouridine synthesis and ribosome biogenesis; NUP155 supports nucleocytoplasmic transport and nuclear-envelope organization; and STT3A supports co-translational protein N-glycosylation in the endoplasmic reticulum. The co-abundance pattern is therefore most consistent with a broad RNA-processing, translation, nuclear-trafficking and protein-biogenesis program rather than a narrowly defined pathway. This interpretation is provisional because the module has no globally significant enrichment and its genes span several cellular compartments.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes, and the encoded proteins are intracellular or nuclear-associated. Most genes have low tissue specificity, and all have low immune-cell specificity, arguing against a blood-cell-enriched module or a simple immune-cell contamination explanation. Protein detection is generally present in liver and often present in ovary, although NUP155 is not detected in either tissue by the stated IHC results and STT3A is not detected in ovary. Several genes show enhancement in late spermatids, with additional enhancement in syncytiotrophoblasts, late primary spermatocytes, esophageal apical cells or neutrophils. These cell-type annotations suggest that some co-abundance may reflect shared epithelial, reproductive or differentiation-related cellular programs, but the available HPA evidence does not identify one dominant cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair reached the stated STRING interaction threshold, there was no STRING functional enrichment, and no hu.MAP complex contained multiple module members. Thus, the module is not supported here as a known physical protein complex or as a densely documented interaction neighborhood. The network itself links EIF4G1 to ZFR, SF3A1, GAR1 and NUP155, while NUP155 links to ABCF1 and STT3A. This pattern places EIF4G1 and NUP155 as apparent network connectors, but the lack of qualifying STRING and hu.MAP support means these edges should be interpreted as co-abundance relationships rather than established direct physical interactions.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared liver-ovary co-abundance pattern may be a new systems-level observation because it is not represented by qualifying STRING interactions, a shared hu.MAP complex or a significant GO/KEGG enrichment signature. However, it cannot be called a new biological mechanism from these results alone. The individual genes and their functions are established, and database absence can reflect incomplete coverage, context dependence, indirect regulation or the distinction between co-abundance and physical interaction. The defensible conclusion is that the cross-tissue co-abundance configuration is potentially novel, whereas novelty of the underlying biology remains unproven and would require replication, independent cohorts and targeted validation.

**Hypothesis.** Hypothesis: in liver and ovary, a shared demand for coordinated intracellular biosynthetic capacity may couple RNA handling and nuclear transport with translation, ribosome and rRNA maturation, and endoplasmic-reticulum protein glycosylation. EIF4G1 and NUP155 may represent central co-abundance anchors connecting cytosolic translation with nuclear exchange, while SF3A1 and GAR1 reflect RNA maturation and ribosome-related activity, and STT3A reflects downstream processing of newly synthesized proteins. This is a mechanistic hypothesis, not an established pathway assignment. It should be tested by replication across independent liver and ovary datasets, cell-composition adjustment, perturbation of the proposed connectors, and measurement of RNA processing, translation and glycosylation outputs.

### Important genes

#### EIF4G1

- **Related proteins** (co-abundance neighbors): ZFR (0.89), SF3A1 (0.84), GAR1 (0.82), NUP155 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 has the strongest connector role in the module and is linked to ZFR, SF3A1, GAR1 and NUP155. Its established function as a scaffold of the EIF4F complex places it directly at cap-dependent translation initiation, a plausible organizing process for a broad biosynthetic module. It is detected in both liver and ovary, has low tissue specificity, and has extensive literature covering translation, cell growth, autophagy and disease associations including neurodegenerative disease and Parkinson disease.
- **Conclusion**: Established: EIF4G1 is a translation-initiation scaffold and the leading network connector in this module. Hypothesis: its co-abundance may mark variation in general translational capacity that is coordinated with nuclear RNA processing. The data do not establish that EIF4G1 causally organizes the other genes.

#### NUP155

- **Related proteins** (co-abundance neighbors): ABCF1 (0.85), EIF4G1 (0.81), STT3A (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 155. Nucleoporins are proteins that play an important role in the assembly and functioning of the nuclear pore complex (NPC) which regulates the movement of macromolecules across the nuclear envelope (NE). The protein encoded by this gene plays a role in the fusion of NE vesicles and formation of the double membrane NE. The protein may also be involved in cardiac physiology and may be associated with t…
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); atrial fibrillation (0.470); familial atrial fibrillation (0.390)
- **Europe PMC papers**: 944
- **Why important**: NUP155 is the second prominent network connector and links EIF4G1 with ABCF1 and STT3A. Its established role in the nuclear pore complex, RNA export, protein import and nuclear-envelope organization makes it a biologically plausible interface between nuclear gene expression and cytosolic protein production. It is tissue enriched in testis and enhanced in late spermatids, is not detected by the stated IHC results in liver or ovary, and has established disease associations including atrial fibrillation and viral disease.
- **Conclusion**: Established: NUP155 participates in nuclear-envelope and nucleocytoplasmic-transport biology and occupies a connector position in the co-abundance graph. Hypothesis: it may couple nuclear export or envelope state to translational and ER-related activity in the shared module. The tissue-detection discrepancy makes this interpretation particularly dependent on transcript or proteomic validation.

#### SF3A1

- **Related proteins** (co-abundance neighbors): EIF4G1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in liver, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 connects to EIF4G1 and supplies the module with an established pre-mRNA-splicing function through the U2 snRNP and spliceosome. It is detected in both liver and ovary, has low tissue specificity, and shows cell-type enhancement in late spermatids and neutrophils. Its substantial literature and disease associations provide stronger prior biological support than the module-level enrichment results.
- **Conclusion**: Established: SF3A1 is a spliceosomal RNA-processing factor that is co-abundant with the module's translation connector. Hypothesis: the module may reflect coordinated demand for transcript maturation and translation rather than a direct SF3A1 protein interaction network. Causality is not demonstrated.

#### GAR1

- **Related proteins** (co-abundance neighbors): EIF4G1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in liver, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GAR1 ribonucleoprotein. This gene is a member of the H/ACA snoRNPs (small nucleolar ribonucleoproteins) gene family. snoRNPs are involved in various aspects of rRNA processing and modification and have been classified into two families: C/D and H/ACA. The H/ACA snoRNPs also include the DKC1, NOLA2 and NOLA3 proteins. These four H/ACA snoRNP proteins localize to the dense fibrillar components of nucleoli and to coiled (Ca…
- **Diseases (Open Targets)**: neurodegenerative disease (0.400); prostate carcinoma (0.198); Thrombocytopenia (0.048); familial primary hypomagnesemia with normocalciuria and normocalcemia (0.041); renal hypomagnesemia 2 (0.041)
- **Europe PMC papers**: 1232
- **Why important**: GAR1 connects to EIF4G1 and represents a distinct nucleolar component of the module. Its established role in H/ACA snoRNPs, rRNA pseudouridylation, ribosome biogenesis and telomere maintenance provides a mechanistic link between RNA modification and translational capacity. It is detected in both liver and ovary, is enhanced in syncytiotrophoblasts, and has substantial literature together with disease associations involving neurodegenerative disease and hematologic or mineral-balance disorders.
- **Conclusion**: Established: GAR1 supports nucleolar RNA modification and ribosome biogenesis. Hypothesis: GAR1 co-abundance may indicate that ribosome production is coordinated with EIF4G1-dependent translation in the shared tissue state. The module does not prove that these proteins act in one complex.

#### STT3A

- **Related proteins** (co-abundance neighbors): NUP155 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: STT3 oligosaccharyltransferase complex catalytic subunit A. The protein encoded by this gene is a catalytic subunit of the N-oligosaccharyltransferase (OST) complex, which functions in the endoplasmic reticulum to transfer glycan chains to asparagine residues of target proteins. A separate complex containing a similar catalytic subunit with an overlapping function also exists. Multiple transcript variants encoding different isoforms have been found for thi…
- **Diseases (Open Targets)**: congenital disorder of glycosylation, type Iw, autosomal dominant (0.751); STT3A-congenital disorder of glycosylation (0.740); dengue disease (0.512); COVID-19 (0.370); hereditary disease (0.192)
- **Europe PMC papers**: 944
- **Why important**: STT3A connects to NUP155 and contributes an established endoplasmic-reticulum protein-biogenesis function through the catalytic N-oligosaccharyltransferase complex. Its annotation expands the module beyond RNA metabolism to co-translational protein modification. It is tissue enhanced in parathyroid gland, detected in liver but not ovary by the stated IHC results, and has strong disease associations with STT3A-related congenital disorders of glycosylation.
- **Conclusion**: Established: STT3A catalyzes N-linked glycosylation during protein biosynthesis and is linked to congenital glycosylation disorders. Hypothesis: its association with NUP155 may reflect coordinated nuclear-to-ER protein-production demand or a shared cellular-state signal. A direct mechanistic connection to the other module genes remains unestablished.

## Module 1

**Tissue pair**: liver and ovary  
**Genes (12)**: ACIN1, DYNC1I2, DHX9, CLINT1, HNRNPR, CAD, RPL12, SF3B3, SUPT16H, SRSF7, ALYREF, SNRNP200

### Function

The module is most strongly interpreted as a nuclear pre-mRNA processing and spliceosome module. The primary evidence is the coherent set of globally corrected terms for RNA splicing, spliceosome-mediated mRNA splicing, mRNA processing, RNA processing, mRNA metabolism, and RNA binding (GO:BP RNA splicing, via transesterification reactions; q_global = 0.00143) through (GO:MF RNA binding; q_global = 0.0497). The same interpretation is independently supported by the STRING enrichment for mRNA splicing, the major mRNA-splicing pathway, RNA metabolism, and spliceosomal processes (STRING Keyword mRNA splicing; within-query FDR = 5.51e-06) through (STRING Process Gene expression; within-query FDR = 0.0046). The core functional signal is supplied by ACIN1, DHX9, HNRNPR, SF3B3, SNRNP200, and SRSF7, with ALYREF providing an additional RNA-export and mRNA-metabolism connection. SUPT16H, CAD, CLINT1, DYNC1I2, and RPL12 may reflect linked transcriptional, nucleotide, vesicular, cytoskeletal, or translational processes rather than the central module function. The RNA-binding component of the module is also supported by (GO:MF RNA binding; q_global = 0.0497).

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are generally detected in both liver and ovary. Most genes have low tissue specificity and low immune-cell specificity, which is consistent with a broadly expressed nuclear or cellular housekeeping-like program rather than a liver-specific or ovary-specific secretory program. The module is therefore unlikely to be explained primarily by circulating plasma proteins. There are limited cell-type signals, including erythrocyte progenitors, megakaryocytic progenitors, neutrophil progenitors, basophils, and several epithelial or stromal cell types. ALYREF is tissue-enhanced in bone marrow and enriched in progenitor or megakaryocyte-related cell types, while CLINT1 is enriched in a myeloid progenitor context and in basophils. These signals warrant checking for blood or hematopoietic contamination, but the overall HPA pattern does not support a dominant blood-cell module. The shared liver-ovary signal is more plausibly a broadly expressed nuclear RNA-processing program, potentially influenced by common cell types or sample composition.

**GO/KEGG enrichment**: 9 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA splicing, via transesterification reactions | 0.00143 | ACIN1, DHX9, HNRNPR, SF3B3, SNRNP200, SRSF7 |
| GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile | 0.00143 | ACIN1, DHX9, HNRNPR, SF3B3, SNRNP200, SRSF7 |
| GO:BP mRNA splicing, via spliceosome | 0.00143 | ACIN1, DHX9, HNRNPR, SF3B3, SNRNP200, SRSF7 |
| KEGG Spliceosome - Homo sapiens (human) | 0.00387 | ACIN1, ALYREF, SF3B3, SNRNP200, SRSF7 |
| GO:BP RNA splicing | 0.00432 | ACIN1, DHX9, HNRNPR, SF3B3, SNRNP200, SRSF7 |
| GO:BP mRNA processing | 0.00691 | ACIN1, DHX9, HNRNPR, SF3B3, SNRNP200, SRSF7 |
| GO:BP mRNA metabolic process | 0.0338 | ACIN1, DHX9, HNRNPR, SF3B3, SNRNP200, SRSF7 |
| GO:BP RNA processing | 0.0426 | ACIN1, DHX9, HNRNPR, SF3B3, SNRNP200, SRSF7 |
| GO:MF RNA binding | 0.0497 | ACIN1, ALYREF, DHX9, HNRNPR, RPL12, SF3B3, SNRNP200, SRSF7, SUPT16H |

### STRING and hu.MAP

STRING contains a connected set of known or strongly supported relationships centered on ALYREF, DHX9, HNRNPR, SRSF7, SF3B3, and SNRNP200. Particularly coherent relationships include ALYREF with DHX9, HNRNPR, and SRSF7; DHX9 with HNRNPR, SF3B3, SNRNP200, and SRSF7; and SF3B3 with SNRNP200. The STRING functional enrichments for splicing and RNA metabolism (STRING Keyword mRNA splicing; within-query FDR = 5.51e-06) through (STRING COMPARTMENTS Catalytic step 2 spliceosome; within-query FDR = 0.0102) therefore support a biologically integrated module rather than an arbitrary co-abundance grouping, although these enrichments are supplementary and are not global multiple-testing evidence. hu.MAP provides additional complex-level support. ACIN1 and SRSF7 recur together across several spliceosome- or exon-junction-related complexes (hu.MAP huMAP3_09943.1) through (hu.MAP huMAP3_11073.1), with ALYREF also present in (hu.MAP huMAP3_09943.1). SF3B3 and SNRNP200 occur together in a large spliceosomal complex (hu.MAP huMAP3_08980.1). The partial overlap between the module and these larger complexes is consistent with a subnetwork or co-abundance slice of established RNA-processing machinery, not necessarily a complete biochemical complex. SUPT16H, RPL12, CAD, CLINT1, and DYNC1I2 lack corresponding STRING or hu.MAP support within the supplied evidence, so their inclusion may reflect co-regulation, indirect coupling, or sample-level co-abundance rather than direct physical interaction.

**STRING interactions (score >= 0.7)**: 10 of 66 gene pairs: ACIN1–ALYREF (0.92); ALYREF–DHX9 (0.953); ALYREF–HNRNPR (0.851); ALYREF–SRSF7 (0.958); DHX9–HNRNPR (0.909); DHX9–SF3B3 (0.73); DHX9–SNRNP200 (0.784); DHX9–SRSF7 (0.789); HNRNPR–SRSF7 (0.833); SF3B3–SNRNP200 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword mRNA splicing (FDR = 5.51e-06, 7 genes); RCTM mRNA Splicing - Major Pathway (FDR = 2.21e-05, 7 genes); RCTM Metabolism of RNA (FDR = 8.02e-05, 8 genes); Process RNA splicing (FDR = 0.00021, 7 genes); Process mRNA processing (FDR = 0.00027, 7 genes); Process mRNA splicing, via spliceosome (FDR = 0.00037, 6 genes); KEGG Spliceosome (FDR = 0.00093, 5 genes); Process RNA metabolic process (FDR = 0.0023, 8 genes); Process Gene expression (FDR = 0.0046, 9 genes); Component Nuclear lumen (FDR = 0.0052, 11 genes); Component Catalytic step 2 spliceosome (FDR = 0.0052, 4 genes); Keyword RNA-binding (FDR = 0.0061, 6 genes); Keyword Spliceosome (FDR = 0.0065, 4 genes); COMPARTMENTS Nucleoplasm (FDR = 0.0102, 6 genes); COMPARTMENTS Catalytic step 2 spliceosome (FDR = 0.0102, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09943.1 (SRSF7, ALYREF, ACIN1; 3/78); huMAP3_06097.1 (SRSF7, ACIN1; 2/22); huMAP3_10564.1 (SRSF7, ACIN1; 2/37); huMAP3_09621.1 (SRSF7, ACIN1; 2/56); huMAP3_11073.1 (SRSF7, ACIN1; 2/67); huMAP3_08980.1 (SNRNP200, SF3B3; 2/97)

### Novelty

The molecular function represented by this module is not new: its central genes, STRING relationships, and hu.MAP overlaps place it within well-established spliceosome, RNA-binding, RNA-export, and mRNA-processing biology. The potentially novel observation is the co-abundance of this particular gene combination across liver and ovary. The fact sheet does not establish whether this exact tissue-pair module has been reported previously, and absence from STRING or hu.MAP would not prove novelty because those resources primarily capture physical interactions or curated complexes rather than tissue-pair co-abundance patterns. I would therefore describe the module as a potentially new tissue-level co-abundance configuration built from largely established molecular machinery, rather than as a newly discovered pathway or complex. Demonstrating novelty would require comparison with published liver and ovary co-expression studies, independent cohorts, and replication after controlling for cell-type composition.

**Hypothesis.** Hypothesis: the shared liver-ovary module reflects coordinated regulation of nuclear RNA maturation, in which spliceosomal assembly and remodeling are coupled to RNA binding, transcript export, and transcriptional output. A plausible mechanistic axis is that SF3B3 and SNRNP200 support spliceosomal recognition and remodeling, SRSF7 and HNRNPR regulate RNA binding and splice-site decisions, DHX9 promotes RNA or RNA-DNA unwinding and transcript handling, while ALYREF links processed transcripts to nuclear export. ACIN1 may connect splicing and exon-junction functions with context-dependent apoptotic regulation. SUPT16H could couple transcription elongation and chromatin accessibility to RNA processing, whereas the less directly supported CAD, CLINT1, DYNC1I2, and RPL12 associations may represent linked cellular state or translational and trafficking programs. This model predicts coordinated changes in splicing and transcript export, but co-abundance alone does not establish physical interaction, causal order, or tissue-specific mechanism.

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): SUPT16H (0.92), RPL12 (0.84), HNRNPR (0.83); STRING partners: ALYREF (0.953), HNRNPR (0.909), SF3B3 (0.73), SNRNP200 (0.784), SRSF7 (0.789)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is a hub-like connector within the module, linking SUPT16H, HNRNPR, SF3B3, SNRNP200, and SRSF7. It appears in nearly all primary RNA-splicing and RNA-processing terms (GO:BP RNA splicing, via transesterification reactions; q_global = 0.00143) through (GO:MF RNA binding; q_global = 0.0497) and in the corresponding STRING splicing and RNA-metabolism evidence (STRING Keyword mRNA splicing; within-query FDR = 5.51e-06) through (STRING Process mRNA splicing, via spliceosome; within-query FDR = 0.00037) and (STRING Process RNA metabolic process; within-query FDR = 0.0023) through (STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.0102). Its established helicase activity provides a mechanistic bridge between RNA structure, transcript processing, and transcriptional regulation. It also has extensive literature and disease associations involving neurodevelopmental and neurodegenerative disorders.
- **Conclusion**: Established: DHX9 is a strong functional anchor for the module and is consistent with spliceosome-associated RNA remodeling. Hypothesis: its co-abundance may help couple RNA helicase activity to tissue-shared regulation of transcript processing. The module does not demonstrate that DHX9 is the causal driver.

#### SF3B3

- **Related proteins** (co-abundance neighbors): SUPT16H (0.86); STRING partners: DHX9 (0.73), SNRNP200 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Nucleoli rim; IHC detected in liver, ovary
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: splicing factor 3b subunit 3. This gene encodes subunit 3 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); dengue disease (0.370); cervical cancer (0.189); cervical carcinoma (0.189); prostate cancer (0.111)
- **Europe PMC papers**: 965
- **Why important**: SF3B3 is a spliceosome U2 small nuclear ribonucleoprotein component and is present in every primary enrichment term (GO:BP RNA splicing, via transesterification reactions; q_global = 0.00143) through (GO:MF RNA binding; q_global = 0.0497). It has a direct STRING relationship with SNRNP200 and an additional relationship with DHX9, while hu.MAP places it with SNRNP200 in a spliceosomal complex (hu.MAP huMAP3_08980.1). Its position connects the module to branch-site recognition and spliceosome assembly, and it has substantial literature and disease-related evidence.
- **Conclusion**: Established: SF3B3 provides direct molecular support for a spliceosomal interpretation and for the SF3B3-SNRNP200 subnetwork. Hypothesis: coordinated SF3B3 abundance may mark variation in spliceosome capacity or assembly state across the two tissues. The data do not show altered catalytic activity or a specific alternative-splicing event.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): SUPT16H (0.82); STRING partners: DHX9 (0.784), SF3B3 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is a U5 small nuclear ribonucleoprotein helicase and a core spliceosomal remodeling factor. It appears across the primary splicing terms (GO:BP RNA splicing, via transesterification reactions; q_global = 0.00143) through (GO:MF RNA binding; q_global = 0.0497), has a very strong STRING relationship with SF3B3, and is also linked to DHX9 in STRING. Its placement beside SF3B3 in hu.MAP (hu.MAP huMAP3_08980.1) gives the module a clear spliceosomal core. It has established associations with retinal degeneration and a substantial literature base.
- **Conclusion**: Established: SNRNP200 supports spliceosome assembly and conformational remodeling and is one of the clearest mechanistic markers of the module. Hypothesis: its co-abundance with SF3B3 may reflect coordinated control of spliceosomal remodeling demand. The absence of HPA protein detection in liver and ovary should be treated as a measurement caveat, not proof of biological absence.

#### SRSF7

- **Related proteins** (co-abundance neighbors): ACIN1 (0.86); STRING partners: ALYREF (0.958), DHX9 (0.789), HNRNPR (0.833)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, ovary
- **hu.MAP 3.0**: huMAP3_09943.1, huMAP3_06097.1, huMAP3_10564.1, huMAP3_09621.1, huMAP3_11073.1
- **Function (MyGene.info)**: serine and arginine rich splicing factor 7. The protein encoded by this gene is a member of the serine/arginine (SR)-rich family of pre-mRNA splicing factors, which constitute part of the spliceosome. Each of these factors contains an N-terminal RNA recognition motif (RRM) for binding RNA and a C-terminal RS domain for binding other proteins. The RS domain is rich in serine and arginine residues and facilitates interaction between different…
- **Diseases (Open Targets)**: neurodegenerative disease (0.536); dengue disease (0.370); cystitis (0.221); smoking initiation (0.107); neoplasm (0.082)
- **Europe PMC papers**: 1327
- **Why important**: SRSF7 is an RNA-binding serine- and arginine-rich splicing factor with a direct module connection to ACIN1 and STRING relationships with ALYREF, DHX9, and HNRNPR. It occurs in every primary enrichment term (GO:BP RNA splicing, via transesterification reactions; q_global = 0.00143) through (GO:MF RNA binding; q_global = 0.0497) and in multiple hu.MAP complexes with ACIN1 (hu.MAP huMAP3_09943.1) through (hu.MAP huMAP3_11073.1). Its established role in alternative-splicing regulation makes it important for interpreting the module as a regulatory RNA-processing program rather than merely a structural spliceosome signature.
- **Conclusion**: Established: SRSF7 is a central RNA-binding and splicing regulator with strong network and complex support. Hypothesis: it may mediate tissue-shared changes in transcript isoform choice within the module. The fact sheet does not identify which transcripts or isoforms are regulated.

#### ALYREF

- **Related proteins** (co-abundance neighbors): HNRNPR (0.86); STRING partners: ACIN1 (0.92), DHX9 (0.953), HNRNPR (0.851), SRSF7 (0.958)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in liver, ovary
- **hu.MAP 3.0**: huMAP3_09943.1
- **Function (MyGene.info)**: Aly/REF export factor. The protein encoded by this gene is a heat stable, nuclear protein and functions as a molecular chaperone. It is thought to regulate dimerization, DNA binding, and transcriptional activity of basic region-leucine zipper (bZIP) proteins. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.542); dengue disease (0.370); neoplasm (0.103); non-small cell lung carcinoma (0.102); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 1636
- **Why important**: ALYREF links the module to mRNA export and RNA metabolism and connects in STRING to ACIN1, DHX9, HNRNPR, and SRSF7. It contributes to the primary spliceosome and RNA-binding evidence (KEGG Spliceosome - Homo sapiens (human); q_global = 0.00387) and (GO:MF RNA binding; q_global = 0.0497), to the STRING splicing and RNA-metabolism evidence (STRING Keyword mRNA splicing; within-query FDR = 5.51e-06) through (STRING COMPARTMENTS Catalytic step 2 spliceosome; within-query FDR = 0.0102), and to a hu.MAP complex containing ACIN1 and SRSF7 (hu.MAP huMAP3_09943.1). Its bone-marrow and progenitor-associated HPA pattern is a useful composition caveat, while its extensive literature supports a well-established transcript-handling role.
- **Conclusion**: Established: ALYREF provides a credible bridge from nuclear RNA processing to export and is embedded in known RNA-processing relationships. Hypothesis: its presence may indicate that the shared module coordinates transcript maturation with export, or it may partly reflect hematopoietic cell contribution. Tissue-level co-abundance cannot distinguish these explanations.

## Module 2

**Tissue pair**: liver and ovary  
**Genes (6)**: ATP1A1, ATP2A2, DMAC2L, NDUFAF4, SYNGR2, VDAC2

### Function

The module is most consistently interpreted as a membrane and mitochondrial ion-handling module. The primary evidence is global enrichment for monoatomic ion transmembrane transporter activity (GO:MF monoatomic ion transmembrane transporter activity; q_global = 0.0344) and the cGMP-PKG signaling pathway (KEGG cGMP-PKG signaling pathway - Homo sapiens (human); q_global = 0.0432). The transporter signal is supported by ATP1A1, ATP2A2, VDAC2, and DMAC2L, while the pathway signal is carried by ATP1A1, ATP2A2, and VDAC2. ATP1A1 establishes plasma-membrane sodium and potassium gradients; ATP2A2 controls intracellular calcium sequestration; VDAC2 provides a mitochondrial outer-membrane metabolite pore and is linked to mitochondrial apoptotic regulation; and DMAC2L is a mitochondrial ATP-synthase component involved in proton transport. NDUFAF4 adds a mitochondrial respiratory-chain assembly connection. SYNGR2 is less well characterized but has reported associations with membrane traffic and regulated exocytosis. Thus, the established interpretation is coordinated ion transport, electrochemical-gradient maintenance, calcium handling, and mitochondrial energy or membrane-state regulation. The cGMP-PKG annotation should be interpreted as pathway membership rather than proof that the entire module directly executes cGMP signaling.

**Cell composition.** The module is not dominated by secreted proteins, plasma proteins, or blood-cell markers. HPA reports no secreted genes and low immune-cell specificity for every member, arguing against a simple blood-contamination explanation. Most members have low tissue specificity, with one tissue-enhanced gene and one group-enriched gene; the enriched tissues are heterogeneous and include parathyroid gland, heart muscle, skeletal muscle, and tongue. All members show some cell-type enhancement, including epithelial, oocyte, muscle, renal, intestinal, and germ-cell populations. This pattern is more compatible with broadly distributed membrane, mitochondrial, and cell-type structural functions than with a liver- or ovary-exclusive program. Protein detection is asymmetric between the tissues: several members are detected in liver, whereas ATP2A2 is detected in ovary, and several proteins are not detected in one or both tissues. Consequently, the shared module may reflect common cellular physiology or differing cell-type composition rather than a specialized pathway unique to both organs.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF monoatomic ion transmembrane transporter activity | 0.0344 | ATP1A1, ATP2A2, DMAC2L, VDAC2 |
| KEGG cGMP-PKG signaling pathway - Homo sapiens (human) | 0.0432 | ATP1A1, ATP2A2, VDAC2 |

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, ATP1A1–ATP2A2, directly connecting the plasma-membrane sodium–potassium pump with the calcium pump. STRING supplementary enrichment independently supports ion transport, inorganic molecular transport, cGMP-PKG signaling, and P-type ATPase or cation-transporter domains (10 supplementary STRING terms; within-query FDR 0.0013–0.0387). These supplementary results reinforce the functional interpretation but are not additional globally corrected evidence. hu.MAP places ATP1A1 and ATP2A2 together in C1, and ATP2A2 and VDAC2 together in C2. However, each complex contains many members outside this module, so the module captures only a small substructure of larger cellular assemblies. NDUFAF4, SYNGR2, and DMAC2L have no reported within-module STRING partner in the supplied evidence; their co-abundance therefore need not represent a direct physical interaction. Overall, the network combines one established ATPase pair with broader mitochondrial, membrane, and transport context rather than constituting a single fully validated physical complex.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: ATP1A1–ATP2A2 (0.82)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Ion transport (FDR = 0.0013, 4 genes); Function Inorganic molecular entity transmembrane transporter activity (FDR = 0.0089, 4 genes); Function Ion transmembrane transporter activity (FDR = 0.0096, 4 genes); KEGG cGMP-PKG signaling pathway (FDR = 0.0136, 3 genes); SMART Cation transporter/ATPase, N-terminus (FDR = 0.018, 2 genes); Pfam E1-E2 ATPase (FDR = 0.0237, 2 genes); Pfam Cation transporting ATPase, C-terminus (FDR = 0.0237, 2 genes); Pfam Cation transport ATPase (P-type) (FDR = 0.0237, 2 genes); Function P-type ion transporter activity (FDR = 0.0387, 2 genes); Function Inorganic cation transmembrane transporter activity (FDR = 0.0387, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10473.1 (ATP1A1, ATP2A2; 2/24); huMAP3_09592.1 (ATP2A2, VDAC2; 2/95)

### Novelty

A strong claim that this is a new biological mechanism is not justified. ATP1A1, ATP2A2, VDAC2, NDUFAF4, and DMAC2L have established roles in ion transport, calcium handling, mitochondrial membrane function, respiratory-chain assembly, or ATP synthesis, and the ATP1A1–ATP2A2 relationship is already supported by STRING and hu.MAP. The exact liver–ovary co-abundance configuration may nevertheless be a potentially novel observation, especially because only one internal STRING edge is present and several module members lack documented physical links in the supplied resources. Yet absence from STRING or hu.MAP cannot establish novelty: it may reflect incomplete interaction coverage, tissue-dependent regulation, indirect co-regulation, or cell-composition effects. The defensible conclusion is that the functional components are established, while the cross-tissue co-abundance arrangement is a candidate observation requiring independent replication and comparison with published tissue proteomic or transcriptomic networks.

**Hypothesis.** Hypothesis: the shared module reflects coordinated maintenance of membrane and organelle electrochemical gradients across liver and ovary cell populations. ATP1A1 could maintain the plasma-membrane sodium and potassium gradient, ATP2A2 could buffer cytosolic calcium through endoplasmic-reticulum uptake, and VDAC2 together with DMAC2L and NDUFAF4 could couple mitochondrial permeability, proton-driven ATP production, and respiratory-chain capacity to cellular energetic demand. SYNGR2 may mark membrane-trafficking or exocytotic state rather than act as a core transporter. In this model, the module is a co-regulated physiological program linking ion homeostasis, mitochondrial energy handling, and membrane traffic. This remains a hypothesis: the co-abundance data do not demonstrate direct biochemical coupling, causal regulation, or active cGMP-PKG signaling.

### Important genes

#### ATP1A1

- **Related proteins** (co-abundance neighbors): ATP2A2 (0.81), NDUFAF4 (0.80); STRING partners: ATP2A2 (0.82)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_10473.1
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 is a central network connector, linked to ATP2A2 and NDUFAF4, and it appears in both primary terms (GO:MF monoatomic ion transmembrane transporter activity; q_global = 0.0344) and (KEGG cGMP-PKG signaling pathway - Homo sapiens (human); q_global = 0.0432) as well as all supplied STRING enrichment categories (10 supplementary STRING terms; within-query FDR 0.0013–0.0387). Its established function is the P-type sodium–potassium pump that creates electrochemical gradients supporting osmoregulation, coupled transport, and excitability. It has tissue-enhanced expression in parathyroid gland and cell-type enhancement across several epithelial and ion-transporting populations. It also has substantial literature and disease associations involving neuropathy, electrolyte-related disease, and cardiac disorders.
- **Conclusion**: Established evidence supports ATP1A1 as a core membrane-gradient component and a major functional anchor of the module. The co-abundance pattern suggests coordinated regulation with calcium and mitochondrial genes, but it does not establish that ATP1A1 directly regulates the other module members in liver or ovary.

#### ATP2A2

- **Related proteins** (co-abundance neighbors): ATP1A1 (0.81); STRING partners: ATP1A1 (0.82)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_10473.1, huMAP3_09592.1
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darie…
- **Diseases (Open Targets)**: Darier disease (0.823); acrokeratosis verruciformis (0.663); neurodegenerative disease (0.507); hereditary disease (0.416); schizophrenia (0.406)
- **Europe PMC papers**: 9327
- **Why important**: ATP2A2 is the other member of the only high-confidence STRING pair and occurs in both primary terms (GO:MF monoatomic ion transmembrane transporter activity; q_global = 0.0344) and (KEGG cGMP-PKG signaling pathway - Homo sapiens (human); q_global = 0.0432) and throughout the relevant STRING annotations (10 supplementary STRING terms; within-query FDR 0.0013–0.0387). It is a SERCA calcium pump responsible for intracellular calcium homeostasis and is linked to endoplasmic-reticulum or sarcoplasmic-reticulum calcium handling. It is group-enriched in muscle-related tissues, detected in ovary, represented in both hu.MAP complexes C1 and C2, and has extensive literature and well-established Darier disease associations.
- **Conclusion**: Established evidence makes ATP2A2 a core calcium-handling component and the strongest ovary-linked anchor in the supplied HPA evidence. It supports a membrane-ion-homeostasis interpretation, while any specific connection to cGMP-PKG signaling or to VDAC2 remains inferential.

#### VDAC2

- **Related proteins** (co-abundance neighbors): NDUFAF4 (0.87), SYNGR2 (0.87), DMAC2L (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: voltage dependent anion channel 2. This gene encodes a member of the voltage-dependent anion channel pore-forming family of proteins that are considered the main pathway for metabolite diffusion across the mitochondrial outer membrane. The encoded protein is also thought to be involved in the mitochondrial apoptotic pathway via regulation of BCL2-antagonist/killer 1 protein activity. Pseudogenes have been identified on chromosomes …
- **Diseases (Open Targets)**: neurodegenerative disease (0.345); alcohol drinking (0.204); atrial fibrillation (0.175); major depressive disorder (0.143); severe combined immunodeficiency (0.118)
- **Europe PMC papers**: 2914
- **Why important**: VDAC2 has the highest network connectivity in the supplied module and links NDUFAF4, SYNGR2, and DMAC2L. It appears in both primary terms (GO:MF monoatomic ion transmembrane transporter activity; q_global = 0.0344) and (KEGG cGMP-PKG signaling pathway - Homo sapiens (human); q_global = 0.0432) and in the ion-transport and cGMP-PKG STRING categories (4 supplementary STRING terms; within-query FDR 0.0013–0.0136). Its established role as a mitochondrial outer-membrane pore supports metabolite diffusion, and it has a reported role in mitochondrial apoptotic regulation and membrane phospholipid processes. It is included in hu.MAP complex C2 and has broad literature and disease associations.
- **Conclusion**: Established evidence supports VDAC2 as the principal mitochondrial interface in the module and a plausible bridge between ion handling and mitochondrial state. Its high network position makes it important, but the co-abundance data do not prove that it mediates the proposed cross-organelle coupling.

#### NDUFAF4

- **Related proteins** (co-abundance neighbors): VDAC2 (0.87), ATP1A1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase complex assembly factor 4. NADH:ubiquinone oxidoreductase (complex I) catalyzes the transfer of electrons from NADH to ubiquinone (coenzyme Q) in the first step of the mitochondrial respiratory chain, resulting in the translocation of protons across the inner mitochondrial membrane. This gene encodes a complex I assembly factor. Mutations in this gene are a cause of mitochondrial complex I deficiency. [provided by RefSeq, O…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.714); type 2 diabetes mellitus (0.607); mitochondrial disease (0.597); diabetes mellitus (0.578); mitochondrial complex I deficiency, nuclear type 15 (0.568)
- **Europe PMC papers**: 378
- **Why important**: NDUFAF4 connects ATP1A1 with VDAC2 in the module and provides a respiratory-chain assembly perspective not captured by the enriched terms. It is a mitochondrial complex-I assembly factor, and mutations are associated with mitochondrial complex-I deficiency. HPA indicates low tissue specificity, mitochondrial localization, and cell-type enhancement in oocytes and parietal cells. Its literature volume is smaller than that of the ATPase genes, but its function is mechanistically relevant to mitochondrial energy production.
- **Conclusion**: Established evidence supports NDUFAF4 as a mitochondrial respiratory-chain assembly component that may explain why it co-varies with VDAC2 and membrane ion pumps. Its role as a driver or regulator of the module is a hypothesis rather than an established conclusion.

#### DMAC2L

- **Related proteins** (co-abundance neighbors): VDAC2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: distal membrane arm assembly component 2 like. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. This gene en…
- **Diseases (Open Targets)**: L-2-hydroxyglutaric aciduria (0.446); hereditary disease (0.399); congenital ptosis (0.086); cataract (0.073); Duane retraction syndrome (0.071)
- **Europe PMC papers**: 37
- **Why important**: DMAC2L is connected to VDAC2 and is the fourth member of the primary ion-transporter term (GO:MF monoatomic ion transmembrane transporter activity; q_global = 0.0344), with additional support from the STRING ion-transport categories (STRING Keyword Ion transport; within-query FDR = 0.0013) (STRING Function Inorganic molecular entity transmembrane transporter activity; within-query FDR = 0.0089) (STRING Function Ion transmembrane transporter activity; within-query FDR = 0.0096) and (STRING Function Inorganic cation transmembrane transporter activity; within-query FDR = 0.0387). It encodes a mitochondrial ATP-synthase subunit involved in the proton channel and oxidative-phosphorylation-related ATP production. Its mitochondrial or nucleoplasmic localization and germ-cell-related cell-type enhancement make it relevant to energetic and reproductive-cell contexts, although its literature volume is comparatively limited.
- **Conclusion**: Established evidence supports DMAC2L as a mitochondrial proton-transport and ATP-synthase component that complements the VDAC2 and NDUFAF4 interpretation. Its inclusion in an ion-transporter enrichment is biologically coherent, but its direct functional relationship with the other module genes remains unproven.

#### SYNGR2

- **Related proteins** (co-abundance neighbors): VDAC2 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: synaptogyrin 2. This gene encodes an integral membrane protein containing four transmembrane regions and a C-terminal cytoplasmic tail that is tyrosine phosphorylated. The exact function of this protein is unclear, but studies of a similar rat protein suggest that it may play a role in regulating membrane traffic in non-neuronal cells. The gene belongs to the synaptogyrin gene family. Alternative splicing results…
- **Diseases (Open Targets)**: neoplasm (0.079); cancer (0.076); maturity-onset diabetes of the young (0.066); transient neonatal diabetes mellitus (0.053); diabetes mellitus, transient neonatal, 3 (0.053)
- **Europe PMC papers**: 261
- **Why important**: SYNGR2 has a peripheral network position, connected only to VDAC2, and it does not occur in the primary GO or KEGG terms or the supplied STRING enrichment terms. It is an integral membrane protein associated in the supplied annotation with regulated exocytosis, synaptic-vesicle membrane organization, and possible membrane traffic in non-neuronal cells. Its low tissue specificity, cell-type enhancement in epithelial and goblet populations, and lack of HPA protein detection in the tested tissues make it a useful boundary gene for interpreting the module.
- **Conclusion**: Established evidence supports SYNGR2 as a membrane-trafficking-associated protein, but not as a core ion transporter. Its co-abundance with VDAC2 may indicate membrane-state or vesicle-trafficking coordination, although this is a weaker and more tentative interpretation than the ATPase or mitochondrial assignments.

## Module 3

**Tissue pair**: liver and ovary  
**Genes (9)**: DDX5, HSPH1, MATR3, CTPS1, RUVBL2, CCT5, CCT3, CCT7, EFTUD2

### Function

The strongest interpretation is a nuclear and cytosolic RNA–protein homeostasis module centered on CCT/TRiC chaperone activity, with links to telomerase RNA localization, telomere maintenance, chromosome organization, RNA processing, and ATP-dependent remodeling. The primary GO evidence is internally coherent: the CCT3–CCT5–CCT7 group is repeatedly represented in (4 globally significant GO/KEGG terms, q_global 4.53e-05–4.53e-05; see the table), (GO:CC protein folding chaperone complex; q_global = 0.000577), and (8 globally significant GO/KEGG terms, q_global 0.00273–0.00273; see the table), while CCT3, CCT5, CCT7, and RUVBL2 support telomere maintenance, chromosome organization, and DNA-related processes in (GO:BP positive regulation of telomere maintenance; q_global = 0.000577), (GO:BP regulation of telomere maintenance; q_global = 0.000862), (GO:BP positive regulation of chromosome organization; q_global = 0.000862), (GO:BP regulation of chromosome organization; q_global = 0.00289), and (4 globally significant GO/KEGG terms, q_global 0.00569–0.00848; see the table). Protein folding and chaperone activity are supported by (GO:CC protein folding chaperone complex; q_global = 0.000577), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.0012), (GO:MF protein folding chaperone; q_global = 0.00372), and (GO:BP protein folding; q_global = 0.00406), with HSPH1 contributing to the broader folding and unfolded-protein-binding signal. The broad ATP, nucleotide-binding, and hydrolysis annotations in (9 globally significant GO/KEGG terms, q_global 0.0102–0.0256; see the table) and (GO:MF pyrophosphatase activity; q_global = 0.0361) (GO:MF hydrolase activity, acting on acid anhydrides; q_global = 0.0361) (GO:MF hydrolase activity, acting on acid anhydrides, in phosphorus-containing anhydrides; q_global = 0.0361) are consistent with an energy-dependent remodeling environment. The sperm–egg recognition and fertilization terms in (GO:BP binding of sperm to zona pellucida; q_global = 0.0099), (GO:BP sperm-egg recognition; q_global = 0.0099), (GO:BP cell-cell recognition; q_global = 0.0302), and (GO:BP single fertilization; q_global = 0.0398) should be interpreted cautiously: they may reflect shared reproductive-cell biology or annotation overlap rather than a specialized fertilization mechanism. MATR3 and EFTUD2 connect the module to nuclear RNA handling and spliceosomal biology, whereas DDX5 provides an RNA-helicase and transcriptional or splicing interface. Thus, the most defensible function is coordinated proteostasis and RNA–nuclear-body regulation, with a plausible telomere-maintenance component.

**Cell composition.** This is not a plasma-protein, secreted-protein, or blood-cell module. The HPA summary reports no secreted genes and low immune-cell specificity throughout, arguing against a blood-contamination explanation. Most genes have low tissue specificity, which is compatible with broadly expressed housekeeping or core cellular machinery. The proteins are detected in both liver and ovary for much of the module, although detection is gene-specific. RUVBL2 is tissue enhanced in testis and several genes show cell-type enrichment in spermatogenic or ciliated-cell populations, including CCT7, CCT5, RUVBL2, HSPH1, and MATR3. CTPS1 is enhanced in hepatocytes, while HSPH1 is enhanced in epididymal efferent duct absorptive cells and MATR3 in several epithelial or progenitor populations. These patterns suggest that the shared liver–ovary signal most likely reflects conserved intracellular machinery, with possible contributions from reproductive or ciliated cell types, rather than circulating proteins or immune cells.

**GO/KEGG enrichment**: 49 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA localization to Cajal body | 4.53e-05 | CCT3, CCT5, CCT7, RUVBL2 |
| GO:BP telomerase RNA localization to Cajal body | 4.53e-05 | CCT3, CCT5, CCT7, RUVBL2 |
| GO:BP telomerase RNA localization | 4.53e-05 | CCT3, CCT5, CCT7, RUVBL2 |
| GO:BP RNA localization to nucleus | 4.53e-05 | CCT3, CCT5, CCT7, RUVBL2 |
| GO:BP positive regulation of telomere maintenance | 0.000577 | CCT3, CCT5, CCT7, RUVBL2 |
| GO:CC protein folding chaperone complex | 0.000577 | CCT3, CCT5, CCT7, RUVBL2 |
| GO:BP regulation of telomere maintenance | 0.000862 | CCT3, CCT5, CCT7, RUVBL2 |
| GO:BP positive regulation of chromosome organization | 0.000862 | CCT3, CCT5, CCT7, RUVBL2 |
| GO:MF ATP-dependent protein folding chaperone | 0.0012 | CCT3, CCT5, CCT7, HSPH1 |
| GO:CC chaperonin-containing T-complex | 0.00273 | CCT3, CCT5, CCT7 |
| GO:BP protein localization to nuclear body | 0.00273 | CCT3, CCT5, CCT7 |
| GO:BP protein localization to Cajal body | 0.00273 | CCT3, CCT5, CCT7 |
| GO:BP regulation of protein localization to Cajal body | 0.00273 | CCT3, CCT5, CCT7 |
| GO:BP positive regulation of protein localization to Cajal body | 0.00273 | CCT3, CCT5, CCT7 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 0.00273 | CCT3, CCT5, CCT7 |

### STRING and hu.MAP

The best-established relationships are the CCT core connections: CCT3, CCT5, and CCT7 form a tightly supported STRING subnetwork and are jointly present in every listed hu.MAP complex (hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). These hu.MAP complexes include additional CCT subunits and associated factors, showing that the module captures a reproducible portion of the larger CCT or TRiC machinery rather than an isolated gene set. RUVBL2 is connected in STRING to CCT3, CCT5, CCT7, and EFTUD2, linking chaperone machinery with ATP-dependent nuclear remodeling and RNA-related functions. DDX5–MATR3 is a known STRING relationship, and EFTUD2–RUVBL2 is also supported. STRING functional enrichment independently agrees with chaperone, unfolded-protein-binding, telomerase-RNA-localization, ATPase, and nucleotide-binding themes in (15 supplementary STRING terms; within-query FDR 5.77e-05–0.0026), but these are supplementary and do not replace the globally corrected GO evidence. The topology therefore contains a well-known CCT core, a RUVBL2-centered bridge toward nuclear and ATP-dependent processes, and smaller RNA-processing or stress-related attachments.

**STRING interactions (score >= 0.7)**: 8 of 36 gene pairs: CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–RUVBL2 (0.766); CCT5–CCT7 (0.999); CCT5–RUVBL2 (0.705); CCT7–RUVBL2 (0.802); DDX5–MATR3 (0.894); EFTUD2–RUVBL2 (0.793)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Unfolded protein binding, and Chaperone complex (FDR = 5.77e-05, 5 genes); NetworkNeighborAL Chaperone complex, and Prefoldin (FDR = 0.00013, 4 genes); Component Chaperone complex (FDR = 0.00047, 4 genes); COMPARTMENTS Chaperone complex (FDR = 0.0005, 4 genes); Process Positive regulation of telomerase RNA localization to Cajal body (FDR = 0.00056, 4 genes); Function ATP-dependent protein folding chaperone (FDR = 0.00065, 4 genes); Process Positive regulation of telomere maintenance (FDR = 0.00073, 4 genes); Function ATP-dependent activity (FDR = 0.0011, 6 genes); Function ATP hydrolysis activity (FDR = 0.0016, 5 genes); Function Nucleoside-triphosphatase activity (FDR = 0.0016, 6 genes); Pfam TCP-1/cpn60 chaperonin family (FDR = 0.0017, 3 genes); Function Purine ribonucleotide binding (FDR = 0.0024, 8 genes); Function Purine ribonucleoside triphosphate binding (FDR = 0.0024, 8 genes); Function Unfolded protein binding (FDR = 0.0024, 4 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis (FDR = 0.0026, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_07938.1 (CCT5, CCT3, CCT7; 3/23); huMAP3_06559.1 (CCT5, CCT3, CCT7; 3/25); huMAP3_09191.1 (CCT5, CCT3, CCT7; 3/32); huMAP3_10656.1 (CCT5, CCT3, CCT7; 3/36); huMAP3_14584.1 (CCT5, CCT3, CCT7; 3/61)

### Novelty

The module should not be claimed as a wholly new molecular complex. Its central CCT3–CCT5–CCT7 relationships are strongly established by STRING and repeated hu.MAP recovery, and the associated chaperone biology is well known. However, the liver–ovary co-abundance organization may still be a new systems-level observation because it combines a partial CCT core with RUVBL2, DDX5, EFTUD2, MATR3, HSPH1, and CTPS1 in a tissue-pair-specific network. The available evidence supports novelty of the observed cross-tissue co-abundance pattern and its proposed integration of proteostasis with RNA and telomere-related biology, not novelty of the individual interactions. Absence from STRING or hu.MAP would not establish novelty, and the presence of known interactions means that experimental validation and comparison with other tissue-pair modules would be needed before making a stronger claim.

**Hypothesis.** Hypothesis: in liver and ovary, coordinated abundance of a partial CCT/TRiC chaperone core may stabilize proteins required for nuclear RNA handling and telomerase-related processes. CCT3, CCT5, and CCT7 could provide the folding and proteostasis scaffold; RUVBL2 could couple that scaffold to ATP-dependent chromatin, DNA, and telomere-associated remodeling; DDX5 and EFTUD2 could connect it to RNA structure, splicing, and nuclear RNA trafficking; HSPH1 could buffer unfolded-protein stress; and CTPS1 could reflect the nucleotide supply needed for RNA and DNA synthesis. Under this model, the shared liver–ovary module represents coordinated maintenance of RNA-processing and genome-associated protein systems rather than a single dedicated tissue function. The reproductive-cell annotations may indicate cell-state modulation of this machinery, but they do not by themselves prove a fertilization-specific mechanism.

### Important genes

#### CCT3

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.82), RUVBL2 (0.82), DDX5 (0.81), CCT5 (0.81); STRING partners: CCT5 (0.999), CCT7 (0.999), RUVBL2 (0.766)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver, ovary
- **hu.MAP 3.0**: huMAP3_01951.1, huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a highly connected module member and one of the core CCT/TRiC subunits. It appears across the full set of primary chaperone, Cajal-body, telomerase-RNA-localization, telomere-maintenance, protein-folding, and DNA-related annotations (49 globally significant GO/KEGG terms, q_global 4.53e-05–0.0476; see the table). Its strong STRING links to CCT5, CCT7, and RUVBL2 and its presence in all listed hu.MAP complexes (hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) make it a structural anchor. The supplied literature record is substantial, and disease associations include neurodevelopmental and neurodegenerative conditions.
- **Conclusion**: Established evidence supports CCT3 as a central component of the CCT chaperone machinery and a key marker of the module’s proteostasis interpretation. Its specific causal role in telomerase RNA localization within liver or ovary remains a hypothesis because the enrichment evidence is based on gene-set annotation and co-abundance rather than direct tissue-specific perturbation.

#### CCT5

- **Related proteins** (co-abundance neighbors): DDX5 (0.86), CCT7 (0.85), EFTUD2 (0.82), CCT3 (0.81); STRING partners: CCT3 (0.999), CCT7 (0.999), RUVBL2 (0.705)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_01951.1, huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 has the strongest network centrality profile in the supplied ordering and connects the CCT core with DDX5 and EFTUD2 as well as RUVBL2. It participates in every primary enrichment term (49 globally significant GO/KEGG terms, q_global 4.53e-05–0.0476; see the table), is present in all hu.MAP complexes (hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1), and is detected in ovary. Its established role is ATP-dependent folding of proteins such as actin and tubulin, and its disease associations include hereditary sensory and autonomic neuropathy with spastic paraplegia and neurodegenerative disease. It also has a substantial literature record.
- **Conclusion**: Established evidence identifies CCT5 as a central chaperone subunit and a plausible driver of the module’s folding and protein-stabilization signal. A direct role for CCT5 in telomere maintenance or reproductive-cell recognition is not established by this module and should remain a hypothesis.

#### CCT7

- **Related proteins** (co-abundance neighbors): CCT5 (0.85); STRING partners: CCT3 (0.999), CCT5 (0.999), RUVBL2 (0.802)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver, ovary
- **hu.MAP 3.0**: huMAP3_01951.1, huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is a core CCT/TRiC component, has very strong STRING support with CCT3 and CCT5, and occurs in every hu.MAP complex listed (hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). It contributes to every primary GO term (49 globally significant GO/KEGG terms, q_global 4.53e-05–0.0476; see the table), including Cajal-body localization, telomerase RNA localization, telomere maintenance, protein folding, and fertilization-related annotations. HPA shows enrichment in early and late spermatogenic cell populations while also showing detection in liver and ovary. Its literature record and disease associations, including hepatocellular carcinoma and neurodegenerative disease, provide additional biological context.
- **Conclusion**: Established evidence supports CCT7 as a conserved chaperone-core marker with possible reproductive-cell modulation. The sperm–egg and telomerase interpretations are biologically plausible but not demonstrated as direct CCT7 functions in these tissues.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): DDX5 (0.84), CCT3 (0.82), HSPH1 (0.81); STRING partners: CCT3 (0.766), CCT5 (0.705), CCT7 (0.802), EFTUD2 (0.793)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 is a highly connected bridge between the CCT group, DDX5, EFTUD2, and HSPH1. It is represented in primary terms for Cajal-body and nuclear RNA localization, telomere maintenance, chromosome organization, DNA-related processes, protein folding, ATP-dependent activity, and protein stabilization (8 globally significant GO/KEGG terms, q_global 4.53e-05–0.000862; see the table), (GO:BP regulation of chromosome organization; q_global = 0.00289), (GO:BP protein folding; q_global = 0.00406), (GO:BP telomere maintenance; q_global = 0.00705), (GO:BP telomere organization; q_global = 0.00848), (4 globally significant GO/KEGG terms, q_global 0.0102–0.022; see the table), and (GO:BP protein stabilization; q_global = 0.0384). Its established ATPase and DNA-helicase activities, together with annotations for DNA repair, recombination, replication, snoRNP assembly, and telomere maintenance, make it the strongest mechanistic bridge beyond the CCT core. HPA reports testis tissue enhancement and enrichment across spermatogenic and ciliated cell types.
- **Conclusion**: Established evidence supports RUVBL2 as an ATP-dependent nuclear remodeling and genome-maintenance factor that connects the module’s chaperone and RNA-associated signals. Its testis-associated expression may explain part of the reproductive annotation, but the shared liver–ovary module does not establish a tissue-specific reproductive role.

#### DDX5

- **Related proteins** (co-abundance neighbors): CCT5 (0.86), RUVBL2 (0.84), EFTUD2 (0.82), CCT3 (0.81); STRING partners: MATR3 (0.894)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in liver, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 is among the most connected module members and links CCT-associated genes with EFTUD2 and RUVBL2. Its primary annotations are concentrated in ATP-dependent and ribonucleotide-related functions (GO:MF ATP-dependent activity; q_global = 0.0102), (GO:MF ATP hydrolysis activity; q_global = 0.022), (4 globally significant GO/KEGG terms, q_global 0.0232–0.0256; see the table), and (GO:MF pyrophosphatase activity; q_global = 0.0361) (GO:MF hydrolase activity, acting on acid anhydrides; q_global = 0.0361) (GO:MF hydrolase activity, acting on acid anhydrides, in phosphorus-containing anhydrides; q_global = 0.0361). The supplied functional description establishes roles in RNA-structure remodeling, transcriptional coregulation, alternative splicing, and small noncoding-RNA processing. Its nuclear localization in nucleoplasm and nucleoli, strong STRING relationship with MATR3, broad disease associations, and extensive literature record make it an important RNA-processing interface.
- **Conclusion**: Established evidence supports DDX5 as the module’s RNA-helicase and nuclear RNA-processing component. Its connection to the CCT core suggests coordinated RNA and protein homeostasis, but a direct role in telomerase RNA localization is a hypothesis rather than a demonstrated function here.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): MATR3 (0.83), CCT5 (0.82), DDX5 (0.82), CCT3 (0.82); STRING partners: RUVBL2 (0.793)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 is highly connected within the co-abundance graph and links DDX5, MATR3, CCT proteins, and RUVBL2. Its primary annotations concern purine-ribonucleotide binding, nucleotide-triphosphate-related activity, and hydrolase activity (4 globally significant GO/KEGG terms, q_global 0.0232–0.0256; see the table) and (GO:MF pyrophosphatase activity; q_global = 0.0361) (GO:MF hydrolase activity, acting on acid anhydrides; q_global = 0.0361) (GO:MF hydrolase activity, acting on acid anhydrides, in phosphorus-containing anhydrides; q_global = 0.0361). Independently, its established function as a spliceosomal GTPase places it in precursor-mRNA processing and spliceosome remodeling. It is detected in both liver and ovary, has a strong disease association with mandibulofacial dysostosis-microcephaly syndrome, and has a substantial literature record.
- **Conclusion**: Established evidence supports EFTUD2 as a spliceosomal and nucleotide-dependent RNA-processing component that broadens the module beyond chaperone biology. Its inferred coordination with CCT and RUVBL2 is supported by network structure and STRING linkage, but its role in telomere or Cajal-body regulation remains hypothetical.

## Module 4

**Tissue pair**: liver and ovary  
**Genes (12)**: ADAR, EIF3F, FNTA, NUP160, PRPF31, PSMC6, PSMC4, PSMC2, PSMD13, UPF1, U2SURP, QARS1

### Function

The strongest interpretation is a conserved intracellular proteostasis module centered on the nineteen-S regulatory particle of the twenty-six-S proteasome. The primary enrichment evidence is unusually coherent: PSMC2, PSMC4, PSMC6 and PSMD13 jointly support the regulatory-particle, accessory-complex, proteasome-activating, proteasome-complex and proteolytic-complex terms (9 globally significant GO/KEGG terms, q_global 0.000134–0.0204; see the table), as well as the KEGG proteasome pathway (KEGG Proteasome - Homo sapiens (human); q_global = 0.00489). PSMC2, PSMC4 and PSMC6 are ATPase components of the regulatory particle, whereas PSMD13 is a non-ATPase component. The remaining genes connect this proteasome core to RNA handling, translation, nucleocytoplasmic transport, protein modification and protein quality control. The all-gene protein-complex enrichment (GO:CC protein-containing complex; q_global = 0.0276) and intracellular-complex enrichment (GO:CC intracellular protein-containing complex; q_global = 0.0359) are consistent with a module assembled from multiple intracellular macromolecular systems rather than a single complete complex. The spinocerebellar ataxia and Epstein–Barr virus pathway terms (KEGG Spinocerebellar ataxia - Homo sapiens (human); q_global = 0.0167), (KEGG Epstein-Barr virus infection - Homo sapiens (human); q_global = 0.0341) should be interpreted as pathway-overlap annotations driven by the proteasome genes, not as evidence that the module specifically represents either disease or infection. STRING RNA-metabolism enrichment (STRING RCTM Metabolism of RNA; within-query FDR = 1.14e-05) is supportive but supplementary; it does not replace the primary proteasome evidence.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It is also unlikely to be a blood-cell contamination signature, because nearly all genes have low immune-cell specificity and UPF1 is not detected in immune cells. The genes have low tissue specificity and are detected in both liver and ovary, which supports a broadly expressed intracellular program rather than a tissue-restricted secretory product. HPA does show cell-type-enhanced signals in several specialized cell types, especially syncytiotrophoblasts and germ-cell or epithelial populations, but these are distributed across different genes and do not establish a shared liver–ovary cell type. The module may therefore reflect conserved cellular proteostasis and RNA-processing activity, while sample composition or shared proliferative or stress-related states could still influence its abundance.

**GO/KEGG enrichment**: 12 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC proteasome regulatory particle | 0.000134 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:CC proteasome accessory complex | 0.000134 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:MF proteasome-activating activity | 0.00195 | PSMC2, PSMC4, PSMC6 |
| KEGG Proteasome - Homo sapiens (human) | 0.00489 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:CC proteasome regulatory particle, base subcomplex | 0.00592 | PSMC2, PSMC4, PSMC6 |
| GO:CC proteasome complex | 0.00856 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:CC endopeptidase complex | 0.0167 | PSMC2, PSMC4, PSMC6, PSMD13 |
| KEGG Spinocerebellar ataxia - Homo sapiens (human) | 0.0167 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:CC peptidase complex | 0.0204 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:CC protein-containing complex | 0.0276 | ADAR, EIF3F, FNTA, NUP160, PRPF31, PSMC2, PSMC4, PSMC6, PSMD13, QARS1, U2SURP, UPF1 |
| KEGG Epstein-Barr virus infection - Homo sapiens (human) | 0.0341 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:CC intracellular protein-containing complex | 0.0359 | FNTA, PSMC2, PSMC4, PSMC6, PSMD13, QARS1 |

### STRING and hu.MAP

STRING provides strong known support for a proteasome submodule: PSMC2, PSMC4, PSMC6 and PSMD13 are mutually connected with very high-confidence relationships, and the same quartet drives the STRING proteasome regulatory-particle enrichments (STRING Component Proteasome regulatory particle; within-query FDR = 0.00033) (STRING COMPARTMENTS Proteasome regulatory particle; within-query FDR = 0.00035) (STRING NetworkNeighborAL Proteasome regulatory particle, and Proteasome alpha-type subunit; within-query FDR = 0.0013). STRING also reports a strong ADAR–UPF1 relationship, while the module contains the weaker EIF3F–PSMD13 relationship. The STRING pathway results linking the quartet to RNA metabolism, apoptosis, NF-kappaB signaling, hypoxia-related processing, antigen presentation, cytokine signaling and cell-cycle protein degradation (STRING RCTM Metabolism of RNA; within-query FDR = 1.14e-05), (11 supplementary STRING terms; within-query FDR 0.0022–0.0022) are useful context but are supplementary and not globally corrected evidence. hu.MAP independently places PSMC2, PSMC4, PSMC6 and PSMD13 in multiple proteasome-containing complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1), showing that the proteasome signal corresponds to known physical complex membership. ADAR and UPF1 co-occur in an RNA-associated hu.MAP complex (hu.MAP huMAP3_10625.1). Thus, the module contains a firmly established proteasome core plus a less completely connected RNA-processing and transport neighborhood; it should not be treated as one experimentally established unified complex.

**STRING interactions (score >= 0.7)**: 8 of 66 gene pairs: ADAR–UPF1 (0.983); EIF3F–PSMD13 (0.705); PSMC2–PSMC4 (0.999); PSMC2–PSMC6 (0.999); PSMC2–PSMD13 (0.999); PSMC4–PSMC6 (0.999); PSMC4–PSMD13 (0.999); PSMC6–PSMD13 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Metabolism of RNA (FDR = 1.14e-05, 9 genes); Component Proteasome regulatory particle (FDR = 0.00033, 4 genes); COMPARTMENTS Proteasome regulatory particle (FDR = 0.00035, 4 genes); NetworkNeighborAL Proteasome regulatory particle, and Proteasome alpha-type subunit (FDR = 0.0013, 4 genes); RCTM Apoptosis (FDR = 0.0022, 5 genes); RCTM Activation of NF-kappaB in B cells (FDR = 0.0022, 4 genes); RCTM Oxygen-dependent proline hydroxylation of Hypoxia-inducible Factor Alpha (FDR = 0.0022, 4 genes); RCTM ER-Phagosome pathway (FDR = 0.0022, 4 genes); RCTM Cross-presentation of soluble exogenous antigens (endosomes) (FDR = 0.0022, 4 genes); RCTM Cytokine Signaling in Immune system (FDR = 0.0022, 6 genes); RCTM Host Interactions of HIV factors (FDR = 0.0022, 5 genes); RCTM Autodegradation of Cdh1 by Cdh1:APC/C (FDR = 0.0022, 4 genes); RCTM SCF-beta-TrCP mediated degradation of Emi1 (FDR = 0.0022, 4 genes); RCTM APC/C:Cdc20 mediated degradation of Securin (FDR = 0.0022, 4 genes); RCTM APC/C:Cdh1 mediated degradation of Cdc20 and other APC/C:Cdh1 targeted proteins in late mitosis/early G1 (FDR = 0.0022, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05064.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/31); huMAP3_09656.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/64); huMAP3_13725.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/69); huMAP3_10625.1 (ADAR, UPF1; 2/57)

### Novelty

The conserved liver–ovary co-abundance pattern may be a new systems-level observation, but the underlying biology is not wholly new. The proteasome relationships among PSMC2, PSMC4, PSMC6 and PSMD13 are already strongly represented in STRING and hu.MAP, and the ADAR–UPF1 relationship is also known. Consequently, this dataset does not establish a novel proteasome complex or a new direct interaction. Its potential novelty lies instead in the reproducible sharing of this proteostasis-centered expression module between liver and ovary, and in the coordinated association of the proteasome core with RNA surveillance, splicing, transport, translation and prenylation-related genes. That interpretation remains a hypothesis until independently replicated across cohorts and tested against cell composition, disease state, stress and proliferation covariates. Absence of some module relationships from STRING or hu.MAP is not evidence of novelty.

**Hypothesis.** Hypothesis: the shared module represents a coordinated intracellular quality-control state in which proteasome regulatory-particle abundance is coupled to RNA maturation and surveillance. Proteasome activity could remove damaged or improperly regulated proteins, while ADAR, UPF1, U2SURP, PRPF31 and NUP160 support RNA editing, processing, export and decay; EIF3F and QARS1 could connect this state to translation, and FNTA could connect it to signaling-protein maturation. In liver and ovary, a common metabolic, developmental or proteotoxic burden could therefore produce co-abundance of these systems. The network and database evidence establish the proteasome core and several known molecular relationships, but they do not demonstrate that the peripheral genes are physically assembled with the proteasome or that one regulates the other. Direct perturbation and co-immunoprecipitation, together with RNA-surveillance and proteasome-activity assays, would be needed to test this mechanism.

### Important genes

#### PSMC2

- **Related proteins** (co-abundance neighbors): PSMD13 (0.87), U2SURP (0.85), PSMC4 (0.85), EIF3F (0.84), ADAR (0.81), PSMC6 (0.80); STRING partners: PSMC4 (0.999), PSMC6 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in liver, ovary
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 has the strongest network position in the module and connects the proteasome quartet to U2SURP, EIF3F and ADAR in addition to the other proteasome members. It is an ATPase subunit of the twenty-six-S proteasome regulatory particle and participates in the globally supported proteasome terms (12 globally significant GO/KEGG terms, q_global 0.000134–0.0359; see the table). Its broad liver and ovary detection, extensive literature, and disease associations involving hematologic malignancy, neoplasm, HIV-related disease and amyloidosis make it a central anchor for interpretation.
- **Conclusion**: Established evidence supports PSMC2 as a central proteasome-regulatory component and the principal network bridge between the proteasome core and peripheral module genes. It is plausible, but not established, that variation in PSMC2 abundance helps coordinate the broader RNA and translation-related neighborhood.

#### PSMC4

- **Related proteins** (co-abundance neighbors): PSMC2 (0.85), PSMD13 (0.82), PRPF31 (0.82), FNTA (0.81); STRING partners: PSMC2 (0.999), PSMC6 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in liver, ovary
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 4. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.603); mantle cell lymphoma (0.542); neoplasm (0.519); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1065
- **Why important**: PSMC4 is a regulatory-particle ATPase with strong connectivity to the proteasome quartet and additional links to PRPF31 and FNTA. It appears in every primary GO and KEGG term listed for the proteasome-centered module (12 globally significant GO/KEGG terms, q_global 0.000134–0.0359; see the table), in the STRING proteasome and supplementary pathway results, and in all three proteasome hu.MAP complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). It is broadly detected in liver and ovary, has extensive literature, and is associated with malignancy, HIV-related disease and amyloidosis.
- **Conclusion**: Established evidence identifies PSMC4 as a core and well-supported proteasome component. Its links to splicing and prenylation genes are co-abundance relationships in this module, not proof of direct mechanistic coupling.

#### PSMC6

- **Related proteins** (co-abundance neighbors): PSMD13 (0.84), PSMC2 (0.80); STRING partners: PSMC2 (0.999), PSMC4 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in liver, ovary
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 6. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.606); mantle cell lymphoma (0.542); neoplasm (0.528); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 748
- **Why important**: PSMC6 is another regulatory-particle ATPase and is tightly embedded in the known proteasome subnetwork through PSMC2, PSMC4 and PSMD13. It supports the primary proteasome terms (12 globally significant GO/KEGG terms, q_global 0.000134–0.0359; see the table), is present in the proteasome complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1), and has HPA protein detection in both tissues. Its annotations include proteasomal degradation, oxidative-stress response and ER-associated degradation, while its disease associations and substantial literature make it biologically interpretable beyond simple network membership.
- **Conclusion**: Established evidence supports PSMC6 as part of the module's proteasome engine and as a plausible marker of protein-quality-control demand. Whether it specifically mediates the liver–ovary conservation or merely tracks the abundance of the shared proteasome is unresolved.

#### PSMD13

- **Related proteins** (co-abundance neighbors): PSMC2 (0.87), PSMC6 (0.84), PSMC4 (0.82); STRING partners: EIF3F (0.705), PSMC2 (0.999), PSMC4 (0.999), PSMC6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 is the non-ATPase proteasome regulatory-particle member that completes the central quartet. It participates in the primary regulatory-particle, proteasome and peptidase-complex terms (GO:CC proteasome regulatory particle; q_global = 0.000134), (GO:CC proteasome accessory complex; q_global = 0.000134), (KEGG Proteasome - Homo sapiens (human); q_global = 0.00489), (7 globally significant GO/KEGG terms, q_global 0.00856–0.0359; see the table), in the strongest STRING proteasome relationships, and in the proteasome hu.MAP complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). It has a central position within the proteasome subgraph, a known link to EIF3F, broad disease associations including malignancy, neurodegeneration and HIV-related disease, and a substantial literature.
- **Conclusion**: Established evidence makes PSMD13 a core structural marker of the proteasome portion of the module. Its co-abundance with EIF3F may indicate a connection to translation or protein quality control, but the available evidence does not establish a direct functional bridge.

#### ADAR

- **Related proteins** (co-abundance neighbors): PSMC2 (0.81); STRING partners: UPF1 (0.983)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in liver, ovary
- **hu.MAP 3.0**: huMAP3_10625.1
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR represents the RNA-processing side of the module. It catalyzes adenosine-to-inosine RNA editing, is annotated for RNA processing and antiviral response, connects to PSMC2 in the co-abundance graph, and has a strong STRING relationship with UPF1. It also participates with UPF1 in the RNA-associated hu.MAP complex (hu.MAP huMAP3_10625.1). ADAR has the most extensive literature among the module genes and strong disease associations involving Aicardi–Goutieres syndrome, dyschromatosis and ADAR-related interferonopathy.
- **Conclusion**: Established evidence supports ADAR as an RNA-editing and immune-response-related component that is associated with the module's proteostasis core and RNA-surveillance branch. The hypothesis that ADAR-dependent RNA quality control is coordinated with proteasome activity in liver and ovary remains to be tested.

#### UPF1

- **Related proteins** (co-abundance neighbors): U2SURP (0.83), NUP160 (0.81); STRING partners: ADAR (0.983)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in liver, ovary
- **hu.MAP 3.0**: huMAP3_10625.1
- **Function (MyGene.info)**: UPF1 RNA helicase and ATPase. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons.…
- **Diseases (Open Targets)**: Intellectual disability (0.437); Global developmental delay (0.426); High anterior hairline (0.425); Frontal bossing (0.425); Hypertelorism (0.425)
- **Europe PMC papers**: 4252
- **Why important**: UPF1 is a central RNA-surveillance factor involved in nonsense-mediated decay, mRNA export and translational termination control. It connects U2SURP and NUP160 in the module, has a strong STRING relationship with ADAR, and participates in the RNA-associated hu.MAP complex (hu.MAP huMAP3_10625.1). It is broadly detected in liver and ovary, has extensive literature, and is associated with developmental and intellectual-disability phenotypes. Its inclusion gives the module a biologically specific RNA-quality-control interpretation beyond generic complex enrichment.
- **Conclusion**: Established evidence supports UPF1 as the principal RNA surveillance and mRNA quality-control marker in the module. Its relationship to the proteasome quartet is indirect in the available evidence, so a shared cellular quality-control state is more defensible than a claimed direct UPF1–proteasome complex.

## Module 5

**Tissue pair**: liver and ovary  
**Genes (5)**: KRT10, KRT9, KRT2, KRT1, KRT5

### Function

This is a keratin intermediate-filament module. The primary evidence is exceptionally coherent: (GO:CC keratin filament; q_global = 1.56e-07) through (GO:BP intermediate filament cytoskeleton organization; q_global = 2.5e-06), (GO:CC intermediate filament; q_global = 8.39e-06) through (GO:BP epidermis development; q_global = 8.55e-05), and (GO:BP epithelial cell differentiation; q_global = 0.00153) through (GO:BP tissue development; q_global = 0.0377) link all or nearly all module genes to keratin filaments, intermediate-filament organization, epithelial and epidermal development, keratinocyte differentiation, keratinization, cornified-envelope formation, and structural molecule activity. (KEGG Cadherin signaling - Homo sapiens (human); q_global = 0.00018) additionally supports a cadherin-signaling connection, consistent with epithelial cell adhesion and cytoskeletal organization. The most defensible interpretation is a differentiated keratinized epithelial structural program rather than a liver- or ovary-specific biochemical pathway.

**Cell composition.** The module is strongly tissue- and cell-type restricted rather than broadly expressed or housekeeping-like. HPA associates most members with skin and suprabasal keratinocytes, with KRT5 also associated with basal and other epithelial cells. KRT9 has a distinctive lymphoid-tissue annotation and KRT5 has an immune-cell annotation, but the dominant pattern is epithelial keratin biology. One member is annotated as secreted in other tissues, yet the module is not predominantly composed of plasma or secreted proteins. All module proteins were not detected by HPA in liver or ovary. Thus, in samples labeled as liver and ovary, the shared signal is more plausibly attributable to keratinizing or contaminating epithelial material, a shared epithelial cell component, tissue-interface material, or sample handling effects than to a resident liver–ovary pathway. The data do not by themselves establish which of these explanations applies.

**GO/KEGG enrichment**: 24 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC keratin filament | 1.56e-07 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament organization | 9.47e-07 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament-based process | 2.5e-06 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament cytoskeleton organization | 2.5e-06 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:MF structural constituent of skin epidermis | 3.53e-06 | KRT1, KRT10, KRT2, KRT5 |
| GO:CC intermediate filament | 8.39e-06 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:CC intermediate filament cytoskeleton | 1.25e-05 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| KEGG Cornified envelope formation - Homo sapiens (human) | 3.46e-05 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP skin development | 5.87e-05 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP epidermis development | 8.55e-05 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| KEGG Cadherin signaling - Homo sapiens (human) | 0.00018 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP keratinocyte differentiation | 0.000564 | KRT1, KRT10, KRT2, KRT5 |
| GO:BP epidermal cell differentiation | 0.000945 | KRT1, KRT10, KRT2, KRT5 |
| GO:BP epithelial cell differentiation | 0.00153 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP keratinization | 0.0018 | KRT1, KRT2, KRT5 |

### STRING and hu.MAP

STRING supports a pre-existing keratin interaction system: the listed high-confidence relationships connect KRT1, KRT10, KRT2, and KRT5, while KRT9 is connected in the module network but has no STRING partners listed in the fact sheet. STRING functional categories (STRING Keyword Keratin; within-query FDR = 3.26e-08) through (STRING RCTM Formation of the cornified envelope; within-query FDR = 6.34e-07) independently support keratin and intermediate-filament biology, and (STRING DISEASES Epidermolytic hyperkeratosis; within-query FDR = 1.94e-06) through (STRING PMID (2019) Keratin 9 L164P mutation in a Chinese pedigree with epidermolytic palmoplantar keratoderma, cytokeratin analysis, and literature review.; within-query FDR = 6.04e-06) connect the module with epidermolytic disease, cornified-envelope formation, wound-related keratin biology, and palmoplantar keratoderma literature. These STRING results validate that the co-abundance pattern recapitulates known keratin relationships, but they are supplementary rather than globally corrected enrichment evidence. No hu.MAP complex contains the required multi-member representation. The absence of a hu.MAP complex does not contradict the module, because keratin filaments can be represented as interaction networks rather than as one stable, curated multiprotein complex.

**STRING interactions (score >= 0.7)**: 6 of 10 gene pairs: KRT1–KRT10 (0.999); KRT1–KRT2 (0.956); KRT1–KRT5 (0.923); KRT10–KRT2 (0.904); KRT10–KRT5 (0.793); KRT2–KRT5 (0.871)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Keratin (FDR = 3.26e-08, 5 genes); Component Keratin filament (FDR = 4.07e-08, 5 genes); SMART Intermediate filament protein (FDR = 4.21e-08, 5 genes); COMPARTMENTS Keratin filament (FDR = 4.31e-08, 5 genes); Keyword Intermediate filament (FDR = 6.31e-08, 5 genes); InterPro Intermediate filament protein, conserved site (FDR = 2.47e-07, 5 genes); InterPro Intermediate filament, rod domain (FDR = 2.47e-07, 5 genes); RCTM Formation of the cornified envelope (FDR = 6.34e-07, 5 genes); DISEASES Epidermolytic hyperkeratosis (FDR = 1.94e-06, 4 genes); PMID (2025) Mass spectrometric detection of keratins in tear fluid. (FDR = 6.04e-06, 5 genes); PMID (2023) Key Factors in the Complex and Coordinated Network of Skin Keratinization: Their Significance and Involvement in Common Skin Conditions. (FDR = 6.04e-06, 5 genes); PMID (2022) A metatranscriptomic approach to explore longitudinal tissue specimens from non-healing diabetes related foot ulcers. (FDR = 6.04e-06, 5 genes); PMID (2022) Palmoplantar Keratoderma: A Molecular Genetic Analysis of Family Cases. (FDR = 6.04e-06, 5 genes); PMID (2021) Keratin Biomaterials in Skin Wound Healing, an Old Player in Modern Medicine: A Mini Review. (FDR = 6.04e-06, 5 genes); PMID (2019) Keratin 9 L164P mutation in a Chinese pedigree with epidermolytic palmoplantar keratoderma, cytokeratin analysis, and literature review. (FDR = 6.04e-06, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be claimed as a newly discovered keratin mechanism. Its central biology is already well established by the globally corrected GO and KEGG terms, the high-confidence STRING relationships, the protein annotations, disease associations, and substantial literature for the individual keratins. What may be novel is the observation that this particular coordinated keratin signature was recovered as a conserved co-abundance module in the liver–ovary comparison. That observation remains provisional because all members are absent by HPA protein detection in both named tissues and are strongly associated with skin or epithelial cell types. Establishing novelty would require replication in independent cohorts, assessment of epithelial contamination and tissue composition, and comparison with previously reported cross-tissue co-abundance modules. Absence from STRING or hu.MAP alone is not evidence of novelty.

**Hypothesis.** Hypothesis: the shared liver–ovary module reflects coordinated abundance of keratinizing epithelial material, potentially from epithelial interfaces, minor epithelial populations, tissue fragments, or sample contamination, rather than a conserved intracellular program intrinsic to hepatocytes and ovarian cells. KRT5 may represent a basal epithelial component, whereas KRT1, KRT10, KRT2, and KRT9 may represent more differentiated or specialized keratin states. Their co-abundance could therefore arise from a continuum of epithelial differentiation in the sampled material. This hypothesis predicts that the module will track epithelial-cell proportion and epithelial marker abundance, and that it will weaken after cell-composition adjustment or careful exclusion of contaminating tissue. It requires direct testing and is not established by the enrichment results alone.

### Important genes

#### KRT1

- **Related proteins** (co-abundance neighbors): KRT10 (0.89), KRT9 (0.88), KRT2 (0.80); STRING partners: KRT10 (0.999), KRT2 (0.956), KRT5 (0.923)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 is a central network member with strong links to KRT10, KRT2, and KRT5. It participates in nearly every primary enrichment theme, including keratin filaments, intermediate-filament organization, epidermal differentiation, keratinization, and cornified-envelope biology. It is skin- and suprabasal-keratinocyte enriched, has extensive literature, and is associated with epidermolytic ichthyosis and palmoplantar keratoderma.
- **Conclusion**: Established: KRT1 is a major structural and differentiation-associated keratin in this module and is a strong indicator of keratinizing epithelial material. Hypothesis: its central network position may make it a useful quantitative marker of the module's epithelial structural state.

#### KRT10

- **Related proteins** (co-abundance neighbors): KRT1 (0.89), KRT9 (0.86), KRT2 (0.82); STRING partners: KRT1 (0.999), KRT2 (0.904), KRT5 (0.793)
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 10. This gene encodes a member of the type I (acidic) cytokeratin family, which belongs to the superfamily of intermediate filament (IF) proteins. Keratins are heteropolymeric structural proteins which form the intermediate filament. These filaments, along with actin microfilaments and microtubules, compose the cytoskeleton of epithelial cells. Mutations in this gene are associated with epidermolytic …
- **Diseases (Open Targets)**: epidermolytic hyperkeratosis 2A, autosomal dominant (0.787); epidermolytic ichthyosis (0.772); congenital reticular ichthyosiform erythroderma (0.727); ichthyosis, annular epidermolytic 1 (0.647); annular epidermolytic ichthyosis (0.642)
- **Europe PMC papers**: 2736
- **Why important**: KRT10 is a central network member connected to KRT1, KRT2, and KRT9, and it appears in nearly all primary enrichment themes. Its annotation places it in suprabasal keratinocytes and the differentiated epidermal cytoskeleton. It has a substantial literature and established associations with several epidermolytic and ichthyotic disorders.
- **Conclusion**: Established: KRT10 supports a differentiated suprabasal keratin program and reinforces the interpretation of the module as epithelial structural biology. Hypothesis: coordinated KRT10 and KRT1 abundance may report the degree of epithelial differentiation in the liver–ovary samples.

#### KRT2

- **Related proteins** (co-abundance neighbors): KRT5 (0.88), KRT10 (0.82), KRT1 (0.80); STRING partners: KRT1 (0.956), KRT10 (0.904), KRT5 (0.871)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location Intermediate filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 2. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is expressed largely in the upper spinous layer of epidermal keratinocytes and mutations in this gene …
- **Diseases (Open Targets)**: superficial epidermolytic ichthyosis (0.815); exfoliative ichthyosis (0.358); Palmoplantar hyperkeratosis (0.267); hereditary disease (0.193); Vertigo (0.145)
- **Europe PMC papers**: 7459
- **Why important**: KRT2 is a central network member linked to KRT5, KRT10, and KRT1. It contributes to the primary evidence for epidermis development, keratinization, keratinocyte differentiation, and intermediate filament organization. It is enriched in suprabasal keratinocytes and is associated with epidermolytic and exfoliative ichthyotic disorders.
- **Conclusion**: Established: KRT2 is a differentiated epithelial keratin that strengthens the interpretation of a suprabasal or keratinizing program. Hypothesis: KRT2 may help distinguish a more differentiated epithelial contribution from a predominantly basal epithelial contribution.

#### KRT5

- **Related proteins** (co-abundance neighbors): KRT2 (0.88); STRING partners: KRT1 (0.923), KRT10 (0.793), KRT2 (0.871)
- **HPA**: Group enriched; Group enriched; blood Immune cell enriched; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 5. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the basal layer of the epidermis with family member KRT14. Mutations in t…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 2C, localized (0.768); epidermolysis bullosa simplex 2A, generalized severe (0.761); epidermolysis bullosa simplex 2B, generalized intermediate (0.761); epidermolysis bullosa simplex 2F, with mottled pigmentation (0.729); Dowling-Degos disease 1 (0.697)
- **Europe PMC papers**: 7044
- **Why important**: KRT5 occupies a basal-epithelial position in the annotation and is linked in the network to KRT2, with STRING support for relationships to KRT1 and KRT10. It contributes to primary terms covering keratin filaments, epithelial differentiation, keratinization, and intermediate-filament polymerization. Its extensive literature and associations with epidermolysis bullosa simplex and other epithelial disorders make it an important basal structural marker.
- **Conclusion**: Established: KRT5 anchors the module to basal epithelial and intermediate-filament biology rather than only terminal differentiation. Hypothesis: the joint presence of KRT5 with suprabasal keratins may indicate mixed epithelial states or epithelial turnover in the sampled material.

#### KRT9

- **Related proteins** (co-abundance neighbors): KRT1 (0.88), KRT10 (0.86); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 9. This gene encodes the type I keratin 9, an intermediate filament chain expressed only in the terminally differentiated epidermis of palms and soles. Mutations in this gene cause epidermolytic palmoplantar keratoderma. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: epidermolytic palmoplantar keratoderma, 1 (0.828); palmoplantar keratoderma, epidermolytic (0.682); Localized epidermolytic hyperkeratosis (0.511); Palmoplantar hyperkeratosis (0.456); Palmoplantar keratoderma (0.438)
- **Europe PMC papers**: 773
- **Why important**: KRT9 is the module's more specialized network member: it connects to KRT1 and KRT10 in the module but has no STRING partners listed. Its annotation describes a type one keratin associated with terminally differentiated palm and sole epidermis, and it is strongly linked to epidermolytic palmoplantar keratoderma. It appears in many primary keratin and epithelial terms despite having less literature than the central keratins.
- **Conclusion**: Established: KRT9 adds a specialized terminal-differentiation and disease-associated component to the module. Hypothesis: its presence may indicate a particular epithelial subtype or keratinization state, but the liver–ovary data do not establish that the sampled material originates from a KRT9-specific tissue.
