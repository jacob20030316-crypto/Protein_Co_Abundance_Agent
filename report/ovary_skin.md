# Conserved co-abundance modules: ovary and skin

## Module 0

**Tissue pair**: ovary and skin  
**Genes (5)**: ADAM10, GOLIM4, MAN2A1, MAIP1, PLXNB2

### Function

The most defensible interpretation is a membrane and Golgi-centered co-abundance program involving protein trafficking, glycoprotein maturation, cell-surface receptor processing, and cell-adhesion signaling. GOLIM4 and MAN2A1 provide a coherent Golgi and N-glycan-processing axis, while ADAM10 and PLXNB2 connect that axis to membrane proteolysis, receptor biology, migration, and adhesion. MAIP1 introduces a mitochondrial protein-insertion and calcium-homeostasis component, so the module may also reflect coordinated cellular remodeling rather than a single biochemical pathway. No GO/KEGG term passed global correction; therefore the functional interpretation is based on the individual gene annotations, network topology, and complex evidence rather than statistically enriched pathway labels.

**Cell composition.** The module is not predominantly composed of secreted or broadly tissue-specific proteins. All genes have low tissue specificity in HPA, and the cell-type annotations are heterogeneous, including oocytes, neutrophils, monocytes and dendritic cells, Müller glia, podocytes, oligodendrocytes, and several epithelial cell types. This argues against a clean ovary-specific or skin-specific program and raises the possibility that the shared signal reflects common cellular states, mixed cell composition, or conserved membrane and organelle biology. Blood-related annotations are present for several genes, but the module is not uniformly immune-cell specific. Protein detection is reported for part of the module in both ovary and skin, whereas other components are not detected in those tissues, so the co-abundance pattern should not automatically be interpreted as coordinated expression in the same resident cell population.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no supplementary STRING functional enrichment. This means that the co-abundance edges are not supported by established STRING physical or functional links. In contrast, ADAM10, PLXNB2, and MAN2A1 co-occur in both hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). These complexes provide partial support for a shared membrane, Golgi, trafficking, or glycan-related protein environment, but they do not establish that the entire module is a single physical complex. GOLIM4 and MAIP1 are absent from the listed hu.MAP complexes, making the complete module more plausibly a coordinated abundance pattern than a known multiprotein assembly.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (ADAM10, PLXNB2, MAN2A1; 3/60); huMAP3_09327.1 (ADAM10, PLXNB2, MAN2A1; 3/93)

### Novelty

The co-abundance observation may be novel, because the complete gene set has no high-confidence STRING interaction support, no STRING enrichment, no globally significant GO/KEGG term, and only partial overlap with hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). However, absence from STRING or hu.MAP alone does not prove biological novelty. The genes and several of their functions are already established, especially ADAM10-mediated ectodomain proteolysis, PLXNB2-mediated semaphorin-related signaling and migration, GOLIM4 Golgi biology, and MAN2A1 N-glycan maturation. The appropriate claim is therefore a potentially novel cross-tissue co-abundance relationship, not a newly discovered molecular pathway. Replication in independent ovary and skin datasets, together with cell-composition adjustment and perturbation experiments, would be required to support a new module mechanism.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular remodeling state in which Golgi cargo handling and N-glycan maturation are coordinated with plasma-membrane receptor turnover and adhesion signaling, while mitochondrial protein insertion and calcium handling provide an organelle-level response. GOLIM4 may organize the Golgi-associated component, MAN2A1 may influence glycoprotein maturation, and ADAM10 together with PLXNB2 may translate altered membrane composition into changes in adhesion, migration, or receptor signaling. The heterogeneous HPA cell-type annotations suggest that this may be a shared state across different cell populations rather than a lineage-specific ovary-skin program. This remains a hypothesis because the module lacks globally significant enrichment and lacks STRING-supported pairwise interactions.

### Important genes

#### GOLIM4

- **Related proteins** (co-abundance neighbors): ADAM10 (0.84), MAIP1 (0.82), MAN2A1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in ovary, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: golgi integral membrane protein 4. The Golgi complex plays a key role in the sorting and modification of proteins exported from the endoplasmic reticulum. The protein encoded by this gene is a type II Golgi-resident protein. It may process proteins synthesized in the rough endoplasmic reticulum and assist in the transport of protein cargo through the Golgi apparatus. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.397); mathematical ability (0.328); head injury (0.300); cholelithiasis (0.299); proliferative diabetic retinopathy (0.284)
- **Europe PMC papers**: 294
- **Why important**: GOLIM4 is the central network connector, linking the other Golgi-associated and membrane-related components in the co-abundance graph. Its established role as a type II Golgi-resident protein involved in sorting and modification of secretory-pathway cargo makes it the strongest candidate for organizing the module's trafficking interpretation. It is detected in ovary and skin, has low tissue specificity, has no listed STRING or hu.MAP support, and has a substantial literature base relative to the other less studied candidates.
- **Conclusion**: Established evidence supports GOLIM4 as a Golgi cargo-handling protein and as the network center of this module. It is reasonable to hypothesize that GOLIM4 contributes to the shared co-abundance signal, but the data do not establish that it directly regulates ADAM10, PLXNB2, MAN2A1, or MAIP1.

#### ADAM10

- **Related proteins** (co-abundance neighbors): GOLIM4 (0.84), PLXNB2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: ADAM metallopeptidase domain 10. Members of the ADAM family are cell surface proteins with a unique structure possessing both potential adhesion and protease domains. This gene encodes and ADAM family member that cleaves many proteins including TNF-alpha and E-cadherin. Alternate splicing results in multiple transcript variants encoding different proteins that may undergo similar processing. [provided by RefSeq, Feb 2016].
- **Diseases (Open Targets)**: reticulate acropigmentation of Kitamura (0.679); Alzheimer disease 18 (0.621); Alzheimer disease (0.522); dementia (0.415); schizophrenia (0.354)
- **Europe PMC papers**: 11139
- **Why important**: ADAM10 is a membrane-associated protease and adhesion-related sheddase with extensive literature and disease annotation. Its known cleavage of TNF-alpha and E-cadherin, together with roles in ectodomain proteolysis, cell adhesion, and Notch signaling, gives the module a plausible signaling and remodeling effector. It connects GOLIM4 and PLXNB2 in the network and is present in both hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1).
- **Conclusion**: Established evidence supports ADAM10 as a regulator of cell-surface protein processing and adhesion-related signaling, with hu.MAP support for its shared complex context with PLXNB2 and MAN2A1. The hypothesis that ADAM10 is the functional membrane effector of this co-abundance module is plausible but is not demonstrated by the absence of STRING interactions.

#### PLXNB2

