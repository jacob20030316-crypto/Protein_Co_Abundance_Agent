# Conserved co-abundance modules: autonomic_nervous_system and placenta

## Module 0

**Tissue pair**: autonomic_nervous_system and placenta  
**Genes (8)**: DBI, BASP1, CALD1, CAPN2, CORO1C, ITGB1, PDLIM7, WDR1

### Function

The most defensible interpretation is a cytoskeleton, adhesion, and contractility-associated module, with links to actin-filament remodeling, cell attachment, membrane organization, and calcium-regulated contraction. WDR1 connects CAPN2, DBI, and CORO1C in the co-abundance graph, while CAPN2 connects to CALD1 and PDLIM7, and CORO1C connects to ITGB1. These connections collectively point toward coordinated regulation of actin dynamics and cell–matrix or cell–cell interactions. The individual annotations support this interpretation: WDR1 is associated with actin-filament depolymerization and cortical cytoskeleton organization; CORO1C with actin organization and neural crest migration; PDLIM7 with actin-cytoskeleton organization and muscle structure; ITGB1 with adhesion; CAPN2 with calcium-activated proteolysis and mechanical responses; and CALD1 with actin bundles and contraction. No GO or KEGG term passed global correction, so the proposed function is an evidence-integrated biological interpretation rather than a globally significant enrichment result.

**Cell composition.** The module is not composed of secreted or plasma proteins: the secreted-gene annotation is absent. Most genes have low tissue specificity, and the HPA single-cell annotations frequently involve platelets, neutrophils, megakaryocytes, or other specialized structural cells. PDLIM7 and CALD1 show associations with neutrophils and stromal or contractile cell types, while several genes are enhanced in platelets or megakaryocytes. Placental protein detection is present for most module members, whereas autonomic-nervous-system tissue protein data are unavailable in the supplied HPA summary. Therefore, the shared module may reflect a conserved cytoskeletal or adhesion program, but it could also partly reflect shared blood-derived, vascular, stromal, platelet, or other cell populations in the sampled tissues. The evidence does not support interpreting it as a placenta-specific secreted program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes, and STRING functional enrichment is absent. Thus, the co-abundance edges are not simply confirmed by the supplied STRING evidence. hu.MAP provides limited prior complex context: WDR1 and CORO1C co-occur in (hu.MAP huMAP3_11076.1), a complex centered on actin-related proteins, and WDR1 and BASP1 co-occur in (hu.MAP huMAP3_09165.1), a broad membrane, cytoskeletal, and signaling complex. These complexes support the plausibility of cytoskeletal or membrane organization, but only a minority of members from either complex belong to this module. The resources therefore provide partial contextual support rather than evidence for a single established multiprotein complex containing the whole module.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11076.1 (WDR1, CORO1C; 2/10); huMAP3_09165.1 (WDR1, BASP1; 2/39)

### Novelty

This module should not be called a wholly new biological pathway. Its inferred themes—actin remodeling, adhesion, contraction, platelet or immune-cell structure, and membrane organization—are established functions of several constituent genes. The potentially novel aspect is the reproducible co-abundance pattern shared by autonomic nervous system and placenta, particularly the linkage of WDR1 with CAPN2, DBI, and CORO1C and the connected CAPN2–CALD1–PDLIM7 and CORO1C–ITGB1 branches. The absence of STRING interactions and the limited overlap with hu.MAP mean that this exact cross-tissue co-abundance configuration may be underrepresented in those resources, but database absence alone cannot establish novelty. The lack of globally significant GO or KEGG enrichment also argues for a cautious, module-level interpretation rather than a claim of discovery of a new pathway.

**Hypothesis.** Hypothesis: the module represents a shared cell-structural state in autonomic nervous system and placenta in which actin turnover, integrin-mediated adhesion, calcium-sensitive proteolysis, and contractile or membrane-associated scaffolding are coordinated. WDR1 and CORO1C may organize actin remodeling, ITGB1 may couple the cytoskeleton to extracellular adhesion, PDLIM7 and CALD1 may stabilize or regulate actin-associated contractile structures, and CAPN2 may provide activity-dependent proteolytic remodeling. DBI and BASP1 could connect this structural state to lipid handling or membrane signaling. A nonexclusive alternative is that the module is driven partly by shared platelet, neutrophil, vascular, or stromal-cell composition rather than by a coordinated program within one cell type. This hypothesis requires cell-resolved expression, perturbation, and protein-interaction testing.

### Important genes

#### WDR1

- **Related proteins** (co-abundance neighbors): CAPN2 (0.88), DBI (0.87), CORO1C (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_11076.1, huMAP3_09165.1
- **Function (MyGene.info)**: WD repeat domain 1. This gene encodes a protein containing 9 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, mostly including a trp-asp at the C-terminal end. WD domains are involved in protein-protein interactions. The encoded protein may help induce the disassembly of actin filaments. Two transcript variants encoding different isoforms have been found for…
- **Diseases (Open Targets)**: periodic fever, immunodeficiency, and thrombocytopenia syndrome (0.705); gout (0.528); neurodegenerative disease (0.526); atrial fibrillation (0.519); intellectual developmental disorder 61 (0.416)
- **Europe PMC papers**: 1861
- **Why important**: WDR1 is the most connected node in the module and links the CAPN2, DBI, and CORO1C branches. Its established annotations include actin-filament depolymerization, cortical cytoskeleton organization, neutrophil-mediated immunity, and platelet formation. It is also present in both hu.MAP contexts, (hu.MAP huMAP3_11076.1) and (hu.MAP huMAP3_09165.1), giving it the strongest bridge between the module graph and prior complex evidence. Its substantial literature and disease associations involving immunodeficiency, thrombocytopenia, inflammation-related phenotypes, and neurodegenerative disease make it a particularly informative anchor.
- **Conclusion**: Established evidence supports WDR1 as a central actin-remodeling and cell-structure component with immune and platelet relevance. It is plausible, but not established, that WDR1 is the organizing node that couples the other module branches in both tissues.

#### CAPN2

- **Related proteins** (co-abundance neighbors): WDR1 (0.88), CALD1 (0.81), PDLIM7 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Connecting piece, Mid piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calpain 2. The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpa…
- **Diseases (Open Targets)**: Alzheimer disease (0.389); urolithiasis (0.288); alcohol drinking (0.288); aortic stenosis (0.141); neoplasm (0.105)
- **Europe PMC papers**: 1796
- **Why important**: CAPN2 is a highly connected module node linking WDR1 to CALD1 and PDLIM7. It encodes a calcium-activated intracellular protease and has annotations involving proteolysis, hypoxia responses, mechanical stimuli, and pregnancy. Its position provides a mechanistic route by which calcium or mechanical state could remodel cytoskeletal and adhesion structures. It also has substantial literature and disease associations spanning neurodegenerative, cardiovascular, renal, and neoplastic contexts.
- **Conclusion**: Established evidence supports CAPN2 as a calcium-sensitive remodeling protease relevant to mechanical and pregnancy-associated biology. Its role as an active regulator of this shared module is a hypothesis because the co-abundance data do not demonstrate protease activity or directionality.

#### PDLIM7

- **Related proteins** (co-abundance neighbors): BASP1 (0.82), CAPN2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Actin filaments, Focal adhesion sites; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 7. The protein encoded by this gene is representative of a family of proteins composed of conserved PDZ and LIM domains. LIM domains are proposed to function in protein-protein recognition in a variety of contexts including gene transcription and development and in cytoskeletal interaction. The LIM domains of this protein bind to protein kinases, whereas the PDZ domain binds to actin filaments. The g…
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); nasopharyngeal carcinoma (0.121); neoplasm (0.120); lymphoma (0.115); Hodgkins lymphoma (0.105)
- **Europe PMC papers**: 808
- **Why important**: PDLIM7 connects CAPN2 with BASP1 and has a structural localization at actin filaments and focal adhesions. Its PDZ and LIM domains support protein recognition and cytoskeletal organization, while its annotations include actin-cytoskeleton organization and muscle structure development. HPA evidence links it to vascular, intestinal, skeletal-muscle, stromal, megakaryocyte, and neutrophil contexts, making it relevant to both structural biology and the possible cell-composition explanation. Its disease associations and literature provide additional biological context.
- **Conclusion**: Established evidence supports PDLIM7 as a cytoskeletal and focal-adhesion scaffold with broad vascular, stromal, and immune-cell relevance. It may coordinate the structural branch of the module, but that coordinating function is not directly demonstrated here.

