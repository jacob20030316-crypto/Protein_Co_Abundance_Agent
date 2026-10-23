# Conserved co-abundance modules: bone_marrow and colon

## Module 0

**Tissue pair**: bone_marrow and colon  
**Genes (8)**: ABRACL, COX18, ESCO2, KANSL2, MRPS33, RXRA, TSPYL5, WDR41

### Function

This module does not support a single established biological function. No GO or KEGG term passed global correction, and there are no supplementary STRING enrichment terms. The genes span mitochondrial protein synthesis and respiratory-chain assembly, chromatin regulation and chromosome cohesion, nuclear-receptor transcription, autophagy-related regulation, and actin-related processes. The sparse co-abundance structure therefore appears more consistent with a shared expression or cellular-state signal than with a defined molecular complex. The strongest functional interpretation is a heterogeneous intracellular maintenance module involving transcriptional regulation, genome maintenance, mitochondrial activity, and cytoskeletal or trafficking processes. No GO or KEGG claim is made as primary evidence because no globally significant GO/KEGG term is present.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only one gene has a secretome annotation, while the others are intracellular, membrane-associated, or lack secretome annotation. Most genes have low tissue specificity, indicating a broadly expressed component rather than a module restricted to bone marrow or colon. Several genes have cell-type-enhanced patterns, including hepatocyte, epithelial, germ-cell, and progenitor-cell associations. Immune-cell specificity is generally low, although RXRA and ESCO2 show immune-cell enhancement in the supplied HPA evidence. The shared signal could therefore partly reflect common cell populations or sample composition in the two tissues, rather than a tissue-pair-specific pathway. HPA protein detection is present for several genes in both tissues but is incomplete, so protein-level support is mixed.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and no hu.MAP complex contains multiple module members. Consequently, the co-abundance edges should not be interpreted as already established physical interactions. The absence of STRING and hu.MAP support argues against a known protein complex, but it does not exclude indirect regulation, context-dependent interactions, or coordinated abundance caused by shared cell state. WDR41 is the most connected gene in the module and links RXRA, TSPYL5, and COX18 in the co-abundance graph, while the remaining genes form short links through TSPYL5, COX18, and MRPS33; this topology is compatible with a statistical bridge between otherwise distinct biological processes.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may represent a previously unrecognized co-abundance pattern, but it cannot be called a new biological discovery from the supplied evidence alone. The lack of globally significant GO or KEGG enrichment, STRING enrichment, high-confidence STRING interactions, and multi-member hu.MAP complexes makes a novel coherent pathway interpretation unlikely at present. A cautious novelty claim is that these genes co-vary in the bone-marrow and colon data under the studied conditions. Independent replication, adjustment for cell composition, and validation at the protein or functional level would be needed to distinguish a genuine conserved regulatory program from shared housekeeping expression, cellular composition, or dataset-specific correlation.

**Hypothesis.** Hypothesis: the module reflects a conserved intracellular cell-state program that couples transcriptional and chromatin regulation with mitochondrial capacity and cellular remodeling. In this model, RXRA and KANSL2 could mark transcriptional regulation, ESCO2 could reflect proliferative or progenitor-associated genome maintenance, MRPS33 and COX18 could reflect mitochondrial translation and respiratory-chain assembly, and WDR41 or ABRACL could reflect autophagy, trafficking, or actin-related state. TSPYL5 may connect the chromatin or signaling side of this state to the mitochondrial and proliferative components. This is a hypothesis based on the gene functions and co-abundance topology, not an established pathway or physical complex.

### Important genes

#### WDR41

- **Related proteins** (co-abundance neighbors): RXRA (0.92), TSPYL5 (0.83), COX18 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 41. Contributes to guanyl-nucleotide exchange factor activity. Involved in regulation of autophagy. Located in cytoplasm. Part of guanyl-nucleotide exchange factor complex. Colocalizes with Atg1/ULK1 kinase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypothyroidism (0.312); ovarian neoplasm (0.306); neurodegenerative disease (0.268); corneal ulcer (0.267); diabetes mellitus (0.263)
- **Europe PMC papers**: 289
- **Why important**: WDR41 has the strongest network position in the module and connects RXRA, TSPYL5, and COX18. Its supplied annotations link it to guanyl-nucleotide exchange factor activity, autophagy regulation, negative regulation of exocytosis, and negative regulation of immune response. It is detected in both bone marrow and colon, making it a plausible bridge between the shared tissue signal and intracellular trafficking or cell-state regulation. Its literature base is substantial compared with several other genes in the module.
- **Conclusion**: Established evidence supports WDR41 as the principal network connector and as a gene associated with autophagy and trafficking-related regulation. It is reasonable to regard WDR41 as a candidate coordinator of the module, but the co-abundance edges do not establish direct molecular interactions or prove that WDR41 drives the shared tissue pattern.

#### RXRA

- **Related proteins** (co-abundance neighbors): WDR41 (0.92); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: retinoid X receptor alpha. Retinoid X receptors (RXRs) and retinoic acid receptors (RARs) are nuclear receptors that mediate the biological effects of retinoids by their involvement in retinoic acid-mediated gene activation. These receptors function as transcription factors by binding as homodimers or heterodimers to specific sequences in the promoters of target genes. The protein encoded by this gene is a member of the ste…
- **Diseases (Open Targets)**: psoriasis (0.583); primary cutaneous T-cell non-Hodgkin lymphoma (0.551); psoriasis vulgaris (0.517); urinary bladder cancer (0.507); neoplasm (0.480)
- **Europe PMC papers**: 5301
- **Why important**: RXRA is the clearest transcriptional regulator in the module and is connected to WDR41. Its established function as a retinoid X receptor supports roles in nuclear-receptor signaling and gene regulation. HPA evidence places it in bone marrow and colon and associates it with hepatocytes, Kupffer cells, monocytes, and neutrophils, including immune-cell enhancement. It also has the largest literature base among the module genes and relevant disease associations involving inflammatory and neoplastic conditions.
- **Conclusion**: Established evidence supports RXRA as a broadly relevant transcriptional and hormone-signaling regulator with plausible relevance to immune and epithelial contexts. Its presence is compatible with a shared cell-state or composition signal, but the module does not establish an RXRA-driven regulatory program.

#### ESCO2

- **Related proteins** (co-abundance neighbors): MRPS33 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: establishment of sister chromatid cohesion N-acetyltransferase 2. This gene encodes a protein that may have acetyltransferase activity and may be required for the establishment of sister chromatid cohesion during the S phase of mitosis. Mutations in this gene have been associated with Roberts syndrome. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: Roberts-SC phocomelia syndrome (0.825); Juberg-Hayward syndrome (0.706); hereditary disease (0.487); Absent radius (0.462); hypercholesterolemia, familial, 1 (0.333)
- **Europe PMC papers**: 1280
- **Why important**: ESCO2 is the module gene with the clearest connection to genome duplication and cell proliferation, through sister chromatid cohesion and post-translational acetylation. It is tissue enhanced in bone marrow, intestine, lymphoid tissue, and testis, and cell-type enhanced in erythrocyte and megakaryocyte progenitors as well as differentiating germ-line cells. Its association with Roberts syndrome provides a strong disease link, and its literature volume is substantial.
- **Conclusion**: Established evidence supports ESCO2 as a chromosome-cohesion and developmental genome-maintenance gene, with particular relevance to proliferative progenitor populations. Its presence may indicate a progenitor or cell-cycle component in the shared signal, but no enrichment result or network evidence demonstrates that this process is the central function of the module.

#### COX18

- **Related proteins** (co-abundance neighbors): ABRACL (0.84), WDR41 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome c oxidase assembly factor COX18. This gene encodes a cytochrome c oxidase assembly protein. The encoded protein is essential for integral membrane protein insertion into the mitochondrial inner membrane. It is also required for cytochrome c oxidase assembly and activity. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.557); Charcot-Marie-Tooth disease (0.526); mitochondrial disease (0.525); ocular hypotension (0.253); sialadenitis (0.253)
- **Europe PMC papers**: 367
- **Why important**: COX18 is connected to WDR41 and ABRACL and has a defined role in cytochrome c oxidase assembly and insertion of membrane proteins into the mitochondrial inner membrane. It is detected in colon and not detected in bone marrow in the supplied immunohistochemistry summary, while its disease associations include mitochondrial and neurodegenerative disorders. The gene therefore provides a concrete mitochondrial interpretation for part of the module.
- **Conclusion**: Established evidence supports COX18 as a mitochondrial respiratory-chain assembly factor. It is a credible marker of mitochondrial functional state within the module, but its tissue-level protein detection pattern and the absence of complex evidence argue against treating it as proof of a shared mitochondrial complex across the two tissues.

#### TSPYL5

- **Related proteins** (co-abundance neighbors): KANSL2 (0.88), MRPS33 (0.84), WDR41 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TSPY like 5. Predicted to enable chromatin binding activity and histone binding activity. Involved in several processes, including cellular response to gamma radiation; positive regulation of protein kinase B signaling; and positive regulation of protein ubiquitination. Predicted to be active in chromatin and nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Vertigo (0.273); ovarian neoplasm (0.260); migraine disorder (0.226); ulcerative colitis (0.186); keratinocyte carcinoma (0.178)
- **Europe PMC papers**: 459
- **Why important**: TSPYL5 has a central bridging position between KANSL2, MRPS33, and WDR41. Its supplied annotations involve chromatin binding, histone binding, nucleosome assembly, protein ubiquitination, and phosphatidylinositol-three-kinase/protein-kinase-B signaling. HPA places it in a testis-enhanced and spermatid-associated expression pattern, while it is not detected in immune cells and is not detected by immunohistochemistry in the two focal tissues. Its disease associations and literature base are meaningful despite its limited direct network support.
- **Conclusion**: Established evidence supports TSPYL5 as a candidate chromatin and signaling regulator and as a statistical bridge in this module. Its testis-associated HPA pattern and lack of focal-tissue protein detection make it especially important for considering broad expression or sample-composition effects. A role as the mechanistic link between chromatin, mitochondrial, and autophagy-related genes remains hypothetical.

## Module 1

**Tissue pair**: bone_marrow and colon  
**Genes (48)**: ACAD10, ALG6, AP1S2, ATG7, BRAF, CDT1, CHEK2, DAAM1, DCTN5, DIS3L2, EXOC8, EYA3, FBXO45, FBXO3, GABPA, GXYLT1, MACROH2A1, FECH, HERC1, IGHM, KDM4C, KIF7, PRKCD, NADSYN1, NLRP2, NPRL3, PIK3C2B, PLSCR1, POU2F1, RAC2, RMP24, ROS1, RTN4IP1, SLC4A7, SDHAF3, SIGMAR1, KNSTRN, SLFN5, STK3, TBCK, TBXAS1, THG1L, TIMM8B, TMEM222, TXNDC11, VHL, XTBD1, ZNF384

### Function

This is a heterogeneous cellular-maintenance module rather than a statistically supported single pathway. No GO or KEGG term passed global correction, so there is no globally significant pathway annotation to assign. Gene-level annotations nevertheless point to several connected biological themes: ubiquitin-dependent protein turnover and stress control through FBXO45, HERC1, FBXO3 and VHL; DNA replication, cell-cycle surveillance and chromatin regulation through CDT1, CHEK2, KDM4C and related genes; membrane trafficking and cytoskeletal organization through AP1S2, DCTN5, EXOC8, PIK3C2B, DAAM1 and RAC2; and immune, apoptotic or inflammatory signaling through PRKCD, RAC2, PLSCR1, TBXAS1 and NLRP2. The module therefore appears to capture coordinated cellular state, trafficking, survival and proliferative programs across bone marrow and colon rather than a narrowly defined biochemical process. The absence of globally enriched GO or KEGG terms does not invalidate the module.

**Cell composition.** The module is not dominated by plasma or secreted proteins; only a small secretome subset is reported, including IGHM as an immunoglobulin gene. HPA shows predominantly low tissue specificity, indicating that much of the module is broadly expressed or housekeeping-like. At the same time, cell-type annotations repeatedly point to neutrophils, neutrophil progenitors, hematopoietic progenitors, monocytes, lymphoid cells, erythrocyte progenitors and epithelial cell types. Several genes are tissue enhanced in bone marrow, lymphoid tissue or intestine, while others are associated with reproductive or lung cell types. Protein detection is present for much of the module in both tissues, but the shared signal could still partly reflect common hematopoietic or epithelial cell populations in the samples rather than a tissue-independent molecular complex.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only sparse physical or functional support within the module. The reported high-confidence relationships are ATG7 with BRAF, PRKCD with RAC2, and PRKCD with VHL. These links support a small signaling and stress-response neighborhood, but they do not establish one unified complex for the whole module. hu.MAP provides two partial complex overlaps: (hu.MAP huMAP3_05645.1) contains DIS3L2 and ZNF384 within a larger complex, and (hu.MAP huMAP3_09952.1) contains PIK3C2B and DCTN5 within a larger dynactin- or trafficking-related complex. The fact that only subsets of each complex are present argues for shared functional context or coordinated abundance rather than proof that the entire module is a physical complex. The sparse STRING connectivity and partial hu.MAP overlap also indicate that most co-abundance relationships are not already documented as direct protein interactions.

**STRING interactions (score >= 0.7)**: 3 of 1128 gene pairs: ATG7–BRAF (0.714); PRKCD–RAC2 (0.946); PRKCD–VHL (0.757)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05645.1 (DIS3L2, ZNF384; 2/6); huMAP3_09952.1 (PIK3C2B, DCTN5; 2/16)

### Novelty

This may represent a novel cross-tissue co-abundance pattern, but the fact sheet does not justify calling it a new biological discovery. The supporting evidence is the reproducible sharing of a module between bone marrow and colon, combined with sparse known interaction coverage and several genes with limited functional characterization. However, absence from STRING or hu.MAP is not evidence of novelty by itself, and the module lacks globally significant GO or KEGG enrichment and lacks STRING functional enrichment. A stronger novelty claim would require independent replication, comparison with published co-expression or proteomic modules, and testing whether the signal persists after adjustment for cell-type composition.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program involving protein quality control, vesicle and membrane trafficking, stress or apoptotic signaling, and proliferation or DNA-replication control in cell populations present in both tissues. In bone marrow, the signal may be especially influenced by myeloid, erythroid and progenitor populations; in colon, it may include epithelial and resident immune populations. PRKCD-RAC2-VHL may represent an immune, cytoskeletal and oxygen- or stress-responsive subnetwork, while FBXO45-centered associations and the CDT1-centered neighborhood may reflect proteostasis and proliferative state. This hypothesis should be tested with cell-type deconvolution, matched single-cell data, perturbation experiments and independent tissue cohorts.

### Important genes

#### FBXO45