- **Related proteins** (co-abundance neighbors): ADAM10 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location None; IHC detected in ovary, skin
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: plexin B2. Members of the B class of plexins, such as PLXNB2 are transmembrane receptors that participate in axon guidance and cell migration in response to semaphorins (Perrot et al. (2002) [PubMed 12183458]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Intellectual disability (0.519); amelogenesis imperfecta (0.518); sensorineural hearing loss disorder (0.516); cutaneous melanoma (0.486); neurodegenerative disease (0.455)
- **Europe PMC papers**: 2109
- **Why important**: PLXNB2 is a transmembrane plexin receptor involved in semaphorin-responsive axon guidance, cell migration, receptor-mediated endocytosis, and cell-cell adhesion. It forms the membrane-signaling counterpart to the Golgi and glycan-processing genes, is detected in both ovary and skin, and appears in both hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Its cell-type annotations spanning epithelial and myeloid populations also make it relevant to the possibility of shared cellular-state or composition effects.
- **Conclusion**: Established evidence supports PLXNB2 as a receptor involved in migration, adhesion, and endocytic signaling, and hu.MAP supports its complex context with ADAM10 and MAN2A1. Its placement beside ADAM10 suggests a possible membrane-remodeling arm of the module, but the co-abundance data do not prove receptor activation or direct functional coupling.

#### MAN2A1

- **Related proteins** (co-abundance neighbors): GOLIM4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: mannosidase alpha class 2A member 1. This gene encodes a glycosyl hydrolase that localizes to the Golgi and catalyzes the final hydrolytic step in the asparagine-linked oligosaccharide (N-glycan) maturation pathway. Mutations in the mouse homolog of this gene have been shown to cause a systemic autoimmune disease similar to human systemic lupus erythematosus. [provided by RefSeq, Dec 2013].
- **Diseases (Open Targets)**: alcohol drinking (0.456); schizophrenia (0.455); COVID-19 (0.370); smoking initiation (0.364); dislocation (0.344)
- **Europe PMC papers**: 663
- **Why important**: MAN2A1 is a Golgi glycosidase that catalyzes a late step in N-glycan maturation, providing a direct biochemical link to GOLIM4 and to the processing of membrane and secretory-pathway proteins. It is present with ADAM10 and PLXNB2 in hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Its established roles in carbohydrate metabolism and glycoprotein processing make it important for testing whether altered glycosylation helps explain the shared ovary-skin pattern.
- **Conclusion**: Established evidence supports MAN2A1 as a Golgi N-glycan-processing enzyme, and hu.MAP supports its occurrence in complexes containing ADAM10 and PLXNB2. A role for MAN2A1 in modifying the trafficking, stability, or surface processing of module-associated proteins is a mechanistic hypothesis, not a demonstrated consequence of this co-abundance result.

#### MAIP1

- **Related proteins** (co-abundance neighbors): GOLIM4 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: matrix AAA peptidase interacting protein 1. Predicted to enable ribosome binding activity. Involved in calcium import into the mitochondrion; mitochondrial calcium ion homeostasis; and protein insertion into mitochondrial membrane. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: schizophrenia (0.251); Abnormality of the skeletal system (0.197); autism spectrum disorder (0.171); metabolic disease (0.162); bipolar disorder (0.157)
- **Europe PMC papers**: 75
- **Why important**: MAIP1 is the least connected and least studied component of the module, but it is biologically informative because its annotation places it in the mitochondrial matrix with roles in mitochondrial protein insertion and calcium import. Its HPA annotation is enhanced in oocytes, and its absence from STRING and hu.MAP distinguishes it from the Golgi and membrane components. It may therefore identify a mitochondrial state linked to cellular remodeling or may represent a context-dependent association requiring validation.
- **Conclusion**: Established evidence supports MAIP1 as a mitochondrial protein associated with protein insertion and calcium homeostasis, but the module provides no independent interaction evidence for it. Its inclusion in the module may indicate coordination between mitochondrial and membrane-trafficking states, although it could also reflect cell-type composition or a dataset-specific co-abundance relationship.

## Module 1

**Tissue pair**: ovary and skin  
**Genes (8)**: AIFM1, ATP5F1A, ATP5F1B, IMMT, NDUFA10, UQCRC1, UQCRC2, TOP2B

### Function

This is a mitochondrial oxidative-phosphorylation and respiratory-chain module. The primary evidence is the strong, globally corrected enrichment for mitochondrial inner membrane and organelle inner membrane components (GO:CC mitochondrial inner membrane; q_global = 2.64e-05), (GO:CC organelle inner membrane; q_global = 4.19e-05), (GO:CC mitochondrial membrane; q_global = 0.000286), and (GO:CC mitochondrial envelope; q_global = 0.000541), respiratory-chain complexes (GO:CC respiratory chain complex; q_global = 5.94e-05), oxidative phosphorylation (KEGG Oxidative phosphorylation - Homo sapiens (human); q_global = 0.000113), (GO:BP oxidative phosphorylation; q_global = 0.000234), and aerobic respiration (GO:BP aerobic respiration; q_global = 0.00501), (GO:BP cellular respiration; q_global = 0.00855). The module also supports proton transmembrane transport and proton-motive-force-driven ATP synthesis (GO:MF proton transmembrane transporter activity; q_global = 0.00496), (GO:BP proton transmembrane transport; q_global = 0.00593), (GO:BP proton motive force-driven mitochondrial ATP synthesis; q_global = 0.0304), (GO:BP proton motive force-driven ATP synthesis; q_global = 0.0384), together with ATP biosynthesis (GO:BP ATP biosynthetic process; q_global = 0.0474). The disease-labelled KEGG terms (KEGG Diabetic cardiomyopathy - Homo sapiens (human); q_global = 0.000468), (KEGG Chemical carcinogenesis - reactive oxygen species - Homo sapiens (human); q_global = 0.000511), and (KEGG Prion disease - Homo sapiens (human); q_global = 0.00139) through (KEGG Alzheimer disease - Homo sapiens (human); q_global = 0.00419), (KEGG Pathways of neurodegeneration - multiple diseases - Homo sapiens (human); q_global = 0.00822), and (KEGG Amyotrophic lateral sclerosis - Homo sapiens (human); q_global = 0.00855) are best interpreted as pathway annotations reflecting mitochondrial dysfunction and oxidative stress, not as evidence that the module specifically causes those diseases. The module is therefore coherent with mitochondrial electron transfer, maintenance of the inner membrane, and energy production.

**Cell composition.** The module is not composed of plasma or secreted proteins: every gene has no secretome annotation, and all genes have low immune-cell specificity in HPA. It is therefore unlikely to represent a blood-cell or circulating-protein contaminant. Most genes have tissue-enhanced or cell-type-enhanced HPA patterns, particularly in tongue, skeletal muscle, heart muscle, parietal cells, esophageal basal and suprabasal cells, oocytes, and trophoblast populations. This indicates that the shared ovary–skin signal may reflect mitochondrial abundance or activity in metabolically active epithelial, reproductive, or other shared cell populations rather than a tissue-exclusive program. HPA protein detection is broad across the two tissues, although IMMT and AIFM1 have weaker or absent detection in one or both tissues. The tissue and cell-type patterns should therefore be treated as context for the module, not as evidence of a secreted or immune-derived signal.

**GO/KEGG enrichment**: 33 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrial inner membrane | 2.64e-05 | AIFM1, ATP5F1A, ATP5F1B, IMMT, NDUFA10, UQCRC1, UQCRC2 |
| GO:CC organelle inner membrane | 4.19e-05 | AIFM1, ATP5F1A, ATP5F1B, IMMT, NDUFA10, UQCRC1, UQCRC2 |
| GO:CC respiratory chain complex | 5.94e-05 | ATP5F1A, ATP5F1B, NDUFA10, UQCRC1, UQCRC2 |
| KEGG Oxidative phosphorylation - Homo sapiens (human) | 0.000113 | ATP5F1A, ATP5F1B, NDUFA10, UQCRC1, UQCRC2 |
| GO:BP oxidative phosphorylation | 0.000234 | ATP5F1A, ATP5F1B, NDUFA10, UQCRC1, UQCRC2 |
| GO:CC mitochondrial membrane | 0.000286 | AIFM1, ATP5F1A, ATP5F1B, IMMT, NDUFA10, UQCRC1, UQCRC2 |
| KEGG Diabetic cardiomyopathy - Homo sapiens (human) | 0.000468 | ATP5F1A, ATP5F1B, NDUFA10, UQCRC1, UQCRC2 |
| KEGG Chemical carcinogenesis - reactive oxygen species - Homo sapiens (human) | 0.000511 | ATP5F1A, ATP5F1B, NDUFA10, UQCRC1, UQCRC2 |
| GO:CC mitochondrial envelope | 0.000541 | AIFM1, ATP5F1A, ATP5F1B, IMMT, NDUFA10, UQCRC1, UQCRC2 |
| GO:CC transmembrane transporter complex | 0.000589 | ATP5F1A, ATP5F1B, NDUFA10, UQCRC1, UQCRC2 |
| GO:CC transporter complex | 0.000742 | ATP5F1A, ATP5F1B, NDUFA10, UQCRC1, UQCRC2 |
| KEGG Thermogenesis - Homo sapiens (human) | 0.000957 | ATP5F1A, ATP5F1B, NDUFA10, UQCRC1, UQCRC2 |
| KEGG Prion disease - Homo sapiens (human) | 0.00139 | ATP5F1A, ATP5F1B, NDUFA10, UQCRC1, UQCRC2 |
| KEGG Parkinson disease - Homo sapiens (human) | 0.00148 | ATP5F1A, ATP5F1B, NDUFA10, UQCRC1, UQCRC2 |
| KEGG Huntington disease - Homo sapiens (human) | 0.00366 | ATP5F1A, ATP5F1B, NDUFA10, UQCRC1, UQCRC2 |

### STRING and hu.MAP

STRING provides extensive prior support for the mitochondrial interpretation. The strongest known relationships include the ATP5F1A–ATP5F1B ATP-synthase pair, the UQCRC1–UQCRC2 complex-III core pair, and links among the ATP-synthase, complex-I, complex-III, and inner-membrane structural proteins. These interactions are summarized by the supplementary STRING enrichments for the inner mitochondrial membrane and respiratory electron transport (STRING Component Inner mitochondrial membrane protein complex; within-query FDR = 8.06e-07) through (STRING RCTM Respiratory electron transport, ATP synthesis by chemiosmotic coupling, and heat production by uncoupling proteins.; within-query FDR = 5.03e-05). The STRING disease-pathway enrichments (STRING KEGG Parkinson disease; within-query FDR = 5.04e-05) through (STRING KEGG Huntington disease; within-query FDR = 9.48e-05) mainly reflect reuse of respiratory-chain genes in neurodegeneration pathways. hu.MAP independently places UQCRC1 and UQCRC2 in multiple complex-III or respiratory-chain assemblies (hu.MAP huMAP3_08546.1), (hu.MAP huMAP3_09600.1), (hu.MAP huMAP3_12621.1) through (hu.MAP huMAP3_12457.1), places ATP5F1A and ATP5F1B in ATP-synthase assemblies (hu.MAP huMAP3_08750.1), (hu.MAP huMAP3_09307.1), and (hu.MAP huMAP3_11095.1), and places NDUFA10 with UQCRC1 in complex-I-related assemblies (hu.MAP huMAP3_14018.1) and (hu.MAP huMAP3_09982.1). Thus, many relationships are already established physical or complex-level associations. The co-abundance module is biologically concordant with these complexes, but its edges should not automatically be interpreted as direct physical binding, especially for AIFM1 and TOP2B.

**STRING interactions (score >= 0.7)**: 13 of 28 gene pairs: ATP5F1A–ATP5F1B (0.999); ATP5F1A–IMMT (0.809); ATP5F1A–NDUFA10 (0.759); ATP5F1A–UQCRC1 (0.97); ATP5F1A–UQCRC2 (0.986); ATP5F1B–IMMT (0.745); ATP5F1B–NDUFA10 (0.938); ATP5F1B–UQCRC1 (0.969); ATP5F1B–UQCRC2 (0.942); IMMT–UQCRC2 (0.811); NDUFA10–UQCRC1 (0.996); NDUFA10–UQCRC2 (0.986); UQCRC1–UQCRC2 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Inner mitochondrial membrane protein complex (FDR = 8.06e-07, 6 genes); COMPARTMENTS Mitochondrial inner membrane (FDR = 8.97e-07, 7 genes); COMPARTMENTS Inner mitochondrial membrane protein complex (FDR = 8.97e-07, 6 genes); Component Mitochondrial inner membrane (FDR = 1.67e-06, 7 genes); WikiPathways Electron transport chain: OXPHOS system in mitochondria (FDR = 6.55e-06, 5 genes); KEGG Oxidative phosphorylation (FDR = 8.94e-06, 5 genes); Keyword Mitochondrion inner membrane (FDR = 1.31e-05, 6 genes); NetworkNeighborAL Respiratory electron transport, ATP synthesis by chemiosmotic coupling, and heat production by uncoupling proteins. (FDR = 2.4e-05, 5 genes); Keyword Transit peptide (FDR = 2.82e-05, 7 genes); KEGG Thermogenesis (FDR = 4.82e-05, 5 genes); RCTM Respiratory electron transport, ATP synthesis by chemiosmotic coupling, and heat production by uncoupling proteins. (FDR = 5.03e-05, 5 genes); KEGG Parkinson disease (FDR = 5.04e-05, 5 genes); KEGG Prion disease (FDR = 5.04e-05, 5 genes); KEGG Alzheimer disease (FDR = 9.48e-05, 5 genes); KEGG Huntington disease (FDR = 9.48e-05, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07245.1 (UQCRC2, ATP5F1A; 2/4); huMAP3_08546.1 (UQCRC2, UQCRC1; 2/9); huMAP3_09600.1 (UQCRC2, UQCRC1; 2/9); huMAP3_08750.1 (ATP5F1B, ATP5F1A; 2/12); huMAP3_12621.1 (UQCRC2, UQCRC1; 2/22); huMAP3_10623.1 (UQCRC2, UQCRC1; 2/24); huMAP3_12457.1 (UQCRC2, UQCRC1; 2/31); huMAP3_09307.1 (ATP5F1B, ATP5F1A; 2/35); huMAP3_11095.1 (ATP5F1B, ATP5F1A; 2/45); huMAP3_14018.1 (NDUFA10, UQCRC1; 2/48); huMAP3_09982.1 (NDUFA10, UQCRC1; 2/49)

### Novelty

The biological function itself is not a new discovery: the component genes are established mitochondrial respiratory-chain, ATP-synthase, inner-membrane, or apoptosis-associated proteins, and much of their connectivity is already represented in STRING and hu.MAP. The potentially novel observation is the conserved co-abundance pattern across ovary and skin, particularly the coordinated inclusion of genes from complex I, complex III, ATP synthase, inner-membrane architecture, and mitochondrial apoptosis. However, the fact sheet does not compare this module with published tissue co-abundance modules or prior ovary–skin analyses, so a claim that the module is entirely new is not justified. Absence of a particular relationship from STRING or hu.MAP would not establish novelty. The most defensible conclusion is that this is a potentially useful tissue-pair co-abundance observation built around a well-established mitochondrial program.

**Hypothesis.** Hypothesis: the conserved ovary–skin module reflects coordinated regulation of mitochondrial respiratory capacity and inner-membrane organization in shared metabolically active cell populations. Coupling of complex-I and complex-III components with ATP synthase may support proton-gradient formation and ATP production, while IMMT may link the signal to cristae organization and AIFM1 may connect respiratory state to apoptosis-related stress responses. TOP2B may represent a tissue-context or indirect co-abundance connection rather than a core mitochondrial component. This hypothesis predicts that module abundance will track mitochondrial content, respiratory activity, cristae integrity, and cellular stress across matched ovary and skin samples; it does not establish direct regulation or causality.

### Important genes

#### UQCRC2

- **Related proteins** (co-abundance neighbors): UQCRC1 (0.90), IMMT (0.82), AIFM1 (0.80); STRING partners: ATP5F1A (0.986), ATP5F1B (0.942), IMMT (0.811), NDUFA10 (0.986), UQCRC1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary, skin
- **hu.MAP 3.0**: huMAP3_07245.1, huMAP3_08546.1, huMAP3_09600.1, huMAP3_12621.1, huMAP3_10623.1, huMAP3_12457.1
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase core protein 2. The protein encoded by this gene is located in the mitochondrion, where it is part of the ubiquinol-cytochrome c reductase complex (also known as complex III). This complex constitutes a part of the mitochondrial respiratory chain. Defects in this gene are a cause of mitochondrial complex III deficiency nuclear type 5. [provided by RefSeq, Jul 2015].
- **Diseases (Open Targets)**: mitochondrial complex III deficiency (0.732); neurodegenerative disease (0.423); mitochondrial disease (0.312); gastric cancer (0.085); adrenoleukodystrophy (0.075)
- **Europe PMC papers**: 3297
- **Why important**: UQCRC2 has a central position in the co-abundance subgraph and connects to UQCRC1, IMMT, and AIFM1. It is the core protein of mitochondrial complex III, participates in ubiquinol-to-cytochrome-c electron transfer, and is included across the major mitochondrial inner-membrane, respiratory-chain, and oxidative-phosphorylation terms (GO:CC mitochondrial inner membrane; q_global = 2.64e-05) through (GO:CC membrane protein complex; q_global = 0.0151), (GO:BP generation of precursor metabolites and energy; q_global = 0.0256), and (GO:BP aerobic electron transport chain; q_global = 0.0474). Its STRING relationships and repeated hu.MAP placement with UQCRC1 support established complex-III biology (hu.MAP huMAP3_08546.1), (hu.MAP huMAP3_09600.1), (hu.MAP huMAP3_12621.1) through (hu.MAP huMAP3_12457.1). Its disease associations include mitochondrial complex-III deficiency and mitochondrial disease, and it has substantial literature support.
- **Conclusion**: Established evidence identifies UQCRC2 as a core complex-III component and a strong structural and functional anchor of this module. The module data support its importance for respiratory-chain coordination, but do not show that UQCRC2 drives the shared ovary–skin pattern.

#### ATP5F1A

- **Related proteins** (co-abundance neighbors): ATP5F1B (0.92), AIFM1 (0.80); STRING partners: ATP5F1B (0.999), IMMT (0.809), NDUFA10 (0.759), UQCRC1 (0.97), UQCRC2 (0.986)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary, skin
- **hu.MAP 3.0**: huMAP3_07245.1, huMAP3_08750.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit alpha. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, using an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic po…
- **Diseases (Open Targets)**: mitochondrial complex V (ATP synthase) deficiency, nuclear type 4A (0.655); mitochondrial proton-transporting ATP synthase complex deficiency (0.648); mitochondrial complex V (ATP synthase) deficiency, nuclear type 4B (0.532); hereditary disease (0.394); Mitochondrial encephalopathy (0.371)
- **Europe PMC papers**: 822
- **Why important**: ATP5F1A is the catalytic alpha subunit of mitochondrial ATP synthase and is linked in the module to ATP5F1B and AIFM1. It contributes to the globally corrected enrichment for oxidative phosphorylation, proton transport, proton-motive-force-driven ATP synthesis, and ATP biosynthesis (GO:CC mitochondrial inner membrane; q_global = 2.64e-05) through (GO:BP oxidative phosphorylation; q_global = 0.000234), (GO:MF proton transmembrane transporter activity; q_global = 0.00496) through (GO:BP proton transmembrane transport; q_global = 0.00593), and (GO:BP proton motive force-driven mitochondrial ATP synthesis; q_global = 0.0304) through (GO:BP ATP biosynthetic process; q_global = 0.0474). Its near-complete STRING connectivity with the other core mitochondrial proteins and its placement in ATP-synthase complexes (hu.MAP huMAP3_07245.1), (hu.MAP huMAP3_08750.1), (hu.MAP huMAP3_09307.1), and (hu.MAP huMAP3_11095.1) make it a key bridge between the respiratory gradient and ATP production. It is associated with mitochondrial complex-V deficiency and mitochondrial encephalopathy.
- **Conclusion**: Established evidence supports ATP5F1A as a central ATP-production component and a functional bridge within the module. Its coordinated abundance may report energy-demand or mitochondrial-content differences between samples, but the data do not establish a tissue-specific ATP-synthase mechanism.

#### NDUFA10

- **Related proteins** (co-abundance neighbors): IMMT (0.83), TOP2B (0.82); STRING partners: ATP5F1A (0.759), ATP5F1B (0.938), UQCRC1 (0.996), UQCRC2 (0.986)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary, skin
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_09982.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit A10. The protein encoded by this gene is a component of 42 kDa complex I, the first enzyme complex in the electron transport chain of mitochondria. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. A mutation in this gene was found in an individual with Leigh syndrome. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.677); Leigh syndrome (0.674); mitochondrial complex I deficiency, nuclear type 22 (0.668); type 2 diabetes mellitus (0.620); diabetes mellitus (0.578)
- **Europe PMC papers**: 1163
- **Why important**: NDUFA10 is a complex-I component involved in NADH-to-ubiquinone electron transfer and proton-gradient generation. It appears in nearly all of the primary respiratory-chain and oxidative-phosphorylation terms (GO:CC mitochondrial inner membrane; q_global = 2.64e-05) through (GO:CC membrane protein complex; q_global = 0.0151), (GO:MF monoatomic cation transmembrane transporter activity; q_global = 0.0191) through (GO:BP aerobic electron transport chain; q_global = 0.0474), has strong STRING links to the ATP-synthase and complex-III genes, and is placed with complex-I-related assemblies in hu.MAP (hu.MAP huMAP3_14018.1) and (hu.MAP huMAP3_09982.1). Its disease associations include complex-I deficiency, Leigh syndrome, and diabetes-related annotations, and it has substantial literature support.
- **Conclusion**: Established evidence makes NDUFA10 a representative complex-I component that connects upstream electron entry with the broader respiratory module. A plausible interpretation is that its co-abundance marks coordinated electron-transport capacity, but the module cannot determine whether NDUFA10 is mechanistically limiting.

#### IMMT

- **Related proteins** (co-abundance neighbors): NDUFA10 (0.83), UQCRC2 (0.82); STRING partners: ATP5F1A (0.809), ATP5F1B (0.745), UQCRC2 (0.811)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inner membrane mitochondrial protein. Enables RNA binding activity. Involved in cristae formation. Located in mitochondrial inner membrane. Part of MICOS complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); multinodular goiter (0.196); alcohol drinking (0.190); breast cancer (0.094); neoplasm (0.087)
- **Europe PMC papers**: 933
- **Why important**: IMMT is an inner-membrane protein involved in cristae formation and the MICOS complex. It connects in the module to NDUFA10 and UQCRC2 and contributes to the globally corrected inner-membrane and organelle-envelope terms (GO:CC mitochondrial inner membrane; q_global = 2.64e-05), (GO:CC organelle inner membrane; q_global = 4.19e-05), (GO:CC mitochondrial membrane; q_global = 0.000286), (GO:CC mitochondrial envelope; q_global = 0.000541), (GO:CC organelle envelope; q_global = 0.00811), and (GO:CC membrane protein complex; q_global = 0.0151). STRING supports its association with the inner-membrane mitochondrial protein complex (STRING Component Inner mitochondrial membrane protein complex; within-query FDR = 8.06e-07) through (STRING Component Mitochondrial inner membrane; within-query FDR = 1.67e-06) and (STRING Keyword Mitochondrion inner membrane; within-query FDR = 1.31e-05), whereas the lack of a listed hu.MAP complex makes its module placement complementary rather than redundant. Its disease associations include neurodegenerative disease and neoplasm, with meaningful literature support.
- **Conclusion**: Established evidence supports IMMT as the module member most directly related to mitochondrial architecture and cristae organization. Its co-abundance may indicate structural coordination of the inner membrane with respiratory complexes, but this architectural role remains a hypothesis for the ovary–skin context.

