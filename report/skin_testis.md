# Conserved co-abundance modules: skin and testis

## Module 0

**Tissue pair**: skin and testis  
**Genes (10)**: AASS, ARFGEF1, CNOT1, CYB5A, DCAKD, NAA15, TRAPPC11, SNRNP200, UBE3A, VPS41

### Function

The module does not have a statistically supported GO or KEGG functional label: no GO/KEGG term passed global correction, and no STRING functional-enrichment term was reported. The network nevertheless suggests a heterogeneous intracellular homeostasis module rather than a single established pathway. Its most coherent functional signal is vesicle and endomembrane biology: TRAPPC11 is linked to ER-to-Golgi transport and COPII assembly, ARFGEF1 to ARF activation and Golgi organization, and VPS41 to HOPS-associated intracellular and endosome-to-lysosome transport. The module also contains genes representing protein quality and expression control, including UBE3A-mediated ubiquitination, NAA15-dependent N-terminal acetylation, CNOT1-dependent mRNA deadenylation and regulation, and SNRNP200-dependent spliceosome function. AASS and CYB5A add mitochondrial lysine catabolism and membrane redox or lipid-related biology. Thus, the best-supported interpretation is coordinated abundance of broadly expressed intracellular trafficking, protein-processing, RNA-processing, and metabolic machinery, with vesicle trafficking as the clearest network-level theme rather than a proven unified pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not strongly blood-cell enriched, with most genes showing low immune-cell specificity and one reported as not detected in immune cells. Most genes have low tissue specificity and low cell-type specificity, supporting a broadly expressed housekeeping-like intracellular component rather than a skin- or testis-specific program. The exceptions are limited and heterogeneous: CYB5A is tissue enhanced in kidney and liver and cell-type enhanced across several epithelial or stromal-related populations, while AASS is enhanced in several cell types including hepatocytes and glial or stromal populations; ARFGEF1 is enhanced in neutrophil progenitors. Protein detection is reported for most genes in both skin and testis. These observations make a shared ubiquitous cellular program more plausible than a blood contamination explanation, although bulk-tissue composition and shared cell types cannot be excluded.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only one high-confidence relationship within the module, CNOT1--SNRNP200, so most module edges are not independently supported as known physical or functional STRING interactions. The STRING-supported pair connects a CCR4-NOT mRNA-regulatory scaffold with a U5 spliceosomal helicase, but it should not be interpreted as proof that the entire module is one complex. hu.MAP identifies one partial complex, huMAP3_08994.1 (hu.MAP huMAP3_08994.1), containing DCAKD and ARFGEF1 among the module genes, with other listed complex members POR, CLCN4, ABCA3, ABCB9, and TMEM9B. This supports one established complex-level connection involving ARFGEF1 and DCAKD, while the remaining genes are not assigned to a shared hu.MAP complex in the fact sheet. The dense module edges around TRAPPC11 and ARFGEF1 are therefore co-abundance relationships, not established physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: CNOT1–SNRNP200 (0.748)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08994.1 (DCAKD, ARFGEF1; 2/7)

### Novelty

This appears novel as a skin-testis conserved co-abundance module, but the evidence supports cautious wording rather than a claim of discovery of a new molecular complex or pathway. The exact gene combination is not presented in the fact sheet as a previously named module, and the network combines genes from trafficking, ubiquitination, RNA regulation, splicing, acetylation, and metabolism. At the same time, several individual functions and disease associations are well established, and the existence of the STRING relationship and the hu.MAP complex (hu.MAP huMAP3_08994.1) shows that parts of the signal are already known. Absence of additional STRING or hu.MAP relationships cannot establish novelty, because those resources are incomplete and co-abundance does not require direct binding. The defensible conclusion is that the cross-tissue co-abundance organization is potentially new, whereas the component biology is largely established and heterogeneous.

**Hypothesis.** Hypothesis: the module reflects a shared basal cellular-maintenance state in skin and testis in which intracellular membrane trafficking and organelle delivery are coordinated with protein maturation, ubiquitin-dependent turnover, RNA surveillance or processing, and lipid or amino-acid metabolism. TRAPPC11 may occupy a central co-abundance position linking trafficking-related proteins with CYB5A, AASS, CNOT1, UBE3A, and SNRNP200, while ARFGEF1 may connect Golgi or endomembrane activity to VPS41 and the DCAKD-containing hu.MAP complex (hu.MAP huMAP3_08994.1). This is a mechanistic hypothesis generated from network topology and annotations, not an experimentally demonstrated pathway; the lack of globally significant GO/KEGG enrichment and the sparse STRING support argue that it requires validation by replication, perturbation, and compartment- or cell-type-resolved measurements.

### Important genes

#### TRAPPC11

- **Related proteins** (co-abundance neighbors): AASS (0.87), CYB5A (0.86), CNOT1 (0.84), UBE3A (0.83), SNRNP200 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: trafficking protein particle complex subunit 11. The protein encoded by this gene is a subunit of the TRAPP (transport protein particle) tethering complex, which functions in intracellular vesicle trafficking. This subunit is involved in early stage endoplasmic reticulum-to-Golgi vesicle transport. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jan 2013].
- **Diseases (Open Targets)**: autosomal recessive limb-girdle muscular dystrophy type R18 (0.805); autosomal recessive limb-girdle muscular dystrophy (0.554); neurodegenerative disease (0.485); hereditary disease (0.471); limb-girdle muscular dystrophy (0.458)
- **Europe PMC papers**: 377
- **Why important**: TRAPPC11 has the strongest network position in the module, with the greatest degree and weighted strength reported in the fact sheet, and connects to five module members including ARFGEF1, CNOT1, UBE3A, SNRNP200, AASS, and CYB5A. Its established role in the TRAPP complex, ER-to-Golgi transport, Golgi organization, and COPII vesicle assembly gives the module its clearest trafficking-centered anchor. It also has a substantial literature record and strong Open Targets association with autosomal recessive limb-girdle muscular dystrophy type R18.
- **Conclusion**: Established: TRAPPC11 is an intracellular trafficking factor and the principal network hub of this module. Hypothesis: it may coordinate the module's vesicle-trafficking signal with protein and RNA homeostasis. The co-abundance data do not prove that its neighbors physically bind TRAPPC11 or that the module causes muscular disease.

#### ARFGEF1

- **Related proteins** (co-abundance neighbors): VPS41 (0.91), DCAKD (0.85), CNOT1 (0.81), UBE3A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_08994.1
- **Function (MyGene.info)**: ARF guanine nucleotide exchange factor 1. ADP-ribosylation factors (ARFs) play an important role in intracellular vesicular trafficking. The protein encoded by this gene is involved in the activation of ARFs by accelerating replacement of bound GDP with GTP. It contains a Sec7 domain, which may be responsible for guanine-nucleotide exchange activity and also brefeldin A inhibition. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: developmental delay, impaired speech, and behavioral abnormalities, with or without seizures (0.774); Intellectual disability (0.646); Joubert syndrome 21 (0.551); Global developmental delay (0.533); hereditary disease (0.528)
- **Europe PMC papers**: 363
- **Why important**: ARFGEF1 is the second strongest network-connected gene and links VPS41, DCAKD, CNOT1, and UBE3A. Its established Sec7-domain function in ARF activation, exocytosis, Golgi organization, and vesicle-mediated transport aligns with the module's most coherent functional theme. It is also one of the two module members in the hu.MAP complex (hu.MAP huMAP3_08994.1) and has reported associations with developmental delay, intellectual disability, and Joubert syndrome twenty-one.
- **Conclusion**: Established: ARFGEF1 is a Golgi and vesicle-trafficking regulator and participates in the partial hu.MAP complex (hu.MAP huMAP3_08994.1). Hypothesis: it may be the bridge between the trafficking subnetwork and the DCAKD-containing complex. The module does not establish a disease mechanism or direct interaction with all of its co-abundant neighbors.

#### UBE3A

- **Related proteins** (co-abundance neighbors): TRAPPC11 (0.83), NAA15 (0.80), ARFGEF1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin protein ligase E3A. This gene encodes an E3 ubiquitin-protein ligase, part of the ubiquitin protein degradation system. This imprinted gene is maternally expressed in brain and biallelically expressed in other tissues. Maternally inherited deletion of this gene causes Angelman Syndrome, characterized by severe motor and intellectual retardation, ataxia, hypotonia, epilepsy, absence of speech, and characteristic facie…
- **Diseases (Open Targets)**: Angelman syndrome (0.843); hereditary disease (0.545); Intellectual disability (0.514); Global developmental delay (0.400); neurodevelopmental disorder (0.346)
- **Europe PMC papers**: 4879
- **Why important**: UBE3A connects the trafficking-centered genes TRAPPC11 and ARFGEF1 with NAA15, and it is detected in both skin and testis. Its E3 ubiquitin-protein ligase function provides a plausible protein-turnover component within an intracellular maintenance program. It is the most extensively studied gene in the module by the supplied literature-volume measure and has a strong Open Targets association with Angelman syndrome.
- **Conclusion**: Established: UBE3A participates in ubiquitin-dependent protein regulation and is strongly linked to Angelman syndrome. Hypothesis: its co-abundance with trafficking genes could reflect coupling between organelle or protein quality control and ubiquitin-mediated turnover. This module alone does not demonstrate tissue-specific imprinting effects or a causal connection to Angelman syndrome.

#### CNOT1

- **Related proteins** (co-abundance neighbors): TRAPPC11 (0.84), ARFGEF1 (0.81); STRING partners: SNRNP200 (0.748)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CCR4-NOT transcription complex subunit 1. Enables armadillo repeat domain binding activity; molecular adaptor activity; and nuclear receptor binding activity. Contributes to poly(A)-specific ribonuclease activity. Involved in several processes, including negative regulation of signal transduction; positive regulation of cytoplasmic mRNA processing body assembly; and regulation of gene expression. Located in P-body and cytosol. Part of CCR…
- **Diseases (Open Targets)**: holoprosencephaly 12 with or without pancreatic agenesis (0.749); Vissers-Bodmer syndrome (0.697); hereditary disease (0.515); complex neurodevelopmental disorder (0.474); neurodegenerative disease (0.471)
- **Europe PMC papers**: 1262
- **Why important**: CNOT1 is a molecular adaptor and core CCR4-NOT complex subunit involved in mRNA deadenylation, mRNA decay, P-body assembly, and regulation of gene expression. It connects TRAPPC11 and ARFGEF1 in the module and has the only high-confidence STRING relationship reported within the module, the CNOT1--SNRNP200 pair. Its disease associations include holoprosencephaly with or without pancreatic agenesis and Vissers-Bodmer syndrome, and its literature volume is substantial.
- **Conclusion**: Established: CNOT1 is a central post-transcriptional regulator and is linked to SNRNP200 by the reported STRING relationship. Hypothesis: it may represent coupling between RNA turnover and the cellular trafficking state. The STRING relationship does not establish a shared complex with TRAPPC11 or ARFGEF1, and the co-abundance pattern does not prove regulatory direction.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): TRAPPC11 (0.80); STRING partners: CNOT1 (0.748)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is the module's spliceosome-associated U5 snRNP helicase and forms the only reported high-confidence STRING relationship with another module member, CNOT1. Its established role in spliceosomal assembly and conformational change adds a pre-mRNA processing dimension to the otherwise trafficking-heavy central subgraph. It also has a substantial literature record and strong disease associations with retinitis pigmentosa and inherited retinal dystrophy.
- **Conclusion**: Established: SNRNP200 is a core spliceosomal factor and is connected to CNOT1 in STRING. Hypothesis: its co-abundance with trafficking and protein-maintenance genes may reflect a general demand for coordinated RNA and proteome homeostasis. The module does not show that splicing is enriched globally or that SNRNP200 mediates the module's tissue sharing.

#### CYB5A

- **Related proteins** (co-abundance neighbors): TRAPPC11 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome b5 type A. The protein encoded by this gene is a membrane-bound cytochrome that reduces ferric hemoglobin (methemoglobin) to ferrous hemoglobin, which is required for stearyl-CoA-desaturase activity. Defects in this gene are a cause of type IV hereditary methemoglobinemia. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2010].
- **Diseases (Open Targets)**: hereditary methemoglobinemia (0.521); 17,20-lyase deficiency, isolated (0.370); methemoglobinemia due to deficiency of methemoglobin reductase (0.370); cholelithiasis (0.301); Abnormality of the skeletal system (0.299)
- **Europe PMC papers**: 915
- **Why important**: CYB5A is directly connected to the principal hub TRAPPC11 and contributes a membrane-associated redox and lipid-related function, including support for stearyl-CoA desaturase activity and methemoglobin reduction. It is the only gene reported as tissue enhanced, with kidney and liver enrichment, and is cell-type enhanced across several epithelial and stromal-related populations. Its established disease associations include hereditary methemoglobinemia and isolated seventeen-twenty lyase deficiency.
- **Conclusion**: Established: CYB5A is a membrane-associated cytochrome with redox and lipid-metabolism roles and has a distinct tissue-enrichment profile. Hypothesis: its connection to TRAPPC11 may reflect coupling of membrane trafficking with lipid or organelle metabolism. The module does not establish that CYB5A drives the shared skin-testis signal, and its kidney or liver enhancement cautions against overinterpreting the module as tissue-specific.

## Module 1

**Tissue pair**: skin and testis  
**Genes (11)**: ABCB7, ALG2, EXOC6B, GIT1, GNAQ, CAMK2D, PUS1, SUPV3L1, TATDN1, THYN1, VCPIP1

### Function

The module does not support a single statistically established GO or KEGG function: no GO or KEGG term passed global correction. Its gene content instead suggests a heterogeneous cellular-maintenance program involving protein N-linked glycosylation through ALG2, RNA modification through PUS1, mitochondrial RNA handling through SUPV3L1, mitochondrial iron-sulfur and heme-related transport through ABCB7, signaling through GNAQ and CAMK2D, intracellular trafficking through EXOC6B, and genome or protein quality control through TATDN1 and VCPIP1. The network is organized around ALG2, with the remaining genes forming mostly weak peripheral connections, so the co-abundance pattern is better interpreted as a cross-tissue cellular state than as a demonstrated pathway module.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and protein detection is reported for nearly all module genes in both skin and testis, supporting broad cellular presence rather than a tissue-exclusive program. Several genes show enhancement in heart muscle, cardiomyocytes, brain, bone marrow, neutrophil-related populations, germ-cell populations, or other specialized cell types. However, most genes have low immune-cell specificity, so the evidence does not strongly support a blood-cell contaminant explanation. The shared signal could instead reflect broadly distributed intracellular functions combined with cell-type composition shared or represented in the two tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and STRING functional enrichment is absent. This means the observed co-abundance edges are not corroborated by the supplied STRING interaction network and should not be treated as established physical interactions. hu.MAP provides the main external structural support: TATDN1 and PUS1 occur together in huMAP complexes (hu.MAP huMAP3_10458.1) and (hu.MAP huMAP3_13468.1). Because each complex contains many additional proteins while only those two module members are present, these observations support a possible shared complex context but not a complete module-level complex. The remaining genes have no supplied hu.MAP membership.

**STRING interactions (score >= 0.7)**: 0 of 55 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10458.1 (TATDN1, PUS1; 2/16); huMAP3_13468.1 (TATDN1, PUS1; 2/99)

### Novelty

This may be a previously unreported cross-tissue co-abundance pattern, but the fact sheet is insufficient to establish that it is a new biological discovery. The absence of STRING interactions and the sparse hu.MAP overlap make the specific network configuration less obviously recognized by those resources, yet absence from a database does not prove novelty. The lack of globally significant GO or KEGG enrichment also prevents a strong claim that the module represents a newly defined pathway. A defensible conclusion is that the module is a potentially novel statistical association requiring replication, comparison with published co-expression resources, and validation in independent skin and testis datasets.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular proteostasis and specialized-cell maintenance state in skin and testis. ALG2 may act as the central abundance-linked hub, while PUS1, SUPV3L1, and ABCB7 represent RNA, mitochondrial, and iron-sulfur or heme-related maintenance processes; GNAQ and CAMK2D could connect this state to calcium-responsive signaling, and EXOC6B could connect it to trafficking and polarized cell biology. The hu.MAP association between TATDN1 and PUS1 raises the possibility that nucleic-acid processing contributes to the state. This is a mechanistic hypothesis rather than an established pathway interpretation, because the module lacks globally significant enrichment and STRING support.

### Important genes

#### ALG2

