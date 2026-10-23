# Conserved co-abundance modules: autonomic_nervous_system and lung

## Module 0

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (7)**: SLC1A5, PPIL2, SAE1, HM13, SUCLA2, TIMM50, TOMM40

### Function

The module most plausibly reflects coordinated intracellular protein and energy homeostasis, with a prominent mitochondrial component. TIMM50 and TOMM40 support mitochondrial precursor import, while SUCLA2 supports tricarboxylic-acid-cycle metabolism. SLC1A5 contributes neutral amino-acid and glutamine transport, SAE1 contributes SUMO-dependent post-translational regulation, HM13 contributes intramembrane proteolysis, and PPIL2 contributes protein folding and RNA-splicing-related functions. These annotations describe plausible component functions, but no GO or KEGG term passed global correction, so the module should not be assigned a formally enriched pathway. The network topology is consistent with a compact, mixed mitochondrial, membrane, metabolic, and protein-homeostasis program rather than a single demonstrated pathway.

**Cell composition.** All module proteins were detected in lung, whereas there was no matching HPA tissue result for autonomic nervous system. The module contains no secreted genes and is not dominated by blood-cell-enriched proteins: most genes have low immune-cell specificity, with only SLC1A5 showing immune-cell enhancement in plasmacytoid dendritic cells. Most genes also have low tissue specificity, which is compatible with broadly expressed intracellular or housekeeping-type biology. The cell-type annotations are heterogeneous, including reproductive, epithelial, and enteric-related cell populations, so a shared cell-composition effect cannot be excluded. The HPA profile does not support a plasma-protein or generalized blood-contamination explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known STRING relationship within the module is the TIMM50–TOMM40 pair, consistent with their complementary roles in mitochondrial protein import. No other within-module STRING relationship met the supplied high-confidence threshold, no STRING functional enrichment was reported, and no hu.MAP complex contained multiple module members. Thus, the network contains one biologically coherent known mitochondrial connection, while the remaining co-abundance edges are not independently supported by the supplied interaction or complex resources. Co-abundance therefore indicates coordinated expression or protein abundance, not physical interaction among all module members.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: TIMM50–TOMM40 (0.971)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is not established as a new molecular complex or a newly discovered pathway by the available evidence. The TIMM50–TOMM40 relationship is already known in STRING, and the individual functions of the genes are established. However, the particular cross-tissue co-abundance grouping may represent a context-specific observation, because most of its edges lack high-confidence STRING support and no multi-member hu.MAP complex was found. That observation is hypothesis-generating rather than proof of novelty: absence from STRING or hu.MAP alone cannot establish that the module is novel. Replication, tissue-cell deconvolution, and independent perturbation or interaction data would be needed.

**Hypothesis.** Hypothesis: in lung and autonomic-nervous-system-related samples, a broadly expressed intracellular program couples mitochondrial protein import and mitochondrial metabolic capacity with amino-acid availability and stress-responsive protein regulation. TIMM50 and TOMM40 may form the mitochondrial-import core; SUCLA2 may report respiratory metabolic demand; SLC1A5 may couple extracellular nutrient transport to that demand; and SAE1, HM13, and PPIL2 may reflect accompanying protein-modification, membrane-processing, and proteostasis responses. This is a mechanistic model, not a demonstrated causal pathway.

### Important genes

#### TIMM50

- **Related proteins** (co-abundance neighbors): SUCLA2 (0.88), SLC1A5 (0.86), HM13 (0.81); STRING partners: TOMM40 (0.971)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translocase of inner mitochondrial membrane 50. This gene encodes a subunit of the TIM23 inner mitochondrial membrane translocase complex. The encoded protein functions as the receptor subunit that recognizes the mitochondrial targeting signal, or presequence, on protein cargo that is destined for the mitochondrial inner membrane and matrix. This protein may also play a role in maintaining the membrane permeability barrier, and knockdown of thi…
- **Diseases (Open Targets)**: 3-methylglutaconic aciduria type 9 (0.773); neurodegenerative disease (0.519); Mitochondrial encephalopathy (0.425); hereditary disease (0.415); Epileptic encephalopathy (0.370)
- **Europe PMC papers**: 442
- **Why important**: TIMM50 has the strongest network position and connects to SUCLA2, SLC1A5, and HM13. Its established function as a receptor subunit of the mitochondrial inner-membrane TIM23 translocase makes it a central candidate for the module's mitochondrial interpretation. It is also linked in the supplied disease evidence to mitochondrial and neurodegenerative disorders, and its literature record supports substantial biological attention.
- **Conclusion**: Established: TIMM50 participates in mitochondrial presequence recognition and mitochondrial protein import, and its perturbation can promote cytochrome-c release and apoptosis. Hypothesis: its central co-abundance position may organize or report a mitochondrial proteostasis state shared across the tissues.

#### TOMM40

- **Related proteins** (co-abundance neighbors): HM13 (0.81), SAE1 (0.81); STRING partners: TIMM50 (0.971)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translocase of outer mitochondrial membrane 40. The protein encoded by this gene is localized in the outer membrane of the mitochondria. It is the channel-forming subunit of the translocase of the mitochondrial outer membrane (TOM) complex that is essential for import of protein precursors into mitochondria. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Aug 2015].
- **Diseases (Open Targets)**: Alzheimer disease (0.325); dementia (0.269); metabolic syndrome (0.262); chronic kidney disease (0.224); Lewy body dementia (0.205)
- **Europe PMC papers**: 2387
- **Why important**: TOMM40 is directly connected to TIMM50 in STRING and occupies a bridging position between TIMM50, HM13, and SAE1 in the co-abundance graph. As the channel-forming subunit of the mitochondrial outer-membrane TOM complex, it complements TIMM50's inner-membrane import role. It has extensive literature coverage and supplied associations with Alzheimer disease, dementia, metabolic syndrome, and Lewy body dementia.
- **Conclusion**: Established: TOMM40 is a core component of mitochondrial outer-membrane precursor import. Hypothesis: its linkage with TIMM50 indicates that coordinated abundance of the outer- and inner-membrane import machinery contributes to the shared module.

#### SUCLA2

- **Related proteins** (co-abundance neighbors): TIMM50 (0.88), PPIL2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase ADP-forming subunit beta. Succinyl-CoA synthetase (SCS) is a mitochondrial matrix enzyme that acts as a heterodimer, being composed of an invariant alpha subunit and a substrate-specific beta subunit. The protein encoded by this gene is an ATP-specific SCS beta subunit that dimerizes with the SCS alpha subunit to form SCS-A, an essential component of the tricarboxylic acid cycle. SCS-A hydrolyzes ATP to convert succinate t…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome, encephalomyopathic form with methylmalonic aciduria (0.816); mitochondrial DNA depletion syndrome, encephalomyopathic form (0.581); neurodegenerative disease (0.485); mitochondrial disease (0.374); disease of peritoneum (0.372)
- **Europe PMC papers**: 1440
- **Why important**: SUCLA2 is one of the stronger internal connectors and links to TIMM50 and PPIL2. Its established role as the ATP-specific beta subunit of succinyl-CoA synthetase places it directly in mitochondrial tricarboxylic-acid-cycle metabolism. The supplied disease evidence connects it to mitochondrial DNA depletion syndromes and other mitochondrial disease, while its literature coverage is substantial.
- **Conclusion**: Established: SUCLA2 supports succinyl-CoA, succinate, and related mitochondrial metabolism. Hypothesis: its co-abundance with mitochondrial import genes may mark coordinated matching of mitochondrial protein supply with energetic or biosynthetic demand.

#### SLC1A5

- **Related proteins** (co-abundance neighbors): TIMM50 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 1 member 5. The SLC1A5 gene encodes a sodium-dependent neutral amino acid transporter that can act as a receptor for RD114/type D retrovirus (Larriba et al., 2001 [PubMed 11781704]).[supplied by OMIM, Jan 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.463); substance abuse (0.231); attention deficit-hyperactivity disorder (0.231); autoimmune disorder of central nervous system (0.213); hypotensive disorder (0.188)
- **Europe PMC papers**: 5038
- **Why important**: SLC1A5 is the module's connection to the plasma membrane and is linked to TIMM50. Its established function is sodium-dependent transport of neutral amino acids, including glutamine and serine, providing a plausible interface between nutrient availability and mitochondrial activity. It has the largest literature record among the module genes and supplied associations with neurological and immune-related disorders.
- **Conclusion**: Established: SLC1A5 mediates neutral amino-acid transport. Hypothesis: its coupling to TIMM50 may reflect nutrient-sensitive regulation of mitochondrial protein homeostasis, although the co-abundance data do not establish directionality or causation.

#### SAE1

- **Related proteins** (co-abundance neighbors): TOMM40 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SUMO1 activating enzyme subunit 1. Posttranslational modification of proteins by the addition of the small protein SUMO (see SUMO1; MIM 601912), or sumoylation, regulates protein structure and intracellular localization. SAE1 and UBA2 (MIM 613295) form a heterodimer that functions as a SUMO-activating enzyme for the sumoylation of proteins (Okuma et al., 1999 [PubMed 9920803]).[supplied by OMIM, Mar 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.476); lysosomal storage disease (0.292); diabetes mellitus (0.268); lymphoid leukemia (0.267); obesity disorder (0.242)
- **Europe PMC papers**: 1843
- **Why important**: SAE1 is connected to TOMM40 and represents a regulatory arm of the module. It forms the SUMO-activating enzyme with UBA2, so its established function can influence protein structure, localization, and stress responses. It has substantial literature coverage and supplied associations with neurodegenerative, metabolic, and malignant conditions.
- **Conclusion**: Established: SAE1 is required for activation of SUMO-dependent protein modification. Hypothesis: its co-abundance with TOMM40 may reflect SUMO-mediated regulation of mitochondrial proteins or cellular stress adaptation, but no direct interaction or causal link within this module is established by the supplied evidence.

## Module 1

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (34)**: AATF, ACIN1, RNPEP, ASNS, BRI3BP, CHD4, CPSF1, CPSF6, CSTF3, DDX46, HPRT1, MCM5, PPP1R12A, NAA15, NELFCD, NUP155, NUP205, NUDT5, NUP93, OSBPL9, PRP4K, RBBP7, RDH11, PDCD11, RRS1, SMARCC2, SUPT5H, SRRT, SSR1, CARS1, TCERG1, TMX1, UTP4, ZFR

### Function

The strongest interpretation is a nuclear gene-expression and RNA-processing module. The primary evidence is the globally corrected enrichment for nuclear protein-containing complexes (GO:CC nuclear protein-containing complex; q_global = 0.00151), which includes nucleoporins, pre-mRNA processing factors, transcriptional regulators, chromatin remodelers, and ribosome-biogenesis factors. The supplementary STRING terms support capped intron-containing pre-mRNA processing, nuclear-lumen localization, and RNA metabolism (STRING RCTM Processing of Capped Intron-Containing Pre-mRNA; within-query FDR = 0.0017)(STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0018)(STRING RCTM Metabolism of RNA; within-query FDR = 0.0073). The network therefore appears to combine nuclear transport with RNA maturation, transcriptional control, and chromatin regulation rather than representing a tissue-specific metabolic pathway. The co-abundance pattern is consistent with coordinated abundance of broadly required nuclear machinery.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the HPA summary identifies only a small minority of secreted genes, and most proteins are intracellular or nuclear. Most genes have low tissue specificity and low immune-cell specificity, arguing against a blood-cell or plasma-protein explanation. HPA protein detection in lung is common among the assessed genes, while there is no matching autonomic-nervous-system tissue dataset in the supplied HPA comparison. Several genes have cell-type-enhanced patterns in reproductive, renal, neural, epithelial, or progenitor populations, but these patterns are heterogeneous rather than forming a coherent autonomic-nervous-system or lung signature. A shared contribution from broadly expressed housekeeping machinery, cellular composition, or sample quality remains plausible.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC nuclear protein-containing complex | 0.00151 | AATF, ACIN1, CHD4, CPSF1, CPSF6, CSTF3, DDX46, MCM5, NELFCD, NUP155, NUP205, NUP93, PDCD11, PRP4K, RBBP7, SMARCC2, SUPT5H, UTP4 |

### STRING and hu.MAP

STRING provides established relationships within several coherent subgroups. The NUP155–NUP205–NUP93 relationships support a nuclear-pore-complex component; CPSF1–CPSF6–CSTF3 support pre-mRNA cleavage and polyadenylation; DDX46–TCERG1 and PRP4K–SRRT–TCERG1 support RNA processing; NELFCD–SUPT5H supports transcriptional pausing and elongation; and CHD4–RBBP7–SMARCC2 supports chromatin-remodeling machinery. AATF, PDCD11, RRS1, and UTP4 form a further nucleolar and ribosome-biogenesis-associated group. hu.MAP independently places PRP4K, SRRT, and ACIN1 in several spliceosome or RNA-processing complexes (hu.MAP huMAP3_09621.1)(hu.MAP huMAP3_11073.1)(hu.MAP huMAP3_09943.1)(hu.MAP huMAP3_07248.1)(hu.MAP huMAP3_08365.1)(hu.MAP huMAP3_09637.1)(hu.MAP huMAP3_10564.1), NUP93 and NUP205 in complexes associated with nuclear-pore components (hu.MAP huMAP3_07789.1)(hu.MAP huMAP3_05673.1)(hu.MAP huMAP3_09042.1), CPSF1 and CSTF3 in cleavage and polyadenylation complexes (hu.MAP huMAP3_00102.1)(hu.MAP huMAP3_09096.1)(hu.MAP huMAP3_11757.1), and CHD4 with RBBP7 in chromatin-remodeling complexes (hu.MAP huMAP3_09499.1)(hu.MAP huMAP3_10472.1)(hu.MAP huMAP3_15128.1). These known relationships show that much of the module recapitulates established molecular machinery. They support biological coherence, but they do not by themselves establish that the co-abundance module is a new physical complex or a direct interaction among all genes.