#### AIFM1

- **Related proteins** (co-abundance neighbors): UQCRC2 (0.80), ATP5F1A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apoptosis inducing factor mitochondria associated 1. This gene encodes a flavoprotein essential for nuclear disassembly in apoptotic cells, and it is found in the mitochondrial intermembrane space in healthy cells. Induction of apoptosis results in the translocation of this protein to the nucleus where it affects chromosome condensation and fragmentation. In addition, this gene product induces mitochondria to release the apoptogenic proteins cytochr…
- **Diseases (Open Targets)**: severe X-linked mitochondrial encephalomyopathy (0.813); X-linked hereditary sensory and autonomic neuropathy with hearing loss (0.798); Charcot-Marie-Tooth disease X-linked recessive 4 (0.761); spondyloepimetaphyseal dysplasia, Bieganski type (0.747); combined oxidative phosphorylation deficiency (0.615)
- **Europe PMC papers**: 1952
- **Why important**: AIFM1 is a mitochondrial flavoprotein associated with apoptotic nuclear disassembly, release of apoptogenic factors, respiratory-chain assembly, and oxidative-phosphorylation deficiency. It connects to UQCRC2 and ATP5F1A in the module and contributes to the inner-membrane and mitochondrial-envelope terms (GO:CC mitochondrial inner membrane; q_global = 2.64e-05), (GO:CC organelle inner membrane; q_global = 4.19e-05), (GO:CC mitochondrial membrane; q_global = 0.000286), (GO:CC mitochondrial envelope; q_global = 0.000541), and (GO:CC organelle envelope; q_global = 0.00811). Unlike several other members, it has no listed STRING partners or hu.MAP complexes in this fact sheet, making it a potentially informative peripheral or context-dependent member rather than a validated physical bridge. It has strong disease associations involving severe mitochondrial encephalomyopathy, sensory neuropathy, and combined oxidative-phosphorylation deficiency, together with substantial literature support.
- **Conclusion**: Established evidence supports AIFM1 as a mitochondrial apoptosis and respiratory-function gene. Its inclusion may connect energetic state with cell-survival stress responses, but the absence of listed STRING and hu.MAP relationships means that such a connection should remain provisional.

## Module 2

**Tissue pair**: ovary and skin  
**Genes (5)**: ASF1A, MCM2, MCM4, MCM6, MCM7

### Function

This is a DNA replication and genome-maintenance module. The primary evidence is exceptionally coherent: (GO:CC MCM complex; q_global = 3.65e-07) identifies the MCM complex, (GO:CC CMG complex; q_global = 2.82e-06) the CMG complex, (GO:BP regulation of DNA-templated DNA replication initiation; q_global = 4.48e-06) and (GO:BP regulation of DNA-templated DNA replication; q_global = 1.32e-05) regulation of DNA replication, (GO:BP DNA-templated DNA replication; q_global = 3.46e-05) and (GO:BP DNA replication; q_global = 0.000204) DNA replication, and (KEGG DNA replication - Homo sapiens (human); q_global = 0.000113) the human DNA-replication pathway. The module also links replication with forked and double-stranded DNA helicase activity through (5 globally significant GO/KEGG terms, q_global 4.59e-05–5.58e-05; see the table) and (GO:MF DNA helicase activity; q_global = 0.000251), and with homologous-recombination and double-strand-break repair through (4 globally significant GO/KEGG terms, q_global 0.000632–0.0011; see the table) and (GO:BP DNA repair; q_global = 0.00182), (GO:BP DNA recombination; q_global = 0.00744) (GO:BP double-strand break repair; q_global = 0.00774) (GO:BP DNA damage response; q_global = 0.00807). All genes contribute to the globally significant DNA-replication or DNA-repair signal through (GO:BP DNA-templated DNA replication; q_global = 3.46e-05), (GO:BP DNA replication; q_global = 0.000204), (GO:BP DNA repair; q_global = 0.00182), (GO:BP DNA damage response; q_global = 0.00807), and (GO:BP DNA metabolic process; q_global = 0.0106). MCM2, MCM4, MCM6, and MCM7 form the core MCM-related signal, while ASF1A adds chromatin assembly and replication-dependent histone handling. The shared ovary–skin pattern is therefore best interpreted as coordinated replication-fork, chromosome-maintenance, and replication-repair biology rather than as a tissue-specific secretory pathway.

**Cell composition.** The module is composed entirely of intracellular nuclear proteins, with no secreted genes. HPA places the proteins in the nucleoplasm and reports no broad immune-cell enrichment, so this is not a plasma-protein or overt blood-cell marker module. However, the HPA evidence shows tissue enhancement that frequently involves bone marrow or lymphoid tissue and cell-type enhancement involving erythrocyte progenitors, megakaryocyte progenitors, monocyte progenitors, and related progenitor populations. This pattern is compatible with proliferation-associated biology and raises the possibility that shared proliferative cell states, including progenitor-like or cycling cells, contribute to the ovary and skin co-abundance signal. It does not by itself establish blood contamination. Protein detection is observed for most genes in both tissues, with ASF1A lacking the reported tissue immunohistochemistry detection and MCM6 not detected in ovary.

**GO/KEGG enrichment**: 46 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC MCM complex | 3.65e-07 | MCM2, MCM4, MCM6, MCM7 |
| GO:BP double-strand break repair via break-induced replication | 8.35e-07 | MCM2, MCM4, MCM6, MCM7 |
| GO:CC CMG complex | 2.82e-06 | MCM2, MCM4, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication initiation | 4.48e-06 | MCM2, MCM4, MCM6, MCM7 |
| GO:CC DNA replication preinitiation complex | 4.48e-06 | MCM2, MCM4, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication | 1.32e-05 | MCM2, MCM4, MCM6, MCM7 |
| GO:BP DNA-templated DNA replication | 3.46e-05 | ASF1A, MCM2, MCM4, MCM6, MCM7 |
| GO:MF four-way junction helicase activity | 4.59e-05 | MCM2, MCM4, MCM6, MCM7 |
| GO:MF forked DNA-dependent helicase activity | 4.59e-05 | MCM2, MCM4, MCM6, MCM7 |
| GO:MF double-stranded DNA helicase activity | 5.58e-05 | MCM2, MCM4, MCM6, MCM7 |
| GO:MF 3'-5' DNA helicase activity | 5.58e-05 | MCM2, MCM4, MCM6, MCM7 |
| GO:MF single-stranded 3'-5' DNA helicase activity | 5.58e-05 | MCM2, MCM4, MCM6, MCM7 |
| GO:BP DNA replication initiation | 9.55e-05 | MCM2, MCM4, MCM6, MCM7 |
| KEGG DNA replication - Homo sapiens (human) | 0.000113 | MCM2, MCM4, MCM6, MCM7 |
| GO:MF single-stranded DNA helicase activity | 0.00013 | MCM2, MCM4, MCM6, MCM7 |

### STRING and hu.MAP

STRING supports a tightly integrated module: every possible gene pair meets the stated high-confidence interaction threshold. The strongest and most complete relationships connect MCM2, MCM4, MCM6, and MCM7, which is consistent with their known MCM-complex membership. STRING supplementary terms (10 supplementary STRING terms; within-query FDR 2.71e-07–5.74e-07) identify the MCM and CMG complexes and conserved MCM domains, while (5 supplementary STRING terms; within-query FDR 1.51e-06–7.39e-06) support DNA unwinding, break-induced replication, replication-initiation control, and ATR activation during replication stress. These STRING terms are corroborative and are not treated as globally corrected enrichment. hu.MAP independently places the MCM core in multiple complexes, including assemblies containing MCMBP, the broader CMG machinery, GINS proteins, CDC45, TIMELESS, TIPIN, CLSPN, and chromatin-associated proteins. ASF1A has a more peripheral hu.MAP placement with MCM2 in a histone and chromatin-assembly complex. Together, the evidence indicates that the network is largely a recovered fragment of established replication machinery, with ASF1A connecting that machinery to nucleosome assembly and replication-associated chromatin handling.