- **Related proteins** (co-abundance neighbors): THYN1 (0.87), PUS1 (0.86), GIT1 (0.86), GNAQ (0.86), CAMK2D (0.84), VCPIP1 (0.83), TATDN1 (0.81), SUPV3L1 (0.81), EXOC6B (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ALG2 alpha-1,3/1,6-mannosyltransferase. This gene encodes a member of the glycosyltransferase 1 family. The encoded protein acts as an alpha 1,3 mannosyltransferase, mannosylating Man(2)GlcNAc(2)-dolichol diphosphate and Man(1)GlcNAc(2)-dolichol diphosphate to form Man(3)GlcNAc(2)-dolichol diphosphate. Defects in this gene have been associated with congenital disorder of glycosylation type Ih (CDG-Ii). Alternative splicing results in mu…
- **Diseases (Open Targets)**: ALG2-congenital disorder of glycosylation (0.727); congenital myasthenic syndrome (0.692); neurodegenerative disease (0.450); congenital disorder of glycosylation (0.372); congenital disorder of glycosylation type I (0.370)
- **Europe PMC papers**: 871
- **Why important**: ALG2 is the dominant network hub, connecting to nearly every other module member with relatively strong co-abundance links. Its established function in dolichol-linked oligosaccharide and glycoprotein biosynthesis gives the module a plausible endoplasmic-reticulum and protein-maturation anchor. It is detected in both tissues, has low tissue specificity, is associated with congenital disorders of glycosylation and congenital myasthenic syndrome, and has substantial literature support.
- **Conclusion**: Established evidence supports ALG2 as the principal network organizer and a glycosylation enzyme. It is not established that ALG2 mechanistically drives the abundance pattern or links all peripheral genes; that interpretation remains a hypothesis.

#### PUS1

- **Related proteins** (co-abundance neighbors): ALG2 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_10458.1, huMAP3_13468.1
- **Function (MyGene.info)**: pseudouridine synthase 1. This gene encodes a pseudouridine synthase that converts uridine to pseudouridine once it has been incorporated into an RNA molecule. The encoded enzyme may play an essential role in tRNA function and in stabilizing the secondary and tertiary structure of many RNAs. A mutation in this gene has been linked to mitochondrial myopathy and sideroblastic anemia. Alternate splicing results in multiple tr…
- **Diseases (Open Targets)**: myopathy, lactic acidosis, and sideroblastic anemia (0.819); mitochondrial disease (0.400); Intellectual disability (0.370); sulfite oxidase deficiency due to molybdenum cofactor deficiency type B1 (0.340); hereditary disease (0.193)
- **Europe PMC papers**: 993
- **Why important**: PUS1 contributes a defined RNA-modification function, including pseudouridine synthesis for cellular and mitochondrial tRNAs, and is localized to both nucleoplasm and mitochondria. It is one of the two module genes jointly represented in huMAP complexes (hu.MAP huMAP3_10458.1) and (hu.MAP huMAP3_13468.1), providing the clearest complex-based support in the module. Its association with mitochondrial myopathy and sideroblastic anemia makes it biologically important, and it has substantial literature support.
- **Conclusion**: Established evidence supports PUS1 as an RNA-modification enzyme with mitochondrial relevance and as a member of the reported huMAP contexts. A direct role for PUS1 in coordinating the whole module or in skin-testis convergence is not established.

#### ABCB7

- **Related proteins** (co-abundance neighbors): TATDN1 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP binding cassette subfamily B member 7. The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily ar…
- **Diseases (Open Targets)**: X-linked sideroblastic anemia with ataxia (0.819); sideroblastic anemia (0.378); hereditary disease (0.340); spinocerebellar ataxia type 1 (0.333); mitochondrial disease (0.187)
- **Europe PMC papers**: 1100
- **Why important**: ABCB7 supplies a mitochondrial transport and iron-sulfur or heme-related interpretation that is distinct from the RNA and glycosylation annotations. It is connected to TATDN1 in the module, is detected in both tissues, and has a strong disease association with X-linked sideroblastic anemia with ataxia. Its literature support is substantial, making it a well-established biological anchor despite its peripheral network position.
- **Conclusion**: Established evidence supports ABCB7 in mitochondrial iron-sulfur cluster and heme-related biology and in relevant hereditary anemia. The module data do not establish that iron handling is the shared function of the skin-testis module.

#### GNAQ

- **Related proteins** (co-abundance neighbors): ALG2 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nuclear speckles, Plasma membrane; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein subunit alpha q. This locus encodes a guanine nucleotide-binding protein. The encoded protein, an alpha subunit in the Gq class, couples a seven-transmembrane domain receptor to activation of phospolipase C-beta. Mutations at this locus have been associated with problems in platelet activation and aggregation. A related pseudogene exists on chromosome 2.[provided by RefSeq, Nov 2010].
- **Diseases (Open Targets)**: Sturge-Weber syndrome (0.694); familial multiple nevi flammei (0.634); congenital hemangioma (0.504); Abnormality of the skeletal system (0.474); uveal melanoma (0.468)
- **Europe PMC papers**: 4970
- **Why important**: GNAQ links the module to receptor-dependent phospholipase C signaling and calcium-related signal transduction. It is connected to the ALG2 hub, is detected in both tissues, and shows enrichment in neutrophil-related cell populations and basophils in the HPA evidence. Its disease associations include Sturge-Weber syndrome, vascular lesions, and uveal melanoma, and it has extensive literature support.
- **Conclusion**: Established evidence supports GNAQ as a signaling G-protein subunit with disease-relevant vascular and pigment-cell biology. Its presence does not demonstrate that immune or vascular signaling explains the module, especially because most module genes have low immune-cell specificity.

#### CAMK2D

- **Related proteins** (co-abundance neighbors): ALG2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Primary cilium tip, Primary cilium transition zone, Principal piece; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium/calmodulin dependent protein kinase II delta. The product of this gene belongs to the serine/threonine protein kinase family and to the Ca(2+)/calmodulin-dependent protein kinase subfamily. Calcium signaling is crucial for several aspects of plasticity at glutamatergic synapses. In mammalian cells, the enzyme is composed of four different chains: alpha, beta, gamma, and delta. The product of this gene is a delta chain. Alternative splicing re…
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.632); atrial fibrillation (0.556); CAMK2D-related neurodevelopmental disorder and dilated cardiomyopathy (0.503); heart conduction disease (0.449); heart failure (0.438)
- **Europe PMC papers**: 2254
- **Why important**: CAMK2D contributes calcium and calmodulin-dependent kinase activity, regulation of membrane depolarization, and regulation of heart contraction. It is connected to ALG2, is tissue-enhanced in heart muscle, and is cell-type enhanced in cardiomyocytes and Sertoli cells, making it relevant to specialized cellular physiology in one of the module's tissues. Its associations with atrial fibrillation, heart failure, conduction disease, and neurodevelopmental disease provide substantial disease context and literature support.
- **Conclusion**: Established evidence supports CAMK2D as a calcium-responsive kinase with cardiac and specialized-cell relevance. A shared CAMK2D-dependent mechanism between skin and testis is not established by the available network or enrichment evidence.

## Module 2

**Tissue pair**: skin and testis  
**Genes (15)**: ACACA, AP2B1, ASMTL, APPL2, EXOC5, HERC4, KIFBP, PTGR2, PPAT, SAMHD1, SEC24D, TBC1D17, TTLL12, UBA3, UNC45A

### Function

The module does not have a globally significant GO or KEGG enrichment: no GO/KEGG term passed global correction, so there is no globally significant GO/KEGG functional annotation to treat as primary evidence. The gene annotations and network instead suggest a heterogeneous cellular module centered on intracellular trafficking, vesicle handling, protein quality control, nucleotide and lipid metabolism, and selected regulatory processes. HERC4 provides a possible ubiquitin-ligase axis; TBC1D17 is linked to endosome-to-Golgi retrograde transport and cilium assembly; EXOC5 supports exocyst-mediated vesicle docking and exocytosis; SEC24D supports COPII cargo loading and ER-to-Golgi transport; APPL2 participates in Rab5-associated endosomal signaling; and PPAT and ACACA represent purine and fatty-acid biosynthetic metabolism. These annotations are mechanistically compatible but do not establish a single coherent biological pathway. The co-abundance pattern may therefore reflect coordinated cellular state, shared trafficking demand, or sample composition rather than a discrete canonical pathway. There are no STRING enrichment terms.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It is also not broadly blood-cell enriched, because most genes have low immune-cell specificity, with only limited immune-cell enhancement. Most genes have low tissue specificity, while many show cell-type enhancement across diverse cell types, including neural, reproductive, epithelial, and immune-related populations. Protein detection is generally present in both skin and testis, although PPAT is detected in testis but not skin. The HPA pattern argues against a simple blood-contamination explanation, but the broad and heterogeneous cell-type pattern means that shared cell types, ubiquitous intracellular machinery, or technical and physiological state effects remain plausible explanations for the cross-tissue co-abundance.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING evidence is sparse. The only high-confidence STRING relationship in the module is ACACA-PPAT, supporting a known metabolic connection between fatty-acid synthesis and purine biosynthesis, but not a complete module-wide interaction network. The hu.MAP evidence consists of (hu.MAP huMAP3_12394.1), in which SEC24D and AP2B1 occur together among a much larger trafficking and vesicle-associated complex. This supports a known relationship between COPII transport and adaptor-mediated vesicle biology, while the absence of hu.MAP assignments for the other genes means that most co-abundance edges are not independently supported by the supplied complex resource. Overall, the module contains a small amount of established molecular connectivity embedded in a largely weakly supported co-abundance structure; co-abundance should not be interpreted as direct physical interaction.

**STRING interactions (score >= 0.7)**: 1 of 105 gene pairs: ACACA–PPAT (0.846)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12394.1 (SEC24D, AP2B1; 2/98)

### Novelty

The module may be a novel cross-tissue co-abundance pattern, because the supplied resources do not show a previously established module-wide interaction or complex: STRING supports only ACACA-PPAT, and hu.MAP supports only the SEC24D-AP2B1 membership in (hu.MAP huMAP3_12394.1). However, this is not sufficient to claim discovery of a new biological complex or pathway. Several individual functions and relationships are already established, and absence from STRING or hu.MAP can reflect incomplete coverage, context dependence, indirect regulation, or tissue-specific behavior. The defensible conclusion is that the cross-tissue co-abundance organization is potentially novel, whereas the underlying gene functions are not.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular homeostatic state in skin and testis that couples vesicle trafficking with proteostasis, cytoskeletal or organelle transport, lipid and purine biosynthetic demand, and selective signaling regulation. In this model, SEC24D, EXOC5, AP2B1, and APPL2 represent linked secretory and endosomal trafficking capacity; HERC4 and UBA3 represent ubiquitin or ubiquitin-like regulation; TBC1D17 and KIFBP connect trafficking with GTPase control and microtubule transport; and ACACA with PPAT reflects anabolic metabolic support. The hypothesis predicts coordinated regulation within particular cell populations rather than a universal physical complex, and requires validation by cell-resolved expression, perturbation, and direct interaction or flux measurements.

### Important genes

#### HERC4