**STRING interactions (score >= 0.7)**: 21 of 561 gene pairs: AATF–PDCD11 (0.989); AATF–UTP4 (0.997); ACIN1–CHD4 (0.82); CHD4–RBBP7 (0.999); CHD4–SMARCC2 (0.775); CHD4–SRRT (0.76); CPSF1–CPSF6 (0.987); CPSF1–CSTF3 (0.999); CPSF6–CSTF3 (0.867); CPSF6–SRRT (0.732); DDX46–TCERG1 (0.927); NELFCD–SUPT5H (0.998); NUP155–NUP205 (0.999); NUP155–NUP93 (0.999); NUP205–NUP93 (0.999); PDCD11–RRS1 (0.786); PDCD11–UTP4 (0.999); PRP4K–SRRT (0.891); PRP4K–TCERG1 (0.927); RRS1–UTP4 (0.739); SRRT–TCERG1 (0.839)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Processing of Capped Intron-Containing Pre-mRNA (FDR = 0.0017, 11 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0018, 20 genes); RCTM Metabolism of RNA (FDR = 0.0073, 14 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09621.1 (PRP4K, SRRT, ACIN1; 3/56); huMAP3_11073.1 (PRP4K, SRRT, ACIN1; 3/67); huMAP3_09943.1 (PRP4K, SRRT, ACIN1; 3/78); huMAP3_07789.1 (NUP93, NUP205; 2/7); huMAP3_05673.1 (NUP93, NUP205; 2/11); huMAP3_07248.1 (PRP4K, ACIN1; 2/12); huMAP3_08365.1 (PRP4K, ACIN1; 2/12); huMAP3_00102.1 (CPSF1, CSTF3; 2/12); huMAP3_09096.1 (CPSF1, CSTF3; 2/15); huMAP3_11757.1 (CPSF1, CSTF3; 2/16); huMAP3_09637.1 (PRP4K, ACIN1; 2/21); huMAP3_09042.1 (NUP93, NUP205; 2/26); huMAP3_09499.1 (CHD4, RBBP7; 2/33); huMAP3_10472.1 (CHD4, RBBP7; 2/36); huMAP3_10564.1 (SRRT, ACIN1; 2/37); huMAP3_15128.1 (CHD4, RBBP7; 2/96)

### Novelty

The module should not be described as a newly discovered molecular complex. Many of its relationships and subassemblies are already represented by STRING and hu.MAP, and the primary GO evidence points to a broad nuclear-complex category rather than a novel pathway. Its potentially novel aspect is the conserved co-abundance of these established nuclear-machinery components across autonomic nervous system and lung samples. That observation may be useful as a cross-tissue systems-level signature, but novelty would require validation in independent cohorts, control for cell composition and technical effects, and comparison with existing co-expression or proteomic modules. Absence of a gene from STRING or hu.MAP is not evidence of novelty.

**Hypothesis.** Hypothesis: the shared module reflects coordinated demand for nuclear gene-expression capacity in cells present in both tissue groups. Nuclear pore components may support nucleocytoplasmic transport, RNA-processing factors may coordinate transcript maturation and export, transcriptional elongation and chromatin-remodeling factors may regulate expression, and nucleolar factors may support ribosome biogenesis. A common cellular state involving active transcription, RNA processing, and protein-production capacity could therefore generate the conserved co-abundance pattern. This remains a hypothesis; the supplied data do not demonstrate causality, direct co-assembly of the full module, or a specific autonomic-lung physiological mechanism.

### Important genes

#### NUP93

- **Related proteins** (co-abundance neighbors): RDH11 (0.84), NUP205 (0.83), TCERG1 (0.83), CPSF6 (0.81); STRING partners: NUP155 (0.999), NUP205 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_07789.1, huMAP3_05673.1, huMAP3_09042.1
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 is a central bridge between the nuclear-pore subgroup and RNA-processing-associated neighbors in the module. It is part of the globally significant nuclear protein-containing-complex term (GO:CC nuclear protein-containing complex; q_global = 0.00151), appears in the STRING RNA-processing and nuclear-lumen terms (STRING RCTM Processing of Capped Intron-Containing Pre-mRNA; within-query FDR = 0.0017)(STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0018)(STRING RCTM Metabolism of RNA; within-query FDR = 0.0073), has established STRING relationships with NUP155 and NUP205, and occurs in multiple hu.MAP complexes (hu.MAP huMAP3_07789.1)(hu.MAP huMAP3_05673.1)(hu.MAP huMAP3_09042.1). Its annotation directly supports nuclear transport, nuclear-pore organization, and RNA export. Its disease associations include nephrotic syndromes and viral infectious disease, and its literature volume is substantial.
- **Conclusion**: Established evidence supports NUP93 as a nuclear-pore and nucleocytoplasmic-transport component that links the module to RNA export and nuclear organization. The module data support coordinated abundance with other nuclear machinery, but do not show that NUP93 drives the shared tissue phenotype.

#### CPSF6

- **Related proteins** (co-abundance neighbors): AATF (0.89), NUP93 (0.81), NUP205 (0.80), NELFCD (0.80); STRING partners: CPSF1 (0.987), CSTF3 (0.867), SRRT (0.732)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cleavage and polyadenylation specific factor 6. The protein encoded by this gene is one subunit of a cleavage factor required for 3' RNA cleavage and polyadenylation processing. The interaction of the protein with the RNA is one of the earliest steps in the assembly of the 3' end processing complex and facilitates the recruitment of other processing factors. The cleavage factor complex is composed of four polypeptides. This gene encodes the 68k…
- **Diseases (Open Targets)**: cancer (0.579); neurodegenerative disease (0.463); Abnormality of the skeletal system (0.451); smoking initiation (0.424); leukemia (0.376)
- **Europe PMC papers**: 1665
- **Why important**: CPSF6 connects the network hub ZFR-associated neighborhood with NUP93, NUP205, AATF, and NELFCD. It is included in (GO:CC nuclear protein-containing complex; q_global = 0.00151) and all three supplementary STRING terms (STRING RCTM Processing of Capped Intron-Containing Pre-mRNA; within-query FDR = 0.0017)(STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0018)(STRING RCTM Metabolism of RNA; within-query FDR = 0.0073), and STRING links it to CPSF1, CSTF3, and SRRT. Its established function in cleavage-factor assembly, mRNA three-prime-end processing, RNA export, and alternative polyadenylation gives the module a direct transcript-maturation interpretation. It has substantial literature and disease associations spanning cancer, neurodegenerative disease, skeletal abnormalities, smoking initiation, and leukemia.
- **Conclusion**: Established evidence supports CPSF6 as a core pre-mRNA three-prime-processing component that connects RNA maturation with nuclear organization in this module. A role in tissue-specific transcript selection is plausible, but the supplied co-abundance data do not establish altered alternative polyadenylation.

#### CHD4

- **Related proteins** (co-abundance neighbors): ZFR (0.87), PDCD11 (0.81); STRING partners: ACIN1 (0.82), RBBP7 (0.999), SMARCC2 (0.775), SRRT (0.76)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_09499.1, huMAP3_10472.1, huMAP3_15128.1
- **Function (MyGene.info)**: chromodomain helicase DNA binding protein 4. The product of this gene belongs to the SNF2/RAD54 helicase family. It represents the main component of the nucleosome remodeling and deacetylase complex and plays an important role in epigenetic transcriptional repression. Patients with dermatomyositis develop antibodies against this protein. Somatic mutations in this gene are associated with serous endometrial tumors. Alternative splicing result…
- **Diseases (Open Targets)**: Sifrim-Hitz-Weiss syndrome (0.810); neurodegenerative disease (0.551); hereditary disease (0.505); endometrial cancer (0.470); uterine carcinosarcoma (0.439)
- **Europe PMC papers**: 3617
- **Why important**: CHD4 links the module to chromatin remodeling and transcriptional repression. It is present in (GO:CC nuclear protein-containing complex; q_global = 0.00151), has STRING relationships with ACIN1, RBBP7, SMARCC2, and SRRT, and participates with RBBP7 in several hu.MAP chromatin-remodeling complexes (hu.MAP huMAP3_09499.1)(hu.MAP huMAP3_10472.1)(hu.MAP huMAP3_15128.1). Its annotation identifies it as a principal component of the nucleosome-remodeling and deacetylase complex, with roles in chromatin remodeling, transcriptional repression, DNA repair, and cell-fate regulation. It has a substantial literature base and disease associations including developmental syndromes and endometrial cancer.
- **Conclusion**: Established evidence supports CHD4 as the principal chromatin-regulatory arm of the module, complementing its RNA-processing and nuclear-transport components. The data support coordinated chromatin and RNA regulation, but do not establish a specific target-gene program in autonomic nervous system or lung.

#### PRP4K

- **Related proteins** (co-abundance neighbors): RBBP7 (0.81), DDX46 (0.80); STRING partners: SRRT (0.891), TCERG1 (0.927)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09621.1, huMAP3_11073.1, huMAP3_09943.1, huMAP3_07248.1, huMAP3_08365.1, huMAP3_09637.1
- **Function (MyGene.info)**: pre-mRNA processing factor kinase PRP4K. Pre-mRNA splicing occurs in two sequential transesterification steps, and the protein encoded by this gene is thought to be involved in pre-mRNA splicing and in signal transduction. This protein belongs to a kinase family that includes serine/arginine-rich protein-specific kinases and cyclin-dependent kinases (CDKs). This protein is regarded as a CDK-like kinase (Clk) with homology to mitogen-acti…
- **Diseases (Open Targets)**: skin neoplasm (0.235); cardiomyopathy (0.227); placenta praevia (0.225); ovarian dysfunction (0.194); glomerulonephritis (0.096)
- **Europe PMC papers**: 126
- **Why important**: PRP4K is a kinase associated with pre-mRNA processing and spliceosome assembly. It is included in (GO:CC nuclear protein-containing complex; q_global = 0.00151), connects to DDX46 and RBBP7 in the module network, and is repeatedly represented with SRRT and ACIN1 in hu.MAP RNA-processing complexes (hu.MAP huMAP3_09621.1)(hu.MAP huMAP3_11073.1)(hu.MAP huMAP3_09943.1)(hu.MAP huMAP3_07248.1)(hu.MAP huMAP3_08365.1)(hu.MAP huMAP3_09637.1). STRING also supports relationships with SRRT and TCERG1. Although its literature volume is smaller than that of several other selected genes, its functional specificity and repeated complex membership make it informative for the spliceosomal interpretation. Its disease associations include skin neoplasm, cardiomyopathy, placental disorders, ovarian dysfunction, and glomerulonephritis.
- **Conclusion**: Established evidence supports PRP4K as a spliceosome-associated regulatory kinase within the RNA-processing arm of the module. It is a plausible mechanistic connector, but the co-abundance pattern does not show kinase activity or identify a specific phosphorylation-dependent process.

#### ZFR

- **Related proteins** (co-abundance neighbors): CHD4 (0.87), MCM5 (0.86), OSBPL9 (0.83), NUP155 (0.83), CPSF1 (0.82), HPRT1 (0.82), UTP4 (0.82), CARS1 (0.81), ASNS (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger RNA binding protein. This gene encodes an RNA-binding protein characterized by its DZF (domain associated with zinc fingers) domain. The encoded protein may play a role in the nucleocytoplasmic shuttling of another RNA-binding protein, Staufen homolog 2, in neurons. Expression of this gene is regulated through alternative polyadenylation that mediates differential microRNA targeting. Elevated expression of this gene h…
- **Diseases (Open Targets)**: neurodegenerative disease (0.483); autosomal recessive spastic paraplegia type 71 (0.370); hyperaldosteronism (0.320); placental abruption (0.311); hearing loss disorder (0.242)
- **Europe PMC papers**: 793
- **Why important**: ZFR has the strongest network connectivity in the supplied module and connects genes from nuclear transport, RNA processing, nucleotide metabolism, translation-related functions, and cellular maintenance. HPA places it in the nucleoplasm with low tissue and cell-type specificity, and the supplied annotation describes an RNA-binding protein involved in nucleocytoplasmic shuttling and alternative-polyadenylation-linked regulation. It has disease associations including neurodegenerative disease and spastic paraplegia, and a substantial literature volume. It lacks listed STRING partners, hu.MAP complexes, and enriched-term membership, making its network position especially useful as a co-abundance observation rather than as independently corroborated complex evidence.
- **Conclusion**: Established evidence supports ZFR as a broadly expressed nuclear RNA-binding protein and a prominent module-network connector. Its position may indicate coordination across several nuclear processes, but the absence of listed STRING and hu.MAP support means that any specific bridging mechanism remains tentative.

## Module 2

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (21)**: ABHD10, ALCAM, CS, CKAP4, HADHB, AHCTF1, ETFA, GTPBP10, NT5DC2, OCIAD1, ORC4, RAB5C, UPF3B, MRPL48, MRPL50, MRPS18B, SETD7, SMARCA1, SRCAP, SUPV3L1, TOP2A

### Function

No GO or KEGG term passed global correction, so the module should not be assigned a formally enriched pathway. Its gene content nevertheless supports a composite mitochondrial and cellular-maintenance interpretation. A prominent substructure connects mitochondrial protein synthesis and RNA handling through GTPBP10, MRPL50, MRPL48, MRPS18B, and SUPV3L1, while another connects mitochondrial energy metabolism through CS, ETFA, and HADHB. Additional genes represent DNA replication and chromosome management, chromatin remodeling, RNA surveillance, endosomal transport, cell adhesion, and nuclear pore biology. The relatively high-connectivity position of GTPBP10 links several of these otherwise distinct processes. Thus, the most defensible interpretation is coordinated abundance of broadly required mitochondrial, metabolic, and genome-maintenance proteins rather than a narrowly defined tissue-specific pathway. The absence of globally significant GO or KEGG enrichment does not invalidate the module, but it limits pathway-level certainty.

**Cell composition.** The module is not predominantly plasma-derived or secreted: only ALCAM is annotated as secreted to blood, while the other genes are not secreted. HPA indicates that most genes have low tissue specificity, with a smaller subset showing tissue-enhanced or tissue-enriched expression. The frequent lung protein detection is consistent with the module being measurable in lung, but does not establish lung-specific biology. Many genes are cell-type enhanced, including cardiomyocyte, epithelial, muscle-associated, progenitor, neuronal, and reproductive cell annotations. Several genes have immune-cell-enhanced annotations, but most have low immune-cell specificity and one is not detected in immune cells. Therefore, the shared module could partly reflect common cell populations or general cellular abundance across autonomic nervous system and lung samples, but the evidence does not support describing it as a blood-cell or plasma-protein module. Its broad expression and mitochondrial content make a housekeeping or cellular-composition contribution plausible.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a partial network of established relationships. The strongest metabolic links are CS with HADHB and ETFA with HADHB, while GTPBP10 connects to MRPL50 and the mitochondrial ribosomal proteins MRPL48 and MRPS18B. hu.MAP provides independent complex-level support for a mitochondrial RNA or mitoribosome-associated substructure: SUPV3L1, MRPL50, and MRPL48 co-occur in (hu.MAP huMAP3_06589.1); MRPL50 and MRPL48 co-occur in (hu.MAP huMAP3_06439.1); and SUPV3L1 and MRPL50 co-occur in (hu.MAP huMAP3_09113.1). These observations indicate that portions of the module recover known mitochondrial protein complexes or functional neighborhoods. Conversely, many module edges have no reported STRING partner or hu.MAP support, and the databases do not establish one unified complex containing all module genes. The network is therefore best viewed as a co-abundance structure containing several known molecular submodules, with additional cross-submodule associations that require experimental validation.

**STRING interactions (score >= 0.7)**: 6 of 210 gene pairs: CS–HADHB (0.951); ETFA–HADHB (0.829); GTPBP10–MRPL50 (0.868); MRPL48–MRPL50 (0.966); MRPL48–MRPS18B (0.933); MRPL50–MRPS18B (0.89)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06589.1 (SUPV3L1, MRPL50, MRPL48; 3/79); huMAP3_06439.1 (MRPL50, MRPL48; 2/57); huMAP3_09113.1 (SUPV3L1, MRPL50; 2/72)

### Novelty

The exact conserved co-abundance module shared by autonomic nervous system and lung may represent a potentially new systems-level observation, especially because it combines mitochondrial translation, mitochondrial metabolism, genome maintenance, adhesion, and trafficking in one cross-tissue pattern. However, it cannot be called wholly novel merely because some edges are absent from STRING or hu.MAP. The mitoribosome relationships, mitochondrial RNA-processing relationships, and CS–ETFA–HADHB metabolic relationships are already supported by established biology. The defensible novelty claim is therefore limited: the tissue-pair-specific co-abundance organization and its cross-submodule arrangement may be novel, whereas several component relationships are known. Confirmation would require replication in independent cohorts, control for cell composition, comparison with existing tissue co-expression modules, and testing whether the cross-submodule links persist after adjustment for mitochondrial abundance and proliferating-cell content.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in autonomic nervous system and lung in which mitochondrial proteome maintenance, mitochondrial translation, and oxidative fuel utilization are coordinated with RNA quality control and genome-maintenance demands. GTPBP10 and the mitoribosomal proteins may mark the mitochondrial translation component; CS, ETFA, and HADHB may mark energy and fatty-acid utilization; and TOP2A, ORC4, SMARCA1, SETD7, and related genes may reflect a proliferative or DNA-maintenance component. ALCAM, RAB5C, and CKAP4 could represent cell-surface, vesicular, or epithelial-context contributions rather than a direct mitochondrial mechanism. This model predicts that the module will track mitochondrial abundance and selected cell states, and that its apparent conservation will weaken or change after rigorous adjustment for cell composition. It should be tested rather than treated as an established causal pathway.

### Important genes

#### GTPBP10

- **Related proteins** (co-abundance neighbors): ALCAM (0.92), ABHD10 (0.88), MRPS18B (0.88), SUPV3L1 (0.87), CS (0.87), MRPL50 (0.86), TOP2A (0.85), HADHB (0.84); STRING partners: MRPL50 (0.868)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GTP binding protein 10. Small G proteins, such as GTPBP10, act as molecular switches that play crucial roles in the regulation of fundamental cellular processes such as protein synthesis, nuclear transport, membrane trafficking, and signal transduction (Hirano et al., 2006 [PubMed 17054726]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); Abnormality of the skeletal system (0.266); bone Paget disease (0.178); type 2 diabetes mellitus (0.097); placenta praevia (0.075)
- **Europe PMC papers**: 153
- **Why important**: GTPBP10 has the most central network position in the supplied graph and connects mitochondrial ribosomal genes with CS, ETFA, HADHB, SUPV3L1, and additional regulatory or cellular genes. Its annotation includes mitochondrial large ribosomal subunit assembly, making it a plausible bridge between mitochondrial translation and metabolism. Its disease associations include neurodegenerative disease and skeletal-system abnormalities, while its literature volume is modest relative to heavily studied core metabolic genes.
- **Conclusion**: Established evidence supports GTPBP10 as a network hub with a role in mitochondrial large ribosomal subunit assembly and as a connector to several metabolic genes. The hypothesis that it coordinates the metabolic and mitoribosomal arms of this module is plausible from network position but is not established by the enrichment results.

#### CS

- **Related proteins** (co-abundance neighbors): GTPBP10 (0.87), ETFA (0.86), CKAP4 (0.83); STRING partners: HADHB (0.951)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS is a canonical mitochondrial tricarboxylic-acid-cycle enzyme and connects in the module to GTPBP10, ETFA, CKAP4, and HADHB. It provides a well-established anchor for oxidative metabolism and has an exceptionally extensive literature base. Its disease associations include neurodegenerative and central nervous system autoimmune disorders, although those associations do not by themselves explain the shared module.
- **Conclusion**: Established evidence identifies CS as a mitochondrial matrix enzyme central to citrate and carbohydrate metabolism. Its module placement supports an oxidative-metabolism component, but the co-abundance data do not demonstrate that CS mechanistically regulates the other genes.

#### HADHB

- **Related proteins** (co-abundance neighbors): GTPBP10 (0.84), ALCAM (0.80); STRING partners: CS (0.951), ETFA (0.829)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydroxyacyl-CoA dehydrogenase trifunctional multienzyme complex subunit beta. This gene encodes the beta subunit of the mitochondrial trifunctional protein, which catalyzes the last three steps of mitochondrial beta-oxidation of long chain fatty acids. The mitochondrial membrane-bound heterocomplex is composed of four alpha and four beta subunits, with the beta subunit catalyzing the 3-ketoacyl-CoA thiolase activity. The encoded protein can also bind RNA and decreases the s…
- **Diseases (Open Targets)**: mitochondrial trifunctional protein deficiency 2 (0.802); mitochondrial trifunctional protein deficiency (0.782); mitochondrial trifunctional protein deficiency 1 (0.700); long chain 3-hydroxyacyl-CoA dehydrogenase deficiency (0.520); hypertrophic cardiomyopathy (0.388)
- **Europe PMC papers**: 2162
- **Why important**: HADHB is a subunit of the mitochondrial trifunctional protein and is connected to GTPBP10, CS, and ETFA. This gives it a strong biochemical position at the intersection of long-chain fatty-acid oxidation and the module's other mitochondrial metabolic signals. It has substantial literature and clear disease associations with mitochondrial trifunctional protein deficiency and related fatty-acid oxidation disorders.
- **Conclusion**: Established evidence supports HADHB as a mitochondrial beta-oxidation enzyme and explains its known relationships with CS and ETFA. Its connection to the mitoribosome-associated genes is a module-level association and should be regarded as a hypothesis about coordinated mitochondrial state, not as proof of direct interaction.

#### MRPL50

- **Related proteins** (co-abundance neighbors): GTPBP10 (0.86); STRING partners: GTPBP10 (0.868), MRPL48 (0.966), MRPS18B (0.89)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_06589.1, huMAP3_06439.1, huMAP3_09113.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein L50. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.494); ankylosing spondylitis (0.060); osteonecrosis (0.049); Genu varum (0.030); Genu valgum (0.030)
- **Europe PMC papers**: 173
- **Why important**: MRPL50 is embedded in the most coherent known mitochondrial complex structure in the module. It is supported by STRING links to MRPL48, MRPS18B, and GTPBP10 and by all three hu.MAP complex records (hu.MAP huMAP3_06589.1), (hu.MAP huMAP3_06439.1), and (hu.MAP huMAP3_09113.1). Its annotation places it in mitochondrial translation, and its disease associations include neurodegenerative disease and skeletal abnormalities. Its literature volume is smaller than that of CS or TOP2A, making the module context particularly informative.
- **Conclusion**: Established evidence supports MRPL50 as a mitochondrial ribosomal protein participating in a known mitoribosomal neighborhood. Its network position makes it a strong marker of the module's mitochondrial translation component. A broader role in coordinating mitochondrial metabolism remains a hypothesis.

#### TOP2A

- **Related proteins** (co-abundance neighbors): SMARCA1 (0.86), UPF3B (0.86), GTPBP10 (0.85), MRPL48 (0.82), ORC4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA topoisomerase II alpha. This gene encodes a DNA topoisomerase, an enzyme that controls and alters the topologic states of DNA during transcription. This nuclear enzyme is involved in processes such as chromosome condensation, chromatid separation, and the relief of torsional stress that occurs during DNA transcription and replication. It catalyzes the transient breaking and rejoining of two strands of duplex DNA which al…
- **Diseases (Open Targets)**: neoplasm (0.618); breast cancer (0.616); acute myeloid leukemia (0.606); plasma cell myeloma (0.594); small cell lung carcinoma (0.580)
- **Europe PMC papers**: 11752
- **Why important**: TOP2A is a highly connected non-mitochondrial node linked to SMARCA1, UPF3B, GTPBP10, MRPL48, and ORC4. Its established functions include DNA topology control, chromosome condensation, chromatid separation, replication-related DNA management, and DNA damage response. It has a very extensive literature base and disease associations spanning neoplasms and acute myeloid leukemia. Its HPA annotations also point to progenitor and proliferative cell contexts.
- **Conclusion**: Established evidence supports TOP2A as a nuclear genome-maintenance and proliferation-associated enzyme. Its presence suggests that the module may partly reflect proliferating or progenitor-cell abundance, but it does not establish a direct mechanistic bridge to mitochondrial translation.

#### ALCAM

- **Related proteins** (co-abundance neighbors): GTPBP10 (0.92), ETFA (0.81), HADHB (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: activated leukocyte cell adhesion molecule. This gene encodes activated leukocyte cell adhesion molecule (ALCAM), also known as CD166 (cluster of differentiation 166), which is a member of a subfamily of immunoglobulin receptors with five immunoglobulin-like domains (VVC2C2C2) in the extracellular domain. This protein binds to T-cell differentiation antigene CD6, and is implicated in the processes of cell adhesion and migration. Multiple al…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.458); mathematical ability (0.453); open-angle glaucoma (0.396); restless legs syndrome (0.379); ovarian dysfunction (0.362)
- **Europe PMC papers**: 4212
- **Why important**: ALCAM is a highly connected module node linked to GTPBP10, ETFA, and HADHB. It is a cell-adhesion and migration receptor, is associated with alveolar and other epithelial cell types, is tissue-enriched in parathyroid gland, and is annotated as secreted to blood. Its disease and trait associations include open-angle glaucoma, restless legs syndrome, and ovarian dysfunction. Its literature volume is substantial, providing broader biological context than many of the less studied module genes.
- **Conclusion**: Established evidence supports ALCAM as a cell-adhesion and migration molecule with relevance to epithelial and immune-cell contexts. Its placement may indicate cell-composition or tissue-interface effects in the shared module. A direct role in coupling adhesion to mitochondrial metabolism is only a hypothesis.

## Module 3

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (5)**: ACADVL, ATAD1, MPDU1, PRXL2A, METTL1

### Function

The module does not have a demonstrated single pathway-level function: no GO or KEGG term passed global correction. Its gene-level annotations point to several compatible cellular processes rather than one established program. MPDU1 supports endoplasmic-reticulum lipid-linked oligosaccharide and glycosylphosphatidylinositol biosynthesis, ACADVL supports mitochondrial long-chain fatty-acid beta-oxidation, METTL1 supports tRNA guanine methylation and tRNA stabilization, PRXL2A supports cellular oxidant detoxification, and ATAD1 supports extraction of mislocalized proteins from the mitochondrial outer membrane. The co-abundance pattern therefore suggests a possible relationship among protein processing, mitochondrial or metabolic stress, RNA maintenance, and redox or proteostasis functions, but this remains an interpretation rather than an enrichment result.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins, and it is not strongly blood-cell enriched. Four genes have low tissue specificity and low immune-cell specificity, while one gene, PRXL2A, is secreted in other tissues and is immune-cell enriched in plasmacytoid dendritic cells. HPA detects all module proteins in lung, whereas there is no matching autonomic-nervous-system HPA tissue result. Single-cell annotations are heterogeneous, including trophoblast, esophageal, spermatid, cardiomyocyte, retinal, endometrial, epididymal, and plasmacytoid-dendritic-cell contexts. This heterogeneity argues against a simple blood-contamination explanation, while the broad tissue distribution means that shared cellular composition or a general cellular-state signal remains possible.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional-enrichment term was reported, no high-confidence STRING interaction was reported among any module gene pair, and no hu.MAP complex contained at least two module members. Thus the module is not supported by the supplied reference interaction or complex resources. Its strongest co-abundance connection is MPDU1 with each of ACADVL, METTL1, PRXL2A, and ATAD1, but these co-abundance links should not be treated as established physical or functional interactions. The absence of database support limits mechanistic confidence but does not invalidate the co-abundance observation.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported co-abundance association because the supplied resources contain no matching high-confidence STRING interactions, no shared hu.MAP complex, and no STRING enrichment. However, those absences do not prove biological novelty: the individual genes and their functions are established, and the observed association could reflect co-regulation, shared cell composition, tissue sampling, or technical factors. The defensible conclusion is that the specific cross-tissue co-abundance configuration appears under-characterized in these resources, not that it is a newly discovered molecular complex or pathway.

**Hypothesis.** Hypothesis: in autonomic nervous system and lung samples, a shared cellular state involving endoplasmic-reticulum glycan processing and mitochondrial quality control may co-vary with fatty-acid oxidation, RNA modification, and antioxidant defense. MPDU1 could mark the protein-processing arm, ATAD1 and ACADVL the mitochondrial or energetic arm, and METTL1 and PRXL2A stress-adaptation arms. This model is provisional because the module has no globally significant GO or KEGG term, no STRING enrichment, no reported high-confidence STRING links, and no hu.MAP complex.

### Important genes

#### MPDU1

- **Related proteins** (co-abundance neighbors): ACADVL (0.87), METTL1 (0.84), PRXL2A (0.83), ATAD1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannose-P-dolichol utilization defect 1. This gene encodes an endoplasmic reticulum membrane protein that is required for utilization of the mannose donor mannose-P-dolichol in the synthesis of lipid-linked oligosaccharides and glycosylphosphatidylinositols. Mutations in this gene result in congenital disorder of glycosylation type If. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2008].
- **Diseases (Open Targets)**: MPDU1-congenital disorder of glycosylation (0.804); RFT1-congenital disorder of glycosylation (0.562); developmental and epileptic encephalopathy, 36 (0.562); PGM1-congenital disorder of glycosylation (0.562); congenital disorder of glycosylation type I (0.526)
- **Europe PMC papers**: 305
- **Why important**: MPDU1 is the central hub of the co-abundance subgraph, connected to every other module member with the greatest weighted strength. It encodes an endoplasmic-reticulum membrane protein required for mannose-donor utilization in lipid-linked oligosaccharide and glycosylphosphatidylinositol biosynthesis. It is linked to congenital disorders of glycosylation and has substantial literature support. Its lung protein detection and broad tissue profile make it a plausible anchor for interpreting the module, although no GO or KEGG term containing it passed global correction.
- **Conclusion**: Established: MPDU1 is the network hub and has a defined role in endoplasmic-reticulum glycan and glycosylphosphatidylinositol biosynthesis, with disease relevance. Hypothesis: its centrality may reflect a shared protein-processing state rather than direct physical coupling to the other module proteins.

#### ACADVL

- **Related proteins** (co-abundance neighbors): MPDU1 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA dehydrogenase very long chain. The protein encoded by this gene is targeted to the inner mitochondrial membrane where it catalyzes the first step of the mitochondrial fatty acid beta-oxidation pathway. This acyl-Coenzyme A dehydrogenase is specific to long-chain and very-long-chain fatty acids. A deficiency in this gene product reduces myocardial fatty acid beta-oxidation and is associated with cardiomyopathy. Alternative splic…
- **Diseases (Open Targets)**: very long chain acyl-CoA dehydrogenase deficiency (0.865); hereditary disease (0.531); long chain acyl-CoA dehydrogenase deficiency (0.506); rhabdomyolysis (0.464); Acute rhabdomyolysis (0.436)
- **Europe PMC papers**: 3504
- **Why important**: ACADVL contributes the mitochondrial energy-metabolism dimension of the module and is connected directly to MPDU1. It catalyzes the first step of long-chain and very-long-chain fatty-acid beta-oxidation, and deficiency is associated with cardiomyopathy, rhabdomyolysis, and related disease annotations. It has the largest literature volume among the module genes and is detected in lung by HPA.
- **Conclusion**: Established: ACADVL is a mitochondrial fatty-acid oxidation enzyme with strong disease and literature support. Hypothesis: its co-abundance with MPDU1 may indicate coordinated energetic and protein-processing demands, but the module does not establish such regulation.

#### METTL1

- **Related proteins** (co-abundance neighbors): MPDU1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methyltransferase 1, tRNA methylguanosine. This gene is similar in sequence to the S. cerevisiae YDL201w gene. The gene product contains a conserved S-adenosylmethionine-binding motif and is inactivated by phosphorylation. Alternative splice variants encoding different protein isoforms have been described for this gene. A pseudogene has been identified on chromosome X. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.393); neoplasm (0.116); Abnormality of neuronal migration (0.111); cancer (0.109); hepatocellular carcinoma (0.108)
- **Europe PMC papers**: 3987
- **Why important**: METTL1 connects directly to the hub MPDU1 and contributes a distinct RNA-maintenance function through tRNA guanine methylation and tRNA stabilization. It has extensive literature support and disease-area associations involving neurodegeneration, neuronal migration, and cancer. HPA places it in the nucleoplasm and detects its protein in lung.
- **Conclusion**: Established: METTL1 is an RNA-modifying enzyme with established tRNA-related functions and disease associations. Hypothesis: its presence may reflect a translational or stress-response component of the shared module, but no supplied enrichment or interaction evidence connects it mechanistically to MPDU1.

#### ATAD1

- **Related proteins** (co-abundance neighbors): MPDU1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoli rim; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase family AAA domain containing 1. Predicted to enable ATP binding activity and transmembrane protein dislocase activity. Involved in extraction of mislocalized protein from mitochondrial outer membrane. Located in mitochondrial outer membrane and peroxisomal membrane. Implicated in hyperekplexia 4. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hyperekplexia 4 (0.637); hereditary hyperekplexia (0.596); neurodegenerative disease (0.503); spondyloepimetaphyseal dysplasia, PAPSS2 type (0.486); placenta praevia (0.215)
- **Europe PMC papers**: 345
- **Why important**: ATAD1 connects directly to MPDU1 and supplies a mitochondrial and membrane-proteostasis interpretation. It enables transmembrane protein dislocase activity and extracts mislocalized proteins from the mitochondrial outer membrane. It is associated with hereditary hyperekplexia and neurodegenerative disease, is detected in lung, and has a distinctive group-enriched spermatid annotation.
- **Conclusion**: Established: ATAD1 participates in mitochondrial membrane-protein quality control and has neurological disease relevance. Hypothesis: it could couple mitochondrial proteostasis to the endoplasmic-reticulum processing signal represented by MPDU1, but this proposed coupling is not supported by STRING or hu.MAP in the supplied data.

#### PRXL2A

- **Related proteins** (co-abundance neighbors): MPDU1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peroxiredoxin like 2A. Enables antioxidant activity. Involved in regulation of osteoclast differentiation. Located in cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: kidney failure (0.323); hypertensive disorder (0.203); sunburn (0.188); Abnormal blistering of the skin (0.109); stomach disorder (0.108)
- **Europe PMC papers**: 140
- **Why important**: PRXL2A connects directly to MPDU1 and is the module member with tissue-enhanced HPA expression, adipose-tissue enrichment, immune-cell enrichment in plasmacytoid dendritic cells, and secretion in other tissues. Its annotation supports antioxidant activity, cellular oxidant detoxification, and regulation of osteoclast differentiation. Although it has the smallest literature volume in the module, its redox and secreted-protein characteristics make it important for interpreting possible tissue or extracellular-state effects.
- **Conclusion**: Established: PRXL2A is associated with antioxidant activity and cellular oxidant detoxification and has distinctive tissue, immune-cell, and secretome annotations. Hypothesis: it may report oxidative or inflammatory state shared by the two tissues, but its secretion and cell-type annotations also make sample composition a competing explanation.

## Module 4

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (15)**: ACLY, MTHFD1, MT-CO2, HNRNPK, HSPA8, TMPO, TMPO, LDHB, PAICS, RAN, FARSB, VARS1, CCT7, CCT8, TECR

### Function

The strongest functional interpretation is coordinated core cellular metabolism supporting nucleotide production, protein folding, RNA and protein handling, and energy or lipid metabolism. The primary evidence is (GO:BP purine-containing compound metabolic process; q_global = 0.0285), a globally corrected enrichment for purine-containing compound metabolic process, represented by ACLY, HSPA8, LDHB, MTHFD1, PAICS, RAN, and TECR. MTHFD1 and PAICS provide direct links to one-carbon and de novo purine biosynthesis, while ACLY, LDHB, and TECR connect the module to acetyl-CoA, redox-linked lactate metabolism, and fatty-acid elongation. RAN, CCT7, CCT8, and HSPA8 support nuclear transport, protein folding, and proteostasis. The STRING tissue enrichments for lymphoblast, lymphocyte, and blood (STRING TISSUES Lymphoblast; within-query FDR = 0.00021) (STRING TISSUES Lymphocyte; within-query FDR = 0.00069) (STRING TISSUES Blood; within-query FDR = 0.0014) are supplementary and suggest that the module may also reflect proliferative or biosynthetically active cells. No additional GO or KEGG term should be treated as globally significant.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly intracellular, with cytosolic, nuclear, nuclear-membrane, mitochondrial, or endoplasmic-reticulum localizations. Most genes have low tissue specificity, while several show cell-type enhancement in diverse populations including erythrocyte progenitors, trophoblast-related cells, spermatogenic cells, hepatocytes, and epithelial cells. HPA reports low immune-cell specificity for nearly all genes and no recurrent enriched blood-cell category, so the module is not specifically established as a blood-cell module. Nevertheless, the STRING lymphoid and blood tissue signals (STRING TISSUES Lymphoblast; within-query FDR = 0.00021) (STRING TISSUES Lymphocyte; within-query FDR = 0.00069) (STRING TISSUES Blood; within-query FDR = 0.0014), together with the broad housekeeping-like biology, mean that shared cellular composition, proliferative state, or general biosynthetic activity could contribute to the apparent conservation between autonomic nervous system and lung. Lung protein detection is widespread among the listed genes, but this does not establish lung-specific function or autonomic-nervous-system specificity.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP purine-containing compound metabolic process | 0.0285 | ACLY, HSPA8, LDHB, MTHFD1, PAICS, RAN, TECR |

### STRING and hu.MAP

STRING supports a connected but heterogeneous set of established relationships. The strongest coherent subnetwork is the CCT7–CCT8 chaperonin pair with links to HSPA8 and RAN; HSPA8 also connects with HNRNPK. A metabolic subnetwork links MTHFD1 with PAICS and ACLY, while FARSB and VARS1 form an aminoacyl-tRNA-synthetase relationship. The STRING evidence therefore supports protein folding, nuclear or RNA-related handling, translation-associated activity, and nucleotide metabolism, but it does not show that every module gene belongs to one physical complex. The hu.MAP evidence is concentrated in CCT7 and CCT8: both occur together in the listed CCT-related complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1), whereas the other module genes are not represented as shared members of those complexes. These observations indicate that some module edges reflect known molecular machinery, while the broader co-abundance pattern likely combines several cellular processes or shared expression states.

**STRING interactions (score >= 0.7)**: 9 of 105 gene pairs: ACLY–MTHFD1 (0.723); CCT7–CCT8 (0.999); CCT7–HSPA8 (0.922); CCT7–RAN (0.726); CCT8–HSPA8 (0.905); CCT8–RAN (0.712); FARSB–VARS1 (0.776); HNRNPK–HSPA8 (0.791); MTHFD1–PAICS (0.9)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Lymphoblast (FDR = 0.00021, 7 genes); TISSUES Lymphocyte (FDR = 0.00069, 8 genes); TISSUES Blood (FDR = 0.0014, 10 genes); TISSUES Sense organ (FDR = 0.009, 7 genes); TISSUES Male reproductive gland (FDR = 0.0193, 10 genes); TISSUES Digestive gland (FDR = 0.0245, 11 genes); TISSUES Liver (FDR = 0.0245, 10 genes); TISSUES Adenocarcinoma cell (FDR = 0.0308, 5 genes); TISSUES Internal male genital organ (FDR = 0.0308, 9 genes); Keyword ATP-binding (FDR = 0.0391, 8 genes); Keyword Nucleotide-binding (FDR = 0.0391, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT8, CCT7; 2/23); huMAP3_06559.1 (CCT8, CCT7; 2/25); huMAP3_09191.1 (CCT8, CCT7; 2/32); huMAP3_10656.1 (CCT8, CCT7; 2/36); huMAP3_14584.1 (CCT8, CCT7; 2/61)

### Novelty

The individual biology is not a new discovery: purine biosynthesis, CCT chaperonin function, HSPA8 chaperoning, RAN-mediated nuclear transport, aminoacyl-tRNA charging, mitochondrial respiration, and lipid metabolism are established functions. Several relationships are also already represented in STRING, and the CCT7–CCT8 relationship is repeatedly represented in hu.MAP (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). The potentially novel aspect is the conserved co-abundance organization of this particular combination across autonomic nervous system and lung. That claim remains provisional because the module contains broadly expressed housekeeping and biosynthetic genes, and because absence from a database would not prove novelty. A defensible conclusion is that this is a potentially useful cross-tissue co-abundance pattern, not evidence by itself for a newly discovered biochemical pathway or tissue-specific mechanism.

**Hypothesis.** Hypothesis: the conserved module reflects a shared intracellular state in which cells maintain purine and related nucleotide supply while coordinating translation, chaperone capacity, nuclear transport, mitochondrial energy handling, and membrane-lipid synthesis. MTHFD1 and PAICS could support purine precursor flux, ACLY and LDHB could couple carbon and redox metabolism to biosynthetic demand, and the CCT7–CCT8–HSPA8–RAN network could support folding and trafficking of proteins needed during that state. The lymphoid and blood-associated STRING signals and the HPA cell-type patterns raise the alternative hypothesis that shared cellular composition or proliferative biosynthetic activity, rather than a specialized autonomic-lung program, drives part of the signal. This should be tested with cell-composition adjustment, independent tissue cohorts, and perturbation of nucleotide or proteostasis pathways.

### Important genes

#### RAN

- **Related proteins** (co-abundance neighbors): CCT8 (0.87), VARS1 (0.86), LDHB (0.84), ACLY (0.83), TMPO (0.82); STRING partners: CCT7 (0.726), CCT8 (0.712)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAN, member RAS oncogene family. RAN (ras-related nuclear protein) is a small GTP binding protein belonging to the RAS superfamily that is essential for the translocation of RNA and proteins through the nuclear pore complex. The RAN protein is also involved in control of DNA synthesis and cell cycle progression. Nuclear localization of RAN requires the presence of regulator of chromosome condensation 1 (RCC1). Mutations in RAN di…
- **Diseases (Open Targets)**: HIV infectious disease (0.565); Orthomyxoviridae infectious disease (0.376); pemphigus foliaceus (0.298); neurodegenerative disease (0.270); Genu valgum (0.136)
- **Europe PMC papers**: 133080
- **Why important**: RAN is the most central connector in the module subgraph and links the CCT, metabolic, and membrane-associated portions of the pattern. Its established functions include nuclear import and export, ribosomal subunit export, DNA synthesis, and cell-cycle control. It participates in the primary purine-related term (GO:BP purine-containing compound metabolic process; q_global = 0.0285) and in many supplementary STRING tissue terms (STRING TISSUES Lymphoblast; within-query FDR = 0.00021) (STRING TISSUES Lymphocyte; within-query FDR = 0.00069) (STRING TISSUES Blood; within-query FDR = 0.0014), (5 supplementary STRING terms; within-query FDR 0.0193–0.0308), and (STRING Keyword Nucleotide-binding; within-query FDR = 0.0391). Its large literature base and broad disease associations make it a strong integrator, although its broad functions also make it vulnerable to interpretation as a generic cellular-state marker.
- **Conclusion**: Established evidence supports RAN as a central nuclear-transport and cell-cycle-associated component connected to the module's metabolic and chaperone signals. Hypothesis: RAN may couple increased biosynthetic demand with nuclear trafficking and proliferation-related activity in the shared tissue state; the module alone does not establish a tissue-specific role for RAN.

