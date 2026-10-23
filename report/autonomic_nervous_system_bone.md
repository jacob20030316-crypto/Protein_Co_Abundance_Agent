# Conserved co-abundance modules: autonomic_nervous_system and bone

## Module 0

**Tissue pair**: autonomic_nervous_system and bone  
**Genes (20)**: AKAP8, BPNT1, CAPZB, POLD1, EDC4, ERBIN, GDAP1, HDAC1, LRRFIP1, MDC1, MYEF2, NIP7, NUP85, PFDN4, PPME1, POLR2E, SCAMP4, SPTAN1, SYNE2, TCEA1

### Function

The module does not support a single narrowly defined pathway. No GO or KEGG term passed global correction, so there is no globally significant enrichment claim to make from those analyses. STRING functional enrichment was also absent. The gene composition instead suggests a mixed cellular-maintenance program: transcription and RNA polymerase activity through POLR2E and TCEA1; chromatin regulation, DNA replication and damage responses through HDAC1, POLD1 and MDC1; RNA processing and nucleocytoplasmic transport through NIP7, EDC4 and NUP85; and cytoskeletal, membrane-trafficking and mitochondrial functions through SCAMP4, CAPZB, SYNE2, SPTAN1 and GDAP1. The module graph is sparse and contains several small branches rather than a single densely connected functional core. Its most defensible interpretation is therefore a shared co-abundance pattern involving broadly required nuclear, cytoskeletal and intracellular maintenance processes, with a possible neuronal or structural component rather than a demonstrated autonomic-nervous-system–bone-specific mechanism.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, while many are cell-type enhanced across diverse cell types, including glial, epithelial, reproductive and blood-associated cell types. Only a small minority show tissue enhancement, and immune-cell specificity is generally low, although isolated associations include neutrophils, NK cells and eosinophils. This pattern argues against a coherent blood-cell or plasma-protein signature, but it does support caution that shared cell types, ubiquitous cellular programs or differences in cellular composition could contribute to the cross-tissue co-abundance. HPA protein detection is unavailable for both of the named tissues, so tissue-level protein validation cannot be inferred.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING identifies only a small set of known high-confidence relationships within the module: POLR2E with TCEA1, POLR2E with NIP7, and POLR2E with PFDN4. These relationships support a real transcription and RNA or protein-biogenesis substructure, but they do not connect the whole module. STRING functional enrichment is absent, and no hu.MAP complex contains multiple module members. Thus, the network contains some established molecular relationships, especially around POLR2E, but most co-abundance edges are not independently supported as physical interactions. The distinction is important: co-abundance may reflect shared regulation, cell composition or coordinated state rather than direct binding.

**STRING interactions (score >= 0.7)**: 3 of 190 gene pairs: NIP7–POLR2E (0.863); PFDN4–POLR2E (0.861); POLR2E–TCEA1 (0.996)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a new cross-tissue co-abundance pattern, but the available evidence is insufficient to call it a newly discovered molecular complex or pathway. Its novelty is supported only in the limited sense that the complete module is not reproduced by the reported STRING interactions or hu.MAP complexes. That absence does not establish biological novelty, because co-abundance relationships can arise from shared regulation, cell-type mixtures, indirect pathways or technical effects. The lack of globally significant GO or KEGG enrichment and the sparse, partitioned graph further argue for a cautious claim: this is a potentially novel association pattern requiring replication and external validation, not yet a novel mechanism.

**Hypothesis.** Hypothesis: the shared signal may arise from coordinated abundance of a general cellular-maintenance state that combines transcriptional and RNA-processing capacity with genome surveillance, cytoskeletal organization and membrane or mitochondrial support. In neural tissue, GDAP1, SPTAN1 and MYEF2 could make the pattern more visible in neuronal or glial populations; in bone, the same broad intracellular program could be contributed by resident stromal, vascular or other nonsecretory cells. SCAMP4 may link membrane trafficking to the nuclear and cytoskeletal branches through its position in the co-abundance graph. This hypothesis predicts that the module will replicate more strongly when comparable cell types or cellular states are matched across tissues, and that it will not necessarily correspond to a single physical complex.

### Important genes

#### SCAMP4