- **Related proteins** (co-abundance neighbors): TBC1D17 (0.85), KIFBP (0.85), EXOC5 (0.84), SEC24D (0.84), PPAT (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HECT and RLD domain containing E3 ubiquitin protein ligase 4. HERC4 belongs to the HERC family of ubiquitin ligases, all of which contain a HECT domain and at least 1 RCC1 (MIM 179710)-like domain (RLD). The 350-amino acid HECT domain is predicted to catalyze the formation of a thioester with ubiquitin before transferring it to a substrate, and the RLD is predicted to act as a guanine nucleotide exchange factor for small G proteins (Hochrainer et al., 2005 […
- **Diseases (Open Targets)**: alcohol drinking (0.344); stroke disorder (0.279); urolithiasis (0.262); placenta praevia (0.187); muscle cramp (0.169)
- **Europe PMC papers**: 436
- **Why important**: HERC4 has the strongest network position in the module and connects several otherwise weakly connected parts of the graph, including TBC1D17, KIFBP, EXOC5, SEC24D, and PPAT. Its HECT and RCC1-like domains support an established role in ubiquitin-ligase biology, and its supplied annotations include protein ubiquitination, ubiquitin-dependent protein catabolism, and spermatogenesis. Its literature volume is substantial relative to several of the less characterized module members. It is therefore a useful candidate for linking proteostasis with trafficking and reproductive biology.
- **Conclusion**: Established evidence supports HERC4 as a ubiquitin-ligase family protein with a central co-abundance position and an annotation relevant to spermatogenesis. It is not established that HERC4 directly regulates the other module genes or creates the cross-tissue module. Its central position makes it a plausible organizing candidate, but that interpretation remains a hypothesis.

#### TBC1D17

- **Related proteins** (co-abundance neighbors): HERC4 (0.85), TTLL12 (0.85), UNC45A (0.84), UBA3 (0.82), ACACA (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TBC1 domain family member 17. Predicted to enable GTPase activator activity. Involved in retrograde transport, endosome to Golgi. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.499); Abnormality of the skeletal system (0.198); heart failure (0.145); heart disorder (0.046); atrial fibrillation (0.036)
- **Europe PMC papers**: 201
- **Why important**: TBC1D17 has a highly connected network position and is annotated with GTPase-activator activity, endosome-to-Golgi retrograde transport, and regulation of cilium assembly. Its HPA profile includes tissue enhancement in skeletal muscle and cell-type enhancement in oocytes and syncytiotrophoblasts, while protein is detected in both studied tissues. These features make it a plausible regulator connecting membrane traffic with specialized cell physiology.
- **Conclusion**: Established evidence supports a role in GTPase regulation and intracellular trafficking, with additional evidence for cilium-related regulation. The shared skin-testis co-abundance and its position near several functionally distinct genes support, but do not prove, a coordinating role in the module. A direct role in the proposed cross-tissue mechanism remains hypothetical.

#### EXOC5

- **Related proteins** (co-abundance neighbors): HERC4 (0.84), AP2B1 (0.81), APPL2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exocyst complex component 5. The protein encoded by this gene is a component of the exocyst complex, a multiple protein complex essential for targeting exocytic vesicles to specific docking sites on the plasma membrane. Though best characterized in yeast, the component proteins and functions of exocyst complex have been demonstrated to be highly conserved in higher eukaryotes. At least eight components of the exocyst complex,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); placental abruption (0.305); thyroid cancer (0.143); injury (0.095); placenta praevia (0.087)
- **Europe PMC papers**: 321
- **Why important**: EXOC5 is a component of the conserved exocyst complex and is annotated for exocytosis, post-Golgi vesicle transport, plasma-membrane protein localization, and membrane fission. It links HERC4 to AP2B1 and APPL2, thereby occupying a plausible bridge between exocytic and endosomal processes. HPA detects the protein in both skin and testis, and its vesicular localization is consistent with the trafficking interpretation.
- **Conclusion**: Established evidence supports EXOC5 as a core exocyst component involved in vesicle targeting and exocytosis. Its network placement supports participation in the module's trafficking aspect, but the supplied data do not establish a tissue-pair-specific function or direct interaction with its module neighbors.

#### SEC24D

- **Related proteins** (co-abundance neighbors): HERC4 (0.84), SAMHD1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: SEC24 homolog D, COPII component. The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec24p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. This gene product is implicated in the shaping of the vesicle, and also in cargo selection and concentration. Mut…
- **Diseases (Open Targets)**: Cole-Carpenter syndrome (0.753); hereditary disease (0.380); osteogenesis imperfecta type 1 (0.370); Seizure (0.259); Intellectual disability (0.259)
- **Europe PMC papers**: 780
- **Why important**: SEC24D is a COPII component involved in cargo selection, ER-to-Golgi transport, and COPII-coated vesicle loading. It connects HERC4 and SAMHD1 in the module and is one of the two module members represented in the hu.MAP complex (hu.MAP huMAP3_12394.1), alongside AP2B1. Its established disease associations with Cole-Carpenter syndrome and osteogenesis imperfecta also emphasize the physiological importance of secretory-pathway function.
- **Conclusion**: Established evidence supports SEC24D as a central ER export and cargo-selection factor, and (hu.MAP huMAP3_12394.1) provides limited independent complex-level support for its relationship with AP2B1. The data do not establish that SEC24D drives the shared skin-testis pattern, so its role as a module organizer is a hypothesis.

#### APPL2

- **Related proteins** (co-abundance neighbors): ASMTL (0.87), EXOC5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor protein, phosphotyrosine interacting with PH domain and leucine zipper 2. The protein encoded by this gene is one of two effectors of the small GTPase RAB5A/Rab5, which are involved in a signal transduction pathway. Both effectors contain an N-terminal Bin/Amphiphysin/Rvs (BAR) domain, a central pleckstrin homology (PH) domain, and a C-terminal phosphotyrosine binding (PTB) domain, and they bind the Rab5 through the BAR domain. They are associated with endosomal membran…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.452); injury (0.317); Hypernatremia (0.226); open-angle glaucoma (0.218); osteomyelitis (0.183)
- **Europe PMC papers**: 456
- **Why important**: APPL2 is a Rab5-associated endosomal effector with BAR, PH, and PTB domains and is annotated for signal transduction, endosomal biology, TGF-beta receptor signaling, and regulation of fibroblast migration. It connects ASMTL and EXOC5, providing a plausible signaling and endosomal interface within the module. HPA places it in vesicles and reports enhancement in microglia, Sertoli cells, and neutrophils, which is relevant to the diverse cellular contexts represented by the module.
- **Conclusion**: Established evidence supports APPL2 as an endosomal signaling adaptor. Its connection to EXOC5 is consistent with coordinated membrane trafficking, but it is not established that APPL2 mediates the conserved skin-testis co-abundance or that the neutrophil signal reflects contamination. Those interpretations remain hypotheses.

#### PPAT

- **Related proteins** (co-abundance neighbors): HERC4 (0.83); STRING partners: ACACA (0.846)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Midbody ring; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoribosyl pyrophosphate amidotransferase. The protein encoded by this gene is a member of the purine/pyrimidine phosphoribosyltransferase family. It is a regulatory allosteric enzyme that catalyzes the first step of de novo purine nucleotide biosythetic pathway. This gene and PAICS/AIRC gene, a bifunctional enzyme catalyzing steps six and seven of this pathway, are located in close proximity on chromosome 4, and divergently transcribed fr…
- **Diseases (Open Targets)**: acute lymphoblastic leukemia (0.594); rheumatoid arthritis (0.588); Crohn disease (0.577); ulcerative colitis (0.562); lymphoid leukemia (0.443)
- **Europe PMC papers**: 1775
- **Why important**: PPAT catalyzes the first regulatory step of de novo purine biosynthesis and has the largest literature volume among the supplied module genes. It forms the sole high-confidence STRING interaction with ACACA, creating the clearest independently supported metabolic relationship in the module. Its midbody-ring localization and detection in testis are also compatible with proliferative or specialized reproductive-cell demands, although it is not detected in skin in the supplied HPA result.
- **Conclusion**: Established evidence supports PPAT as a key purine-biosynthetic enzyme and supports its relationship with ACACA through STRING. The metabolic pair may indicate biosynthetic demand within part of the module, but it does not establish a direct link to vesicle trafficking or explain the full cross-tissue pattern. Any role in a shared anabolic state is therefore a hypothesis.

## Module 3

**Tissue pair**: skin and testis  
**Genes (18)**: ACADVL, ACO2, ACSS1, ATP1A1, ATP2A2, CANX, CDK5RAP3, GFM1, GHDC, GPD2, MMUT, OPA1, ALDH18A1, PDIA5, PITRM1, SACM1L, TFRC, TOP2A

### Function

The module does not have a formally supported GO or KEGG functional enrichment: no term passed global correction. Its gene composition instead points to a distributed cellular-maintenance program combining mitochondrial metabolism, mitochondrial dynamics, mitochondrial translation, calcium handling, membrane ion gradients, and endoplasmic-reticulum protein quality control. The strongest network position belongs to ACSS1, which connects metabolic, mitochondrial, redox, and ER-associated genes. A mitochondrial metabolic arm includes ACSS1, ACO2, MMUT, ACADVL, GPD2, and ALDH18A1; a mitochondrial maintenance arm includes OPA1, GFM1, and PITRM1; and a membrane or ER arm includes ATP1A1, ATP2A2, CANX, and PDIA5. TOP2A introduces a proliferative or germ-cell-associated component, but the network does not support a single narrowly defined pathway. Thus, the most defensible interpretation is a conserved cellular homeostasis module rather than a specific GO-defined process. The absence of globally enriched terms does not invalidate the module.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. Only a minority of genes are annotated as secreted, and most genes are intracellular mitochondrial, ER, cytosolic, nuclear, or membrane proteins. The HPA profile is broadly distributed: most genes have low tissue specificity, while the remainder show tissue or cell-type enhancement across diverse tissues and cell types. All module proteins were detected in both skin and testis, supporting genuine presence in both tissues. Most genes have low immune-cell specificity, so the module is not best explained as a blood-cell module, although TFRC and GPD2 have immune or blood-cell-associated HPA patterns and TFRC is secreted to blood. The broad expression and repeated association with metabolically active, contractile, epithelial, germ-cell, trophoblast, and neural-associated cell types suggest that shared cellular physiology or shared cell states may contribute to the cross-tissue co-abundance signal. HPA therefore supports a broadly expressed housekeeping-like component with tissue- and cell-state-specific overlays, rather than a module dominated by blood contamination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only two high-confidence relationships within the module: ATP1A1 with ATP2A2 and ATP2A2 with CANX. These relationships support a membrane-calcium and ER-associated substructure, but STRING reports no supplementary functional enrichment. hu.MAP provides partial membership in three complexes. MMUT, ALDH18A1, and GFM1 recur in two mitochondrial or metabolic complexes (hu.MAP huMAP3_13468.1) (hu.MAP huMAP3_10525.1), with ACSS1 additionally represented in (hu.MAP huMAP3_13468.1). ATP1A1 and ATP2A2 occur together in a membrane or transport complex (hu.MAP huMAP3_10473.1). These partial complex overlaps support real biological coherence around mitochondrial metabolism and membrane or calcium handling, but they do not show that the entire co-abundance module is a single physical complex. Most module edges lack corresponding high-confidence STRING support, indicating that the co-abundance network captures coordinated expression or abundance beyond established protein-protein interactions.

**STRING interactions (score >= 0.7)**: 2 of 153 gene pairs: ATP1A1–ATP2A2 (0.82); ATP2A2–CANX (0.849)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (MMUT, ALDH18A1, GFM1, ACSS1; 4/99); huMAP3_10525.1 (MMUT, ALDH18A1, GFM1; 3/33); huMAP3_10473.1 (ATP1A1, ATP2A2; 2/24)

### Novelty

The exact conserved skin-testis co-abundance module may represent a new systems-level observation, because the supplied resources do not identify it as a previously defined unified module and most of its network relationships are not supported by high-confidence STRING links or shared hu.MAP complex membership. However, the underlying biology is not wholly new: the mitochondrial enzymes, calcium pumps, ER chaperones, and mitochondrial translation factors have established functions, disease links, and partial complex relationships. Therefore the appropriate claim is novelty of the cross-tissue co-abundance organization or its integrated combination, not discovery of new gene functions or a new physical complex. Absence from STRING or hu.MAP alone cannot establish novelty. Independent replication, comparison with published tissue co-expression modules, and experimental testing would be needed to call the module definitively novel.

**Hypothesis.** Hypothesis: in both skin and testis, a shared population of metabolically active or differentiating cells coordinates mitochondrial fuel handling and respiratory capacity with protein-folding quality control and membrane calcium or ion homeostasis. ACSS1, ACO2, MMUT, and ACADVL could support carbon flux and energy production; OPA1, GFM1, and PITRM1 could maintain mitochondrial structure, translation, and proteostasis; and ATP1A1, ATP2A2, CANX, and PDIA5 could couple ionic or calcium handling to ER folding. The co-abundance pattern may therefore reflect a common demand for energetic, proteostatic, and membrane homeostasis during tissue-specific differentiation, including germ-cell-associated states in testis. This is a mechanistic hypothesis, not a conclusion from enrichment, because no GO or KEGG term passed global correction and most edges are not established physical interactions.

### Important genes

#### ACSS1

- **Related proteins** (co-abundance neighbors): TFRC (0.92), ACADVL (0.90), GPD2 (0.88), PDIA5 (0.88), OPA1 (0.84), ACO2 (0.83), CANX (0.81), GFM1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: acyl-CoA synthetase short chain family member 1. This gene encodes a mitochondrial acetyl-CoA synthetase enzyme. A similar protein in mice plays an important role in the tricarboxylic acid cycle by catalyzing the conversion of acetate to acetyl CoA. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Nov 2011].
- **Diseases (Open Targets)**: response to antihypertensive drug (0.284); neurodegenerative disease (0.220); acute myeloid leukemia (0.061); neoplasm (0.048); hepatocellular carcinoma (0.039)
- **Europe PMC papers**: 1022
- **Why important**: ACSS1 is the strongest network hub and connects TFRC, ACADVL, GPD2, PDIA5, OPA1, ACO2, CANX, and GFM1. Its established function as a mitochondrial acetyl-CoA synthetase links acetate utilization to central metabolism. It is also part of hu.MAP complex (hu.MAP huMAP3_13468.1), is detected in both tissues, and has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports ACSS1 as the network's central metabolic integrator and as a mitochondrial enzyme relevant to acetyl-CoA production. The proposed role of ACSS1 as the driver that coordinates the module is a hypothesis based on network position, not a demonstrated causal relationship.

#### ACO2