**STRING interactions (score >= 0.7)**: 10 of 10 gene pairs: ASF1A–MCM2 (0.992); ASF1A–MCM4 (0.899); ASF1A–MCM6 (0.9); ASF1A–MCM7 (0.879); MCM2–MCM4 (0.999); MCM2–MCM6 (0.999); MCM2–MCM7 (0.999); MCM4–MCM6 (0.999); MCM4–MCM7 (0.999); MCM6–MCM7 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component MCM complex (FDR = 2.71e-07, 4 genes); COMPARTMENTS MCM complex (FDR = 2.93e-07, 4 genes); InterPro MCM domain (FDR = 4.54e-07, 4 genes); InterPro Mini-chromosome maintenance, conserved site (FDR = 4.54e-07, 4 genes); InterPro MCM N-terminal domain (FDR = 4.54e-07, 4 genes); InterPro Mini-chromosome maintenance protein (FDR = 4.54e-07, 4 genes); InterPro MCM OB domain (FDR = 4.54e-07, 4 genes); InterPro MCM, AAA-lid domain (FDR = 4.54e-07, 4 genes); Component CMG complex (FDR = 5.32e-07, 4 genes); COMPARTMENTS CMG complex (FDR = 5.74e-07, 4 genes); RCTM Unwinding of DNA (FDR = 1.51e-06, 4 genes); Process Double-strand break repair via break-induced replication (FDR = 2.83e-06, 4 genes); Process Regulation of DNA-templated DNA replication initiation (FDR = 4.81e-06, 4 genes); Process DNA unwinding involved in DNA replication (FDR = 6.12e-06, 4 genes); RCTM Activation of ATR in response to replication stress (FDR = 7.39e-06, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06061.1 (MCM4, MCM7, MCM2, MCM6; 4/5); huMAP3_05529.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_07113.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_14758.1 (MCM4, MCM7, MCM2, MCM6; 4/14); huMAP3_08554.1 (MCM4, MCM7, MCM2, MCM6; 4/15); huMAP3_11832.1 (MCM4, MCM7, MCM2, MCM6; 4/15); huMAP3_12180.1 (MCM4, MCM7, MCM2, MCM6; 4/17); huMAP3_09860.1 (MCM4, MCM2, MCM6; 3/4); huMAP3_00154.1 (MCM4, MCM2, MCM6; 3/5); huMAP3_11119.1 (MCM4, MCM7, MCM6; 3/14); huMAP3_09466.1 (MCM4, MCM2, MCM6; 3/23); huMAP3_10862.1 (MCM4, MCM2, MCM6; 3/33); huMAP3_14306.1 (MCM4, MCM2, MCM6; 3/55); huMAP3_02602.1 (MCM4, MCM6; 2/2); huMAP3_08848.1 (MCM4, MCM6; 2/15); huMAP3_10747.1 (MCM2, ASF1A; 2/25)

### Novelty

The biological function of this module is not a new molecular discovery: MCM2, MCM4, MCM6, and MCM7 are well-established replication-complex proteins, their pairwise STRING relationships are already known, and hu.MAP contains multiple compatible complexes. The potentially novel aspect is the observation that this particular co-abundance configuration is conserved between ovary and skin. That cross-tissue recurrence may be useful as a systems-level observation, but it should not be claimed as a newly discovered complex or mechanism. Absence of a particular module boundary or exact five-gene grouping from STRING or hu.MAP would not prove novelty, because those resources describe known interactions and complexes rather than this specific tissue-pair co-abundance pattern. Independent replication in additional cohorts, control for cell composition, and comparison with other proliferative modules would be needed to establish whether the cross-tissue grouping is genuinely distinctive.

**Hypothesis.** Hypothesis: the conserved ovary–skin module reflects a shared cycling or replication-demanding cell state in which the MCM helicase core licenses and supports replication forks, while ASF1A coordinates histone delivery and nucleosome reassembly during DNA synthesis and repair. The accompanying repair and replication-stress annotations suggest that the state may include management of stalled or damaged forks, but the co-abundance data do not demonstrate replication stress, cell-cycle phase, or causal regulation. A testable prediction is that module abundance will track markers of proliferating progenitor or renewing cells and will correlate with independent measures of replication activity, while adjustment for cell composition will determine how much of the shared signal is intrinsic to tissue cells.

### Important genes

#### MCM2

- **Related proteins** (co-abundance neighbors): MCM6 (0.88), MCM7 (0.87), ASF1A (0.83); STRING partners: ASF1A (0.992), MCM4 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary, skin
- **hu.MAP 3.0**: huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_10747.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a central member of the MCM core and is connected to MCM6, MCM7, and ASF1A in the module. It contributes to every primary MCM-related enrichment listed across (46 globally significant GO/KEGG terms, q_global 3.65e-07–0.0467; see the table) where present, including replication initiation, helicase activity, repair, and cell-cycle DNA replication. HPA detects it in both ovary and skin and shows enhancement in bone marrow and lymphoid tissue. It has the largest literature volume among the module genes and disease associations including autosomal dominant nonsyndromic hearing loss. Its broad annotation and network centrality make it a strong representative of the module's core function.
- **Conclusion**: Established: MCM2 is a conserved component of the replication licensing and helicase machinery and is strongly supported as a core module gene by GO/KEGG, STRING, hu.MAP, and literature evidence. Hypothesis: its abundance may act as a sensitive indicator of the proliferative state represented in both tissues, but this cannot be inferred as a tissue-specific causal role from co-abundance alone.

#### MCM4

- **Related proteins** (co-abundance neighbors): MCM6 (0.89), MCM7 (0.86); STRING partners: ASF1A (0.899), MCM2 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary, skin
- **hu.MAP 3.0**: huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_11119.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 4. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication rel…
- **Diseases (Open Targets)**: primary immunodeficiency with natural-killer cell deficiency and adrenal insufficiency (0.714); X-linked adrenal hypoplasia congenita (0.185); lung adenocarcinoma (0.112); microcephaly (0.111); neoplasm (0.102)
- **Europe PMC papers**: 4082
- **Why important**: MCM4 is part of the tightly connected MCM2–MCM4–MCM6–MCM7 core and participates in the full set of globally significant MCM, CMG, replication, helicase, and repair annotations, including (6 globally significant GO/KEGG terms, q_global 3.65e-07–1.32e-05; see the table), (13 globally significant GO/KEGG terms, q_global 4.59e-05–0.000632; see the table), and later repair terms. It has extensive STRING and hu.MAP support across assemblies containing the MCM and CMG machinery. HPA detects it in ovary and skin, with enhancement in bone marrow, and disease associations include natural-killer-cell deficiency with adrenal insufficiency and adrenal hypoplasia. Its network position and established disease relevance make it an important functional core gene.
- **Conclusion**: Established: MCM4 is a core replication-complex component with strong independent complex and pathway support. Hypothesis: variation in its co-abundance may reflect differences in replication capacity or replication-associated repair demand, but the module does not establish such a direction of effect.

#### MCM6

- **Related proteins** (co-abundance neighbors): MCM4 (0.89), MCM2 (0.88), MCM7 (0.88), ASF1A (0.86); STRING partners: ASF1A (0.9), MCM2 (0.999), MCM4 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_11119.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 6. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: lactose intolerance (0.246); neurodegenerative disease (0.225); obesity disorder (0.166); nervous system disorder (0.141); systemic lupus erythematosus (0.140)
- **Europe PMC papers**: 3766
- **Why important**: MCM6 has the strongest weighted network position in the module and connects the MCM core to ASF1A. It appears across the primary MCM, replication, helicase, recombination, and DNA-repair terms, including (6 globally significant GO/KEGG terms, q_global 3.65e-07–1.32e-05; see the table), (32 globally significant GO/KEGG terms, q_global 4.59e-05–0.0117; see the table), and (4 globally significant GO/KEGG terms, q_global 0.0289–0.0467; see the table). It is represented in many hu.MAP complexes and has complete STRING support with the other module genes. HPA places it in the nucleoplasm, with lymphoid-tissue and multiple progenitor-cell enhancements, while protein detection is reported in skin but not ovary. Its annotated disease associations include lactose intolerance, neurodegenerative disease, obesity disorder, and systemic lupus erythematosus, and it has substantial literature coverage.
- **Conclusion**: Established: MCM6 is a highly connected MCM-core gene with strong pathway, interaction, and complex evidence. Hypothesis: its tissue-asymmetric protein detection could reflect abundance or sampling differences rather than absence of the biology in ovary; this requires direct validation.

#### MCM7

- **Related proteins** (co-abundance neighbors): MCM6 (0.88), MCM2 (0.87), MCM4 (0.86), ASF1A (0.83); STRING partners: ASF1A (0.879), MCM2 (0.999), MCM4 (0.999), MCM6 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary, skin
- **hu.MAP 3.0**: huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_11119.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 is a highly connected member of the MCM core and is detected by HPA in both ovary and skin. It participates in the globally significant MCM, CMG, replication, helicase, homologous-recombination, and DNA-damage-response annotations. STRING and hu.MAP support its association with the MCM and CMG assemblies. It has extensive literature coverage and disease associations including spastic paraplegia, Meier-Gorlin syndrome, AP-four deficiency syndrome, microcephaly, and trichiasis. Its combination of cross-tissue detection, network connectivity, and disease relevance makes it a particularly useful marker of the conserved module.
- **Conclusion**: Established: MCM7 is a core replication and repair-machinery component supported by the enrichment, interaction, complex, HPA, and literature evidence. Hypothesis: MCM7 may help report the abundance of replication-competent cells shared by ovary and skin, but it is not evidence by itself for a specific disease mechanism in either tissue.

#### ASF1A

- **Related proteins** (co-abundance neighbors): MCM6 (0.86), MCM7 (0.83), MCM2 (0.83); STRING partners: MCM2 (0.992), MCM4 (0.899), MCM6 (0.9), MCM7 (0.879)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10747.1
- **Function (MyGene.info)**: anti-silencing function 1A histone chaperone. This gene encodes a member of the H3/H4 family of histone chaperone proteins and is similar to the anti-silencing function-1 gene in yeast. The protein is a key component of a histone donor complex that functions in nucleosome assembly. It interacts with histones H3 and H4, and functions together with a chromatin assembly factor during DNA replication and repair. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: hypothyroidism (0.351); neurodegenerative disease (0.255); schizophrenia (0.142); intelligence (0.142); hepatocellular carcinoma (0.099)
- **Europe PMC papers**: 4470
- **Why important**: ASF1A is the module's chromatin-focused member. It connects to all four MCM-core proteins in the co-abundance network and contributes to the globally significant terms for DNA replication, DNA repair, DNA damage response, DNA metabolism, and chromosome biology, including (GO:BP DNA-templated DNA replication; q_global = 3.46e-05), (GO:BP DNA replication; q_global = 0.000204), (GO:BP DNA repair; q_global = 0.00182), (GO:BP DNA damage response; q_global = 0.00807), (GO:BP DNA metabolic process; q_global = 0.0106), and (GO:CC chromosome; q_global = 0.0467). Its curated function is histone chaperoning, nucleosome assembly, and replication- and repair-associated chromatin handling. hu.MAP links it with MCM2 in a chromatin and histone-related complex, although it has no separate STRING functional-enrichment term in the supplied results. HPA reports low tissue specificity and cell-type enhancement in megakaryocytes and oocytes, and it has substantial literature coverage with disease associations including hypothyroidism, neurodegenerative disease, schizophrenia, intelligence, and hepatocellular carcinoma.
- **Conclusion**: Established: ASF1A supplies a biologically plausible chromatin-assembly bridge between DNA replication and repair and the MCM helicase core. Hypothesis: its inclusion may indicate that the shared tissue signal involves chromatin restoration during active replication, rather than merely passive co-expression of MCM genes.

## Module 3

**Tissue pair**: ovary and skin  
**Genes (10)**: ATP1A1, ATP1B3, ATP2A2, CANX, CKAP4, HMOX2, MOGS, NCSTN, DARS2, TIMM50

### Function

The module is most consistent with a membrane and endoplasmic-reticulum calcium and cation-handling program linked to protein folding and maturation. The strongest primary evidence is the global enrichment for mineral absorption (KEGG Mineral absorption - Homo sapiens (human); q_global = 0.00518), endoplasmic reticulum (GO:CC endoplasmic reticulum; q_global = 0.0115), melanosome and pigment granule (GO:CC melanosome; q_global = 0.0117) (GO:CC pigment granule; q_global = 0.0117), cation-transporting ATPase complexes (GO:CC cation-transporting ATPase complex; q_global = 0.0122) (GO:CC ATPase dependent transmembrane transport complex; q_global = 0.0122), and additional ATPase-related transport pathways (KEGG Cardiac muscle contraction - Homo sapiens (human); q_global = 0.0227) (KEGG Pancreatic secretion - Homo sapiens (human); q_global = 0.0227) (KEGG Thyroid hormone synthesis - Homo sapiens (human); q_global = 0.027). The endoplasmic-reticulum membrane and subcompartment enrichments (GO:CC endoplasmic reticulum membrane; q_global = 0.0493) (GO:CC endoplasmic reticulum subcompartment; q_global = 0.0493) support an integrated secretory and membrane-protein quality-control context. The pathway labels involving cardiac muscle, pancreatic secretion, and thyroid hormone synthesis should not be interpreted as evidence that the module specifically represents those organs; they are driven largely by the shared ATPase genes. Together, the genes suggest coordinated ion-gradient maintenance, calcium sequestration, ER folding and glycoprotein processing, membrane-complex assembly, and possibly pigment-organelle biology. No GO or KEGG term without an globally significant GO/KEGG tag is used as primary global evidence.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. The proteins are predominantly intracellular or membrane associated, with ER, plasma-membrane, mitochondrial, vesicular, and cytosolic locations. Most genes have low tissue specificity, while the HPA single-cell annotations span several cell types, including late spermatids, cardiomyocytes, neutrophils, and other epithelial or specialized cells. Blood-cell specificity is generally low, with immune-cell enhancement reported for only CKAP4 and basophil enrichment represented in the summary. Therefore, a simple blood contamination explanation is not supported, although shared cell types or broadly expressed cellular machinery could contribute to the ovary-skin conservation. Protein detection is broad in both tissues, supporting that the module is not merely an undetected or technically absent tissue program. The tissue-enhanced annotation for ATP1A1 in parathyroid gland and the group-enriched annotation for ATP2A2 in muscle-related tissues indicate some cell- or tissue-contextual contributions, but they do not establish a tissue-specific module identity.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Mineral absorption - Homo sapiens (human) | 0.00518 | ATP1A1, ATP1B3, HMOX2 |
| GO:CC endoplasmic reticulum | 0.0115 | ATP1A1, ATP2A2, CANX, CKAP4, HMOX2, MOGS, NCSTN, TIMM50 |
| GO:CC melanosome | 0.0117 | ATP1A1, ATP1B3, CANX, NCSTN |
| GO:CC pigment granule | 0.0117 | ATP1A1, ATP1B3, CANX, NCSTN |
| GO:CC cation-transporting ATPase complex | 0.0122 | ATP1A1, ATP1B3, ATP2A2 |
| GO:CC ATPase dependent transmembrane transport complex | 0.0122 | ATP1A1, ATP1B3, ATP2A2 |
| KEGG Cardiac muscle contraction - Homo sapiens (human) | 0.0227 | ATP1A1, ATP1B3, ATP2A2 |
| KEGG Pancreatic secretion - Homo sapiens (human) | 0.0227 | ATP1A1, ATP1B3, ATP2A2 |
| KEGG Thyroid hormone synthesis - Homo sapiens (human) | 0.027 | ATP1A1, ATP1B3, CANX |
| GO:CC endoplasmic reticulum membrane | 0.0493 | ATP2A2, CANX, CKAP4, HMOX2, MOGS, NCSTN |
| GO:CC endoplasmic reticulum subcompartment | 0.0493 | ATP2A2, CANX, CKAP4, HMOX2, MOGS, NCSTN |

### STRING and hu.MAP

STRING supports a compact biochemical core rather than ten uniformly connected proteins. The strongest known relationship is ATP1A1 with ATP1B3, and ATP1A1 also connects with ATP2A2; these relationships agree with a cation-transporting ATPase complex. ATP2A2 connects with CANX, while CANX connects strongly with MOGS and also with NCSTN, linking calcium handling to ER chaperoning, glycoprotein processing, and membrane-protein processing. STRING functional categories independently support transmembrane helices, integral membrane components, the cation-transporting ATPase complex, melanosome, and ER membrane (15 supplementary STRING terms; within-query FDR 0.00055–0.0064). These STRING results are supplementary and do not replace the globally corrected GO or KEGG evidence. hu.MAP identifies one complex containing ATP1A1 and ATP2A2 (hu.MAP huMAP3_10473.1), which provides independent complex-level support for the ATPase component. The remaining module members are not represented together in a hu.MAP complex with multiple module members, so the full module is not an established single physical complex. The network therefore appears to combine a known ATPase core with an ER quality-control and membrane-trafficking neighborhood.

**STRING interactions (score >= 0.7)**: 6 of 45 gene pairs: ATP1A1–ATP1B3 (0.995); ATP1A1–ATP2A2 (0.82); ATP1B3–ATP2A2 (0.821); ATP2A2–CANX (0.849); CANX–MOGS (0.952); CANX–NCSTN (0.754)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transmembrane helix (FDR = 0.00055, 8 genes); Component Integral component of membrane (FDR = 0.00076, 9 genes); Component Cation-transporting ATPase complex (FDR = 0.00076, 3 genes); Component Integral component of plasma membrane (FDR = 0.0013, 5 genes); Component Melanosome (FDR = 0.0013, 4 genes); KEGG Mineral absorption (FDR = 0.0017, 3 genes); COMPARTMENTS Cation-transporting ATPase complex (FDR = 0.0022, 3 genes); Component Endoplasmic reticulum membrane (FDR = 0.0033, 6 genes); KEGG Cardiac muscle contraction (FDR = 0.0034, 3 genes); KEGG Thyroid hormone synthesis (FDR = 0.0034, 3 genes); KEGG Pancreatic secretion (FDR = 0.0034, 3 genes); KEGG Adrenergic signaling in cardiomyocytes (FDR = 0.0035, 3 genes); KEGG cGMP-PKG signaling pathway (FDR = 0.0048, 3 genes); KEGG cAMP signaling pathway (FDR = 0.0048, 3 genes); Component Endoplasmic reticulum (FDR = 0.0064, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10473.1 (ATP1A1, ATP2A2; 2/24)

### Novelty

This module should not be described as a newly discovered molecular complex. The ATP1A1-ATP1B3 relationship, the ATPase associations involving ATP1A1 and ATP2A2, and several CANX-centered ER relationships are already supported by STRING, while ATP1A1 and ATP2A2 also occur together in hu.MAP (hu.MAP huMAP3_10473.1). The enrichment themes are likewise biologically recognizable rather than unprecedented. However, the conserved co-abundance of this particular combination across ovary and skin may represent a novel tissue-pair observation or a useful systems-level association. The absence of a complete match in STRING or hu.MAP cannot establish novelty, because co-abundance can reflect shared regulation, cell composition, transient contacts, or pathway coordination rather than a stable physical complex. A defensible novelty claim is therefore limited to the cross-tissue co-abundance organization and its specific combination of ion transport, ER processing, and membrane biology, pending replication in independent cohorts and experimental testing.

**Hypothesis.** Hypothesis: in both ovary and skin, a shared population of viable, metabolically active cells coordinately maintains plasma-membrane sodium and potassium gradients and ER calcium handling while producing and quality-controlling membrane glycoproteins. ATP1A1 and ATP1B3 may provide the plasma-membrane sodium-potassium pump component, while ATP2A2 supports ER calcium sequestration. CANX and MOGS may couple calcium-sensitive ER folding with N-linked glycan processing, and NCSTN may connect the membrane-protein processing environment to gamma-secretase-related biology. The co-abundance could consequently reflect a coordinated membrane-proteostasis state that is shared by selected ovarian and cutaneous cell populations. This is a mechanistic hypothesis, not proof of direct physical interaction among all module members; it should be tested through cell-type-resolved expression, perturbation of the ATPase or ER components, and measurement of ion gradients, ER stress, glycoprotein maturation, and membrane-protein processing.

### Important genes

#### CANX

- **Related proteins** (co-abundance neighbors): CKAP4 (0.82), ATP1A1 (0.82), DARS2 (0.82), MOGS (0.81), ATP1B3 (0.81); STRING partners: ATP2A2 (0.849), MOGS (0.952), NCSTN (0.754)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in ovary, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX has the strongest network position in the module and is connected to several ATPase, ER, and glycoprotein-processing genes. It is an ER calcium-binding molecular chaperone involved in folding and quality control of newly synthesized N-linked glycoproteins. It contributes to the globally significant ER, melanosome, pigment-granule, and ER-membrane findings (6 globally significant GO/KEGG terms, q_global 0.0115–0.0493; see the table). Its STRING links to ATP2A2, MOGS, and NCSTN provide a bridge between calcium handling, glycan processing, and membrane-protein maturation. Its substantial literature volume and disease links make it a well-established biological anchor rather than an obscure network passenger.
- **Conclusion**: Established conclusion: CANX is the most plausible ER proteostasis hub in this module and provides strong support for an ER-centered interpretation. Hypothesis: its co-abundance with the ATPase genes marks coordinated calcium-dependent folding capacity in shared ovarian and cutaneous cell populations.

#### ATP1A1

- **Related proteins** (co-abundance neighbors): ATP1B3 (0.88), ATP2A2 (0.85), CANX (0.82), TIMM50 (0.81); STRING partners: ATP1B3 (0.995), ATP2A2 (0.82)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_10473.1
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 is a highly connected network member and participates in nearly all of the globally significant pathway enrichments, including mineral absorption, melanosome and pigment granule, cation-transporting ATPase, cardiac muscle contraction, pancreatic secretion, and thyroid hormone synthesis (8 globally significant GO/KEGG terms, q_global 0.00518–0.027; see the table). It encodes the catalytic sodium-potassium pump subunit that establishes transmembrane sodium and potassium gradients. Its very strong STRING relationship with ATP1B3 and relationships with ATP2A2 and CANX define the central ion-transport and ER-associated portion of the module. It is represented with ATP2A2 in hu.MAP (hu.MAP huMAP3_10473.1), has broad protein detection, and has substantial literature and disease association.
- **Conclusion**: Established conclusion: ATP1A1 is a principal functional driver of the module's ion-transport signature and a central network connector. Hypothesis: variation in ATP1A1 abundance may coordinate membrane excitability or transport demands with ER calcium and proteostasis requirements in the shared tissues.

#### ATP2A2

- **Related proteins** (co-abundance neighbors): ATP1A1 (0.85), HMOX2 (0.80); STRING partners: ATP1A1 (0.82), ATP1B3 (0.821), CANX (0.849)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in ovary, skin
- **hu.MAP 3.0**: huMAP3_10473.1
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darie…
- **Diseases (Open Targets)**: Darier disease (0.823); acrokeratosis verruciformis (0.663); neurodegenerative disease (0.507); hereditary disease (0.416); schizophrenia (0.406)
- **Europe PMC papers**: 9327
- **Why important**: ATP2A2 is the module's principal ER calcium pump and belongs to the cation-transporting ATPase and ER-membrane enrichments (7 globally significant GO/KEGG terms, q_global 0.0115–0.0493; see the table). It connects in the network to ATP1A1 and HMOX2 and has STRING support with ATP1A1, ATP1B3, and CANX. Its presence with ATP1A1 in hu.MAP (hu.MAP huMAP3_10473.1) supports a known ATPase-related complex context. Its established role in calcium transport, epidermis development, and muscle-related physiology is especially relevant to a module shared by skin and ovary. Its disease association with Darier disease gives the gene direct relevance to cutaneous biology, and it has substantial literature support.
- **Conclusion**: Established conclusion: ATP2A2 provides the strongest mechanistic link between ER calcium handling and the skin-relevant biology of the module. Hypothesis: coordinated ATP2A2 and ATP1A1 activity may maintain coupled intracellular and extracellular ion homeostasis in the conserved cell state.

#### MOGS

- **Related proteins** (co-abundance neighbors): CANX (0.81); STRING partners: CANX (0.952)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in ovary, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosyl-oligosaccharide glucosidase. This gene encodes the first enzyme in the N-linked oligosaccharide processing pathway. The enzyme cleaves the distal alpha-1,2-linked glucose residue from the Glc(3)-Man(9)-GlcNAc(2) oligosaccharide precursor. This protein is located in the lumen of the endoplasmic reticulum. Defects in this gene are a cause of type IIb congenital disorder of glycosylation (CDGIIb). Two transcript variants encodin…
- **Diseases (Open Targets)**: MOGS-congenital disorder of glycosylation (0.818); congenital disorder of glycosylation (0.374); congenital disorder of glycosylation type II (0.370); severe acute respiratory syndrome (0.370); SRD5A3-congenital disorder of glycosylation (0.370)
- **Europe PMC papers**: 987
- **Why important**: MOGS is directly connected to CANX and is included in the globally significant ER and ER-membrane terms (GO:CC endoplasmic reticulum; q_global = 0.0115) (GO:CC endoplasmic reticulum membrane; q_global = 0.0493) (GO:CC endoplasmic reticulum subcompartment; q_global = 0.0493). It encodes an ER enzyme that initiates processing of N-linked oligosaccharides, placing it in the same protein-folding and glycoprotein-maturation process as CANX. Its strong STRING relationship with CANX supports a known functional connection rather than a purely statistical co-abundance link. Its congenital-disorder associations provide disease relevance, while its literature volume is substantial enough to support an established molecular interpretation.
- **Conclusion**: Established conclusion: MOGS supports the interpretation that the module includes ER glycan processing and quality control. Hypothesis: MOGS abundance may track the glycoprotein-processing load generated by the membrane proteins whose maturation depends on the module's ER environment.

#### NCSTN

- **Related proteins** (co-abundance neighbors): TIMM50 (0.87); STRING partners: CANX (0.754)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nicastrin. This gene encodes a type I transmembrane glycoprotein that is an integral component of the multimeric gamma-secretase complex. The encoded protein cleaves integral membrane proteins, including Notch receptors and beta-amyloid precursor protein, and may be a stabilizing cofactor required for gamma-secretase complex assembly. The cleavage of beta-amyloid precursor protein yields amyloid beta peptide…
- **Diseases (Open Targets)**: acne inversa, familial, 1 (0.724); neurodegenerative disease (0.525); desmoid tumor (0.503); Alzheimer disease (0.406); hidradenitis suppurativa (0.389)
- **Europe PMC papers**: 2357
- **Why important**: NCSTN contributes to the globally significant ER, melanosome, pigment-granule, and ER-membrane terms (5 globally significant GO/KEGG terms, q_global 0.0115–0.0493; see the table). It encodes nicastrin, a stabilizing component of the gamma-secretase complex involved in cleavage of integral membrane proteins, including Notch receptors and amyloid precursor protein. Its STRING connection to CANX links membrane-protein processing with ER quality control, while its network edge to TIMM50 suggests a less-established cross-compartment association within this module. Its disease associations include acne inversa, hidradenitis suppurativa, and Alzheimer disease, giving it relevance to skin and membrane biology. Its literature volume is substantial.
- **Conclusion**: Established conclusion: NCSTN contributes a membrane-proteolysis and protein-processing dimension that complements the ATPase and ER chaperone core. Hypothesis: its co-abundance with CANX may reflect coordinated production or turnover of membrane proteins in the conserved ovarian and cutaneous cellular state, but direct coupling to the ATPase core remains unproven.

## Module 4

**Tissue pair**: ovary and skin  
**Genes (8)**: DHX9, FAM120A, HNRNPL, HNRNPR, IGF2BP3, RPL12, SUPT16H, EFTUD2

### Function

The module is best interpreted as a conserved RNA-binding and post-transcriptional gene-regulation module. All members support the globally corrected RNA-binding and nucleic-acid-binding terms (GO:MF RNA binding; q_global = 0.00698) and (GO:MF nucleic acid binding; q_global = 0.0481). DHX9 and IGF2BP3 additionally support globally corrected CRD-mediated mRNA stabilization (GO:BP CRD-mediated mRNA stabilization; q_global = 0.0366). STRING supplements this interpretation with RNA binding, mRNA binding, RNA metabolism, mRNA processing, and major-pathway splicing (STRING Keyword RNA-binding; within-query FDR = 0.0029), (STRING Function RNA binding; within-query FDR = 0.0043), (STRING WikiPathways mRNA processing; within-query FDR = 0.005), (STRING RCTM Metabolism of RNA; within-query FDR = 0.03), (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0325), (STRING Function mRNA binding; within-query FDR = 0.0442). The module therefore links RNA recognition and stabilization with splicing, translation, and transcriptional or chromatin-associated regulation rather than representing one single molecular complex.

**Cell composition.** The HPA evidence argues against a plasma or secreted-protein module: no member is secreted, and most proteins are detected in both ovary and skin. Most genes have low tissue specificity and low immune-cell specificity, with no recurring enriched blood-cell population. The broadly expressed RNA-processing, translation, splicing, and transcriptional functions suggest a housekeeping-like component. IGF2BP3 is the main exception, with tissue enhancement in lymphoid tissue and placenta, several cell-type enhancements, no immune-cell detection, and no HPA protein detection in ovary or skin. Shared cellular RNA-processing programs are therefore more plausible than a blood or secreted-protein explanation, although cell-composition effects cannot be excluded.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF RNA binding | 0.00698 | DHX9, EFTUD2, FAM120A, HNRNPL, HNRNPR, IGF2BP3, RPL12, SUPT16H |
| GO:BP CRD-mediated mRNA stabilization | 0.0366 | DHX9, IGF2BP3 |
| GO:MF nucleic acid binding | 0.0481 | DHX9, EFTUD2, FAM120A, HNRNPL, HNRNPR, IGF2BP3, RPL12, SUPT16H |

### STRING and hu.MAP

STRING supports a known RNA-processing core involving DHX9, HNRNPL, and HNRNPR, together with an EFTUD2-RPL12 relationship. Its enrichment results support RNA binding, mRNA processing, splicing, RNA metabolism, and mRNA stabilization (STRING Keyword RNA-binding; within-query FDR = 0.0029) through (STRING Function mRNA binding; within-query FDR = 0.0442). hu.MAP repeatedly places HNRNPR, HNRNPL, and FAM120A in larger heterogeneous nuclear ribonucleoprotein-associated complexes (hu.MAP huMAP3_07225.1) through (hu.MAP huMAP3_07581.1). These findings support biological coherence and overlap with established RNA-protein assemblies, but the module is not identical to any one hu.MAP complex. Relationships involving FAM120A, IGF2BP3, SUPT16H, and other members should not be assumed to be direct physical interactions unless specifically supported.

**STRING interactions (score >= 0.7)**: 4 of 28 gene pairs: DHX9–HNRNPL (0.901); DHX9–HNRNPR (0.909); EFTUD2–RPL12 (0.752); HNRNPL–HNRNPR (0.961)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword RNA-binding (FDR = 0.0029, 6 genes); Function RNA binding (FDR = 0.0043, 8 genes); Keyword Isopeptide bond (FDR = 0.0044, 7 genes); NetworkNeighborAL Mixed, incl. CRD-mediated mRNA stabilization, and Zinc finger, CHHC-type (FDR = 0.0049, 3 genes); WikiPathways mRNA processing (FDR = 0.005, 4 genes); Keyword Ubl conjugation (FDR = 0.0107, 7 genes); PMID (2021) Identification of host proteins differentially associated with HIV-1 RNA splice variants. (FDR = 0.0166, 5 genes); RCTM Metabolism of RNA (FDR = 0.03, 6 genes); RCTM mRNA Splicing - Major Pathway (FDR = 0.0325, 4 genes); Function mRNA binding (FDR = 0.0442, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07225.1 (HNRNPR, HNRNPL, FAM120A; 3/7); huMAP3_09654.1 (HNRNPR, HNRNPL, FAM120A; 3/13); huMAP3_10659.1 (HNRNPR, HNRNPL, FAM120A; 3/28); huMAP3_10625.1 (HNRNPR, HNRNPL, FAM120A; 3/57); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09281.1 (HNRNPR, FAM120A; 2/14); huMAP3_07581.1 (HNRNPR, HNRNPL; 2/21)

### Novelty

The dominant functions and central HNRNPL-HNRNPR-DHX9 relationships are already established, so this is not a wholly new molecular pathway. Its potential novelty is the coordinated co-abundance of this particular RNA-helicase, heterogeneous nuclear ribonucleoprotein, mRNA-stabilization, spliceosomal, ribosomal, and chromatin-transcription combination across ovary and skin. The supplied resources do not establish whether this exact tissue-pair co-abundance module has been reported previously. Absence from STRING or hu.MAP would not prove novelty because those resources describe interactions and complexes rather than tissue-pair co-abundance. The appropriate conclusion is established biology with a potentially novel systems-level tissue association requiring independent validation.

**Hypothesis.** Hypothesis: shared ovary and skin cellular populations coordinate an RNA-management program in which DHX9 remodels RNA structures, HNRNPL and HNRNPR organize RNA-protein assemblies, IGF2BP3 stabilizes selected transcripts, EFTUD2 supports spliceosome function, SUPT16H connects transcription to chromatin remodeling, and RPL12 reflects translation. FAM120A may help coordinate RNA-binding and splicing-related regulation. This is a mechanistic hypothesis, not proof of causality, direct binding among all members, or a common target-transcript set.

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): FAM120A (0.87), IGF2BP3 (0.85), HNRNPR (0.84), HNRNPL (0.81); STRING partners: HNRNPL (0.901), HNRNPR (0.909)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is a high-connectivity module member linking IGF2BP3, HNRNPR, HNRNPL, and FAM120A. It is the module's RNA helicase and has established roles in unwinding RNA and DNA-RNA complexes, alternative splicing, transcriptional regulation, and nucleic-acid metabolism. It supports (GO:MF RNA binding; q_global = 0.00698), (GO:BP CRD-mediated mRNA stabilization; q_global = 0.0366), and (GO:MF nucleic acid binding; q_global = 0.0481) and appears throughout the STRING RNA-processing evidence (STRING Keyword RNA-binding; within-query FDR = 0.0029) through (STRING Function mRNA binding; within-query FDR = 0.0442). Its extensive literature and disease associations make it a strong interpretive anchor.
- **Conclusion**: Established: DHX9 is a multifunctional RNA helicase and central network connector. Hypothesis: it may couple RNA-structure remodeling to the heterogeneous nuclear ribonucleoprotein and mRNA-stabilization components.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): RPL12 (0.82), DHX9 (0.81); STRING partners: DHX9 (0.901), HNRNPR (0.961)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary, skin
- **hu.MAP 3.0**: huMAP3_07225.1, huMAP3_09654.1, huMAP3_10659.1, huMAP3_10625.1, huMAP3_06093.1, huMAP3_07581.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is a core RNA-processing factor connected to DHX9 and HNRNPR. It supports (GO:MF RNA binding; q_global = 0.00698) and (GO:MF nucleic acid binding; q_global = 0.0481) and the STRING evidence for RNA binding, mRNA binding, RNA processing, and splicing (STRING Keyword RNA-binding; within-query FDR = 0.0029) through (STRING Function mRNA binding; within-query FDR = 0.0442). It repeatedly occurs with HNRNPR and FAM120A in hu.MAP complexes (hu.MAP huMAP3_07225.1) through (hu.MAP huMAP3_06093.1) and (hu.MAP huMAP3_07581.1). Its established function, disease associations, and substantial literature support its importance.
- **Conclusion**: Established: HNRNPL participates in mRNA packaging, processing, and regulation and is part of several known RNA-protein assemblies. Hypothesis: it may help define transcript selectivity and assembly state in the shared ovary-skin program.

#### HNRNPR

- **Related proteins** (co-abundance neighbors): SUPT16H (0.88), DHX9 (0.84), FAM120A (0.83); STRING partners: DHX9 (0.909), HNRNPL (0.961)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary, skin
- **hu.MAP 3.0**: huMAP3_07225.1, huMAP3_09654.1, huMAP3_10659.1, huMAP3_10625.1, huMAP3_06093.1, huMAP3_09281.1, huMAP3_07581.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR connects SUPT16H, DHX9, and FAM120A and supports (GO:MF RNA binding; q_global = 0.00698) and (GO:MF nucleic acid binding; q_global = 0.0481) as well as the principal STRING RNA-processing signals (STRING Keyword RNA-binding; within-query FDR = 0.0029) through (STRING Function mRNA binding; within-query FDR = 0.0442). It has established spliceosomal and mRNA-processing functions and is repeatedly present with HNRNPL and FAM120A in hu.MAP complexes (hu.MAP huMAP3_07225.1) through (hu.MAP huMAP3_07581.1). Its disease associations and literature further support functional importance.
- **Conclusion**: Established: HNRNPR is a spliceosome-associated heterogeneous nuclear ribonucleoprotein and a recurrent member of known RNA-protein complexes. Hypothesis: together with HNRNPL, it may form a central RNA-binding scaffold that recruits other module components.

#### IGF2BP3

- **Related proteins** (co-abundance neighbors): DHX9 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor 2 mRNA binding protein 3. The protein encoded by this gene is primarily found in the nucleolus, where it can bind to the 5' UTR of the insulin-like growth factor II leader 3 mRNA and may repress translation of insulin-like growth factor II during late development. The encoded protein contains several KH domains, which are important in RNA binding and are known to be involved in RNA synthesis and metabolism. A pseudogene ex…
- **Diseases (Open Targets)**: neurodegenerative disease (0.536); type 2 diabetes mellitus (0.405); diabetes mellitus (0.304); celiac disease (0.254); placental abruption (0.175)
- **Europe PMC papers**: 5072
- **Why important**: IGF2BP3 is one of the two genes supporting globally corrected CRD-mediated mRNA stabilization (GO:BP CRD-mediated mRNA stabilization; q_global = 0.0366), while also supporting (GO:MF RNA binding; q_global = 0.00698) and (GO:MF nucleic acid binding; q_global = 0.0481). It connects to DHX9 and contributes to STRING evidence for RNA binding, mRNA binding, RNA metabolism, and mRNA stabilization (STRING Keyword RNA-binding; within-query FDR = 0.0029), (STRING Function RNA binding; within-query FDR = 0.0043), (STRING Keyword Ubl conjugation; within-query FDR = 0.0107), (STRING PMID (2021) Identification of host proteins differentially associated with HIV-1 RNA splice variants.; within-query FDR = 0.0166), (STRING RCTM Metabolism of RNA; within-query FDR = 0.03), (STRING Function mRNA binding; within-query FDR = 0.0442). Its KH domains and established transcript-regulatory role complement the heterogeneous nuclear ribonucleoproteins. Its tissue-enhanced HPA pattern and lack of HPA protein detection in ovary and skin make it important for evaluating cell composition or context-specific regulation.
- **Conclusion**: Established: IGF2BP3 is an RNA-binding protein associated with mRNA stabilization and transcript regulation. Hypothesis: it may provide transcript selectivity to the broader RNA-processing scaffold, but this requires direct validation in ovary and skin.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): FAM120A (0.81); STRING partners: RPL12 (0.752)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 links the module to spliceosomal assembly and conformational change and supports (GO:MF RNA binding; q_global = 0.00698) and (GO:MF nucleic acid binding; q_global = 0.0481). It contributes to supplementary mRNA-processing and major-splicing evidence (STRING Function RNA binding; within-query FDR = 0.0043), (STRING WikiPathways mRNA processing; within-query FDR = 0.005), (STRING Keyword Ubl conjugation; within-query FDR = 0.0107), (STRING RCTM Metabolism of RNA; within-query FDR = 0.03), (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0325). Its connection to FAM120A and STRING relationship with RPL12 link spliceosomal activity with the translation-associated portion of the network. Its established spliceosomal role and disease association make it informative despite its peripheral network position.
- **Conclusion**: Established: EFTUD2 is a spliceosomal factor involved in snRNP assembly, spliceosome remodeling, and pre-mRNA splicing. Hypothesis: it may represent the processing arm that links RNA recognition and remodeling to mature transcript production.

