# Conserved co-abundance modules: autonomic_nervous_system and skin

## Module 0

**Tissue pair**: autonomic_nervous_system and skin  
**Genes (50)**: PPP2R5D, ACO2, ASPH, ASS1, CABP7, CBL, MT-CO2, CYB5A, DIABLO, DHX33, DBN1, DHFR, ECHDC1, EHBP1, EIF2B5, ERGIC2, ERLIN1, FBXO30, FHL1, HSDL1, IMP4, TMPO, TMPO, LARP4, MSH3, NAA10, NAA40, NEK7, PDXK, PHF3, CDC40, CRYZ, RPL3, RMDN3, SEC23B, SEC24D, SENP3, SKA3, YARS2, TCP11L1, TACC3, CCT5, CCT8, THOC2, THYN1, TTI2, UBE2S, VIRMA, WASHC4, XTBD1

### Function

No GO or KEGG term passed global multiple-testing correction, and STRING reported no functional enrichment. Therefore, the module does not support a single statistically established pathway-level function. Its gene annotations instead indicate a mixed cellular-maintenance program. SKA3, TACC3, NEK7 and related genes are associated with spindle organization, mitosis and chromosome segregation; THOC2, CDC40, DHX33 and VIRMA support RNA export, RNA processing and RNA modification; UBE2S, CBL, FBXO30 and NAA40 support ubiquitin-dependent regulation or protein modification; SEC23B and SEC24D support COPII-mediated endoplasmic-reticulum-to-Golgi trafficking; CCT5 and CCT8 support cytosolic protein folding. The most defensible interpretation is therefore a coordinated state involving cell-cycle activity, RNA and protein homeostasis, intracellular trafficking and metabolic maintenance, rather than a narrowly defined tissue-specific pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, while the tissue-enhanced annotations are distributed across diverse tissues including liver, muscle, kidney and lymphoid tissue. Cell-type-enhanced annotations are also heterogeneous, with recurring signals in neutrophil-lineage and spermatogenic cells but no coherent single-cell identity. Most genes have low immune-cell specificity, although selected genes show neutrophil, plasmacytoid dendritic-cell or other blood-cell associations. Thus, the module does not look primarily like a plasma-protein or blood-contamination module, but sample composition or shared proliferative and structural cell states could contribute to its conservation between autonomic nervous system and skin. HPA protein detection is available for skin and is present for most of the module, whereas the autonomic-nervous-system comparison has no matching HPA tissue.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The high-confidence STRING evidence consists of a small set of established pairwise relationships rather than a densely connected interaction network. These include CCT5-CCT8, CCT5-RPL3, CDC40-DHX33, CBL-UBE2S, MT-CO2-THYN1, NAA10-NAA40 and SEC23B-SEC24D. The strongest and most repeated hu.MAP evidence concerns the SEC23B-SEC24D COPII pair across (hu.MAP huMAP3_00065.1), (hu.MAP huMAP3_00707.1), (hu.MAP huMAP3_07775.1), (hu.MAP huMAP3_06453.1), (hu.MAP huMAP3_09282.1), (hu.MAP huMAP3_11128.1), (hu.MAP huMAP3_11237.1), (hu.MAP huMAP3_13535.1) and (hu.MAP huMAP3_12394.1), and the CCT5-CCT8 chaperonin pair across (hu.MAP huMAP3_07938.1), (hu.MAP huMAP3_06559.1), (hu.MAP huMAP3_09191.1), (hu.MAP huMAP3_10656.1) and (hu.MAP huMAP3_14584.1). Additional hu.MAP support connects THOC2 with VIRMA in (hu.MAP huMAP3_09943.1), ERLIN1 with RMDN3 in (hu.MAP huMAP3_10725.1), EIF2B5 with TTI2 in (hu.MAP huMAP3_11232.1), and PHF3 with XTBD1 in (hu.MAP huMAP3_07778.1). These relationships show that parts of the module recover known protein complexes, especially COPII trafficking and chaperonin-mediated folding. However, most module genes lack a recorded STRING partner or hu.MAP complex in the supplied evidence, so the databases support embedded submodules rather than one unified physical complex.