- **Related proteins** (co-abundance neighbors): ACSS1 (0.83), MMUT (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aconitase 2. The protein encoded by this gene belongs to the aconitase/IPM isomerase family. It is an enzyme that catalyzes the interconversion of citrate to isocitrate via cis-aconitate in the second step of the TCA cycle. This protein is encoded in the nucleus and functions in the mitochondrion. It was found to be one of the mitochondrial matrix proteins that are preferentially degraded by the serine proteas…
- **Diseases (Open Targets)**: infantile cerebellar-retinal degeneration (0.814); optic atrophy 9 (0.693); autosomal dominant optic atrophy, classic form (0.619); optic atrophy (0.601); mitochondrial disease (0.505)
- **Europe PMC papers**: 3559
- **Why important**: ACO2 is a mitochondrial tricarboxylic-acid-cycle enzyme connected to ACSS1 and MMUT. Its tissue enhancement in heart muscle, skeletal muscle, and tongue is consistent with association with energetically demanding cells. It has a strong established disease literature involving mitochondrial and optic-atrophy-related disorders.
- **Conclusion**: Established evidence supports ACO2 as a marker and functional component of mitochondrial carbon metabolism within the module. Its connection to the broader skin-testis co-abundance program may indicate coordinated energy demand, but the module does not prove that ACO2 regulates the other genes.

#### OPA1

- **Related proteins** (co-abundance neighbors): GHDC (0.85), ACSS1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OPA1 mitochondrial dynamin like GTPase. The protein encoded by this gene is a nuclear-encoded mitochondrial protein with similarity to dynamin-related GTPases. The encoded protein localizes to the inner mitochondrial membrane and helps regulate mitochondrial stability and energy output. This protein also sequesters cytochrome c. Mutations in this gene have been associated with optic atrophy type 1, which is a dominantly inherited optic …
- **Diseases (Open Targets)**: autosomal dominant optic atrophy, classic form (0.846); Behr syndrome (0.812); optic atrophy with or without deafness, ophthalmoplegia, myopathy, ataxia, and neuropathy (0.766); mitochondrial DNA depletion syndrome 14B (cardioencephalomyopathic type) (0.745); optic atrophy (0.653)
- **Europe PMC papers**: 12169
- **Why important**: OPA1 links ACSS1 with GHDC and encodes a mitochondrial inner-membrane dynamin-like GTPase involved in mitochondrial organization, fusion, stability, and energy output. It has extensive literature and well-established associations with optic atrophy and other mitochondrial disorders.
- **Conclusion**: Established evidence supports OPA1 as the mitochondrial-architecture component of the module. A coordinated relationship between mitochondrial morphology and the metabolic genes is biologically plausible, but it remains a hypothesis because the module contains no direct experimental evidence of such regulation.

#### ATP2A2

- **Related proteins** (co-abundance neighbors): CANX (0.80), ALDH18A1 (0.80); STRING partners: ATP1A1 (0.82), CANX (0.849)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_10473.1
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darie…
- **Diseases (Open Targets)**: Darier disease (0.823); acrokeratosis verruciformis (0.663); neurodegenerative disease (0.507); hereditary disease (0.416); schizophrenia (0.406)
- **Europe PMC papers**: 9327
- **Why important**: ATP2A2 is connected to CANX and ALDH18A1, has STRING support with ATP1A1 and CANX, and belongs to hu.MAP complex (hu.MAP huMAP3_10473.1). Its established function is calcium pumping into the sarcoplasmic or endoplasmic reticulum. It is group-enriched in muscle-associated tissues and is strongly associated with Darier disease, a skin disorder.
- **Conclusion**: Established evidence supports ATP2A2 as the calcium-handling and membrane component of the module and provides a direct link to skin biology through its disease association. Its proposed coupling of calcium homeostasis to mitochondrial and ER quality-control activity is a hypothesis supported by network context, not by global enrichment.

#### CANX

- **Related proteins** (co-abundance neighbors): ALDH18A1 (0.82), ACSS1 (0.81), ATP2A2 (0.80); STRING partners: ATP2A2 (0.849)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is an ER calcium-binding chaperone connected to ATP2A2, ALDH18A1, and ACSS1, with a high-confidence STRING relationship to ATP2A2. It supports folding and quality control of newly synthesized glycoproteins and is enriched in late spermatids, making it particularly relevant to the testis component. It also has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports CANX as an ER proteostasis factor and as part of a known ATP2A2-associated relationship. Its late-spermatid association makes it a plausible contributor to the testis signal, while its role in the shared skin-testis mechanism remains a hypothesis.

#### GFM1

- **Related proteins** (co-abundance neighbors): PITRM1 (0.83), SACM1L (0.81), ACSS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1
- **Function (MyGene.info)**: G elongation factor mitochondrial 1. Eukaryotes contain two protein translational systems, one in the cytoplasm and one in the mitochondria. Mitochondrial translation is crucial for maintaining mitochondrial function and mutations in this system lead to a breakdown in the respiratory chain-oxidative phosphorylation system and to impaired maintenance of mitochondrial DNA. This gene encodes one of the mitochondrial translation elongati…
- **Diseases (Open Targets)**: hepatoencephalopathy due to combined oxidative phosphorylation defect type 1 (0.822); neurodegenerative disease (0.463); combined oxidative phosphorylation deficiency (0.451); hereditary disease (0.341); Leigh syndrome (0.313)
- **Europe PMC papers**: 1380
- **Why important**: GFM1 encodes a mitochondrial translation elongation factor, connects PITRM1, SACM1L, and ACSS1, and occurs in both hu.MAP mitochondrial complexes (hu.MAP huMAP3_13468.1) (hu.MAP huMAP3_10525.1). Its established function links the module to maintenance of mitochondrial protein synthesis and respiratory-chain competence. It also has substantial literature and disease associations involving combined oxidative-phosphorylation defects.
- **Conclusion**: Established evidence supports GFM1 as a mitochondrial translation and respiratory-function component with physical-complex context. Its network connection to ACSS1 suggests coordinated mitochondrial maintenance, but whether GFM1 is mechanistically responsible for the shared co-abundance pattern is unproven.

## Module 4

**Tissue pair**: skin and testis  
**Genes (15)**: ACO1, ADK, CFL2, DUSP3, FKBP5, EPHX1, IST1, MAPK14, PALLD, PCCA, TM9SF4, USP15, VPS33A, WFS1, XPO5

### Function

This is not a statistically defined GO or KEGG functional module: no GO or KEGG term passed global correction, and there was no supplementary STRING enrichment. The gene set nevertheless combines several intracellular themes supported by individual annotations: mitochondrial and metabolic activity through PCCA, ACO1, EPHX1 and ADK; protein folding and stress regulation through FKBP5 and WFS1; vesicle and endosomal trafficking through IST1, TM9SF4 and VPS33A; actin and cell-structure regulation through PALLD and CFL2; RNA transport through XPO5; and signaling control through DUSP3 and MAPK14. The network is therefore best interpreted as a heterogeneous co-abundance program involving metabolism, proteostasis, membrane trafficking, cytoskeletal state and stress-responsive signaling, rather than as a single established biochemical pathway. The strongest direct interaction evidence is the DUSP3–MAPK14 relationship, consistent with regulation of MAPK signaling, but most other links represent co-abundance rather than established physical interactions.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of its members is annotated as secreted. Most members have low immune-cell specificity, while a smaller subset is enhanced in neutrophils, basophils or monocytes. HPA tissue and single-cell annotations are diverse, including liver, skeletal muscle, tongue, heart muscle, adrenal gland, hepatocytes, smooth muscle cells, proximal tubule cells, neutrophils and reproductive-cell populations. Protein detection is common in both skin and testis, although several proteins are not detected in one of the two tissues. This pattern argues against a simple plasma-protein explanation and is compatible with shared resident cell types, broadly distributed intracellular programs, or mixed tissue cellular composition. The immune-associated annotations mean that blood or infiltrating myeloid cells cannot be excluded, but the predominance of low immune-cell specificity does not support a purely blood-cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, between DUSP3 and MAPK14. This is biologically interpretable because DUSP3 is a dual-specificity phosphatase and MAPK14 is a stress- and cytokine-responsive MAP kinase. No other within-module STRING relationship is reported at the specified confidence threshold. hu.MAP reports no complex containing at least two module members. Thus, the module is not supported as a known multiprotein complex, and its edges should primarily be viewed as coordinated abundance relationships. The DUSP3–MAPK14 pair may represent a genuine signaling subunit, whereas the broader network may arise from shared cell state, tissue composition, or coordinated regulation.

**STRING interactions (score >= 0.7)**: 1 of 105 gene pairs: DUSP3–MAPK14 (0.936)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The finding should not be called a new molecular complex or a newly discovered pathway. Most individual gene functions and disease associations are established, and one internal interaction is already represented in STRING. Conversely, the absence of hu.MAP complexes and the sparse STRING connectivity do not prove novelty, because co-abundance relationships need not be physical interactions and interaction databases are incomplete. The potentially novel aspect is the tissue-pair co-abundance pattern linking these otherwise heterogeneous genes in skin and testis. That claim remains provisional and would require replication in independent cohorts, control for cell composition, and experimental testing of the proposed relationships.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular adaptation present in selected skin and testis cell populations, combining mitochondrial and small-molecule metabolism with proteostasis, vesicle handling, actin remodeling and stress-responsive MAPK control. PCCA may mark the central abundance axis, while WFS1, FKBP5, IST1, TM9SF4 and VPS33A connect protein and membrane handling, and DUSP3 may restrain MAPK14-dependent stress or inflammatory signaling. The apparent coordination could be driven by a common cell state rather than direct physical assembly. A testable prediction is that cell types expressing this module will show coordinated changes in metabolic activity, endosomal trafficking, cytoskeletal organization and MAPK phosphorylation, and that the pattern will weaken after explicit adjustment for cell-type composition.

### Important genes

#### PCCA

- **Related proteins** (co-abundance neighbors): FKBP5 (0.88), EPHX1 (0.86), ACO1 (0.86), IST1 (0.85), ADK (0.84), XPO5 (0.83), DUSP3 (0.83), MAPK14 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: propionyl-CoA carboxylase subunit alpha. The protein encoded by this gene is the alpha subunit of the heterodimeric mitochondrial enzyme Propionyl-CoA carboxylase. PCCA encodes the biotin-binding region of this enzyme. Mutations in either PCCA or PCCB (encoding the beta subunit) lead to an enzyme deficiency resulting in propionic acidemia. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by…
- **Diseases (Open Targets)**: propionic acidemia (0.853); hereditary disease (0.487); dilated cardiomyopathy (0.370); neurodegenerative disease (0.357); pontocerebellar hypoplasia type 2D (0.340)
- **Europe PMC papers**: 2633
- **Why important**: PCCA is the most connected node in the co-abundance subgraph and links the largest portion of the network, including FKBP5, EPHX1, ACO1, IST1, ADK, XPO5, DUSP3 and MAPK14. Its established role as the biotin-binding alpha subunit of propionyl-CoA carboxylase provides a mitochondrial metabolic anchor, and its association with propionic acidemia gives the module a clear disease-relevant metabolic component. Its high literature volume also makes it a well-characterized reference point.
- **Conclusion**: Established evidence supports PCCA as the principal network hub and as a mitochondrial short-chain and branched-chain fatty-acid metabolic enzyme. It is plausible, but not established, that PCCA abundance marks the metabolic cell state underlying the module or coordinates the other branches.

#### WFS1

- **Related proteins** (co-abundance neighbors): USP15 (0.86), FKBP5 (0.82), TM9SF4 (0.82), VPS33A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: wolframin ER transmembrane glycoprotein. This gene encodes a transmembrane protein, which is located primarily in the endoplasmic reticulum and ubiquitously expressed with highest levels in brain, pancreas, heart, and insulinoma beta-cell lines. Mutations in this gene are associated with Wolfram syndrome, also called DIDMOAD (Diabetes Insipidus, Diabetes Mellitus, Optic Atrophy, and Deafness), an autosomal recessive disorder. The disease…
- **Diseases (Open Targets)**: Wolfram syndrome (0.851); Wolfram-like syndrome (0.818); type 2 diabetes mellitus (0.764); autosomal dominant nonsyndromic hearing loss (0.749); cataract (0.703)
- **Europe PMC papers**: 3064
- **Why important**: WFS1 occupies a branch connecting USP15, FKBP5, TM9SF4 and VPS33A. It encodes an endoplasmic-reticulum transmembrane glycoprotein involved in ER overload response and is strongly associated with Wolfram syndrome and related disorders. Its detection in both tissues and its broad tissue specificity make it a useful candidate for a shared cellular stress or proteostasis program rather than a tissue-restricted marker.
- **Conclusion**: Established evidence supports WFS1 as an ER-linked regulator with important disease relevance and connections to protein stability and cellular stress. The hypothesis that it organizes the module's trafficking and proteostasis branch is supported by co-abundance and annotations but is not demonstrated as a physical or causal relationship.

#### FKBP5

- **Related proteins** (co-abundance neighbors): PCCA (0.88), PALLD (0.83), WFS1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FKBP prolyl isomerase 5. The protein encoded by this gene is a member of the immunophilin protein family, which play a role in immunoregulation and basic cellular processes involving protein folding and trafficking. This encoded protein is a cis-trans prolyl isomerase that binds to the immunosuppressants FK506 and rapamycin. It is thought to mediate calcineurin inhibition. It also interacts functionally with mature hetero…
- **Diseases (Open Targets)**: hypothyroidism (0.434); thyroid gland disorder (0.317); osteoarthritis, hip (0.284); ulcerative colitis (0.256); ovarian dysfunction (0.246)
- **Europe PMC papers**: 7900
- **Why important**: FKBP5 connects PCCA, PALLD and WFS1 and therefore links the metabolic, cytoskeletal and ER-associated branches. It is a well-studied immunophilin involved in protein folding, trafficking and regulation of phosphatidylinositol three-kinase and protein kinase B signaling, and it interacts with mature progesterone-receptor complexes. Its presence in cell populations including neutrophils, monocyte progenitors, podocytes and proximal tubule cells is consistent with a context-sensitive intracellular stress regulator.
- **Conclusion**: Established evidence supports FKBP5 as a protein-folding and signaling regulator with broad cellular roles. It is a plausible integrator of the module, but the data do not establish that it mechanistically couples PCCA, WFS1 and PALLD in skin or testis.

#### DUSP3

- **Related proteins** (co-abundance neighbors): PCCA (0.83); STRING partners: MAPK14 (0.936)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dual specificity phosphatase 3. The protein encoded by this gene is a member of the dual specificity protein phosphatase subfamily. These phosphatases inactivate their target kinases by dephosphorylating both the phosphoserine/threonine and phosphotyrosine residues. They negatively regulate members of the mitogen-activated protein (MAP) kinase superfamily (MAPK/ERK, SAPK/JNK, p38), which are associated with cellular proliferatio…
- **Diseases (Open Targets)**: coronary artery disorder (0.231); metabolic syndrome (0.186); neoplasm (0.089); osteosarcoma (0.074); hyperinsulinism due to INSR deficiency (0.057)
- **Europe PMC papers**: 1055
- **Why important**: DUSP3 is directly connected to MAPK14 in STRING and is also connected to the central PCCA node in the co-abundance graph. Its established phosphatase activity can inhibit MAPK-family signaling, including MAPK cascades, and its annotation includes negative regulation of cell migration and epidermal-growth-factor-receptor signaling. It is detected at the transcript or protein level in a cell context that includes late spermatids and several other specialized populations.
- **Conclusion**: Established evidence supports DUSP3 as a signaling phosphatase and supports its relationship with MAPK regulation. The module-level interpretation that DUSP3 buffers a shared stress or inflammatory signal is a reasonable hypothesis, not a demonstrated mechanism in these tissues.

#### MAPK14

- **Related proteins** (co-abundance neighbors): PCCA (0.80); STRING partners: DUSP3 (0.936)
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Nuclear speckles; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitogen-activated protein kinase 14. The protein encoded by this gene is a member of the MAP kinase family. MAP kinases act as an integration point for multiple biochemical signals, and are involved in a wide variety of cellular processes such as proliferation, differentiation, transcription regulation and development. This kinase is activated by various environmental stresses and proinflammatory cytokines. The activation requires it…
- **Diseases (Open Targets)**: neurodegenerative disease (0.464); autoimmune disorder of central nervous system (0.459); Alzheimer disease (0.337); Parkinson disease (0.316); lysosomal storage disease (0.303)
- **Europe PMC papers**: 8074
- **Why important**: MAPK14 forms the only reported high-confidence STRING interaction within the module, with DUSP3, and is connected to PCCA in the co-abundance network. It is a central stress- and cytokine-responsive kinase involved in signal integration, transcriptional regulation and chemotaxis. Its HPA profile includes neutrophil and basophil enrichment, making it particularly relevant when considering immune-cell contributions to the shared tissue signal.
- **Conclusion**: Established evidence supports MAPK14 as a major stress and inflammatory signaling node and supports its functional opposition or regulation by DUSP3. Its contribution to this module may reflect signaling state or myeloid-cell abundance; the available evidence does not distinguish those explanations.

#### VPS33A

- **Related proteins** (co-abundance neighbors): WFS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS33A core subunit of CORVET and HOPS complexes. This gene encodes a tethering protein and a core subunit of the homotypic fusion and protein sorting (HOPS) complex. The HOPS complex and a second endosomal tethering complex called the class C core vacuole/endosome tethering (CORVET) complex, perform diverse functions in endocytosis including membrane tethering, RabGTPase interaction, activation and proofreading of synaptic-soluble N-ethylmaleimi…
- **Diseases (Open Targets)**: mucopolysaccharidosis-plus syndrome (0.752); neurodegenerative disease (0.496); COVID-19 (0.370); placental abruption (0.198); retinitis pigmentosa (0.097)
- **Europe PMC papers**: 912
- **Why important**: VPS33A is connected to WFS1 in the co-abundance network and is a core subunit of the CORVET and HOPS endosomal tethering complexes. Its established roles in endosome-to-lysosome transport, vesicle-mediated transport, membrane fusion and organelle localization provide a mechanistic link between ER stress, trafficking and intracellular degradation. Its disease association with mucopolysaccharidosis-plus syndrome further emphasizes the importance of its trafficking function.
- **Conclusion**: Established evidence supports VPS33A as an endosomal tethering and membrane-trafficking factor. Its co-abundance with WFS1 is consistent with a shared proteostasis and trafficking state, but no physical complex involving other module members is reported, so a direct module-specific role remains hypothetical.

## Module 5

**Tissue pair**: skin and testis  
**Genes (14)**: AP1B1, EHD1, EXOC3, ITSN1, NBAS, RTCA, SELENOO, USO1, VPS11, VPS18, VPS53, WASHC4, WASHC5, TJP2

### Function

The module is best interpreted as an intracellular membrane-trafficking and protein-localization program centered on endosomal and vesicular transport. The strongest primary evidence is the coordinated enrichment for vesicle-mediated transport (GO:BP vesicle-mediated transport; q_global = 0.000601), protein transport (GO:BP protein transport; q_global = 0.00102), intracellular protein localization (GO:BP intracellular protein localization; q_global = 0.00208), establishment of protein localization (GO:BP establishment of protein localization; q_global = 0.00252), vesicle tethering complexes (GO:CC vesicle tethering complex; q_global = 0.00362), vesicle membranes (GO:CC cytoplasmic vesicle membrane; q_global = 0.0041)(GO:CC vesicle membrane; q_global = 0.00444), endosomes (GO:CC endosome; q_global = 0.0104), early endosomes (GO:CC early endosome; q_global = 0.0345), and endosomal transport (GO:BP endosomal transport; q_global = 0.0404). These terms cover most of the module and converge on cargo sorting, vesicle tethering, endosomal organization, recycling, and delivery between the Golgi, endosomes, lysosomes, and plasma membrane. The supplementary STRING results independently support the same interpretation through vesicle transport, endosome, vesicle organization, docking, and protein localization terms (15 supplementary STRING terms; within-query FDR 1.08e-06–0.0073). The sparse co-abundance graph is not a single compact physical complex: it contains hubs and bridges linking the VPS, WASH, adaptor, exocyst, Golgi, and endocytic components. Thus, the module most plausibly represents a coordinated trafficking system rather than one uniform complex.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly intracellular, including cytosolic, Golgi, vesicular, plasma-membrane, nucleoplasmic, mitochondrial, and junctional locations. Most genes have low tissue specificity, which is compatible with broadly deployed cellular machinery, but the module is not simply an undifferentiated housekeeping signature because many genes show cell-type enhancement. Relevant cell-type signals include late or early spermatids, neutrophils, microglia, oligodendrocytes, astrocytes, hepatocytes, and muscle-related cells. Blood-cell specificity is generally low, although a minority of genes are enhanced in immune cells such as eosinophils and non-classical monocytes. Protein detection is broadly observed in both skin and testis. The shared module could therefore reflect conserved trafficking machinery in resident or specialized cells of both tissues, with a possible contribution from spermatogenic and immune-associated cell populations, rather than contamination by circulating plasma proteins.

**GO/KEGG enrichment**: 12 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP vesicle-mediated transport | 0.000601 | AP1B1, EHD1, EXOC3, ITSN1, NBAS, USO1, VPS11, VPS18, VPS53, WASHC4, WASHC5 |
| GO:BP protein transport | 0.00102 | AP1B1, EHD1, EXOC3, ITSN1, NBAS, USO1, VPS11, VPS18, VPS53, WASHC4, WASHC5 |
| GO:BP intracellular protein localization | 0.00208 | AP1B1, EHD1, EXOC3, ITSN1, NBAS, TJP2, USO1, VPS11, VPS18, VPS53, WASHC4, WASHC5 |
| GO:BP establishment of protein localization | 0.00252 | AP1B1, EHD1, EXOC3, ITSN1, NBAS, USO1, VPS11, VPS18, VPS53, WASHC4, WASHC5 |
| GO:CC vesicle tethering complex | 0.00362 | EXOC3, NBAS, VPS11, VPS18, VPS53 |
| GO:CC cytoplasmic vesicle membrane | 0.0041 | AP1B1, EHD1, EXOC3, USO1, VPS11, VPS18, VPS53, WASHC4, WASHC5 |
| GO:CC vesicle membrane | 0.00444 | AP1B1, EHD1, EXOC3, USO1, VPS11, VPS18, VPS53, WASHC4, WASHC5 |
| GO:BP macromolecule localization | 0.00683 | AP1B1, EHD1, EXOC3, ITSN1, NBAS, TJP2, USO1, VPS11, VPS18, VPS53, WASHC4, WASHC5 |
| GO:CC endosome | 0.0104 | AP1B1, EHD1, ITSN1, VPS11, VPS18, VPS53, WASHC4, WASHC5 |
| GO:CC early endosome | 0.0345 | AP1B1, EHD1, VPS11, VPS18, WASHC4, WASHC5 |
| GO:BP establishment of localization in cell | 0.0366 | AP1B1, EHD1, EXOC3, ITSN1, USO1, VPS11, VPS18, VPS53, WASHC4, WASHC5 |
| GO:BP endosomal transport | 0.0404 | EHD1, ITSN1, VPS53, WASHC4, WASHC5 |

### STRING and hu.MAP

STRING provides strong pairwise support for VPS11-VPS18 and WASHC4-WASHC5, and supports EXOC3-VPS53 with a lower but still retained interaction score. These relationships are biologically coherent: VPS11 and VPS18 are shared components of CORVET and HOPS-related trafficking machinery, WASHC4 and WASHC5 are WASH-complex components, and EXOC3 belongs to the exocyst system. The STRING functional results (15 supplementary STRING terms; within-query FDR 1.08e-06–0.0073) reinforce vesicle, endosome, docking, transport, and localization functions, but their FDR values are supplementary and are not treated as global enrichment significance. hu.MAP independently places VPS11 with VPS18 in multiple complexes (hu.MAP huMAP3_08749.1) (hu.MAP huMAP3_13822.1) (hu.MAP huMAP3_12433.1) (hu.MAP huMAP3_12945.1), WASHC4 with WASHC5 in WASH-related complexes (hu.MAP huMAP3_05454.1)(hu.MAP huMAP3_06652.1)(hu.MAP huMAP3_08077.1)(hu.MAP huMAP3_10870.1)(hu.MAP huMAP3_12900.1), and AP1B1 with ITSN1 in several adaptor and endocytic assemblies (hu.MAP huMAP3_12394.1)(hu.MAP huMAP3_08540.1)(hu.MAP huMAP3_09107.1) (hu.MAP huMAP3_08320.1) (hu.MAP huMAP3_09403.1) (hu.MAP huMAP3_12376.1) (hu.MAP huMAP3_10876.1)(hu.MAP huMAP3_10762.1)(hu.MAP huMAP3_12918.1). The module therefore contains several recognizable machinery fragments, while many cross-system links are inferred from co-abundance rather than directly established physical interaction.

**STRING interactions (score >= 0.7)**: 3 of 91 gene pairs: EXOC3–VPS53 (0.773); VPS11–VPS18 (0.999); WASHC4–WASHC5 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Protein transport (FDR = 1.08e-06, 11 genes); Process Vesicle-mediated transport (FDR = 0.00018, 11 genes); Keyword Endosome (FDR = 0.00022, 7 genes); Process Protein localization (FDR = 0.00036, 12 genes); Process Protein transport (FDR = 0.00036, 11 genes); Component Cytoplasmic vesicle membrane (FDR = 0.001, 9 genes); Component Vesicle tethering complex (FDR = 0.001, 5 genes); Component Endosome (FDR = 0.0011, 8 genes); COMPARTMENTS Vesicle tethering complex (FDR = 0.0018, 5 genes); Process Vesicle organization (FDR = 0.0038, 6 genes); Component Early endosome (FDR = 0.0042, 6 genes); Component Endosome membrane (FDR = 0.0057, 6 genes); Process Transport (FDR = 0.0073, 12 genes); Process Vesicle docking (FDR = 0.0073, 4 genes); Process Establishment of localization in cell (FDR = 0.0073, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12394.1 (USO1, AP1B1, ITSN1; 3/98); huMAP3_05454.1 (WASHC5, WASHC4; 2/2); huMAP3_08749.1 (VPS11, VPS18; 2/9); huMAP3_13822.1 (VPS11, VPS18; 2/9); huMAP3_12433.1 (VPS11, VPS18; 2/11); huMAP3_12945.1 (VPS11, VPS18; 2/12); huMAP3_06652.1 (WASHC5, WASHC4; 2/14); huMAP3_08077.1 (WASHC5, WASHC4; 2/16); huMAP3_08540.1 (AP1B1, ITSN1; 2/19); huMAP3_10870.1 (WASHC5, WASHC4; 2/20); huMAP3_09107.1 (AP1B1, ITSN1; 2/23); huMAP3_08320.1 (AP1B1, ITSN1; 2/24); huMAP3_09403.1 (AP1B1, ITSN1; 2/26); huMAP3_12376.1 (AP1B1, ITSN1; 2/32); huMAP3_10876.1 (AP1B1, ITSN1; 2/40); huMAP3_12900.1 (WASHC5, WASHC4; 2/50); huMAP3_10762.1 (AP1B1, ITSN1; 2/62); huMAP3_12918.1 (AP1B1, ITSN1; 2/62)

### Novelty

The module should not be presented as a discovery of a new vesicle-trafficking pathway. Its central components and several pairwise relationships are already well established by gene function, STRING, and hu.MAP. What may be new is the coordinated co-abundance of these trafficking systems in a module shared by skin and testis, particularly the way endosomal, Golgi, tethering, WASH, adaptor, and exocyst-related genes are connected in this tissue pair. The sparse STRING connectivity and the partial overlap with hu.MAP complexes argue against claiming that the entire module is a known physical complex. Conversely, absence of a database interaction is not evidence of novelty, because co-abundance can reflect shared regulation, cell composition, or functional coordination. The cautious conclusion is that the biological machinery is established, whereas the tissue-pair module organization and its possible skin-testis relevance are potentially novel and require replication and experimental validation.

**Hypothesis.** Hypothesis: in both skin and testis, a conserved cellular program coordinates cargo entry, sorting, tethering, recycling, and delivery across endosomes, the Golgi, lysosomes, and the plasma membrane. VPS11-VPS18 may provide a tethering and endolysosomal core; WASHC4-WASHC5 may couple endosomal traffic to actin remodeling; AP1B1 and ITSN1 may select or internalize cargo; EXOC3 may support delivery to defined plasma-membrane sites; and NBAS, USO1, and VPS53 may connect Golgi, ER, and retrograde trafficking. EHD1 and TJP2 could reflect tissue-specific coupling to endocytic recycling and epithelial or cell-junction organization. This is a mechanistic hypothesis rather than proof of a single physical assembly. Testing it would require cell-type-resolved expression, perturbation of hub genes, and direct measurement of cargo movement or endosomal recycling in skin and testicular cell models.

### Important genes

#### VPS11

- **Related proteins** (co-abundance neighbors): VPS18 (0.82), EXOC3 (0.82), WASHC4 (0.82), RTCA (0.81); STRING partners: VPS18 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_08749.1, huMAP3_13822.1, huMAP3_12433.1, huMAP3_12945.1
- **Function (MyGene.info)**: VPS11 core subunit of CORVET and HOPS complexes. Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene encodes the human homolog of yeast class C Vps11 protein. The mammalian class C Vps proteins are predominantly associated with late…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 12 (0.723); neurodegenerative disease (0.527); POLR-related leukodystrophy (0.527); dystonia 32 (0.410); VPS11-related neurological disorder (0.370)
- **Europe PMC papers**: 849
- **Why important**: VPS11 is the strongest network hub in the module and connects to VPS18, EXOC3, WASHC4, and RTCA. It appears in nearly all primary vesicle, localization, tethering, membrane, endosome, and endosomal-transport terms (11 globally significant GO/KEGG terms, q_global 0.000601–0.0366; see the table), as well as all STRING supplementary terms (15 supplementary STRING terms; within-query FDR 1.08e-06–0.0073). It is a core component of CORVET and HOPS complexes, and its relationship with VPS18 is strongly supported by STRING and hu.MAP (hu.MAP huMAP3_08749.1) (hu.MAP huMAP3_13822.1) (hu.MAP huMAP3_12433.1) (hu.MAP huMAP3_12945.1). Its neurological disease associations and substantial literature support make it an informative mechanistic anchor rather than a generic marker.
- **Conclusion**: Established: VPS11 is a central endolysosomal trafficking component with strong functional, network, STRING, hu.MAP, and disease evidence. Hypothesis: its central position may organize the shared module by coupling endosomal maturation and lysosomal delivery to WASH and exocyst-associated trafficking in both tissues.

#### VPS18

- **Related proteins** (co-abundance neighbors): WASHC5 (0.83), VPS11 (0.82); STRING partners: VPS11 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_08749.1, huMAP3_13822.1, huMAP3_12433.1, huMAP3_12945.1
- **Function (MyGene.info)**: VPS18 core subunit of CORVET and HOPS complexes. Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene encodes the human homolog of yeast class C Vps18 protein. The mammalian class C Vps proteins are predominantly associated with late…
- **Diseases (Open Targets)**: neurodegenerative disease (0.541); COVID-19 (0.372); male infertility (0.190); neoplasm (0.091); ulcerative colitis (0.062)
- **Europe PMC papers**: 802
- **Why important**: VPS18 forms the strongest STRING-supported pair with VPS11 and repeatedly co-occurs with VPS11 in hu.MAP complexes (hu.MAP huMAP3_08749.1) (hu.MAP huMAP3_13822.1) (hu.MAP huMAP3_12433.1) (hu.MAP huMAP3_12945.1). It is represented across the primary vesicle transport, protein localization, vesicle membrane, tethering, endosome, and endosomal-transport terms (12 globally significant GO/KEGG terms, q_global 0.000601–0.0404; see the table), and across the STRING supplementary categories (15 supplementary STRING terms; within-query FDR 1.08e-06–0.0073). Its established role as a CORVET and HOPS component gives the module a defined endolysosomal core. HPA detects it in both tissues and identifies cell-type enhancement in Hofbauer cells and neutrophils, which may be relevant to tissue cellular composition.
- **Conclusion**: Established: VPS18 is a conserved endolysosomal tethering component that substantiates the module's vesicle-trafficking interpretation. Hypothesis: coordinated VPS11-VPS18 abundance may mark variation in endosome-to-lysosome capacity across specialized or immune-associated cells in skin and testis.

#### WASHC4

- **Related proteins** (co-abundance neighbors): VPS53 (0.83), SELENOO (0.83), VPS11 (0.82); STRING partners: WASHC5 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_05454.1, huMAP3_06652.1, huMAP3_08077.1, huMAP3_10870.1, huMAP3_12900.1
- **Function (MyGene.info)**: WASH complex subunit 4. This gene encodes a component of the WASH complex, which functions in the intracellular transport of endosomes. Mutations in this gene have been detected in individuals with autosomal recessive cognitive disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014].
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.611); Intellectual disability (0.345); mathematical ability (0.322); Abnormality of the skeletal system (0.148); corneal ulcer (0.140)
- **Europe PMC papers**: 116
- **Why important**: WASHC4 is a network bridge linking VPS53, SELENOO, and VPS11 and is paired with WASHC5 by STRING. It participates in most primary transport and localization terms and in the endosome and endosomal-transport terms (12 globally significant GO/KEGG terms, q_global 0.000601–0.0404; see the table). Its WASH-complex function connects endosomal trafficking to Arp2/3-dependent actin nucleation, while hu.MAP repeatedly places it with WASHC5 (hu.MAP huMAP3_05454.1)(hu.MAP huMAP3_06652.1)(hu.MAP huMAP3_08077.1)(hu.MAP huMAP3_10870.1)(hu.MAP huMAP3_12900.1). Its association with autosomal recessive intellectual disability adds disease relevance despite a more modest literature volume than the major trafficking hubs.
- **Conclusion**: Established: WASHC4 is a WASH-complex component with established endosomal and actin-remodeling functions and strong complex-level support. Hypothesis: WASHC4 may provide the actin-dependent remodeling interface that links the VPS tethering machinery to cargo recycling in the shared tissue module.

