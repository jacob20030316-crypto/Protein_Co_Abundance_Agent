# Conserved co-abundance modules: brain and breast

## Module 0

**Tissue pair**: brain and breast  
**Genes (8)**: ACIN1, IKBKG, NUP35, GATAD2A, DPF2, SF3A1, WDR43, YEATS2

### Function

The strongest functional interpretation is a nuclear gene-regulatory and RNA-processing module. The primary evidence is (GO:CC nuclear protein-containing complex; q_global = 0.0439), a globally significant enrichment for nuclear protein-containing complexes involving WDR43, GATAD2A, DPF2, ACIN1, SF3A1, and NUP35. These genes collectively support chromatin remodeling and transcriptional regulation, ribosome biogenesis, pre-mRNA splicing, apoptotic chromatin condensation, and nucleocytoplasmic transport. The supplementary STRING signals for isopeptide-bond biology, Ubl conjugation, and the nucleus (STRING Keyword Isopeptide bond; within-query FDR = 0.0021), (STRING Keyword Ubl conjugation; within-query FDR = 0.0063), (STRING Keyword Nucleus; within-query FDR = 0.0165) are consistent with nuclear regulatory activity, but they are not global enrichment evidence. YEATS2 is the network hub and is annotated as a scaffolding subunit of the ATAC histone-acetyltransferase complex. The module therefore most plausibly reflects coordinated nuclear organization and regulation of gene expression, with linked RNA maturation and stress or cell-fate responses. The enrichment result is driven by a shared cellular program and should not be interpreted as proof that all module genes form one physical complex.

**Cell composition.** The module is composed of intracellular, broadly distributed proteins rather than plasma or secreted proteins: no member is secreted, and all members have low tissue specificity in HPA. Protein detection in both brain and breast for most assessed genes supports reproducible presence in both tissues. HPA does not indicate broad blood-cell enrichment; all members have low immune-cell specificity and no enriched blood-cell category is reported. Some single-cell annotations involve neutrophils, platelets, retinal cells, germ-cell populations, alveolar cells, basal keratinocytes, and oocytes, but these are heterogeneous and do not establish a blood-derived module. The shared co-abundance pattern is therefore more consistent with a broadly expressed nuclear or housekeeping-like regulatory program, possibly influenced by shared cell types or general cellular state, than with a plasma-protein or blood-contamination signal.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC nuclear protein-containing complex | 0.0439 | ACIN1, DPF2, GATAD2A, NUP35, SF3A1, WDR43 |

### STRING and hu.MAP

At the reported high-confidence STRING threshold, none of the possible within-module gene pairs is supported by a STRING interaction, and no hu.MAP complex contains multiple module members. Thus, the module is not a directly recovered known protein complex in these resources. The STRING functional keywords (STRING Keyword Isopeptide bond; within-query FDR = 0.0021), (STRING Keyword Ubl conjugation; within-query FDR = 0.0063), and (STRING Keyword Nucleus; within-query FDR = 0.0165) provide pathway-level or annotation-level support for nuclear and ubiquitin-like regulatory biology, but they do not establish physical interactions among these genes. The star-like co-abundance topology, centered on YEATS2, may reflect coordinated regulation, shared cellular state, or indirect functional coupling rather than a stable molecular assembly.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Isopeptide bond (FDR = 0.0021, 7 genes); Keyword Ubl conjugation (FDR = 0.0063, 7 genes); Keyword Nucleus (FDR = 0.0165, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears to be a potentially new cross-tissue co-abundance association rather than a rediscovery of a known physical complex. The absence of high-confidence STRING edges and multi-member hu.MAP complexes makes the specific network arrangement underrepresented in those resources. However, absence from interaction databases does not prove biological novelty: several members have established roles in chromatin regulation, transcription, splicing, nuclear transport, apoptosis, or NF-kappaB signaling, and the globally significant nuclear-complex annotation (GO:CC nuclear protein-containing complex; q_global = 0.0439) shows that the functional themes are not wholly unprecedented. The defensible claim is novelty of the coordinated brain-breast co-abundance pattern and its YEATS2-centered organization, pending replication in independent cohorts and testing against cell composition and technical effects.

**Hypothesis.** Hypothesis: a shared nuclear regulatory state in brain and breast coordinates YEATS2-associated chromatin regulation with NuRD- and ATAC-related transcriptional control, RNA splicing, ribosome biogenesis, nuclear transport, apoptotic chromatin responses, and NF-kappaB-linked signaling. YEATS2 may act as the principal co-abundance organizer, while the other genes represent parallel nuclear processes that respond to the same cellular state rather than subunits of one physical complex. This hypothesis should be tested by independent co-expression replication, adjustment for cell composition, perturbation of YEATS2, and assays of chromatin accessibility, transcription, splicing, and NF-kappaB activity.

### Important genes

#### YEATS2

- **Related proteins** (co-abundance neighbors): WDR43 (0.89), GATAD2A (0.88), IKBKG (0.82), DPF2 (0.81), ACIN1 (0.81), SF3A1 (0.81), NUP35 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: YEATS domain containing 2. Summary: The protein encoded by this gene is a scaffolding subunit of the ATAC complex, which is a complex with acetyltransferase activity on histones H3 and H4. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, May 2017].
- **Diseases (Open Targets)**: benign adult familial myoclonic epilepsy (0.485); epilepsy, familial adult myoclonic (0.378); prostate carcinoma (0.262); response to antibiotic (0.162); poisoning (0.162)
- **Europe PMC papers**: 556
- **Why important**: YEATS2 is the central network hub, connected to every other module member with comparatively strong co-abundance links. It is a scaffolding subunit of the ATAC histone-acetyltransferase complex and is annotated for chromatin remodeling and transcriptional regulation. Its central topology makes it the leading candidate for organizing the observed module, while its disease associations include familial adult myoclonic epilepsy and prostate carcinoma. Its literature volume is substantial, supporting a biologically grounded interpretation despite the lack of STRING or hu.MAP support.
- **Conclusion**: Established evidence supports YEATS2 as an ATAC-associated chromatin-regulatory scaffold and as the module's co-abundance hub. It is plausible, but not established, that YEATS2 is a causal organizer of the cross-tissue module; direct perturbation is required.

#### GATAD2A

- **Related proteins** (co-abundance neighbors): YEATS2 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GATA zinc finger domain containing 2A. Enables protein-macromolecule adaptor activity. Involved in negative regulation of transcription, DNA-templated. Located in nucleoplasm. Part of NuRD complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.505); Parkinson disease (0.259); Alzheimer disease (0.258); lysosomal storage disease (0.257); Hypercholesterolemia (0.168)
- **Europe PMC papers**: 893
- **Why important**: GATAD2A is part of the NuRD complex and functions in transcriptional repression, chromatin remodeling, and cell-fate regulation. It is connected directly to YEATS2 and contributes to the globally significant nuclear protein-containing complex signal (GO:CC nuclear protein-containing complex; q_global = 0.0439). HPA detects it in both brain and breast, and its disease associations include neurodegenerative disease, Parkinson disease, and Alzheimer disease. Its substantial literature base makes it an important bridge between the network and disease-relevant chromatin biology.
- **Conclusion**: Established evidence supports GATAD2A as a nuclear chromatin-regulatory adaptor with disease relevance. Its participation in this module is consistent with shared transcriptional-state regulation, but the co-abundance data do not show that it physically interacts with YEATS2 in these tissues.

#### SF3A1

- **Related proteins** (co-abundance neighbors): YEATS2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in brain, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 is a core component of the U2 small nuclear ribonucleoprotein and is required for spliceosome assembly and pre-mRNA splicing. It belongs to (GO:CC nuclear protein-containing complex; q_global = 0.0439) and to all three supplementary STRING keyword sets (STRING Keyword Isopeptide bond; within-query FDR = 0.0021), (STRING Keyword Ubl conjugation; within-query FDR = 0.0063), (STRING Keyword Nucleus; within-query FDR = 0.0165). It is detected in brain and breast and has extensive literature coverage, with disease associations that include neurodegenerative disease and diffuse large B-cell lymphoma. It provides a strong mechanistic link from nuclear regulation to RNA processing.
- **Conclusion**: Established evidence supports SF3A1 as a core spliceosomal factor. Its inclusion suggests that the module may couple transcriptional or chromatin state to RNA maturation, but that coupling remains a hypothesis rather than a demonstrated mechanism.

#### WDR43