#### CORO1C

- **Related proteins** (co-abundance neighbors): WDR1 (0.83), ITGB1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_11076.1
- **Function (MyGene.info)**: coronin 1C. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.453); Parkinson disease (0.322); Alzheimer disease (0.312); lysosomal storage disease (0.310); liver disorder (0.261)
- **Europe PMC papers**: 774
- **Why important**: CORO1C is connected to WDR1 and ITGB1, thereby linking actin remodeling to integrin-associated adhesion. Its annotations include actin-filament organization, phagocytosis, signal transduction, and neural crest cell migration. It is also a member with WDR1 of hu.MAP complex (hu.MAP huMAP3_11076.1). HPA identifies platelet enhancement, while disease associations include neurodegenerative and lysosomal-storage-related conditions, giving it relevance to both cytoskeletal trafficking and tissue-specific cell states.
- **Conclusion**: Established evidence supports CORO1C as an actin-regulatory and membrane-trafficking component that can plausibly connect WDR1 to ITGB1. Its specific contribution to the cross-tissue module remains inferential because STRING does not confirm the module relationships.

#### ITGB1

- **Related proteins** (co-abundance neighbors): CORO1C (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is the module's direct connection from CORO1C to integrin-mediated adhesion. Integrin beta one is a membrane receptor subunit involved in cell adhesion, angiogenesis, phagocytosis, embryogenesis, tissue repair, hemostasis, and immune responses. Its focal-adhesion localization and placental detection are especially relevant to a placenta-associated module, while its platelet and epithelial cell-type annotations support possible contributions from vascular or blood-related populations. Its extensive literature and disease associations make it a strong functional marker even though it has limited network connectivity here.
- **Conclusion**: Established evidence supports ITGB1 as an adhesion and cell–matrix interface component. Its presence is consistent with a structural module, but it does not establish whether the shared signal arises from trophoblast, vascular, platelet, epithelial, or another cell population.

#### CALD1

- **Related proteins** (co-abundance neighbors): CAPN2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Actin filaments; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caldesmon 1. This gene encodes a calmodulin- and actin-binding protein that plays an essential role in the regulation of smooth muscle and nonmuscle contraction. The conserved domain of this protein possesses the binding activities to Ca(2+)-calmodulin, actin, tropomyosin, myosin, and phospholipids. This protein is a potent inhibitor of the actin-tropomyosin activated myosin MgATPase, and serves as a mediating…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.499); diaphragmatic hernia (0.447); glaucoma (0.405); diverticular disease (0.393); open-angle glaucoma (0.390)
- **Europe PMC papers**: 3386
- **Why important**: CALD1 is connected to CAPN2 and provides the clearest contractile interpretation of that branch. It binds actin, calmodulin, tropomyosin, myosin, and phospholipids, and regulates calcium-dependent smooth-muscle and nonmuscle contraction. Its annotations include actin-bundle assembly and muscle contraction. HPA links it to decidual stromal cells, extravillous trophoblasts, myoepithelial cells, hepatic stellate cells, and neutrophils, while placental protein detection supports tissue relevance. Its substantial literature and associations with structural and ocular disorders add clinical context.
- **Conclusion**: Established evidence supports CALD1 as an actin-associated contractility regulator with plausible relevance to placental stromal or trophoblast structure. Its proposed coupling to CAPN2-dependent remodeling is a hypothesis rather than a demonstrated mechanism in this module.

## Module 1

**Tissue pair**: autonomic_nervous_system and placenta  
**Genes (11)**: AHNAK, CNDP2, EEA1, FLNB, IMPDH2, IQGAP1, PDLIM1, PLEC, SEC23A, NARS1, TPM1

### Function

The most coherent interpretation is a broadly expressed intracellular structural and trafficking module, with links to cytoskeletal organization, cell shape, membrane repair, endocytosis, vesicle transport, and protein production. This interpretation is based on the functions of EEA1, SEC23A, IQGAP1, PLEC, AHNAK, FLNB, TPM1, PDLIM1, NARS1, IMPDH2, and CNDP2, together with the observed network connections. The network contains an endosomal and secretory-trafficking neighborhood involving EEA1, SEC23A, IQGAP1, and PLEC; a cytoskeletal scaffold neighborhood involving AHNAK, PLEC, FLNB, TPM1, and PDLIM1; and a smaller translation, nucleotide, and peptide-metabolism neighborhood involving NARS1, IMPDH2, and CNDP2. No GO or KEGG term passed global correction, so pathway-level enrichment cannot be claimed. The proposed function is therefore an annotation-based network interpretation rather than statistically validated pathway enrichment.

