# Conserved co-abundance modules: breast and cell line

## Module 0

**Tissue pair**: breast and cell line  
**Genes (20)**: PPP2R2D, ACSS2, ANKRD50, ATG4A, B3GALT6, DEPDC5, DMXL1, EIF3L, EMILIN1, GSTCD, PHKB, MON1B, PCGF1, ARHGAP25, RYR2, SLC35F6, SIK2, TUBB8, XRCC6, ZNF277

### Function

This module does not support a single, established biological function. No GO/KEGG term passed global correction, and there was no supplementary STRING functional enrichment. The gene annotations nevertheless suggest several weakly connected biological themes: nuclear regulation and chromatin control through PCGF1 and ZNF277; nutrient sensing, autophagy, and growth control through DEPDC5, PPP2R2D, and ATG4A; cellular metabolism through ACSS2 and PHKB; calcium handling through RYR2; and vesicle, cytoskeletal, extracellular-matrix, and DNA-repair functions contributed by other members. These are annotations of individual genes, not significantly enriched module-level processes. The network is therefore better interpreted as a co-abundance pattern spanning multiple cellular programs than as a canonical pathway module.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only EMILIN1 is annotated as secreted to the extracellular matrix. It is also not strongly blood-cell specific. Most genes have low tissue specificity, while many show cell-type-enhanced expression across diverse cell types; only a subset has immune-cell enhancement, and several are not detected in immune cells. Enrichment of neutrophil-related cell types and representation of stromal, muscle, endocrine, reproductive, and epithelial cell types suggest that sample composition or shared cell states could contribute to the breast–cell-line association. Breast protein detection is present for many members, whereas the cell-line comparison has no matching HPA tissue dataset, so the HPA evidence does not establish that this is a breast-specific program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The co-abundance graph should not be treated as a physical interaction network. STRING supports only the PPP2R2D–RYR2 relationship among the module members, and there is no STRING functional enrichment. No hu.MAP complex contains multiple module members. Thus, most module edges are not already supported as physical protein interactions or membership in a known multiprotein complex. The supported PPP2R2D–RYR2 relationship is biologically interesting because it connects phosphatase regulation with calcium-channel biology, but it is insufficient to define the whole module.

**STRING interactions (score >= 0.7)**: 1 of 190 gene pairs: PPP2R2D–RYR2 (0.9)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a new co-abundance association in this breast–cell-line comparison, but novelty is not established by the current evidence. Its limited overlap with STRING and hu.MAP argues against simple recovery of a well-known protein complex, while the absence of globally significant GO/KEGG enrichment and the heterogeneous annotations argue against a clearly recognized pathway module. The pattern could instead reflect correlated cell composition, a shared physiological or stress state, or technical and model-specific expression structure. Independent cohorts, preservation testing, perturbation experiments, and comparison with published co-expression modules would be needed before calling it a novel biological mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state rather than a single biochemical pathway. A plausible model is that a broadly expressed nuclear regulatory background, centred on PCGF1, co-varies with nutrient and autophagy control through DEPDC5 and PPP2R2D, while cell-type-specific components such as RYR2, ACSS2, PHKB, EMILIN1, and ARHGAP25 contribute according to the mixture of muscle, stromal, immune, endocrine, and epithelial cells present in the samples. The observed PPP2R2D–RYR2 connection could represent coordinated regulation of phosphorylation and calcium handling, but this mechanistic link remains a hypothesis and is not demonstrated by the enrichment results.

### Important genes

#### PCGF1

- **Related proteins** (co-abundance neighbors): ZNF277 (0.91), PPP2R2D (0.89), EIF3L (0.87), XRCC6 (0.85), ACSS2 (0.84), PHKB (0.84), MON1B (0.83), GSTCD (0.83), DMXL1 (0.82), TUBB8 (0.82), ANKRD50 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polycomb group ring finger 1. PCGF1 is a mammalian homolog of the Drosophila polycomb group genes, which act as transcriptional repressors to regulate anterior-posterior patterning in early embryonic development (Nunes et al., 2001 [PubMed 11287196]). See also PCGF2 (MIM 600346).[supplied by OMIM, Aug 2008].
- **Diseases (Open Targets)**: neoplasm (0.091); central nervous system cancer (0.085); glioma (0.085); early-onset non-syndromic cataract (0.078); colorectal cancer (0.077)
- **Europe PMC papers**: 623
- **Why important**: PCGF1 is the strongest network hub in the module and connects genes spanning nuclear regulation, metabolism, trafficking, DNA repair, and phosphatase-related functions. Its annotated role as a polycomb-group transcriptional repressor and its nucleoplasmic localization make it a plausible organizing marker for a shared transcriptional or chromatin state. It has substantial literature support and reported associations with neoplastic disease, although no module-level enrichment or physical interaction evidence supports a specific PCGF1-centred complex here.
- **Conclusion**: Established evidence supports PCGF1 as a central co-abundance connector and a nuclear transcriptional regulator. It is a reasonable candidate driver or marker of the module, but whether it mechanistically controls the other members is unresolved.

#### DEPDC5

- **Related proteins** (co-abundance neighbors): EMILIN1 (0.85), ANKRD50 (0.84), SLC35F6 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEP domain containing 5, GATOR1 subcomplex subunit. This gene encodes a member of the IML1 family of proteins involved in G-protein signaling pathways. The mechanistic target of rapamycin complex 1 (mTORC1) pathway regulates cell growth by sensing the availability of nutrients. The protein encoded by this gene is a component of the GATOR1 (GAP activity toward Rags) complex which inhibits the amino acid-sensing branch of the mTORC1 pathway. Mutation…
- **Diseases (Open Targets)**: familial focal epilepsy with variable foci (0.801); epilepsy, familial focal, with variable foci 1 (0.768); developmental and epileptic encephalopathy 111 (0.565); hereditary disease (0.549); Seizure (0.534)
- **Europe PMC papers**: 1366
- **Why important**: DEPDC5 links the module to nutrient sensing through the GATOR1 complex and negative regulation of mTORC1, with additional annotation for amino-acid starvation responses and autophagy. It connects EMILIN1, ANKRD50, and SLC35F6 within the co-abundance graph and has strong disease relevance through familial focal epilepsy and related disorders. Its literature volume is substantial relative to many other module members.
- **Conclusion**: Established evidence supports DEPDC5 as a regulator of amino-acid-sensitive mTORC1 signalling and autophagy. Its participation in this module may indicate a nutrient or growth-state component, but the module data do not demonstrate that mTORC1 activity is the cause of the co-abundance pattern.

#### RYR2

- **Related proteins** (co-abundance neighbors): ARHGAP25 (0.86), DMXL1 (0.86); STRING partners: PPP2R2D (0.9)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ryanodine receptor 2. This gene encodes a ryanodine receptor found in cardiac muscle sarcoplasmic reticulum. The encoded protein is one of the components of a calcium channel, composed of a tetramer of the ryanodine receptor proteins and a tetramer of FK506 binding protein 1B proteins, that supplies calcium to cardiac muscle. Mutations in this gene are associated with stress-induced polymorphic ventricular tachycardia …
- **Diseases (Open Targets)**: catecholaminergic polymorphic ventricular tachycardia 1 (0.833); ventricular arrhythmias due to cardiac ryanodine receptor calcium release deficiency syndrome (0.739); catecholaminergic polymorphic ventricular tachycardia (0.731); arrhythmogenic right ventricular cardiomyopathy (0.662); Abnormality of the cardiovascular system (0.550)
- **Europe PMC papers**: 10446
- **Why important**: RYR2 is tissue-enriched in heart muscle and cell-type-enriched in cardiomyocytes, making it a distinctive tissue-associated member rather than a broadly expressed housekeeping gene. It encodes a cardiac calcium-release channel with extensive literature and strong associations with inherited ventricular arrhythmia syndromes. It also participates in the only STRING-supported relationship within the module, with PPP2R2D.
- **Conclusion**: Established evidence supports RYR2 as a cardiac calcium-channel gene and supports its known relationship with PPP2R2D in STRING. Its presence may reflect a calcium-handling or cell-composition signal, but it does not establish a cardiac mechanism in breast or cell-line samples.

#### PPP2R2D

- **Related proteins** (co-abundance neighbors): PCGF1 (0.89), ATG4A (0.81); STRING partners: RYR2 (0.9)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase 2 regulatory subunit Bdelta. Predicted to enable protein phosphatase regulator activity. Predicted to be involved in exit from mitosis and peptidyl-serine dephosphorylation. Predicted to be part of protein phosphatase type 2A complex. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: intelligence (0.392); mathematical ability (0.392); myocardial ischemia (0.307); autism spectrum disorder (0.286); attention deficit-hyperactivity disorder (0.286)
- **Europe PMC papers**: 367
- **Why important**: PPP2R2D connects PCGF1 and ATG4A in the co-abundance graph and is the partner of RYR2 in the only STRING-supported interaction. Its annotation places it within protein phosphatase type 2A regulation, mitotic exit, chromosome segregation, and serine dephosphorylation. This gives it a plausible role at the interface of phosphorylation control, cell-cycle state, and the calcium-related signal represented by RYR2.
- **Conclusion**: Established evidence supports PPP2R2D as a regulatory subunit associated with phosphatase biology and as a known STRING partner of RYR2. A coordinating role in this module is plausible, but the co-abundance data do not show whether the interaction is active or functionally important in these samples.

#### ACSS2

- **Related proteins** (co-abundance neighbors): PCGF1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase short chain family member 2. This gene encodes a cytosolic enzyme that catalyzes the activation of acetate for use in lipid synthesis and energy generation. The protein acts as a monomer and produces acetyl-CoA from acetate in a reaction that requires ATP. Expression of this gene is regulated by sterol regulatory element-binding proteins, transcription factors that activate genes required for the synthesis of cholesterol and …
- **Diseases (Open Targets)**: neurodegenerative disease (0.371); orofacial cleft (0.333); autoimmune disorder of central nervous system (0.261); coronary artery disorder (0.152); delusional disorder (0.142)
- **Europe PMC papers**: 2948
- **Why important**: ACSS2 is connected to the module hub PCGF1 and provides a defined metabolic interpretation: activation of acetate to acetyl-CoA for lipid synthesis and energy generation. Its tissue enhancement in skeletal muscle and cell-type enhancement across adipocytes, lactating breast cells, cardiomyocytes, and intestinal secretory cells are consistent with a metabolically responsive component. It also has substantial literature support and disease associations involving neural and cardiovascular phenotypes.
- **Conclusion**: Established evidence supports ACSS2 as an acetate-utilizing metabolic enzyme regulated in the context of lipid and energy metabolism. Its co-abundance with PCGF1 may mark coordination between metabolism and nuclear regulation, but this connection remains inferential rather than demonstrated.

## Module 1

**Tissue pair**: breast and cell line  
**Genes (17)**: A2M, B4GALT1, COBL, CRELD1, DAPP1, ERAP1, FAM199X, KRT14, KRT5, MICU1, SLC16A3, MYH14, NAA35, NEK7, NUBP2, SARM1, SMARCE1

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established pathway-level function from enrichment. The strongest interpretable signal is a sparse network organized around FAM199X, with an epithelial structural component formed by KRT5 and KRT14. KRT5 and KRT14 are basal epithelial keratins that form intermediate-filament structures, while the remaining genes represent diverse processes including actin regulation, glycosylation, lactate transport, antigenic peptide processing, mitochondrial calcium control, chromatin remodeling, and cell-cycle regulation. This heterogeneity argues against assigning the whole module to one established biochemical pathway. The module may instead reflect coordinated abundance associated with epithelial or basal-cell content, cellular state, or a shared sample component.

**Cell composition.** The module is not dominated by secreted or plasma proteins, although A2M and ERAP1 are secreted to blood and B4GALT1 and CRELD1 have intracellular or membrane-associated secretome annotations. Most genes have low or broad tissue specificity, and many are detected in breast tissue. HPA profiles also point toward epithelial and barrier-related populations, including basal and suprabasal keratinocytes, esophageal epithelial cells, ocular epithelial cells, and related tissues. Several genes show enrichment in neutrophils or other blood-associated cell types, and some show immune-cell enrichment. This makes a contribution from blood, infiltrating cells, or shared epithelial cell types plausible, but the HPA evidence does not establish that the module is a blood-cell module. The absence of a matching HPA tissue context for the cell line limits direct comparison between the two systems.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module: the known KRT14-KRT5 interaction. The supplementary STRING HPO signal (STRING HPO Dystrophic toenail; within-query FDR = 0.0487) links KRT14, KRT5, and SMARCE1 with dystrophic toenail, but this is supplementary evidence and is not a globally corrected GO or KEGG result. The lack of additional high-confidence STRING relationships indicates that most module edges are not supported by the queried STRING interaction network. No hu.MAP complex contains multiple module members. Thus, the module contains a validated keratin-pair subnetwork but otherwise appears weakly supported as a known physical complex or interaction network.

