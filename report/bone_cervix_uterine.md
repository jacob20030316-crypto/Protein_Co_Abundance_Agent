# Conserved co-abundance modules: bone and cervix_uterine

## Module 0

**Tissue pair**: bone and cervix_uterine  
**Genes (6)**: CISD1, HTATIP2, NIPSNAP1, PQBP1, SNRPB2, TMA16

### Function

The module does not have a statistically supported GO or KEGG functional label: no term passed global correction. Its gene annotations nevertheless suggest a mixed cellular program involving nuclear RNA processing and splicing, ribosome-related biogenesis, mitochondrial redox or iron-sulfur biology, and possible vesicular or cellular-stress regulation. The co-abundance network is sparse and divided into small links rather than forming a coherent, densely connected pathway. The strongest functional interpretation is therefore a shared expression program combining housekeeping-like nuclear machinery with mitochondrial and stress-associated functions, rather than a demonstrated bone- or cervix-specific pathway. The spliceosomal interpretation is supported by the annotations of SNRPB2 and PQBP1 and by their shared hu.MAP complex membership (hu.MAP huMAP3_06511.1), but it remains an interpretation rather than a globally significant enrichment result.

**Cell composition.** The module is not composed of plasma proteins or secreted proteins: the HPA summary reports no secreted genes. All genes have low immune-cell specificity, and no blood-cell enrichment is reported, so a blood-contamination explanation is not supported by the available HPA evidence. Most genes show low tissue specificity, consistent with broadly distributed cellular functions, while several show cell-type-enhanced patterns in reproductive, epithelial, platelet, hepatic, or related cell types. The module is detected at the protein level in cervix_uterine for several genes, whereas bone has no matching HPA tissue data. The mixture of broadly expressed intracellular proteins and cell-type-enhanced genes means that shared cellular composition or a general intracellular state could contribute to the cross-tissue module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional enrichment or high-confidence STRING pairwise interaction is reported. Thus, the co-abundance edges are not corroborated by the specified STRING evidence and should not be interpreted as established direct physical interactions. hu.MAP provides one relevant complex association (hu.MAP huMAP3_06511.1): SNRPB2 and PQBP1 occur together within a large spliceosome-related complex. This supports a known molecular context for that pair, but only a small part of the complex is represented in the module. The remaining genes have no listed hu.MAP complex membership. Overall, the network appears to capture coordinated abundance without strong evidence that all members form one physical complex.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06511.1 (PQBP1, SNRPB2; 2/79)

### Novelty

The exact cross-tissue co-abundance module may be a new observation, because the supplied resources do not show a matching STRING interaction network or a shared hu.MAP complex encompassing the module. However, that does not establish biological novelty by itself. Several component functions are already well established, especially spliceosomal RNA processing for SNRPB2 and PQBP1 and mitochondrial iron-sulfur or redox biology for CISD1. The defensible claim is that the cross-tissue co-abundance arrangement and its possible coordination of these functional classes are potentially novel, while the underlying gene functions and the limited known complex relationship are not novel.

**Hypothesis.** Hypothesis: the module reflects a conserved intracellular maintenance state shared by bone and cervix_uterine, in which nuclear RNA processing is coordinated with mitochondrial quality control, redox handling, and cellular stress or survival programs. SNRPB2 and PQBP1 may represent the RNA-processing arm, CISD1 and NIPSNAP1 the mitochondrial or organelle-maintenance arm, and HTATIP2 a possible stress, transcriptional, or survival-related connector. TMA16 may link the RNA-associated portion to ribosome-related biogenesis. This hypothesis is based on gene annotations and the observed co-abundance structure; it is not established by global enrichment, STRING interactions, or a demonstrated biochemical complex.

### Important genes

#### SNRPB2