- **Related proteins** (co-abundance neighbors): ALG6 (0.92), HERC1 (0.88), CHEK2 (0.84), EXOC8 (0.84), KNSTRN (0.83), SLC4A7 (0.83), DIS3L2 (0.81), GABPA (0.81), SLFN5 (0.80), PLSCR1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: F-box protein 45. Members of the F-box protein family, such as FBXO45, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (summary by …
- **Diseases (Open Targets)**: hypothyroidism (0.108); hepatocellular carcinoma (0.094); breast cancer (0.084); breast carcinoma (0.081); non-small cell lung carcinoma (0.080)
- **Europe PMC papers**: 459
- **Why important**: FBXO45 is the most connected hub in the module and links genes involved in protein turnover, DNA-damage response, membrane trafficking, chromosome segregation and cellular transport. Its gene-level annotation supports ubiquitin-dependent proteolysis, and it has substantial literature coverage. Its broad HPA profile makes it plausible as a general cellular-state marker rather than a tissue-specific driver.
- **Conclusion**: Established evidence supports FBXO45 as a central network integrator with a role related to ubiquitin-dependent protein regulation. Its hub position does not prove that it mechanistically drives the shared module. The most defensible interpretation is that FBXO45 marks coordinated proteostasis and cellular stress, with a causal role remaining hypothetical.

#### CDT1

- **Related proteins** (co-abundance neighbors): AP1S2 (0.93), DCTN5 (0.87), POU2F1 (0.86), HERC1 (0.85), PRKCD (0.84), NPRL3 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromatin licensing and DNA replication factor 1. The protein encoded by this gene is involved in the formation of the pre-replication complex that is necessary for DNA replication. The encoded protein can bind geminin, which prevents replication and may function to prevent this protein from initiating replication at inappropriate origins. Phosphorylation of this protein by cyclin A-dependent kinases results in degradation of the protein. [provid…
- **Diseases (Open Targets)**: Meier-Gorlin syndrome (0.802); neurodegenerative disease (0.451); microcephalic primordial dwarfism (0.370); hereditary disease (0.194); chronic kidney disease (0.191)
- **Europe PMC papers**: 4370
- **Why important**: CDT1 has a prominent network position and connects to AP1S2, DCTN5, POU2F1, HERC1, PRKCD and NPRL3. It is tissue enriched in bone marrow and detected in both tissues by immunohistochemistry. Its established function in pre-replication-complex formation, replication control and cell-cycle regulation makes it informative for interpreting proliferative or progenitor-cell contributions.
- **Conclusion**: Established evidence supports CDT1 as a DNA-replication licensing and cell-cycle regulator associated with bone-marrow cellular states. The co-abundance pattern may therefore partly reflect proliferating progenitors or cycling cells, but the data do not establish that replication control is the primary function of the whole module.

#### PRKCD

- **Related proteins** (co-abundance neighbors): CDT1 (0.84); STRING partners: RAC2 (0.946), VHL (0.757)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase C delta. The protein encoded by this gene is a member of the protein kinase C family of serine- and threonine-specific protein kinases. The encoded protein is activated by diacylglycerol and is both a tumor suppressor and a positive regulator of cell cycle progression. Also, this protein can positively or negatively regulate apoptosis. Defects in this gene are a cause of autoimmune lymphoproliferative synd…
- **Diseases (Open Targets)**: autoimmune lymphoproliferative syndrome (0.685); acute myeloid leukemia (0.556); mast cell leukemia (0.475); systemic mastocytosis (0.471); mastocytosis (0.464)
- **Europe PMC papers**: 3335
- **Why important**: PRKCD connects the module to both RAC2 and VHL through reported STRING relationships and is co-abundant with CDT1. It is detected in both tissues and is enhanced in neutrophils and platelets. Its established functions include protein kinase signaling, apoptosis, stress responses and DNA-damage responses, and it has disease associations involving immune dysregulation and myeloid malignancy.
- **Conclusion**: Established evidence supports PRKCD as a biologically informative signaling node connecting immune-cell behavior with apoptosis and stress responses. The network supports a possible bridge between immune and proliferative states, but it does not show that PRKCD directly organizes the complete module.

#### RAC2

- **Related proteins** (co-abundance neighbors): VHL (0.87); STRING partners: PRKCD (0.946)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rac family small GTPase 2. This gene encodes a member of the Ras superfamily of small guanosine triphosphate (GTP)-metabolizing proteins. The encoded protein localizes to the plasma membrane, where it regulates diverse processes, such as secretion, phagocytosis, and cell polarization. Activity of this protein is also involved in the generation of reactive oxygen species. Mutations in this gene are associated with neutrophil…
- **Diseases (Open Targets)**: neutrophil immunodeficiency syndrome (0.717); immunodeficiency 73b with defective neutrophil chemotaxis and lymphopenia (0.692); immunodeficiency 73c with defective neutrophil chemotaxis and hypogammaglobulinemia (0.585); T-B+ severe combined immunodeficiency (0.526); T-B- severe combined immunodeficiency (0.526)
- **Europe PMC papers**: 5552
- **Why important**: RAC2 is group enriched in bone marrow and lymphoid tissue and is associated with B-cell, megakaryocyte-progenitor and mast-cell populations. It regulates chemotaxis, actin organization, polarity, secretion, phagocytosis and reactive oxygen generation. Its strong STRING relationship with PRKCD provides one of the clearest known interaction links inside the module, and its disease associations include neutrophil immunodeficiency.
- **Conclusion**: Established evidence supports RAC2 as a hematopoietic and immune-cell cytoskeletal regulator. It makes a blood-cell contribution to the shared module plausible, especially in bone marrow. Whether the RAC2 signal reflects a conserved tissue program or shared immune-cell abundance cannot be resolved from the current module alone.

#### VHL

- **Related proteins** (co-abundance neighbors): ZNF384 (0.94), RAC2 (0.87), PLSCR1 (0.84), FBXO3 (0.84); STRING partners: PRKCD (0.757)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: von Hippel-Lindau tumor suppressor. This gene encodes a component of a ubiquitination complex. The encoded protein is involved in the ubiquitination and degradation of hypoxia-inducible-factor (HIF), which is a transcription factor that plays a central role in the regulation of gene expression by oxygen. In addition to oxygen-related gene expression, this protein plays a role in many other cellular processes including cilia formatio…
- **Diseases (Open Targets)**: von Hippel-Lindau disease (0.889); Chuvash polycythemia (0.794); pheochromocytoma (0.759); hereditary pheochromocytoma-paraganglioma (0.726); clear cell renal carcinoma (0.643)
- **Europe PMC papers**: 27012
- **Why important**: VHL occupies a connective position with ZNF384, RAC2, PLSCR1 and FBXO3 and has a reported STRING relationship with PRKCD. Its established role in an ubiquitination complex controlling HIF degradation links the module to oxygen-sensitive transcription, while its additional roles include cytokine signaling, senescence and extracellular-matrix regulation. It is detected in both tissues and has extensive disease literature.
- **Conclusion**: Established evidence supports VHL as a regulator of oxygen-responsive protein degradation and broader cellular signaling. Its placement near PRKCD and RAC2 makes stress and immune signaling a reasonable interpretive theme, but a direct hypoxia mechanism for this module remains unproven.

#### ROS1

- **Related proteins** (co-abundance neighbors): EYA3 (0.96), ACAD10 (0.94), SIGMAR1 (0.90), TIMM8B (0.88), STK3 (0.82), XTBD1 (0.81), THG1L (0.80); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ROS proto-oncogene 1, receptor tyrosine kinase. This proto-oncogene, highly-expressed in a variety of tumor cell lines, belongs to the sevenless subfamily of tyrosine kinase insulin receptor genes. The protein encoded by this gene is a type I integral membrane protein with tyrosine kinase activity. The protein may function as a growth or differentiation factor receptor. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.712); neoplasm (0.614); lung adenocarcinoma (0.590); cancer (0.543); lung carcinoma (0.432)
- **Europe PMC papers**: 16744
- **Why important**: ROS1 has high network connectivity relative to most module members and links EYA3, ACAD10, SIGMAR1, TIMM8B, STK3, XTBD1 and THG1L. It is group enriched in epididymis and lung, is not detected in immune cells according to HPA, and has extensive literature and disease associations involving receptor tyrosine-kinase signaling and cancer. Its presence broadens the module beyond a purely hematopoietic interpretation.
- **Conclusion**: Established evidence supports ROS1 as a receptor tyrosine kinase associated with growth, differentiation and epithelial or tumor biology. Its module membership may indicate a shared epithelial or signaling-state component, but the lack of STRING or hu.MAP support means that its mechanistic connection to the other module genes remains hypothetical.

## Module 2

**Tissue pair**: bone_marrow and colon  
**Genes (5)**: SERPINC1, APOA4, APOB, CFH, GC

### Function

The strongest interpretation is a circulating plasma-protein and blood-microparticle module with linked lipid-transport, complement-regulatory, glycosaminoglycan-binding, and coagulation functions. (GO:CC blood microparticle; q_global = 0.000806) identifies blood microparticle as the primary cellular-component signal, supported by APOA4, CFH, GC, and SERPINC1. The globally corrected molecular-function terms (GO:MF heparin binding; q_global = 0.00543), (GO:MF glycosaminoglycan binding; q_global = 0.0152), and (GO:MF sulfur compound binding; q_global = 0.047) converge on heparin, glycosaminoglycan, and sulfur-compound binding, driven by APOB, CFH, and SERPINC1. GC contributes vitamin-D transport; CFH regulates alternative-pathway complement activation; SERPINC1 inhibits thrombin and other coagulation proteases; APOB mediates lipoprotein transport; and APOA4 is an intestinally produced secreted apolipoprotein associated with lipid transport and mucosal innate immunity. Thus, the module is better viewed as a coordinated extracellular blood-protein signature than as a pathway operating primarily inside bone-marrow or colon cells.

**Cell composition.** All module genes are annotated as secreted to blood. HPA links most of the module to liver and hepatocytes, while APOB and APOA4 are linked to intestine and enterocytes. The module is therefore dominated by plasma or secreted proteins rather than tissue-resident proteins. Most genes are not detected in immune cells, with CFH showing immune-cell enhancement in MAIT T-cells. HPA protein detection is absent in bone marrow for the module and limited in colon, which argues against interpreting this as a locally synthesized bone-marrow or colon program. A plausible explanation is shared circulating-protein carryover, vascular or blood-microparticle content, or a shared extracellular compartment in the sampled tissues. The blood-microparticle annotation (GO:CC blood microparticle; q_global = 0.000806) and the secreted-protein STRING signal (STRING Keyword Secreted; within-query FDR = 6.16e-05) support this interpretation, but do not by themselves establish the source of the proteins in the tissue measurements.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 0.000806 | APOA4, CFH, GC, SERPINC1 |
| GO:MF heparin binding | 0.00543 | APOB, CFH, SERPINC1 |
| GO:MF glycosaminoglycan binding | 0.0152 | APOB, CFH, SERPINC1 |
| GO:MF sulfur compound binding | 0.047 | APOB, CFH, SERPINC1 |

### STRING and hu.MAP

STRING supports two high-confidence pairwise relationships within the module: the very strong APOA4--APOB association and the GC--SERPINC1 association. These relationships are consistent with known lipoprotein biology and with a circulating protein environment, respectively. The remaining co-abundance edges are not supported by high-confidence STRING pairwise interactions in the supplied evidence, so co-abundance should not be equated with direct physical binding. hu.MAP provides broader complex-level context: GC, APOA4, CFH, and SERPINC1 occur together in (hu.MAP huMAP3_15040.1); GC, APOA4, and CFH occur together in (hu.MAP huMAP3_10678.1); and GC and APOA4 occur together in (hu.MAP huMAP3_09434.1). The larger complexes contain many complement, coagulation, acute-phase, apolipoprotein, and plasma proteins. This supports a known extracellular plasma-protein neighborhood, while also indicating that the module is a selected substructure of broader complexes rather than a uniquely defined molecular complex.

**STRING interactions (score >= 0.7)**: 2 of 10 gene pairs: APOA4–APOB (0.992); GC–SERPINC1 (0.84)
**STRING functional enrichment (supplementary, within-query FDR)**: PMID (2021) Detection of Circulating Serum Protein Biomarkers of Non-Muscle Invasive Bladder Cancer after Protein Corona-Silver Nanoparticles Analysis by SWATH-MS. (FDR = 1.45e-05, 5 genes); Keyword Secreted (FDR = 6.16e-05, 5 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 6.63e-05, 5 genes); Component Blood microparticle (FDR = 0.00014, 4 genes); COMPARTMENTS Blood microparticle (FDR = 0.00015, 4 genes); PMID (2015) Effects of olanzapine on serum protein phosphorylation patterns in patients with schizophrenia. (FDR = 0.00017, 4 genes); PMID (2023) Serum proteome profiling of naturally acquired Babesia rossi infection in dogs. (FDR = 0.00038, 4 genes); PMID (2023) Comparative proteomics of proliferative diabetic retinopathy in people with Type 2 diabetes highlights the role of inflammation, visual transduction, and extracellular matrix pathways. (FDR = 0.00038, 4 genes); PMID (2023) Quantitative Proteomics of Maternal Blood Plasma in Isolated Intrauterine Growth Restriction. (FDR = 0.00038, 4 genes); PMID (2022) Systematic Review and Meta-Analysis on MS-Based Proteomics Applied to Human Peripheral Fluids to Assess Potential Biomarkers of Bipolar Disorder. (FDR = 0.00038, 4 genes); PMID (2022) Effects of Omega-3 and Antioxidant Cocktail Supplement on Prolonged Bed Rest: Results from Serum Proteome and Sphingolipids Analysis. (FDR = 0.00038, 4 genes); PMID (2021) Systemic Effects of Hemorrhagic Snake Venom Metalloproteinases: Untargeted Peptidomics to Explore the Pathodegradome of Plasma Proteins. (FDR = 0.00038, 4 genes); PMID (2020) Lipid mass spectrometry imaging and proteomic analysis of severe aortic stenosis. (FDR = 0.00038, 4 genes); PMID (2020) The Constitutive Proteome of Human Aqueous Humor and Race Specific Alterations. (FDR = 0.00038, 4 genes); PMID (2018) High density lipoprotein proteome is associated with cardiovascular risk factors and atherosclerosis burden as evaluated by coronary CT angiography. (FDR = 0.00038, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINC1, GC, APOA4, CFH; 4/64); huMAP3_10678.1 (GC, APOA4, CFH; 3/71); huMAP3_09434.1 (GC, APOA4; 2/33)

### Novelty

The underlying biology is not new: the module contains well-characterized plasma proteins, a known apolipoprotein relationship, a known GC--SERPINC1 relationship, and membership in established hu.MAP plasma-protein complexes. The STRING serum and plasma-proteomics annotations (STRING PMID (2021) Detection of Circulating Serum Protein Biomarkers of Non-Muscle Invasive Bladder Cancer after Protein Corona-Silver Nanoparticles Analysis by SWATH-MS.; within-query FDR = 1.45e-05) and (STRING PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers.; within-query FDR = 6.63e-05) through (STRING PMID (2018) High density lipoprotein proteome is associated with cardiovascular risk factors and atherosclerosis burden as evaluated by coronary CT angiography.; within-query FDR = 0.00038) further show that these proteins repeatedly appear together in circulating-protein studies. The exact conserved co-abundance module across bone marrow and colon may be a useful dataset-specific observation, but the supplied evidence does not establish it as a new biochemical pathway or novel protein complex. Absence of some pairwise STRING links or absence of APOB from the listed hu.MAP complexes cannot prove novelty, because co-abundance can arise from shared secretion, blood contamination, vesicles, or correlated tissue exposure. A stronger novelty claim would require independent tissue cohorts, control for plasma abundance and vascular content, and validation at the transcript, protein, and spatial levels.

**Hypothesis.** Hypothesis: this conserved module reflects a shared circulating extracellular compartment sampled by bone marrow and colon. Liver-derived GC, CFH, and SERPINC1, together with liver- and intestine-derived APOB and intestine-derived APOA4, may travel in plasma lipoproteins or blood microparticles and co-vary according to vascular exposure, lipid transport, complement regulation, and coagulation state. The APOA4--APOB relationship may represent a lipoprotein-associated component, while the GC--SERPINC1 relationship and the hu.MAP context may represent broader association with plasma protease-regulatory and complement-related assemblies. This is a hypothesis rather than proof of a direct common complex or of local production in either tissue.

### Important genes

#### GC

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.85), CFH (0.83), APOA4 (0.83); STRING partners: SERPINC1 (0.84)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09434.1
- **Function (MyGene.info)**: GC vitamin D binding protein. The protein encoded by this gene belongs to the albumin gene family. It is a multifunctional protein found in plasma, ascitic fluid, cerebrospinal fluid and on the surface of many cell types. It binds to vitamin D and its plasma metabolites and transports them to target tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq,…
- **Diseases (Open Targets)**: vitamin D deficiency (0.574); vitamin deficiency (0.552); chronic obstructive pulmonary disease (0.499); squamous cell carcinoma (0.339); central nervous system cancer (0.334)
- **Europe PMC papers**: 363974
- **Why important**: GC is the central network connector in the module, linking SERPINC1, CFH, and APOA4. It is liver-enriched, secreted to blood, present in all listed hu.MAP contexts, and participates in the primary blood-microparticle term (GO:CC blood microparticle; q_global = 0.000806). Its established vitamin-D binding and transport function provides a metabolic and extracellular transport axis. Its substantial literature and disease associations involving vitamin deficiency, pulmonary disease, and cancer make it an informative anchor for interpreting the module.
- **Conclusion**: Established evidence supports GC as a circulating transport protein and a network bridge connecting lipid-associated, complement-associated, and coagulation-associated proteins. The hypothesis that GC organizes or stabilizes the entire module is not established by the supplied co-abundance data.

#### CFH