#### ITSN1

- **Related proteins** (co-abundance neighbors): NBAS (0.83), EHD1 (0.82), TJP2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_12394.1, huMAP3_08540.1, huMAP3_09107.1, huMAP3_08320.1, huMAP3_09403.1, huMAP3_12376.1, huMAP3_10876.1, huMAP3_10762.1, huMAP3_12918.1
- **Function (MyGene.info)**: intersectin 1. The protein encoded by this gene is a cytoplasmic membrane-associated protein that indirectly coordinates endocytic membrane traffic with the actin assembly machinery. In addition, the encoded protein may regulate the formation of clathrin-coated vesicles and could be involved in synaptic vesicle recycling. This protein has been shown to interact with dynamin, CDC42, SNAP23, SNAP25, SPIN90, EPS15,…
- **Diseases (Open Targets)**: hereditary disease (0.531); neurodevelopmental disorder (0.451); Autistic behavior (0.404); Intellectual disability (0.378); autosomal dominant non-syndromic intellectual disability (0.371)
- **Europe PMC papers**: 1094
- **Why important**: ITSN1 is a network connector linking NBAS, EHD1, and TJP2. It contributes to the primary vesicle, protein-localization, endosome, and endosomal-transport terms (4 globally significant GO/KEGG terms, q_global 0.000601–0.00252; see the table)(GO:BP macromolecule localization; q_global = 0.00683)(GO:CC endosome; q_global = 0.0104)(GO:BP establishment of localization in cell; q_global = 0.0366)(GO:BP endosomal transport; q_global = 0.0404). Its established roles in endocytosis, clathrin-coated vesicle formation, membrane-associated signaling, and coordination with actin machinery provide a mechanistic link between cargo internalization and downstream trafficking. hu.MAP repeatedly places ITSN1 with AP1B1 and broader adaptor or endocytic assemblies (hu.MAP huMAP3_12394.1)(hu.MAP huMAP3_08540.1)(hu.MAP huMAP3_09107.1) (hu.MAP huMAP3_08320.1) (hu.MAP huMAP3_09403.1) (hu.MAP huMAP3_12376.1) (hu.MAP huMAP3_10876.1)(hu.MAP huMAP3_10762.1)(hu.MAP huMAP3_12918.1). HPA reports cell-type enhancement in adipocytes, macrophages, and rod photoreceptors, with immune enhancement in eosinophils and non-classical monocytes.
- **Conclusion**: Established: ITSN1 is an endocytic and membrane-trafficking adaptor with strong annotation and complex-context support. Hypothesis: ITSN1 may connect tissue-specific cargo uptake to the conserved endosomal transport machinery, potentially explaining part of the shared skin-testis co-abundance pattern.

#### EHD1

- **Related proteins** (co-abundance neighbors): ITSN1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Plasma membrane; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EH domain containing 1. This gene belongs to a highly conserved gene family encoding EPS15 homology (EH) domain-containing proteins. The protein-binding EH domain was first noted in EPS15, a substrate for the epidermal growth factor receptor. The EH domain has been shown to be an important motif in proteins involved in protein-protein interactions and in intracellular sorting. The protein encoded by this gene is thought …
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.107); neoplasm (0.101); device complication (0.091); lung adenocarcinoma (0.079); osteosarcoma (0.074)
- **Europe PMC papers**: 1857
- **Why important**: EHD1 is directly connected to ITSN1 and appears in every primary term from vesicle transport through endosomal transport (12 globally significant GO/KEGG terms, q_global 0.000601–0.0404; see the table). It has established roles in endocytosis and endocytic recycling, making it particularly informative for the recycling arm of the module. HPA identifies tissue enhancement in testis and bone marrow and cell-group enrichment in early and late spermatids and neutrophils, providing a direct link to the tissue pair and to possible cellular substructure. Its disease evidence is less definitive than that of the VPS or WASH components, but its biological placement and literature support are substantial.
- **Conclusion**: Established: EHD1 is an endocytic-recycling factor with strong primary enrichment and a testis-associated HPA signal. Hypothesis: EHD1 may be a tissue-relevant output component that couples the conserved trafficking core to membrane recycling in spermatogenic cells and selected skin cell populations.

## Module 6

**Tissue pair**: skin and testis  
**Genes (16)**: MTHFD1, DDX46, EIF3C, MATR3, MTA2, NASP, PDCD6IP, PFAS, ATIC, RECQL, SF3A1, SF3B3, AARS1, NARS1, SYNE2, USP5

### Function

The strongest supported interpretation is a conserved nuclear RNA-processing and pre-mRNA-splicing module, centered on U2 spliceosome biology. The primary evidence is the globally corrected enrichment for the U2 snRNP (GO:CC U2 snRNP; q_global = 0.0417) and U2-type prespliceosome assembly (GO:BP U2-type prespliceosome assembly; q_global = 0.0417), both involving DDX46, SF3A1, and SF3B3. These genes have coherent molecular annotations: SF3A1 and SF3B3 are U2 snRNP components, while DDX46 is a DEAD-box RNA helicase involved in U2-type prespliceosome assembly. The network contains a particularly coherent spliceosomal subgraph linking these three genes, supported by strong STRING relationships and multiple hu.MAP complexes. Other module genes indicate complementary cellular programs rather than a single uniformly connected pathway: ATIC, PFAS, and MTHFD1 support purine and one-carbon metabolism; AARS1 and NARS1 support aminoacyl-tRNA charging; RECQL supports DNA replication and repair; EIF3C supports translation initiation; and MTA2, MATR3, USP5, PDCD6IP, NASP, and SYNE2 represent chromatin, RNA regulation, proteostasis, vesicle, nuclear-envelope, or structural functions. No STRING functional-enrichment term was reported, so the spliceosomal interpretation rests primarily on (GO:CC U2 snRNP; q_global = 0.0417) and (GO:BP U2-type prespliceosome assembly; q_global = 0.0417), with the remaining annotations providing biological context. Absence of additional enriched terms does not invalidate the module.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the HPA summary identifies only a single secreted gene, and the proteins are detected in both skin and testis. Most genes have low tissue specificity, which is consistent with broadly used intracellular machinery rather than a narrowly tissue-restricted program. The module is also not broadly blood-cell specific overall, although several genes show cell-type enhancement in erythrocyte progenitors, megakaryocytes, neutrophils, or eosinophils, and several show enhancement in epithelial or germ-cell populations. Therefore, blood contamination or a shared blood-cell population is not the leading interpretation, but cellular composition may contribute to the observed cross-tissue co-abundance. The presence of late spermatid, spermatocyte, Sertoli-cell, and other testis-associated single-cell signals is compatible with the shared module being expressed in particular cell populations within the tissues rather than representing a skin-and-testis-specific pathway.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC U2 snRNP | 0.0417 | DDX46, SF3A1, SF3B3 |
| GO:BP U2-type prespliceosome assembly | 0.0417 | DDX46, SF3A1, SF3B3 |

### STRING and hu.MAP

STRING provides six high-confidence pairwise relationships. The most coherent cluster is DDX46 with SF3A1 and SF3B3, matching the U2 snRNP and prespliceosome evidence in (GO:CC U2 snRNP; q_global = 0.0417) and (GO:BP U2-type prespliceosome assembly; q_global = 0.0417). STRING also supports AARS1 with NARS1 and links ATIC with MTHFD1 and PFAS, consistent with aminoacyl-tRNA and purine-related cellular processes. hu.MAP independently places DDX46, SF3A1, and SF3B3 together in several spliceosomal complexes (hu.MAP huMAP3_04549.1), (hu.MAP huMAP3_06511.1), and (hu.MAP huMAP3_08980.1). It places AARS1 and NARS1 together in (hu.MAP huMAP3_10302.1), and places ATIC with MTHFD1 in (hu.MAP huMAP3_12823.1). Additional complexes connect AARS1 or NARS1 with RECQL (hu.MAP huMAP3_10115.1), (hu.MAP huMAP3_10088.1), and (hu.MAP huMAP3_14982.1), while (hu.MAP huMAP3_14442.1) provides a broader mixed complex context. These results show that the module contains a well-supported spliceosomal core and smaller biochemical or macromolecular neighborhoods. The hu.MAP overlaps are partial rather than complete complex recovery, so they support shared machinery but do not establish that all module members form one physical complex.

**STRING interactions (score >= 0.7)**: 6 of 120 gene pairs: AARS1–NARS1 (0.947); ATIC–MTHFD1 (0.998); ATIC–PFAS (0.819); DDX46–SF3A1 (0.999); DDX46–SF3B3 (0.997); SF3A1–SF3B3 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10115.1 (NARS1, RECQL, AARS1; 3/14); huMAP3_04549.1 (SF3B3, SF3A1, DDX46; 3/52); huMAP3_06511.1 (SF3B3, SF3A1, DDX46; 3/79); huMAP3_08980.1 (SF3B3, SF3A1, DDX46; 3/97); huMAP3_12823.1 (MTHFD1, ATIC; 2/7); huMAP3_10302.1 (NARS1, AARS1; 2/9); huMAP3_10088.1 (NARS1, RECQL; 2/10); huMAP3_14982.1 (NARS1, RECQL; 2/28); huMAP3_14442.1 (ATIC, AARS1; 2/57)