#### CCT8

- **Related proteins** (co-abundance neighbors): VARS1 (0.88), RAN (0.87), HSPA8 (0.87), MTHFD1 (0.84); STRING partners: CCT7 (0.999), HSPA8 (0.905), RAN (0.712)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is highly connected within the module and is paired with CCT7 in every listed hu.MAP complex (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). STRING also supports relationships with CCT7, HSPA8, and RAN. Its established role is as a subunit of the CCT chaperonin, which folds newly synthesized proteins and supports protein stabilization. It is represented in nearly all supplementary STRING enrichment categories and has lung protein detection, making it a strong marker of the module's proteostasis component.
- **Conclusion**: Established evidence identifies CCT8 as part of known CCT chaperonin machinery and as a bridge to HSPA8 and RAN. Hypothesis: CCT8 may report or help sustain elevated protein-folding demand in the conserved module, but its broad expression argues against treating it as an autonomic-lung-specific effector.

#### MTHFD1

- **Related proteins** (co-abundance neighbors): HNRNPK (0.86), CCT8 (0.84), CCT7 (0.82); STRING partners: ACLY (0.723), PAICS (0.9)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methylenetetrahydrofolate dehydrogenase, cyclohydrolase and formyltetrahydrofolate synthetase 1. This gene encodes a protein that possesses three distinct enzymatic activities, 5,10-methylenetetrahydrofolate dehydrogenase, 5,10-methenyltetrahydrofolate cyclohydrolase and 10-formyltetrahydrofolate synthetase. Each of these activities catalyzes one of three sequential reactions in the interconversion of 1-carbon derivatives of tetrahydrofolate, which are substrates for methionine, thymidylate, …
- **Diseases (Open Targets)**: combined immunodeficiency and megaloblastic anemia with or without hyperhomocysteinemia (0.773); severe combined immunodeficiency (0.473); neural tube defects, folate-sensitive (0.414); isolated spina bifida (0.376); atrial fibrillation (0.332)
- **Europe PMC papers**: 1939
- **Why important**: MTHFD1 connects the CCT and RNA-associated side of the network to the metabolic core through STRING links with ACLY and PAICS. It is present in (GO:BP purine-containing compound metabolic process; q_global = 0.0285) and in several lymphoid, blood, liver, and nucleotide-related supplementary terms (STRING TISSUES Lymphoblast; within-query FDR = 0.00021) (STRING TISSUES Lymphocyte; within-query FDR = 0.00069) (STRING TISSUES Blood; within-query FDR = 0.0014), (STRING TISSUES Digestive gland; within-query FDR = 0.0245), (STRING TISSUES Liver; within-query FDR = 0.0245), and (STRING Keyword ATP-binding; within-query FDR = 0.0391) (STRING Keyword Nucleotide-binding; within-query FDR = 0.0391). Its established multifunctional folate-dependent activities supply one-carbon units relevant to methionine, thymidylate, and de novo purine synthesis. It also has a substantial disease literature involving folate-sensitive and immune-developmental disorders.
- **Conclusion**: Established evidence supports MTHFD1 as a plausible metabolic anchor for the globally supported purine-related function. Hypothesis: variation in MTHFD1 activity could help coordinate nucleotide supply with translation and cell proliferation in the shared module, but co-abundance does not demonstrate altered folate flux.

#### PAICS

- **Related proteins** (co-abundance neighbors): CCT7 (0.82); STRING partners: MTHFD1 (0.9)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoribosylaminoimidazole carboxylase and phosphoribosylaminoimidazolesuccinocarboxamide synthase. This gene encodes a bifunctional enzyme containing phosphoribosylaminoimidazole carboxylase activity in its N-terminal region and phosphoribosylaminoimidazole succinocarboxamide synthetase in its C-terminal region. It catalyzes steps 6 and 7 of purine biosynthesis. The gene is closely linked and divergently transcribed with a locus that encodes an enzyme in the same pathway, and transcription of t…
- **Diseases (Open Targets)**: PAICS deficiency (0.606); Polyhydramnios (0.370); acute myeloid leukemia (0.165); neoplasm (0.107); non-small cell lung carcinoma (0.100)
- **Europe PMC papers**: 960
- **Why important**: PAICS is a bifunctional enzyme that catalyzes consecutive steps in de novo purine biosynthesis and is directly represented in (GO:BP purine-containing compound metabolic process; q_global = 0.0285). Its STRING relationship with MTHFD1 is strong, and it appears across many supplementary tissue and nucleotide-binding terms (5 supplementary STRING terms; within-query FDR 0.00021–0.0193) and (4 supplementary STRING terms; within-query FDR 0.0308–0.0391). Its HPA cell-type enhancements include erythrocyte progenitors and several epithelial or trophoblast-related populations, consistent with biosynthetic demand in proliferating cells. It also has disease associations involving PAICS deficiency and malignancy.
- **Conclusion**: Established evidence makes PAICS one of the clearest pathway-specific members of the module, supporting genuine purine-biosynthetic content rather than a purely generic housekeeping interpretation. Hypothesis: PAICS may be a rate-relevant contributor to nucleotide demand in the shared cellular state, but the data do not establish pathway activation or oncogenic function in either tissue.

#### HSPA8

- **Related proteins** (co-abundance neighbors): CCT8 (0.87), FARSB (0.85), VARS1 (0.84); STRING partners: CCT7 (0.922), CCT8 (0.905), HNRNPK (0.791)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Flagellar centriole, Annulus; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 8. This gene encodes a member of the heat shock protein 70 family, which contains both heat-inducible and constitutively expressed members. This protein belongs to the latter group, which are also referred to as heat-shock cognate proteins. It functions as a chaperone, and binds to nascent polypeptides to facilitate correct folding. It also functions as an ATPase in the disassembly of clathrin-coated…
- **Diseases (Open Targets)**: dengue disease (0.505); systemic lupus erythematosus (0.375); smoking initiation (0.199); Lennox-Gastaut syndrome (0.118); neoplasm (0.105)
- **Europe PMC papers**: 6937
- **Why important**: HSPA8 links CCT7 and CCT8 to the broader module and connects with HNRNPK in STRING. It is a constitutively expressed HSP seventy-family chaperone involved in folding nascent proteins, responses to unfolded proteins, RNA processing, and vesicle disassembly. It occurs in (GO:BP purine-containing compound metabolic process; q_global = 0.0285) and in most supplementary STRING categories (7 supplementary STRING terms; within-query FDR 0.00021–0.0245) and (STRING TISSUES Internal male genital organ; within-query FDR = 0.0308) (STRING Keyword ATP-binding; within-query FDR = 0.0391) (STRING Keyword Nucleotide-binding; within-query FDR = 0.0391), and it has a substantial literature base and broad disease associations.
- **Conclusion**: Established evidence supports HSPA8 as a proteostasis and trafficking component that is physically or functionally connected to the CCT machinery. Hypothesis: HSPA8 may buffer increased protein-folding and transport demand accompanying nucleotide and metabolic activity, but its constitutive expression makes it a poor standalone indicator of a specialized tissue mechanism.

#### ACLY

- **Related proteins** (co-abundance neighbors): RAN (0.83), LDHB (0.81); STRING partners: MTHFD1 (0.723)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP citrate lyase. ATP citrate lyase is the primary enzyme responsible for the synthesis of cytosolic acetyl-CoA in many tissues. The enzyme is a tetramer (relative molecular weight approximately 440,000) of apparently identical subunits. It catalyzes the formation of acetyl-CoA and oxaloacetate from citrate and CoA with a concomitant hydrolysis of ATP to ADP and phosphate. The product, acetyl-CoA, serves several im…
- **Diseases (Open Targets)**: familial hypercholesterolemia (0.532); Hypercholesterolemia (0.532); atherosclerosis (0.470); inherited lipid metabolism disorder (0.467); cardiovascular disorder (0.449)
- **Europe PMC papers**: 7957
- **Why important**: ACLY is part of (GO:BP purine-containing compound metabolic process; q_global = 0.0285), links to MTHFD1 in STRING, and connects in the module subgraph with RAN and LDHB. Its established function is production of cytosolic acetyl-CoA from citrate, supporting fatty-acid and cholesterol synthesis. Its disease associations include hypercholesterolemia and atherosclerosis, and its presence in nucleotide-related enrichment is compatible with broad carbon allocation toward biosynthesis rather than with purine metabolism alone.
- **Conclusion**: Established evidence supports ACLY as a carbon-allocation enzyme that may connect energy metabolism with biosynthetic processes in the module. Hypothesis: ACLY could help supply acetyl-CoA for membrane or lipid production during the shared cellular state, but the module does not demonstrate increased lipogenesis or a causal ACLY-dependent mechanism.

## Module 5

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (6)**: ACSL3, AIFM1, EMC1, NUP210, RAB18, SLC25A12

### Function

The module does not have a GO or KEGG term passing global correction, so no canonical pathway or biological process can be assigned from primary enrichment evidence. Its gene annotations instead point to coordinated organelle and membrane homeostasis: ACSL3 supports long-chain fatty-acyl-CoA production and lipid metabolism; RAB18 supports intracellular membrane trafficking, lipid-droplet organization and sterol homeostasis; EMC1 supports insertion of membrane proteins into the endoplasmic reticulum; SLC25A12 supports mitochondrial aspartate–glutamate exchange and the malate–aspartate shuttle; AIFM1 supports mitochondrial respiratory-chain assembly and apoptosis; and NUP210 is a nuclear-pore component involved in nucleocytoplasmic transport. The co-abundance structure therefore suggests linked lipid, endoplasmic-reticulum, mitochondrial and nuclear-envelope functions, but this is an annotation-based interpretation rather than a globally enriched pathway result.

**Cell composition.** This is not a plasma-protein or secreted-protein module: none of the genes is annotated as secreted, and all are detected in lung by HPA. The module also does not show a blood-cell-enriched profile; every member has low immune-cell specificity. Its composition is heterogeneous: some genes have tissue-enhanced expression, while others have low tissue specificity, and all show cell-type enhancement across distinct cell populations. The enrichment of NUP210 in bone marrow and lymphoid tissue and its association with progenitor and B-cell populations may reflect cellular composition in some samples, but the overall HPA pattern does not support a simple blood-contamination explanation. The shared signal may instead reflect broadly distributed organelle functions or a recurring combination of cell states present in autonomic nervous system and lung.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no high-confidence interaction evidence among the module genes and no supplementary STRING functional enrichment. hu.MAP provides the only supplied complex-level evidence: (hu.MAP huMAP3_06885.1) places SLC25A12 and RAB18 in the same partial complex, alongside SLC2A1 and NDUFA11. This supports a known complex-level relationship involving two module members, but it does not establish direct physical interaction between every module gene or explain the entire co-abundance pattern. The lack of STRING links means that most of the observed network structure is not represented by the supplied high-confidence interaction database.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06885.1 (SLC25A12, RAB18; 2/4)

### Novelty

The shared co-abundance configuration may be a novel observation, because the module connects genes from lipid metabolism, membrane insertion, vesicle trafficking, mitochondrial function and nuclear transport without corresponding high-confidence STRING interactions or broad pathway enrichment. However, it cannot be called a new biological mechanism solely because STRING lacks interactions: database incompleteness, context dependence, indirect regulation and co-expression effects remain possible. The hu.MAP evidence (hu.MAP huMAP3_06885.1) also shows that part of the relationship is already represented in a known complex. The defensible conclusion is that the cross-tissue co-abundance pattern is potentially novel and worthy of validation, while the individual gene functions and at least part of the complex context are established.

**Hypothesis.** Hypothesis: in autonomic nervous system and lung samples, the module reflects a coordinated organelle-stress or membrane-remodeling state in which ACSL3 supplies activated fatty acids, RAB18 regulates lipid and vesicle trafficking, EMC1 maintains insertion of membrane proteins into the endoplasmic reticulum, and SLC25A12 links mitochondrial metabolite exchange to cellular energy and redox handling. AIFM1 could connect this state to mitochondrial respiratory competence and apoptosis susceptibility, while NUP210 could couple it to nuclear-envelope and nucleocytoplasmic transport changes. This model predicts coordinated changes in lipid handling, endoplasmic-reticulum membrane maintenance, mitochondrial metabolism and cell survival, but the supplied data do not establish directionality, causality or a shared physical complex.

### Important genes

#### ACSL3

- **Related proteins** (co-abundance neighbors): NUP210 (0.83), RAB18 (0.83), EMC1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 3. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme is highly expressed…
- **Diseases (Open Targets)**: prostate adenocarcinoma (0.370); acute myeloid leukemia (0.313); neurodegenerative disease (0.300); ovarian dysfunction (0.253); Abnormality of the skeletal system (0.215)
- **Europe PMC papers**: 2930
- **Why important**: ACSL3 has the strongest central position in the supplied co-abundance graph and connects the lipid-metabolism component to EMC1, RAB18 and NUP210. Its established annotation as a long-chain fatty-acyl-CoA ligase links the module to fatty-acid metabolism, lipid biosynthesis and fatty-acid degradation. It is also the most extensively studied member by the supplied literature volume and has disease associations spanning cancer, neurodegeneration, ovarian dysfunction and skeletal abnormality.
- **Conclusion**: Established: ACSL3 is a plausible metabolic anchor for the module, supported by its network position and fatty-acyl-CoA function. Hypothesis: its co-abundance may couple lipid activation to ER, vesicle and nuclear-envelope remodeling in the shared tissue state; this coupling requires experimental validation.

#### EMC1

- **Related proteins** (co-abundance neighbors): ACSL3 (0.82), AIFM1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ER membrane protein complex subunit 1. This gene encodes a single-pass type I transmembrane protein, which is a subunit of the endoplasmic reticulum membrane protein complex (EMC). Multiple alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2012].
- **Diseases (Open Targets)**: cerebellar atrophy, visual impairment, and psychomotor retardation; (0.769); hereditary disease (0.497); inherited retinal dystrophy (0.487); Global developmental delay (0.411); Cerebellar atrophy (0.410)
- **Europe PMC papers**: 416
- **Why important**: EMC1 connects ACSL3 with AIFM1, thereby occupying a bridge between lipid-associated and mitochondrial-associated portions of the module. Its established function in the endoplasmic-reticulum membrane complex makes it relevant to membrane-protein insertion and ER organization. Its disease associations include cerebellar atrophy, visual impairment, psychomotor retardation, inherited retinal dystrophy and developmental delay.
- **Conclusion**: Established: EMC1 provides a biologically credible ER membrane component and is supported by a defined membrane-insertion function. Hypothesis: EMC1 may mediate coordination between lipid remodeling and mitochondrial stress in this module, but the co-abundance data do not prove that it is a causal bridge.

#### AIFM1

- **Related proteins** (co-abundance neighbors): EMC1 (0.81), SLC25A12 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apoptosis inducing factor mitochondria associated 1. This gene encodes a flavoprotein essential for nuclear disassembly in apoptotic cells, and it is found in the mitochondrial intermembrane space in healthy cells. Induction of apoptosis results in the translocation of this protein to the nucleus where it affects chromosome condensation and fragmentation. In addition, this gene product induces mitochondria to release the apoptogenic proteins cytochr…
- **Diseases (Open Targets)**: severe X-linked mitochondrial encephalomyopathy (0.813); X-linked hereditary sensory and autonomic neuropathy with hearing loss (0.798); Charcot-Marie-Tooth disease X-linked recessive 4 (0.761); spondyloepimetaphyseal dysplasia, Bieganski type (0.747); combined oxidative phosphorylation deficiency (0.615)
- **Europe PMC papers**: 1952
- **Why important**: AIFM1 occupies a bridging position between EMC1 and SLC25A12 and is localized to mitochondria. Its established functions include mitochondrial respiratory-chain assembly, response to ischemia, response to toxic substances and apoptotic processes. It has substantial literature support and disease associations including severe mitochondrial encephalomyopathy, hereditary sensory and autonomic neuropathy and combined oxidative-phosphorylation deficiency.
- **Conclusion**: Established: AIFM1 is a strong mitochondrial and cell-survival marker within the module, with direct relevance to the autonomic nervous system context through its disease associations. Hypothesis: it may report mitochondrial vulnerability or altered apoptosis susceptibility accompanying membrane and lipid remodeling; causality is not demonstrated.

#### RAB18

- **Related proteins** (co-abundance neighbors): ACSL3 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_06885.1
- **Function (MyGene.info)**: RAB18, member RAS oncogene family. The protein encoded by this gene is a member of a family of Ras-related small GTPases that regulate membrane trafficking in organelles and transport vesicles. Knockdown studies is zebrafish suggest that this protein may have a role in eye and brain development. Mutations in this gene are associated with Warburg micro syndrome type 3. Alternatively spliced transcript variants have been found for th…
- **Diseases (Open Targets)**: Warburg micro syndrome (0.815); neurodegenerative disease (0.496); cerebral atherosclerosis (0.275); malunion fracture (0.239); adolescent idiopathic scoliosis (0.229)
- **Europe PMC papers**: 2168
- **Why important**: RAB18 links ACSL3 to the hu.MAP-supported complex context (hu.MAP huMAP3_06885.1) with SLC25A12. Its established small-GTPase function in organelle and vesicle trafficking, together with roles in lipid-droplet organization and sterol homeostasis, makes it a key candidate for connecting lipid metabolism to membrane trafficking. It has substantial literature support and a strong disease association with Warburg micro syndrome.
- **Conclusion**: Established: RAB18 is a mechanistically relevant membrane-trafficking and lipid-organelle regulator, and its participation in (hu.MAP huMAP3_06885.1) is the clearest complex-level support in the module. Hypothesis: RAB18 may coordinate lipid-droplet or vesicle behavior with mitochondrial metabolite handling in the shared tissue state, but direct interaction with the other module members is not established by STRING.

#### SLC25A12

- **Related proteins** (co-abundance neighbors): AIFM1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_06885.1
- **Function (MyGene.info)**: solute carrier family 25 member 12. This gene encodes a calcium-binding mitochondrial carrier protein. The encoded protein localizes to the mitochondria and is involved in the exchange of aspartate for glutamate across the inner mitochondrial membrane. Polymorphisms in this gene may be associated with autism, and mutations in this gene may also be a cause of global cerebral hypomyelination. Alternatively spliced transcript variants …
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 39 (0.799); hereditary disease (0.416); Global developmental delay (0.370); developmental and epileptic encephalopathy, 1 (0.274); X-linked spasticity-intellectual disability-epilepsy syndrome (0.266)
- **Europe PMC papers**: 992
- **Why important**: SLC25A12 connects AIFM1 to the hu.MAP complex context (hu.MAP huMAP3_06885.1) and is enriched in skeletal muscle and tongue, with cell-type enhancement in brain inhibitory neurons, choroid plexus epithelial cells and myonuclei. Its established mitochondrial carrier activity exchanges aspartate and glutamate and contributes to the malate–aspartate shuttle, NAD metabolism and calcium responses. Its disease associations include developmental and epileptic encephalopathy, global developmental delay and X-linked neurodevelopmental syndromes.
- **Conclusion**: Established: SLC25A12 is a strong mitochondrial metabolic candidate and provides a plausible nervous-system-relevant component of the module. Hypothesis: it may couple mitochondrial redox and amino-acid transport to the membrane-remodeling program represented by ACSL3 and RAB18; this remains a testable model rather than an established mechanism.

## Module 6

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (10)**: ADNP, DCPH1, ATRX, CDK5, DHX36, GRWD1, POGZ, RBM34, TBL3, TEX10

### Function

The module is most consistent with a nuclear gene-regulatory and RNA or ribosome-biogenesis program, rather than a tissue-specific signaling pathway. TBL3, GRWD1, TEX10, RBM34, and DHX36 form the supplementary STRING-associated ribosome-biogenesis neighborhood (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 0.0148), while ATRX, POGZ, and ADNP connect the module to chromatin organization and transcriptional regulation through the hu.MAP complexes (hu.MAP huMAP3_11539.1) and (hu.MAP huMAP3_09963.1). The co-abundance graph links these neighborhoods through TBL3, ATRX, POGZ, and ADNP, but the graph is sparse and does not establish one unified physical complex. No GO or KEGG term passed global correction, so the functional interpretation is hypothesis-generating rather than statistically confirmed by global enrichment.

**Cell composition.** The module is composed entirely of intracellular or nuclear proteins, with no secreted genes and uniformly low immune-cell specificity. Most genes have low tissue specificity, arguing against a blood-derived or plasma-protein explanation. HPA single-cell annotations indicate cell-type-enhanced expression for many members, including reproductive, neural, cardiac, stromal, and alveolar cell populations, but these annotations are heterogeneous rather than defining one shared cell type. CDK5 is tissue-enhanced in brain, whereas the remaining genes are broadly distributed by tissue-level annotation. Lung protein detection is present for several members, while autonomic-nervous-system protein evidence is unavailable in the supplied HPA comparison. The shared module may therefore reflect a conserved intracellular program or cell-state mixture rather than contamination by blood or secreted proteins.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known STRING relationship is GRWD1-TBL3, supporting a ribosome-biogenesis or nucleolar association. ADNP-POGZ is also a high-confidence STRING relationship and independently supports a regulatory partnership. The remaining co-abundance edges are not represented by high-confidence STRING links in the supplied evidence, so co-abundance should not be equated with direct physical interaction. hu.MAP provides convergent complex-level support for ATRX, POGZ, and ADNP in (hu.MAP huMAP3_11539.1), and for POGZ and ADNP in (hu.MAP huMAP3_09963.1). These results suggest that part of the module overlaps known chromatin-associated assemblies, while the RNA-processing and ribosome-biogenesis portion is only partly supported by established interaction data. The STRING enrichment (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 0.0148) is supplementary and is not global enrichment evidence.

**STRING interactions (score >= 0.7)**: 2 of 45 gene pairs: ADNP–POGZ (0.716); GRWD1–TBL3 (0.942)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 0.0148, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11539.1 (ATRX, POGZ, ADNP; 3/32); huMAP3_09963.1 (POGZ, ADNP; 2/16)

### Novelty

This module should not be declared a newly discovered molecular complex. Several of its relationships and functional neighborhoods are already represented in STRING and hu.MAP, especially the GRWD1-TBL3 pair, the ADNP-POGZ pair, and the ATRX-POGZ-ADNP complex context. The potentially novel aspect is the cross-tissue co-abundance association connecting chromatin regulators with nucleolar and RNA-processing proteins in autonomic nervous system and lung samples. However, the sparse network, absence of globally significant GO or KEGG enrichment, and incomplete physical-interaction support mean that this association requires replication, control for cell composition, and independent validation before it can be considered a novel biological mechanism. Absence from a reference database alone would not establish novelty.

**Hypothesis.** Hypothesis: the shared module reflects coordinated regulation of nuclear gene expression in a conserved cellular state, in which ATRX, POGZ, and ADNP organize chromatin or transcriptional programs while TBL3, GRWD1, TEX10, RBM34, and DHX36 support nucleolar RNA processing and ribosome production. CDK5 may connect this state to neuronal or cytoskeletal regulation, and DCPH1 may connect it to DNA-damage-responsive chromatin control. The observed co-abundance could arise from coordinated activity within particular lung and autonomic nervous system cell populations rather than direct assembly of all module proteins into one complex.

### Important genes

#### TBL3

- **Related proteins** (co-abundance neighbors): DHX36 (0.88), GRWD1 (0.86), ADNP (0.83), TEX10 (0.80); STRING partners: GRWD1 (0.942)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transducin beta like 3. The protein encoded by this gene has sequence similarity with members of the WD40 repeat-containing protein family. The WD40 group is a large family of proteins, which appear to have a regulatory function. It is believed that the WD40 repeats mediate protein-protein interactions and members of the family are involved in signal transduction, RNA processing, gene regulation, vesicular trafficking, c…
- **Diseases (Open Targets)**: Huntington disease (0.011); pulmonary fibrosis (0.004); infection (0.004); neoplasm (0.004); cancer (0.004)
- **Europe PMC papers**: 283
- **Why important**: TBL3 is the main network connector in the supplied graph, linking the ribosome-biogenesis-associated genes with ADNP and the broader module. It has the strongest STRING support through GRWD1-TBL3 and is annotated to nucleolar localization, rRNA processing, and small-subunit biogenesis. Its WD-repeat architecture is compatible with a protein-interaction scaffold. The literature volume is substantial, and disease-oriented evidence includes pulmonary fibrosis and neurodegenerative disease associations.
- **Conclusion**: Established evidence supports TBL3 as a central nucleolar and ribosome-biogenesis-associated component of the module. It is plausible, but not demonstrated, that TBL3 coordinates the nucleolar neighborhood with the chromatin-regulatory neighborhood.

#### ATRX

- **Related proteins** (co-abundance neighbors): CDK5 (0.85), POGZ (0.85), DCPH1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_11539.1
- **Function (MyGene.info)**: ATRX chromatin remodeler. The protein encoded by this gene contains an ATPase/helicase domain, and thus it belongs to the SWI/SNF family of chromatin remodeling proteins. This protein is found to undergo cell cycle-dependent phosphorylation, which regulates its nuclear matrix and chromatin association, and suggests its involvement in the gene regulation at interphase and chromosomal segregation in mitosis. Mutations in thi…
- **Diseases (Open Targets)**: alpha thalassemia-X-linked intellectual disability syndrome (0.848); intellectual disability-hypotonic facies syndrome, X-linked, 1 (0.786); alpha-thalassemia-myelodysplastic syndrome (0.664); alpha thalassemia-intellectual disability syndrome type 1 (0.606); ATR-X-related syndrome (0.568)
- **Europe PMC papers**: 12307
- **Why important**: ATRX has a prominent network position and connects to POGZ and DCPH1 while also linking to CDK5. It is a chromatin remodeler with established roles in chromatin organization, transcriptional regulation, cell-cycle control, and DNA-damage responses. It is present in hu.MAP complex (hu.MAP huMAP3_11539.1), has lung protein detection, and has extensive literature and strong disease associations involving ATR-X-related syndromes and intellectual disability.
- **Conclusion**: Established evidence supports ATRX as a chromatin-regulatory anchor of the module. Its connection to nucleolar genes is an association in this network and should not yet be interpreted as a direct ATRX-mediated ribosome-biogenesis mechanism.

#### POGZ

- **Related proteins** (co-abundance neighbors): ATRX (0.85), ADNP (0.81); STRING partners: ADNP (0.716)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_11539.1, huMAP3_09963.1
- **Function (MyGene.info)**: pogo transposable element derived with ZNF domain. The protein encoded by this gene appears to be a zinc finger protein containing a transposase domain at the C-terminus. This protein was found to interact with the transcription factor SP1 in a yeast two-hybrid system. Alternatively spliced transcript variants encoding distinct isoforms have been observed. [provided by RefSeq, Aug 2010].
- **Diseases (Open Targets)**: white-sutton syndrome (0.784); Intellectual disability (0.635); autism spectrum disorder (0.572); hereditary disease (0.550); neurodegenerative disease (0.517)
- **Europe PMC papers**: 804
- **Why important**: POGZ connects ATRX and ADNP, is supported by the STRING ADNP-POGZ relationship, and occurs in both hu.MAP complexes (hu.MAP huMAP3_11539.1) and (hu.MAP huMAP3_09963.1). Its annotations include transcriptional regulation, homologous-recombination repair, sister-chromatid cohesion, and kinetochore assembly. It has lung protein detection and well-established associations with White-Sutton syndrome, intellectual disability, and autism spectrum disorder.
- **Conclusion**: Established evidence supports POGZ as a chromatin and genome-maintenance regulator within a known ADNP-associated complex context. Its role as a bridge between the chromatin and RNA-processing neighborhoods is a plausible network hypothesis rather than a demonstrated biochemical function.

#### ADNP