- **Related proteins** (co-abundance neighbors): APOB (0.83), GC (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: complement factor H. This gene is a member of the Regulator of Complement Activation (RCA) gene cluster and encodes a protein with twenty short consensus repeat (SCR) domains. This protein is secreted into the bloodstream and has an essential role in the regulation of complement activation, restricting this innate defense mechanism to microbial infections. Mutations in this gene have been associated with hemolytic-ure…
- **Diseases (Open Targets)**: complement factor H deficiency (0.769); age-related macular degeneration (0.750); atypical hemolytic-uremic syndrome (0.729); age related macular degeneration 4 (0.711); Doyne honeycomb retinal dystrophy (0.688)
- **Europe PMC papers**: 9287
- **Why important**: CFH has strong network placement through links to APOB and GC and appears in every globally corrected enrichment term (GO:CC blood microparticle; q_global = 0.000806) through (GO:MF sulfur compound binding; q_global = 0.047). It is a secreted liver-associated regulator of complement activation and is linked to inflammatory and complement disease biology, including atypical hemolytic-uremic syndrome and macular degeneration. It also appears in the hu.MAP complexes (hu.MAP huMAP3_15040.1) and (hu.MAP huMAP3_10678.1), giving it a bridge between the blood-microparticle signal and broader complement-plasma assemblies.
- **Conclusion**: Established evidence supports CFH as the principal innate-immune and complement-regulatory component of the module. Its inclusion does not demonstrate active complement activation in either tissue; it may simply reflect circulating CFH abundance or blood-derived material.

#### SERPINC1

- **Related proteins** (co-abundance neighbors): GC (0.85); STRING partners: GC (0.84)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 is the module's coagulation-regulatory representative and participates in all globally corrected terms (GO:CC blood microparticle; q_global = 0.000806) through (GO:MF sulfur compound binding; q_global = 0.047). It is liver-enriched and secreted to blood, and its annotated heparin-binding domain and antithrombin activity directly explain the heparin-binding signal (GO:MF heparin binding; q_global = 0.00543). Its high-confidence STRING relationship with GC and membership in (hu.MAP huMAP3_15040.1) connect coagulation regulation to the broader plasma-protein context. Its extensive disease literature concerning antithrombin deficiency and venous thrombosis makes it biologically consequential despite its peripheral network position.
- **Conclusion**: Established evidence supports SERPINC1 as the coagulation and heparin-binding component of the module. The data do not show that the module represents a thrombogenic state or that SERPINC1 activity is altered in bone marrow or colon.

#### APOB

- **Related proteins** (co-abundance neighbors): CFH (0.83); STRING partners: APOA4 (0.992)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Vesicles, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein B. This gene product is the main apolipoprotein of chylomicrons and low density lipoproteins (LDL), and is the ligand for the LDL receptor. It occurs in plasma as two main isoforms, apoB-48 and apoB-100: the former is synthesized exclusively in the gut and the latter in the liver. The intestinal and the hepatic forms of apoB are encoded by a single gene from a single, very long mRNA. The two isoforms…
- **Diseases (Open Targets)**: hypercholesterolemia, autosomal dominant, type B (0.814); Hypercholesterolemia (0.812); familial hypobetalipoproteinemia 1 (0.803); familial hypercholesterolemia (0.780); metabolic disease (0.729)
- **Europe PMC papers**: 28452
- **Why important**: APOB contributes the strongest lipid-transport interpretation and connects to CFH in the co-abundance graph while also having a high-confidence STRING relationship with APOA4. It is associated with both intestine and liver, is secreted to blood, and encodes the principal structural apolipoprotein of chylomicron and LDL particles. Its presence in (GO:MF heparin binding; q_global = 0.00543), (GO:MF glycosaminoglycan binding; q_global = 0.0152), and (GO:MF sulfur compound binding; q_global = 0.047) links lipoprotein biology to the module's glycosaminoglycan- and sulfur-compound-binding signals. APOB has a very large literature and well-established associations with hypercholesterolemia and familial lipid disorders.
- **Conclusion**: Established evidence supports APOB as the lipoprotein-associated component that helps explain why the module is shared between an intestinally relevant tissue and a vascularly exposed tissue. The module does not establish altered lipid metabolism in either tissue or prove that APOB directly binds CFH.

#### APOA4

- **Related proteins** (co-abundance neighbors): GC (0.83); STRING partners: APOB (0.992)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09434.1
- **Function (MyGene.info)**: apolipoprotein A4. Apoliprotein (apo) A-IV gene contains 3 exons separated by two introns. A sequence polymorphism has been identified in the 3'UTR of the third exon.  The primary translation product is a 396-residue preprotein which after proteolytic processing is secreted its primary site of synthesis, the intestine, in association with chylomicron particles.  Although its precise function is not known, apo A-IV i…
- **Diseases (Open Targets)**: tubulointerstitial kidney disease, autosomal dominant, 2 (0.482); AL amyloidosis (0.463); metabolic syndrome (0.425); familial hyperlipidemia (0.359); diabetes mellitus (0.336)
- **Europe PMC papers**: 4955
- **Why important**: APOA4 is intestine-enriched, enterocyte-associated, secreted to blood, and connected to APOB by a very high-confidence STRING relationship. It occurs in all listed hu.MAP complexes and contributes to the blood-microparticle term (GO:CC blood microparticle; q_global = 0.000806). Its known association with intestinal secretion, lipid transport, cholesterol biology, and mucosal innate immune response makes it the clearest tissue-linked complement to the liver-derived proteins. Its substantial literature and metabolic disease associations support its use as an important marker of the intestinal and lipoprotein side of the module.
- **Conclusion**: Established evidence supports APOA4 as an intestinally derived, lipoprotein-associated secreted protein within a broader plasma signature. Its presence does not demonstrate local APOA4 production in colon, because the HPA evidence identifies intestine and enterocytes rather than colon tissue itself.

## Module 3

**Tissue pair**: bone_marrow and colon  
**Genes (15)**: AP5Z1, CCNY, CYLD, DIS3L, PDSS2, ERO1B, FAM120C, FAM184A, FBXO6, FPGS, LIMK1, RPUSD4, SACS, TRAPPC11, WDFY2

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established pathway assignment from primary enrichment evidence. Its genes instead span several cellular processes, including ubiquitin-dependent proteolysis and DNA repair through FBXO6, folate homeostasis and proliferation through FPGS, endoplasmic-reticulum protein folding through ERO1B, coenzyme Q biosynthesis through PDSS2, RNA turnover through DIS3L, cytoskeletal and signaling regulation through LIMK1 and CYLD, and intracellular trafficking through TRAPPC11 and AP5Z1. The network therefore appears functionally heterogeneous rather than a clearly defined canonical pathway. The supplementary STRING signal (STRING NetworkNeighborAL Mixed, incl. Cyclin-dependent protein kinase holoenzyme complex, and Dual specificity phosphatase, catalytic domain; within-query FDR = 0.021) links WDFY2, CCNY, and SACS to a mixed cyclin-dependent kinase and dual-specificity-phosphatase-related annotation, but this is supplementary evidence and does not establish a module-wide function.

**Cell composition.** The HPA profile argues against a module dominated by plasma or secreted proteins: secreted proteins are a minority, most genes have low tissue specificity, and most have low immune-cell specificity. A subset has cell-type-enhanced patterns involving neutrophils, megakaryocytes, Hofbauer cells, myonuclei, pancreatic acinar cells, or spermatids, but these patterns are diverse rather than consistent with one shared blood-cell population. CYLD and CCNY show neutrophil-related HPA signals, while several genes are detected in both bone marrow and colon. Overall, the shared module may reflect broadly expressed intracellular programs, mixed cellular composition, or coordinated sample-state effects rather than a specialized bone-marrow or colon lineage program. HPA protein detection is broader in colon than in bone marrow, and absence of detection for individual genes should not be interpreted as absence of transcription or function.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING reports no high-confidence pairwise interactions among the module genes. The only STRING functional annotation is the supplementary mixed annotation (STRING NetworkNeighborAL Mixed, incl. Cyclin-dependent protein kinase holoenzyme complex, and Dual specificity phosphatase, catalytic domain; within-query FDR = 0.021), involving WDFY2, CCNY, and SACS; it does not demonstrate direct physical binding or a coherent shared complex. hu.MAP provides one partial complex observation (hu.MAP huMAP3_12776.1), in which FPGS and PDSS2 occur together with ALAS1, THEM4, and PDSS1. This is the clearest known complex-level relationship in the module, but only a subset of its members is present, so it supports a possible connection between folate-related and mitochondrial or metabolic biology rather than a complete module mechanism. The absence of STRING interactions and the limited hu.MAP overlap indicate that most module edges are not established physical interactions.

**STRING interactions (score >= 0.7)**: 0 of 105 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Mixed, incl. Cyclin-dependent protein kinase holoenzyme complex, and Dual specificity phosphatase, catalytic domain (FDR = 0.021, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12776.1 (FPGS, PDSS2; 2/5)

### Novelty

The co-abundance pattern appears unusual relative to the interaction and complex resources because most module relationships are absent from STRING and hu.MAP, and no GO/KEGG term passed global correction. That combination makes the module a potentially novel transcriptomic or proteomic association pattern, but it is not sufficient to claim a new biological complex or pathway. The heterogeneous annotations, low tissue specificity for most genes, and lack of a coherent enrichment result provide alternative explanations such as shared regulation, sample composition, cellular stress, or correlated abundance effects. Novelty should therefore be stated as a candidate observation requiring replication, tissue-cell deconvolution, independent cohorts, and perturbational or biochemical validation.

**Hypothesis.** Hypothesis: the module may represent a context-dependent intracellular homeostasis program that combines proteostasis and trafficking with nucleotide and mitochondrial metabolism. In this model, FBXO6, ERO1B, TRAPPC11, and SACS could reflect protein quality-control or secretory-system state, while FPGS and PDSS2 could reflect demands for folate-dependent biosynthesis and respiratory-chain support. CYLD, LIMK1, and CCNY could connect this state to inflammatory, cytoskeletal, or proliferative signaling. The hypothesis is deliberately provisional: the absence of STRING support, the lack of globally significant GO/KEGG enrichment, and the mixed HPA cell-type signals mean that coordinated regulation or shared sample composition may explain the co-abundance pattern without direct molecular interaction.

### Important genes

#### FBXO6

- **Related proteins** (co-abundance neighbors): FAM120C (0.94), ERO1B (0.89), DIS3L (0.85), AP5Z1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: F-box protein 6. This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls…
- **Diseases (Open Targets)**: iron metabolism disease (0.088); ovarian cancer (0.077); ovarian carcinoma (0.077); osteoarthritis (0.075); tuberculosis (0.056)
- **Europe PMC papers**: 432
- **Why important**: FBXO6 is among the more connected genes in the module and links FAM120C, ERO1B, DIS3L, and AP5Z1, making it a network hub that spans otherwise distinct portions of the graph. Its established F-box role places it in phosphorylation-dependent ubiquitination, proteolysis, DNA-damage checkpoint signaling, and DNA repair. It is broadly detected in the relevant tissues, has substantial literature, and has disease associations including iron-metabolism disease and osteoarthritis.
- **Conclusion**: Established evidence supports FBXO6 as a proteostasis and ubiquitin-system component with a central network position. It is a plausible coordinator or marker of the module, but the module data do not establish that FBXO6 physically regulates the other members or drives the shared abundance pattern.

#### FPGS

- **Related proteins** (co-abundance neighbors): CYLD (0.86), SACS (0.84), ERO1B (0.84), WDFY2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_12776.1
- **Function (MyGene.info)**: folylpolyglutamate synthase. This gene encodes the folylpolyglutamate synthetase enzyme. This enzyme has a central role in establishing and maintaining both cytosolic and mitochondrial folylpolyglutamate concentrations and, therefore, is essential for folate homeostasis and the survival of proliferating cells. This enzyme catalyzes the ATP-dependent addition of glutamate moieties to folate and folate derivatives. Alternative …
- **Diseases (Open Targets)**: telangiectasia, hereditary hemorrhagic, type 1 (0.425); device complication (0.070); arthropathy (0.070); acute lymphoblastic leukemia (0.054); leukemia (0.036)
- **Europe PMC papers**: 5024
- **Why important**: FPGS is a highly connected module gene and connects CYLD, SACS, ERO1B, and WDFY2. Its folylpolyglutamate synthetase activity is central to cytosolic and mitochondrial folate homeostasis and is important for proliferating cells. It also participates in the partial hu.MAP complex (hu.MAP huMAP3_12776.1) with PDSS2, giving it the strongest direct complex-level support in the module. Its disease associations include hereditary hemorrhagic telangiectasia and leukemia-related phenotypes, and it has extensive literature.
- **Conclusion**: Established evidence supports FPGS as a core metabolic enzyme with relevance to folate supply and proliferation, and (hu.MAP huMAP3_12776.1) supports a known complex relationship with PDSS2. It remains uncertain whether folate metabolism explains the whole module or merely one segment of the network.

#### ERO1B

- **Related proteins** (co-abundance neighbors): FBXO6 (0.89), LIMK1 (0.86), FPGS (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: endoplasmic reticulum oxidoreductase 1 beta. Enables thiol oxidase activity. Involved in protein folding in endoplasmic reticulum. Predicted to be located in membrane. Predicted to be active in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: alcohol drinking (0.198); urolithiasis (0.198); type 2 diabetes mellitus (0.167); ovarian dysfunction (0.153); Developmental cataract (0.118)
- **Europe PMC papers**: 254
- **Why important**: ERO1B occupies a connecting position between FBXO6, LIMK1, and FPGS. It is an endoplasmic-reticulum thiol oxidase involved in protein folding, the unfolded-protein response, and insulin processing. Its pancreas-enriched tissue profile and acinar and islet cell associations contrast with the broad tissue profile of many other module genes, making it informative for assessing cell-state or sample-composition explanations. It has disease associations involving diabetes, urolithiasis, and developmental cataract.
- **Conclusion**: Established evidence supports ERO1B as an endoplasmic-reticulum folding and redox component. Its inclusion could indicate proteostasis or secretory-system activity, but the HPA pattern also raises the possibility that its co-abundance reflects particular cell populations rather than a conserved cross-tissue mechanism.

#### PDSS2

- **Related proteins** (co-abundance neighbors): FAM184A (0.89), LIMK1 (0.82), CYLD (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: huMAP3_12776.1
- **Function (MyGene.info)**: decaprenyl diphosphate synthase subunit 2. The protein encoded by this gene is an enzyme that synthesizes the prenyl side-chain of coenzyme Q, or ubiquinone, one of the key elements in the respiratory chain. The gene product catalyzes the formation of all trans-polyprenyl pyrophosphates from isopentyl diphosphate in the assembly of polyisoprenoid side chains, the first step in coenzyme Q biosynthesis. Defects in this gene are a cause of co…
- **Diseases (Open Targets)**: coenzyme Q10 deficiency, primary, 3 (0.765); neurodegenerative disease (0.534); Leigh syndrome (0.418); coenzyme Q10 deficiency (0.372); lymphoid leukemia (0.344)
- **Europe PMC papers**: 805
- **Why important**: PDSS2 is a connected metabolic gene linking FAM184A, LIMK1, and CYLD and is one of the two module members in the hu.MAP complex (hu.MAP huMAP3_12776.1). It catalyzes a key step in coenzyme Q side-chain synthesis, connecting the module to mitochondrial respiratory function. Its disease associations include primary coenzyme Q deficiency, Leigh syndrome, neurodegenerative disease, and lymphoid leukemia, with a substantial literature base.
- **Conclusion**: Established evidence supports PDSS2 as a mitochondrial coenzyme Q biosynthesis enzyme and supports its complex-level relationship with FPGS through (hu.MAP huMAP3_12776.1). A mitochondrial-metabolic contribution to the module is plausible, but no globally significant enrichment or interaction evidence shows that PDSS2 defines the module.

#### CYLD

- **Related proteins** (co-abundance neighbors): FPGS (0.86), PDSS2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Centriolar satellite; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CYLD lysine 63 deubiquitinase. This gene is encodes a cytoplasmic protein with three cytoskeletal-associated protein-glycine-conserved (CAP-GLY) domains that functions as a deubiquitinating enzyme. Mutations in this gene have been associated with cylindromatosis, multiple familial trichoepithelioma, and Brooke-Spiegler syndrome. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. [pr…
- **Diseases (Open Targets)**: Brooke-Spiegler syndrome (0.753); familial cylindromatosis (0.724); frontotemporal dementia and/or amyotrophic lateral sclerosis (0.682); familial multiple trichoepithelioma (0.598); trichoepithelioma, multiple familial, 1 (0.514)
- **Europe PMC papers**: 5773
- **Why important**: CYLD links FPGS and PDSS2 and is tissue-enhanced in bone marrow with a neutrophil-associated HPA pattern. It is a deubiquitinase involved in regulation of tumor-necrosis-factor signaling, type-one interferon production, innate receptor signaling, and canonical NF-kappa-B signaling. It has extensive disease evidence, particularly for Brooke-Spiegler syndrome, familial cylindromatosis, and related tumor phenotypes.
- **Conclusion**: Established evidence supports CYLD as an immune and signaling regulator with a plausible connection to the bone-marrow context. Its network placement could connect metabolic and inflammatory states, but the available data do not establish immune activation as the module’s primary function, especially because most genes have low immune-cell specificity.

## Module 4

**Tissue pair**: bone_marrow and colon  
**Genes (5)**: APOC2, ASL, C4BPA, CP, ITIH2

### Function

The strongest globally corrected functional interpretation is a blood-microparticle-associated module (GO:CC blood microparticle; q_global = 0.0417). Its genes point to a circulating liver-derived protein program involving extracellular matrix stabilization and protease inhibition through ITIH2, complement regulation through C4BPA, copper and iron handling through CP, lipid transport and triglyceride metabolism through APOC2, and hepatic nitrogen metabolism through ASL. The pattern is therefore best interpreted as a plasma or blood-microparticle-associated metabolic, immune-regulatory, and extracellular-environment module rather than as a coherent intracellular pathway. The STRING-derived observations support secreted, plasma, blood-microparticle, complement, coagulation, and protein-lipid themes (4 supplementary STRING terms; within-query FDR 0.0071–0.0235), but these are supplementary evidence rather than globally corrected enrichment. The lack of a significant within-module GO or KEGG term does not invalidate the module; it indicates that the module is biologically heterogeneous and small.

**Cell composition.** The module is dominated by liver-enriched genes in HPA, and most of its proteins are secreted to blood. HPA reports no protein detection in bone marrow for the module and detection of only ASL in colon, with the remaining proteins not detected there. This strongly suggests that the shared bone-marrow and colon signal may reflect circulating plasma proteins, blood microparticles, sample exposure to blood, or a systemic liver-derived state rather than local expression by bone-marrow or colon cells. The module is not uniformly blood-cell enriched: APOC2 is immune-cell enriched in NK cells and C4BPA in neutrophils, whereas ITIH2 and CP are not detected in immune cells and ASL has low immune-cell specificity. ASL has colonocyte and intestinal epithelial enhancement, providing a possible local colon contribution, but the overall composition is more consistent with a secreted plasma program than with a tissue-resident cellular module.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 0.0417 | C4BPA, CP, ITIH2 |

### STRING and hu.MAP

No high-confidence STRING relationship is present among the module genes, so STRING does not provide direct interaction support for the co-abundance edges. In contrast, hu.MAP repeatedly places CP, C4BPA, and ITIH2 together in broad plasma, complement, coagulation, and extracellular-protein complexes (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1). These repeated complex memberships indicate that part of the module recapitulates known biochemical co-occurrence or shared plasma-complex context. APOC2 and ASL have no listed hu.MAP complex membership, and APOC2, ASL, and the other module genes have no listed STRING partners. Thus, the network is stronger as a coordinated abundance signature than as evidence for a single physical molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: PMID (2018) Obesity shows preserved plasma proteome in large independent clinical cohorts. (FDR = 0.003, 4 genes); PMID (2022) The Aging Features of Thyrotoxicosis Mice: Malnutrition, Immunosenescence and Lipotoxicity. (FDR = 0.0059, 4 genes); Keyword Secreted (FDR = 0.0071, 4 genes); PMID (2020) Revelation of Proteomic Indicators for Colorectal Cancer in Initial Stages of Development. (FDR = 0.0098, 4 genes); NetworkNeighborAL Complement and coagulation cascades, and Protein-lipid complex (FDR = 0.021, 3 genes); Component Blood microparticle (FDR = 0.0215, 3 genes); TISSUES Plasma cell (FDR = 0.0233, 3 genes); COMPARTMENTS Blood microparticle (FDR = 0.0235, 3 genes); PMID (2020) Identification of Putative Early Atherosclerosis Biomarkers by Unsupervised Deconvolution of Heterogeneous Vascular Proteomes. (FDR = 0.0264, 3 genes); PMID (2019) Analysis of Differentially Expressed Genes in Coronary Artery Disease by Integrated Microarray Analysis. (FDR = 0.0264, 4 genes); Keyword Signal (FDR = 0.0333, 4 genes); PMID (2023) Integrating Proteomics and Lipidomics for Evaluating the Risk of Breast Cancer Progression: A Pilot Study. (FDR = 0.0378, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09273.1 (CP, C4BPA, ITIH2; 3/28); huMAP3_08395.1 (CP, C4BPA, ITIH2; 3/43); huMAP3_09531.1 (CP, C4BPA, ITIH2; 3/47); huMAP3_10101.1 (CP, C4BPA, ITIH2; 3/49); huMAP3_15040.1 (CP, C4BPA, ITIH2; 3/64); huMAP3_10678.1 (CP, C4BPA, ITIH2; 3/71); huMAP3_02236.1 (CP, ITIH2; 2/7); huMAP3_07541.1 (C4BPA, ITIH2; 2/19); huMAP3_07265.1 (CP, ITIH2; 2/20); huMAP3_07701.1 (C4BPA, ITIH2; 2/22)

### Novelty

The module should not be presented as a newly discovered molecular complex or pathway. Its central biological pattern is already anticipated by known functions of secreted liver proteins and by the repeated hu.MAP association of CP, C4BPA, and ITIH2 with broad plasma-related complexes. The shared bone-marrow and colon co-abundance pattern may still be a useful context-specific observation, especially if it is reproducible and robust to adjustment for blood contamination and systemic effects. However, the absence of STRING edges or the absence of a hu.MAP entry for the complete module does not establish novelty. The most defensible conclusion is contextual novelty of the co-abundance signature, not novelty of the underlying protein biology.

**Hypothesis.** Hypothesis: this conserved module reflects a circulating liver-derived plasma or blood-microparticle program that links complement regulation, extracellular-matrix and protease control, metal-dependent redox biology, lipid transport, and hepatic metabolism. In bone marrow and colon datasets, shared variation in plasma exposure, vascular permeability, inflammation, nutritional state, or systemic metabolic status could produce the coordinated abundance pattern. ASL may additionally capture a colon epithelial contribution, whereas the secreted proteins may mainly represent the extracellular compartment rather than transcription within the sampled tissues. This hypothesis should be tested by adjusting for plasma-protein abundance and blood contamination, examining paired tissue and plasma measurements, and checking whether the module persists within purified tissue cell populations.

### Important genes

#### ITIH2

- **Related proteins** (co-abundance neighbors): C4BPA (0.86), CP (0.80), APOC2 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09273.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_02236.1, huMAP3_07541.1, huMAP3_07265.1, huMAP3_07701.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 2. The inter-alpha-trypsin inhibitors (ITI) are a family of structurally related plasma serine protease inhibitors involved in extracellular matrix stabilization and in prevention of tumor metastasis. The ITI family contains multiple proteins made up of a light chain (see MIM 176870) and a variable number of heavy chains (Salier et al., 1987 [PubMed 2446322]; Himmelfarb et al., 2004 [PubMed 14744536]…
- **Diseases (Open Targets)**: acute tonsillitis (0.357); neurodegenerative disease (0.332); type 2 diabetes mellitus (0.231); non-alcoholic fatty liver (0.231); adverse effect (0.213)
- **Europe PMC papers**: 1020
- **Why important**: ITIH2 is the most connected and strongest node in the module, linking C4BPA, CP, and APOC2. It is liver-enriched, secreted to blood, contributes to the globally significant blood-microparticle term (GO:CC blood microparticle; q_global = 0.0417), and is present in every listed hu.MAP complex containing module members (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_02236.1) (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_07701.1). Its established function in extracellular-matrix stabilization and prevention of tumor metastasis gives it a plausible extracellular organizing role. It also has broad disease associations and substantial literature support, while the supplementary STRING results repeatedly place it in plasma, blood-microparticle, complement, coagulation, and protein-lipid contexts (12 supplementary STRING terms; within-query FDR 0.003–0.0378).
- **Conclusion**: Established evidence supports ITIH2 as the principal network and extracellular-plasma marker of the module. It is a strong candidate for tracking the module, but its centrality does not prove that it causally organizes the other proteins. The hypothesis that ITIH2 helps coordinate the shared extracellular state remains to be tested.

#### C4BPA

- **Related proteins** (co-abundance neighbors): ITIH2 (0.86); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09273.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07541.1, huMAP3_07701.1
- **Function (MyGene.info)**: complement component 4 binding protein alpha. This gene encodes a member of a superfamily of proteins composed predominantly of tandemly arrayed short consensus repeats of approximately 60 amino acids. Along with a single, unique beta-chain, seven identical alpha-chains encoded by this gene assemble into the predominant isoform of C4b-binding protein, a multimeric protein that controls activation of the complement cascade through the classica…
- **Diseases (Open Targets)**: venous thromboembolism (0.445); dengue disease (0.370); Thromboembolism (0.332); Alzheimer disease (0.246); Parkinson disease (0.243)
- **Europe PMC papers**: 1611
- **Why important**: C4BPA is one of the genes in the globally corrected blood-microparticle term (GO:CC blood microparticle; q_global = 0.0417), is liver-enriched and secreted to blood, and is repeatedly grouped with ITIH2 and CP in hu.MAP complexes (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_07701.1). Its established role is regulation of classical complement activation and immune responses. It is also associated with thromboembolic and neurodegenerative disease contexts and has substantial literature support. Supplementary STRING results consistently connect it to plasma, complement, coagulation, and blood-microparticle themes (11 supplementary STRING terms; within-query FDR 0.003–0.0333).
- **Conclusion**: Established evidence identifies C4BPA as the clearest immune-regulatory component of the module and supports a circulating complement-related interpretation. It may contribute to the module's relationship with inflammation or vascular biology, but a causal role in the cross-tissue co-abundance pattern is only a hypothesis.

#### CP

- **Related proteins** (co-abundance neighbors): ITIH2 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09273.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_02236.1, huMAP3_07265.1
- **Function (MyGene.info)**: ceruloplasmin. The protein encoded by this gene is a metalloprotein that binds most of the copper in plasma and is involved in the peroxidation of Fe(II)transferrin to Fe(III) transferrin. Mutations in this gene cause aceruloplasminemia, which results in iron accumulation and tissue damage, and is associated with diabetes and neurologic abnormalities. Two transcript variants, one protein-coding and the other not…
- **Diseases (Open Targets)**: aceruloplasminemia (0.827); cerebellar ataxia (0.572); Hermansky-Pudlak syndrome 3 (0.564); Hermansky-Pudlak syndrome (0.543); neurodegeneration with brain iron accumulation (0.510)
- **Europe PMC papers**: 171928
- **Why important**: CP is part of the globally corrected blood-microparticle term (GO:CC blood microparticle; q_global = 0.0417), is liver-enriched and secreted to blood, and repeatedly co-occurs with C4BPA and ITIH2 in hu.MAP complexes (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_02236.1) (hu.MAP huMAP3_07265.1). Its established function in copper binding, iron oxidation, and oxidant detoxification provides a metal-handling and redox dimension that complements the complement and extracellular-matrix signals. CP has extensive literature support and strong disease relevance through aceruloplasminemia, iron accumulation, diabetes, and neurological abnormalities. The supplementary STRING evidence repeatedly places it in plasma and blood-microparticle contexts (10 supplementary STRING terms; within-query FDR 0.003–0.0378).
- **Conclusion**: Established evidence supports CP as the module's metal and redox component and as a marker of circulating plasma biology. Its coordinated abundance could reflect systemic inflammatory, vascular, or metabolic state, but the module does not establish which of these states is responsible.

#### APOC2

- **Related proteins** (co-abundance neighbors): ASL (0.82), ITIH2 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein C2. This gene encodes a lipid-binding protein belonging to the apolipoprotein gene family. The protein is secreted in plasma where it is a component of very low density lipoprotein. This protein activates the enzyme lipoprotein lipase, which hydrolyzes triglycerides and thus provides free fatty acids for cells. Mutations in this gene cause hyperlipoproteinemia type IB, characterized by hypertriglyceri…
- **Diseases (Open Targets)**: familial apolipoprotein C-II deficiency (0.774); Hyperlipoproteinemia type 1 (0.665); Abnormality of the cardiovascular system (0.466); amyloidosis (0.388); familial chylomicronemia syndrome (0.383)
- **Europe PMC papers**: 3747
- **Why important**: APOC2 connects the central ITIH2 node to ASL and is the module's clearest lipid-metabolism component. It is liver-enriched, secreted to blood, and immune-cell enriched in NK cells according to HPA. Its established role as a plasma lipoprotein component and activator of lipoprotein lipase explains the supplementary associations with plasma proteomes, lipid-related contexts, cardiovascular disease, and protein-lipid complexes (8 supplementary STRING terms; within-query FDR 0.003–0.0378). It has a well-established disease connection to apolipoprotein C-II deficiency, hyperlipoproteinemia, pancreatitis, and atherosclerosis, with extensive literature support.
- **Conclusion**: Established evidence supports APOC2 as a lipid-transport and triglyceride-processing marker within the module. It may indicate systemic lipid status or lipoprotein exposure in the tissue samples, but the network does not show that APOC2 directly regulates the other module members.

#### ASL

- **Related proteins** (co-abundance neighbors): APOC2 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: argininosuccinate lyase. This gene encodes a member of the lyase 1 family. The encoded protein forms a cytosolic homotetramer and primarily catalyzes the reversible hydrolytic cleavage of argininosuccinate into arginine and fumarate, an essential step in the liver in detoxifying ammonia via the urea cycle. Mutations in this gene result in the autosomal recessive disorder argininosuccinic aciduria, or argininosuccinic acid…
- **Diseases (Open Targets)**: argininosuccinic aciduria (0.866); hereditary disease (0.508); neurodevelopmental disorder (0.436); dystonic disorder (0.370); Tremor (0.370)
- **Europe PMC papers**: 13702
- **Why important**: ASL is connected to APOC2 and is the only module gene with HPA protein detection in colon. It is enhanced in colonocytes and several intestinal epithelial cell types as well as hepatocytes, unlike the predominantly secreted plasma proteins. Its established function in the urea cycle, arginine metabolism, and arginine biosynthesis gives the module a possible tissue-metabolic component. ASL has very extensive literature support and strong disease relevance through argininosuccinic aciduria and related hereditary and neurodevelopmental disorders.
- **Conclusion**: Established evidence supports ASL as the best candidate for a local colon epithelial or hepatic metabolic contribution. Its presence does not demonstrate that the whole module is produced locally in colon or bone marrow. The hypothesis that ASL links epithelial metabolism to the circulating lipid and plasma-protein signal requires tissue-specific validation.

## Module 5

**Tissue pair**: bone_marrow and colon  
**Genes (9)**: GRAMD1C, BCAT2, CBX5, FOCAD, AGL, GPRIN3, LYN, NEK9, PCNP

### Function

This is a heterogeneous co-abundance module rather than a clearly established pathway module. No GO or KEGG term passed global correction, so there is no globally supported pathway-level enrichment to assign. The individual gene annotations span branched-chain amino-acid metabolism through BCAT2, glycogen metabolism through AGL, intracellular cholesterol transport through GRAMD1C, ubiquitin-dependent protein turnover through PCNP, chromatin organization through CBX5, mitotic regulation through NEK9, and immune-cell signaling through LYN. GPRIN3 is the central network node, but its own annotation is neuronal projection development and it lacks detected protein in both profiled tissues. Taken together, the module is best interpreted as a shared expression program involving cellular metabolism, nuclear regulation, membrane signaling, and cell-state composition, rather than as evidence for a single conserved biochemical function.

**Cell composition.** The module is not dominated by plasma or secreted proteins; the HPA summary reports no secreted genes. It is also not broadly blood-cell specific: most genes have low immune-cell specificity, with GRAMD1C showing group enrichment in memory B cells, naive B cells, and neutrophils, and LYN showing neutrophil enrichment. Instead, the genes have diverse tissue and cell-type patterns, including choroid plexus, skeletal muscle, tongue, brain, astrocytes, pituitary cell types, and glial populations. LYN is the clearest bone-marrow or immune-associated component. Protein detection differs between bone marrow and colon, while several genes are detected in colon or in both tissues and others are not detected in either tissue. This mixture argues against a simple secreted-protein module and is compatible with shared cell types, variable cellular composition, or coordinated expression of unrelated cell-state programs in the two tissue groups.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes, no STRING functional enrichment, and no hu.MAP complex containing multiple module members. The co-abundance edges therefore should not be treated as established physical interactions, shared complex membership, or experimentally supported pathway links. The absence of STRING and hu.MAP support makes the central position of GPRIN3 a statistical expression-network observation rather than evidence that GPRIN3 physically binds the peripheral genes. Known biology remains present at the individual-gene level, especially the established enzymatic role of BCAT2, the glycogen-debranching role of AGL, the cholesterol-transfer annotation of GRAMD1C, the chromatin role of CBX5, and the signaling role of LYN.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may represent a previously uncharacterized co-abundance association, because the specific gene set has no high-confidence STRING links, no multi-member hu.MAP complex, and no globally significant GO or KEGG enrichment. However, those database absences do not establish novelty. Several component genes and their individual functions are already well studied, and the observed pattern could arise from tissue composition, cell-state variation, or technical features of cross-tissue expression. The appropriate conclusion is therefore that the joint co-abundance pattern is a candidate novel observation requiring replication and validation, not that the underlying biology or gene functions are novel.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state or composition signal present in both bone marrow and colon, in which a small immune-associated component centered on LYN co-varies with metabolic, membrane, chromatin, and cell-cycle genes in particular cell populations. A possible biological interpretation is coordinated variation in cellular activation or turnover, with LYN marking immune signaling, BCAT2 and AGL marking nutrient and energy metabolism, GRAMD1C marking membrane cholesterol handling, and CBX5 or NEK9 marking nuclear or proliferative state. This is a hypothesis only: the lack of global enrichment, STRING support, and hu.MAP support means that direct molecular coupling has not been demonstrated.

### Important genes

#### GPRIN3

- **Related proteins** (co-abundance neighbors): BCAT2 (0.93), AGL (0.87), PCNP (0.85), FOCAD (0.81), LYN (0.81), NEK9 (0.81), CBX5 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GPRIN family member 3. Predicted to be involved in neuron projection development. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: cystic kidney disease (0.317); Genetic renal or urinary tract malformation (0.298); ovarian dysfunction (0.282); DNA methylation (0.281); neurodegenerative disease (0.280)
- **Europe PMC papers**: 237
- **Why important**: GPRIN3 is the central and most highly connected node in the co-abundance subgraph, linking BCAT2, AGL, PCNP, FOCAD, LYN, NEK9, and CBX5. That network position makes it important for understanding why the module was detected, even though it has no STRING or hu.MAP support, no globally enriched term, and no detected HPA protein in bone marrow or colon. Its supplied annotation concerns predicted neuron projection development, and its disease associations are comparatively tentative. The literature volume is limited relative to heavily studied kinases and metabolic enzymes.
- **Conclusion**: Established evidence supports GPRIN3 as a statistical hub of this module, not as a proven molecular organizer. Its role in the shared tissue program remains hypothetical and should be tested independently at the transcript and protein levels.

#### LYN

- **Related proteins** (co-abundance neighbors): GPRIN3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enhanced; location Plasma membrane; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LYN proto-oncogene, Src family tyrosine kinase. This gene encodes a tyrosine protein kinase, which maybe involved in the regulation of mast cell degranulation, and erythroid differentiation. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2011].
- **Diseases (Open Targets)**: autoinflammatory disease, systemic, with vasculitis (0.712); chronic myeloid leukemia (0.601); cancer (0.569); acute lymphoblastic leukemia (0.562); neurodegenerative disease (0.528)
- **Europe PMC papers**: 15695
- **Why important**: LYN is the most biologically direct link to the bone-marrow context and is enriched in neutrophils, with tissue enhancement in bone marrow and lymphoid tissue. It is a Src-family tyrosine kinase with supplied roles in cytokine regulation, B-cell homeostasis, mast-cell degranulation, and erythroid differentiation. It is connected to GPRIN3 in the module and has the largest literature volume among the listed genes, together with disease associations in inflammatory disease, leukemia, and cancer.
- **Conclusion**: Established evidence supports LYN as an immune and hematopoietic signaling marker that could explain part of the shared co-abundance pattern. It does not establish that LYN directly regulates the other module genes, because neither STRING nor hu.MAP supports such coupling.

#### BCAT2

- **Related proteins** (co-abundance neighbors): GPRIN3 (0.93), GRAMD1C (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: branched chain amino acid transaminase 2. This gene encodes a branched chain aminotransferase found in mitochondria. The encoded protein forms a dimer that catalyzes the first step in the production of the branched chain amino acids leucine, isoleucine, and valine. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: hypervalinemia and hyperleucine-isoleucinemia (0.688); neurodegenerative disease (0.236); pancreatic ductal adenocarcinoma (0.104); neoplasm (0.097); cancer (0.091)
- **Europe PMC papers**: 1446
- **Why important**: BCAT2 is a mitochondrial branched-chain amino-acid aminotransferase and is the metabolic partner most directly connected to the central GPRIN3 node while also connecting to GRAMD1C. Its annotation supports branched-chain amino-acid catabolism and biosynthesis, and its disease associations include hypervalinemia and hyperleucine-isoleucinemia. It has a substantial literature base and is detected by HPA in colon but not bone marrow.
- **Conclusion**: Established evidence supports BCAT2 as a genuine metabolic component of the module. The shared expression with LYN or GPRIN3 is an association rather than evidence that immune signaling directly controls branched-chain amino-acid metabolism in these tissues.

#### AGL

- **Related proteins** (co-abundance neighbors): GPRIN3 (0.87); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: amylo-alpha-1,6-glucosidase and 4-alpha-glucanotransferase. This gene encodes the glycogen debrancher enzyme which is involved in glycogen degradation. This enzyme has two independent catalytic activities which occur at different sites on the protein: a 4-alpha-glucotransferase activity and a amylo-1,6-glucosidase activity. Mutations in this gene are associated with glycogen storage disease although a wide range of enzymatic and clinical variability occurs…
- **Diseases (Open Targets)**: glycogen storage disease III (0.831); disorder of glycogen metabolism (0.768); glycogen storage disease XV (0.608); hereditary disease (0.507); Acute rhabdomyolysis (0.463)
- **Europe PMC papers**: 4441
- **Why important**: AGL encodes the glycogen-debranching enzyme and is the module's clearest glycogen and energy metabolism marker. It is connected to GPRIN3 and has tissue enrichment in skeletal muscle and tongue, while its disease associations include glycogen storage disease. Its extensive literature base and established enzymatic function make it more interpretable than the module's less characterized hub.
- **Conclusion**: Established evidence supports AGL as a glycogen-metabolism gene that contributes to the module's metabolic aspect. Its inclusion does not demonstrate a shared glycogen pathway across bone marrow and colon, particularly because no GO or KEGG term was globally enriched.

#### GRAMD1C

- **Related proteins** (co-abundance neighbors): BCAT2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Plasma membrane, Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GRAM domain containing 1C. Predicted to enable cholesterol binding activity and cholesterol transfer activity. Predicted to be involved in cellular response to cholesterol. Predicted to be located in endoplasmic reticulum membrane; endoplasmic reticulum-plasma membrane contact site; and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: gastritis (0.193); myocardial ischemia (0.172); Abnormality of the skeletal system (0.140); glycogen storage disease VI (0.065); hyperlipoproteinemia type V (0.064)
- **Europe PMC papers**: 2685
- **Why important**: GRAMD1C is connected to BCAT2 and is annotated for cholesterol binding, cholesterol transfer, and intracellular sterol transport at endoplasmic-reticulum and plasma-membrane contact sites. HPA places it in several cell-type contexts and reports group enrichment among selected blood-cell types, while its protein is detected in colon but not bone marrow. Its literature volume is substantial, although its disease associations are less specific than those of LYN or AGL.
- **Conclusion**: Established evidence supports GRAMD1C as a membrane lipid-handling component and a possible bridge between metabolic and membrane-state variation. A direct functional link to BCAT2 or the rest of the module remains a hypothesis unsupported by physical-interaction databases.

## Module 6

**Tissue pair**: bone_marrow and colon  
**Genes (10)**: ATP11B, BRD9, FHIT, TUBGCP5, HYCC1, PHKA2, NPC1L1, MT-ND3, RAB31, TOR2A

### Function

This module does not have a single statistically supported GO or KEGG functional annotation: no GO or KEGG term passed global correction. Its genes nevertheless suggest a heterogeneous cellular program involving mitochondrial respiration and oxidative stress through MT-ND3, intracellular and endosomal trafficking through RAB31, sterol uptake through NPC1L1, membrane lipid translocation through ATP11B, chromatin regulation through BRD9, purine metabolism and genome-stress responses through FHIT, glycogen metabolism through PHKA2, and microtubule organization through TUBGCP5. These functional observations are gene-level evidence rather than enrichment evidence. The sparse co-abundance graph therefore supports a cautious interpretation as a mixed membrane-trafficking, metabolic, and cell-state module rather than a well-defined canonical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only TOR2A is annotated as secreted to blood, while the remaining genes are non-secreted. It is also not strongly blood-cell specific. Most genes have low immune-cell specificity, although RAB31 is immune-cell enhanced and is associated with myeloid populations, while FHIT is immune-cell enriched in naive CD4 T cells. HPA single-cell evidence is distributed across diverse cell types, including enterocytes, hepatocytes, neutrophils, epithelial cells, and other specialized populations. NPC1L1 is group enriched in intestine and liver, and FHIT is tissue enriched in choroid plexus, whereas most genes have low tissue specificity. Protein detection is broader in colon than in bone marrow, and TOR2A is not detected in either tissue by IHC. Overall, the shared module could partly reflect shared or varying cell-type composition, but it does not look like a simple plasma-protein or uniformly blood-cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and no hu.MAP complex contains multiple module members. Thus the co-abundance relationships are not corroborated by the queried physical-interaction or complex resources. The module graph itself is sparse: MT-ND3 and RAB31 occupy the most connected positions, with links to genes involved in trafficking, membrane biology, and cellular metabolism, while the other genes form limited pairwise associations. This pattern is compatible with coordinated expression or shared cellular context, but it does not establish direct molecular binding or a common complex.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unrecognized co-abundance pattern, because its within-module relationships are not represented by high-confidence STRING interactions or multi-member hu.MAP complexes. However, that absence alone does not demonstrate biological novelty. Several constituent genes have well-established individual functions and substantial literature, including MT-ND3, NPC1L1, and FHIT, so the potentially novel result is the cross-tissue co-abundance relationship and its particular combination of genes, not the discovery of new gene functions. The lack of globally enriched GO or KEGG terms further argues against claiming a newly defined canonical pathway.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program linking mitochondrial energetic activity with membrane and vesicle biology in cells represented in bone marrow and colon. MT-ND3 may mark respiratory or oxidative-state variation, while RAB31 may connect that state to endosomal and regulated-exocytosis processes; NPC1L1 and ATP11B may capture sterol and phospholipid handling, and BRD9, FHIT, PHKA2, and TUBGCP5 may reflect accompanying transcriptional, genome-stress, metabolic, or cytoskeletal state differences. Cell-type mixture, particularly contributions from epithelial, myeloid, or progenitor populations, is an alternative explanation that should be tested before assigning a unified mechanism.

### Important genes

#### MT-ND3

- **Related proteins** (co-abundance neighbors): NPC1L1 (0.87), BRD9 (0.87), TOR2A (0.81), HYCC1 (0.81), ATP11B (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH dehydrogenase subunit 3. Enables NADH dehydrogenase (ubiquinone) activity. Involved in mitochondrial electron transport, NADH to ubiquinone. Part of mitochondrial respiratory chain complex I. Implicated in Leber hereditary optic neuropathy; Leigh disease; and Parkinson's disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Leigh syndrome (0.717); mitochondrial disease (0.671); mitochondrial complex I deficiency (0.667); type 2 diabetes mellitus (0.609); diabetes mellitus (0.584)
- **Europe PMC papers**: 2660
- **Why important**: MT-ND3 has the strongest network position and connects to NPC1L1, BRD9, TOR2A, HYCC1, and ATP11B. It encodes a mitochondrial respiratory-chain subunit involved in NADH-linked electron transport and is associated with oxidative stress, aerobic respiration, mitochondrial disease, Leigh disease, and Parkinson's disease. Its substantial literature base makes it a biologically established anchor for an energetic or oxidative-state interpretation.
- **Conclusion**: Established evidence supports MT-ND3 as a mitochondrial respiratory-chain gene and the principal network hub. It is reasonable to hypothesize that its co-abundance marks mitochondrial state, but the module does not establish that MT-ND3 functionally drives the other genes.

#### RAB31

- **Related proteins** (co-abundance neighbors): PHKA2 (0.85), TUBGCP5 (0.83), ATP11B (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus, Vesicles; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB31, member RAS oncogene family. Small GTP-binding proteins of the RAB family, such as RAB31, play essential roles in vesicle and granule targeting (Bao et al., 2002 [PubMed 11784320]).[supplied by OMIM, Jul 2009]
- **Diseases (Open Targets)**: Dupuytren Contracture (0.470); fibroblastic disorder (0.352); fasciitis (0.307); Alzheimer disease (0.289); Parkinson disease (0.289)
- **Europe PMC papers**: 1316
- **Why important**: RAB31 is the other prominent network connector, linking PHKA2, TUBGCP5, and ATP11B. It is a Rab-family small GTP-binding protein involved in intracellular and endosomal transport, receptor internalization, Golgi-to-plasma-membrane transport, and regulated exocytosis. HPA places it in myeloid-associated cell types and identifies immune-cell enhancement in basophils, making it informative for both trafficking and possible cell-composition interpretations. Its literature support is substantial.
- **Conclusion**: Established evidence supports RAB31 as a vesicle-trafficking regulator and a plausible marker of cellular composition or activation. Its centrality suggests a coordinating role in the observed expression pattern, but there is no direct interaction evidence connecting it to the other module members.

#### NPC1L1

- **Related proteins** (co-abundance neighbors): MT-ND3 (0.87); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NPC1 like intracellular cholesterol transporter 1. The protein encoded by this gene is a multi-pass membrane protein. It contains a conserved N-terminal Niemann-Pick C1 (NPC1) domain and a putative sterol-sensing domain (SSD) which includes a YQRL motif functioning as a plasma membrane to trans-Golgi network transport signal in other proteins. This protein takes up free cholesterol into cells through vesicular endocytosis and plays a critical role…
- **Diseases (Open Targets)**: Hypercholesterolemia (0.733); hyperlipidemia (0.696); inherited lipid metabolism disorder (0.644); familial hypercholesterolemia (0.634); cardiovascular disorder (0.526)
- **Europe PMC papers**: 3189
- **Why important**: NPC1L1 is directly connected to MT-ND3 and is group enriched in intestine and liver, with expression in several absorptive and hepatic cell types. It is a sterol-sensing membrane transporter involved in intestinal cholesterol absorption, sterol and lipoprotein handling, and vitamin E metabolism. Its disease associations include hypercholesterolemia and inherited lipid disorders, and it has a substantial literature base. It provides a strong tissue and lipid-metabolism signal within an otherwise heterogeneous module.
- **Conclusion**: Established evidence supports NPC1L1 as a sterol-transport and intestinal-absorption gene. Its presence may indicate epithelial or hepatic-like cellular contribution rather than a universal bone-marrow–colon mechanism; a direct mechanistic link to MT-ND3 remains hypothetical.

#### FHIT

- **Related proteins** (co-abundance neighbors): HYCC1 (0.86); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location Nucleoli fibrillar center, Plasma membrane; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fragile histidine triad diadenosine triphosphatase. The protein encoded by this gene is a P1-P3-bis(5'-adenosyl) triphosphate hydrolase involved in purine metabolism. This gene encompasses the common fragile site FRA3B on chromosome 3, where carcinogen-induced damage can lead to translocations and aberrant transcripts. In fact, aberrant transcripts from this gene have been found in about half of all esophageal, stomach, and colon carcinomas. The en…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.514); major depressive disorder (0.510); obesity disorder (0.495); type 2 diabetes mellitus (0.425); diabetes mellitus (0.421)
- **Europe PMC papers**: 4266
- **Why important**: FHIT connects to HYCC1 and has the strongest literature volume among the selected genes. It participates in purine-nucleotide metabolism, diadenosine-triphosphate catabolism, and p53-linked apoptotic signaling, and is described as a tumor suppressor associated with the common fragile site and aberrant transcripts in several carcinomas, including colon carcinoma. Its HPA profile includes tissue enrichment in choroid plexus and immune-cell enrichment in naive CD4 T cells, adding both disease-relevant and composition-related context.
- **Conclusion**: Established evidence supports FHIT as a genome-stress, purine-metabolism, and tumor-suppressor gene with relevance to colon cancer biology. Its co-abundance with HYCC1 is not enough to infer a shared pathway, but FHIT makes cellular stress or altered proliferative state a plausible module-level hypothesis.

#### BRD9

- **Related proteins** (co-abundance neighbors): MT-ND3 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: bromodomain containing 9. Enables lysine-acetylated histone binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in nucleoplasm. Part of SWI/SNF complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.540); alcohol drinking (0.215); urolithiasis (0.215); acute myeloid leukemia (0.110); neoplasm (0.110)
- **Europe PMC papers**: 1470
- **Why important**: BRD9 is connected to MT-ND3 and encodes a bromodomain protein associated with acetylated-histone binding, transcriptional regulation, chromatin remodeling, DNA repair, stem-cell maintenance, and cell-population control. It is a component of the SWI/SNF complex and has a substantial literature base. Its detection in both bone marrow and colon supports relevance to the shared tissue pair, although its cell-type enhancement in early spermatids is not specific to these tissues.
- **Conclusion**: Established evidence supports BRD9 as a chromatin-regulatory component rather than a metabolic or trafficking protein. Its association with MT-ND3 may reflect coordinated cell state, proliferation, or composition; a direct connection between mitochondrial activity and BRD9 in this module is a hypothesis, not an established finding.

## Module 7

**Tissue pair**: bone_marrow and colon  
**Genes (6)**: TGFBI, COL6A1, COL6A2, COL6A3, COL12A1, HBA1

### Function

This is a strongly coherent extracellular-matrix and collagen module. The primary evidence is the globally corrected enrichment for extracellular-matrix structural constituent (GO:MF extracellular matrix structural constituent; q_global = 1.04e-06), external encapsulating structure (GO:CC external encapsulating structure; q_global = 5.73e-06), extracellular matrix (GO:CC extracellular matrix; q_global = 5.73e-06), tensile-strength structural constituent (GO:MF extracellular matrix structural constituent conferring tensile strength; q_global = 6.64e-06), collagen trimer (GO:CC collagen trimer; q_global = 2.62e-05), collagen-trimer complex (GO:CC complex of collagen trimers; q_global = 0.000694), collagen binding (GO:MF collagen binding; q_global = 0.00305), collagen type VI trimer (GO:CC collagen type VI trimer; q_global = 0.00505), collagen beaded filament (GO:CC collagen beaded filament; q_global = 0.00505), and the basement-membrane/interstitial-matrix interface (GO:CC basement membrane/interstitial matrix interface; q_global = 0.00505). The module also supports cell adhesion (GO:BP cell adhesion; q_global = 0.029), ECM-receptor interaction (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.00688), and integrin signaling (KEGG Integrin signaling - Homo sapiens (human); q_global = 0.0432). These terms converge on a structural and adhesive extracellular-matrix role rather than a generic housekeeping function. The KEGG protein-digestion-and-absorption result (KEGG Protein digestion and absorption - Homo sapiens (human); q_global = 5.54e-05) is consistent with collagen representation in that pathway but is less informative about the biological mechanism. The absence of primary enrichment for HBA1-related functions indicates that HBA1 is not driving the module-level functional interpretation.

**Cell composition.** The module is dominated by secreted or extracellular-matrix-associated proteins: COL6A1, COL6A2, COL6A3, COL12A1, and TGFBI are all annotated as secreted or extracellular-matrix proteins in HPA. The collagen genes are enriched in stromal, fibroblast, hepatic-stellate, pericyte-related, or fibro-adipogenic cell populations, while TGFBI is associated with stromal and myeloid populations. HBA1 is bone-marrow and erythrocyte associated and has no primary GO/KEGG enrichment in this module. HPA therefore supports a stromal extracellular-matrix signal, with a possible contribution from shared cell composition or blood-derived material in the sampled tissues, rather than a broadly expressed housekeeping module. Protein detection differs between bone marrow and colon, so the shared co-abundance pattern should not be interpreted as uniform protein production by the same cells in both tissues.

**GO/KEGG enrichment**: 17 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF extracellular matrix structural constituent | 1.04e-06 | COL12A1, COL6A1, COL6A2, COL6A3, TGFBI |
| GO:CC external encapsulating structure | 5.73e-06 | COL12A1, COL6A1, COL6A2, COL6A3, TGFBI |
| GO:CC extracellular matrix | 5.73e-06 | COL12A1, COL6A1, COL6A2, COL6A3, TGFBI |
| GO:MF extracellular matrix structural constituent conferring tensile strength | 6.64e-06 | COL12A1, COL6A1, COL6A2, COL6A3 |
| GO:CC collagen trimer | 2.62e-05 | COL12A1, COL6A1, COL6A2, COL6A3 |
| KEGG Protein digestion and absorption - Homo sapiens (human) | 5.54e-05 | COL12A1, COL6A1, COL6A2, COL6A3 |
| GO:CC complex of collagen trimers | 0.000694 | COL12A1, COL6A1, COL6A3 |
| GO:MF structural molecule activity | 0.00297 | COL12A1, COL6A1, COL6A2, COL6A3, TGFBI |
| GO:MF collagen binding | 0.00305 | COL6A1, COL6A2, TGFBI |
| GO:CC collagen type VI trimer | 0.00505 | COL6A1, COL6A3 |
| GO:CC collagen beaded filament | 0.00505 | COL6A1, COL6A3 |
| GO:CC basement membrane/interstitial matrix interface | 0.00505 | COL6A1, COL6A3 |
| GO:CC von-Willerbrand-factor-A-domain-rich collagen trimer | 0.00505 | COL6A1, COL6A3 |
| KEGG ECM-receptor interaction - Homo sapiens (human) | 0.00688 | COL6A1, COL6A2, COL6A3 |
| GO:CC endoplasmic reticulum lumen | 0.0102 | COL12A1, COL6A1, COL6A2, COL6A3 |

### STRING and hu.MAP

STRING provides strong known connections among the collagen genes: COL6A1, COL6A2, and COL6A3 form a highly connected type VI collagen relationship, and COL12A1 connects to each of them. STRING also supports the extracellular-matrix and collagen interpretation (STRING Function Extracellular matrix structural constituent; within-query FDR = 5.9e-08) (STRING Keyword Extracellular matrix; within-query FDR = 1.14e-07) (STRING Keyword Collagen; within-query FDR = 4.92e-07). The congenital muscular dystrophy and connective-tissue phenotype annotations (12 supplementary STRING terms; within-query FDR 1.14e-07–7.6e-07) are supplementary and should not be treated as globally corrected enrichment. TGFBI is connected to COL6A2 and COL6A3 in the module network, but it has no listed STRING partner, making its module relationship less established in STRING. hu.MAP identifies COL6A3 and COL12A1 together in a collagen-rich complex (hu.MAP huMAP3_13038.1), while the other module genes have no reported hu.MAP complex containing multiple module members. Thus, much of the module reflects established collagen biology, but the full tissue-specific co-abundance pattern extends beyond the explicitly supported complexes.

**STRING interactions (score >= 0.7)**: 6 of 15 gene pairs: COL12A1–COL6A1 (0.781); COL12A1–COL6A2 (0.793); COL12A1–COL6A3 (0.788); COL6A1–COL6A2 (0.998); COL6A1–COL6A3 (0.994); COL6A2–COL6A3 (0.994)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Extracellular matrix structural constituent (FDR = 5.9e-08, 5 genes); Keyword Extracellular matrix (FDR = 1.14e-07, 5 genes); Keyword Congenital muscular dystrophy (FDR = 1.14e-07, 4 genes); Keyword Collagen (FDR = 4.92e-07, 4 genes); HPO Hyperextensibility at wrists (FDR = 5.86e-07, 4 genes); HPO Congenital muscular torticollis (FDR = 5.86e-07, 4 genes); HPO Increased laxity of fingers (FDR = 5.86e-07, 4 genes); HPO Progressive proximal muscle weakness (FDR = 5.86e-07, 4 genes); HPO Diaphragmatic weakness (FDR = 5.86e-07, 4 genes); HPO Curved toe phalanx (FDR = 5.86e-07, 4 genes); HPO Reduced maximal expiratory pressure (FDR = 5.86e-07, 4 genes); HPO Reduced muscle collagen VI (FDR = 5.86e-07, 4 genes); HPO Increased endomysial connective tissue (FDR = 5.86e-07, 4 genes); HPO Cigarette-paper scars (FDR = 5.98e-07, 4 genes); HPO Quadriceps muscle weakness (FDR = 7.6e-07, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13038.1 (COL6A3, COL12A1; 2/40)

### Novelty

This should not be claimed as a wholly new collagen interaction module: the COL6A1, COL6A2, COL6A3, and COL12A1 relationships are already supported by STRING, and COL6A3 with COL12A1 occurs in hu.MAP (hu.MAP huMAP3_13038.1). The potentially novel aspect is the conserved co-abundance organization of this extracellular matrix set across bone marrow and colon, particularly its association with TGFBI and the observed tissue and cell-type composition. However, absence from STRING or hu.MAP is not evidence of novelty. A genuine novelty claim would require comparison with published cross-tissue co-expression studies, independent cohorts, and cell-composition-controlled analyses; the fact sheet alone supports a careful candidate finding rather than a definitive new biological mechanism.

**Hypothesis.** Hypothesis: this conserved module represents coordinated production and remodeling of a stromal extracellular-matrix niche shared by bone marrow and colon. The COL6A1-COL6A2-COL6A3 type VI collagen unit may provide the core beaded-filament scaffold, COL12A1 may organize interactions with surrounding collagen fibrils, and TGFBI may link the matrix to integrin-mediated adhesion and cell behavior. HBA1 may reflect accompanying erythroid or blood-related material in bone-marrow samples rather than a mechanistic member of the matrix program. This hypothesis predicts that the module will track stromal-cell abundance and matrix deposition, and that its apparent conservation will weaken after adjustment for stromal and blood-cell composition.

### Important genes

#### COL6A3

- **Related proteins** (co-abundance neighbors): COL6A1 (0.92), COL6A2 (0.92), TGFBI (0.86), HBA1; HBA2 (0.85); STRING partners: COL12A1 (0.788), COL6A1 (0.994), COL6A2 (0.994)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_13038.1
- **Function (MyGene.info)**: collagen type VI alpha 3 chain. This gene encodes the alpha-3 chain, one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The alpha-3 chain of type VI collagen is much larger than the alpha-1 and -2 chains. This difference in size is largely due to an increase in the number of subdomains, similar to von Willebrand Factor type A domains, that are found in the amino termin…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy (0.766); dystonia 27 (0.764); Bethlem myopathy (0.758); Bethlem myopathy 1C (0.747); Bethlem myopathy 1A (0.718)
- **Europe PMC papers**: 5386
- **Why important**: COL6A3 has the strongest network position in the module, connecting to COL6A1, COL6A2, TGFBI, and the HBA1/HBA2-associated edge. It appears in nearly all primary collagen, matrix, adhesion, and integrin-related terms, is part of the hu.MAP collagen complex (hu.MAP huMAP3_13038.1), and is annotated as the large alpha chain of type VI collagen. Its disease associations include Bethlem myopathy and Ullrich congenital muscular dystrophy, and its literature volume is substantial. It is also stromal and fibroblast-associated in HPA and not detected in immune cells.
- **Conclusion**: Established evidence supports COL6A3 as a central structural component and network hub of the module, with strong relevance to type VI collagen biology and connective-tissue disease. The hypothesis that it organizes the shared bone-marrow and colon niche is plausible but requires cell-composition-controlled validation.

#### COL6A1

- **Related proteins** (co-abundance neighbors): COL6A3 (0.92), COL12A1 (0.83); STRING partners: COL12A1 (0.781), COL6A2 (0.998), COL6A3 (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is a core type VI collagen chain and has strong relationships with COL6A2, COL6A3, and COL12A1 in STRING. It participates in every primary matrix and collagen term listed for the module, including the type VI collagen trimer (GO:CC collagen type VI trimer; q_global = 0.00505), and is associated with osteoblast differentiation, tissue development, and skeletal muscle fiber development. It has extensive literature and disease associations with Bethlem myopathy and Ullrich congenital muscular dystrophy.
- **Conclusion**: Established evidence identifies COL6A1 as a core scaffold gene whose co-abundance is strongly consistent with a type VI collagen program. Its detection in colon but not bone marrow cautions that the cross-tissue signal may involve differing cellular sources or shared matrix-related variation rather than identical local expression.

#### COL6A2

- **Related proteins** (co-abundance neighbors): COL6A3 (0.92), TGFBI (0.86); STRING partners: COL12A1 (0.793), COL6A1 (0.998), COL6A3 (0.994)
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Cytosol; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 2 chain. This gene encodes one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The product of this gene contains several domains similar to von Willebrand Factor type A domains. These domains have been shown to bind extracellular matrix proteins, an interaction that explains the importance of this collagen in organizing matrix components. Mutation…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy 1B (0.770); Bethlem myopathy (0.755); Ullrich congenital muscular dystrophy (0.743); Bethlem myopathy 1B (0.723); Bethlem myopathy 1A (0.713)
- **Europe PMC papers**: 4115
- **Why important**: COL6A2 is a type VI collagen chain with strong STRING relationships to COL6A1 and COL6A3 and module links to TGFBI. It contributes to the primary extracellular-matrix, collagen, collagen-binding, ECM-receptor, and integrin-signaling terms (6 globally significant GO/KEGG terms, q_global 1.04e-06–0.0432; see the table). Its annotated role in organizing matrix components and its associations with Bethlem myopathy and Ullrich scleroatonic muscular dystrophy give it direct functional and disease relevance.
- **Conclusion**: Established evidence supports COL6A2 as an integral component of the type VI collagen scaffold and a contributor to matrix organization. Its association with several T-cell populations in HPA leaves open the possibility that part of its cross-tissue co-abundance reflects cellular composition.

#### TGFBI

- **Related proteins** (co-abundance neighbors): COL6A2 (0.86), COL6A3 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transforming growth factor beta induced. This gene encodes an RGD-containing protein that binds to type I, II and IV collagens. The RGD motif is found in many extracellular matrix proteins modulating cell adhesion and serves as a ligand recognition sequence for several integrins. This protein plays a role in cell-collagen interactions and may be involved in endochondrial bone formation in cartilage. The protein is induced by transforming…
- **Diseases (Open Targets)**: lattice corneal dystrophy type I (0.826); Reis-Bucklers corneal dystrophy (0.728); granular corneal dystrophy type I (0.723); granular corneal dystrophy type II (0.716); epithelial basement membrane dystrophy (0.710)
- **Europe PMC papers**: 5444
- **Why important**: TGFBI is the module's principal non-collagen matrix regulator. It connects to COL6A2 and COL6A3, contains an RGD motif, binds several collagen types, and can influence integrin-mediated cell adhesion. It contributes to the primary matrix, collagen-binding, and cell-adhesion terms (4 globally significant GO/KEGG terms, q_global 1.04e-06–0.029; see the table). Its HPA associations include stromal, macrophage, dendritic, and monocyte populations, while its disease literature is particularly strong for corneal dystrophies.
- **Conclusion**: Established evidence supports TGFBI as a matrix-cell interface protein that could connect the collagen scaffold to adhesion signaling. Its role as the mediator of the conserved bone-marrow and colon pattern is a hypothesis, because STRING does not list a partner for it and the module-level association may partly reflect stromal or myeloid composition.

#### COL12A1

- **Related proteins** (co-abundance neighbors): COL6A1 (0.83); STRING partners: COL6A1 (0.781), COL6A2 (0.793), COL6A3 (0.788)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_13038.1
- **Function (MyGene.info)**: collagen type XII alpha 1 chain. This gene encodes the alpha chain of type XII collagen, a member of the FACIT (fibril-associated collagens with interrupted triple helices) collagen family. Type XII collagen is a homotrimer found in association with type I collagen, an association that is thought to modify the interactions between collagen I fibrils and the surrounding matrix. Alternatively spliced transcript variants encoding di…
- **Diseases (Open Targets)**: Bethlem myopathy 2 (0.794); Ullrich congenital muscular dystrophy 2 (0.709); Bethlem myopathy (0.617); Abnormality of the skeletal system (0.533); Ullrich congenital muscular dystrophy (0.501)
- **Europe PMC papers**: 3324
- **Why important**: COL12A1 is the module's type XII collagen component and connects in STRING to all three type VI collagen genes. It is also one of the two module members in the hu.MAP collagen-rich complex (hu.MAP huMAP3_13038.1). Its annotations support collagen fibril organization and tissue development, and its disease associations include Bethlem myopathy and Ullrich congenital muscular dystrophy. Its network degree is limited, but its position links the type VI collagen unit to the broader collagen-fibril environment.
- **Conclusion**: Established evidence supports COL12A1 as an accessory fibril-associated collagen that strengthens the interpretation of the module as an organized matrix assembly rather than isolated collagen gene expression. Its proposed role in coordinating the shared tissue niche remains a hypothesis.

## Module 8

**Tissue pair**: bone_marrow and colon  
**Genes (9)**: C1D, DOCK10, ELMO1, GPSM3, IRAG2, KALRN, MTRF1, SOS1, VAV1

### Function

The module is most consistently interpreted as a small-GTPase regulatory and signaling module. The primary evidence is the globally corrected enrichment for GTPase regulator activity (GO:MF GTPase regulator activity; q_global = 0.000647), guanyl-nucleotide exchange factor activity (GO:MF guanyl-nucleotide exchange factor activity; q_global = 0.000648), nucleoside-triphosphatase regulator activity (GO:MF nucleoside-triphosphatase regulator activity; q_global = 0.000669), and small-GTPase-mediated signal transduction (GO:BP small GTPase-mediated signal transduction; q_global = 0.0215). The contributing genes are concentrated among Rho-family and Ras-related signaling regulators, including DOCK10, ELMO1, GPSM3, KALRN, SOS1, and VAV1. The supplementary STRING annotations support pleckstrin-homology domains, guanine-nucleotide exchange, Dbl-homology domains, Rac signaling, GPCR-related signaling, and endothelial RhoGEF biology (15 supplementary STRING terms; within-query FDR 0.00012–0.0262). Together with the stated functions of VAV1, ELMO1, DOCK10, SOS1, and GPSM3, this points to regulation of cytoskeletal remodeling, cell migration, phagocytosis, immune-cell activation, and signal transmission. The module should not be reduced to a single pathway: KALRN and SOS1 also connect the pattern to broader Ras or Rho signaling, while ELMO1 and DOCK10 suggest coordinated control of Rac-dependent motility and engulfment.

**Cell composition.** This is not a plasma-protein or secreted-protein module: none of the genes is annotated as secreted. It is also not a uniformly broadly expressed housekeeping module. HPA data show frequent tissue or cell-type enhancement in lymphoid tissue, bone marrow, brain, macrophages, mast cells, microglia, monocytes, NK cells, neutrophils, and related hematopoietic populations. VAV1 is enhanced in bone marrow and lymphoid tissue, GPSM3 is group-enriched in bone marrow, intestine, lung, and lymphoid tissue, and several genes are enhanced in immune or hematopoietic cell types. At the same time, KALRN, ELMO1, and DOCK10 have brain or neural-cell associations, so the module is not exclusively hematopoietic. Protein detection in both bone marrow and colon for many members supports biological presence in both tissues, but the shared signal may partly reflect shared immune or stromal cellular composition rather than a tissue-wide program operating identically in every cell.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF GTPase regulator activity | 0.000647 | DOCK10, ELMO1, GPSM3, KALRN, SOS1, VAV1 |
| GO:MF guanyl-nucleotide exchange factor activity | 0.000648 | DOCK10, ELMO1, KALRN, SOS1, VAV1 |
| GO:MF nucleoside-triphosphatase regulator activity | 0.000669 | DOCK10, ELMO1, GPSM3, KALRN, SOS1, VAV1 |
| GO:BP small GTPase-mediated signal transduction | 0.0215 | DOCK10, ELMO1, KALRN, SOS1, VAV1 |

### STRING and hu.MAP

The strongest known STRING relationship is SOS1-VAV1, indicating a well-supported connection between two central regulators in the module. No other module pair reaches the stated high-confidence STRING threshold, so most co-abundance edges are not established as direct physical interactions by this resource. hu.MAP identifies a complex containing SOS1 and ELMO1 together with several DOCK, ELMO, RAC, CRKL, RAPGEF, and related proteins (hu.MAP huMAP3_13135.1). This supports a known molecular neighborhood involving nucleotide exchange, Rac-family signaling, and cytoskeletal control, but it does not prove that every module member forms one physical complex. The contrast between the co-abundance network and the sparse high-confidence interaction map suggests that the module may represent a co-regulated signaling program or shared cellular context rather than a single stable complex.

**STRING interactions (score >= 0.7)**: 1 of 36 gene pairs: SOS1–VAV1 (0.977)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Pleckstrin homology domain. (FDR = 0.00012, 5 genes); InterPro Pleckstrin homology domain (FDR = 0.00067, 5 genes); Keyword Guanine-nucleotide releasing factor (FDR = 0.0015, 4 genes); SMART Guanine nucleotide exchange factor for Rho/Rac/Cdc42-like GTPases (FDR = 0.0023, 3 genes); PMID (2015) Endothelial RhoGEFs: A systematic analysis of their expression profiles in VEGF-stimulated and tumor endothelial cells. (FDR = 0.0025, 5 genes); InterPro PH-like domain superfamily (FDR = 0.0035, 5 genes); InterPro Dbl homology (DH) domain (FDR = 0.0089, 3 genes); InterPro Dbl homology (DH) domain superfamily (FDR = 0.0089, 3 genes); Function Guanyl-nucleotide exchange factor activity (FDR = 0.01, 4 genes); Function GTPase regulator activity (FDR = 0.01, 5 genes); RCTM NRAGE signals death through JNK (FDR = 0.0167, 3 genes); RCTM GPCR downstream signalling (FDR = 0.0167, 4 genes); RCTM G alpha (12/13) signalling events (FDR = 0.0167, 3 genes); RCTM RAC1 GTPase cycle (FDR = 0.0167, 4 genes); RCTM Erythropoietin activates RAS (FDR = 0.0262, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13135.1 (SOS1, ELMO1; 2/15)

### Novelty

The underlying biology is not new: GTPase regulation, Rho-family exchange factors, VAV1-dependent hematopoietic signaling, SOS1 Ras signaling, and ELMO or DOCK-mediated motility are established processes. The module-level finding may nevertheless be a new observation because the coordinated co-abundance pattern is not recapitulated by extensive high-confidence STRING connectivity, and hu.MAP provides only a partial complex overlap (hu.MAP huMAP3_13135.1). However, absence of most pairs from STRING or hu.MAP cannot by itself establish novelty. The defensible conclusion is that this is a potentially novel cross-tissue co-abundance configuration built from largely established signaling components; confirmation would require replication in independent bone-marrow and colon cohorts, cell-type-aware analysis, and testing whether the same gene relationships persist within matched cell populations.

**Hypothesis.** Hypothesis: the conserved module reflects a shared immune or hematopoietic signaling state present in bone marrow and colon, in which SOS1, VAV1, KALRN, DOCK10, and ELMO1 coordinate Ras or Rho-family nucleotide cycling with actin remodeling, migration, receptor signaling, and phagocytic or engulfment behavior. GPSM3 may connect this state to inflammatory and leukocyte-chemotactic regulation, while IRAG2 may provide a membrane or endoplasmic-reticulum-associated context. The brain-associated HPA signals for several genes raise an alternative possibility that part of the module is a broadly reused motility or signaling program rather than an exclusively immune program. This mechanistic interpretation is a hypothesis, not a demonstrated physical pathway.

### Important genes

#### KALRN

- **Related proteins** (co-abundance neighbors): DOCK10 (0.91), IRAG2 (0.85), VAV1 (0.84), ELMO1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kalirin RhoGEF kinase. Huntington's disease (HD), a neurodegenerative disorder characterized by loss of striatal neurons, is caused by an expansion of a polyglutamine tract in the HD protein huntingtin. This gene encodes a protein that interacts with the huntingtin-associated protein 1, which is a huntingtin binding protein that may function in vesicle trafficking. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: hypothyroidism (0.464); neurodegenerative disease (0.425); nodular goiter (0.412); open-angle glaucoma (0.388); Abnormality of the skeletal system (0.323)
- **Europe PMC papers**: 1026
- **Why important**: KALRN is the most connected and strongest member of the co-abundance subgraph, linking DOCK10, IRAG2, VAV1, and ELMO1. It appears in every primary enrichment term (4 globally significant GO/KEGG terms, q_global 0.000647–0.0215; see the table) and in the supplementary RhoGEF, pleckstrin-homology, Dbl-homology, Rac-cycle, and GPCR-related annotations (14 supplementary STRING terms; within-query FDR 0.00012–0.0167). Its annotated roles include RhoGEF kinase activity, signal transduction, axon guidance, vesicle transport, and nervous-system development. It has extensive literature and disease associations including Huntington's disease, neurodegenerative disease, glaucoma, and skeletal-system abnormalities.
- **Conclusion**: Established evidence supports KALRN as a central Rho-related signaling regulator and the network hub of this module. Its participation in the shared bone-marrow and colon program is supported by co-abundance and HPA detection, but a specific immune-cell mechanism remains a hypothesis because it lacks high-confidence STRING or hu.MAP support within this module.

#### SOS1

- **Related proteins** (co-abundance neighbors): ELMO1 (0.82), GPSM3 (0.81), C1D (0.81); STRING partners: VAV1 (0.977)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: huMAP3_13135.1
- **Function (MyGene.info)**: SOS Ras/Rac guanine nucleotide exchange factor 1. This gene encodes a protein that is a guanine nucleotide exchange factor for RAS proteins, membrane proteins that bind guanine nucleotides and participate in signal transduction pathways. GTP binding activates and GTP hydrolysis inactivates RAS proteins. The product of this gene may regulate RAS proteins by facilitating the exchange of GTP for GDP. Mutations in this gene are associated with gingiv…
- **Diseases (Open Targets)**: Noonan syndrome (0.871); hereditary gingival fibromatosis (0.718); RASopathy (0.673); cancer (0.604); Noonan syndrome and Noonan-related syndrome (0.565)
- **Europe PMC papers**: 7803
- **Why important**: SOS1 is a central connector in the module and is linked to ELMO1, GPSM3, and C1D. It contributes to all primary terms (4 globally significant GO/KEGG terms, q_global 0.000647–0.0215; see the table) and to nearly all relevant supplementary signaling annotations (5 supplementary STRING terms; within-query FDR 0.00012–0.0025), (9 supplementary STRING terms; within-query FDR 0.0089–0.0262). Its established function is guanine-nucleotide exchange for Ras proteins, with roles in Ras signaling and epidermal-growth-factor-receptor signaling. It is the most extensively studied gene among the module members in the supplied literature summary and has strong disease associations with Noonan syndrome, RASopathy, hereditary gingival fibromatosis, and cancer. It also forms the one high-confidence STRING pair with VAV1 and shares the hu.MAP complex with ELMO1 (hu.MAP huMAP3_13135.1).
- **Conclusion**: Established evidence makes SOS1 a key signaling bridge and the strongest molecular anchor for the module. Its exact contribution here may involve Ras signaling, cross-talk with Rho-family pathways, or both; the cross-talk interpretation is plausible but not directly demonstrated by the supplied interaction data.

#### VAV1

- **Related proteins** (co-abundance neighbors): KALRN (0.84), MTRF1 (0.82); STRING partners: SOS1 (0.977)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vav guanine nucleotide exchange factor 1. This gene is a member of the VAV gene family. The VAV proteins are guanine nucleotide exchange factors (GEFs) for Rho family GTPases that activate pathways leading to actin cytoskeletal rearrangements and transcriptional alterations. The encoded protein is important in hematopoiesis, playing a role in T-cell and B-cell development and activation. The encoded protein has been identified as the spec…
- **Diseases (Open Targets)**: cutaneous leishmaniasis (0.503); cancer (0.394); lung adenocarcinoma (0.230); Shock (0.218); breast carcinoma (0.211)
- **Europe PMC papers**: 6288
- **Why important**: VAV1 is connected to KALRN and MTRF1, appears in all primary enrichment terms (4 globally significant GO/KEGG terms, q_global 0.000647–0.0215; see the table), and is included throughout the supplementary GTPase, RhoGEF, Rac-cycle, GPCR, and hematopoietic signaling annotations (15 supplementary STRING terms; within-query FDR 0.00012–0.0262). Its established functions include Rho-family exchange, actin rearrangement, immune receptor signaling, T-cell and B-cell development and activation, natural-killer-cell activation, cell migration, and platelet activation. HPA places it in bone marrow and lymphoid tissue and in several immune-cell types. It has a substantial literature and disease associations involving infection, cancer, and shock. The SOS1-VAV1 STRING relationship is the strongest known pair in the module.
- **Conclusion**: Established evidence identifies VAV1 as the clearest immune and hematopoietic signaling component and supports a role in linking receptor activation to cytoskeletal responses. It is reasonable to hypothesize that VAV1 helps explain the shared bone-marrow and colon signal, but the module data do not establish which immune cell population drives the association.

#### ELMO1

- **Related proteins** (co-abundance neighbors): KALRN (0.84), SOS1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13135.1
- **Function (MyGene.info)**: engulfment and cell motility 1. This gene encodes a member of the engulfment and cell motility protein family. These proteins interact with dedicator of cytokinesis proteins to promote phagocytosis and cell migration. Increased expression of this gene and dedicator of cytokinesis 1 may promote glioma cell invasion, and single nucleotide polymorphisms in this gene may be associated with diabetic nephropathy. Alternative splicing …
- **Diseases (Open Targets)**: psoriasis (0.540); hypothyroidism (0.540); autoimmune disease (0.489); cutaneous leishmaniasis (0.462); primary biliary cholangitis (0.440)
- **Europe PMC papers**: 2265
- **Why important**: ELMO1 is connected to KALRN and SOS1, contributes to every primary enrichment term (4 globally significant GO/KEGG terms, q_global 0.000647–0.0215; see the table), and is represented in the pleckstrin-homology and endothelial-RhoGEF supplementary annotations (STRING SMART Pleckstrin homology domain.; within-query FDR = 0.00012), (STRING InterPro Pleckstrin homology domain; within-query FDR = 0.00067), (STRING PMID (2015) Endothelial RhoGEFs: A systematic analysis of their expression profiles in VEGF-stimulated and tumor endothelial cells.; within-query FDR = 0.0025), and (STRING InterPro PH-like domain superfamily; within-query FDR = 0.0035). Its established functions include interaction with DOCK proteins, phagocytosis, engulfment, cell motility, Rac signaling, and actin organization. HPA associates it with macrophages, mast cells, hematopoietic stem cells, megakaryocyte-erythroid progenitors, and microglia. It also shares the hu.MAP complex with SOS1 (hu.MAP huMAP3_13135.1) and has meaningful literature and disease associations involving invasion, diabetic nephropathy, and autoimmune or inflammatory disorders.
- **Conclusion**: Established evidence supports ELMO1 as a bridge between nucleotide-exchange signaling and engulfment or motility machinery. Its network and hu.MAP context make it important for interpreting the module as a coordinated signaling neighborhood, although the supplied data do not prove that ELMO1 physically connects to every co-abundant partner in this tissue pair.

#### DOCK10

- **Related proteins** (co-abundance neighbors): KALRN (0.91); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dedicator of cytokinesis 10. This gene encodes a member of the dedicator of cytokinesis protein family. Members of this family are guanosine nucleotide exchange factors for Rho GTPases and defined by the presence of conserved DOCK-homology regions. The encoded protein belongs to the D (or Zizimin) subfamily of DOCK proteins, which also contain an N-terminal pleckstrin homology domain. Alternatively spliced transcript variants…
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); hypothyroidism (0.393); response to antihypertensive drug (0.295); poisoning (0.295); rhinitis (0.274)
- **Europe PMC papers**: 615
- **Why important**: DOCK10 is a direct neighbor of KALRN and appears in every primary enrichment term (4 globally significant GO/KEGG terms, q_global 0.000647–0.0215; see the table). It is also included in the supplementary pleckstrin-homology, guanine-nucleotide exchange, RhoGEF, GTPase-regulator, and Rac-cycle annotations (6 supplementary STRING terms; within-query FDR 0.00012–0.0035) and (STRING Function Guanyl-nucleotide exchange factor activity; within-query FDR = 0.01), (STRING Function GTPase regulator activity; within-query FDR = 0.01), (STRING RCTM RAC1 GTPase cycle; within-query FDR = 0.0167). Its established molecular identity is a DOCK-family Rho-GTPase exchange factor with a pleckstrin-homology domain. Its annotated biological roles include B-cell homeostasis, marginal-zone B-cell differentiation, cell migration, Rho regulation, and positive regulation of GTPase activity. HPA links it to lymphoid tissue and several immune or microglial cell types, while disease resources associate it with neurodegenerative disease, hypothyroidism, and other conditions.
- **Conclusion**: Established evidence supports DOCK10 as a plausible effector of Rho-dependent migration and lymphoid-cell organization. Its limited direct network connectivity makes it less of a structural hub than KALRN or SOS1, but its concordant annotation across all primary terms gives it strong functional importance. A specific role in the shared tissue module remains a hypothesis.

## Module 9

**Tissue pair**: bone_marrow and colon  
**Genes (5)**: MT-CO1, HSD17B8, F13A1, FAAH2, UBA7

### Function

No GO or KEGG term passed global correction, and there is no supplementary STRING enrichment. The module therefore does not support a single statistically established pathway-level function. Its gene annotations instead indicate a mixed biological signal involving lipid and steroid metabolism through FAAH2 and HSD17B8, mitochondrial respiration through MT-CO1, coagulation and fibrin cross-linking through F13A1, and stress, innate immune, and protein-modification processes through UBA7. The network structure is centered on FAAH2, with the other genes connected to it but not to one another, so the module is better interpreted as a coordinated abundance pattern than as evidence for a coherent molecular complex.

**Cell composition.** The module is not dominated by secreted or broadly housekeeping proteins. F13A1 is secreted to blood and is associated with macrophages, megakaryocytes, platelets, classical monocytes, and myeloid dendritic cells, making blood or platelet contribution plausible. HPA evidence also links several genes to megakaryocytes, platelets, plasma cells, hepatocytes, enterocytes, and colonocytes. MT-CO1 is detected in both tissues and is mitochondrial, whereas HSD17B8 and UBA7 are detected in colon but not bone marrow. The mixture of tissue-enhanced, cell-type-enhanced, and low-specificity proteins suggests that the conserved pattern may partly reflect shared cell types, blood contamination, or a common cellular state rather than a tissue-independent pathway. Only F13A1 is explicitly secreted, and the module is not uniformly blood-cell enriched.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair meets the provided high-confidence STRING interaction criterion, and no STRING functional enrichment is reported. No hu.MAP complex contains multiple module members. Thus, the module is not supported as a previously catalogued physical complex or as a dense known interaction neighborhood. The lack of STRING and hu.MAP support does not invalidate the co-abundance pattern, but it argues against interpreting the four edges as established molecular interactions. FAAH2 is the sole network hub in this module, while HSD17B8, F13A1, MT-CO1, and UBA7 are peripheral partners connected only to FAAH2.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel tissue-pair co-abundance pattern, because the provided interaction and complex resources contain no corresponding supported relationships and the module has no globally corrected GO or KEGG annotation. However, it cannot be called a newly discovered biochemical pathway from these data alone. The genes individually have established functions and disease or literature associations, and absence from STRING or hu.MAP is not proof of novelty. The strongest defensible claim is that this particular conserved co-abundance configuration, especially the association of FAAH2 with F13A1, MT-CO1, UBA7, and HSD17B8 across bone marrow and colon, is not explained by the supplied reference resources.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-composition or cellular-state signal in bone marrow and colon. In this model, FAAH2 captures variation in lipid-amide metabolism and acts as the abundance hub, while F13A1 reflects platelet or myeloid contribution, MT-CO1 reflects mitochondrial respiratory activity, UBA7 reflects stress or innate immune-related protein modification, and HSD17B8 reflects steroid and fatty-acid metabolic state. These genes may therefore co-vary because the samples contain related mixtures of metabolic, platelet, immune, and epithelial cells, rather than because the proteins form one physical pathway. This hypothesis should be tested with cell-composition adjustment, protein localization or interaction assays, and replication in independent tissue cohorts.

### Important genes

#### FAAH2

- **Related proteins** (co-abundance neighbors): HSD17B8 (0.86), F13A1 (0.85), MT-CO1 (0.84), UBA7 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fatty acid amide hydrolase 2. This gene encodes a fatty acid amide hydrolase that shares a conserved protein motif with the amidase signature family of enzymes. The encoded enzyme is able to catalyze the hydrolysis of a broad range of bioactive lipids, including those from the three main classes of fatty acid amides; N-acylethanolamines, fatty acid primary amides and N-acyl amino acids. This enzyme has a preference for monouns…
- **Diseases (Open Targets)**: hypertensive disorder (0.302); hypogonadism (0.239); type 2 diabetes mellitus (0.128); androgenetic alopecia (0.084); systemic lupus erythematosus (0.048)
- **Europe PMC papers**: 187
- **Why important**: FAAH2 is the network hub and is connected to every other module member. Its annotated amidase activity spans bioactive lipids, including fatty acid amides and N-acyl amino acids, and its annotation includes arachidonate metabolism. It therefore provides the strongest candidate anchor for interpreting the module. Its literature base is established, although less extensive than that of MT-CO1 or F13A1.
- **Conclusion**: Established evidence supports FAAH2 as a lipid-metabolizing enzyme and as the central abundance correlate in this module. It is not established that FAAH2 physically regulates the other module genes. A plausible hypothesis is that FAAH2 abundance tracks a lipid-metabolic state shared by the relevant bone-marrow and colon cellular populations.

#### F13A1

- **Related proteins** (co-abundance neighbors): FAAH2 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coagulation factor XIII A chain. This gene encodes the coagulation factor XIII A subunit. Coagulation factor XIII is the last zymogen to become activated in the blood coagulation cascade. Plasma factor XIII is a heterotetramer composed of 2 A subunits and 2 B subunits. The A subunits have catalytic function, and the B subunits do not have enzymatic activity and may serve as plasma carrier molecules. Platelet factor XIII is compri…
- **Diseases (Open Targets)**: Factor XIII subunit A deficiency (0.808); factor XIII, A subunit, deficiency of (0.740); congenital factor XIII deficiency (0.527); thrombophilia due to thrombin defect (0.485); hemorrhage (0.463)
- **Europe PMC papers**: 2585
- **Why important**: F13A1 is connected to the hub and has a strong biological interpretation: it encodes the catalytic A subunit of coagulation factor XIII, participates in fibrin clot formation and peptide cross-linking, is secreted to blood, and is associated with macrophages, megakaryocytes, platelets, classical monocytes, and myeloid dendritic cells. It also has an extensive literature and clear disease associations involving factor XIII deficiency and hemorrhage.
- **Conclusion**: Established evidence supports F13A1 as a coagulation and platelet or myeloid-associated protein. Its presence does not demonstrate a direct interaction with FAAH2. The most likely interpretation is that F13A1 marks a blood-cell or platelet-related component of the shared abundance signal, though a metabolic connection remains hypothetical.

#### MT-CO1

- **Related proteins** (co-abundance neighbors): FAAH2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome c oxidase subunit I. Contributes to cytochrome-c oxidase activity. Predicted to be involved in electron transport coupled proton transport and mitochondrial electron transport, cytochrome c to oxygen. Part of mitochondrial respiratory chain complex III and mitochondrial respiratory chain complex IV. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: mitochondrial disease (0.706); mitochondrial non-syndromic sensorineural hearing loss (0.701); Leber hereditary optic neuropathy (0.697); mitochondrial complex IV deficiency, nuclear-type (0.691); MELAS syndrome (0.663)
- **Europe PMC papers**: 3479
- **Why important**: MT-CO1 is connected to FAAH2 and encodes a core mitochondrial respiratory-chain subunit involved in cytochrome-c oxidation, oxidative phosphorylation, aerobic respiration, and responses to hypoxia or oxidative stress. It is detected in both tissues and is enhanced in colonocytes, enterocytes, and hepatocytes. It also has a broad literature and well-established mitochondrial disease associations.
- **Conclusion**: Established evidence supports MT-CO1 as a marker of mitochondrial respiratory activity and oxidative state. The module does not establish a specific mitochondrial interaction with FAAH2 or the other genes. Its co-abundance may indicate variation in energetic demand or cell composition in the sampled tissues.

#### UBA7

- **Related proteins** (co-abundance neighbors): FAAH2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoplasm, Vesicles; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin like modifier activating enzyme 7. The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E1 ubiquitin-activating enzyme family. The encod…
- **Diseases (Open Targets)**: dengue disease (0.371); anemia (phenotype) (0.229); intelligence (0.164); uveal melanoma (0.147); Back pain (0.123)
- **Europe PMC papers**: 643
- **Why important**: UBA7 is connected to FAAH2 and encodes an E1 enzyme involved in protein ubiquitination and ISG15-protein conjugation. Its annotations include stress response, DNA-damage response, and innate immune response. HPA links it to megakaryocytes and platelets, and it is detected in colon. These properties make it informative for a possible stress or immune-state component, despite its peripheral network position.
- **Conclusion**: Established evidence supports UBA7 as a protein-modification enzyme with roles in stress and innate immune biology. The module provides no evidence that UBA7 directly controls FAAH2 or the other members. Its co-abundance is consistent with a shared cellular stress or immune state, but that interpretation remains a hypothesis.

#### HSD17B8

- **Related proteins** (co-abundance neighbors): FAAH2 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydroxysteroid 17-beta dehydrogenase 8. In mice, the Ke6 protein is a 17-beta-hydroxysteroid dehydrogenase that can regulate the concentration of biologically active estrogens and androgens. It is preferentially an oxidative enzyme and inactivates estradiol, testosterone, and dihydrotestosterone. However, the enzyme has some reductive activity and can synthesize estradiol from estrone. The protein encoded by this gene is similar to Ke6 …
- **Diseases (Open Targets)**: maturity-onset diabetes of the young (0.083); breast cancer (0.074); breast carcinoma (0.074); maturity-onset diabetes of the young type 3 (0.072); hyperproinsulinemia (0.051)
- **Europe PMC papers**: 429
- **Why important**: HSD17B8 is the peripheral partner with the clearest annotation for steroid and fatty-acid metabolism. It is a short-chain dehydrogenase-family enzyme associated with estrogen and androgen inactivation, fatty-acid biosynthesis, and estrogen metabolism. HPA shows enhancement in enterocytes and hepatocytes and detection in colon, providing a plausible tissue-relevant metabolic context. Its literature base is established but more limited than that of MT-CO1 or F13A1.
- **Conclusion**: Established evidence supports HSD17B8 as a steroid and lipid-metabolizing enzyme. Its connection to FAAH2 is a co-abundance relationship, not a demonstrated physical or enzymatic interaction. It may contribute to a shared epithelial or hepatic-like metabolic state, but this mechanistic interpretation requires independent testing.

## Module 10

**Tissue pair**: bone_marrow and colon  
**Genes (6)**: CEP135, DOK2, SLC2A6, CYB5R2, PARVG, SMC1B

### Function

No GO or KEGG term passed global correction, and there was no STRING functional-enrichment result. Therefore, the module does not support a specific pathway-level function from enrichment analysis. Its gene content is heterogeneous: it combines redox biology and possible respiratory-burst relevance through CYB5R2, hematopoietic signal transduction through DOK2, adhesion and actin organization through PARVG, hexose transport and glycolytic regulation through SLC2A6, meiotic cohesion through SMC1B, and centriole biology through CEP135. The co-abundance pattern is therefore more consistent with a shared cellular-composition or cellular-state signal than with a single established biochemical pathway. The central position of CYB5R2 makes it the main network-organizing candidate, but co-abundance does not establish direct molecular regulation.

**Cell composition.** The module is not composed of plasma or secreted proteins: the fact sheet reports no secreted genes. It is also not a uniform housekeeping module. HPA evidence points toward immune and hematopoietic representation, including lymphoid tissue, monocytes, dendritic cells, macrophage-related cells, eosinophils, and B-cell populations. PARVG is enhanced in bone marrow and lymphoid tissue, DOK2 is enhanced in lung and lymphoid tissue, and SLC2A6 is enhanced in lymphoid tissue and in a monocyte population. At the same time, CYB5R2 and SMC1B show testis-related enrichment, while other genes show neural, retinal, epithelial, or progenitor-associated patterns. The shared bone-marrow and colon signal may therefore reflect immune-cell representation or a shared cell state in the samples, with additional contribution from biologically distinct expression programs.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no hu.MAP complex contained multiple module members. The co-abundance edges are consequently not corroborated as established physical interactions by these resources. Known biology still exists for individual genes: DOK2 participates in hematopoietic receptor and Ras-related signaling, PARVG is an actin-associated adhesion protein, SLC2A6 is a hexose transporter, CYB5R2 belongs to a cytochrome-b reductase family, SMC1B functions in meiotic chromosome cohesion, and CEP135 functions in centriole biology. These annotations support plausible individual roles but do not demonstrate a shared protein complex or direct pathway.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a newly discovered molecular complex or pathway. Its co-abundance pattern may be a novel observation in the bone-marrow and colon comparison, but the available evidence does not establish biological novelty. The lack of STRING and hu.MAP support means that the pattern is not represented as a known interaction complex in those resources, yet absence from those databases alone cannot prove novelty. The heterogeneous annotations, lack of globally significant enrichment, and immune-plus-germline expression mixture instead make sample composition, context dependence, or an indirect co-regulated state important alternative explanations.

**Hypothesis.** Hypothesis: the module reflects a shared immune or hematopoietic cellular-state signal present in both bone marrow and colon, centered statistically on CYB5R2 and accompanied by genes involved in hematopoietic signaling, adhesion, and nutrient transport. DOK2 and PARVG could mark signaling and adhesive properties of immune-lineage cells, while SLC2A6 could reflect altered carbohydrate handling. The testis-associated genes SMC1B and CYB5R2, together with the centriole-associated CEP135, may represent context-dependent expression or cell-state contributions rather than components of one physical mechanism. This hypothesis requires validation with cell-type deconvolution, independent cohorts, protein-level measurements, and perturbation experiments.

### Important genes

#### CYB5R2

- **Related proteins** (co-abundance neighbors): SMC1B (0.92), DOK2 (0.88), PARVG (0.86), SLC2A6 (0.82), CEP135 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome b5 reductase 2. The protein encoded by this gene belongs to the flavoprotein pyridine nucleotide cytochrome reductase family of proteins. Cytochrome b-type NAD(P)H oxidoreductases are implicated in many processes including cholesterol biosynthesis, fatty acid desaturation and elongation, and respiratory burst in neutrophils and macrophages. Cytochrome b5 reductases have soluble and membrane-bound forms that are t…
- **Diseases (Open Targets)**: familial hemolytic anemia (0.236); inherited hemoglobinopathy (0.236); non-autoimmune hemolytic anemia (0.205); interstitial lung disease (0.175); nasopharyngeal carcinoma (0.093)
- **Europe PMC papers**: 303
- **Why important**: CYB5R2 is the network hub, connecting every other module member in the co-abundance subgraph. Its cytochrome-b reductase family function links it to redox biology, cholesterol and fatty-acid processes, and respiratory-burst biology in neutrophils and macrophages. HPA shows enrichment in retinal and testis contexts and association with eosinophil and B-cell populations. It also has the strongest literature volume among the selected genes and disease links involving hemolytic anemia and hemoglobinopathy.
- **Conclusion**: Established evidence supports CYB5R2 as the statistical center of the module and as a redox-related protein with immune-relevant functional plausibility. It is not established that CYB5R2 physically regulates the other module genes or that it drives the shared bone-marrow and colon pattern. Its hub status makes it the leading candidate for follow-up, not proof of causality.

#### DOK2

- **Related proteins** (co-abundance neighbors): CYB5R2 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: docking protein 2. The protein encoded by this gene is constitutively tyrosine phosphorylated in hematopoietic progenitors isolated from chronic myelogenous leukemia (CML) patients in the chronic phase. It may be a critical substrate for p210(bcr/abl), a chimeric protein whose presence is associated with CML. This encoded protein binds p120 (RasGAP) from CML cells. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: atopic eczema (0.491); respiratory system disorder (0.348); exocrine pancreatic carcinoma (0.348); substance-related disorder (0.258); drug allergy (0.115)
- **Europe PMC papers**: 640
- **Why important**: DOK2 is connected to CYB5R2 and has a strong hematopoietic interpretation. It is associated with cell-surface receptor signaling, tyrosine-kinase signaling, Ras signaling, and hematopoietic progenitor biology. HPA places it in lung and lymphoid tissue and in dendritic-cell, Hofbauer-cell, Kupffer-cell, macrophage, megakaryocyte, and eosinophil contexts. It also has the largest literature volume among the selected signaling-related genes and disease associations involving atopic eczema and respiratory disorders.
- **Conclusion**: Established evidence supports DOK2 as a hematopoietic signaling adaptor and a plausible marker of immune-cell composition or activation. The module does not establish that DOK2 mediates the CYB5R2 association or explains the colon signal. Any role in the proposed shared state remains a hypothesis.

#### PARVG

- **Related proteins** (co-abundance neighbors): CYB5R2 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: parvin gamma. Members of the parvin family, including PARVG, are actin-binding proteins associated with focal contacts.[supplied by OMIM, Aug 2004].
- **Diseases (Open Targets)**: alcohol drinking (0.306); corneal neovascularization (0.212); metabolic syndrome (0.074); placental abruption (0.034); cardiomyopathy (0.034)
- **Europe PMC papers**: 306
- **Why important**: PARVG is connected to CYB5R2 and is enhanced in bone marrow and lymphoid tissue. Its established annotation concerns actin binding, focal contacts, cell adhesion, cell-matrix adhesion, cell spreading, and cell polarity. HPA associates it with B cells, dendritic cells, hematopoietic stem cells, Hofbauer cells, and Kupffer cells, and protein detection is reported in both tissues relevant to the module. These features make it a useful candidate for linking immune-cell identity with adhesion or tissue positioning.
- **Conclusion**: Established evidence supports PARVG as an adhesion and cytoskeletal protein with hematopoietic relevance. The shared co-abundance with CYB5R2 does not demonstrate a direct interaction or prove that adhesion biology is the module function. Its proposed role in coordinating immune-cell positioning across the two tissues is therefore a hypothesis.

#### SLC2A6

- **Related proteins** (co-abundance neighbors): CYB5R2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 2 member 6. Hexose transport into mammalian cells is catalyzed by a family of membrane proteins, including SLC2A6, that contain 12 transmembrane domains and a number of critical conserved residues.[supplied by OMIM, Jul 2002].
- **Diseases (Open Targets)**: osteoarthritis (0.188); Alzheimer disease (0.130); cancer (0.080); lung adenocarcinoma (0.076); metabolic syndrome (0.074)
- **Europe PMC papers**: 559
- **Why important**: SLC2A6 is connected to CYB5R2 and encodes a membrane hexose transporter associated with glucose, fructose, and dehydroascorbic-acid transport and regulation of glycolytic processes. HPA shows enrichment in brain and lymphoid tissue and enhancement in a non-classical monocyte population, with protein detection in colon. Its annotations provide a plausible metabolic component to an immune-cell state, and its disease associations include osteoarthritis, Alzheimer disease, cancer, lung adenocarcinoma, and metabolic syndrome.
- **Conclusion**: Established evidence supports SLC2A6 as a nutrient-transport and metabolism-related membrane protein with immune-cell relevance. The module does not establish that altered hexose transport causes the observed co-abundance pattern. A metabolic interpretation is plausible but remains a hypothesis requiring cell-specific validation.

#### CEP135

- **Related proteins** (co-abundance neighbors): CYB5R2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece, Principal piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: centrosomal protein 135. This gene encodes a centrosomal protein, which acts as a scaffolding protein during early centriole biogenesis, and is also required for centriole-centriole cohesion during interphase. Mutations in this gene are associated with autosomal recessive primary microcephaly-8. [provided by RefSeq, Jun 2012].
- **Diseases (Open Targets)**: autosomal recessive primary microcephaly (0.749); hereditary disease (0.496); Primary microcephaly (0.372); auditory neuropathy (0.333); neurodegenerative disease (0.174)
- **Europe PMC papers**: 777
- **Why important**: CEP135 is connected to CYB5R2 and encodes a centrosomal scaffold required for centriole biogenesis and centriole cohesion, with an additional role in non-motile cilium assembly. It is associated with erythrocyte progenitors and late primary spermatocytes in HPA and with primary microcephaly and related neurological disease in Open Targets. Its annotation introduces a cell-division and centrosome-related possibility that could be relevant to progenitor or proliferative states.
- **Conclusion**: Established evidence supports CEP135 as a centrosome and centriole protein with disease relevance to microcephaly. There is no evidence here that centrosome biology is a shared function of the module or that CEP135 acts with CYB5R2. Its inclusion is best treated as a hypothesis about cellular state rather than as evidence for a centrosomal complex.

## Module 11

**Tissue pair**: bone_marrow and colon  
**Genes (10)**: DPP3, MSH5, AARS1, CARS1, DARS1, TARS1, CCT5, CCT3, CCT7, CCT8

### Function

The strongest interpretation is a conserved intracellular proteostasis and translation-support module. The central signal is the CCT/TRiC chaperonin submodule formed by CCT3, CCT5, CCT7, and CCT8. This interpretation is supported by the globally corrected chaperonin-containing T-complex and ATP-dependent protein-folding terms (GO:CC chaperonin-containing T-complex; q_global = 5.5e-07), (GO:MF ATP-dependent protein folding chaperone; q_global = 9.92e-05), (GO:CC protein folding chaperone complex; q_global = 0.000306), (GO:MF protein folding chaperone; q_global = 0.000938), (GO:MF unfolded protein binding; q_global = 0.00284), and (GO:BP protein folding; q_global = 0.0361), and independently by the STRING chaperonin annotations (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 8.03e-07) through (STRING NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis; within-query FDR = 5.49e-06). The CCT genes are also connected by very strong STRING relationships and recur together in multiple hu.MAP complexes (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_01951.1). A second component consists of aminoacyl-tRNA synthetases: AARS1, CARS1, DARS1, and TARS1. Their shared aminoacyl-tRNA biosynthesis and tRNA-aminoacylation signal is globally significant (GO:MF aminoacyl-tRNA ligase activity; q_global = 0.00257), (GO:BP tRNA aminoacylation for protein translation; q_global = 0.00257), (GO:BP amino acid activation; q_global = 0.00343), (GO:BP tRNA aminoacylation; q_global = 0.00343), and (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 0.00375), while their STRING and hu.MAP links support a translation-related subnetwork. The telomere-maintenance and Cajal-body terms (GO:BP positive regulation of telomerase RNA localization to Cajal body; q_global = 5.5e-07) through (GO:BP positive regulation of telomere maintenance via telomere lengthening; q_global = 5.31e-05), (GO:BP regulation of telomere maintenance via telomerase; q_global = 0.000306), (GO:BP regulation of telomere maintenance via telomere lengthening; q_global = 0.000527), (GO:BP telomere maintenance via telomerase; q_global = 0.000718), (GO:BP telomere maintenance via telomere lengthening; q_global = 0.00106), (GO:BP positive regulation of telomere maintenance; q_global = 0.00233), and (GO:BP regulation of telomere maintenance; q_global = 0.00861) through (GO:BP telomere organization; q_global = 0.0268) are driven by the CCT quartet and indicate biologically relevant annotations, but they do not by themselves establish that this entire co-abundance module directly controls telomerase. Fertilization and sperm-recognition terms should likewise be treated cautiously as annotation overlap rather than as the primary function. Overall, the module most plausibly reflects general protein folding, proteostasis, and translational capacity, with a possible connection to nuclear RNA and telomere-related processes.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly intracellular, with cytosolic or nucleoplasmic locations. Most genes have low tissue specificity and low immune-cell specificity, and protein detection is present in both bone marrow and colon for nearly all genes with available data. This favors a broadly expressed housekeeping or cellular-capacity program rather than a module specific to either tissue. Some genes show cell-type-enhanced expression, particularly in spermatogenic cells, and MSH5 is tissue enhanced in testis and immune-cell enhanced in basophils. Those observations may reflect specialized cellular states or shared low-abundance cell populations, but they do not support interpreting the module as a blood-cell or immune module. The cross-tissue conservation could therefore reflect common expression of intracellular folding and translation machinery, or shared cell-composition effects, rather than a bone-marrow–colon-specific pathway.

**GO/KEGG enrichment**: 60 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chaperonin-containing T-complex | 5.5e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 5.5e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 1.97e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 1.97e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 1.97e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 4.64e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 4.64e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 4.64e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP binding of sperm to zona pellucida | 9.08e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to Cajal body | 9.08e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 9.08e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 9.08e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 9.08e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP sperm-egg recognition | 1.58e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 2.56e-05 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING provides strong, already known relationships within two coherent parts of the module. The CCT genes form a densely connected chaperonin group, with CCT3, CCT5, CCT7, and CCT8 linked at very high confidence. The aminoacyl-tRNA synthetase group is connected through AARS1, CARS1, DARS1, and TARS1, and TARS1 also links to CCT5. These relationships are consistent with established protein-folding and translation machinery rather than an interaction network created solely by co-abundance. The STRING functional results (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 8.03e-07) through (STRING RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding; within-query FDR = 1.53e-05) support the CCT complex, actin folding, cellular proteostasis, and G-protein-beta folding. hu.MAP independently places the CCT quartet in several complexes (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_01951.1), and places DARS1 with TARS1 in aminoacylation-related complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). In contrast, MSH5 and DPP3 have no reported STRING partners in this module, and MSH5 has no hu.MAP complex assignment here. Thus, the network contains well-established physical or complex-level cores plus less-established co-abundance links, especially the connection involving MSH5 and DPP3.

**STRING interactions (score >= 0.7)**: 11 of 45 gene pairs: AARS1–CARS1 (0.872); AARS1–DARS1 (0.743); AARS1–TARS1 (0.929); CARS1–TARS1 (0.817); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT5–TARS1 (0.727); CCT7–CCT8 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam TCP-1/cpn60 chaperonin family (FDR = 8.03e-07, 4 genes); Component Chaperonin-containing T-complex (FDR = 1.48e-06, 4 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 1.63e-06, 4 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 3e-06, 4 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 3e-06, 4 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 3e-06, 4 genes); InterPro GroEL-like apical domain superfamily (FDR = 3e-06, 4 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 3e-06, 4 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 3e-06, 4 genes); RCTM Folding of actin by CCT/TriC (FDR = 3.88e-06, 4 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis (FDR = 5.49e-06, 4 genes); RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding (FDR = 1.53e-05, 4 genes); Process Binding of sperm to zona pellucida (FDR = 1.74e-05, 4 genes); Process Positive regulation of establishment of protein localization to telomere (FDR = 1.74e-05, 4 genes); Process Positive regulation of protein localization to Cajal body (FDR = 1.74e-05, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_02637.1 (DARS1, TARS1; 2/14); huMAP3_13688.1 (DARS1, TARS1; 2/14)

### Novelty

The module should not be presented as a discovery of a new CCT complex, a new aminoacyl-tRNA synthetase pathway, or a new MSH5 function. Those gene functions and several relationships are already well established by STRING, hu.MAP, and the supplied gene annotations. The potentially novel aspect is the reproducible co-abundance organization of these components as a conserved module shared by bone marrow and colon, particularly the way the CCT, aminoacylation, and MSH5-associated portions are joined. However, the supplied evidence does not establish that this tissue-pair module is absent from prior co-expression studies, nor does absence from STRING or hu.MAP prove novelty. The appropriate conclusion is that the cross-tissue co-abundance pattern may be a new systems-level observation, while its molecular parts are largely established and require independent replication and perturbation before claiming a new mechanism.

**Hypothesis.** Hypothesis: the shared module represents a cell-state program that couples CCT/TRiC-mediated folding of newly synthesized proteins with aminoacyl-tRNA charging, thereby sustaining proteome production in cells present in both tissues. CCT activity may also support nuclear-body and telomere-associated processes, consistent with the globally corrected Cajal-body and telomere annotations (GO:BP positive regulation of telomerase RNA localization to Cajal body; q_global = 5.5e-07) through (GO:BP positive regulation of telomere maintenance via telomere lengthening; q_global = 5.31e-05) and (GO:BP regulation of telomere maintenance; q_global = 0.00861) through (GO:BP telomere organization; q_global = 0.0268). MSH5 may mark a specialized DNA-repair or reproductive-cell component that becomes co-abundant with this proteostasis program, but the MSH5 connection is currently a hypothesis rather than an established physical interaction. A testable prediction is that samples with stronger module activity will show coordinated increases in CCT-dependent folding capacity and aminoacylation capacity, without requiring enrichment for secreted proteins or immune-cell identity.

### Important genes

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT3 (0.87), CCT5 (0.83), CCT7 (0.83), DARS1 (0.80); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is the strongest network connector in the module and links the CCT core to DARS1. It participates in the globally corrected chaperonin, protein-folding, telomere, Cajal-body, and protein-stabilization annotations (GO:CC chaperonin-containing T-complex; q_global = 5.5e-07) through (GO:MF ATP binding; q_global = 0.000562) and (GO:BP RNA-templated DNA biosynthetic process; q_global = 0.000718) through (GO:BP protein stabilization; q_global = 0.0361). It is present in multiple hu.MAP CCT complexes (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_14584.1) and has substantial literature and disease association evidence.
- **Conclusion**: Established evidence supports CCT8 as a core component of the CCT/TRiC folding machinery and as a useful representative of the module's proteostasis signal. Its possible role in the module's telomere or Cajal-body interpretation remains an annotation-supported inference, not proof of a direct tissue-specific mechanism.

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT7 (0.87), CCT8 (0.87), CCT5 (0.85); STRING partners: CCT5 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a central CCT subunit with strong connections to CCT5, CCT7, and CCT8. It is included throughout the CCT-related globally corrected terms (GO:CC chaperonin-containing T-complex; q_global = 5.5e-07) through (GO:BP positive regulation of DNA biosynthetic process; q_global = 0.000527) and (GO:BP RNA-templated DNA biosynthetic process; q_global = 0.000718) through (GO:BP protein stabilization; q_global = 0.0361), and in several hu.MAP complexes (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_01951.1). Its annotation directly describes ATP-dependent folding of proteins including actin and tubulin, and it has the largest literature volume among the CCT genes in this module.
- **Conclusion**: Established evidence identifies CCT3 as a structural and functional component of the CCT/TRiC chaperonin. It is therefore a strong anchor for interpreting the module as intracellular folding and proteostasis, while disease associations do not by themselves demonstrate causality in bone marrow or colon.

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT3 (0.85), CCT8 (0.83); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999), TARS1 (0.727)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is embedded in the CCT core, connects to TARS1, and appears in all of the major CCT hu.MAP complexes (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_01951.1). Its globally corrected annotations include chaperonin complex, protein folding, protein stabilization, Cajal-body localization, and telomere-related terms. It also has a substantial literature and documented disease associations.
- **Conclusion**: Established evidence supports CCT5 as part of the module's conserved chaperone machinery and as a possible bridge between folding and translational capacity through its TARS1 relationship. The bridge is network-supported, but the co-abundance data do not establish direct regulation between CCT5 and TARS1.

#### DARS1

- **Related proteins** (co-abundance neighbors): MSH5 (0.81), AARS1 (0.80), CCT8 (0.80); STRING partners: AARS1 (0.743)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 1. This gene encodes a member of a multienzyme complex that functions in mediating the attachment of amino acids to their cognate tRNAs. The encoded protein ligates L-aspartate to tRNA(Asp). Mutations in this gene have been found in patients showing hypomyelination with brainstem and spinal cord involvement and leg spasticity. Alternative splicing results in multiple transcript variants. [provided by…
- **Diseases (Open Targets)**: hypomyelination with brain stem and spinal cord involvement and leg spasticity (0.773); atrial fibrillation (0.268); Abnormal brain morphology (0.266); tooth hard tissue disease (0.226); Pancreatic pseudocyst (0.225)
- **Europe PMC papers**: 238
- **Why important**: DARS1 connects the CCT-associated portion through CCT8 with the aminoacyl-tRNA synthetase portion through AARS1 and MSH5. It contributes to the globally corrected aminoacyl-tRNA biosynthesis and translation terms (GO:MF ATP binding; q_global = 0.000562) through (GO:MF adenyl ribonucleotide binding; q_global = 0.000583), (GO:MF adenyl nucleotide binding; q_global = 0.00104), (GO:MF purine ribonucleoside triphosphate binding; q_global = 0.00193) through (GO:BP tRNA aminoacylation for protein translation; q_global = 0.00257), and (GO:MF purine nucleotide binding; q_global = 0.00335) through (GO:MF anion binding; q_global = 0.0111), and it appears with TARS1 in hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Its disease associations provide functional relevance beyond generic housekeeping annotation.
- **Conclusion**: Established evidence supports DARS1 as a translational-capacity component and as a network bridge between module substructures. The specific role of DARS1 in linking proteostasis to MSH5 or to the cross-tissue phenotype is a hypothesis requiring experimental testing.

#### MSH5

- **Related proteins** (co-abundance neighbors): DPP3 (0.82), CARS1 (0.82), DARS1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutS homolog 5. This gene encodes a member of the mutS family of proteins that are involved in DNA mismatch repair and meiotic recombination. This protein is similar to a Saccharomyces cerevisiae protein that participates in segregation fidelity and crossing-over events during meiosis. This protein plays a role in promoting ionizing radiation-induced apoptosis. This protein forms hetero-oligomers with another mem…
- **Diseases (Open Targets)**: spermatogenic failure 74 (0.639); primary ovarian failure (0.596); premature ovarian failure 13 (0.503); neurodegenerative disease (0.471); genetic non-acquired premature ovarian failure (0.397)
- **Europe PMC papers**: 1807
- **Why important**: MSH5 is important because it is unusual within the module: it has a higher network position than its lack of STRING or hu.MAP support would suggest, connecting DPP3, CARS1, and DARS1. Its established annotation concerns DNA mismatch repair and meiotic recombination, and its HPA profile is enriched in testis and several specialized cell types. It has strong disease-association and literature support, including reproductive failure and DNA-repair-related biology.
- **Conclusion**: Established evidence supports MSH5 as a DNA-repair and meiotic-recombination protein with a specialized expression pattern. Its inclusion in this shared module is not explained by known STRING or hu.MAP relationships, so its connection to the CCT and aminoacylation machinery should be regarded as a co-abundance hypothesis, potentially reflecting cell state or composition rather than a direct molecular complex.

## Module 12

**Tissue pair**: bone_marrow and colon  
**Genes (6)**: DPYSL5, H3-3A, HNRNPL, ICAM5, NCOA3, NUP35

### Function

No GO or KEGG term passed global correction, and STRING reported no supplementary enrichment. The annotations instead suggest a heterogeneous module rather than a single established pathway. ICAM5 and DPYSL5 point toward neural cell adhesion, neuronal development, and axon-related biology; HNRNPL, NCOA3, NUP35, and H3-3A represent RNA processing, transcriptional coactivation, nucleocytoplasmic transport, and chromatin or nucleosome biology. ICAM5 is the apparent network hub, whereas the other genes are peripheral or weakly connected in the reported co-abundance structure. Thus, the safest functional interpretation is a coordinated expression state combining a neural or adhesion-associated signal with broadly distributed nuclear regulatory genes, not a validated biochemical pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: the supplied HPA summary reports no secreted genes. It is also not uniformly blood-cell enriched. Most genes have low immune-cell specificity or are not detected in immune cells, although H3-3A is immune-cell enhanced in neutrophils and NCOA3 is enhanced in B-cell and plasma-cell populations. Several genes are broadly expressed or nuclear housekeeping-type regulators, including HNRNPL, NCOA3, NUP35, and H3-3A. In contrast, ICAM5 and DPYSL5 are tissue enriched in brain and are not detected in immune cells. The HPA pattern therefore favors a mixture of broadly expressed nuclear genes with cell-type-associated signals, potentially reflecting shared cellular composition, rare contaminating or analogous cell states, or coordinated regulation in the sampled tissues rather than a secreted blood-derived program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module members, no STRING functional enrichment was reported, and no hu.MAP complex contained multiple module members. The listed co-abundance edges should therefore be interpreted as expression covariation, not as established physical protein interactions. Known biology exists for individual proteins: ICAM5 is an immunoglobulin-superfamily adhesion molecule with neuronal and leukocyte-binding functions; HNRNPL participates in heterogeneous nuclear ribonucleoprotein and RNA-processing biology; NCOA3 is a transcriptional coactivator with histone-acetyltransferase-associated activity; NUP35 is a nuclear-pore component; DPYSL5 belongs to the CRMP family; and H3-3A encodes a histone variant. However, the supplied interaction resources do not support a shared molecular complex or a previously established physical network.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This co-abundance pattern appears unusual and may be a newly observed tissue-pair module, because the supplied resources show no STRING interactions, no multi-member hu.MAP complex, and no globally significant GO or KEGG enrichment. Those absences do not prove biological novelty: the module may reflect correlated abundance, cell composition, tissue-specific regulation, or an incompletely catalogued association rather than a new molecular mechanism. The combination of ICAM5 and DPYSL5 with general nuclear regulators is biologically heterogeneous, which argues against claiming discovery of a new pathway. A defensible novelty claim is therefore limited to the observation of this co-abundance configuration in bone marrow and colon; confirmation would require replication, cell-composition adjustment, and independent experimental or cohort validation.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-composition or cell-state signal present in both tissues, in which a neural-adhesion or neuronal-development-associated expression component represented by ICAM5 and DPYSL5 covaries with general nuclear RNA, chromatin, transcriptional, and transport machinery represented by HNRNPL, NCOA3, NUP35, and H3-3A. A further possibility is that ICAM5-centered covariation captures a rare or ectopic cell population, or a tissue-repair and differentiation state, rather than direct protein cooperation. This hypothesis is supported by the HPA tissue and single-cell annotations and by the apparent network centrality of ICAM5, but it is not established by the co-abundance data and is not supported as a physical complex by STRING or hu.MAP.

### Important genes

#### ICAM5

- **Related proteins** (co-abundance neighbors): H3-3A; H3-3B (0.90), HNRNPL (0.88), DPYSL5 (0.84), NCOA3 (0.83), NUP35 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: intercellular adhesion molecule 5. The protein encoded by this gene is a member of the intercellular adhesion molecule (ICAM) family. All ICAM proteins are type I transmembrane glycoproteins, contain 2-9 immunoglobulin-like C2-type domains, and bind to the leukocyte adhesion LFA-1 protein. This protein is expressed on the surface of telencephalic neurons and displays two types of adhesion activity, homophilic binding between neuron…
- **Diseases (Open Targets)**: inflammatory bowel disease (0.341); atopic eczema (0.327); hypertensive disorder (0.310); chronic obstructive pulmonary disease (0.182); cardiac arrhythmia (0.181)
- **Europe PMC papers**: 653
- **Why important**: ICAM5 is the apparent hub of the supplied co-abundance network and connects the neural or adhesion-associated signal to the other module members. Its HPA annotation is brain-enriched, with enhancement in neuronal and alveolar cell types, and it is not detected in immune cells. Its established function includes neuronal homophilic adhesion and heterophilic adhesion involving leukocyte integrin biology. It also has substantial disease-oriented and literature support, including inflammatory bowel disease relevance, making it the most informative anchor for interpreting the module.
- **Conclusion**: Established: ICAM5 is a neuronal adhesion molecule and the central co-abundance feature in this module. Hypothesis: its centrality may mark a shared cell-state or composition signal rather than direct interaction with the nuclear proteins.

#### DPYSL5

- **Related proteins** (co-abundance neighbors): ICAM5 (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dihydropyrimidinase like 5. This gene encodes a member of the CRMP (collapsing response mediator protein) family thought to be involved in neural development. Antibodies to the encoded protein were found in some patients with neurologic symptoms who had paraneoplastic syndrome. A pseudogene of this gene is found on chromosome 11. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provi…
- **Diseases (Open Targets)**: Ritscher-Schinzel syndrome 4 (0.634); developmental disability (0.371); Ritscher-Schinzel syndrome (0.371); complex neurodevelopmental disorder (0.370); neurodegenerative disease (0.330)
- **Europe PMC papers**: 478
- **Why important**: DPYSL5 provides an independent neural-developmental interpretation alongside ICAM5. It is brain-enriched, absent from immune cells in the supplied HPA annotation, and associated with neural development, axon guidance, neuron differentiation, and dendrite regulation. It is directly connected to ICAM5 in the reported network and has disease associations involving neurodevelopment and neurodegeneration. Its literature base is meaningful but more focused than that of the broadly studied nuclear regulators.
- **Conclusion**: Established: DPYSL5 is a CRMP-family protein linked to neural development and axon-related biology. Hypothesis: its co-abundance with ICAM5 may indicate a neural-like or differentiation-related cellular signal in the samples, not a demonstrated ICAM5-DPYSL5 complex.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): ICAM5 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is a nuclear RNA-binding regulator with extensive literature and a direct reported association with ICAM5 in the module. Its established functions include RNA processing and regulation of alternative splicing. Unlike ICAM5 and DPYSL5, it has low tissue specificity, is detected in both sampled tissues, and has low immune-cell specificity, making it a plausible broadly expressed state marker rather than a tissue-specific driver.
- **Conclusion**: Established: HNRNPL is a general nuclear RNA-processing factor and is not specifically supported as a component of a neural adhesion pathway. Hypothesis: its covariation with ICAM5 may reflect transcriptional or cellular-state coupling, sample composition, or coordinated RNA-processing demand.

#### NCOA3

- **Related proteins** (co-abundance neighbors): ICAM5 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nuclear receptor coactivator 3. The protein encoded by this gene is a nuclear receptor coactivator that interacts with nuclear hormone receptors to enhance their transcriptional activator functions. The encoded protein has histone acetyltransferase activity and recruits p300/CBP-associated factor and CREB binding protein as part of a multisubunit coactivation complex. This protein is initially found in the cytoplasm but is trans…
- **Diseases (Open Targets)**: sensorineural hearing loss disorder (0.340); metabolic syndrome (0.300); osteoarthritis (0.286); alcohol drinking (0.276); Genu valgum (0.270)
- **Europe PMC papers**: 3051
- **Why important**: NCOA3 is a transcriptional coactivator with broad regulatory influence, histone-acetyltransferase-associated activity, and a substantial literature base. It is detected in both tissues, has low tissue specificity, and is enhanced in B-cell and plasma-cell populations, which provides a possible immune or cellular-composition explanation for part of the shared signal. Its reported connection to ICAM5 places a broadly acting transcriptional regulator alongside the neural-associated hub.
- **Conclusion**: Established: NCOA3 regulates transcription through nuclear-receptor coactivation and chromatin-associated mechanisms. Hypothesis: its module association may reflect a shared transcriptional state or B-lineage contribution rather than a direct functional partnership with ICAM5.

#### H3-3A

- **Related proteins** (co-abundance neighbors): none; STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: H3.3 histone A. Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Two molecules of each of the four core histones (H2A, H2B, H3, and H4) form an octamer, around which approximately 146 bp of DNA is wrapped in repeating units, called nucleosomes. The linker histone, H1, interacts with linker DNA between nucleosomes and functions in the com…
- **Diseases (Open Targets)**: Bryant-Li-Bhoj neurodevelopmental syndrome 1 (0.750); glioma (0.660); Bryant-Li-Bhoj neurodevelopmental syndrome 2 (0.619); malignant glioma (0.462); breast carcinoma (0.439)
- **Europe PMC papers**: 89323
- **Why important**: H3-3A encodes a histone variant and is therefore relevant to chromatin organization and cell-state regulation. It is tissue enhanced in bone marrow and immune-cell enhanced in neutrophils, while also being detected in both sampled tissues. Its very extensive literature and disease associations make it a useful contextual marker, although the supplied network fields do not establish it as a biochemical interaction partner.
- **Conclusion**: Established: H3-3A is a chromatin-associated histone gene with a bone-marrow and neutrophil-related expression signal in the supplied HPA evidence. Hypothesis: its co-abundance may capture proliferative, differentiation, or sample-composition effects that are shared between bone marrow and colon.

## Module 13

**Tissue pair**: bone_marrow and colon  
**Genes (5)**: ELP6, PRKD3, LZTR1, SMG8, ZBTB1

### Function

No GO or KEGG term passed global correction, so the module has no statistically established pathway assignment from those analyses. The supplied annotations instead indicate a mixed intracellular regulatory module: LZTR1 is linked to ubiquitin-dependent protein turnover and negative regulation of Ras signalling; ZBTB1 to transcriptional, cytokine, immune, DNA-repair and chromatin-related regulation; SMG8 to nonsense-mediated mRNA decay; ELP6 to the Elongator complex, tRNA modification and translation regulation; and PRKD3 to protein phosphorylation, intracellular signalling and sphingolipid biology. The most defensible interpretation is coordinated abundance of broadly expressed nuclear, cytosolic and membrane-associated regulators rather than a demonstrated single biochemical pathway. LZTR1 is the central connector in the supplied subgraph, with ZBTB1 as a secondary bridge.

**Cell composition.** All module genes have low tissue specificity, and the module is not enriched for secreted proteins or blood-cell-specific proteins according to HPA. Protein detection is present for most assayed genes in both bone marrow and colon, while ELP6 has no HPA protein detection in either listed tissue and one gene has no data. The single-cell annotations are heterogeneous, including proximal tubule cells, innate lymphoid cells, neural and glial populations, melanocytes, rod photoreceptor cells and somatotrophs. This argues against a plasma-protein module or a clearly blood-cell-enriched module. Because the genes are broadly expressed and intracellular, the shared signal could reflect common cellular regulatory machinery, technical or compositional covariance, or a shared cell state rather than a tissue-specific function.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING reports no high-confidence pairwise interactions among the module genes. The only supplementary STRING association is (STRING SMART Broad-Complex, Tramtrack and Bric a brac; within-query FDR = 0.0332), a SMART Broad-Complex, Tramtrack and Bric a brac domain term involving LZTR1 and ZBTB1; this is not global enrichment evidence and does not establish a physical interaction. No hu.MAP complex contains at least two module members. Accordingly, the co-abundance edges are not corroborated by the supplied curated interaction or complex resources. The network may capture coordinated expression, indirect regulation, shared cellular context or measurement covariance rather than a known protein complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Broad-Complex, Tramtrack and Bric a brac (FDR = 0.0332, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a new co-abundance observation, but it cannot be called a newly discovered molecular mechanism. The module combines regulators of ubiquitination, transcription and immunity, RNA surveillance, translation-related biology and kinase signalling, while lacking support from high-confidence STRING interactions and multi-member hu.MAP complexes. Those facts support novelty of the observed cross-tissue co-abundance pattern, but they also make a biological interpretation uncertain. Absence from STRING and hu.MAP alone does not prove novelty, because databases are incomplete and co-abundance does not require direct physical binding. A stronger novelty claim would require independent replication, adjustment for cell composition and technical effects, and experimental or perturbational validation.

**Hypothesis.** Hypothesis: the shared bone-marrow and colon signal reflects a conserved intracellular stress or state-regulation program in broadly expressed cells. In this model, LZTR1-linked protein turnover and Ras regulation, ZBTB1-linked transcriptional and immune regulation, SMG8-linked RNA quality control, ELP6-linked translational control, and PRKD3-linked signalling are coordinated. This is a mechanistic hypothesis, not an enrichment result. It predicts that the genes should covary across relevant cell states after adjustment for cell composition, and that perturbing the regulatory relationships should alter protein turnover, RNA surveillance or signalling outputs. The heterogeneous HPA cell-type pattern and lack of curated interactions mean that shared cellular composition or technical covariance remains a plausible alternative.

### Important genes

#### LZTR1

- **Related proteins** (co-abundance neighbors): SMG8 (0.86), PRKD3 (0.83), ZBTB1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: leucine zipper like post translational regulator 1. This gene encodes a member of the BTB-kelch superfamily. Initially described as a putative transcriptional regulator based on weak homology to members of the basic leucine zipper-like family, the encoded protein subsequently has been shown to localize exclusively to the Golgi network where it may help stabilize the Gogli complex. Deletion of this gene may be associated with DiGeorge syndrome. [pro…
- **Diseases (Open Targets)**: Noonan syndrome (0.843); schwannomatosis (0.820); Noonan syndrome 10 (0.790); LZTR1-related schwannomatosis (0.779); RASopathy (0.570)
- **Europe PMC papers**: 1630
- **Why important**: LZTR1 has the strongest network centrality in the supplied subgraph and connects to SMG8, PRKD3 and ZBTB1. Its BTB-kelch-superfamily annotation, Golgi localization, ubiquitin-related functions and Ras-regulatory association make it the most plausible organizational candidate. It also has substantial literature and disease links including Noonan syndrome, schwannomatosis and RASopathy.
- **Conclusion**: Established: LZTR1 is the network connector and has documented associations with protein turnover, Ras regulation and several disease phenotypes. Hypothesis: LZTR1 may coordinate the module, directly or indirectly, but a causal hub role is not established without interaction or perturbation evidence.

#### ZBTB1

- **Related proteins** (co-abundance neighbors): ELP6 (0.84), LZTR1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger and BTB domain containing 1. Enables K63-linked polyubiquitin modification-dependent protein binding activity; protein heterodimerization activity; and protein homodimerization activity. Involved in several processes, including cellular response to UV; nucleobase-containing compound biosynthetic process; and protein homooligomerization. Located in centrosome; nuclear body; and nuclear membrane. [provided by Alliance of Genome…
- **Diseases (Open Targets)**: atopic eczema (0.218); Chronic Obstructive Asthma (0.202); hypothyroidism (0.186); placental retention (0.182); neurodegenerative disease (0.158)
- **Europe PMC papers**: 301
- **Why important**: ZBTB1 is connected to LZTR1 and ELP6 and is the other member of the supplementary STRING domain term (STRING SMART Broad-Complex, Tramtrack and Bric a brac; within-query FDR = 0.0332). Its annotated roles in transcriptional repression, cytokine production, immune regulation, DNA repair and chromatin remodeling provide a plausible bridge between cell state and gene expression. It has disease associations including atopic eczema and chronic obstructive asthma and has a substantial literature base.
- **Conclusion**: Established: ZBTB1 is a nuclear regulatory protein with immune and genome-maintenance annotations and is HPA-enhanced in innate lymphoid cells. Hypothesis: it may couple cellular state to the co-abundance pattern, but the module does not establish that it regulates the other genes.

#### PRKD3

- **Related proteins** (co-abundance neighbors): LZTR1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase D3. This gene belongs to the multigene protein kinase D family of serine/threonine kinases, which bind diacylglycerol and phorbol esters. Members of this family are characterized by an N-terminal regulatory domain comprised of a tandem repeat of cysteine-rich zinc-finger motifs and a pleckstrin domain. The C-terminal region contains the catalytic domain and is distantly related to calcium-regulated ki…
- **Diseases (Open Targets)**: acute myeloid leukemia (0.542); mast cell leukemia (0.475); systemic mastocytosis (0.471); mastocytosis (0.462); neurodegenerative disease (0.439)
- **Europe PMC papers**: 569
- **Why important**: PRKD3 is directly connected to the central LZTR1 node and encodes a diacylglycerol-responsive serine/threonine kinase involved in intracellular signalling, protein phosphorylation, phospholipase C-activating receptor signalling and sphingolipid biology. Its disease associations include acute myeloid leukemia and mast-cell disorders, which are relevant to bone-marrow biology. Its kinase activity gives the module a plausible signal-transduction effector.
- **Conclusion**: Established: PRKD3 is a signalling kinase with relevant hematologic disease associations and is detected in both listed tissues. Hypothesis: PRKD3 could be an output arm of the proposed state-regulation program, but its functional connection to the other module genes is not demonstrated.

#### SMG8

- **Related proteins** (co-abundance neighbors): LZTR1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SMG8 nonsense mediated mRNA decay factor. Involved in nuclear-transcribed mRNA catabolic process, nonsense-mediated decay and regulation of protein kinase activity. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Alzahrani-Kuwahara syndrome (0.730); microcephaly (0.483); Short stature (0.483); Intellectual disability (0.483); Abnormal facial shape (0.483)
- **Europe PMC papers**: 261
- **Why important**: SMG8 is connected directly to LZTR1 and represents the RNA-surveillance component of the module through nonsense-mediated mRNA decay. Its annotation also includes regulation of protein kinase activity, providing a possible conceptual link between RNA quality control and signalling. It has disease associations involving neurodevelopmental phenotypes and a meaningful literature base.
- **Conclusion**: Established: SMG8 is a nonsense-mediated mRNA decay factor with broad tissue expression and protein detection in both listed tissues. Hypothesis: its co-abundance with LZTR1 could reflect coordinated quality control during a shared cellular state, but this relationship is not supported by curated interaction data.

#### ELP6

- **Related proteins** (co-abundance neighbors): ZBTB1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: elongator acetyltransferase complex subunit 6. Predicted to be involved in positive regulation of cell migration. Located in cytosol and nucleus. Part of elongator holoenzyme complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Crohn disease (0.328); neurodegenerative disease (0.298); inflammatory bowel disease (0.181); cervical carcinoma (0.169); ulcerative colitis (0.095)
- **Europe PMC papers**: 318
- **Why important**: ELP6 is connected to ZBTB1 and supplies the module's translation-related component through the Elongator holoenzyme, tRNA wobble uridine modification and regulation of translation. It also has an annotation for positive regulation of cell migration and disease links involving Crohn disease, inflammatory bowel disease and neurodegenerative disease. Its position provides a possible bridge between gene-expression control and cellular behaviour despite limited HPA protein detection.
- **Conclusion**: Established: ELP6 is an Elongator-associated translation regulator with disease associations relevant to intestinal inflammation and is the least cell-type-specific member in the HPA summary. Hypothesis: ELP6 may connect transcriptional regulation to translational capacity in the shared module, but that proposed role requires direct testing.

## Module 14

**Tissue pair**: bone_marrow and colon  
**Genes (5)**: MYO18A, PIP4K2C, PTMS, SLC35F3, SREK1

### Function

The module does not have a statistically supported GO or KEGG functional theme: no GO/KEGG term passed global correction. Its gene annotations nevertheless suggest a mixed intracellular program involving membrane and Golgi biology, cytoskeletal organization, nuclear DNA or transcriptional processes, RNA splicing, phosphatidylinositol metabolism, autophagy, and transport. The co-abundance structure is centered on SLC35F3, which is connected to the other module genes, whereas the peripheral genes are not mutually connected. This pattern is more consistent with coordinated abundance across several cellular processes than with a demonstrated single biochemical pathway. The module should therefore be interpreted as a candidate cross-tissue co-abundance signature rather than a proven functional complex.

**Cell composition.** The module is not dominated by secreted or plasma proteins, since none of its members is annotated as secreted. It also does not show a uniform blood-cell composition: some genes have immune-cell enrichment, one is not detected in immune cells, and others have low immune-cell specificity. HPA profiles are heterogeneous, including brain, skeletal muscle, tongue, liver, and broadly distributed expression patterns, with several specialized cell-type associations. Protein detection in both bone marrow and colon is present for most members, supporting detectability in the two tissues, but the heterogeneous tissue and cell-type profiles mean that the shared module could reflect mixed cellular composition, common structural or housekeeping-related demands, or coordinated expression in selected cell populations rather than a bone-marrow–colon-specific pathway. The evidence does not support a simple plasma-protein or uniform blood-cell explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There is no supplementary STRING functional enrichment. None of the possible within-module gene pairs reaches the supplied high-confidence STRING interaction threshold, and no hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not independently corroborated as established physical or functional interactions by these resources. This weakens the case that the module is a canonical protein complex, but it does not invalidate the co-abundance signal: co-regulation, shared cell composition, indirect pathway coupling, or context-dependent interactions could produce the observed structure. The absence of STRING and hu.MAP support should be treated as lack of corroboration, not evidence that the genes are biologically unrelated.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unrecognized cross-tissue co-abundance association because the selected genes have no shared high-confidence STRING interactions, no shared hu.MAP complex membership, no STRING enrichment, and no globally significant GO or KEGG theme. However, these observations do not establish biological novelty. Several members have established molecular annotations and disease literature, and the module may arise from cell-composition effects, correlated abundance without direct binding, or a context-specific regulatory relationship. The defensible conclusion is that the specific bone-marrow–colon co-abundance configuration appears under-characterized in the supplied resources, while the individual genes and their functions are not themselves novel.

**Hypothesis.** Hypothesis: variation in a cell-state or cell-composition program may coordinate SLC35F3-associated membrane or Golgi transport with MYO18A-dependent cytoskeletal and Golgi organization, while PTMS, SREK1, and PIP4K2C report linked nuclear, RNA-processing, and phosphoinositide or autophagy states. In bone marrow and colon, this could reflect shared abundance changes across selected non-secreted cell populations rather than a direct five-protein complex. This hypothesis predicts that the association should be tested with cell-resolved expression, independent cohorts, perturbation of SLC35F3 or its candidate partners, and assays distinguishing co-regulation from physical interaction. The proposed mechanism is not established by the current enrichment or interaction evidence.

### Important genes

#### SLC35F3

- **Related proteins** (co-abundance neighbors): MYO18A (0.92), PTMS (0.87), SREK1 (0.84), PIP4K2C (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 35 member F3. Involved in thiamine transport. Predicted to be integral component of membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypertensive disorder (0.465); neurodegenerative disease (0.369); alcohol drinking (0.338); diverticular disease (0.320); pericarditis (0.309)
- **Europe PMC papers**: 590
- **Why important**: SLC35F3 is the central network node, connected to every other member in the supplied co-abundance graph. It is annotated as a Golgi membrane protein involved in thiamine and choline transport, and its HPA profile is enriched in brain-related tissues and cell types, with immune-cell enrichment in plasmacytoid dendritic cells. Its literature volume is moderate relative to PTMS and MYO18A, so it is a plausible organizing marker but not a well-established module hub in these tissues.
- **Conclusion**: Established evidence supports a membrane or Golgi transport role and centrality within this co-abundance module. It is not established that SLC35F3 physically interacts with the other members or drives their abundance. A plausible hypothesis is that it marks a shared transport or cellular-state program, but this requires experimental validation.

#### MYO18A

- **Related proteins** (co-abundance neighbors): SLC35F3 (0.92); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin XVIIIA. The protein encoded by this gene can bind GOLPH3, linking the Golgi to the cytoskeleton and influencing Golgi membrane trafficking. The encoded protein is also part of a complex that assembles lamellar actomyosin bundles and may be required for cell migration. [provided by RefSeq, Oct 2016].
- **Diseases (Open Targets)**: cancer (0.607); chronic myeloid leukemia (0.371); myelodysplastic syndrome (0.370); acute lymphoblastic leukemia (0.370); leukemia (0.370)
- **Europe PMC papers**: 734
- **Why important**: MYO18A is the most strongly connected peripheral member through its association with SLC35F3. It has established annotations involving Golgi-to-cytoskeleton linkage, Golgi membrane trafficking, actomyosin organization, cell migration, and macrophage activation. HPA detects its protein in both tissues and associates it with muscle, tongue, cardiomyocyte, myonuclear, esophageal, and tuft-cell contexts. Its literature volume is substantial, and its disease associations include hematologic malignancy categories.
- **Conclusion**: Established evidence supports MYO18A as a cytoskeletal and Golgi-trafficking protein that could plausibly connect membrane organization to cellular architecture. Its module relationship is only a co-abundance association, not a demonstrated interaction. A reasonable hypothesis is that MYO18A captures tissue or cell-state variation affecting Golgi and cytoskeletal remodeling.

#### PTMS

- **Related proteins** (co-abundance neighbors): SLC35F3 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Nucleoli, Nucleoli rim; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: parathymosin. Predicted to be involved in DNA replication. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: blood coagulation disease (0.061); insomnia (0.053); Von Willebrand disease (0.045); hemorrhagic disease (0.045); purpura (0.045)
- **Europe PMC papers**: 28077
- **Why important**: PTMS is directly connected to the central SLC35F3 node and has the largest literature volume among the module members. It is annotated with nuclear localization and roles related to DNA replication, transcriptional regulation, and apoptosis. HPA detects it in both tissues and associates it with liver, hepatocytes, megakaryocytes, smooth muscle, and basophils. Its disease associations include coagulation and bleeding-related conditions.
- **Conclusion**: Established evidence supports PTMS as a well-studied nuclear protein with links to replication, transcription, and cell survival. The module does not establish a mechanistic bridge between PTMS and Golgi transport. The association may instead reflect a shared proliferative, survival, or cellular-composition state in the sampled tissues.

#### SREK1

- **Related proteins** (co-abundance neighbors): SLC35F3 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: splicing regulatory glutamic acid and lysine rich protein 1. This gene encodes a member of a family of serine/arginine-rich (SR) splicing proteins containing RNA recognition motif (RRM) domains. The encoded protein interacts with other SR proteins to modulate splice site selection. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jul 2012].
- **Diseases (Open Targets)**: neurodegenerative disease (0.530); lysosomal storage disease (0.361); alcohol drinking (0.347); tongue cancer (0.281); spondylolisthesis (0.244)
- **Europe PMC papers**: 197
- **Why important**: SREK1 is connected to SLC35F3 and is localized to the nucleoplasm and nuclear speckles. Its established annotation identifies it as an SR-family splicing regulator containing RNA-recognition domains and modulating splice-site selection. HPA indicates low tissue and immune-cell specificity, with protein detection in both tissues. Its literature volume is limited relative to PTMS and MYO18A, making it useful as a potentially informative but less characterized module component.
- **Conclusion**: Established evidence supports a role in pre-mRNA splicing and broad cellular expression. It is not established that altered SREK1 abundance causes the other module genes to co-vary. A testable hypothesis is that the module partly reflects a general RNA-processing or transcriptional state coupled indirectly to membrane and cytoskeletal programs.

#### PIP4K2C

- **Related proteins** (co-abundance neighbors): SLC35F3 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphatidylinositol-5-phosphate 4-kinase type 2 gamma. Enables 1-phosphatidylinositol-4-phosphate 5-kinase activity and identical protein binding activity. Involved in several processes, including 1-phosphatidyl-1D-myo-inositol 4,5-bisphosphate biosynthetic process; negative regulation of 1-phosphatidylinositol-4-phosphate 5-kinase activity; and positive regulation of autophagosome assembly. Located in several cellular components, including autophagos…
- **Diseases (Open Targets)**: neurodegenerative disease (0.480); autoimmune disorder of central nervous system (0.347); smoking initiation (0.077); common variable immunodeficiency (0.066); isolated agammaglobulinemia (0.063)
- **Europe PMC papers**: 397
- **Why important**: PIP4K2C is connected to SLC35F3 in the module graph. It has established functions in phosphatidylinositol phosphate metabolism, regulation of insulin-receptor signaling, and positive regulation of autophagosome assembly. HPA places it in the cytosol and associates it with specialized epithelial and reproductive cell types, while showing low immune-cell specificity and detection in both tissues. Its literature volume is modest, and its disease associations include neurodegenerative and autoimmune categories.
- **Conclusion**: Established evidence supports PIP4K2C as a lipid-signaling and autophagy-related regulator. Its co-abundance with SLC35F3 does not demonstrate a direct biochemical relationship. A plausible hypothesis is that phosphoinositide-dependent membrane or autophagy state links this gene to the broader transport and cellular-stress signature.