- **Related proteins** (co-abundance neighbors): LRRFIP1 (0.86), TCEA1 (0.85), PPME1 (0.84), PFDN4 (0.83), POLR2E (0.82), CAPZB (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: secretory carrier membrane protein 4. Secretory carrier membrane proteins (SCAMPs) are widely distributed integral membrane proteins implicated in membrane trafficking. Most SCAMPs (e.g., SCAMP1; MIM 606911) have N-terminal cytoplasmic NPF (arg-pro-phe) repeats, 4 central transmembrane regions, and a short C-terminal cytoplasmic tail. These SCAMPs likely have a role in endocytosis that is mediated by their NPF repeats. Other SCAMPs, s…
- **Diseases (Open Targets)**: neurodegenerative disease (0.550); intellectual disability-strabismus syndrome (0.514); hereditary disease (0.193); microcephaly (0.111); central nervous system cancer (0.021)
- **Europe PMC papers**: 145
- **Why important**: SCAMP4 has the strongest network position in the module and connects membrane-trafficking biology to several otherwise separated branches, including TCEA1, PFDN4, POLR2E, PPME1, LRRFIP1 and CAPZB. Its annotation supports a role in exocytosis and protein transport, while HPA places it in the Golgi apparatus and vesicles and identifies ciliated-cell enhancement. Its disease associations include neurodegenerative disease and neurodevelopmental conditions, and its literature volume is moderate relative to the module.
- **Conclusion**: Established evidence supports SCAMP4 as a network hub with a membrane-trafficking role. Its position makes it an important integrator candidate, but the absence of global enrichment and direct STRING partners means that a causal role in the shared autonomic-nervous-system–bone pattern remains hypothetical.

#### GDAP1

- **Related proteins** (co-abundance neighbors): SPTAN1 (0.85), NIP7 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ganglioside induced differentiation associated protein 1. This gene encodes a member of the ganglioside-induced differentiation-associated protein family, which may play a role in a signal transduction pathway during neuronal development. Mutations in this gene have been associated with various forms of Charcot-Marie-Tooth Disease and neuropathy. Two transcript variants encoding different isoforms and a noncoding variant have been identified for this gen…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2K (0.833); Charcot-Marie-Tooth disease type 4A (0.803); Charcot-Marie-Tooth disease recessive intermediate A (0.784); autosomal dominant Charcot-Marie-Tooth disease type 2K (0.664); Charcot-Marie-Tooth disease (0.631)
- **Europe PMC papers**: 1052
- **Why important**: GDAP1 links the neuronal and structural parts of the graph through SPTAN1 and NIP7. It is tissue enhanced in brain, cell-type enhanced in glial and neuronal populations, localized to mitochondria, and annotated for mitochondrial fission and fusion. Its disease associations are particularly strong for Charcot–Marie–Tooth disease and related neuropathies, and it has substantial literature support.
- **Conclusion**: Established evidence supports GDAP1 as a mitochondrial and peripheral-neural biology marker with disease relevance. It is a plausible contributor to the autonomic-nervous-system side of the module, but its relevance to bone and the full shared module is not established by the supplied data.

#### POLR2E

- **Related proteins** (co-abundance neighbors): SCAMP4 (0.82); STRING partners: NIP7 (0.863), PFDN4 (0.861), TCEA1 (0.996)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase II, I and III subunit E. This gene encodes the fifth largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. This subunit is shared by the other two DNA-directed RNA polymerases and is present in two-fold molar excess over the other polymerase subunits. An interaction between this subunit and a hepatitis virus transactivating protein has been demonstrated, suggesting …
- **Diseases (Open Targets)**: HIV infectious disease (0.600); neurodegenerative disease (0.461); Orthomyxoviridae infectious disease (0.370); dengue disease (0.370); acrocephalosyndactyly (0.370)
- **Europe PMC papers**: 519
- **Why important**: POLR2E is the central member of the module's only clearly supported STRING interaction cluster, with known links to TCEA1, NIP7 and PFDN4. It is a shared subunit of DNA-dependent RNA polymerases and is annotated for transcription initiation and elongation. Its broad tissue profile is compatible with a general cellular program, and its disease associations include viral infection, neurodevelopmental disease and other disorders.
- **Conclusion**: Established evidence supports POLR2E as a transcriptional machinery component and as the best-supported molecular bridge in the module. It is more likely to mark a broadly active cellular state than a tissue-specific mechanism; any role in coordinating the other branches is a hypothesis.

#### POLD1

- **Related proteins** (co-abundance neighbors): BPNT1 (0.95), EDC4 (0.87), HDAC1 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA polymerase delta 1, catalytic subunit. This gene encodes the 125-kDa catalytic subunit of DNA polymerase delta. DNA polymerase delta possesses both polymerase and 3' to 5' exonuclease activity and plays a critical role in DNA replication and repair. Alternatively spliced transcript variants have been observed for this gene, and a pseudogene of this gene is located on the long arm of chromosome 6. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: mandibular hypoplasia-deafness-progeroid syndrome (0.768); non-small cell lung carcinoma (0.690); acute lymphoblastic leukemia (0.671); colorectal cancer (0.670); acute myeloid leukemia (0.659)
- **Europe PMC papers**: 3886
- **Why important**: POLD1 connects BPNT1, EDC4 and HDAC1 in a nuclear branch involving DNA replication, repair, RNA decay and chromatin regulation. It encodes the catalytic subunit of DNA polymerase delta, with polymerase and proofreading functions, and is associated with developmental syndromes and several cancers. Its extensive literature makes its molecular function unusually well established within this module.
- **Conclusion**: Established evidence supports POLD1 as a genome-replication and DNA-repair factor. Its inclusion is consistent with a cellular stress, proliferation or repair state, but the module data do not show that DNA repair is the dominant shared function.

#### HDAC1

- **Related proteins** (co-abundance neighbors): POLD1 (0.87), ERBIN (0.86), LRRFIP1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: histone deacetylase 1. Histone acetylation and deacetylation, catalyzed by multisubunit complexes, play a key role in the regulation of eukaryotic gene expression. The protein encoded by this gene belongs to the histone deacetylase/acuc/apha family and is a component of the histone deacetylase complex. It also interacts with retinoblastoma tumor-suppressor protein and this complex is a key element in the control of cell…
- **Diseases (Open Targets)**: neoplasm (0.573); primary cutaneous T-cell non-Hodgkin lymphoma (0.568); plasma cell myeloma (0.567); T-cell non-Hodgkin lymphoma (0.521); peripheral T-cell lymphoma, not otherwise specified (0.518)
- **Europe PMC papers**: 29753
- **Why important**: HDAC1 connects POLD1, ERBIN and LRRFIP1 and provides a chromatin-regulatory link between the nuclear and signaling-associated branches. It is a component of histone deacetylase complexes involved in transcriptional regulation, chromatin organization and cell differentiation. It has the largest literature volume among the highlighted genes and extensive cancer-related disease associations.
- **Conclusion**: Established evidence supports HDAC1 as a central chromatin and transcriptional regulator. It is a credible marker of coordinated nuclear regulation, but its high ubiquity and broad disease literature reduce its specificity for this cross-tissue module.

## Module 1

**Tissue pair**: autonomic_nervous_system and bone  
**Genes (5)**: DDX21, MDH1, PFKM, PHIP, RBM10

### Function

No GO or KEGG term passed global multiple-testing correction, so the module has no globally significant pathway annotation. The gene composition nevertheless suggests a mixed metabolic and gene-expression program. MDH1 and PFKM support cytosolic redox, malate-aspartate shuttle, glycolytic, and muscle-associated energy metabolism, while RBM10 and DDX21 support RNA processing, ribosome or spliceosome-related regulation, chromatin or transcriptional control, and cellular growth. PHIP adds possible links to insulin-receptor signaling, glucose-transporter regulation in skeletal muscle, chromatin organization, and transcriptional regulation. The co-abundance pattern therefore may reflect coordinated metabolic demand together with RNA and regulatory activity, but this remains an interpretation rather than a globally enriched pathway claim.

**Cell composition.** The module is not dominated by secreted or plasma proteins: the HPA summary reports no secreted genes. It is also unlikely to represent a blood-cell program because every member has low immune-cell specificity and no enriched blood-cell category is reported. Most genes have low tissue specificity, while MDH1 and PFKM show heart-muscle, tongue, or skeletal-muscle enrichment. Several genes have cell-type-enhanced profiles, including cardiomyocytes, myonuclei, Müller glia, keratinocytes, Hofbauer cells, and parietal cells, but the pattern is heterogeneous rather than a single clearly defined cell population. The shared module may therefore reflect broadly expressed intracellular biology combined with muscle-associated metabolic expression, rather than blood contamination or a secreted-protein signal. There is no matching HPA tissue-level protein evidence for either named tissue in the supplied summary.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and no STRING functional-enrichment result was available. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated here as established high-confidence physical interactions or as membership in a known multiprotein complex. The absence of STRING and hu.MAP support does not invalidate the co-abundance module; it indicates that the observed relationships may be expression-level coordination, indirect regulation, tissue or cell-composition coupling, or interactions not represented in those resources.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact cross-tissue co-abundance module appears potentially novel because its internal relationships are not represented by high-confidence STRING interactions or a shared hu.MAP complex, and because no prior database-defined functional module is supplied for these genes. However, database absence alone cannot establish novelty. Several individual gene functions and disease associations are well established, and the metabolic pairing of MDH1 with PFKM is biologically recognizable. The defensible claim is therefore that the particular autonomic-nervous-system and bone co-abundance configuration is a candidate new observation requiring independent replication, preservation of the pattern after cell-composition adjustment, and experimental testing.

**Hypothesis.** Hypothesis: the module represents coordinated adaptation of intracellular energy metabolism and gene-expression control in cells or samples contributing to both autonomic nervous system and bone datasets. PFKM could support glycolytic flux, MDH1 could couple cytosolic redox balance and the malate-aspartate shuttle to energy demand, and RBM10, DDX21, and PHIP could adjust RNA processing, ribosome or transcriptional programs, chromatin state, and growth or signaling responses. A shared muscle-associated or metabolically active cell state could generate the cross-tissue co-abundance pattern. This hypothesis should be tested by replication in independent cohorts, comparison with cell-type proportions, and perturbation of metabolic and RNA-regulatory components.

### Important genes

#### RBM10

- **Related proteins** (co-abundance neighbors): MDH1 (0.92), DDX21 (0.85), PFKM (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 10. This gene encodes a nuclear protein that belongs to a family proteins that contain an RNA-binding motif. The encoded protein associates with hnRNP proteins and may be involved in regulating alternative splicing. Defects in this gene are the cause of the X-linked recessive disorder, TARP syndrome. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Mar 2011].
- **Diseases (Open Targets)**: TARP syndrome (0.787); lung adenocarcinoma (0.629); neurodegenerative disease (0.526); pancreatic adenocarcinoma (0.513); non-small cell lung carcinoma (0.510)
- **Europe PMC papers**: 1601
- **Why important**: RBM10 has the strongest network position in the supplied module and connects the metabolic members MDH1 and PFKM with the RNA helicase DDX21. Its established role as an RNA-binding nuclear protein involved in alternative splicing provides a plausible regulatory bridge between metabolic state and gene-expression control. Its TARP-syndrome association and substantial literature support make it an informative mechanistic anchor, while its low tissue and cell-type specificity argues against interpreting it as a tissue-exclusive marker.
- **Conclusion**: Established evidence supports RBM10 as a broadly expressed nuclear RNA-regulatory protein and as the most central connector in this co-abundance subgraph. It is a plausible integrator of the module, but the data do not establish that RBM10 regulates the other module genes or causes the cross-tissue association.

#### MDH1

- **Related proteins** (co-abundance neighbors): RBM10 (0.92), PFKM (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Centrosome, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: malate dehydrogenase 1. This gene encodes an enzyme that catalyzes the NAD/NADH-dependent, reversible oxidation of malate to oxaloacetate in many metabolic pathways, including the citric acid cycle. Two main isozymes are known to exist in eukaryotic cells: one is found in the mitochondrial matrix and the other in the cytoplasm. This gene encodes the cytosolic isozyme, which plays a key role in the malate-aspartate shuttl…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 88 (0.499); prostate carcinoma (0.455); neurodegenerative disease (0.348); asthma (0.320); Abnormality of the skeletal system (0.295)
- **Europe PMC papers**: 3198
- **Why important**: MDH1 is directly connected to RBM10 and PFKM and contributes a central metabolic link within the module. Its established cytosolic malate dehydrogenase activity, role in the malate-aspartate shuttle, and participation in redox and tricarboxylic-acid-related metabolism provide a concrete biochemical interpretation. Its tissue-enhanced profile in heart muscle and tongue is also consistent with metabolically active muscle-associated contexts, and it has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports MDH1 as a cytosolic metabolic and redox-balance enzyme. The module suggests that its abundance may track glycolytic and regulatory activity across the two tissues, but it does not demonstrate a direct functional interaction with RBM10 or PFKM.

#### PFKM

- **Related proteins** (co-abundance neighbors): MDH1 (0.86), RBM10 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphofructokinase, muscle. Three phosphofructokinase isozymes exist in humans: muscle, liver and platelet. These isozymes function as subunits of the mammalian tetramer phosphofructokinase, which catalyzes the phosphorylation of fructose-6-phosphate to fructose-1,6-bisphosphate. Tetramer composition varies depending on tissue type. This gene encodes the muscle-type isozyme. Mutations in this gene have been associated with g…
- **Diseases (Open Targets)**: glycogen storage disease VII (0.819); disorder of glycogen metabolism (0.372); peroxisome biogenesis disorder (0.333); neurodegenerative disease (0.319); anemia (phenotype) (0.288)
- **Europe PMC papers**: 2506
- **Why important**: PFKM is connected to MDH1 and RBM10 and is the clearest muscle-associated metabolic member. It encodes the muscle-type phosphofructokinase isozyme, a core glycolytic enzyme, and its HPA profile is group-enriched in skeletal muscle and tongue with enhancement in cardiomyocytes and other muscle-related cell types. Its association with glycogen storage disease type VII and substantial literature make it important for interpreting the module as potentially related to energy demand and muscle-like cellular states.
- **Conclusion**: Established evidence supports PFKM as a muscle-type glycolytic enzyme with a disease link to glycogen metabolism. Its co-abundance with MDH1 supports a metabolic interpretation, but the absence of globally significant enrichment and the heterogeneous tissue context prevent concluding that the module is a dedicated muscle or glycolysis module.

#### DDX21

- **Related proteins** (co-abundance neighbors): RBM10 (0.85), PHIP (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 connects RBM10 to PHIP and supplies a second nuclear or nucleolar regulatory axis. Its established DEAD-box helicase family function is compatible with RNA structural remodeling and ribosome or spliceosome-related processes, while the supplied annotations also include chromatin remodeling, transcriptional regulation, and osteoblast differentiation. Its cell-type enhancement in basal and suprabasal keratinocytes and substantial literature add biological context, although it is not specific to the two tissues.
- **Conclusion**: Established evidence supports DDX21 as an RNA and gene-regulatory factor with reported relevance to osteoblast differentiation. The module permits the hypothesis that DDX21 participates in a shared transcriptional or RNA-processing state, but it does not show that DDX21 mediates the bone or autonomic-tissue relationship.

#### PHIP

- **Related proteins** (co-abundance neighbors): DDX21 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PHIP subunit of CUL4-Ring ligase complex. This gene encodes a protein that binds to the insulin receptor substrate 1 protein and regulates glucose transporter translocation in skeletal muscle cells. The encoded protein may also regulate growth and survival of pancreatic beta cells. Elevated copy number of this gene may be associated with melanoma severity and the encoded protein may promote melanoma metastasis in human patients. [provided…
- **Diseases (Open Targets)**: PHIP-related behavioral problems-intellectual disability-obesity-dysmorphic features syndrome (0.805); Intellectual disability (0.544); hereditary disease (0.543); obesity due to melanocortin 4 receptor deficiency (0.383); obesity disorder (0.383)
- **Europe PMC papers**: 2064
- **Why important**: PHIP is the terminal member of the supplied subgraph, connected to DDX21, and links the regulatory portion of the module to insulin-receptor signaling, glucose-transporter translocation in skeletal muscle, chromatin organization, and cell-population regulation. Its association with PHIP-related intellectual-disability and obesity phenotypes, together with substantial literature, makes it relevant to signaling, metabolism, and organismal phenotypes. Its low tissue and cell-type specificity cautions against using it as a tissue marker.
- **Conclusion**: Established evidence supports PHIP as a signaling, chromatin, and growth-related protein with relevance to skeletal-muscle glucose handling and human neurodevelopmental or obesity phenotypes. Its position suggests a possible regulatory connection to the RNA-control branch, but that connection is a hypothesis because neither STRING nor hu.MAP supports a known complex involving the module members.