## Module 5

**Tissue pair**: ovary and skin  
**Genes (7)**: ETFA, RDH13, RTN1, SLC25A13, SEC22B, SSR1, VDAC2

### Function

The module does not have a single statistically supported GO or KEGG functional label: no GO/KEGG term passed global correction. Its gene-level annotations nevertheless point to a coordinated intracellular membrane and mitochondrial program. SEC22B and SSR1 support ER membrane trafficking and protein translocation, while RTN1 supports ER membrane organization. SLC25A13, VDAC2, ETFA, and RDH13 support mitochondrial transport, metabolite exchange, electron transfer, fatty-acid oxidation, retinoid metabolism, and protection from oxidative stress. The co-abundance structure therefore most plausibly reflects coupling between ER trafficking and mitochondrial metabolic or stress-related processes, rather than a formally established pathway. Because the module is small and lacks corrected enrichment, this interpretation remains integrative and provisional.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the genes are intracellular or membrane-associated, and the HPA summary identifies only one secreted gene. Most genes have low tissue specificity, while several show cell-type-enhanced or group-enriched expression. Neutrophils recur among the enriched cell types, and liver-associated expression recurs among tissues; RTN1 also has group-enriched monocyte and myeloid dendritic-cell annotations. However, most genes have low immune-cell specificity, so the evidence does not support describing the module as a blood-cell module. The shared ovary-skin signal could partly reflect common cell populations, sample-composition effects, or broadly used intracellular programs rather than a tissue-specific ovary-skin mechanism. Protein detection is stronger in skin than ovary for this gene set, which also cautions against interpreting the module as uniformly active at the protein level in both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied confidence threshold, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple members of the module. Thus, the co-abundance edges should not be treated as established physical protein interactions or as evidence for a known multiprotein complex. The observed relationships may represent coordinated regulation, shared cellular context, indirect metabolic coupling, or technical and compositional covariance. The absence of STRING and hu.MAP support is informative about current interaction knowledge, but it does not disprove functional coordination.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module appears potentially novel as a cross-tissue co-abundance pattern because its members do not form a recognized high-confidence STRING interaction network or a supported hu.MAP complex, and no corrected GO/KEGG or STRING enrichment provides a pre-existing pathway label. That conclusion should be limited to the module-level relationship. The individual genes and their functions are well established to different degrees, and several have substantial disease and literature associations. Therefore, the evidence supports a potentially new observation of coordinated abundance across ovary and skin, but it does not establish a new molecular complex, a new pathway, or a new disease mechanism. Independent replication, cell-composition adjustment, and experimental validation would be needed to claim discovery.