**STRING interactions (score >= 0.7)**: 1 of 136 gene pairs: KRT14–KRT5 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: HPO Dystrophic toenail (FDR = 0.0487, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be described as a new biological pathway or a newly discovered complex. Its main evidence is co-abundance rather than established physical interaction, and the only clearly known internal interaction is KRT5-KRT14. FAM199X is a central network node in this module but has no listed STRING partners or hu.MAP complex membership, making its role potentially interesting but currently unvalidated. The absence of STRING or hu.MAP support alone does not prove novelty; the module could reflect tissue composition, shared regulation, indirect co-expression, or technical and sampling effects. A genuine novel association would require replication, adjustment for cell composition, and orthogonal molecular validation.

**Hypothesis.** Hypothesis: this shared breast-cell-line module reflects a composite epithelial-state signal rather than a single pathway. In this model, KRT5 and KRT14 report basal epithelial cytoskeletal abundance, while FAM199X acts as a co-abundance hub linking that epithelial signal to diverse cellular programs. B4GALT1 could connect the signal to Golgi glycosylation and membrane protein processing, and ERAP1 could connect it to antigenic peptide processing and extracellular immune-related biology. The apparent association with blood-cell-enriched genes may reflect mixed cellular composition or a shared stress or inflammatory state. This hypothesis is not established by the enrichment analysis and should be tested by cell-composition correction, independent cohorts, protein-level measurements, and perturbation of the proposed hub or epithelial component.

### Important genes

#### FAM199X

- **Related proteins** (co-abundance neighbors): COBL (0.98), SARM1 (0.88), MYH14 (0.87), SLC16A3 (0.86), ERAP1 (0.85), MICU1 (0.85), CRELD1 (0.85), SMARCE1 (0.84), NAA35 (0.84), KRT14 (0.82), NUBP2 (0.81), A2M (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: family with sequence similarity 199, X-linked
- **Diseases (Open Targets)**: neurodegenerative disease (0.516); 15q11q13 microduplication syndrome (0.118); meningococcal infection (0.002); type 1 diabetes mellitus (0.002); ovarian serous cystadenocarcinoma (0.000)
- **Europe PMC papers**: 1553
- **Why important**: FAM199X has the strongest network position and connects many otherwise weakly connected genes, yet it has no listed STRING partners, no hu.MAP complex membership, and no globally significant GO or KEGG annotation. Its sequence-similarity-family annotation and broad HPA profile provide little mechanistic resolution, while its substantial literature volume and disease-linked Open Targets associations make it a useful candidate for follow-up. It is important primarily because of network position and uncertainty, not because its molecular function is established.
- **Conclusion**: Established evidence supports FAM199X as the module's central co-abundance node and places it at the Golgi apparatus in the HPA record. Its causal role, molecular partners, and contribution to the breast-cell-line association remain unknown. The hypothesis that it coordinates epithelial, metabolic, or stress-related programs requires direct interaction and perturbation experiments.

#### KRT5

- **Related proteins** (co-abundance neighbors): KRT14 (0.80); STRING partners: KRT14 (0.999)
- **HPA**: Group enriched; Group enriched; blood Immune cell enriched; location Intermediate filaments; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 5. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the basal layer of the epidermis with family member KRT14. Mutations in t…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 2C, localized (0.768); epidermolysis bullosa simplex 2A, generalized severe (0.761); epidermolysis bullosa simplex 2B, generalized intermediate (0.761); epidermolysis bullosa simplex 2F, with mottled pigmentation (0.729); Dowling-Degos disease 1 (0.697)
- **Europe PMC papers**: 7044
- **Why important**: KRT5 is a high-confidence partner of KRT14 in STRING and is positioned in the module's epithelial branch. Its HPA profile is enriched in basal and suprabasal epithelial populations and in tissues containing stratified epithelium. Its established function is intermediate-filament polymerization and epithelial structural support, and it has strong disease and literature support through epidermolysis bullosa and related epithelial disorders.
- **Conclusion**: KRT5 is an established epithelial structural marker and a credible biological anchor for the module. The data support interpreting the KRT5 signal as epithelial or basal-cell abundance, but they do not show that KRT5 regulates the other module genes or that the entire module is a keratin pathway.

#### KRT14

- **Related proteins** (co-abundance neighbors): FAM199X (0.82), KRT5 (0.80); STRING partners: KRT5 (0.999)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Intermediate filaments; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 14. This gene encodes a member of the keratin family, the most diverse group of intermediate filaments. This gene product, a type I keratin, is usually found as a heterotetramer with two keratin 5 molecules, a type II keratin. Together they form the cytoskeleton of epithelial cells. Mutations in the genes for these keratins are associated with epidermolysis bullosa simplex. At least one pseudogene has…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 1A, generalized severe (0.823); epidermolysis bullosa simplex 1C, localized (0.818); epidermolysis bullosa simplex 1B, generalized intermediate (0.802); epidermolysis bullosa simplex 1D, generalized, intermediate or severe, autosomal recessive (0.759); Naegeli-Franceschetti-Jadassohn syndrome (0.759)
- **Europe PMC papers**: 6348
- **Why important**: KRT14 forms the known high-confidence KRT5-KRT14 keratin pair and has tissue-enriched and cell-type-enriched HPA profiles for skin and basal epithelial populations. Its annotated roles include epithelial morphogenesis, epidermal development, keratinocyte differentiation, and intermediate-filament organization. It has extensive literature and strong disease associations with epidermolysis bullosa simplex. It also contributes to the only supplementary STRING enrichment signal (STRING HPO Dystrophic toenail; within-query FDR = 0.0487).
- **Conclusion**: KRT14 provides the clearest established functional interpretation of part of the module: basal epithelial cytoskeletal organization. Its presence supports an epithelial-cell or epithelial-state explanation, but the supplementary HPO association (STRING HPO Dystrophic toenail; within-query FDR = 0.0487) is not global enrichment evidence and does not establish a module-wide disease mechanism.

#### B4GALT1

- **Related proteins** (co-abundance neighbors): DAPP1 (0.93); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: beta-1,4-galactosyltransferase 1. This gene is one of seven beta-1,4-galactosyltransferase (beta4GalT) genes. They encode type II membrane-bound glycoproteins that appear to have exclusive specificity for the donor substrate UDP-galactose; all transfer galactose in a beta1,4 linkage to similar acceptor sugars: GlcNAc, Glc, and Xyl. Each beta4GalT has a distinct function in the biosynthesis of different glycoconjugates and sacchari…
- **Diseases (Open Targets)**: B4GALT1-congenital disorder of glycosylation (0.755); neurodegenerative disease (0.546); congenital disorder of glycosylation type II (0.526); gout (0.442); combined low LDL and fibrinogen (0.379)
- **Europe PMC papers**: 1618
- **Why important**: B4GALT1 links to DAPP1 in the co-abundance graph and encodes a Golgi type membrane glycosyltransferase involved in glycoconjugate and N-linked glycosylation processes. Its HPA annotations include breast detection, lactating-cell and neutrophil cell-type enhancement, immune-cell enrichment, and intracellular or membrane-associated secretion. It has substantial literature and disease associations involving congenital glycosylation disorders and circulating fibrinogen.
- **Conclusion**: B4GALT1 is an established glycosylation enzyme that could explain a membrane-processing or epithelial-secretory aspect of the module. The current network does not demonstrate a physical link between B4GALT1 and the keratin pair, so any connection to the epithelial signal remains a hypothesis.

#### ERAP1

- **Related proteins** (co-abundance neighbors): FAM199X (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: endoplasmic reticulum aminopeptidase 1. The protein encoded by this gene is an aminopeptidase involved in trimming HLA class I-binding precursors so that they can be presented on MHC class I molecules. The encoded protein acts as a monomer or as a heterodimer with ERAP2. This protein may also be involved in blood pressure regulation by inactivation of angiotensin II. Three transcript variants encoding two different isoforms have been fo…
- **Diseases (Open Targets)**: psoriasis (0.513); ankylosing spondylitis (0.457); hypertensive disorder (0.437); anterior uveitis (0.411); iridocyclitis (0.401)
- **Europe PMC papers**: 2233
- **Why important**: ERAP1 is connected to the central FAM199X node and has a defined role in trimming peptides for HLA class I antigen presentation. It is secreted to blood according to HPA, is detected in breast tissue, and has disease associations involving inflammatory and immune-mediated conditions. Its literature volume is substantial, and its function provides a biologically meaningful bridge between intracellular protein processing and immune-related sample composition.
- **Conclusion**: ERAP1 supports the possibility that immune context or antigen-processing state contributes to the shared co-abundance pattern. Its inclusion does not prove immune infiltration or a functional interaction with FAM199X, and the module lacks globally significant enrichment for antigen presentation.

## Module 2

**Tissue pair**: breast and cell line  
**Genes (29)**: ABHD17C, ABCA3, ARHGEF10L, CDH11, CTSK, COMTD1, DDX55, DOCK4, FCGRT, GGNBP2, ITGAL, KIAA0513, RPS6KB1, MMP1, MYPOP, NEK1, NEFM, PGAP6, PPM1L, SLC60A2, SRPX, STC1, GTF3C1, TLR2, TMEM175, TOB1, UBE3B, VAV1, ZNF668

### Function

The strongest functional interpretation is an inflammatory, leukocyte-interaction and extracellular-matrix-remodeling module. The primary evidence is the globally corrected KEGG rheumatoid arthritis term (KEGG Rheumatoid arthritis - Homo sapiens (human); q_global = 0.0188), supported by the shared presence of TLR2, ITGAL, CTSK and MMP1. TLR2 and ITGAL indicate innate-immune recognition and leukocyte adhesion, while CTSK and MMP1 indicate lysosomal or extracellular proteolysis and matrix disassembly. The term should be interpreted as a pathway-level annotation rather than evidence that the samples represent rheumatoid arthritis. The absence of additional globally corrected GO or KEGG terms does not invalidate the module; it indicates that the remaining functional interpretation is based on gene annotations, network context and supplementary evidence.

**Cell composition.** The module is heterogeneous rather than a coherent breast epithelial program. HPA evidence shows broad representation of low-specificity genes together with tissue- and cell-type-enhanced genes associated with bone marrow, lymphoid tissue, monocytes, neutrophils, fibroblasts and macrophages. Several members are secreted or extracellularly associated, including SRPX, STC1 and MMP1, while CTSK has intracellular and membrane-associated secretome annotation. The immune-cell pattern is particularly notable for TLR2, ITGAL, VAV1, ARHGEF10L and FCGRT, and may reflect leukocyte abundance or shared myeloid cell types in the breast samples rather than a function intrinsic to breast cells. HPA breast protein detection is present for part of the module, whereas the cell-line comparison has no matching HPA tissue evidence. The brain, epithelial, germ-cell and fibroblast annotations further indicate that the module contains broadly distributed or context-dependent genes, not a uniform lineage marker set.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Rheumatoid arthritis - Homo sapiens (human) | 0.0188 | CTSK, ITGAL, MMP1, TLR2 |

### STRING and hu.MAP

STRING provides limited direct support for the module as a unified physical interaction network. The principal high-confidence known interaction is ITGAL with VAV1, connecting leukocyte adhesion to a guanine-nucleotide-exchange signaling protein. This relationship is biologically consistent with immune-cell activation and migration. STRING supplementary enrichment independently recovers the rheumatoid arthritis pathway (STRING KEGG Rheumatoid arthritis; within-query FDR = 0.0023), but it is supplementary and not global enrichment evidence. hu.MAP identifies one low-complexity overlap in complex C1, containing ABHD17C and UBE3B among the module genes. This supports a known complex association for that pair, but the remaining complex members are outside the module and the complex does not explain the immune and matrix-remodeling portion. Most co-abundance links therefore are not supported by the listed STRING or hu.MAP relationships, suggesting that the network is primarily a coordinated abundance pattern rather than a catalog of established physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 406 gene pairs: ITGAL–VAV1 (0.948)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Rheumatoid arthritis (FDR = 0.0023, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08668.1 (ABHD17C, UBE3B; 2/15)

### Novelty

This module should not be called a newly discovered biological pathway. Its core interpretation combines well-established biology: TLR2-mediated innate immune recognition, ITGAL-dependent leukocyte adhesion, VAV1-mediated immune signaling, CTSK-mediated proteolysis and MMP1-mediated extracellular-matrix breakdown. The limited overlap with STRING and hu.MAP may indicate context-specific co-abundance, indirect regulation, cell-mixture effects or incomplete interaction databases, but database absence alone does not establish novelty. The potentially novel result is the reproducible breast–cell-line co-abundance association of this mixed immune, matrix and cellular-maintenance gene set. That claim requires validation in independent cohorts, cell-composition adjustment, perturbation experiments and comparison with existing co-expression modules.

**Hypothesis.** Hypothesis: the conserved module reflects a shared inflammatory-remodeling state that is driven partly by immune-cell or myeloid-cell representation and partly by matrix-remodeling activity. TLR2 activation may promote leukocyte signaling through ITGAL and VAV1, while CTSK and MMP1 contribute to proteolytic remodeling of collagen-containing extracellular material. SRPX, CDH11 and fibroblast-associated expression could connect the immune component to stromal adhesion and tissue remodeling. The other module branches may represent correlated lysosomal, membrane-trafficking, transcriptional or growth-regulatory states rather than direct physical parts of one pathway. This hypothesis predicts that module abundance will track immune and stromal composition, inflammatory stimulation and extracellular-matrix turnover, and should be tested with deconvolution, matched cell-state measurements and functional perturbation.

### Important genes

#### TLR2

- **Related proteins** (co-abundance neighbors): ITGAL (0.88), ARHGEF10L (0.81), FCGRT (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: toll like receptor 2. The protein encoded by this gene is a member of the Toll-like receptor (TLR) family which plays a fundamental role in pathogen recognition and activation of innate immunity. TLRs are highly conserved from Drosophila to humans and share structural and functional similarities. This protein is a cell-surface protein that can form heterodimers with other TLR family members to recognize conserved molec…
- **Diseases (Open Targets)**: tuberculosis (0.489); inborn error of immunity (0.372); neurodegenerative disease (0.229); attenuated familial adenomatous polyposis (0.185); colorectal cancer (0.184)
- **Europe PMC papers**: 90571
- **Why important**: TLR2 is a central biological anchor because it is part of the primary KEGG evidence (KEGG Rheumatoid arthritis - Homo sapiens (human); q_global = 0.0188) and the supplementary STRING term (STRING KEGG Rheumatoid arthritis; within-query FDR = 0.0023). It is tissue-enhanced in bone marrow, enriched in neutrophils and associated with several myeloid blood-cell populations. Its annotated role in pathogen recognition and innate-immune signaling gives the module a clear inflammatory entry point. It also has a large literature base and broad disease relevance, making it more interpretable than the less characterized module members.
- **Conclusion**: Established evidence supports TLR2 as an immune-recognition component and as a plausible marker of myeloid or neutrophil representation. It is not established that TLR2 initiates the entire module in breast or cell-line samples; that causal role remains a hypothesis.

#### ITGAL

- **Related proteins** (co-abundance neighbors): TLR2 (0.88), SRPX (0.86); STRING partners: VAV1 (0.948)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha L. ITGAL encodes the integrin alpha L chain. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain. This I-domain containing alpha integrin combines with the beta 2 chain (ITGB2) to form the integrin lymphocyte function-associated antigen-1 (LFA-1), which is expressed on all leukocytes. LFA-1 plays a central role in leukocyte intercellular adhesion through…
- **Diseases (Open Targets)**: psoriasis vulgaris (0.585); dry eye syndrome (0.568); psoriasis (0.473); eye disorder (0.371); ulcerative colitis (0.336)
- **Europe PMC papers**: 2930
- **Why important**: ITGAL is part of the primary KEGG evidence (KEGG Rheumatoid arthritis - Homo sapiens (human); q_global = 0.0188) and supplementary STRING evidence (STRING KEGG Rheumatoid arthritis; within-query FDR = 0.0023). It encodes the leukocyte integrin alpha chain that forms LFA-type adhesion machinery with a beta chain, and its annotations emphasize leukocyte adhesion, inflammatory response and immune-cell interaction. It is enhanced in bone marrow and lymphoid tissue and in multiple leukocyte-related cell types. Its high-confidence STRING relationship with VAV1 provides the clearest known interaction in the module.
- **Conclusion**: Established evidence supports ITGAL as a leukocyte-adhesion and immune-cell-state marker that links the module to cell contact and migration. The co-abundance data do not establish whether ITGAL is functionally active in the breast or cell line context.

#### CTSK

- **Related proteins** (co-abundance neighbors): VAV1 (0.91), SRPX (0.88), CDH11 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cathepsin K. The protein encoded by this gene is a lysosomal cysteine proteinase involved in bone remodeling and resorption. This protein, which is a member of the peptidase C1 protein family, is predominantly expressed in osteoclasts. However, the encoded protein is also expressed in a significant fraction of human breast cancers, where it could contribute to tumor invasiveness. Mutations in this gene are the…
- **Diseases (Open Targets)**: pycnodysostosis (0.835); hereditary disease (0.451); osteoporosis (0.395); neurodegenerative disease (0.371); skeletal dysplasia (0.362)
- **Europe PMC papers**: 10452
- **Why important**: CTSK is part of the primary KEGG evidence (KEGG Rheumatoid arthritis - Homo sapiens (human); q_global = 0.0188) and supplementary STRING evidence (STRING KEGG Rheumatoid arthritis; within-query FDR = 0.0023). It is a lysosomal cysteine protease with documented roles in bone remodeling, collagen catabolism and extracellular-matrix disassembly, and it is associated with fibroblast and classical-monocyte states in HPA evidence. It has a substantial disease and literature record, including skeletal disease and breast-cancer relevance. Its network links to VAV1, SRPX and CDH11 place it at the interface of immune, stromal and matrix-associated signals.
- **Conclusion**: Established evidence supports CTSK as a proteolytic remodeling component and a plausible bridge between myeloid or stromal states and matrix turnover. Its causal contribution to this conserved module, rather than passive correlation with cell composition, remains unproven.

#### MMP1

- **Related proteins** (co-abundance neighbors): KIAA0513 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: matrix metallopeptidase 1. This gene encodes a member of the peptidase M10 family of matrix metalloproteinases (MMPs). Proteins in this family are involved in the breakdown of extracellular matrix in normal physiological processes, such as embryonic development, reproduction, and tissue remodeling, as well as in disease processes, such as arthritis and metastasis. The encoded preproprotein is proteolytically processed to ge…
- **Diseases (Open Targets)**: acne (0.615); rosacea (0.580); periodontitis (0.569); infection (0.551); spotted fever (0.491)
- **Europe PMC papers**: 27247
- **Why important**: MMP1 is part of the primary KEGG evidence (KEGG Rheumatoid arthritis - Homo sapiens (human); q_global = 0.0188) and supplementary STRING evidence (STRING KEGG Rheumatoid arthritis; within-query FDR = 0.0023). It is a secreted extracellular-matrix protease annotated for interstitial-collagen breakdown, matrix disassembly and tissue remodeling. HPA places it in fibroblast-associated cell types and assigns extracellular-matrix secretion, complementing the immune-cell signals from TLR2 and ITGAL. MMP1 also has a very large literature base and established relevance to inflammation, tissue remodeling and metastasis-related biology.
- **Conclusion**: Established evidence supports MMP1 as an extracellular matrix-remodeling effector within the module. It is plausible that MMP1 reports stromal activation or tissue injury, but the data do not show that it is regulated by TLR2 or that it drives the shared co-abundance pattern.

#### VAV1

- **Related proteins** (co-abundance neighbors): CTSK (0.91); STRING partners: ITGAL (0.948)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vav guanine nucleotide exchange factor 1. This gene is a member of the VAV gene family. The VAV proteins are guanine nucleotide exchange factors (GEFs) for Rho family GTPases that activate pathways leading to actin cytoskeletal rearrangements and transcriptional alterations. The encoded protein is important in hematopoiesis, playing a role in T-cell and B-cell development and activation. The encoded protein has been identified as the spec…
- **Diseases (Open Targets)**: cutaneous leishmaniasis (0.503); cancer (0.394); lung adenocarcinoma (0.230); Shock (0.218); breast carcinoma (0.211)
- **Europe PMC papers**: 6288
- **Why important**: VAV1 is the module member participating in the listed high-confidence STRING interaction with ITGAL. It is a guanine-nucleotide-exchange factor involved in Rho-family signaling, hematopoiesis, lymphocyte development and immune-cell activation. Its HPA annotation associates it with bone marrow, lymphoid tissue, B cells, macrophages and other immune-related cell types. Its established signaling function makes it a useful mechanistic connector between leukocyte adhesion and cytoskeletal or migratory responses, even though it is not in the globally corrected GO or KEGG term.
- **Conclusion**: Established evidence supports VAV1 as an immune signaling and cytoskeletal-regulation component linked to ITGAL. Its position suggests a possible signaling bridge, but the co-abundance network alone cannot demonstrate direct pathway transmission through VAV1 in these samples.

## Module 3

**Tissue pair**: breast and cell line  
**Genes (38)**: APBB1IP, ADNP, AFG2B, B4GALT4, BCL2, CD109, CPVL, DGKB, EIF2AK2, ELMOD2, ELOC, F9, FLNB, GBA1, GFRA1, DPAGT1, IFI44L, KLHL18, PPFIBP1, LOXL1, LRRC32, NCF4, NCKAP1, NDUFA6, OMA1, PACC1, SERPINE1, PIEZO1, PTCD3, PRXL2A, GFM2, SLC12A9, SLC25A32, SCARB1, INIP, FARS2, SYT7, ATP6V0A2

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent. The gene annotations nevertheless suggest a heterogeneous module with several converging themes: innate antiviral defense through IFI44L and EIF2AK2; immune-cell and phagocyte biology through NCF4, CPVL and APBB1IP; extracellular signaling and matrix or adhesion regulation through LRRC32, CD109, LOXL1 and FLNB; coagulation through F9 and SERPINE1; and mitochondrial, lipid or membrane processes through DGKB, SLC25A32, GBA1, OMA1 and related genes. The network therefore does not support assigning a single established pathway function. Its strongest functional interpretation is a mixed immune–vascular or extracellular-interface program with additional mitochondrial and cell-survival components. The absence of globally significant enrichment does not invalidate the module, but it means that this interpretation is driven by gene-level annotations and network structure rather than by a corrected pathway result.

**Cell composition.** The module is not dominated by secreted proteins, although secreted-to-blood members such as F9 and SERPINE1 and an extracellular-matrix member such as LOXL1 are present. Most genes have low tissue specificity, while many show cell-type-enhanced expression. HPA points toward a mixture of lymphoid, myeloid, hepatic, neural, vascular and trophoblast-associated signals rather than a uniform breast epithelial identity. Neutrophil, monocyte, macrophage, dendritic-cell and T-regulatory-cell signals are notable, including the blood-associated NCF4 and the myeloid-associated CPVL. This raises the possibility that the shared breast–cell-line module partly reflects blood or immune-cell admixture, shared stromal or endothelial features, or broad cellular programs. Breast protein detection is present for many members, but the absence of a matching HPA tissue for the cell-line context limits direct tissue-composition comparison.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The known STRING evidence is very limited: the only high-confidence STRING relationship is EIF2AK2–IFI44L. This supports a real antiviral or interferon-related connection within part of the module, but does not establish the remaining co-abundance edges as physical interactions. hu.MAP provides one partial complex association, (hu.MAP huMAP3_09327.1), containing GBA1 and CD109 among many other complex members. Because only a small subset of that complex is represented in the module, (hu.MAP huMAP3_09327.1) supports possible complex-related context rather than a complete module mechanism. The sparse STRING and hu.MAP overlap indicates that the co-abundance structure is not simply a known protein complex or a densely documented interaction network.

**STRING interactions (score >= 0.7)**: 1 of 703 gene pairs: EIF2AK2–IFI44L (0.927)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09327.1 (GBA1, CD109; 2/93)

### Novelty

The module should not be called a new biological discovery solely because most of its relationships are absent from STRING or hu.MAP. Those databases are incomplete, and co-abundance does not by itself establish molecular interaction. A cautious conclusion is that the particular cross-context co-abundance pattern may be under-described, while its component biology is not novel: antiviral signaling, coagulation, apoptosis, immune-cell functions, mitochondrial translation, lipid handling and extracellular signaling are all established areas. The potentially novel aspect is the combination of these signals and their reproducibility across breast and cell-line data, which would require independent cohorts, cell-composition adjustment, perturbation experiments or replication in orthogonal datasets to support a new finding.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state or sample-composition program at an immune–vascular or extracellular interface. An antiviral or inflammatory state may connect EIF2AK2 and IFI44L with myeloid and phagocyte-associated genes, while LRRC32, CD109, LOXL1 and SERPINE1 could represent regulation of TGF-beta-related signaling, matrix remodeling and coagulation. BCL2 may mark survival of the contributing cells, and mitochondrial or membrane genes may reflect the metabolic and trafficking requirements of that state. A competing explanation is that the module is assembled largely by mixed-cell or blood-associated signals rather than by one coordinated intracellular pathway.

### Important genes

#### LRRC32

- **Related proteins** (co-abundance neighbors): SLC25A32 (0.96), NCF4 (0.86), B4GALT4 (0.82), APBB1IP (0.81), CPVL (0.81), SLC12A9 (0.81), PTCD3 (0.81), AFG2B (0.81), OMA1 (0.81), PIEZO1 (0.81), SCARB1 (0.80), DPAGT1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: leucine rich repeat containing 32. This gene encodes a type I membrane protein which contains 20 leucine-rich repeats. Alterations in the chromosomal region 11q13-11q14 are involved in several pathologies. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: cleft palate, proliferative retinopathy, and developmental delay (0.623); asthma (0.502); atopic eczema (0.408); dermatitis (0.381); Hepatitis (0.355)
- **Europe PMC papers**: 2406
- **Why important**: LRRC32 is the strongest network hub in the supplied subgraph and connects genes associated with transport, myeloid biology, membrane signaling and cell adhesion. Its annotation includes transforming growth factor beta receptor signaling, and HPA associates it with T-regulatory cells, fibroblasts, pericytes and lymphatic endothelial cells. Its disease associations include cleft palate, proliferative retinopathy, asthma, atopic eczema, dermatitis and hepatitis, while its literature record is substantial.
- **Conclusion**: Established evidence supports LRRC32 as a network-organizing membrane protein associated with TGF-beta-related signaling and several stromal or immune cell types. It is a plausible integrative marker of the module, but the data do not establish that it mechanistically regulates the other module members.

#### IFI44L

- **Related proteins** (co-abundance neighbors): PRXL2A (0.89), ATP6V0A2 (0.86), NCKAP1 (0.85), FARS2 (0.83), EIF2AK2 (0.82), ELMOD2 (0.80), PTCD3 (0.80); STRING partners: EIF2AK2 (0.927)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: interferon induced protein 44 like. Predicted to enable GTP binding activity. Involved in defense response to virus. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: MMR-related febrile seizures (0.427); Febrile seizure (within the age range of 3 months to 6 years) (0.344); response to vaccine (0.342); CINCA syndrome (0.185); Encephalopathy (0.148)
- **Europe PMC papers**: 3361
- **Why important**: IFI44L is a central bridge between several module genes and the only gene directly supported by a high-confidence STRING relationship with EIF2AK2. Its annotation supports antiviral defense, immune response and predicted GTP binding, and HPA shows enhancement in macrophages, microglia and plasmacytoid dendritic cells. It has substantial literature and disease links involving febrile seizures, vaccine response and inflammatory neurological conditions.
- **Conclusion**: Established evidence supports IFI44L as the clearest antiviral or innate-immune anchor of the module, especially because its relationship with EIF2AK2 is independently represented in STRING. Its role as the driver of the whole module remains a hypothesis.

#### F9

- **Related proteins** (co-abundance neighbors): OMA1 (0.89), GFM2 (0.87), ADNP (0.86), CD109 (0.84), PPFIBP1 (0.83), GBA1 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coagulation factor IX. This gene encodes vitamin K-dependent coagulation factor IX that circulates in the blood as an inactive zymogen. This factor is converted to an active form by factor XIa, which excises the activation peptide and thus generates a heavy chain and a light chain held together by one or more disulfide bonds. The role of this activated factor IX in the blood coagulation cascade is to activate factor X t…
- **Diseases (Open Targets)**: hemophilia B (0.890); hemophilia A (0.763); thrombophilia, X-linked, due to factor 9 defect (0.747); x-linked warfarin sensitivity (0.694); hemorrhage (0.581)
- **Europe PMC papers**: 13996
- **Why important**: F9 is a blood-secreted coagulation factor with strong disease and literature support, especially for hemophilia B and related bleeding or thrombosis biology. In the module it links to OMA1, GFM2, ADNP, CD109 and PPFIBP1, thereby connecting a circulating plasma protein to intracellular and membrane-associated genes. HPA identifies liver and hepatocyte enrichment and no immune-cell detection.
- **Conclusion**: Established evidence supports F9 as a circulating liver-derived coagulation component, not as evidence for a unified intracellular pathway. Its presence makes blood or plasma contribution a serious alternative explanation for the shared module.

#### BCL2

- **Related proteins** (co-abundance neighbors): INIP (0.93), LOXL1 (0.85), GFRA1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BCL2 apoptosis regulator. This gene encodes an integral outer mitochondrial membrane protein that blocks the apoptotic death of some cells such as lymphocytes. Constitutive expression of BCL2, such as in the case of translocation of BCL2 to Ig heavy chain locus, is thought to be the cause of follicular lymphoma. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016].
- **Diseases (Open Targets)**: B-cell chronic lymphocytic leukemia (0.740); neoplasm (0.605); diffuse large B-cell lymphoma (0.554); neurodegenerative disease (0.541); prostate carcinoma (0.533)
- **Europe PMC papers**: 83347
- **Why important**: BCL2 is a highly studied mitochondrial apoptosis regulator with very extensive literature and established associations with lymphoid malignancy and other disease contexts. It connects to INIP, LOXL1 and GFRA1 in the module, linking cell survival with genome stability, extracellular-matrix biology and receptor signaling. HPA detects it in breast and shows enhancement in B cells and other cell types.
- **Conclusion**: Established evidence supports BCL2 as a cell-survival marker and plausible indicator of the viability state of contributing cells. The module does not demonstrate that BCL2 is coordinating the immune, coagulation or mitochondrial signals.

#### DGKB

- **Related proteins** (co-abundance neighbors): INIP (0.86), SLC25A32 (0.85), ELOC (0.83), SERPINE1 (0.82), NDUFA6 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: diacylglycerol kinase beta. Diacylglycerol kinases (DGKs) are regulators of the intracellular concentration of the second messenger diacylglycerol (DAG) and thus play a key role in cellular processes. Nine mammalian isotypes have been identified, which are encoded by separate genes. Mammalian DGK isozymes contain a conserved catalytic (kinase) domain and a cysteine-rich domain (CRD). The protein encoded by this gene is a dia…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.559); diabetes mellitus (0.542); diverticular disease (0.486); mathematical ability (0.437); Abnormality of the skeletal system (0.424)
- **Europe PMC papers**: 832
- **Why important**: DGKB is a network connector associated with diacylglycerol metabolism, phosphatidic-acid biosynthesis, signal transduction, platelet activation and G-protein-coupled receptor signaling. HPA identifies brain enrichment and enhancement in neuronal, adrenal and granulosa-cell contexts. It links INIP, SLC25A32, ELOC, SERPINE1 and NDUFA6, joining signaling, transcriptional regulation, coagulation-associated biology and mitochondrial function.
- **Conclusion**: Established evidence supports DGKB as a lipid-signaling and membrane-regulatory enzyme with a plausible connection to platelet and receptor signaling. Its placement in this module is consistent with a signaling or metabolic interface, but a causal role is not established.

## Module 4

**Tissue pair**: breast and cell line  
**Genes (22)**: ACACA, ANKRD17, AP3B2, HLCS, C7orf25, C8A, DHX57, DIS3L2, TSFM, FBF1, HABP2, HPS3, INTS7, KIF2A, MCM7, OPA1, OSBPL11, PPP4R3A, SPAG5, SPATS2, TEX264, ATP6V1C1

### Function

This module does not support a single established biological pathway. No GO or KEGG term passed global correction, and STRING reported no supplementary functional enrichment. The strongest biological interpretation is a heterogeneous co-abundance program organized around AP3B2, with possible contributions from intracellular vesicle trafficking, organelle and lysosome-related processes, lipid and biotin metabolism, mitochondrial function, and cell-cycle activity. These themes are suggested by individual gene annotations rather than by statistically significant module-level enrichment. The module may therefore capture coordinated expression across shared cellular states rather than a discrete molecular complex or pathway.

**Cell composition.** The module is not predominantly composed of plasma proteins, secreted proteins, or blood-cell-specific genes. Most genes have low tissue specificity, while many show cell-type-enhanced expression across diverse cell types, including neuronal, reproductive, muscle, and progenitor populations. C8A and HABP2 are liver-enriched proteins secreted to blood, forming a small circulating-protein component. The blood-cell evidence is generally weak, although SPAG5 has group-enriched blood-cell expression and C7orf25 is immune-cell enhanced in basophils. HPA detects several module proteins in breast, but no matching HPA tissue is available for the cell-line condition. The broad and mixed expression profile means that the shared module could partly reflect common cellular composition or general cell-state effects rather than a breast-specific mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The module has very limited prior molecular-interaction support. STRING identifies ACACA and HLCS as a high-confidence known interaction, consistent with their biochemical relationship in fatty-acid synthesis and biotin-dependent carboxylase function. No other module pair is represented as a high-confidence STRING interaction in the supplied evidence. No hu.MAP complex contains multiple module members. Thus, the co-abundance network should not be interpreted as a known physical complex. Most edges are co-abundance relationships without independent interaction evidence, and the central position of AP3B2 is not by itself evidence that AP3B2 physically binds the other genes.

**STRING interactions (score >= 0.7)**: 1 of 231 gene pairs: ACACA–HLCS (0.961)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be novel as a cross-tissue co-abundance pattern because it combines a central neuronal AP-3-related gene with genes involved in metabolism, organelle trafficking, cell division, mitochondrial biology, RNA handling, and circulating complement biology, while lacking a matching STRING-enriched pathway or hu.MAP complex. However, this does not establish a new biological mechanism. The presence of the known ACACA-HLCS relationship, established functions for many individual genes, and the absence of supporting interactions for most edges indicate that the novelty lies primarily in the observed co-abundance organization. Validation in independent breast and cell-line datasets, assessment of cell composition, and perturbation experiments would be required before claiming a novel regulatory module.

**Hypothesis.** Hypothesis: the module represents a shared cell-state program linking vesicle and organelle handling centered on AP3B2 with metabolic capacity, mitochondrial maintenance, proliferative activity, and a minor circulating-protein signal. In breast samples, this pattern could arise from coordinated abundance across epithelial or other constituent cell states, while in the cell line it could reflect a conserved growth or organelle-maintenance state. The ACACA-HLCS relationship provides a plausible metabolic submodule, whereas the links from AP3B2 to the other genes may reflect coordinated transcription, shared cellular composition, or indirect regulation rather than direct physical binding. This hypothesis is not established by the available enrichment or interaction evidence.

### Important genes

#### AP3B2

- **Related proteins** (co-abundance neighbors): HPS3 (0.93), PPP4R3A (0.93), TEX264 (0.89), INTS7 (0.87), C7orf25 (0.85), DIS3L2 (0.84), OPA1 (0.84), ATP6V1C1 (0.83), SPAG5 (0.83), OSBPL11 (0.83), ACACA (0.83), KIF2A (0.82), HLCS (0.82), DHX57 (0.81), TSFM (0.81), MCM7 (0.81), ANKRD17 (0.81), SPATS2 (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor related protein complex 3 subunit beta 2. Adaptor protein complex 3 (AP-3 complex) is a heterotrimeric protein complex involved in the formation of clathrin-coated synaptic vesicles. The protein encoded by this gene represents the beta subunit of the neuron-specific AP-3 complex and was first identified as the target antigen in human paraneoplastic neurologic disorders. The encoded subunit binds clathrin and is phosphorylated by a casein …
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 48 (0.730); genetic developmental and epileptic encephalopathy (0.371); undetermined early-onset epileptic encephalopathy (0.370); Epileptic encephalopathy (0.334); intelligence (0.311)
- **Europe PMC papers**: 537
- **Why important**: AP3B2 is the principal network hub and connects genes spanning vesicle biology, RNA processing, mitochondrial function, cell division, and intracellular acidification. Its established function is as the beta subunit of the neuron-specific AP-3 complex, involved in clathrin-coated synaptic-vesicle formation and intracellular transport. HPA links it to brain and neuroendocrine cell types, and its disease associations include developmental and epileptic encephalopathy. Its substantial literature makes it the best candidate for organizing interpretation of the module, even though STRING provides no known partners for the module edges.
- **Conclusion**: Established evidence supports AP3B2 as an intracellular trafficking and vesicle-coat protein with neuronal relevance. Its role as the biological driver of this module is a hypothesis based on network position and co-abundance, not a demonstrated physical or regulatory relationship.

#### ACACA

- **Related proteins** (co-abundance neighbors): AP3B2 (0.83), FBF1 (0.82); STRING partners: HLCS (0.961)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA carboxylase alpha. Acetyl-CoA carboxylase (ACC) is a complex multifunctional enzyme system. ACC is a biotin-containing enzyme which catalyzes the carboxylation of acetyl-CoA to malonyl-CoA, the rate-limiting step in fatty acid synthesis. There are two ACC forms, alpha and beta, encoded by two different genes. ACC-alpha is highly enriched in lipogenic tissues. The enzyme is under long term control at the transcriptio…
- **Diseases (Open Targets)**: neurodegenerative disease (0.550); Alzheimer disease (0.463); lysosomal storage disease (0.460); Parkinson disease (0.460); autoimmune disorder of central nervous system (0.383)
- **Europe PMC papers**: 6268
- **Why important**: ACACA is a central metabolic marker within the module and is linked in the co-abundance network to AP3B2 and FBF1. It catalyzes the rate-limiting step of fatty-acid synthesis, and its function is directly relevant to membrane production and cellular energy storage. It is detected in breast by HPA and has extensive literature and disease associations, including neurodegenerative and lipid-related contexts. Its known STRING relationship with HLCS gives this part of the module stronger mechanistic support than most other edges.
- **Conclusion**: Established evidence supports ACACA as a major fatty-acid biosynthetic enzyme and as part of a known biochemical relationship with HLCS. Whether ACACA provides a metabolic explanation for the whole module, or merely marks a shared metabolic state, remains unresolved.

#### HLCS

- **Related proteins** (co-abundance neighbors): AP3B2 (0.82); STRING partners: ACACA (0.961)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: holocarboxylase synthetase. This gene encodes an enzyme that catalyzes the binding of biotin to carboxylases and histones. The protein plays an important role in gluconeogenesis, fatty acid synthesis and branched chain amino acid catabolism. Defects in this gene are the cause of holocarboxylase synthetase deficiency. Multiple alternatively spliced variants, encoding the same protein, have been identified.[provided by RefSeq,…
- **Diseases (Open Targets)**: holocarboxylase synthetase deficiency (0.855); inborn vitamin metabolic disorder (0.526); hereditary disease (0.471); neurodegenerative disease (0.383); male infertility (0.210)
- **Europe PMC papers**: 1440
- **Why important**: HLCS is the partner of ACACA in the only high-confidence STRING interaction among module members. It attaches biotin to carboxylases and histones and supports fatty-acid synthesis, gluconeogenesis, and branched-chain amino-acid catabolism. It is detected in breast and has a well-established disease association with holocarboxylase synthetase deficiency. This makes HLCS an important anchor for the module's metabolic interpretation.
- **Conclusion**: Established evidence supports HLCS as a biotin-dependent modification enzyme with a direct relationship to ACACA. Its broader connection to the module is inferential and could reflect coordinated metabolic demand rather than a dedicated module-specific mechanism.

#### C8A

- **Related proteins** (co-abundance neighbors): HABP2 (0.88), C7orf25 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C8 alpha chain. C8 is a component of the complement system and contains three polypeptides, alpha, beta and gamma. This gene encodes the alpha subunit of C8. C8 participates in the formation of the membrane attack complex (MAC). The MAC assembles on bacterial membranes to form a pore, permitting disruption of bacterial membrane organization. Mutations in this gene cause complement C8 alpha-gamma deficiency. [prov…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.690); complement deficiency (0.462); focal epilepsy (0.234); ankylosing spondylitis (0.214); pernicious anemia (0.097)
- **Europe PMC papers**: 1382
- **Why important**: C8A is a liver-enriched protein secreted to blood and encodes a component of the complement membrane-attack complex. It has strong disease relevance through complement C8 deficiency and substantial literature. In the module it connects to HABP2, another liver-derived secreted protein, and to C7orf25. These annotations identify a circulating extracellular component that differs sharply from the intracellular functions represented by many other module genes.
- **Conclusion**: Established evidence supports C8A as a secreted complement protein, likely reflecting extracellular or plasma-associated biology. Its inclusion does not establish that complement participates in the intracellular co-abundance program; it may instead indicate circulating protein carryover, shared sample composition, or an indirect tissue-level signal.

#### SPAG5

- **Related proteins** (co-abundance neighbors): AP3B2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Group enriched; location Nuclear bodies, Mitotic spindle; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sperm associated antigen 5. This gene encodes a protein associated with the mitotic spindle apparatus. The encoded protein may be involved in the functional and dynamic regulation of mitotic spindles. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.493); neoplasm (0.112); breast cancer (0.110); hepatocellular carcinoma (0.110); breast carcinoma (0.108)
- **Europe PMC papers**: 5926
- **Why important**: SPAG5 is associated with the mitotic spindle and chromosome segregation, and it is tissue enhanced in bone marrow, kidney, and testis. It is detected in breast and has extensive literature, including associations with breast cancer and other neoplastic contexts. Its presence supplies a plausible proliferative or mitotic component to a module otherwise dominated by heterogeneous single-gene annotations.
- **Conclusion**: Established evidence supports SPAG5 as a spindle-associated cell-division protein with disease relevance in cancer contexts. Its contribution to this shared module is most plausibly a marker of proliferative state, but a causal role in organizing the module is not established.

## Module 5

**Tissue pair**: breast and cell line  
**Genes (45)**: SLC33A1, ACTR10, CDK19, CEMIP2, CEP89, CHD1, CHD4, CHST2, CPSF1, COPS3, DDX21, DDX59, DHCR7, DNAJC10, ELMO3, PTK2, TBRG4, MACROH2A2, HDAC8, MTIF3, INTS6, JAK2, KCT2, LYPLAL1, MAPK13, NBEAL2, NOC3L, NUB1, PDS5B, DHRS7B, RBP7, RNF213, POLR2A, POLR3A, SHPRH, SYTL5, TBC1D10A, GTF3C4, TMTC3, TOE1, TOR2A, TOR2A, SNRNP200, UGGT1, WDR47

### Function

No GO/KEGG term passed global correction, so the module does not have a statistically established pathway annotation from that analysis. Its strongest supplementary signal is a helicase-related group involving SHPRH, SNRNP200, DDX59, DDX21, CHD4 and CHD1 (5 supplementary STRING terms; within-query FDR 0.0052–0.0289). The gene annotations and network structure additionally point to a mixed nuclear gene-expression program involving RNA processing, transcriptional regulation, chromatin remodeling, DNA repair, and RNA polymerase activity. The topology is organized around SYTL5, with several largely separate branches rather than a densely interconnected canonical pathway. Accordingly, the most defensible interpretation is a broad cellular co-abundance program rather than a single demonstrated biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only TOR2A is annotated as secreted to blood, while UGGT1 has intracellular and membrane localization. Most genes have low tissue specificity, and the breast protein data show broad detection rather than a restricted secretory signature. Many genes are cell-type enhanced, but the module is not strongly immune-cell biased overall. Neutrophil-associated genes, including JAK2, NBEAL2, CDK19 and RNF213, and additional monocyte or NK-cell associations suggest that blood or shared immune-cell content could contribute to co-abundance in some samples, but the HPA profile does not support a predominantly blood-cell module. The shared breast–cell-line signal may therefore reflect broadly expressed cellular machinery, with possible contributions from shared epithelial or immune-related cell states.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The high-confidence STRING evidence is sparse but biologically coherent in places. Known relationships connect JAK2 with PTK2 and MAPK13, connect POLR2A with CDK19, CPSF1 and INTS6, connect POLR3A with GTF3C4, and connect DNAJC10 with UGGT1. These relationships support signalling, transcriptional regulation, RNA processing and endoplasmic-reticulum quality control as genuine components of the module, but they do not establish one unified interaction complex. hu.MAP provides additional support for recurring physical-complex membership: CHD4 and SHPRH occur together in chromatin-remodeling-related complexes (hu.MAP huMAP3_09499.1), (hu.MAP huMAP3_10472.1) and (hu.MAP huMAP3_15128.1); POLR2A and POLR3A recur in transcription-associated complexes (hu.MAP huMAP3_08487.1) (hu.MAP huMAP3_06426.1) (hu.MAP huMAP3_14318.1) (hu.MAP huMAP3_11092.1); RNF213, TBRG4 and PDS5B co-occur in (hu.MAP huMAP3_11232.1); DHRS7B and DHCR7 occur in a membrane and sterol-associated complex (hu.MAP huMAP3_09592.1); and SNRNP200 with TOE1 occurs in an RNA-processing complex (hu.MAP huMAP3_08980.1). Because each complex captures only a small subset of the module, these results support several established molecular neighborhoods rather than a single known complex underlying the entire module.

**STRING interactions (score >= 0.7)**: 7 of 990 gene pairs: CDK19–POLR2A (0.881); CPSF1–POLR2A (0.728); DNAJC10–UGGT1 (0.728); GTF3C4–POLR3A (0.784); INTS6–POLR2A (0.999); JAK2–PTK2 (0.962); MAPK13–PTK2 (0.914)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Helicase superfamily c-terminal domain (FDR = 0.0052, 6 genes); Keyword Helicase (FDR = 0.0177, 6 genes); SMART DEAD-like helicases superfamily (FDR = 0.0287, 5 genes); InterPro Helicase, C-terminal (FDR = 0.0289, 6 genes); InterPro Helicase superfamily 1/2, ATP-binding domain (FDR = 0.0289, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11232.1 (RNF213, TBRG4, PDS5B; 3/78); huMAP3_09499.1 (CHD4, SHPRH; 2/33); huMAP3_10472.1 (CHD4, SHPRH; 2/36); huMAP3_08487.1 (POLR3A, POLR2A; 2/37); huMAP3_06426.1 (POLR3A, POLR2A; 2/38); huMAP3_14318.1 (POLR3A, POLR2A; 2/58); huMAP3_11092.1 (POLR3A, POLR2A; 2/65); huMAP3_15128.1 (CHD4, SHPRH; 2/96); huMAP3_09592.1 (DHRS7B, DHCR7; 2/95); huMAP3_08980.1 (SNRNP200, TOE1; 2/97)

### Novelty

This may be a new tissue-pair co-abundance observation, but the fact sheet does not provide evidence sufficient to claim discovery of a new molecular pathway or interaction complex. The constituent biology is largely established: JAK2–PTK2 and PTK2–MAPK13 are known STRING relationships, and the POLR2A, POLR3A, CHD4, SHPRH and SNRNP200 memberships are represented in STRING or hu.MAP. The potentially novel aspect is the coordinated abundance of these otherwise partly disconnected cellular programs in breast and cell-line data, particularly the central position of SYTL5, which has no recorded STRING partners or hu.MAP complex membership here. Absence from the reference interaction resources alone does not prove novelty. A novelty claim would require comparison with prior tissue-specific co-abundance modules, independent cohorts, and experimental validation.

**Hypothesis.** Hypothesis: the module represents a shared cellular-state program in which transcriptional output, RNA maturation, chromatin remodeling, proteostasis and stress-responsive signalling vary together across breast samples and cell lines. SYTL5 may act as a co-abundance hub reflecting vesicle or membrane-trafficking state, while JAK2–PTK2–MAPK13 could report cytokine, adhesion or stress signalling. In parallel, INTS6, POLR2A, POLR3A, helicase-associated genes and CHD4 could reflect coordinated changes in transcription, RNA processing and chromatin organization. The apparent coupling may arise from a common regulatory state, shared cell composition, or technical covariance rather than direct physical interaction. This hypothesis should be tested by replication, adjustment for cell composition, perturbation of the signalling branch, and measurement of transcriptional and RNA-processing outputs.

### Important genes

#### SYTL5

- **Related proteins** (co-abundance neighbors): RNF213 (0.90), TOE1 (0.89), GTF3C4 (0.88), WDR47 (0.88), PDS5B (0.88), NOC3L (0.87), DDX21 (0.87), PTK2 (0.86), TMTC3 (0.86), ELMO3 (0.85), TBC1D10A (0.85), DNAJC10 (0.84), SNRNP200 (0.84), COPS3 (0.84), MACROH2A2 (0.84), DHRS7B (0.83), UGGT1 (0.83), INTS6 (0.83), TBRG4 (0.82), POLR2A (0.82), CHD1 (0.82), CHD4 (0.82), LYPLAL1 (0.82), SLC33A1 (0.81), CPSF1 (0.81), NUB1 (0.81), DDX59 (0.80), DHCR7 (0.80), POLR3A (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: synaptotagmin like 5. The protein encoded by this gene belongs to the synaptotagmin-like (Slp) protein family, which contains a unique homology domain at the N-terminus, referred to as the Slp homology domain (SHD). The SHD functions as a binding site for Rab27A, which plays a role in protein transport. Expression of this gene is restricted to placenta and liver, suggesting that it might be involved in Rab27A-dependent…
- **Diseases (Open Targets)**: laterality defects, autosomal dominant (0.111); adrenal cortex carcinoma (0.043); thyroid gland papillary carcinoma (0.039); pancreatic adenocarcinoma (0.038); eyelid disorder (0.036)
- **Europe PMC papers**: 202
- **Why important**: SYTL5 is the principal network hub, with many strong co-abundance links to genes spanning RNA processing, transcription, signalling, trafficking and chromatin biology. Its annotation supports Rab27A-dependent intracellular transport and exocytosis, and its HPA profile is tissue enhanced in brain and cell-type enhanced in several epithelial and neural populations. It has no STRING partners or hu.MAP assignment in the fact sheet, making its central network position particularly informative but also requiring caution. Its literature volume is moderate relative to the heavily studied signalling and transcription genes in this module.
- **Conclusion**: Established evidence supports SYTL5 as a statistical co-abundance hub with a plausible membrane-trafficking function. It is not established that SYTL5 physically organizes the other module branches. Its hub status could reflect a shared cellular state or indirect regulation, so it is a leading candidate for validation rather than a proven driver.

#### JAK2

- **Related proteins** (co-abundance neighbors): MAPK13 (0.91), ACTR10 (0.87), CEP89 (0.84), NBEAL2 (0.82), PTK2 (0.81); STRING partners: PTK2 (0.962)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Janus kinase 2. This gene encodes a non-receptor tyrosine kinase that plays a central role in cytokine and growth factor signalling. The primary isoform of this protein has an N-terminal FERM domain that is required for erythropoietin receptor association, an SH2 domain that binds STAT transcription factors, a pseudokinase domain and a C-terminal tyrosine kinase domain. Cytokine binding induces autophosphorylatio…
- **Diseases (Open Targets)**: acquired polycythemia vera (0.804); primary myelofibrosis (0.748); myelofibrosis (0.740); ulcerative colitis (0.732); myeloproliferative disorder (0.712)
- **Europe PMC papers**: 55185
- **Why important**: JAK2 is a biologically important signalling kinase with a central role in cytokine and growth-factor signalling and strong disease associations with myeloproliferative disorders. Within the module it connects to PTK2 and MAPK13, and both relationships are supported by high-confidence STRING evidence. HPA links JAK2 to neutrophils, neutrophil progenitors and basophils, while detecting it in breast, making it relevant to both signalling biology and possible immune-cell composition.
- **Conclusion**: Established evidence supports JAK2 as a signalling node and supports its relationships with PTK2 and MAPK13. The module does not establish that JAK2 activation caused the observed co-abundance, nor that the signal is tumour-cell intrinsic; immune-cell contribution remains a plausible alternative.

#### POLR2A

- **Related proteins** (co-abundance neighbors): SYTL5 (0.82); STRING partners: CDK19 (0.881), CPSF1 (0.728), INTS6 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08487.1, huMAP3_06426.1, huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase II subunit A. This gene encodes the largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene contains a carboxy terminal domain composed of heptapeptide repeats that are essential for polymerase activity. These repeats contain serine and threonine residues that are phosphorylated in actively transcribing RNA polymerase. In addition, …
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and variable intellectual and behavioral abnormalities (0.738); HIV infectious disease (0.600); hereditary disease (0.479); syndromic intellectual disability (0.462); Orthomyxoviridae infectious disease (0.374)
- **Europe PMC papers**: 4546
- **Why important**: POLR2A encodes the largest subunit of RNA polymerase II and is therefore a core component of messenger-RNA transcription. It is connected in STRING to CDK19, CPSF1 and INTS6, and it recurs with POLR3A across several hu.MAP transcription-associated complexes (hu.MAP huMAP3_08487.1) (hu.MAP huMAP3_06426.1) (hu.MAP huMAP3_14318.1) (hu.MAP huMAP3_11092.1). Its position links the module to transcriptional activity and RNA maturation, while its substantial literature base makes its function well established.
- **Conclusion**: Established evidence supports POLR2A as a core transcriptional component and supports several known relationships represented in this module. Its presence is more consistent with a broad transcriptional state than with a novel POLR2A-specific mechanism.

#### CHD4

- **Related proteins** (co-abundance neighbors): SYTL5 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_09499.1, huMAP3_10472.1, huMAP3_15128.1
- **Function (MyGene.info)**: chromodomain helicase DNA binding protein 4. The product of this gene belongs to the SNF2/RAD54 helicase family. It represents the main component of the nucleosome remodeling and deacetylase complex and plays an important role in epigenetic transcriptional repression. Patients with dermatomyositis develop antibodies against this protein. Somatic mutations in this gene are associated with serous endometrial tumors. Alternative splicing result…
- **Diseases (Open Targets)**: Sifrim-Hitz-Weiss syndrome (0.810); neurodegenerative disease (0.551); hereditary disease (0.505); endometrial cancer (0.470); uterine carcinosarcoma (0.439)
- **Europe PMC papers**: 3617
- **Why important**: CHD4 is a chromatin-remodelling ATPase and a principal component of the nucleosome-remodelling and deacetylase complex. It participates in DNA repair and transcriptional repression, appears in all listed supplementary helicase-related STRING terms (5 supplementary STRING terms; within-query FDR 0.0052–0.0289), and occurs with SHPRH in multiple hu.MAP complexes (hu.MAP huMAP3_09499.1), (hu.MAP huMAP3_10472.1) and (hu.MAP huMAP3_15128.1). It is well studied and has disease associations involving developmental syndromes and endometrial cancer.
- **Conclusion**: Established evidence supports CHD4 as a chromatin and DNA-repair component and supports its association with SHPRH-related complexes and the helicase signal. The module does not demonstrate that CHD4 activity is altered or that it controls the other branches; coordinated abundance may simply reflect a general chromatin or proliferation state.

#### INTS6

- **Related proteins** (co-abundance neighbors): CDK19 (0.84), SYTL5 (0.83), CHST2 (0.81); STRING partners: POLR2A (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrator complex subunit 6. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. The protein encoded by this gene is a DEAD box protein that is part of a complex that interacts with the C-terminus of RNA polymerase II and is involved in 3' end processing of snRNAs. In addition, this gene is a candidate tumor suppressor and is located in the critical region of loss of het…
- **Diseases (Open Targets)**: neurodegenerative disease (0.501); Abnormality of the skeletal system (0.258); gestational diabetes (0.252); optic neuritis (0.235); neuropathy (0.235)
- **Europe PMC papers**: 807
- **Why important**: INTS6 is part of the Integrator machinery involved in snRNA processing, transcriptional surveillance and RNA polymerase II regulation. It is connected to POLR2A by an especially strong STRING relationship and also links to CDK19, SYTL5 and CHST2 in the module network. Its candidate tumour-suppressor status and documented links to transcription and RNA processing give it functional relevance beyond being a generic housekeeping transcript.
- **Conclusion**: Established evidence supports INTS6 as an RNA-processing and transcription-regulatory component, with a known POLR2A relationship. Its connection to SYTL5 and CHST2 is a module-level co-abundance observation, not proof of direct molecular binding or a causal bridge between trafficking and RNA processing.

## Module 6

**Tissue pair**: breast and cell line  
**Genes (5)**: ACBD5, LDB3, PIGU, TRIM2, TRIM3

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established pathway-level functional assignment from GO/KEGG. Its structure is centered on LDB3, which connects to PIGU, ACBD5, TRIM2, and TRIM3. The most coherent functional signals come from the gene annotations: LDB3 is associated with PDZ/LIM-mediated cytoskeletal and muscle organization, PIGU with GPI-anchor biosynthesis, ACBD5 with peroxisomal lipid handling and pexophagy, and TRIM2/TRIM3 with RING-B-box-coiled-coil proteins, cytoplasmic filaments, and ubiquitin-related processes. The STRING supplementary terms (STRING SMART B-Box C-terminal domain; within-query FDR = 0.009) through (STRING InterPro Zinc finger, RING-type, eukaryotic; within-query FDR = 0.0457) are driven entirely by TRIM2 and TRIM3 and indicate shared domain architecture rather than enrichment of the whole module. Overall, this is best interpreted as a mixed structural and protein-homeostasis module with a possible cytoskeletal or organelle-associated context, rather than as a demonstrated canonical pathway.

**Cell composition.** The module contains no secreted genes and does not show a plasma-protein signature. HPA evidence also argues against a broadly blood-cell-derived module: most genes have low immune cell specificity or are not detected in immune cells, although TRIM2 is immune-cell enhanced in memory CD4 T-cells. The genes are not uniformly housekeeping-like. Instead, the profile is heterogeneous, with tissue or cell-type associations involving brain, muscle, oligodendrocytes, cardiomyocytes, myonuclei, epicardial cells, retinal pigment epithelial cells, and enterocytes. Thus, the shared breast–cell-line signal is unlikely to be explained simply by secreted blood proteins, but it could reflect shared structural, organelle, or cell-state features and should not automatically be interpreted as breast-specific biology. HPA protein detection in breast is limited to PIGU and ACBD5, while LDB3, TRIM2, and TRIM3 are not detected there.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship among module genes is TRIM2–TRIM3. Their shared STRING annotations (STRING SMART B-Box C-terminal domain; within-query FDR = 0.009) through (STRING InterPro Zinc finger, RING-type, eukaryotic; within-query FDR = 0.0457) consistently point to related B-box, RING-type zinc-finger, filamin-like, and NHL-repeat features. This is established domain-level support for a TRIM2/TRIM3 relationship, but it does not establish a functional interaction involving all module genes. hu.MAP independently places TRIM2 and TRIM3 together in (hu.MAP huMAP3_03664.1), and includes them with KLHL5 in (hu.MAP huMAP3_09516.1) and with KLHL5 and SKA2 in (hu.MAP huMAP3_10203.1). LDB3, PIGU, and ACBD5 have no listed hu.MAP complexes or STRING partners in this evidence set. Consequently, the network contains a known TRIM2–TRIM3 submodule embedded in an otherwise weakly externally supported co-abundance structure; the LDB3-centered edges may represent co-regulation, context dependence, or indirect biology rather than known physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: TRIM2–TRIM3 (0.709)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART B-Box C-terminal domain (FDR = 0.009, 2 genes); SMART Filamin-type immunoglobulin domains (FDR = 0.009, 2 genes); Pfam NHL repeat (FDR = 0.0131, 2 genes); SMART B-Box-type zinc finger (FDR = 0.0314, 2 genes); InterPro NHL repeat (FDR = 0.0457, 2 genes); InterPro Filamin/ABP280 repeat (FDR = 0.0457, 2 genes); InterPro B-box, C-terminal (FDR = 0.0457, 2 genes); InterPro Filamin/ABP280 repeat-like (FDR = 0.0457, 2 genes); InterPro Zinc finger, RING-type, eukaryotic (FDR = 0.0457, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03664.1 (TRIM3, TRIM2; 2/2); huMAP3_09516.1 (TRIM3, TRIM2; 2/3); huMAP3_10203.1 (TRIM3, TRIM2; 2/4)

### Novelty

The module should not be claimed as a wholly new molecular complex or pathway. Its TRIM2–TRIM3 relationship and their shared domain architecture are already supported by STRING and hu.MAP (STRING SMART B-Box C-terminal domain; within-query FDR = 0.009) through (STRING InterPro Zinc finger, RING-type, eukaryotic; within-query FDR = 0.0457) and (hu.MAP huMAP3_03664.1) through (hu.MAP huMAP3_10203.1). The potentially novel aspect is the breast–cell-line co-abundance configuration linking LDB3 with PIGU, ACBD5, TRIM2, and TRIM3, because those specific connections are not represented by the listed STRING or hu.MAP evidence. However, absence from those resources alone does not prove novelty, and the lack of globally significant GO/KEGG enrichment makes a strong novel pathway claim unwarranted. The appropriate conclusion is a potentially interesting, but currently unvalidated, context-specific co-abundance association built around a known TRIM pair.

**Hypothesis.** Hypothesis: in breast and the matched cell-line context, LDB3-associated cytoskeletal or membrane-proximal organization may be co-regulated with protein quality-control and organelle processes represented by TRIM2, TRIM3, ACBD5, and PIGU. TRIM2 and TRIM3 could provide a shared ubiquitin-related structural submodule, while LDB3 could link that state to cytoskeletal organization; ACBD5 and PIGU may reflect accompanying peroxisomal lipid-handling and GPI-anchor-biosynthetic states. This is a mechanistic hypothesis, not an established physical complex. It should be tested by replication across independent breast and cell-line datasets, protein-level interaction assays, perturbation of LDB3 or the TRIM genes, and examination of whether the co-abundance pattern tracks cell composition or a specific cellular state.

### Important genes

#### LDB3

- **Related proteins** (co-abundance neighbors): PIGU (0.88), ACBD5 (0.82), TRIM2 (0.82), TRIM3 (0.81); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Focal adhesion sites, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LIM domain binding 3. This gene encodes a PDZ domain-containing protein. PDZ motifs are modular protein-protein interaction domains consisting of 80-120 amino acid residues. PDZ domain-containing proteins interact with each other in cytoskeletal assembly or with other proteins involved in targeting and clustering of membrane proteins. The protein encoded by this gene interacts with alpha-actinin-2 through its N-termina…
- **Diseases (Open Targets)**: myofibrillar myopathy 4 (0.781); hypertrophic cardiomyopathy (0.735); cardiomyopathy, dilated, 2l (0.606); left ventricular noncompaction (0.593); atrial fibrillation (0.490)
- **Europe PMC papers**: 1388
- **Why important**: LDB3 is the central network hub, connecting to every other module gene, and is the most direct candidate for organizing the module's structure. Its PDZ and LIM domain functions, focal-adhesion and cytosolic localization, and annotations for heart development, actin-cytoskeleton organization, and muscle structure development provide a coherent structural context. Its extensive literature and associations with several cardiomyopathies and myofibrillar myopathy make it biologically and clinically important.
- **Conclusion**: Established evidence supports LDB3 as a cytoskeletal and muscle-associated hub with substantial disease relevance. The hypothesis that it coordinates the other module genes is suggested by network position but is not established by the listed physical-interaction resources.

#### TRIM2

- **Related proteins** (co-abundance neighbors): LDB3 (0.82); STRING partners: TRIM3 (0.709)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Centrosome; IHC detected in none
- **hu.MAP 3.0**: huMAP3_03664.1, huMAP3_09516.1, huMAP3_10203.1
- **Function (MyGene.info)**: tripartite motif containing 2. The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein localizes to cytoplasmic filaments. It plays a neuroprotective role and functions as an E3-ubiquitin ligase in proteasome-mediated degradation of target proteins. Mutations in this ge…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease type 2R (0.703); refractive error (0.317); Tietze syndrome (0.211); cardiomyopathy (0.203); thyrotoxic periodic paralysis (0.201)
- **Europe PMC papers**: 980
- **Why important**: TRIM2 is one half of the only STRING-supported gene pair and occurs with TRIM3 in every listed hu.MAP complex (hu.MAP huMAP3_03664.1), (hu.MAP huMAP3_09516.1), and (hu.MAP huMAP3_10203.1). The STRING domain terms (STRING SMART B-Box C-terminal domain; within-query FDR = 0.009) through (STRING InterPro Zinc finger, RING-type, eukaryotic; within-query FDR = 0.0457) support shared TRIM-family architecture. Its reported E3-ubiquitin-ligase and proteasome-related functions, cytoplasmic-filament localization, neuroprotective role, and association with early-onset axonal neuropathy make it a strong functional anchor.
- **Conclusion**: Established evidence supports TRIM2 as a ubiquitin-system and filament-associated protein that is closely related to TRIM3. Its proposed connection to LDB3 in this module remains a co-abundance hypothesis rather than a demonstrated direct interaction.

#### TRIM3

- **Related proteins** (co-abundance neighbors): LDB3 (0.81); STRING partners: TRIM2 (0.709)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_03664.1, huMAP3_09516.1, huMAP3_10203.1
- **Function (MyGene.info)**: tripartite motif containing 3. The protein encoded by this gene is a member of the tripartite motif (TRIM) family, also called the 'RING-B-box-coiled-coil' (RBCC) subgroup of RING finger proteins. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. This protein localizes to cytoplasmic filaments. It is similar to a rat protein which is a specific partner for t…
- **Diseases (Open Targets)**: autism (0.111); neoplasm (0.110); breast cancer (0.105); breast carcinoma (0.105); gastric cancer (0.087)
- **Europe PMC papers**: 751
- **Why important**: TRIM3 is the partner of TRIM2 in STRING and in all listed hu.MAP complexes (hu.MAP huMAP3_03664.1), (hu.MAP huMAP3_09516.1), and (hu.MAP huMAP3_10203.1), while sharing the complete set of supplementary domain annotations (STRING SMART B-Box C-terminal domain; within-query FDR = 0.009) through (STRING InterPro Zinc finger, RING-type, eukaryotic; within-query FDR = 0.0457). Its reported roles include protein ubiquitination, proteasome-mediated catabolism, nervous-system development, neural precursor proliferation, and positive regulation of toll-like receptor three signaling. Its brain-enriched HPA profile and substantial literature further support its importance.
- **Conclusion**: Established evidence supports TRIM3 as a TRIM-family protein associated with ubiquitin-dependent regulation and neural biology. Its role as a bridge between the known TRIM pair and the LDB3-centered co-abundance pattern is plausible but unproven.

#### ACBD5

- **Related proteins** (co-abundance neighbors): LDB3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Peroxisomes; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA binding domain containing 5. This gene encodes a member of the acyl-Coenzyme A binding protein family, known to function in the transport and distribution of long chain acyl-Coenzyme A in cells. This gene may play a role in the differentiation of megakaryocytes and formation of platelets. A related protein in yeast is involved in autophagy of peroxisomes. A mutation in this gene has been associated with autosomal dominant thr…
- **Diseases (Open Targets)**: retinal dystrophy with leukodystrophy (0.695); acyl-CoA binding domain containing protein 5 deficiency (0.462); hyperinsulinemic hypoglycemia, familial, 4 (0.372); retinal disorder (0.341); Alzheimer disease (0.267)
- **Europe PMC papers**: 431
- **Why important**: ACBD5 supplies a distinct organelle and metabolic dimension to the module. It is localized to peroxisomes and is annotated for acyl-CoA handling, fatty-acid metabolism, fatty-acid catabolism, and pexophagy. Its disease associations include retinal dystrophy with leukodystrophy and ACBD5 deficiency, and HPA identifies cell-type enhancement in epicardial and retinal pigment epithelial cells. It is connected to the central LDB3 hub in the co-abundance graph.
- **Conclusion**: Established evidence supports ACBD5 as a peroxisomal lipid-handling and organelle-quality-control protein with disease relevance. Its relationship with LDB3 and the TRIM pair is currently a module-level association, not an established molecular mechanism.

#### PIGU

- **Related proteins** (co-abundance neighbors): LDB3 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphatidylinositol glycan anchor biosynthesis class U. The protein encoded by this gene shares similarity with Saccharomyces cerevisiae Cdc91, a predicted integral membrane protein that may function in cell division control. The protein encoded by this gene is the fifth subunit of GPI transamidase that attaches GPI-anchors to proteins. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: glycosylphosphatidylinositol biosynthesis defect 21 (0.695); skin neoplasm (0.312); skin cancer (0.302); skin disorder (0.280); basal cell carcinoma (0.276)
- **Europe PMC papers**: 388
- **Why important**: PIGU represents the membrane-biogenesis component of the module. It is a subunit of the GPI transamidase machinery and is annotated for GPI-anchor biosynthesis, attachment of GPI anchors to proteins, and receptor-signaling regulation. It is detected in breast by HPA, connects directly to LDB3 in the module graph, and has disease associations with a glycosylphosphatidylinositol-biosynthesis defect and several skin-related conditions.
- **Conclusion**: Established evidence supports PIGU as a GPI-anchor biosynthesis factor. Its direct co-abundance with LDB3 may reflect coordinated membrane and cytoskeletal state, but there is no listed evidence that PIGU physically interacts with LDB3 or with either TRIM protein.

## Module 7

**Tissue pair**: breast and cell line  
**Genes (10)**: ADA2, MAOA, CCNL1, DLG3, FUNDC1, NIPSNAP3A, POLR2D, SHROOM2, TEP1, TNRC18

### Function

No GO/KEGG term passed global correction, so there is no globally supported pathway or biological-process enrichment for this module. The module is best interpreted as a sparse co-abundance pattern linking several otherwise distinct biological programs rather than as a demonstrated canonical complex. FUNDC1 and NIPSNAP3A provide a mitochondrial quality-control and mitophagy axis; MAOA represents mitochondrial amine metabolism; POLR2D and CCNL1 represent RNA polymerase II transcription and transcriptional or splicing regulation; SHROOM2 represents actin organization, epithelial polarity, cell morphogenesis, and migration; ADA2 represents secreted adenosine metabolism and immune-cell differentiation; TEP1 represents telomere-associated ribonucleoprotein biology; and DLG3 and TNRC18 contribute scaffold, polarity, chromatin, or localization-related functions. The network therefore suggests coordinated cellular-state variation involving mitochondrial status, transcriptional regulation, structural organization, and cell-type composition, but it does not establish a single molecular pathway.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: ADA2 is the only secreted gene. It is also not broadly characterized as a blood-cell module. Most genes have low immune-cell specificity, several are not detected in immune cells, and only TNRC18 is immune-cell enhanced; ADA2 is tissue enhanced in lymphoid tissue and has immune-related single-cell annotations. The HPA single-cell annotations are heterogeneous, including megakaryocytes, oocytes, parietal cells, rod photoreceptors, cDCs, and other specialized cell types. Four genes are tissue enhanced in distinct tissues, while the remainder have low tissue specificity. Thus, the shared breast and cell-line signal may reflect broadly varying cellular states or mixed cell-type contributions rather than a uniform breast-specific program. Protein detection in breast supports expression of only part of the module and does not establish coordinated protein abundance.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair met the supplied high-confidence STRING interaction criterion, and there are no reported STRING functional-enrichment terms. No hu.MAP complex contains multiple module members. Consequently, the co-abundance relationships are not corroborated here as known physical protein interactions or membership in a recognized multiprotein complex. The weighted links may instead reflect correlated expression, shared regulation, cellular composition, stress state, or indirect biology. In particular, the central position of FUNDC1 is a network property and should not be interpreted as proof that it physically binds its listed neighbors.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is potentially novel as a cross-tissue co-abundance pattern because it combines genes from mitochondrial quality control, amine metabolism, transcription, cell architecture, immune signaling, and telomere biology without support from a known STRING interaction network or a shared hu.MAP complex. However, absence from those resources does not prove biological novelty: the pattern could arise from indirect regulation, correlated cell composition, technical or context-dependent expression, or limited database coverage. The lack of globally significant GO/KEGG enrichment also prevents claiming discovery of a new pathway. A defensible conclusion is that the co-abundance pattern is an interesting, currently unvalidated association requiring replication and perturbational or protein-level testing.

**Hypothesis.** Hypothesis: in breast and cell-line samples, a shared cellular-state program couples mitochondrial quality control and oxidative metabolism with transcriptional adaptation, structural remodeling, and selected immune or secretory signals. FUNDC1 may mark the mitochondrial-state component, while POLR2D and CCNL1 may reflect transcriptional responsiveness, SHROOM2 may reflect changes in cytoskeletal or epithelial organization, and ADA2 may report an associated immune or secretory context. MAOA and NIPSNAP3A provide additional mitochondrial or vesicular-state readouts. This model is mechanistic only as a hypothesis: the current evidence supports co-abundance and individual gene functions, not causal direction, direct binding, or a unified pathway.

### Important genes

#### FUNDC1

- **Related proteins** (co-abundance neighbors): MAOA (0.87), SHROOM2 (0.86), TEP1 (0.81), DLG3 (0.81), POLR2D (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FUN14 domain containing 1. This gene encodes a protein with a FUN14 superfamily domain. The function of the encoded protein is not known. [provided by RefSeq, Sep 2011].
- **Diseases (Open Targets)**: neoplasm (0.094); cancer (0.089); hepatocellular carcinoma (0.086); breast cancer (0.083); hydrops fetalis (0.082)
- **Europe PMC papers**: 3114
- **Why important**: FUNDC1 has the strongest network position in the module and connects to genes spanning mitochondrial, transcriptional, structural, and telomere-related annotations. Its established annotations include mitophagy, mitochondrial fusion, autophagy of mitochondria, and response to hypoxia. It is detected in breast by HPA, has low tissue specificity, and has substantial literature coverage. These features make it the most informative candidate marker of a mitochondrial cellular-state component, while its cancer and breast-cancer associations provide context rather than proof of a role in this module.
- **Conclusion**: Established: FUNDC1 is a mitochondrial FUN14-domain protein associated with mitophagy and mitochondrial stress-related biology, and it is the most connected member of this co-abundance subgraph. Hypothesis: it may organize or report the module's mitochondrial-state signal. The data do not establish that FUNDC1 regulates the other genes or physically interacts with them.

#### ADA2

- **Related proteins** (co-abundance neighbors): POLR2D (0.87), NIPSNAP3A (0.85), CCNL1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenosine deaminase 2. This gene encodes a member of a subfamily of the adenosine deaminase protein family. The encoded protein is one of two adenosine deaminases found in humans, which regulate levels of the signaling molecule, adenosine. The encoded protein is secreted from monocytes undergoing differentiation and may regulate cell proliferation and differentiation. This gene may be responsible for some of the phenoty…
- **Diseases (Open Targets)**: polyarteritis nodosa, childhoood-onset (0.819); Sneddon syndrome (0.771); Diamond-Blackfan anemia (0.597); autoinflammatory syndrome (0.507); Behcet disease (0.477)
- **Europe PMC papers**: 2846
- **Why important**: ADA2 is a connected intermediate in the network and is the only secreted member. It regulates adenosine-related metabolism, is secreted by differentiating monocytes, and may influence cell proliferation and differentiation. HPA places it in a lymphoid-tissue context and annotates it in dendritic, macrophage, Kupffer-cell, and monocyte-progenitor populations. Its disease associations are particularly strong for inflammatory and vasculitic disorders, and it has substantial literature coverage. It therefore provides a biologically distinctive link between the module and extracellular or immune context.
- **Conclusion**: Established: ADA2 is a secreted adenosine deaminase associated with immune-cell differentiation and inflammatory disease. Hypothesis: ADA2 may reflect a paracrine or cell-composition component of the shared module rather than a core intracellular member. The evidence does not show that ADA2 directly drives the module or forms a complex with its neighbors.

#### MAOA

- **Related proteins** (co-abundance neighbors): FUNDC1 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Mitochondria; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: monoamine oxidase A. This gene is one of two neighboring gene family members that encode mitochondrial enzymes which catalyze the oxidative deamination of amines, such as dopamine, norepinephrine, and serotonin. Mutation of this gene results in Brunner syndrome. This gene has also been associated with a variety of other psychiatric disorders, including antisocial behavior. Alternatively spliced transcript variants enc…
- **Diseases (Open Targets)**: Brunner syndrome (0.788); major depressive disorder (0.613); depressive disorder (0.544); hypertensive disorder (0.464); hereditary disease (0.451)
- **Europe PMC papers**: 7415
- **Why important**: MAOA connects directly to FUNDC1 and supplies a well-established mitochondrial metabolic function. It catalyzes oxidative deamination of biogenic amines, including dopamine, norepinephrine, and serotonin. HPA detects it in breast and places it in an intestine-enhanced context, with broad specialized-cell annotations. It has extensive literature coverage and well-established disease associations, including Brunner syndrome and psychiatric disorders. Its presence helps distinguish the module from a purely transcriptional or structural signal.
- **Conclusion**: Established: MAOA is a mitochondrial amine-metabolizing enzyme with strong literature and disease evidence. Hypothesis: its co-abundance with FUNDC1 may indicate coordinated variation in mitochondrial metabolic and quality-control states. The module does not demonstrate a direct functional connection between MAOA and FUNDC1.

#### SHROOM2

- **Related proteins** (co-abundance neighbors): FUNDC1 (0.86), TNRC18 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: shroom family member 2. This gene represents the human homolog of Xenopus laevis apical protein (APX) gene, which is implicated in amiloride-sensitive sodium channel activity. It is expressed in endothelial cells and facilitates the formation of a contractile network within endothelial cells. Depletion of this gene results in an increase in endothelial sprouting, migration, and angiogenesis. This gene is highly expressed…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); colorectal cancer (0.453); prostate carcinoma (0.411); colorectal adenocarcinoma (0.343); Meniere disease (0.266)
- **Europe PMC papers**: 477
- **Why important**: SHROOM2 links FUNDC1 to TNRC18 and is the principal structural or cell-architecture candidate in the module. Its established annotations include actin-filament organization, cell morphogenesis, epithelial polarity, cell migration, and endothelial contractile-network formation. HPA places it at the plasma membrane and cell junctions, with enrichment in retina and several specialized cell types, while it is not detected in immune cells and is not detected in breast by the supplied IHC evidence. Its disease and cancer associations are more limited than those of MAOA, but its function is highly informative for interpreting the module's structural component.
- **Conclusion**: Established: SHROOM2 is a cell-architecture and actin-associated protein involved in polarity, morphogenesis, migration, and endothelial behavior. Hypothesis: its co-abundance may indicate changes in epithelial or cytoskeletal state that accompany mitochondrial remodeling. The lack of breast protein detection argues for caution when treating it as a breast-protein marker.

#### POLR2D

- **Related proteins** (co-abundance neighbors): ADA2 (0.87), FUNDC1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase II subunit D. This gene encodes the fourth largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. In yeast, this polymerase subunit is associated with the polymerase under suboptimal growth conditions and may have a stress protective role. A sequence for a ribosomal pseudogene is contained within the 3' untranslated region of the transcript from this gene.…
- **Diseases (Open Targets)**: HIV infectious disease (0.600); acrocephalosyndactyly (0.370); dengue disease (0.370); Orthomyxoviridae infectious disease (0.370); Alzheimer disease (0.235)
- **Europe PMC papers**: 361
- **Why important**: POLR2D is linked to ADA2 and FUNDC1 and represents a fundamental transcriptional machinery component. It is a subunit of RNA polymerase II, with annotations covering transcription initiation and elongation. HPA reports nucleoplasmic and nuclear-speckle localization, testis tissue enhancement, and detection in breast. Although its literature volume is lower than that of the more intensively studied candidates, its core role makes it a plausible readout of transcriptional state rather than a specialized secreted or immune marker.
- **Conclusion**: Established: POLR2D is an RNA polymerase II subunit involved in messenger-RNA transcription. Hypothesis: its co-abundance may reflect transcriptional adaptation accompanying mitochondrial or cellular-state changes. The evidence does not show that POLR2D specifically regulates the other module genes.

## Module 8

**Tissue pair**: breast and cell line  
**Genes (28)**: AEBP1, ALDH1L2, ATP9B, BBS1, BBX, CPNE2, CPTP, DYNC2LI1, DCUN1D3, DPH6, FMNL3, HLA-F, ICAM3, ITFG2, KDF1, MTARC1, MMAA, R3HDM1, RGS12, RAPGEF1, RUSC1, SAMD9L, SCD5, SMIM13, SORCS2, TMEM63A, TMC4, TMPPE

### Function

The module does not have a single statistically established GO or KEGG function: no term passed global correction, and there are no supplementary STRING enrichment terms. Its strongest biological signals are therefore annotation-based and heterogeneous rather than enrichment-based. BBS1 is the central co-abundance hub and is associated with cilium assembly, intracellular protein localization, Golgi-to-plasma-membrane transport, photoreceptor maintenance, and Bardet-Biedl syndrome. Other module members point to lipid handling and vesicle biology through CPTP, ATP9B, and SCD5; signal regulation through RAPGEF1 and RGS12; cytoskeletal remodeling through FMNL3; lysosomal nutrient sensing through ITFG2; immune adhesion through ICAM3; and neuronal or ciliary biology through SORCS2, DYNC2LI1, TMEM63A, and related genes. The most defensible interpretation is a mixed membrane-trafficking, organelle, signaling, and cell-state co-abundance module rather than a defined canonical pathway.

**Cell composition.** The HPA profile is mixed. The largest tissue category is low tissue specificity, while many genes are tissue or cell-type enhanced, especially in brain-related cell types, epithelial populations, and some immune populations. Brain-associated signals include SORCS2, R3HDM1, SMIM13, TMEM63A, and SCD5, whereas ICAM3, RAPGEF1, SAMD9L, HLA-F, MTARC1, and FMNL3 provide immune or hematopoietic associations. The module is not predominantly composed of plasma or secreted proteins: only AEBP1 is annotated as secreted with unknown location. It is also not convincingly a blood-cell module, because most genes have low immune-cell specificity, although immune-associated genes could reflect shared cellular composition. Breast protein detection is present for many members, whereas the cell-line comparison has no matching HPA tissue protein-detection evidence. The shared signal may therefore reflect a mixture of broadly expressed membrane and organelle biology with contributions from particular cell states rather than a breast-specific secreted program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no STRING functional-enrichment result. Thus, the co-abundance edges should not be interpreted as established physical protein interactions. hu.MAP provides one limited complex observation, (hu.MAP huMAP3_15126.1), in which TMPPE and TMC4 occur together within a much larger annotated complex. Because only a small subset of that complex is represented in the module and the listed complex has limited confidence, (hu.MAP huMAP3_15126.1) supports a possible membrane-associated relationship but does not define the module. The absence of STRING links and the sparse, tree-like co-abundance structure indicate that the module is not simply recovering a well-established protein complex.

**STRING interactions (score >= 0.7)**: 0 of 378 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15126.1 (TMPPE, TMC4; 2/82)

### Novelty

This pattern may be a dataset-specific co-abundance association, but it cannot be called a newly discovered biological pathway or complex. The absence of STRING interactions and the limited hu.MAP overlap make the coordinated pattern less familiar in current interaction resources, yet database absence alone is not evidence of novelty. The lack of globally significant GO or KEGG enrichment, the absence of STRING enrichment, and the broad mixture of ciliary, lipid, immune, epithelial, neuronal, and metabolic annotations argue for cautious novelty claims. A reasonable conclusion is that the module is potentially novel as a cross-tissue co-abundance pattern, while its biological mechanism remains unestablished and requires replication, cell-composition adjustment, and orthogonal experiments.

**Hypothesis.** Hypothesis: the module reflects coordinated variation in membrane and organelle homeostasis across shared cellular states in breast samples and cell lines. BBS1-centered trafficking and ciliary biology may be coupled to ATP9B- and CPTP-related lipid movement, SCD5-dependent membrane lipid composition, ITFG2-linked lysosomal nutrient sensing, and signaling or adhesion processes involving RAPGEF1, RGS12, and ICAM3. SORCS2 and other brain-associated genes may indicate a shared vesicular or cell-state program rather than neuronal tissue contamination specifically. This hypothesis predicts that the module will weaken after careful adjustment for cell composition and will show partial preservation under perturbations affecting membrane trafficking, lipid balance, or lysosomal signaling. These mechanistic links are hypotheses, not established conclusions from the current co-abundance data.

### Important genes

#### BBS1

- **Related proteins** (co-abundance neighbors): R3HDM1 (0.97), SAMD9L (0.90), MTARC1 (0.90), TMEM63A (0.88), ATP9B (0.86), ALDH1L2 (0.86), CPNE2 (0.85), DCUN1D3 (0.83), ITFG2 (0.83), MMAA (0.82), BBX (0.82), HLA-F (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Midbody; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Bardet-Biedl syndrome 1. Mutations in this gene have been observed in patients with the major form (type 1) of Bardet-Biedl syndrome. The encoded protein may play a role in eye, limb, cardiac and reproductive system development. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: Bardet-Biedl syndrome 1 (0.828); Bardet-Biedl syndrome (0.774); retinitis pigmentosa (0.694); inherited retinal dystrophy (0.560); hereditary disease (0.506)
- **Europe PMC papers**: 2029
- **Why important**: BBS1 is the highest-connectivity hub in the module and links many otherwise weakly connected branches. Its established annotations include cilium assembly, photoreceptor maintenance, intracellular protein localization, Golgi-to-plasma-membrane transport, and fat-cell differentiation. It is strongly associated with Bardet-Biedl syndrome and retinal disease, and it has a substantial literature base. Its hub position makes it the best network-level anchor, although hub status in a co-abundance graph does not prove biochemical control.
- **Conclusion**: Established evidence supports BBS1 as a ciliary and intracellular-trafficking gene with major disease relevance and as the central statistical organizer of this module. It is plausible, but unproven, that BBS1-linked trafficking biology helps organize the shared co-abundance signal.

#### ATP9B

- **Related proteins** (co-abundance neighbors): BBS1 (0.86), CPTP (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase phospholipid transporting 9B. Predicted to enable ATPase-coupled intramembrane lipid transporter activity. Predicted to be involved in endocytosis; phospholipid translocation; and retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum. Located in perinuclear region of cytoplasm and trans-Golgi network. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypopituitarism (0.316); response to stimulus (0.248); adverse effect (0.248); Pancreatic pseudocyst (0.242); femur fracture (0.205)
- **Europe PMC papers**: 261
- **Why important**: ATP9B connects the BBS1 branch to CPTP and is annotated for phospholipid transport, phospholipid translocation, endocytosis, and retrograde Golgi-to-endoplasmic-reticulum transport. It is detected in breast tissue and provides a direct functional bridge between membrane lipid handling and intracellular trafficking. Its literature base is smaller than that of BBS1 or ICAM3, making it informative but less established as a disease or pathway marker.
- **Conclusion**: Established evidence supports ATP9B as a predicted phospholipid transporter involved in membrane and vesicle processes. Its position and annotation support a membrane-homeostasis interpretation, but the module does not establish that ATP9B mechanistically drives the co-abundance pattern.

#### CPTP

- **Related proteins** (co-abundance neighbors): ICAM3 (0.87), RAPGEF1 (0.86), ATP9B (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Flagellar centriole, Mid piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ceramide-1-phosphate transfer protein. Enables ceramide 1-phosphate binding activity and ceramide 1-phosphate transfer activity. Involved in several processes, including ceramide 1-phosphate transport; negative regulation of NLRP3 inflammasome complex assembly; and negative regulation of interleukin-1 beta production. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: pachyonychia congenita (0.074); neoplasm (0.042); refractive error (0.040); pulmonary embolism (0.030); nerve plexus disorder (0.024)
- **Europe PMC papers**: 453
- **Why important**: CPTP connects ATP9B with ICAM3 and is annotated for ceramide-phosphate binding and transfer, ceramide transport, glycolipid transport, and negative regulation of inflammatory processes including NLRP3 inflammasome assembly and interleukin one beta production. It therefore provides a mechanistic link between lipid trafficking and inflammatory signaling. Its disease evidence is more limited than its functional annotation, but its literature base is meaningful.
- **Conclusion**: Established evidence supports CPTP as a ceramide-phosphate and inflammatory-regulation protein. It is a credible candidate for coupling membrane lipid state to immune signaling in the module, but that coupling remains a hypothesis because no enrichment or physical interaction evidence supports it here.

#### ICAM3

- **Related proteins** (co-abundance neighbors): CPTP (0.87), SMIM13 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: intercellular adhesion molecule 3. The protein encoded by this gene is a member of the intercellular adhesion molecule (ICAM) family. All ICAM proteins are type I transmembrane glycoproteins, contain 2-9 immunoglobulin-like C2-type domains, and bind to the leukocyte adhesion LFA-1 protein. This protein is constitutively and abundantly expressed by all leucocytes and may be the most important ligand for LFA-1 in the initiation of th…
- **Diseases (Open Targets)**: lymphatic system disorder (0.227); rheumatoid arthritis (0.079); severe acute respiratory syndrome (0.067); cancer (0.059); chronic rhinosinusitis with nasal polyps (0.055)
- **Europe PMC papers**: 1777
- **Why important**: ICAM3 is tissue enhanced in bone marrow and lymphoid tissue, is associated with leukocytes and neutrophils, and connects the CPTP branch with SMIM13. Its established functions include leukocyte adhesion, integrin-mediated signaling, immune response, and regulation of lymphocyte-related interactions. It has a large literature base and clear relevance to immune-cell composition, making it important for interpreting whether the module reflects shared cell types.
- **Conclusion**: Established evidence supports ICAM3 as an immune-cell adhesion and signaling molecule. It may mark an immune contribution to the module or shared sample composition, but it should not be taken as evidence that the entire module is an immune pathway.

#### SORCS2

- **Related proteins** (co-abundance neighbors): CPNE2 (0.84), FMNL3 (0.83), DPH6 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sortilin related VPS10 domain containing receptor 2. This gene encodes one family member of vacuolar protein sorting 10 (VPS10) domain-containing receptor proteins. The VPS10 domain name comes from the yeast carboxypeptidase Y sorting receptor Vps10 protein. Members of this gene family are large with many exons but the CDS lengths are usually less than 3700 nt. Very large introns typically separate the exons encoding the VPS10 domain; the remaining …
- **Diseases (Open Targets)**: osteoarthritis (0.338); alcohol drinking (0.311); risk-taking behaviour (0.282); Back pain (0.273); type 2 diabetes mellitus (0.259)
- **Europe PMC papers**: 1127
- **Why important**: SORCS2 connects CPNE2 and FMNL3 and is tissue enhanced in brain, with cell-type associations across glial populations and renal collecting duct principal cells. Its established annotations include intracellular protein transport, neuropeptide signaling, and long-term synaptic depression. It has a substantial literature base and represents the prominent neuronal or vesicular side of the module.
- **Conclusion**: Established evidence supports SORCS2 as a VPS10-domain sorting receptor associated with intracellular transport and neuronal signaling. Its presence supports a vesicle-trafficking interpretation, but its brain-associated expression could also reflect cell-state composition rather than a mechanism shared by breast and cell-line samples.

#### ITFG2

- **Related proteins** (co-abundance neighbors): BBS1 (0.83), KDF1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin alpha FG-GAP repeat containing 2. Involved in cellular response to amino acid starvation; cellular response to glucose starvation; and negative regulation of TORC1 signaling. Located in lysosomal membrane. Part of KICSTOR complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.266); neurodegenerative disease (0.258); Graves disease (0.198); cerebellar ataxia (0.186); Intellectual disability (0.185)
- **Europe PMC papers**: 187
- **Why important**: ITFG2 connects BBS1 with KDF1 and is annotated as a lysosomal membrane component, a member of the KICSTOR complex, and a regulator of TORC1 responses to amino-acid and glucose starvation. It is detected in breast tissue and provides a nutrient-sensing and lysosomal axis that complements the module’s trafficking and lipid annotations. Its literature and disease-association evidence are more limited than those of the major hub genes.
- **Conclusion**: Established evidence supports ITFG2 as a lysosomal nutrient-response component involved in negative regulation of TORC1. It is a plausible link between metabolic state and membrane-organelle co-abundance, but the current data do not establish that lysosomal nutrient sensing is the module’s primary function.

## Module 9

**Tissue pair**: breast and cell line  
**Genes (16)**: AGK, ALKBH1, ANO6, ARID2, UGCG, DHFR, FASTKD1, HACD2, MED16, NBEA, NLRX1, PIGM, PTPRCAP, TCAF2, TMEM186, TMEM223

### Function

No GO/KEGG term passed global correction, and STRING returned no supplementary functional enrichment. Therefore, the module does not support a single established pathway-level function. Its gene-level annotations suggest a heterogeneous theme involving membrane and organelle biology, mitochondrial processes, lipid and glycosphingolipid metabolism, nucleic-acid regulation, transcriptional control, and immune or membrane-signaling functions. TMEM186 is the main co-abundance hub and connects genes from these different functional areas, but this topology does not establish physical interaction or a unified biochemical pathway. The most defensible interpretation is a conserved co-abundance state associated with membrane-organelle homeostasis and cellular state, rather than a proven canonical complex or pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only one member is annotated as secreted, and most members have low tissue specificity. It is also not broadly characterized as a blood-cell module, because most genes have low immune-cell specificity and only a minority show immune-cell enhancement or enrichment. Nevertheless, HPA indicates substantial cell-type specificity across diverse populations, including epithelial, neuronal, adipocyte, muscle, platelet, and selected immune-cell populations. UGCG has bone-marrow and plasmacytoid-dendritic-cell associations, PTPRCAP is enriched in intestine and lymphoid tissue and is linked to lymphocyte biology, and ANO6 is associated with platelets. These signals could reflect shared cellular composition or sample-state effects rather than a breast-specific program. Protein detection in breast is present for many members, whereas the cell-line comparison has no matching HPA tissue-protein assessment.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING relationships among the module members, and no hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not corroborated as known protein-protein interactions or as membership in a known multi-protein complex. This weakens a direct physical-complex interpretation but does not invalidate the co-abundance module: coordinated regulation, shared organelle dependence, membrane composition, cell state, or indirect cellular-composition effects can produce co-abundance without documented physical interaction. The absence of STRING and hu.MAP support should therefore be interpreted as evidence that the module is not explained by a currently catalogued interaction complex.

**STRING interactions (score >= 0.7)**: 0 of 120 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a new co-abundance association because its members form a cross-functional pattern with no recorded high-confidence STRING links, no shared hu.MAP complex, and no globally significant GO/KEGG enrichment. However, it cannot be called a newly discovered biological pathway or mechanism on these data alone. The lack of database support is not proof of novelty; it may reflect indirect regulation, tissue or cell-state composition, incomplete interaction databases, or a statistical association that does not correspond to a physical mechanism. The appropriate conclusion is that this is a novel or under-characterized network-level observation requiring independent replication and perturbation testing.

**Hypothesis.** Hypothesis: the conserved breast–cell-line module reflects coordinated regulation of membrane and organelle homeostasis in a shared cellular state. TMEM186 may mark the central co-abundance axis linking mitochondrial functions, lipid handling, membrane trafficking, and regulatory genes, while UGCG, PIGM, HACD2, and AGK contribute to lipid, glycosphingolipid, GPI-anchor, and glycerolipid processes. NLRX1 and FASTKD1 could connect the state to mitochondrial signaling and mitochondrial RNA control, whereas ANO6 and PTPRCAP may represent membrane remodeling or immune-associated components. This model predicts coordinated changes in membrane lipid composition, mitochondrial function, and cell-surface signaling, but it remains a hypothesis rather than an established mechanism.

### Important genes

#### TMEM186

- **Related proteins** (co-abundance neighbors): ALKBH1 (0.87), TCAF2 (0.86), ARID2 (0.85), HACD2 (0.83), NLRX1 (0.83), DHFR (0.82), AGK (0.82), ANO6 (0.81), FASTKD1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transmembrane protein 186. This gene encodes a potential transmembrane protein. [provided by RefSeq, Dec 2012].
- **Diseases (Open Targets)**: GABA aminotransaminase deficiency (0.515); PMM2-congenital disorder of glycosylation (0.379); hereditary disease (0.183); primary thrombocytopenia (0.080); osteonecrosis (0.057)
- **Europe PMC papers**: 186
- **Why important**: TMEM186 is the central network hub, connecting genes involved in mitochondrial biology, lipid metabolism, membrane transport, DNA or RNA-related regulation, and signaling. Its low tissue specificity is compatible with a broadly shared cellular program, while its annotated mitochondrial respiratory-chain assembly function provides a plausible organelle-level anchor. It has comparatively substantial literature support among the less characterized membrane genes.
- **Conclusion**: Established evidence supports TMEM186 as the principal co-abundance connector and as a potential transmembrane protein with an annotation related to mitochondrial respiratory-chain assembly. It is not established that TMEM186 mechanistically coordinates the other module members; that coordinating role is a hypothesis based on network position.

#### UGCG

- **Related proteins** (co-abundance neighbors): PIGM (0.87), TCAF2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UDP-glucose ceramide glucosyltransferase. This gene encodes an enzyme that catalyzes the first glycosylation step in the biosynthesis of glycosphingolipids, which are membrane components containing lipid and sugar moieties. The product of this reaction is glucosylceramide, which is the core structure of many glycosphingolipids. [provided by RefSeq, Dec 2014].
- **Diseases (Open Targets)**: Gaucher disease (0.576); Gaucher disease type I (0.503); Niemann-Pick disease type C (0.501); glycogen storage disease II (0.494); Fabry disease (0.390)
- **Europe PMC papers**: 1536
- **Why important**: UGCG is a biochemical anchor for the membrane-lipid interpretation. It catalyzes the first glycosylation step in glycosphingolipid biosynthesis, is linked to glucosylceramide production, and connects in the module to PIGM and TCAF2. HPA associates it with bone marrow, plasmacytoid dendritic cells, and several epithelial populations, making it relevant both to membrane biology and to possible cellular-composition effects. Its disease associations include lysosomal storage disorders, and it has a substantial literature base.
- **Conclusion**: Established evidence supports UGCG as a glycosphingolipid-biosynthesis enzyme and as a biologically important membrane-metabolism gene. Its presence supports lipid-membrane involvement but does not demonstrate that glycosphingolipid metabolism is enriched at the module level, because no GO/KEGG term passed global correction.

#### ANO6

- **Related proteins** (co-abundance neighbors): TMEM186 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: anoctamin 6. This gene encodes a multi-pass transmembrane protein that belongs to the anoctamin family. This protein is an essential component for the calcium-dependent exposure of phosphatidylserine on the cell surface. The scrambling of phospholipid occurs in various biological systems, such as when blood platelets are activated, they expose phosphatidylserine to trigger the clotting system. Mutations in thi…
- **Diseases (Open Targets)**: Scott syndrome (0.713); COVID-19 (0.372); alcohol drinking (0.327); hydrocephalus, nonsyndromic, autosomal recessive 2 (0.266); Congenital muscular alpha-dystroglycanopathy with brain and eye anomalies (0.266)
- **Europe PMC papers**: 812
- **Why important**: ANO6 provides a strong membrane-remodeling and platelet-related connection. It is a calcium-dependent phospholipid scramblase, participates in phosphatidylserine exposure and coagulation, and is associated with Scott syndrome. It is detected in breast and shows cell-type enhancement in adipocytes, myonuclei, and platelets. Its position as a peripheral neighbor of TMEM186 links this established membrane function to the central co-abundance axis.
- **Conclusion**: Established evidence supports ANO6 in plasma-membrane phospholipid scrambling and blood-coagulation biology. Its inclusion may reflect membrane-state regulation or platelet-related composition, but the module does not establish a coagulation function and should not be interpreted as a platelet module without external sample-level validation.

#### NLRX1

- **Related proteins** (co-abundance neighbors): TMEM186 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NLR family member X1. The protein encoded by this gene is a member of the NLR family and localizes to the outer mitochondrial membrane. The encoded protein is a regulator of mitochondrial antivirus responses. Three transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Aug 2013].
- **Diseases (Open Targets)**: neoplasm (0.106); Insulin resistance (0.097); experimental autoimmune encephalomyelitis (0.093); infection (0.092); esophageal squamous cell carcinoma (0.082)
- **Europe PMC papers**: 1629
- **Why important**: NLRX1 contributes a mitochondrial and innate-signaling dimension. It localizes to the outer mitochondrial membrane and is annotated as a negative regulator of antiviral RIG-I signaling and canonical NF-kappa B signaling. It is detected in breast, has esophageal tissue and epithelial associations, and shows immune-cell enhancement in eosinophils. Its substantial literature supports a well-established role in mitochondrial immune regulation.
- **Conclusion**: Established evidence supports NLRX1 as a mitochondrial regulator of antiviral and inflammatory signaling. Its co-abundance with TMEM186 is consistent with a possible mitochondrial cellular-state component, but a direct role for NLRX1 in organizing this module remains hypothetical.

#### DHFR

- **Related proteins** (co-abundance neighbors): TMEM186 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Mitochondria; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dihydrofolate reductase. Dihydrofolate reductase converts dihydrofolate into tetrahydrofolate, a methyl group shuttle required for the de novo synthesis of purines, thymidylic acid, and certain amino acids. While the functional dihydrofolate reductase gene has been mapped to chromosome 5, multiple intronless processed pseudogenes or dihydrofolate reductase-like genes have been identified on separate chromosomes. Dihydrofo…
- **Diseases (Open Targets)**: constitutional megaloblastic anemia with severe neurologic disease (0.785); rheumatoid arthritis (0.618); non-small cell lung carcinoma (0.615); acute lymphoblastic leukemia (0.605); psoriasis (0.596)
- **Europe PMC papers**: 15911
- **Why important**: DHFR is a highly established metabolic and biosynthetic gene connected to TMEM186 in the module. It supports tetrahydrofolate metabolism and the synthesis of nucleotides and amino acids, and it is relevant to DNA replication and megaloblastic anemia. Its very large literature base makes it a robust marker of biosynthetic or proliferative demand, although its broad expression makes it less specific mechanistically.
- **Conclusion**: Established evidence supports DHFR in folate-dependent biosynthesis and nucleotide production. Its module membership may indicate a general biosynthetic or growth-related state rather than a specialized pathway; the co-abundance data do not show that folate metabolism is a module-level enrichment.

#### NBEA

- **Related proteins** (co-abundance neighbors): TCAF2 (0.87), MED16 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neurobeachin. This gene encodes a member of a large, diverse group of A-kinase anchor proteins that target the activity of protein kinase A to specific subcellular sites by binding to its type II regulatory subunits. Brain-specific expression and coat protein-like membrane recruitment of a highly similar protein in mouse suggest an involvement in neuronal post-Golgi membrane traffic. Mutations in this gene may …
- **Diseases (Open Targets)**: neurodevelopmental disorder with or without early-onset generalized epilepsy (0.650); epilepsy, early-onset, with or without developmental delay (0.619); Intellectual disability (0.564); hereditary disease (0.516); cerebellar, ocular, craniofacial, and genital syndrome (0.497)
- **Europe PMC papers**: 780
- **Why important**: NBEA is a distinctive regulatory member because it is tissue-enriched in retina, detected in breast, localized to the Golgi, and annotated in synapse organization and post-Golgi membrane trafficking biology. It connects TCAF2 and MED16, linking membrane trafficking to transcriptional regulation. Its disease associations include neurodevelopmental and epilepsy phenotypes, and it has a comparatively large literature base.
- **Conclusion**: Established evidence supports NBEA as an A-kinase-anchoring and membrane-trafficking-related protein with neurodevelopmental disease associations. Its presence broadens the module beyond a simple lipid or mitochondrial interpretation; any role in the proposed shared membrane-organelle state is a hypothesis.

## Module 10

**Tissue pair**: breast and cell line  
**Genes (6)**: AIMP1, BPHL, PPA2, MRPL42, TMEM106C, TPD52

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING functional enrichment. The module therefore does not support a formally established pathway annotation. Its structure is star-like, with TMEM106C as the central co-abundance hub linking proteins associated with endoplasmic-reticulum membrane biology, translation, mitochondrial function, metabolism, and cell signaling. Established evidence supports a mixed cellular-state module rather than a single demonstrated biological pathway. The shared breast and cell-line signal may reflect coordinated abundance of cellular maintenance, mitochondrial, metabolic, and membrane-associated proteins, but this interpretation remains provisional.

**Cell composition.** All module proteins were detected by HPA in breast, whereas matching HPA tissue information was unavailable for the cell-line context. Most genes have low immune-cell specificity, so the module does not strongly resemble a blood-cell contamination signature. One member, AIMP1, is secreted to blood, and TPD52 is enhanced in memory B cells and several other cell types, but the module as a whole is not predominantly secreted or blood-cell enriched. The HPA pattern is heterogeneous: some members are broadly expressed, while others show enhancement in kidney, liver, retina, enterocytes, adipocytes, hepatocytes, or germ-cell populations. This heterogeneity argues against assigning the module to a single tissue or cell type. The shared module could instead reflect a conserved cellular program, differences in cell composition, or correlated abundance of proteins that are active in distinct compartments.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was identified among the module pairs, and no hu.MAP complex contained multiple module members. Thus, the co-abundance relationships are not supported here by previously catalogued physical or functional interactions at the queried thresholds. The absence of STRING and hu.MAP support does not invalidate the co-abundance module: co-regulation, shared abundance drivers, indirect dependencies, transient interactions, compartmental coordination, or incomplete database coverage could all produce correlated protein levels without a recorded binary interaction or complex membership. TMEM106C is the network hub by co-abundance, but its hub status is specific to this module and is not independently confirmed by the supplied interaction databases.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears to be a potentially under-characterized co-abundance association rather than an established molecular complex or pathway. Its novelty is supported by the lack of overlapping high-confidence STRING interactions, the lack of a multi-member hu.MAP complex, and the lack of a globally significant GO or KEGG term. However, these observations do not prove that the biological relationship is new. The module may represent a context-specific abundance pattern, indirect regulation, or an incompletely annotated combination of known proteins. A claim of discovery would require replication in independent breast and cell-line data, comparison with published co-expression or proteomic modules, and experimental testing of the predicted relationships.

**Hypothesis.** Hypothesis: TMEM106C may coordinate a conserved cellular-state program that links an endoplasmic-reticulum or membrane-associated component with mitochondrial protein synthesis, mitochondrial phosphate and energy homeostasis, metabolic processing, and signaling or secretory responses. In this model, TMEM106C is the abundance-associated organizing feature, while AIMP1 and TPD52 could connect the state to signaling, secretion, angiogenesis, inflammation, proliferation, or B-cell-related biology, and BPHL, MRPL42, and PPA2 could report mitochondrial or metabolic status. This is a mechanistic hypothesis only; the supplied enrichment, STRING, and hu.MAP results do not establish direct physical interaction, causal regulation, or a single pathway.

### Important genes

#### TMEM106C

- **Related proteins** (co-abundance neighbors): AIMP1 (0.92), TPD52 (0.85), MRPL42 (0.82), BPHL (0.81), PPA2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transmembrane protein 106C. Predicted to be located in endoplasmic reticulum membrane. Predicted to be integral component of membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: prostate carcinoma (0.267); hepatocellular carcinoma (0.099); osteoarthritis, hip (0.083); cancer (0.080); alcohol drinking (0.057)
- **Europe PMC papers**: 179
- **Why important**: TMEM106C is the central co-abundance hub and is connected to every other module member, making it the most informative candidate for explaining the module's internal structure. It is annotated as a predicted integral endoplasmic-reticulum membrane protein. Its tissue specificity is low, while its single-cell pattern is enhanced in intestinal and epididymal epithelial populations. It has a moderate literature base and disease associations including prostate carcinoma and hepatocellular carcinoma.
- **Conclusion**: Established evidence: TMEM106C is the network hub and has a predicted endoplasmic-reticulum membrane localization. Hypothesis: it may organize or mark a membrane-linked cellular state that is reflected in mitochondrial, metabolic, and signaling protein abundance. The co-abundance data do not establish that TMEM106C regulates the other genes.

#### AIMP1

- **Related proteins** (co-abundance neighbors): TMEM106C (0.92); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aminoacyl tRNA synthetase complex interacting multifunctional protein 1. The protein encoded by this gene is a cytokine that is specifically induced by apoptosis, and it is involved in the control of angiogenesis, inflammation, and wound healing. The release of this cytokine renders the tumor-associated vasculature sensitive to tumor necrosis factor. The precursor protein is identical to the p43 subunit, which is associated with the multi-tRNA synthetase complex, and i…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 3 (0.790); Pelizaeus-Merzbacher-like disease (0.657); POLR-related leukodystrophy (0.657); leukodystrophy (0.372); autosomal recessive non-syndromic intellectual disability (0.371)
- **Europe PMC papers**: 663
- **Why important**: AIMP1 is the only secreted-to-blood member and has the strongest documented connection to signaling and intercellular biology in the module. It is the p43 component associated with the multi-tRNA synthetase complex and is described as an apoptosis-induced cytokine involved in angiogenesis, inflammation, wound healing, endothelial proliferation, leukocyte migration, and translation-related activity. It is connected directly to the hub and has a substantial literature base, as well as disease associations involving leukodystrophy.
- **Conclusion**: Established evidence: AIMP1 has both intracellular translation-associated and extracellular cytokine-related functions, and its secretion could make abundance sensitive to tissue state or sample composition. Hypothesis: AIMP1 may provide a signaling or secretory bridge between the hub-centered cellular program and extracellular responses. The module does not demonstrate secretion-driven causality or immune contamination.

#### TPD52

- **Related proteins** (co-abundance neighbors): TMEM106C (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tumor protein D52. Enables calcium ion binding activity and protein homodimerization activity. Involved in B cell differentiation. Located in endoplasmic reticulum and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: prostate carcinoma (0.393); rheumatoid arthritis (0.347); skin disorder (0.267); cervical carcinoma (0.256); Parkinson disease (0.252)
- **Europe PMC papers**: 1217
- **Why important**: TPD52 is directly connected to TMEM106C and has the largest literature base among the module members. It is associated with calcium ion binding, homodimerization, secretion, proliferation, anatomical morphogenesis, and B-cell differentiation. HPA shows tissue enhancement in retina and immune-cell enhancement in memory B cells, while also detecting the protein in breast. Its disease associations include cancer and rheumatoid arthritis.
- **Conclusion**: Established evidence: TPD52 is a broadly studied signaling and proliferation-associated protein with a notable memory-B-cell pattern and a direct module connection to TMEM106C. Hypothesis: it may reflect secretory, proliferative, or cell-state variation within breast samples rather than a core biochemical complex. The available evidence does not show that TPD52 drives the module.

#### PPA2

- **Related proteins** (co-abundance neighbors): TMEM106C (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inorganic pyrophosphatase 2. The protein encoded by this gene is localized to the mitochondrion, is highly similar to members of the inorganic pyrophosphatase (PPase) family, and contains the signature sequence essential for the catalytic activity of PPase. PPases catalyze the hydrolysis of pyrophosphate to inorganic phosphate, which is important for the phosphate metabolism of cells. Alternate transcriptional splice variants…
- **Diseases (Open Targets)**: sudden cardiac arrest (0.802); neurodegenerative disease (0.535); hereditary disease (0.513); Abnormality of the cardiovascular system (0.407); dilated cardiomyopathy (0.371)
- **Europe PMC papers**: 1003
- **Why important**: PPA2 is a mitochondrial inorganic pyrophosphatase linked to phosphate and diphosphate metabolism and regulation of mitochondrial membrane potential. It is directly connected to TMEM106C, is detected in breast, and has a substantial literature base. Its disease associations include sudden cardiac arrest, cardiomyopathy, neurodegenerative disease, and other hereditary conditions, making mitochondrial phosphate handling biologically consequential.
- **Conclusion**: Established evidence: PPA2 provides a clear mitochondrial metabolic component and is relevant to membrane potential and disease biology. Hypothesis: its co-abundance with TMEM106C may indicate coordinated mitochondrial and membrane-state variation. The module does not establish a direct interaction between PPA2 and TMEM106C.

#### BPHL

- **Related proteins** (co-abundance neighbors): TMEM106C (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biphenyl hydrolase like. This gene encodes a member of the serine protease family of hydrolytic enzymes which contain a serine in their active site. The encoded protein may play a role in activation of the antiviral prodrug valacyclovir. Alternatively spliced transcript variants have been described.[provided by RefSeq, Jan 2009].
- **Diseases (Open Targets)**: alcohol drinking (0.181); urolithiasis (0.181); handedness (0.164); musculoskeletal system disorder (0.122); tooth disorder (0.109)
- **Europe PMC papers**: 358
- **Why important**: BPHL is directly connected to TMEM106C and encodes a serine hydrolase-family protein associated with amino-acid metabolism, xenobiotic metabolism, toxic-substance response, and homocysteine metabolism. HPA shows enhancement in kidney and liver and in adipocytes, enterocytes, and hepatocytes, giving it a strong metabolic and tissue-context signal. It has more literature than the other less-characterized module members and is linked to possible activation of the antiviral prodrug valacyclovir.
- **Conclusion**: Established evidence: BPHL contributes a tissue-associated metabolic and detoxification interpretation to the module. Hypothesis: BPHL may report metabolic state or substrate-processing capacity that covaries with the hub and mitochondrial proteins. Its presence does not prove that the module is a detoxification pathway.

## Module 11

**Tissue pair**: breast and cell line  
**Genes (24)**: AMPD3, CACNA1A, CRYL1, CXXC1, ESRP2, FRMD8, ICA1, JPH2, KATNB1, LSM8, MEN1, MYSM1, NME4, NAP1L5, NVL, PHYH, PIGQ, ARHGAP17, RNF141, RAPGEF6, SGCB, SNX21, SPAG1, TGFBRAP1

### Function

This is a heterogeneous co-abundance module rather than a coherently annotated pathway. No GO or KEGG term passed global correction, and STRING functional enrichment was absent, so there is no statistically supported pathway-level assignment from enrichment. The network nevertheless contains several functional themes: RAPGEF6 links small-GTPase signaling and membrane localization to multiple otherwise weakly connected genes; CACNA1A, JPH2, and ICA1 suggest calcium-channel, junctional-membrane, and secretory-vesicle biology; SGCB and AMPD3 suggest muscle or erythrocyte-associated biology; and CXXC1, MEN1, MYSM1, LSM8, and NAP1L5 suggest chromatin, transcription, RNA-processing, or nucleosome-related biology. These themes are better viewed as candidate components than as an established unified function.

**Cell composition.** The module is not dominated by plasma or secreted proteins: no member is annotated as secreted. Most genes have low tissue specificity, while the remainder show diverse tissue or cell-type enhancement, including skeletal muscle, brain, liver, bone marrow, kidney, late spermatids, neurons, epithelial cells, and myoid cells. Immune-cell specificity is generally low, with only isolated immune-enriched or group-enriched signals. Protein detection in breast is widespread among the assayed genes, whereas there is no matching HPA tissue for the cell-line context. Overall, the composition does not support a simple plasma-protein or blood-contamination explanation, but the broad and heterogeneous expression pattern means that shared cell composition, common cellular states, or technical co-abundance could contribute.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only one high-confidence relationship within the module, between CXXC1 and MEN1. This is concordant with hu.MAP complex C1, which also contains CXXC1 and MEN1 together with many chromatin and histone-modifying proteins. Thus, the CXXC1–MEN1 pair is an established molecular relationship and supports a chromatin-regulatory component. The remaining module edges are not represented by high-confidence STRING interactions, and no other multi-member hu.MAP complex is reported. Consequently, the network is not a densely known physical interaction complex; its co-abundance structure may reflect co-regulation, shared cellular context, indirect biology, or data-specific association rather than direct binding throughout.

**STRING interactions (score >= 0.7)**: 1 of 276 gene pairs: CXXC1–MEN1 (0.732)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11602.1 (MEN1, CXXC1; 2/25)

### Novelty

The module may represent a previously unreported co-abundance association, but it cannot be called a new biological mechanism from the supplied evidence alone. The limited overlap with STRING and hu.MAP indicates that most module relationships are not established physical interactions in those resources, which makes the overall pattern potentially interesting. However, absence from these databases does not establish novelty: the module could combine known functions through shared expression, cell-type composition, indirect regulation, or technical effects. The strongest defensible claim is that this is a novel candidate association requiring replication and perturbational validation, with the CXXC1–MEN1 relationship already established.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state that couples membrane and vesicle organization, calcium-dependent signaling, cytoskeletal or junctional function, and selective transcriptional or chromatin regulation. RAPGEF6 may act as an organizing signaling hub connecting membrane-associated and trafficking-related proteins, while the CXXC1–MEN1 pair may represent a chromatin-regulatory anchor. The muscle-, neuronal-, epithelial-, and germ-cell-associated HPA patterns suggest that this state may be reused across differentiated cell types rather than being specific to breast biology. This hypothesis should be tested by replication across independent breast and cell-line datasets, cell-type deconvolution, perturbation of RAPGEF6 or the CXXC1–MEN1 axis, and measurement of calcium handling, trafficking, cytoskeletal organization, and transcriptional responses.

### Important genes

#### RAPGEF6

- **Related proteins** (co-abundance neighbors): SNX21 (0.93), CXXC1 (0.87), SPAG1 (0.87), FRMD8 (0.85), NVL (0.84), ESRP2 (0.84), KATNB1 (0.83), TGFBRAP1 (0.83), CRYL1 (0.82), PHYH (0.82), MEN1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rap guanine nucleotide exchange factor 6. Enables several functions, including GTP-dependent protein binding activity; guanyl-nucleotide exchange factor activity; and phosphatidic acid binding activity. Involved in microvillus assembly; positive regulation of GTPase activity; and protein localization to plasma membrane. Located in several cellular components, including apical plasma membrane; centrosome; and endocytic vesicle. [provided b…
- **Diseases (Open Targets)**: asthma (0.349); Crohn disease (0.336); Abnormality of limbs (0.321); nasal cavity polyp (0.268); Abnormality of the skeletal system (0.242)
- **Europe PMC papers**: 342
- **Why important**: RAPGEF6 is the principal network hub, with the greatest connectivity and weighted strength in the module. Its annotated functions include Rap and other small-GTPase signaling, phosphatidic-acid binding, microvillus assembly, and plasma-membrane localization. It connects genes spanning trafficking, signaling, cytoskeletal, ciliary, transcriptional, and metabolic annotations. It also has substantial literature and several disease associations, making it the most informative candidate for testing whether the module has a regulatory core rather than being a passive expression cluster.
- **Conclusion**: Established evidence supports RAPGEF6 as a central network coordinator with small-GTPase and membrane-related functions. It is not established that RAPGEF6 drives the entire module. A reasonable hypothesis is that its abundance links membrane organization and signaling to the other module components.

#### CXXC1

- **Related proteins** (co-abundance neighbors): RAPGEF6 (0.87); STRING partners: MEN1 (0.732)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_11602.1
- **Function (MyGene.info)**: CXXC finger protein 1. This gene encodes a protein that functions as a transcriptional activator that binds specifically to non-methylated CpG motifs through its CXXC domain. The protein is a component of the SETD1 complex, regulates gene expression and is essential for vertebrate development. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); Alzheimer disease (0.370); Parkinson disease (0.370); lysosomal storage disease (0.370); Abnormal pupillary function (0.255)
- **Europe PMC papers**: 545
- **Why important**: CXXC1 is directly connected in STRING to MEN1 and is present with MEN1 in hu.MAP complex C1. It binds non-methylated CpG motifs and participates in the SETD1 complex, chromatin organization, and transcriptional regulation. Its position provides the clearest bridge from the co-abundance module to a known molecular complex, despite its limited direct connectivity within the module.
- **Conclusion**: Established evidence supports CXXC1 as a chromatin-associated transcriptional regulator and as a known partner of MEN1. It is not established that the full module is a SETD1 or MEN1 complex. The chromatin interpretation should therefore be restricted to the CXXC1–MEN1 submodule unless further physical or perturbational evidence is obtained.

#### MEN1

- **Related proteins** (co-abundance neighbors): RAPGEF6 (0.81); STRING partners: CXXC1 (0.732)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_11602.1
- **Function (MyGene.info)**: menin 1. This gene encodes menin, a tumor suppressor associated with a syndrome known as multiple endocrine neoplasia type 1. Menin is a scaffold protein that functions in histone modification and epigenetic gene regulation. It is thought to regulate several pathways and processes by altering chromatin structure through the modification of histones. [provided by RefSeq, May 2019].
- **Diseases (Open Targets)**: multiple endocrine neoplasia type 1 (0.866); parathyroid gland adenoma (0.675); endocrine gland neoplasm (0.663); multiple endocrine neoplasia (0.661); Angiofibroma (0.642)
- **Europe PMC papers**: 7686
- **Why important**: MEN1 encodes menin, a well-established tumor suppressor and scaffold involved in histone modification, epigenetic regulation, transcription, DNA repair, and endocrine neoplasia. It forms the only reported high-confidence STRING pair in the module, with CXXC1, and is part of the corresponding hu.MAP complex. Its strong disease and literature support makes it a biologically consequential anchor even though its module degree is limited.
- **Conclusion**: Established evidence supports MEN1 as an epigenetic scaffold and tumor-suppressor-associated factor, together with its relationship to CXXC1. It is not established that MEN1 explains the non-chromatin genes in the module. Any claim that the module represents MEN1-driven breast biology remains a hypothesis.

#### CACNA1A

- **Related proteins** (co-abundance neighbors): PIGQ (0.93), SGCB (0.85), JPH2 (0.81), ICA1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium voltage-gated channel subunit alpha1 A. Voltage-dependent calcium channels mediate the entry of calcium ions into excitable cells, and are also involved in a variety of calcium-dependent processes, including muscle contraction, hormone or neurotransmitter release, and gene expression. Calcium channels are multisubunit complexes composed of alpha-1, beta, alpha-2/delta, and gamma subunits. The channel activity is directed by the pore-for…
- **Diseases (Open Targets)**: episodic ataxia type 2 (0.842); migraine, familial hemiplegic, 1 (0.822); developmental and epileptic encephalopathy, 42 (0.813); spinocerebellar ataxia type 6 (0.771); Seizure (0.720)
- **Europe PMC papers**: 4556
- **Why important**: CACNA1A encodes the pore-forming subunit of a voltage-dependent calcium channel and has extensive functional and disease evidence involving calcium transport, synaptic signaling, ataxia, migraine, and epileptic disorders. Within the module it connects to PIGQ, SGCB, JPH2, and ICA1, creating the clearest local cluster of calcium, membrane, junctional, and secretory biology. Its brain-enriched and neuronal cell-type patterns support a specialized excitable-cell signal, although its detection pattern does not establish a breast-specific role.
- **Conclusion**: Established evidence supports CACNA1A as a calcium-channel component with major roles in excitable-cell physiology and inherited neurological disease. The module supports a candidate association with membrane calcium handling, but it does not establish functional CACNA1A channels in the shared breast and cell-line context.

#### SGCB

- **Related proteins** (co-abundance neighbors): SNX21 (0.85), CACNA1A (0.85), MYSM1 (0.80), AMPD3 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sarcoglycan beta. This gene encodes a member of the sarcoglycan family. Sarcoglycans are transmembrane components in the dystrophin-glycoprotein complex which help stabilize the muscle fiber membranes and link the muscle cytoskeleton to the extracellular matrix. Mutations in this gene have been associated with limb-girdle muscular dystrophy.[provided by RefSeq, Oct 2008].
- **Diseases (Open Targets)**: autosomal recessive limb-girdle muscular dystrophy type 2E (0.805); autosomal recessive limb-girdle muscular dystrophy (0.698); qualitative or quantitative defects of beta-sarcoglycan (0.471); hereditary disease (0.463); dilated cardiomyopathy (0.387)
- **Europe PMC papers**: 1548
- **Why important**: SGCB is a structural component of the dystrophin-glycoprotein complex that stabilizes muscle-cell membranes and links cytoskeleton to extracellular matrix. It connects locally to CACNA1A, SNX21, MYSM1, and AMPD3, thereby linking membrane stability with signaling and nucleotide metabolism. Its skeletal-muscle enrichment and established limb-girdle muscular-dystrophy associations make it a useful marker of a muscle-like or membrane-structural component.
- **Conclusion**: Established evidence supports SGCB in muscle membrane integrity and muscular dystrophy. Its presence does not prove that the module is a muscle module, especially because HPA patterns are heterogeneous. A plausible hypothesis is that SGCB marks a shared membrane or cytoskeletal state rather than a direct SGCB-centered complex.

#### TGFBRAP1

- **Related proteins** (co-abundance neighbors): RAPGEF6 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transforming growth factor beta receptor associated protein 1. This gene encodes a protein that binds to transforming growth factor-beta (TGF-beta) receptors and plays a role in TGF-beta signaling. The encoded protein acts as a chaprone in signaling downstream of TGF-beta. It is involved in signal-dependent association with SMAD4. The protein is also a component of mammalian CORVET, a multisubunit tethering protein complex that is involved in fusion of early …
- **Diseases (Open Targets)**: substance-related disorder (0.234); schizophrenia (0.204); intelligence (0.204); obesity disorder (0.199); abdominal aortic aneurysm (0.162)
- **Europe PMC papers**: 424
- **Why important**: TGFBRAP1 connects the module hub to established transforming-growth-factor-beta receptor signaling, SMAD association, intracellular transport, and the CORVET endosomal tethering complex. This combination is relevant because it can conceptually connect signaling with vesicle and endosome biology. Its breast detection and hematopoietic-stem-cell enhancement provide context, while its disease evidence is less specific than that of MEN1 or CACNA1A.
- **Conclusion**: Established evidence supports TGFBRAP1 as a TGF-beta-associated signaling and endosomal-transport factor. Its module relationship to RAPGEF6 is a co-abundance observation, not proof of direct interaction. It is a plausible mediator of signaling-to-trafficking coordination within the proposed mechanism.

## Module 12

**Tissue pair**: breast and cell line  
**Genes (17)**: ANKRD27, CORO7, DCPS, ARHGDIB, GGACT, GRWD1, SELL, MAL2, NECAP2, OGFOD3, PPP3CA, RAVER1, RNASEH2A, RYR1, SLC75A1, SLC25A26, STK4

### Function

The module does not have a globally significant GO or KEGG annotation: no globally significant GO/KEGG term passed global correction. There is also no supplementary STRING enrichment. Its structure is a star-like co-abundance pattern centered on SELL, with most other genes connected only to that hub or occurring in small pairs. The genes span leukocyte adhesion and migration through SELL, immune-cell signaling through STK4 and DCPS, RNA processing and genome maintenance through RAVER1, RNASEH2A, and GRWD1, membrane and vesicle trafficking through MAL2, ANKRD27, CORO7, and NECAP2, and tissue-specialized calcium, mitochondrial, neuronal, renal, or muscle biology through RYR1, SLC25A26, PPP3CA, and GGACT. Therefore, the safest functional interpretation is a heterogeneous co-abundance signature organized around leukocyte-associated SELL expression rather than a single established molecular pathway.

**Cell composition.** This module is not dominated by secreted proteins; the HPA summary reports no secreted genes. It is also not broadly uniformly housekeeping-like. Several genes are tissue or cell-type associated, especially SELL and STK4 with bone marrow and lymphoid tissue, SELL with neutrophils, and DCPS with plasmacytoid dendritic cells and plasma cells. Other genes show specialized associations with skeletal muscle, esophagus, kidney, brain, or glial and neuronal populations. Most genes have low immune-cell specificity, so the module is not a coherent blood-cell program despite the leukocyte-linked hub. Its presence in breast and cell-line data could reflect shared cellular composition, a mixture of lineage signals, or coordinated abundance of otherwise unrelated transcripts. HPA protein detection in breast is incomplete, and there is no matching HPA tissue for the cell-line context.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no STRING functional-enrichment result was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not supported here as known physical protein interactions or as membership in a known protein complex. The strongest internal structure is the association of SELL with several otherwise weakly connected genes, while RYR1 is paired with ANKRD27 and DCPS, and MAL2 is paired with SLC25A26. These relationships should be treated as data-derived co-abundance relationships, not established biochemical partnerships.

**STRING interactions (score >= 0.7)**: 0 of 136 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module-level pattern appears unusual in the supplied reference resources because it has no high-confidence STRING interactions, no multi-member hu.MAP complex, no STRING enrichment, and no globally significant GO or KEGG term. However, that does not by itself establish a new biological discovery. Several individual genes have well-established functions and disease associations, and the module contains strong tissue and cell-type signals that could arise from sample composition, lineage admixture, or technical and biological context shared by breast and cell-line samples. The defensible conclusion is that this particular cross-context co-abundance assembly is a candidate novel association pattern, requiring replication, cell-composition adjustment, and independent interaction or perturbation experiments before being called a new mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared abundance state in which a leukocyte-adhesion or leukocyte-associated signal marked by SELL covaries with genes involved in intracellular trafficking, cytoskeletal or signaling control, RNA and DNA metabolism, and specialized tissue programs. One possible explanation is that a small immune-lineage contribution or a related cellular state is present in both sample groups, while the remaining genes are coupled indirectly through cellular composition or state rather than through one physical complex. A competing hypothesis is that SELL-centered regulation coordinates membrane trafficking and stress-responsive programs in a subset of cells. These alternatives are hypotheses, not conclusions from the current enrichment and interaction evidence.

### Important genes

#### SELL

- **Related proteins** (co-abundance neighbors): RAVER1 (0.94), RNASEH2A (0.94), STK4 (0.93), DCPS (0.88), SLC75A1 (0.88), GRWD1 (0.86), CORO7 (0.85), MAL2 (0.84), ARHGDIB (0.83), OGFOD3 (0.83), GGACT (0.83), PPP3CA (0.82), NECAP2 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: selectin L. This gene encodes a cell surface adhesion molecule that belongs to a family of adhesion/homing receptors. The encoded protein contains a C-type lectin-like domain, a calcium-binding epidermal growth factor-like domain, and two short complement-like repeats. The gene product is required for binding and subsequent rolling of leucocytes on endothelial cells, facilitating their migration into secondar…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.367); asthma (0.304); lymphatic system disorder (0.286); ankylosing spondylitis (0.202); atrial fibrillation (0.189)
- **Europe PMC papers**: 14927
- **Why important**: SELL is the central network hub and has the strongest weighted connectivity in the module. Its established function is as a cell-surface adhesion and homing receptor that supports leukocyte rolling and migration. HPA links it to bone marrow, lymphoid tissue, and neutrophils, while MyGene.info lists leukocyte adhesion, leukocyte migration, and cytokine response. It also has substantial literature and multiple immune and inflammatory disease associations.
- **Conclusion**: Established evidence supports SELL as the principal biological anchor and a marker of leukocyte-associated biology. It is not established that SELL physically regulates the other module genes; the hub relationship is co-abundance-based. The leading interpretation is that SELL captures cellular composition or state, with a possible but unproven role in organizing the broader module.

#### STK4

- **Related proteins** (co-abundance neighbors): SELL (0.93); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine/threonine kinase 4. The protein encoded by this gene is a cytoplasmic kinase that is structurally similar to the yeast Ste20p kinase, which acts upstream of the stress-induced mitogen-activated protein kinase cascade. The encoded protein can phosphorylate myelin basic protein and undergoes autophosphorylation. A caspase-cleaved fragment of the encoded protein has been shown to be capable of phosphorylating histone H2…
- **Diseases (Open Targets)**: combined immunodeficiency due to STK4 deficiency (0.755); severe combined immunodeficiency (0.546); combined immunodeficiency (0.465); combined immunodeficiency due to DOCK8 deficiency (0.462); immunodeficiency disease (0.344)
- **Europe PMC papers**: 1768
- **Why important**: STK4 is directly connected to SELL and is enriched by HPA in bone marrow and lymphoid tissue, with associations across B cells, dendritic cells, mast cells, neutrophil progenitors, and neutrophils. Its established functions include protein phosphorylation, signal transduction, cell morphogenesis, and apoptosis. It has disease associations involving combined immunodeficiency and a substantial literature.
- **Conclusion**: Established evidence supports STK4 as an immune-relevant signaling and survival component that is consistent with the SELL-centered interpretation. Its participation in this specific module is supported by co-abundance and cell-type evidence, but a direct mechanistic connection to SELL or the other genes remains unproven.

#### DCPS

- **Related proteins** (co-abundance neighbors): SELL (0.88), RYR1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: decapping enzyme, scavenger. This gene encodes a member of the histidine triad family of pyrophosphatases that removes short mRNA fragments containing the 5' mRNA cap structure, which appear in the 3' -> 5' mRNA decay pathway, following deadenylation and exosome-mediated turnover. This enzyme hydrolyzes the triphosphate linkage of the cap structure (7-methylguanosine nucleoside triphosphate) to yield 7-methylguanosine monopho…
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.670); neurodegenerative disease (0.574); autoimmune disorder of central nervous system (0.428); response to statin (0.282); urinary system disorder (0.201)
- **Europe PMC papers**: 886
- **Why important**: DCPS is connected to both SELL and RYR1, giving it a bridging position within the otherwise fragmented network. It is associated by HPA with liver tissue, plasmacytoid dendritic cells, and plasma cells. Its established function is mRNA cap decapping in RNA turnover, with additional annotation for RNA processing and splicing. It has a documented connection to autosomal recessive intellectual disability and a meaningful literature.
- **Conclusion**: Established evidence supports DCPS as an RNA-processing enzyme with a cell-type pattern that may connect immune and secretory-cell signals. The apparent bridge in this module is a hypothesis generated by the network, not evidence that DCPS links SELL and RYR1 biochemically.

#### RYR1

- **Related proteins** (co-abundance neighbors): ANKRD27 (0.91), DCPS (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ryanodine receptor 1. This gene encodes a ryanodine receptor found in skeletal muscle. The encoded protein functions as a calcium release channel in the sarcoplasmic reticulum but also serves to connect the sarcoplasmic reticulum and transverse tubule. Mutations in this gene are associated with malignant hyperthermia susceptibility, central core disease, and minicore myopathy with external ophthalmoplegia. Alternativel…
- **Diseases (Open Targets)**: central core myopathy (0.848); congenital multicore myopathy with external ophthalmoplegia (0.842); King-Denborough syndrome (0.803); malignant hyperthermia of anesthesia (0.800); RYR1-related myopathy (0.698)
- **Europe PMC papers**: 7774
- **Why important**: RYR1 is a distinctive module member because it encodes a calcium-release channel with a well-established skeletal-muscle role and strong associations with malignant hyperthermia and congenital myopathies. It forms a small co-abundance pair with ANKRD27 and is also connected to DCPS. HPA associates it with skeletal muscle, tongue, and myonuclei, and it has a large disease and literature record.
- **Conclusion**: Established evidence supports RYR1 as a calcium-handling and muscle-lineage marker, not as an immune or breast-specific module component. Its presence suggests that the module may combine lineage or sample-composition signals. Any proposed role for RYR1 in the broader SELL-centered program is speculative.

#### MAL2

- **Related proteins** (co-abundance neighbors): SLC25A26 (0.90), SELL (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mal, T cell differentiation protein 2. This gene encodes a multispan transmembrane protein belonging to the MAL proteolipid family. The protein is a component of lipid rafts and, in polarized cells, it primarily localizes to endosomal structures beneath the apical membrane. It is required for transcytosis, an intracellular transport pathway used to deliver membrane-bound proteins and exogenous cargos from the basolateral to the apical …
- **Diseases (Open Targets)**: cholelithiasis (0.335); hypertensive disorder (0.323); chronic rhinosinusitis with nasal polyps (0.302); chronic bronchitis (0.292); endocrine system disorder (0.284)
- **Europe PMC papers**: 1980
- **Why important**: MAL2 is connected to SELL and SLC25A26 and encodes a membrane protein involved in lipid rafts, polarized-cell endosomal localization, and transcytosis. HPA associates it with esophageal, gastric, and intestinal epithelial cell types and reports no detection in immune cells. It therefore provides an informative contrast to the leukocyte-linked genes and has a moderate literature record.
- **Conclusion**: Established evidence supports MAL2 as an epithelial membrane-trafficking protein. Its co-abundance with SELL may reflect shared sample composition, membrane-state regulation, or indirect coupling rather than a known physical partnership. The epithelial and immune signals together argue against assigning the module to a single canonical cell type.

## Module 13

**Tissue pair**: breast and cell line  
**Genes (6)**: AP4S1, CLK4, CYTH2, HPS5, MYO9A, UBE2L6

### Function

No GO or KEGG term passed global correction, and STRING reported no supplementary functional enrichment. The gene annotations nevertheless suggest a membrane-trafficking and intracellular-organization theme. MYO9A is an actin-based unconventional myosin associated with cell-junction organization and epithelial polarity; AP4S1 participates in vesicle formation and cargo sorting; CYTH2 supports endocytosis, vesicle transport, actin organization and ARF signaling; and HPS5 supports lysosome-related organelle biogenesis. UBE2L6 contributes ubiquitin and ISG15-protein conjugation, while CLK4 may regulate alternative splicing. The module is therefore most plausibly related to coordinated membrane trafficking, cytoskeletal organization and intracellular protein handling, but this is an annotation-based interpretation rather than an enrichment-supported conclusion.

**Cell composition.** All module proteins are detected in breast tissue, and none is annotated as secreted. The proteins are intracellular, vesicular, plasma-membrane or cytoskeletal rather than plasma proteins. HPA reports low immune-cell specificity for every gene and no enriched blood-cell population, arguing against a blood-cell explanation. All genes show cell-type enhancement, with recurring signals in spermatids and additional signals in epithelial, cardiac, podocyte, microglial and stromal populations. The shared module may therefore reflect a common cellular state or shared cell type rather than a tissue-specific secreted or immune program. Direct comparison with the cell-line samples is limited because matching HPA tissue protein data are unavailable.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The co-abundance graph is connected and chain-like, with MYO9A linking UBE2L6, CYTH2 and AP4S1, and AP4S1 linking onward to HPS5 and CLK4. None of the possible gene pairs is represented by a high-confidence STRING interaction in the supplied evidence, and STRING reports no functional enrichment. No hu.MAP complex contains multiple module members. The observed edges are therefore co-abundance relationships rather than established physical interactions or membership in a known multiprotein complex. The shared trafficking, actin, organelle, ubiquitin and splicing annotations provide some biological coherence, but they do not establish one molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be described as a newly discovered pathway. Its particular co-abundance pattern may be unusual because it lacks high-confidence STRING links, lacks a multi-member hu.MAP complex and has no globally significant GO or KEGG term. However, absence from STRING or hu.MAP does not demonstrate novelty. Co-abundance can arise from shared regulation, cellular composition, correlated abundance or indirect biological relationships. The defensible conclusion is that this breast–cell-line pattern is an interesting candidate association requiring independent validation, not an established novel mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of polarized membrane trafficking and organelle handling in a shared epithelial or specialized cell-state program. In this model, MYO9A and CYTH2 connect actin organization, membrane association and ARF-regulated trafficking; AP4S1 contributes cargo sorting; HPS5 contributes lysosome-related organelle biogenesis; UBE2L6 contributes selective protein modification and turnover; and CLK4 may tune the relevant cellular state through alternative-splicing regulation. This hypothesis is consistent with the annotations and network arrangement, but it is not demonstrated by enrichment, STRING, hu.MAP or direct biochemical evidence.

### Important genes

#### MYO9A

- **Related proteins** (co-abundance neighbors): UBE2L6 (0.86), CYTH2 (0.85), AP4S1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin IXA. This gene encodes a member of the myosin superfamily. The protein represents an unconventional myosin; it should not be confused with the conventional non-muscle myosin-9 (MYH9). Unconventional myosins contain the basic domains of conventional myosins and are further distinguished from class members by their tail domains. They function as actin-based molecular motors. Mutations in this gene have b…
- **Diseases (Open Targets)**: presynaptic congenital myasthenic syndrome (0.664); placental abruption (0.234); hereditary disease (0.194); focal segmental glomerulosclerosis (0.183); adverse effect (0.178)
- **Europe PMC papers**: 444
- **Why important**: MYO9A is the most central node in the supplied co-abundance graph and connects the trafficking, actin-associated and adaptor-related portions of the module. Its established role as an unconventional actin-based myosin, together with functions in cell-junction organization and epithelial apical–basal polarity, makes it a strong candidate for linking membrane organization to cytoskeletal state. It has substantial literature coverage and disease associations including Bardet–Biedl syndrome and presynaptic congenital myasthenic syndrome.
- **Conclusion**: Established evidence supports MYO9A as a membrane- and actin-organizing protein with relevant disease biology. It is a plausible coordinating gene for this module, but the co-abundance data do not establish that MYO9A regulates the other module members.

#### AP4S1

- **Related proteins** (co-abundance neighbors): HPS5 (0.85), MYO9A (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor related protein complex 4 subunit sigma 1. This gene encodes a member of the adaptor complexes small subunit protein family. These proteins are components of the heterotetrameric adaptor protein complexes, which play important roles in the secretory and endocytic pathways by mediating vesicle formation and sorting of integral membrane proteins. The encoded protein is the small subunit of adaptor protein complex-4, which is associated with …
- **Diseases (Open Targets)**: AP-4 deficiency syndrome (0.760); hereditary spastic paraplegia 52 (0.725); Spastic paraplegia (0.545); hereditary disease (0.493); Global developmental delay (0.485)
- **Europe PMC papers**: 286
- **Why important**: AP4S1 occupies an internal position connecting MYO9A with HPS5. Its established function as a subunit of adaptor protein complex four and its role in vesicle formation and sorting provide a direct mechanistic link to intracellular cargo trafficking. Its disease associations include AP-four deficiency syndrome and hereditary spastic paraplegia, and its protein is detected in breast tissue.
- **Conclusion**: Established evidence supports AP4S1 as a vesicle-sorting component. Its network position makes it a plausible bridge between membrane organization and organelle trafficking, while any specific role in this shared module remains a hypothesis.

#### HPS5

- **Related proteins** (co-abundance neighbors): AP4S1 (0.85), CLK4 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HPS5 biogenesis of lysosomal organelles complex 2 subunit 2. This gene encodes a protein that may play a role in organelle biogenesis associated with melanosomes, platelet dense granules, and lysosomes. This protein interacts with Hermansky-Pudlak syndrome 6 protein and may interact with the cytoplasmic domain of integrin, alpha-3. Mutations in this gene are associated with Hermansky-Pudlak syndrome type 5. Multiple transcript variants encoding two distinct…
- **Diseases (Open Targets)**: Hermansky-Pudlak syndrome (0.799); Hermansky-Pudlak syndrome without pulmonary fibrosis (0.791); neurodegenerative disease (0.301); hair color (0.282); hereditary disease (0.195)
- **Europe PMC papers**: 479
- **Why important**: HPS5 forms the branch connecting AP4S1 and CLK4 and has a well-defined role in lysosome-related organelle biogenesis, including melanosomes and platelet dense granules. Its association with Hermansky–Pudlak syndrome gives the gene strong disease relevance, and it has substantial literature coverage. HPA also reports liver enrichment and enhancement in several specialized cell populations.
- **Conclusion**: Established evidence supports HPS5 in organelle biogenesis and Hermansky–Pudlak syndrome. Its inclusion suggests that organelle handling may contribute to the module, but the apparent connection to AP4S1 and CLK4 is based on co-abundance rather than a demonstrated complex.

#### UBE2L6

- **Related proteins** (co-abundance neighbors): MYO9A (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin conjugating enzyme E2 L6. The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes (E1s), ubiquitin-conjugating enzymes (E2s) and ubiquitin-protein ligases (E3s). This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. This enzyme is …
- **Diseases (Open Targets)**: major depressive disorder (0.099); schizophrenia (0.079); melanoma (0.078); attention deficit-hyperactivity disorder (0.076); nasopharyngeal carcinoma (0.075)
- **Europe PMC papers**: 1113
- **Why important**: UBE2L6 is directly connected to MYO9A and contributes a distinct protein-quality-control axis through ubiquitination and ISG15-protein conjugation. It has the largest literature volume among the module genes and disease associations spanning neuropsychiatric conditions and melanoma. Its broad tissue profile and low immune-cell specificity argue against interpreting its presence as evidence of a blood-cell module.
- **Conclusion**: Established evidence supports UBE2L6 as an E2 ubiquitin-conjugating enzyme involved in protein modification and turnover. Its role in this module may represent coordinated protein processing or cellular-state regulation, but a direct connection to MYO9A or the trafficking genes is unproven.

#### CYTH2

- **Related proteins** (co-abundance neighbors): MYO9A (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytohesin 2. The protein encoded by this gene is a member of the PSCD family. Members of this family have identical structural organization that consists of an N-terminal coiled-coil motif, a central Sec7 domain, and a C-terminal pleckstrin homology (PH) domain. The coiled-coil motif is involved in homodimerization, the Sec7 domain contains guanine-nucleotide exchange protein (GEP) activity, and the PH domain …
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); IgA glomerulonephritis (0.320); brain compression (0.107); edema (0.107); colorectal cancer (0.073)
- **Europe PMC papers**: 190
- **Why important**: CYTH2 is directly connected to MYO9A and supplies a strong functional link to endocytosis, vesicle-mediated transport, actin-cytoskeleton organization and ARF signaling. Its Sec seven and pleckstrin-homology domains are relevant to coupling signaling with membrane trafficking. It also shows cell-type enhancement across epithelial, reproductive and placental-related populations.
- **Conclusion**: Established evidence supports CYTH2 as a membrane-associated ARF exchange factor involved in endocytic and actin-related processes. It is a credible functional contributor to the membrane-organization interpretation, but the module does not establish a direct MYO9A–CYTH2 biochemical interaction.

#### CLK4

- **Related proteins** (co-abundance neighbors): HPS5 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CDC like kinase 4. The protein encoded by this gene belongs to the CDC2-like protein kinase (CLK) family. This protein kinase can interact with and phosphorylate the serine- and arginine-rich (SR) proteins, which are known to play an important role in the formation of spliceosomes, and thus may be involved in the regulation of alternative splicing. Studies in the Israeli sand rat Psammomys obesus suggested that the …
- **Diseases (Open Targets)**: autoimmune disorder of central nervous system (0.352); esophageal squamous cell carcinoma (0.075); cardiac hypertrophy (0.066); prostate carcinoma (0.055); heart failure (0.047)
- **Europe PMC papers**: 561
- **Why important**: CLK4 is located on the HPS5 branch and contributes a regulatory dimension through phosphorylation of serine- and arginine-rich splicing factors. Its annotation in regulation of RNA splicing and disease associations involving cardiac and esophageal disorders make it biologically relevant despite its peripheral network position. Its enhancement in early and late spermatids may also indicate a specialized cellular-state component.
- **Conclusion**: Established evidence supports CLK4 as a splicing-regulatory kinase. Its presence may indicate coordination between cellular trafficking and gene-expression or splicing state, but that connection is a hypothesis rather than an established property of this module.

## Module 14

**Tissue pair**: breast and cell line  
**Genes (5)**: APBA1, MSRA, METTL21A, MYO18B, NAT14

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent. The module therefore does not support a single statistically established pathway assignment. Its topology is a short chain linking MSRA, APBA1, NAT14, and METTL21A, with MYO18B branching from MSRA. The annotations suggest several biological themes rather than one coherent canonical pathway: repair of oxidatively damaged proteins through MSRA, neuronal APP-associated intracellular trafficking and synaptic biology through APBA1, putative acetyltransferase and transcription-related activity through NAT14, muscle-associated trafficking or nuclear regulation through MYO18B, and HSPA-associated lysine methylation and protein-folding regulation through METTL21A. These annotations support a cautious interpretation as a possible proteostasis, intracellular trafficking, and cell-state module, but not as a demonstrated pathway.

**Cell composition.** The module is not secreted, arguing against a plasma-protein or secretome explanation. Most members have tissue- or cell-type-enhanced expression rather than broad housekeeping-like expression. Brain enrichment is prominent, with neuronal and glial cell-type associations for MSRA and APBA1, while NAT14 is also tissue-enhanced in brain. MYO18B is associated with cardiac and skeletal muscle, and METTL21A has low tissue specificity with cell-type enhancement in cardiomyocytes and mast cells. Most genes are not detected in immune cells, although MSRA has an eosinophil association and METTL21A has low immune-cell specificity. Thus, the module is unlikely to be explained primarily by blood-cell contamination. The divergent brain, muscle, kidney, liver, and heart associations suggest that shared cell state, proteostasis, or sample-specific composition may contribute more than a single tissue identity. Breast protein detection is present for MSRA and METTL21A, absent for MYO18B, and unavailable for the remaining members; there is no matching HPA tissue assessment for the cell-line context.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship was reported among the module genes, and no STRING functional enrichment was found. No hu.MAP complex contained multiple module members. Consequently, the co-abundance edges are not corroborated here as established physical interactions or membership in a known multiprotein complex. The individual annotations do contain known functional relationships outside this module, such as APBA1 interaction with APP and the biochemical activities assigned to MSRA and METTL21A. These facts provide biological plausibility for selected themes but do not validate the observed co-abundance edges as direct molecular binding relationships.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a previously unrecognized co-abundance association in the breast and cell-line comparison, because the module is not reproduced by the available high-confidence STRING network or by a shared hu.MAP complex. However, that absence does not establish novelty: co-abundance can reflect shared regulation, cell composition, protein stability, or technical covariance without corresponding to physical interaction. The lack of globally significant GO or KEGG enrichment globally significant GO/KEGG and the heterogeneous tissue annotations further argue against claiming discovery of a new pathway. The defensible conclusion is that the module is a potentially novel sample-level co-abundance pattern whose mechanistic and disease relevance require independent replication and targeted experiments.

**Hypothesis.** Hypothesis: the module reflects a coordinated proteostasis and intracellular-trafficking state rather than a stable protein complex. Oxidative protein repair by MSRA and HSPA-related lysine methylation by METTL21A could mark cellular protein-quality-control demands, while APBA1 could connect that state to vesicular or neuronal trafficking, NAT14 could contribute a poorly characterized membrane-associated regulatory activity, and MYO18B could reflect cytoskeletal or muscle-linked trafficking. The shared breast and cell-line signal may therefore arise from convergent regulation of protein maintenance and intracellular transport in a subset of cells. This is a hypothesis only; the absence of STRING and hu.MAP support means the edges should not be interpreted as direct physical interactions.

### Important genes

#### MSRA

- **Related proteins** (co-abundance neighbors): MYO18B (0.83), APBA1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionine sulfoxide reductase A. This gene encodes a ubiquitous and highly conserved protein that carries out the enzymatic reduction of methionine sulfoxide to methionine. Human and animal studies have shown the highest levels of expression in kidney and nervous tissue. The protein functions in the repair of oxidatively damaged proteins to restore biological activity. Alternative splicing results in multiple transcript variants.…
- **Diseases (Open Targets)**: hypertensive disorder (0.487); alcohol drinking (0.480); type 2 diabetes mellitus (0.467); bipolar disorder (0.446); Irritability (0.429)
- **Europe PMC papers**: 8330
- **Why important**: MSRA is the strongest network connector, linking APBA1 and MYO18B. Its established enzymatic role is repair of oxidatively damaged methionine residues, with annotations for protein repair and cellular responses to oxidative stress. It is tissue-enhanced in kidney and liver and has extensive literature relative to the other module members. Its disease associations include hypertension, alcohol-related behavior, type two diabetes, bipolar disorder, and irritability.
- **Conclusion**: Established evidence supports MSRA as the clearest proteostasis and oxidative-stress anchor of the module. Its central network position makes it an important candidate contributor to the observed co-abundance pattern. It is not established that MSRA physically interacts with APBA1 or MYO18B, nor that it drives the module.

#### APBA1

- **Related proteins** (co-abundance neighbors): MSRA (0.83), NAT14 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: amyloid beta precursor protein binding family A member 1. The protein encoded by this gene is a member of the X11 protein family. It is a neuronal adapter protein that interacts with the Alzheimer's disease amyloid precursor protein (APP). It stabilizes APP and inhibits production of proteolytic APP fragments including the A beta peptide that is deposited in the brains of Alzheimer's disease patients. This gene product is believed to be involved in signa…
- **Diseases (Open Targets)**: neurodegenerative disease (0.338); mathematical ability (0.329); intelligence (0.301); drug allergy (0.230); adolescent idiopathic scoliosis (0.224)
- **Europe PMC papers**: 480
- **Why important**: APBA1 is an internal connector between MSRA and NAT14. It is a neuronal adapter associated with APP, intracellular protein transport, axo-dendritic transport, chemical synaptic transmission, and nervous-system development. Its strong brain and neuronal cell-type associations make it the clearest tissue-context marker for the neural aspect of the module. Its literature is smaller than that of MSRA but sufficient to support a defined trafficking and APP-related biological role.
- **Conclusion**: Established evidence supports APBA1 as a neuronal intracellular-trafficking and APP-associated adapter. Its position may link the oxidative-proteostasis signal to vesicular transport in the co-abundance pattern. Whether that link operates in breast or cell-line samples is unresolved and remains a hypothesis.

#### NAT14

- **Related proteins** (co-abundance neighbors): APBA1 (0.82), METTL21A (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-acetyltransferase 14 (putative). Predicted to enable N-acetyltransferase activity. Predicted to be integral component of membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Vertigo (0.034); esophageal squamous cell carcinoma (0.013); neoplasm (0.005); breast cancer (0.004); congenital hydrocephalus (0.004)
- **Europe PMC papers**: 92
- **Why important**: NAT14 is an internal connector between APBA1 and METTL21A. It is annotated as a putative N-acetyltransferase with predicted membrane integration and transcription-related functions. It is brain-enhanced and associated with several ciliated, endocrine, and epithelial cell types. Its relatively limited literature and putative annotation make it especially valuable as a potentially undercharacterized component of the module. Disease links include vertigo, esophageal squamous cell carcinoma, neoplasm, breast cancer, and congenital hydrocephalus.
- **Conclusion**: Established evidence supports only a putative enzymatic and membrane-associated role for NAT14. Its network position makes it a plausible bridge between APBA1 and METTL21A, but the module provides no evidence that NAT14 mediates either connection. Its role in the shared breast and cell-line signal is therefore an important testable hypothesis.

#### METTL21A

- **Related proteins** (co-abundance neighbors): NAT14 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methyltransferase 21A, HSPA lysine. Enables ATPase binding activity; Hsp70 protein binding activity; and protein-lysine N-methyltransferase activity. Involved in peptidyl-lysine methylation. Part of protein-containing complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: essential hypertension (0.171); hypertensive disorder (0.166); histiocytoma, Angiomatoid fibrous (0.118); obesity disorder (0.081); Abnormality of the skeletal system (0.080)
- **Europe PMC papers**: 194
- **Why important**: METTL21A is a terminal network member connected to NAT14. It has annotations for HSPA binding, protein-lysine methyltransferase activity, peptidyl-lysine methylation, and regulation of protein folding. Unlike most members, it has low tissue specificity, while showing cell-type enhancement in cardiomyocytes and mast cells. Its literature is modest, and its disease associations include hypertension, obesity-related disorder, and skeletal-system abnormality.
- **Conclusion**: Established evidence supports METTL21A as a candidate regulator of protein folding through lysine methylation and HSPA-associated activity. Its annotation provides the strongest connection to a proteostasis interpretation alongside MSRA. Direct functional coupling to NAT14 or coordinated action in this module has not been established.

#### MYO18B

- **Related proteins** (co-abundance neighbors): MSRA (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Nucleoplasm, Centrosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin XVIIIB. The protein encoded by this gene may regulate muscle-specific genes when in the nucleus and may influence intracellular trafficking when in the cytoplasm. The encoded protein functions as a homodimer and may interact with F actin. Mutations in this gene are associated with lung cancer. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: Klippel-Feil anomaly-myopathy-facial dysmorphism syndrome (0.786); atrial fibrillation (0.564); hereditary disease (0.453); mathematical ability (0.438); Brugada syndrome (0.438)
- **Europe PMC papers**: 719
- **Why important**: MYO18B is the peripheral branch of the module, connected only to MSRA. It is associated with muscle-enriched expression, nuclear localization, centrosomal localization, possible regulation of muscle-specific genes, intracellular trafficking, and interaction with F-actin. Its disease associations include a myopathy-facial-dysmorphism syndrome, atrial fibrillation, Brugada syndrome, and lung cancer. Its literature is substantial enough to support a recognized muscle and cytoskeletal context, although it is not detected in breast by the supplied HPA evidence.
- **Conclusion**: Established evidence supports MYO18B as a muscle- and cytoskeleton-related myosin with possible nuclear and trafficking functions. Its peripheral position suggests it may represent a cell-state or lineage component rather than a core module driver. A functional connection to MSRA is not established, so its role in the shared module remains unresolved.

## Module 15

**Tissue pair**: breast and cell line  
**Genes (5)**: ATP1A1, MGAT4A, RAB18, RILPL1, ZC3H7B

### Function

No GO or KEGG term passed global correction, and STRING supplied no supplementary enrichment. The module is therefore not assignable to a single established pathway from enrichment evidence. Its structure is a sparse MGAT4A-centered pattern linking Golgi N-glycan branching with membrane ion transport, intracellular membrane trafficking, cytoskeletal or ciliary transport, and post-transcriptional regulation. MGAT4A provides the strongest network-centered signal, while the other genes connect to it individually. This supports a broad membrane and epithelial-cell organization interpretation, but not a demonstrated common biochemical process.

**Cell composition.** The module does not resemble a blood-cell or plasma-protein module. The genes have low immune-cell specificity or are not detected in immune cells, and no blood-cell-enriched group is reported. One gene, MGAT4A, is secreted to blood, but the module is not predominantly secreted. Tissue evidence is heterogeneous, including bone marrow, parathyroid gland, heart muscle, and skeletal muscle, while cell-type evidence includes epithelial, muscle, lactating breast, and other specialized cell types. Most genes show cell-type-enhanced rather than broadly nonspecific expression. Breast protein detection is present for nearly all genes with available data, whereas the cell-line comparison has no matching HPA tissue context. The shared signal could therefore reflect conserved epithelial or membrane biology, sample composition, or coordinated abundance of proteins expressed in breast-derived material; it should not be interpreted as a breast-specific mechanism without further validation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship was present among the module genes, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated here as established protein-protein interactions or membership in a known multiprotein complex. The MGAT4A-centered topology may represent coordinated regulation, shared localization, cell-state composition, or indirect biology rather than direct binding. Established functional links remain plausible at the process level: MGAT4A acts in Golgi glycoprotein processing, ATP1A1 maintains sodium and potassium gradients, RAB18 regulates membrane trafficking, RILPL1 is implicated in ciliary and plasma-membrane transport, and ZC3H7B has roles in post-transcriptional regulation and microRNA processing.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially interesting co-abundance observation, but it cannot be called a new biological module solely because STRING and hu.MAP lack matching relationships. The absence of globally significant GO or KEGG enrichment, the absence of STRING and hu.MAP support, and the sparse hub-and-spoke structure all weaken the case for a previously unrecognized conserved complex. A reasonable novelty claim is narrower: the coordinated abundance of these particular genes across breast and cell-line data may be underdescribed and merits testing. Establishing novelty would require independent replication, comparison with published coexpression or proteomic modules, control for tissue and cell-type composition, and experimental testing of whether the association persists after adjustment for abundance and localization effects.

**Hypothesis.** Hypothesis: the module reflects a conserved epithelial or membrane-trafficking state in which Golgi glycan branching by MGAT4A is coordinated with membrane homeostasis through ATP1A1, vesicle and lipid-associated trafficking through RAB18, ciliary or plasma-membrane transport through RILPL1, and post-transcriptional regulation through ZC3H7B. In this model, MGAT4A is a state marker or regulatory center rather than a proven physical interactor, and the observed pattern could arise because these genes respond to a shared differentiation, membrane-remodeling, or secretory-cell program. This hypothesis predicts that the association should be reproducible within epithelial or breast-relevant cell states and should weaken if driven mainly by mixed-cell composition.

### Important genes

#### MGAT4A

- **Related proteins** (co-abundance neighbors): ATP1A1 (0.89), ZC3H7B (0.88), RAB18 (0.84), RILPL1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminyltransferase A. This gene encodes a key glycosyltransferase that regulates the formation of tri- and multiantennary branching structures in the Golgi apparatus. The encoded protein, in addition to the related isoenzyme B, catalyzes the transfer of N-acetylglucosamine (GlcNAc) from UDP-GlcNAc in a beta-1,4 linkage to the Man-alpha-1,3-Man-beta-1,4-GlcNAc arm of R-Man-alpha-1,6(GlcNAc-beta-1,2-Man-alpha-1,3)Man-bet…
- **Diseases (Open Targets)**: COVID-19 (0.371); smoking initiation (0.280); placental abruption (0.233); obesity disorder (0.127); neoplasm (0.081)
- **Europe PMC papers**: 608
- **Why important**: MGAT4A is the network hub, connecting to every other module member with the strongest aggregate connectivity. Its established Golgi localization and glycosyltransferase function make it the clearest mechanistic bridge to glycoprotein biosynthesis and N-glycan processing. It is tissue enhanced in bone marrow, cell-type enhanced in several immune-related categories despite low overall immune specificity, detected in breast, secreted to blood, and supported by a substantial literature and multiple disease-oriented associations.
- **Conclusion**: Established evidence supports MGAT4A as the central glycosylation-related gene and the principal network anchor. It is not established that MGAT4A physically regulates the other module genes. The module-level interpretation that MGAT4A marks a coordinated membrane or epithelial state is a hypothesis.

#### ATP1A1

- **Related proteins** (co-abundance neighbors): MGAT4A (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 is the canonical plasma-membrane sodium-potassium pump subunit and is the module's clearest membrane-homeostasis gene. It is tissue enhanced in parathyroid gland, cell-type enhanced across several absorptive and secretory epithelial populations, detected in breast, and has extensive literature and strong disease associations. Its direct module connection is only to MGAT4A, so its importance comes more from biological interpretability than network breadth.
- **Conclusion**: Established evidence supports a role in electrochemical-gradient maintenance and epithelial transport. Its co-abundance with MGAT4A may indicate coordinated membrane and secretory physiology, but a direct functional relationship between the two genes is not demonstrated by the supplied interaction evidence.

#### RAB18

- **Related proteins** (co-abundance neighbors): MGAT4A (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB18, member RAS oncogene family. The protein encoded by this gene is a member of a family of Ras-related small GTPases that regulate membrane trafficking in organelles and transport vesicles. Knockdown studies is zebrafish suggest that this protein may have a role in eye and brain development. Mutations in this gene are associated with Warburg micro syndrome type 3. Alternatively spliced transcript variants have been found for th…
- **Diseases (Open Targets)**: Warburg micro syndrome (0.815); neurodegenerative disease (0.496); cerebral atherosclerosis (0.275); malunion fracture (0.239); adolescent idiopathic scoliosis (0.229)
- **Europe PMC papers**: 2168
- **Why important**: RAB18 is a well-studied small GTPase involved in intracellular protein transport, organelle and vesicle trafficking, lipid-droplet organization, and sterol homeostasis. It is connected to the MGAT4A hub, detected in breast, and enhanced in breast lactating and esophageal apical cells. Its disease association with Warburg micro syndrome and comparatively substantial literature make it an informative trafficking component.
- **Conclusion**: Established evidence supports RAB18 as a membrane-trafficking regulator with relevance to specialized epithelial and neural biology. Its participation in an MGAT4A-centered glycosylation program remains a hypothesis, not a demonstrated physical or genetic interaction.

#### RILPL1

- **Related proteins** (co-abundance neighbors): MGAT4A (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Primary cilium, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rab interacting lysosomal protein like 1. Predicted to enable protein dimerization activity. Predicted to be involved in several processes, including cilium assembly; epithelial cell morphogenesis; and protein transport from ciliary membrane to plasma membrane. Located in cytosol; nucleoplasm; and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: oculopharyngodistal myopathy (0.465); oculopharyngodistal myopathy 4 (0.383); neurodegenerative disease (0.245); maturity-onset diabetes of the young (0.068); maturity-onset diabetes of the young type 3 (0.058)
- **Europe PMC papers**: 264
- **Why important**: RILPL1 contributes a distinct ciliary and plasma-membrane transport perspective. It is associated with cilium assembly, epithelial morphogenesis, and transport from the ciliary membrane to the plasma membrane, and is tissue enhanced in heart and skeletal muscle. It is detected in breast and links to the MGAT4A hub despite having limited literature relative to ATP1A1 and RAB18. Its disease associations provide additional relevance to membrane and structural-cell biology.
- **Conclusion**: Established evidence supports roles in ciliary, epithelial, and membrane transport processes. A shared ciliary or epithelial-remodeling program with MGAT4A is plausible but remains inferential because no STRING or hu.MAP relationship supports a direct complex.

#### ZC3H7B

- **Related proteins** (co-abundance neighbors): MGAT4A (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger CCCH-type containing 7B. This gene encodes a protein that contains a tetratricopeptide repeat domain. The encoded protein also interacts with the rotavirus non-structural protein NSP3. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: mathematical ability (0.281); Myoclonus (0.155); neurotic disorder (0.138); smoking cessation (0.130); ovarian neoplasm (0.121)
- **Europe PMC papers**: 426
- **Why important**: ZC3H7B adds a regulatory layer distinct from the membrane and trafficking genes. It is broadly expressed by the HPA summary, is not detected in immune cells, and is annotated for post-transcriptional gene regulation and microRNA processing. It has a more limited literature than the major transport genes but is connected to the MGAT4A hub, making it potentially informative for regulation of the shared abundance state.
- **Conclusion**: Established evidence supports a role in post-transcriptional regulation and a tetratricopeptide-repeat-containing protein context. Its presence in this module does not establish control over MGAT4A or the membrane genes; coordinated regulation of a cell-state program is a hypothesis.

## Module 16

**Tissue pair**: breast and cell line  
**Genes (9)**: BST1, CACNA2D2, CDC20, COL2A1, GSKIP, LRP2, MYH3, NUDT14, SGCD

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established pathway-level function from enrichment. The gene annotations instead indicate a biologically heterogeneous program spanning muscle structure and contraction through SGCD, MYH3 and CACNA2D2, epithelial or receptor-mediated uptake through LRP2, cell-cycle regulation through CDC20, nucleotide metabolism through NUDT14, Wnt regulation through GSKIP, extracellular matrix biology through COL2A1, and adhesion or immune-related signaling through BST1. The co-abundance pattern is therefore more consistent with a mixed tissue or cell-state signal than with a single confirmed canonical pathway.

**Cell composition.** This is not predominantly a plasma-protein module and it is not uniformly blood-cell enriched. HPA profiles show broad heterogeneity, with tissue-enhanced genes associated with muscle, kidney, retina, lung, bone marrow and reproductive tissues, alongside cell-type associations involving early spermatids, enterocytes, monocyte progenitors, oocytes and retinal cells. BST1 has immune-cell-enhanced expression, while several genes are not detected in immune cells or have low immune-cell specificity. COL2A1 is secreted to the extracellular matrix and BST1 is intracellular and membrane-associated, so secreted or extracellular proteins are present but do not define the module. The shared breast and cell-line signal could therefore reflect shared cellular composition, stress or differentiation state, or coordinated expression across otherwise unrelated lineage programs. Breast protein detection is available for only part of the module, and the available breast evidence is mixed.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no hu.MAP complex containing multiple module members. Thus, the observed co-abundance edges are not corroborated by the supplied known-interaction or complex resources. This does not disprove co-regulation or indirect biological coordination, but it argues against interpreting the module as a previously established physical protein complex. Known functions remain biologically informative individually: SGCD belongs to the dystrophin-glycoprotein complex, LRP2 is a multi-ligand endocytic receptor, CDC20 regulates cell-cycle progression, and GSKIP modulates GSK3-beta and Wnt signaling, but these established relationships are external to the module's reported STRING and hu.MAP connectivity.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a novel co-abundance association because its gene combination is not supported by high-confidence STRING interactions, a shared hu.MAP complex, or significant GO or KEGG enrichment. However, absence from these resources alone does not establish novelty. Several individual genes and their functions are well established, and the module may arise from shared tissue composition, lineage mixing, coordinated differentiation, technical co-abundance, or indirect regulation rather than a previously unknown molecular complex. A claim of novelty would require independent replication, control for cell composition, and validation in additional breast and cell-line datasets.

**Hypothesis.** Hypothesis: the module reflects a mixed differentiation or cellular-composition program in which a muscle or contractile structural signal, epithelial uptake and adhesion features, proliferative activity, and lineage-associated expression become co-abundant in breast-derived samples and cell lines. SGCD may mark the structural or membrane-associated component, while LRP2 and BST1 may represent epithelial or stromal and immune-associated context, and CDC20 may capture proliferative state. GSKIP, NUDT14 and the remaining genes could be co-regulated indirectly through differentiation, trafficking or metabolic state. This is a hypothesis rather than an enrichment-supported pathway conclusion and should be tested by deconvolution, single-cell localization, perturbation, and replication.

### Important genes

#### SGCD

- **Related proteins** (co-abundance neighbors): CACNA2D2 (0.93), COL2A1 (0.85), LRP2 (0.84), GSKIP (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sarcoglycan delta. The protein encoded by this gene is one of the four known components of the sarcoglycan complex, which is a subcomplex of the dystrophin-glycoprotein complex (DGC). DGC forms a link between the F-actin cytoskeleton and the extracellular matrix. This protein is expressed most abundantly in skeletal and cardiac muscle. Mutations in this gene have been associated with autosomal recessive limb-girdle …
- **Diseases (Open Targets)**: autosomal recessive limb-girdle muscular dystrophy type 2F (0.770); dilated cardiomyopathy 1L (0.719); autosomal recessive limb-girdle muscular dystrophy (0.612); familial isolated dilated cardiomyopathy (0.539); schizophrenia (0.437)
- **Europe PMC papers**: 1340
- **Why important**: SGCD has the strongest network position in the module and connects the muscle-associated, receptor-associated and extracellular-matrix-associated portions of the graph. Its established role as a sarcoglycan component linking the actin cytoskeleton with the extracellular matrix, together with skeletal and cardiac muscle expression and associations with limb-girdle muscular dystrophy and dilated cardiomyopathy, makes it a biologically central structural candidate. Its literature base is substantial.
- **Conclusion**: Established evidence supports SGCD as the leading structural anchor and a plausible marker of a muscle-like or membrane-cytoskeletal state. It is not established that SGCD functionally drives the other module genes, because neither STRING nor hu.MAP supports those within-module relationships.

#### LRP2

- **Related proteins** (co-abundance neighbors): SGCD (0.84), BST1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LDL receptor related protein 2. The protein encoded by this gene, low density lipoprotein-related protein 2 (LRP2) or megalin, is a multi-ligand endocytic receptor that is expressed in many different tissues but primarily in absorptive epithilial tissues such as the kidney. This glycoprotein has a large amino-terminal extracellular domain, a single transmembrane domain, and a short carboxy-terminal cytoplasmic tail. The extracel…
- **Diseases (Open Targets)**: Donnai-Barrow syndrome (0.795); Intellectual disability (0.542); gout (0.520); Hearing impairment (0.472); hereditary disease (0.418)
- **Europe PMC papers**: 5656
- **Why important**: LRP2 occupies a connecting position between SGCD and BST1 and has extensive functional and disease annotation. It is a multi-ligand endocytic receptor enriched in absorptive epithelial tissues, especially kidney, and is associated with retinal and developmental biology as well as Donnai-Barrow syndrome. Its cell-junction localization makes it relevant to epithelial organization and material uptake.
- **Conclusion**: Established evidence supports LRP2 as an epithelial endocytic and junction-associated marker. Its presence supports a tissue-composition or epithelial-state interpretation, but a direct mechanistic link to SGCD or BST1 remains hypothetical.

#### CDC20

- **Related proteins** (co-abundance neighbors): MYH3 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell division cycle 20. CDC20 appears to act as a regulatory protein interacting with several other proteins at multiple points in the cell cycle. It is required for two microtubule-dependent processes, nuclear movement prior to anaphase and chromosome separation. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: oocyte maturation defect 14 (0.725); neurodegenerative disease (0.527); female infertility due to oocyte meiotic arrest (0.384); asparaginase-induced acute pancreatitis (0.352); hepatocellular carcinoma (0.127)
- **Europe PMC papers**: 9924
- **Why important**: CDC20 is the module's clearest cell-cycle-associated gene. It occupies a terminal network position connected to MYH3, is enriched in bone marrow and lymphoid tissue, and is associated with mitotic checkpoint control, chromosome separation and proliferative regulation. It also has a large literature base and disease relevance.
- **Conclusion**: Established evidence supports CDC20 as a marker of proliferative or dividing-cell state. Its co-abundance with a muscle-associated gene does not establish a shared pathway and may instead indicate mixed cellular states or indirect co-regulation.

#### GSKIP

- **Related proteins** (co-abundance neighbors): NUDT14 (0.83), SGCD (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GSK3B interacting protein. This gene encodes a protein that is involved as a negative regulator of GSK3-beta in the Wnt signaling pathway. The encoded protein may play a role in the retinoic acid signaling pathway by regulating the functional interactions between GSK3-beta, beta-catenin and cyclin D1, and it regulates the beta-catenin/N-cadherin pool. The encoded protein contains a GSK3-beta interacting domain (GID) in its …
- **Diseases (Open Targets)**: Sjogren syndrome (0.101); neurodegenerative disease (0.070); surfactant metabolism dysfunction, pulmonary, 1 (0.066); hereditary pulmonary alveolar proteinosis (0.064); isolated Pierre-Robin syndrome (0.056)
- **Europe PMC papers**: 409
- **Why important**: GSKIP connects NUDT14 with SGCD and has a defined signaling role as a GSK3-beta-interacting protein involved in Wnt regulation, beta-catenin and N-cadherin pools, and retinoic acid-related signaling. Its Golgi and vesicle localization and breast immunohistochemical detection provide context for a trafficking or signaling interpretation.
- **Conclusion**: Established evidence supports GSKIP as a signaling and trafficking-related regulator that could help connect differentiation and adhesion states. Its role as an organizer of this module is a hypothesis because no module-level enrichment or known interaction evidence supports that conclusion.

#### BST1

- **Related proteins** (co-abundance neighbors): LRP2 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: bone marrow stromal cell antigen 1. Bone marrow stromal cell antigen-1 is a stromal cell line-derived glycosylphosphatidylinositol-anchored molecule that facilitates pre-B-cell growth. The deduced amino acid sequence exhibits 33% similarity with CD38. BST1 expression is enhanced in bone marrow stromal cell lines derived from patients with rheumatoid arthritis. The polyclonal B-cell abnormalities in rheumatoid arthritis may be, at le…
- **Diseases (Open Targets)**: Parkinson disease (0.537); Lewy body dementia (0.291); autoimmune disorder of central nervous system (0.289); malignant pleural mesothelioma (0.094); neoplasm (0.093)
- **Europe PMC papers**: 1456
- **Why important**: BST1 is connected to LRP2 and provides the strongest immune-context signal in the module. It is enriched in bone marrow and intestine, associated with monocyte and neutrophil populations, and has established links to cell-matrix adhesion, cellular extravasation, humoral immune response and actin-cytoskeleton regulation. It also has substantial disease literature.
- **Conclusion**: Established evidence supports BST1 as a marker of stromal or myeloid-associated context and adhesion-related signaling. It raises the possibility that sample composition contributes to the module, but it does not demonstrate immune-cell contamination or a causal relationship with LRP2.

## Module 17

**Tissue pair**: breast and cell line  
**Genes (11)**: CCDC126, RCSD1, DOCK2, HLA-DRB4, FMNL1, GIMAP8, ARHGAP45, PKD2, PTPN7, RAP2A, RSBN1

### Function

The module is most consistent with a hematopoietic immune-cell program involving lymphoid-associated expression, actin-cytoskeleton remodeling, small-GTPase regulation, cell migration, and antigen-presentation context. This interpretation is supported by the functions of DOCK2, ARHGAP45, PTPN7, FMNL1, RCSD1, RAP2A, GIMAP8, and HLA-DRB4, together with the supplementary STRING tissue signals for lymphoid tissue, lymphocytes, and T lymphocytes (STRING TISSUES Lymphoid tissue; within-query FDR = 0.015)(STRING TISSUES Lymphocyte; within-query FDR = 0.015)(STRING TISSUES T-lymphocyte; within-query FDR = 0.015). However, no GO/KEGG term passed global correction, so these annotations are an integrated biological interpretation rather than globally significant enrichment evidence.

**Cell composition.** The module appears strongly influenced by immune and hematopoietic cell composition rather than representing a breast-epithelial program. HPA most frequently links the genes to lymphoid tissue and bone marrow, while single-cell annotations repeatedly implicate neutrophils, B cells, monocytes, macrophages, microglia, hematopoietic progenitors, and related immune populations. Most genes have low blood-cell specificity, so the pattern should not be described as a uniformly blood-cell-specific signature; nevertheless, the repeated lymphoid and myeloid associations support a shared immune-cell or immune-contamination explanation in breast and cell-line samples. Only a minority of genes are secreted, with CCDC126 reported as secreted to blood and PKD2 classified as secreted with unknown location. Breast protein detection is present for several genes, whereas there is no matching HPA tissue result for the cell-line setting. HLA-DRB4 lacks HPA annotation, so its immune interpretation comes from its known class-II antigen-presentation function rather than HPA evidence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The supplementary STRING enrichment points toward lymphoid, lymphocyte, and T-lymphocyte tissue associations (STRING TISSUES Lymphoid tissue; within-query FDR = 0.015)(STRING TISSUES Lymphocyte; within-query FDR = 0.015)(STRING TISSUES T-lymphocyte; within-query FDR = 0.015), especially through the genes DOCK2, ARHGAP45, FMNL1, RCSD1, and GIMAP8. These are functional-enrichment signals and should not be treated as globally corrected module enrichment. No high-confidence STRING interaction was present among the module genes, and no hu.MAP complex contained multiple module members. Thus, the co-abundance structure is not supported by a pre-existing dense protein-interaction network or a known shared complex. The strongest within-module links connect GIMAP8 with several cytoskeletal or signaling genes, connect DOCK2 with HLA-DRB4 and PTPN7, and connect ARHGAP45 with GIMAP8 and PTPN7. These relationships may reflect coordinated cell-state expression, correlated cell composition, or indirect pathway coherence rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 0 of 55 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Lymphoid tissue (FDR = 0.015, 7 genes); TISSUES Lymphocyte (FDR = 0.015, 5 genes); TISSUES T-lymphocyte (FDR = 0.015, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may represent a previously unrecognized co-abundance pattern, but it cannot be called a definitively new biological mechanism. The absence of STRING interactions and hu.MAP complexes means that the exact co-abundance combination is not readily explained by an established physical complex, which supports novelty at the network-observation level. It does not prove novelty because database coverage, tissue context, cell composition, and indirect regulation can all produce absent database links. The repeated immune-cell and lymphoid annotations provide a plausible known biological context, while the particular combination of GIMAP8, cytoskeletal regulators, signaling regulators, HLA-DRB4, and less characterized genes may be novel as a cross-context co-abundance signature. Independent replication, cell-type deconvolution, and perturbation or protein-level validation would be needed to establish that it is more than shared immune-cell composition.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of hematopoietic cells, particularly lymphoid or related immune populations, together with a cell-migration and cytoskeletal-signaling state. In this model, DOCK2 and RAP2A promote or organize small-GTPase-dependent migration and actin remodeling, ARHGAP45 and PTPN7 tune GTPase and phosphorylation signaling, FMNL1 and RCSD1 contribute to cytoskeletal organization, and GIMAP8 marks the associated immune-cell state. HLA-DRB4 may indicate antigen-presenting-cell or class-II presentation context. The co-abundance could therefore arise from a shared immune-cell mixture or state in breast material and cell-line samples, rather than from one physical multiprotein complex. This remains a hypothesis because the module lacks globally significant GO/KEGG enrichment, high-confidence STRING links, and a shared hu.MAP complex.

### Important genes

#### GIMAP8

- **Related proteins** (co-abundance neighbors): ARHGAP45 (0.92), RSBN1 (0.89), PKD2 (0.88), FMNL1 (0.87), RCSD1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GTPase, IMAP family member 8. This gene encodes a protein belonging to the GTP-binding superfamily and to the immuno-associated nucleotide (IAN) subfamily of nucleotide-binding proteins. In humans, the IAN subfamily genes are located in a cluster at 7q36.1. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: corneal dystrophy (0.300); autism (0.111); lung adenocarcinoma (0.089); neoplasm (0.076); Oral ulcer (0.033)
- **Europe PMC papers**: 283
- **Why important**: GIMAP8 has the strongest network position in the module and links several otherwise weakly connected genes, including ARHGAP45, RSBN1, PKD2, FMNL1, and RCSD1. It is a GTP-binding protein in the immune-associated nucleotide family, is tissue-enhanced in lymphoid tissue, and participates in the supplementary lymphoid STRING signal (STRING TISSUES Lymphoid tissue; within-query FDR = 0.015). Its network centrality and immune-associated expression make it a useful marker of the module's cell-state component. Its literature volume is substantial relative to several of the less characterized genes, while its disease associations are comparatively nonspecific.
- **Conclusion**: Established evidence supports GIMAP8 as a central co-abundance marker with lymphoid-associated expression and immune-related molecular identity. It is plausible that GIMAP8 helps report the immune-cell state represented by the module, but the data do not establish that it physically regulates the other module proteins or drives the module.

#### DOCK2

- **Related proteins** (co-abundance neighbors): HLA-DRB4 (0.91), PTPN7 (0.86); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dedicator of cytokinesis 2. The protein encoded by this gene belongs to the CDM protein family. It is specifically expressed in hematopoietic cells and is predominantly expressed in peripheral blood leukocytes. The protein is involved in remodeling of the actin cytoskeleton required for lymphocyte migration in response to chemokine signaling. It activates members of the Rho family of GTPases, for example RAC1 and RAC2, by ac…
- **Diseases (Open Targets)**: DOCK2 deficiency (0.788); severe combined immunodeficiency (0.371); HIV infectious disease (0.370); bipolar disorder (0.346); muscle cramp (0.315)
- **Europe PMC papers**: 3228
- **Why important**: DOCK2 connects HLA-DRB4 with PTPN7 and participates in all of the supplementary lymphoid STRING tissue signals (STRING TISSUES Lymphoid tissue; within-query FDR = 0.015)(STRING TISSUES Lymphocyte; within-query FDR = 0.015)(STRING TISSUES T-lymphocyte; within-query FDR = 0.015). It is preferentially expressed in hematopoietic cells, acts as a guanine-nucleotide exchange factor for RAC-family GTPases, and is linked to lymphocyte migration and actin-cytoskeleton remodeling. It also has a strong disease association with DOCK2 deficiency and a substantial literature base, making it one of the best mechanistic anchors in the module.
- **Conclusion**: Established evidence supports DOCK2 as a hematopoietic migration and cytoskeletal-signaling gene that fits the module's immune-cell interpretation. It may coordinate the inferred motility program, but direct regulation of the other module members is not demonstrated by the available interaction data.

#### ARHGAP45

- **Related proteins** (co-abundance neighbors): GIMAP8 (0.92), PTPN7 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho GTPase activating protein 45. Predicted to enable GTPase activator activity. Predicted to be involved in activation of GTPase activity. Located in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Alzheimer disease (0.338); inflammatory bowel disease (0.316); dementia (0.296); neurodegenerative disease (0.259); anemia (phenotype) (0.099)
- **Europe PMC papers**: 203
- **Why important**: ARHGAP45 is connected to both GIMAP8 and PTPN7 and appears in every supplementary lymphoid STRING signal (STRING TISSUES Lymphoid tissue; within-query FDR = 0.015)(STRING TISSUES Lymphocyte; within-query FDR = 0.015)(STRING TISSUES T-lymphocyte; within-query FDR = 0.015). Its annotated function is regulation of small-GTPase signaling, and HPA links it to bone marrow, lung, intestine, and lymphoid tissue as well as B-cell-related cell types. It therefore provides a direct molecular bridge between the immune-cell composition signal and the inferred Rho-family signaling program, despite having a relatively limited literature volume.
- **Conclusion**: Established evidence supports ARHGAP45 as a plausible regulator of the signaling state represented by the module. Its contribution to the observed co-abundance pattern and its possible cooperation with DOCK2 or PTPN7 remain hypotheses rather than demonstrated molecular interactions.

#### PTPN7

- **Related proteins** (co-abundance neighbors): DOCK2 (0.86), ARHGAP45 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein tyrosine phosphatase non-receptor type 7. The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This gene is preferentially expressed in a variety of hematopoietic cells, and is an early response gene in lymphokine stimulated cel…
- **Diseases (Open Targets)**: neurodegenerative disease (0.296); Precordial pain (0.268); rectosigmoid junction neoplasm (0.264); Abnormality of the skeletal system (0.186); neoplasm (0.094)
- **Europe PMC papers**: 537
- **Why important**: PTPN7 connects DOCK2 and ARHGAP45 and is included in the supplementary lymphoid and lymphocyte signals (STRING TISSUES Lymphoid tissue; within-query FDR = 0.015)(STRING TISSUES Lymphocyte; within-query FDR = 0.015). It is a hematopoietic protein tyrosine phosphatase and an early response gene in lymphokine-stimulated cells, with reported roles in MAPK signaling and protein dephosphorylation. Its established signaling function and larger literature base make it an important candidate for interpreting the module as a regulated immune-cell state rather than a passive abundance signature.
- **Conclusion**: Established evidence supports PTPN7 as a hematopoietic signaling regulator that could tune MAPK and phosphorylation-dependent responses. The module supports coordinated abundance with other immune signaling genes, but does not show that PTPN7 is the causal organizer of the network.

#### HLA-DRB4

- **Related proteins** (co-abundance neighbors): DOCK2 (0.91), RAP2A (0.84), CCDC126 (0.82); STRING partners: none
- **HPA**: no annotation
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: major histocompatibility complex, class II, DR beta 4. HLA-DRB4 belongs to the HLA class II beta chain paralogues. This class II molecule is a heterodimer consisting of an alpha (DRA) and a beta (DRB) chain, both anchored in the membrane. It plays a central role in the immune system by presenting peptides derived from extracellular proteins. Class II molecules are expressed in antigen presenting cells. The beta chain is approximately 26-28 kDa and its…
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 2422
- **Why important**: HLA-DRB4 is the most direct antigen-presentation marker in the module. It encodes a class-II major-histocompatibility beta chain involved in presenting extracellular peptides and connects in the co-abundance graph to DOCK2, RAP2A, and CCDC126. Its extensive literature base and established immune function give it strong interpretive value even though it has no supplementary STRING tissue-term assignment and lacks HPA annotation in this fact sheet.
- **Conclusion**: Established evidence supports HLA-DRB4 as an antigen-presentation context marker, consistent with immune or antigen-presenting-cell material in the samples. Its co-abundance with migration and signaling genes may reflect shared cell composition or coordinated immune activation, but the available evidence does not establish a direct complex or pathway linking these proteins.

## Module 18

**Tissue pair**: breast and cell line  
**Genes (5)**: CLASP2, FKBP11, FSTL5, RBM15, SEMA3C

### Function

The module does not support a single established biochemical pathway: no GO or KEGG term passed global correction, and STRING functional enrichment was absent. Its structure is instead a co-abundance pattern centered on FSTL5, which is connected to RBM15, CLASP2, SEMA3C, and FKBP11, while those peripheral genes are not co-connected in the inferred subgraph. The annotations suggest a mixed program involving neural and retinal cell biology, cytoskeletal organization, extracellular guidance signaling, RNA regulation, and protein folding. Therefore, the most defensible interpretation is a coordinated tissue or cell-state signature rather than a demonstrated canonical pathway. The pattern may reflect shared cellular composition or coordinated expression of otherwise distinct functions.

**Cell composition.** The module is not predominantly a plasma-protein or secreted-protein module: FSTL5 and SEMA3C are secreted, but the other genes are not annotated as secreted. FKBP11 is enriched in plasma cells and enhanced in a MAIT T-cell context, whereas the other genes show low, absent, or limited immune-cell specificity. FSTL5 and CLASP2 are associated with brain and retina, and FSTL5, CLASP2, and SEMA3C show cell-type-enhanced patterns outside breast tissue. RBM15 is tissue-enhanced in bone marrow, and FKBP11 is tissue-enhanced in pancreas. Thus, the module appears compositionally heterogeneous rather than broadly expressed housekeeping-like. The HPA evidence is also sparse for breast protein detection, with only limited direct confirmation and several genes lacking data; there is no matching HPA tissue for the cell-line comparison. A contribution from shared neural, stromal, secretory, or immune-related cell states remains possible, but blood contamination is not established.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship was detected among the module genes, and no hu.MAP complex contained multiple module members. The abundance edges therefore should not be interpreted as established physical protein interactions. The absence of STRING and hu.MAP support indicates that this module is not recapitulating a known protein complex or a densely documented interaction neighborhood. It may instead represent coordinated regulation, shared cellular composition, indirect signaling, or a technical or context-dependent co-abundance pattern. Established functional evidence comes from the individual annotations: RBM15 is linked to RNA processing and RNA methylation, CLASP2 to microtubule and cell-polarity processes, SEMA3C to secreted guidance signaling and developmental morphogenesis, FKBP11 to proline-containing protein folding, and FSTL5 to predicted calcium binding and cell differentiation.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel cross-context co-abundance association, because the module has no matching high-confidence STRING relationships, no multi-member hu.MAP complex, and no globally significant GO or KEGG annotation. Those observations do not prove biological novelty: absence from interaction databases can reflect incomplete coverage, indirect relationships, tissue specificity, or context dependence, and the lack of enrichment can arise from the small and functionally mixed gene set. The appropriate conclusion is that the specific breast–cell-line co-abundance pattern is not explained by the supplied established interaction resources and merits validation, but a claim that it is a new biological module is not yet justified.

**Hypothesis.** Hypothesis: the module reflects a context-dependent cell-state or composition signal in which FSTL5-associated extracellular signaling is co-regulated with cytoskeletal organization through CLASP2, developmental or guidance signaling through SEMA3C, RNA-regulatory control through RBM15, and secretory-protein folding through FKBP11. This could arise from coordinated representation of specialized neural-like, stromal, secretory, or immune-related cell states in the breast and cell-line samples, rather than from direct binding among the encoded proteins. The hypothesis should be tested using independent cohorts, cell-type deconvolution, transcript or protein measurements, and perturbation of the candidate regulatory components.

### Important genes

#### FSTL5

- **Related proteins** (co-abundance neighbors): RBM15 (0.85), CLASP2 (0.84), SEMA3C (0.83), FKBP11 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: follistatin like 5. Predicted to enable calcium ion binding activity. Predicted to be involved in cell differentiation. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: placenta praevia (0.341); retinal degeneration (0.332); Jaundice (0.299); ovarian neoplasm (0.270); Abnormality of the skeletal system (0.250)
- **Europe PMC papers**: 429
- **Why important**: FSTL5 is the network hub, connected to every other module member in the co-abundance subgraph, making it the principal organizing marker of the module. It is associated with brain and retina, is secreted in brain, and has predicted calcium-binding and cell-differentiation functions. Its disease associations include retinal degeneration, ovarian neoplasm, skeletal abnormalities, and other traits, while its literature is substantial. The hub position is network evidence, not proof of molecular binding.
- **Conclusion**: Established: FSTL5 is the strongest module-level marker and has extracellular, neural or retinal, and differentiation-related annotation. Hypothesis: FSTL5 may mark or help coordinate the cell state represented by the module, but a causal role and the direction of regulation remain unproven.

#### RBM15

- **Related proteins** (co-abundance neighbors): FSTL5 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 15. Members of the SPEN (Split-end) family of proteins, including RBM15, have repressor function in several signaling pathways and may bind to RNA through interaction with spliceosome components (Hiriart et al., 2005 [PubMed 16129689]).[supplied by OMIM, Feb 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); lung adenocarcinoma (0.219); esophageal squamous cell carcinoma (0.209); osteosarcoma (0.209); hepatocellular carcinoma (0.206)
- **Europe PMC papers**: 3897
- **Why important**: RBM15 is the module member with the greatest literature volume and is tissue-enhanced in bone marrow, with breast protein detection. Its established annotations connect it to alternative mRNA splicing, RNA methylation, thrombopoietin signaling, and myeloid and megakaryocyte differentiation. It is connected to FSTL5 in the module but lacks STRING and hu.MAP support within this set. Disease-linked associations include neurodegenerative disease and several cancers.
- **Conclusion**: Established: RBM15 is a biologically consequential RNA-regulatory and hematopoietic factor. Hypothesis: its co-abundance with FSTL5 may indicate shared regulation or a bone-marrow-like or differentiation-related cell-state contribution, not a direct RBM15–FSTL5 interaction.

#### CLASP2

- **Related proteins** (co-abundance neighbors): FSTL5 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytoplasmic linker associated protein 2. Enables cytoskeletal protein binding activity; dystroglycan binding activity; and protein tyrosine kinase binding activity. Involved in several processes, including microtubule cytoskeleton organization; positive regulation of extracellular matrix organization; and regulation of supramolecular fiber organization. Located in several cellular components, including basal cortex; cortical microtubule …
- **Diseases (Open Targets)**: neurodegenerative disease (0.423); stricture or kinking of ureter (0.263); Abnormal nasolacrimal system morphology (0.261); myopia (0.253); adult-onset Still disease (0.179)
- **Europe PMC papers**: 748
- **Why important**: CLASP2 provides the clearest cytoskeletal component of the module. It is associated with microtubule organization, microtubule nucleation, Golgi organization, mitotic-spindle organization, cell polarity, extracellular-matrix organization, and cytoskeletal binding. Its HPA pattern is enhanced in brain and retina and in oligodendrocyte and rod-photoreceptor contexts. It has disease associations including neurodegenerative disease and myopia, and a substantial literature.
- **Conclusion**: Established: CLASP2 is a microtubule and cell-polarity regulator with a neural or retinal expression pattern. Hypothesis: its association with FSTL5 may report coordinated structural remodeling or specialized cell morphology in the shared module, but the data do not establish a direct mechanistic link.

#### SEMA3C

- **Related proteins** (co-abundance neighbors): FSTL5 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Golgi apparatus, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: semaphorin 3C. This gene encodes a secreted glycoprotein that belongs to the semaphorin class 3 family of neuronal guidance cues. The encoded protein contains an N-terminal sema domain, integrin and immunoglobulin-like domains, and a C-terminal basic domain. Homodimerization and proteolytic cleavage of the C-terminal propeptide are necessary for the function of the encoded protein. It binds a neuropilin co-recep…
- **Diseases (Open Targets)**: atrial fibrillation (0.518); coronary artery disorder (0.455); neurodegenerative disease (0.446); glaucoma (0.438); open-angle glaucoma (0.432)
- **Europe PMC papers**: 2154
- **Why important**: SEMA3C is a secreted semaphorin and supplies a plausible extracellular signaling component. Its established biology includes neuropilin and plexin-associated guidance signaling, neural crest migration, and cardiovascular developmental morphogenesis. HPA detects cell-type enhancement in several epithelial, stromal, and pigment-cell contexts and immune-cell enrichment in basophils. Its disease associations include atrial fibrillation, coronary artery disease, glaucoma, and neurodegenerative disease, with a substantial literature.
- **Conclusion**: Established: SEMA3C is an extracellular guidance cue with broad developmental and disease relevance. Hypothesis: it may mediate or mark extracellular communication associated with the FSTL5-centered state, although no physical interaction or pathway enrichment supports that mechanism here.

#### FKBP11

- **Related proteins** (co-abundance neighbors): FSTL5 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enhanced; location Centrosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FKBP prolyl isomerase 11. FKBP11 belongs to the FKBP family of peptidyl-prolyl cis/trans isomerases, which catalyze the folding of proline-containing polypeptides. The peptidyl-prolyl isomerase activity of FKBP proteins is inhibited by the immunosuppressant compounds FK506 and rapamycin (Rulten et al., 2006 [PubMed 16596453]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: alcohol drinking (0.103); osteosarcoma (0.081); smoking initiation (0.080); hepatocellular carcinoma (0.061); nonpapillary renal cell carcinoma (0.060)
- **Europe PMC papers**: 831
- **Why important**: FKBP11 contributes a protein-folding interpretation distinct from the other genes. It is a prolyl isomerase involved in folding proline-containing polypeptides and is tissue-enhanced in pancreas and enriched in plasma cells, with immune-cell enhancement in MAIT T cells. Its protein was not detected in breast by the supplied HPA evidence. It also has disease-linked associations including osteosarcoma, hepatocellular carcinoma, and renal cancer.
- **Conclusion**: Established: FKBP11 is a secretory or immune-associated protein-folding factor whose expression pattern differs from the neural and cytoskeletal members. Hypothesis: its co-abundance with FSTL5 may reflect a shared secretory-load or cell-composition signal rather than participation in a common molecular complex.

## Module 19

**Tissue pair**: breast and cell line  
**Genes (5)**: CLSPN, SLC1A3, PDE5A, PDZD8, TNXB

### Function

The module does not support a single established pathway or molecular process. No GO or KEGG term passed global correction, and there were no supplementary STRING enrichment terms. Its network is a star centered on TNXB, with CLSPN, PDE5A, PDZD8, and SLC1A3 connected to TNXB but not to one another. The genes represent extracellular-matrix biology, DNA-replication checkpoint control, cyclic-nucleotide signaling, organelle lipid and calcium handling, and glutamate transport. Therefore, the most cautious interpretation is a conserved co-abundance pattern rather than a demonstrated functional complex or pathway. The pattern may reflect shared regulation, cellular composition, or an indirect relationship centered on TNXB.

**Cell composition.** The module is not predominantly a plasma-protein or broadly expressed housekeeping module. TNXB is a secreted extracellular-matrix protein, whereas the other genes are intracellular or membrane-associated. HPA evidence indicates substantial cell-type specificity: several genes are enhanced in progenitor populations, including erythrocyte, megakaryocyte, and neutrophil progenitors, while SLC1A3 is associated with glial cell types and selected myeloid populations. Tissue associations include bone marrow, brain, retina, lymphoid tissue, testis, and adrenal gland. Most genes are not detected in immune cells, although SLC1A3 has enrichment in monocyte and myeloid dendritic-cell groups. Thus, sample composition or shared rare cell types could contribute to the breast and cell-line co-abundance signal. Breast protein detection is available for only part of the module, and no matching HPA tissue evidence is provided for the cell line.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was detected among the module genes, and no hu.MAP complex contained multiple module members. The absence of these relationships means that the co-abundance edges are not supported here as established physical protein interactions or membership in a known multiprotein complex. It is compatible with indirect regulation, shared cellular context, correlated abundance caused by sample composition, or an interaction that is condition-specific or insufficiently represented in those resources. It does not by itself invalidate the module.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be claimed as a new biological complex or pathway. Its star-shaped structure, lack of globally significant GO or KEGG enrichment, absence of supplementary STRING enrichment, lack of high-confidence STRING interactions, and lack of a hu.MAP complex all limit mechanistic support. At the same time, absence from STRING or hu.MAP does not prove novelty, because those databases emphasize known physical or curated relationships and may miss context-dependent co-abundance. The defensible conclusion is that this is a potentially novel cross-context co-abundance pattern whose biological novelty remains unestablished and requires independent replication, cell-composition adjustment, and targeted validation.

**Hypothesis.** Hypothesis: the module may represent a context-dependent transcriptional or abundance program linking TNXB-associated extracellular-matrix state with distinct proliferative, metabolic, signaling, and neural or glial features in the sampled material. TNXB could mark stromal or matrix-related context, while the other genes may report particular cell states or mixtures of progenitor, neural-associated, and contractile or signaling populations. A shared cell-type composition effect is an alternative hypothesis and may be more plausible than direct molecular cooperation, given the lack of known pairwise interactions and complexes. This hypothesis should be tested by single-cell deconvolution, replication in independent breast and cell-line datasets, and perturbation of TNXB-associated cellular context.

### Important genes

#### TNXB

- **Related proteins** (co-abundance neighbors): CLSPN (0.92), PDE5A (0.85), PDZD8 (0.82), SLC1A3 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tenascin XB. This gene encodes a member of the tenascin family of extracellular matrix glycoproteins. The tenascins have anti-adhesive effects, as opposed to fibronectin which is adhesive. This protein is thought to function in matrix maturation during wound healing, and its deficiency has been associated with the connective tissue disorder Ehlers-Danlos syndrome. This gene localizes to the major histocompatib…
- **Diseases (Open Targets)**: Ehlers-Danlos syndrome due to tenascin-X deficiency (0.795); vesicoureteral reflux 8 (0.703); Abnormality of the cardiovascular system (0.550); Ehlers-Danlos syndrome (0.522); hereditary disease (0.390)
- **Europe PMC papers**: 2382
- **Why important**: TNXB is the central network gene, connected to every other module member, and is the only clear topological hub. It encodes an extracellular-matrix tenascin with anti-adhesive properties and reported roles in matrix maturation, wound healing, cell adhesion, actin organization, collagen metabolism, and cell differentiation. Its disease associations include tenascin-X deficiency and Ehlers-Danlos syndrome, and it has substantial literature coverage. HPA places it in extracellular matrix secretion and associates it with stromal, neural, and progenitor-related cell types.
- **Conclusion**: Established evidence supports TNXB as the network anchor and as an extracellular-matrix and connective-tissue gene with disease relevance. It is not established that TNXB directly regulates the other module genes or that it creates the observed co-abundance pattern. Its hub position makes it the leading candidate marker of the module, but not proof of a causal role.

#### SLC1A3

- **Related proteins** (co-abundance neighbors): TNXB (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Nucleoli, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 1 member 3. This gene encodes a member of a member of a high affinity glutamate transporter family. This gene functions in the termination of excitatory neurotransmission in central nervous system. Mutations are associated with episodic ataxia, Type 6. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Feb 2014].
- **Diseases (Open Targets)**: episodic ataxia type 6 (0.768); neurodegenerative disease (0.491); osteoporosis (0.439); episodic ataxia type 2 (0.387); autoimmune disorder of central nervous system (0.370)
- **Europe PMC papers**: 3774
- **Why important**: SLC1A3 is functionally distinctive because it encodes a high-affinity glutamate transporter involved in neurotransmitter uptake and glutamate transport. It has the largest literature representation among the module genes and is associated with episodic ataxia type six and other neurological or immune-related disease annotations. HPA links it to brain and retina, astrocytes, ependymal cells, microglia, macrophages, and selected myeloid populations. Its connection to the TNXB hub may therefore help identify a neural, glial, or cell-composition component of the module.
- **Conclusion**: Established evidence supports SLC1A3 as a glutamate-transporter gene with strong neural and selected myeloid cell-type associations. It is not established that its connection with TNXB reflects direct regulation or a shared pathway. In this module, SLC1A3 may be a particularly informative indicator of cellular composition or context rather than a core member of a physical complex.

#### CLSPN

- **Related proteins** (co-abundance neighbors): TNXB (0.92); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: claspin. The product of this gene is an essential upstream regulator of checkpoint kinase 1 and triggers a checkpoint arrest of the cell cycle in response to replicative stress or DNA damage. The protein is also required for efficient DNA replication during a normal S phase. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2010].
- **Diseases (Open Targets)**: myoepithelial tumor (0.111); cancer (0.108); neoplasm (0.106); gastric cancer (0.079); melanoma (0.079)
- **Europe PMC papers**: 1263
- **Why important**: CLSPN encodes claspin, an upstream regulator of checkpoint kinase one that supports DNA replication and checkpoint responses to replication stress or DNA damage. HPA associates it with bone marrow, lymphoid tissue, testis, retina, and progenitor populations, including erythrocyte and megakaryocyte progenitors. Its position is peripheral, connected only to TNXB, but its cell-cycle checkpoint function gives the module a possible proliferative or progenitor-state component. Its disease and cancer annotations provide additional biological relevance.
- **Conclusion**: Established evidence supports CLSPN as a DNA-replication and damage-checkpoint regulator with progenitor-associated expression. The module does not establish a mechanistic link between CLSPN and TNXB, nor does it demonstrate enrichment for cell-cycle biology. Its presence is therefore best treated as a candidate marker of a proliferative or progenitor-related state.

#### PDE5A

- **Related proteins** (co-abundance neighbors): TNXB (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphodiesterase 5A. This gene encodes a cGMP-binding, cGMP-specific phosphodiesterase, a member of the cyclic nucleotide phosphodiesterase family. This phosphodiesterase specifically hydrolyzes cGMP to 5'-GMP. It is involved in the regulation of intracellular concentrations of cyclic nucleotides and is important for smooth muscle relaxation in the cardiovascular system. Alternative splicing of this gene results in th…
- **Diseases (Open Targets)**: coronary artery disorder (0.666); erectile dysfunction (0.615); pulmonary arterial hypertension (0.609); benign prostatic hyperplasia (0.607); pulmonary hypertension (0.596)
- **Europe PMC papers**: 1763
- **Why important**: PDE5A encodes a cGMP-specific phosphodiesterase that controls cyclic-nucleotide signaling and is important for smooth-muscle relaxation. It is associated with cardiovascular and pulmonary vascular disorders and is detected in breast tissue by HPA. Its cell-type associations include adipocytes, cardiomyocytes, epicardial cells, fibro-adipogenic progenitors, and myonuclei. Although it is a peripheral node, its connection to TNXB may indicate a stromal, vascular, contractile, or tissue-remodeling context.
- **Conclusion**: Established evidence supports PDE5A as a cyclic-GMP signaling regulator with cardiovascular and contractile-tissue relevance. The data do not establish that PDE5A and TNXB participate in one pathway in this module. PDE5A is best interpreted as a contextual signaling marker whose co-abundance may reflect tissue or cell-state composition.

#### PDZD8

- **Related proteins** (co-abundance neighbors): TNXB (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ domain containing 8. Predicted to enable lipid binding activity and metal ion binding activity. Involved in several processes, including mitochondrial calcium ion homeostasis; mitochondrion-endoplasmic reticulum membrane tethering; and regulation of cell morphogenesis. Located in endoplasmic reticulum membrane and mitochondria-associated endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Apr 20…
- **Diseases (Open Targets)**: intellectual developmental disorder with autism and dysmorphic facies (0.577); Global developmental delay (0.372); Intellectual disability (0.371); Hypertelorism (0.370); Abnormality of the face (0.370)
- **Europe PMC papers**: 424
- **Why important**: PDZD8 is a less extensively studied module member, but its reported functions include lipid binding, mitochondrial calcium homeostasis, mitochondria-endoplasmic-reticulum tethering, lipophagy, and intermembrane lipid transfer. HPA associates it with bone marrow and progenitor populations, including erythrocyte, megakaryocyte, megakaryocyte-erythroid, and neutrophil progenitors. It is a peripheral node connected only to TNXB, yet it may provide a metabolic or organelle-homeostasis dimension to the module.
- **Conclusion**: Established evidence supports PDZD8 as an organelle-contact, lipid-handling, and calcium-homeostasis gene with progenitor-associated expression. Its relationship to TNXB is not established as direct or mechanistic. Because its literature base is more limited than that of the other selected genes, its role in the module remains especially hypothesis-generating.

## Module 20

**Tissue pair**: breast and cell line  
**Genes (6)**: FAM111A, KRIT1, SCEL, TOR4A, PLAU, XDH

### Function

No GO/KEGG term passed global multiple-testing correction, and there was no supplementary STRING functional enrichment. Therefore, the module does not support a statistically established shared pathway or biological process from enrichment analysis. Its gene annotations instead indicate a heterogeneous combination of purine oxidative metabolism through XDH, extracellular proteolysis and plasminogen activation through PLAU, cell junction, integrin, Rap1 and endothelial regulatory functions through KRIT1, DNA replication and damage-response functions through FAM111A, epithelial differentiation and cornified-envelope biology through SCEL, and a poorly characterized torsin-family protein represented by TOR4A. The module is therefore best interpreted as a coordinated expression pattern whose biological meaning remains unresolved rather than as a demonstrated canonical pathway.

**Cell composition.** The module is heterogeneous rather than dominated by plasma or secreted proteins. PLAU is secreted to blood and has blood-cell-enriched HPA annotations, but the other genes are not described as secreted proteins; XDH is intracellular and membrane-associated, while SCEL is plasma-membrane localized. HPA tissue evidence spans breast, esophagus, skin, kidney and urinary bladder, with several genes broadly expressed and others showing epithelial or organ-associated enrichment. Single-cell annotations include epithelial populations, renal epithelial populations, myeloid and granulocytic progenitors, and dendritic or neutrophil-related blood-cell categories. This mixed pattern argues against a simple blood-only explanation, although PLAU and its immune-cell enrichment make blood, vascular, inflammatory or stromal contributions plausible in bulk samples. Breast protein detection is present for part of the module and absent for the remainder, so the shared breast and cell-line signal may also reflect common epithelial, proliferative or stress-related cellular states rather than one uniform cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was recorded among the module genes, and no hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated here as established physical protein interactions or membership in a known multiprotein complex. The strongest co-abundance connectivity is centered on XDH, which connects to SCEL, KRIT1, FAM111A and TOR4A, while PLAU connects to TOR4A. This network topology may identify coordinated regulation, shared cellular context, or indirect biology, but it should not be interpreted as evidence that these proteins directly bind one another. The lack of STRING and hu.MAP support is informative about prior interaction knowledge, not evidence that the co-abundance pattern is artifactual.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent an under-characterized cross-context co-abundance pattern, because its member combination lacks supporting high-confidence STRING interactions, lacks a shared hu.MAP complex, and lacks a globally significant GO/KEGG annotation. However, these absences do not establish that the module is a new biological discovery. Several member genes have substantial prior literature and established disease or cellular functions, so novelty is more defensibly claimed for the specific coordinated expression relationship across breast and cell-line samples, not for the individual genes or for a newly discovered pathway. Independent replication, preservation testing in additional cohorts, adjustment for cell composition and technical covariates, and targeted protein or perturbation experiments would be required before calling the module novel and mechanistically meaningful.

**Hypothesis.** Hypothesis: the module reflects a shared epithelial or tissue-state program that combines epithelial barrier or differentiation features, extracellular proteolytic remodeling, purine redox metabolism, vascular or junctional regulation, and cell-cycle or replication-associated activity. XDH may act as the expression-network anchor, with TOR4A linking the metabolic-centered portion to PLAU-associated extracellular remodeling. This could arise from a common stress, remodeling or proliferative state in breast samples and cell lines, or from variation in epithelial, stromal and immune admixture. This is a hypothesis rather than an established pathway: the absence of globally significant enrichment, STRING support and hu.MAP complexes means that direct molecular coupling remains unproven.

### Important genes

#### XDH

- **Related proteins** (co-abundance neighbors): SCEL (0.87), KRIT1 (0.86), FAM111A (0.85), TOR4A (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: xanthine dehydrogenase. Xanthine dehydrogenase belongs to the group of molybdenum-containing hydroxylases involved in the oxidative metabolism of purines. The encoded protein has been identified as a moonlighting protein based on its ability to perform mechanistically distinct functions. Xanthine dehydrogenase can be converted to xanthine oxidase by reversible sulfhydryl oxidation or by irreversible proteolytic modificat…
- **Diseases (Open Targets)**: xanthinuria type I (0.735); gout (0.698); hyperuricemia (0.612); leukemia (0.603); lymphoma (0.603)
- **Europe PMC papers**: 17182
- **Why important**: XDH is the most connected and strongest network member, linking several otherwise weakly connected genes. Its established function in molybdenum-dependent purine oxidative metabolism gives the module a plausible metabolic anchor, and its moonlighting capability broadens possible cellular interpretations. It has extensive literature and disease associations including xanthinuria, gout and hyperuricemia, while HPA places it in a breast-associated tissue group and in lactating breast cells.
- **Conclusion**: Established evidence supports XDH as a purine-metabolism enzyme and as the central co-abundance node. It is reasonable to prioritize XDH for validation, but it is not established that XDH functionally drives the other module genes. Its hub status may reflect shared regulation or sample composition rather than direct biochemical control.

#### PLAU

- **Related proteins** (co-abundance neighbors): TOR4A (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Group enriched; location Golgi apparatus, Vesicles; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plasminogen activator, urokinase. This gene encodes a secreted serine protease that converts plasminogen to plasmin. The encoded preproprotein is proteolytically processed to generate A and B polypeptide chains. These chains associate via a single disulfide bond to form the catalytically inactive high molecular weight urokinase-type plasminogen activator (HMW-uPA). HMW-uPA can be further processed into the catalytically active low…
- **Diseases (Open Targets)**: Quebec platelet disorder (0.616); abdominal aortic aneurysm (0.515); myocardial infarction (0.494); inflammatory bowel disease (0.486); Recurrent thrombophlebitis (0.370)
- **Europe PMC papers**: 15345
- **Why important**: PLAU provides the clearest extracellular and disease-relevant functional component: it is a secreted serine protease that converts plasminogen to plasmin and is involved in proteolysis, chemotaxis and cell migration-related processes. It is the module member with blood-cell-enriched HPA annotations and is detected in breast tissue. Its extensive literature and associations with vascular, inflammatory and thrombotic disorders make it important for interpreting possible stromal, immune or extracellular-remodeling contributions.
- **Conclusion**: Established evidence supports PLAU as a secreted proteolytic and migratory regulator with potential blood or tissue-remodeling relevance. Its inclusion does not prove that the whole module is a blood module, because most members are not secreted or blood-cell enriched. A role for PLAU in linking the module to extracellular remodeling is plausible but remains a hypothesis.

#### KRIT1

- **Related proteins** (co-abundance neighbors): XDH (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: KRIT1 ankyrin repeat containing. This gene encodes a protein containing four ankyrin repeats, a band 4.1/ezrin/radixin/moesin (FERM) domain, and multiple NPXY sequences. The encoded protein is localized in the nucleus and cytoplasm. It binds to integrin cytoplasmic domain-associated protein-1 alpha (ICAP1alpha), and plays a critical role in beta1-integrin-mediated cell proliferation. It associates with junction proteins and RAS-r…
- **Diseases (Open Targets)**: cerebral cavernous malformation 1 (0.754); cerebral cavernous malformation (0.681); famililal cerebral cavernous malformations (0.675); hereditary disease (0.519); cavernous hemangioma (0.417)
- **Europe PMC papers**: 1214
- **Why important**: KRIT1 is directly connected to the central XDH node and has an established role in junctional integrity, beta-one-integrin-associated signaling, Rap1-related biology, endothelial proliferation and angiogenesis regulation. It has a strong disease connection to cerebral cavernous malformation and related vascular disorders. Its renal epithelial single-cell enrichment and vesicular localization also fit a possible epithelial or vascular-state interpretation.
- **Conclusion**: Established evidence supports KRIT1 as a junctional and vascular signaling regulator with major disease relevance. Its co-abundance with XDH may indicate a shared tissue-state or vascular-associated program, but there is no evidence here for a direct XDH–KRIT1 molecular interaction or for a vascular disease mechanism in this module.

#### FAM111A

- **Related proteins** (co-abundance neighbors): XDH (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FAM111 trypsin like peptidase A. The protein encoded by this gene is cell-cycle regulated, and has nuclear localization. The C-terminal half of the protein shares homology with trypsin-like peptidases and it contains a PCNA-interacting peptide (PIP) box, that is necessary for its co-localization with proliferating cell nuclear antigen (PCNA). Reduced expression of this gene resulted in DNA replication defects, consistent with the…
- **Diseases (Open Targets)**: osteocraniostenosis (0.734); autosomal dominant Kenny-Caffey syndrome (0.722); Kenny-Caffey syndrome (0.596); prostate carcinoma (0.542); prostate cancer (0.498)
- **Europe PMC papers**: 495
- **Why important**: FAM111A is connected to XDH and contributes a distinct nuclear function involving cell-cycle regulation, PCNA-associated DNA replication, replication-fork processing and DNA damage response. It has established disease associations including Kenny-Caffey syndrome and osteocraniostenosis, as well as cancer associations. Its nuclear localization and enrichment in monocyte and neutrophil progenitor categories make it useful for testing whether the module reflects proliferation or cellular-state composition.
- **Conclusion**: Established evidence supports FAM111A as a replication- and genome-maintenance-related protein. Its presence may indicate a proliferative component in the shared signal, but the module data do not demonstrate that replication biology explains the entire module or that FAM111A regulates the other members.

## Module 21

**Tissue pair**: breast and cell line  
**Genes (5)**: FTO, HELZ, PIK3R4, ROR2, SNRPA1

### Function

The module does not support a specific pathway assignment. No GO or KEGG term passed global correction, so there are no globally significant GO/KEGG terms; there are also no supplementary supplementary STRING terms or STRING functional-enrichment terms. The network is organized around ROR2, which is connected to FTO, PIK3R4, HELZ, and SNRPA1, but the partners represent diverse functions: receptor signaling, RNA modification and metabolism, phosphoinositide signaling and autophagy, RNA helicase activity, and spliceosomal RNA processing. The most defensible interpretation is therefore a co-abundance module reflecting coordinated regulation or shared cellular state rather than a demonstrated single biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: every gene is annotated as non-secreted. HPA reports low tissue specificity across the module, with cell-type enhancement distributed across several distinct epithelial, stromal, germ-cell, and trophoblast populations. ROR2 is annotated as immune-cell enriched in MAIT cells, whereas the other genes have low immune-cell specificity. Protein detection is reported for most module genes in breast, while there is no matching HPA tissue for the cell-line context. These observations argue against a simple plasma-protein or blood-cell module, but they do not exclude contributions from shared cell states or mixed cellular composition in breast and cell-line samples.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship among module members is the interaction between PIK3R4 and SNRPA1. No other module-member pair has STRING support at the stated threshold, and no hu.MAP complex contains multiple module members. Thus, the network is not corroborated as a known multiprotein complex. The PIK3R4-SNRPA1 relationship provides some evidence of molecular association, but the broader module topology, especially the ROR2-centered connectivity, should be interpreted primarily as a co-abundance pattern rather than as a validated physical interaction network.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: PIK3R4–SNRPA1 (0.777)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears to be a potentially novel co-abundance association, but it cannot be claimed as a newly discovered biological pathway. The lack of global GO or KEGG enrichment, STRING enrichment, and shared hu.MAP complexes means that established pathway or complex evidence is weak. At the same time, absence from STRING or hu.MAP alone does not establish novelty, because these resources are incomplete and the module could reflect transcriptional, post-transcriptional, cell-state, or sample-composition effects. The strongest novelty claim is therefore that this particular cross-context co-abundance pattern may be under-documented, not that the underlying gene functions are novel.

**Hypothesis.** Hypothesis: the module may represent a coordinated cellular-state program linking ROR2-associated receptor signaling with intracellular trafficking or autophagy through PIK3R4, and with RNA regulation through FTO, HELZ, and SNRPA1. ROR2 may act as the abundance-level connector while the other genes report downstream changes in signaling, RNA metabolism, and protein or organelle turnover. This model is provisional: the absence of globally significant enrichment and the lack of a shared hu.MAP complex mean that the relationships could instead arise from correlated cell composition or indirect regulation. Testing should include replication across independent breast and cell-line datasets, perturbation of ROR2 or PIK3R4, and measurement of RNA processing, autophagy-related trafficking, and receptor-signaling outputs.

### Important genes

#### ROR2

- **Related proteins** (co-abundance neighbors): FTO (0.86), PIK3R4 (0.84), HELZ (0.81), SNRPA1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ROR family WNT receptor 2. The protein encoded by this gene is a receptor protein tyrosine kinase and type I transmembrane protein that belongs to the ROR subfamily of cell surface receptors.  The protein may be involved in the early formation of the chondrocytes and may be required for cartilage and growth plate development.  Mutations in this gene can cause brachydactyly type B, a skeletal disorder characterized by hypopl…
- **Diseases (Open Targets)**: autosomal recessive Robinow syndrome (0.811); brachydactyly type B1 (0.759); Robinow syndrome (0.643); Abnormality of the skeletal system (0.560); neurodegenerative disease (0.502)
- **Europe PMC papers**: 4123
- **Why important**: ROR2 is the central network gene, connected to every other module member, and is a receptor tyrosine kinase involved in signal transduction, cell-surface receptor signaling, and positive regulation of cell migration. It has extensive literature coverage and established disease associations involving skeletal development and Robinow syndrome. HPA also places it in several cell-type-enhanced contexts and identifies MAIT-cell enrichment, making it relevant both to signaling biology and to possible cellular-composition effects.
- **Conclusion**: Established evidence supports ROR2 as the module's topological hub and as a biologically important receptor. It is not established that ROR2 drives the co-abundance module or directly interacts with the other members. Its role as an upstream coordinator is therefore a hypothesis requiring perturbational validation.

#### PIK3R4

- **Related proteins** (co-abundance neighbors): ROR2 (0.84); STRING partners: SNRPA1 (0.777)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles, Microtubules, Primary cilium; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoinositide-3-kinase regulatory subunit 4. Predicted to enable protein serine/threonine kinase activity. Involved in positive regulation of phosphatidylinositol 3-kinase activity; receptor catabolic process; and regulation of cytokinesis. Located in late endosome and microtubule cytoskeleton. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.538); COVID-19 (0.465); dengue disease (0.370); severe acute respiratory syndrome (0.370); central nervous system malformation (0.262)
- **Europe PMC papers**: 1088
- **Why important**: PIK3R4 is connected to ROR2 and has the module's only STRING-supported relationship with SNRPA1. Its annotations link it to phosphatidylinositol-kinase regulation, receptor catabolism, cytokinesis, lysosomal targeting, pexophagy, and macroautophagy. Its vesicular, microtubular, and primary-cilium localization makes it a plausible bridge between receptor-associated signaling and intracellular trafficking. It has a substantial disease and literature record, although less extensive than ROR2 or FTO.
- **Conclusion**: Established evidence supports PIK3R4 as a regulator of phosphoinositide-related signaling and autophagy-associated trafficking, and STRING supports its association with SNRPA1. It is not established that PIK3R4 connects ROR2 signaling to the RNA-processing genes in this module. That bridging function remains a hypothesis.

#### FTO

- **Related proteins** (co-abundance neighbors): ROR2 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FTO alpha-ketoglutarate dependent dioxygenase. This gene is a nuclear protein of the AlkB related non-haem iron and 2-oxoglutarate-dependent oxygenase superfamily but the exact physiological function of this gene is not known. Other non-heme iron enzymes function to reverse alkylated DNA and RNA damage by oxidative demethylation. Studies in mice and humans indicate a role in nervous and cardiovascular systems and a strong association with body…
- **Diseases (Open Targets)**: lethal polymalformative syndrome, Boissel type (0.711); obesity disorder (0.698); type 2 diabetes mellitus (0.629); diabetes mellitus (0.620); osteoarthritis (0.599)
- **Europe PMC papers**: 16853
- **Why important**: FTO is directly connected to the ROR2 hub and is a well-studied nuclear or cytosolic dioxygenase associated with RNA and DNA repair-related chemistry, RNA processing, lipid storage, temperature homeostasis, and organismal growth. It has very extensive literature coverage and established disease associations involving obesity, diabetes, and related metabolic phenotypes. Its respiratory-ciliated-cell enhancement adds a possible cell-state context without implying tissue specificity.
- **Conclusion**: Established evidence supports FTO as a major regulator of nucleic-acid and metabolic biology with strong disease relevance. The module does not establish a direct functional connection between FTO and ROR2, nor does it identify an FTO-dependent mechanism. Any role for FTO in coordinating the module is therefore hypothetical.

#### SNRPA1

- **Related proteins** (co-abundance neighbors): ROR2 (0.80); STRING partners: PIK3R4 (0.777)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: small nuclear ribonucleoprotein polypeptide A'. Enables RNA binding activity. Involved in mRNA splicing, via spliceosome and spermatogenesis. Located in nuclear speck. Part of U2-type catalytic step 2 spliceosome and U2-type precatalytic spliceosome. Implicated in connective tissue disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.538); dengue disease (0.370); phosphorus metabolism disease (0.196); hypotensive disorder (0.196); cancer (0.087)
- **Europe PMC papers**: 520
- **Why important**: SNRPA1 is a spliceosomal RNA-binding protein involved in U2-type spliceosome assembly and pre-mRNA splicing. It is connected to ROR2 in the co-abundance network and has the only STRING-supported pair in the module, linking it to PIK3R4. Its nucleoplasmic localization and enhancement in reproductive and trophoblast-related cell types make it relevant to RNA-processing and cellular-state interpretations. It has a moderate literature record and reported disease associations.
- **Conclusion**: Established evidence supports SNRPA1 as a core spliceosomal component and supports its molecular association with PIK3R4 through STRING. It is not established that splicing changes generate the module or that SNRPA1 participates in ROR2 signaling. Those connections are hypotheses.

#### HELZ

- **Related proteins** (co-abundance neighbors): ROR2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: helicase with zinc finger. HELZ is a member of the superfamily I class of RNA helicases. RNA helicases alter the conformation of RNA by unwinding double-stranded regions, thereby altering the biologic activity of the RNA molecule and regulating access to other proteins (Wagner et al., 1999 [PubMed 10471385]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Hypercholesterolemia (0.336); Abnormal brain morphology (0.266); smoking initiation (0.234); ovarian neoplasm (0.178); autoimmune thyroid disease (0.174)
- **Europe PMC papers**: 303
- **Why important**: HELZ is an RNA helicase associated with RNA remodeling, post-transcriptional gene silencing, translational repression, and deadenylation-dependent mRNA decay. It is connected to ROR2 and is annotated in a Sertoli-cell-enhanced context. Its literature volume is smaller than that of the other selected genes, which makes it valuable as a potentially under-characterized component rather than as an already established pathway marker.
- **Conclusion**: Established evidence supports HELZ as an RNA-regulatory helicase. The module provides no enrichment or complex evidence establishing that HELZ participates in a shared pathway with ROR2, PIK3R4, FTO, or SNRPA1. Its proposed role in a coordinated post-transcriptional program is therefore exploratory.