### Novelty

The module is unlikely to represent a wholly new molecular mechanism because its central relationships are already established by STRING and hu.MAP, and the functions of its principal genes are well documented. Its potentially novel aspect is the conserved co-abundance organization across skin and testis: the fact sheet does not establish that this exact tissue-pair module, with this particular combination of spliceosomal, metabolic, translation, repair, and structural genes, has previously been described. That claim requires comparison with published tissue co-abundance studies and other network resources. Absence from STRING or hu.MAP would not by itself prove novelty, and here the strongest core relationships are present in those resources. A cautious conclusion is that the module may be a new tissue-level co-abundance configuration built from largely known molecular machinery, rather than a newly discovered protein complex or pathway.

**Hypothesis.** Hypothesis: the module reflects coordinated maintenance of gene expression and genome integrity in actively renewing or developmentally specialized cells shared between skin and testis. A U2 spliceosomal core composed of DDX46, SF3A1, and SF3B3 may coordinate pre-mRNA processing, while EIF3C and the aminoacyl-tRNA synthetases support downstream protein production. ATIC, PFAS, and MTHFD1 may provide nucleotide and one-carbon metabolic capacity needed for RNA synthesis, DNA replication, and cell proliferation; RECQL may help protect replicating genomes; NASP may support chromatin assembly; and SYNE2, MATR3, MTA2, USP5, and PDCD6IP may connect nuclear organization, RNA regulation, protein stability, or cell-structural processes. This is a mechanistic model rather than a demonstrated causal pathway. The co-abundance data cannot establish direct regulation, physical interaction among every module member, or whether the pattern arises from coordinated intracellular regulation versus shared cellular composition.

### Important genes

#### SF3A1

- **Related proteins** (co-abundance neighbors): SF3B3 (0.87), PFAS (0.83), MATR3 (0.82), MTA2 (0.81), EIF3C (0.80); STRING partners: DDX46 (0.999), SF3B3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_04549.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 has the highest network connectivity and weighted strength in the module and directly connects to SF3B3 and the module's spliceosomal neighborhood. It is a component of the SF3A complex and mature U2 snRNP, and it participates in spliceosome assembly, splice-site recognition, and pre-mRNA splicing. It is included in both primary terms (GO:CC U2 snRNP; q_global = 0.0417) and (GO:BP U2-type prespliceosome assembly; q_global = 0.0417), is supported by strong STRING links to DDX46 and SF3B3, and occurs in hu.MAP spliceosomal complexes (hu.MAP huMAP3_04549.1), (hu.MAP huMAP3_06511.1), and (hu.MAP huMAP3_08980.1). Its extensive literature record and disease associations make it a well-established biological anchor rather than a speculative marker.
- **Conclusion**: Established evidence supports SF3A1 as a central U2 spliceosome component and a principal anchor of this module. The module data support its importance for the shared co-abundance pattern, but do not show that SF3A1 drives the pattern or that it is uniquely responsible for tissue sharing.

#### SF3B3

- **Related proteins** (co-abundance neighbors): SF3A1 (0.87), EIF3C (0.84), MATR3 (0.83); STRING partners: DDX46 (0.997), SF3A1 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Nucleoli rim; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_04549.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: splicing factor 3b subunit 3. This gene encodes subunit 3 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); dengue disease (0.370); cervical cancer (0.189); cervical carcinoma (0.189); prostate cancer (0.111)
- **Europe PMC papers**: 965
- **Why important**: SF3B3 is part of the same highly coherent spliceosomal subgraph as SF3A1 and DDX46. It is a subunit of the SF3B complex and U2 snRNP, contributes to branch-site recognition and spliceosome conformational transitions, and is present in both globally corrected terms (GO:CC U2 snRNP; q_global = 0.0417) and (GO:BP U2-type prespliceosome assembly; q_global = 0.0417). Its strong STRING relationships and repeated hu.MAP placement in (hu.MAP huMAP3_04549.1), (hu.MAP huMAP3_06511.1), and (hu.MAP huMAP3_08980.1) provide convergent evidence that this is a genuine molecular neighborhood. It also has substantial literature and disease-oriented annotation.
- **Conclusion**: Established evidence identifies SF3B3 as a core component of the module's U2-splicing signal. Its co-abundance with SF3A1 and DDX46 is biologically coherent, while any tissue-specific or causal role beyond general spliceosome function remains a hypothesis.

#### DDX46

- **Related proteins** (co-abundance neighbors): EIF3C (0.81); STRING partners: SF3A1 (0.999), SF3B3 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_04549.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: DEAD-box helicase 46. This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribu…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); dengue disease (0.370); Hypercholesterolemia (0.203); lung adenocarcinoma (0.074); osteosarcoma (0.053)
- **Europe PMC papers**: 592
- **Why important**: DDX46 is directly represented in both primary terms (GO:CC U2 snRNP; q_global = 0.0417) and (GO:BP U2-type prespliceosome assembly; q_global = 0.0417) and is strongly connected by STRING to SF3A1 and SF3B3. Its DEAD-box helicase annotation provides a mechanistic explanation for RNA remodeling during U2-type prespliceosome assembly. It appears in the same multiple hu.MAP spliceosomal complexes (hu.MAP huMAP3_04549.1), (hu.MAP huMAP3_06511.1), and (hu.MAP huMAP3_08980.1), making it a key bridge between the enrichment result and the physical-complex evidence. Its disease associations and literature support a biologically important RNA-processing role.
- **Conclusion**: Established evidence supports DDX46 as a functional member of the U2 prespliceosome machinery and a critical interpretive anchor for this module. The data do not establish whether DDX46 activity is altered in skin or testis, or whether it mediates the cross-tissue co-abundance.

#### ATIC

- **Related proteins** (co-abundance neighbors): RECQL (0.84), NARS1 (0.83), SYNE2 (0.83); STRING partners: MTHFD1 (0.998), PFAS (0.819)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_12823.1, huMAP3_14442.1
- **Function (MyGene.info)**: 5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase. This gene encodes a bifunctional protein that catalyzes the last two steps of the de novo purine biosynthetic pathway. The N-terminal domain has phosphoribosylaminoimidazolecarboxamide formyltransferase activity, and the C-terminal domain has IMP cyclohydrolase activity. A mutation in this gene results in AICA-ribosiduria. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: AICA-ribosiduria (0.708); cancer (0.571); Intellectual disability (0.463); lung adenocarcinoma (0.390); anaplastic large cell lymphoma (0.374)
- **Europe PMC papers**: 5200
- **Why important**: ATIC is a highly connected metabolic node linked to RECQL, NARS1, and SYNE2 in the module. It catalyzes the final reactions of de novo purine biosynthesis, has a strong STRING relationship with MTHFD1, and is included with MTHFD1 in hu.MAP complex (hu.MAP huMAP3_12823.1). Its disease associations include AICA-ribosiduria and other disorders, and its extensive literature indicates that it is a well-characterized metabolic enzyme. It therefore represents a substantial non-spliceosomal branch of the module.
- **Conclusion**: Established evidence supports ATIC as a purine-biosynthetic component and as part of a metabolic neighborhood involving MTHFD1 and PFAS. Its connection to the spliceosomal core is network-level evidence only; a direct role in coordinating splicing with metabolism is a hypothesis.

#### RECQL

- **Related proteins** (co-abundance neighbors): ATIC (0.84), MTHFD1 (0.83), SYNE2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_10115.1, huMAP3_10088.1, huMAP3_14982.1
- **Function (MyGene.info)**: RecQ like helicase. The protein encoded by this gene is a member of the RecQ DNA helicase family. DNA helicases are enzymes involved in various types of DNA repair, including mismatch repair, nucleotide excision repair and direct repair. The encoded protein is involved in the processing of Holliday junctions, the suppression of sister chromatid exchanges, telomere maintenance, and is required for genotoxic stress res…
- **Diseases (Open Targets)**: RECON progeroid syndrome (0.595); hereditary neoplastic syndrome (0.505); obesity disorder (0.404); myofibrillar myopathy 8 (0.334); hereditary breast ovarian cancer syndrome (0.328)
- **Europe PMC papers**: 954
- **Why important**: RECQL occupies a connective position linking ATIC, MTHFD1, and SYNE2, and it occurs with NARS1 in several hu.MAP contexts (hu.MAP huMAP3_10115.1), (hu.MAP huMAP3_10088.1), and (hu.MAP huMAP3_14982.1). Its established function as a RecQ-family DNA helicase includes DNA repair, replication-fork processing, recombination, Holliday-junction processing, and telomere maintenance. Its disease associations include progeroid and hereditary neoplastic syndromes. These properties make it important for interpreting the module as extending beyond RNA processing into genome maintenance.
- **Conclusion**: Established evidence supports RECQL as a DNA-repair and replication factor connected to the module's metabolic and structural neighborhood. The proposed coordination between RECQL-mediated genome maintenance and the spliceosomal core is plausible but not demonstrated by the supplied data.

## Module 7

**Tissue pair**: skin and testis  
**Genes (7)**: CAPRIN1, DDX5, DYNC1H1, EXOC4, IPO11, NEK9, TXNRD1

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established pathway assignment from enrichment. The individual gene annotations instead point to a coordinated intracellular program involving cell-cycle regulation, RNA processing and translation control, nucleocytoplasmic transport, microtubule-based transport, vesicle trafficking, and redox homeostasis. NEK9 is the most connected network node and links TXNRD1, CAPRIN1, DDX5, and EXOC4, while EXOC4 connects the NEK9-centered portion to DYNC1H1. The module is therefore best interpreted as a composite cellular machinery module rather than as evidence for one narrowly defined biochemical pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: no member is annotated as secreted, and all members have detected protein in both skin and testis. Most genes have low tissue specificity and low immune-cell specificity, arguing against a module primarily driven by circulating plasma proteins or broad blood-cell contamination. One gene is immune-cell enhanced for NK cells, but this is not a module-wide pattern. Most genes are cell-type enhanced in distinct cell types, including spermatids or spermatocytes, epithelial cells, endothelial cells, photoreceptors, and cardiomyocytes. The shared skin-testis signal could therefore reflect conserved intracellular programs or shared cellular states, with a possible contribution from specific cell populations, rather than a uniform tissue-specific secretory program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was detected among the module members, and STRING supplied no functional-enrichment result. Thus, the co-abundance edges are not independently supported by the reported STRING interaction network. hu.MAP provides the main external complex evidence: DDX5 and CAPRIN1 co-occur as module members in (hu.MAP huMAP3_05711.1), (hu.MAP huMAP3_07909.1), (hu.MAP huMAP3_09754.1), (hu.MAP huMAP3_10631.1), and (hu.MAP huMAP3_11111.1). However, each complex contains many additional proteins and only this pair is shared with the module, so hu.MAP supports a relationship between DDX5 and CAPRIN1 but does not establish the entire module as one physical complex. The lack of STRING links and the limited hu.MAP overlap suggest that the module is more likely to represent coordinated abundance across cellular processes than a single well-defined physical assembly.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05711.1 (DDX5, CAPRIN1; 2/8); huMAP3_07909.1 (DDX5, CAPRIN1; 2/8); huMAP3_09754.1 (DDX5, CAPRIN1; 2/9); huMAP3_10631.1 (DDX5, CAPRIN1; 2/28); huMAP3_11111.1 (DDX5, CAPRIN1; 2/29)

### Novelty

The conserved co-abundance pattern across skin and testis may be a novel systems-level observation, because the reported module edges lack high-confidence STRING support and most module genes have no reported hu.MAP membership. Nevertheless, absence from STRING or hu.MAP does not prove biological novelty: co-abundance can arise from shared regulation, cell-state composition, or indirect functional coupling, and incomplete reference networks can miss real associations. The strongest defensible conclusion is that this particular cross-tissue co-abundance organization is not explained by an already established interaction complex in the supplied resources, while its component functions are individually well established.

**Hypothesis.** Hypothesis: the module reflects a coordinated intracellular state in which NEK9-linked cell-cycle control is coupled to RNA handling and translation regulation through DDX5 and CAPRIN1, while EXOC4 and DYNC1H1 support vesicle and microtubule-dependent transport, IPO11 supports nuclear import, and TXNRD1 buffers redox stress. In testis this state could accompany germ-cell development, and in skin it could support proliferative, transport, or stress-adaptive epithelial processes. This is a mechanistic hypothesis based on the co-abundance structure and known gene functions, not an experimentally demonstrated pathway.

### Important genes

#### NEK9

- **Related proteins** (co-abundance neighbors): TXNRD1 (0.89), CAPRIN1 (0.83), DDX5 (0.82), EXOC4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NIMA related kinase 9. This gene encodes a member of the NimA (never in mitosis A) family of serine/threonine protein kinases. The encoded protein is activated in mitosis and, in turn, activates other family members during mitosis. This protein also mediates cellular processes that are essential for interphase progression. [provided by RefSeq, Jul 2016].
- **Diseases (Open Targets)**: NEK9-related lethal skeletal dysplasia (0.713); arthrogryposis, Perthes disease, and upward gaze palsy (0.641); nevus comedonicus syndrome (0.632); hereditary disease (0.416); neurodegenerative disease (0.380)
- **Europe PMC papers**: 754
- **Why important**: NEK9 is the most connected node in the module and links the kinase, RNA-associated, vesicle-associated, and redox-associated parts of the network. Its established function includes activation of mitotic processes and regulation of interphase progression. It also has disease associations involving skeletal development and other hereditary conditions, together with substantial literature support.
- **Conclusion**: Established evidence supports NEK9 as the network organizer and a regulator of cell-cycle biology. The hypothesis that NEK9 coordinates the other module processes in skin and testis is plausible from its network position but is not demonstrated by the supplied interaction or enrichment evidence.

#### DDX5

- **Related proteins** (co-abundance neighbors): NEK9 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_05711.1, huMAP3_07909.1, huMAP3_09754.1, huMAP3_10631.1, huMAP3_11111.1
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 is a well-studied RNA helicase involved in RNA structural remodeling, transcriptional coregulation, alternative splicing, and small noncoding RNA processing. It is one of the two module members repeatedly represented together in the hu.MAP complexes (hu.MAP huMAP3_05711.1), (hu.MAP huMAP3_07909.1), (hu.MAP huMAP3_09754.1), (hu.MAP huMAP3_10631.1), and (hu.MAP huMAP3_11111.1), and it has extensive literature and disease-related investigation.
- **Conclusion**: Established evidence supports DDX5 as an RNA-processing and gene-regulatory component, with additional support for association with CAPRIN1 in hu.MAP. Its proposed role as a mediator connecting RNA regulation to the broader co-abundance program remains a hypothesis.

#### CAPRIN1

- **Related proteins** (co-abundance neighbors): NEK9 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_05711.1, huMAP3_07909.1, huMAP3_09754.1, huMAP3_10631.1, huMAP3_11111.1
- **Function (MyGene.info)**: cell cycle associated protein 1. Enables RNA binding activity. Predicted to be involved in negative regulation of translation and positive regulation of dendritic spine morphogenesis. Located in cell leading edge and cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder with language impairment, autism, and attention deficit-hyperactivity disorder (0.692); neurodegeneration, childhood-onset, with cerebellar ataxia and cognitive decline (0.677); complex neurodevelopmental disorder (0.370); juvenile myoclonic epilepsy (0.340); Seizure (0.333)
- **Europe PMC papers**: 1194
- **Why important**: CAPRIN1 is directly connected to the central NEK9 node and repeatedly co-occurs with DDX5 in the hu.MAP complexes (hu.MAP huMAP3_05711.1), (hu.MAP huMAP3_07909.1), (hu.MAP huMAP3_09754.1), (hu.MAP huMAP3_10631.1), and (hu.MAP huMAP3_11111.1). Its established annotations include RNA binding, negative regulation of translation, stress-granule assembly, mRNA decapping regulation, and membraneless organelle assembly. It is also cell-type enhanced in early spermatids and late primary spermatocytes, making it especially relevant to the testis component.
- **Conclusion**: Established evidence supports CAPRIN1 as an RNA and translation-control factor with a plausible germ-cell connection. The hypothesis that CAPRIN1 helps couple germ-cell RNA regulation to the wider module is consistent with the evidence but cannot be claimed as a demonstrated mechanism.

#### DYNC1H1

- **Related proteins** (co-abundance neighbors): IPO11 (0.81), EXOC4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 1 heavy chain 1. Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polyp…
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy without contractures (0.816); intellectual disability, autosomal dominant 13 (0.815); Charcot-Marie-Tooth disease axonal type 2O (0.799); autosomal dominant non-syndromic intellectual disability (0.634); hereditary disease (0.545)
- **Europe PMC papers**: 1731
- **Why important**: DYNC1H1 encodes the cytoplasmic dynein heavy chain and is connected in the module to IPO11 and EXOC4. Its established functions include microtubule-based movement, organelle and protein transport, spindle organization, nuclear migration, and retrograde axonal transport. It has extensive literature and strong disease associations involving neuromuscular and neurodevelopmental disorders.
- **Conclusion**: Established evidence supports DYNC1H1 as the module's principal long-range microtubule motor component. Its participation in a shared skin-testis transport state is a reasonable hypothesis, but the supplied data do not establish a direct physical or regulatory connection to the other module members.