**Hypothesis.** Hypothesis: in a shared cellular context present in ovary and skin, ER membrane organization and trafficking may be co-regulated with mitochondrial substrate exchange, electron transfer, and protection from metabolic or oxidative stress. SEC22B, SSR1, and RTN1 could represent the ER-side component, while SLC25A13, VDAC2, ETFA, and RDH13 could represent the mitochondrial metabolic and stress-response component. The apparent linkage may arise through coordinated organelle homeostasis rather than direct physical binding. A competing hypothesis is that the pattern is driven by shared cell-type composition, particularly cells with neutrophil-related or other cell-type-enhanced expression. This hypothesis is not demonstrated by the enrichment or interaction evidence and should be tested by cell-resolved expression, perturbation, and organelle-function assays.

### Important genes

#### SEC22B

- **Related proteins** (co-abundance neighbors): SLC25A13 (0.86), VDAC2 (0.81), RDH13 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC22 homolog B, vesicle trafficking protein. The protein encoded by this gene is a member of the SEC22 family of vesicle trafficking proteins. It seems to complex with SNARE and it is thought to play a role in the ER-Golgi protein trafficking. This protein has strong similarity to Mus musculus and Cricetulus griseus proteins.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: inflammatory bowel disease (0.285); luminal A breast carcinoma (0.271); colitis (0.238); enteritis (0.238); Crohn disease (0.233)
- **Europe PMC papers**: 1006
- **Why important**: SEC22B has the strongest network connectivity in the module and links the ER-trafficking side to both SLC25A13 and the VDAC2-RDH13 side. Its established role in ER-to-Golgi and retrograde vesicle transport, vesicle fusion, autophagy, and starvation responses makes it a plausible organizational marker for the membrane-trafficking component. It also has extensive literature and disease-association coverage, although those associations do not establish that this module causes those diseases.
- **Conclusion**: Established evidence: SEC22B is a vesicle-trafficking protein with ER-Golgi and autophagy-related functions and is a central co-abundance connector in this module. Hypothesis: it may coordinate ER trafficking with mitochondrial adaptation in the shared ovary-skin context. The module does not establish a direct SEC22B interaction with its neighboring proteins.