**Cell composition.** The module is not dominated by plasma or secreted proteins: all genes are annotated as non-secreted, and the proteins detected in placenta are predominantly intracellular or membrane-associated. Most genes have low tissue specificity, which is compatible with broadly expressed cellular machinery rather than a placenta-exclusive or autonomic-nervous-system-exclusive program. HPA evidence highlights structural and stromal or epithelial contexts, including skeletal muscle, heart muscle, extravillous trophoblasts, decidual stromal cells, enterocytes, urothelial cells, and related cell types. Immune-cell specificity is generally low, although PDLIM1, TPM1, and other genes have selected blood-cell or immune-cell annotations. Thus, the shared module is more plausibly related to common structural, trafficking, and cellular-state features than to a plasma-protein signal; residual contribution from shared cell types in the two tissues remains possible.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides two high-confidence relationships within the module: AHNAK with PLEC, and CNDP2 with NARS1. These relationships support the existence of a structural scaffold connection and a separate peptide- or translation-associated connection, but they do not establish a single unified biochemical pathway. No STRING functional-enrichment result was reported. The hu.MAP evidence is limited to complex C1, in which FLNB and AHNAK occur together with additional membrane, signaling, and cytoskeletal-associated proteins. This supports a known protein-complex context for part of the module, while the absence of hu.MAP assignments for the other genes indicates that much of the co-abundance structure is not directly represented by the queried complex data. The network therefore combines a small amount of established physical or complex-level support with broader co-abundance associations.

**STRING interactions (score >= 0.7)**: 2 of 55 gene pairs: AHNAK–PLEC (0.73); CNDP2–NARS1 (0.856)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05674.1 (FLNB, AHNAK; 2/12)

### Novelty

This may be a new tissue-pair co-abundance observation, but the module should not be called a newly discovered molecular complex or pathway. Several component functions and some relationships are already established: AHNAK and PLEC have STRING support, and FLNB with AHNAK appears in hu.MAP complex C1. The genes themselves also have substantial prior literature, especially EEA1, TPM1, IQGAP1, AHNAK, PLEC, and FLNB. Conversely, the particular co-abundance grouping across autonomic nervous system and placenta is not validated by the reported GO, KEGG, or STRING enrichment evidence, and its biological meaning is not demonstrated by the database annotations alone. Absence of additional STRING or hu.MAP links cannot prove novelty. The defensible claim is that the cross-tissue co-abundance pattern is a hypothesis-generating association whose novelty requires independent replication and comparison with published tissue co-expression studies.

**Hypothesis.** Hypothesis: the module reflects a shared cell-architecture and intracellular-trafficking state present in selected cell populations of autonomic nervous system and placenta. In this model, SEC23A supports ER-to-Golgi cargo export, EEA1 supports endosomal organization and vesicle fusion, and IQGAP1 connects membrane signaling to cytoskeletal remodeling. AHNAK, PLEC, FLNB, TPM1, and PDLIM1 could stabilize or coordinate actin, intermediate-filament, and membrane-associated structures during cell shape change, migration, or membrane repair. NARS1, IMPDH2, and CNDP2 could reflect the biosynthetic and metabolic demands of these cells. This is a mechanistic hypothesis, not a demonstrated causal pathway; the lack of globally significant GO or KEGG terms and the sparse database interaction support require testing by cell-resolved expression, protein localization, perturbation, and replication in independent cohorts.

### Important genes

#### EEA1