- **Related proteins** (co-abundance neighbors): TBL3 (0.83), POGZ (0.81); STRING partners: POGZ (0.716)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Centrosome; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_11539.1, huMAP3_09963.1
- **Function (MyGene.info)**: activity dependent neuroprotector homeobox. Vasoactive intestinal peptide is a neuroprotective factor that has a stimulatory effect on the growth of some tumor cells and an inhibitory effect on others. This gene encodes a protein that is upregulated by vasoactive intestinal peptide and may be involved in its stimulatory effect on certain tumor cells. The encoded protein contains one homeobox and nine zinc finger domains, suggesting that it …
- **Diseases (Open Targets)**: ADNP-related multiple congenital anomalies - intellectual disability - autism spectrum disorder (0.788); hereditary disease (0.548); Intellectual disability (0.533); neurodegenerative disease (0.494); prostate carcinoma (0.420)
- **Europe PMC papers**: 1699
- **Why important**: ADNP is connected to POGZ and TBL3 and is present in both hu.MAP complexes (hu.MAP huMAP3_11539.1) and (hu.MAP huMAP3_09963.1). It encodes a transcription-related protein with homeobox and zinc-finger features and is annotated to gene-expression regulation and neuron-projection development. It has lung protein detection, extensive literature, and disease associations involving neurodevelopment, intellectual disability, autism spectrum disorder, and neurodegeneration.
- **Conclusion**: Established evidence supports ADNP as a transcriptional and neurodevelopmental regulator participating in known complex contexts. Its co-abundance with TBL3 may indicate coordinated regulation of nuclear and nucleolar programs, but direct functional coupling remains unproven.

#### CDK5

- **Related proteins** (co-abundance neighbors): ATRX (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cyclin dependent kinase 5. This gene encodes a proline-directed serine/threonine kinase that is a member of the cyclin-dependent kinase family of proteins. Unlike other members of the family, the protein encoded by this gene does not directly control cell cycle regulation. Instead the protein, which is predominantly expressed at high levels in mammalian postmitotic central nervous system neurons, functions in diverse proces…
- **Diseases (Open Targets)**: Alzheimer disease (0.680); lissencephaly 7 with cerebellar hypoplasia (0.680); neurodegenerative disease (0.480); Parkinson disease (0.379); autoimmune disorder of central nervous system (0.366)
- **Europe PMC papers**: 12790
- **Why important**: CDK5 is the module's brain-enhanced gene and occupies the connection between ATRX and the rest of the regulatory neighborhood. It is a neuronal kinase associated with synaptic plasticity, neuronal migration, axonogenesis, synapse assembly, and synaptic vesicle exocytosis. It has lung protein detection, extensive literature, and disease associations including Alzheimer disease, Parkinson disease, and lissencephaly.
- **Conclusion**: Established evidence supports CDK5 as a neuronal signaling and cytoskeletal regulator. Its placement beside ATRX suggests a possible link between chromatin state and neuronal or cytoskeletal processes, but the module does not establish that CDK5 drives the shared autonomic nervous system and lung association.

## Module 7

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (22)**: AP1S1, ASH2L, CNPY3, CPSF2, CPSF3, DCAF13, ECI1, FAF1, IDH3A, KIF11, LRWD1, NUP107, NUP214, NUCB1, NUDCD2, PDHB, PHB1, RBM33, MRPL45, SPIN1, XAB2, GTF3C5

### Function

No GO/KEGG term passed global correction, and there are no supplementary STRING enrichment terms. The gene annotations nevertheless suggest a composite cellular-maintenance program rather than a well-defined tissue-specific pathway. One component concerns nuclear RNA metabolism, including pre-mRNA splicing, mRNA three-prime-end processing, RNA export and nucleocytoplasmic transport through XAB2, CPSF2, CPSF3, RBM33, NUP107 and NUP214. Another concerns mitochondrial energy metabolism and protein synthesis through PDHB, IDH3A, ECI1 and MRPL45. Additional members relate to mitotic spindle function, chromatin and transcriptional regulation, vesicle trafficking, protein folding and apoptosis. The sparse network therefore supports a broad housekeeping or cell-state interpretation more strongly than a single specialized biological function.

**Cell composition.** The module is not dominated by plasma or secreted proteins and is not strongly blood-cell enriched. Most genes have low tissue specificity and low immune-cell specificity, while several are detected in lung and have broadly intracellular localizations. NUCB1 is secreted to blood, and CNPY3 and PHB1 have intracellular and membrane secretome annotations, but this is a minority pattern rather than the defining feature. HPA profiles include scattered enrichment in testis, tongue, brain, bone marrow and lymphoid tissue, with cell-type signals involving germ cells, epithelial cells, progenitors and selected immune cells. This breadth, together with widespread lung protein detection, argues against interpreting the module as autonomic-nervous-system-specific or as a simple blood-contamination signature. Shared abundance may instead reflect common cellular composition, general biosynthetic demand or a broadly expressed cell state in the two tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports established relationships for CPSF2 with CPSF3, IDH3A with PDHB, and NUP107 with NUP214. The CPSF2-CPSF3 pair is also represented in the hu.MAP complexes (hu.MAP huMAP3_00102.1), (hu.MAP huMAP3_09096.1) and (hu.MAP huMAP3_11757.1), while the NUP107-NUP214 pair is represented in (hu.MAP huMAP3_12581.1). These findings validate local substructures involving mRNA three-prime-end processing, mitochondrial metabolism and the nuclear pore. The remaining module connections are not supported by high-confidence STRING partners or multi-member hu.MAP complexes in the supplied evidence. Thus, the module is not a single experimentally established protein complex; it is a co-abundance structure containing several known molecular units connected by correlations that may reflect shared expression, cell state or indirect biological coordination.

**STRING interactions (score >= 0.7)**: 3 of 231 gene pairs: CPSF2–CPSF3 (0.999); IDH3A–PDHB (0.856); NUP107–NUP214 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00102.1 (CPSF2, CPSF3; 2/12); huMAP3_09096.1 (CPSF2, CPSF3; 2/15); huMAP3_11757.1 (CPSF2, CPSF3; 2/16); huMAP3_12581.1 (NUP214, NUP107; 2/58)

### Novelty

The exact shared co-abundance module may be a new integrative observation, because the supplied resources do not identify it as one previously established complex or pathway. However, it would be incorrect to call the underlying biology wholly novel: the CPSF, nuclear-pore and mitochondrial relationships are already known from STRING, hu.MAP and gene-function annotations. The evidence therefore supports novelty at the level of the cross-tissue co-abundance arrangement and its combination of molecular processes, not novelty of the individual interactions. Absence of additional STRING or hu.MAP links cannot by itself establish discovery; independent replication, cell-composition adjustment, perturbation experiments and comparison with published co-expression modules would be needed to substantiate a new biological mechanism.

**Hypothesis.** Hypothesis: the shared module reflects a conserved basal cell-maintenance state in which RNA processing and nuclear export are coordinated with mitochondrial energy production and, in some cells, proliferation or stress adaptation. CPSF and XAB2-related RNA maturation, NUP-mediated transport, and mitochondrial PDHB-IDH3A activity could rise together when cells require sustained transcription, transcript processing and energy supply. The observed association may be driven partly by shared cell types or general cellular activity rather than a tissue-specific autonomic nervous system mechanism. This hypothesis should be tested by cell-type-resolved data, covariate adjustment for abundance and composition, and perturbation of the RNA-processing and mitochondrial components.

### Important genes

#### CPSF3

- **Related proteins** (co-abundance neighbors): XAB2 (0.83), CPSF2 (0.82), NUDCD2 (0.81), KIF11 (0.80); STRING partners: CPSF2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_00102.1, huMAP3_09096.1, huMAP3_11757.1
- **Function (MyGene.info)**: cleavage and polyadenylation specific factor 3. This gene encodes a member of the metallo-beta-lactamase family. The encoded protein is a 73kDa subunit of the cleavage and polyadenylation specificity factor and functions as an endonuclease that recognizes the pre-mRNA 3'-cleavage site AAUAAA prior to polyadenylation. It also cleaves after the pre-mRNA sequence ACCCA during histone 3'-end pre-mRNA processing. [provided by RefSeq, Oct 2012].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, hypotonia, nystagmus, and seizures (0.601); neurodegenerative disease (0.527); neurodevelopmental disorder with hypotonia, microcephaly, and seizures (0.416); complex neurodevelopmental disorder (0.370); dengue disease (0.370)
- **Europe PMC papers**: 548
- **Why important**: CPSF3 is a central module node connected to XAB2, CPSF2, NUDCD2 and KIF11. Established annotation identifies it as the endonuclease within the cleavage and polyadenylation specificity factor and as a participant in mRNA three-prime-end and histone mRNA processing. Its direct STRING relationship with CPSF2 and its membership in (hu.MAP huMAP3_00102.1), (hu.MAP huMAP3_09096.1) and (hu.MAP huMAP3_11757.1) provide unusually strong external support for a local RNA-processing unit. It also has substantial literature and disease relevance involving neurodevelopmental and neurodegenerative conditions.
- **Conclusion**: Established evidence supports CPSF3 as a genuine RNA three-prime-end-processing component of the module. The module data do not establish that CPSF3 drives the shared tissue pattern or that altered CPSF3 activity causes it; those are hypotheses requiring functional testing.

#### XAB2

- **Related proteins** (co-abundance neighbors): SPIN1 (0.89), LRWD1 (0.84), CPSF3 (0.83), ASH2L (0.81), RBM33 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: XPA binding protein 2. Involved in mRNA splicing, via spliceosome; transcription, DNA-templated; and transcription-coupled nucleotide-excision repair. Located in nucleoplasm. Part of U2-type catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dengue disease (0.370); neoplasm (0.081); colorectal carcinoma (0.074); neuropathic pain (0.055); gastric cancer (0.043)
- **Europe PMC papers**: 587
- **Why important**: XAB2 is among the most connected genes in the module and links SPIN1, LRWD1, CPSF3, ASH2L and RBM33. Established annotation places it in the catalytic step-two spliceosome and in transcription-coupled nucleotide-excision repair, transcription and RNA processing. Its position provides a plausible bridge between transcript maturation, transcriptional control and genome maintenance. It has a substantial literature and disease-association record, although no direct STRING or hu.MAP relationship is supplied for its module edges.
- **Conclusion**: Established evidence supports XAB2 as an integrative RNA-processing and genome-maintenance candidate. Its bridging position is compatible with coordinated transcript handling, but the co-abundance data alone cannot distinguish direct molecular cooperation from shared cellular demand.

#### NUP214

- **Related proteins** (co-abundance neighbors): RBM33 (0.81); STRING partners: NUP107 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 214. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene is a member of the FG-repeat-containing nucleoporins. The protein encoded by this gene is localized to the cytoplas…
- **Diseases (Open Targets)**: familial acute necrotizing encephalopathy (0.664); Orthomyxoviridae infectious disease (0.543); HIV infectious disease (0.542); viral infectious disease (0.527); Global developmental delay (0.435)
- **Europe PMC papers**: 2712
- **Why important**: NUP214 connects RBM33 to NUP107 and forms the directly supported NUP107-NUP214 pair in STRING and (hu.MAP huMAP3_12581.1). Established annotation places NUP214 at the cytoplasmic face of the nuclear pore, where it participates in RNA export, protein transport and nucleocytoplasmic transport. Its HPA profile also shows tissue and blood-cell enrichment patterns, making it informative for assessing whether the module reflects cell composition. NUP214 has a substantial literature and associations with developmental and infectious disease.
- **Conclusion**: Established evidence supports NUP214 as the nuclear-transport representative of the module and validates a local nuclear-pore substructure. Its abundance could report general transport demand or cell-type composition; the data do not show that it creates the shared module.

#### PDHB

- **Related proteins** (co-abundance neighbors): MRPL45 (0.87), PHB1 (0.80); STRING partners: IDH3A (0.856)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyruvate dehydrogenase E1 subunit beta. The pyruvate dehydrogenase (PDH) complex is a nuclear-encoded mitochondrial multienzyme complex that catalyzes the overall conversion of pyruvate to acetyl-CoA and carbon dioxide, and provides the primary link between glycolysis and the tricarboxylic acid (TCA) cycle. The PDH complex is composed of multiple copies of three enzymatic components: pyruvate dehydrogenase (E1), dihydrolipoamide acetylt…
- **Diseases (Open Targets)**: pyruvate dehydrogenase E1-beta deficiency (0.796); pyruvate decarboxylase deficiency (0.672); pyruvate dehydrogenase phosphatase deficiency (0.421); neurodegenerative disease (0.392); hereditary disease (0.190)
- **Europe PMC papers**: 3002
- **Why important**: PDHB links MRPL45 with PHB1 and has a high-confidence STRING relationship with IDH3A. Established annotation identifies it as the beta subunit of pyruvate dehydrogenase, connecting glycolytic pyruvate conversion to acetyl-CoA production and the tricarboxylic acid cycle. It has extensive literature and a strong disease-association record involving pyruvate-dehydrogenase deficiency and neurodegeneration. Its mitochondrial localization gives the module a clear metabolic axis.
- **Conclusion**: Established evidence supports PDHB as a mitochondrial energy-metabolism component and as part of a known IDH3A-linked substructure. A coordinated metabolic contribution is plausible, but the module does not demonstrate altered flux through pyruvate dehydrogenase or a causal metabolic mechanism.

#### IDH3A

- **Related proteins** (co-abundance neighbors): MRPL45 (0.81), NUCB1 (0.81); STRING partners: PDHB (0.856)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: isocitrate dehydrogenase (NAD(+)) 3 catalytic subunit alpha. Isocitrate dehydrogenases catalyze the oxidative decarboxylation of isocitrate to 2-oxoglutarate. These enzymes belong to two distinct subclasses, one of which utilizes NAD(+) as the electron acceptor and the other NADP(+). Five isocitrate dehydrogenases have been reported: three NAD(+)-dependent isocitrate dehydrogenases, which localize to the mitochondrial matrix, and two NADP(+)-dependent isoci…
- **Diseases (Open Targets)**: retinitis pigmentosa 90 (0.791); retinitis pigmentosa (0.467); neurodegenerative disease (0.437); inherited retinal dystrophy (0.381); colorectal carcinoma (0.182)
- **Europe PMC papers**: 1497
- **Why important**: IDH3A connects PDHB with NUCB1 and participates in the directly supported mitochondrial pair with PDHB. Established annotation identifies it as the catalytic alpha subunit of the NAD-dependent mitochondrial isocitrate dehydrogenase and assigns it to carbohydrate metabolism and the tricarboxylic acid cycle. Its HPA profile includes an immune-cell signal involving plasmacytoid dendritic cells, which is relevant when considering cell composition. It has substantial literature and disease associations involving retinal and neurodegenerative disorders.
- **Conclusion**: Established evidence supports IDH3A as a mitochondrial tricarboxylic-acid-cycle representative and as a known metabolic partner of PDHB in this module. Its association with the shared module may indicate coordinated energy metabolism, but it does not prove a tissue-specific metabolic adaptation or causal disease process.

## Module 8

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (16)**: AP3D1, ATG9A, CHORDC1, DDX56, DNAJB1, ENY2, GPATCH8, KIF3B, METAP2, MAPRE2, MMTAG2, NSFL1C, PHF6, POLR2D, SEH1L, WDR26

### Function

The module is best interpreted as a heterogeneous intracellular maintenance and trafficking program rather than a single confidently enriched pathway. Its genes span nuclear transport and transcriptional regulation, RNA processing, protein folding and stress response, microtubule organization, vesicle and lysosome trafficking, autophagy, and translational protein processing. The strongest structural signal is a set of connected pairs and small local neighborhoods, including WDR26 with SEH1L, POLR2D, ATG9A, and DNAJB1; METAP2 with NSFL1C, AP3D1, and CHORDC1; and MAPRE2 with MMTAG2, DDX56, and GPATCH8. No GO or KEGG term passed global correction, and there was no STRING functional enrichment. Therefore, these annotations support a broad cellular-proteostasis, transport, and gene-expression interpretation, but do not establish a specific pathway as significantly enriched.

**Cell composition.** The module does not resemble a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It also does not show blood-cell enrichment, because every gene has low immune-cell specificity and no enriched blood-cell category is reported. Most genes have low tissue specificity, while a minority show tissue enhancement in brain, skeletal muscle, or testis. Cell-type-enhanced annotations are widespread and heterogeneous, including esophageal apical cells, oocytes, myonuclei, late spermatids, erythrocyte progenitors, neural cells, and other cell types. This argues against a simple blood-contamination explanation, but the shared module could still reflect common intracellular programs or shared cellular composition across the two tissues. Lung protein detection is reported for many genes, whereas autonomic-nervous-system protein detection has no matching HPA tissue, so the tissue-level protein evidence is asymmetric.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the possible within-module gene pairs, and no STRING functional enrichment was reported. No hu.MAP complex contains at least two module members. Thus, the co-abundance relationships are not recapitulated by the supplied high-confidence physical-interaction or curated-complex resources. This does not refute coordinated regulation: co-abundance can arise from shared cell states, transcriptional programs, organelle demand, or indirect cellular coupling rather than direct physical binding. The module contains biologically plausible functional links, such as ATG9A in autophagy, AP3D1 in vesicle and lysosome trafficking, DNAJB1 in chaperone activity, and POLR2D and ENY2 in transcription and RNA export, but these links remain annotation-based rather than established as a shared molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 120 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a new co-abundance observation, but it cannot be claimed as a newly discovered biological pathway. Its lack of STRING and hu.MAP support indicates that this exact grouping is not represented in the supplied high-confidence interaction or complex evidence, yet absence from those resources alone does not prove novelty. The genes have established individual functions and substantial prior literature, while the cross-tissue co-abundance organization and its relevance to autonomic nervous system and lung biology appear less established from the supplied evidence. The appropriate conclusion is that the module-level association is potentially novel and hypothesis-generating, requiring replication, cell-composition control, and independent molecular validation.

**Hypothesis.** Hypothesis: the shared module reflects coordinated cellular maintenance under variable proteostatic, trafficking, and cytoskeletal demands. WDR26 may organize a local regulatory neighborhood involving nuclear-pore-associated SEH1L, transcription-related POLR2D, autophagy-related ATG9A, and chaperone-associated DNAJB1, while METAP2-linked and MAPRE2-linked neighborhoods connect protein maturation, vesicle handling, microtubule organization, and RNA processing. In autonomic nervous system and lung samples, a common cellular state or shared cell-type mixture could therefore produce coordinated abundance of these otherwise diverse genes. This mechanism is provisional: the lack of globally significant GO or KEGG enrichment, STRING interactions, and hu.MAP complexes means the hypothesis is not established by the current module alone.

### Important genes

#### WDR26

- **Related proteins** (co-abundance neighbors): SEH1L (0.89), POLR2D (0.87), ATG9A (0.85), DNAJB1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 26. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: Skraban-Deardorff syndrome (0.798); neurodegenerative disease (0.539); hereditary disease (0.529); Intellectual disability (0.501); gastritis (0.207)
- **Europe PMC papers**: 416
- **Why important**: WDR26 is the most connected node in the supplied module and links four neighborhoods involving SEH1L, POLR2D, ATG9A, and DNAJB1. Its WD-repeat architecture is compatible with multiprotein-complex organization, and its supplied annotation includes proteasome-mediated ubiquitin-dependent protein catabolism. It also has a disease association with Skraban-Deardorff syndrome and a substantial literature base.
- **Conclusion**: Established evidence supports WDR26 as a network-centered scaffold candidate with links to protein turnover and multiple intracellular processes. It is a plausible module anchor, but the co-abundance network does not demonstrate direct binding or prove that WDR26 regulates the other module members.

#### ATG9A

- **Related proteins** (co-abundance neighbors): WDR26 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: autophagy related 9A. Acts upstream of or within autophagosome assembly. Located in endosome; phagophore assembly site; and trans-Golgi network. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); lysosomal storage disease (0.370); cancer (0.094); neoplasm (0.091); triple-negative breast carcinoma (0.076)
- **Europe PMC papers**: 2152
- **Why important**: ATG9A is the module member most directly associated with autophagy and membrane remodeling in the supplied annotations. It is connected to WDR26, is located in vesicles, and has tissue enhancement in skeletal muscle with cell-type enhancement across several neural and glial populations. It also has the largest reported literature volume among the listed genes and disease associations involving neurodegenerative and lysosomal disease.
- **Conclusion**: Established evidence supports ATG9A as a core autophagosome and membrane-trafficking factor with relevance to neural and muscle biology. Its position as a peripheral neighbor of WDR26 makes it informative for the module hypothesis, but does not establish that autophagy is the defining function of the entire module.

#### METAP2

- **Related proteins** (co-abundance neighbors): NSFL1C (0.86), AP3D1 (0.83), CHORDC1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionyl aminopeptidase 2. The protein encoded by this gene is a member of the methionyl aminopeptidase family. The encoded protein functions both by protecting the alpha subunit of eukaryotic initiation factor 2 from inhibitory phosphorylation and by removing the amino-terminal methionine residue from nascent proteins. Increased expression of this gene is associated with various forms of cancer, and the anti-cancer drugs f…
- **Diseases (Open Targets)**: neurodegenerative disease (0.521); autoimmune disorder of central nervous system (0.316); obesity disorder (0.305); Prader-Willi syndrome (0.279); Polyphagia (0.259)
- **Europe PMC papers**: 828
- **Why important**: METAP2 is one of the more connected nodes and links NSFL1C, AP3D1, and CHORDC1. Its established functions include removal of the amino-terminal methionine from nascent proteins, protection of the translation-initiation factor subunit from inhibitory phosphorylation, proteolysis, and protein processing. It is detected in lung and has a substantial literature base, including links to cancer and other disease areas.
- **Conclusion**: Established evidence supports METAP2 as a protein maturation and translation-associated factor that could connect proteostasis with trafficking-related partners. Its network position makes it a strong representative of the module's protein-processing aspect, while the present data do not show that METAP2 drives the shared tissue association.

#### DNAJB1

- **Related proteins** (co-abundance neighbors): WDR26 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DnaJ heat shock protein family (Hsp40) member B1. This gene encodes a member of the DnaJ or Hsp40 (heat shock protein 40 kD) family of proteins. DNAJ family members are characterized by a highly conserved amino acid stretch called the 'J-domain' and function as one of the two major classes of molecular chaperones involved in a wide range of cellular events, such as protein folding and oligomeric protein complex assembly. The encoded protein is a …
- **Diseases (Open Targets)**: fibrolamellar hepatocellular carcinoma (0.377); hepatocellular adenoma (0.370); bile duct adenocarcinoma (0.370); hepatocellular carcinoma (0.290); hepatoblastoma (0.281)
- **Europe PMC papers**: 2924
- **Why important**: DNAJB1 is directly connected to the central WDR26 node and is a molecular chaperone that stimulates Hsp70 activity, supports protein folding, and responds to unfolded-protein and heat stress. It is detected in lung, has several cell-type-enhanced annotations, disease associations involving liver tumors, and a large literature base.
- **Conclusion**: Established evidence supports DNAJB1 as a proteostasis and stress-response component. Its direct module connection to WDR26 makes it relevant to a possible protein-quality-control interpretation, but the module does not establish an unfolded-protein response or a disease-specific stress state.

#### MAPRE2

- **Related proteins** (co-abundance neighbors): MMTAG2 (0.87), DDX56 (0.83), GPATCH8 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: microtubule associated protein RP/EB family member 2. The protein encoded by this gene shares significant homology to the adenomatous polyposis coli (APC) protein-binding EB1 gene family. This protein is a microtubule-associated protein that is necessary for spindle symmetry during mitosis. It is thought to play a role in the tumorigenesis of colorectal cancers and the proliferative control of normal cells. Alternative splicing of this gene results i…
- **Diseases (Open Targets)**: multiple benign circumferential skin creases on limbs (0.746); skin creases, congenital symmetric circumferential, 2 (0.697); neurodegenerative disease (0.464); Brugada syndrome (0.388); developmental disability (0.340)
- **Europe PMC papers**: 475
- **Why important**: MAPRE2 is a connected internal node linking MMTAG2, DDX56, and GPATCH8. Its supplied functions include microtubule-end and spindle regulation, microtubule localization, and focal-adhesion-related processes. It is tissue-enhanced in brain and cell-type-enhanced in myonuclei, NK cells, and retinal bipolar cells, with reported associations involving developmental and neurodegenerative phenotypes.
- **Conclusion**: Established evidence supports MAPRE2 as a cytoskeletal and cell-division-related factor that broadens the module beyond proteostasis. Its position suggests a possible interface between cytoskeletal organization and RNA or nuclear processes, but that interface remains a hypothesis rather than a demonstrated physical complex.

## Module 9

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (16)**: APEX1, BRIX1, CBX5, HNRNPH1, HNRNPL, PKM, LDHA, MAT2A, MTFP1, PSMC2, PSMD13, SEC16A, YARS1, CCT3, EFTUD2, WDR12

### Function

No GO/KEGG term passed global correction, so the module does not have a formally established enriched pathway under the specified criterion. Its internal structure nevertheless suggests a broad cellular maintenance program rather than a tissue-specific pathway. The genes span translation and aminoacylation through YARS1, glycolytic and lactate metabolism through PKM and LDHA, DNA repair through APEX1, RNA processing through HNRNPH1, HNRNPL and EFTUD2, ribosome biogenesis through BRIX1 and WDR12, protein folding through CCT3, mitochondrial dynamics through MTFP1, vesicle export through SEC16A, chromatin regulation through CBX5, and proteasomal degradation through PSMC2 and PSMD13. The supplementary STRING terms (STRING Keyword Ubl conjugation; within-query FDR = 0.0394) and (STRING Keyword Isopeptide bond; within-query FDR = 0.0408) are consistent with ubiquitin-related protein handling, but they are not global GO/KEGG evidence. Overall, the module most plausibly represents coordinated proteostasis, biosynthetic activity, RNA and DNA maintenance, and intermediary metabolism.

**Cell composition.** The module is not dominated by plasma or secreted proteins: HPA reports no secreted genes. It is also not blood-cell enriched, because every gene has low immune-cell specificity and no enriched blood-cell category is reported. Most genes have low tissue specificity, and the tissue-enhanced signals are scattered across skeletal muscle, tongue, pancreas and choroid plexus rather than concentrated in a coherent autonomic or pulmonary identity. Many proteins are cytosolic or nuclear housekeeping-type factors involved in translation, RNA processing, DNA repair, proteostasis, chromatin, ribosome production and metabolism. This makes a shared abundance program caused by broadly distributed cellular activity more plausible than a specialized autonomic-nervous-system or lung lineage signature. The cell-type-enhanced annotations are heterogeneous, including trophoblast, glial, epithelial, muscle, adipocyte and other cell types, so they do not support a single shared cell type. Lung protein detection is broadly present for most genes, while the autonomic nervous system has no matching HPA tissue measurement; therefore the cross-tissue interpretation should not be treated as direct protein-level confirmation in both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a small set of strong, biologically interpretable relationships. BRIX1-WDR12 supports a ribosome-biogenesis connection; HNRNPH1-HNRNPL supports an RNA-processing connection; LDHA-PKM supports glycolytic coupling; and PSMC2-PSMD13 supports proteasome assembly or function. The STRING supplementary terms (STRING Keyword Ubl conjugation; within-query FDR = 0.0394) and (STRING Keyword Isopeptide bond; within-query FDR = 0.0408) connect many members to ubiquitin conjugation and isopeptide-bond biology, but these are within-query STRING results and are not globally corrected enrichment evidence. hu.MAP independently places PKM, APEX1 and YARS1 together in (hu.MAP huMAP3_14442.1), places APEX1 and YARS1 together across (hu.MAP huMAP3_04783.1), (hu.MAP huMAP3_10115.1) and (hu.MAP huMAP3_13998.1), and repeatedly places PSMC2 and PSMD13 together in proteasome complexes through (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1). These observations show that parts of the module recover known molecular machinery. The remaining cross-process links are not strongly supported by the listed STRING or hu.MAP relationships and may reflect co-abundance, shared cellular state, indirect regulation or sample composition rather than direct physical interaction.