- **Related proteins** (co-abundance neighbors): PQBP1 (0.91), TMA16 (0.84), HTATIP2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_06511.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein polypeptide B2. The protein encoded by this gene associates with stem loop IV of U2 small nuclear ribonucleoprotein (U2 snRNP) in the presence of snRNP-A'. The encoded protein may play a role in pre-mRNA splicing. Autoantibodies from patients with systemic lupus erythematosus frequently recognize epitopes on the encoded protein. Two transcript variants encoding the same protein have been found for this gene. [pro…
- **Diseases (Open Targets)**: neurodegenerative disease (0.372); dengue disease (0.370); sleep apnea syndrome (0.233); preeclampsia (0.111); gestational diabetes (0.111)
- **Europe PMC papers**: 336
- **Why important**: SNRPB2 has the most central position in the module network and connects to PQBP1, TMA16, and HTATIP2. Its established role in U2 snRNP association, spliceosomal assembly, and pre-mRNA splicing gives the module its clearest mechanistic anchor. It also shares the hu.MAP complex context with PQBP1 (hu.MAP huMAP3_06511.1) and has substantial literature coverage.
- **Conclusion**: Established evidence supports SNRPB2 as a nuclear pre-mRNA-splicing component and as a central co-abundance hub. It is reasonable to hypothesize that it helps define the RNA-processing aspect of the module, but the data do not establish that its network links are direct physical interactions or that splicing is enriched at the module level.

#### PQBP1

- **Related proteins** (co-abundance neighbors): SNRPB2 (0.91); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles, Primary cilium; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_06511.1
- **Function (MyGene.info)**: polyglutamine binding protein 1. This gene encodes a nuclear polyglutamine-binding protein that is involved with transcription activation. The encoded protein contains a WW domain. Mutations in this gene have been found in patients with Renpenning syndrome 1 and other syndromes with X-linked cognitive disability. Multiple alternatively spliced transcript variants that encode different protein isoforms have been described for this…
- **Diseases (Open Targets)**: Renpenning syndrome (0.787); neurodegenerative disease (0.531); hereditary disease (0.466); Intellectual disability (0.449); microcephaly (0.419)
- **Europe PMC papers**: 1075
- **Why important**: PQBP1 is linked directly to SNRPB2 and shares the hu.MAP complex (hu.MAP huMAP3_06511.1). Its annotations connect alternative splicing with transcriptional regulation and innate antiviral responses, while its disease associations and comparatively large literature base make it biologically informative beyond a generic housekeeping marker.
- **Conclusion**: Established evidence supports PQBP1 as a nuclear regulatory protein involved in transcription and alternative splicing, with disease relevance in X-linked neurodevelopmental syndromes. Its membership in this module is compatible with a conserved RNA-processing program, but any antiviral or tissue-specific role here remains hypothetical.

#### CISD1