#### SLC25A13

- **Related proteins** (co-abundance neighbors): SEC22B (0.86), ETFA (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 25 member 13. This gene is a member of the mitochondrial carrier family. The encoded protein contains four EF-hand Ca(2+) binding motifs in the N-terminal domain, and localizes to mitochondria. The protein catalyzes the exchange of aspartate for glutamate and a proton across the inner mitochondrial membrane, and is stimulated by calcium on the external side of the inner mitochondrial membrane. Mutations in this…
- **Diseases (Open Targets)**: neonatal intrahepatic cholestasis due to citrin deficiency (0.804); citrullinemia type II (0.756); citrin deficiency (0.652); citrullinemia (0.649); citrullinemia type I (0.464)
- **Europe PMC papers**: 1421
- **Why important**: SLC25A13 connects SEC22B to ETFA and is a mitochondrial carrier with calcium-regulated aspartate, glutamate, and proton exchange. Its functions in mitochondrial transport, gluconeogenesis, and ATP production provide a mechanistic bridge between organelle transport and cellular metabolism. Its liver-enriched HPA profile and strong association with citrin-deficiency disorders make it a particularly informative metabolic anchor, while detection in both ovary and skin supports relevance to the shared tissue comparison.
- **Conclusion**: Established evidence: SLC25A13 is a mitochondrial carrier involved in amino-acid exchange and metabolic homeostasis and is linked to citrin-deficiency disorders. Hypothesis: its co-abundance with SEC22B and ETFA may reflect coordinated ER-mitochondrial metabolic support. The data do not show that SLC25A13 directly binds either neighbor.

#### VDAC2

- **Related proteins** (co-abundance neighbors): SSR1 (0.82), SEC22B (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: voltage dependent anion channel 2. This gene encodes a member of the voltage-dependent anion channel pore-forming family of proteins that are considered the main pathway for metabolite diffusion across the mitochondrial outer membrane. The encoded protein is also thought to be involved in the mitochondrial apoptotic pathway via regulation of BCL2-antagonist/killer 1 protein activity. Pseudogenes have been identified on chromosomes …
- **Diseases (Open Targets)**: neurodegenerative disease (0.345); alcohol drinking (0.204); atrial fibrillation (0.175); major depressive disorder (0.143); severe combined immunodeficiency (0.118)
- **Europe PMC papers**: 2914
- **Why important**: VDAC2 is positioned at the junction of the SSR1 and SEC22B branches and is a mitochondrial outer-membrane channel involved in metabolite diffusion and mitochondrial outer-membrane permeabilization. This places it at a biologically plausible interface between mitochondrial metabolism, membrane state, and apoptosis-related signaling. It is also one of the more extensively studied genes in the module, with broad disease literature, although those disease links are not specific evidence for this co-abundance pattern.
- **Conclusion**: Established evidence: VDAC2 supports mitochondrial transport and apoptotic membrane regulation and occupies a connecting position in the module network. Hypothesis: VDAC2 may couple ER membrane organization to mitochondrial stress or survival responses. The module alone cannot determine whether this coupling is causal or merely reflects shared cellular state.

#### ETFA

- **Related proteins** (co-abundance neighbors): SLC25A13 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein subunit alpha. ETFA participates in catalyzing the initial step of the mitochondrial fatty acid beta-oxidation. It shuttles electrons between primary flavoprotein dehydrogenases and the membrane-bound electron transfer flavoprotein ubiquinone oxidoreductase. Defects in electron-transfer-flavoprotein have been implicated in type II glutaricaciduria in which multiple acyl-CoA dehydrogenase deficiencies result in l…
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.834); glutaric aciduria (0.756); hereditary disease (0.469); multiple acyl-CoA dehydrogenase deficiency, mild type (0.370); multiple acyl-CoA dehydrogenase deficiency, severe neonatal type (0.370)
- **Europe PMC papers**: 1433
- **Why important**: ETFA forms the metabolic arm of the module through its connection with SLC25A13. Its established role in electron transfer from fatty-acid and other acyl-CoA dehydrogenases to the respiratory chain directly supports a mitochondrial energy-production interpretation. Its liver- and hepatocyte-associated HPA annotations and strong disease associations with multiple acyl-CoA dehydrogenase deficiency make it useful for interpreting the module's metabolic dimension.
- **Conclusion**: Established evidence: ETFA participates in mitochondrial electron transfer, fatty-acid beta-oxidation, and amino-acid catabolism and is implicated in multiple acyl-CoA dehydrogenase deficiency. Hypothesis: ETFA may mark a metabolic-demand state that is coordinated with ER trafficking and mitochondrial transport in the shared module. There is no evidence here that the module represents a disease-specific ETFA program.

#### SSR1

- **Related proteins** (co-abundance neighbors): RTN1 (0.82), VDAC2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal sequence receptor subunit 1. The signal sequence receptor (SSR) is a glycosylated endoplasmic reticulum (ER) membrane receptor associated with protein translocation across the ER membrane. The SSR consists of 2 subunits, a 34-kD glycoprotein encoded by this gene and a 22-kD glycoprotein. This gene generates several mRNA species as a result of complex alternative polyadenylation. This gene is unusual in that it utilizes arrays…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.470); diabetes mellitus (0.344); neurodegenerative disease (0.329); Inguinal hernia (0.322); refractive error (0.315)
- **Europe PMC papers**: 938
- **Why important**: SSR1 connects RTN1 with VDAC2 and represents the protein-translocation side of the ER component. Its role as a subunit of the ER signal-sequence receptor supports a connection to cotranslational membrane targeting and protein translocation. Its broad tissue profile and substantial literature make it a useful housekeeping-like structural marker, but its lack of tissue specificity also weakens a tissue-specific interpretation.
- **Conclusion**: Established evidence: SSR1 is an ER membrane receptor subunit involved in protein targeting and translocation and occupies a bridging position between the ER and mitochondrial branches. Hypothesis: it may indicate increased coordination between ER protein handling and mitochondrial homeostasis. The data do not establish that SSR1 is specifically regulated by the ovary-skin shared program.

#### RTN1

- **Related proteins** (co-abundance neighbors): SSR1 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: reticulon 1. This gene belongs to the family of reticulon encoding genes. Reticulons are associated with the endoplasmic reticulum, and are involved in neuroendocrine secretion or in membrane trafficking in neuroendocrine cells. This gene is considered to be a specific marker for neurological diseases and cancer, and is a potential molecular target for therapy. Alternative splicing results in multiple transcri…
- **Diseases (Open Targets)**: neurodegenerative disease (0.464); major depressive disorder (0.258); atrial fibrillation (0.258); urinary bladder disorder (0.256); laryngeal carcinoma (0.223)
- **Europe PMC papers**: 1104
- **Why important**: RTN1 is the ER-organization endpoint connected to SSR1 and adds a distinct cellular context to the module. Its established roles include ER tubular-network formation and membrane organization, with additional annotations in neuronal development and neuroendocrine secretion. Its brain-enriched tissue profile and monocyte or myeloid dendritic-cell group enrichment make it important for detecting possible cell-composition or context effects, while its disease literature is substantial.
- **Conclusion**: Established evidence: RTN1 contributes to ER membrane architecture and has cell-type and tissue patterns that differ from the ovary-skin comparison. Hypothesis: RTN1 may report a shared ER-structural state or a minority cell population that helps generate the observed covariance. Because its HPA protein detection is absent in both listed tissues, it should not be treated as direct proof of an active ovary-skin protein mechanism.

## Module 6

**Tissue pair**: ovary and skin  
**Genes (8)**: PSMC6, PSMC4, PSMC2, PSMD13, CCT5, CCT3, CCT7, CCT8

### Function

The module is best interpreted as a conserved intracellular proteostasis module with two coordinated components: the chaperonin-containing T-complex and the proteasome regulatory particle. The globally corrected GO/KEGG evidence supports ATP-dependent protein folding, protein stabilization, intracellular complex activity, and proteasome-mediated ubiquitin-dependent protein catabolism (GO:CC chaperonin-containing T-complex; q_global = 7.93e-07), (GO:CC proteasome regulatory particle; q_global = 2.82e-06), (GO:CC intracellular protein-containing complex; q_global = 2.39e-05), (GO:MF ATP hydrolysis activity; q_global = 3.43e-05), (GO:MF proteasome-activating activity; q_global = 0.00012), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.000143), (KEGG Proteasome - Homo sapiens (human); q_global = 0.000186), (GO:CC protein folding chaperone complex; q_global = 0.000294), (GO:CC proteasome complex; q_global = 0.000445), (GO:MF protein folding chaperone; q_global = 0.000879), (GO:MF unfolded protein binding; q_global = 0.00275), (GO:BP positive regulation of proteasomal protein catabolic process; q_global = 0.0304), (GO:BP proteasome-mediated ubiquitin-dependent protein catabolic process; q_global = 0.0305), (GO:BP protein stabilization; q_global = 0.0336), (GO:BP protein folding; q_global = 0.0384). The CCT component is also associated with RNA and telomerase-RNA localization to the Cajal body and with telomere maintenance (GO:BP regulation of telomerase RNA localization to Cajal body; q_global = 7.93e-07), (GO:BP RNA localization to Cajal body; q_global = 2.82e-06), (GO:BP telomerase RNA localization to Cajal body; q_global = 2.82e-06), (GO:BP telomerase RNA localization; q_global = 2.82e-06), (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 1.31e-05), (GO:BP regulation of telomere maintenance via telomerase; q_global = 7.74e-05), (GO:BP telomere maintenance via telomerase; q_global = 0.000238), (GO:BP regulation of telomere maintenance; q_global = 0.00246), (GO:BP telomere maintenance; q_global = 0.00816), (GO:BP telomere organization; q_global = 0.0088), (GO:BP RNA localization; q_global = 0.0495). Those annotations are biologically plausible functions of the CCT-containing proteins, but the enrichment does not show that this module specifically controls telomerase in ovary or skin. Fertilization and sperm-related terms are also globally enriched (GO:BP binding of sperm to zona pellucida; q_global = 6.7e-06), (GO:BP sperm-egg recognition; q_global = 1.31e-05), (GO:BP single fertilization; q_global = 0.00054), (GO:BP fertilization; q_global = 0.00152), (GO:BP sexual reproduction; q_global = 0.0192), but they should be interpreted cautiously because the same CCT genes have broad intracellular chaperone roles and the HPA profile includes germ-cell-enhanced expression. Overall, the strongest interpretation is coordinated folding and degradation of proteins, with possible links to nuclear RNA handling and cell-state maintenance.

**Cell composition.** The module is not composed of plasma proteins or secreted proteins: HPA reports no secreted genes. It is also not blood-cell enriched, since all genes have low immune-cell specificity. All genes have low tissue specificity, and the proteins are detected in ovary and skin, supporting a broadly expressed intracellular program rather than a tissue-specific secretory signature. HPA nevertheless reports cell-type-enhanced expression for several genes in late primary spermatocytes, early or late spermatids, syncytiotrophoblasts, oocytes, and esophageal apical cells. Therefore, the shared module may reflect a conserved housekeeping or proteostasis program present in multiple cell types, while the reproductive-cell annotations could partly reflect cellular composition or state. The data do not support explaining this module as blood contamination.