**STRING interactions (score >= 0.7)**: 4 of 120 gene pairs: BRIX1–WDR12 (0.998); HNRNPH1–HNRNPL (0.982); LDHA–PKM (0.997); PSMC2–PSMD13 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Ubl conjugation (FDR = 0.0394, 11 genes); Keyword Isopeptide bond (FDR = 0.0408, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (PKM, APEX1, YARS1; 3/57); huMAP3_04783.1 (APEX1, YARS1; 2/4); huMAP3_10115.1 (APEX1, YARS1; 2/14); huMAP3_13998.1 (APEX1, YARS1; 2/23); huMAP3_05064.1 (PSMC2, PSMD13; 2/31); huMAP3_09656.1 (PSMC2, PSMD13; 2/64); huMAP3_13725.1 (PSMC2, PSMD13; 2/69)

### Novelty

The module should not be presented as a newly discovered molecular complex or as a newly established pathway. Several of its relationships are already known: the PKM-LDHA pair, the PSMC2-PSMD13 proteasome pair, the HNRNPH1-HNRNPL RNA-binding pair, the BRIX1-WDR12 ribosome-biogenesis pair, and the APEX1-YARS1-containing hu.MAP complexes. The potentially novel aspect is the cross-tissue co-abundance configuration that places these established components in one shared module across autonomic nervous system and lung. However, the available evidence does not show whether this configuration has been reported previously, and absence from a reference interaction resource would not establish novelty. A careful claim is therefore that the module is a potentially useful data-derived association pattern, not a proven new complex, mechanism or disease pathway.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular stress and maintenance state shared between the sampled autonomic nervous system and lung. In this model, increased biosynthetic and translational demand engages YARS1 and associated protein-production machinery; PKM and LDHA support glycolytic energy generation; CCT3 and the proteasome components PSMC2 and PSMD13 maintain protein folding and removal of damaged proteins; APEX1 and CBX5 help manage DNA damage and chromatin consequences; and the hnRNP, EFTUD2, BRIX1 and WDR12 components maintain RNA processing and ribosome production. MTFP1 and SEC16A could connect this state to mitochondrial dynamics and secretory-pathway organization. This is a mechanistic hypothesis, not a demonstrated causal chain. It should be tested with cell-resolved expression or protein data, perturbation of selected hub genes, and assessment of whether the module tracks cellular stress, metabolic demand or tissue composition.

### Important genes

#### YARS1

- **Related proteins** (co-abundance neighbors): APEX1 (0.85), MAT2A (0.84), HNRNPH1 (0.84), PSMC2 (0.83), PSMD13 (0.82), BRIX1 (0.81), LDHA (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_14442.1, huMAP3_04783.1, huMAP3_10115.1, huMAP3_13998.1
- **Function (MyGene.info)**: tyrosyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Tyrosyl-tRNA synthetase belongs to the class I tRNA synthetase family. Cytokine activities have also been observ…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease dominant intermediate C (0.739); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset 2 (0.707); hereditary disease (0.509); Charcot-Marie-Tooth disease (0.418); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset (0.333)
- **Europe PMC papers**: 215
- **Why important**: YARS1 is the central network connector in the supplied graph, linking APEX1, MAT2A, HNRNPH1, PSMC2, PSMD13, BRIX1 and LDHA. It is a tyrosyl-tRNA synthetase with an established role in aminoacylation and protein translation, and the fact sheet also notes cytokine activity for a processed human form. It occurs with APEX1 in several hu.MAP complexes (hu.MAP huMAP3_14442.1), (hu.MAP huMAP3_04783.1), (hu.MAP huMAP3_10115.1) and (hu.MAP huMAP3_13998.1), has neurologic and multisystem disease associations, and has substantial literature support.
- **Conclusion**: Established evidence supports YARS1 as a translation-related housekeeping protein and as an important structural connector in this module. The hypothesis that it coordinates metabolic, proteasomal and RNA-maintenance processes in the shared tissue state is plausible from its network position but is not demonstrated.

#### APEX1

- **Related proteins** (co-abundance neighbors): MTFP1 (0.89), YARS1 (0.85), PKM (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_14442.1, huMAP3_04783.1, huMAP3_10115.1, huMAP3_13998.1
- **Function (MyGene.info)**: apurinic/apyrimidinic endodeoxyribonuclease 1. The APEX gene encodes the major AP endonuclease in human cells. It encodes the APEX endonuclease, a DNA repair enzyme with apurinic/apyrimidinic (AP) activity. Such AP activity sites occur frequently in DNA molecules by spontaneous hydrolysis, by DNA damaging agents or by DNA glycosylases that remove specific abnormal bases. The AP sites are the most frequent pre-mutagenic lesions that can prevent…
- **Diseases (Open Targets)**: neurodegenerative disease (0.464); Galloway-Mowat syndrome (0.429); hereditary disease (0.161); neoplasm (0.118); non-small cell lung carcinoma (0.115)
- **Europe PMC papers**: 2928
- **Why important**: APEX1 links YARS1, PKM and MTFP1 and is present with YARS1 in multiple hu.MAP complexes (hu.MAP huMAP3_14442.1), (hu.MAP huMAP3_04783.1), (hu.MAP huMAP3_10115.1) and (hu.MAP huMAP3_13998.1). Its established function is apurinic/apyrimidinic endonuclease activity in base-excision DNA repair, with additional roles in telomere maintenance and apoptotic signaling. It has the largest literature volume among the selected genes and disease associations spanning neurodegeneration, Galloway-Mowat syndrome and lung cancer.
- **Conclusion**: Established evidence identifies APEX1 as a DNA-repair and genome-maintenance factor that is strongly connected to YARS1 in the module and in hu.MAP. A role as a bridge between genome maintenance, metabolism and mitochondrial state is a reasonable hypothesis, but the co-abundance data do not establish that mechanism.

#### PKM

- **Related proteins** (co-abundance neighbors): LDHA (0.83), APEX1 (0.81); STRING partners: LDHA (0.997)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: pyruvate kinase M1/2. This gene encodes a protein involved in glycolysis. The encoded protein is a pyruvate kinase that catalyzes the transfer of a phosphoryl group from phosphoenolpyruvate to ADP, generating ATP and pyruvate. This protein has been shown to interact with thyroid hormone and may mediate cellular metabolic effects induced by thyroid hormones. This protein has been found to bind Opa protein, a bacterial o…
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); autoimmune disorder of central nervous system (0.370); tympanic membrane perforation (0.204); neoplasm (0.121); hepatocellular carcinoma (0.120)
- **Europe PMC papers**: 8544
- **Why important**: PKM is directly connected to LDHA in STRING and to APEX1 in the module, and it is included in hu.MAP complex (hu.MAP huMAP3_14442.1) with APEX1 and YARS1. Its established function is pyruvate-kinase activity in glycolysis, with additional reported roles in chromatin remodeling, programmed cell death and transcriptional regulation. It has a very large literature base and disease associations including neurodegenerative disease and cancer.
- **Conclusion**: Established evidence supports PKM as the principal metabolic anchor of the module, especially through its known relationship with LDHA. It may connect energy metabolism to proteostasis or DNA maintenance in the shared tissue state, but that cross-process role remains a hypothesis.

#### LDHA

- **Related proteins** (co-abundance neighbors): PKM (0.83), YARS1 (0.81); STRING partners: PKM (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lactate dehydrogenase A. This gene encodes the A subunit of lactate dehydrogenase enzyme which catalyzes the reversible conversion of pyruvate to lactate with the concomitant oxidation of NADH to NAD in anaerobic glycolysis. The protein is found predominantly in skeletal muscle and belongs to the lactate dehydrogenase family. Mutations in this gene have been linked to exertional myoglobinuria. The human genome contains se…
- **Diseases (Open Targets)**: glycogen storage disease due to lactate dehydrogenase M-subunit deficiency (0.755); disorder of glycogen metabolism (0.505); glycogen storage disease XV (0.505); primary hyperoxaluria (0.447); hereditary disease (0.190)
- **Europe PMC papers**: 20747
- **Why important**: LDHA forms the strongest listed STRING relationship with PKM and is connected to YARS1 in the module. It catalyzes the reversible conversion of pyruvate and lactate during anaerobic glycolysis and has established associations with lactate metabolism, muscle biology and inherited metabolic disease. Its literature volume is especially large, making it a well-supported metabolic marker rather than an unexplored gene.
- **Conclusion**: Established evidence supports LDHA as a glycolytic and lactate-metabolism component that reinforces the PKM signal. The hypothesis that glycolytic flux helps drive the co-abundance of translation, proteasome and repair proteins is biologically coherent but not proven by this module.

#### PSMC2

- **Related proteins** (co-abundance neighbors): CCT3 (0.85), YARS1 (0.83), EFTUD2 (0.81); STRING partners: PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 connects YARS1, CCT3 and EFTUD2 and has a near-maximal STRING relationship with PSMD13. Together with PSMD13 it appears in hu.MAP proteasome complexes (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1). Its established function is as an ATPase component of the proteasome regulator, supporting ubiquitin-dependent protein degradation and responses to oxidative stress. It has substantial literature and disease associations involving myeloma, lymphoma, neoplasia, HIV and amyloidosis.
- **Conclusion**: Established evidence supports PSMC2 as a proteostasis and protein-quality-control anchor, with independent support from STRING and hu.MAP. Its possible role in coupling proteasomal demand to translation, metabolism and RNA processing is a hypothesis rather than an experimentally established property of this module.

#### PSMD13

- **Related proteins** (co-abundance neighbors): YARS1 (0.82); STRING partners: PSMC2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 is the non-ATPase partner of PSMC2 in STRING and is repeatedly represented with PSMC2 in hu.MAP complexes (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1). Its established function is as a proteasome regulatory component involved in ubiquitin-dependent protein catabolism, oxidative-stress response and type I interferon response. It also has disease associations involving plasma-cell myeloma, mantle-cell lymphoma, neurodegeneration, neoplasia and HIV, with a substantial literature base.
- **Conclusion**: Established evidence supports PSMD13 as a proteasome-associated partner that strengthens the interpretation of a protein-quality-control arm in the module. The possibility that this arm is activated together with glycolytic and translation programs in autonomic nervous system and lung samples is a hypothesis requiring cellular and perturbational validation.

## Module 10

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (16)**: ARPC5L, CHERP, CWC27, EDC4, HNRNPLL, JMJD6, MDN1, MYCBP, NR2C2AP, PAXBP1, PELO, PSME3IP1, TAF5, UHRF1, XRN2, ZNF326

### Function

The strongest functional interpretation is coordinated nuclear RNA and mRNA quality-control biology. (GO:BP mRNA metabolic process; q_global = 0.0105) is the only GO/KEGG term that passed global correction and links much of the module to mRNA metabolic process, including CWC27, EDC4, HNRNPLL, JMJD6, PAXBP1, PELO, TAF5, XRN2 and ZNF326. This interpretation is reinforced, but only supplementary, by the STRING terms for mRNA metabolism and RNA metabolism (STRING Process mRNA metabolic process; within-query FDR = 0.01) and (STRING Process RNA metabolic process; within-query FDR = 0.0424). The member annotations support several connected processes: RNA splicing through CWC27, HNRNPLL and PAXBP1; mRNA decapping and decay through EDC4 and PELO; transcription termination and RNA catabolism through XRN2; transcriptional regulation through ZNF326 and TAF5; and ribosome rescue or ribosome biogenesis through PELO and MDN1. The module therefore appears to represent a coordinated RNA-processing and RNA-surveillance program rather than a tissue-specific effector pathway. Its biological meaning is likely broader than any single sub-process because the module also contains genes involved in transcription, ribosome assembly, chromatin or transcriptional regulation, cell-cycle or DNA-damage control, calcium homeostasis, and actin regulation.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most members have low tissue specificity, and protein detection in lung is reported for nearly all members with available lung evidence, which is consistent with broadly present intracellular proteins rather than a specialized lung or autonomic nervous system product. HPA single-cell annotations are nevertheless informative: many genes are enhanced in germ-cell states, while others are associated with erythrocyte or neutrophil progenitors, and one gene is enhanced in a lymphoid or bone-marrow context. This pattern could reflect shared proliferative, progenitor, or cell-composition signals in the two tissue groups. It does not support a simple blood-contamination explanation because the blood-cell specificity is generally low, several genes are not detected in immune cells, and the proteins are intracellular rather than secreted. The shared module may therefore primarily reflect a broadly expressed RNA-processing program, with possible contribution from shared cell states or progenitor-like populations.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP mRNA metabolic process | 0.0105 | CWC27, EDC4, HNRNPLL, JMJD6, PAXBP1, PELO, TAF5, XRN2, ZNF326 |

### STRING and hu.MAP

At the supplied high-confidence STRING threshold, no pairwise interaction among module genes was present, and hu.MAP reported no complex containing multiple module members. Thus the module is not corroborated as a known physical protein complex by these resources. STRING functional enrichment nevertheless independently points toward RNA and mRNA metabolism (STRING Process mRNA metabolic process; within-query FDR = 0.01) and (STRING Process RNA metabolic process; within-query FDR = 0.0424). The absence of STRING edges and hu.MAP complexes means that the co-abundance edges should be interpreted primarily as coordinated abundance relationships, not as demonstrated direct binding. The genes can still participate in the same cellular workflow through transient interactions, distinct complexes, shared transcriptional control, or common dependence on cell state.

**STRING interactions (score >= 0.7)**: 0 of 120 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Process mRNA metabolic process (FDR = 0.01, 9 genes); Process RNA metabolic process (FDR = 0.0424, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module is potentially novel as a conserved co-abundance pattern shared by autonomic nervous system and lung, because it is not represented by a known multi-member STRING interaction set or a hu.MAP complex. However, those absences do not establish novelty: the individual functions of RNA splicing, mRNA decay, transcriptional regulation, ribosome rescue, and RNA surveillance are already established, and the common mRNA-metabolism signal is supported by both (GO:BP mRNA metabolic process; q_global = 0.0105) and the supplementary STRING terms (STRING Process mRNA metabolic process; within-query FDR = 0.01) and (STRING Process RNA metabolic process; within-query FDR = 0.0424). The defensible conclusion is that the cross-tissue co-abundance organization may be new or under-characterized, whereas the underlying molecular functions are not new. Confirmation would require comparison with published tissue co-expression modules, independent cohorts, cell-composition controls, and perturbation or physical-interaction experiments.

**Hypothesis.** Hypothesis: the shared module marks a conserved cellular demand for maintaining transcript fidelity and protein-production capacity in lung and autonomic nervous system samples. A coordinated program involving transcriptional control through ZNF326 and TAF5, spliceosome-associated processing through CWC27 and HNRNPLL, mRNA decapping or decay through EDC4 and XRN2, and stalled-ribosome rescue through PELO could couple transcript maturation to removal of defective transcripts and protection from translation stress. The association with progenitor-like HPA cell states suggests that variation in proliferative or differentiation state may help generate the co-abundance pattern. This is a mechanistic hypothesis, not a demonstrated pathway: the lack of high-confidence STRING relationships and hu.MAP complexes argues that the proposed coordination may be regulatory or state-dependent rather than a single stable molecular assembly.

### Important genes

#### ZNF326

- **Related proteins** (co-abundance neighbors): ARPC5L (0.87), CWC27 (0.84), PSME3IP1 (0.84), NR2C2AP (0.82), MYCBP (0.81), XRN2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger protein 326. Enables RNA polymerase II complex binding activity. Involved in regulation of DNA-templated transcription, elongation and regulation of RNA splicing. Located in nucleoplasm. Part of DBIRD complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: ocular hypotension (0.227); insomnia (0.222); adolescent idiopathic scoliosis (0.207); juvenile dermatomyositis (0.205); major depressive disorder (0.205)
- **Europe PMC papers**: 258
- **Why important**: ZNF326 is the strongest network hub in the supplied subgraph and connects the RNA-processing signal to several module members, including CWC27, XRN2 and PSME3IP1. It is directly present in the globally significant mRNA metabolic term (GO:BP mRNA metabolic process; q_global = 0.0105) and both supplementary STRING terms (STRING Process mRNA metabolic process; within-query FDR = 0.01) and (STRING Process RNA metabolic process; within-query FDR = 0.0424). Its annotations implicate RNA splicing, transcriptional elongation and RNA polymerase binding, while its membership in the DBIRD complex provides a plausible bridge between transcription and RNA processing. It has substantial literature coverage and disease associations that include ocular and neuropsychiatric traits, although those associations do not establish a role in this module.
- **Conclusion**: Established: ZNF326 is a central co-abundance member with annotations linking transcription and RNA processing. Hypothesis: it may act as a regulatory coordinator of the module, but the absence of STRING and hu.MAP support prevents claiming that it physically organizes the other proteins.

#### PELO

- **Related proteins** (co-abundance neighbors): HNRNPLL (0.84), CHERP (0.84), EDC4 (0.82), MDN1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pelota mRNA surveillance and ribosome rescue factor. This gene encodes a protein which contains a conserved nuclear localization signal. The encoded protein may have a role in spermatogenesis, cell cycle control, and in meiotic cell division. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.445); diabetes mellitus (0.431); open-angle glaucoma (0.346); familial lipoprotein lipase deficiency (0.319); pulmonary edema (0.292)
- **Europe PMC papers**: 1610
- **Why important**: PELO is a well-connected internal node linking HNRNPLL, CHERP, EDC4 and MDN1. It appears in (GO:BP mRNA metabolic process; q_global = 0.0105), (STRING Process mRNA metabolic process; within-query FDR = 0.01) and (STRING Process RNA metabolic process; within-query FDR = 0.0424), and its established functions in RNA surveillance, non-stop and no-go decay, ribosome disassembly, and rescue of stalled ribosomes make it especially informative for the quality-control interpretation. It has substantial literature volume and disease associations that include metabolic and pulmonary phenotypes.
- **Conclusion**: Established: PELO provides a direct molecular link between defective-mRNA handling and translation surveillance. Hypothesis: its co-abundance with both RNA-decay and ribosome-related genes may indicate coordinated protection from translational stress in the shared tissue context.

#### XRN2

- **Related proteins** (co-abundance neighbors): ZNF326 (0.81), CWC27 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 5'-3' exoribonuclease 2. This gene encodes a 5'-3' exonuclease that promotes transcription termination at cotranscriptional cleavage sites. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: attention deficit-hyperactivity disorder (0.339); neurodegenerative disease (0.326); atrial fibrillation (0.305); food allergy (0.271); adolescent idiopathic scoliosis (0.221)
- **Europe PMC papers**: 1676
- **Why important**: XRN2 is connected to the ZNF326-CWC27 portion of the module and is included in (GO:BP mRNA metabolic process; q_global = 0.0105), (STRING Process mRNA metabolic process; within-query FDR = 0.01) and (STRING Process RNA metabolic process; within-query FDR = 0.0424). Its established roles in five-prime-to-three-prime exonucleolytic RNA degradation, RNA polymerase termination, rRNA processing and RNA catabolism place it at the interface of transcript production and transcript removal. It also has substantial literature coverage and disease associations involving neurodegenerative and cardiovascular traits.
- **Conclusion**: Established: XRN2 is a plausible core effector of RNA maturation and degradation within the module. Hypothesis: coordinated XRN2 abundance may couple transcription termination with downstream RNA surveillance, but the co-abundance data do not demonstrate directionality or direct regulation by ZNF326 or CWC27.

#### CWC27

- **Related proteins** (co-abundance neighbors): ZNF326 (0.84), XRN2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CWC27 spliceosome associated cyclophilin. Predicted to enable peptidyl-prolyl cis-trans isomerase activity. Predicted to be involved in protein peptidyl-prolyl isomerization. Located in nucleoplasm. Part of U2-type precatalytic spliceosome and catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: metaphyseal chondrodysplasia-retinitis pigmentosa syndrome (0.764); retinitis pigmentosa (0.450); inherited retinal dystrophy (0.433); Abnormality of the skeletal system (0.421); diverticular disease (0.394)
- **Europe PMC papers**: 282
- **Why important**: CWC27 occupies a bridge position between ZNF326 and XRN2 and is present in (GO:BP mRNA metabolic process; q_global = 0.0105), (STRING Process mRNA metabolic process; within-query FDR = 0.01) and (STRING Process RNA metabolic process; within-query FDR = 0.0424). Its spliceosome association and predicted peptidyl-prolyl isomerase activity provide direct support for pre-mRNA processing and spliceosome function. Its disease associations include skeletal and retinal syndromes, and its literature volume is sufficient to make it a biologically interpretable module member rather than an uncharacterized correlate.
- **Conclusion**: Established: CWC27 supports a spliceosome and RNA-processing component of the module. Hypothesis: its position may reflect coordination between transcript splicing and subsequent RNA decay, but no direct physical link to the other module members is established here.

#### HNRNPLL

- **Related proteins** (co-abundance neighbors): PELO (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L like. HNRNPLL is a master regulator of activation-induced alternative splicing in T cells. In particular, it alters splicing of CD45 (PTPRC; MIM 151460), a tyrosine phosphatase essential for T-cell development and activation (Oberdoerffer et al., 2008 [PubMed 18669861]).[supplied by OMIM, Aug 2008].
- **Diseases (Open Targets)**: placenta praevia (0.222); gastric ulcer (0.222); hemorrhage (0.222); post term pregnancy (0.079); kidney disorder (0.079)
- **Europe PMC papers**: 335
- **Why important**: HNRNPLL is connected to PELO and is present in (GO:BP mRNA metabolic process; q_global = 0.0105), (STRING Process mRNA metabolic process; within-query FDR = 0.01) and (STRING Process RNA metabolic process; within-query FDR = 0.0424). It is an established regulator of alternative splicing, including activation-dependent splicing in T cells, and its HPA annotation in progenitor and pituicyte-related cell states is relevant to interpreting possible cell-state contributions. Its literature volume is moderate and its known role provides a functional complement to the decay and surveillance activities represented by PELO and EDC4.
- **Conclusion**: Established: HNRNPLL contributes an alternative-splicing interpretation and may reflect cell-state-sensitive RNA regulation. Hypothesis: it could help explain how a broadly expressed RNA-processing program varies across the two tissue groups, but the module does not establish a T-cell-specific mechanism.

## Module 11

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (10)**: ATP11C, CPSF7, GTF2I, APOOL, EMG1, REXO2, PCK2, TFAM, ATP6V0A1, WDR48

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING functional enrichment. Therefore, the module does not support a specific pathway-level functional assignment from enrichment alone. Its network is composed of several small connected segments rather than a densely interconnected system. The strongest biological themes suggested by the gene annotations are intracellular organelle maintenance, mitochondrial gene expression and metabolism, vesicle or organelle acidification, RNA processing, transcriptional regulation, and membrane lipid translocation. ATP6V0A1 supports organelle acidification and autophagic or endosomal processes; PCK2, TFAM, REXO2, and APOOL point toward mitochondrial metabolism, mitochondrial nucleic-acid maintenance, and crista organization; CPSF7 and EMG1 support RNA maturation; and ATP11C supports phospholipid translocation. Taken together, the most defensible interpretation is a broad intracellular homeostasis or cellular-state module rather than a narrowly defined autonomic or pulmonary pathway.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. It is also not blood-cell enriched according to the supplied HPA evidence, because every gene has low immune-cell specificity and no enriched blood-cell category is reported. Most genes have low tissue specificity, while the tissue-enhanced or group-enriched signals are distributed across liver, brain, intestine, kidney, and other contexts rather than concentrated in autonomic nervous system or lung. The single-cell annotations include reproductive and developmental cell types, with one neutrophil association, but do not establish a shared blood-cell source. Protein detection in lung is broad across the module, whereas no matching autonomic-nervous-system HPA tissue assessment is available. Thus, the shared co-abundance pattern is more plausibly a broadly expressed cellular-state signal, or a shared cell-composition effect, than a secreted or blood-derived signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes. This argues against interpreting the co-abundance edges as established physical protein interactions, although lack of a STRING edge does not exclude functional, regulatory, compartmental, or context-dependent relationships. The principal independent complex evidence is (hu.MAP huMAP3_12042.1), a hu.MAP complex containing ATP11C and ATP6V0A1 alongside many proteins associated with vacuolar ATPase, vesicle, membrane, and organelle functions. This supports a possible shared organelle or membrane-related context for that pair, but the complex is much broader than the module and does not validate the entire network. The remaining module relationships have no supplied hu.MAP or STRING support, so their interpretation should remain cautious.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12042.1 (ATP11C, ATP6V0A1; 2/56)

### Novelty

The module may represent a new tissue-pair co-abundance observation, but it cannot be called a newly discovered molecular complex or pathway. The absence of STRING interactions and the limited hu.MAP overlap indicate that this exact gene combination is not well represented by the supplied catalogued interaction resources. However, that absence alone does not prove novelty: co-abundance can arise from shared regulation, cell composition, protein abundance constraints, organelle state, or technical and sampling effects. Several component genes have established functions and disease links, and (hu.MAP huMAP3_12042.1) provides partial prior complex context. A novelty claim would therefore require replication in independent autonomic-nervous-system and lung cohorts, control for cell composition and tissue quality, and comparison with published co-expression or proteomic modules.

**Hypothesis.** Hypothesis: the module reflects a coordinated cellular maintenance state involving mitochondrial fitness, intracellular RNA and protein processing, vesicular acidification, and membrane lipid handling. In this model, mitochondrial functions involving PCK2, TFAM, REXO2, and APOOL are coupled to ATP6V0A1-dependent organelle acidification and ATP11C-dependent membrane lipid asymmetry, while GTF2I, CPSF7, and EMG1 report associated changes in transcriptional, transcript-processing, and ribosome-biogenesis capacity. The observed pattern could therefore arise when related lung and autonomic cell populations experience a common metabolic or organelle-demand state. This is a hypothesis rather than a demonstrated mechanism, because enrichment was globally negative and most relationships lack direct interaction support.

### Important genes

#### ATP6V0A1

- **Related proteins** (co-abundance neighbors): REXO2 (0.88), TFAM (0.83), PCK2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_12042.1
- **Function (MyGene.info)**: ATPase H+ transporting V0 subunit a1. This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 d…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy 104 (0.712); neurodevelopmental disorder with epilepsy and brain atrophy (0.696); Seizure (0.420); hereditary disease (0.414); developmental disability (0.370)
- **Europe PMC papers**: 854
- **Why important**: ATP6V0A1 is among the most connected genes in the module and participates in (hu.MAP huMAP3_12042.1). Its established function as a vacuolar ATPase subunit links it to acidification of lysosomal, endosomal, Golgi, and vesicular compartments, autophagy, and synaptic vesicle proton gradients. It is tissue-enhanced in brain, detected in lung, and has substantial literature and disease association with developmental and epileptic disorders. Its central network position and organelle function make it a strong anchor for interpreting the module.
- **Conclusion**: Established evidence supports ATP6V0A1 as an organelle-acidification and vesicle-biology component, with partial complex support from (hu.MAP huMAP3_12042.1). It is plausible, but unproven, that its co-abundance connects vesicular acidification to the mitochondrial and RNA-processing signals in this module.

#### ATP11C

- **Related proteins** (co-abundance neighbors): PCK2 (0.90), CPSF7 (0.85), GTF2I (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12042.1
- **Function (MyGene.info)**: ATPase phospholipid transporting 11C (ATP11C blood group). Enables phosphatidylethanolamine flippase activity and phosphatidylserine flippase activity. Predicted to be involved in phospholipid translocation; positive regulation of B cell differentiation; and pre-B cell differentiation. Located in endoplasmic reticulum and plasma membrane. Is integral component of plasma membrane. Implicated in X-linked congenital hemolytic anemia. [provided by Alliance of…
- **Diseases (Open Targets)**: familial hemolytic anemia (0.558); neutropenia, severe congenital, 2, autosomal dominant (0.069); autosomal dominant severe congenital neutropenia (0.069); Rh deficiency syndrome (0.067); neonatal intrahepatic cholestasis due to citrin deficiency (0.062)
- **Europe PMC papers**: 536
- **Why important**: ATP11C has one of the strongest network positions and connects the PCK2, CPSF7, and GTF2I branches. It encodes a phosphatidylserine and phosphatidylethanolamine flippase involved in membrane lipid translocation and is also represented with ATP6V0A1 in (hu.MAP huMAP3_12042.1). Its established links to membrane biology, B-cell differentiation, and X-linked congenital hemolytic anemia provide a mechanistic bridge between cellular membranes and disease-relevant physiology. It has substantial literature support.
- **Conclusion**: Established evidence supports ATP11C as a membrane-lipid homeostasis gene and a plausible module hub. The idea that it coordinates membrane lipid asymmetry with organelle acidification in this tissue pair remains a hypothesis, not a demonstrated interaction.

#### PCK2

- **Related proteins** (co-abundance neighbors): ATP11C (0.90), ATP6V0A1 (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoenolpyruvate carboxykinase 2, mitochondrial. This gene encodes a mitochondrial enzyme that catalyzes the conversion of oxaloacetate to phosphoenolpyruvate in the presence of guanosine triphosphate (GTP). A cytosolic form of this protein is encoded by a different gene and is the key enzyme of gluconeogenesis in the liver. Alternatively spliced transcript variants have been described. [provided by RefSeq, Apr 2014].
- **Diseases (Open Targets)**: phosphoenolpyruvate carboxykinase deficiency, mitochondrial (0.511); phosphoenolpyruvate carboxykinase deficiency (0.443); neuropathy (0.187); Gait disturbance (0.185); retinitis pigmentosa (0.148)
- **Europe PMC papers**: 2644
- **Why important**: PCK2 connects ATP11C with ATP6V0A1 and is therefore positioned at the compact central link between membrane and organelle-related branches. Its established mitochondrial phosphoenolpyruvate carboxykinase activity connects oxaloacetate metabolism with gluconeogenic and nutrient-response processes. HPA associates it with intestine, kidney, and liver and with several metabolically specialized cell types. It has extensive literature and disease associations involving mitochondrial PCK2 deficiency and neurological or visual phenotypes.
- **Conclusion**: Established evidence supports PCK2 as a mitochondrial metabolic regulator. Its network placement makes metabolic state a credible explanation for part of the module, but the data do not establish that PCK2 directly regulates either ATP11C or ATP6V0A1.

#### TFAM

- **Related proteins** (co-abundance neighbors): ATP6V0A1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transcription factor A, mitochondrial. This gene encodes a key mitochondrial transcription factor containing two high mobility group motifs. The encoded protein also functions in mitochondrial DNA replication and repair. Sequence polymorphisms in this gene are associated with Alzheimer's and Parkinson's diseases. There are pseudogenes for this gene on chromosomes 6, 7, and 11. Alternative splicing results in multiple transcript variant…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome 15 (hepatocerebral type) (0.689); neurodegenerative disease (0.550); stroke disorder (0.191); alcohol drinking (0.189); musculoskeletal system disorder (0.132)
- **Europe PMC papers**: 14423
- **Why important**: TFAM connects directly to ATP6V0A1 and is a key regulator of mitochondrial DNA transcription, replication, and repair. It has very extensive literature, disease associations involving mitochondrial DNA depletion and neurodegeneration, and HPA protein detection in lung. Its function provides a strong biological rationale for interpreting the module as involving mitochondrial capacity or stress, despite its peripheral network position.
- **Conclusion**: Established evidence supports TFAM as a mitochondrial genome maintenance factor with neurological disease relevance. A coordinated mitochondrial fitness program is a reasonable interpretation of its co-abundance with PCK2, REXO2, and APOOL, but this coordination remains inferential.

#### GTF2I

- **Related proteins** (co-abundance neighbors): ATP11C (0.85), WDR48 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: general transcription factor IIi. This gene encodes a phosphoprotein containing six characteristic repeat motifs. The encoded protein binds to the initiator element (Inr) and E-box element in promoters and functions as a regulator of transcription. This locus, along with several other neighboring genes, is deleted in Williams-Beuren syndrome. There are many closely related genes and pseudogenes for this gene on chromosome 7. This …
- **Diseases (Open Targets)**: neurodegenerative disease (0.548); type 2 diabetes mellitus (0.520); atrial fibrillation (0.519); hypertensive disorder (0.500); Abnormality of the skeletal system (0.495)
- **Europe PMC papers**: 2606
- **Why important**: GTF2I links ATP11C with WDR48 and represents the transcriptional-regulatory branch of the module. It is a transcription factor associated with RNA polymerase II regulation and with Williams-Beuren syndrome through the relevant chromosomal region. It has substantial literature and multiple disease associations, including neurodegenerative, metabolic, cardiovascular, and hypertensive conditions. Its network position suggests that transcriptional state may contribute to the observed co-abundance pattern.
- **Conclusion**: Established evidence supports GTF2I as a transcriptional regulator with broad disease relevance. Its connection to the membrane branch may reflect shared cellular regulation, but no direct regulatory relationship between GTF2I and the other module genes is established here.

## Module 12

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (6)**: ATL3, CANX, HSPA13, MAIP1, UQCRC1, RAB21

### Function

The module does not have a GO or KEGG term that passed global correction, and STRING functional enrichment is absent. Its gene annotations nevertheless suggest a cellular homeostasis theme spanning endoplasmic-reticulum organization and protein quality control, intracellular membrane trafficking, mitochondrial calcium handling, and respiratory-chain activity. The co-abundance pattern therefore appears biologically compatible with coordinated organelle maintenance rather than with a confidently assigned canonical pathway. Because the network is a connected chain, the pattern may reflect coordinated cellular state or shared regulation more than a set of direct physical interactions.

**Cell composition.** The module is not dominated by plasma proteins, secreted proteins, or blood-cell-enriched genes. HPA assigns low immune-cell specificity to every member, and only HSPA13 has an intracellular-and-membrane secretome annotation. Most genes have low tissue specificity, while UQCRC1 is tissue enhanced in muscle-related tissues. Several genes show enrichment in reproductive or specialized cell types, especially spermatid-related populations, but this does not establish that the lung or autonomic-nervous-system signal originates from those cells. Protein detection in lung is reported for nearly all members with available tissue data, whereas autonomic-nervous-system matching tissue data are unavailable. Overall, the module is more consistent with broadly distributed intracellular proteins and shared cellular machinery than with a blood-contamination signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair reaches the reported high-confidence STRING interaction threshold, and no hu.MAP complex contains multiple module members. Thus, the observed co-abundance edges are not supported here by curated high-confidence protein interactions or a shared hu.MAP complex. The absence of these relationships means the module should not be described as a validated physical complex. Instead, it may represent coordinated expression, indirect functional coupling, organelle-state covariation, or context-specific relationships that are not captured by these resources.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is potentially novel as a cross-tissue co-abundance pattern because it links ER proteins, a membrane-trafficking GTPase, mitochondrial proteins, and a microsomal heat-shock protein without corresponding STRING or hu.MAP support. However, novelty cannot be established solely from absence in those databases. Several individual gene functions and disease associations are already established, and the module may reflect a new relationship among known components rather than newly discovered molecular functions. The lack of globally significant GO or KEGG enrichment also limits claims that it represents a previously unrecognized pathway.

**Hypothesis.** Hypothesis: the shared module captures a conserved organelle-stress and trafficking state in which ER architecture and quality control are coordinated with endosomal transport and mitochondrial function. ATL3 could organize ER tubules, CANX and HSPA13 could support folding and handling of membrane or secretory proteins, RAB21 could couple trafficking to adhesion or receptor movement, and MAIP1 together with UQCRC1 could reflect mitochondrial calcium and respiratory capacity. This model predicts coordinated changes in ER morphology, protein-folding burden, vesicle trafficking, and mitochondrial respiration, but the co-abundance data alone do not establish directionality, causality, or direct molecular binding.

### Important genes

#### ATL3

- **Related proteins** (co-abundance neighbors): RAB21 (0.82), UQCRC1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: atlastin GTPase 3. This gene encodes a member of a family of dynamin-like, integral membrane GTPases. The encoded protein is required for the proper formation of the network of interconnected tubules of the endoplasmic reticulum. Mutations in this gene may be associated with hereditary sensory neuropathy type IF. Alternatively spliced transcript variants that encode distinct isoforms have been described. [provided b…
- **Diseases (Open Targets)**: neuropathy, hereditary sensory, type 1F (0.718); hereditary sensory and autonomic neuropathy type 1 (0.617); hereditary disease (0.193); Familial prostate cancer (0.112); prostate cancer (0.112)
- **Europe PMC papers**: 672
- **Why important**: ATL3 is a topological bridge between RAB21 and UQCRC1 in the module and has a direct role in ER tubular-network organization and membrane fusion. Its established association with hereditary sensory neuropathy and hereditary sensory and autonomic neuropathy is especially relevant to an autonomic-nervous-system comparison. It has a substantial literature base, supporting interpretation beyond a purely computational association.
- **Conclusion**: Established: ATL3 is an ER membrane GTPase involved in ER organization and is linked to hereditary neuropathy. Hypothesis: ATL3 may connect ER architecture to mitochondrial or trafficking-related state changes represented by this module; the module does not prove that it is the causal hub.

#### CANX

- **Related proteins** (co-abundance neighbors): MAIP1 (0.82), RAB21 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is a highly connected internal node linking MAIP1 and RAB21. It is an ER calcium-binding chaperone involved in glycoprotein folding, assembly, secretion, and ER quality control, making it a strong candidate for the module's proteostasis component. Its extensive literature and disease-area associations provide comparatively strong prior biological support.
- **Conclusion**: Established: CANX participates in ER protein folding and quality control. Hypothesis: CANX may be a major readout of coordinated ER stress or secretory-load regulation in the shared module, although the data do not show that CANX drives the other genes.

#### RAB21

- **Related proteins** (co-abundance neighbors): ATL3 (0.82), CANX (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB21, member RAS oncogene family. This gene belongs to the Rab family of monomeric GTPases, which are involved in the control of cellular membrane traffic. The encoded protein plays a role in the targeted trafficking of integrins via its association with integrin alpha tails. As a consequence, the encoded protein is involved in the regulation of cell adhesion and migration. Expression of this gene is associated with a poor prognos…
- **Diseases (Open Targets)**: neurodegenerative disease (0.469); small intestine neuroendocrine neoplasm (0.095); neoplasm (0.085); posterior cortical atrophy (0.074); nonpapillary renal cell carcinoma (0.065)
- **Europe PMC papers**: 999
- **Why important**: RAB21 is an internal connector between ATL3 and CANX and is annotated in intracellular transport, exocytosis, receptor-mediated endocytosis, axonal transport, adhesion, and migration. These functions provide a plausible bridge between membrane trafficking and neuronal or epithelial cellular states. It also has a substantial literature base and disease associations involving neurodegenerative and neoplastic conditions.
- **Conclusion**: Established: RAB21 regulates membrane traffic and can influence integrin trafficking, adhesion, and migration. Hypothesis: RAB21 may couple ER-derived membrane handling to cell-surface trafficking in the shared module, but co-abundance does not establish a direct interaction with ATL3 or CANX.

#### UQCRC1

- **Related proteins** (co-abundance neighbors): ATL3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase core protein 1. Enables ubiquitin protein ligase binding activity. Predicted to be involved in oxidative phosphorylation. Predicted to act upstream of or within mitochondrial electron transport, ubiquinol to cytochrome c. Located in mitochondrion. Implicated in Alzheimer's disease. Biomarker of Alzheimer's disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: parkinsonism with polyneuropathy (0.642); neurodegenerative disease (0.569); Parkinson disease (0.521); Alzheimer disease (0.519); lysosomal storage disease (0.498)
- **Europe PMC papers**: 1860
- **Why important**: UQCRC1 is the mitochondrial respiratory-chain component at one end of the module and is connected to ATL3. Its annotations support a role in ubiquinol-to-cytochrome-c electron transfer, oxidative phosphorylation, aerobic respiration, and cellular respiration. HPA reports tissue enhancement in muscle-related tissues, and disease resources associate it with neurodegenerative and Parkinson-related conditions. Its substantial literature makes it an important indicator of mitochondrial energetic state.
- **Conclusion**: Established: UQCRC1 is associated with mitochondrial electron transport and respiratory function. Hypothesis: its co-abundance with the ER-organizing ATL3 may indicate coordination between ER structure and mitochondrial energy demand, but the module does not demonstrate organelle contact or metabolic causality.

#### MAIP1

- **Related proteins** (co-abundance neighbors): HSPA13 (0.84), CANX (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: matrix AAA peptidase interacting protein 1. Predicted to enable ribosome binding activity. Involved in calcium import into the mitochondrion; mitochondrial calcium ion homeostasis; and protein insertion into mitochondrial membrane. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: schizophrenia (0.251); Abnormality of the skeletal system (0.197); autism spectrum disorder (0.171); metabolic disease (0.162); bipolar disorder (0.157)
- **Europe PMC papers**: 75
- **Why important**: MAIP1 is a network connector linking CANX and HSPA13 and is annotated to mitochondrial calcium import, mitochondrial calcium homeostasis, and insertion of proteins into the mitochondrial membrane. Its disease associations include neurodevelopmental and metabolic categories, although its literature volume is more limited than that of the better-characterized module members. Its position and mitochondrial annotations make it useful for testing the proposed ER–mitochondrial connection.
- **Conclusion**: Established: MAIP1 is annotated with mitochondrial membrane insertion and calcium-handling functions. Hypothesis: MAIP1 may help convey mitochondrial calcium or membrane-biogenesis state into the shared co-abundance pattern, but this interpretation requires independent functional validation.

## Module 13

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (31)**: BCLAF1, CIAO1, CLCC1, DOCK7, EPS15L1, ERLIN2, EXOSC7, FAM120A, FMR1, RAP1GDS1, HDGFL2, KDM3B, NOP2, NUP88, OSBPL8, PRRC2B, PRRC2C, RBM12, RBM15, RB1, UPF1, POLR1B, RRP1, RSF1, SNW1, CTTN, PPAN, DNTTIP2, TP53BP1, YLPM1, ZMYM2

### Function

The strongest interpretation is a broadly expressed intracellular RNA and nuclear gene-regulatory module, with linked RNA binding, splicing, RNA surveillance, ribosome biogenesis, chromatin, and DNA-damage-response features. This is an interpretation from the annotated genes and network, not a globally significant enrichment result: no GO or KEGG term passed global correction. The supplementary STRING keywords (STRING Keyword Methylation; within-query FDR = 0.0114) and (STRING Keyword Nucleus; within-query FDR = 0.0443) are consistent with methylation-related and nuclear biology, but they are not global enrichment evidence. The dense co-abundance relationships around RBM15, FAM120A, SNW1, and YLPM1 suggest coordinated RNA-associated regulation, while the NOP2–RRP1–PPAN–POLR1B relationships point to a nucleolar and ribosome-production component. DOCK7, EPS15L1, CTTN, OSBPL8, and ERLIN2 provide cytoskeletal, trafficking, lipid, and endoplasmic-reticulum links. Overall, the module is more consistent with a shared cellular state involving RNA processing and nuclear maintenance than with a narrowly defined autonomic or pulmonary pathway.

**Cell composition.** This is not a plasma or secreted-protein module: the genes are overwhelmingly intracellular, with nuclear, nucleolar, cytosolic, vesicular, endoplasmic-reticulum, or plasma-membrane locations and only one secreted-gene annotation. HPA shows generally low tissue specificity, and most genes have low immune-cell specificity, arguing against a simple blood-cell or plasma-protein explanation. Some cell-type-enhanced signals occur in astrocytes, late primary spermatocytes, ependymal cells, neutrophils, and other cell types, but they are heterogeneous rather than a coherent blood signature. Bone-marrow tissue enhancement for RBM15 and BCLAF1 and isolated immune-cell enhancement should therefore be treated as possible contributors, not proof that the shared module is driven by blood contamination. Protein detection in lung is broad across the available module annotations, while autonomic-nervous-system tissue matching was unavailable, so tissue-level protein evidence does not establish autonomic specificity.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited but biologically coherent set of already known relationships. The strongest links connect NOP2 with RRP1 and PPAN, NOP2 with POLR1B, RB1 with TP53BP1, and BCLAF1 with SNW1; STRING also links FAM120A with UPF1. These relationships support nucleolar ribosome production, DNA-damage and cell-cycle control, and RNA surveillance or processing, respectively. The STRING keyword results (STRING Keyword Methylation; within-query FDR = 0.0114) and (STRING Keyword Nucleus; within-query FDR = 0.0443) reinforce methylation-related and nuclear annotations but remain supplementary within-query evidence. hu.MAP provides partial complex-level support: TP53BP1 and ZMYM2 co-occur in (hu.MAP huMAP3_12566.1), UPF1 and FAM120A in (hu.MAP huMAP3_10625.1), and DNTTIP2 and FAM120A in (hu.MAP huMAP3_05807.1). Each complex match contains only a small subset of the module, so the module is not established as a single known complex. Many co-abundance edges lack corresponding high-confidence STRING or hu.MAP support, indicating that the network contains both known molecular relationships and tissue-state correlations.

**STRING interactions (score >= 0.7)**: 8 of 465 gene pairs: BCLAF1–RBM15 (0.72); BCLAF1–SNW1 (0.823); FAM120A–UPF1 (0.741); NOP2–POLR1B (0.879); NOP2–PPAN (0.781); NOP2–RRP1 (0.908); PPAN–RRP1 (0.895); RB1–TP53BP1 (0.928)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Methylation (FDR = 0.0114, 12 genes); Keyword Nucleus (FDR = 0.0443, 23 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12566.1 (TP53BP1, ZMYM2; 2/51); huMAP3_10625.1 (UPF1, FAM120A; 2/57); huMAP3_05807.1 (DNTTIP2, FAM120A; 2/81)

### Novelty

The module should not be called a newly discovered molecular complex or a proven new pathway. Its constituent functions and several relationships are established in the literature and databases, and the absence of a STRING or hu.MAP edge is not evidence of novelty. A more defensible claim is that this particular cross-tissue co-abundance organization may be a new systems-level observation: it combines RNA-processing and surveillance genes, nucleolar machinery, chromatin and DNA-damage regulators, and selected neuronal or membrane-trafficking genes across autonomic nervous system and lung. Novelty would require replication in independent cohorts, preservation after adjustment for cell composition and technical effects, and comparison with existing tissue and single-cell modules. The lack of globally significant GO or KEGG enrichment limits claims of pathway-level novelty but does not invalidate the module.

**Hypothesis.** Hypothesis: a shared cellular program involving RNA maturation, RNA quality control, nucleolar ribosome production, and chromatin or DNA-damage management is coordinated across selected cells present in autonomic nervous system and lung. RBM15, FAM120A, SNW1, and YLPM1 could form a co-abundance-centered RNA-regulatory axis; NOP2, RRP1, PPAN, and POLR1B could reflect coupled ribosome biogenesis; and RB1, TP53BP1, RSF1, and KDM3B could connect this state to proliferation and genome maintenance. DOCK7, EPS15L1, CTTN, OSBPL8, and ERLIN2 may represent context-dependent links to neuronal polarity, endocytosis, cytoskeletal organization, lipid transfer, and endoplasmic-reticulum signaling. This is a testable hypothesis, not a demonstrated mechanism: perturbation of the proposed RNA-regulatory axis should alter RNA processing or surveillance and possibly nucleolar or stress responses in relevant autonomic and pulmonary cell types.

### Important genes

#### RBM15

- **Related proteins** (co-abundance neighbors): RBM12 (0.88), RSF1 (0.88), FAM120A (0.86), SNW1 (0.85), YLPM1 (0.84), RB1 (0.84), HDGFL2 (0.84), NUP88 (0.83), FMR1 (0.82), RAP1GDS1 (0.81), TP53BP1 (0.80), POLR1B (0.80); STRING partners: BCLAF1 (0.72)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 15. Members of the SPEN (Split-end) family of proteins, including RBM15, have repressor function in several signaling pathways and may bind to RNA through interaction with spliceosome components (Hiriart et al., 2005 [PubMed 16129689]).[supplied by OMIM, Feb 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); lung adenocarcinoma (0.219); esophageal squamous cell carcinoma (0.209); osteosarcoma (0.209); hepatocellular carcinoma (0.206)
- **Europe PMC papers**: 3897
- **Why important**: RBM15 is the most network-central selected gene, linking many module members including FAM120A, SNW1, RBM12, RSF1, YLPM1, and DNA- or chromatin-associated genes. Its established annotations include RNA binding, alternative splicing, RNA methylation, thrombopoietin signaling, and myeloid or megakaryocyte differentiation. Its bone-marrow tissue enhancement and lung detection are relevant to interpreting the shared tissue signal, while its substantial literature and disease associations make it a strong biological anchor.
- **Conclusion**: Established evidence supports RBM15 as a plausible RNA-processing and regulatory hub with hematopoietic relevance. The module supports a hypothesis that RBM15 helps coordinate the shared RNA-centered state, but co-abundance does not establish that it regulates the other module genes in these tissues.

#### FAM120A

- **Related proteins** (co-abundance neighbors): PRRC2B (0.89), RBM15 (0.86), RRP1 (0.85), EPS15L1 (0.84), YLPM1 (0.83), SNW1 (0.82), BCLAF1 (0.81), CTTN (0.81), UPF1 (0.81); STRING partners: UPF1 (0.741)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_05807.1
- **Function (MyGene.info)**: family with sequence similarity 120 member A. Enables RNA binding activity. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.325); major depressive disorder (0.304); neurodegenerative disease (0.273); neurotic disorder (0.216); irritable bowel syndrome (0.214)
- **Europe PMC papers**: 467
- **Why important**: FAM120A has a central network position and connects RBM15, RRP1, EPS15L1, YLPM1, SNW1, BCLAF1, CTTN, and PRRC2B. It has RNA-binding and RNA-splicing annotations, a stress-related inflammasome annotation, and direct STRING and hu.MAP support through UPF1 and complexes (hu.MAP huMAP3_10625.1) and (hu.MAP huMAP3_05807.1). It is broadly expressed and detected in lung, making it a useful bridge between the core RNA signal and tissue context.
- **Conclusion**: Established evidence supports FAM120A as an RNA-associated cytosolic connector with links to translation or stress biology. Its position makes it a strong candidate mediator of the module, but the proposed bridge between cytosolic stress handling and nuclear RNA processing remains a hypothesis.

#### SNW1

- **Related proteins** (co-abundance neighbors): PRRC2C (0.92), UPF1 (0.85), YLPM1 (0.85), RBM15 (0.85), BCLAF1 (0.85), RRP1 (0.83), FAM120A (0.82), EPS15L1 (0.81); STRING partners: BCLAF1 (0.823)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SNW domain containing 1. This gene, a member of the SNW gene family, encodes a coactivator that enhances transcription from some Pol II promoters. This coactivator can bind to the ligand-binding domain of the vitamin D receptor and to retinoid receptors to enhance vitamin D-, retinoic acid-, estrogen-, and glucocorticoid-mediated gene expression. It can also function as a splicing factor by interacting with poly(A)-bindin…
- **Diseases (Open Targets)**: cancer (0.580); dengue disease (0.370); neurodegenerative disease (0.261); congenital lactic acidosis, Saguenay-Lac-Saint-Jean type (0.118); chondromalacia (0.052)
- **Europe PMC papers**: 653
- **Why important**: SNW1 is among the more connected genes and links PRRC2C, UPF1, YLPM1, RBM15, BCLAF1, RRP1, FAM120A, and EPS15L1. Its established functions include transcriptional coactivation, mRNA splicing, vitamin or steroid receptor coactivation, and regulation of DNA-damage-related apoptosis. Its STRING relationship with BCLAF1 (STRING Keyword Nucleus; within-query FDR = 0.0443) and lung protein detection support a real nuclear regulatory component rather than an isolated annotation.
- **Conclusion**: Established evidence supports SNW1 as a transcriptional and splicing regulator that can connect RNA processing to signaling. In this module it is a plausible coordinator, but there is no direct evidence here that it drives autonomic-lung co-abundance.

#### RRP1

- **Related proteins** (co-abundance neighbors): KDM3B (0.89), RAP1GDS1 (0.87), FAM120A (0.85), SNW1 (0.83), CIAO1 (0.82); STRING partners: NOP2 (0.908), PPAN (0.895)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Mitotic chromosome; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal RNA processing 1. The protein encoded by this gene is the putative homolog of the yeast ribosomal RNA processing protein RRP1. The encoded protein is involved in the late stages of nucleologenesis at the end of mitosis, and may be required for the generation of 28S rRNA. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.494); breast ductal adenocarcinoma (0.111); malignant hyperthermia of anesthesia (0.055); familial cold autoinflammatory syndrome (0.053); familial cold autoinflammatory syndrome 4 (0.053)
- **Europe PMC papers**: 540
- **Why important**: RRP1 connects the RNA-associated core to KDM3B, RAP1GDS1, FAM120A, and SNW1, and has strong STRING relationships with NOP2 and PPAN. Its established function is late nucleologenesis and maturation of ribosomal RNA, with nucleolar and mitotic-chromosome localization. The combination of network placement, nucleolar biology, and literature support makes it an important link between RNA processing and ribosome production.
- **Conclusion**: Established evidence supports RRP1 as a nucleolar ribosome-biogenesis component. Its co-abundance with the RNA-regulatory core suggests a coordinated cellular biosynthetic state, but it does not prove a direct physical complex spanning the whole module.

#### TP53BP1

- **Related proteins** (co-abundance neighbors): RSF1 (0.84), RBM15 (0.80); STRING partners: RB1 (0.928)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_12566.1
- **Function (MyGene.info)**: tumor protein p53 binding protein 1. This gene encodes a protein that functions in the DNA double-strand break repair pathway choice, promoting non-homologous end joining (NHEJ) pathways, and limiting homologous recombination. This protein plays multiple roles in the DNA damage response, including promoting checkpoint signaling following DNA damage, acting as a scaffold for recruitment of DNA damage response proteins to damaged chrom…
- **Diseases (Open Targets)**: neurodegenerative disease (0.367); microcephaly and chorioretinopathy 3 (0.353); alcohol drinking (0.269); urolithiasis (0.269); microcephaly and chorioretinopathy 1 (0.266)
- **Europe PMC papers**: 2200
- **Why important**: TP53BP1 links RBM15 and RSF1 in the module and has a high-confidence STRING relationship with RB1. It is an established DNA double-strand-break response scaffold that promotes non-homologous end joining, checkpoint signaling, and repair-pathway choice. It also has hu.MAP support with ZMYM2 in (hu.MAP huMAP3_12566.1), and its extensive literature and disease associations make it a strong indicator that genome maintenance is part of the module's possible cellular state.
- **Conclusion**: Established evidence supports TP53BP1 as a DNA-damage and chromatin-linked regulator. Its presence supports a genome-maintenance interpretation, but the module does not demonstrate that DNA damage caused the observed co-abundance pattern.

#### DOCK7

- **Related proteins** (co-abundance neighbors): EPS15L1 (0.88), ZMYM2 (0.86), OSBPL8 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dedicator of cytokinesis 7. The protein encoded by this gene is a guanine nucleotide exchange factor (GEF) that plays a role in axon formation and neuronal polarization. The encoded protein displays GEF activity toward RAC1 and RAC3 Rho small GTPases but not toward CDC42. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2012].
- **Diseases (Open Targets)**: genetic developmental and epileptic encephalopathy (0.766); familial hypobetalipoproteinemia 2 (0.533); hereditary disease (0.488); metabolic syndrome (0.373); infantile epileptic encephalopathy (0.372)
- **Europe PMC papers**: 822
- **Why important**: DOCK7 provides a biologically distinctive connection to the autonomic-neural context: it is an established RAC1 and RAC3 guanine-nucleotide exchange factor involved in axon formation, neuronal polarization, microtubule organization, and axonogenesis. It connects EPS15L1, ZMYM2, and OSBPL8, and HPA shows enrichment in astrocytes and ependymal cells as well as an immune-cell-enhanced signal in myeloid dendritic cells. Its disease associations include developmental epileptic encephalopathy, giving it substantial functional and clinical relevance despite its peripheral network position.
- **Conclusion**: Established evidence supports DOCK7 as a neuronal-polarity and cytoskeletal regulator. In this module it may mark a neural or cell-structure context that accompanies the RNA-centered program, but it is not evidence that the entire module is neuron-specific.

## Module 14

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (29)**: CCAR1, DCUN1D1, DDX42, DDX5, EIF3L, G6PD, GMPS, HNRNPF, HSPH1, EIF4G1, EIF6, IMPDH2, MESD, NOL6, NUP43, NUP62, OLA1, PCNA, PSMC6, PSMC4, SMARCA4, SPR, AARS1, KARS1, RARS1, TARS1, TIAL1, SNRNP200, UBQLN2

### Function

The module is best interpreted as a conserved intracellular gene-expression and proteostasis program, centered on nucleotide-dependent cellular activity. The primary evidence is the coherent enrichment of adenyl nucleotide binding, nucleotide binding, ATP binding, adenyl ribonucleotide binding, and nucleoside phosphate binding (5 globally significant GO/KEGG terms, q_global 0.00798–0.0476; see the table). These terms are driven by aminoacyl-tRNA synthetases, RNA helicases, translation factors, proteasome ATPases, chromatin-remodeling machinery, and nucleotide-biosynthesis enzymes. Accordingly, the module most plausibly reflects coordinated capacity for protein synthesis, RNA processing, chromatin regulation, protein quality control, and nucleotide metabolism rather than a tissue-specific autonomic or pulmonary signaling pathway. STRING supplementary annotations support lung and respiratory-system representation (STRING TISSUES Lung; within-query FDR = 0.0025) (STRING TISSUES Respiratory system; within-query FDR = 0.003), protein biosynthesis (STRING Keyword Protein biosynthesis; within-query FDR = 0.0088), and nucleotide or ATP binding (STRING Keyword ATP-binding; within-query FDR = 0.0234), (STRING Function Nucleotide binding; within-query FDR = 0.0446) (STRING Function ATP binding; within-query FDR = 0.0446), but these are not independent globally corrected GO evidence. The absence of a more specific biological-process term does not invalidate the module.

**Cell composition.** The module is overwhelmingly composed of intracellular, broadly expressed proteins. HPA reports low tissue specificity for most genes and low immune-cell specificity for nearly all genes, arguing against a module dominated by plasma proteins, secreted proteins, or a particular blood-cell population. Only a small minority are annotated as secreted, while the listed proteins are mainly cytosolic, nucleoplasmic, nucleolar, or proteasomal. Protein detection in lung is widespread among the tested genes, whereas there is no matching HPA tissue for autonomic nervous system. Cell-type-enhanced annotations involving spermatids, epithelial cells, and other proliferative or specialized cells should therefore be treated cautiously: they may reflect shared housekeeping, translation, RNA-processing, or cell-state programs rather than a specific contaminating cell type. The blood-cell evidence does not support a predominantly blood-derived explanation.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF adenyl nucleotide binding | 0.00798 | AARS1, DDX42, DDX5, EIF4G1, G6PD, GMPS, HSPH1, KARS1, OLA1, PSMC4, PSMC6, RARS1, SMARCA4, SNRNP200, SPR, TARS1 |
| GO:MF nucleotide binding | 0.0407 | AARS1, DDX42, DDX5, EIF4G1, G6PD, GMPS, HSPH1, IMPDH2, KARS1, OLA1, PSMC4, PSMC6, RARS1, SMARCA4, SNRNP200, SPR, TARS1 |
| GO:MF ATP binding | 0.0446 | AARS1, DDX42, DDX5, EIF4G1, GMPS, HSPH1, KARS1, OLA1, PSMC4, PSMC6, RARS1, SMARCA4, SNRNP200, TARS1 |
| GO:MF adenyl ribonucleotide binding | 0.046 | AARS1, DDX42, DDX5, EIF4G1, GMPS, HSPH1, KARS1, OLA1, PSMC4, PSMC6, RARS1, SMARCA4, SNRNP200, TARS1 |
| GO:MF nucleoside phosphate binding | 0.0476 | AARS1, DDX42, DDX5, EIF4G1, G6PD, GMPS, HSPH1, IMPDH2, KARS1, OLA1, PSMC4, PSMC6, RARS1, SMARCA4, SNRNP200, SPR, TARS1 |

### STRING and hu.MAP

STRING confirms several established relationships within the module. The aminoacyl-tRNA synthetase group AARS1, KARS1, RARS1, and TARS1 is strongly connected, as are GMPS with IMPDH2, EIF3L with EIF4G1, EIF4G1 with EIF6 and TIAL1, PSMC4 with PSMC6, NUP43 with NUP62, and DDX5 with CCAR1, HNRNPF, and SMARCA4. These links show that part of the co-abundance structure recapitulates known translation, nucleotide metabolism, proteasome, nuclear-pore, and RNA-regulatory relationships. hu.MAP independently supports membership of the aminoacyl-tRNA synthetases in a shared complex (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), translation-initiation components in EIF3-related complexes (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1), proteasome ATPases in proteasome assemblies (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1), nucleoporins in a nuclear-pore complex (hu.MAP huMAP3_12581.1), and spliceosome-associated proteins in (hu.MAP huMAP3_08980.1). Thus, the module is not merely a collection of unrelated genes; it contains several recognizable molecular subassemblies. At the same time, many module edges lack STRING or hu.MAP support, so the co-abundance network should not be equated with a single physical complex.

**STRING interactions (score >= 0.7)**: 19 of 406 gene pairs: AARS1–KARS1 (0.992); AARS1–RARS1 (0.85); AARS1–TARS1 (0.929); CCAR1–DDX5 (0.836); DDX5–HNRNPF (0.807); DDX5–SMARCA4 (0.782); EIF3L–EIF4G1 (0.924); EIF4G1–EIF6 (0.775); EIF4G1–TIAL1 (0.905); GMPS–IMPDH2 (0.998); GMPS–KARS1 (0.835); GMPS–RARS1 (0.872); HNRNPF–TIAL1 (0.774); KARS1–RARS1 (0.999); KARS1–TARS1 (0.838); NUP43–NUP62 (0.984); OLA1–RARS1 (0.747); PSMC4–PSMC6 (0.999); RARS1–TARS1 (0.806)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Lung (FDR = 0.0025, 15 genes); TISSUES Respiratory system (FDR = 0.003, 16 genes); Keyword Protein biosynthesis (FDR = 0.0088, 7 genes); TISSUES Organism form (FDR = 0.0172, 18 genes); Keyword Acetylation (FDR = 0.0234, 25 genes); Keyword ATP-binding (FDR = 0.0234, 13 genes); Keyword RNA-binding (FDR = 0.0234, 10 genes); TISSUES Embryonic structure (FDR = 0.0323, 17 genes); Function Nucleotide binding (FDR = 0.0446, 17 genes); Function ATP binding (FDR = 0.0446, 14 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (TARS1, RARS1, KARS1; 3/14); huMAP3_13688.1 (TARS1, RARS1, KARS1; 3/14); huMAP3_14442.1 (AARS1, GMPS, OLA1; 3/57); huMAP3_13175.1 (EIF4G1, EIF3L; 2/20); huMAP3_11246.1 (EIF4G1, EIF3L; 2/24); huMAP3_05064.1 (PSMC4, PSMC6; 2/31); huMAP3_12581.1 (NUP62, NUP43; 2/58); huMAP3_09656.1 (PSMC4, PSMC6; 2/64); huMAP3_13725.1 (PSMC4, PSMC6; 2/69); huMAP3_08980.1 (SNRNP200, DDX42; 2/97)

### Novelty

The molecular components are not individually novel: many relationships are already represented in STRING and hu.MAP, and the functions of the principal genes are well established. The potentially new observation is the coordinated co-abundance of these otherwise distinct translation, RNA-processing, proteasome, nucleotide, chromatin, and nuclear-transport components across autonomic nervous system and lung. However, the fact sheet does not establish that this tissue-pair module has never been reported elsewhere. Absence of some edges from STRING or hu.MAP cannot prove novelty, because those resources emphasize physical or curated relationships rather than tissue-specific co-abundance. The defensible conclusion is that the module represents a potentially novel cross-tissue association built from largely established cellular machinery; confirmation would require comparison with independent cohorts, other tissue pairs, and published co-expression resources.

**Hypothesis.** Hypothesis: autonomic nervous system and lung share a cellular-state program in which high translational demand and RNA processing are coupled to nucleotide supply, proteasomal quality control, chromatin regulation, and nuclear-cytoplasmic transport. The aminoacyl-tRNA synthetase and translation-initiation components could support protein production, IMPDH2 and GMPS could maintain guanine-nucleotide availability, PSMC4 and PSMC6 could support removal of damaged or misfolded proteins, and DDX5, SNRNP200, and SMARCA4 could coordinate RNA processing and transcriptional adaptation. This is a mechanistic model rather than proof of direct physical cooperation; the co-abundance data alone cannot determine directionality, cell type, or causal regulation.

### Important genes

#### AARS1

- **Related proteins** (co-abundance neighbors): KARS1 (0.88), SNRNP200 (0.87), RARS1 (0.86), IMPDH2 (0.85), PSMC4 (0.85), OLA1 (0.85), EIF3L (0.84), SPR (0.81), EIF6 (0.81), HSPH1 (0.81), TARS1 (0.80), MESD (0.80), SMARCA4 (0.80); STRING partners: KARS1 (0.992), RARS1 (0.85), TARS1 (0.929)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: alanyl-tRNA synthetase 1. The human alanyl-tRNA synthetase (AARS) belongs to a family of tRNA synthases, of the class II enzymes.  Class II tRNA synthases evolved early in evolution and are highly conserved. This is reflected by the fact that 498 of the 968-residue polypeptide human AARS shares 41% identity witht the E.coli protein.  tRNA synthases are the enzymes that interpret the RNA code and attach specific aminoacids …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2N (0.762); developmental and epileptic encephalopathy, 29 (0.747); undetermined early-onset epileptic encephalopathy (0.678); trichothiodystrophy 8, nonphotosensitive (0.568); Charcot-Marie-Tooth disease type 2 (0.566)
- **Europe PMC papers**: 672
- **Why important**: AARS1 has the strongest network position in the supplied ranking and connects the aminoacyl-tRNA synthetase group with RNA-processing, proteasome, nucleotide, and translation-related neighbors. It is present in every primary globally corrected GO term (5 globally significant GO/KEGG terms, q_global 0.00798–0.0476; see the table), belongs to a hu.MAP complex with GMPS and OLA1 (hu.MAP huMAP3_14442.1), and has established roles in tRNA aminoacylation. Its disease associations include axonal Charcot-Marie-Tooth disease and developmental epileptic encephalopathy, with substantial literature support.
- **Conclusion**: Established: AARS1 is a broadly expressed cytosolic aminoacyl-tRNA synthetase and a central statistical hub of this module. Hypothesis: it may mark a shared translational-demand axis linking the two tissues, but the network does not show that AARS1 drives the module.

#### KARS1

- **Related proteins** (co-abundance neighbors): AARS1 (0.88), EIF6 (0.85), EIF3L (0.83), SNRNP200 (0.83), HNRNPF (0.83), PSMC4 (0.83), OLA1 (0.80); STRING partners: AARS1 (0.992), GMPS (0.835), RARS1 (0.999), TARS1 (0.838)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: lysyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. Lysyl-tRNA synthetase is a homodimer localized to the cytoplasm which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Alternatively spliced transcript variants encoding different…
- **Diseases (Open Targets)**: leukoencephalopathy, progressive, infantile-onset, with or without deafness (0.753); deafness, congenital, and adult-onset progressive leukoencephalopathy (0.714); autosomal recessive nonsyndromic hearing loss 89 (0.685); Charcot-Marie-Tooth disease recessive intermediate B (0.670); deafness (0.534)
- **Europe PMC papers**: 232
- **Why important**: KARS1 links AARS1, RARS1, TARS1, GMPS, EIF6, EIF3L, and other module members, while participating in the aminoacyl-tRNA synthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). It contributes to all primary GO terms (5 globally significant GO/KEGG terms, q_global 0.00798–0.0476; see the table) and has established functions in lysine charging of tRNA and translation. Its disease associations include progressive leukoencephalopathy and hearing loss, providing a clinically informative translation-related anchor.
- **Conclusion**: Established: KARS1 is a core translation-supporting enzyme with direct network and complex support. Hypothesis: coordinated KARS1 abundance may reflect a shared requirement for protein synthesis or stress adaptation in autonomic and pulmonary cells.

#### SMARCA4

- **Related proteins** (co-abundance neighbors): NUP43 (0.91), NUP62 (0.86), SNRNP200 (0.83), CCAR1 (0.81), AARS1 (0.80); STRING partners: DDX5 (0.782)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center, Nucleoli rim; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SWI/SNF related BAF chromatin remodeling complex subunit ATPase 4. The protein encoded by this gene is a member of the SWI/SNF family of proteins and is similar to the brahma protein of Drosophila. Members of this family have helicase and ATPase activities and are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI, wh…
- **Diseases (Open Targets)**: intellectual disability, autosomal dominant 16 (0.796); rhabdoid tumor predisposition syndrome 2 (0.788); familial rhabdoid tumor (0.685); rhabdoid tumor (0.627); medulloblastoma (0.586)
- **Europe PMC papers**: 9906
- **Why important**: SMARCA4 connects the module to chromatin remodeling and transcriptional regulation, and its network neighbors include NUP43, NUP62, SNRNP200, CCAR1, and AARS1. It appears in every primary GO term (5 globally significant GO/KEGG terms, q_global 0.00798–0.0476; see the table) and has strong STRING support for lung and respiratory-system representation (STRING TISSUES Lung; within-query FDR = 0.0025) (STRING TISSUES Respiratory system; within-query FDR = 0.003). Its SWI/SNF ATPase function and extensive literature connect it to transcriptional control, neural development, intellectual disability, and rhabdoid tumor predisposition.
- **Conclusion**: Established: SMARCA4 supplies a plausible regulatory and chromatin-remodeling component within an otherwise strongly translational module. Hypothesis: it could help couple cellular state or stress to the transcriptional program represented by the module, although direct coupling is not demonstrated.

#### EIF4G1

- **Related proteins** (co-abundance neighbors): HSPH1 (0.85), PCNA (0.81), DCUN1D1 (0.81); STRING partners: EIF3L (0.924), EIF6 (0.775), TIAL1 (0.905)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_13175.1, huMAP3_11246.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 is a translation-initiation scaffold connected to HSPH1, PCNA, DCUN1D1, EIF3L, EIF6, and TIAL1. It participates in hu.MAP translation-initiation complexes (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1), is present in every primary GO term (5 globally significant GO/KEGG terms, q_global 0.00798–0.0476; see the table), and is supported by STRING annotations for lung, respiratory system, protein biosynthesis, and RNA binding (STRING TISSUES Lung; within-query FDR = 0.0025) (STRING TISSUES Respiratory system; within-query FDR = 0.003) (STRING Keyword Protein biosynthesis; within-query FDR = 0.0088), (STRING Keyword RNA-binding; within-query FDR = 0.0234). Its established role in cap-dependent translation and associations with Parkinson disease and neurodegenerative disease make it relevant to both tissue context and disease biology.
- **Conclusion**: Established: EIF4G1 is a major translational-initiation scaffold and a bridge between translation and RNA-regulatory members. Hypothesis: it may be a functional bottleneck through which shared cellular demand is reflected in co-abundance, but causality is untested.

#### PSMC4

- **Related proteins** (co-abundance neighbors): PSMC6 (0.89), AARS1 (0.85), KARS1 (0.83), NUP43 (0.82); STRING partners: PSMC6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 4. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.603); mantle cell lymphoma (0.542); neoplasm (0.519); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1065
- **Why important**: PSMC4 is linked to PSMC6 and to translation-related module hubs, and both proteins are represented in multiple hu.MAP proteasome assemblies (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). PSMC4 appears in every primary GO term (5 globally significant GO/KEGG terms, q_global 0.00798–0.0476; see the table) and in the STRING lung and respiratory-system annotations (STRING TISSUES Lung; within-query FDR = 0.0025) (STRING TISSUES Respiratory system; within-query FDR = 0.003). Its established role as a proteasome regulatory ATPase connects the module to ubiquitin-dependent protein degradation, oxidative stress responses, and proteostasis. It also has disease associations involving plasma-cell myeloma, mantle-cell lymphoma, neoplasia, HIV infection, and amyloidosis.
- **Conclusion**: Established: PSMC4 provides strong physical-complex support for a proteostasis branch of the module. Hypothesis: proteasome activity may be coordinated with translation to manage protein-folding or stress burden in both tissues.

#### DDX5

- **Related proteins** (co-abundance neighbors): PCNA (0.86), EIF3L (0.84), NOL6 (0.83); STRING partners: CCAR1 (0.836), HNRNPF (0.807), SMARCA4 (0.782)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 connects PCNA, EIF3L, and NOL6 in the module and has STRING relationships with CCAR1, HNRNPF, and SMARCA4. It is present in every primary GO term (5 globally significant GO/KEGG terms, q_global 0.00798–0.0476; see the table) and in the STRING lung and respiratory system annotations (STRING TISSUES Lung; within-query FDR = 0.0025) (STRING TISSUES Respiratory system; within-query FDR = 0.003), as well as RNA-binding and ATP-binding annotations (STRING Keyword ATP-binding; within-query FDR = 0.0234) (STRING Keyword RNA-binding; within-query FDR = 0.0234). Its established DEAD-box helicase functions include RNA-structure remodeling, splicing, transcriptional coregulation, and small noncoding RNA processing. Its literature includes cancer, viral disease, and other disease contexts.
- **Conclusion**: Established: DDX5 is a multifunctional RNA-regulatory hub that bridges the translational and nuclear branches of the module. Hypothesis: it may coordinate RNA processing with changes in translation or cellular proliferation, but the shared tissue module does not identify its regulatory direction.

## Module 15

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (6)**: CENPF, DDX20, DIAPH1, RPAP1, RPAP3, TOR1AIP2

### Function

No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The most defensible interpretation is a mixed cellular-state module rather than a single established biological pathway. TOR1AIP2 is the network hub and connects the RNA-polymerase-associated genes RPAP1 and RPAP3 with DIAPH1 and CENPF. RPAP1 and RPAP3 support an RNA-polymerase-associated transcriptional and protein-stabilization interpretation, DDX20 supports RNA processing and transcriptional regulation, DIAPH1 supports actin and cytoskeletal organization, and CENPF supports mitotic and chromosome-segregation biology. These signals are compatible with coordination of transcription, RNA handling, cytoskeletal organization, and proliferative state, but the absence of a globally corrected term means this integrated function remains interpretive rather than demonstrated enrichment.

**Cell composition.** The module is not composed of secreted or plasma proteins, and the HPA summary does not indicate broad immune-cell specificity. Most genes have low tissue specificity, while selected genes show enrichment in testis, bone marrow, lymphoid tissue, or progenitor and differentiating cell types. CENPF is associated with progenitor and proliferative cell types, DDX20 with germ-cell populations, and DIAPH1 with neutrophil and platelet-related cell types. This pattern is more consistent with a mixture of broadly expressed intracellular proteins plus cell-state or tissue-composition effects than with a dedicated lung or autonomic-nervous-system program. Lung protein detection is present for some module members, but the autonomic-nervous-system protein comparison is unavailable. The module therefore could partly reflect shared cellular composition or proliferation-related variation in the sampled tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence known interaction, between RPAP1 and RPAP3. This supports a real molecular connection within the module but does not establish the entire co-abundance subgraph as a physical complex. hu.MAP independently places RPAP1 and RPAP3 together in the complexes (hu.MAP huMAP3_09057.1), (hu.MAP huMAP3_08487.1), (hu.MAP huMAP3_06426.1), (hu.MAP huMAP3_14318.1), and (hu.MAP huMAP3_11092.1), each of which contains many additional transcriptional, RNA-polymerase-associated, and regulatory proteins. No other module gene has a reported STRING interaction or hu.MAP complex membership in the supplied evidence. Thus, the strongest known core is RPAP1–RPAP3, while the links involving TOR1AIP2, DIAPH1, CENPF, and DDX20 are co-abundance relationships whose molecular mechanisms remain unresolved.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: RPAP1–RPAP3 (0.931)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09057.1 (RPAP1, RPAP3; 2/36); huMAP3_08487.1 (RPAP1, RPAP3; 2/37); huMAP3_06426.1 (RPAP1, RPAP3; 2/38); huMAP3_14318.1 (RPAP1, RPAP3; 2/58); huMAP3_11092.1 (RPAP1, RPAP3; 2/65)

### Novelty

The cross-tissue co-abundance pattern may be a new systems-level observation, especially because the module links a TOR1AIP2-centered network with the known RPAP1–RPAP3 association and with cytoskeletal and cell-cycle genes. However, it cannot be called a wholly new molecular discovery: the RPAP1–RPAP3 relationship is already represented in STRING, and their shared participation in hu.MAP complexes is established in (hu.MAP huMAP3_09057.1), (hu.MAP huMAP3_08487.1), (hu.MAP huMAP3_06426.1), (hu.MAP huMAP3_14318.1), and (hu.MAP huMAP3_11092.1). The absence of database relationships for the remaining edges does not prove novelty. A defensible claim is therefore novelty of the tissue-pair co-abundance configuration or its biological context, pending validation in independent cohorts and direct molecular assays.

**Hypothesis.** Hypothesis: variation in an intracellular structural and transcriptional state may couple the ER and nuclear-envelope-associated role of TOR1AIP2 to RNA-polymerase-associated regulation through RPAP1 and RPAP3, while simultaneously tracking cytoskeletal remodeling through DIAPH1 and proliferative or chromosome-segregation state through CENPF. DDX20 may contribute RNA-processing regulation to this state. The apparent conservation across autonomic nervous system and lung could therefore reflect a shared cellular program or shared cell-state composition rather than a tissue-specific pathway. This hypothesis should be tested by replication, cell-composition adjustment, perturbation of TOR1AIP2 or the RPAP pair, and measurement of transcriptional, cytoskeletal, and cell-cycle consequences.

### Important genes

#### TOR1AIP2

- **Related proteins** (co-abundance neighbors): DIAPH1 (0.83), RPAP3 (0.82), CENPF (0.82), RPAP1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: torsin 1A interacting protein 2. One of the two protein isoforms encoded by this gene is a type II integral membrane protein found in the endoplasmic reticulum (ER). The encoded protein is a cofactor for the ATPase TorsinA, regulating the amount of TorsinA present in the ER compared to that found in the nuclear envelope. Defects in this protein are a cause of early onset primary dystonia, a neuromuscular disease. The other isofor…
- **Diseases (Open Targets)**: autosomal recessive limb-girdle muscular dystrophy type 2Y (0.535); centronuclear myopathy (0.340); hereditary disease (0.192); aneurysm (0.142); Abnormality of refraction (0.142)
- **Europe PMC papers**: 210
- **Why important**: TOR1AIP2 is the central network hub, connecting RPAP1, RPAP3, DIAPH1, and CENPF. Its annotated ER and nuclear-envelope-related functions provide a plausible structural link between the otherwise mixed transcriptional, cytoskeletal, and cell-state signals. It is associated with early-onset primary dystonia and additional neuromuscular and structural disease annotations, and it has a substantial literature base relative to the other less characterized module components.
- **Conclusion**: Established evidence supports TOR1AIP2 as the topological organizer of the module and as a regulator of TorsinA-related ER biology. It is plausible, but not established, that TOR1AIP2 coordinates the other module signals or explains conservation between the tissues.

#### RPAP3

- **Related proteins** (co-abundance neighbors): TOR1AIP2 (0.82), DDX20 (0.81); STRING partners: RPAP1 (0.931)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_09057.1, huMAP3_08487.1, huMAP3_06426.1, huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase II associated protein 3. This gene encodes an RNA polymerase II-associated protein. The encoded protein may function in transcriptional regulation and may also regulate apoptosis. Alternatively spliced transcript variants have been described. [provided by RefSeq, Mar 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.418); cardiovascular disorder (0.255); spermatocele (0.204); lysosomal storage disease (0.115); alcohol drinking (0.094)
- **Europe PMC papers**: 334
- **Why important**: RPAP3 has a direct high-confidence STRING relationship with RPAP1 and is present with RPAP1 in every reported hu.MAP complex (hu.MAP huMAP3_09057.1), (hu.MAP huMAP3_08487.1), (hu.MAP huMAP3_06426.1), (hu.MAP huMAP3_14318.1), and (hu.MAP huMAP3_11092.1). It connects TOR1AIP2 to DDX20 in the co-abundance network and is annotated as an RNA-polymerase-associated protein involved in transcriptional regulation and protein stabilization. Its disease associations include neurodegenerative and cardiovascular disorders, and it has a well-developed literature base within this module.
- **Conclusion**: Established evidence supports RPAP3 as part of a known RNA-polymerase-associated molecular neighborhood and as a bridge between the known RPAP pair and the rest of the module. Its role as the functional mediator of the cross-tissue co-abundance pattern remains a hypothesis.

#### RPAP1

- **Related proteins** (co-abundance neighbors): TOR1AIP2 (0.82); STRING partners: RPAP3 (0.931)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_09057.1, huMAP3_08487.1, huMAP3_06426.1, huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase II associated protein 1. This protein forms part of the RNA polymerase II (RNAPII) enzyme complex and may recruit RNAPII to chromatin through its interaction with acetylated histones. [provided by RefSeq, Jul 2012].
- **Diseases (Open Targets)**: neurodegenerative disease (0.523); type 2 diabetes mellitus (0.345); diabetes mellitus (0.227); Crohn disease (0.181); cardiac arrhythmia (0.157)
- **Europe PMC papers**: 268
- **Why important**: RPAP1 is the partner of RPAP3 in STRING and in all listed hu.MAP complexes (hu.MAP huMAP3_09057.1), (hu.MAP huMAP3_08487.1), (hu.MAP huMAP3_06426.1), (hu.MAP huMAP3_14318.1), and (hu.MAP huMAP3_11092.1). Its annotation places it in the RNA polymerase complex and links it to recruitment of that machinery to chromatin. It also has disease associations involving neurodegenerative, metabolic, gastrointestinal, and cardiac phenotypes, giving it biological relevance beyond the network edge itself.
- **Conclusion**: Established evidence supports RPAP1 as a component of a known transcription-associated complex and as a robustly supported core member of the module. It is not established that altered RPAP1 abundance drives the module or a tissue-specific phenotype.

#### DIAPH1

- **Related proteins** (co-abundance neighbors): TOR1AIP2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: diaphanous related formin 1. This gene is a homolog of the Drosophila diaphanous gene, and has been linked to autosomal dominant, fully penetrant, nonsyndromic sensorineural progressive low-frequency hearing loss. Actin polymerization involves proteins known to interact with diaphanous protein in Drosophila and mouse. It has therefore been speculated that this gene may have a role in the regulation of actin polymerization in …
- **Diseases (Open Targets)**: progressive microcephaly-seizures-cortical blindness-developmental delay syndrome (0.771); autosomal dominant nonsyndromic hearing loss 1 (0.755); DIAPH1-related sensorineural hearing loss-thrombocytopenia syndrome (0.462); deafness (0.458); Global developmental delay (0.435)
- **Europe PMC papers**: 2166
- **Why important**: DIAPH1 is directly connected to the hub TOR1AIP2 and contributes a distinct cytoskeletal arm to the module. Its annotations support actin polymerization, cytoskeleton organization, brain development, neuron projection development, and sensory function. It has extensive literature and disease associations including hearing loss, thrombocytopenia-related disease, microcephaly, seizures, cortical blindness, and developmental delay. Its HPA cell-type pattern includes neutrophils and platelets, which also makes it important for assessing cellular-composition confounding.
- **Conclusion**: Established evidence supports DIAPH1 as an actin-regulatory and disease-relevant gene with a plausible connection to structural remodeling. Its co-abundance with the RPAP genes may represent coordinated cellular state, indirect regulation, or composition effects; a direct mechanistic link is not established.

#### CENPF

- **Related proteins** (co-abundance neighbors): TOR1AIP2 (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: centromere protein F. This gene encodes a protein that associates with the centromere-kinetochore complex. The protein is a component of the nuclear matrix during the G2 phase of interphase. In late G2 the protein associates with the kinetochore and maintains this association through early anaphase. It localizes to the spindle midzone and the intracellular bridge in late anaphase and telophase, respectively, and is tho…
- **Diseases (Open Targets)**: Stromme syndrome (0.818); female infertility (0.461); Neurodevelopmental delay (0.425); neurodegenerative disease (0.390); microcephalic primordial dwarfism (0.370)
- **Europe PMC papers**: 4616
- **Why important**: CENPF connects to the TOR1AIP2 hub and contributes a strong cell-cycle and chromosome-segregation interpretation. Its annotations include the mitotic cell cycle, chromosome segregation, spindle-checkpoint signaling, and regulation of the G2/M transition. HPA associates it with bone marrow, lymphoid tissue, testis, and multiple progenitor or differentiating cell types. It has the largest literature volume among the module genes and disease associations including Stromme syndrome, infertility, neurodevelopmental delay, and primordial dwarfism.
- **Conclusion**: Established evidence supports CENPF as a marker and regulator of proliferative and mitotic cell states. Its presence may indicate cell-cycle composition or activity rather than a specialized autonomic-nervous-system or lung function, so its role in the module is most cautiously interpreted as a state-related component.

## Module 16

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (5)**: CLASP1, EIF4G3, LBR, PDXDC1, RNF214

### Function

The module does not support a specific pathway-level functional assignment from GO or KEGG: no GO or KEGG term passed global correction, and there are no supplementary STRING enrichment terms. Its internal structure is more consistent with a weakly connected set of cellular genes than with a coherent canonical pathway. The annotated functions span microtubule organization and stabilization through CLASP1, translation initiation through EIF4G3, nuclear-envelope and sterol-related biology through LBR, predicted ubiquitin transfer through RNF214, and Golgi-associated cadherin-binding or carboxylic-acid biology through PDXDC1. These annotations support a cautious interpretation involving general cellular organization, gene-expression control, and intracellular trafficking, rather than a single established biological process.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. All genes have low tissue specificity, and protein detection in lung is present for most members, whereas the autonomic-nervous-system tissue lacks a matching HPA entry. Several genes show cell-type-associated patterns involving neutrophils or neutrophil progenitors, and other signals involve epithelial, neuronal, muscle, or erythroid-lineage populations. Two genes have immune-cell-enhanced annotations, although the overall immune-cell specificity is mostly low. Thus, the shared signal could reflect broadly expressed intracellular proteins, shared cellular admixture, or blood and immune-cell representation in the sampled tissues; it should not be interpreted as evidence for a tissue-specific secreted program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and no hu.MAP complex contains multiple module members. Therefore, the observed co-abundance edges are not corroborated by the supplied catalogues of known physical or functional associations. This does not disprove biological coordination: co-abundance can arise from shared cell composition, coordinated regulation, indirect physiology, or technical structure. It does mean that the module currently lacks external interaction or complex support and should be treated as exploratory.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be novel as a co-abundance observation, but novelty is not established. Its lack of STRING and hu.MAP support shows that the particular set and its observed co-abundance pattern are not represented in the supplied high-confidence interaction or complex evidence; absence from those resources alone cannot demonstrate a new biological mechanism. The genes themselves are not uniformly uncharacterized: CLASP1, EIF4G3, and LBR have substantial literature and established cellular functions, while RNF214 and PDXDC1 have more limited or predictive annotation. A convincing novelty claim would require replication in independent cohorts, control for cell-type composition and tissue effects, comparison with published co-expression resources, and experimental testing of any proposed mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of broadly expressed intracellular proteins in a shared lung-associated cellular context, potentially influenced by immune or granulocyte admixture, rather than a single molecular complex. Within that context, translation control through EIF4G3, cytoskeletal organization through CLASP1, nuclear-envelope and sterol-linked biology through LBR, and Golgi or protein-turnover processes through PDXDC1 and RNF214 may vary together as part of cellular state. This is a hypothesis only; the absence of globally significant GO or KEGG enrichment and the lack of STRING or hu.MAP support prevent treating it as an established mechanism.

### Important genes

#### CLASP1

- **Related proteins** (co-abundance neighbors): LBR (0.84), EIF4G3 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytoplasmic linker associated protein 1. CLASPs, such as CLASP1, are nonmotor microtubule-associated proteins that interact with CLIPs (e.g., CLIP170; MIM 179838). CLASP1 is involved in the regulation of microtubule dynamics at the kinetochore and throughout the spindle (Maiato et al., 2003 [PubMed 12837247]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: RNU4ATAC spectrum disorder (0.561); Roifman syndrome (0.560); microcephalic osteodysplastic primordial dwarfism type I (0.559); Lowry-Wood syndrome (0.551); neurodegenerative disease (0.521)
- **Europe PMC papers**: 738
- **Why important**: CLASP1 has the strongest weighted position in the module and connects the cytoskeletal branch to EIF4G3 and RNF214. Its established functions include microtubule organization, microtubule nucleation, suppression of microtubule depolymerization, Golgi organization, and mitotic-spindle organization. It also has the largest literature footprint among the selected genes and disease links involving several developmental and neurodegenerative conditions. Its lung detection supports biological presence in the sampled tissue, but its broad tissue specificity argues against a lung-specific interpretation.
- **Conclusion**: Established evidence supports CLASP1 as a cytoskeletal and intracellular-organization gene occupying a central position in this small module. It is a plausible marker of coordinated cellular state, but there is no evidence here that CLASP1 mechanistically drives the module or that its known functions explain the co-abundance pattern.

#### EIF4G3

- **Related proteins** (co-abundance neighbors): CLASP1 (0.84), RNF214 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 3. The protein encoded by this gene is thought to be part of the eIF4F protein complex, which is involved in mRNA cap recognition and transport of mRNAs to the ribosome. Interestingly, a microRNA (miR-520c-3p) has been found that negatively regulates synthesis of the encoded protein, and this leads to a global decrease in protein translation and cell proliferation. Therefore, this protein is a key co…
- **Diseases (Open Targets)**: smoking initiation (0.426); dengue disease (0.370); essential hypertension (0.270); hypertensive disorder (0.269); heparin cofactor 2 deficiency (0.266)
- **Europe PMC papers**: 1502
- **Why important**: EIF4G3 is centrally positioned between CLASP1 and RNF214 and is a core component of the eIF4F translation-initiation machinery. Its annotations include translational initiation and regulation of translation, with additional links to autophagy and cell proliferation. It has a substantial literature base and disease or trait associations that include vascular and infectious contexts. Its association with neutrophils and neutrophil progenitors makes it relevant to the possibility that cellular composition contributes to the shared signal.
- **Conclusion**: Established evidence supports EIF4G3 as a translation-control component and a plausible indicator of cellular biosynthetic state. The module does not establish altered translation as its function, because no globally significant enrichment or external interaction support was observed.

#### LBR

- **Related proteins** (co-abundance neighbors): CLASP1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nuclear membrane; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lamin B receptor. The protein encoded by this gene belongs to the ERG4/ERG24 family. It localized in the nuclear envelope inner membrane and anchors the lamina and the heterochromatin to the membrane. It may mediate interaction between chromatin and lamin B. Mutations of this gene has been associated with autosomal recessive HEM/Greenberg skeletal dysplasia. Alternative splicing occurs at this locus and two transcr…
- **Diseases (Open Targets)**: Greenberg dysplasia (0.817); Pelger-Huet anomaly (0.731); regressive spondylometaphyseal dysplasia (0.729); Reynolds syndrome (0.543); Abnormality of the skeletal system (0.488)
- **Europe PMC papers**: 3274
- **Why important**: LBR links the module's cytoskeletal side through CLASP1 and has the strongest literature support among the genes considered. It is an inner nuclear-envelope protein that connects nuclear lamina and heterochromatin biology, and it is annotated in sterol biosynthesis and neutrophil differentiation. Its group-enriched pattern in erythroid and myeloid progenitors, together with its disease associations involving nuclear-envelope and skeletal abnormalities, makes it particularly informative for interpreting possible blood-cell or developmental-cell contributions.
- **Conclusion**: Established evidence supports LBR as a nuclear-envelope, chromatin-associated, sterol-related, and hematopoietic-differentiation gene. In this module it may report cellular composition or maturation state, but the data do not show that LBR physically interacts with CLASP1 or that it defines the module's function.

#### RNF214

- **Related proteins** (co-abundance neighbors): PDXDC1 (0.85), EIF4G3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Immune cell enhanced; location Golgi apparatus, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ring finger protein 214. Predicted to enable ubiquitin-protein transferase activity. Predicted to be involved in protein ubiquitination. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: ovarian dysfunction (0.222); familial lipoprotein lipase deficiency (0.218); hyperlipidemia (0.086); hepatocellular carcinoma (0.084); hypothyroidism (0.049)
- **Europe PMC papers**: 106
- **Why important**: RNF214 is one of the two higher-connectivity nodes and links PDXDC1 with EIF4G3. It is predicted to have ubiquitin-protein transferase activity and to participate in protein ubiquitination, while its disease and trait associations include lipid-related and endocrine contexts. Its literature volume is more limited than that of CLASP1, EIF4G3, or LBR, which makes it potentially informative but less firmly characterized.
- **Conclusion**: Established evidence is limited mainly to predicted ubiquitination-related function and reported disease associations. RNF214 is a reasonable candidate for protein-turnover or regulatory-state involvement, but any role in coordinating this module remains hypothetical and requires direct biochemical or perturbation evidence.

#### PDXDC1

- **Related proteins** (co-abundance neighbors): RNF214 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyridoxal dependent decarboxylase domain containing 1. Enables cadherin binding activity. Predicted to be involved in carboxylic acid metabolic process. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: autoimmune disorder of central nervous system (0.325); uterine corpus leiomyoma (0.325); type 2 diabetes mellitus (0.135); obesity disorder (0.123); nerve plexus disorder (0.096)
- **Europe PMC papers**: 379
- **Why important**: PDXDC1 is a peripheral module member connected to RNF214 and is localized to the Golgi and vesicles. Its annotations include cadherin binding and a predicted role in carboxylic-acid metabolism, while its cell-type associations include neuronal and renal epithelial populations. It has a moderate literature base and disease or trait links spanning central nervous system autoimmunity, metabolic disease, obesity, and nerve-plexus disease. These features make it useful for evaluating whether the module reflects intracellular trafficking or mixed cellular composition.
- **Conclusion**: Established evidence supports PDXDC1 as a Golgi or vesicle-associated protein with partly predicted molecular functions. Its peripheral position and limited mechanistic characterization make it more useful as a hypothesis-generating marker than as an established driver of the module.

## Module 17

**Tissue pair**: autonomic_nervous_system and lung  
**Genes (15)**: DNMT1, HIBCH, L2HGDH, ME2, NDUFS1, MRPL4, MRPL13, MRPL55, MRPS27, SDHA, SFXN1, SMARCD1, DARS2, IARS2, ZC3HAV1

### Function

The module is best interpreted as a mitochondrial bioenergetics and mitochondrial gene-expression module. The strongest primary evidence is the coordinated enrichment of mitochondrial matrix and mitochondrial compartments (GO:CC mitochondrial matrix; q_global = 8.35e-05), (GO:CC mitochondrion; q_global = 0.000271), together with mitochondrial membranes and inner membrane (GO:CC mitochondrial membrane; q_global = 0.000991), (GO:CC mitochondrial inner membrane; q_global = 0.00105), (GO:CC mitochondrial envelope; q_global = 0.00166), (GO:CC organelle inner membrane; q_global = 0.00191). Mitochondrial translation and mitochondrial gene expression are also supported after global correction (GO:BP mitochondrial translation; q_global = 0.000728), (GO:BP mitochondrial gene expression; q_global = 0.00435), with mitochondrial and organellar ribosome terms represented by MRPL13, MRPL4, MRPL55 and MRPS27 (GO:CC organellar ribosome; q_global = 0.02), (GO:CC mitochondrial ribosome; q_global = 0.02). The gene composition spans mitochondrial translation machinery, respiratory-chain components, amino-acid and organic-acid metabolism, and mitochondrial transport. Thus, the most defensible interpretation is coordinated variation in mitochondrial protein production and oxidative metabolism, rather than a narrowly defined signaling pathway. DNMT1, SMARCD1 and ZC3HAV1 are not supported by the primary enrichment terms and may represent peripheral or context-dependent connections rather than the core function.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary identifies only one secreted gene, and most genes are intracellular mitochondrial proteins or enzymes. The module is also not strongly blood-cell enriched; most genes have low immune-cell specificity, although SFXN1 and L2HGDH show basophil-related enrichment and ZC3HAV1 has bone-marrow and several immune-cell-associated patterns. The HPA profile is otherwise compatible with broadly distributed or cell-state-associated mitochondrial biology, with tissue-enhanced signals in muscle, kidney, choroid plexus and liver and cell-type-enhanced signals in several epithelial, neural, muscle and reproductive cell types. Protein detection in lung is widespread among the module genes, whereas there is no matching autonomic-nervous-system HPA tissue entry. Therefore, the shared module is more plausibly related to mitochondrial content or metabolic state in constituent cells than to blood contamination, although differences in cell composition between tissues remain a possible contributor.

**GO/KEGG enrichment**: 10 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrial matrix | 8.35e-05 | DARS2, HIBCH, IARS2, ME2, MRPL13, MRPL4, MRPL55, MRPS27, NDUFS1, SDHA |
| GO:CC mitochondrion | 0.000271 | DARS2, DNMT1, HIBCH, IARS2, L2HGDH, ME2, MRPL13, MRPL4, MRPL55, MRPS27, NDUFS1, SDHA, SFXN1 |
| GO:BP mitochondrial translation | 0.000728 | DARS2, IARS2, MRPL13, MRPL4, MRPL55, MRPS27 |
| GO:CC mitochondrial membrane | 0.000991 | DARS2, L2HGDH, MRPL13, MRPL4, MRPL55, MRPS27, NDUFS1, SDHA, SFXN1 |
| GO:CC mitochondrial inner membrane | 0.00105 | L2HGDH, MRPL13, MRPL4, MRPL55, MRPS27, NDUFS1, SDHA, SFXN1 |
| GO:CC mitochondrial envelope | 0.00166 | DARS2, L2HGDH, MRPL13, MRPL4, MRPL55, MRPS27, NDUFS1, SDHA, SFXN1 |
| GO:CC organelle inner membrane | 0.00191 | L2HGDH, MRPL13, MRPL4, MRPL55, MRPS27, NDUFS1, SDHA, SFXN1 |
| GO:BP mitochondrial gene expression | 0.00435 | DARS2, IARS2, MRPL13, MRPL4, MRPL55, MRPS27 |
| GO:CC organellar ribosome | 0.02 | MRPL13, MRPL4, MRPL55, MRPS27 |
| GO:CC mitochondrial ribosome | 0.02 | MRPL13, MRPL4, MRPL55, MRPS27 |

### STRING and hu.MAP

STRING supports a structured mitochondrial network rather than a collection of unrelated genes. The strongest known relationships include the mitochondrial large-ribosomal-protein group involving MRPL13, MRPL4, MRPL55 and MRPS27, the aminoacyl-tRNA-synthetase pair DARS2 and IARS2, and the respiratory-chain pair NDUFS1 and SDHA. STRING functional terms independently support mitochondrial localization, mitochondrial matrix, inner membrane, mitochondrial translation and mitochondrial ribosome annotations (STRING Keyword Mitochondrion; within-query FDR = 4.72e-06) through (STRING Component Ribosomal subunit; within-query FDR = 0.0093), but these are supplementary and are not treated as global enrichment evidence. hu.MAP provides repeated complex-level support for MRPL55, MRPL13 and MRPL4 in mitochondrial ribosome-related assemblies (hu.MAP huMAP3_04652.1) through (hu.MAP huMAP3_06589.1), and places DARS2 with IARS2 in mitochondrial amino-acid metabolism or translation-associated complexes (hu.MAP huMAP3_09668.1), (hu.MAP huMAP3_10525.1), (hu.MAP huMAP3_13468.1). MRPS27 is additionally represented in a hu.MAP complex (hu.MAP huMAP3_05807.1). The fact that several module genes are members of larger known complexes means that part of the co-abundance pattern is consistent with established physical or functional organization. Conversely, many module edges are not represented by STRING or hu.MAP, so the network should not be interpreted as a fully validated physical complex.

**STRING interactions (score >= 0.7)**: 10 of 105 gene pairs: DARS2–IARS2 (0.895); HIBCH–MRPL13 (0.946); HIBCH–MRPL4 (0.943); MRPL13–MRPL4 (0.999); MRPL13–MRPL55 (0.97); MRPL13–MRPS27 (0.905); MRPL4–MRPL55 (0.959); MRPL4–MRPS27 (0.895); MRPL55–MRPS27 (0.876); NDUFS1–SDHA (0.995)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Mitochondrion (FDR = 4.72e-06, 12 genes); COMPARTMENTS Mitochondrion (FDR = 2.47e-05, 12 genes); COMPARTMENTS Mitochondrial matrix (FDR = 3.2e-05, 9 genes); Keyword Transit peptide (FDR = 8.48e-05, 9 genes); Component Mitochondrion (FDR = 0.00022, 12 genes); Component Mitochondrial inner membrane (FDR = 0.00022, 8 genes); Component Mitochondrial matrix (FDR = 0.00022, 9 genes); Process Mitochondrial translation (FDR = 0.00099, 6 genes); Component Mitochondrial protein-containing complex (FDR = 0.003, 6 genes); Component Mitochondrial ribosome (FDR = 0.0031, 4 genes); COMPARTMENTS Mitochondrial inner membrane (FDR = 0.0088, 6 genes); COMPARTMENTS Mitochondrial ribosome (FDR = 0.0088, 4 genes); COMPARTMENTS Ribosomal subunit (FDR = 0.0088, 4 genes); COMPARTMENTS Mitochondrial protein complex (FDR = 0.0088, 6 genes); Component Ribosomal subunit (FDR = 0.0093, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04652.1 (MRPL55, MRPL13, MRPL4; 3/30); huMAP3_06439.1 (MRPL55, MRPL13, MRPL4; 3/57); huMAP3_06550.1 (MRPL55, MRPL13, MRPL4; 3/62); huMAP3_07939.1 (MRPL55, MRPL13, MRPL4; 3/68); huMAP3_08458.1 (MRPL55, MRPL13, MRPL4; 3/70); huMAP3_09113.1 (MRPL55, MRPL13, MRPL4; 3/72); huMAP3_09483.1 (MRPL55, MRPL13, MRPL4; 3/74); huMAP3_06589.1 (MRPL55, MRPL13, MRPL4; 3/79); huMAP3_09668.1 (DARS2, IARS2; 2/8); huMAP3_00983.1 (MRPL55, MRPL4; 2/22); huMAP3_01856.1 (MRPL55, MRPL13; 2/31); huMAP3_10525.1 (DARS2, IARS2; 2/33); huMAP3_05807.1 (ZC3HAV1, MRPS27; 2/81); huMAP3_13468.1 (DARS2, IARS2; 2/99)

### Novelty

The mitochondrial interpretation itself is not a new biological discovery: the individual genes, mitochondrial ribosome relationships, respiratory-chain relationships and associated disease links are already well established. The module-level observation may nevertheless be a new cross-tissue co-abundance pattern, because the fact sheet does not identify an existing named module spanning autonomic nervous system and lung. That claim should remain provisional. Known STRING edges and repeated hu.MAP complexes explain a substantial core of the structure, weakening any claim that the entire module is novel. Absence of some edges from STRING or hu.MAP cannot establish novelty, since those resources are incomplete and represent different evidence types. The strongest defensible novelty claim is therefore a potentially novel tissue-pair-specific coordination of established mitochondrial programs, requiring replication in independent cohorts and testing against cell composition, tissue quality and mitochondrial-content covariates.

**Hypothesis.** Hypothesis: shared physiological or cellular demands in autonomic nervous system and lung produce coordinated mitochondrial adaptation, coupling mitochondrial ribosome assembly and translation with respiratory-chain activity, organic-acid metabolism and amino-acid handling. In this model, MRPL13, MRPL4, MRPL55 and MRPS27 track mitochondrial protein-production capacity; DARS2 and IARS2 support mitochondrial tRNA charging; NDUFS1 and SDHA represent oxidative electron transport; and L2HGDH, HIBCH, ME2 and SFXN1 connect the program to mitochondrial substrate metabolism and transport. The co-abundance signal could reflect coordinated mitochondrial abundance or energetic state within shared cell populations rather than direct regulation among every module member. DNMT1, SMARCD1 and ZC3HAV1 may indicate additional coupling to nuclear regulation, chromatin state or antiviral response, but that extension is a hypothesis and is not established by the primary enrichment results.

### Important genes

#### MRPL55

- **Related proteins** (co-abundance neighbors): ZC3HAV1 (0.85), MRPL4 (0.84), MRPS27 (0.84), MRPL13 (0.83), DNMT1 (0.81); STRING partners: MRPL13 (0.97), MRPL4 (0.959), MRPS27 (0.876)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_04652.1, huMAP3_06439.1, huMAP3_06550.1, huMAP3_07939.1, huMAP3_08458.1, huMAP3_09113.1, huMAP3_09483.1, huMAP3_06589.1, huMAP3_00983.1, huMAP3_01856.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein L55. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.486); hypertensive disorder (0.071); essential hypertension (0.057); atrial fibrillation (0.043); cardiovascular disorder (0.038)
- **Europe PMC papers**: 192
- **Why important**: MRPL55 has the strongest network position in the module and connects to the mitochondrial ribosomal group, including MRPL13, MRPL4 and MRPS27. It appears in every primary GO term (GO:CC mitochondrial matrix; q_global = 8.35e-05) through (GO:CC mitochondrial ribosome; q_global = 0.02), every supplementary STRING term (STRING Keyword Mitochondrion; within-query FDR = 4.72e-06) through (STRING Component Ribosomal subunit; within-query FDR = 0.0093), and most of the hu.MAP mitochondrial ribosome complexes (hu.MAP huMAP3_04652.1) through (hu.MAP huMAP3_06589.1), (hu.MAP huMAP3_00983.1), (hu.MAP huMAP3_01856.1). Its annotation identifies it as a mitochondrial large-subunit ribosomal protein, and its disease and neurodegeneration associations make it a useful marker of the biological relevance of the module. Its literature support is substantial.
- **Conclusion**: Established evidence supports MRPL55 as a central marker of mitochondrial translation and mitoribosome-related co-abundance. It is reasonable to treat it as a module hub, but the data do not demonstrate that MRPL55 causally controls the other genes.

#### MRPL4

- **Related proteins** (co-abundance neighbors): MRPS27 (0.86), MRPL55 (0.84), NDUFS1 (0.81); STRING partners: HIBCH (0.943), MRPL13 (0.999), MRPL55 (0.959), MRPS27 (0.895)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_04652.1, huMAP3_06439.1, huMAP3_06550.1, huMAP3_07939.1, huMAP3_08458.1, huMAP3_09113.1, huMAP3_09483.1, huMAP3_06589.1, huMAP3_00983.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein L4. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.484); lymphatic system disorder (0.275); aortic stenosis (0.056); allergic rhinitis (0.043); gastric cancer (0.020)
- **Europe PMC papers**: 350
- **Why important**: MRPL4 is a mitochondrial large-subunit ribosomal protein with a strong network connection to MRPL55, MRPS27 and NDUFS1, and it is linked to HIBCH and MRPL13 in STRING. It is present in every primary GO term (GO:CC mitochondrial matrix; q_global = 8.35e-05) through (GO:CC mitochondrial ribosome; q_global = 0.02), is repeatedly represented in hu.MAP complexes (hu.MAP huMAP3_04652.1) through (hu.MAP huMAP3_06589.1), (hu.MAP huMAP3_00983.1), and has extensive literature and disease-association support. Its position bridges the mitochondrial ribosome signal and the respiratory-chain component NDUFS1.
- **Conclusion**: Established evidence identifies MRPL4 as a core mitochondrial translation component and a plausible connector between the ribosomal and respiratory portions of the module. A direct regulatory bridge remains hypothetical.

#### DARS2

- **Related proteins** (co-abundance neighbors): L2HGDH (0.84), DNMT1 (0.80); STRING partners: IARS2 (0.895)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_09668.1, huMAP3_10525.1, huMAP3_13468.1
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 2, mitochondrial. The protein encoded by this gene belongs to the class-II aminoacyl-tRNA synthetase family. It is a mitochondrial enzyme that specifically aminoacylates aspartyl-tRNA. Mutations in this gene are associated with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation (LBSL). [provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: leukoencephalopathy with brain stem and spinal cord involvement-high lactate syndrome (0.843); neurodegenerative disease (0.527); hereditary disease (0.518); hypertensive disorder (0.425); Cerebral cortical atrophy (0.425)
- **Europe PMC papers**: 796
- **Why important**: DARS2 is a mitochondrial aspartyl-tRNA synthetase and is included in the primary mitochondrial and mitochondrial gene-expression terms (GO:CC mitochondrial matrix; q_global = 8.35e-05), (GO:CC mitochondrion; q_global = 0.000271), (GO:BP mitochondrial translation; q_global = 0.000728), (GO:CC mitochondrial membrane; q_global = 0.000991), (GO:CC mitochondrial envelope; q_global = 0.00166), (GO:BP mitochondrial gene expression; q_global = 0.00435). It connects in the module to L2HGDH and DNMT1 and has a known STRING relationship with IARS2. hu.MAP places DARS2 and IARS2 together in several mitochondrial complexes (hu.MAP huMAP3_09668.1), (hu.MAP huMAP3_10525.1), (hu.MAP huMAP3_13468.1). Its established association with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation is particularly relevant to a tissue pair involving autonomic and pulmonary biology.
- **Conclusion**: Established evidence supports DARS2 as a marker of mitochondrial translation capacity and mitochondrial tRNA charging. Its disease association supports biological importance, but the module does not show that this specific co-abundance pattern causes neurological or pulmonary disease.

#### NDUFS1

- **Related proteins** (co-abundance neighbors): SMARCD1 (0.82), MRPL4 (0.81); STRING partners: SDHA (0.995)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S1. The protein encoded by this gene belongs to the complex I 75 kDa subunit family. Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Thi…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 5 (0.810); mitochondrial complex I deficiency (0.647); type 2 diabetes mellitus (0.608); Parkinson disease (0.603); diabetes mellitus (0.580)
- **Europe PMC papers**: 2567
- **Why important**: NDUFS1 is the largest subunit of respiratory-chain complex I and contributes to mitochondrial electron transport and proton-motive-force-linked ATP synthesis. It is present in the primary mitochondrial matrix and membrane terms (GO:CC mitochondrial matrix; q_global = 8.35e-05), (GO:CC mitochondrion; q_global = 0.000271), (GO:CC mitochondrial membrane; q_global = 0.000991), (GO:CC mitochondrial inner membrane; q_global = 0.00105), (GO:CC mitochondrial envelope; q_global = 0.00166), (GO:CC organelle inner membrane; q_global = 0.00191), connects to MRPL4 in the module, and has a very strong known STRING relationship with SDHA. Its HPA profile is enhanced in heart and skeletal muscle and in several neural or epithelial cell types, while its disease associations include complex I deficiency and Parkinson disease.
- **Conclusion**: Established evidence supports NDUFS1 as the respiratory-chain anchor of the module. Its connection to the mitoribosomal component is consistent with coordinated mitochondrial function, but it does not prove physical interaction between complex I and the mitochondrial ribosome in this module.

#### L2HGDH

- **Related proteins** (co-abundance neighbors): ME2 (0.87), DARS2 (0.84), SFXN1 (0.82), HIBCH (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: L-2-hydroxyglutarate dehydrogenase. This gene encodes L-2-hydroxyglutarate dehydrogenase, a FAD-dependent enzyme that oxidizes L-2-hydroxyglutarate to alpha-ketoglutarate in a variety of mammalian tissues. Mutations in this gene cause L-2-hydroxyglutaric aciduria, a rare autosomal recessive neurometabolic disorder resulting in moderate to severe cognitive disability. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: L-2-hydroxyglutaric aciduria (0.823); neurodegenerative disease (0.514); hereditary disease (0.452); gout (0.376); lysosomal storage disease (0.370)
- **Europe PMC papers**: 521
- **Why important**: L2HGDH is a mitochondrial enzyme that oxidizes L-2-hydroxyglutarate to alpha-ketoglutarate and participates in organic-acid and tricarboxylic-acid-related metabolism. It has a relatively central position, connecting ME2, DARS2, SFXN1 and HIBCH, and appears in several primary mitochondrial compartment terms (GO:CC mitochondrion; q_global = 0.000271), (GO:CC mitochondrial membrane; q_global = 0.000991), (GO:CC mitochondrial inner membrane; q_global = 0.00105), (GO:CC mitochondrial envelope; q_global = 0.00166), (GO:CC organelle inner membrane; q_global = 0.00191). Its association with L-2-hydroxyglutaric aciduria and neurodegenerative disease provides a disease-relevant link between mitochondrial metabolism and nervous-system phenotypes.
- **Conclusion**: Established evidence supports L2HGDH as a metabolic connector within the mitochondrial program, linking substrate handling to translation-associated and membrane-associated genes. The data support a coordinating role as a marker, not a demonstrated causal role in the tissue-pair module.