- **Related proteins** (co-abundance neighbors): SEC23A (0.91), IQGAP1 (0.88), IMPDH2 (0.86), PLEC (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Vesicles; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: early endosome antigen 1. Enables 1-phosphatidylinositol binding activity; GTP-dependent protein binding activity; and protein homodimerization activity. Involved in endocytosis; vesicle fusion; and viral RNA genome replication. Located in cytosol and early endosome. Is extrinsic component of plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: autoimmune disorder of central nervous system (0.370); liver disorder (0.298); external ear disorder (0.273); benign digestive system neoplasm (0.256); Alzheimer disease (0.163)
- **Europe PMC papers**: 7344
- **Why important**: EEA1 is the strongest network connector in the module and links SEC23A, IQGAP1, IMPDH2, and PLEC. Its established localization to early endosomes and function in endocytosis, vesicle fusion, and endosomal transport make it a central candidate for the trafficking interpretation. It is broadly expressed, detected in placenta, and supported by a large literature. Its disease associations include central nervous system autoimmunity and Alzheimer disease, but those associations do not establish a role in this module.
- **Conclusion**: Established evidence supports EEA1 as a broadly expressed endosomal trafficking component and as a network hub. The module-specific conclusion is that EEA1 is a plausible organizer of the trafficking side of the module; whether it drives the shared tissue-pair signal is unproven.

#### PLEC

- **Related proteins** (co-abundance neighbors): IMPDH2 (0.84), EEA1 (0.83), AHNAK (0.80); STRING partners: AHNAK (0.73)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plectin. Plectin is a prominent member of an important family of structurally and in part functionally related proteins, termed plakins or cytolinkers, that are capable of interlinking different elements of the cytoskeleton. Plakins, with their multi-domain structure and enormous size, not only play crucial roles in maintaining cell and tissue integrity and orchestrating dynamic changes in cytoarchitecture…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 5B, with muscular dystrophy (0.796); epidermolysis bullosa simplex 5A, Ogna type (0.775); autosomal recessive limb-girdle muscular dystrophy type 2Q (0.768); epidermolysis bullosa simplex 5C, with pyloric atresia (0.755); epidermolysis bullosa simplex with nail dystrophy (0.695)
- **Europe PMC papers**: 2578
- **Why important**: PLEC connects EEA1, AHNAK, and IMPDH2 and is supported by the STRING relationship with AHNAK. Its established role as a plakin and cytolinker integrates intermediate filaments, actin-associated structures, cell shape, and tissue integrity. It is tissue-enhanced in skeletal muscle, detected in placenta, and has strong disease links to epidermolysis bullosa and muscular dystrophy. Its position at the intersection of trafficking and structural proteins makes it especially informative.
- **Conclusion**: Established evidence supports PLEC as a major cytoskeletal scaffold with disease-relevant roles in tissue integrity. In this module, PLEC plausibly couples cellular architecture to vesicle-associated processes, but the co-abundance data do not demonstrate a direct causal coupling.

#### AHNAK

- **Related proteins** (co-abundance neighbors): FLNB (0.87), TPM1 (0.84), PLEC (0.80); STRING partners: PLEC (0.73)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_05674.1
- **Function (MyGene.info)**: AHNAK nucleoprotein. The protein encoded by this gene is a large (700 kDa) structural scaffold protein consisting of a central domain with 128 aa repeats. The encoded protein may play a role in such diverse processes as blood-brain barrier formation, cell structure and migration, cardiac calcium channel regulation, and tumor metastasis. A much shorter variant encoding a 17 kDa isoform exists for this gene, and the sho…
- **Diseases (Open Targets)**: Aganglionic megacolon (0.266); neoplasm (0.108); hepatocellular carcinoma (0.093); cancer (0.085); melanoma (0.085)
- **Europe PMC papers**: 2886
- **Why important**: AHNAK is connected to FLNB, TPM1, and PLEC and has both STRING support with PLEC and participation with FLNB in hu.MAP complex C1. Its established description as a large structural scaffold includes cell structure, migration, membrane repair, and possible cardiac and barrier functions. It is also annotated in Schwann and epithelial cell contexts and has a substantial literature.
- **Conclusion**: Established evidence supports AHNAK as a structural and membrane-associated scaffold with known relationships to PLEC and FLNB. The module-specific conclusion is that AHNAK is a credible bridge between the cytoskeletal neighborhood and the shared tissue-cellular state, while its precise role in autonomic nervous system and placenta remains a hypothesis.

#### SEC23A

- **Related proteins** (co-abundance neighbors): EEA1 (0.91), IQGAP1 (0.84), NARS1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A is strongly connected within the trafficking-centered part of the network, neighboring EEA1, IQGAP1, and NARS1. Its established role as a COPII component in ER-to-Golgi transport provides a specific secretory-pathway anchor for the module. It is broadly expressed, detected in placenta, and has a defined disease association with craniolenticulosutural dysplasia.
- **Conclusion**: Established evidence supports SEC23A as an ER export and vesicle-budding component. In this module, it supports a protein-trafficking interpretation rather than a tissue-specific secreted-protein interpretation. A direct functional partnership with the other module members is not established.

#### TPM1

- **Related proteins** (co-abundance neighbors): AHNAK (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tropomyosin 1. This gene is a member of the tropomyosin family of highly conserved, widely distributed actin-binding proteins involved in the contractile system of striated and smooth muscles and the cytoskeleton of non-muscle cells. Tropomyosin is composed of two alpha-helical chains arranged as a coiled-coil. It is polymerized end to end along the two grooves of actin filaments and provides stability to the fi…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy (0.798); left ventricular noncompaction (0.760); left ventricular noncompaction 9 (0.664); familial isolated dilated cardiomyopathy (0.639); hypertrophic cardiomyopathy 3 (0.596)
- **Europe PMC papers**: 6278
- **Why important**: TPM1 links to AHNAK and provides a strong contractile and actin-filament interpretation. It is tissue-enhanced in heart and skeletal muscle and is associated with decidual stromal, extravillous trophoblast, and other contractile or stromal cell types. Its extensive literature and established associations with cardiomyopathies make it biologically important, although it was not detected by the cited placental immunohistochemistry result.
- **Conclusion**: Established evidence supports TPM1 as an actin-binding regulator of contractile and cytoskeletal systems with cardiac disease relevance. The module-specific conclusion is that TPM1 may mark a contractile or cytoskeletal cell state shared across tissues, but its absence from the cited placental protein-detection result cautions against treating it as a universal placental component.

#### PDLIM1

- **Related proteins** (co-abundance neighbors): NARS1 (0.86), CNDP2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Actin filaments; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 1. This gene encodes a member of the enigma protein family. The protein contains two protein interacting domains, a PDZ domain at the amino terminal end and one to three LIM domains at the carboxyl terminal. It is a cytoplasmic protein associated with the cytoskeleton. The protein may function as an adapter to bring other LIM-interacting proteins to the cytoskeleton. Pseudogenes associated with this …
- **Diseases (Open Targets)**: ovarian dysfunction (0.167); atrial fibrillation (0.138); liver disorder (0.126); Peyronie disease (0.117); uterine corpus leiomyoma (0.092)
- **Europe PMC papers**: 1123
- **Why important**: PDLIM1 connects the CNDP2 and NARS1 branch and links cytoskeletal organization with responses to hypoxia and oxidative stress, cell polarity, heart development, and migration. It is tissue-enhanced in skeletal muscle and has cell-type annotations in decidual stromal cells, enterocytes, megakaryocytes, and platelets, as well as selected blood-cell enrichment. Its position suggests that it may report cellular structural state and tissue or blood-cell composition.
- **Conclusion**: Established evidence supports PDLIM1 as a cytoskeletal adaptor with polarity, stress-response, and migration functions. In this module, it is a plausible indicator of a stromal, contractile, or cell-composition component, but the blood-cell annotations mean that sample composition must be considered before assigning a tissue-intrinsic mechanism.

## Module 2

**Tissue pair**: autonomic_nervous_system and placenta  
**Genes (8)**: AKAP12, CALU, FLNA, MAP1B, PEPD, PLS3, PZP, STMN1

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING enrichment. The strongest interpretation therefore comes from the gene identities and the co-abundance topology rather than formal pathway enrichment. The module is most consistent with a vascular and placental structural-cell program involving actin and microtubule organization, cell shape, migration, and intracellular signaling. AKAP12 and PLS3 occupy the most connected positions; their links to MAP1B, CALU, and one another suggest coordination between cytoskeletal architecture, localized signaling, and cellular remodeling. MAP1B and STMN1 support a microtubule-related component, whereas PLS3 and FLNA support actin organization. CALU adds an endoplasmic-reticulum calcium-handling and protein-folding dimension, and PEPD adds proline and collagen-related metabolism. These annotations support a coherent biological interpretation, but they do not establish a single canonical pathway for the module.

**Cell composition.** The module is not predominantly a plasma or secreted-protein module: only a minority of its genes are classified as secreted, with PZP explicitly annotated as secreted to blood. It is also not dominated by immune-cell markers. Most genes have tissue- or cell-type-enhanced HPA patterns, especially vascular smooth muscle cells, smooth muscle cells, pericytes, trophoblasts, endothelial-related cells, and neuronal or retinal cells. Several genes are enhanced in blood vessel, brain, retina, intestine, or kidney. Seven of the eight proteins are detected in placenta, whereas the autonomic-nervous-system comparison has no matching HPA tissue measurement. Some immune-cell enrichment is present, including plasmacytoid dendritic cells and selected lymphocyte populations, but the overall pattern favors shared vascular, stromal, placental, and structural cell types over a simple blood-contamination explanation. PZP could nevertheless contribute a circulating or pregnancy-associated component, so sample composition and plasma carryover should be assessed.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

None of the possible gene pairs reached the supplied high-confidence STRING interaction threshold, and no STRING functional-enrichment result was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not supported here as established physical protein interactions or membership in a known multiprotein complex. The absence of STRING and hu.MAP support does not invalidate the module; it indicates that the observed relationships may reflect coordinated expression, shared cell-type composition, indirect regulation, or interactions that are not represented in those resources. The internal network is nevertheless structured rather than random-looking, with a central AKAP12–PLS3–CALU–MAP1B neighborhood and peripheral links involving PEPD, STMN1, FLNA, and PZP.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a new cross-tissue co-abundance pattern, but the data do not prove that it is a new biological mechanism. Its possible novelty is supported by the absence of a corresponding established STRING interaction network, the absence of a shared hu.MAP complex, and the lack of a recognized globally enriched GO or KEGG pathway. However, database absence alone cannot establish novelty. The module could reflect a known cell-type mixture, coordinated vascular or placental state, or technical and sampling effects that are incompletely captured by existing resources. Replication across independent cohorts, adjustment for cell composition, transcript-level validation, and protein-level or perturbational testing would be needed before claiming a novel mechanism.

**Hypothesis.** Hypothesis: this conserved module reflects a shared vascular, stromal, or trophoblast-associated remodeling state in which AKAP12 organizes localized kinase and phosphatase signaling, PLS3 and FLNA regulate actin architecture, MAP1B and STMN1 tune microtubule stability, and CALU supports calcium-dependent endoplasmic-reticulum function. PEPD may support extracellular-matrix or collagen-related proline handling, while PZP may represent a pregnancy-associated circulating protease-regulatory component. The module could therefore coordinate cell shape, adhesion, migration, cytoskeletal turnover, and secretory or matrix remodeling in autonomic-nervous-system and placental samples. This is a mechanistic hypothesis, not an established causal pathway.

### Important genes

#### AKAP12

- **Related proteins** (co-abundance neighbors): PLS3 (0.94), CALU (0.93), PEPD (0.89), MAP1B (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: A-kinase anchoring protein 12. The A-kinase anchor proteins (AKAPs) are a group of structurally diverse proteins, which have the common function of binding to the regulatory subunit of protein kinase A (PKA) and confining the holoenzyme to discrete locations within the cell. This gene encodes a member of the AKAP family. The encoded protein is expressed in endothelial cells, cultured fibroblasts, and osteosarcoma cells. It asso…
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); hair color (0.460); cutaneous melanoma (0.403); skin aging (0.376); Abnormality of the skeletal system (0.329)
- **Europe PMC papers**: 2075
- **Why important**: AKAP12 is a central network node connected to PLS3, CALU, PEPD, and MAP1B. Its established function as a scaffold for protein kinase A, protein kinase C, and phosphatase signaling provides a plausible organizing role for the module. It is detected in placenta and has broad literature coverage, while its HPA pattern is compatible with stromal and vascular-associated biology.
- **Conclusion**: Established evidence supports AKAP12 as a signaling-scaffold protein and as the most central coordinator in this module. Hypothesis: AKAP12 may couple localized signaling to cytoskeletal remodeling in the shared tissue state, but the co-abundance data do not demonstrate direct biochemical coupling.

#### PLS3

- **Related proteins** (co-abundance neighbors): AKAP12 (0.94), STMN1 (0.90), MAP1B (0.90), PEPD (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plastin 3. Plastins are a family of actin-binding proteins that are conserved throughout eukaryote evolution and expressed in most tissues of higher eukaryotes. In humans, two ubiquitous plastin isoforms (L and T) have been identified. Plastin 1 (otherwise known as Fimbrin) is a third distinct plastin isoform which is specifically expressed at high levels in the small intestine. The L isoform is expressed on…
- **Diseases (Open Targets)**: X-linked osteoporosis with fractures (0.727); congenital diaphragmatic hernia (0.553); osteoporosis (0.477); hernia, anterior diaphragmatic (0.380); postmenopausal osteoporosis (0.341)
- **Europe PMC papers**: 1365
- **Why important**: PLS3 is among the most connected genes and links AKAP12, STMN1, MAP1B, and PEPD. Plastin three is an actin-binding protein with functions in actin-bundle and actin-network formation, and its HPA pattern is enhanced in blood vessel tissue with additional epithelial and immune-cell associations. It has established skeletal and cytoskeletal disease links and substantial literature.
- **Conclusion**: Established evidence supports PLS3 as an actin-architecture component and a plausible structural core of the module. Hypothesis: its co-abundance with MAP1B and STMN1 may indicate coordinated actin–microtubule remodeling, although this cross-system coupling remains untested here.

#### MAP1B

- **Related proteins** (co-abundance neighbors): PLS3 (0.90), AKAP12 (0.87), CALU (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: microtubule associated protein 1B. This gene encodes a protein that belongs to the microtubule-associated protein family. The proteins of this family are thought to be involved in microtubule assembly, which is an essential step in neurogenesis. The product of this gene is a precursor polypeptide that presumably undergoes proteolytic processing to generate the final MAP1B heavy chain and LC1 light chain. Gene knockout studies of th…
- **Diseases (Open Targets)**: periventricular nodular heterotopia 9 (0.762); hearing loss, autosomal dominant 83 (0.547); neurodegenerative disease (0.538); periventricular nodular heterotopia (0.522); hereditary disease (0.496)
- **Europe PMC papers**: 3710
- **Why important**: MAP1B is directly connected to PLS3, AKAP12, and CALU and is tissue-enhanced in blood vessel, brain, and retina. Its established roles in microtubule organization, neuron migration, axonogenesis, and nervous-system development make it especially relevant to a module conserved between an autonomic-nervous-system group and placenta. It also has disease associations involving neuronal development and is well represented in the literature.
- **Conclusion**: Established evidence supports MAP1B as the principal neuronal and microtubule-related marker in the module. Hypothesis: MAP1B may connect vascular or trophoblast structural remodeling to neural-like cytoskeletal programs, but a shared cell-state explanation remains equally plausible.

#### CALU

- **Related proteins** (co-abundance neighbors): AKAP12 (0.93), MAP1B (0.86), FLNA (0.85), PZP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calumenin. The product of this gene is a calcium-binding protein localized in the endoplasmic reticulum (ER) and it is involved in such ER functions as protein folding and sorting. This protein belongs to a family of multiple EF-hand proteins (CERC) that include reticulocalbin, ERC-55, and Cab45 and the product of this gene. Alternatively spliced transcript variants encoding different isoforms have been iden…
- **Diseases (Open Targets)**: intelligence (0.490); mathematical ability (0.469); autism spectrum disorder (0.333); attention deficit-hyperactivity disorder (0.333); Alzheimer disease (0.308)
- **Europe PMC papers**: 9190
- **Why important**: CALU is a central connector linking AKAP12, MAP1B, FLNA, and PZP. It is an endoplasmic-reticulum calcium-binding protein involved in protein folding and sorting, and it is enhanced in extravillous trophoblasts and detected in placenta. Its extensive literature and links to neurological and cognitive traits make it a useful bridge between secretory-cell biology, signaling, and cytoskeletal organization.
- **Conclusion**: Established evidence supports CALU as an endoplasmic-reticulum calcium and protein-processing protein positioned at an important network junction. Hypothesis: CALU may couple secretory or calcium-handling demands in trophoblast or vascular cells to cytoskeletal remodeling, but the module does not establish that causal role.

#### FLNA

- **Related proteins** (co-abundance neighbors): CALU (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA connects CALU and is enhanced in blood vessel and intestine, with cell-type associations spanning myoepithelial, stromal, hepatic stellate, and megakaryocyte populations. Its established function is to crosslink actin and connect the cytoskeleton to membrane receptors, integrins, and signaling systems. It has extensive disease literature involving neuronal migration and skeletal-development syndromes.
- **Conclusion**: Established evidence supports FLNA as a membrane-linked actin-organizing protein that can connect cell shape, adhesion, migration, and signaling. Hypothesis: FLNA may provide the mechanical interface through which this module relates cytoskeletal remodeling to vascular or placental cell behavior, but the limited direct network connectivity argues against treating it as the sole driver.

## Module 3

**Tissue pair**: autonomic_nervous_system and placenta  
**Genes (9)**: ANXA6, ARPC4, HSPA5, CANX, TUFM, HBA1, LMNB1, PDIA4, PRDX4

### Function

No GO/KEGG term passed global correction, so the module does not support a formally significant pathway assignment from globally significant GO/KEGG evidence. Its most coherent biological feature is endoplasmic-reticulum protein quality control: CANX, HSPA5, and PDIA4 form a high-confidence STRING-supported chaperone and disulfide-folding subnetwork. PRDX4 adds oxidative and redox control, while TUFM points to mitochondrial translation. ANXA6, LMNB1, and ARPC4 represent membrane-calcium, nuclear-envelope, and actin-remodelling biology, respectively. HBA1 and HBA2 introduce an erythroid or hemoglobin-associated signal. Overall, this is best interpreted as a mixed cellular-state or sample-composition module with an ER proteostasis core rather than as a single established pathway.

**Cell composition.** The module is not dominated by secreted plasma proteins: the HPA summary identifies only a minority as secreted, and the annotated secretome entries are intracellular or membrane-associated. Most genes have low tissue specificity, supporting a broadly expressed housekeeping or stress-related component. The HPA single-cell evidence is concentrated in secretory and trophoblast-related populations, including extravillous trophoblasts, syncytiotrophoblasts, plasma cells, and epididymal cells. HBA1 is specifically associated with erythrocytes and hematopoietic or lymphoid tissues, and HBA2 occurs with HBA1 in the network, raising the possibility of erythroid material or blood-related sample composition. However, overall immune-cell specificity is low, so the module should not be labelled a generic immune module. Placental protein detection supports that much of the module is present in placenta, whereas matching autonomic-nervous-system protein evidence is unavailable in the fact sheet. The shared signal may therefore reflect trophoblast or secretory-cell abundance, a general proteostasis state, and possibly erythroid carryover rather than a specialized function of both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The reported STRING relationships are CANX with HSPA5, CANX with PDIA4, and HSPA5 with PDIA4. These known relationships support a genuine ER folding and quality-control subnetwork within the co-abundance module. No STRING functional-enrichment result was reported. No hu.MAP complex contains multiple module members, so the module is not independently supported as a known physical complex by hu.MAP. The remaining co-abundance links, including connections involving TUFM, ANXA6, LMNB1, ARPC4, and the hemoglobin genes, are not backed by reported high-confidence STRING partners in the fact sheet. Thus, the network combines a biologically interpretable known ER interaction cluster with weaker or potentially composition-driven co-abundance associations.

**STRING interactions (score >= 0.7)**: 3 of 36 gene pairs: CANX–HSPA5 (0.998); CANX–PDIA4 (0.931); HSPA5–PDIA4 (0.99)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a new tissue-pair co-abundance observation, because its precise occurrence across autonomic nervous system and placenta is not established by the supplied interaction resources. Nevertheless, it should not be claimed as a new molecular mechanism. The CANX-HSPA5-PDIA4 relationships are already known, the component genes are individually well studied, and the absence of a hu.MAP complex or additional STRING support does not prove novelty. The strongest defensible novelty claim is therefore the tissue-pair-specific co-abundance configuration and its possible association with placental secretory or proteostasis state, pending replication and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a shared secretory-cell and cellular-stress state in autonomic nervous system and placenta, in which ER chaperoning and disulfide-bond processing are coordinated with peroxide detoxification and mitochondrial protein synthesis. In placenta, trophoblast-associated abundance may be a major contributor. The hemoglobin-gene signal may additionally indicate erythroid material or blood-related composition in some samples. This hypothesis predicts that module activity will track markers of ER unfolded-protein handling, secretory-cell abundance, oxidative stress, and sample erythroid content, rather than defining a dedicated autonomic-placental pathway.

### Important genes

#### HSPA5

- **Related proteins** (co-abundance neighbors): CANX (0.81); STRING partners: CANX (0.998), PDIA4 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is a central biological anchor of the ER component and is directly linked in STRING to CANX and PDIA4. It is an ER HSP seventy chaperone and master regulator of ER homeostasis, with HPA enrichment in extravillous trophoblasts, syncytiotrophoblasts, plasma cells, and epididymal cells. It also has the largest literature presence among the module genes and broad disease relevance in the supplied Open Targets evidence.
- **Conclusion**: Established evidence supports HSPA5 as an ER folding and stress-response factor and as part of the known CANX-HSPA5-PDIA4 interaction cluster. The hypothesis that its co-abundance marks trophoblast or secretory-cell stress in this tissue pair is plausible but not established by this module alone.

#### CANX

- **Related proteins** (co-abundance neighbors): HSPA5 (0.81), HBA1; HBA2 (0.80); STRING partners: HSPA5 (0.998), PDIA4 (0.931)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is the ER lectin chaperone that links the module's ER core to glycoprotein folding and quality control. It is directly connected in STRING to both HSPA5 and PDIA4 and has a prominent network position. HPA assigns it to the ER and shows cell-type enrichment in late spermatids, while the supplied annotation supports roles in protein folding, secretion, and ER-associated degradation.
- **Conclusion**: Established evidence supports CANX as a mechanistic component of ER protein quality control and as a known partner of HSPA5 and PDIA4. Its contribution to a shared placental and autonomic cellular state remains a hypothesis rather than a demonstrated tissue-specific mechanism.

#### PDIA4

- **Related proteins** (co-abundance neighbors): TUFM (0.86); STRING partners: CANX (0.931), HSPA5 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 provides the module with a direct disulfide-isomerase and oxidative protein-folding function. It is connected in STRING to CANX and HSPA5, is localized to the ER, and is enriched in extravillous trophoblasts, hepatocytes, epididymal principal cells, and plasma cells. Its annotation also links it to immunoglobulin assembly and ER-stress responses.
- **Conclusion**: Established evidence supports PDIA4 as an ER thiol-disulfide processing factor within a known chaperone network. Its trophoblast and plasma-cell associations make it relevant to a secretory-cell interpretation, but the module does not establish whether PDIA4 drives the shared co-abundance pattern.

#### TUFM

- **Related proteins** (co-abundance neighbors): PDIA4 (0.86), HBA1; HBA2 (0.84), PRDX4 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Tu translation elongation factor, mitochondrial. This gene encodes a protein which participates in protein translation in mitochondria. Mutations in this gene have been associated with combined oxidative phosphorylation deficiency resulting in lactic acidosis and fatal encephalopathy. A pseudogene has been identified on chromosome 17. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 4 (0.769); neurodegenerative disease (0.502); COVID-19 (0.471); combined oxidative phosphorylation deficiency (0.370); ulcerative colitis (0.303)
- **Europe PMC papers**: 1391
- **Why important**: TUFM has a strong position in the co-abundance graph and connects the ER-related PDIA4 signal with PRDX4 and the hemoglobin-associated nodes. It encodes a mitochondrial translation elongation factor, and its supplied disease annotations connect mitochondrial translation failure with severe oxidative-phosphorylation disorders and encephalopathy. It is also detected in placenta and has substantial literature support.
- **Conclusion**: Established evidence supports TUFM as a mitochondrial translation factor, but it has no reported STRING partner in this module. Its placement may indicate coupling between mitochondrial proteostasis and ER or oxidative stress, although that cross-compartment mechanism is a hypothesis.

#### HBA1

- **Related proteins** (co-abundance neighbors): none; STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hemoglobin subunit alpha 1. The human alpha globin gene cluster located on chromosome 16 spans about 30 kb and includes seven loci: 5'- zeta - pseudozeta - mu - pseudoalpha-1 - alpha-2 - alpha-1 - theta - 3'. The alpha-2 (HBA2) and alpha-1 (HBA1) coding sequences are identical. These genes differ slightly over the 5' untranslated regions and the introns, but they differ significantly over the 3' untranslated regions. Two alp…
- **Diseases (Open Targets)**: alpha thalassemia spectrum (0.758); hemoglobin H disease (0.755); hemoglobin M disease (0.735); Heinz body anemia (0.698); primary familial polycythemia due to EPO receptor mutation (0.689)
- **Europe PMC papers**: 4551
- **Why important**: HBA1 is important because it marks a distinct compositional axis rather than because of network centrality: it is associated with erythrocytes, bone marrow, lymphoid tissue, and selected blood-cell populations in HPA, and it co-occurs with HBA2 in the module graph. Its annotation supports oxygen, carbon-dioxide, nitric-oxide, and peroxide-related biology, while its disease associations include alpha-thalassemia-spectrum disorders.
- **Conclusion**: Established evidence supports HBA1 as an erythroid hemoglobin component and a possible indicator of blood or erythroid material in the samples. Its relationship to the ER chaperone core is not mechanistically established, so a composition-driven explanation is more defensible than a direct functional interaction.

## Module 4

**Tissue pair**: autonomic_nervous_system and placenta  
**Genes (5)**: B2M, DBN1, PKM, LGALS1, LTF

### Function

The module does not have a GO or KEGG term passing global multiple-testing correction, so no GO/KEGG functional annotation can be treated as globally enriched. Its gene content instead supports a mixed biological signal involving extracellular and immune-associated proteins, cellular glycolytic metabolism, cell-surface or cytoskeletal organization, and tissue-interface biology. LGALS1 is associated with cell-cell and cell-matrix interactions and regulation of cellular signaling and apoptosis; B2M represents MHC class I-associated and immune-related biology; PKM represents glycolytic energy production; LTF represents antimicrobial, iron-binding, and mucosal innate defense; and DBN1 represents actin organization and neuronal or synaptic structure. These annotations are biologically plausible but do not constitute enrichment of the module as a whole.

**Cell composition.** The module has a strong composition-related interpretation. LGALS1, B2M, and LTF are secreted to blood according to HPA, so secreted or circulating protein contribution is prominent. LTF is group-enriched in bone marrow and salivary gland and is blood-cell associated with neutrophil and non-classical monocyte annotations, whereas the other genes generally show low immune-cell specificity. Several genes are cell-type enhanced in decidual stromal cells, fibroblasts, platelets, or cDCs, and PKM is tissue-enhanced in skeletal muscle and tongue. The shared autonomic-nervous-system and placenta signal may therefore reflect shared stromal, vascular, secreted-protein, or sample-cellular composition rather than a specialized pathway intrinsic to both tissues. Placental protein detection supports expression of part of the module in placenta, while the supplied HPA tissue result provides no protein-detection evidence for the autonomic nervous system.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

At the supplied high-confidence STRING threshold, none of the possible gene pairs is supported as an interaction, and no hu.MAP complex contains multiple module members. Thus the co-abundance edges are not corroborated by the available physical-interaction or curated-complex resources. The supplementary STRING tissue result (STRING TISSUES Spleen; within-query FDR = 0.0394) links LGALS1, LTF, PKM, and B2M to spleen, which is consistent with an immune or blood-related context, but it is not global enrichment evidence and does not establish direct molecular interaction. The absence of STRING and hu.MAP support means the module is better viewed as a coordinated abundance pattern than as a demonstrated protein complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Spleen (FDR = 0.0394, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is not established as a new biological pathway or protein complex. The lack of high-confidence STRING interactions and the lack of a multi-member hu.MAP complex make a previously characterized physical module unlikely, but database absence alone cannot prove novelty. The genes themselves have substantial prior functional and disease literature, and their individual roles are not new. The potentially novel aspect is the tissue-pair-specific co-abundance pattern linking placental or stromal, immune-secreted, metabolic, and cytoskeletal signals. That claim remains provisional because the module has no globally significant GO/KEGG term and may be driven by shared cell types or circulating proteins.

**Hypothesis.** Hypothesis: this conserved co-abundance pattern reflects a shared tissue-interface or sample-composition state in which stromal or trophoblast-associated cells coexist with circulating or myeloid-derived proteins. LGALS1 could represent the central extracellular or cell-interaction component, B2M an antigen-presentation or inflammatory context marker, PKM a metabolic-demand marker, LTF a secreted innate-defense or myeloid contribution, and DBN1 a structural or neuronal-cell component. In placenta this could correspond to stromal, trophoblast, vascular, and immune-cell admixture; in autonomic nervous system samples it could reflect related stromal, vascular, immune, or tissue-interface contributions. This model predicts that the co-abundance will track cell-composition and secreted-protein measures more strongly than a shared physical complex.

### Important genes

#### LGALS1

- **Related proteins** (co-abundance neighbors): PKM (0.88), B2M (0.85), LTF (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galectin 1. The galectins are a family of beta-galactoside-binding proteins implicated in modulating cell-cell and cell-matrix interactions. This gene product may act as an autocrine negative growth factor that regulates cell proliferation. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: glaucoma (0.349); open-angle glaucoma (0.343); chronic kidney disease (0.330); smoking initiation (0.162); melanoma (0.121)
- **Europe PMC papers**: 4025
- **Why important**: LGALS1 is the most connected node in the supplied module and links to PKM, B2M, and LTF. Its galactoside-binding function is relevant to cell-cell and cell-matrix interactions, and HPA places it in decidual stromal cells, extravillous trophoblasts, fibroblasts, and cDCs while identifying it as secreted to blood. It is detected in placenta and has the largest literature volume among the module genes, with disease associations including glaucoma, chronic kidney disease, and melanoma.
- **Conclusion**: Established evidence supports LGALS1 as a central abundance correlate with extracellular and stromal or trophoblast relevance. It is a plausible module anchor, but the data do not establish that LGALS1 physically connects the other proteins or mechanistically drives the shared tissue pattern.

#### B2M

- **Related proteins** (co-abundance neighbors): LGALS1 (0.85), DBN1 (0.82), PKM (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Plasma membrane; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: beta-2-microglobulin. This gene encodes a serum protein found in association with the major histocompatibility complex (MHC) class I heavy chain on the surface of nearly all nucleated cells. The protein has a predominantly beta-pleated sheet structure that can form amyloid fibrils in some pathological conditions. The encoded antimicrobial protein displays antibacterial activity in amniotic fluid. A mutation in this gen…
- **Diseases (Open Targets)**: MHC class I deficiency (0.656); diffuse large B-cell lymphoma (0.595); HIV infectious disease (0.532); amyloidosis, hereditary systemic 6 (0.528); AL amyloidosis (0.468)
- **Europe PMC papers**: 25100
- **Why important**: B2M is also highly connected, linking LGALS1, DBN1, and PKM. It is the MHC class I associated beta-2-microglobulin protein, is secreted to blood, and has HPA annotations for cDCs, decidual stromal cells, enterocytes, Kupffer cells, and plasma cells. Its immune function, placental detection, extensive literature, and disease associations with MHC class I deficiency, lymphoma, HIV, and amyloidosis make it a strong indicator of immune or circulating-protein context.
- **Conclusion**: Established evidence supports B2M as a central marker of a broad immune or tissue-fluid environment rather than as evidence for a module-specific complex. Its presence strengthens the possibility that shared cellular composition contributes to the conserved signal.

#### PKM

- **Related proteins** (co-abundance neighbors): LGALS1 (0.88), B2M (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyruvate kinase M1/2. This gene encodes a protein involved in glycolysis. The encoded protein is a pyruvate kinase that catalyzes the transfer of a phosphoryl group from phosphoenolpyruvate to ADP, generating ATP and pyruvate. This protein has been shown to interact with thyroid hormone and may mediate cellular metabolic effects induced by thyroid hormones. This protein has been found to bind Opa protein, a bacterial o…
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); autoimmune disorder of central nervous system (0.370); tympanic membrane perforation (0.204); neoplasm (0.121); hepatocellular carcinoma (0.120)
- **Europe PMC papers**: 8544
- **Why important**: PKM connects both LGALS1 and B2M and supplies the clearest metabolic component of the module through its established role in glycolysis and ATP-generating pyruvate production. HPA identifies tissue enhancement in skeletal muscle and tongue, cell-type enhancement in extravillous trophoblasts and several epithelial or germ-cell populations, and placental protein detection. It also has a substantial literature and disease links including neurodegenerative disease and central nervous system autoimmunity.
- **Conclusion**: Established evidence supports PKM as a metabolic-demand marker embedded in the co-abundance pattern. It is consistent with active or compositionally distinct cells in placenta and autonomic nervous system samples, but the module does not show that PKM-specific glycolysis is the organizing mechanism.

#### LTF

- **Related proteins** (co-abundance neighbors): LGALS1 (0.85); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lactotransferrin. This gene is a member of the transferrin family of genes and its protein product is found in the secondary granules of neutrophils. The protein is a major iron-binding protein in milk and body secretions with an antimicrobial activity, making it an important component of the non-specific immune system. The protein demonstrates a broad spectrum of properties, including regulation of iron homeostasi…
- **Diseases (Open Targets)**: tuberculosis (0.517); AL amyloidosis (0.467); Abnormality of the skeletal system (0.435); schizophrenia (0.235); inflammatory bowel disease (0.218)
- **Europe PMC papers**: 7000
- **Why important**: LTF is connected to LGALS1 and is the most compositionally distinctive immune-secreted member. It is a neutrophil-granule and body-secretions protein with iron-binding, antimicrobial, and mucosal-defense functions. HPA places it in bone marrow and salivary gland, associates it with neutrophils and non-classical monocytes, and identifies it as secreted to blood. It contributes to the supplementary spleen association (STRING TISSUES Spleen; within-query FDR = 0.0394) and has literature linking it to infection, inflammation, and systemic disease.
- **Conclusion**: Established evidence supports LTF as a likely indicator of secreted innate-defense or myeloid contribution. It may explain part of the cross-tissue co-abundance through sample composition or circulating protein, but its single module connection makes it less likely to be a structural hub.

#### DBN1

- **Related proteins** (co-abundance neighbors): B2M (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: drebrin 1. The protein encoded by this gene is a cytoplasmic actin-binding protein thought to play a role in the process of neuronal growth. It is a member of the drebrin family of proteins that are developmentally regulated in the brain. A decrease in the amount of this protein in the brain has been implicated as a possible contributing factor in the pathogenesis of memory disturbance in Alzheimer's disease…
- **Diseases (Open Targets)**: intelligence (0.286); Tinnitus (0.207); Alzheimer disease (0.194); mathematical ability (0.175); attention deficit-hyperactivity disorder (0.175)
- **Europe PMC papers**: 1154
- **Why important**: DBN1 is connected to B2M and provides the module's most direct neuronal and structural annotation through actin binding, dendritic development, and synaptic plasticity. HPA identifies it in decidual stromal cells, fibroblasts, late spermatids, and platelets, with plasma-membrane localization and no placental immunohistochemical detection in the supplied evidence. Its literature volume is smaller than that of the other selected genes, but its function is especially relevant to the autonomic nervous system.
- **Conclusion**: Established evidence supports DBN1 as a structural or neuronal-context marker with a peripheral position in this module. Its inclusion is compatible with autonomic tissue biology, but the available evidence does not demonstrate that the module is a neuronal synaptic module or that DBN1 explains the placenta association.