**GO/KEGG enrichment**: 72 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chaperonin-containing T-complex | 7.93e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 7.93e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 7.93e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:CC proteasome regulatory particle | 2.82e-06 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:CC proteasome accessory complex | 2.82e-06 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:BP RNA localization to Cajal body | 2.82e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 2.82e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 2.82e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 2.82e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 2.82e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 2.82e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 2.82e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 2.82e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 2.82e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP binding of sperm to zona pellucida | 6.7e-06 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING provides strong within-component support. CCT3, CCT5, CCT7, and CCT8 form a densely connected CCT group, with the corresponding chaperonin family, T-complex, ATP-dependent folding, and cellular proteostasis annotations (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 8.8e-07), (STRING Component Chaperonin-containing T-complex; within-query FDR = 2.09e-06), (STRING COMPARTMENTS Chaperonin-containing T-complex; within-query FDR = 2.26e-06), (STRING InterPro Chaperonin TCP-1, conserved site; within-query FDR = 3.5e-06), (STRING InterPro Chaperonin Cpn60/GroEL/TCP-1 family; within-query FDR = 3.5e-06), (STRING InterPro Chaperone tailless complex polypeptide 1 (TCP-1); within-query FDR = 3.5e-06), (STRING InterPro GroEL-like apical domain superfamily; within-query FDR = 3.5e-06), (STRING InterPro TCP-1-like chaperonin intermediate domain superfamily; within-query FDR = 3.5e-06), (STRING InterPro GroEL-like equatorial domain superfamily; within-query FDR = 3.5e-06), (STRING RCTM Folding of actin by CCT/TriC; within-query FDR = 5.35e-06), (STRING NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis; within-query FDR = 6.66e-06). PSMC2, PSMC4, PSMC6, and PSMD13 form a connected proteasome-regulatory group, with STRING support for the proteasome regulatory particle (STRING Component Proteasome regulatory particle; within-query FDR = 2.09e-06), (STRING COMPARTMENTS Proteasome regulatory particle; within-query FDR = 2.26e-06). The bridge between the groups is the STRING relationship between CCT8 and PSMC2, so the module is not merely two unrelated gene sets. The STRING sperm-proteome association (STRING PMID (2019) Proteomic analysis reveals dysregulated cell signaling in ejaculated spermatozoa from infertile men.; within-query FDR = 3.26e-07) is supplementary and may reflect the germ-cell-enhanced HPA pattern, but it is not global enrichment evidence. hu.MAP independently places the four CCT genes in multiple CCT-containing complexes (hu.MAP huMAP3_07938.1), (hu.MAP huMAP3_06559.1), (hu.MAP huMAP3_09191.1), (hu.MAP huMAP3_10656.1), (hu.MAP huMAP3_14584.1), (hu.MAP huMAP3_01951.1), and places the four proteasome genes in multiple proteasome complexes (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1). These are established physical or complex-level relationships, meaning that much of the module's internal structure recapitulates known molecular machinery.

**STRING interactions (score >= 0.7)**: 13 of 28 gene pairs: CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999); CCT8–PSMC2 (0.733); PSMC2–PSMC4 (0.999); PSMC2–PSMC6 (0.999); PSMC2–PSMD13 (0.999); PSMC4–PSMC6 (0.999); PSMC4–PSMD13 (0.999); PSMC6–PSMD13 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: PMID (2019) Proteomic analysis reveals dysregulated cell signaling in ejaculated spermatozoa from infertile men. (FDR = 3.26e-07, 7 genes); Pfam TCP-1/cpn60 chaperonin family (FDR = 8.8e-07, 4 genes); Component Chaperonin-containing T-complex (FDR = 2.09e-06, 4 genes); Component Proteasome regulatory particle (FDR = 2.09e-06, 4 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 2.26e-06, 4 genes); COMPARTMENTS Proteasome regulatory particle (FDR = 2.26e-06, 4 genes); Function ATP hydrolysis activity (FDR = 2.42e-06, 7 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 3.5e-06, 4 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 3.5e-06, 4 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 3.5e-06, 4 genes); InterPro GroEL-like apical domain superfamily (FDR = 3.5e-06, 4 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 3.5e-06, 4 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 3.5e-06, 4 genes); RCTM Folding of actin by CCT/TriC (FDR = 5.35e-06, 4 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis (FDR = 6.66e-06, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_05064.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/31); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_09656.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/64); huMAP3_13725.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/69); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8)

### Novelty

The module as a whole should not be claimed as a newly discovered protein complex or pathway. Its two major substructures are already well established by STRING, hu.MAP, GO, KEGG, and the gene descriptions: one is a CCT chaperonin assembly and the other is a proteasome regulatory assembly. The potentially novel aspect is the conserved co-abundance of these components across ovary and skin, particularly their organization into one module with a CCT-to-proteasome connection. That observation may be a useful tissue-pair or dataset-level finding, but the supplied evidence alone does not establish that the cross-component relationship is mechanistically direct, tissue-specific, or previously unreported. Absence of a complete matching module in STRING or hu.MAP would not by itself prove novelty.

**Hypothesis.** Hypothesis: in ovary and skin, a shared cellular state couples CCT-mediated folding of newly synthesized or stress-sensitive proteins to proteasomal removal of damaged, misfolded, or otherwise regulated proteins. The CCT and proteasome assemblies could therefore rise and fall together as a proteostasis program, with CCT8 and PSMC2 representing a possible co-abundance bridge. The CCT component may additionally support nuclear RNA and telomerase-RNA handling, whereas the proteasome component may regulate the stability of proteins involved in stress responses and cell-state maintenance. This is a mechanistic hypothesis, not a demonstrated physical pathway; it should be tested by independent abundance replication, cell-type-resolved analysis, perturbation of CCT or proteasome activity, and measurement of folding, degradation, and nuclear RNA phenotypes.

### Important genes

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT8 (0.92), CCT7 (0.87), PSMC2 (0.86), CCT3 (0.84), PSMC4 (0.83); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in ovary, skin
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is the highest-connectivity module member and links several CCT genes with proteasome-related neighbors. It is a subunit of the ATP-dependent CCT chaperonin that folds proteins including actin and tubulin. It appears across many globally corrected folding, protein-stabilization, Cajal-body, telomere-maintenance, and intracellular-complex terms, and across the STRING CCT and proteostasis annotations (GO:CC chaperonin-containing T-complex; q_global = 7.93e-07), (GO:BP regulation of telomerase RNA localization to Cajal body; q_global = 7.93e-07), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.000143), (GO:CC protein folding chaperone complex; q_global = 0.000294), (GO:MF unfolded protein binding; q_global = 0.00275), (GO:BP protein stabilization; q_global = 0.0336), (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 8.8e-07), (STRING Component Chaperonin-containing T-complex; within-query FDR = 2.09e-06), (STRING RCTM Folding of actin by CCT/TriC; within-query FDR = 5.35e-06), (STRING NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis; within-query FDR = 6.66e-06). HPA detects it in ovary and skin and reports enhancement in late primary spermatocytes. Its substantial literature and disease associations make it a well-characterized anchor rather than a speculative driver.
- **Conclusion**: Established evidence supports CCT5 as a central component of the module's chaperone arm and as a strong marker of intracellular proteostasis. It is reasonable to hypothesize that its central network position helps couple folding capacity to the proteasome arm, but the co-abundance network does not prove that CCT5 directly regulates that coupling.

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT5 (0.92), CCT7 (0.85), CCT3 (0.84); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999), PSMC2 (0.733)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in ovary, skin
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is a CCT subunit with strong connectivity to the other CCT genes and is the only explicitly represented bridge from the CCT group to PSMC2 in STRING. It participates in the globally corrected chaperonin, protein-folding, Cajal-body, telomere, and zona-pellucida-related annotations (GO:CC chaperonin-containing T-complex; q_global = 7.93e-07), (GO:BP regulation of telomerase RNA localization to Cajal body; q_global = 7.93e-07), (GO:BP binding of sperm to zona pellucida; q_global = 6.7e-06), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.000143), (GO:CC protein folding chaperone complex; q_global = 0.000294), (GO:MF unfolded protein binding; q_global = 0.00275), (GO:CC zona pellucida receptor complex; q_global = 0.0155), and in the STRING CCT and proteostasis evidence (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 8.8e-07), (STRING Component Chaperonin-containing T-complex; within-query FDR = 2.09e-06), (STRING RCTM Folding of actin by CCT/TriC; within-query FDR = 5.35e-06), (STRING NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis; within-query FDR = 6.66e-06). HPA detects it in ovary and skin and reports enhancement in oocytes. Its broad literature and cancer-related Open Targets associations indicate that it is biologically well studied.
- **Conclusion**: Established evidence supports CCT8 as a core chaperonin component and a plausible network interface between folding and proteasome-related abundance. The oocyte annotation is compatible with relevance to ovary, but does not establish a reproductive-specific function in this shared module.

#### PSMC2

- **Related proteins** (co-abundance neighbors): CCT5 (0.86), PSMC4 (0.83), PSMC6 (0.80), PSMD13 (0.80); STRING partners: CCT8 (0.733), PSMC4 (0.999), PSMC6 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in ovary, skin
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is the most connected member of the proteasome arm and connects to CCT5 as well as the other proteasome genes. It encodes an ATPase subunit of the proteasome regulatory particle. It contributes to globally corrected proteasome, ATP-dependent activity, and ubiquitin-dependent protein-catabolism terms (GO:CC proteasome regulatory particle; q_global = 2.82e-06), (GO:MF ATP hydrolysis activity; q_global = 3.43e-05), (GO:MF proteasome-activating activity; q_global = 0.00012), (KEGG Proteasome - Homo sapiens (human); q_global = 0.000186), (GO:CC proteasome regulatory particle, base subcomplex; q_global = 0.000351), (GO:CC proteasome complex; q_global = 0.000445), (GO:BP positive regulation of proteasomal protein catabolic process; q_global = 0.0304), (GO:BP proteasome-mediated ubiquitin-dependent protein catabolic process; q_global = 0.0305), and to STRING and hu.MAP proteasome evidence (STRING Component Proteasome regulatory particle; within-query FDR = 2.09e-06), (STRING COMPARTMENTS Proteasome regulatory particle; within-query FDR = 2.26e-06), (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1). HPA detects it in ovary and skin, with syncytiotrophoblast enhancement. Its substantial literature and disease associations involving plasma-cell neoplasia and amyloidosis further support its established functional importance.
- **Conclusion**: Established evidence identifies PSMC2 as a central proteasome-regulatory component and a strong marker of the module's degradation arm. Its connection to CCT5 supports coordinated proteostasis as an interpretation, but does not establish directionality or direct biochemical coupling.

#### PSMC4

- **Related proteins** (co-abundance neighbors): CCT5 (0.83), PSMC2 (0.83); STRING partners: PSMC2 (0.999), PSMC6 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in ovary, skin
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 4. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.603); mantle cell lymphoma (0.542); neoplasm (0.519); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1065
- **Why important**: PSMC4 is an ATPase subunit of the proteasome regulatory particle and is connected to the other proteasome members in STRING and hu.MAP. It contributes to the globally corrected proteasome, ATP-dependent activity, and ubiquitin-dependent catabolism terms (GO:CC proteasome regulatory particle; q_global = 2.82e-06), (GO:MF ATP hydrolysis activity; q_global = 3.43e-05), (KEGG Proteasome - Homo sapiens (human); q_global = 0.000186), (GO:CC proteasome complex; q_global = 0.000445), (GO:BP positive regulation of proteasomal protein catabolic process; q_global = 0.0304), (GO:BP proteasome-mediated ubiquitin-dependent protein catabolic process; q_global = 0.0305), and to proteasome and sperm-proteome supplementary evidence (STRING PMID (2019) Proteomic analysis reveals dysregulated cell signaling in ejaculated spermatozoa from infertile men.; within-query FDR = 3.26e-07), (STRING Component Proteasome regulatory particle; within-query FDR = 2.09e-06), (STRING COMPARTMENTS Proteasome regulatory particle; within-query FDR = 2.26e-06), (STRING Function ATP hydrolysis activity; within-query FDR = 2.42e-06). HPA detects it in ovary and skin and reports enhancement in germ-cell and placental-related cell types. It has substantial literature and disease associations overlapping the proteasome arm.
- **Conclusion**: Established evidence supports PSMC4 as a representative and functionally important member of the proteasome arm. Its germ-cell-enhanced profile may contribute to the reproductive annotations, but cannot by itself establish that the module is reproductive-specific.

#### PSMD13

- **Related proteins** (co-abundance neighbors): PSMC2 (0.80); STRING partners: PSMC2 (0.999), PSMC4 (0.999), PSMC6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 is the non-ATPase member of the selected proteasome group and helps show that the module includes regulatory architecture rather than only ATPase subunits. It contributes to globally corrected proteasome-complex and ubiquitin-dependent catabolism terms (GO:CC proteasome regulatory particle; q_global = 2.82e-06), (KEGG Proteasome - Homo sapiens (human); q_global = 0.000186), (GO:CC proteasome complex; q_global = 0.000445), (GO:BP sexual reproduction; q_global = 0.0192), (GO:BP proteasome-mediated ubiquitin-dependent protein catabolic process; q_global = 0.0305), and is present in STRING and hu.MAP proteasome relationships (STRING Component Proteasome regulatory particle; within-query FDR = 2.09e-06), (STRING COMPARTMENTS Proteasome regulatory particle; within-query FDR = 2.26e-06), (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1). HPA detects it in skin, but not ovary, making it a useful cautionary example that module-level conservation does not require identical protein detection for every member in each tissue. Its literature and disease associations support established relevance to proteostasis.
- **Conclusion**: Established evidence supports PSMD13 as a proteasome-regulatory component that strengthens the degradation-side interpretation. The tissue-detection asymmetry suggests that its contribution may vary between tissues, so it should not be treated as proof of a uniform ovary-skin mechanism.