- **Related proteins** (co-abundance neighbors): YEATS2 (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 43. Enables RNA binding activity. Involved in positive regulation of rRNA processing and positive regulation of transcription by RNA polymerase I. Located in fibrillar center. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: mood disorder (0.232); breast carcinoma (0.190); triple-negative breast carcinoma (0.169); gout (0.160); luminal A breast carcinoma (0.140)
- **Europe PMC papers**: 371
- **Why important**: WDR43 is the only low-degree peripheral member that contributes directly to (GO:CC nuclear protein-containing complex; q_global = 0.0439) and to the supplementary nuclear, isopeptide-bond, and Ubl-conjugation signals (STRING Keyword Isopeptide bond; within-query FDR = 0.0021), (STRING Keyword Ubl conjugation; within-query FDR = 0.0063), (STRING Keyword Nucleus; within-query FDR = 0.0165). It is annotated for RNA binding, ribosomal small-subunit biogenesis, rRNA processing, and RNA polymerase transcriptional regulation. It is detected in brain but not breast by the reported HPA IHC result, and its disease associations include breast carcinoma and mood disorder. Its lower network connectivity does not diminish its value as a functionally informative peripheral component.
- **Conclusion**: Established evidence supports WDR43 in rRNA processing and transcriptional regulation. Its module association may indicate coordinated nucleolar and nuclear activity, but the breast co-abundance relationship should be independently replicated because the reported protein detection is asymmetric.

#### IKBKG

- **Related proteins** (co-abundance neighbors): YEATS2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inhibitor of nuclear factor kappa B kinase regulatory subunit gamma. This gene encodes the regulatory subunit of the inhibitor of kappaB kinase (IKK) complex, which activates NF-kappaB resulting in activation of genes involved in inflammation, immunity, cell survival, and other pathways. Mutations in this gene result in incontinentia pigmenti, hypohidrotic ectodermal dysplasia, and several other types of immunodeficiencies. A pseudogene highly similar to this locus…
- **Diseases (Open Targets)**: incontinentia pigmenti (0.832); ectodermal dysplasia and immunodeficiency 1 (0.806); immunodeficiency 33 (0.768); ectodermal dysplasia and immune deficiency (0.661); autoinflammatory disease, X-linked (0.641)
- **Europe PMC papers**: 2838
- **Why important**: IKBKG encodes NEMO, the regulatory subunit of the IKK complex that activates NF-kappaB and thereby controls inflammation, immunity, cell survival, apoptosis, and antiviral responses. It is connected to the YEATS2 hub and contributes to the supplementary isopeptide-bond, Ubl-conjugation, and nucleus signals (STRING Keyword Isopeptide bond; within-query FDR = 0.0021), (STRING Keyword Ubl conjugation; within-query FDR = 0.0063), (STRING Keyword Nucleus; within-query FDR = 0.0165). HPA detects it in both brain and breast, and its disease associations include incontinentia pigmenti, ectodermal dysplasia, and immunodeficiency. Its large literature base makes it the most established signaling component in the module.
- **Conclusion**: Established evidence supports IKBKG as a central NF-kappaB signaling regulator with strong immune and developmental disease relevance. Its association with this broadly nuclear module may reflect integration of inflammatory signaling with nuclear transcriptional state, but this is a hypothesis and not evidence of a physical complex with the other members.

## Module 1

**Tissue pair**: brain and breast  
**Genes (16)**: AKAP8L, CHAMP1, CHCHD7, CMTM6, CEP250, SPECC1L, DIDO1, GALNS, GLYR1, HDGF, NIPBL, RAB11FIP1, RPTOR, RSF1, WDR26, ZNF638

### Function

The module most plausibly reflects a broadly expressed nuclear regulatory program that combines chromatin organization, transcriptional control, RNA processing, chromosome segregation, and cell-cycle-related functions. This interpretation is supported by the annotations of RSF1, GLYR1, NIPBL, AKAP8L, ZNF638, CHAMP1, and CEP250, which respectively implicate chromatin remodeling, nucleosome-associated regulation, cohesin loading, mRNA export and chromatin regulation, RNA splicing, kinetochore function, and centrosome cohesion. Additional genes connect this nuclear program to vesicle trafficking, actin organization, lysosomal degradation, growth signaling, and apoptosis. CHCHD7 is the prominent network hub and links many of these functionally diverse genes, although the co-abundance edges should not be interpreted as direct physical interactions. No GO or KEGG term passed global correction, so the functional interpretation is based on the collective gene annotations and network architecture rather than statistically significant pathway enrichment.

**Cell composition.** The module does not appear to be primarily a plasma-protein or secreted-protein module. HPA assigns low tissue specificity to every member, and the genes are detected at the protein level in both brain and breast for nearly the entire module, supporting a broadly expressed cellular program rather than a tissue-restricted signature. The module is also not broadly blood-cell-specific: HPA reports low immune-cell specificity for nearly all members, although several genes show enhancement in neutrophils, megakaryocytes, or other cell types. RAB11FIP1 is enhanced in neutrophils and is immune-cell enhanced, while HDGF is secreted to blood and two genes are classified as secreted or intracellular-and-membrane proteins. These findings leave open some contribution from shared blood or stromal cell populations, but they do not support interpreting the whole module as a blood-protein module. HPA cell-type annotations also include neural, epithelial, glial, and proliferative cell types, consistent with a shared housekeeping or cell-state-associated program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supplies only two high-confidence relationships within the module: NIPBL with RSF1 and NIPBL with ZNF638. These relationships provide focused support for a chromatin and transcriptional-regulatory core, but STRING provides no functional enrichment for the module. hu.MAP identifies one complex containing CHAMP1 and RSF1 (hu.MAP huMAP3_11539.1), but the module contains only a small subset of that larger complex and the remaining listed members are outside the module. Thus, the hu.MAP evidence supports a possible connection between chromosome segregation and chromatin-associated machinery, without establishing that the entire co-abundance module is one physical complex. The contrast between the co-abundance network and the sparse STRING and hu.MAP overlap indicates that many observed associations may be indirect, state-dependent, or driven by coordinated expression rather than established protein binding.

**STRING interactions (score >= 0.7)**: 2 of 120 gene pairs: NIPBL–RSF1 (0.72); NIPBL–ZNF638 (0.745)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11539.1 (CHAMP1, RSF1; 2/32)

### Novelty

This is a potentially novel conserved co-abundance module, but the fact sheet does not establish that it is a newly discovered molecular complex or a new pathway. The module brings together a strongly connected CHCHD7-centered expression structure with a smaller, independently supported NIPBL-linked chromatin subgroup and a CHAMP1-RSF1 hu.MAP connection. That particular cross-functional combination may be novel as a brain-breast co-abundance pattern. However, absence of many module edges from STRING or hu.MAP cannot by itself demonstrate novelty, because those resources emphasize experimentally supported physical or functional relationships and do not comprehensively represent co-abundance associations. The lack of globally significant GO or KEGG enrichment also prevents claiming a newly defined pathway on enrichment grounds. Novelty should therefore be framed as a candidate conserved expression module requiring replication and experimental validation.

**Hypothesis.** Hypothesis: the module represents a shared cellular state in brain and breast in which chromatin accessibility, transcription and RNA handling, chromosome or centrosome organization, and membrane-trafficking processes are coordinately regulated. CHCHD7 may occupy a central co-abundance position linking nuclear, cytoskeletal, and trafficking-related components, while NIPBL, RSF1, and ZNF638 may form a regulatory axis connecting cohesin loading, chromatin remodeling, and RNA processing. RPTOR, RAB11FIP1, CMTM6, and HDGF could reflect growth, recycling, and extracellular signaling consequences of that state. This is a mechanistic model rather than an established interaction map; direct binding, causal regulation, and the cellular source of the shared signal must be tested experimentally.

### Important genes

#### CHCHD7

- **Related proteins** (co-abundance neighbors): SPECC1L (0.91), RAB11FIP1 (0.90), RPTOR (0.87), RSF1 (0.86), AKAP8L (0.85), HDGF (0.83), CHAMP1 (0.83), GLYR1 (0.81), ZNF638 (0.81), WDR26 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cell Junctions; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coiled-coil-helix-coiled-coil-helix domain containing 7. Predicted to be located in mitochondrial intermembrane space. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Salivary Gland Pleomorphic Adenoma (0.370); Parotid Gland Pleomorphic Adenoma (0.370); salivary gland carcinoma ex pleomorphic adenoma (0.370); salivary gland adenoid cystic carcinoma (0.370); salivary gland mucoepidermoid carcinoma (0.277)
- **Europe PMC papers**: 316
- **Why important**: CHCHD7 is the central network hub, with the strongest weighted connectivity in the module and links to genes involved in actin organization, vesicle recycling, mTOR regulation, chromatin-associated processes, chromosome alignment, and growth signaling. Its MyGene.info annotation places it in the mitochondrial intermembrane space and associates it with mitochondrial respiratory-chain complex assembly. It has broad literature coverage and disease links to salivary-gland tumors, while HPA detects it in brain but not breast, making its cross-tissue co-abundance especially worth checking.
- **Conclusion**: Established: CHCHD7 is the module's principal co-abundance hub and has a reported mitochondrial respiratory-chain association. Hypothesis: it may coordinate mitochondrial or cellular energetic state with the nuclear, cytoskeletal, and trafficking signals represented by its neighbors. Its centrality does not prove that it physically regulates those partners.

#### NIPBL

- **Related proteins** (co-abundance neighbors): CEP250 (0.81); STRING partners: RSF1 (0.72), ZNF638 (0.745)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NIPBL cohesin loading factor. This gene encodes the homolog of the Drosophila melanogaster Nipped-B gene product and fungal Scc2-type sister chromatid cohesion proteins. The Drosophila protein facilitates enhancer-promoter communication of remote enhancers and plays a role in developmental regulation. It is also homologous to a family of chromosomal adherins with broad roles in sister chromatid cohesion, chromosome condensatio…
- **Diseases (Open Targets)**: Cornelia de Lange syndrome (0.864); hereditary disease (0.544); Dislocated radial head (0.462); Intellectual disability (0.384); low grade glioma (0.370)
- **Europe PMC papers**: 2494
- **Why important**: NIPBL is a cohesin-loading factor with roles in sister-chromatid segregation, chromatin remodeling, enhancer-promoter communication, development, and DNA repair. It has direct high-confidence STRING relationships with RSF1 and ZNF638, providing the clearest supported bridge between the module's chromatin and RNA-regulatory components. Its disease association with Cornelia de Lange syndrome and intellectual disability gives the gene strong biological relevance, and it has substantial literature coverage.
- **Conclusion**: Established: NIPBL is a major chromosomal and gene-regulatory factor and is the module's STRING-supported connector to RSF1 and ZNF638. Hypothesis: variation in cohesin loading or enhancer-promoter regulation could help generate the shared co-abundance state across brain and breast.

#### RSF1

- **Related proteins** (co-abundance neighbors): CHCHD7 (0.86), DIDO1 (0.80); STRING partners: NIPBL (0.72)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, breast
- **hu.MAP 3.0**: huMAP3_11539.1
- **Function (MyGene.info)**: remodeling and spacing factor 1. This gene encodes a nuclear protein that interacts with hepatitis B virus X protein (HBX) and facilitates transcription of hepatitis B virus genes by the HBX transcription activator, suggesting a role for this interaction in the virus life cycle. This protein also interacts with SNF2H protein to form the RSF chromatin-remodeling complex, where the SNF2H subunit functions as the nucleosome-dependen…
- **Diseases (Open Targets)**: myopathy (0.313); neurodevelopmental disorder (0.187); infection (0.172); handedness (0.156); neoplasm (0.101)
- **Europe PMC papers**: 783
- **Why important**: RSF1 is a nucleoplasmic histone chaperone and component of the RSF chromatin-remodeling complex. Its annotations include chromatin organization, nucleosome assembly, transcriptional regulation, and heterochromatin formation. RSF1 participates in hu.MAP complex (hu.MAP huMAP3_11539.1) with CHAMP1 and has a STRING relationship with NIPBL, placing it at the intersection of the two strongest external evidence types in the module. It also has substantial literature coverage.
- **Conclusion**: Established: RSF1 has documented chromatin-remodeling functions, is part of hu.MAP complex (hu.MAP huMAP3_11539.1), and is linked by STRING to NIPBL. Hypothesis: RSF1 may help couple chromatin state to chromosome segregation or transcriptional output in the conserved module.

#### RPTOR

- **Related proteins** (co-abundance neighbors): CHCHD7 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Lysosomes; IHC detected in brain, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: regulatory associated protein of MTOR complex 1. This gene encodes a component of a signaling pathway that regulates cell growth in response to nutrient and insulin levels. The encoded protein forms a stoichiometric complex with the mTOR kinase, and also associates with eukaryotic initiation factor 4E-binding protein-1 and ribosomal protein S6 kinase. The protein positively regulates the downstream effector ribosomal protein S6 kinase, and negat…
- **Diseases (Open Targets)**: neurodegenerative disease (0.440); Abnormality of the skeletal system (0.393); dengue disease (0.371); congestive heart failure (0.319); obesity disorder (0.304)
- **Europe PMC papers**: 6928
- **Why important**: RPTOR is a core component of the mTOR complex one signaling system and regulates cell growth, cell size, starvation responses, endothelial proliferation, and DNA-damage responses. It is connected to the network hub CHCHD7 and has by far the largest literature volume among the module genes. Its disease associations span neurodegenerative, metabolic, cardiovascular, and infectious contexts, making it a strong candidate for interpreting shared cellular-state biology.
- **Conclusion**: Established: RPTOR is a central mTOR-associated growth and nutrient-response regulator with broad disease relevance. Hypothesis: its co-abundance with CHCHD7 may indicate that energetic or nutrient-sensitive signaling is coordinated with the module's chromatin and trafficking program, but this cannot be inferred as a direct molecular interaction.

#### SPECC1L

- **Related proteins** (co-abundance neighbors): CHCHD7 (0.91); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Actin filaments; IHC detected in brain, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sperm antigen with calponin homology and coiled-coil domains 1 like. This gene encodes a coiled-coil domain containing protein. The encoded protein may play a critical role in actin-cytoskeletal reorganization during facial morphogenesis. Mutations in this gene are a cause of oblique facial clefting-1. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. A read-through transcript composed of SPECC1L (sperm antigen w…
- **Diseases (Open Targets)**: Teebi hypertelorism syndrome 1 (0.728); Opitz G/BBB syndrome (0.648); Teebi hypertelorism syndrome (0.607); Tessier number 4 facial cleft (0.589); neurodegenerative disease (0.489)
- **Europe PMC papers**: 624
- **Why important**: SPECC1L is connected directly to CHCHD7 and encodes a coiled-coil protein associated with actin-cytoskeleton organization and cell adhesion. It is implicated in facial morphogenesis and several craniofacial disorders, and HPA shows enrichment across multiple neural and epithelial cell types while detecting the protein in both brain and breast. Its literature volume is substantial relative to many of the less characterized module members.
- **Conclusion**: Established: SPECC1L has reported roles in actin-cytoskeletal reorganization, cell adhesion, and craniofacial development. Hypothesis: it may connect CHCHD7-centered intracellular organization to tissue architecture or cell adhesion in both tissues.

## Module 2

**Tissue pair**: brain and breast  
**Genes (8)**: ALB, ALDOB, CS, EIF4A2, MDH1, NME1, NME3, STMN2

### Function

The strongest functional signal is nucleotide-phosphate metabolism. NME1 and NME3 jointly support UTP biosynthesis, UTP metabolism, and GTP biosynthesis, all supported by globally corrected enrichment (GO:BP UTP biosynthetic process; q_global = 0.0301), (GO:BP UTP metabolic process; q_global = 0.0301), and (GO:BP GTP biosynthetic process; q_global = 0.0447). The supplementary STRING annotations independently identify both genes as nucleoside diphosphate kinases (5 supplementary STRING terms; within-query FDR 0.0099–0.0345). The remaining genes suggest broader metabolic and cellular context: ALDOB participates in glycolysis and fructose metabolism, MDH1 in cytosolic malate metabolism and the malate-aspartate shuttle, CS in mitochondrial citrate metabolism, EIF4A2 in translation initiation, and STMN2 in neuronal microtubule regulation. Thus, the most defensible interpretation is a nucleotide-supply signal embedded in a mixed metabolic, translational, and neuronal-expression background. The enrichment is concentrated in the NME1–NME3 pair rather than distributed across the whole module, so it should not be interpreted as proof that every module member performs the same function.

**Cell composition.** This is not predominantly a plasma or secreted-protein module. Albumin is explicitly secreted to blood and is liver- and hepatocyte-enriched, making it a plausible circulating or sample-composition marker, but secreted proteins are a minority of the module. The HPA profile instead indicates a heterogeneous mixture of broadly expressed or metabolic proteins, tissue-enriched proteins, and cell-type-associated proteins. ALDOB is enriched in intestine, kidney, and liver and is not detected in brain or breast by the supplied protein evidence; STMN2 is brain-enriched and associated with neuronal cell types; MDH1 and CS show enhanced expression in muscle- or tongue-related tissues; and NME1, NME3, and EIF4A2 have low tissue or immune specificity. Most genes have low immune-cell specificity, although STMN2 is immune-cell enriched for plasmacytoid dendritic cells. The combination of albumin, tissue-mismatched metabolic markers, and broad housekeeping-like genes means that shared blood, stromal, or cellular composition effects should be considered alongside a biological brain–breast program. Protein detection is also incomplete in both tissues, and ALDOB and ALB are not detected in the supplied brain or breast protein measurements.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP UTP biosynthetic process | 0.0301 | NME1, NME3 |
| GO:BP UTP metabolic process | 0.0301 | NME1, NME3 |
| GO:BP GTP biosynthetic process | 0.0447 | NME1, NME3 |

### STRING and hu.MAP

STRING supports a single high-confidence relationship within the module: NME1–NME3 (5 supplementary STRING terms; within-query FDR 0.0099–0.0345). This relationship is concordant with their shared globally significant nucleotide-biosynthesis annotations (GO:BP UTP biosynthetic process; q_global = 0.0301) (GO:BP UTP metabolic process; q_global = 0.0301) (GO:BP GTP biosynthetic process; q_global = 0.0447), so the NME pair is an established molecular subunit of the module rather than an inference based only on co-abundance. hu.MAP independently places NME1 and NME3 together in complexes (hu.MAP huMAP3_04679.1) and (hu.MAP huMAP3_07150.1), alongside NME2, NME4, NDUFA4 and, in one complex, additional proteins. The other module members are not represented in the supplied STRING high-confidence interactions or hu.MAP complexes. Therefore, the module contains a validated NME1–NME3 core but lacks evidence for a physical complex spanning all members. The remaining links, especially the ALDOB-centered co-abundance relationships, should be treated as expression-level associations rather than established physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 28 gene pairs: NME1–NME3 (0.989)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART These are enzymes that catalyze nonsubstrate specific conversions of nucleoside diphosphates to nucleoside triphosphates. These enzymes play important roles in bacterial growth, signal transduction and pathogenicity. (FDR = 0.0099, 2 genes); InterPro Nucleoside diphosphate kinase (FDR = 0.0345, 2 genes); InterPro Nucleoside diphosphate kinase, active site (FDR = 0.0345, 2 genes); InterPro Nucleoside diphosphate kinase-like domain (FDR = 0.0345, 2 genes); InterPro Nucleoside diphosphate kinase-like domain superfamily (FDR = 0.0345, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04679.1 (NME1, NME3; 2/5); huMAP3_07150.1 (NME1, NME3; 2/8)

### Novelty

The NME1–NME3 relationship and their nucleoside diphosphate kinase function are established, as shown by STRING, hu.MAP, and the corrected enrichment terms. The potentially novel aspect is the particular cross-tissue co-abundance module that places this known NME pair with ALDOB, MDH1, STMN2, ALB, EIF4A2, and CS, with ALDOB acting as the central co-abundance connector. However, the supplied evidence does not establish that this whole module is a new biological complex or a new pathway. Lack of STRING or hu.MAP support for the full set is compatible with novelty, but it is not proof of novelty because co-abundance edges may reflect shared cell composition, circulating albumin, tissue contamination, technical effects, or context-dependent regulation. A claim of a new finding would require independent replication, control for cell-type and blood-derived signals, and validation beyond the existing NME relationships.

**Hypothesis.** Hypothesis: in brain and breast samples, a shared cellular or sample-composition state may couple nucleotide-triphosphate supply through the NME1–NME3 pair with energetic and biosynthetic metabolism through ALDOB, MDH1, and CS, while EIF4A2 and STMN2 reflect translational and neuronal or cytoskeletal context. Albumin may add a blood-derived component, and ALDOB may appear central because it tracks the mixture of metabolic and tissue-associated signals rather than physically organizing the module. A testable prediction is that the NME1–NME3 relationship will remain after adjustment for cell type and blood contamination, whereas the ALB and ALDOB associations may weaken; the neuronal STMN2 association should also depend on the neuronal contribution of the samples.

### Important genes

#### ALDOB

- **Related proteins** (co-abundance neighbors): MDH1 (0.90), STMN2 (0.89), NME3 (0.89), ALB (0.88), EIF4A2 (0.84), NME1 (0.82), CS (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldolase, fructose-bisphosphate B. Fructose-1,6-bisphosphate aldolase (EC 4.1.2.13) is a tetrameric glycolytic enzyme that catalyzes the reversible conversion of fructose-1,6-bisphosphate to glyceraldehyde 3-phosphate and dihydroxyacetone phosphate. Vertebrates have 3 aldolase isozymes which are distinguished by their electrophoretic and catalytic properties. Differences indicate that aldolases A, B, and C are distinct proteins, th…
- **Diseases (Open Targets)**: hereditary fructose intolerance (0.846); hereditary disease (0.518); acute liver failure (0.463); disorder of glycogen metabolism (0.455); carbohydrate metabolism disease (0.357)
- **Europe PMC papers**: 2383
- **Why important**: ALDOB is the central co-abundance connector in the supplied network, linking every other member without corresponding STRING or hu.MAP support. It is a glycolytic fructose-bisphosphate aldolase with liver, intestine, and kidney enrichment, and it has established associations with hereditary fructose intolerance and liver-related disease. Its literature is substantial. Its absence in the supplied brain and breast protein detection is important because it makes a transcript-level, cell-composition, or sample-quality explanation plausible.
- **Conclusion**: Established: ALDOB is a metabolic enzyme and the network-level hub of this module. Hypothesis: ALDOB may be a shared metabolic-state marker or a composition-sensitive connector rather than the mechanistic driver of the whole module.

#### NME1

- **Related proteins** (co-abundance neighbors): ALDOB (0.82); STRING partners: NME3 (0.989)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain, breast
- **hu.MAP 3.0**: huMAP3_04679.1, huMAP3_07150.1
- **Function (MyGene.info)**: NME/NM23 nucleoside diphosphate kinase 1. This gene (NME1) was identified because of its reduced mRNA transcript levels in highly metastatic cells. Nucleoside diphosphate kinase (NDK) exists as a hexamer composed of 'A' (encoded by this gene) and 'B' (encoded by NME2) isoforms. Mutations in this gene have been identified in aggressive neuroblastomas. Two transcript variants encoding different isoforms have been found for this gene. Co-tra…
- **Diseases (Open Targets)**: placenta praevia (0.211); Dermatochalasis (0.136); neoplasm (0.117); smoking initiation (0.113); melanoma (0.112)
- **Europe PMC papers**: 3306
- **Why important**: NME1 is part of the only STRING-supported high-confidence pair in the module and occurs with NME3 in both supplied hu.MAP complexes (hu.MAP huMAP3_04679.1) and (hu.MAP huMAP3_07150.1). It contributes to all primary globally corrected terms (GO:BP UTP biosynthetic process; q_global = 0.0301) (GO:BP UTP metabolic process; q_global = 0.0301) (GO:BP GTP biosynthetic process; q_global = 0.0447) and has a well-established nucleoside diphosphate kinase function. It also has extensive literature and disease links involving aggressive neuroblastoma and other disease annotations.
- **Conclusion**: Established: NME1 is a strong candidate for the functional core because its molecular interaction and nucleotide-biosynthesis annotations agree. Hypothesis: its co-abundance with the broader module may indicate increased nucleotide demand or cellular stress, but the supplied data do not establish that mechanism.

#### NME3

- **Related proteins** (co-abundance neighbors): ALDOB (0.89); STRING partners: NME1 (0.989)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_04679.1, huMAP3_07150.1
- **Function (MyGene.info)**: NME/NM23 nucleoside diphosphate kinase 3. Predicted to enable nucleoside diphosphate kinase activity. Predicted to be involved in apoptotic process and nucleotide metabolic process. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: atrial fibrillation (0.094); atrial flutter (0.092); genetic developmental and epileptic encephalopathy (0.072); undetermined early-onset epileptic encephalopathy (0.063); familial infantile myoclonic epilepsy (0.060)
- **Europe PMC papers**: 882
- **Why important**: NME3 forms the validated NME1–NME3 pair, is present in both supplied hu.MAP complexes (hu.MAP huMAP3_04679.1) and (hu.MAP huMAP3_07150.1), and contributes to every primary enriched term (GO:BP UTP biosynthetic process; q_global = 0.0301) (GO:BP UTP metabolic process; q_global = 0.0301) (GO:BP GTP biosynthetic process; q_global = 0.0447) as well as all supplementary STRING functional annotations (5 supplementary STRING terms; within-query FDR 0.0099–0.0345). It has low tissue and cell-type specificity, consistent with a  broadly distributed intracellular nucleotide-metabolism role, and has disease annotations including epileptic encephalopathy.
- **Conclusion**: Established: NME3 is a functionally concordant partner of NME1 and is central to the module's strongest evidence. Hypothesis: NME3 may help connect a broadly expressed nucleotide-supply program to tissue-specific metabolic states, but this broader role remains untested here.

#### STMN2

- **Related proteins** (co-abundance neighbors): ALDOB (0.89); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: stathmin 2. This gene encodes a member of the stathmin family of phosphoproteins. Stathmin proteins function in microtubule dynamics and signal transduction. The encoded protein plays a regulatory role in neuronal growth and is also thought to be involved in osteogenesis. Reductions in the expression of this gene have been associated with Down's syndrome and Alzheimer's disease. Alternatively spliced transcri…
- **Diseases (Open Targets)**: neurodegenerative disease (0.371); schizophrenia (0.313); intelligence (0.312); immune system disorder (0.307); alcohol drinking (0.275)
- **Europe PMC papers**: 2193
- **Why important**: STMN2 provides the clearest brain-specific biological context: it is tissue-enriched in brain, associated with excitatory and inhibitory neurons and other brain neuronal populations, and functions in microtubule dynamics and neurite development. It has substantial literature and associations with neurodegenerative disease, schizophrenia, and related traits. Its direct network connection is only to ALDOB, and it lacks supplied STRING or hu.MAP support.
- **Conclusion**: Established: STMN2 is a neuronal cytoskeletal and neurite-related marker that may explain the brain component of the shared module. Hypothesis: its co-abundance with metabolic genes may reflect neuronal energetic or structural demand, but it could alternatively mark neuronal cell content.

#### ALB

- **Related proteins** (co-abundance neighbors): ALDOB (0.88); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB is the most conspicuous composition-sensitive member. It is liver- and hepatocyte-enriched, secreted to blood, and encodes the major plasma albumin carrier. It has very extensive literature and broad disease associations. It is connected to ALDOB in the module but has no supplied STRING or hu.MAP support, and its protein is not detected in the supplied brain or breast measurements.
- **Conclusion**: Established: ALB is a circulating plasma protein and a plausible blood-derived or sample-quality marker. Hypothesis: its inclusion may reflect blood content or shared vascular exposure rather than a tissue-intrinsic component of the conserved brain–breast mechanism.

## Module 3

**Tissue pair**: brain and breast  
**Genes (7)**: ANAPC16, HAPLN2, IDUA, NFKBIB, TIMM8A, USF1, UTS2

### Function

The module does not support a single statistically established GO or KEGG function: no GO/KEGG term passed global correction, and STRING reported no supplementary functional enrichment. Its genes nevertheless suggest several biological themes. HAPLN2 represents extracellular-matrix and hyaluronan-related biology with a strong brain and oligodendrocyte association. UTS2 represents a secreted vasoactive peptide with links to blood-pressure regulation, vascular diameter, muscle contraction, and synaptic signaling. IDUA represents lysosomal glycosaminoglycan degradation. TIMM8A represents mitochondrial inner-membrane protein import and nervous-system biology. USF1 represents transcriptional regulation and glucose or hypoxia-responsive signaling, while NFKBIB represents regulation of NF-kappa-B activation. ANAPC16 represents anaphase-promoting-complex activity and ubiquitin-dependent cell-cycle regulation. Overall, the module is better interpreted as a heterogeneous co-abundance signature spanning extracellular, vascular, mitochondrial, lysosomal, transcriptional, inflammatory, and cell-cycle-related biology rather than as an established pathway.

**Cell composition.** The module is not predominantly composed of secreted or plasma proteins. HAPLN2 is secreted in brain, and UTS2 is secreted to blood; IDUA is reported as intracellular and membrane-associated rather than a plasma protein. Most genes have low tissue specificity and low immune-cell specificity, which argues against a strongly blood-cell-defined module. UTS2 is immune-cell enriched in T-reg cells, so a contribution from shared immune or circulating-cell content remains possible. The tissue pattern is mixed: HAPLN2 is brain-enriched and oligodendrocyte-enriched, NFKBIB is testis-enhanced and enriched in spermatid groups, UTS2 is enhanced in adrenal gland, bone marrow, and brain, and TIMM8A is enhanced in several basal or progenitor-like cell populations. Protein detection in both brain and breast for several genes is compatible with a shared measurable tissue signature, but the absence of breast protein detection for HAPLN2 and the lack of immunohistochemical detection for UTS2 mean that the conserved co-abundance pattern should not automatically be interpreted as a breast-localized version of a brain-specific biological program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

None of the possible gene pairs reached the fact-sheet threshold for a STRING interaction, and STRING supplied no functional enrichment. No hu.MAP complex contained multiple module members. Therefore, the module is not supported by high-confidence prior protein-interaction or complex membership evidence. The co-abundance edges are consequently distinct from established physical interactions and may reflect coordinated regulation, shared cell composition, tissue mixture, indirect biology, or technical covariance. The internal network has two comparatively central connectors, ANAPC16 and HAPLN2. ANAPC16 links IDUA, NFKBIB, and USF1, whereas HAPLN2 links USF1, TIMM8A, and UTS2. This organization creates a bridge between a regulatory or ubiquitination-related branch and an extracellular, mitochondrial, and vasoactive branch, but it does not establish a molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a new co-abundance observation, but it cannot be called a newly discovered biological pathway on the present evidence. The lack of STRING interactions and hu.MAP complexes makes the particular combination of genes less obviously represented as a known physical module, yet database absence alone does not prove novelty. The genes themselves are individually well characterized to differing degrees, and several have substantial disease or literature associations. The strongest defensible novelty claim is therefore that their conserved co-abundance across brain and breast is a potentially novel systems-level association requiring independent validation, not that the underlying functions or interactions are novel.

**Hypothesis.** Hypothesis: the conserved signature reflects a shared tissue-state or cell-composition program that couples extracellular-matrix and vascular signaling with cellular stress and organelle maintenance. In this model, HAPLN2 and UTS2 mark extracellular or secreted signaling, TIMM8A and IDUA reflect mitochondrial and lysosomal maintenance, and USF1, NFKBIB, and ANAPC16 provide regulatory links involving transcription, NF-kappa-B restraint, ubiquitination, and cell-cycle control. A more cautious alternative is that the apparent bridge is generated by shared cell types or circulating material, particularly because UTS2 is blood-secreted and T-reg enriched while HAPLN2 is strongly brain-associated. This hypothesis should be tested with cell-resolved data, independent cohorts, protein-level measurements, and perturbation or interaction assays rather than inferred solely from co-abundance.

### Important genes

#### HAPLN2

- **Related proteins** (co-abundance neighbors): USF1 (0.84), TIMM8A (0.83), UTS2 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hyaluronan and proteoglycan link protein 2. Predicted to enable hyaluronic acid binding activity. Predicted to be involved in central nervous system development and skeletal system development. Predicted to act upstream of or within establishment of blood-nerve barrier and extracellular matrix assembly. Predicted to be located in extracellular region. Predicted to be active in extracellular matrix. [provided by Alliance of Genome Resources,…
- **Diseases (Open Targets)**: craniosynostosis (0.118); Parkinson disease (0.078); diabetic ketoacidosis (0.051); autosomal dominant optic atrophy, classic form (0.046); Stargardt disease (0.035)
- **Europe PMC papers**: 288
- **Why important**: HAPLN2 is one of the most connected genes in the co-abundance subgraph and links the module's extracellular branch to USF1, TIMM8A, and UTS2. Its annotation supports hyaluronan binding, extracellular-matrix assembly, cell adhesion, central nervous-system development, and skeletal development. HPA identifies it as brain-enriched, oligodendrocyte-enriched, and secreted in brain, while its protein was not detected in breast. It has a meaningful disease literature including craniosynostosis, Parkinson disease, optic atrophy, and Stargardt disease.
- **Conclusion**: Established: HAPLN2 is the strongest tissue-specific and extracellular anchor of the module, especially for brain biology. Hypothesis: its co-abundance with TIMM8A and UTS2 may reflect a coordinated extracellular-neural or vascular state, but the lack of STRING and hu.MAP support means this is not an established physical pathway.

#### USF1

- **Related proteins** (co-abundance neighbors): HAPLN2 (0.84), ANAPC16 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: upstream transcription factor 1. This gene encodes a member of the basic helix-loop-helix leucine zipper family, and can function as a cellular transcription factor. The encoded protein can activate transcription through pyrimidine-rich initiator (Inr) elements and E-box motifs. This gene has been linked to familial combined hyperlipidemia (FCHL). Alternative splicing of this gene results in multiple transcript variants. A relate…
- **Diseases (Open Targets)**: neurodegenerative disease (0.438); breast cancer (0.095); breast carcinoma (0.095); glioma (0.093); central nervous system cancer (0.093)
- **Europe PMC papers**: 3190
- **Why important**: USF1 is a bridge between ANAPC16 and HAPLN2 and is the principal transcriptional-regulatory candidate in the module. It is a basic helix-loop-helix leucine-zipper transcription factor that regulates transcription through initiator and E-box motifs and is annotated for hypoxia response, glucose metabolism, and glucose-mediated signaling. It has the largest literature presence among the module genes and disease associations including familial combined hyperlipidemia, neurodegenerative disease, breast cancer, glioma, and central nervous-system cancer.
- **Conclusion**: Established: USF1 is a plausible regulator of gene-expression state and metabolic or stress responses, and its network position makes it a natural candidate bridge. Hypothesis: USF1 could coordinate the otherwise heterogeneous module, but the co-abundance data do not demonstrate that it regulates the other module genes in these tissues.

#### ANAPC16

- **Related proteins** (co-abundance neighbors): IDUA (0.88), NFKBIB (0.85), USF1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in brain, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: anaphase promoting complex subunit 16. Involved in protein ubiquitination. Located in cytosol and kinetochore. Part of anaphase-promoting complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.235); osteoarthritis, knee (0.102); alcohol drinking (0.064); Alzheimer disease (0.060); ovarian dysfunction (0.060)
- **Europe PMC papers**: 128
- **Why important**: ANAPC16 has the strongest connective position in the subgraph and links IDUA, NFKBIB, and USF1. It is an anaphase-promoting-complex subunit involved in protein ubiquitination, mitotic and meiotic cell-cycle regulation, and ubiquitin-linked catabolic processes. Its protein was detected in both brain and breast, and its disease-oriented associations include neurodegenerative disease, Alzheimer disease, osteoarthritis, and ovarian dysfunction.
- **Conclusion**: Established: ANAPC16 is a broadly expressed intracellular component that could report shared proteostasis or proliferative state rather than a tissue-specific function. Hypothesis: its central network position may indicate a regulatory or covariance bridge connecting ubiquitination with transcriptional, inflammatory, and lysosomal signals, but no complex or interaction evidence confirms that mechanism.

#### IDUA

- **Related proteins** (co-abundance neighbors): ANAPC16 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in brain, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alpha-L-iduronidase. This gene encodes an enzyme that hydrolyzes the terminal alpha-L-iduronic acid residues of two glycosaminoglycans, dermatan sulfate and heparan sulfate. This hydrolysis is required for the lysosomal degradation of these glycosaminoglycans. Mutations in this gene that result in enzymatic deficiency lead to the autosomal recessive disease mucopolysaccharidosis type I (MPS I). [provided by RefSeq, Ju…
- **Diseases (Open Targets)**: Hurler syndrome (0.850); Scheie syndrome (0.848); Hurler-Scheie syndrome (0.848); mucopolysaccharidosis type 1 (0.814); mucopolysaccharidosis (0.702)
- **Europe PMC papers**: 2004
- **Why important**: IDUA connects to ANAPC16 and contributes a specific lysosomal and glycosaminoglycan-degradation function. Its enzyme removes terminal alpha-L-iduronic acid residues from dermatan sulfate and heparan sulfate, and deficiency causes mucopolysaccharidosis type one. It is broadly detected in brain and breast, is associated with vesicles, and has extensive disease literature centered on the mucopolysaccharidosis spectrum.
- **Conclusion**: Established: IDUA is a well-supported lysosomal glycosaminoglycan-catabolism gene and a plausible indicator of extracellular-matrix turnover or lysosomal maintenance. Hypothesis: its co-abundance with ANAPC16 may reflect coordinated proteostasis or matrix-processing state, but the module does not establish a direct relationship between them.

#### TIMM8A

- **Related proteins** (co-abundance neighbors): HAPLN2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translocase of inner mitochondrial membrane 8A. This translocase is involved in the import and insertion of hydrophobic membrane proteins from the cytoplasm into the mitochondrial inner membrane. The gene is mutated in Mohr-Tranebjaerg syndrome/Deafness Dystonia Syndrome (MTS/DDS) and it is postulated that MTS/DDS is a mitochondrial disease caused by a defective mitochondrial protein import system. Defects in this gene also cause Jensen syndrom…
- **Diseases (Open Targets)**: deafness dystonia syndrome (0.815); hearing loss disorder (0.372); eye disorder (0.370); hereditary disease (0.297); auditory neuropathy (0.269)
- **Europe PMC papers**: 625
- **Why important**: TIMM8A links HAPLN2 to a mitochondrial branch and is annotated for import and insertion of hydrophobic proteins into the mitochondrial inner membrane, protein localization to mitochondria, and nervous-system development. It is detected in both brain and breast and is cell-type enhanced in basal and progenitor-like populations. Its established disease associations include Mohr-Tranebjaerg syndrome, deafness-dystonia syndrome, Jensen syndrome, auditory neuropathy, and related hearing or eye disorders.
- **Conclusion**: Established: TIMM8A provides a mitochondrial-maintenance and neurodevelopmental interpretation for part of the module. Hypothesis: its connection to HAPLN2 may indicate coupling between extracellular neural-cell state and mitochondrial stress, but this remains speculative without physical-interaction or perturbation evidence.

#### NFKBIB

- **Related proteins** (co-abundance neighbors): ANAPC16 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NFKB inhibitor beta. The protein encoded by this gene belongs to the NF-kappa-B inhibitor family, which inhibit NF-kappa-B by complexing with, and trapping it in the cytoplasm. Phosphorylation of serine residues on these proteins by kinases marks them for destruction via the ubiquitination pathway, thereby allowing activation of the NF-kappa-B, which translocates to the nucleus to function as a transcription factor. A…
- **Diseases (Open Targets)**: dementia (0.371); dengue disease (0.370); gastrointestinal stromal tumor (0.074); Sepsis (0.058); ovarian carcinoma (0.026)
- **Europe PMC papers**: 966
- **Why important**: NFKBIB connects to ANAPC16 and contributes an inflammatory-signaling control point. Its protein inhibits NF-kappa-B by retaining NF-kappa-B complexes in the cytoplasm until phosphorylation-dependent destruction permits nuclear translocation. HPA describes it as testis-enhanced and enriched in early and late spermatid groups, while its disease associations include dementia, dengue disease, sepsis, and ovarian carcinoma. Its literature is substantial enough to support an established signaling role.
- **Conclusion**: Established: NFKBIB is a regulator of NF-kappa-B availability and may mark inflammatory or stress-responsive state. Hypothesis: its covariance with ANAPC16 could connect ubiquitin-dependent protein turnover to NF-kappa-B control, but the module's mixed tissue and cell-type pattern also permits a composition-driven explanation.

## Module 4

**Tissue pair**: brain and breast  
**Genes (7)**: COL4A2, ITGA7, LAMA4, LAMB2, NID1, PLIN4, SORBS1

### Function

The module is most strongly interpreted as a basement-membrane and extracellular-matrix adhesion module. Primary evidence is provided by (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.000725) through (KEGG PI3K-Akt signaling pathway - Homo sapiens (human); q_global = 0.0116), which consistently connect COL4A2, ITGA7, LAMA4, LAMB2 and NID1 with ECM–receptor interaction, basement membrane, extracellular-matrix structural function, integrin signaling, focal adhesion and PI3K–Akt signaling. The basement-membrane organization terms (GO:BP glomerular basement membrane development; q_global = 0.0359), (GO:BP regulation of basement membrane organization; q_global = 0.0359) and (GO:CC solid phase of basement membrane; q_global = 0.0489) reinforce this interpretation. The synaptic-cleft association (GO:CC synaptic cleft; q_global = 0.0489) is compatible with specialized basement-membrane and adhesion structures in neural tissue, but does not by itself establish a synaptic function. The infection and cancer pathway terms (KEGG Human papillomavirus infection - Homo sapiens (human); q_global = 0.0201), (KEGG Small cell lung cancer - Homo sapiens (human); q_global = 0.0356) and (KEGG Amoebiasis - Homo sapiens (human); q_global = 0.0399) are better regarded as pathway-context mappings driven by the same ECM genes, rather than evidence that the module specifically performs an infectious or cancer process. SORBS1 and PLIN4 contribute a cell–matrix, cytoskeletal and lipid-associated context, but neither has a globally significant GO/KEGG annotation in this module.

**Cell composition.** The module is dominated by extracellular-matrix and secreted-to-matrix proteins: LAMB2, COL4A2, NID1 and LAMA4 are annotated as secreted to the extracellular matrix, while the HPA profile identifies broad enrichment in stromal, muscle, vascular and adipocyte-related cell types. Most genes are not detected in immune cells, although NID1 has group-enriched blood-cell expression and SORBS1 is immune-cell enriched in basophils. This pattern argues against a primarily blood-cell module, while leaving open the possibility that shared vascular, stromal, smooth-muscle, muscle or adipocyte populations contribute to the brain–breast co-abundance signal. PLIN4 is especially suggestive of adipocyte or lipid-droplet biology and is detected in breast but not brain protein measurements. Conversely, several matrix genes are not detected by HPA immunohistochemistry in the assayed brain or breast samples, so the co-abundance relationship should not be interpreted as proof that every encoded protein is abundant in both tissues. The module therefore may reflect shared extracellular architecture or shared cell populations rather than a tissue-specific neuronal or mammary epithelial program.

**GO/KEGG enrichment**: 16 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG ECM-receptor interaction - Homo sapiens (human) | 0.000725 | COL4A2, ITGA7, LAMA4, LAMB2 |
| GO:CC basement membrane | 0.000982 | COL4A2, LAMA4, LAMB2, NID1 |
| GO:MF extracellular matrix structural constituent | 0.0037 | COL4A2, LAMA4, LAMB2, NID1 |
| KEGG Integrin signaling - Homo sapiens (human) | 0.00448 | COL4A2, ITGA7, LAMA4, LAMB2 |
| GO:CC external encapsulating structure | 0.00902 | COL4A2, LAMA4, LAMB2, NID1 |
| GO:CC extracellular matrix | 0.00902 | COL4A2, LAMA4, LAMB2, NID1 |
| KEGG Focal adhesion - Homo sapiens (human) | 0.00939 | COL4A2, ITGA7, LAMA4, LAMB2 |
| KEGG PI3K-Akt signaling pathway - Homo sapiens (human) | 0.0116 | COL4A2, ITGA7, LAMA4, LAMB2 |
| GO:CC protein complex involved in cell adhesion | 0.0159 | ITGA7, LAMB2, NID1 |
| KEGG Human papillomavirus infection - Homo sapiens (human) | 0.0201 | COL4A2, ITGA7, LAMA4, LAMB2 |
| KEGG Small cell lung cancer - Homo sapiens (human) | 0.0356 | COL4A2, LAMA4, LAMB2 |
| GO:BP glomerular basement membrane development | 0.0359 | LAMB2, NID1 |
| GO:BP regulation of basement membrane organization | 0.0359 | LAMB2, NID1 |
| KEGG Amoebiasis - Homo sapiens (human) | 0.0399 | COL4A2, LAMA4, LAMB2 |
| GO:CC synaptic cleft | 0.0489 | LAMA4, LAMB2 |

### STRING and hu.MAP

STRING provides coherent known relationships among the core matrix genes. The strongest connections include LAMA4 with LAMB2 and ITGA7, together with links among LAMA4, NID1, COL4A2 and LAMB2; the STRING enrichments (STRING RCTM Laminin interactions; within-query FDR = 1.66e-07) through (STRING Function Extracellular matrix structural constituent; within-query FDR = 0.0009) independently describe laminin interactions, basement membrane, collagen formation, ECM–receptor interaction, focal adhesion and extracellular-matrix structural function. These relationships indicate that much of the module recapitulates known molecular biology rather than being an arbitrary correlation cluster. ITGA7 supplies a receptor-side connection to laminin and adhesion signaling, whereas LAMA4, LAMB2, COL4A2 and NID1 supply extracellular scaffold components. hu.MAP contributes one complex, (hu.MAP huMAP3_14233.1), containing LAMA4 and NID1 together with additional laminin and nidogen-associated proteins. However, hu.MAP does not establish a complete physical complex containing all module members. SORBS1 and PLIN4 have no reported STRING partners in the supplied high-confidence network, and the absence of a hu.MAP assignment for most genes limits claims about a single experimentally defined multiprotein complex.

**STRING interactions (score >= 0.7)**: 8 of 21 gene pairs: COL4A2–ITGA7 (0.769); COL4A2–LAMA4 (0.798); COL4A2–NID1 (0.823); ITGA7–LAMA4 (0.894); ITGA7–LAMB2 (0.719); LAMA4–LAMB2 (0.93); LAMA4–NID1 (0.797); LAMB2–NID1 (0.734)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Laminin interactions (FDR = 1.66e-07, 5 genes); Keyword Basement membrane (FDR = 6.74e-06, 4 genes); NetworkNeighborAL Laminin IV, and G2 nidogen domain and fibulin (FDR = 7.54e-06, 4 genes); NetworkNeighborAL Collagen formation, and Protein complex involved in cell adhesion (FDR = 1.07e-05, 5 genes); KEGG ECM-receptor interaction (FDR = 7.54e-05, 4 genes); COMPARTMENTS Basement membrane (FDR = 0.00011, 4 genes); RCTM ECM proteoglycans (FDR = 0.00025, 4 genes); Component Basement membrane (FDR = 0.00036, 4 genes); COMPARTMENTS Laminin complex (FDR = 0.00048, 3 genes); KEGG PI3K-Akt signaling pathway (FDR = 0.00073, 4 genes); KEGG Focal adhesion (FDR = 0.00073, 4 genes); Function Extracellular matrix structural constituent (FDR = 0.0009, 4 genes); KEGG Human papillomavirus infection (FDR = 0.00094, 4 genes); KEGG Amoebiasis (FDR = 0.0017, 3 genes); KEGG Small cell lung cancer (FDR = 0.0017, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14233.1 (NID1, LAMA4; 2/14)

### Novelty

This is not best described as a newly discovered molecular pathway: the central laminin, nidogen, collagen and integrin relationships are already supported by STRING, the LAMA4–NID1 pair appears in hu.MAP (hu.MAP huMAP3_14233.1), and the annotations and disease literature are established. The potentially novel aspect is the conserved co-abundance configuration across brain and breast, particularly the association of the matrix core with SORBS1 and PLIN4 in this tissue pair. That cross-tissue module-level observation could be new, but novelty cannot be established from the fact sheet alone. Lack of STRING or hu.MAP support for SORBS1–PLIN4 or for the complete module is evidence of limited prior cataloguing, not proof that these relationships are biologically novel. Independent replication, control for cell composition, and perturbation or spatial evidence would be needed to distinguish a new coordinated program from shared stromal, vascular, muscle or adipocyte composition.

**Hypothesis.** Hypothesis: the module represents a conserved vascular or stromal basement-membrane program shared by brain and breast. In this model, LAMA4 and LAMB2 form laminin scaffold components that are organized with NID1 and COL4A2, while ITGA7 couples the matrix to cell-surface adhesion and integrin signaling. SORBS1 may connect adhesion receptors to cytoskeletal or insulin-responsive processes, and PLIN4 may mark a lipid-rich adipocyte or muscle-associated cellular context. The resulting co-abundance signal could reflect coordinated extracellular support, cell adhesion and mechanosensitive signaling in shared vascular, stromal, muscle or adipocyte populations. This is a hypothesis rather than an established mechanism; the fact sheet does not demonstrate direct physical assembly of all module proteins, causal signaling, or a specific brain or breast cell of origin.

### Important genes

#### LAMB2

- **Related proteins** (co-abundance neighbors): COL4A2 (0.83), PLIN4 (0.83), NID1 (0.82), SORBS1 (0.81); STRING partners: ITGA7 (0.719), LAMA4 (0.93), NID1 (0.734)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in brain, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit beta 2. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: LAMB2-related infantile-onset nephrotic syndrome (0.808); Pierson syndrome (0.797); nephrotic syndrome (0.496); eye disorder (0.434); synaptic congenital myasthenic syndrome (0.381)
- **Europe PMC papers**: 2504
- **Why important**: LAMB2 is the most connected module gene by the supplied network ranking and participates in every primary GO/KEGG association from (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.000725) through (GO:CC solid phase of basement membrane; q_global = 0.0489). It is a secreted extracellular-matrix laminin subunit, links to COL4A2, NID1, LAMA4 and ITGA7 in STRING, and has an extensive disease and literature record including Pierson syndrome and nephrotic disease associations. Its HPA protein signal is detected in both brain and breast, making it a strong bridge between the shared tissue context and the matrix interpretation.
- **Conclusion**: Established evidence supports LAMB2 as a central basement-membrane scaffold and adhesion-signaling component of the module. The hypothesis that it is the principal organizer of the cross-tissue co-abundance pattern remains unproven because network centrality and co-abundance do not establish causal hierarchy.

#### LAMA4

- **Related proteins** (co-abundance neighbors): ITGA7 (0.80); STRING partners: COL4A2 (0.798), ITGA7 (0.894), LAMB2 (0.93), NID1 (0.797)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_14233.1
- **Function (MyGene.info)**: laminin subunit alpha 4. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins are composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respecti…
- **Diseases (Open Targets)**: dilated cardiomyopathy 1JJ (0.517); eye disorder (0.434); familial isolated dilated cardiomyopathy (0.387); retinal disorder (0.370); bacterial infectious disease (0.370)
- **Europe PMC papers**: 2561
- **Why important**: LAMA4 is a core laminin component with extensive participation in the primary enrichment results and strong STRING links to ITGA7, LAMB2, NID1 and COL4A2. It is present in the hu.MAP complex with NID1 (hu.MAP huMAP3_14233.1), is secreted to the extracellular matrix, and has tissue and single-cell associations spanning vascular, muscle, adipocyte and glial-related populations. Its annotations include regulation of adhesion and migration, nervous-system development and signaling.
- **Conclusion**: Established evidence identifies LAMA4 as a central extracellular scaffold and plausible ligand-side partner for ITGA7. Its contribution to a shared brain–breast cell program is a reasonable hypothesis, but the HPA profile and lack of breast immunohistochemical detection caution against assigning it specifically to breast tissue without further validation.

#### ITGA7

- **Related proteins** (co-abundance neighbors): SORBS1 (0.83), LAMA4 (0.80); STRING partners: COL4A2 (0.769), LAMA4 (0.894), LAMB2 (0.719)
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Plasma membrane; IHC detected in brain, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha 7. The protein encoded by this gene belongs to the integrin alpha chain family. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain. They mediate a wide spectrum of cell-cell and cell-matrix interactions, and thus play a role in cell migration, morphologic development, differentiation, and metastasis. This protein functions as a receptor for the basement…
- **Diseases (Open Targets)**: congenital muscular dystrophy due to integrin alpha-7 deficiency (0.738); neurodegenerative disease (0.526); congenital muscular dystrophy due to LMNA mutation (0.421); congenital muscular dystrophy (0.417); congenital fiber-type disproportion myopathy (0.382)
- **Europe PMC papers**: 2126
- **Why important**: ITGA7 is the principal membrane receptor-side gene in the module. It contributes to the ECM–receptor, integrin, focal-adhesion and PI3K–Akt terms (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.000725), (KEGG Integrin signaling - Homo sapiens (human); q_global = 0.00448), (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.00939) and (KEGG PI3K-Akt signaling pathway - Homo sapiens (human); q_global = 0.0116), connects strongly to LAMA4 in STRING, and is also linked to COL4A2 and LAMB2. Its established biology includes laminin binding, cell–matrix adhesion, migration and muscle development, with HPA enrichment in cardiac and skeletal muscle and disease associations involving congenital muscular dystrophy.
- **Conclusion**: Established evidence supports ITGA7 as the likely interface through which basement-membrane composition can influence cell adhesion and signaling. It may help explain coordination with muscle, vascular or stromal populations, but the module does not establish that ITGA7-mediated signaling causes the observed cross-tissue abundance pattern.

#### COL4A2

- **Related proteins** (co-abundance neighbors): LAMB2 (0.83); STRING partners: ITGA7 (0.769), LAMA4 (0.798), NID1 (0.823)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type IV alpha 2 chain. This gene encodes one of the six subunits of type IV collagen, the major structural component of basement membranes. The C-terminal portion of the protein, known as canstatin, is an inhibitor of angiogenesis and tumor growth. Like the other members of the type IV collagen gene family, this gene is organized in a head-to-head conformation with another type IV collagen gene so that each gene pair sh…
- **Diseases (Open Targets)**: brain small vessel disease 2A, autosomal dominant (0.728); porencephaly (0.612); Dupuytren Contracture (0.587); coronary artery disorder (0.548); hemorrhage, intracerebral, susceptibility to (0.541)
- **Europe PMC papers**: 5290
- **Why important**: COL4A2 is a type IV collagen chain and a primary contributor to the basement-membrane, ECM structural and ECM–receptor terms, including (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.000725), (GO:CC basement membrane; q_global = 0.000982), (GO:MF extracellular matrix structural constituent; q_global = 0.0037), (KEGG Integrin signaling - Homo sapiens (human); q_global = 0.00448), (GO:CC extracellular matrix; q_global = 0.00902) and (GO:CC solid phase of basement membrane; q_global = 0.0489). It connects in STRING to LAMB2, LAMA4, NID1 and ITGA7 and has a substantial disease literature involving brain small-vessel disease, porencephaly and intracerebral hemorrhage susceptibility. Its encoded matrix product and canstatin-related biology make it relevant to both structural integrity and vascular signaling.
- **Conclusion**: Established evidence supports COL4A2 as a structural basement-membrane component with particular relevance to vascular and brain integrity. Its lack of HPA immunohistochemical detection in the assayed brain and breast samples means that its module membership may reflect transcript or cell-composition relationships rather than abundant detectable protein in those samples.

#### NID1

- **Related proteins** (co-abundance neighbors): LAMB2 (0.82); STRING partners: COL4A2 (0.823), LAMA4 (0.797), LAMB2 (0.734)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14233.1
- **Function (MyGene.info)**: nidogen 1. This gene encodes a member of the nidogen family of basement membrane glycoproteins. The protein interacts with several other components of basement membranes, and may play a role in cell interactions with the extracellular matrix. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.425); focal epilepsy (0.259); Hemiparesis (0.259); Hydrocephalus (0.259); placental retention (0.233)
- **Europe PMC papers**: 1838
- **Why important**: NID1 is a basement-membrane linker glycoprotein contributing to (GO:CC basement membrane; q_global = 0.000982), (GO:MF extracellular matrix structural constituent; q_global = 0.0037), (GO:CC external encapsulating structure; q_global = 0.00902), (GO:CC extracellular matrix; q_global = 0.00902), (GO:CC protein complex involved in cell adhesion; q_global = 0.0159), (GO:BP glomerular basement membrane development; q_global = 0.0359) and (GO:BP regulation of basement membrane organization; q_global = 0.0359). It links to LAMB2, LAMA4 and COL4A2 in STRING and forms the LAMA4–NID1 hu.MAP association (hu.MAP huMAP3_14233.1). Its cell-type profile includes fibro-adipogenic progenitors, fibroblasts and cardiomyocytes, while its disease associations include neurodegenerative disease, focal epilepsy, hydrocephalus and placental retention.
- **Conclusion**: Established evidence supports NID1 as a connector that helps organize basement-membrane components and cell–matrix adhesion. Its blood-cell group enrichment and lack of detected protein in the assayed brain and breast samples raise an alternative composition-related explanation that should be tested before interpreting it as a tissue-intrinsic driver.

#### SORBS1

- **Related proteins** (co-abundance neighbors): ITGA7 (0.83), PLIN4 (0.81), LAMB2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Focal adhesion sites; IHC detected in brain, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sorbin and SH3 domain containing 1. This gene encodes a CBL-associated protein which functions in the signaling and stimulation of insulin. Mutations in this gene may be associated with human disorders of insulin resistance. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.454); atrial fibrillation (0.394); urinary system disorder (0.381); uterine corpus leiomyoma (0.351); hypertensive disorder (0.345)
- **Europe PMC papers**: 1367
- **Why important**: SORBS1 is not a primary enrichment driver, but it is structurally informative because it connects within the module to ITGA7, PLIN4 and LAMB2 and is localized to focal-adhesion sites. Its annotations include cytoskeleton organization, cell–matrix adhesion, insulin-receptor signaling, cell-substrate adhesion and stress-fiber assembly. HPA associates it with blood vessels and with adipocyte, astrocyte, glial, cardiomyocyte and ependymal cell types, while disease evidence includes insulin-resistance-related biology and several cardiometabolic or neurological associations.
- **Conclusion**: Established evidence supports SORBS1 as a plausible intracellular adhesion and signaling adaptor that could connect the extracellular matrix core to cytoskeletal or insulin-responsive states. Its role as a mechanistic bridge in this module is a hypothesis because it lacks supplied STRING or hu.MAP support and has no globally significant GO/KEGG term in the module.