#### EXOC4

- **Related proteins** (co-abundance neighbors): NEK9 (0.80), DYNC1H1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exocyst complex component 4. The protein encoded by this gene is a component of the exocyst complex, a multiple protein complex essential for targeting exocytic vesicles to specific docking sites on the plasma membrane. Though best characterized in yeast, the component proteins and functions of exocyst complex have been demonstrated to be highly conserved in higher eukaryotes. At least eight components of the exocyst complex,…
- **Diseases (Open Targets)**: alcohol drinking (0.484); intelligence (0.394); neurodegenerative disease (0.356); major depressive disorder (0.353); mathematical ability (0.322)
- **Europe PMC papers**: 582
- **Why important**: EXOC4 connects NEK9 and DYNC1H1 and encodes a component of the conserved exocyst complex. Its established functions include vesicle docking, exocytosis, Golgi-to-plasma-membrane transport, cytokinesis, autophagy regulation, and cilium assembly. Its position provides a bridge between cell-cycle-associated and transport-associated features of the module.
- **Conclusion**: Established evidence supports EXOC4 as a vesicle-trafficking and membrane-targeting factor. The hypothesis that it links dynein-dependent transport with NEK9-associated cellular regulation is suggested by the co-abundance edges but is not independently confirmed by STRING or hu.MAP evidence.

## Module 8

**Tissue pair**: skin and testis  
**Genes (11)**: DHX9, ADAR, IARS1, KARS1, LARS1, QARS1, RARS1, CCT5, CCT3, CCT7, CCT8

### Function

The module is best interpreted as a conserved intracellular gene-expression and protein-homeostasis program. Its strongest primary evidence is the enrichment of intracellular protein-containing complexes (GO:CC intracellular protein-containing complex; q_global = 6.15e-07), the CCT chaperonin complex (4 globally significant GO/KEGG terms, q_global 5.09e-05–0.0134; see the table), aminoacyl-tRNA synthetase activity and tRNA aminoacylation (4 globally significant GO/KEGG terms, q_global 2.45e-05–0.00157; see the table), and broader nucleic-acid, RNA, translation, and protein-biosynthetic processes (6 globally significant GO/KEGG terms, q_global 0.000243–0.05; see the table). The CCT subunits support ATP-dependent folding of newly synthesized proteins, whereas the synthetase group supports accurate translation. ADAR and DHX9 add RNA editing, RNA unwinding, RNA processing, and nuclear RNA regulation. The telomerase, Cajal-body, fertilization, and sperm-recognition terms (41 globally significant GO/KEGG terms, q_global 1.44e-05–0.0159; see the table) are statistically supported but should be interpreted cautiously: they are driven largely by the CCT subunits and do not by themselves establish a specialized reproductive or telomere-specific role for the entire module. The most coherent functional interpretation is coordinated protein folding, translation, and RNA handling in highly biosynthetically active cells.

**Cell composition.** This is not a plasma-protein or conventional secreted-protein module. HPA reports intracellular or nuclear locations for the annotated proteins, with only a single secretome flag in the module summary and no indication that the module is dominated by extracellular proteins. Every module gene is detected in both skin and testis, while all have low tissue specificity. Several genes are enhanced in spermatogenic cell types, including early or late spermatids and late primary spermatocytes, but the module also includes broadly expressed housekeeping-type machinery. HPA reports low immune-cell specificity for every gene, with no enriched blood-cell category, so a blood-cell explanation is not favored by this evidence. The shared skin-testis signal may therefore reflect ubiquitous biosynthetic machinery, with additional contribution from germ-cell abundance or activity in testis, rather than a tissue-specific secretory program.

**GO/KEGG enrichment**: 76 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC intracellular protein-containing complex | 6.15e-07 | CCT3, CCT5, CCT7, CCT8, DHX9, IARS1, KARS1, LARS1, QARS1, RARS1 |
| GO:BP protein localization to nuclear body | 1.44e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 1.44e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 1.44e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 1.44e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 1.44e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 1.44e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 1.44e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 2.45e-05 | IARS1, KARS1, LARS1, QARS1, RARS1 |
| GO:CC chaperonin-containing T-complex | 5.09e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomere maintenance via telomerase | 5.09e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 5.09e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to Cajal body | 5.09e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 5.09e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 5.09e-05 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING supports three internally coherent components. The CCT genes CCT3, CCT5, CCT7, and CCT8 form a densely connected chaperonin group, and the five synthetases IARS1, KARS1, LARS1, QARS1, and RARS1 form a densely connected aminoacyl-tRNA synthetase group. ADAR and DHX9 form a separate high-confidence RNA-processing connection, with KARS1 linking that pair to the synthetase group in the module graph. The STRING functional results independently support ATP binding, the aminoacyl-tRNA synthetase multienzyme complex, and the TCP-1 chaperonin family (15 supplementary STRING terms; within-query FDR 1.32e-05–0.00021), although these are supplementary rather than globally corrected enrichment evidence. hu.MAP identifies the synthetases together in multisynthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1) and the CCT genes together in several CCT-related complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). Thus, much of the network is supported by established physical or complex-level biology. The remaining cross-component links are weaker as mechanistic evidence and may represent co-abundance coordination, shared cellular demand, or indirect regulation rather than one physical complex.

**STRING interactions (score >= 0.7)**: 17 of 55 gene pairs: ADAR–DHX9 (0.922); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999); IARS1–KARS1 (0.999); IARS1–LARS1 (0.999); IARS1–QARS1 (0.999); IARS1–RARS1 (0.999); KARS1–LARS1 (0.999); KARS1–QARS1 (0.999); KARS1–RARS1 (0.999); LARS1–QARS1 (0.999); LARS1–RARS1 (0.999); QARS1–RARS1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword ATP-binding (FDR = 1.32e-05, 10 genes); Component aminoacyl-tRNA synthetase multienzyme complex (FDR = 1.6e-05, 5 genes); COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex (FDR = 2.37e-05, 5 genes); Pfam TCP-1/cpn60 chaperonin family (FDR = 3.85e-05, 4 genes); Component Chaperonin-containing T-complex (FDR = 5.54e-05, 4 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 5.78e-05, 4 genes); Function ATP binding (FDR = 6.39e-05, 10 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 0.00014, 5 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 0.00016, 4 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 0.00016, 4 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 0.00016, 4 genes); InterPro GroEL-like apical domain superfamily (FDR = 0.00016, 4 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 0.00016, 4 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 0.00016, 4 genes); Function aminoacyl-tRNA ligase activity (FDR = 0.00021, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (IARS1, QARS1, RARS1, KARS1, LARS1; 5/14); huMAP3_13688.1 (IARS1, QARS1, RARS1, KARS1, LARS1; 5/14); huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8)

### Novelty

The individual functions and two major physical assemblies are not new: the CCT chaperonin and multisynthetase complexes are already represented by STRING and hu.MAP, and the ADAR-DHX9 relationship is also supported by STRING. Consequently, the module should not be presented as discovery of a previously unknown complex or pathway. Its potentially novel aspect is the reproducible co-abundance of these established translation, folding, and RNA-processing components across skin and testis. That cross-tissue organization could be a useful systems-level observation, but absence from a particular database would not prove novelty. Demonstrating novelty would require independent cohorts, preservation testing, comparison with existing tissue co-expression resources, and experimental or perturbational validation of the proposed cross-component coordination.

**Hypothesis.** Hypothesis: the module represents a shared biosynthetic stress-buffering program that couples aminoacyl-tRNA charging with CCT-mediated folding and RNA quality control. In cells with substantial protein production, the synthetase assembly could sustain translational fidelity, CCT could fold newly synthesized client proteins, and the ADAR-DHX9 pair could regulate or process structured RNA and RNA-DNA intermediates. In testis, enhanced representation in spermatogenic populations may reflect the high demand for protein synthesis and remodeling during germ-cell differentiation; in skin, the same broadly expressed machinery may reflect routine renewal and proteostasis. The telomerase and Cajal-body annotations suggest a possible connection to nuclear RNA localization and genome maintenance, but that extension remains a hypothesis rather than proof of a dedicated telomere mechanism.

### Important genes

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT8 (0.93), CCT7 (0.88), CCT3 (0.84); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is a central member of the CCT subnetwork, with strong connections to CCT3, CCT7, and CCT8 and membership in multiple hu.MAP CCT-related complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). Its primary annotations support ATP-dependent chaperone-mediated protein folding, while its HPA profile places it in both tissues and enhances it in late primary spermatocytes. It has an established disease association with hereditary sensory and autonomic neuropathy with spastic paraplegia, and its literature base is extensive.
- **Conclusion**: Established evidence supports CCT5 as a core structural and functional component of the chaperonin arm of the module. A role in supporting proteome remodeling during spermatogenesis or skin renewal is plausible from the co-abundance and HPA context, but the module does not establish a tissue-specific CCT5 mechanism.

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT5 (0.93), CCT7 (0.91), CCT3 (0.85); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is one of the strongest-connected CCT members in the module and links directly to CCT3, CCT5, and CCT7. It is represented across the CCT, chaperone, nuclear-body, and telomerase-related primary annotations (62 globally significant GO/KEGG terms, q_global 6.15e-07–0.0442; see the table). HPA detects it in skin and testis and reports localization compatible with nucleoplasm and sperm structural regions. It also has a substantial literature base and cancer-related Open Targets associations.
- **Conclusion**: Established evidence supports CCT8 as a core CCT subunit and a plausible contributor to folding and nuclear-body biology. Its sperm-region localization and telomerase-related annotations motivate a reproductive-cell hypothesis, but they do not demonstrate that CCT8 directly controls telomerase in this module.

#### IARS1

- **Related proteins** (co-abundance neighbors): LARS1 (0.88), KARS1 (0.86), RARS1 (0.81); STRING partners: KARS1 (0.999), LARS1 (0.999), QARS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in skin, testis
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Isoleucine-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family and has been identified as a …
- **Diseases (Open Targets)**: growth retardation, intellectual developmental disorder, hypotonia, and hepatopathy (0.733); Abnormality of the skeletal system (0.332); microcephaly (0.289); Global developmental delay (0.289); Hallux valgus (0.184)
- **Europe PMC papers**: 184
- **Why important**: IARS1 is a highly connected member of the synthetase subnetwork and connects to KARS1, LARS1, QARS1, and RARS1 in STRING. It belongs to both hu.MAP multisynthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1) and contributes to the globally supported aminoacyl-tRNA and translation evidence (11 globally significant GO/KEGG terms, q_global 2.45e-05–0.05; see the table). It has a disease association involving developmental, skeletal, and hepatopathy phenotypes and a well-established enzymatic function, although its literature volume is smaller than that of the CCT genes.
- **Conclusion**: Established evidence supports IARS1 as a functional anchor of the translation-support arm. Its inclusion argues that the module is not merely a generic CCT expression signal. A contribution to translational fidelity in germ cells or renewing skin is a reasonable hypothesis, not a demonstrated tissue-specific function.

#### ADAR

- **Related proteins** (co-abundance neighbors): DHX9 (0.84), KARS1 (0.80); STRING partners: DHX9 (0.922)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR provides the module with a distinct RNA-editing function. It is connected to DHX9 by STRING and contributes to the primary RNA, nucleic-acid, gene-expression, and nuclear-localization evidence (10 globally significant GO/KEGG terms, q_global 0.000173–0.0442; see the table). HPA enhances it in neutrophils but reports low immune-cell specificity overall, and it is detected in both tissues. ADAR has extensive literature and strong disease associations involving Aicardi-Goutieres syndrome, interferonopathy, and dyschromatosis symmetrica hereditaria.
- **Conclusion**: Established evidence supports ADAR as the principal RNA-editing and innate-RNA-regulatory component of the module. Its connection to the translation and chaperone arms is not sufficient to prove a single physical assembly; coordinated RNA quality control is a plausible interpretation that requires validation.

#### DHX9

- **Related proteins** (co-abundance neighbors): ADAR (0.84); STRING partners: ADAR (0.922)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is the module's ATP-dependent RNA and DNA-RNA helicase component, with a STRING connection to ADAR and primary annotations for nucleic-acid metabolism, RNA localization, gene expression, and translation-related processes (23 globally significant GO/KEGG terms, q_global 6.15e-07–0.05; see the table). It is nuclear and cytoplasmic, detected in both tissues, has extensive literature, and is associated with developmental and neurodegenerative disease phenotypes.
- **Conclusion**: Established evidence supports DHX9 as an RNA-structure and nucleic-acid regulatory component that complements ADAR. Its position does not establish direct physical coupling to the CCT or synthetase assemblies, so any model in which it coordinates the whole module remains provisional.

## Module 9

**Tissue pair**: skin and testis  
**Genes (14)**: DPYSL3, EHD2, AGL, GMPR2, HSPA2, ISYNA1, KANK2, PRKCA, LRBA, ALDH6A1, IGF2R, MYLK, OXR1, PALS2

### Function

The module does not support a single statistically established GO or KEGG function: no globally significant GO/KEGG term passed global correction. Its gene content instead suggests a composite cellular program involving cytoskeletal organization, membrane trafficking, smooth-muscle or contractile biology, intracellular signaling, intermediary metabolism, and testis-associated proteostasis. EHD2 is the principal network connector and links membrane-associated trafficking biology with MYLK, KANK2, ISYNA1, GMPR2, PALS2, and HSPA2. MYLK and KANK2 support an actomyosin and cell-polarity interpretation, while PRKCA and DPYSL3 suggest signaling and cytoskeletal remodeling. ALDH6A1, AGL, ISYNA1, and GMPR2 contribute mitochondrial, glycogen, inositol, and purine metabolic dimensions. These annotations are mechanistic clues rather than a globally validated enrichment result.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of its genes is classified as secreted. It is also not uniformly blood-cell specific. HPA profiles show a mixture of low tissue specificity, tissue-enhanced, and group-enriched genes, with recurring associations to testis, skeletal muscle, brain, and stromal or smooth-muscle-related cell types. Several genes have immune-cell enhancement, including associations with neutrophils, basophils, eosinophils, T-reg cells, or naive B cells, but other genes are not detected in immune cells or have low immune specificity. The shared signal could therefore reflect common stromal, smooth-muscle, vascular, contractile, or specialized testicular cell populations in the sampled tissues, rather than a blood or plasma-protein artifact. Protein detection is frequent in both tissues, but the differing tissue-specific immunohistochemistry patterns caution against interpreting the module as a uniform skin-testis program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and STRING functional enrichment was absent. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated here as established physical interactions or membership in a known multiprotein complex. The absence of STRING and hu.MAP support does not invalidate the module; it indicates that the observed coordination may reflect shared cell composition, co-regulation, parallel processes, or interactions that are tissue-specific, transient, indirect, or incompletely curated. The apparent network structure should therefore be treated as a co-abundance framework rather than a protein-interaction map.

**STRING interactions (score >= 0.7)**: 0 of 91 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel tissue-pair co-abundance pattern, but it cannot be declared a new molecular complex or a newly discovered pathway. The case for novelty is that the module lacks high-confidence STRING relationships, lacks a shared hu.MAP complex, and has no globally significant GO or KEGG term. However, absence from these resources is not proof of novelty. Several component genes have substantial prior literature and established biological functions, so the likely novel aspect is their coordinated abundance across skin and testis, possibly reflecting a shared cellular context, rather than the individual gene functions. Replication in independent datasets, cell-type-aware analyses, and experimental validation would be required to establish a genuinely new biological mechanism.

**Hypothesis.** Hypothesis: the module represents a shared structural and metabolic state of specialized contractile or stromal cells present in skin and testis. In this model, EHD2 coordinates membrane organization and endocytic recycling with actin-associated components; MYLK and KANK2 support contractility, cell polarity, and actin regulation; PRKCA and DPYSL3 provide signaling and cytoskeletal remodeling; and ALDH6A1, AGL, ISYNA1, and GMPR2 support the metabolic demands of the state. HSPA2 and testis-associated expression may indicate an added reproductive-cell or proteostasis component, while immune-cell annotations could reflect limited sample admixture or shared vascular and stromal contexts. This is a hypothesis generated from co-abundance and annotation concordance, not an established pathway.

### Important genes

#### EHD2

- **Related proteins** (co-abundance neighbors): MYLK (0.92), ISYNA1 (0.83), GMPR2 (0.82), PALS2 (0.82), HSPA2 (0.81), KANK2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EH domain containing 2. This gene encodes a member of the EH domain-containing protein family. These proteins are characterized by a C-terminal EF-hand domain, a nucleotide-binding consensus site at the N terminus and a bipartite nuclear localization signal. The encoded protein interacts with the actin cytoskeleton through an N-terminal domain and also binds to an EH domain-binding protein through the C-terminal EH domai…
- **Diseases (Open Targets)**: disorder of patella (0.201); neuromuscular disease (0.201); muscular disease (0.201); triple-negative breast carcinoma (0.095); breast cancer (0.094)
- **Europe PMC papers**: 1131
- **Why important**: EHD2 has the strongest network connectivity and links most of the module's apparent branches, including actomyosin, membrane, metabolic, and testis-associated genes. Its established functions in endocytosis, endocytic recycling, plasma-membrane organization, and actin-related processes make it a plausible structural organizer. Its disease associations include muscular and neuromuscular disorders, and its literature support is substantial.
- **Conclusion**: Established: EHD2 is a membrane- and actin-associated trafficking protein and the central co-abundance connector in this module. Hypothesis: it may coordinate membrane remodeling with contractile or stromal-cell state in the shared tissues. The network position supports this interpretation, but does not demonstrate direct binding to its co-abundant partners.