**STRING interactions (score >= 0.7)**: 7 of 1225 gene pairs: CBL–UBE2S (0.738); CCT5–CCT8 (0.999); CCT5–RPL3 (0.731); CDC40–DHX33 (0.818); MT-CO2–THYN1 (0.837); NAA10–NAA40 (0.811); SEC23B–SEC24D (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00065.1 (SEC24D, SEC23B; 2/4); huMAP3_00707.1 (SEC24D, SEC23B; 2/4); huMAP3_07775.1 (SEC24D, SEC23B; 2/5); huMAP3_06453.1 (SEC24D, SEC23B; 2/6); huMAP3_09282.1 (SEC24D, SEC23B; 2/6); huMAP3_11128.1 (SEC24D, SEC23B; 2/8); huMAP3_11237.1 (SEC24D, SEC23B; 2/12); huMAP3_07778.1 (PHF3, XTBD1; 2/14); huMAP3_13535.1 (SEC24D, SEC23B; 2/14); huMAP3_07938.1 (CCT5, CCT8; 2/23); huMAP3_06559.1 (CCT5, CCT8; 2/25); huMAP3_09191.1 (CCT5, CCT8; 2/32); huMAP3_10656.1 (CCT5, CCT8; 2/36); huMAP3_10725.1 (ERLIN1, RMDN3; 2/59); huMAP3_14584.1 (CCT5, CCT8; 2/61); huMAP3_11232.1 (EIF2B5, TTI2; 2/78); huMAP3_09943.1 (VIRMA, THOC2; 2/78); huMAP3_12394.1 (SEC24D, SEC23B; 2/98)

### Novelty

The cross-tissue co-abundance observation may be a new biological finding, but novelty cannot be established from this fact sheet alone. The module is not a previously unrecognized collection of molecular relationships: several internal links are already represented in STRING and hu.MAP, particularly the COPII and CCT relationships. Conversely, the absence of global GO or KEGG enrichment, the lack of STRING functional enrichment and the limited physical-interaction coverage mean that the shared autonomic-nervous-system/skin organization is not explained by an established canonical pathway. The appropriate conclusion is that the conserved co-abundance pattern is potentially novel as a tissue-pair observation, while its molecular mechanism remains unresolved and requires replication, cell-composition controls and experimental testing.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in selected autonomic-nervous-system and skin cells in which proliferation or regenerative activity increases the demand for spindle control, RNA processing, protein folding, ubiquitin regulation and ER-to-Golgi cargo handling. The SEC23B-SEC24D COPII machinery could support increased biosynthetic trafficking, while CCT5-CCT8 could maintain folding of newly synthesized proteins; SKA3, TACC3 and NEK7 could mark a mitotic component, and CBL-UBE2S could couple signaling or cell-cycle state to regulated protein turnover. This may be a coordinated cell-state program or a shared cell-type-composition effect rather than a direct physical complex. The hypothesis predicts that module activity should track proliferative, regenerative or biosynthetic cell states and should diminish after adjustment for cell composition.

### Important genes

#### SKA3

- **Related proteins** (co-abundance neighbors): THOC2 (0.92), TMPO (0.90), PDXK (0.90), SENP3 (0.89), CBL (0.88), UBE2S (0.87), YARS2 (0.86), DHFR (0.86), ASPH (0.84), NEK7 (0.83), EIF2B5 (0.82), WASHC4 (0.81), PPP2R5D (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Mitotic spindle, Centrosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: spindle and kinetochore associated complex subunit 3. This gene encodes a component of the spindle and kinetochore-associated protein complex that regulates microtubule attachment to the kinetochores during mitosis. The encoded protein localizes to the outer kinetechore and may be required for normal chromosome segregation and cell division. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.388); lysosomal storage disease (0.141); hepatocellular carcinoma (0.112); lung adenocarcinoma (0.110); neoplasm (0.102)
- **Europe PMC papers**: 656
- **Why important**: SKA3 is the strongest network-connected gene in the supplied subgraph and links multiple module neighborhoods, including THOC2, TMPO, PDXK, SENP3, CBL, UBE2S, YARS2 and DHFR. Its established function is in the spindle and kinetochore-associated complex, microtubule attachment and chromosome segregation. HPA describes tissue enhancement in bone marrow, lymphoid tissue and testis and cell-type enhancement in differentiating germ-cell and progenitor-like populations, while showing no immune-cell detection. It has extensive literature and disease associations spanning neurodegenerative disease and neoplasia.
- **Conclusion**: Established evidence supports SKA3 as a central marker of mitotic and spindle-related biology in the module. Its network position makes it a plausible organizing gene for the co-abundance pattern, but the data do not establish that SKA3 drives the shared tissue module.

#### SEC23B

- **Related proteins** (co-abundance neighbors): FBXO30 (0.81); STRING partners: SEC24D (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Vesicles, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_00065.1, huMAP3_00707.1, huMAP3_07775.1, huMAP3_06453.1, huMAP3_09282.1, huMAP3_11128.1, huMAP3_11237.1, huMAP3_13535.1, huMAP3_12394.1
- **Function (MyGene.info)**: SEC23 homolog B, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The function of this gene product has been implicated in cargo selection and concentration. Multiple alternativel…
- **Diseases (Open Targets)**: congenital dyserythropoietic anemia type 2 (0.834); Cowden syndrome 7 (0.730); congenital dyserythropoietic anemia (0.438); hereditary disease (0.194); hereditary ataxia (0.118)
- **Europe PMC papers**: 847
- **Why important**: SEC23B is directly paired with SEC24D in STRING and repeatedly appears with SEC24D in high-confidence hu.MAP complexes (hu.MAP huMAP3_00065.1), (hu.MAP huMAP3_00707.1), (hu.MAP huMAP3_07775.1), (hu.MAP huMAP3_06453.1), (hu.MAP huMAP3_09282.1), (hu.MAP huMAP3_11128.1), (hu.MAP huMAP3_11237.1), (hu.MAP huMAP3_13535.1) and (hu.MAP huMAP3_12394.1). It is a COPII component involved in ER-to-Golgi vesicle budding and cargo loading. Its disease associations include congenital dyserythropoietic anemia and Cowden syndrome, and HPA places the protein in the ER, vesicles and cytosol, with cell-type enhancement in neutrophils.
- **Conclusion**: Established evidence identifies SEC23B as a credible trafficking component and one of the best-supported physical submodule markers. Its presence supports increased secretory-pathway or membrane-trafficking demand, but it does not demonstrate that the whole module is a secretory or blood-cell program.

#### SEC24D

- **Related proteins** (co-abundance neighbors): FHL1 (0.85); STRING partners: SEC23B (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_00065.1, huMAP3_00707.1, huMAP3_07775.1, huMAP3_06453.1, huMAP3_09282.1, huMAP3_11128.1, huMAP3_11237.1, huMAP3_13535.1, huMAP3_12394.1
- **Function (MyGene.info)**: SEC24 homolog D, COPII component. The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec24p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. This gene product is implicated in the shaping of the vesicle, and also in cargo selection and concentration. Mut…
- **Diseases (Open Targets)**: Cole-Carpenter syndrome (0.753); hereditary disease (0.380); osteogenesis imperfecta type 1 (0.370); Seizure (0.259); Intellectual disability (0.259)
- **Europe PMC papers**: 780
- **Why important**: SEC24D forms the matching COPII pair with SEC23B and is represented with SEC23B across the repeated hu.MAP complexes (hu.MAP huMAP3_00065.1), (hu.MAP huMAP3_00707.1), (hu.MAP huMAP3_07775.1), (hu.MAP huMAP3_06453.1), (hu.MAP huMAP3_09282.1), (hu.MAP huMAP3_11128.1), (hu.MAP huMAP3_11237.1), (hu.MAP huMAP3_13535.1) and (hu.MAP huMAP3_12394.1). It contributes to COPII vesicle shaping, cargo selection and ER-to-Golgi transport. HPA places it in vesicles and reports enhancement in several pituitary cell types including plasma cells. Its disease associations include Cole-Carpenter syndrome and osteogenesis imperfecta.
- **Conclusion**: Established evidence supports SEC24D as a functionally meaningful trafficking partner of SEC23B and as a robust anchor of one module substructure. The shared abundance of this pair is consistent with coordinated vesicle transport, although it remains a hypothesis that this transport activity explains conservation across both tissues.

#### CCT5

- **Related proteins** (co-abundance neighbors): RPL3 (0.86); STRING partners: CCT8 (0.999), RPL3 (0.731)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is linked to CCT8 and RPL3 in STRING and appears with CCT8 across several hu.MAP complexes, including (hu.MAP huMAP3_07938.1), (hu.MAP huMAP3_06559.1), (hu.MAP huMAP3_09191.1), (hu.MAP huMAP3_10656.1) and (hu.MAP huMAP3_14584.1). CCT5 is a subunit of the CCT chaperonin complex, which folds newly synthesized proteins including actin and tubulin. It has an established association with hereditary sensory and autonomic neuropathy with spastic paraplegia and has substantial literature. HPA reports low tissue specificity with cell-type enhancement in late primary spermatocytes and protein detection in skin.
- **Conclusion**: Established evidence supports CCT5 as a protein-folding and cytoskeletal-proteostasis marker that is especially relevant to the autonomic-nervous-system context. Its co-abundance with CCT8 strengthens the interpretation of a chaperonin submodule, but does not prove that proteostasis is the primary driver of the entire module.

#### FHL1

- **Related proteins** (co-abundance neighbors): TACC3 (0.91), CDC40 (0.88), SEC24D (0.85), HSDL1 (0.85), TTI2 (0.81), CYB5A (0.80), ERGIC2 (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: four and a half LIM domains 1. This gene encodes a member of the four-and-a-half-LIM-only protein family. Family members contain two highly conserved, tandemly arranged, zinc finger domains with four highly conserved cysteines binding a zinc atom in each zinc finger. Expression of these family members occurs in a cell- and tissue-specific mode and these proteins are involved in many cellular processes. Mutations in this gene ha…
- **Diseases (Open Targets)**: X-linked myopathy with postural muscle atrophy (0.810); myopathy, reducing body, X-linked, early-onset, severe (0.648); myopathy, reducing body, X-linked, childhood-onset (0.640); Emery-Dreifuss muscular dystrophy (0.630); Uruguay Faciocardiomusculoskeletal syndrome (0.585)
- **Europe PMC papers**: 3059
- **Why important**: FHL1 connects several otherwise distinct neighborhoods through TACC3, CDC40, SEC24D, HSDL1, TTI2, CYB5A and ERGIC2. It is group-enriched in skeletal muscle and tongue, is enhanced in myonuclei and adipocytes, and is detected in skin. Its established functions include muscle development, regulation of cell growth and regulation of potassium transport. It has extensive literature and strong disease associations with X-linked myopathies and Emery-Dreifuss muscular dystrophy.
- **Conclusion**: Established evidence supports FHL1 as a tissue- and structural-state connector linking muscle-associated biology with trafficking and cell-cycle-related genes. Its position suggests that it may help explain cross-tissue co-abundance, but the available data do not show that muscle-lineage biology is the defining function of the module.

## Module 1

**Tissue pair**: autonomic_nervous_system and skin  
**Genes (47)**: PPP2R1B, ARMC8, ASCC3, ASNS, ATXN10, BIRC6, CAMSAP1, CETN2, CHD1, CHD4, CPSF1, COPS7B, CSTF3, DCTN1, DDX19B, DDX6, LIG4, POLA1, DRG2, GAK, GEMIN6, FECH, HSPH1, LNPK, METAP1, MSH6, PPP1R12A, PDCD6IP, PPM1G, PRPF4, PSIP1, MRPL45, POLR2B, RPF2, RRP15, PDCD11, SLC27A4, SNRNP40, AARS1, NARS1, TRAPPC11, UNC119B, USP28, UTP15, UTP4, VPS41, ZFR

### Function

No GO or KEGG term passed global correction, so no pathway is established by primary enrichment evidence. The module is best interpreted as a broadly expressed intracellular maintenance program rather than a tissue-specific pathway. Its genes cover vesicle trafficking and organelle organization through TRAPPC11 and VPS41; transcription and RNA handling through POLR2B, CPSF1, CSTF3, PRPF4, SNRNP40, and GEMIN6; ribosomal RNA production through PDCD11, UTP4, UTP15, RPF2, and RRP15; DNA replication and repair through MSH6, LIG4, POLA1, CHD4, and USP28; and protein synthesis or proteostasis through AARS1, NARS1, ASNS, HSPH1, and METAP1. The co-abundance pattern therefore most plausibly reflects coordinated cellular biosynthetic, genome-maintenance, and trafficking capacity. The network contains several internally coherent local clusters, but its disconnected structure and lack of global GO or KEGG enrichment argue against assigning it a single narrowly defined biological process.

**Cell composition.** The HPA profile argues against a plasma-protein, secreted-protein, or blood-cell module. Nearly all genes have low immune-cell specificity, only one gene is annotated as secreted, and only one is immune-cell enriched. Most genes have low tissue specificity, while the tissue-enhanced genes are distributed across retina, liver, pancreas, skeletal muscle, testis, bone marrow, and other tissues. Cell-type-enhanced annotations are heterogeneous and include germ-cell, neuronal, epithelial, ciliated, erythroid, and progenitor populations. Protein detection is broadly present in skin for most tested genes, whereas autonomic-nervous-system protein data are unavailable. This composition is most consistent with a shared cellular or housekeeping-like program present in cells represented in both tissues, although the heterogeneous cell-type annotations leave open a contribution from shared cell states or sample composition.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports several established local relationships: AARS1 with NARS1 and ASNS; LIG4 with MSH6 and CETN2; CPSF1 with CSTF3; PDCD11 with POLR2B, RPF2, UTP15, and UTP4; UTP15 with UTP4 and RPF2; PRPF4 with SNRNP40; and additional links among the ribosome-biogenesis and DNA-maintenance genes. These relationships indicate that parts of the module recapitulate known molecular machinery rather than being arbitrary correlations. hu.MAP independently places PRPF4, GEMIN6, and SNRNP40 in a spliceosomal or snRNP-associated complex (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_06511.1); UTP15 and UTP4 in small-subunit-processome and RNA-processing complexes (hu.MAP huMAP3_01743.1) (hu.MAP huMAP3_14264.1); AARS1 and NARS1 in aminoacylation-associated complexes (hu.MAP huMAP3_10302.1) (hu.MAP huMAP3_10115.1); CPSF1 and CSTF3 in cleavage and polyadenylation complexes (hu.MAP huMAP3_00102.1) (hu.MAP huMAP3_09096.1) (hu.MAP huMAP3_11757.1); MSH6 and ATXN10 in a broader DNA-maintenance-associated complex (hu.MAP huMAP3_09042.1); and FECH with PPP2R1B in several larger complexes (hu.MAP huMAP3_07998.1) (hu.MAP huMAP3_09709.1) (hu.MAP huMAP3_10333.1) (hu.MAP huMAP3_13510.1). The hu.MAP overlaps are usually partial, so they support modular substructures but do not establish one unified complex.

**STRING interactions (score >= 0.7)**: 18 of 1081 gene pairs: AARS1–ASNS (0.84); AARS1–NARS1 (0.947); ASNS–NARS1 (0.943); CETN2–LIG4 (0.914); CETN2–MSH6 (0.917); CPSF1–CSTF3 (0.999); LIG4–MSH6 (0.965); METAP1–POLR2B (0.707); MSH6–POLA1 (0.882); PDCD11–POLR2B (0.919); PDCD11–RPF2 (0.976); PDCD11–UTP15 (0.987); PDCD11–UTP4 (0.999); PRPF4–SNRNP40 (0.986); RPF2–RRP15 (0.985); RPF2–UTP15 (0.74); RPF2–UTP4 (0.909); UTP15–UTP4 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (PRPF4, GEMIN6, SNRNP40; 3/97); huMAP3_01743.1 (UTP15, UTP4; 2/6); huMAP3_10302.1 (NARS1, AARS1; 2/9); huMAP3_05025.1 (DRG2, CAMSAP1; 2/10); huMAP3_00102.1 (CPSF1, CSTF3; 2/12); huMAP3_10115.1 (NARS1, AARS1; 2/14); huMAP3_09096.1 (CPSF1, CSTF3; 2/15); huMAP3_11757.1 (CPSF1, CSTF3; 2/16); huMAP3_14264.1 (UTP15, UTP4; 2/20); huMAP3_07998.1 (FECH, PPP2R1B; 2/26); huMAP3_09042.1 (MSH6, ATXN10; 2/26); huMAP3_09709.1 (FECH, PPP2R1B; 2/57); huMAP3_10333.1 (FECH, PPP2R1B; 2/63); huMAP3_06511.1 (PRPF4, GEMIN6; 2/79); huMAP3_13510.1 (FECH, PPP2R1B; 2/85)

### Novelty

The module should not be called a newly discovered molecular complex or a novel pathway. Several of its relationships and substructures are already documented by STRING and hu.MAP, and the constituent genes have established functions. A potentially novel aspect is the reproducible co-abundance of this particular combination across autonomic nervous system and skin, especially the juxtaposition of trafficking, RNA maturation, ribosome production, genome maintenance, and translation-related genes. However, the supplied evidence does not establish whether this cross-tissue module has been reported previously, whether it is driven by a shared cell population, or whether it reflects technical or compositional effects. Absence from STRING or hu.MAP would not prove novelty, and the partial database support here favors describing the finding as a potentially informative tissue-pair co-abundance pattern requiring replication.

**Hypothesis.** Hypothesis: the module represents a shared cellular stress and biosynthetic-readiness state in which vesicle and organelle trafficking, transcriptional output, RNA splicing and three-prime processing, ribosome biogenesis, translation, and DNA surveillance are coordinately maintained. TRAPPC11 and VPS41 could connect intracellular transport with organelle homeostasis, while POLR2B, CPSF1, PRPF4, UTP4, UTP15, and PDCD11 could support production and maturation of transcripts and ribosomes. MSH6, LIG4, POLA1, and CHD4 could preserve genome integrity during cell maintenance or proliferation. This is a mechanistic hypothesis, not a demonstrated causal pathway; it should be tested by replication across independent tissue cohorts, cell-type deconvolution, and perturbation of the proposed hub genes.

### Important genes

#### TRAPPC11

- **Related proteins** (co-abundance neighbors): POLR2B (0.93), METAP1 (0.90), DCTN1 (0.85), GAK (0.84), CPSF1 (0.84), DDX19B (0.83), CETN2 (0.83), PDCD11 (0.82), COPS7B (0.82), PRPF4 (0.82), PPP1R12A (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: trafficking protein particle complex subunit 11. The protein encoded by this gene is a subunit of the TRAPP (transport protein particle) tethering complex, which functions in intracellular vesicle trafficking. This subunit is involved in early stage endoplasmic reticulum-to-Golgi vesicle transport. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jan 2013].
- **Diseases (Open Targets)**: autosomal recessive limb-girdle muscular dystrophy type R18 (0.805); autosomal recessive limb-girdle muscular dystrophy (0.554); neurodegenerative disease (0.485); hereditary disease (0.471); limb-girdle muscular dystrophy (0.458)
- **Europe PMC papers**: 377
- **Why important**: TRAPPC11 is the strongest network hub in the supplied subgraph and connects genes involved in transcription, RNA processing, vesicle trafficking, centrosomal biology, and protein maturation. Its established role as a TRAPP-complex subunit in endoplasmic-reticulum-to-Golgi transport provides a plausible cellular-organization anchor. It also has a substantial literature base and disease associations including limb-girdle muscular dystrophy and neurodegenerative disease. STRING does not report partners for TRAPPC11 in the supplied evidence, and hu.MAP does not place it in a listed complex, so its hub status is based on the co-abundance network rather than known physical interaction evidence.
- **Conclusion**: Established evidence supports TRAPPC11 as a vesicle-trafficking and Golgi-organization protein and as a central co-abundance node. It is a plausible integrator of the module, but a causal role in coordinating the other module processes remains hypothetical.

#### POLR2B

- **Related proteins** (co-abundance neighbors): TRAPPC11 (0.93), USP28 (0.87), CHD4 (0.82), CAMSAP1 (0.82), DDX19B (0.81); STRING partners: METAP1 (0.707), PDCD11 (0.919)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase II subunit B. This gene encodes the second largest subunit of RNA polymerase II (Pol II), a DNA-dependent RNA polymerase that catalyzes the transcription of DNA into precursors of mRNA, snRNA and microRNA. This subunit and the largest subunit form opposite sides of the center cleft of Pol II. Deletion of the flap loop region of this subunit results in a decrease in the rate of transcriptional elongation. Altern…
- **Diseases (Open Targets)**: HIV infectious disease (0.600); Orthomyxoviridae infectious disease (0.370); dengue disease (0.370); acrocephalosyndactyly (0.370); neurodegenerative disease (0.341)
- **Europe PMC papers**: 589
- **Why important**: POLR2B is a central transcriptional component and occupies a bridging position between TRAPPC11, METAP1, PDCD11, CAMSAP1, DDX19B, USP28, and CHD4. Its established role as a core subunit of RNA polymerase II makes it relevant to the transcript-production side of the module. STRING supports links to METAP1 and PDCD11, while the network also connects it to DNA-damage and chromatin-related genes. Its literature volume is substantial and includes disease associations involving infection, neurodegeneration, and developmental abnormalities.
- **Conclusion**: Established evidence supports POLR2B as a core transcriptional machinery component and a plausible bridge among several module neighborhoods. The data do not show that altered POLR2B activity causes the cross-tissue co-abundance pattern.

#### MSH6

- **Related proteins** (co-abundance neighbors): UNC119B (0.86), DDX19B (0.84), VPS41 (0.82); STRING partners: CETN2 (0.917), LIG4 (0.965), POLA1 (0.882)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus, Vesicles; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_09042.1
- **Function (MyGene.info)**: mutS homolog 6. This gene encodes a member of the DNA mismatch repair MutS family. In E. coli, the MutS protein helps in the recognition of mismatched nucleotides prior to their repair. A highly conserved region of approximately 150 aa, called the Walker-A adenine nucleotide binding motif, exists in MutS homologs. The encoded protein heterodimerizes with MSH2 to form a mismatch recognition complex that functions …
- **Diseases (Open Targets)**: Lynch syndrome (0.878); colorectal cancer (0.832); endometrial cancer (0.819); mismatch repair cancer syndrome (0.799); mismatch repair cancer syndrome 1 (0.737)
- **Europe PMC papers**: 17901
- **Why important**: MSH6 is a key genome-maintenance gene with a large literature base and strong disease evidence for Lynch syndrome and mismatch-repair cancer syndromes. In the module it links DDX19B, VPS41, and UNC119B, and STRING connects it to LIG4, CETN2, and POLA1. This places mismatch recognition alongside DNA ligation, replication initiation, and centrosomal or ciliary-associated proteins. Its HPA profile is broadly expressed with low immune specificity, arguing against a blood-cell explanation for its presence.
- **Conclusion**: Established evidence supports MSH6 as a mismatch-repair factor and supports its known relationships with DNA-maintenance proteins. Its co-abundance with trafficking and ciliary genes may indicate a shared cellular state, but any functional coupling beyond known interactions is hypothetical.

#### AARS1

- **Related proteins** (co-abundance neighbors): NARS1 (0.82), PPM1G (0.82); STRING partners: ASNS (0.84), NARS1 (0.947)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_10302.1, huMAP3_10115.1
- **Function (MyGene.info)**: alanyl-tRNA synthetase 1. The human alanyl-tRNA synthetase (AARS) belongs to a family of tRNA synthases, of the class II enzymes.  Class II tRNA synthases evolved early in evolution and are highly conserved. This is reflected by the fact that 498 of the 968-residue polypeptide human AARS shares 41% identity witht the E.coli protein.  tRNA synthases are the enzymes that interpret the RNA code and attach specific aminoacids …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2N (0.762); developmental and epileptic encephalopathy, 29 (0.747); undetermined early-onset epileptic encephalopathy (0.678); trichothiodystrophy 8, nonphotosensitive (0.568); Charcot-Marie-Tooth disease type 2 (0.566)
- **Europe PMC papers**: 672
- **Why important**: AARS1 is a translation-related enzyme and participates in a coherent local network with NARS1 and ASNS. STRING supports the AARS1-NARS1 and AARS1-ASNS relationships, while hu.MAP places AARS1 and NARS1 together in multiple complexes (hu.MAP huMAP3_10302.1) (hu.MAP huMAP3_10115.1). AARS1 has established links to aminoacylation and tRNA processing, a meaningful function for a module that also contains transcriptional and ribosome-biogenesis machinery. Its disease associations include Charcot-Marie-Tooth disease and developmental epileptic encephalopathy, and it has a substantial literature base.
- **Conclusion**: Established evidence supports AARS1 as a translation and tRNA-aminoacylation component embedded in a known local interaction neighborhood. Its presence supports a biosynthetic interpretation, but it does not by itself establish that translation is the dominant function of the whole module.

#### UTP4

- **Related proteins** (co-abundance neighbors): ASCC3 (0.88), UTP15 (0.88), CPSF1 (0.83), ARMC8 (0.81); STRING partners: PDCD11 (0.999), RPF2 (0.909), UTP15 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_01743.1, huMAP3_14264.1
- **Function (MyGene.info)**: UTP4 small subunit processome component. This gene encodes a WD40-repeat-containing protein that is localized to the nucleolus. Mutation of this gene causes North American Indian childhood cirrhosis, a severe intrahepatic cholestasis that results in transient neonatal jaundice, and progresses to periportal fibrosis and cirrhosis in childhood and adolescence. Alternative splicing results in multiple transcript variants. [provided by RefSe…
- **Diseases (Open Targets)**: hereditary North American Indian childhood cirrhosis (0.420); cardiovascular disorder (0.101); basal cell carcinoma (0.079); hypertensive disorder (0.064); osteosarcoma (0.052)
- **Europe PMC papers**: 214
- **Why important**: UTP4 is a network connector linking ASCC3, UTP15, CPSF1, and ARMC8. STRING shows strong relationships with PDCD11, RPF2, and UTP15, and hu.MAP places it with UTP15 in small-subunit-processome and RNA-processing complexes (hu.MAP huMAP3_01743.1) (hu.MAP huMAP3_14264.1). Its established nucleolar role in small-subunit ribosomal RNA maturation makes it a strong representative of the ribosome-biogenesis neighborhood. It also has a defined inherited liver-disease association, while its HPA profile is broadly expressed with low immune specificity.
- **Conclusion**: Established evidence supports UTP4 as a nucleolar ribosome-biogenesis factor with several known interaction partners in the module. Its co-abundance suggests coordinated RNA and ribosome production, but the absence of globally significant enrichment prevents claiming a definitive ribosome-biogenesis module annotation.

## Module 2

**Tissue pair**: autonomic_nervous_system and skin  
**Genes (33)**: NT5E, ALDH2, ACTR10, SDHC, CHERP, CNOT10, CASK, DAGLB, POLE, DPYSL3, FKBP15, GGPS1, GNL3, HEATR3, MKI67, PRKCA, LIPA, MCCC1, MGME1, MYLK, NDUFA13, NOL11, PLS1, PTK7, PPAT, POLR3B, GTF3C4, TRMT5, TXNRD1, USP16, XPO5, ZC3H7B, ZFAND5

### Function

No GO or KEGG term passed global correction, so this module should not be assigned a single statistically established pathway function. Its genes instead suggest a heterogeneous cellular-state program combining protein kinase and calcium-dependent signaling, cytoskeletal organization, mitochondrial respiration and redox control, lipid handling, RNA transport and processing, DNA replication and repair, and cell proliferation. PRKCA, MYLK, CASK, DPYSL3, PTK7, and DAGLB support signaling, adhesion, actin, and neuronal or cell-migration biology. ALDH2, NDUFA13, SDHC, TXNRD1, and MGME1 support aldehyde detoxification, mitochondrial respiratory activity, and redox or mitochondrial-genome maintenance. POLE, POLR3B, HEATR3, NOL11, XPO5, and USP16 support replication, transcription, ribosome-related processes, RNA export, and chromatin regulation. These are established functions of individual genes, not evidence of a globally enriched module pathway. The network therefore appears more consistent with a shared cellular composition or physiological-state signal than with a sharply defined molecular complex.

**Cell composition.** The module is not predominantly plasma or secreted: only a small subset is annotated as secreted, and most genes are intracellular. It is also not uniformly blood-cell specific. HPA reports broadly low tissue specificity for most genes, while many genes are cell-type enhanced, including erythrocyte progenitors, oligodendrocyte progenitor cells, Kupffer cells, monocytes, and several epithelial or reproductive cell types. The presence of LIPA, ALDH2, HEATR3, FKBP15, and related immune or myeloid-associated signals raises the possibility of shared myeloid or macrophage content, whereas POLE, MKI67, and PPAT may reflect proliferative or progenitor-cell content. HPA protein detection is frequent in skin for the annotated genes, but there is no matching autonomic-nervous-system tissue protein assessment in this fact sheet. Overall, the module is better viewed as a mixture of broadly expressed housekeeping, metabolic, structural, and cell-type-associated genes than as a tissue-specific secreted program. Blood or shared-cell-type composition remains a plausible contributor, but it is not proven.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides very limited prior interaction support. The only high-confidence STRING relationship is NDUFA13 with SDHC, linking mitochondrial complex I and complex II components; this supports a mitochondrial respiratory connection but does not validate the entire module. STRING reports no functional enrichment. hu.MAP repeatedly places HEATR3 and XPO5 together in complexes (hu.MAP huMAP3_08298.1), (hu.MAP huMAP3_09053.1), (hu.MAP huMAP3_09114.1), (hu.MAP huMAP3_10202.1), and (hu.MAP huMAP3_10287.1). However, each complex contains many members and only these two module genes, so the evidence supports a recurring transport or ribosome-associated complex context rather than a module-wide complex. The remaining co-abundance edges are not independently confirmed by the supplied STRING or hu.MAP evidence. Thus, the network contains a small amount of known molecular support embedded within a largely unvalidated co-abundance structure.

**STRING interactions (score >= 0.7)**: 1 of 528 gene pairs: NDUFA13–SDHC (0.794)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08298.1 (HEATR3, XPO5; 2/24); huMAP3_09053.1 (HEATR3, XPO5; 2/25); huMAP3_09114.1 (HEATR3, XPO5; 2/30); huMAP3_10202.1 (HEATR3, XPO5; 2/52); huMAP3_10287.1 (HEATR3, XPO5; 2/53)

### Novelty

The cross-tissue co-abundance pattern may be a new observation, because the supplied evidence does not identify an established autonomic-nervous-system and skin module with this complete combination of genes. However, it cannot be claimed as a new biological pathway or new protein complex. The absence of global GO or KEGG enrichment, the lack of STRING enrichment, the sparse STRING interaction support, and the broad and heterogeneous HPA composition all weaken a strong novelty claim. Several component relationships and gene functions are already established, including the NDUFA13–SDHC mitochondrial relationship and the recurring HEATR3–XPO5 hu.MAP context. The most defensible conclusion is that this is a potentially novel reproducible co-abundance pattern whose biological mechanism remains unresolved and requires replication, cell-composition adjustment, and independent validation.

**Hypothesis.** Hypothesis: the shared module reflects coordinated abundance of a mixed cellular-state program present in both tissues, possibly combining mitochondrial and aldehyde or redox stress handling with calcium-dependent signaling, cytoskeletal remodeling, RNA transport, and proliferative or progenitor-cell activity. A contribution from shared myeloid, progenitor, or other contaminating cell populations is also plausible. In this model, PRKCA, MYLK, and CASK could connect signaling and cytoskeletal responses; ALDH2, NDUFA13, SDHC, and TXNRD1 could represent metabolic or redox adaptation; and HEATR3 with XPO5 could represent a recurring intracellular transport or ribosome-related context. This is a mechanistic proposal rather than an established interpretation, because the module has no globally significant enrichment and little direct physical-interaction support.

### Important genes

#### PRKCA

- **Related proteins** (co-abundance neighbors): MYLK (0.91), ACTR10 (0.86), DPYSL3 (0.86), GGPS1 (0.85), ALDH2 (0.84), XPO5 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase C alpha. Protein kinase C (PKC) is a family of serine- and threonine-specific protein kinases that can be activated by calcium and the second messenger diacylglycerol. PKC family members phosphorylate a wide variety of protein targets and are known to be involved in diverse cellular signaling pathways. PKC family members also serve as major receptors for phorbol esters, a class of tumor promoters. Each mem…
- **Diseases (Open Targets)**: acute myeloid leukemia (0.554); hypertrophic cardiomyopathy (0.506); mast cell leukemia (0.475); systemic mastocytosis (0.471); heart failure (0.462)
- **Europe PMC papers**: 5462
- **Why important**: PRKCA has the strongest weighted network position among the highlighted genes and connects MYLK, ACTR10, DPYSL3, GGPS1, ALDH2, and XPO5. Its established protein-kinase function, calcium and diacylglycerol responsiveness, links to phosphorylation, reactive-oxygen responses, desmosome assembly, and endothelial proliferation make it a plausible signaling bridge between structural and metabolic parts of the module. It is brain tissue enhanced and associated with several leukemia and cardiovascular disease annotations. The literature volume is extensive.
- **Conclusion**: Established: PRKCA is a multifunctional signaling kinase with a central co-abundance position and relevant brain-associated HPA pattern. Hypothesis: it may coordinate stress-responsive signaling and cytoskeletal or adhesion changes in the shared module. The network does not establish that PRKCA directly regulates the other module genes.

#### ALDH2

- **Related proteins** (co-abundance neighbors): HEATR3 (0.91), MYLK (0.87), PRKCA (0.84), ZFAND5 (0.83), NOL11 (0.82), POLR3B (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 2 family member. This protein belongs to the aldehyde dehydrogenase family of proteins. Aldehyde dehydrogenase is the second enzyme of the major oxidative pathway of alcohol metabolism. Two major liver isoforms of aldehyde dehydrogenase, cytosolic and mitochondrial, can be distinguished by their electrophoretic mobilities, kinetic properties, and subcellular localizations. Most Caucasians have two major isozymes, …
- **Diseases (Open Targets)**: alcohol dependence (0.654); alcohol drinking (0.549); AMED syndrome, digenic (0.503); gout (0.501); atrial fibrillation (0.469)
- **Europe PMC papers**: 7978
- **Why important**: ALDH2 is among the strongest network hubs and connects HEATR3, MYLK, PRKCA, ZFAND5, NOL11, and POLR3B. Its established aldehyde-catabolic and detoxification functions provide a concrete metabolic interpretation, while HPA links it to liver, hepatocytes, Kupffer cells, and classical monocytes or myeloid dendritic cells. It is detected in skin and has extensive literature and disease associations including alcohol-related, metabolic, and cardiovascular conditions.
- **Conclusion**: Established: ALDH2 is a major aldehyde-detoxification enzyme with strong network connectivity and plausible myeloid or metabolic cell-type associations. Hypothesis: its co-abundance may mark oxidative or lipid-derived aldehyde stress shared by cells in both tissues. The module does not demonstrate altered ALDH2 enzymatic activity.

#### POLE

- **Related proteins** (co-abundance neighbors): NT5E (0.91), PTK7 (0.87), PLS1 (0.87), ACTR10 (0.86), USP16 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA polymerase epsilon, catalytic subunit. This gene encodes the catalytic subunit of DNA polymerase epsilon. The enzyme is involved in DNA repair and chromosomal DNA replication. Mutations in this gene have been associated with colorectal cancer 12 and facial dysmorphism, immunodeficiency, livedo, and short stature. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal cancer, susceptibility to, 12 (0.739); intrauterine growth retardation, metaphyseal dysplasia, adrenal hypoplasia congenita, genital anomalies, and immunodeficiency (0.735); facial dysmorphism-immunodeficiency-livedo-short stature syndrome (0.732); non-small cell lung carcinoma (0.668); B-cell chronic lymphocytic leukemia (0.660)
- **Europe PMC papers**: 71098
- **Why important**: POLE has a high network position and connects NT5E, PTK7, PLS1, ACTR10, and USP16. Its established role as the catalytic subunit of DNA polymerase epsilon places DNA replication and repair in the module, while HPA associates it with bone marrow and several progenitor populations. Its disease associations include colorectal cancer susceptibility and an immunodeficiency or developmental syndrome, and it has a very extensive literature base.
- **Conclusion**: Established: POLE represents DNA replication and repair and is associated with progenitor-rich cellular contexts. Hypothesis: POLE may indicate a proliferative or regenerative component of the shared module rather than a direct functional connection to the signaling and metabolic genes. Its presence alone does not establish that the entire module is a cell-cycle module.

#### HEATR3

- **Related proteins** (co-abundance neighbors): ALDH2 (0.91), LIPA (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_08298.1, huMAP3_09053.1, huMAP3_09114.1, huMAP3_10202.1, huMAP3_10287.1
- **Function (MyGene.info)**: HEAT repeat containing 3. The protein encoded by this gene plays a role in ribosomal protein transport and in the assembly of the 5S ribonucleoprotein particle (5S RNP). The encoded protein also may be involved in NOD2-mediated NF-kappaB signaling. [provided by RefSeq, Jul 2016].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.616); Diamond-Blackfan anemia (0.588); Diamond-Blackfan anemia 21 (0.501); Intellectual disability (0.495); Abnormal finger morphology (0.494)
- **Europe PMC papers**: 242
- **Why important**: HEATR3 connects ALDH2 and LIPA and is the only module gene besides XPO5 represented together across all listed hu.MAP complexes (hu.MAP huMAP3_08298.1), (hu.MAP huMAP3_09053.1), (hu.MAP huMAP3_09114.1), (hu.MAP huMAP3_10202.1), and (hu.MAP huMAP3_10287.1). Its established roles in ribosomal protein transport and five-S ribonucleoprotein assembly, together with HPA association with macrophages and monocytes, make it informative for both intracellular assembly and possible cell-composition interpretations. Its disease associations include Diamond-Blackfan anemia, and its literature volume is comparatively sparse.
- **Conclusion**: Established: HEATR3 has recurring hu.MAP context and functions in ribosomal transport and assembly. Hypothesis: HEATR3 may help connect a biosynthetic or ribosome-related state with the myeloid-associated component of the module. The partial overlap of large hu.MAP complexes does not prove that HEATR3 and the full module operate as one complex.

#### XPO5

- **Related proteins** (co-abundance neighbors): PRKCA (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_08298.1, huMAP3_09053.1, huMAP3_09114.1, huMAP3_10202.1, huMAP3_10287.1
- **Function (MyGene.info)**: exportin 5. This gene encodes a member of the karyopherin family that is required for the transport of small RNAs and double-stranded RNA-binding proteins from the nucleus to the cytoplasm. The encoded protein translocates cargo through the nuclear pore complex in a RanGTP-dependent process. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.533); smoking initiation (0.206); POLR1C-related disorder (0.111); hepatocellular carcinoma (0.099); cancer (0.097)
- **Europe PMC papers**: 1541
- **Why important**: XPO5 is directly connected to PRKCA and shares the recurring hu.MAP complex context with HEATR3 across (hu.MAP huMAP3_08298.1), (hu.MAP huMAP3_09053.1), (hu.MAP huMAP3_09114.1), (hu.MAP huMAP3_10202.1), and (hu.MAP huMAP3_10287.1). Its established role in nuclear export of small RNAs and double-stranded RNA-binding proteins, including pre-miRNA export, provides a plausible post-transcriptional regulatory link. HPA detects it in skin and associates it with epicardial cells. It has moderate literature volume and disease associations involving neurodegeneration and cancer.
- **Conclusion**: Established: XPO5 mediates RNA and protein export and is repeatedly represented with HEATR3 in hu.MAP complexes. Hypothesis: coordinated XPO5 and HEATR3 abundance could reflect altered RNA processing or ribosome-related demand in the shared cell state. The co-abundance edge to PRKCA does not establish direct molecular binding.

## Module 3

**Tissue pair**: autonomic_nervous_system and skin  
**Genes (13)**: PRKAG1, BRAP, CYP51A1, GOPC, MTHFD2, MTFP1, NUP50, RAB10, FARSB, TMOD3, TRIM33, TRIM56, NAE1

### Function

The module does not support a single pathway-level functional assignment from GO or KEGG: no GO or KEGG term passed global multiple-testing correction. The gene annotations instead suggest a mixed intracellular program involving signal regulation and protein modification (BRAP, TRIM56, TRIM33, NAE1), sterol biosynthesis (CYP51A1), mitochondrial dynamics and one-carbon metabolism (MTFP1, MTHFD2), vesicle trafficking and membrane delivery (RAB10, GOPC), actin organization and cell adhesion (TMOD3), nuclear transport (NUP50), translation (FARSB), and cellular energy sensing (PRKAG1). BRAP is the principal network hub, with links to several otherwise weakly connected branches. Thus, the most defensible interpretation is a coordinated abundance pattern of broadly distributed intracellular proteins rather than a demonstrated, coherent biochemical pathway. The absence of a globally enriched term does not invalidate the module.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins: the HPA summary reports no secreted genes. It also does not resemble a blood-cell module, because nearly all genes have low immune-cell specificity and only TRIM33 is reported as immune-cell enhanced, in basophils. Most genes have low tissue specificity, consistent with broadly expressed intracellular proteins rather than tissue-restricted markers. The cell-type annotations are heterogeneous, with signals in epithelial, germ-cell, glial, neuronal, muscle, stromal, and other cell types. This heterogeneity makes a simple shared skin–autonomic-nervous-system cell identity unlikely, although shared cellular composition, technical effects, or common cellular stress and metabolic states could contribute. Skin protein detection is present for several genes, while autonomic-nervous-system protein detection is unavailable in the supplied HPA comparison.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and no STRING functional-enrichment result is reported. No hu.MAP complex contains multiple module members. Therefore, the co-abundance relationships are not corroborated here by known physical interactions or a shared curated complex. The network may represent coordinated regulation, shared expression across samples, indirect biology, or data-driven co-abundance rather than a physical molecular machine. The absence of STRING and hu.MAP support also means that the central position of BRAP should be interpreted as a property of this co-abundance network, not as evidence of a validated interaction hub.

**STRING interactions (score >= 0.7)**: 0 of 78 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears to be a potentially novel co-abundance association rather than a previously established complex or pathway. The rationale is that the module has no high-confidence STRING edges, no multi-member hu.MAP complex, no STRING enrichment, and no globally corrected GO or KEGG term. However, these observations do not prove biological novelty: several genes have substantial prior literature and individually established functions, and the module may reassemble known processes through shared regulation or tissue composition. A claim of a new mechanism would require independent replication, preservation of the co-abundance pattern in additional cohorts, control for cell composition and technical covariates, and targeted experiments.

**Hypothesis.** Hypothesis: the shared module reflects a common intracellular state present in subsets of autonomic-nervous-system and skin samples, coupling energy and mitochondrial management with sterol and folate metabolism, vesicle trafficking, cytoskeletal organization, and regulated protein modification. BRAP may mark the central coordinated state, while CYP51A1, MTFP1, PRKAG1, and RAB10 represent metabolic, mitochondrial, energy-sensing, and trafficking components. TRIM56 and related ubiquitination regulators could connect this state to stress or innate-response signaling. This is a hypothesis from co-abundance and gene annotations, not an established pathway or physical complex.

### Important genes

#### BRAP

- **Related proteins** (co-abundance neighbors): PRKAG1 (0.88), TMOD3 (0.84), CYP51A1 (0.82), NAE1 (0.81), NUP50 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BRCA1 associated protein. The protein encoded by this gene was identified by its ability to bind to the nuclear localization signal of BRCA1 and other proteins. It is a cytoplasmic protein which may regulate nuclear targeting by retaining proteins with a nuclear localization signal in the cytoplasm. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: gout (0.234); colorectal cancer (0.202); age-related macular degeneration (0.186); COVID-19 (0.179); heart failure (0.158)
- **Europe PMC papers**: 6455
- **Why important**: BRAP is the strongest network hub in the supplied subgraph and connects genes spanning energy sensing, cytoskeletal organization, sterol metabolism, neddylation, and nuclear transport. Its annotation supports roles in nuclear targeting, signal transduction, MAPK-related biology, and protein ubiquitination. It also has the largest listed literature volume and multiple Open Targets disease associations, making it the most informative candidate for testing whether the module has a regulatory core.
- **Conclusion**: Established evidence: BRAP is the co-abundance hub and has documented functions in nuclear targeting and signal regulation. Hypothesis: BRAP may coordinate the broader module state, but its centrality does not establish direct molecular interactions or causality.

#### CYP51A1

- **Related proteins** (co-abundance neighbors): BRAP (0.82), FARSB (0.82), TRIM33 (0.82), MTFP1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome P450 family 51 subfamily A member 1. This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This endoplasmic reticulum protein participates in the synthesis of cholesterol by catalyzing the removal of the 14alpha-methyl group from lanosterol. Homologous g…
- **Diseases (Open Targets)**: Developmental cataract (0.398); early-onset non-syndromic cataract (0.371); cataract (0.371); Prolonged QT interval (0.346); neurodegenerative disease (0.280)
- **Europe PMC papers**: 1488
- **Why important**: CYP51A1 is a central connector in the sterol-related branch and is linked in the module to BRAP, FARSB, TRIM33, and MTFP1. Its established enzyme function in cholesterol and sterol biosynthesis provides one of the clearest biochemical anchors for the module. It has tissue enhancement in liver and cell-type enhancement in several metabolically active or muscle-related populations, and it has disease associations including cataract-related conditions and prolonged QT interval.
- **Conclusion**: Established evidence: CYP51A1 catalyzes a defined step in cholesterol biosynthesis. Hypothesis: its co-abundance with mitochondrial, regulatory, and translation-related genes may indicate coordinated lipid and cellular-energy demand, but the module does not demonstrate altered sterol flux.

#### MTFP1

- **Related proteins** (co-abundance neighbors): RAB10 (0.85), MTHFD2 (0.82), CYP51A1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial fission process 1. MTP18 is a mitochondrial protein and downstream target of the phosphatidylinositol 3-kinase (see PIK3CA, MIM 171834) signaling pathway that plays a role in cell viability and mitochondrial dynamics (Tondera et al., 2004 [PubMed 15155745]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: neoplasm (0.092); hepatocellular carcinoma (0.076); gastric cancer (0.063); cancer (0.053); pancreatic ductal adenocarcinoma (0.035)
- **Europe PMC papers**: 731
- **Why important**: MTFP1 links the mitochondrial branch to CYP51A1 and RAB10 and is annotated as a regulator of mitochondrial fission and fusion. This gives the module a plausible organelle-dynamics component connecting metabolism with membrane trafficking. It has multiple cancer-related Open Targets associations and an established literature base, although it is not a high-connectivity hub.
- **Conclusion**: Established evidence: MTFP1 is a mitochondrial protein involved in mitochondrial dynamics. Hypothesis: MTFP1 may couple mitochondrial remodeling to the shared metabolic and trafficking state in the two tissues; the co-abundance data do not establish a direct link to CYP51A1 or RAB10.

#### PRKAG1

- **Related proteins** (co-abundance neighbors): BRAP (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase AMP-activated non-catalytic subunit gamma 1. The protein encoded by this gene is a regulatory subunit of the AMP-activated protein kinase (AMPK). AMPK is a heterotrimer consisting of an alpha catalytic subunit, and non-catalytic beta and gamma subunits. AMPK is an important energy-sensing enzyme that monitors cellular energy status. In response to cellular metabolic stresses, AMPK is activated, and thus phosphorylates and inactivates acetyl-…
- **Diseases (Open Targets)**: cardiovascular disorder (0.370); intelligence (0.323); kidney failure (0.280); Abnormality of the skeletal system (0.273); hypertensive heart disease (0.197)
- **Europe PMC papers**: 746
- **Why important**: PRKAG1 is the module member most directly connected to cellular energy sensing because it encodes a regulatory subunit of AMPK. It is connected to BRAP, the network hub, and is enriched in several neural and glial cell types in the HPA annotations. Its functional annotation includes responses to nutrient levels and glucose starvation, and Open Targets lists cardiovascular and metabolic-related disease associations.
- **Conclusion**: Established evidence: PRKAG1 is an AMPK regulatory subunit involved in cellular energy sensing. Hypothesis: it could provide a physiological explanation for coordinated abundance of metabolic, mitochondrial, and signaling proteins, but AMPK activation itself was not measured.

#### RAB10

- **Related proteins** (co-abundance neighbors): MTFP1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB10, member RAS oncogene family. RAB10 belongs to the RAS (see HRAS; MIM 190020) superfamily of small GTPases. RAB proteins localize to exocytic and endocytic compartments and regulate intracellular vesicle trafficking (Bao et al., 1998 [PubMed 9918381]).[supplied by OMIM, Mar 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.549); digestive system disorder (0.242); cervical carcinoma (0.215); lobular capilliary hemangioma (0.165); hepatocellular carcinoma (0.109)
- **Europe PMC papers**: 2856
- **Why important**: RAB10 represents the vesicle-trafficking arm of the module and is linked to MTFP1. Its established functions include exocytosis, Golgi-to-plasma-membrane transport, endosomal transport, and axonogenesis. HPA annotations place it in epithelial and keratinocyte-related cell types, which is relevant to the skin component, while its disease associations and substantial literature support make it a useful candidate for testing tissue-specific trafficking consequences.
- **Conclusion**: Established evidence: RAB10 regulates intracellular vesicle trafficking and membrane delivery. Hypothesis: RAB10 may connect the module to shared epithelial or neuronal membrane-trafficking demands, but the module does not show whether trafficking is increased or decreased.

#### TRIM56

- **Related proteins** (co-abundance neighbors): GOPC (0.82), TMOD3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tripartite motif containing 56. Enables RNA binding activity. Predicted to be involved in several processes, including defense response to other organism; positive regulation of macromolecule metabolic process; and protein K63-linked ubiquitination. Predicted to be located in cytoplasm. Predicted to be active in chromatin and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.339); neoplasm (0.101); glioma (0.101); central nervous system cancer (0.101); glioblastoma (0.100)
- **Europe PMC papers**: 945
- **Why important**: TRIM56 occupies a regulatory branch connected to TMOD3 and GOPC and is annotated for ubiquitination, type I interferon production, and innate immune responses. It is detected in skin and has a substantial literature base, while its low immune-cell specificity argues against interpreting the whole module as a blood-cell signature. Its position makes it a candidate link between intracellular protein regulation, membrane organization, and stress or defense signaling.
- **Conclusion**: Established evidence: TRIM56 has documented annotations involving ubiquitination and type I interferon regulation. Hypothesis: it may reflect a local epithelial or intrinsic stress-response component of the module rather than infiltrating immune cells; this requires direct measurement of interferon activity.

## Module 4

**Tissue pair**: autonomic_nervous_system and skin  
**Genes (45)**: ABRAXAS2, DDX20, DDX24, DDX52, POLA2, ECI1, ERLIN2, FKBP14, FUT8, GFPT2, GTPBP10, CKMT1A, KIF20A, KIF14, KLC4, MAP1B, NUP93, NUSAP1, ORC2, ORC4, PHAX, PDCL, PRPF39, RAB8B, RCL1, RFC1, MRPL1, MRPL11, MRPL50, RNASEH2A, MRPS18B, MRPS33, SACS, SMARCAD1, SRRT, STOM, SUPV3L1, TBL3, TCERG1, TEX10, TIMMDC1, TMA16, TPX2, TRIO, TRMT1L

### Function

The module does not have a single statistically established GO or KEGG function: no globally significant GO/KEGG term passed global correction. Its gene content nevertheless forms several biologically coherent, but supplementary, themes. These include mitochondrial translation and mitochondrial RNA handling through MRPL1, MRPL11, MRPL50, MRPS18B, MRPS33, GTPBP10 and SUPV3L1; ribosome biogenesis and RNA processing through RCL1, TBL3, DDX24, DDX52, TEX10, PHAX and SRRT; DNA replication, repair and chromatin maintenance through ORC2, ORC4, POLA2, RFC1, RNASEH2A and SMARCAD1; and mitotic spindle or cytokinetic organization through TPX2, KIF14, KIF20A, NUSAP1 and ABRAXAS2. MAP1B, KLC4 and TRIO add microtubule, transport and cytoskeletal biology. The most defensible interpretation is therefore a conserved cellular maintenance and proliferation module combining mitochondrial protein synthesis, nucleic-acid processing, genome maintenance and cytoskeletal cell-cycle functions, rather than a narrowly autonomic-nervous-system or skin-specific pathway.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module: the HPA summary identifies only a small secreted subset, and the listed genes are predominantly intracellular, including mitochondrial, nucleoplasmic, nucleolar, cytosolic and membrane-associated proteins. Most genes have low tissue specificity and low immune-cell specificity. HPA nevertheless shows recurring enrichment in bone marrow, lymphoid tissue, testis and selected proliferative or progenitor cell types, including erythrocyte progenitors, enteric transient amplifying cells and several spermatogenic populations. A minority of genes have immune-cell enhancement, while several are not detected in immune cells. Protein detection in skin is broad among the tested genes, but there is no matching HPA tissue result for autonomic nervous system. Thus, the shared signal could reflect a common intracellular program or shared cellular states in the sampled tissues, with possible contribution from proliferating, progenitor or blood-associated cells. It should not be interpreted as evidence that the module is a blood-contamination module without cell-composition adjustment.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports several established physical or functional neighborhoods within the co-abundance module. TPX2, KIF14, KIF20A and NUSAP1 form a coherent mitotic spindle and cytokinesis neighborhood. MRPL1, MRPL11, MRPL50, MRPS18B and MRPS33 form a strong mitochondrial-ribosomal neighborhood, with GTPBP10 connected to that group. RCL1, TBL3, DDX52 and DDX24 form an RNA-processing and ribosome-biogenesis neighborhood, while PHAX, SRRT and TCERG1 support an RNA-export or RNA-processing connection. ORC2, ORC4, POLA2 and RFC1 support DNA-replication machinery. These relationships indicate that parts of the module recapitulate known molecular machinery rather than being arbitrary correlations. The STRING functional-enrichment result was absent, so these interactions should not be converted into a globally significant pathway claim. hu.MAP independently reinforces the mitochondrial-ribosome interpretation: MRPL1, MRPL11 and MRPL50 recur together across several complexes, with SUPV3L1 included in two of them, as shown by (hu.MAP huMAP3_09113.1) through (hu.MAP huMAP3_04652.1). ERLIN2 and STOM share a hu.MAP complex in (hu.MAP huMAP3_10725.1), but this is a small peripheral connection. The fact that many module members are not assigned to hu.MAP complexes means that the co-abundance module extends beyond one known physical complex.

**STRING interactions (score >= 0.7)**: 30 of 990 gene pairs: DDX20–PHAX (0.899); DDX24–DDX52 (0.919); DDX24–TBL3 (0.898); DDX52–RCL1 (0.753); DDX52–TBL3 (0.766); GTPBP10–MRPL11 (0.948); GTPBP10–MRPL50 (0.868); KIF14–KIF20A (0.973); KIF14–NUSAP1 (0.899); KIF14–TPX2 (0.903); KIF20A–NUSAP1 (0.956); KIF20A–TPX2 (0.972); MRPL1–MRPL11 (0.998); MRPL1–MRPL50 (0.973); MRPL1–MRPS18B (0.896); MRPL1–MRPS33 (0.837); MRPL11–MRPL50 (0.94); MRPL11–MRPS18B (0.952); MRPL11–MRPS33 (0.88); MRPL50–MRPS18B (0.89); MRPL50–MRPS33 (0.922); MRPS18B–MRPS33 (0.998); NUSAP1–TPX2 (0.964); ORC2–ORC4 (0.999); ORC4–POLA2 (0.747); PHAX–SRRT (0.987); POLA2–RFC1 (0.85); RCL1–TBL3 (0.997); RCL1–TEX10 (0.727); SRRT–TCERG1 (0.839)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09113.1 (SUPV3L1, MRPL50, MRPL1, MRPL11; 4/72); huMAP3_06589.1 (SUPV3L1, MRPL50, MRPL1, MRPL11; 4/79); huMAP3_06439.1 (MRPL50, MRPL1, MRPL11; 3/57); huMAP3_06550.1 (MRPL50, MRPL1, MRPL11; 3/62); huMAP3_07939.1 (MRPL50, MRPL1, MRPL11; 3/68); huMAP3_08458.1 (MRPL50, MRPL1, MRPL11; 3/70); huMAP3_09483.1 (MRPL50, MRPL1, MRPL11; 3/74); huMAP3_04652.1 (MRPL1, MRPL11; 2/30); huMAP3_10725.1 (ERLIN2, STOM; 2/59)

### Novelty

The module is not wholly novel at the molecular-interaction level. Many of its strongest relationships are already represented in STRING, and the mitochondrial-ribosome subset is repeatedly represented in hu.MAP. Therefore, absence of a hu.MAP or STRING entry for individual genes cannot establish discovery of a new biological interaction. The potentially novel aspect is the cross-tissue co-abundance organization linking mitochondrial translation, RNA processing, genome maintenance and mitotic cytoskeletal machinery in autonomic nervous system and skin. That interpretation remains provisional because the module has no globally significant GO or KEGG term, contains broadly expressed genes, and may partly reflect shared cell-state or cell-composition effects. A claim of a new finding would require replication in independent tissue cohorts, preservation after cell-type and blood-content adjustment, and comparison with existing co-expression or proteomic modules.

**Hypothesis.** Hypothesis: the conserved module reflects a demand-coupled cellular maintenance program in which mitochondrial translation and RNA quality control support energy production, while DNA replication, chromatin restoration and mitotic spindle machinery support renewal or repair of tissue cells. In skin, this could be associated with epidermal or stromal turnover and local cellular stress; in autonomic nervous system samples, it could reflect metabolically active support cells, axonal or neuronal maintenance, or shared progenitor-like states. GTPBP10 may connect mitochondrial ribosome assembly with the RNA-processing and cytoskeletal portions of the module. This is a mechanistic model, not an established tissue-specific pathway, and it should be tested by cell-resolved measurements, perturbation of the mitochondrial-ribosome or spindle submodules, and assessment of whether the module tracks proliferation, mitochondrial activity or tissue injury.

### Important genes

#### GTPBP10

- **Related proteins** (co-abundance neighbors): TPX2 (0.92), DDX20 (0.89), MRPS18B (0.87), SUPV3L1 (0.87), TEX10 (0.86), RCL1 (0.86), TCERG1 (0.84), MRPL50 (0.83), POLA2 (0.83), TMA16 (0.83), FKBP14 (0.83), ECI1 (0.82), SMARCAD1 (0.81), TRIO (0.80), MAP1B (0.80), CKMT1A; CKMT1B (0.80); STRING partners: MRPL11 (0.948), MRPL50 (0.868)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GTP binding protein 10. Small G proteins, such as GTPBP10, act as molecular switches that play crucial roles in the regulation of fundamental cellular processes such as protein synthesis, nuclear transport, membrane trafficking, and signal transduction (Hirano et al., 2006 [PubMed 17054726]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); Abnormality of the skeletal system (0.266); bone Paget disease (0.178); type 2 diabetes mellitus (0.097); placenta praevia (0.075)
- **Europe PMC papers**: 153
- **Why important**: GTPBP10 is the strongest network hub in the supplied subgraph and connects TPX2, DDX20, mitochondrial ribosomal proteins, SUPV3L1, TEX10, RCL1 and TCERG1. Its annotation links it to mitochondrial large-ribosomal-subunit assembly, and STRING links it directly to MRPL11 and MRPL50. It therefore provides a plausible bridge between mitochondrial translation, RNA processing and the broader module. Its literature volume is moderate, and the supplied disease associations include neurodegenerative disease and bone Paget disease.
- **Conclusion**: Established: GTPBP10 is a central co-abundance connector and is annotated in mitochondrial ribosome assembly, with known STRING relationships to mitochondrial-ribosome components. Hypothesis: it may coordinate mitochondrial translation with nuclear RNA-processing or cell-cycle demands in the shared tissue state. The disease associations are supportive context, not evidence that this module causes those diseases.

#### TPX2

- **Related proteins** (co-abundance neighbors): GTPBP10 (0.92), RCL1 (0.85), MRPL1 (0.83), MRPS18B (0.82), KIF14 (0.82); STRING partners: KIF14 (0.903), KIF20A (0.972), NUSAP1 (0.964)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TPX2 microtubule nucleation factor. Enables importin-alpha family protein binding activity and protein kinase binding activity. Involved in activation of protein kinase activity; microtubule cytoskeleton organization; and negative regulation of microtubule depolymerization. Located in intercellular bridge; mitotic spindle; and nucleoplasm. Colocalizes with spindle pole. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.124); neoplasm (0.117); breast carcinoma (0.116); non-small cell lung carcinoma (0.112); breast cancer (0.110)
- **Europe PMC papers**: 4216
- **Why important**: TPX2 occupies a connected mitotic neighborhood with KIF14, KIF20A and NUSAP1 and also connects to GTPBP10 and several mitochondrial-ribosome genes. Its established annotation concerns spindle assembly, microtubule nucleation and suppression of microtubule depolymerization. HPA shows enhancement in bone marrow, lymphoid tissue and testis and in multiple proliferative or progenitor cell types. It has substantial literature and reported associations with several cancers and neoplasms.
- **Conclusion**: Established: TPX2 is a well-studied mitotic spindle regulator and a meaningful connector between the module's proliferation-related and mitochondrial neighborhoods. Hypothesis: its presence indicates that part of the shared autonomic-nervous-system and skin signal may arise from renewal, repair or proliferative cell states rather than specialized neural physiology.

#### MRPL1

- **Related proteins** (co-abundance neighbors): ORC4 (0.85), TPX2 (0.83), POLA2 (0.82); STRING partners: MRPL11 (0.998), MRPL50 (0.973), MRPS18B (0.896), MRPS33 (0.837)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_09113.1, huMAP3_06589.1, huMAP3_06439.1, huMAP3_06550.1, huMAP3_07939.1, huMAP3_08458.1, huMAP3_09483.1, huMAP3_04652.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein L1. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: preeclampsia (0.256); hair color (0.074); tongue cancer (0.043); stricture (0.028); COVID-19 (0.025)
- **Europe PMC papers**: 297
- **Why important**: MRPL1 is a core member of the mitochondrial-ribosome neighborhood. It is assigned to all of the listed hu.MAP complexes containing the mitochondrial-ribosome subset, including (hu.MAP huMAP3_09113.1) through (hu.MAP huMAP3_04652.1), and has strong STRING relationships with MRPL11, MRPL50, MRPS18B and MRPS33. Its established function is as a mitochondrial large-subunit ribosomal protein involved in mitochondrial translation. It has disease and trait associations in the supplied evidence, including preeclampsia, hair color and tongue cancer, with a moderate literature volume.
- **Conclusion**: Established: MRPL1 is a repeated physical-complex marker of the mitochondrial translation component of the module. Hypothesis: coordinated abundance of MRPL1 and its mitochondrial-ribosome partners may indicate increased mitochondrial protein-synthesis capacity in cells shared by the two tissues. The module does not establish a specific disease role for MRPL1.

#### SMARCAD1

- **Related proteins** (co-abundance neighbors): ORC2 (0.87), MRPS33 (0.85), GFPT2 (0.83), PHAX (0.82), RCL1 (0.81), GTPBP10 (0.81), RNASEH2A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SNF2 related chromatin remodeling ATPase with DExD box 1. This gene encodes a member of the SNF subfamily of helicase proteins. The encoded protein plays a critical role in the restoration of heterochromatin organization and propagation of epigenetic patterns following DNA replication by mediating histone H3/H4 deacetylation. Mutations in this gene are associated with adermatoglyphia. Alternatively spliced transcript variants encoding multiple isoforms h…
- **Diseases (Open Targets)**: palmoplantar keratoderma-sclerodactyly syndrome (0.600); absence of fingerprints-congenital milia syndrome (0.580); Adermatoglyphia (0.568); type 2 diabetes mellitus (0.396); isolated congenital adermatoglyphia (0.373)
- **Europe PMC papers**: 708
- **Why important**: SMARCAD1 has a relatively central position and connects DNA-replication-associated ORC2, RNA-processing factors, GFPT2, GTPBP10 and RNASEH2A. It is annotated as a chromatin-remodeling ATPase involved in heterochromatin organization, DNA-double-strand-break processing and chromosome separation. Its disease associations are especially relevant to skin, including adermatoglyphia and palmoplantar keratoderma-sclerodactyly syndrome. It also has a substantial literature base, despite having no listed STRING partner.
- **Conclusion**: Established: SMARCAD1 provides a biologically credible genome-maintenance and chromatin link within the module and has direct skin-related disease relevance. Hypothesis: it may couple chromatin restoration during tissue renewal to the mitochondrial and RNA-processing activities represented elsewhere in the module. Its lack of a listed STRING partner means this proposed connection is based mainly on co-abundance and network context.

#### GFPT2

- **Related proteins** (co-abundance neighbors): PRPF39 (0.87), POLA2 (0.86), SMARCAD1 (0.83), PHAX (0.82), ORC2 (0.82), FUT8 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamine--fructose-6-phosphate transaminase 2. Predicted to enable glutamine-fructose-6-phosphate transaminase (isomerizing) activity. Predicted to be involved in UDP-N-acetylglucosamine metabolic process; fructose 6-phosphate metabolic process; and protein N-linked glycosylation. Predicted to act upstream of or within cellular response to leukemia inhibitory factor. Predicted to be located in cytosol. Implicated in type 2 diabetes mellitus. […
- **Diseases (Open Targets)**: primary thrombocytopenia (0.244); cholelithiasis (0.221); pneumonitis (0.156); neoplasm (0.108); glomerulonephritis (0.103)
- **Europe PMC papers**: 1281
- **Why important**: GFPT2 is a network connector linking PRPF39, POLA2, SMARCAD1, PHAX and FUT8. Its annotation places it in the hexosamine and UDP-N-acetylglucosamine biosynthetic axis, with implications for carbohydrate metabolism and protein N-linked glycosylation. HPA shows tissue enhancement in adipose tissue and cell-type enhancement in fibroblast-like and stromal populations, with immune-cell enhancement in MAIT cells. It has a relatively substantial literature and reported associations with metabolic, hematologic and inflammatory disorders.
- **Conclusion**: Established: GFPT2 contributes a metabolic and glycosylation-related branch and connects it to DNA-replication and RNA-export factors. Hypothesis: GFPT2 may reflect biosynthetic support for membrane, extracellular or stress-response protein production in skin-associated stromal cells, although the module is not a secreted-protein module. This role requires cell-specific validation.

## Module 5

**Tissue pair**: autonomic_nervous_system and skin  
**Genes (44)**: ACO1, AKAP8, AKAP13, AKR1B1, AP3D1, ARIH1, BABAM1, BCLAF1, GLB1, CALD1, TTC4, CIT, DIS3L2, EEA1, EHD4, EML4, EMILIN1, EPS15, EXOC7, FNTA, FRYL, GEMIN4, GFPT1, GRIPAP1, EPHX1, KIF2A, LEMD3, MYEF2, NUP188, NUP85, OSBPL3, PIK3C2A, PDIA5, PRRC2B, RPL26L1, POLR1B, POLR2E, RPP30, SLC29A1, SEH1L, UBR7, WDR12, ZC3H14, ZC3HAV1

### Function

The most defensible interpretation is a mixed intracellular trafficking and cellular maintenance module, with a specific signal for synaptic vesicle endosomal processing. The only globally corrected GO or KEGG evidence is (GO:BP synaptic vesicle endosomal processing; q_global = 0.0225), supported by AP3D1, EEA1, and GRIPAP1. This connects vesicle coating, early-endosome function, receptor or cargo recycling, and postsynaptic trafficking. AP3D1 supports Golgi-to-lysosome and pigment- or neurotransmitter-vesicle trafficking; EEA1 supports early-endosome fusion and transport; and GRIPAP1 supports receptor transport and recycling at the postsynapse. PIK3C2A and EPS15 provide additional annotated support for phosphoinositide-dependent endocytosis and vesicular trafficking, although these annotations are not globally enriched. The module also contains coherent housekeeping processes involving nuclear transport, transcription, RNA processing, ribosome production, protein quality control, and cell division. Thus, it should not be described as a dedicated synaptic module: the evidence favors a trafficking-centered module embedded in broadly required cellular machinery. No STRING functional-enrichment term was reported. The absence of additional enrichment does not invalidate the module.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. Only a small subset is secreted, with EMILIN1 specifically annotated as secreted to the extracellular matrix and PDIA5 and GLB1 having intracellular or membrane-related secretome annotations. HPA indicates broad tissue distribution for most members, while a smaller subset is tissue enhanced or tissue enriched in sites such as liver, adrenal gland, testis, bone marrow, and skeletal muscle. Most members have low immune-cell specificity, so the module does not strongly resemble a blood-cell contamination signature, despite individual associations with neutrophils, monocytes, eosinophils, basophils, or related cells. The single-cell annotations are heterogeneous, including reproductive cell types, neural or glial populations, epithelial cells, and some immune populations. Protein detection is broadly present in skin for the annotated module members, whereas there is no matching HPA tissue for the autonomic nervous system. Consequently, the shared signal may partly reflect common cellular composition or ubiquitous cellular machinery rather than a tissue-specific autonomic-neural program.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP synaptic vesicle endosomal processing | 0.0225 | AP3D1, EEA1, GRIPAP1 |

### STRING and hu.MAP

STRING provides a sparse but structured set of known relationships. The strongest physical or functional cluster is the nucleoporin group NUP188, NUP85, and SEH1L, with mutually supported relationships among these proteins. POLR1B is linked to POLR2E, RPL26L1, and WDR12, while AKR1B1 is linked to GLB1. EEA1 is linked to GRIPAP1, and EML4 is linked to KIF2A. These relationships indicate that parts of the co-abundance network recapitulate established molecular machinery rather than representing wholly unconnected genes. The hu.MAP evidence reinforces this interpretation: NUP188, NUP85, and SEH1L repeatedly occur together in nuclear-pore complexes (hu.MAP huMAP3_08489.1), (hu.MAP huMAP3_09825.1), (hu.MAP huMAP3_07492.1), (hu.MAP huMAP3_09710.1), and (hu.MAP huMAP3_12581.1); POLR1B and POLR2E recur in RNA-polymerase-related assemblies (hu.MAP huMAP3_00807.1), (hu.MAP huMAP3_09057.1), (hu.MAP huMAP3_08487.1), (hu.MAP huMAP3_06426.1), (hu.MAP huMAP3_14318.1), and (hu.MAP huMAP3_11092.1); ZC3H14 and BCLAF1 recur in RNA processing assemblies (hu.MAP huMAP3_06097.1), (hu.MAP huMAP3_10564.1), (hu.MAP huMAP3_11073.1), and (hu.MAP huMAP3_09943.1); ACO1 and LEMD3 occur in complexes related to signaling or nuclear regulation (hu.MAP huMAP3_14587.1) and (hu.MAP huMAP3_13623.1); and PIK3C2A with EPS15 recur in endocytic assemblies (hu.MAP huMAP3_10762.1), (hu.MAP huMAP3_12918.1), and (hu.MAP huMAP3_12394.1). Because many complexes contain only a subset of their members in this module, the hu.MAP results support embedded molecular subsystems rather than a single complete complex.

**STRING interactions (score >= 0.7)**: 10 of 946 gene pairs: AKR1B1–GLB1 (0.903); EEA1–GRIPAP1 (0.754); EML4–KIF2A (0.781); NUP188–NUP85 (0.992); NUP188–SEH1L (0.991); NUP85–SEH1L (0.999); POLR1B–POLR2E (0.999); POLR1B–RPL26L1 (0.753); POLR1B–WDR12 (0.86); RPL26L1–WDR12 (0.905)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08489.1 (NUP188, SEH1L, NUP85; 3/10); huMAP3_09825.1 (NUP188, SEH1L, NUP85; 3/27); huMAP3_14587.1 (ACO1, LEMD3; 2/10); huMAP3_07492.1 (NUP188, SEH1L; 2/10); huMAP3_13623.1 (ACO1, LEMD3; 2/11); huMAP3_09710.1 (NUP188, SEH1L; 2/13); huMAP3_06097.1 (ZC3H14, BCLAF1; 2/22); huMAP3_00807.1 (POLR2E, POLR1B; 2/30); huMAP3_09057.1 (POLR2E, POLR1B; 2/36); huMAP3_10564.1 (ZC3H14, BCLAF1; 2/37); huMAP3_08487.1 (POLR2E, POLR1B; 2/37); huMAP3_06426.1 (POLR2E, POLR1B; 2/38); huMAP3_12581.1 (SEH1L, NUP85; 2/58); huMAP3_14318.1 (POLR2E, POLR1B; 2/58); huMAP3_10762.1 (PIK3C2A, EPS15; 2/62); huMAP3_12918.1 (PIK3C2A, EPS15; 2/62); huMAP3_11092.1 (POLR2E, POLR1B; 2/65); huMAP3_11073.1 (ZC3H14, BCLAF1; 2/67); huMAP3_09943.1 (ZC3H14, BCLAF1; 2/78); huMAP3_11232.1 (GEMIN4, NUP85; 2/78); huMAP3_12394.1 (PIK3C2A, EPS15; 2/98)

### Novelty

The co-abundance module may be a new cross-tissue observation, but the factorial claim that it is a new biological mechanism is not established. Several internal relationships are already known through STRING and hu.MAP, especially the nuclear-pore, RNA-polymerase, RNA-processing, and endocytic assemblies. The module's potentially novel aspect is the specific co-abundance organization shared by autonomic nervous system and skin, particularly the juxtaposition of endosomal, vesicle, nuclear transport, and broadly expressed maintenance proteins. However, the broad HPA distribution, sparse direct connectivity, lack of STRING functional enrichment, and mixture of several cellular systems make strong novelty claims premature. Replication in independent cohorts, cell-type-adjusted analyses, perturbation experiments, and comparison with previously reported tissue-pair modules would be needed before calling it a novel biological program.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular state in which membrane trafficking and endosomal recycling are coordinated with nuclear transport, RNA processing, and biosynthetic capacity. In skin and autonomic-related samples, cells expressing this state may maintain high demand for receptor and vesicle handling, cargo delivery, and adaptation to differentiation or signaling. AP3D1, EEA1, GRIPAP1, PIK3C2A, and EPS15 could form the trafficking-facing component, while NUP188, NUP85, SEH1L, POLR1B, and POLR2E represent coupled nuclear and transcriptional maintenance. This is a mechanistic proposal, not a demonstrated causal pathway; the module could instead partly arise from shared cell types or coordinated abundance of broadly required proteins.

### Important genes

#### MYEF2

- **Related proteins** (co-abundance neighbors): PIK3C2A (0.90), LEMD3 (0.89), EPHX1 (0.89), EML4 (0.88), NUP85 (0.86), GEMIN4 (0.86), POLR2E (0.85), EPS15 (0.84), POLR1B (0.83), ZC3HAV1 (0.83), PDIA5 (0.83), AKAP13 (0.82), GLB1 (0.82), NUP188 (0.81), AKR1B1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myelin expression factor 2. Enables RNA binding activity. Involved in myotube differentiation and neuron differentiation. Located in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: oculocutaneous albinism type 6 (0.520); neurodegenerative disease (0.442); hereditary disease (0.413); oculocutaneous albinism (0.266); tooth disorder (0.193)
- **Europe PMC papers**: 356
- **Why important**: MYEF2 is the central network hub in the supplied topology, connecting trafficking-related proteins, nuclear-pore proteins, RNA polymerase components, and other module members. Its annotation supports RNA binding, myotube differentiation, and neuron differentiation, and HPA places it in the nucleoplasm with skin protein detection and no immune-cell detection. Its disease associations include oculocutaneous albinism and neurodegenerative disease, while the literature volume is substantial relative to many less characterized module genes. These features make it a useful integrative marker, although the module does not establish that MYEF2 drives the network.
- **Conclusion**: Established evidence: MYEF2 is the topological hub and has annotations compatible with nuclear RNA regulation and neuronal or muscle differentiation. Hypothesis: MYEF2 may coordinate transcriptional or post-transcriptional state with trafficking machinery in the shared module. Direct interaction evidence with the module partners is not provided, so a causal role remains unproven.

#### PIK3C2A

- **Related proteins** (co-abundance neighbors): MYEF2 (0.90), AKAP13 (0.89), SLC29A1 (0.85), LEMD3 (0.85), AKAP8 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_10762.1, huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: phosphatidylinositol-4-phosphate 3-kinase catalytic subunit type 2 alpha. The protein encoded by this gene belongs to the phosphoinositide 3-kinase (PI3K) family. PI3-kinases play roles in signaling pathways involved in cell proliferation, oncogenic transformation, cell survival, cell migration, and intracellular protein trafficking. This protein contains a lipid kinase catalytic domain as well as a C-terminal C2 domain, a characteristic of class II PI3-kinases. C2 doma…
- **Diseases (Open Targets)**: oculocerebrodental syndrome (0.750); Short stature (0.333); Alzheimer disease (0.325); Parkinson disease (0.323); neurodegenerative disease (0.323)
- **Europe PMC papers**: 1123
- **Why important**: PIK3C2A connects the hub to AKAP13, SLC29A1, LEMD3, and AKAP8 and is represented in several hu.MAP endocytic complexes with EPS15 (hu.MAP huMAP3_10762.1), (hu.MAP huMAP3_12918.1), and (hu.MAP huMAP3_12394.1). Its annotated class-II PI3K activity, C-terminal lipid-binding domain, endocytosis, exocytosis, receptor signaling, and autophagy functions provide a plausible signaling-to-trafficking bridge. Its disease associations include oculocerebrodental syndrome and neurodegenerative disease, and it has a substantial literature base. HPA indicates broad tissue specificity and low immune specificity, consistent with a general cellular role.
- **Conclusion**: Established evidence: PIK3C2A is a trafficking and signaling protein represented in endocytic complexes and connected to the module hub. Hypothesis: it may couple local phosphoinositide signaling to endosomal recycling in the shared tissue state. The co-abundance data do not demonstrate that its kinase activity causes the module.

#### AP3D1

- **Related proteins** (co-abundance neighbors): DIS3L2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor related protein complex 3 subunit delta 1. The protein encoded by this gene is a subunit of the AP3 adaptor-like complex, which is not clathrin-associated, but is associated with the golgi region, as well as more peripheral structures. The AP-3 complex facilitates the budding of vesicles from the golgi membrane, and may be directly involved in trafficking to lysosomes. This subunit is implicated in intracellular biogenesis and trafficking …
- **Diseases (Open Targets)**: Hermansky-Pudlak syndrome 10 (0.584); Hermansky-Pudlak syndrome 2 (0.455); Hermansky-Pudlak syndrome (0.432); Alzheimer disease (0.421); lysosomal storage disease (0.417)
- **Europe PMC papers**: 637
- **Why important**: AP3D1 is one of the three genes supporting the sole globally corrected term (GO:BP synaptic vesicle endosomal processing; q_global = 0.0225). It is a component of the AP-three adaptor complex and is annotated for vesicle budding, lysosomal transport, pigment-granule biogenesis, platelet dense-granule trafficking, and neurotransmitter-vesicle trafficking. Its disease associations include Hermansky-Pudlak syndrome and lysosomal storage disease, which are directly relevant to organelle and cargo trafficking. Although its network position is peripheral, its annotation is unusually specific for the module's strongest enrichment signal.
- **Conclusion**: Established evidence: AP3D1 is a biologically credible anchor for the synaptic-vesicle endosomal-processing interpretation through (GO:BP synaptic vesicle endosomal processing; q_global = 0.0225) and its adaptor-complex function. Hypothesis: AP3D1 may mark regulated vesicle or lysosome-related trafficking shared by relevant neural and skin cell populations. The data do not establish synaptic activity in either tissue.

#### EEA1

- **Related proteins** (co-abundance neighbors): PRRC2B (0.83); STRING partners: GRIPAP1 (0.754)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Vesicles; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: early endosome antigen 1. Enables 1-phosphatidylinositol binding activity; GTP-dependent protein binding activity; and protein homodimerization activity. Involved in endocytosis; vesicle fusion; and viral RNA genome replication. Located in cytosol and early endosome. Is extrinsic component of plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: autoimmune disorder of central nervous system (0.370); liver disorder (0.298); external ear disorder (0.273); benign digestive system neoplasm (0.256); Alzheimer disease (0.163)
- **Europe PMC papers**: 7344
- **Why important**: EEA1 is another direct contributor to (GO:BP synaptic vesicle endosomal processing; q_global = 0.0225) and is annotated as an early-endosome protein involved in endocytosis, vesicle fusion, early-to-late endosome transport, and synaptic-vesicle to endosome fusion. It is linked to GRIPAP1 by a high-confidence STRING relationship, providing a direct connection between early-endosome machinery and receptor-trafficking biology. HPA places it in vesicles, with skin detection and no immune-cell detection. Its extensive literature and association with endosomal and viral processes make it a strong functional representative even though it is not a major topological hub.
- **Conclusion**: Established evidence: EEA1 supports endosomal processing in (GO:BP synaptic vesicle endosomal processing; q_global = 0.0225) and has a known relationship with GRIPAP1. Hypothesis: EEA1 could be a proximal effector of coordinated cargo recycling in the shared module. The module alone cannot distinguish neural vesicle biology from general endocytosis.

#### NUP85

- **Related proteins** (co-abundance neighbors): MYEF2 (0.86); STRING partners: NUP188 (0.992), SEH1L (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_08489.1, huMAP3_09825.1, huMAP3_12581.1, huMAP3_11232.1
- **Function (MyGene.info)**: nucleoporin 85. This gene encodes a protein component of the Nup107-160 subunit of the nuclear pore complex. Nuclear pore complexes are embedded in the nuclear envelope and promote bidirectional transport of macromolecules between the cytoplasm and nucleus. The encoded protein can also bind to the C-terminus of chemokine (C-C motif) receptor 2 (CCR2) and promote chemotaxis of monocytes, thereby participating in t…
- **Diseases (Open Targets)**: nephrotic syndrome (0.596); Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.527); Seckel syndrome (0.371)
- **Europe PMC papers**: 872
- **Why important**: NUP85 represents the best-supported nuclear-pore subsystem. It is connected by STRING to NUP188 and SEH1L, and these proteins recur together across multiple hu.MAP nuclear-pore complexes (hu.MAP huMAP3_08489.1), (hu.MAP huMAP3_09825.1), (hu.MAP huMAP3_07492.1), (hu.MAP huMAP3_09710.1), and (hu.MAP huMAP3_12581.1). NUP85 is annotated for nucleocytoplasmic transport, nuclear pore function, mRNA export, and protein import, with disease associations including nephrotic syndrome and Seckel syndrome. Its network position is not central, but its repeated complex membership gives it strong structural interpretability and shows that the module contains a real established nuclear-transport component.
- **Conclusion**: Established evidence: NUP85 participates in a known Nup107-160-related nuclear-pore subsystem, corroborated by both STRING and hu.MAP. Hypothesis: coordinated nuclear transport could support the transcriptional and trafficking demands of the shared cell state. There is no evidence here that NUP85 links directly to synaptic vesicle processing.

## Module 6

**Tissue pair**: autonomic_nervous_system and skin  
**Genes (32)**: ACSL3, AGK, APMAP, ATP1A1, BCAT1, HCCS, CD276, CENPV, CRELD2, EIPR1, ESS2, FANCI, GLS, GPD2, HDGFL2, HIBCH, L2HGDH, LDAH, LIMCH1, MLH1, IGF2R, NDC1, NOL9, NRCAM, ALDH18A1, PPM1B, PUS1, RDH11, RUFY1, TBL2, TCEA1, VPS4B

### Function

This module does not support a single formally enriched GO or KEGG function: no globally significant GO/KEGG term passed global correction. The gene-level evidence instead points to a mixed cellular program involving mitochondrial and cytosolic metabolism, especially glutamine, glutamate, branched-chain amino-acid, proline, lipid, and redox-related processes, together with RNA processing, transcription, DNA repair, vesicular trafficking, membrane transport, and neuronal cell adhesion. The strongest coherent biochemical signal is the linked glutamate and amino-acid metabolism represented by GLS, ALDH18A1, BCAT1, HIBCH, and L2HGDH. A second signal is cellular maintenance and genome integrity, represented by ESS2, FANCI, MLH1, PUS1, and HDGFL2. NRCAM and ATP1A1 provide plausible neural or excitable-cell context, but the absence of global enrichment means that this should be interpreted as a heterogeneous co-abundance program rather than a proven pathway-specific module.

**Cell composition.** The module is not dominated by secreted or plasma proteins: the HPA summary identifies only a small secreted component, with NRCAM as an example of a brain-secreted protein. Most genes are intracellular, including mitochondrial enzymes, nuclear RNA or DNA regulators, membrane proteins, and trafficking factors. The HPA profile is mixed rather than tissue specific. Many genes are cell-type enhanced, with recurring signals in neural or glial cells, epithelial and reproductive cells, and myeloid populations. Neutrophil and other blood-cell associations occur for several genes, including IGF2R, GPD2, APMAP, ACSL3, FANCI, and L2HGDH, but the overall profile does not establish a blood-cell module. Protein detection in skin is broad, whereas autonomic-nervous-system protein evidence is unavailable in the HPA comparison. Thus, shared cell types, tissue handling, or a general intracellular state could contribute to the cross-tissue co-abundance, and a specific autonomic-neural interpretation should not be assumed.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supplies a limited but biologically coherent set of high-confidence relationships: ALDH18A1 connects with GLS and BCAT1, GLS connects with L2HGDH, and FANCI connects with MLH1. These relationships support a real metabolic subnetwork centered on glutamine and related carbon metabolism, plus a genome-maintenance connection, but they do not explain the whole module. Most module pairs lack STRING support, and STRING functional enrichment is absent. hu.MAP provides orthogonal complex evidence. (hu.MAP huMAP3_13468.1) places GLS, ALDH18A1, and PUS1 in a broad mitochondrial or metabolic complex context; (hu.MAP huMAP3_10458.1) independently places GLS and PUS1 in another complex; and (hu.MAP huMAP3_09592.1) places ACSL3 and FANCI in a broad membrane, lipid, and genome-maintenance complex context. Because each complex contains many members outside the module, these findings support participation in known cellular machinery rather than a module-specific physical complex. Overall, the network appears to combine a supported metabolic core with more weakly connected cellular processes.

**STRING interactions (score >= 0.7)**: 4 of 496 gene pairs: ALDH18A1–BCAT1 (0.729); ALDH18A1–GLS (0.973); FANCI–MLH1 (0.789); GLS–L2HGDH (0.829)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (GLS, ALDH18A1, PUS1; 3/99); huMAP3_10458.1 (GLS, PUS1; 2/16); huMAP3_09592.1 (ACSL3, FANCI; 2/95)

### Novelty

The module should not be called a newly discovered biological pathway. Its most interpretable relationships are already known through STRING or hu.MAP (hu.MAP huMAP3_13468.1) (hu.MAP huMAP3_10458.1) (hu.MAP huMAP3_09592.1), and the individual genes have established biochemical or cellular functions. The potentially novel aspect is the cross-tissue co-abundance of this particular combination in autonomic nervous system and skin, especially the juxtaposition of glutamine-related metabolism, lipid handling, RNA or DNA maintenance, and neural or epithelial context. That claim remains provisional because the module has no globally corrected GO or KEGG enrichment, limited direct interaction support, mixed HPA cell-type signals, and no independent replication or perturbation evidence in the fact sheet. Absence from STRING or hu.MAP for many pairs is evidence of incomplete prior annotation, not proof that the co-abundance pattern is novel.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular stress or homeostatic state in metabolically active autonomic-neural and skin-associated cells, in which mitochondrial amino-acid and lipid metabolism supplies energy and biosynthetic intermediates while RNA processing, DNA repair, membrane trafficking, and ion-gradient maintenance preserve cell function. GLS, ALDH18A1, BCAT1, HIBCH, and L2HGDH could form a metabolic arm; ATP1A1, AGK, ACSL3, and LDAH could support membrane and lipid homeostasis; and ESS2, PUS1, FANCI, MLH1, and HDGFL2 could reflect maintenance of RNA or genome integrity. NRCAM may connect this state to neural adhesion or signaling. This is a mechanistic model, not an established causal explanation; it requires validation by cell-resolved expression, protein measurements, perturbation, and metabolic or stress-response assays.

### Important genes

#### GLS

- **Related proteins** (co-abundance neighbors): NRCAM (0.90), IGF2R (0.82); STRING partners: ALDH18A1 (0.973), L2HGDH (0.829)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10458.1
- **Function (MyGene.info)**: glutaminase. This gene encodes the K-type mitochondrial glutaminase. The encoded protein is an phosphate-activated amidohydrolase that catalyzes the hydrolysis of glutamine to glutamate and ammonia. This protein is primarily expressed in the brain and kidney plays an essential role in generating energy for metabolism, synthesizing the brain neurotransmitter glutamate and maintaining acid-base balance in the ki…
- **Diseases (Open Targets)**: global developmental delay, progressive ataxia, and elevated glutamine (0.662); genetic developmental and epileptic encephalopathy (0.626); infantile cataract, skin abnormalities, glutamate excess, and impaired intellectual development (0.591); neurodegenerative disease (0.372); glutaminase deficiency (0.371)
- **Europe PMC papers**: 15605
- **Why important**: GLS is a key metabolic hub within the supported core: it connects to NRCAM and IGF2R in the co-abundance graph, has direct STRING support with ALDH18A1 and L2HGDH, and appears in both hu.MAP complexes (hu.MAP huMAP3_13468.1) (hu.MAP huMAP3_10458.1). Its established function is mitochondrial glutamine hydrolysis to glutamate and ammonia, with relevance to brain metabolism and renal acid-base biology. Its disease associations include developmental and epileptic disorders, glutaminase deficiency, and other neurological phenotypes, and it has an extensive literature.
- **Conclusion**: Established: GLS is a mitochondrial glutamine-metabolism enzyme with strong database, interaction, complex, and disease support. Hypothesis: its position in this shared module may indicate coordinated glutamine utilization across neural and skin-associated cells, but the module alone does not establish altered glutaminase activity.

#### ALDH18A1

- **Related proteins** (co-abundance neighbors): AGK (0.84), GPD2 (0.80); STRING partners: BCAT1 (0.729), GLS (0.973)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: aldehyde dehydrogenase 18 family member A1. This gene is a member of the aldehyde dehydrogenase family and encodes a bifunctional ATP- and NADPH-dependent mitochondrial enzyme with both gamma-glutamyl kinase and gamma-glutamyl phosphate reductase activities. The encoded protein catalyzes the reduction of glutamate to delta1-pyrroline-5-carboxylate, a critical step in the de novo biosynthesis of proline, ornithine and arginine. Mutations in …
- **Diseases (Open Targets)**: ALDH18A1-related de Barsy syndrome (0.832); cutis laxa, autosomal dominant 3 (0.816); autosomal recessive complex spastic paraplegia type 9B (0.814); de Barsy syndrome (0.731); autosomal dominant spastic paraplegia type 9 (0.706)
- **Europe PMC papers**: 1168
- **Why important**: ALDH18A1 is connected to GLS and BCAT1 through STRING and to GLS and PUS1 through hu.MAP (hu.MAP huMAP3_13468.1). It is a mitochondrial enzyme that channels glutamate toward proline, ornithine, and arginine biosynthesis, making it a plausible metabolic bridge between amino-acid utilization and biosynthetic or stress responses. Its established disease associations include de Barsy syndrome, cutis laxa, and hereditary spastic paraplegia, with substantial literature. Its skin protein detection and salivary-gland enhancement also provide tissue-contextual support.
- **Conclusion**: Established: ALDH18A1 has a defined mitochondrial biosynthetic function and supported links to the module’s metabolic core. Hypothesis: coordinated ALDH18A1 and GLS abundance may regulate glutamate allocation between energy production and proline or arginine biosynthesis in the shared tissue state.

#### ESS2

- **Related proteins** (co-abundance neighbors): VPS4B (0.84), PUS1 (0.84), PPM1B (0.83), HIBCH (0.83), TCEA1 (0.82), RUFY1 (0.82), FANCI (0.82), HDGFL2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ess-2 spliceosome associated protein. This gene is located within the minimal DGS critical region (MDGCR) thought to contain the gene(s) responsible for a group of developmental disorders. These disorders include DiGeorge syndrome, velocardiofacial syndrome, conotruncal anomaly face syndrome, and some familial or sporadic conotruncal cardiac defects which have been associated with microdeletion of 22q11.2. The encoded protein may be a…
- **Diseases (Open Targets)**: arthropathy (0.097); prostate carcinoma (0.076); Familial prostate cancer (0.076); prostate cancer (0.076); alcohol drinking (0.038)
- **Europe PMC papers**: 173
- **Why important**: ESS2 is the most structurally central node in the co-abundance graph and links multiple otherwise separate branches, including PUS1, FANCI, HIBCH, TCEA1, RUFY1, HDGFL2, and VPS4B. It has no STRING or hu.MAP support in the supplied data, which makes its network centrality particularly informative but also more uncertain. Its annotation supports spliceosome-associated mRNA splicing and nervous-system development, and its disease context includes the DiGeorge syndrome critical region. Its literature volume is more limited than that of the major metabolic genes.
- **Conclusion**: Established: ESS2 is a spliceosome-associated gene with a central co-abundance position and relevant developmental annotation. Hypothesis: ESS2 may coordinate RNA processing with the metabolic and cellular-maintenance state, but its centrality could also reflect shared regulation rather than direct molecular interactions.

#### NRCAM

- **Related proteins** (co-abundance neighbors): GLS (0.90), IGF2R (0.88), CD276 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neuronal cell adhesion molecule. Cell adhesion molecules (CAMs) are members of the immunoglobulin superfamily. This gene encodes a neuronal cell adhesion molecule with multiple immunoglobulin-like C2-type domains and fibronectin type-III domains. This ankyrin-binding protein is involved in neuron-neuron adhesion and promotes directional signaling during axonal cone growth. This gene is also expressed in non-neural tissues and may…
- **Diseases (Open Targets)**: neurodevelopmental disorder with neuromuscular and skeletal abnormalities (0.774); complex neurodevelopmental disorder (0.370); stroke disorder (0.261); alcohol drinking (0.257); ovarian neoplasm (0.255)
- **Europe PMC papers**: 2314
- **Why important**: NRCAM is the clearest neural-context gene in the module. It is connected to GLS, IGF2R, and CD276, is enhanced in brain, adrenal, and retinal tissues, and is associated with neuronal adhesion, axon guidance, axonogenesis, and synaptic assembly. It is also linked to neurodevelopmental disorders and has a substantial literature. Its association with GLS creates a biologically plausible interface between neural cell communication and mitochondrial glutamate metabolism, although the direct relationship is not supported by STRING in the supplied evidence.
- **Conclusion**: Established: NRCAM is a neuronal cell-adhesion molecule with strong neural annotation and disease relevance. Hypothesis: NRCAM may mark a neural or neuroectodermal cellular component shared with skin rather than drive the module’s metabolic behavior.

#### MLH1

- **Related proteins** (co-abundance neighbors): EIPR1 (0.81), BCAT1 (0.80); STRING partners: FANCI (0.789)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutL homolog 1. The protein encoded by this gene can heterodimerize with mismatch repair endonuclease PMS2 to form MutL alpha, part of the DNA mismatch repair system. When MutL alpha is bound by MutS beta and some accessory proteins, the PMS2 subunit of MutL alpha introduces a single-strand break near DNA mismatches, providing an entry point for exonuclease degradation. The encoded protein is also involved in DNA…
- **Diseases (Open Targets)**: Lynch syndrome (0.848); colorectal cancer (0.820); mismatch repair cancer syndrome 1 (0.806); Muir-Torre syndrome (0.758); colon carcinoma (0.744)
- **Europe PMC papers**: 25031
- **Why important**: MLH1 provides a well-established genome-maintenance axis. It connects to FANCI through STRING, while FANCI also occurs with ACSL3 in hu.MAP complex (hu.MAP huMAP3_09592.1). MLH1 is a core mismatch-repair protein with extensive literature and strong associations with Lynch syndrome and colorectal cancer. Its co-abundance with metabolic and RNA-processing genes may indicate a broader cell-maintenance state, although MLH1 itself has relatively low graph degree.
- **Conclusion**: Established: MLH1 performs mismatch repair and DNA-damage signaling and has strong disease evidence. Hypothesis: the MLH1-FANCI connection may indicate coordinated genome protection in cells experiencing metabolic or replication stress, but this cannot be inferred as a causal process from co-abundance alone.

## Module 7

**Tissue pair**: autonomic_nervous_system and skin  
**Genes (17)**: ADK, ARHGEF40, CETN3, CFL2, DAXX, EIF2B2, ELMOD2, HSPA13, NIPBL, NOM1, NUP43, ELAC2, SRPK1, THOC1, TTK, TXLNG, ZNFX1

### Function

The module does not have a securely defined pathway-level function: no GO or KEGG term passed global multiple-testing correction, and STRING supplied no functional enrichment. Its genes nevertheless point to a mixed intracellular program involving nuclear RNA export and processing, chromatin and transcriptional regulation, translation, nucleotide metabolism, cell-cycle control, innate defense, and cytoskeletal regulation. The co-abundance pattern is therefore better interpreted as a possible shared cellular state or regulatory program than as evidence for a single biochemical complex or pathway. The strongest network-connected genes, including THOC1, DAXX, ADK, NIPBL, and SRPK1, connect processes that could influence gene expression, RNA handling, and cellular stress responses. These interpretations are annotations and network-based hypotheses rather than globally significant enrichment results.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only one gene is annotated as secreted, while the remainder are intracellular or membrane-associated. Most genes have low tissue specificity, which is compatible with broadly expressed, housekeeping-like cellular machinery rather than a tissue-exclusive autonomic or skin program. The HPA single-cell evidence shows repeated enhancement in neutrophils and reproductive-cell populations, with additional enhancement in stromal, epithelial, muscle, and other cell types. Blood-cell specificity is low for most genes, with only a minority showing immune-cell enhancement, so the module is not clearly a blood-cell module, although sample cell composition could contribute to its signal. Protein detection in skin is widespread among the annotated genes, whereas the autonomic-nervous-system comparison lacks a matching HPA tissue assessment. The broad expression pattern and heterogeneous cell-type annotations caution against assigning the module specifically to autonomic neurons or skin cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was detected among the module genes, and no hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated here as established physical protein interactions or membership in a shared canonical complex. Known functional relationships still exist at the annotation level: THOC1 is associated with TREX-mediated messenger RNA export, NIPBL with cohesin loading and chromatin organization, SRPK1 with regulation of splicing, ADK with adenosine and purine metabolism, and DAXX with transcriptional repression and chromatin-related regulation. The lack of database-supported physical interactions favors a model of coordinated expression, shared cellular state, or indirect regulation rather than a stable multiprotein assembly.

**STRING interactions (score >= 0.7)**: 0 of 136 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may represent a novel tissue-pair co-abundance observation, because the supplied network is not reproduced as a known STRING interaction network or hu.MAP complex. However, database absence does not establish biological novelty: the pattern could arise from broad housekeeping expression, shared cell types, sample composition, technical covariance, or indirect regulation. The absence of globally significant GO or KEGG enrichment also means that the module currently lacks independent pathway-level support. A claim of a new biological mechanism would require replication in independent autonomic-nervous-system and skin datasets, control for cell composition, and targeted validation of the coordinated expression pattern.

**Hypothesis.** Hypothesis: the module reflects a broadly expressed intracellular adaptation that couples RNA processing, transcriptional and chromatin control, nucleotide availability, translation, and stress or innate-defense responses across cells represented in autonomic-nervous-system and skin samples. ADK could influence cellular signaling through adenosine and nucleotide salvage, while THOC1, SRPK1, DAXX, and NIPBL could coordinate RNA export, splicing, transcriptional repression, and chromatin organization. The remaining genes may represent linked cell-cycle, nucleocytoplasmic-transport, cytoskeletal, and protein-folding states rather than components of one physical complex. This is a testable hypothesis, not an established module function.

### Important genes

#### THOC1

- **Related proteins** (co-abundance neighbors): ELAC2 (0.84), HSPA13 (0.83), ADK (0.83), TXLNG (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: THO complex subunit 1. HPR1 is part of the TREX (transcription/export) complex, which includes TEX1 (MIM 606929), THO2 (MIM 300395), ALY (MIM 604171), and UAP56 (MIM 142560).[supplied by OMIM, Nov 2010]
- **Diseases (Open Targets)**: neurodegenerative disease (0.409); hearing loss, autosomal dominant 86 (0.362); alcohol drinking (0.231); urolithiasis (0.231); immune system disorder (0.226)
- **Europe PMC papers**: 804
- **Why important**: THOC1 has among the strongest network connectivity in the module and links ELAC2, HSPA13, ADK, and TXLNG. It is a component of the TREX transcription and messenger RNA export machinery, is localized to nuclear speckles, and has substantial literature support. Its broad tissue and cell-type profile makes it a plausible marker of a general RNA-handling state rather than a skin-specific factor.
- **Conclusion**: Established evidence supports a role for THOC1 in messenger RNA export and TREX-related nuclear RNA handling. It is reasonable to regard THOC1 as a network anchor for the module's RNA-processing aspect. It is not established that THOC1 mechanistically drives the shared autonomic-nervous-system and skin co-abundance pattern.

#### DAXX

- **Related proteins** (co-abundance neighbors): TXLNG (0.85), NIPBL (0.82), ADK (0.82), SRPK1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: death domain associated protein. This gene encodes a multifunctional protein that resides in multiple locations in the nucleus and in the cytoplasm. It interacts with a wide variety of proteins, such as apoptosis antigen Fas, centromere protein C, and transcription factor erythroblastosis virus E26 oncogene homolog 1. In the nucleus, the encoded protein functions as a potent transcription repressor that binds to sumoylated transc…
- **Diseases (Open Targets)**: pancreatic neuroendocrine tumor (0.465); viral infectious disease (0.465); dengue disease (0.464); cancer (0.394); melanoma (0.372)
- **Europe PMC papers**: 5810
- **Why important**: DAXX is among the most connected genes and links TXLNG, NIPBL, ADK, and SRPK1. It is a multifunctional nuclear and cytoplasmic protein involved in transcriptional repression, chromatin remodeling, gene-expression regulation, and death-receptor-associated signaling. Its extensive literature and disease associations make it a biologically informative candidate for interpreting a regulatory rather than structural module.
- **Conclusion**: Established evidence supports DAXX as a regulator of transcription and chromatin-associated cellular responses. Its position makes it a plausible integrator of the module's nuclear regulatory signals. A direct DAXX-centered mechanism for this tissue-pair module remains hypothetical because neither STRING nor hu.MAP provides supporting within-module physical relationships.

#### ADK

- **Related proteins** (co-abundance neighbors): THOC1 (0.83), DAXX (0.82), NOM1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenosine kinase. This gene an enzyme which catalyzes the transfer of the gamma-phosphate from ATP to adenosine, thereby serving as a regulator of concentrations of both extracellular adenosine and intracellular adenine nucleotides. Adenosine has widespread effects on the cardiovascular, nervous, respiratory, and immune systems and inhibitors of the enzyme could play an important pharmacological role in increasing …
- **Diseases (Open Targets)**: adenosine kinase deficiency (0.780); autosomal recessive non-syndromic intellectual disability (0.370); neurodegenerative disease (0.320); hypertensive disorder (0.294); essential hypertension (0.287)
- **Europe PMC papers**: 5244
- **Why important**: ADK is highly connected and links THOC1, DAXX, and NOM1. It controls adenosine phosphorylation and purine-nucleotide salvage, thereby connecting metabolism with signaling in nervous, cardiovascular, respiratory, and immune contexts. Its disease associations and substantial literature make it a strong candidate for a metabolic or signaling contribution to the module.
- **Conclusion**: Established evidence supports ADK as an enzyme regulating intracellular adenine-nucleotide metabolism and extracellular adenosine availability. ADK could provide a metabolic context for coordinated expression of the module. It is not established that altered adenosine metabolism explains the co-abundance pattern, so that interpretation requires direct metabolic and expression validation.

#### NIPBL

- **Related proteins** (co-abundance neighbors): ZNFX1 (0.82), DAXX (0.82), SRPK1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NIPBL cohesin loading factor. This gene encodes the homolog of the Drosophila melanogaster Nipped-B gene product and fungal Scc2-type sister chromatid cohesion proteins. The Drosophila protein facilitates enhancer-promoter communication of remote enhancers and plays a role in developmental regulation. It is also homologous to a family of chromosomal adherins with broad roles in sister chromatid cohesion, chromosome condensatio…
- **Diseases (Open Targets)**: Cornelia de Lange syndrome (0.864); hereditary disease (0.544); Dislocated radial head (0.462); Intellectual disability (0.384); low grade glioma (0.370)
- **Europe PMC papers**: 2494
- **Why important**: NIPBL connects ZNFX1, DAXX, and SRPK1 and occupies a central position within the module's regulatory subnetwork. It is the cohesin-loading factor associated with enhancer-promoter communication, chromosome organization, transcriptional regulation, development, and DNA repair. Its strong disease relevance, including Cornelia de Lange syndrome, supports its importance as a biologically consequential regulatory gene.
- **Conclusion**: Established evidence supports NIPBL in cohesin loading, chromatin organization, and developmental gene regulation. Its network placement is consistent with a possible transcriptional and chromatin-regulatory component. The module does not establish that NIPBL activity is altered or that it mediates the shared tissue signal.

#### SRPK1

- **Related proteins** (co-abundance neighbors): ZNFX1 (0.82), DAXX (0.81), NIPBL (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SRSF protein kinase 1. This gene encodes a serine/arginine protein kinase specific for the SR (serine/arginine-rich domain) family of splicing factors. The protein localizes to the nucleus and the cytoplasm. It is thought to play a role in regulation of both constitutive and alternative splicing by regulating intracellular localization of splicing factors. Alternative splicing of this gene results in multiple transcript…
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); COVID-19 (0.372); celiac disease (0.190); ulcerative colitis (0.132); type 1 diabetes mellitus (0.123)
- **Europe PMC papers**: 1777
- **Why important**: SRPK1 links ZNFX1, DAXX, and NIPBL and is positioned within the module's regulatory core. It phosphorylates SR splicing factors and is associated with RNA splicing, spliceosomal assembly, chromosome segregation, and signal transduction. Its disease literature and cell-type annotations, including neutrophil-related enhancement, make it useful for connecting RNA processing with possible cell-state effects.
- **Conclusion**: Established evidence supports SRPK1 as a regulator of SR-protein localization and pre-messenger-RNA splicing. It is a plausible contributor to coordinated RNA-processing variation in the module. Whether SRPK1 links the module to immune-cell composition or to tissue biology is unresolved and should be tested rather than inferred from the co-abundance network alone.

## Module 8

**Tissue pair**: autonomic_nervous_system and skin  
**Genes (38)**: AGO2, AQR, ARFIP2, ATRX, BUB1B, PPP3R1, CDC73, DDX54, POLD1, ECT2, FOXRED1, KIF22, LRRFIP2, MCM2, MSH2, NSF, NUP98, PRRC2A, RAB3A, RIF1, RPAP3, POLR2A, POLR2D, POLR3A, SAP30, SEC24C, SETDB1, TMEM97, SRPK2, SRSF5, STAG2, TBCEL, TRIM24, TRMT11, SNRNP200, UBR5, UHRF1, ZMYND8

### Function

The primary, globally corrected GO evidence supports a chromosome and chromatin-associated module (GO:CC chromosome; q_global = 0.00383) (GO:CC chromatin; q_global = 0.0183). The contributing genes include chromatin regulators, transcription machinery, DNA replication and repair factors, chromosome-segregation proteins, and RNA-processing components. STRING supplementary annotations independently place many members in the nucleus, nucleoplasm, and chromosome-associated compartments (STRING Keyword Nucleus; within-query FDR = 0.0239) (STRING Component Nucleoplasm; within-query FDR = 0.0498) (STRING Component Chromosome; within-query FDR = 0.0498). The most defensible interpretation is a nuclear genome-maintenance and gene-regulation program, combining chromatin organization with transcriptional control, DNA replication or repair, and cell-cycle chromosome handling. The evidence does not establish a tissue-specific autonomic or skin function, and no KEGG term is provided as globally significant.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. Most members have low tissue specificity, and most also have low immune-cell specificity, which is consistent with broadly expressed nuclear machinery rather than a specialized circulating compartment. Nevertheless, several genes show enhancement in bone marrow, lymphoid tissue, testis, or progenitor populations, including erythrocyte, monocyte, neutrophil, and megakaryocyte progenitors. This raises the possibility that part of the shared signal reflects proliferative or progenitor-cell content in the samples rather than a distinctive autonomic-nervous-system or skin program. HPA protein detection is available for skin for many members, whereas there is no matching autonomic-nervous-system tissue assessment. The module therefore appears chiefly intracellular and nuclear, with a substantial housekeeping or cell-state component and a possible contribution from shared proliferating cell types.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chromosome | 0.00383 | ATRX, BUB1B, CDC73, KIF22, MCM2, MSH2, NUP98, POLD1, POLR2A, RIF1, SAP30, SETDB1, SRPK2, STAG2, TRIM24, UBR5, UHRF1, ZMYND8 |
| GO:CC chromatin | 0.0183 | ATRX, KIF22, MCM2, POLR2A, RIF1, SAP30, SRPK2, STAG2, TRIM24, UBR5, UHRF1, ZMYND8 |

### STRING and hu.MAP

STRING supports selected known relationships rather than a uniformly connected physical complex. Examples include the ATRX–SETDB1 and ATRX–STAG2 chromatin relationships, SETDB1–UHRF1, MCM2–POLD1 and MSH2–POLD1 replication or repair relationships, POLR2A–POLR2D and CDC73–POLR2A transcription relationships, AQR–SNRNP200 spliceosomal coupling, and SRPK2–SRSF5 splicing coupling. The BUB1B links to ECT2, KIF22, NUP98, and UBR5 connect checkpoint, chromosome, and nuclear regulatory functions. hu.MAP independently places module members in recurring RNA polymerase-associated complexes (hu.MAP huMAP3_11092.1) (hu.MAP huMAP3_14318.1) (hu.MAP huMAP3_09843.1) (hu.MAP huMAP3_08487.1) (hu.MAP huMAP3_06426.1) (hu.MAP huMAP3_10747.1) (hu.MAP huMAP3_07454.1) (hu.MAP huMAP3_07749.1) (hu.MAP huMAP3_00807.1) (hu.MAP huMAP3_09057.1), spliceosomal complexes containing AQR and SNRNP200 (hu.MAP huMAP3_06726.1) (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1), and a chromatin or histone-associated complex containing ATRX and MCM2 (hu.MAP huMAP3_10747.1). These concordant relationships show that the module contains genuine known molecular machinery, but the module itself is broader than any single complex. The absence of a hu.MAP assignment for many genes and the presence of several loosely connected branches argue for a coordinated cellular state or co-abundance program rather than one purified biochemical assembly.

**STRING interactions (score >= 0.7)**: 16 of 703 gene pairs: AGO2–POLR2A (0.78); AQR–SNRNP200 (0.994); ATRX–SETDB1 (0.786); ATRX–STAG2 (0.73); BUB1B–ECT2 (0.864); BUB1B–KIF22 (0.709); BUB1B–NUP98 (0.833); BUB1B–UBR5 (0.782); CDC73–POLR2A (0.999); CDC73–POLR2D (0.932); MCM2–POLD1 (0.959); MSH2–POLD1 (0.994); POLR2A–POLR2D (0.999); POLR3A–RPAP3 (0.882); SETDB1–UHRF1 (0.716); SRPK2–SRSF5 (0.901)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Nucleus (FDR = 0.0239, 28 genes); Component Nucleoplasm (FDR = 0.0498, 27 genes); Component Chromosome (FDR = 0.0498, 15 genes); Keyword Zinc (FDR = 0.0499, 12 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11092.1 (POLR3A, POLR2D, POLR2A, CDC73, RPAP3; 5/65); huMAP3_14318.1 (POLR3A, POLR2D, POLR2A, RPAP3; 4/58); huMAP3_09843.1 (POLR2D, POLR2A, CDC73; 3/29); huMAP3_08487.1 (POLR3A, POLR2A, RPAP3; 3/37); huMAP3_06426.1 (POLR3A, POLR2A, RPAP3; 3/38); huMAP3_10747.1 (ATRX, MCM2; 2/25); huMAP3_07454.1 (POLR2D, CDC73; 2/27); huMAP3_07749.1 (POLR2D, CDC73; 2/28); huMAP3_00807.1 (POLR3A, RPAP3; 2/30); huMAP3_09057.1 (POLR3A, RPAP3; 2/36); huMAP3_06726.1 (AQR, SNRNP200; 2/37); huMAP3_08501.1 (AQR, SNRNP200; 2/47); huMAP3_09504.1 (AQR, SNRNP200; 2/51); huMAP3_09945.1 (AQR, SNRNP200; 2/61); huMAP3_05807.1 (SRPK2, DDX54; 2/81)

### Novelty

The exact conserved co-abundance module across autonomic nervous system and skin is not established as a known biological entity by the supplied evidence. Its component relationships are largely familiar: transcriptional machinery, chromatin regulators, DNA replication and repair proteins, checkpoint factors, and spliceosomal proteins are already represented in STRING and hu.MAP. Thus the likely novel aspect is the cross-tissue co-abundance pattern and its particular combination of genes, not the discovery of previously unknown molecular interactions. The result is suggestive of a reproducible shared nuclear cell state, but novelty should remain provisional until independently replicated, tested against cell-composition covariates, and compared with published cross-tissue coexpression modules. Lack of a STRING or hu.MAP record for the entire module is not evidence by itself that the module is novel.

**Hypothesis.** Hypothesis: the conserved module reflects a shared proliferative or stress-responsive nuclear state in cells present in both tissue groups. Coordinated chromatin regulation by TRIM24, ATRX, SETDB1, SAP30, ZMYND8, and UHRF1 could help organize transcriptionally active and repressed chromatin, while POLR2A and associated polymerase components execute gene transcription. MCM2, POLD1, and MSH2 could support replication competence and genome surveillance, with BUB1B, KIF22, and STAG2 contributing to chromosome segregation. RNA-processing members may couple this state to transcript maturation. In skin, the state could accompany renewal or repair; in autonomic-nervous-system samples, it could arise from shared progenitor, glial, vascular, immune, or other proliferative cell content. This is a mechanistic hypothesis, not a demonstrated tissue-specific pathway, and it should be tested by cell-type-resolved expression, proliferation markers, perturbation of chromatin regulators, and replication in independent cohorts.

### Important genes

#### TRIM24

- **Related proteins** (co-abundance neighbors): POLR2A (0.87), KIF22 (0.85), CDC73 (0.85), ATRX (0.82), SETDB1 (0.81), SEC24C (0.81), MCM2 (0.80), NUP98 (0.80), STAG2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tripartite motif containing 24. The protein encoded by this gene mediates transcriptional control by interaction with the activation function 2 (AF2) region of several nuclear receptors, including the estrogen, retinoic acid, and vitamin D3 receptors. The protein localizes to nuclear bodies and is thought to associate with chromatin and heterochromatin-associated factors. The protein is a member of the tripartite motif (TRIM) fa…
- **Diseases (Open Targets)**: cancer (0.609); neurodegenerative disease (0.540); leukemia (0.380); lung adenocarcinoma (0.374); acute lymphoblastic leukemia (0.372)
- **Europe PMC papers**: 2114
- **Why important**: TRIM24 is the strongest network hub in the supplied module and connects directly to POLR2A, KIF22, CDC73, ATRX, SETDB1, SEC24C, MCM2, and NUP98. It is present in both primary chromosome and chromatin terms (GO:CC chromosome; q_global = 0.00383) (GO:CC chromatin; q_global = 0.0183) and in all listed STRING supplementary compartments (4 supplementary STRING terms; within-query FDR 0.0239–0.0499). Its established functions include transcriptional control through nuclear-receptor interactions, chromatin or heterochromatin association, and ubiquitin-related regulation. It is detected in skin by HPA and has extensive literature and disease-association coverage.
- **Conclusion**: Established evidence supports TRIM24 as a central chromatin and transcriptional organizer and as the most influential topological connector in this module. Its centrality makes it a strong candidate for coordinating the module, but the co-abundance data do not prove that TRIM24 regulates the other module members in these tissues.

#### POLR2A

- **Related proteins** (co-abundance neighbors): TRIM24 (0.87), ECT2 (0.81); STRING partners: AGO2 (0.78), CDC73 (0.999), POLR2D (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11092.1, huMAP3_14318.1, huMAP3_09843.1, huMAP3_08487.1, huMAP3_06426.1
- **Function (MyGene.info)**: RNA polymerase II subunit A. This gene encodes the largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene contains a carboxy terminal domain composed of heptapeptide repeats that are essential for polymerase activity. These repeats contain serine and threonine residues that are phosphorylated in actively transcribing RNA polymerase. In addition, …
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and variable intellectual and behavioral abnormalities (0.738); HIV infectious disease (0.600); hereditary disease (0.479); syndromic intellectual disability (0.462); Orthomyxoviridae infectious disease (0.374)
- **Europe PMC papers**: 4546
- **Why important**: POLR2A is the catalytic core subunit of RNA polymerase II and is included in both primary chromosome and chromatin terms (GO:CC chromosome; q_global = 0.00383) (GO:CC chromatin; q_global = 0.0183). It connects in STRING to CDC73 and POLR2D with strong support and to AGO2, and it participates in several hu.MAP polymerase-associated complexes (hu.MAP huMAP3_11092.1) (hu.MAP huMAP3_14318.1) (hu.MAP huMAP3_09843.1) (hu.MAP huMAP3_08487.1) (hu.MAP huMAP3_06426.1). It is also one of the clearest molecular bridges between the module and general transcriptional machinery.
- **Conclusion**: Established evidence identifies POLR2A as a core transcriptional component embedded in known polymerase complexes. Its presence supports a transcription-linked interpretation of the module, but because RNA polymerase components are broadly expressed, it is not evidence for an autonomic- or skin-specific mechanism.

#### ATRX

- **Related proteins** (co-abundance neighbors): TBCEL (0.83), TRIM24 (0.82); STRING partners: SETDB1 (0.786), STAG2 (0.73)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_10747.1
- **Function (MyGene.info)**: ATRX chromatin remodeler. The protein encoded by this gene contains an ATPase/helicase domain, and thus it belongs to the SWI/SNF family of chromatin remodeling proteins. This protein is found to undergo cell cycle-dependent phosphorylation, which regulates its nuclear matrix and chromatin association, and suggests its involvement in the gene regulation at interphase and chromosomal segregation in mitosis. Mutations in thi…
- **Diseases (Open Targets)**: alpha thalassemia-X-linked intellectual disability syndrome (0.848); intellectual disability-hypotonic facies syndrome, X-linked, 1 (0.786); alpha-thalassemia-myelodysplastic syndrome (0.664); alpha thalassemia-intellectual disability syndrome type 1 (0.606); ATR-X-related syndrome (0.568)
- **Europe PMC papers**: 12307
- **Why important**: ATRX is included in both primary chromosome and chromatin terms (GO:CC chromosome; q_global = 0.00383) (GO:CC chromatin; q_global = 0.0183), has STRING relationships with SETDB1 and STAG2, and appears with MCM2 in a hu.MAP chromatin or histone-associated complex (hu.MAP huMAP3_10747.1). Its established functions include chromatin remodeling, heterochromatin organization, transcriptional regulation, DNA replication-related control, and DNA-damage signaling. It is detected in skin and has strong disease associations involving intellectual disability and alpha-thalassemia-related syndromes.
- **Conclusion**: Established evidence supports ATRX as a mechanistically relevant chromatin and genome-maintenance component. Its placement supports a chromatin-centered module interpretation, while the module does not establish whether ATRX activity is altered or merely co-abundant with other nuclear proteins.

#### MSH2

- **Related proteins** (co-abundance neighbors): BUB1B (0.88), ECT2 (0.83), TRMT11 (0.82); STRING partners: POLD1 (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutS homolog 2. This locus is frequently mutated in hereditary nonpolyposis colon cancer (HNPCC). When cloned, it was discovered to be a human homolog of the E. coli mismatch repair gene mutS, consistent with the characteristic alterations in microsatellite sequences (RER+ phenotype) found in HNPCC. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: Lynch syndrome (0.891); colorectal cancer (0.776); mismatch repair cancer syndrome (0.775); Muir-Torre syndrome (0.752); mismatch repair cancer syndrome 1 (0.740)
- **Europe PMC papers**: 22581
- **Why important**: MSH2 is a primary chromosome-term member (GO:CC chromosome; q_global = 0.00383) and has a strong STRING relationship with POLD1, alongside module connections to BUB1B and ECT2. It is an established mismatch-repair and DNA-damage-tolerance factor with a very large literature base and strong disease associations with Lynch syndrome and related colorectal cancer syndromes. HPA places it in a broadly expressed nuclear context and detects it in skin.
- **Conclusion**: Established evidence makes MSH2 a strong marker of genome surveillance and repair within the module. Its inclusion supports a genome-integrity interpretation, but it does not show that mismatch repair is activated or defective in either tissue.

#### BUB1B

- **Related proteins** (co-abundance neighbors): AGO2 (0.93), MSH2 (0.88), ECT2 (0.84), SNRNP200 (0.82), RIF1 (0.80); STRING partners: ECT2 (0.864), KIF22 (0.709), NUP98 (0.833), UBR5 (0.782)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BUB1 mitotic checkpoint serine/threonine kinase B. This gene encodes a kinase involved in spindle checkpoint function. The protein has been localized to the kinetochore and plays a role in the inhibition of the anaphase-promoting complex/cyclosome (APC/C), delaying the onset of anaphase and ensuring proper chromosome segregation. Impaired spindle checkpoint function has been found in many forms of cancer. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: mosaic variegated aneuploidy syndrome (0.815); mosaic variegated aneuploidy syndrome 1 (0.794); premature chromatid separation trait (0.631); neurodegenerative disease (0.537); colorectal cancer (0.503)
- **Europe PMC papers**: 3723
- **Why important**: BUB1B is included in the primary chromosome term (GO:CC chromosome; q_global = 0.00383) and connects the module to ECT2, KIF22, NUP98, UBR5, MSH2, and RIF1 through the supplied STRING network. Its established function is the spindle-assembly checkpoint, delaying anaphase and supporting accurate chromosome segregation. HPA shows enhancement in bone marrow, lymphoid tissue, and testis, as well as several progenitor populations, and its disease associations include mosaic variegated aneuploidy syndromes.
- **Conclusion**: Established evidence supports BUB1B as the clearest cell-cycle checkpoint representative among the selected genes. Its progenitor-associated HPA pattern strengthens the possibility that the module partly reflects proliferative cell composition, although it does not prove that explanation.

## Module 9

**Tissue pair**: autonomic_nervous_system and skin  
**Genes (25)**: ALG3, CGN, TRIP10, DPH5, EIF2AK2, HDAC2, HEATR1, IDE, INTS3, IQGAP2, ITGA1, PRKAR2B, LUC7L, NDUFS1, NUP160, TP53I11, PFN2, SEC16A, SEC23A, SUN1, TTI1, VTA1, WDR48, XPO4, ZCCHC3

### Function

No GO or KEGG term passed global multiple-testing correction, so the module does not support a formally significant pathway assignment. The strongest biological interpretation is therefore integrative and provisional: a dispersed intracellular maintenance module connecting epithelial junction and cytoskeletal organization, nucleocytoplasmic transport, RNA processing and genome surveillance, mitochondrial respiration, and secretory-pathway trafficking. CGN is the principal network hub and links adhesion-related biology with XPO4, HDAC2, NDUFS1, PRKAR2B, NUP160, VTA1, and other module members. The module also contains coherent local processes: XPO4 and NUP160 support nuclear transport; INTS3 and HEATR1 support RNA processing and genome stability; SEC16A and SEC23A support ER-to-Golgi trafficking; IQGAP2, PFN2, TRIP10, CGN, and ITGA1 support actin, adhesion, and cell morphology; and NDUFS1 supports mitochondrial respiration. These are mechanistic annotations of individual genes and local subnetworks, not evidence of globally enriched GO or KEGG biology. The weakly connected structure and absence of STRING functional enrichment argue against treating the module as a single established pathway.

**Cell composition.** The module does not resemble a plasma-protein or broadly secreted-protein module. HPA identifies only one secreted gene, IDE, and most genes have low tissue specificity rather than a shared tissue-restricted profile. Immune-cell specificity is generally low, with only a small subset showing immune enhancement or enrichment, so a blood-cell contamination explanation is not strongly supported. Protein detection is available for skin and is present for most of the genes there, whereas there is no matching HPA tissue for autonomic nervous system. The HPA pattern is heterogeneous: skeletal muscle, neuronal, epithelial, podocyte, reproductive-cell, and other cell-type signals occur across different genes. This heterogeneity is more consistent with a mixture of broadly expressed cellular machinery and selected cell-type programs than with a uniform autonomic-nervous-system or skin-specific secretory signature. Shared cell types, technical co-abundance, or common cellular state could therefore contribute to the cross-tissue module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence known relationship within the module, SEC16A--SEC23A. This pair is biologically coherent because SEC16A participates in ER export and COPII formation, while SEC23A is a COPII component involved in ER-to-Golgi transport. The same pair occurs in hu.MAP complex C6, supporting a known secretory-pathway relationship rather than an unexplained network edge. hu.MAP also repeatedly places TTI1, NUP160, INTS3, and XPO4 together in C1, C2, and related complexes, with NUP160 and XPO4 recurring in additional complexes and INTS3 and XPO4 recurring in another complex. These repeated memberships support a local nuclear-transport or multiprotein-complex signal. However, most module pairs are absent from the supplied high-confidence STRING network, and many hu.MAP complexes contain only a small subset of module members among many total complex members. Thus the module is not a densely established protein-interaction complex; it combines a few known relationships with many co-abundance associations that remain mechanistically unvalidated.

**STRING interactions (score >= 0.7)**: 1 of 300 gene pairs: SEC16A–SEC23A (0.988)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10202.1 (TTI1, NUP160, INTS3, XPO4; 4/52); huMAP3_11232.1 (TTI1, NUP160, INTS3, XPO4; 4/78); huMAP3_08298.1 (NUP160, XPO4; 2/24); huMAP3_09114.1 (NUP160, XPO4; 2/30); huMAP3_10287.1 (INTS3, XPO4; 2/53); huMAP3_12394.1 (SEC16A, SEC23A; 2/98)

### Novelty

The module may represent a new cross-tissue co-abundance association, but the fact sheet does not establish that it is a new biological mechanism. Its novelty is supported by the sparse overlap with high-confidence STRING interactions and by the fact that the module combines genes from several established cellular systems without a globally significant GO or KEGG term. Conversely, the individual processes and several local relationships are already well known: SEC16A--SEC23A is supported by STRING and hu.MAP, and TTI1, NUP160, INTS3, and XPO4 recur in hu.MAP complexes. Absence from STRING or hu.MAP alone cannot prove novelty, because co-abundance edges may reflect tissue state, cell composition, regulation, or context-specific interactions not represented in those resources. The defensible conclusion is that the cross-tissue module configuration is potentially novel, whereas its component biology is largely established and its unifying mechanism remains unproven.

**Hypothesis.** Hypothesis: the module captures a shared cellular-resilience state present in autonomic nervous system and skin, in which epithelial or cell-matrix architecture is coordinated with intracellular trafficking, nuclear transport, RNA and DNA quality control, mitochondrial energy production, and regulated signaling. CGN, IQGAP2, PFN2, TRIP10, and ITGA1 could connect adhesion and cytoskeletal remodeling to cell state, while XPO4, NUP160, INTS3, HDAC2, and WDR48 could coordinate nuclear transport, transcriptional or RNA processing responses, and genome surveillance. SEC16A and SEC23A could maintain secretory-pathway capacity, while NDUFS1 could support the energetic demand of remodeling. This is a hypothesis generated from local annotations and network structure, not a demonstrated pathway or causal mechanism. It should be tested by cell-type-resolved expression or proteomics, perturbation of the hub genes, and validation of the predicted interactions in both tissues.

### Important genes

#### CGN

- **Related proteins** (co-abundance neighbors): IDE (0.90), TRIP10 (0.89), XPO4 (0.87), HDAC2 (0.86), NUP160 (0.84), PRKAR2B (0.82), NDUFS1 (0.82), VTA1 (0.81), HEATR1 (0.81), INTS3 (0.81), SEC23A (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cingulin. Enables cadherin binding activity. Predicted to act upstream of or within bicellular tight junction assembly; epithelial cell morphogenesis; and microtubule cytoskeleton organization. Located in bicellular tight junction and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.359); nonsyndromic deafness (0.118); skin disorder (0.094); colorectal carcinoma (0.086); ovarian carcinoma (0.065)
- **Europe PMC papers**: 3593
- **Why important**: CGN is the most connected and strongest hub in the module, linking genes involved in adhesion, nuclear transport, cytoskeletal organization, metabolism, and vesicle biology. Its HPA localization at the plasma membrane and cell junctions, together with its cadherin-binding and epithelial-morphogenesis annotations, makes it a plausible interface between tissue architecture and intracellular state. It also has substantial literature and disease associations involving skeletal, skin, and neoplastic abnormalities.
- **Conclusion**: Established evidence supports CGN as the network hub and as a junction-associated regulator of epithelial organization and cytoskeletal behavior. Its role as the upstream organizer of the entire cross-tissue module is a hypothesis, not an established conclusion.

#### XPO4

- **Related proteins** (co-abundance neighbors): ALG3 (0.88), CGN (0.87), SUN1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10202.1, huMAP3_11232.1, huMAP3_08298.1, huMAP3_09114.1, huMAP3_10287.1
- **Function (MyGene.info)**: exportin 4. XPO4 belongs to a large family of karyopherins (see MIM 602738) that mediate the transport of proteins and other cargo between the nuclear and cytoplasmic compartments (Lipowsky et al., 2000 [PubMed 10944119]).[supplied by OMIM, Mar 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); autosomal recessive nonsyndromic hearing loss 1A (0.340); uveal melanoma (0.274); bone remodeling disease (0.181); alcohol drinking (0.167)
- **Europe PMC papers**: 400
- **Why important**: XPO4 occupies a strategically informative position near CGN, ALG3, and SUN1 and recurs across several hu.MAP complexes, making it one of the strongest complex-supported members. Its established function is nuclear export and nucleocytoplasmic transport. HPA shows skeletal-muscle enhancement and myonuclear enrichment, which is relevant to a module shared by tissues with substantial structural and excitable-cell components. Its disease associations include neurodegenerative and hearing-related disorders.
- **Conclusion**: Established evidence supports XPO4 as a nuclear transport factor with repeated complex membership. A role in coupling nuclear transport to the tissue-shared co-abundance state is plausible but remains inferential.

#### SEC16A

- **Related proteins** (co-abundance neighbors): TP53I11 (0.83); STRING partners: SEC23A (0.988)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: SEC16 homolog A, endoplasmic reticulum export factor. This gene encodes a protein that forms part of the Sec16 complex. This protein has a role in protein transport from the endoplasmic reticulum (ER) to the Golgi and mediates COPII vesicle formation at the transitional ER. Alternative splicing results in multiple transcript variants that encode different protein isoforms. [provided by RefSeq, Feb 2013].
- **Diseases (Open Targets)**: squamous cell carcinoma (0.288); Crohn disease (0.277); bladder calculus (0.241); nephrolithiasis (0.235); actinic keratosis (0.215)
- **Europe PMC papers**: 595
- **Why important**: SEC16A is one half of the module's only high-confidence STRING interaction, pairing with SEC23A, and both genes occur together in hu.MAP complex C6. SEC16A organizes ER exit sites, COPII vesicle formation, and ER-to-Golgi transport. Its skin protein detection and disease associations including squamous cell carcinoma and actinic keratosis make it especially relevant to the skin component.
- **Conclusion**: Established evidence supports SEC16A as an ER export and secretory-pathway factor and supports its relationship with SEC23A. Its co-abundance with the nuclear, adhesion, and mitochondrial genes may indicate coordinated cellular maintenance, but that broader connection is a hypothesis.

#### SEC23A

- **Related proteins** (co-abundance neighbors): CGN (0.80); STRING partners: SEC16A (0.988)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A is the partner of SEC16A in the only high-confidence STRING edge and in hu.MAP complex C6. It is a COPII component involved in cargo loading, vesicle budding, and ER-to-Golgi transport. Its established disease associations include craniolenticulosutural dysplasia and metabolic conditions, while skin protein detection supports relevance to the skin samples.
- **Conclusion**: Established evidence supports SEC23A as a core COPII trafficking factor and validates the local SEC16A--SEC23A relationship. The module does not establish that SEC23A coordinates the other module branches.

#### INTS3

- **Related proteins** (co-abundance neighbors): IQGAP2 (0.85), CGN (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoli; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_10202.1, huMAP3_11232.1, huMAP3_10287.1
- **Function (MyGene.info)**: integrator complex subunit 3. The protein encoded by this gene can form a complex with human single-strand DNA binding proteins 1 or 2 (hSSB1 and hSSB2) and other proteins to mediate genome stability and the DNA damage response. The encoded protein is also part of a multiprotein complex that interacts with the C-terminal domain of RNA polymerase II large subunit to help regulate processing of U1 and U2 small nuclear RNAs. [pro…
- **Diseases (Open Targets)**: neurodegenerative disease (0.176); hypertensive disorder (0.123); Familial prostate cancer (0.111); myoepithelial tumor (0.111); prostate cancer (0.111)
- **Europe PMC papers**: 338
- **Why important**: INTS3 connects to IQGAP2 and CGN in the co-abundance graph and recurs in several hu.MAP complexes with TTI1, NUP160, and XPO4. Its established functions include Integrator-associated RNA processing, transcriptional regulation, DNA repair, and damage response. HPA shows enrichment in several neural and glial cell types, which provides a biologically plausible bridge to autonomic nervous system samples.
- **Conclusion**: Established evidence supports INTS3 as a gene-expression and genome-stability factor with repeated complex support. Its apparent coordination with adhesion and trafficking genes in this module is a hypothesis based on co-abundance and network placement.

#### IQGAP2

- **Related proteins** (co-abundance neighbors): INTS3 (0.85), TTI1 (0.85), PFN2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IQ motif containing GTPase activating protein 2. This gene encodes a member of the IQGAP family. The encoded protein contains three IQ domains, one calponin homology domain, one Ras-GAP domain and one WW domain. This protein interacts with components of the cytoskeleton, with cell adhesion molecules, and with several signaling molecules to regulate cell morphology and motility. It also acts as a tumor suppressor and has been found to play a role…
- **Diseases (Open Targets)**: prostate carcinoma (0.374); cholelithiasis (0.344); neurodegenerative disease (0.320); alcohol drinking (0.300); escherichia coli infection (0.269)
- **Europe PMC papers**: 1654
- **Why important**: IQGAP2 links TTI1, INTS3, and PFN2 and provides a bridge between signaling, actin organization, cell morphology, and the complex-associated nuclear branch. Its domain architecture and annotations support interaction with cytoskeletal and adhesion machinery, while HPA shows liver and several hematopoietic or granulocytic cell-type signals. It has a substantial literature and disease associations involving cancer, metabolic disease, and neurodegeneration.
- **Conclusion**: Established evidence supports IQGAP2 as a signaling and cytoskeletal regulator with links to cell morphology and motility. Its position suggests a possible connector between cytoskeletal and nuclear-state components, but this integrative role is not directly demonstrated.

## Module 10

**Tissue pair**: autonomic_nervous_system and skin  
**Genes (27)**: ANAPC7, ARAP1, C5orf22, CERT1, CIAO1, CNOT12, CPSF2, GPS1, EPB41L3, EXOC5, GDPGP1, GNAI1, IQGAP3, ISY1, LEO1, CDC42BPA, DR1, PDCL3, POGLUT1, POGZ, PSMG1, RBM27, SMYD3, SPATS2, STAT1, TRIM26, USP47

### Function

The module does not support a single statistically established GO or KEGG function: no globally significant GO/KEGG term passed global correction. Its internal co-abundance structure nevertheless spans several compatible cellular themes. TRIM26 and SMYD3 occupy prominent network positions and connect regulatory, chromatin, and ubiquitin-related biology; EXOC5 and CDC42BPA connect vesicle targeting, plasma-membrane organization, CDC42 signaling, and actin remodeling; POGLUT1 links the module to endoplasmic-reticulum protein glycosylation and Notch regulation; and GNAI1 provides a link to heterotrimeric G-protein signaling. These observations support a broad cellular-regulation and membrane-cytoskeleton interpretation rather than a specific pathway assignment. The module may therefore reflect coordinated abundance of proteins involved in transcriptional control, protein modification, vesicle trafficking, cell shape, and signaling, but this remains an integrative interpretation rather than an enrichment result.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a single secreted gene, and most proteins are intracellular or membrane-associated. Most genes have low tissue specificity, so the shared signal is unlikely to represent a sharply tissue-restricted autonomic or skin program. Many genes are cell-type enhanced, with recurring annotations involving epicardial cells, late spermatids, oligodendrocytes, monocytes, and neutrophils, but the overall blood-cell specificity is low. A small immune-related contribution is plausible, especially because ARAP1, C5orf22, CERT1, and related genes have myeloid or granulocyte-associated HPA annotations, yet the module does not resemble a canonical blood-cell or plasma-protein signature. Skin protein detection is common among the measured genes, whereas the autonomic nervous system has no matching HPA protein-detection category in this summary. Thus, shared cell types, broad cellular housekeeping, or sample-composition effects should be considered alongside a tissue-shared biological program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no high-confidence interaction or supplementary enrichment evidence for this module. Consequently, the co-abundance edges should not be interpreted as established physical protein interactions. hu.MAP provides one complex-level relationship (hu.MAP huMAP3_12900.1), in which ARAP1 and CNOT12 occur among members of a larger complex. This is limited support for known complex membership and does not establish that the whole module is a physical complex. The remaining genes have no reported hu.MAP complex with multiple module members in the fact sheet. Overall, the network appears to capture coordinated abundance or indirect functional coupling more than a densely documented protein-interaction assembly.

**STRING interactions (score >= 0.7)**: 0 of 351 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12900.1 (ARAP1, CNOT12; 2/50)

### Novelty

The module is plausibly a new observation as a cross-tissue co-abundance pattern, because the fact sheet provides no STRING network, only one partial hu.MAP complex overlap (hu.MAP huMAP3_12900.1), and no globally significant GO or KEGG term. However, these absences do not prove novelty. Most component genes have established individual functions, disease associations, and literature, and several pairwise biological relationships could already be known outside the databases summarized here. The defensible conclusion is that the particular conserved co-abundance configuration across autonomic nervous system and skin is insufficiently characterized by the supplied interaction and enrichment resources, rather than that every gene relationship is novel.

**Hypothesis.** Hypothesis: the module reflects a shared structural-maintenance and cellular-regulation state present in skin and autonomic nervous system samples. In this model, CDC42BPA and EXOC5 coordinate actin-dependent membrane organization and vesicle delivery, GNAI1 modulates receptor-linked signaling, POGLUT1 influences endoplasmic-reticulum glycosylation and Notch-related cell-state control, while TRIM26 and SMYD3 provide regulatory connections through ubiquitin-related and chromatin-associated processes. The co-abundance signal could arise from coordinated remodeling of cell shape, membrane trafficking, and transcriptional state, or from shared cellular composition, rather than from one discrete molecular complex. This hypothesis requires validation with independent cohorts, cell-resolved measurements, perturbation experiments, and direct interaction or activity assays.

### Important genes

#### TRIM26

- **Related proteins** (co-abundance neighbors): POGZ (0.90), CDC42BPA (0.88), SMYD3 (0.87), POGLUT1 (0.81), PDCL3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tripartite motif containing 26. The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein localizes to cytoplasmic bodies. Although the function of the protein is unknown, the RING domain suggests that the protein may have DNA-binding activity. The gene localizes to the ma…
- **Diseases (Open Targets)**: neurodegenerative disease (0.296); hepatocellular carcinoma (0.099); non-small cell lung carcinoma (0.096); colorectal carcinoma (0.081); nasopharyngeal carcinoma (0.080)
- **Europe PMC papers**: 798
- **Why important**: TRIM26 has one of the strongest network positions in the module and connects to POGZ, CDC42BPA, SMYD3, POGLUT1, and PDCL3. Its TRIM-family architecture and reported roles in ubiquitin-dependent proteolysis, antiviral innate responses, and non-canonical NF-kappaB regulation make it a plausible regulatory hub. It has skin protein detection, broad tissue distribution, disease associations including neurodegenerative disease and several cancers, and a substantial literature base.
- **Conclusion**: Established evidence supports TRIM26 as a regulatory protein with immune and ubiquitin-related functions and as a prominent co-abundance hub. It is not established that TRIM26 physically binds the neighboring module proteins or drives the shared tissue pattern. Its role as an upstream organizer of the proposed module is therefore a hypothesis.

#### SMYD3

- **Related proteins** (co-abundance neighbors): TRIM26 (0.87), CDC42BPA (0.84), POGLUT1 (0.83), ISY1 (0.82), EXOC5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SET and MYND domain containing 3. This gene encodes a histone methyltransferase which functions in RNA polymerase II complexes by an interaction with a specific RNA helicase. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2011].
- **Diseases (Open Targets)**: placental abruption (0.292); digestive system disorder (0.234); Abnormal nasolacrimal system morphology (0.234); injury (0.199); liver disorder (0.198)
- **Europe PMC papers**: 1872
- **Why important**: SMYD3 is among the strongest network nodes and connects TRIM26, CDC42BPA, POGLUT1, ISY1, and EXOC5. Its established histone-methyltransferase and RNA-polymerase-associated functions provide a plausible link between chromatin or transcriptional state and the membrane, cytoskeletal, and trafficking genes in the module. It has skin protein detection, disease associations involving developmental and systemic disorders, and a comparatively large literature base.
- **Conclusion**: Established evidence supports SMYD3 as a chromatin and transcriptional regulator. The module data do not establish that SMYD3 controls the abundance of its co-abundant neighbors, nor that its catalytic activity explains conservation across the two tissues. A transcriptional-state contribution is a reasonable but untested hypothesis.

#### EXOC5

- **Related proteins** (co-abundance neighbors): GPS1 (0.85), PDCL3 (0.81), PSMG1 (0.81), SMYD3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exocyst complex component 5. The protein encoded by this gene is a component of the exocyst complex, a multiple protein complex essential for targeting exocytic vesicles to specific docking sites on the plasma membrane. Though best characterized in yeast, the component proteins and functions of exocyst complex have been demonstrated to be highly conserved in higher eukaryotes. At least eight components of the exocyst complex,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); placental abruption (0.305); thyroid cancer (0.143); injury (0.095); placenta praevia (0.087)
- **Europe PMC papers**: 321
- **Why important**: EXOC5 is a network connector between GPS1, PDCL3, PSMG1, and SMYD3. As an exocyst component, it has a direct established role in targeting exocytic vesicles to the plasma membrane and in post-Golgi transport, with links to actin remodeling and membrane localization. It is detected in skin, has broad tissue specificity, and has disease associations including neurodegenerative disease and cancer.
- **Conclusion**: Established evidence supports EXOC5 as a vesicle-trafficking and membrane-targeting component. Its position makes it a plausible bridge between regulatory proteins and structural or signaling processes, but the fact sheet does not demonstrate a direct interaction with the neighboring module proteins or a tissue-specific exocyst mechanism.

#### CDC42BPA

- **Related proteins** (co-abundance neighbors): TRIM26 (0.88), SMYD3 (0.84), GNAI1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CDC42 binding protein kinase alpha. The protein encoded by this gene is a member of the serine/threonine protein kinase family. This kinase contains multiple functional domains. Its kinase domain is highly similar to that of the myotonic dystrophy protein kinase (DMPK). This kinase also contains a Rac interactive binding (CRIB) domain, and has been shown to bind CDC42. It may function as a CDC42 downstream effector mediating CDC42 i…
- **Diseases (Open Targets)**: neurodegenerative disease (0.518); Abnormality of the skeletal system (0.364); autosomal recessive ataxia due to ubiquinone deficiency (0.333); type 2 diabetes mellitus (0.319); stomach disorder (0.317)
- **Europe PMC papers**: 541
- **Why important**: CDC42BPA links the high-position TRIM26 and SMYD3 nodes to GNAI1. Its CDC42-responsive kinase activity and reported roles in peripheral actin formation, cytoskeletal reorganization, cell migration, and actomyosin organization provide a mechanistic route from signaling to cell shape. It is detected in skin and has disease associations spanning neurodegenerative, skeletal, metabolic, and ataxia-related conditions.
- **Conclusion**: Established evidence supports CDC42BPA as a cytoskeletal kinase and CDC42 effector. Its module position is consistent with a signaling-to-cytoskeleton bridge, but the shared co-abundance pattern does not show that CDC42BPA is active or causally responsible for tissue conservation.

#### POGLUT1

- **Related proteins** (co-abundance neighbors): SMYD3 (0.83), TRIM26 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein O-glucosyltransferase 1. This gene encodes a protein with both O-glucosyltransferase and O-xylosyltransferase activity which localizes to the lumen of the endoplasmic reticulum. This protein has a carboxy-terminal KTEL motif which is predicted to function as an endoplasmic reticulum retention signal. This gene is an essential regulator of Notch signalling and likely plays a role in cell fate and tissue formation during de…
- **Diseases (Open Targets)**: Dowling-Degos disease (0.706); autosomal recessive limb-girdle muscular dystrophy type 2U (0.696); neurodegenerative disease (0.522); autosomal recessive limb-girdle muscular dystrophy (0.370); hereditary disease (0.192)
- **Europe PMC papers**: 492
- **Why important**: POGLUT1 connects SMYD3 and TRIM26 and is the only selected gene that directly links endoplasmic-reticulum protein modification to Notch-related developmental regulation. Its established O-glycosyltransferase activities, ER retention, Notch regulation, and associations with Dowling-Degos disease and limb-girdle muscular dystrophy make it biologically informative for a module shared by neural-associated and skin-associated tissues. HPA places it in the ER and identifies intracellular and membrane localization.
- **Conclusion**: Established evidence supports POGLUT1 as an ER glycosylation enzyme and Notch pathway regulator with relevant inherited disease associations. Its contribution to this module could involve cell-state or tissue-maintenance signaling, but that connection is a hypothesis because no globally significant enrichment or direct module interaction evidence is available.

## Module 11

**Tissue pair**: autonomic_nervous_system and skin  
**Genes (35)**: ATG4B, BAZ1A, CDKN2A, CWC27, DNMT1, FLNB, GNA11, GCLC, IFIT5, CAMK2G, KIF11, LBR, LTA4H, MAP1A, MEN1, MMTAG2, NME7, NEMF, OPA1, PDLIM1, PELO, RASA1, UPF3B, SAMHD1, SETD7, DNTTIP2, TRMT10C, TNPO1, TOP2A, TPM1, URGCP, UTP25, ATP6V0A1, VTN, ZMYM4

### Function

No GO or KEGG term passed global correction, so these resources provide no globally significant functional annotation for the module. The gene and network evidence instead indicates a mixed intracellular program involving microtubule and cytoskeletal organization, chromatin regulation, DNA replication and repair, RNA surveillance, ribosome rescue, mitochondrial maintenance, autophagy, and cell proliferation. MAP1A is the principal network hub and links the module to microtubule biology and neurodevelopment. A second apparent axis comprises BAZ1A, DNMT1, SETD7, TOP2A, and related nuclear regulators, consistent with chromatin state, genome maintenance, and proliferative activity. These are integrative interpretations rather than globally corrected enrichment results.

**Cell composition.** This is not a plasma or secreted-protein module. VTN is the only explicitly secreted gene and is liver-enriched, so it could reflect a circulating or extracellular contribution rather than the core intracellular program. Most genes have low tissue specificity, and many show broad or mixed cell-type patterns. HPA evidence does show recurring enrichment in bone-marrow and blood progenitor populations, especially neutrophil and monocyte progenitors, with additional immune-cell signals. Therefore, the shared signal could partly reflect common blood or progenitor-cell content in the tissue samples. At the same time, protein detection in skin is widespread among the module genes, while several genes have tissue-enhanced profiles in brain, muscle, liver, lymphoid tissue, or bone marrow. The module should consequently not be interpreted as a uniform autonomic-neural or skin-specific program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited set of established relationships rather than a densely connected physical interaction network. The strongest-supported relationships include DNMT1–SETD7, KIF11–TOP2A, CDKN2A–RASA1, ATG4B–MAP1A, CDKN2A–DNMT1, and NEMF–PELO. These relationships support coherent submodules involving chromatin regulation, mitosis, Ras signaling, autophagy or cytoskeletal biology, and ribosome quality control, but they do not explain the entire co-abundance structure. hu.MAP provides repeated support for PELO and SAMHD1 occurring together across several complexes (hu.MAP huMAP3_08528.1), (hu.MAP huMAP3_09346.1), (hu.MAP huMAP3_07082.1), (hu.MAP huMAP3_09664.1), (hu.MAP huMAP3_10665.1), for FLNB and GNA11 in a membrane or cytoskeletal complex (hu.MAP huMAP3_05674.1), and for PDLIM1 and LTA4H in a broad complex (hu.MAP huMAP3_14442.1). DNTTIP2 and MMTAG2 also co-occur in a large complex (hu.MAP huMAP3_05807.1). Most module genes have no reported STRING or hu.MAP relationship in the supplied evidence. Thus, the co-abundance module is broader than any single established complex and likely combines several cell-state or compartmental signals.

**STRING interactions (score >= 0.7)**: 6 of 595 gene pairs: ATG4B–MAP1A (0.739); CDKN2A–DNMT1 (0.703); CDKN2A–RASA1 (0.794); DNMT1–SETD7 (0.936); KIF11–TOP2A (0.975); NEMF–PELO (0.717)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08528.1 (PELO, SAMHD1; 2/2); huMAP3_09346.1 (PELO, SAMHD1; 2/3); huMAP3_07082.1 (PELO, SAMHD1; 2/4); huMAP3_09664.1 (PELO, SAMHD1; 2/5); huMAP3_05674.1 (FLNB, GNA11; 2/12); huMAP3_10665.1 (PELO, SAMHD1; 2/42); huMAP3_14442.1 (PDLIM1, LTA4H; 2/57); huMAP3_05807.1 (DNTTIP2, MMTAG2; 2/81)

### Novelty

The module-level finding should be regarded as potentially novel but not proven to be a new biological complex or pathway. The supplied evidence does not identify a prior report of this exact conserved co-abundance module across autonomic nervous system and skin, and the particular combination of neural, cytoskeletal, chromatin, genome-maintenance, RNA-surveillance, and immune-associated genes is distinctive. However, the limited STRING connectivity, the absence of globally significant GO or KEGG enrichment, the broad HPA expression profiles, and the recurring blood-progenitor signals make a shared cell-composition or general cell-state explanation plausible. Absence from STRING or hu.MAP is not evidence of novelty. The appropriate conclusion is that this is a novel network-level observation requiring replication, cell-composition adjustment, and independent validation rather than a newly discovered molecular complex.

**Hypothesis.** Hypothesis: the conserved module reflects a shared tissue cell state involving cytoskeletal remodeling and intracellular quality control, coupled to chromatin and genome-maintenance activity. In this model, MAP1A, TPM1, FLNB, PDLIM1, and related genes represent structural remodeling; DNMT1, BAZ1A, SETD7, TOP2A, and CWC27 represent regulation of chromatin, DNA topology, and RNA processing; PELO, NEMF, and SAMHD1 represent translational surveillance, ribosome rescue, and stress or innate-immune response; and GCLC, ATG4B, OPA1, and ATP6V0A1 represent protection of cellular homeostasis. VTN and the blood-progenitor-associated HPA signals raise the alternative hypothesis that part of the shared pattern is contributed by vascular, circulating, or infiltrating cells. These mechanisms are hypotheses derived from the combined network and annotation evidence, not demonstrated causal relationships.

### Important genes

#### MAP1A

- **Related proteins** (co-abundance neighbors): PELO (0.91), UTP25 (0.89), NEMF (0.88), TRMT10C (0.85), DNMT1 (0.84), TOP2A (0.84), TPM1 (0.83), TNPO1 (0.82), CWC27 (0.82), ATP6V0A1 (0.82), BAZ1A (0.81); STRING partners: ATG4B (0.739)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: microtubule associated protein 1A. This gene encodes a protein that belongs to the microtubule-associated protein family. The proteins of this family are thought to be involved in microtubule assembly, which is an essential step in neurogenesis. The product of this gene is a precursor polypeptide that presumably undergoes proteolytic processing to generate the final MAP1A heavy chain and LC2 light chain. Expression of this gene is …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.340); venous thromboembolism (0.238); hereditary disease (0.118); autism spectrum disorder (0.094); urinary bladder cancer (0.075)
- **Europe PMC papers**: 1240
- **Why important**: MAP1A is the dominant network hub by weighted connectivity and links to PELO, NEMF, DNMT1, TOP2A, TPM1, and other module genes. Its established function is microtubule association, with roles in microtubule organization, axonogenesis, dendrite development, and neurogenesis. HPA reports brain enrichment and lack of skin protein detection, making it especially informative for the autonomic-nervous-system side of the shared module. It also has substantial literature and disease associations involving neurodevelopment.
- **Conclusion**: Established evidence supports MAP1A as a structural microtubule and neural-associated anchor of the module. It is plausible that MAP1A helps connect cytoskeletal state to the broader module, but its co-abundance with the nuclear and quality-control genes does not establish direct molecular cooperation.

#### BAZ1A

- **Related proteins** (co-abundance neighbors): GCLC (0.88), DNTTIP2 (0.85), MEN1 (0.85), CWC27 (0.85), SAMHD1 (0.84), ZMYM4 (0.84), MAP1A (0.81), DNMT1 (0.81), IFIT5 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: bromodomain adjacent to zinc finger domain 1A. The BAZ1A gene encodes the accessory subunit of the ATP-dependent chromatin assembly factor (ACF), a member of the ISWI ('imitation switch') family of chromatin remodeling complexes (summarized by Racki et al., 2009 [PubMed 20033039]).[supplied by OMIM, Apr 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); non-small cell lung carcinoma (0.405); lung adenocarcinoma (0.395); hypothyroidism (0.391); psoriasis (0.346)
- **Europe PMC papers**: 666
- **Why important**: BAZ1A is a high-connectivity hub linked to GCLC, DNTTIP2, MEN1, CWC27, SAMHD1, ZMYM4, MAP1A, and DNMT1. It is an accessory component of ATP-dependent chromatin assembly machinery and is annotated for nucleosome assembly, chromatin remodeling, DNA replication, and transcriptional regulation. HPA shows bone-marrow and neutrophil-associated enhancement, while its protein is detected in skin. Its disease associations include neurodegenerative disease, lung cancer, hypothyroidism, and psoriasis.
- **Conclusion**: Established evidence supports BAZ1A as a nuclear chromatin-regulatory component that may also track progenitor or neutrophil-related cell states. Its position makes it a strong candidate for coordinating nuclear state with the rest of the module, but that coordinating role remains a hypothesis.

#### DNMT1

- **Related proteins** (co-abundance neighbors): MAP1A (0.84), BAZ1A (0.81), NME7 (0.80), ZMYM4 (0.80); STRING partners: CDKN2A (0.703), SETD7 (0.936)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA methyltransferase 1. This gene encodes an enzyme that transfers methyl groups to cytosine nucleotides of genomic DNA. This protein is the major enzyme responsible for maintaining methylation patterns following DNA replication and shows a preference for hemi-methylated DNA. Methylation of DNA is an important component of mammalian epigenetic gene regulation. Aberrant methylation patterns are found in human tumors and a…
- **Diseases (Open Targets)**: autosomal dominant cerebellar ataxia, deafness and narcolepsy (0.806); hereditary sensory neuropathy-deafness-dementia syndrome (0.777); acute myeloid leukemia (0.623); myelodysplastic syndrome (0.615); cancer (0.612)
- **Europe PMC papers**: 30754
- **Why important**: DNMT1 connects the MAP1A and BAZ1A portions of the network and has established STRING relationships with SETD7 and CDKN2A. It maintains DNA methylation after replication and regulates transcription and constitutive heterochromatin. It is detected in skin and shows cell-type enhancement in several progenitor populations. DNMT1 has extensive literature and important associations with hereditary neurologic disease, myeloid disorders, and cancer.
- **Conclusion**: Established evidence supports DNMT1 as a central epigenetic and genome-maintenance marker in the module. The network is consistent with a shared proliferative or differentiation-related chromatin state, but it does not demonstrate that DNMT1 drives the cross-tissue co-abundance pattern.

#### TOP2A

- **Related proteins** (co-abundance neighbors): MAP1A (0.84), UPF3B (0.82), ZMYM4 (0.82), NME7 (0.81), LBR (0.80); STRING partners: KIF11 (0.975)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA topoisomerase II alpha. This gene encodes a DNA topoisomerase, an enzyme that controls and alters the topologic states of DNA during transcription. This nuclear enzyme is involved in processes such as chromosome condensation, chromatid separation, and the relief of torsional stress that occurs during DNA transcription and replication. It catalyzes the transient breaking and rejoining of two strands of duplex DNA which al…
- **Diseases (Open Targets)**: neoplasm (0.618); breast cancer (0.616); acute myeloid leukemia (0.606); plasma cell myeloma (0.594); small cell lung carcinoma (0.580)
- **Europe PMC papers**: 11752
- **Why important**: TOP2A occupies a connected nuclear position with MAP1A, UPF3B, ZMYM4, NME7, and LBR and has a very strong established STRING relationship with KIF11. Its known functions include DNA topology control, chromosome condensation, chromatid separation, and replication-associated genome maintenance. HPA shows enhancement in lymphoid tissue and several proliferative progenitor populations, with protein detection in skin. It has extensive literature and strong associations with neoplasia and hematologic malignancy.
- **Conclusion**: Established evidence supports TOP2A as a marker of proliferative, chromosome-handling, and genome-maintenance activity. Its presence may indicate proliferating cells within both tissue datasets, but the module data cannot distinguish true tissue conservation from shared proliferative-cell composition.

#### NEMF

- **Related proteins** (co-abundance neighbors): MAP1A (0.88), URGCP (0.86), LBR (0.85), MMTAG2 (0.84); STRING partners: PELO (0.717)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nuclear export mediator factor. This gene encodes a component of the ribosome quality control complex. The encoded protein facilitates the recognition and ubiquitination of stalled 60S subunits by the ubiquitin ligase listerin. A similar protein in fly functions as a tumor suppressor. [provided by RefSeq, Jul 2016].
- **Diseases (Open Targets)**: intellectual developmental disorder with speech delay and axonal peripheral neuropathy (0.708); hereditary disease (0.471); Global developmental delay (0.374); Intellectual disability (0.371); cerebellar ataxia (0.370)
- **Europe PMC papers**: 2061
- **Why important**: NEMF links MAP1A, URGCP, LBR, and MMTAG2 and has a STRING relationship with PELO. It is a component of the ribosome quality-control machinery that recognizes and helps process stalled translation products. It occurs with PELO and SAMHD1 across several hu.MAP complexes (hu.MAP huMAP3_08528.1), (hu.MAP huMAP3_09346.1), (hu.MAP huMAP3_07082.1), (hu.MAP huMAP3_09664.1), and (hu.MAP huMAP3_10665.1). It has substantial literature and disease associations involving intellectual disability, developmental delay, and peripheral neuropathy.
- **Conclusion**: Established evidence supports NEMF as a translational quality-control and proteostasis component that provides a plausible functional bridge between the structural and nuclear portions of the module. A coordinated stress-response interpretation is reasonable, but direct participation of the whole module in one ribosome-quality-control pathway is not established.

## Module 12

**Tissue pair**: autonomic_nervous_system and skin  
**Genes (37)**: ATXN2L, BID, ARFGEF1, CNOT1, CTNND1, DCAF1, DIAPH1, LIG3, GFM1, ENTR1, GEMIN8, HLTF, IGF2BP3, EIF4E, LAMC1, MCM5, ABCC1, MTMR2, NAA50, NUCB1, BCKDHA, OSBPL9, POLDIP3, PDLIM7, PIK3R4, PPP4C, PPP6R3, PTGR1, RBM22, RFC3, SNX2, DARS2, SYNE2, ACAA2, UBA6, UBE3A, YTHDF2

### Function

No GO or KEGG term passed global correction, so the module does not support a formally established pathway-level enrichment. STRING functional enrichment was also absent. The network nevertheless contains a biologically mixed set of RNA-processing and post-transcriptional regulators, DNA replication and repair factors, mitochondrial translation and metabolism proteins, vesicle and lipid-trafficking proteins, cytoskeletal regulators, and cell-adhesion or extracellular-matrix proteins. GEMIN8 is the central co-abundance connector, linking these otherwise diverse processes. The most defensible interpretation is a broad cellular maintenance and stress-adaptation module rather than a narrowly defined tissue pathway. The co-abundance pattern may reflect coordinated regulation of gene expression, proteostasis, genome maintenance, mitochondrial function, and cellular structure, but this remains an interpretation rather than an enriched-term result.

**Cell composition.** The module is not dominated by plasma or secreted proteins: HPA identifies only a small secreted subset, including NUCB1 and LAMC1. Most genes have low tissue specificity, while many show cell-type-enhanced patterns across diverse epithelial, stromal, muscle, reproductive, and hematopoietic cell types. The blood-cell evidence is mixed and generally weak: most genes have low immune-cell specificity, with only a limited subset showing immune enhancement or enrichment. Thus, a simple blood contamination explanation is not strongly supported, although shared cell types or differences in cellular composition between autonomic nervous system and skin samples could contribute. Protein detection is broadly observed in skin, whereas matching autonomic-nervous-system protein data are unavailable in the fact sheet. The composition therefore favors a broadly expressed cellular program with contributions from particular cell populations, not a plasma-protein module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a few high-confidence pairwise relationships within the module. The strongest known links connect CNOT1 with YTHDF2 and IGF2BP3 with YTHDF2, supporting an RNA stability and mRNA-decay component. MCM5 with RFC3 supports a DNA replication or repair component. The absence of STRING functional enrichment means these known links do not establish a unified pathway. hu.MAP provides more structured support: ACAA2, DARS2, and GFM1 occur together in a mitochondrial metabolism and translation complex (hu.MAP huMAP3_13468.1); DARS2 and GFM1 also recur in another related mitochondrial complex (hu.MAP huMAP3_10525.1). LIG3 and HLTF co-occur across several DNA repair and chromatin-associated complexes (hu.MAP huMAP3_10730.1), (hu.MAP huMAP3_10578.1), (hu.MAP huMAP3_14846.1), (hu.MAP huMAP3_13854.1). UBA6 and BID occur together in a ubiquitin and apoptosis-associated complex (hu.MAP huMAP3_14442.1). These observations indicate that parts of the module recapitulate known molecular machinery, while the full co-abundance network joins several established cellular subsystems without demonstrating that all members physically interact.

**STRING interactions (score >= 0.7)**: 3 of 666 gene pairs: CNOT1–YTHDF2 (0.986); IGF2BP3–YTHDF2 (0.845); MCM5–RFC3 (0.937)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (ACAA2, DARS2, GFM1; 3/99); huMAP3_10730.1 (LIG3, HLTF; 2/11); huMAP3_10578.1 (LIG3, HLTF; 2/21); huMAP3_14846.1 (LIG3, HLTF; 2/27); huMAP3_13854.1 (LIG3, HLTF; 2/29); huMAP3_10525.1 (DARS2, GFM1; 2/33); huMAP3_14442.1 (UBA6, BID; 2/57)

### Novelty

The shared co-abundance module may be a new systems-level observation, because the integrated pattern across autonomic nervous system and skin is not established by the supplied annotations. However, it should not be called a newly discovered molecular complex or pathway. Several internal relationships are already known through STRING and hu.MAP, including RNA-decay associations, replication-associated proteins, mitochondrial translation or metabolism complexes, and DNA-repair complexes. The lack of STRING or hu.MAP coverage for many edges does not prove novelty, because database incompleteness and indirect co-abundance can explain unrecorded relationships. A cautious novelty claim is therefore that the tissue-shared co-abundance organization is potentially novel, whereas many component functions and subcomplexes are established.

**Hypothesis.** Hypothesis: the module represents a shared cellular resilience program present in autonomic nervous system and skin cells. Coordinated regulation of RNA fate through CNOT1, YTHDF2, and related RNA-binding factors could adjust translation and transcript turnover during changes in cellular state. In parallel, mitochondrial translation and metabolism through DARS2, GFM1, and ACAA2 could support energy and biosynthetic demands, while LIG3, HLTF, MCM5, and RFC3 could maintain genome integrity. Trafficking, adhesion, cytoskeletal, and extracellular-matrix genes could couple this intracellular maintenance program to cell architecture and tissue interactions. This is a mechanistic model to test, not a conclusion established by global enrichment. It predicts that module activity should track cellular stress, turnover, mitochondrial demand, or repair state and should be evaluated with independent cohorts, cell-type-resolved data, and perturbation experiments.

### Important genes

#### GEMIN8

- **Related proteins** (co-abundance neighbors): LIG3 (0.94), CNOT1 (0.94), EIF4E (0.88), RFC3 (0.88), PDLIM7 (0.88), SNX2 (0.87), NAA50 (0.87), ACAA2 (0.87), MCM5 (0.85), DCAF1 (0.84), UBE3A (0.84), HLTF (0.84), DIAPH1 (0.83), OSBPL9 (0.82), LAMC1 (0.82), GFM1 (0.81), CTNND1 (0.80), UBA6 (0.80), IGF2BP3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gem nuclear organelle associated protein 8. The protein encoded by this gene is part of the SMN complex, which is necessary for spliceosomal snRNP assembly in the cytoplasm and pre-mRNA splicing in the nucleus. The encoded protein binds to both SMN1 and the GEMIN6/GEMIN7 heterodimer, mediating their interaction. This protein is found in nuclear Gemini of Cajal bodies (gems) and in the cytoplasm. Three transcript variants encoding the same p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); glaucoma (0.083); open-angle glaucoma (0.062); proximal spinal muscular atrophy (0.018); Alzheimer disease (0.011)
- **Europe PMC papers**: 165
- **Why important**: GEMIN8 is the principal network hub, connecting RNA-related factors, DNA replication and repair factors, mitochondrial proteins, trafficking proteins, and structural regulators. It is part of the SMN complex and supports spliceosomal snRNP assembly. Its central position makes it the strongest candidate for organizing the observed co-abundance pattern, although it has no direct STRING or hu.MAP support in this module.
- **Conclusion**: Established evidence supports GEMIN8 as a spliceosomal snRNP-assembly component and as the central statistical connector of the module. The hypothesis that it coordinates the broader tissue-shared program is plausible from network position but remains unproven.

#### CNOT1

- **Related proteins** (co-abundance neighbors): GEMIN8 (0.94), ENTR1 (0.91); STRING partners: YTHDF2 (0.986)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CCR4-NOT transcription complex subunit 1. Enables armadillo repeat domain binding activity; molecular adaptor activity; and nuclear receptor binding activity. Contributes to poly(A)-specific ribonuclease activity. Involved in several processes, including negative regulation of signal transduction; positive regulation of cytoplasmic mRNA processing body assembly; and regulation of gene expression. Located in P-body and cytosol. Part of CCR…
- **Diseases (Open Targets)**: holoprosencephaly 12 with or without pancreatic agenesis (0.749); Vissers-Bodmer syndrome (0.697); hereditary disease (0.515); complex neurodevelopmental disorder (0.474); neurodegenerative disease (0.471)
- **Europe PMC papers**: 1262
- **Why important**: CNOT1 is a core CCR4-NOT complex subunit with a major role in mRNA deadenylation, mRNA decay, translation control, and P-body organization. It is directly connected to YTHDF2 by high-confidence STRING evidence and is one of the two immediate network partners of GEMIN8. It also has substantial literature and disease annotation, including developmental disease associations.
- **Conclusion**: Established evidence supports CNOT1 as a central post-transcriptional regulator and confirms its relationship with YTHDF2. Its possible role as an RNA-level coordinator of the complete module is a hypothesis rather than an established tissue-specific mechanism.

#### YTHDF2

- **Related proteins** (co-abundance neighbors): ATXN2L (0.81); STRING partners: CNOT1 (0.986), IGF2BP3 (0.845)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: YTH N6-methyladenosine RNA binding protein F2. This gene encodes a member of the YTH (YT521-B homology) superfamily containing YTH domain. The YTH domain is typical for the eukaryotes and is particularly abundant in plants. The YTH domain is usually located in the middle of the protein sequence and may function in binding to RNA. In addition to a YTH domain, this protein has a proline rich region which may be involved in signal transduction. A…
- **Diseases (Open Targets)**: neurodegenerative disease (0.448); type 2 diabetes mellitus (0.157); neoplasm (0.118); hepatocellular carcinoma (0.117); gastric cancer (0.111)
- **Europe PMC papers**: 7075
- **Why important**: YTHDF2 is an mRNA-binding protein involved in mRNA catabolism and is linked by STRING to both CNOT1 and IGF2BP3. This places it at the intersection of RNA decay and RNA stabilization or translation-associated regulation. It is also a heavily studied gene with disease and developmental annotations, making it a biologically informative marker of the module's RNA-processing component.
- **Conclusion**: Established evidence supports YTHDF2 as an RNA-binding and mRNA-decay factor and supports its known relationships with CNOT1 and IGF2BP3. Its co-abundance with mitochondrial, repair, and structural genes may indicate coordinated cell-state regulation, but causality is not established.

#### LIG3

- **Related proteins** (co-abundance neighbors): GEMIN8 (0.94); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_10730.1, huMAP3_10578.1, huMAP3_14846.1, huMAP3_13854.1
- **Function (MyGene.info)**: DNA ligase 3. This gene is a member of the DNA ligase family. Each member of this family encodes a protein that catalyzes the joining of DNA ends but they each have a distinct role in DNA metabolism. The protein encoded by this gene is involved in excision repair and is located in both the mitochondria and nucleus, with translation initiation from the upstream start codon allowing for transport to the mitochond…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome 20 (mngie type) (0.663); cerebellar ataxia (0.551); Neurogenic bladder (0.551); Leukoencephalopathy (0.551); macular degeneration (0.551)
- **Europe PMC papers**: 1768
- **Why important**: LIG3 is a DNA ligase with nuclear and mitochondrial roles in DNA repair, including base-excision repair and repair-associated DNA synthesis. It is paired with HLTF across several hu.MAP DNA-repair and chromatin-associated complexes (hu.MAP huMAP3_10730.1), (hu.MAP huMAP3_10578.1), (hu.MAP huMAP3_14846.1), (hu.MAP huMAP3_13854.1). Its disease associations include mitochondrial DNA depletion and neurological disorders, relevant to a module shared by neural and skin tissues.
- **Conclusion**: Established evidence supports LIG3 in nuclear and mitochondrial DNA maintenance and supports its recurring complex membership with HLTF. A role for this pair in a shared tissue resilience or repair state is a testable hypothesis, not a demonstrated module function.

#### DARS2

- **Related proteins** (co-abundance neighbors): ENTR1 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 2, mitochondrial. The protein encoded by this gene belongs to the class-II aminoacyl-tRNA synthetase family. It is a mitochondrial enzyme that specifically aminoacylates aspartyl-tRNA. Mutations in this gene are associated with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation (LBSL). [provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: leukoencephalopathy with brain stem and spinal cord involvement-high lactate syndrome (0.843); neurodegenerative disease (0.527); hereditary disease (0.518); hypertensive disorder (0.425); Cerebral cortical atrophy (0.425)
- **Europe PMC papers**: 796
- **Why important**: DARS2 is a mitochondrial aminoacyl-tRNA synthetase required for mitochondrial translation. It occurs with GFM1 and ACAA2 in a hu.MAP mitochondrial complex (hu.MAP huMAP3_13468.1) and with GFM1 in another related complex (hu.MAP huMAP3_10525.1). Its established association with leukoencephalopathy and lactate elevation gives it particular relevance to mitochondrial and nervous-system biology.
- **Conclusion**: Established evidence supports DARS2 in mitochondrial tRNA charging and supports its complex-level relationships with GFM1 and ACAA2. Its participation in a shared mitochondrial stress-adaptation program is plausible, but the co-abundance data do not establish that mechanism.

## Module 13

**Tissue pair**: autonomic_nervous_system and skin  
**Genes (7)**: SLC4A2, CDK1, DDX31, ERBIN, LTN1, RNGTT, MEAK7

### Function

The module contains 7 genes connected by 6 co-abundance edges, but no GO/KEGG term passed global correction: the globally significant GO/KEGG field is empty. Therefore, the function cannot be assigned from statistically significant pathway enrichment. The gene annotations instead suggest a heterogeneous intracellular program involving epithelial membrane organization and ERBB2/Ras-related signaling through ERBIN, anion and bicarbonate transport through SLC4A2, TOR and nutrient or insulin responses through MEAK7, ribosome-associated quality control through LTN1, RNA processing and ribosome biogenesis through RNGTT and DDX31, and cell-cycle progression through CDK1. The most defensible interpretation is a coordinated cellular-state or cell-composition signal rather than a single established biochemical pathway. The supplementary STRING fields are also empty, so there is no supplementary STRING enrichment to strengthen a pathway-level interpretation.

**Cell composition.** All 7 genes have HPA annotations, and 5 show low tissue specificity while 2 are tissue enhanced. No genes are annotated as secreted, arguing against a plasma or secreted-protein module. 6 genes are detected in skin, with 1 having no skin protein-detection result, whereas autonomic-nervous-system protein detection has no usable matching HPA tissue result. The HPA single-cell pattern is diverse, including neutrophils, oligodendrocytes, early spermatids, photoreceptors, esophageal suprabasal cells, trophoblast populations, choroid plexus epithelial cells, parietal cells and retinal pigment epithelial cells. Most genes have low immune-cell specificity, while 1 gene, CDK1, is immune-cell enhanced and is also enhanced in bone marrow and lymphoid tissue. Thus, the module does not look like a conventional blood or secreted-protein signature, although shared proliferative or epithelial-cell states and sample cellular composition could contribute to the cross-tissue co-abundance.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING reports 0 high-confidence physical or functional interactions among 21 possible gene pairs, and hu.MAP reports 0 complexes containing at least two module members. Accordingly, none of the module edges is independently supported here as a known high-confidence STRING relationship, and no multi-member hu.MAP complex explains the module. The co-abundance graph therefore captures coordinated abundance without demonstrating direct physical binding or membership in a known complex. Known molecular relationships are instead supplied by individual gene annotations: ERBIN is an ERBB2-interacting LAP-family protein, LTN1 is an E3 ubiquitin ligase involved in stalled-ribosome rescue, MEAK7 is associated with TOR signaling, RNGTT performs mRNA capping, DDX31 is a DEAD-box helicase associated with ribosome biogenesis, SLC4A2 is an anion exchanger, and CDK1 is the catalytic kinase of the M-phase-promoting-factor complex. These established functions are complementary but do not establish one shared physical machine.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel cross-tissue co-abundance association because the supplied analysis identifies a module shared by autonomic nervous system and skin, while neither STRING nor hu.MAP provides an overlapping interaction or complex. However, absence from those resources does not prove novelty: it may reflect tissue-specific regulation, indirect coordination, cell-type composition, incomplete database coverage, or a signal that is not a physical interaction network. The lack of globally significant GO/KEGG enrichment also means that the module cannot be claimed as a newly discovered pathway. The appropriate conclusion is that the cross-tissue abundance pattern is a candidate finding requiring replication and independent validation, not that a new molecular complex has been established.

**Hypothesis.** Hypothesis: the module reflects a coordinated state of skin-associated or epithelial cells in which ERBIN-linked membrane and junctional signaling is coupled to MEAK7-mediated nutrient or TOR responses, SLC4A2-mediated intracellular ion and bicarbonate handling, and a demand for protein and RNA quality control represented by LTN1, RNGTT and DDX31. CDK1 may mark a proliferative or cell-cycle component of that state rather than directly participating in the same molecular complex. This hypothesis predicts that module abundance will track epithelial or regenerative cell states, proliferative activity, and cellular stress or nutrient signaling across both tissues. It should be tested with cell-resolved data, independent cohorts, perturbation of the proposed regulators, and protein-level measurements.

### Important genes

#### ERBIN

- **Related proteins** (co-abundance neighbors): LTN1 (0.85), DDX31 (0.83), MEAK7 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: erbb2 interacting protein. This gene is a member of the leucine-rich repeat and PDZ domain (LAP) family. The encoded protein contains 17 leucine-rich repeats and one PDZ domain. It binds to the unphosphorylated form of the ERBB2 protein and regulates ERBB2 function and localization. It has also been shown to affect the Ras signaling pathway by disrupting Ras-Raf interaction. Alternatively spliced transcript variants encodin…
- **Diseases (Open Targets)**: cancer (0.599); alcohol drinking (0.307); tuberculosis (0.257); adolescent idiopathic scoliosis (0.233); ovarian neoplasm (0.212)
- **Europe PMC papers**: 944
- **Why important**: ERBIN is the topological hub, with the greatest weighted degree in this module and connections to LTN1, DDX31 and MEAK7. Its established ERBB2-binding, Ras-related signaling, plasma-membrane and cell-junction localization, regulation of keratinocyte differentiation, and skin detection make it the strongest candidate for linking epithelial organization to the rest of the module. It also has substantial literature support, with 944 Europe PMC papers.
- **Conclusion**: Established: ERBIN is a membrane and junction-associated ERBB2-interacting protein with reported effects on Ras signaling and keratinocyte differentiation. Conclusion: it is the most plausible organizational anchor of the co-abundance pattern. Hypothesis: ERBIN may couple epithelial state to the intracellular stress, nutrient and RNA-quality-control signals represented by neighboring genes, but the co-abundance data do not prove that mechanism.

#### CDK1

- **Related proteins** (co-abundance neighbors): SLC4A2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cyclin dependent kinase 1. The protein encoded by this gene is a member of the Ser/Thr protein kinase family. This protein is a catalytic subunit of the highly conserved protein kinase complex known as M-phase promoting factor (MPF), which is essential for G2/M phase transitions of eukaryotic cell cycle. Mitotic cyclins stably associate with this protein and function as regulatory subunits. The kinase activity of this prote…
- **Diseases (Open Targets)**: neurodegenerative disease (0.535); Alzheimer disease (0.526); Parkinson disease (0.523); lysosomal storage disease (0.512); prostatitis (0.404)
- **Europe PMC papers**: 33995
- **Why important**: CDK1 is the canonical catalytic kinase of the M-phase-promoting-factor complex and has annotations spanning G2/M transition, DNA replication, DNA repair and chromatin remodeling. It is the module gene with tissue enhancement in bone marrow and lymphoid tissue and immune-cell enhancement in NK cells and T-reg cells, while also appearing in several progenitor and amplifying cell populations. Its very large literature base, with 33995 Europe PMC papers, makes its biology especially well established.
- **Conclusion**: Established: CDK1 marks cell-cycle control and is enriched in several proliferative or progenitor contexts in the HPA evidence. Conclusion: CDK1 may be a marker of proliferative cell composition within the shared module rather than a specific autonomic-skin mechanism. Hypothesis: coordinated CDK1 abundance could indicate regenerative or proliferative states that co-vary with ERBIN, SLC4A2 and MEAK7.

#### SLC4A2

- **Related proteins** (co-abundance neighbors): LTN1 (0.85), CDK1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Nuclear speckles, Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 4 member 2. This gene encodes a member of the anion exchanger family of membrane transport proteins. The encoded protein regulates intracellular pH, biliary bicarbonate secretion, and chloride uptake. Reduced expression of this gene may be associated with primary biliary cirrhosis (PBC) in human patients, while differential expression of this gene may be associated with malignant hepatocellular carcinoma, col…
- **Diseases (Open Targets)**: osteopetrosis, autosomal recessive 9 (0.429); Abnormality of the skeletal system (0.312); distal renal tubular acidosis (0.259); primary biliary cholangitis (0.095); cancer (0.077)
- **Europe PMC papers**: 757
- **Why important**: SLC4A2 is an intermediate node connecting LTN1 and CDK1. It is tissue enhanced in choroid plexus and group enriched across choroid plexus epithelial, parietal, retinal pigment epithelial and syncytiotrophoblast populations. Its established anion-exchange, chloride-uptake and bicarbonate-transport functions provide a plausible physiological bridge between membrane state, intracellular pH and cellular metabolism. It has 757 Europe PMC papers and reported disease associations involving osteopetrosis, skeletal abnormalities, distal renal tubular acidosis and primary biliary cholangitis.
- **Conclusion**: Established: SLC4A2 is a membrane anion transporter with roles in intracellular pH and bicarbonate handling. Conclusion: it is an important functional candidate because ion transport could coordinate otherwise diverse cellular programs, but its tissue and cell-type pattern is broad and not specific to autonomic nervous system or skin. Hypothesis: SLC4A2 may report or help stabilize an epithelial transport and metabolic state linked to the module.

#### MEAK7

- **Related proteins** (co-abundance neighbors): RNGTT (0.82), ERBIN (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MTOR associated protein MEAK7. Involved in several processes, including TOR signaling; positive regulation of protein localization to lysosome; and response to insulin. Located in cytosol; lysosomal membrane; and nuclear lumen. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: alcohol drinking (0.338); stroke disorder (0.302); psoriatic arthritis (0.204); lung carcinoma (0.089); lung cancer (0.089)
- **Europe PMC papers**: 75
- **Why important**: MEAK7 connects ERBIN to RNGTT and is annotated in TOR signaling, lysosomal localization, nutrient and insulin responses, oxidative-stress response, cell migration and population proliferation. Its cell-type-enhanced pattern includes cone and rod photoreceptors, esophageal suprabasal cells and syncytiotrophoblasts, consistent with a context-dependent cellular-state role rather than a blood-specific signal. It has a smaller literature base, with 75 Europe PMC papers, making it a comparatively under-characterized candidate.
- **Conclusion**: Established: MEAK7 is associated with TOR signaling, nutrient or insulin response and lysosomal localization. Conclusion: it is an informative candidate for interpreting the module as a nutrient, stress or growth-state program, but direct participation in this module is not established. Hypothesis: MEAK7 may mediate the connection between ERBIN-associated epithelial signaling and the proliferative or metabolic state marked by CDK1.

#### LTN1

- **Related proteins** (co-abundance neighbors): ERBIN (0.85), SLC4A2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: listerin E3 ubiquitin protein ligase 1. Like most RING finger proteins, LTN1 functions as an E3 ubiquitin ligase (Chu et al., 2009 [PubMed 19196968]).[supplied by OMIM, Nov 2010].
- **Diseases (Open Targets)**: ovarian neoplasm (0.238); Alzheimer disease (0.232); sweat gland disorder (0.221); keloid (0.189); gestational diabetes (0.160)
- **Europe PMC papers**: 625
- **Why important**: LTN1 is connected to both ERBIN and SLC4A2 and encodes the listerin E3 ubiquitin ligase. Its established role in rescue of stalled cytosolic ribosomes and ribosome-associated ubiquitin-dependent protein catabolism gives the module a protein-quality-control component. It has 625 Europe PMC papers and reported associations including sweat-gland disorder and keloid.
- **Conclusion**: Established: LTN1 participates in E3 ubiquitination and quality control of stalled translation. Conclusion: it is a strong candidate for explaining why a membrane or epithelial state might co-vary with RNA and protein homeostasis genes, although no direct interaction with the other module members is supported by STRING or hu.MAP here. Hypothesis: LTN1 may buffer translational stress arising during epithelial growth, differentiation or altered nutrient signaling.

## Module 14

**Tissue pair**: autonomic_nervous_system and skin  
**Genes (5)**: DDX55, ERI1, KRI1, NAA20, PPHLN1

### Function

No GO or KEGG term passed global multiple-testing correction, and STRING supplied no supplementary enrichment; therefore this module does not support a statistically established shared pathway. The gene annotations instead suggest a mixed functional signal: PPHLN1 is associated with terminal keratinocyte differentiation and epidermal barrier integrity, while DDX55, KRI1, and ERI1 are associated with ribosome biogenesis or RNA processing, and NAA20 with cotranslational N-terminal protein acetylation. The co-abundance pattern is therefore more consistent with coordinated expression of epithelial-structure and general intracellular biosynthetic functions than with a defined pathway or protein complex. These functional interpretations are established gene-level annotations, not enrichment claims.

**Cell composition.** The module is not dominated by plasma or secreted proteins: every member is annotated as non-secreted, and all have low immune-cell specificity in HPA. All members also have low tissue specificity, arguing against a strongly tissue-restricted program. Most proteins are detected in skin, whereas autonomic-nervous-system protein detection was unavailable because there was no matching HPA tissue. Several genes show cell-type-enhanced expression in specialized populations, including spermatid, neural, glial, epithelial, renal, Hofbauer-cell, or neutrophil populations, but the module has no recurrent enriched blood-cell category. Overall, the evidence does not indicate a plasma-protein or blood-cell contamination signature, although shared broadly expressed cellular programs and sample cell composition could contribute to the co-abundance pattern.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair in the module met the reported STRING interaction threshold, and no hu.MAP complex contained multiple module members. Thus, the observed co-abundance edges are not supported here by high-confidence known physical or functional interactions in either resource. PPHLN1 is the central network connector, linking KRI1, ERI1, and DDX55, while DDX55 links to NAA20; this topology may reflect coordinated abundance or shared regulation rather than a physically assembled complex. The absence of STRING and hu.MAP support limits claims of direct molecular interaction but does not invalidate the co-abundance module.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel cross-tissue co-abundance association, because the module is not represented as a high-confidence STRING interaction network or a hu.MAP complex and combines genes with distinct annotated roles. However, absence from those resources alone cannot establish novelty: the pattern could reflect broadly expressed genes, epithelial representation in skin, technical or compositional effects, or an under-characterized regulatory relationship. The strongest defensible conclusion is that the specific shared co-abundance pattern is not explained by currently documented high-confidence interactions in the supplied resources, while its biological novelty remains unproven.

**Hypothesis.** Hypothesis: the shared module reflects coordinated expression of a broadly expressed intracellular RNA and protein-maturation program that is coupled to epithelial differentiation in skin. PPHLN1 may provide the epithelial-barrier context, while ERI1, KRI1, and DDX55 represent RNA-processing or ribosome-biogenesis activity and NAA20 represents cotranslational protein modification. A common differentiation or proteostasis state could produce co-abundance across autonomic-nervous-system and skin samples without requiring direct physical interaction among the proteins. This hypothesis should be tested with independent cohorts, cell-type-aware analyses, and perturbation or localization experiments.

### Important genes

#### PPHLN1

- **Related proteins** (co-abundance neighbors): KRI1 (0.83), ERI1 (0.82), DDX55 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: periphilin 1. The protein encoded by this gene is one of the several proteins that become sequentially incorporated into the cornified cell envelope during the terminal differentiation of keratinocyte at the outer layers of epidermis. This protein interacts with periplakin, which is known as a precursor of the cornified cell envelope. The cellular localization pattern and insolubility of this protein suggest th…
- **Diseases (Open Targets)**: alcohol drinking (0.252); actinic keratosis (0.247); stroke disorder (0.224); hypothyroidism (0.224); systemic lupus erythematosus (0.211)
- **Europe PMC papers**: 360
- **Why important**: PPHLN1 has the strongest network centrality in the module and connects to KRI1, ERI1, and DDX55. Its established role in terminal keratinocyte differentiation, interaction with periplakin, and contribution to epidermal integrity makes it the clearest tissue-relevant anchor. It is detected in skin, has broad tissue and immune-cell profiles, and has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports PPHLN1 as an epithelial differentiation and barrier-associated protein and as the principal network connector. It is a plausible organizer of the module's skin-related context, but the supplied data do not establish that it directly regulates the other module genes.

#### ERI1

- **Related proteins** (co-abundance neighbors): PPHLN1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exoribonuclease 1. Enables 3'-5' exonuclease activity. Predicted to be involved in exonucleolytic trimming to generate mature 3'-end of 5.8S rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Located in cytoplasm and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: spondyloepimetaphyseal dysplasia, Guo-Campeau type (0.660); Hoxha-Aliu syndrome (0.586); neurodegenerative disease (0.478); hypertensive disorder (0.476); Abnormality of the skeletal system (0.453)
- **Europe PMC papers**: 561
- **Why important**: ERI1 contributes a direct module connection to PPHLN1 and has the strongest literature representation among the module genes in the fact sheet. Its established exonuclease activity and roles in five-point-eight-S rRNA maturation and rRNA processing provide a biologically coherent intracellular function, while its HPA cell-type-enhanced pattern spans several specialized cell populations.
- **Conclusion**: Established evidence supports ERI1 as an RNA-processing factor with broad cellular relevance. Its co-abundance with PPHLN1 may indicate a shared differentiation or biosynthetic state, but a direct epithelial-barrier role is only a hypothesis.

#### DDX55

- **Related proteins** (co-abundance neighbors): NAA20 (0.81), PPHLN1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 55. This gene encodes a member of protein family containing a characteristic Asp-Glu-Ala-Asp (DEAD) motif. These proteins are putative RNA helicases, and may be involved in a range of nuclear processes including translational initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Multiple alternatively spliced transcript variants have been found for this gene. Pseudogen…
- **Diseases (Open Targets)**: hypothyroidism (0.296); neurodegenerative disease (0.247); coronary artery disorder (0.096); type 2 diabetes mellitus (0.093); hepatocellular carcinoma (0.077)
- **Europe PMC papers**: 206
- **Why important**: DDX55 occupies an intermediate network position, connecting PPHLN1 with NAA20, and is annotated as a DEAD-box helicase involved in nuclear RNA-related processes and large-subunit rRNA maturation. Its nucleolar localization and skin detection make it a useful link between the epithelial context and the proposed RNA-processing component.
- **Conclusion**: Established evidence supports DDX55 as an RNA-processing or ribosome-assembly factor. Its network placement supports a possible bridge between RNA metabolism and the other module functions, but the module does not demonstrate a physical interaction or a specific role in skin or autonomic tissue.

#### NAA20

- **Related proteins** (co-abundance neighbors): DDX55 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-alpha-acetyltransferase 20, NatB catalytic subunit. NAT5 is a component of N-acetyltransferase complex B (NatB). Human NatB performs cotranslational N(alpha)-terminal acetylation of methionine residues when they are followed by asparagine (Starheim et al., 2008 [PubMed 18570629]).[supplied by OMIM, Apr 2009].
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal recessive 73 (0.520); neurodegenerative disease (0.380); autosomal recessive non-syndromic intellectual disability (0.370); liver disorder (0.190); syndromic intellectual disability (0.185)
- **Europe PMC papers**: 236
- **Why important**: NAA20 is the module's connection to cotranslational protein modification and is linked to DDX55 in the co-abundance graph. Its established function as the catalytic subunit of NatB gives the module a plausible protein-maturation component, and its cell-type-enhanced expression includes several epithelial populations.
- **Conclusion**: Established evidence supports NAA20 as a NatB-dependent N-terminal acetylation factor. Its association with DDX55 is compatible with coordinated biosynthetic activity, but any role in the proposed cross-tissue module mechanism remains hypothetical.

#### KRI1

- **Related proteins** (co-abundance neighbors): PPHLN1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: KRI1 homolog. This gene overlaps with the gene for cysteine endopeptidase AUT-like 4 in a head-to-tail orientation. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: metabolic disease (0.293); neurodegenerative disease (0.220); osteoarthritis (0.044); Knee pain (0.028); arthropathy (0.027)
- **Europe PMC papers**: 172
- **Why important**: KRI1 is directly connected to the central PPHLN1 node and is annotated with a specific role in endonucleolytic cleavage during precursor rRNA processing. Its inclusion provides an independent RNA-biogenesis link within a module otherwise anchored by an epithelial differentiation protein.
- **Conclusion**: Established evidence supports KRI1 as an rRNA-processing factor. Its co-abundance with PPHLN1 may mark a shared cellular state rather than a direct molecular partnership, because neither STRING nor hu.MAP supports a known interaction here.

## Module 15

**Tissue pair**: autonomic_nervous_system and skin  
**Genes (5)**: DNMT3A, EIF3L, MAK16, MCFD2, MYH10

### Function

This module does not support a single established molecular function. No GO or KEGG term passed global correction, and STRING supplied no functional enrichment. The co-abundance structure is a small star-like subgraph centered on DNMT3A, with MCFD2, MAK16, EIF3L, and MYH10 each linked to DNMT3A but not to one another. The genes represent heterogeneous processes: de novo DNA methylation and transcriptional regulation for DNMT3A, ER-to-Golgi cargo transport for MCFD2, ribosomal RNA maturation for MAK16, translation initiation for EIF3L, and actomyosin organization, cell shape, motility, cytokinesis, and regulated exocytosis for MYH10. Thus, the most defensible interpretation is a coordinated abundance state involving nuclear regulation, protein and RNA biosynthetic machinery, intracellular trafficking, and cytoskeletal function rather than a defined pathway or physical complex.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only one secreted gene, while MCFD2 is described as a soluble luminal ER cargo receptor component. It is also not blood-cell enriched. Most genes have low immune-cell specificity, and MYH10 is not detected in immune cells. Four genes have low tissue specificity, whereas MYH10 is tissue enriched in blood vessel. The cell-type-enhanced annotations are dispersed across gonadotrophs, myonuclei, rod photoreceptors, cardiomyocytes, esophageal apical cells, Müller glia, salivary acinar cells, and several mesenchymal or endocrine populations, with no common cell type. All module proteins are detected in skin, but there is no matching HPA tissue result for autonomic nervous system. Overall, the module could reflect broadly shared cellular abundance or sample-composition effects, but the available HPA evidence does not support a simple blood contamination explanation or a single shared cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and no STRING functional enrichment was reported. No hu.MAP complex contains at least two module members. Therefore, the observed co-abundance links are not corroborated here as established protein-protein interactions or membership in a known multiprotein complex. The absence of STRING and hu.MAP support does not disprove biological coordination; it indicates that this dataset provides co-abundance evidence without independent physical-network confirmation.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The conserved co-abundance pattern may be a new observation in this tissue-pair analysis because it is not represented by a known STRING interaction network or hu.MAP complex. However, that absence alone cannot establish novelty. The genes themselves have well-described individual functions, and the module may arise from shared expression, cell-state variation, technical effects, or indirect regulation rather than a newly discovered molecular mechanism. A strong novelty claim would require replication in independent autonomic nervous system and skin datasets, control for cell composition and sample quality, and validation of the abundance relationships at the protein level. The appropriate conclusion is therefore that the module is a potentially novel cross-tissue co-abundance association, not yet a validated new biological pathway.

**Hypothesis.** Hypothesis: a shared cellular state involving DNMT3A-linked regulatory activity may co-vary with the production, trafficking, translation, and cytoskeletal handling of proteins in skin and autonomic nervous system samples. In this model, DNMT3A is a network-centered marker of the state, while MCFD2 reflects secretory-pathway capacity, EIF3L and MAK16 reflect biosynthetic capacity, and MYH10 reflects actomyosin-dependent architecture or trafficking. This is a mechanistic hypothesis rather than an established pathway. The lack of global GO or KEGG enrichment, STRING support, and hu.MAP support means that direct causal links among these proteins remain un demonstrated by the supplied evidence.

### Important genes

#### DNMT3A

- **Related proteins** (co-abundance neighbors): MCFD2 (0.84), MAK16 (0.82), EIF3L (0.81), MYH10 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA methyltransferase 3 alpha. CpG methylation is an epigenetic modification that is important for embryonic development, imprinting, and X-chromosome inactivation. Studies in mice have demonstrated that DNA methylation is required for mammalian development. This gene encodes a DNA methyltransferase that is thought to function in de novo methylation, rather than maintenance methylation. The protein localizes to the cytoplasm an…
- **Diseases (Open Targets)**: acute myeloid leukemia (0.858); Tatton-Brown-Rahman overgrowth syndrome (0.844); Heyn-Sproul-Jackson syndrome (0.763); myelodysplastic syndrome (0.741); myeloid leukemia (0.682)
- **Europe PMC papers**: 31456
- **Why important**: DNMT3A is the network hub, connected to every other module member with relatively strong co-abundance links. Its established function is de novo DNA methylation, with roles in developmental regulation, imprinting, heterochromatin, transcriptional regulation, and responses to cellular stressors. It has extensive literature and strong disease associations including acute myeloid leukemia, myelodysplastic disease, and Tatton-Brown-Rahman overgrowth syndrome. Its central network position makes it the principal candidate for a module-level regulatory marker, although its hub status does not demonstrate that it causes the other genes' abundance.
- **Conclusion**: Established: DNMT3A is the network-centered gene with a well-supported epigenetic function and substantial disease literature. Hypothesis: DNMT3A may mark or contribute to a shared regulatory cell state underlying the cross-tissue co-abundance pattern. The data do not establish direct regulation of the other module genes.

#### MYH10

- **Related proteins** (co-abundance neighbors): DNMT3A (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Actin filaments; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin heavy chain 10. This gene encodes a member of the myosin superfamily. The protein represents a conventional non-muscle myosin; it should not be confused with the unconventional myosin-10 (MYO10). Myosins are actin-dependent motor proteins with diverse functions including regulation of cytokinesis, cell motility, and cell polarity. Mutations in this gene have been associated with May-Hegglin anomaly and developmen…
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.484); hereditary disease (0.453); congenital ptosis (0.425); Hypertelorism (0.425); Wide nose (0.425)
- **Europe PMC papers**: 3179
- **Why important**: MYH10 is the module's most tissue-specific gene in the HPA summary, enriched in blood vessel and localized to actin filaments. Its established function as non-muscle myosin supports roles in cell shape, actin-dependent movement, cytokinesis, polarity, and regulated exocytosis. It has substantial literature and disease associations involving developmental defects, May-Hegglin anomaly, and neurodevelopmental or congenital phenotypes. Its connection to the DNMT3A-centered network provides a plausible bridge between regulatory state and tissue architecture, even though no physical interaction is reported.
- **Conclusion**: Established: MYH10 is an actomyosin motor associated with vascular and structural cellular programs and is not immune-cell enriched in the supplied HPA evidence. Hypothesis: MYH10 may capture vascular, contractile, polarity, or trafficking variation contributing to the shared module. A direct DNMT3A-MYH10 mechanism is not demonstrated.

#### MCFD2

- **Related proteins** (co-abundance neighbors): DNMT3A (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: multiple coagulation factor deficiency 2, ER cargo receptor complex subunit. This gene encodes a soluble luminal protein with two calmodulin-like EF-hand motifs at its C-terminus. This protein forms a complex with LMAN1 (lectin mannose binding protein 1; also known as ERGIC-53) that facilitates the transport of coagulation factors V (FV) and VIII (FVIII) from the endoplasmic reticulum to the Golgi apparatus via an endoplasmic reticulum Golgi intermediate compartment (ERGIC…
- **Diseases (Open Targets)**: combined deficiency of factor V and factor VIII (0.712); neurodegenerative disease (0.529); multiple intestinal atresia (0.415); factor V and factor VIII, combined deficiency of, type 1 (0.333); autoimmune disorder of central nervous system (0.331)
- **Europe PMC papers**: 433
- **Why important**: MCFD2 provides the module with a distinct secretory-pathway interpretation. It is an ER cargo receptor component that forms a complex with LMAN1 to transport coagulation factors from the ER toward the Golgi, and pathogenic variants cause combined factor V and factor VIII deficiency. It has less extensive literature than DNMT3A or MYH10 but a clear molecular function and a specific inherited disease association. Its peripheral position, with a single link to DNMT3A, makes it useful for testing whether the module reflects a broad cellular state rather than a tightly interconnected pathway.
- **Conclusion**: Established: MCFD2 participates in ER-to-Golgi cargo transport and is linked to combined coagulation-factor deficiency. Hypothesis: its co-abundance with DNMT3A may reflect shared secretory or cellular-state variation in the sampled tissues. The module does not establish a new MCFD2 interaction or a coagulation-specific process.

#### EIF3L

- **Related proteins** (co-abundance neighbors): DNMT3A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit L. Enables RNA binding activity. Contributes to translation initiation factor activity. Involved in translational initiation and viral translational termination-reinitiation. Located in membrane. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.503); Hydrocephalus (0.064); open-angle glaucoma (0.042); severe acute respiratory syndrome (0.032); COVID-19 (0.032)
- **Europe PMC papers**: 558
- **Why important**: EIF3L represents the translation machinery within the module. It contributes to eukaryotic translation initiation and is part of the eukaryotic initiation factor complex, with additional annotated roles in viral translational termination-reinitiation. It has a moderate literature base and reported associations with neurodegenerative disease and other neurological or infectious conditions. Its low tissue specificity and low cell-type specificity make it a plausible broadly expressed state marker rather than a tissue-restricted driver.
- **Conclusion**: Established: EIF3L is a translation-initiation component with broad expression characteristics in the supplied HPA evidence. Hypothesis: its co-abundance may indicate altered protein synthesis capacity accompanying the module state. The data do not show that EIF3L is specifically involved in autonomic nervous system or skin biology here.