- **Related proteins** (co-abundance neighbors): HTATIP2 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CDGSH iron sulfur domain 1. This gene encodes a protein with a CDGSH iron-sulfur domain and has been shown to bind a redox-active [2Fe-2S] cluster. The encoded protein has been localized to the outer membrane of mitochondria and is thought to play a role in regulation of oxidation. Genes encoding similar proteins are located on chromosomes 4 and 17, and a pseudogene of this gene is located on chromosome 2. [provided by RefSe…
- **Diseases (Open Targets)**: neurodegenerative disease (0.539); Abnormality of the integument (0.348); secondary malignant neoplasm (0.306); Parkinson disease (0.296); biliary tract disorder (0.283)
- **Europe PMC papers**: 1042
- **Why important**: CISD1 is the module’s mitochondrial redox and iron-sulfur candidate. It is tissue-enhanced in parathyroid gland, localized to mitochondria, and annotated for an iron-sulfur domain, oxidation regulation, iron homeostasis, autophagy, and protein maturation. It also has substantial literature coverage and disease associations involving neurodegeneration and other disorders.
- **Conclusion**: Established evidence supports CISD1 as a mitochondrial protein that binds a redox-active iron-sulfur cluster and participates in mitochondrial or cellular stress biology. Its connection to HTATIP2 is a co-abundance relationship without STRING support, so its proposed role as part of a coordinated module-level stress program remains a hypothesis.

#### HTATIP2

- **Related proteins** (co-abundance neighbors): CISD1 (0.85), SNRPB2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HIV-1 Tat interactive protein 2. Enables protein serine/threonine kinase activity. Involved in import into nucleus and regulation of angiogenesis. Acts upstream of or within positive regulation of programmed cell death; positive regulation of transcription by RNA polymerase II; and protein autophosphorylation. Located in cytosol and nuclear envelope. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: COVID-19 (0.345); severe acute respiratory syndrome (0.344); liver disorder (0.215); placental abruption (0.214); neoplasm (0.116)
- **Europe PMC papers**: 622
- **Why important**: HTATIP2 occupies a bridging position between CISD1 and SNRPB2. Its annotations include regulation of programmed cell death, transcription, protein autophosphorylation, and cytoplasmic translation, making it a plausible interface between mitochondrial or stress biology and nuclear regulation. It is detected in cervix_uterine and has substantial literature coverage.
- **Conclusion**: Established evidence supports HTATIP2 as a regulator associated with transcription, survival-related processes, and cellular signaling. Its apparent bridging role is supported by network placement, but whether it mechanistically coordinates the RNA-processing and mitochondrial portions of this module is not demonstrated.

#### NIPSNAP1

- **Related proteins** (co-abundance neighbors): TMA16 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nipsnap homolog 1. This gene encodes a member of the NipSnap family of proteins that may be involved in vesicular transport. A similar protein in mice inhibits the calcium channel TRPV6, and is also localized to the inner mitochondrial membrane where it may play a role in mitochondrial DNA maintenance. A pseudogene of this gene is located on the short arm of chromosome 17. Alternatively spliced transcript variants e…
- **Diseases (Open Targets)**: hypothyroidism (0.298); glaucoma (0.198); bile duct disorder (0.192); neoplasm (0.069); cancer (0.054)
- **Europe PMC papers**: 391
- **Why important**: NIPSNAP1 is linked to TMA16 and provides a second organelle or trafficking-related perspective. Its annotations implicate vesicular transport, mitochondrial localization or maintenance, and mitophagy, while HPA shows tissue enhancement in liver and cell-type enhancement in hepatocytes and proximal tubule cells.
- **Conclusion**: Established evidence supports NIPSNAP1 as a NipSnap-family protein associated with vesicular and mitochondrial biology, including mitophagy-related annotation. Its participation in a bone–cervix_uterine maintenance program is a hypothesis based on co-abundance and should not be treated as a demonstrated tissue mechanism.

#### TMA16

- **Related proteins** (co-abundance neighbors): SNRPB2 (0.84), NIPSNAP1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translation machinery associated 16 homolog. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: eyelid disorder (0.276); Abnormality of limbs (0.258); acute tonsillitis (0.200); digestive system disorder (0.194); obesity disorder (0.194)
- **Europe PMC papers**: 87
- **Why important**: TMA16 links NIPSNAP1 with SNRPB2 and is annotated to the nucleolus, nucleoplasm, and ribosomal large-subunit biogenesis. Its cell-type-enhanced pattern includes germ-cell and megakaryocyte contexts, and it may represent a biosynthetic or ribosome-related component distinct from the spliceosomal genes.
- **Conclusion**: Established evidence supports TMA16 as a nucleolar factor associated with ribosomal large-subunit biogenesis. Its network position suggests possible coordination between RNA processing, ribosome production, and organelle-related biology, but that integrated mechanism is not directly established.

## Module 1

**Tissue pair**: bone and cervix_uterine  
**Genes (5)**: CACYBP, LDHA, NAA50, TPD52, TPD52L2

### Function

The module does not have a GO or KEGG term passing global correction, so no pathway-level function can be assigned from primary enrichment evidence. Its strongest directly supported feature is a TPD52-family association: TPD52 and TPD52L2 are linked by STRING and recur together across several hu.MAP complexes (STRING Pfam Tumour protein D52 family; within-query FDR = 0.0258) (hu.MAP huMAP3_12428.1). The remaining genes suggest a mixed cellular program involving calcium-linked protein regulation through CACYBP, protein N-terminal acetylation and chromatin or cohesion biology through NAA50, and glycolytic lactate production through LDHA. These annotations support a possible combination of vesicle or cytosolic protein organization, proteostasis, biosynthetic regulation, and cellular energy metabolism, but the module should not be interpreted as a single established pathway.

**Cell composition.** The module is not composed of secreted proteins, and most genes have low tissue specificity. HPA indicates low immune-cell specificity for most genes, with one immune-cell-enhanced gene, TPD52, associated with memory B cells and also with B cells and plasma cells. Other cell-type associations include megakaryocytes, neural or glial populations, choroid plexus epithelial cells, myonuclei, ocular epithelial cells, migrating cytotrophoblasts, and oocytes. All module proteins are detected in cervix_uterine, whereas the supplied bone protein-detection field has no matching HPA tissue. Thus, the shared signal is unlikely to be explained simply by a secreted plasma-protein program or a broad blood-cell module, although shared cell composition and tissue-context effects remain plausible.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING pair is TPD52 with TPD52L2, supporting a known relationship between these two family members. STRING supplementary enrichment identifies the TPD52 family (STRING Pfam Tumour protein D52 family; within-query FDR = 0.0258), but this is not global enrichment evidence. TPD52 and TPD52L2 also co-occur in several hu.MAP complexes (hu.MAP huMAP3_12428.1), including complexes containing other TPD52-like proteins and, in some cases, neuronal receptor-associated, transcriptional, or signaling proteins. The repeated pairwise presence across these complexes indicates that part of the module reflects a known protein-family and complex framework. CACYBP, NAA50, and LDHA have no supplied STRING partners or hu.MAP complexes, so their links to the module are co-abundance relationships rather than established physical interactions in these resources.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: TPD52–TPD52L2 (0.825)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam Tumour protein D52 family (FDR = 0.0258, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12428.1 (TPD52L2, TPD52; 2/4); huMAP3_11893.1 (TPD52L2, TPD52; 2/6); huMAP3_14896.1 (TPD52L2, TPD52; 2/6); huMAP3_13312.1 (TPD52L2, TPD52; 2/7); huMAP3_10107.1 (TPD52L2, TPD52; 2/9); huMAP3_14355.1 (TPD52L2, TPD52; 2/10); huMAP3_11787.1 (TPD52L2, TPD52; 2/11)

### Novelty

The complete five-gene co-abundance module may represent a tissue-pair-specific observation, but it cannot be called a new molecular complex or a newly discovered pathway. The TPD52–TPD52L2 relationship and their shared complex contexts are already documented (STRING Pfam Tumour protein D52 family; within-query FDR = 0.0258) (hu.MAP huMAP3_12428.1). The potentially novel aspect is the coordinated occurrence of these two genes with CACYBP, NAA50, and LDHA in bone and cervix_uterine. However, absence of the latter genes from the supplied STRING and hu.MAP evidence does not prove novelty; it may reflect tissue context, co-regulation, incomplete interaction coverage, or indirect biological coupling. The lack of globally significant GO or KEGG enrichment further limits claims of a newly defined functional pathway.

**Hypothesis.** Hypothesis: the module represents a shared cellular-state program rather than a discrete canonical pathway. In this model, TPD52 and TPD52L2 provide a vesicle- or cytosol-associated protein-organization component, CACYBP connects calcium-responsive regulation with ubiquitin-dependent proteostasis, NAA50 reflects protein acetylation and proliferative or chromatin-linked demands, and LDHA reflects glycolytic adaptation. Their coordinated abundance in bone and cervix_uterine could arise from a common requirement for protein organization, proteostasis, biosynthetic regulation, and energy metabolism in cells present in both tissues. This hypothesis requires validation using cell-resolved expression, perturbation, and protein-interaction measurements.

### Important genes

#### TPD52

- **Related proteins** (co-abundance neighbors): TPD52L2 (0.84), CACYBP (0.82); STRING partners: TPD52L2 (0.825)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_12428.1, huMAP3_11893.1, huMAP3_14896.1, huMAP3_13312.1, huMAP3_10107.1, huMAP3_14355.1, huMAP3_11787.1
- **Function (MyGene.info)**: tumor protein D52. Enables calcium ion binding activity and protein homodimerization activity. Involved in B cell differentiation. Located in endoplasmic reticulum and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: prostate carcinoma (0.393); rheumatoid arthritis (0.347); skin disorder (0.267); cervical carcinoma (0.256); Parkinson disease (0.252)
- **Europe PMC papers**: 1217
- **Why important**: TPD52 is one of the two central family members in the module. It is directly connected to TPD52L2 in STRING and appears with TPD52L2 across multiple hu.MAP complexes (STRING Pfam Tumour protein D52 family; within-query FDR = 0.0258) (hu.MAP huMAP3_12428.1). It has tissue-enhanced expression in retina, cell-type associations with B cells, plasma cells, choroid plexus epithelial cells, and salivary ionocytes, and an immune-cell-enhanced memory B-cell annotation. Its supplied functions include calcium ion binding, homodimerization, B-cell differentiation, secretion, and regulation of cell proliferation. It also has disease associations including prostate carcinoma, rheumatoid arthritis, and cervical carcinoma, with substantial literature volume.
- **Conclusion**: Established evidence supports TPD52 as a biologically relevant anchor of the module and as the best-supported link to B-cell and secretion-related biology. The supplied evidence does not establish that TPD52 drives the shared bone–cervix_uterine signal or that the module is a B-cell program.

#### TPD52L2

- **Related proteins** (co-abundance neighbors): TPD52 (0.84), CACYBP (0.84); STRING partners: TPD52 (0.825)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_12428.1, huMAP3_11893.1, huMAP3_14896.1, huMAP3_13312.1, huMAP3_10107.1, huMAP3_14355.1, huMAP3_11787.1
- **Function (MyGene.info)**: TPD52 like 2. This gene encodes a member of the tumor protein D52-like family. These proteins are characterized by an N-terminal coiled-coil motif that is used to form homo- and heteromeric complexes with other tumor protein D52-like proteins. Expression of this gene may be a marker for breast cancer and acute lymphoblastic leukemia. Alternatively spliced transcript variants encoding multiple isoforms have been…
- **Diseases (Open Targets)**: breast cancer (0.088); breast carcinoma (0.087); neoplasm (0.078); gastric cancer (0.078); posterior cortical atrophy (0.077)
- **Europe PMC papers**: 1316
- **Why important**: TPD52L2 is the other recurring TPD52-family member and is directly connected to TPD52 in STRING. It participates with TPD52 in multiple hu.MAP complexes (STRING Pfam Tumour protein D52 family; within-query FDR = 0.0258) (hu.MAP huMAP3_12428.1). Its coiled-coil family architecture supports homo- and heteromeric complex formation, and its vesicular localization is compatible with intracellular protein organization. HPA associates it with astrocytes, Bergmann glia, excitatory and inhibitory neurons, and choroid plexus epithelial cells. It also has cancer-related disease associations and substantial literature volume.
- **Conclusion**: Established evidence supports TPD52L2 as a known complex-associated partner of TPD52 and a plausible structural contributor to the module. Its neural and vesicular annotations broaden the possible cellular context, but they do not demonstrate a neural mechanism in either tissue.

#### CACYBP

- **Related proteins** (co-abundance neighbors): NAA50 (0.86), TPD52L2 (0.84), LDHA (0.83), TPD52 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcyclin binding protein. The protein encoded by this gene is a calcyclin binding protein. It may be involved in calcium-dependent ubiquitination and subsequent proteosomal degradation of target proteins. It probably serves as a molecular bridge in ubiquitin E3 complexes and participates in the ubiquitin-mediated degradation of beta-catenin. Two alternatively spliced transcript variants encoding different isoforms have bee…
- **Diseases (Open Targets)**: esophageal disorder (0.358); gastroesophageal reflux disease (0.291); Abnormality of the skeletal system (0.262); mood disorder (0.202); major depressive disorder (0.202)
- **Europe PMC papers**: 835
- **Why important**: CACYBP has the most connected position in the supplied co-abundance subgraph, linking both TPD52-family genes with NAA50 and LDHA. Its described function as a calcyclin-binding protein and possible bridge in ubiquitin E3 complexes connects the module to calcium-responsive proteostasis and beta-catenin degradation. It is associated with megakaryocytes, migrating cytotrophoblasts, and oocytes, has low tissue and immune specificity, and has a substantial literature base. Its disease associations include skeletal-system abnormality and several gastrointestinal or mood-related conditions.
- **Conclusion**: Established evidence supports CACYBP as the network connector and as a plausible proteostasis-related integrator. Its central co-abundance position does not prove physical bridging or causal control of the other module genes.

#### NAA50

- **Related proteins** (co-abundance neighbors): CACYBP (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-alpha-acetyltransferase 50, NatE catalytic subunit. Enables H4 histone acetyltransferase activity; peptide alpha-N-acetyltransferase activity; and peptidyl-lysine acetyltransferase activity. Involved in N-terminal protein amino acid acetylation; establishment of mitotic sister chromatid cohesion; and mitotic sister chromatid cohesion, centromeric. Located in cytosol and nucleus. Part of NatA complex. [provided by Alliance of Genome Resources, Apr 2…
- **Diseases (Open Targets)**: musculoskeletal system disorder (0.174); Abnormality of the skeletal system (0.147); upper respiratory tract disorder (0.066); neuroblastoma (0.059); alcohol drinking (0.035)
- **Europe PMC papers**: 308
- **Why important**: NAA50 links to CACYBP in the module and encodes the catalytic subunit of the NatE N-terminal acetyltransferase. Its supplied functions include N-terminal protein acetylation, lysine acetylation, chromatin remodeling, and mitotic sister-chromatid cohesion. HPA reports skeletal-muscle tissue enhancement and myonuclear association, while its literature volume is smaller than that of the other major module genes. Its disease associations include musculoskeletal and skeletal-system abnormalities.
- **Conclusion**: Established evidence supports NAA50 as a protein-modification and cell-division-related gene that may explain part of the module's biosynthetic or proliferative context. The module does not establish that NAA50 is functionally coupled to the TPD52 family or that cohesion biology is the principal module function.

#### LDHA

- **Related proteins** (co-abundance neighbors): CACYBP (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lactate dehydrogenase A. This gene encodes the A subunit of lactate dehydrogenase enzyme which catalyzes the reversible conversion of pyruvate to lactate with the concomitant oxidation of NADH to NAD in anaerobic glycolysis. The protein is found predominantly in skeletal muscle and belongs to the lactate dehydrogenase family. Mutations in this gene have been linked to exertional myoglobinuria. The human genome contains se…
- **Diseases (Open Targets)**: glycogen storage disease due to lactate dehydrogenase M-subunit deficiency (0.755); disorder of glycogen metabolism (0.505); glycogen storage disease XV (0.505); primary hyperoxaluria (0.447); hereditary disease (0.190)
- **Europe PMC papers**: 20747
- **Why important**: LDHA links to CACYBP and encodes the A subunit of lactate dehydrogenase, catalyzing the reversible conversion of pyruvate to lactate during anaerobic glycolysis. It is associated with skeletal muscle, megakaryocytes, ocular epithelial cells, and other brain neurons, and has the largest literature volume among the module genes. Its disease associations prominently include lactate-dehydrogenase deficiency and glycogen-metabolism disorders.
- **Conclusion**: Established evidence supports LDHA as a metabolic marker that could reflect glycolytic demand or cell composition. Its presence does not demonstrate that glycolysis is globally enriched in the module, particularly because no GO or KEGG term passed global correction.