#### MYLK

- **Related proteins** (co-abundance neighbors): EHD2 (0.92), IGF2R (0.82), ALDH6A1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin light chain kinase. This gene, a muscle member of the immunoglobulin gene superfamily, encodes myosin light chain kinase which is a calcium/calmodulin dependent enzyme. This kinase phosphorylates myosin regulatory light chains to facilitate myosin interaction with actin filaments to produce contractile activity. This gene encodes both smooth muscle and nonmuscle isoforms. In addition, using a separate promoter in an …
- **Diseases (Open Targets)**: aortic aneurysm, familial thoracic 7 (0.767); familial thoracic aortic aneurysm and aortic dissection (0.710); megacystis-microcolon-intestinal hypoperistalsis syndrome 1 (0.617); megacystis-microcolon-intestinal hypoperistalsis syndrome (0.597); Rare genetic vascular disease (0.483)
- **Europe PMC papers**: 10503
- **Why important**: MYLK is a highly connected module member with a tissue-enhanced profile in smooth muscle and seminal vesicle and cell-type associations with peritubular myoid cells, platelets, and hepatic stellate cells. Its established calcium-calmodulin-dependent phosphorylation of myosin regulatory light chains directly supports contractile activity, cell migration, and bleb formation. It has strong disease associations with familial aortic aneurysm and related vascular disorders and extensive literature support.
- **Conclusion**: Established: MYLK is a central regulator of actomyosin contractility and is biologically compatible with smooth-muscle or stromal-cell contributions. Hypothesis: MYLK may be one of the main functional drivers of the shared skin-testis co-abundance state. The module does not establish that its kinase activity is altered.

#### ALDH6A1

- **Related proteins** (co-abundance neighbors): OXR1 (0.86), PRKCA (0.85), MYLK (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 6 family member A1. This gene encodes a member of the aldehyde dehydrogenase protein family. The encoded protein is a mitochondrial methylmalonate semialdehyde dehydrogenase that plays a role in the valine and pyrimidine catabolic pathways. This protein catalyzes the irreversible oxidative decarboxylation of malonate and methylmalonate semialdehydes to acetyl- and propionyl-CoA. Methylmalonate semialdehyde dehydrogen…
- **Diseases (Open Targets)**: methylmalonate semialdehyde dehydrogenase deficiency (0.706); hereditary disease (0.413); alcohol drinking (0.158); atrial fibrillation (0.089); gastric cancer (0.076)
- **Europe PMC papers**: 1031
- **Why important**: ALDH6A1 connects the contractility-associated branch to OXR1 and PRKCA and is group-enriched in kidney and liver, with mitochondrial localization. Its established role in methylmalonate semialdehyde, valine, and pyrimidine catabolism provides a defined metabolic component that could support cells with specialized energetic demands. It is associated with methylmalonate semialdehyde dehydrogenase deficiency and has meaningful literature support.
- **Conclusion**: Established: ALDH6A1 is a mitochondrial catabolic enzyme and a disease-relevant metabolic gene. Hypothesis: its co-abundance with structural and signaling genes may indicate metabolic support for a contractile or specialized reproductive-cell state. The data do not establish metabolic flux or mitochondrial dysfunction in either tissue.

#### PRKCA

- **Related proteins** (co-abundance neighbors): ALDH6A1 (0.85), DPYSL3 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase C alpha. Protein kinase C (PKC) is a family of serine- and threonine-specific protein kinases that can be activated by calcium and the second messenger diacylglycerol. PKC family members phosphorylate a wide variety of protein targets and are known to be involved in diverse cellular signaling pathways. PKC family members also serve as major receptors for phorbol esters, a class of tumor promoters. Each mem…
- **Diseases (Open Targets)**: acute myeloid leukemia (0.554); hypertrophic cardiomyopathy (0.506); mast cell leukemia (0.475); systemic mastocytosis (0.471); heart failure (0.462)
- **Europe PMC papers**: 5462
- **Why important**: PRKCA occupies a branch connecting ALDH6A1 with DPYSL3 and contributes a signaling link between metabolism and cytoskeletal remodeling. Its established calcium- and diacylglycerol-responsive kinase activity, roles in protein phosphorylation, desmosome assembly, and endothelial proliferation, and its brain-enhanced HPA profile broaden the module beyond a simple muscle signature. It has extensive literature support and multiple disease associations, including hematologic and cardiac disorders.
- **Conclusion**: Established: PRKCA is a multifunctional signaling kinase with plausible effects on adhesion and cytoskeletal organization. Hypothesis: it may tune the structural or migratory state represented by the module. The co-abundance evidence does not identify its substrates or prove pathway activation.

#### AGL

- **Related proteins** (co-abundance neighbors): KANK2 (0.83), LRBA (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: amylo-alpha-1,6-glucosidase and 4-alpha-glucanotransferase. This gene encodes the glycogen debrancher enzyme which is involved in glycogen degradation. This enzyme has two independent catalytic activities which occur at different sites on the protein: a 4-alpha-glucotransferase activity and a amylo-1,6-glucosidase activity. Mutations in this gene are associated with glycogen storage disease although a wide range of enzymatic and clinical variability occurs…
- **Diseases (Open Targets)**: glycogen storage disease III (0.831); disorder of glycogen metabolism (0.768); glycogen storage disease XV (0.608); hereditary disease (0.507); Acute rhabdomyolysis (0.463)
- **Europe PMC papers**: 4441
- **Why important**: AGL links KANK2 and LRBA and is group-enriched in skeletal muscle and tongue, making it relevant to a possible contractile or muscle-associated cellular context. Its established glycogen-debranching activities connect the module to glycogen breakdown and nutrient-responsive metabolism. Its association with glycogen storage disease and rhabdomyolysis, together with substantial literature support, makes it biologically informative even though its network connectivity is not dominant.
- **Conclusion**: Established: AGL is a glycogen-metabolism enzyme with clear muscle and metabolic disease relevance. Hypothesis: coordinated AGL abundance may support energy provision for cells undergoing contractile or remodeling activity. The module does not demonstrate altered glycogen stores or AGL enzymatic activity.

#### HSPA2

- **Related proteins** (co-abundance neighbors): EHD2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Flagellar centriole, Annulus; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 2. Enables disordered domain specific binding activity; enzyme binding activity; and unfolded protein binding activity. Involved in negative regulation of inclusion body assembly and protein refolding. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: glaucoma (0.294); open-angle glaucoma (0.278); hypothyroidism (0.122); non-small cell lung carcinoma (0.100); neoplasm (0.094)
- **Europe PMC papers**: 2107
- **Why important**: HSPA2 is directly connected to EHD2 and has a tissue-enhanced profile in testis and skeletal muscle, with cell-type associations to primary spermatocytes and trophoblast-related populations. Its established roles in protein refolding, unfolded-protein responses, male meiotic division, spermatogenesis, and spermatid development make it particularly informative for the testis side of the shared module. It has substantial literature support, although its network position is peripheral.
- **Conclusion**: Established: HSPA2 is a reproductive-cell and proteostasis-associated chaperone with a strong testis-relevant biological context. Hypothesis: it may mark a specialized or stress-sensitive reproductive-cell component that is co-abundant with the broader membrane and cytoskeletal program. The data do not establish that the module reflects meiotic cells rather than another HSPA2-expressing cell population.

## Module 10

**Tissue pair**: skin and testis  
**Genes (6)**: ERLIN2, SIRAL1, RANGRF, PGP, PPP4R1, XPO7

### Function

No GO or KEGG term passed global correction, and STRING supplied no functional enrichment. Therefore, the module does not support a statistically established pathway-level function from enrichment alone. Its gene annotations suggest a heterogeneous intracellular module touching nuclear and nucleocytoplasmic transport, phosphatase-regulated signaling, endoplasmic-reticulum lipid and protein quality control, and glycerolipid metabolism. The co-abundance structure is a chain-like set of local associations rather than a densely connected pathway: PGP links to RANGRF and SIRAL1, RANGRF links to XPO7, XPO7 links to PPP4R1, and SIRAL1 links to ERLIN2. This supports a cautious interpretation as a coordinated cellular-state module rather than a demonstrated canonical complex or pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins, and it does not show a broad blood-cell signature. ERLIN2 is annotated as intracellular and membrane-associated, while the other genes are not secreted. Most genes have low tissue specificity, and protein detection is present in both skin and testis for nearly all genes with available data. Cell-type signals are mixed: PGP and RANGRF are enriched in late spermatids, SIRAL1 is enhanced in late primary spermatocytes and pituicytes or FSCs, and PPP4R1 is enhanced in several epithelial and immune-related cell types including neutrophils. Only one gene is tissue enhanced, in brain. Thus, shared cell states or broadly expressed intracellular programs are more plausible explanations than a blood-contamination explanation, although spermatogenic contribution should be considered for the testis signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair met the supplied STRING interaction threshold, and no STRING functional enrichment was present. No hu.MAP complex contained multiple module members. Consequently, the co-abundance edges are not independently supported here as established physical interactions or membership in a known multiprotein complex. This does not invalidate the module: co-abundance can reflect shared regulation, cell composition, compartmental state, or indirect functional coupling. It does mean that the network should not be described as a validated physical complex.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unrecognized co-abundance pattern, because its specific cross-tissue grouping is not recovered as a STRING-supported interaction network or a hu.MAP complex. However, absence from those resources does not establish biological novelty. Several component functions and disease associations are already established, particularly for PGP, RANGRF, XPO7, PPP4R1, and ERLIN2. The defensible conclusion is that the tissue-pair co-abundance configuration is potentially novel, while the individual molecular functions are not necessarily novel and require independent validation.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of intracellular trafficking and signaling across skin and testis, linking nuclear transport through XPO7 and RANGRF with PP4-associated regulation through PPP4R1, endoplasmic-reticulum lipid and protein quality control through ERLIN2, and metabolic or stress-related functions through PGP and SIRAL1. In testis, the association with spermatogenic cell types could indicate a shared cellular-state program during germ-cell differentiation; in skin, the same program may arise from broadly expressed epithelial or intracellular maintenance processes. This is a mechanistic hypothesis, not an established pathway assignment, because enrichment, STRING, and hu.MAP evidence do not independently confirm it.

### Important genes

#### XPO7

- **Related proteins** (co-abundance neighbors): RANGRF (0.83), PPP4R1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exportin 7. The transport of protein and large RNAs through the nuclear pore complexes (NPC) is an energy-dependent and regulated process. The import of proteins with a nuclear localization signal (NLS) is accomplished by recognition of one or more clusters of basic amino acids by the importin-alpha/beta complex; see MIM 600685 and MIM 602738. The small GTPase RAN (MIM 601179) plays a key role in NLS-dependen…
- **Diseases (Open Targets)**: atrial fibrillation (0.474); neurodegenerative disease (0.471); substance-related disorder (0.353); Alzheimer disease (0.351); Parkinson disease (0.351)
- **Europe PMC papers**: 450
- **Why important**: XPO7 is an internal connector between RANGRF and PPP4R1, placing it at the interface of the transport-related and phosphatase-related portions of the module. Its established function concerns nucleocytoplasmic transport, and its broad tissue profile is compatible with a shared cellular process rather than a tissue-exclusive marker. Its disease associations and literature support make it a strong mechanistic anchor.
- **Conclusion**: Established evidence supports XPO7 as a nuclear transport factor and as a central connector in this co-abundance graph. It is plausible, but unproven, that altered nucleocytoplasmic transport helps coordinate the module across skin and testis.

#### ERLIN2

- **Related proteins** (co-abundance neighbors): SIRAL1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ER lipid raft associated 2. This gene encodes a member of the SPFH domain-containing family of lipid raft-associated proteins. The encoded protein is localized to lipid rafts of the endoplasmic reticulum and plays a critical role in inositol 1,4,5-trisphosphate (IP3) signaling by mediating ER-associated degradation of activated IP3 receptors. Mutations in this gene are a cause of spastic paraplegia-18 (SPG18). Alternatively …
- **Diseases (Open Targets)**: hereditary spastic paraplegia 18 (0.757); spastic paraplegia 18b, autosomal recessive (0.659); hereditary spastic paraplegia (0.631); cancer (0.587); autosomal dominant complex spastic paraplegia (0.570)
- **Europe PMC papers**: 595
- **Why important**: ERLIN2 is the module's endoplasmic-reticulum component and is connected to SIRAL1. It participates in ER-associated degradation, IP3-receptor regulation, and lipid-related signaling, and it has a strong established association with hereditary spastic paraplegia. Its compartmental annotation provides a concrete cellular location for part of the proposed mechanism.
- **Conclusion**: Established evidence supports ERLIN2 as an ER lipid-raft and protein-quality-control factor with disease relevance. Its placement in this module suggests possible coupling to intracellular stress or lipid signaling, but the co-abundance data do not demonstrate that coupling.

#### PPP4R1

- **Related proteins** (co-abundance neighbors): XPO7 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase 4 regulatory subunit 1. This gene encodes one of several alternate regulatory subunits of serine/threonine protein phosphatase 4 (PP4). The protein features multiple HEAT repeats. This protein forms a complex with PP4RC. This complex may have a distinct role from other PP4 complexes, including regulation of HDAC3 (Zhang et al., PMID: 15805470). There is also a transcribed pseudogene on chromosome 20. Alternative splicing…
- **Diseases (Open Targets)**: neurodegenerative disease (0.435); mathematical ability (0.433); smoking initiation (0.387); lysosomal storage disease (0.333); Alzheimer disease (0.333)
- **Europe PMC papers**: 395
- **Why important**: PPP4R1 is the regulatory endpoint attached to XPO7 and is a regulatory subunit of protein phosphatase four. Its annotations support roles in protein phosphorylation and signal transduction, while its cell-type profile includes epithelial and neutrophil-associated signals. This makes it relevant for testing whether the module reflects signaling-state regulation rather than a physical complex.
- **Conclusion**: Established evidence supports PPP4R1 as a PP4 regulatory component involved in signaling-related regulation. Its module association may indicate coordinated phosphoregulation, but no direct interaction with the other module genes is established by the supplied STRING or hu.MAP results.

#### RANGRF

- **Related proteins** (co-abundance neighbors): PGP (0.88), XPO7 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAN guanine nucleotide release factor. This gene encodes a protein that has been shown to function as a guanine nucleotide release factor in mouse and to regulate the expression and function of the Nav1.5 cardiac sodium channel in human. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2010].
- **Diseases (Open Targets)**: cardiac arrhythmia (0.209); Rare familial disorder with hypertrophic cardiomyopathy (0.063); hypertrophic cardiomyopathy (0.063); familial isolated dilated cardiomyopathy (0.061); familial long QT syndrome (0.059)
- **Europe PMC papers**: 235
- **Why important**: RANGRF connects PGP to XPO7 and has a comparatively specific functional description involving Ran-related activity, membrane depolarization, cardiac channel regulation, and intracellular trafficking. Its enrichment in late spermatids makes it especially relevant to the tissue-pair context. Its cardiac disease associations provide an independently documented biological phenotype.
- **Conclusion**: Established evidence supports RANGRF as a regulator with roles in trafficking and ion-channel function, and the tissue data support relevance to spermatogenic cells. Its apparent bridge to XPO7 is a network observation; a shared transport mechanism remains a hypothesis.

#### PGP

- **Related proteins** (co-abundance neighbors): RANGRF (0.88), SIRAL1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Nuclear bodies; IHC detected in skin, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglycolate phosphatase. Enables glycerol-3-phosphatase activity and phosphoglycolate phosphatase activity. Involved in glycerol biosynthetic process; glycerophospholipid metabolic process; and negative regulation of gluconeogenesis. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.499); Abnormality of the skeletal system (0.356); lysosomal storage disease (0.347); neoplasm (0.118); cancer (0.117)
- **Europe PMC papers**: 16025
- **Why important**: PGP has the highest network connectivity in the module and links the RANGRF and SIRAL1 sides of the graph. Its annotated activities include phosphoglycolate and glycerol-3-phosphatase activity, glycerol biosynthesis, glycerophospholipid metabolism, and toxic-metabolite repair. It is tissue enhanced in brain and enriched in late spermatids, while its substantial literature and disease-area associations make it a useful metabolic and cellular-state marker.
- **Conclusion**: Established evidence supports PGP as a metabolic and metabolite-repair enzyme with relevance in spermatogenic cells. Its central position makes it a candidate integrator of metabolic state, but the module does not establish that PGP drives the other genes or that the module is a glycerolipid pathway.
