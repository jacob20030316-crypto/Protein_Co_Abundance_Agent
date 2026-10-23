# Conserved co-abundance modules: heart and prostate

## Module 0

**Tissue pair**: heart and prostate  
**Genes (22)**: BZW2, ANK3, CISD2, EIF3C, FKBP3, GANAB, HNRNPH1, HSP90AA1, LDHA, MESD, OLA1, PSMC6, PSMC2, ADSL, RAN, RUVBL2, SPTBN1, QARS1, CCT7, VPS35, XPO1, XRCC6

### Function

The module is most consistent with a conserved intracellular gene-expression and proteostasis program. The primary evidence is the broad, globally corrected enrichment for regulation of macromolecule metabolism (GO:BP regulation of macromolecule metabolic process; q_global = 0.0071), macromolecule biosynthesis (GO:BP macromolecule biosynthetic process; q_global = 0.0123), metabolic-process regulation (GO:BP regulation of metabolic process; q_global = 0.0147), gene expression (GO:BP gene expression; q_global = 0.0273), ribonucleoprotein-complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0335), and regulation of macromolecule biosynthesis (GO:BP regulation of macromolecule biosynthetic process; q_global = 0.0345). The genes collectively cover translation initiation and aminoacylation through EIF3C and QARS1, RNA handling and nuclear transport through HNRNPH1, RAN, and XPO1, protein folding through CCT7, HSP90AA1, FKBP3, and MESD, proteasomal degradation through PSMC2 and PSMC6, and DNA maintenance through RUVBL2 and XRCC6. Thus, the most defensible interpretation is coordinated control of RNA and protein production, maturation, trafficking, and quality control, rather than a narrowly specialized pathway. The module also contains cytoskeletal and membrane-organizing genes, including ANK3 and SPTBN1, and metabolic or organelle-associated genes, so the network may integrate cellular maintenance with tissue-specific structural demands. No STRING functional-enrichment term was reported, so the GO evidence should carry the main functional interpretation.

**Cell composition.** This is not a plasma-protein or secreted-protein module and it does not show a blood-cell signature. The HPA summary reports low immune-cell specificity for all module genes and only a small secreted-gene component, with the relevant proteins described as intracellular or membrane-associated. Most genes have low tissue specificity, while a smaller subset is enhanced in skeletal muscle, tongue, heart muscle, or testis. Many genes are cell-type enhanced, particularly in reproductive, trophoblast, epithelial, neuronal, or glial populations, but the module is not dominated by a single blood or immune cell type. Protein detection is broadly observed in both heart and prostate for most genes, supporting a shared cellular maintenance program in the sampled tissues. The shared signal could nevertheless reflect common cell populations or common demands for translation, folding, transport, and proteasomal quality control rather than a heart-and-prostate-specific biological pathway.

**GO/KEGG enrichment**: 6 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulation of macromolecule metabolic process | 0.0071 | ANK3, BZW2, CCT7, EIF3C, FKBP3, HNRNPH1, HSP90AA1, PSMC2, PSMC6, QARS1, RAN, RUVBL2, SPTBN1, VPS35, XPO1, XRCC6 |
| GO:BP macromolecule biosynthetic process | 0.0123 | ANK3, BZW2, CCT7, EIF3C, FKBP3, GANAB, HNRNPH1, HSP90AA1, MESD, PSMC6, QARS1, RAN, RUVBL2, SPTBN1, VPS35, XPO1, XRCC6 |
| GO:BP regulation of metabolic process | 0.0147 | ANK3, BZW2, CCT7, CISD2, EIF3C, FKBP3, HNRNPH1, HSP90AA1, PSMC2, PSMC6, QARS1, RAN, RUVBL2, SPTBN1, VPS35, XPO1, XRCC6 |
| GO:BP gene expression | 0.0273 | ANK3, BZW2, CCT7, EIF3C, FKBP3, HNRNPH1, HSP90AA1, MESD, PSMC6, QARS1, RAN, RUVBL2, SPTBN1, VPS35, XPO1, XRCC6 |
| GO:BP ribonucleoprotein complex biogenesis | 0.0335 | EIF3C, HSP90AA1, RAN, RUVBL2, XPO1 |
| GO:BP regulation of macromolecule biosynthetic process | 0.0345 | ANK3, BZW2, CCT7, EIF3C, FKBP3, HNRNPH1, HSP90AA1, PSMC6, QARS1, RAN, RUVBL2, SPTBN1, VPS35, XRCC6 |

### STRING and hu.MAP

The high-confidence STRING relationships support several established local structures: ANK3 with SPTBN1 links membrane organization to the spectrin cytoskeleton; PSMC2 with PSMC6 links two proteasome ATPase subunits; and RAN with XPO1 links the Ran-dependent nuclear export system. Additional STRING links connect CCT7 with EIF3C, HSP90AA1, RAN, and RUVBL2, and connect HSP90AA1 with RUVBL2, providing a coherent chaperone, translation, nuclear transport, and chromatin or DNA-maintenance neighborhood. STRING reported no enriched functional term, so these relationships support architecture rather than independent global enrichment. hu.MAP provides established complex-level support for FKBP3 and MESD in two complexes, and for PSMC2 and PSMC6 in multiple proteasome-related complexes. ADSL and OLA1 also occur together in a hu.MAP complex, although their complex membership is broader and less specific to the module. The partial overlap with large complexes indicates that some module edges reflect known protein-complex biology, while the module as a whole is not simply one canonical complex.

**STRING interactions (score >= 0.7)**: 8 of 231 gene pairs: ANK3–SPTBN1 (0.974); CCT7–EIF3C (0.728); CCT7–HSP90AA1 (0.849); CCT7–RAN (0.726); CCT7–RUVBL2 (0.802); HSP90AA1–RUVBL2 (0.886); PSMC2–PSMC6 (0.999); RAN–XPO1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13998.1 (FKBP3, MESD; 2/23); huMAP3_14982.1 (FKBP3, MESD; 2/28); huMAP3_05064.1 (PSMC2, PSMC6; 2/31); huMAP3_14442.1 (ADSL, OLA1; 2/57); huMAP3_09656.1 (PSMC2, PSMC6; 2/64); huMAP3_13725.1 (PSMC2, PSMC6; 2/69)

### Novelty

This module should not be called a wholly new molecular system. Several of its relationships and components have established biological identities in STRING and hu.MAP, especially the Ran-XPO1 transport pair, the proteasome ATPase pair, the ANK3-SPTBN1 cytoskeletal pair, and the hu.MAP proteasome and FKBP3-MESD memberships. However, the conserved co-abundance organization across heart and prostate may still be a potentially novel observation: the fact sheet does not show a previously named heart-prostate module or a STRING-enriched pathway that completely explains the gene set. Absence of a STRING or hu.MAP annotation for many module relationships is compatible with a new co-abundance context, but it does not establish novelty because databases are incomplete and co-abundance does not demonstrate direct physical interaction. The appropriate conclusion is that the module represents a potentially novel cross-tissue coordination of largely established cellular processes, requiring replication and comparison with published tissue co-abundance modules before claiming a new biological mechanism.

**Hypothesis.** Hypothesis: in both heart and prostate, a shared cellular state increases coordinated demand for translation, folding, nuclear-cytoplasmic exchange, DNA maintenance, and proteasomal turnover. EIF3C and QARS1 could support protein production, CCT7, HSP90AA1, FKBP3, and MESD could buffer folding and maturation, RAN and XPO1 could coordinate nuclear transport, and PSMC2 with PSMC6 could remove damaged or obsolete proteins. RUVBL2 and XRCC6 could connect this maintenance state to DNA repair and genome stability, while ANK3 and SPTBN1 could couple it to cellular architecture. This is a mechanistic model inferred from co-abundance and known gene functions, not proof that these proteins form one physical pathway or that any member causally regulates the others.

### Important genes

#### RAN

- **Related proteins** (co-abundance neighbors): CCT7 (0.92), RUVBL2 (0.90), XRCC6 (0.90), EIF3C (0.90), XPO1 (0.89), LDHA (0.86), HNRNPH1 (0.84), QARS1 (0.84), HSP90AA1 (0.83), GANAB (0.82), PSMC2 (0.82); STRING partners: CCT7 (0.726), XPO1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAN, member RAS oncogene family. RAN (ras-related nuclear protein) is a small GTP binding protein belonging to the RAS superfamily that is essential for the translocation of RNA and proteins through the nuclear pore complex. The RAN protein is also involved in control of DNA synthesis and cell cycle progression. Nuclear localization of RAN requires the presence of regulator of chromosome condensation 1 (RCC1). Mutations in RAN di…
- **Diseases (Open Targets)**: HIV infectious disease (0.565); Orthomyxoviridae infectious disease (0.376); pemphigus foliaceus (0.298); neurodegenerative disease (0.270); Genu valgum (0.136)
- **Europe PMC papers**: 133080
- **Why important**: RAN is the most connected module gene and links CCT7, RUVBL2, XRCC6, EIF3C, XPO1, HNRNPH1, and QARS1 in the co-abundance network. It is annotated for nuclear transport, ribosomal subunit export, DNA metabolism, and cell-cycle functions, and it participates in the globally corrected terms (GO:BP regulation of macromolecule metabolic process; q_global = 0.0071) through (GO:BP regulation of macromolecule biosynthetic process; q_global = 0.0345). Its very large literature base and disease links make it a strong anchor for interpreting the module as a core nuclear-cytoplasmic maintenance program.
- **Conclusion**: Established evidence supports RAN as a central nuclear transport and macromolecule-production component of the module. It is plausible, but not established, that RAN coordinates the observed cross-tissue module by coupling nuclear export to translation and protein quality control.

#### CCT7

- **Related proteins** (co-abundance neighbors): QARS1 (0.96), RAN (0.92), EIF3C (0.90), RUVBL2 (0.90), XRCC6 (0.88), BZW2 (0.86), HNRNPH1 (0.85), HSP90AA1 (0.84), XPO1 (0.83), ADSL (0.83); STRING partners: EIF3C (0.728), HSP90AA1 (0.849), RAN (0.726), RUVBL2 (0.802)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 has a highly central network position and connects translation-associated genes with HSP90AA1, RUVBL2, RAN, and XRCC6. As a subunit of the CCT chaperonin, it supports ATP-dependent folding of actin, tubulin, and other client proteins. It is present in (GO:BP regulation of macromolecule metabolic process; q_global = 0.0071), (GO:BP macromolecule biosynthetic process; q_global = 0.0123), (GO:BP regulation of metabolic process; q_global = 0.0147), (GO:BP gene expression; q_global = 0.0273), and (GO:BP regulation of macromolecule biosynthetic process; q_global = 0.0345), is detected in both heart and prostate, and has established STRING links to several central module genes.
- **Conclusion**: Established evidence supports CCT7 as a proteostasis hub that helps explain why the module combines gene-expression machinery with structural and stress-related proteins. Its role as a cross-tissue coordinator of the whole module remains a hypothesis rather than a demonstrated causal function.

#### HSP90AA1

- **Related proteins** (co-abundance neighbors): EIF3C (0.91), XPO1 (0.90), BZW2 (0.85), PSMC2 (0.84), CCT7 (0.84), QARS1 (0.84), RUVBL2 (0.83), RAN (0.83), FKBP3 (0.83); STRING partners: CCT7 (0.849), RUVBL2 (0.886)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein 90 alpha family class A member 1. The protein encoded by this gene is an inducible molecular chaperone that functions as a homodimer. The encoded protein aids in the proper folding of specific target proteins by use of an ATPase activity that is modulated by co-chaperones. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: cancer (0.643); plasma cell myeloma (0.404); non-small cell lung carcinoma (0.394); dengue disease (0.375); Orthomyxoviridae infectious disease (0.375)
- **Europe PMC papers**: 8215
- **Why important**: HSP90AA1 is a central network member connected to EIF3C, XPO1, BZW2, PSMC2, CCT7, QARS1, RUVBL2, and RAN. It is an inducible molecular chaperone involved in folding selected client proteins and is represented in every globally corrected term (GO:BP regulation of macromolecule metabolic process; q_global = 0.0071) through (GO:BP regulation of macromolecule biosynthetic process; q_global = 0.0345). Its strong STRING relationships with CCT7 and RUVBL2 support a chaperone and remodeling neighborhood, and its extensive literature and disease associations make it an important biological interpreter.
- **Conclusion**: Established evidence supports HSP90AA1 as a major protein-folding and cellular-stress component. The fact that HPA did not detect it immunohistochemically in heart or prostate cautions against treating its measured co-abundance as direct evidence of abundant local protein; its transcript or protein regulation may still contribute to the module.

#### EIF3C

- **Related proteins** (co-abundance neighbors): HSP90AA1 (0.91), CCT7 (0.90), RAN (0.90), PSMC2 (0.89), PSMC6 (0.89), BZW2 (0.87), SPTBN1 (0.82); STRING partners: CCT7 (0.728)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C connects translation-related and proteostasis-related genes, including HSP90AA1, CCT7, RAN, PSMC2, PSMC6, BZW2, and SPTBN1. It enables ribosome binding and translation initiation and occurs in all globally corrected terms (GO:BP regulation of macromolecule metabolic process; q_global = 0.0071) through (GO:BP regulation of macromolecule biosynthetic process; q_global = 0.0345). HPA detects it in both heart and prostate, and its literature and disease associations provide support for interpreting the module as an active macromolecule-biosynthesis program.
- **Conclusion**: Established evidence supports EIF3C as a translation-initiation component at the center of the module's gene-expression signal. It is reasonable to hypothesize that EIF3C helps couple increased translation to chaperone and proteasome demand, but the co-abundance data do not establish that coupling causally.

#### PSMC2

- **Related proteins** (co-abundance neighbors): CISD2 (0.91), EIF3C (0.89), RUVBL2 (0.88), XRCC6 (0.86), QARS1 (0.86), XPO1 (0.85), BZW2 (0.84), HSP90AA1 (0.84), RAN (0.82), OLA1 (0.81); STRING partners: PSMC6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in heart, prostate
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is highly connected within the module and links proteasomal degradation with EIF3C, RUVBL2, XRCC6, QARS1, XPO1, BZW2, and HSP90AA1. Together with PSMC6, it forms a known proteasome ATPase relationship in STRING and appears in several hu.MAP proteasome-related complexes. Its annotations include ubiquitin-dependent proteolysis and oxidative-stress response, while its disease associations include hematologic malignancy and amyloidosis.
- **Conclusion**: Established evidence supports PSMC2 as the module's clearest protein-clearance component and as a bridge between biosynthesis, stress handling, and degradation. Its participation in a coordinated proteostasis response across heart and prostate is a plausible hypothesis, not a demonstrated tissue-specific mechanism.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): CCT7 (0.90), RAN (0.90), PSMC2 (0.88), XRCC6 (0.87), ADSL (0.84), HSP90AA1 (0.83); STRING partners: CCT7 (0.802), HSP90AA1 (0.886)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 connects CCT7, RAN, PSMC2, XRCC6, ADSL, and HSP90AA1. It has ATPase and DNA-helicase activities and annotations involving DNA repair, recombination, DNA-replication regulation, telomere maintenance, and ribonucleoprotein assembly. It appears in all globally corrected terms (GO:BP regulation of macromolecule metabolic process; q_global = 0.0071) through (GO:BP regulation of macromolecule biosynthetic process; q_global = 0.0345), and its STRING links with CCT7 and HSP90AA1 support a remodeling and chaperone-associated neighborhood. Its disease associations include hypogonadotropic hypogonadism and neoplasm.
- **Conclusion**: Established evidence supports RUVBL2 as a multifunctional ATPase connecting RNA or ribonucleoprotein biology with genome maintenance and proteostasis. Its position suggests a possible coordination point between these processes, but the module does not prove that RUVBL2 mechanistically drives the shared heart-prostate signal.

## Module 1

**Tissue pair**: heart and prostate  
**Genes (33)**: GOT2, ACADM, ACADVL, ACO2, ACSL1, AIFM1, MAOA, ATP5PB, ATP5F1A, ATP5F1C, CS, MT-CO2, HADHB, ETFA, ETFDH, FUNDC2, HSDL2, L2HGDH, IMMT, NDUFA9, NDUFA10, NDUFS1, NDUFS2, NDUFV1, DBT, DLAT, PDHB, UQCRC2, SDHA, SPRYD4, SUCLG1, SUCLA2, SUCLG2

### Function

This is a mitochondrial oxidative-energy module. The strongest interpretation is coordinated mitochondrial respiration, electron transport, oxidative phosphorylation, tricarboxylic-acid-cycle activity, and ATP production. This conclusion is supported directly by the globally corrected terms for mitochondrion, mitochondrial matrix, mitochondrial membranes, cellular and aerobic respiration, oxidative phosphorylation, the respiratory electron-transport chain, proton-motive-force-driven ATP synthesis, the TCA cycle, and related energy-generating processes (6 globally significant GO/KEGG terms, q_global 6.67e-08–1.58e-05; see the table), (17 globally significant GO/KEGG terms, q_global 0.000179–0.00336; see the table), (GO:BP tricarboxylic acid cycle; q_global = 0.0121), (7 globally significant GO/KEGG terms, q_global 0.023–0.0297; see the table). The module spans substrate entry and oxidation through the TCA cycle, respiratory complexes, and ATP synthase. STRING independently supports mitochondrial localization and the connection between the TCA cycle and respiratory electron transport (15 supplementary STRING terms; within-query FDR 6.32e-10–1.6e-05). The network is therefore biologically coherent rather than merely a collection of loosely related metabolic genes. The disease-pathway terms involving cardiomyopathy, neurodegeneration, and reactive oxygen species (KEGG Diabetic cardiomyopathy - Homo sapiens (human); q_global = 0.00144), (KEGG Chemical carcinogenesis - reactive oxygen species - Homo sapiens (human); q_global = 0.00689), (KEGG Parkinson disease - Homo sapiens (human); q_global = 0.0127), (KEGG Huntington disease - Homo sapiens (human); q_global = 0.0318), (KEGG Non-alcoholic fatty liver disease - Homo sapiens (human); q_global = 0.0389), (KEGG Prion disease - Homo sapiens (human); q_global = 0.0396), (KEGG Amyotrophic lateral sclerosis - Homo sapiens (human); q_global = 0.0488) should be interpreted as pathway overlap with mitochondrial dysfunction, not as evidence that the module specifically causes any of those diseases.

**Cell composition.** The module is not dominated by plasma proteins, secreted proteins, or blood-cell markers: the HPA summary reports no secreted genes and generally low immune-cell specificity. Most members are mitochondrial and are detected at the protein level in heart and prostate, supporting a genuine tissue-associated mitochondrial program. HPA tissue and single-cell annotations nevertheless show substantial enrichment in metabolically active tissues and cell types, especially tongue, skeletal muscle, liver, heart muscle, parietal cells, hepatocytes, enterocytes, and related epithelial or muscle populations. This pattern suggests that the shared heart–prostate signal may partly reflect conserved abundance of mitochondria-rich or metabolically active cells rather than a prostate-specific mechanism. ACSL1 and L2HGDH have immune-cell annotations involving neutrophils or basophils, but these are isolated observations and do not make the module a blood-cell module. SPRYD4 is an exception with no heart or prostate protein detection in HPA, so its inclusion should be treated cautiously.

**GO/KEGG enrichment**: 50 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrion | 6.67e-08 | ACADM, ACADVL, ACO2, ACSL1, AIFM1, ATP5F1A, ATP5F1C, ATP5PB, CS, DBT, DLAT, ETFA, ETFDH, FUNDC2, GOT2, HADHB, HSDL2, IMMT, L2HGDH, MAOA, MT-CO2, NDUFA10, NDUFA9, NDUFS1, NDUFS2, NDUFV1, PDHB, SDHA, SPRYD4, SUCLA2, SUCLG1, SUCLG2, UQCRC2 |
| GO:BP energy derivation by oxidation of organic compounds | 2.74e-07 | ACADM, ACADVL, ACO2, ATP5F1A, ATP5F1C, ATP5PB, CS, DLAT, ETFA, ETFDH, MT-CO2, NDUFA10, NDUFA9, NDUFS1, NDUFS2, NDUFV1, PDHB, SDHA, SUCLA2, SUCLG1, SUCLG2, UQCRC2 |
| GO:BP generation of precursor metabolites and energy | 9.27e-07 | ACADM, ACADVL, ACO2, ATP5F1A, ATP5F1C, ATP5PB, CS, DLAT, ETFA, ETFDH, MT-CO2, NDUFA10, NDUFA9, NDUFS1, NDUFS2, NDUFV1, PDHB, SDHA, SUCLA2, SUCLG1, SUCLG2, UQCRC2 |
| GO:BP cellular respiration | 1.97e-06 | ACO2, ATP5F1A, ATP5F1C, ATP5PB, CS, DLAT, ETFA, ETFDH, MT-CO2, NDUFA10, NDUFA9, NDUFS1, NDUFS2, NDUFV1, PDHB, SDHA, SUCLA2, SUCLG1, SUCLG2, UQCRC2 |
| GO:BP aerobic respiration | 1.21e-05 | ACO2, ATP5F1A, ATP5F1C, ATP5PB, CS, DLAT, MT-CO2, NDUFA10, NDUFA9, NDUFS1, NDUFS2, NDUFV1, PDHB, SDHA, SUCLA2, SUCLG1, SUCLG2, UQCRC2 |
| GO:CC mitochondrial matrix | 1.58e-05 | ACADM, ACADVL, ACO2, ATP5F1A, ATP5F1C, ATP5PB, CS, DBT, DLAT, ETFA, GOT2, HADHB, MT-CO2, NDUFA10, NDUFA9, NDUFS1, NDUFS2, PDHB, SDHA, SUCLA2, SUCLG1, SUCLG2 |
| GO:CC mitochondrial membrane | 3.68e-05 | ACADM, ACADVL, ACSL1, AIFM1, ATP5F1A, ATP5F1C, ATP5PB, ETFDH, FUNDC2, HADHB, IMMT, L2HGDH, MAOA, MT-CO2, NDUFA10, NDUFA9, NDUFS1, NDUFS2, NDUFV1, SDHA, UQCRC2 |
| GO:CC mitochondrial envelope | 0.000163 | ACADM, ACADVL, ACSL1, AIFM1, ATP5F1A, ATP5F1C, ATP5PB, ETFDH, FUNDC2, HADHB, IMMT, L2HGDH, MAOA, MT-CO2, NDUFA10, NDUFA9, NDUFS1, NDUFS2, NDUFV1, SDHA, UQCRC2 |
| KEGG Metabolic pathways - Homo sapiens (human) | 0.000179 | ACADM, ACADVL, ACO2, ACSL1, ATP5F1A, ATP5F1C, ATP5PB, CS, DBT, DLAT, GOT2, HADHB, L2HGDH, MAOA, MT-CO2, NDUFA10, NDUFA9, NDUFS1, NDUFS2, NDUFV1, PDHB, SDHA, SUCLA2, SUCLG1, SUCLG2, UQCRC2 |
| KEGG Thermogenesis - Homo sapiens (human) | 0.000253 | ACSL1, ATP5F1A, ATP5F1C, ATP5PB, MT-CO2, NDUFA10, NDUFA9, NDUFS1, NDUFS2, NDUFV1, SDHA, UQCRC2 |
| KEGG Oxidative phosphorylation - Homo sapiens (human) | 0.000408 | ATP5F1A, ATP5F1C, ATP5PB, MT-CO2, NDUFA10, NDUFA9, NDUFS1, NDUFS2, NDUFV1, SDHA, UQCRC2 |
| GO:CC mitochondrial inner membrane | 0.000414 | ACADVL, AIFM1, ATP5F1A, ATP5F1C, ATP5PB, ETFDH, HADHB, IMMT, L2HGDH, MT-CO2, NDUFA10, NDUFA9, NDUFS1, NDUFS2, NDUFV1, SDHA, UQCRC2 |
| GO:CC organelle inner membrane | 0.000519 | ACADVL, AIFM1, ATP5F1A, ATP5F1C, ATP5PB, ETFDH, HADHB, IMMT, L2HGDH, MT-CO2, NDUFA10, NDUFA9, NDUFS1, NDUFS2, NDUFV1, SDHA, UQCRC2 |
| GO:BP proton motive force-driven mitochondrial ATP synthesis | 0.000751 | ATP5F1A, ATP5F1C, ATP5PB, NDUFA10, NDUFA9, NDUFS1, NDUFS2, NDUFV1, SDHA |
| GO:CC respiratory chain complex | 0.000923 | ATP5F1A, ATP5F1C, ATP5PB, MT-CO2, NDUFA10, NDUFA9, NDUFS1, NDUFS2, NDUFV1, SDHA, UQCRC2 |

### STRING and hu.MAP

STRING contains many high-confidence relationships among the module genes, including links within fatty-acid oxidation, the TCA cycle, respiratory electron transport, and ATP synthase. The strongest network-supported structure connects ACADM, ACADVL, ETFA, ETFDH, HADHB, and ACSL1 with central respiratory and TCA genes, while another dense structure connects NDUFA10, NDUFA9, NDUFS1, NDUFS2, NDUFV1, SDHA, MT-CO2, and UQCRC2. These relationships are largely established functional or physical associations, so the co-abundance network recapitulates known mitochondrial biology rather than establishing new protein interactions. hu.MAP independently identifies repeated complex-I groupings containing NDUFA10, NDUFA9, NDUFS1, NDUFS2, and NDUFV1 (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1) (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_07653.1), pyruvate-dehydrogenase groupings containing DLAT, PDHB, and DBT (hu.MAP huMAP3_12248.1), (hu.MAP huMAP3_04919.1) (hu.MAP huMAP3_08216.1) (hu.MAP huMAP3_07514.1) (hu.MAP huMAP3_09761.1) (hu.MAP huMAP3_10899.1) (hu.MAP huMAP3_10412.1) (hu.MAP huMAP3_14339.1) (hu.MAP huMAP3_11877.1) (hu.MAP huMAP3_14864.1), ATP-synthase groupings containing ATP5PB, ATP5F1A, and ATP5F1C (hu.MAP huMAP3_09307.1), (hu.MAP huMAP3_11095.1), (hu.MAP huMAP3_08716.1) (hu.MAP huMAP3_07476.1) (hu.MAP huMAP3_05994.1) (hu.MAP huMAP3_08393.1) (hu.MAP huMAP3_09775.1), and respiratory-complex groupings involving MT-CO2 and UQCRC2 (hu.MAP huMAP3_00773.1), (hu.MAP huMAP3_10623.1). The repeated complex-I and ATP-synthase memberships provide particularly strong support that the module captures coordinated abundance of established mitochondrial assemblies. The module should not be interpreted as one single physical complex; it is a cross-complex metabolic and respiratory program.

**STRING interactions (score >= 0.7)**: 163 of 528 gene pairs: ACADM–ACADVL (0.713); ACADM–ACSL1 (0.728); ACADM–ETFA (0.995); ACADM–ETFDH (0.766); ACADM–HADHB (0.886); ACADM–HSDL2 (0.835); ACADM–SUCLA2 (0.755); ACADVL–ACSL1 (0.841); ACADVL–ETFA (0.877); ACADVL–ETFDH (0.817); ACADVL–HADHB (0.988); ACADVL–HSDL2 (0.787); ACO2–ATP5F1A (0.884); ACO2–CS (0.999); ACO2–DLAT (0.727); ACO2–GOT2 (0.753); ACO2–NDUFA10 (0.747); ACO2–NDUFA9 (0.756); ACO2–NDUFS1 (0.865); ACO2–NDUFS2 (0.955); ACO2–NDUFV1 (0.944); ACO2–SDHA (0.975); ACO2–SUCLA2 (0.862); ACO2–SUCLG1 (0.929); ACO2–SUCLG2 (0.735); ACO2–UQCRC2 (0.879); ATP5F1A–ATP5F1C (0.999); ATP5F1A–ATP5PB (0.999); ATP5F1A–CS (0.94); ATP5F1A–DLAT (0.8); ATP5F1A–ETFA (0.786); ATP5F1A–IMMT (0.809); ATP5F1A–MT-CO2 (0.719); ATP5F1A–NDUFA10 (0.759); ATP5F1A–NDUFA9 (0.947); ATP5F1A–NDUFS1 (0.961); ATP5F1A–NDUFS2 (0.98); ATP5F1A–NDUFV1 (0.958); ATP5F1A–PDHB (0.81); ATP5F1A–SDHA (0.972); ATP5F1A–SUCLA2 (0.802); ATP5F1A–SUCLG1 (0.853); ATP5F1A–UQCRC2 (0.986); ATP5F1C–ATP5PB (0.999); ATP5F1C–CS (0.726); ATP5F1C–ETFA (0.715); ATP5F1C–NDUFA10 (0.919); ATP5F1C–NDUFA9 (0.934); ATP5F1C–NDUFS1 (0.959); ATP5F1C–NDUFS2 (0.95); ATP5F1C–NDUFV1 (0.949); ATP5F1C–PDHB (0.913); ATP5F1C–SDHA (0.75); ATP5F1C–SUCLA2 (0.751); ATP5F1C–SUCLG1 (0.934); ATP5F1C–SUCLG2 (0.728); ATP5F1C–UQCRC2 (0.98); ATP5PB–NDUFA9 (0.853); ATP5PB–NDUFS1 (0.886); ATP5PB–NDUFS2 (0.85); ATP5PB–NDUFV1 (0.731); ATP5PB–SDHA (0.755); ATP5PB–UQCRC2 (0.973); CS–DBT (0.865); CS–DLAT (0.996); CS–GOT2 (0.952); CS–HADHB (0.951); CS–L2HGDH (0.931); CS–NDUFS1 (0.737); CS–NDUFS2 (0.772); CS–NDUFV1 (0.724); CS–PDHB (0.941); CS–SDHA (0.984); CS–SUCLA2 (0.96); CS–SUCLG1 (0.929); CS–SUCLG2 (0.948); CS–UQCRC2 (0.746); DBT–HADHB (0.843); DBT–PDHB (0.957); DBT–SDHA (0.714); DBT–SUCLA2 (0.901); DBT–SUCLG1 (0.956); DBT–SUCLG2 (0.89); DLAT–HADHB (0.906); DLAT–NDUFS1 (0.773); DLAT–NDUFS2 (0.713); DLAT–PDHB (0.999); DLAT–SDHA (0.852); DLAT–SUCLA2 (0.982); DLAT–SUCLG1 (0.99); DLAT–SUCLG2 (0.967); ETFA–ETFDH (0.999); ETFA–HADHB (0.829); ETFA–PDHB (0.728); ETFA–SDHA (0.706); ETFA–SUCLG1 (0.956); ETFA–UQCRC2 (0.757); ETFDH–HADHB (0.924); ETFDH–HSDL2 (0.701); GOT2–NDUFS2 (0.802); GOT2–SDHA (0.981); HADHB–HSDL2 (0.918); HADHB–SDHA (0.785); HADHB–SUCLA2 (0.915); HADHB–SUCLG1 (0.94); HADHB–SUCLG2 (0.897); HADHB–UQCRC2 (0.763); IMMT–NDUFA9 (0.747); IMMT–NDUFS1 (0.901); IMMT–NDUFS2 (0.735); IMMT–UQCRC2 (0.811); MT-CO2–NDUFA10 (0.859); MT-CO2–NDUFA9 (0.885); MT-CO2–NDUFS1 (0.976); MT-CO2–NDUFS2 (0.985); MT-CO2–NDUFV1 (0.972); MT-CO2–SDHA (0.958); MT-CO2–UQCRC2 (0.999); NDUFA10–NDUFA9 (0.999); NDUFA10–NDUFS1 (0.999); NDUFA10–NDUFS2 (0.999); NDUFA10–NDUFV1 (0.999); NDUFA10–SDHA (0.793); NDUFA10–SUCLG1 (0.836); NDUFA10–UQCRC2 (0.986); NDUFA9–NDUFS1 (0.999); NDUFA9–NDUFS2 (0.999); NDUFA9–NDUFV1 (0.999); NDUFA9–PDHB (0.733); NDUFA9–SDHA (0.982); NDUFA9–SUCLG1 (0.774); NDUFA9–UQCRC2 (0.997); NDUFS1–NDUFS2 (0.999); NDUFS1–NDUFV1 (0.999); NDUFS1–PDHB (0.809); NDUFS1–SDHA (0.995); NDUFS1–SUCLA2 (0.777); NDUFS1–SUCLG1 (0.752); NDUFS1–SUCLG2 (0.728); NDUFS1–UQCRC2 (0.998); NDUFS2–NDUFV1 (0.999); NDUFS2–SDHA (0.998); NDUFS2–SUCLA2 (0.837); NDUFS2–SUCLG1 (0.916); NDUFS2–SUCLG2 (0.8); NDUFS2–UQCRC2 (0.994); NDUFV1–PDHB (0.738); NDUFV1–SDHA (0.999); NDUFV1–SUCLG1 (0.836); NDUFV1–UQCRC2 (0.998); PDHB–SDHA (0.731); PDHB–SUCLA2 (0.921); PDHB–SUCLG1 (0.821); PDHB–UQCRC2 (0.905); SDHA–SUCLA2 (0.998); SDHA–SUCLG1 (0.999); SDHA–SUCLG2 (0.997); SDHA–UQCRC2 (0.99); SUCLA2–SUCLG1 (0.999); SUCLA2–SUCLG2 (0.928); SUCLA2–UQCRC2 (0.7); SUCLG1–SUCLG2 (0.999); SUCLG1–UQCRC2 (0.866)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Mitochondrion (FDR = 6.32e-10, 32 genes); Keyword Transit peptide (FDR = 2.58e-09, 27 genes); RCTM The citric acid (TCA) cycle and respiratory electron transport (FDR = 3.58e-09, 21 genes); Keyword Mitochondrion (FDR = 4.72e-09, 30 genes); Component Mitochondrion (FDR = 6.92e-09, 32 genes); Process Energy derivation by oxidation of organic compounds (FDR = 2.89e-08, 22 genes); Process Cellular respiration (FDR = 8.24e-08, 20 genes); Process Aerobic respiration (FDR = 4.51e-07, 18 genes); COMPARTMENTS Mitochondrial protein complex (FDR = 6.88e-07, 19 genes); Component Mitochondrial protein-containing complex (FDR = 1.78e-06, 18 genes); COMPARTMENTS Mitochondrial matrix (FDR = 2.28e-06, 21 genes); COMPARTMENTS Mitochondrial membrane (FDR = 6.02e-06, 20 genes); Component Mitochondrial membrane (FDR = 6.66e-06, 21 genes); HPO Abnormality of acid-base homeostasis (FDR = 7.47e-06, 21 genes); Component Mitochondrial matrix (FDR = 1.6e-05, 21 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14018.1 (NDUFS2, NDUFA10, NDUFS1, NDUFV1, NDUFA9; 5/48); huMAP3_06397.1 (NDUFS2, NDUFA10, NDUFS1, NDUFV1, NDUFA9; 5/49); huMAP3_09982.1 (NDUFS2, NDUFA10, NDUFS1, NDUFV1, NDUFA9; 5/49); huMAP3_09567.1 (NDUFS2, NDUFA10, NDUFS1, NDUFV1, NDUFA9; 5/52); huMAP3_14878.1 (NDUFS2, NDUFA10, NDUFS1, NDUFV1, NDUFA9; 5/53); huMAP3_02819.1 (NDUFA10, NDUFS1, NDUFV1, NDUFA9; 4/34); huMAP3_07653.1 (NDUFA10, NDUFS1, NDUFA9; 3/7); huMAP3_12248.1 (DLAT, PDHB, DBT; 3/22); huMAP3_09307.1 (ATP5PB, ATP5F1A, ATP5F1C; 3/35); huMAP3_11095.1 (ATP5PB, ATP5F1A, ATP5F1C; 3/45); huMAP3_00773.1 (MT-CO2, UQCRC2; 2/3); huMAP3_07245.1 (UQCRC2, ATP5F1A; 2/4); huMAP3_12388.1 (ACADM, ETFA; 2/7); huMAP3_04919.1 (DLAT, PDHB; 2/7); huMAP3_08216.1 (DLAT, PDHB; 2/8); huMAP3_07514.1 (DLAT, PDHB; 2/9); huMAP3_09761.1 (DLAT, PDHB; 2/10); huMAP3_10899.1 (DLAT, PDHB; 2/10); huMAP3_10412.1 (DLAT, PDHB; 2/12); huMAP3_14339.1 (DLAT, PDHB; 2/13); huMAP3_11877.1 (DLAT, PDHB; 2/14); huMAP3_14864.1 (DLAT, PDHB; 2/14); huMAP3_08716.1 (ATP5PB, ATP5F1C; 2/15); huMAP3_07476.1 (ATP5PB, ATP5F1C; 2/18); huMAP3_05994.1 (ATP5PB, ATP5F1C; 2/19); huMAP3_08393.1 (ATP5PB, ATP5F1C; 2/19); huMAP3_09775.1 (ATP5PB, ATP5F1C; 2/21); huMAP3_10623.1 (MT-CO2, UQCRC2; 2/24); huMAP3_08132.1 (NDUFS2, NDUFV1; 2/24); huMAP3_06247.1 (UQCRC2, ATP5PB; 2/65)

### Novelty

The module is unlikely to represent a newly discovered mitochondrial function: its principal genes, annotations, STRING relationships, and hu.MAP complexes are already well established. What may be new is the observation that these known mitochondrial components form a conserved co-abundance module across heart and prostate in this particular dataset. That dataset-level conservation could be biologically useful, but the fact sheet does not establish tissue-specific causality, a novel physical interaction, or a previously unknown pathway. Absence of hu.MAP membership for several genes and absence of listed STRING partners for some genes do not prove novelty, because database coverage and evidence types are incomplete. The most defensible claim is therefore a potentially novel cross-tissue co-abundance pattern built from largely established mitochondrial biology.

**Hypothesis.** Hypothesis: the module reflects a shared mitochondrial energy-demand program in metabolically active heart and prostate cells. Coordinated abundance of fatty-acid oxidation components such as ACADM, ACADVL, ETFA, ETFDH, and HADHB may supply reducing equivalents and acetyl units; PDHB and DLAT may connect pyruvate oxidation to the TCA cycle; respiratory-chain components may convert those reducing equivalents into a proton gradient; and ATP5F1A, ATP5F1C, and ATP5PB may use that gradient for ATP synthesis. IMMT may help maintain inner-membrane and cristae organization needed for this process. A testable prediction is that variation in this module will track mitochondrial respiratory capacity and substrate oxidation across matched heart and prostate samples, while also being sensitive to differences in the abundance of mitochondria-rich cell populations. This is a mechanistic model, not a demonstrated causal mechanism.

### Important genes

#### SDHA

- **Related proteins** (co-abundance neighbors): MAOA (0.87), IMMT (0.85), NDUFS2 (0.85), AIFM1 (0.84), GOT2 (0.83), HSDL2 (0.83), ACADVL (0.82); STRING partners: ACO2 (0.975), ATP5F1A (0.972), ATP5F1C (0.75), ATP5PB (0.755), CS (0.984), DBT (0.714), DLAT (0.852), ETFA (0.706), GOT2 (0.981), HADHB (0.785), MT-CO2 (0.958), NDUFA10 (0.793), NDUFA9 (0.982), NDUFS1 (0.995), NDUFS2 (0.998), NDUFV1 (0.999), PDHB (0.731), SUCLA2 (0.998), SUCLG1 (0.999), SUCLG2 (0.997), UQCRC2 (0.99)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate dehydrogenase complex flavoprotein subunit A. This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identi…
- **Diseases (Open Targets)**: mitochondrial complex II deficiency, nuclear type 1 (0.813); pheochromocytoma/paraganglioma syndrome 5 (0.790); dilated cardiomyopathy 1GG (0.768); neurodegeneration with ataxia and late-onset optic atrophy (0.761); gastrointestinal stromal tumor (0.743)
- **Europe PMC papers**: 12756
- **Why important**: SDHA is one of the most connected genes in the module and links the TCA cycle directly to respiratory complex II. It is present across nearly all of the primary mitochondrial respiration and energy terms, has extensive STRING support with TCA, respiratory-chain, ATP-synthase, and pyruvate-oxidation genes, and is supported by multiple mitochondrial complex annotations. HPA describes heart- and skeletal-muscle enhancement and detects the protein in both tissues. Its disease associations include complex-II deficiency and cardiomyopathy, and it has a substantial literature base.
- **Conclusion**: Established evidence supports SDHA as a central metabolic and respiratory anchor of the module, not merely a correlated marker. The co-abundance data are consistent with coordinated complex-II and TCA activity, but do not show that SDHA is the driver of the cross-tissue module or that the module causes SDHA-associated disease.

#### NDUFS1

- **Related proteins** (co-abundance neighbors): AIFM1 (0.91), NDUFA10 (0.85), UQCRC2 (0.85), IMMT (0.84), NDUFS2 (0.84), PDHB (0.80); STRING partners: ACO2 (0.865), ATP5F1A (0.961), ATP5F1C (0.959), ATP5PB (0.886), CS (0.737), DLAT (0.773), IMMT (0.901), MT-CO2 (0.976), NDUFA10 (0.999), NDUFA9 (0.999), NDUFS2 (0.999), NDUFV1 (0.999), PDHB (0.809), SDHA (0.995), SUCLA2 (0.777), SUCLG1 (0.752), SUCLG2 (0.728), UQCRC2 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, prostate
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1, huMAP3_02819.1, huMAP3_07653.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S1. The protein encoded by this gene belongs to the complex I 75 kDa subunit family. Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Thi…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 5 (0.810); mitochondrial complex I deficiency (0.647); type 2 diabetes mellitus (0.608); Parkinson disease (0.603); diabetes mellitus (0.580)
- **Europe PMC papers**: 2567
- **Why important**: NDUFS1 is a highly connected complex-I core subunit and belongs to the recurring hu.MAP complex-I groupings (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1) (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_07653.1). It has extensive STRING relationships with complex-I components, SDHA, ATP synthase, cytochrome-c oxidase, TCA enzymes, and pyruvate-dehydrogenase-related genes. It is annotated for NADH-to-ubiquinone electron transfer, respiratory-chain assembly, and ATP synthesis. HPA shows enhancement in heart muscle and skeletal muscle with protein detection in both module tissues. Its disease associations include complex-I deficiency, diabetes, and Parkinson disease, with a substantial literature base.
- **Conclusion**: Established evidence identifies NDUFS1 as a core respiratory-chain component and a bridge between the complex-I subnetwork and the wider oxidative-energy program. Its centrality supports a coordinated respiratory interpretation, while the network does not establish a tissue-specific pathogenic role.

#### NDUFS2

- **Related proteins** (co-abundance neighbors): ATP5F1C (0.87), NDUFA9 (0.86), SDHA (0.85), NDUFS1 (0.84), CS (0.82), AIFM1 (0.82), UQCRC2 (0.81); STRING partners: ACO2 (0.955), ATP5F1A (0.98), ATP5F1C (0.95), ATP5PB (0.85), CS (0.772), DLAT (0.713), GOT2 (0.802), IMMT (0.735), MT-CO2 (0.985), NDUFA10 (0.999), NDUFA9 (0.999), NDUFS1 (0.999), NDUFV1 (0.999), SDHA (0.998), SUCLA2 (0.837), SUCLG1 (0.916), SUCLG2 (0.8), UQCRC2 (0.994)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1, huMAP3_08132.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S2. The protein encoded by this gene is a core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (complex I). Mammalian mitochondrial complex I is composed of at least 43 different subunits, 7 of which are encoded by the mitochondrial genome, and the rest are the products of nuclear genes. The iron-sulfur protein fraction of complex I is made up of 7 subunits, including this g…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.758); mitochondrial complex I deficiency, nuclear type 6 (0.665); type 2 diabetes mellitus (0.608); mitochondrial disease (0.596); Parkinson disease (0.588)
- **Europe PMC papers**: 1723
- **Why important**: NDUFS2 is a connected complex-I core subunit with especially broad STRING support across TCA, respiratory-chain, ATP-synthase, and membrane-associated genes. It recurs in the high-confidence hu.MAP complex-I groupings (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1) and (hu.MAP huMAP3_08132.1), and it contributes to many globally corrected terms covering mitochondrial respiration, oxidative phosphorylation, proton-motive-force-driven ATP synthesis, and respiratory complexes. HPA shows tissue enhancement in skeletal muscle and tongue and detects the protein in heart, although not in prostate. Its established associations include complex-I deficiency, Leigh syndrome, diabetes, and Parkinson disease.
- **Conclusion**: Established evidence supports NDUFS2 as a strong molecular representative of the complex-I portion of the module. The lack of prostate protein detection in HPA cautions against assuming uniform protein-level behavior across the two tissues, but does not negate the transcript or co-abundance signal.

#### PDHB

- **Related proteins** (co-abundance neighbors): NDUFA10 (0.89), ETFA (0.83), ETFDH (0.83), IMMT (0.81), SUCLA2 (0.80), NDUFS1 (0.80), ACO2 (0.80); STRING partners: ATP5F1A (0.81), ATP5F1C (0.913), CS (0.941), DBT (0.957), DLAT (0.999), ETFA (0.728), NDUFA9 (0.733), NDUFS1 (0.809), NDUFV1 (0.738), SDHA (0.731), SUCLA2 (0.921), SUCLG1 (0.821), UQCRC2 (0.905)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, prostate
- **hu.MAP 3.0**: huMAP3_12248.1, huMAP3_04919.1, huMAP3_08216.1, huMAP3_07514.1, huMAP3_09761.1, huMAP3_10899.1, huMAP3_10412.1, huMAP3_14339.1, huMAP3_11877.1, huMAP3_14864.1
- **Function (MyGene.info)**: pyruvate dehydrogenase E1 subunit beta. The pyruvate dehydrogenase (PDH) complex is a nuclear-encoded mitochondrial multienzyme complex that catalyzes the overall conversion of pyruvate to acetyl-CoA and carbon dioxide, and provides the primary link between glycolysis and the tricarboxylic acid (TCA) cycle. The PDH complex is composed of multiple copies of three enzymatic components: pyruvate dehydrogenase (E1), dihydrolipoamide acetylt…
- **Diseases (Open Targets)**: pyruvate dehydrogenase E1-beta deficiency (0.796); pyruvate decarboxylase deficiency (0.672); pyruvate dehydrogenase phosphatase deficiency (0.421); neurodegenerative disease (0.392); hereditary disease (0.190)
- **Europe PMC papers**: 3002
- **Why important**: PDHB connects glycolytic pyruvate entry to mitochondrial acetyl-CoA production and the TCA cycle. It is highly connected to DLAT, DBT, TCA enzymes, respiratory proteins, and ATP-synthase components in STRING, and it participates in the hu.MAP pyruvate-dehydrogenase groupings (hu.MAP huMAP3_12248.1), (hu.MAP huMAP3_04919.1) (hu.MAP huMAP3_08216.1) (hu.MAP huMAP3_07514.1) (hu.MAP huMAP3_09761.1) (hu.MAP huMAP3_10899.1) (hu.MAP huMAP3_10412.1) (hu.MAP huMAP3_14339.1) (hu.MAP huMAP3_11877.1) (hu.MAP huMAP3_14864.1). It contributes to globally corrected energy, respiration, metabolic-pathway, and TCA-cycle terms (6 globally significant GO/KEGG terms, q_global 6.67e-08–1.58e-05; see the table), (KEGG Metabolic pathways - Homo sapiens (human); q_global = 0.000179), (KEGG Diabetic cardiomyopathy - Homo sapiens (human); q_global = 0.00144), (4 globally significant GO/KEGG terms, q_global 0.00257–0.00405; see the table), (GO:BP purine-containing compound biosynthetic process; q_global = 0.00786), (GO:BP tricarboxylic acid cycle; q_global = 0.0121), (GO:BP nucleoside phosphate biosynthetic process; q_global = 0.0127), (GO:BP purine-containing compound metabolic process; q_global = 0.024), (GO:BP nucleoside phosphate metabolic process; q_global = 0.0278), and (GO:BP nucleobase-containing small molecule metabolic process; q_global = 0.0484). HPA detects the protein in both tissues, and its disease associations include pyruvate-dehydrogenase E1-beta deficiency and related metabolic disease. Its literature base is substantial.
- **Conclusion**: Established evidence supports PDHB as the module component that links carbohydrate-derived carbon to mitochondrial oxidation. The module is compatible with coordinated pyruvate utilization, but co-abundance alone cannot determine whether pyruvate oxidation, fatty-acid oxidation, or another substrate is dominant in either tissue.

#### ACADVL

- **Related proteins** (co-abundance neighbors): GOT2 (0.91), ACSL1 (0.87), MAOA (0.83), SDHA (0.82), AIFM1 (0.82); STRING partners: ACADM (0.713), ACSL1 (0.841), ETFA (0.877), ETFDH (0.817), HADHB (0.988), HSDL2 (0.787)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA dehydrogenase very long chain. The protein encoded by this gene is targeted to the inner mitochondrial membrane where it catalyzes the first step of the mitochondrial fatty acid beta-oxidation pathway. This acyl-Coenzyme A dehydrogenase is specific to long-chain and very-long-chain fatty acids. A deficiency in this gene product reduces myocardial fatty acid beta-oxidation and is associated with cardiomyopathy. Alternative splic…
- **Diseases (Open Targets)**: very long chain acyl-CoA dehydrogenase deficiency (0.865); hereditary disease (0.531); long chain acyl-CoA dehydrogenase deficiency (0.506); rhabdomyolysis (0.464); Acute rhabdomyolysis (0.436)
- **Europe PMC papers**: 3504
- **Why important**: ACADVL provides the long-chain fatty-acid oxidation arm of the module and is connected to ACADM, ACSL1, ETFA, ETFDH, HADHB, and respiratory metabolism. It contributes to the mitochondrial, energy-derivation, metabolic-pathway, and fatty-acid-related primary terms (GO:CC mitochondrion; q_global = 6.67e-08) (GO:BP energy derivation by oxidation of organic compounds; q_global = 2.74e-07) (GO:BP generation of precursor metabolites and energy; q_global = 9.27e-07), (4 globally significant GO/KEGG terms, q_global 1.58e-05–0.000179; see the table), (GO:CC mitochondrial inner membrane; q_global = 0.000414), (GO:CC organelle inner membrane; q_global = 0.000519), (GO:CC organelle envelope; q_global = 0.000958), and (GO:BP small molecule metabolic process; q_global = 0.00336). HPA identifies mitochondrial localization, cardiomyocyte enhancement, and protein detection in both tissues. Its established disease association with very-long-chain acyl-CoA dehydrogenase deficiency and cardiomyopathy is particularly relevant to heart biology, and it has a substantial literature base.
- **Conclusion**: Established evidence supports ACADVL as a substrate-oxidation component that broadens the module beyond respiratory-chain subunits. Its presence supports a hypothesis of coordinated lipid and carbohydrate fuel oxidation, but does not establish that fatty acids are the principal fuel in prostate or heart samples.

#### IMMT

- **Related proteins** (co-abundance neighbors): SDHA (0.85), NDUFS1 (0.84), PDHB (0.81), UQCRC2 (0.81), ETFA (0.80); STRING partners: ATP5F1A (0.809), NDUFA9 (0.747), NDUFS1 (0.901), NDUFS2 (0.735), UQCRC2 (0.811)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inner membrane mitochondrial protein. Enables RNA binding activity. Involved in cristae formation. Located in mitochondrial inner membrane. Part of MICOS complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); multinodular goiter (0.196); alcohol drinking (0.190); breast cancer (0.094); neoplasm (0.087)
- **Europe PMC papers**: 933
- **Why important**: IMMT is a mitochondrial inner-membrane and MICOS-complex component involved in cristae formation. Although its direct module connectivity is more selective, it connects to SDHA, NDUFS1, NDUFS2, UQCRC2, ATP5F1A, and other respiratory proteins in STRING. It contributes to the mitochondrial membrane and inner-membrane primary terms (GO:CC mitochondrion; q_global = 6.67e-08), (GO:CC mitochondrial membrane; q_global = 3.68e-05), (GO:CC mitochondrial envelope; q_global = 0.000163), (GO:CC mitochondrial inner membrane; q_global = 0.000414), (GO:CC organelle inner membrane; q_global = 0.000519), and (GO:CC organelle envelope; q_global = 0.000958), and HPA detects the protein in heart. Its annotation supplies structural context for the respiratory and ATP-synthesis machinery rather than representing another soluble metabolic enzyme.
- **Conclusion**: Established evidence supports IMMT as a plausible structural organizer linking mitochondrial architecture with respiratory-chain abundance. The hypothesis that IMMT-mediated cristae organization explains part of the shared co-abundance pattern remains untested in this module.

## Module 2

**Tissue pair**: heart and prostate  
**Genes (21)**: ABHD11, CLTC, CTNNA1, EIF3L, FKBP4, SHMT2, HNRNPK, IMPDH2, MATR3, DDOST, PNP, PSMC4, PSMA1, PSMB3, PSMD13, FARSB, KARS1, RARS1, CCT5, CCT3, CCT8

### Function

The module is best interpreted as a broadly conserved intracellular protein-homeostasis and gene-expression module. The primary evidence is enrichment for intracellular protein-containing complexes (GO:CC intracellular protein-containing complex; q_global = 0.00384) and macromolecule metabolic process (GO:BP macromolecule metabolic process; q_global = 0.031). Its genes represent several connected cellular activities: CCT3, CCT5, and CCT8 support chaperonin-mediated protein folding; PSMA1, PSMB3, PSMC4, and PSMD13 represent proteasome machinery; RARS1, KARS1, and FARSB support aminoacyl-tRNA charging; EIF3L supports translation initiation; HNRNPK and MATR3 support RNA processing; and SHMT2, IMPDH2, and PNP support metabolic pathways. The network therefore appears to capture coordinated abundance of protein synthesis, folding, quality control, RNA handling, and intermediary metabolism rather than a narrowly tissue-specific pathway. The STRING RNA-binding and protein-metabolism categories (STRING Function RNA binding; within-query FDR = 0.0052) and (STRING RCTM Metabolism of proteins; within-query FDR = 0.0069) are consistent with this interpretation, while the tissue-category results (STRING TISSUES Carcinoma cell; within-query FDR = 0.009), (STRING TISSUES Adenocarcinoma cell; within-query FDR = 0.0141), (STRING TISSUES Lymphoblast; within-query FDR = 0.0323), and (STRING TISSUES Lymphocyte; within-query FDR = 0.0323) should be treated as supplementary context rather than primary global enrichment evidence.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: HPA identifies only a single secreted gene, and the proteins are largely intracellular, with cytosolic, nuclear, mitochondrial, endosomal, or endoplasmic-reticulum localizations. The module is broadly expressed by tissue according to HPA, with most genes having low tissue specificity, and its proteins are detected in both heart and prostate for many members. HPA reports low immune-cell specificity across the module and no recurring blood-cell enrichment, so a blood-cell explanation is not supported by this evidence. The cell-type-enhanced annotations are heterogeneous and include reproductive, epithelial, trophoblast, megakaryocyte, and other cell types; this argues for a general cellular-state or protein-handling signal rather than a coherent infiltrating blood-cell population. The absence of protein detection for some genes in either tissue also cautions against assuming that every transcript-level co-abundance relationship reflects abundant protein in both organs.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC intracellular protein-containing complex | 0.00384 | CCT3, CCT5, CCT8, KARS1, PSMA1, PSMB3, PSMC4, PSMD13, RARS1 |
| GO:BP macromolecule metabolic process | 0.031 | CCT3, CCT5, CCT8, CLTC, DDOST, EIF3L, FARSB, FKBP4, HNRNPK, KARS1, MATR3, PNP, PSMA1, PSMB3, PSMC4, PSMD13, RARS1, SHMT2 |

### STRING and hu.MAP

Several parts of the module reproduce well-known physical or functional assemblies. STRING strongly connects the CCT3-CCT5-CCT8 chaperonin subgroup, the proteasome-related PSMA1-PSMB3-PSMC4-PSMD13 subgroup, and the aminoacyl-tRNA synthetase relationships involving RARS1, KARS1, and FARSB. HNRNPK-MATR3 and IMPDH2-PNP are also represented by high-confidence STRING relationships. hu.MAP independently places the proteasome genes in multiple proteasome complexes (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1), (hu.MAP huMAP3_05064.1), and (hu.MAP huMAP3_00356.1), the CCT genes in several chaperonin complexes (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_01951.1), the synthetases in aminoacylation complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), and HNRNPK with MATR3 in an RNA-binding complex (hu.MAP huMAP3_10625.1). These concordant annotations show that substantial parts of the module reflect established molecular complexes. The remaining cross-complex links are less directly established by STRING or hu.MAP and may represent shared cellular demand, indirect regulation, or co-abundance driven by common cell state rather than one physical megacomplex.

**STRING interactions (score >= 0.7)**: 15 of 210 gene pairs: CCT3–CCT5 (0.999); CCT3–CCT8 (0.999); CCT5–CCT8 (0.999); CCT8–PSMA1 (0.797); FARSB–KARS1 (0.813); FARSB–RARS1 (0.706); HNRNPK–MATR3 (0.923); IMPDH2–PNP (0.753); KARS1–RARS1 (0.999); PSMA1–PSMB3 (0.999); PSMA1–PSMC4 (0.999); PSMA1–PSMD13 (0.999); PSMB3–PSMC4 (0.999); PSMB3–PSMD13 (0.999); PSMC4–PSMD13 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function RNA binding (FDR = 0.0052, 14 genes); RCTM Metabolism of proteins (FDR = 0.0069, 13 genes); TISSUES Carcinoma cell (FDR = 0.009, 10 genes); TISSUES Adenocarcinoma cell (FDR = 0.0141, 9 genes); RCTM PCP/CE pathway (FDR = 0.0318, 5 genes); RCTM Infectious disease (FDR = 0.0318, 9 genes); TISSUES Lymphoblast (FDR = 0.0323, 8 genes); TISSUES Lymphocyte (FDR = 0.0323, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09656.1 (PSMA1, PSMC4, PSMB3, PSMD13; 4/64); huMAP3_13725.1 (PSMA1, PSMC4, PSMB3, PSMD13; 4/69); huMAP3_07938.1 (CCT5, CCT3, CCT8; 3/23); huMAP3_06559.1 (CCT5, CCT3, CCT8; 3/25); huMAP3_09191.1 (CCT5, CCT3, CCT8; 3/32); huMAP3_10656.1 (CCT5, CCT3, CCT8; 3/36); huMAP3_14584.1 (CCT5, CCT3, CCT8; 3/61); huMAP3_01951.1 (CCT5, CCT3; 2/8); huMAP3_02637.1 (RARS1, KARS1; 2/14); huMAP3_13688.1 (RARS1, KARS1; 2/14); huMAP3_05064.1 (PSMC4, PSMD13; 2/31); huMAP3_00356.1 (PSMA1, PSMB3; 2/33); huMAP3_10625.1 (MATR3, HNRNPK; 2/57)

### Novelty

The module as a whole should not be claimed as a newly discovered molecular complex. Its strongest cores are already known: the CCT chaperonin, the proteasome, aminoacyl-tRNA synthetase assemblies, and the HNRNPK-MATR3 RNA-related association are supported by STRING and hu.MAP. The potentially novel aspect is the conserved co-abundance of these otherwise distinct systems across heart and prostate, especially the observed wiring between chaperoning, translation, proteasomal turnover, RNA processing, and metabolism. However, absence of a complete matching entry in STRING or hu.MAP would not establish novelty, because co-abundance can reflect indirect coordination and database coverage is incomplete. A defensible conclusion is that this is a potentially informative cross-complex co-abundance pattern, not demonstrated evidence of a new complex or a new biological pathway.

**Hypothesis.** Hypothesis: heart and prostate cells coordinate a shared proteostasis-and-biosynthetic state in which increased demand for protein production is coupled to chaperonin folding, proteasomal quality control, RNA processing, aminoacyl-tRNA charging, and nucleotide or one-carbon metabolism. The central CCT and proteasome subgroups could buffer newly synthesized or damaged proteins, while EIF3L, the synthetases, HNRNPK, MATR3, SHMT2, IMPDH2, and PNP could provide translational, RNA, and metabolic support. This model predicts that module activity should track cellular protein-turnover and biosynthetic load rather than a heart-specific or prostate-specific function. It remains a hypothesis because co-abundance does not establish physical interaction, directionality, or causal regulation.

### Important genes

#### CCT3

- **Related proteins** (co-abundance neighbors): EIF3L (0.91), CCT8 (0.90), RARS1 (0.87), FARSB (0.85), CCT5 (0.85), SHMT2 (0.83), IMPDH2 (0.82); STRING partners: CCT5 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in heart, prostate
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a highly connected central member of the module and is part of the tightly linked CCT3-CCT5-CCT8 subgroup in STRING. It belongs to multiple hu.MAP chaperonin complexes (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_01951.1) and contributes to both primary terms (GO:CC intracellular protein-containing complex; q_global = 0.00384) and (GO:BP macromolecule metabolic process; q_global = 0.031). Its established function is as a subunit of the CCT chaperonin that folds proteins including actin and tubulin. It is detected in both heart and prostate, has broad tissue distribution, and has substantial literature support, including disease associations involving neurodevelopmental and neurodegenerative phenotypes.
- **Conclusion**: Established: CCT3 is a core marker of the module's conserved protein-folding machinery and is supported by network, complex, localization, and enrichment evidence. Hypothesis: variation in CCT3 abundance may help organize the broader cross-complex proteostasis signal, but the module does not demonstrate that CCT3 controls the other systems.

#### PSMA1

- **Related proteins** (co-abundance neighbors): CCT5 (0.87), RARS1 (0.84), PSMD13 (0.82); STRING partners: CCT8 (0.797), PSMB3 (0.999), PSMC4 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, prostate
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1, huMAP3_00356.1
- **Function (MyGene.info)**: proteasome 20S subunit alpha 1. The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent proc…
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.535); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1417
- **Why important**: PSMA1 anchors the proteasome component of the module and has strong STRING relationships with PSMB3, PSMC4, and PSMD13. It occurs in several hu.MAP proteasome complexes (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1), and (hu.MAP huMAP3_00356.1) and contributes to both primary terms (GO:CC intracellular protein-containing complex; q_global = 0.00384) and (GO:BP macromolecule metabolic process; q_global = 0.031). Its established role is as an alpha subunit of the twenty-six S proteasome, supporting ubiquitin-dependent protein degradation, protein quality control, DNA repair, and apoptotic processes. It is detected in both tissues and has extensive literature and disease associations involving plasma-cell malignancy, lymphoma, neoplasia, infection, and amyloidosis.
- **Conclusion**: Established: PSMA1 provides strong evidence that proteasomal turnover is a genuine component of the module rather than an annotation artifact. Hypothesis: coordinated PSMA1 abundance may reflect increased protein-quality-control demand in both tissues, but it cannot by itself establish altered proteasome activity.

#### RARS1

- **Related proteins** (co-abundance neighbors): CCT5 (0.92), EIF3L (0.90), PSMD13 (0.88), CCT3 (0.87), PSMC4 (0.86), CTNNA1 (0.85), FARSB (0.85), MATR3 (0.84), PSMA1 (0.84), SHMT2 (0.83); STRING partners: FARSB (0.706), KARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 has high network connectivity and links the chaperonin, proteasome, RNA-associated, and aminoacylation portions of the module. It contributes to both primary terms (GO:CC intracellular protein-containing complex; q_global = 0.00384) and (GO:BP macromolecule metabolic process; q_global = 0.031), forms strong STRING relationships with KARS1 and FARSB, and occurs in hu.MAP aminoacylation complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Its established function is arginyl-tRNA aminoacylation, a direct requirement for accurate protein translation. It is detected in prostate, has a broad tissue profile, and is associated with hypomyelinating leukodystrophy and related hereditary disease phenotypes.
- **Conclusion**: Established: RARS1 is a plausible bridge between translation capacity and the module's folding and degradation systems. Hypothesis: RARS1 may report coordinated translational load across heart and prostate, although the co-abundance data do not show that it drives proteostasis.

#### SHMT2

- **Related proteins** (co-abundance neighbors): IMPDH2 (0.90), CCT8 (0.86), ABHD11 (0.85), EIF3L (0.84), CCT3 (0.83), RARS1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine hydroxymethyltransferase 2. This gene encodes the mitochondrial form of a pyridoxal phosphate-dependent enzyme that catalyzes the reversible reaction of serine and tetrahydrofolate to glycine and 5,10-methylene tetrahydrofolate. The encoded product is primarily responsible for glycine synthesis. The activity of the encoded protein has been suggested to be the primary source of intracellular glycine. The gene which encodes th…
- **Diseases (Open Targets)**: neurodevelopmental disorder with cardiomyopathy, spasticity, and brain abnormalities (0.771); microcephaly (0.370); polymicrogyria (0.370); neurodevelopmental disorder (0.336); hereditary disease (0.192)
- **Europe PMC papers**: 2579
- **Why important**: SHMT2 connects the CCT subgroup with IMPDH2, EIF3L, and other module members, and contributes to the primary macromolecule-metabolism term (GO:BP macromolecule metabolic process; q_global = 0.031). Its established mitochondrial function is reversible serine and tetrahydrofolate metabolism, supporting glycine production and one-carbon metabolism, with links to oxidative phosphorylation. HPA reports tissue enhancement in liver and detection in prostate, while Open Targets associates it with neurodevelopmental disorders including cardiomyopathy and spasticity. Its literature volume is substantial, indicating that it is a well-studied metabolic gene rather than an uncharacterized connector.
- **Conclusion**: Established: SHMT2 supplies a credible metabolic dimension to a module otherwise dominated by protein handling and gene-expression machinery. Hypothesis: mitochondrial one-carbon metabolism may support the biosynthetic demand represented by the module, but the available evidence does not establish metabolic control of the network.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): DDOST (0.88), CCT8 (0.88), MATR3 (0.82); STRING partners: MATR3 (0.923)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, prostate
- **hu.MAP 3.0**: huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK links CCT8 and DDOST with MATR3 and is part of the RNA-binding STRING category (STRING Function RNA binding; within-query FDR = 0.0052). Its HNRNPK-MATR3 relationship is strongly supported by STRING, and both genes occur together in hu.MAP complex (hu.MAP huMAP3_10625.1). Its established role is in heterogeneous nuclear RNA binding, pre-mRNA processing, RNA transport, and transcriptional regulation. It is detected in both heart and prostate, has low tissue and immune specificity, and has extensive literature with disease associations including Au-Kline syndrome and neurodevelopmental disorders.
- **Conclusion**: Established: HNRNPK supports interpretation of the module as involving RNA handling in addition to protein folding and degradation. Hypothesis: HNRNPK may coordinate RNA-processing demand with translation and proteostasis, but this proposed coordination requires experimental validation.

## Module 3

**Tissue pair**: heart and prostate  
**Genes (5)**: AGK, MMAB, NDUFAF4, PNPT1, IARS2

### Function

The module is most consistent with a mitochondrial maintenance and metabolic-support program rather than a narrowly defined pathway. Every member is annotated as mitochondrial, and the genes collectively represent mitochondrial translation and translational fidelity (IARS2), mitochondrial RNA processing and turnover (PNPT1), mitochondrial membrane lipid metabolism (AGK), cobalamin activation for methylmalonyl-CoA metabolism (MMAB), and respiratory-chain complex I assembly (NDUFAF4). However, no GO or KEGG term passed global correction, so this functional interpretation is based on the concordant gene annotations and network context, not on statistically significant enrichment. The co-abundance pattern may therefore reflect coordinated mitochondrial abundance or state rather than a single discrete biochemical pathway.

**Cell composition.** The module does not appear to be composed of plasma or secreted proteins: the secreted-gene annotation is absent for every member. Protein was detected in both heart muscle and prostate for every gene, supporting biological detectability in both tissues. Most genes have low tissue specificity and low immune-cell specificity, arguing against a module driven primarily by blood contamination or a broadly prominent immune-cell population. One gene, MMAB, is tissue-enhanced in liver, while several genes show cell-type-enhanced patterns in distinct cell types; these isolated enrichments do not establish a shared liver, epithelial, oocyte, or NK-cell origin. Overall, the composition is more compatible with a conserved intracellular mitochondrial program present in multiple cell types than with a secreted or blood-cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes, and STRING provides no supplementary functional enrichment. Thus, the co-abundance relationships are not corroborated by the examined STRING interaction network and should not be interpreted as established direct physical interactions. hu.MAP provides one relevant complex, (hu.MAP huMAP3_13468.1), containing PNPT1 and IARS2 together with many additional mitochondrial and metabolic proteins. This supports a connection between mitochondrial RNA handling and mitochondrial translation within a broader mitochondrial proteome context, but the large and heterogeneous complex membership does not demonstrate that all module genes form one physical complex. AGK, MMAB, and NDUFAF4 have no reported hu.MAP membership in the supplied evidence.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (PNPT1, IARS2; 2/99)

### Novelty

This module may represent a new co-abundance association rather than a newly discovered molecular complex or pathway. Its novelty is supported by the absence of high-confidence STRING links and by the limited overlap with the supplied hu.MAP evidence, but those absences alone cannot establish novelty because interaction databases are incomplete and co-abundance can reflect shared regulation, organelle abundance, cell composition, or indirect physiology. The strongest defensible claim is that the coordinated heart–prostate abundance pattern involving these particular mitochondrial functions is not explained by an already documented STRING interaction network in the supplied data. Independent replication, tissue-aware controls, and comparison with published co-expression or proteomic modules would be needed before calling it a genuinely new biological mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated mitochondrial quality and metabolic capacity in heart and prostate cells. Mitochondrial RNA processing by PNPT1 and mitochondrial translation by IARS2 could support production of respiratory-chain components; NDUFAF4 could support complex I assembly; AGK could couple mitochondrial membrane lipid metabolism to organelle maintenance; and MMAB could support mitochondrial propionate and cobalamin-dependent metabolism. In this model, the genes co-vary because mitochondrial gene expression, membrane integrity, respiratory-chain assembly, and metabolic throughput are jointly regulated. This is a mechanistic hypothesis, not an established interaction model, because the module lacks globally significant GO or KEGG enrichment and high-confidence STRING links.

### Important genes

#### IARS2

- **Related proteins** (co-abundance neighbors): PNPT1 (0.86), NDUFAF4 (0.86), AGK (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, prostate
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 2, mitochondrial. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Two forms of isoleucine-tRNA synthetase exist, a cytoplasmic form and a mitochondrial form. This gene encodes th…
- **Diseases (Open Targets)**: cataract-growth hormone deficiency-sensory neuropathy-sensorineural hearing loss-skeletal dysplasia syndrome (0.724); Leigh syndrome (0.563); hereditary disease (0.416); neurodegenerative disease (0.411); mitochondrial disease (0.374)
- **Europe PMC papers**: 411
- **Why important**: IARS2 is the most connected node in the module and links PNPT1, NDUFAF4, and AGK in the supplied network. It encodes mitochondrial isoleucine-tRNA synthetase and is annotated for mitochondrial translation, aminoacylation, and translational fidelity. Its mitochondrial disease associations and substantial literature support make it a strong anchor for interpreting the module as a mitochondrial gene-expression program.
- **Conclusion**: Established evidence supports IARS2 as a central network component involved in mitochondrial translation and associated mitochondrial disease. It is plausible, but not proven, that IARS2 is a functional coordinator of the module; co-abundance and network position do not establish direct regulation of its neighbors.

#### PNPT1

- **Related proteins** (co-abundance neighbors): IARS2 (0.86), MMAB (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, prostate
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: polyribonucleotide nucleotidyltransferase 1. The protein encoded by this gene belongs to the evolutionary conserved polynucleotide phosphorylase family comprised of phosphate dependent 3'-to-5' exoribonucleases implicated in RNA processing and degradation. This enzyme is predominantly localized in the mitochondrial intermembrane space and is involved in import of RNA to mitochondria. Mutations in this gene have been associated with combined …
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 13 (0.807); autosomal recessive nonsyndromic hearing loss 70 (0.740); spinocerebellar ataxia type 25 (0.709); deafness (0.676); hearing loss, autosomal recessive (0.634)
- **Europe PMC papers**: 839
- **Why important**: PNPT1 is connected to IARS2 and MMAB and is one of the two module members represented in hu.MAP complex (hu.MAP huMAP3_13468.1). It participates in mitochondrial RNA import, processing, and degradation, providing a mechanistic bridge between mitochondrial RNA handling and translation. Its associations with combined oxidative-phosphorylation deficiency and inherited hearing disorders add disease relevance.
- **Conclusion**: Established evidence supports PNPT1 as a mitochondrial RNA-processing factor and as part of the broader hu.MAP context represented by (hu.MAP huMAP3_13468.1). A role in coordinating the observed module is a hypothesis; the supplied data do not show that PNPT1 physically binds the other module genes.

#### AGK

- **Related proteins** (co-abundance neighbors): MMAB (0.85), IARS2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acylglycerol kinase. The protein encoded by this gene is a mitochondrial membrane protein involved in lipid and glycerolipid metabolism. The encoded protein is a lipid kinase that catalyzes the formation of phosphatidic and lysophosphatidic acids. Defects in this gene have been associated with mitochondrial DNA depletion syndrome 10. [provided by RefSeq, Feb 2012].
- **Diseases (Open Targets)**: Sengers syndrome (0.812); cataract 38 (0.727); cancer (0.548); mitochondrial DNA depletion syndrome (0.504); hereditary disease (0.494)
- **Europe PMC papers**: 1476
- **Why important**: AGK connects IARS2 and MMAB in the module and encodes a mitochondrial membrane lipid kinase involved in glycerolipid, sphingosine, and ceramide biosynthesis. Its association with Sengers syndrome and mitochondrial DNA depletion syndrome makes it relevant to mitochondrial membrane function and organelle integrity. It also has the largest literature volume among the module genes in the supplied evidence.
- **Conclusion**: Established evidence supports AGK as a mitochondrial membrane and lipid-metabolism protein with clinically important mitochondrial disease associations. Its placement may indicate coupling between lipid environment and mitochondrial translation or metabolism, but that coupling remains a hypothesis rather than a demonstrated molecular interaction.

#### MMAB

- **Related proteins** (co-abundance neighbors): AGK (0.85), PNPT1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: metabolism of cobalamin associated B. This gene encodes a protein that catalyzes the final step in the conversion of vitamin B(12) into adenosylcobalamin (AdoCbl), a vitamin B12-containing coenzyme for methylmalonyl-CoA mutase. Mutations in the gene are the cause of vitamin B12-dependent methylmalonic aciduria linked to the cblB complementation group. Alternatively spliced transcript variants have been found. [provided by RefSeq, Apr …
- **Diseases (Open Targets)**: methylmalonic aciduria cblb type (0.831); vitamin B12-responsive methylmalonic acidemia (0.556); methylmalonic acidemia (0.544); hereditary disease (0.494); neurodegenerative disease (0.476)
- **Europe PMC papers**: 808
- **Why important**: MMAB connects AGK and PNPT1 and is the only tissue-enhanced gene in the module, with liver enhancement in the HPA summary. It catalyzes formation of adenosylcobalamin, the coenzyme required by methylmalonyl-CoA mutase, and is linked to cobalamin-related methylmalonic aciduria. Its network position connects mitochondrial lipid-related and RNA-related components to mitochondrial intermediary metabolism.
- **Conclusion**: Established evidence supports MMAB as a mitochondrial cobalamin-activation enzyme with a clear metabolic and disease role. Its liver-enhanced profile may indicate metabolic specialization, but it does not show that the heart–prostate module is liver-derived or that MMAB mechanistically controls the other members.

#### NDUFAF4

- **Related proteins** (co-abundance neighbors): IARS2 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase complex assembly factor 4. NADH:ubiquinone oxidoreductase (complex I) catalyzes the transfer of electrons from NADH to ubiquinone (coenzyme Q) in the first step of the mitochondrial respiratory chain, resulting in the translocation of protons across the inner mitochondrial membrane. This gene encodes a complex I assembly factor. Mutations in this gene are a cause of mitochondrial complex I deficiency. [provided by RefSeq, O…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.714); type 2 diabetes mellitus (0.607); mitochondrial disease (0.597); diabetes mellitus (0.578); mitochondrial complex I deficiency, nuclear type 15 (0.568)
- **Europe PMC papers**: 378
- **Why important**: NDUFAF4 is connected to IARS2 and encodes a complex I assembly factor. It provides the clearest link in the module to respiratory-chain construction and oxidative phosphorylation, and it is associated with mitochondrial complex I deficiency. Although it is peripheral in the supplied network, its function is highly informative for the proposed mitochondrial respiratory-capacity interpretation.
- **Conclusion**: Established evidence supports NDUFAF4 as a factor in mitochondrial complex I assembly and as a disease-relevant mitochondrial protein. Its co-abundance with IARS2 is consistent with coordinated mitochondrial gene-expression and respiratory-chain capacity, but the module does not establish a direct NDUFAF4–IARS2 interaction.

## Module 4

**Tissue pair**: heart and prostate  
**Genes (5)**: ANXA4, ANXA6, CAP2, GSN, PARVA

### Function

The module is most consistent with a conserved actin-cytoskeleton and calcium-dependent membrane-regulation signal. CAP2 is the central co-abundance hub and is connected with PARVA, ANXA4, ANXA6, and GSN. The gene annotations support actin organization, focal-adhesion and cell-adhesion biology, membrane-associated calcium-dependent processes, and actin filament assembly or disassembly. This interpretation is based on the individual gene functions and the network structure, not on enrichment significance. No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The lack of an enriched term does not invalidate the co-abundance pattern.

**Cell composition.** The module does not appear to be predominantly plasma or secreted: only GSN is annotated as secreted to blood, while the other genes are not secreted. It is not strongly blood-cell-specific overall, although PARVA and GSN have immune-cell-enhanced associations and GSN is associated with eosinophils. The HPA profile instead points to a mixed cellular and tissue composition, including muscle-associated, epithelial or ductal, stromal, adipocyte, vascular, and other cell-type signals. CAP2 is tissue-enhanced in skeletal muscle and tongue and cell-type enriched in myonuclei; GSN is tissue-enhanced in heart muscle; ANXA4 is tissue-enhanced in gallbladder and pancreas; PARVA and ANXA6 have low tissue specificity. Protein detection is concordant for three genes in both heart and prostate, but CAP2 is detected in heart rather than prostate and ANXA4 is detected in prostate rather than heart, while GSN is not detected by IHC in either tissue. Therefore, the shared module could reflect conserved cytoskeletal biology in resident cells, shared stromal or vascular components, or sample-composition effects; the evidence does not establish a single cell source.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No pair among the module genes has a high-confidence STRING interaction in the supplied results, and STRING reports no supplementary functional-enrichment terms. No hu.MAP complex contains at least two module members. Thus, the co-abundance relationships are not corroborated here as established physical interactions or as membership in a known hu.MAP complex. CAP2 connects to every other module gene in the inferred co-abundance subgraph, whereas the remaining genes are peripheral; this supports a coordinated expression or abundance program but does not by itself prove direct molecular binding. The known biology of the individual proteins provides functional coherence around actin, adhesion, membrane, and calcium-regulated processes, but the network should not be described as a validated protein complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a potentially interesting cross-tissue co-abundance pattern, but it cannot be called a definitively new biological mechanism. Its apparent novelty comes from the specific conserved grouping of CAP2, PARVA, ANXA4, ANXA6, and GSN in heart and prostate together with the absence of a matching high-confidence STRING interaction set or shared hu.MAP complex in the supplied resources. Those absences do not prove novelty: the pattern could reflect correlated abundance, cell composition, tissue handling, or incomplete database coverage. The appropriate conclusion is that the cross-tissue module is a candidate novel association requiring independent replication and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a conserved structural-response program in which CAP2 coordinates actin-cytoskeleton organization with focal-adhesion biology through PARVA, while ANXA4 and ANXA6 contribute calcium-dependent membrane and trafficking responses and GSN regulates actin filament turnover. In heart and prostate, this program may arise in shared contractile, stromal, epithelial, vascular, or other resident cell populations and may be modulated by tissue composition. This is a mechanistic hypothesis inferred from co-abundance and known individual functions, not an experimentally established pathway or direct interaction model.

### Important genes

#### CAP2

- **Related proteins** (co-abundance neighbors): PARVA (0.85), ANXA4 (0.84), ANXA6 (0.83), GSN (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Nucleoplasm, Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cyclase associated actin cytoskeleton regulatory protein 2. This gene was identified by its similarity to the gene for human adenylyl cyclase-associated protein. The function of the protein encoded by this gene is unknown. However, the protein appears to be able to interact with adenylyl cyclase-associated protein and actin. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: cardiomyopathy, dilated, 2I (0.639); hemorrhoid (0.403); familial isolated dilated cardiomyopathy (0.391); gastroduodenitis (0.320); pregnancy disorder (0.268)
- **Europe PMC papers**: 1667
- **Why important**: CAP2 is the central hub, connected with every other module member, and therefore is the strongest network-level anchor. Its supplied annotation links it to the actin cytoskeleton, cell morphogenesis, polarity, and signal transduction. It is tissue-enhanced in skeletal muscle and tongue and cell-type enriched in myonuclei, and it has cardiomyopathy associations in Open Targets. Its substantial literature volume also makes it comparatively well characterized.
- **Conclusion**: Established evidence supports CAP2 as the principal organizational marker of this co-abundance module and as a plausible link to actin and muscle-related biology. It is a reasonable candidate driver, but the network does not establish that CAP2 directly regulates the other proteins or causes the tissue-shared pattern.

#### PARVA

- **Related proteins** (co-abundance neighbors): CAP2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Actin filaments, Focal adhesion sites; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: parvin alpha. This gene encodes a member of the parvin family of actin-binding proteins. Parvins are associated with focal contacts and contain calponin homology domains that bind to actin filaments. The encoded protein is part of the integrin-linked kinase signaling complex and plays a role in cell adhesion, motility and survival. [provided by RefSeq, Dec 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.487); osteoarthritis, hip (0.339); total hip arthroplasty (0.339); open-angle glaucoma (0.337); Pancreatic pseudocyst (0.331)
- **Europe PMC papers**: 3949
- **Why important**: PARVA provides the module’s direct connection from the central hub to focal-adhesion and integrin-linked kinase biology. Its supplied annotation supports actin binding, cell adhesion, motility, survival, polarity, and actin-cytoskeleton organization. It is detected by IHC in both heart and prostate, and its cell-type associations include adipocytes, podocytes, smooth muscle cells, and other specialized populations.
- **Conclusion**: Established evidence supports PARVA as a plausible adhesion and cytoskeletal component of the module and as a useful bridge between CAP2-associated actin regulation and tissue architecture. The proposed role in the shared module remains an inference from co-abundance; no direct interaction with the other members is supported by the supplied STRING or hu.MAP results.

#### GSN

- **Related proteins** (co-abundance neighbors): CAP2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gelsolin. The protein encoded by this gene binds to the 'plus' ends of actin monomers and filaments to prevent monomer exchange. The encoded calcium-regulated protein functions in both assembly and disassembly of actin filaments. Defects in this gene are a cause of familial amyloidosis Finnish type (FAF). Multiple transcript variants encoding several different isoforms have been found for this gene. [provid…
- **Diseases (Open Targets)**: Finnish type amyloidosis (0.805); AL amyloidosis (0.463); neuropathy (0.418); cardiomyopathy (0.418); cutis laxa (0.417)
- **Europe PMC papers**: 5062
- **Why important**: GSN is a calcium-regulated actin assembly and disassembly protein and is the module member with the strongest direct connection to actin filament turnover in the supplied annotations. It is tissue-enhanced in heart muscle, has an immune-cell association with eosinophils, and is secreted to blood. It also has cardiomyopathy and amyloidosis associations and a large literature base.
- **Conclusion**: Established evidence supports GSN as a biologically important actin-remodeling component and as a possible contributor to the heart-related aspect of the module. Its blood secretion and lack of IHC detection in the two listed tissues raise a composition or circulating-protein alternative, so its presence should not automatically be interpreted as a resident-cell mechanism.

#### ANXA6

- **Related proteins** (co-abundance neighbors): CAP2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A6. Annexin VI belongs to a family of calcium-dependent membrane and phospholipid binding proteins. Several members of the annexin family have been implicated in membrane-related events along exocytotic and endocytotic pathways. The annexin VI gene is approximately 60 kbp long and contains 26 exons. It encodes a protein of about 68 kDa that consists of eight 68-amino acid repeats separated by linking …
- **Diseases (Open Targets)**: systemic lupus erythematosus (0.292); asthma (0.194); poisoning (0.193); stricture (0.193); neoplasm (0.115)
- **Europe PMC papers**: 1621
- **Why important**: ANXA6 contributes a membrane and calcium-regulated dimension distinct from the core actin annotations. Its supplied functions include calcium ion transport, transmembrane ion transport, mitochondrial calcium homeostasis, and apoptotic signaling. It is detected in both heart and prostate and has cell-type-enhanced associations spanning adipocytes, hepatic stellate cells, peritubular myoid cells, photoreceptor cells, and syncytiotrophoblasts.
- **Conclusion**: Established evidence supports ANXA6 as a plausible calcium-sensitive membrane-regulatory component that could couple cytoskeletal state to cellular stress or trafficking. Its mechanistic placement within this module is a hypothesis because no enriched GO or KEGG term, STRING interaction, or hu.MAP complex connects it directly to the other members.

#### ANXA4

- **Related proteins** (co-abundance neighbors): CAP2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A4. Annexin IV (ANX4) belongs to the annexin family of calcium-dependent phospholipid binding proteins. Although their functions are still not clearly defined, several members of the annexin family have been implicated in membrane-related events along exocytotic and endocytotic pathways. ANX4 has 45 to 59% identity with other members of its family and shares a similar size and exon-intron organization…
- **Diseases (Open Targets)**: atrial fibrillation (0.445); Abnormality of the skeletal system (0.385); dentures (0.301); neurodegenerative disease (0.268); placental abruption (0.235)
- **Europe PMC papers**: 1395
- **Why important**: ANXA4 adds a second calcium-dependent membrane-associated protein and is connected to CAP2 in the co-abundance graph. Its supplied annotation supports membrane-related events, epithelial differentiation, and regulation of inflammatory or apoptotic processes. It is tissue-enhanced in gallbladder and pancreas, cell-type enhanced in cholangiocytes and pancreatic duct cells, and detected in prostate but not heart.
- **Conclusion**: Established evidence supports ANXA4 as a membrane-associated and epithelial-context marker that may explain part of the module’s non-muscle composition. Its inclusion in a conserved heart-prostate module may reflect shared epithelial or other cellular abundance patterns rather than a direct CAP2-ANXA4 pathway; that distinction requires replication and cell-resolved testing.

## Module 5

**Tissue pair**: heart and prostate  
**Genes (11)**: APMAP, ASPH, ATP1A1, GPS1, HSD17B4, DNM1L, DYNC1H1, TSFM, NIPSNAP1, ATIC, SEC22B

### Function

The module does not have a statistically supported GO or KEGG functional enrichment: no globally significant GO/KEGG term passed global correction. STRING functional enrichment is also absent, so the module should not be assigned a single established pathway. Its genes nevertheless point to a heterogeneous cellular maintenance program involving plasma-membrane ion gradients and excitability through ATP1A1, mitochondrial translation through TSFM, mitochondrial and peroxisomal dynamics through TSFM and DNM1L, peroxisomal fatty-acid metabolism through HSD17B4, purine biosynthesis through ATIC, intracellular transport through DYNC1H1 and SEC22B, and calcium-related cellular regulation through ASPH. The sparse topology is compatible with coordinated abundance of several related aspects of cellular transport, organelle maintenance, metabolism, and membrane physiology, but it does not establish direct molecular cooperation.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not broadly uniform housekeeping biology, because most members are cell-type enhanced and several have tissue-enhanced profiles. Liver and hepatocyte signals recur, while neutrophil and neutrophil-progenitor annotations also recur; additional signals involve trophoblasts, adipocytes, kidney-related cells, and neural or retinal cells. Blood-cell specificity is generally low, with only limited immune-cell enhancement, so this is not a clearly blood-cell module. The mixed HPA pattern suggests that the heart–prostate association could partly reflect shared or variable cellular composition, stromal or immune admixture, or common metabolic and organelle states rather than a dedicated heart–prostate pathway. Protein detection is mixed between the tissues, which further argues for cautious interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair has a high-confidence STRING interaction in the supplied analysis, and no STRING functional enrichment is present. No hu.MAP complex contains multiple module members. Therefore, the co-abundance edges should be interpreted as statistical relationships in the tissue data, not as established physical interactions. The absence of STRING and hu.MAP support means that the module does not recapitulate a recognized protein complex. It does not exclude indirect regulation, tissue-composition effects, transient interactions, or proteins that are not well represented in those resources.

**STRING interactions (score >= 0.7)**: 0 of 55 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel cross-tissue co-abundance pattern, but it cannot be called a newly discovered biological mechanism from the present evidence alone. Its novelty is supported only in the limited sense that the specific module lacks corresponding STRING interactions, hu.MAP complexes, and enrichment support. Those databases are incomplete, and their absence is not proof of novelty. The heterogeneous annotations, sparse topology, and lack of globally significant enrichment make independent replication, adjustment for cell composition, and validation in additional heart and prostate cohorts essential before claiming a new conserved pathway.

**Hypothesis.** Hypothesis: the module captures a shared cellular state involving membrane transport and calcium-related physiology coupled to organelle quality control and lipid or purine metabolism. ATP1A1 and ASPH may represent membrane and calcium-regulatory features; TSFM and DNM1L may represent mitochondrial translation and organelle dynamics; HSD17B4 may represent peroxisomal lipid handling; and SEC22B and DYNC1H1 may reflect vesicle and intracellular cargo transport. A common metabolic or stress-related state in particular cell populations could produce the observed co-abundance pattern across heart and prostate. This hypothesis is not established by enrichment, physical-interaction, or complex evidence and should be tested with cell-type-resolved data, perturbation experiments, and independent cohorts.

### Important genes

#### ATP1A1

- **Related proteins** (co-abundance neighbors): APMAP (0.85), SEC22B (0.84), ASPH (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 is a central network node and connects the module to APMAP, SEC22B, and ASPH. Its established function is the sodium–potassium pump that maintains electrochemical gradients required for osmoregulation, coupled transport, and electrical excitability. It is detected in prostate, has membrane and vesicular localization, and has extensive literature and disease associations involving cardiac and neuromuscular phenotypes. Its hub position makes it an important indicator of the module's membrane-physiology component, although the co-abundance edges do not demonstrate direct interaction.
- **Conclusion**: Established evidence supports ATP1A1 as a membrane ion-gradient and excitability component with relevance to heart biology and disease. It is a plausible anchor for the module, but it is not established that ATP1A1 mechanistically coordinates the other members in this module.

#### TSFM

- **Related proteins** (co-abundance neighbors): ATIC (0.85), DNM1L (0.84), NIPSNAP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Ts translation elongation factor, mitochondrial. This gene encodes a mitochondrial translation elongation factor. The encoded protein is an enzyme that catalyzes the exchange of guanine nucleotides on the translation elongation factor Tu during the elongation step of mitchondrial protein translation. Mutations in this gene are associated with combined oxidative phosphorylation deficiency-3 syndrome. Alternate splicing results in multiple transcr…
- **Diseases (Open Targets)**: fatal mitochondrial disease due to combined oxidative phosphorylation defect type 3 (0.795); steroid-resistant nephrotic syndrome (0.474); hereditary disease (0.414); mitochondrial disease (0.372); neurodegenerative disease (0.370)
- **Europe PMC papers**: 484
- **Why important**: TSFM is a highly connected node linked to ATIC, DNM1L, and NIPSNAP1. It has a mitochondrial localization and an established role in mitochondrial translation elongation. Its disease associations include combined oxidative-phosphorylation deficiency and other mitochondrial phenotypes. Although its literature volume is more limited than that of ATP1A1 or ATIC, its network position and specific organelle function make it a strong candidate for connecting mitochondrial protein production with the broader module.
- **Conclusion**: Established evidence supports TSFM as a mitochondrial translation factor with disease relevance. Its connection to DNM1L suggests a possible relationship between mitochondrial protein synthesis and mitochondrial dynamics, but that relationship is a hypothesis from the co-abundance pattern rather than a demonstrated molecular mechanism.

#### DYNC1H1

- **Related proteins** (co-abundance neighbors): GPS1 (0.83), HSD17B4 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 1 heavy chain 1. Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polyp…
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy without contractures (0.816); intellectual disability, autosomal dominant 13 (0.815); Charcot-Marie-Tooth disease axonal type 2O (0.799); autosomal dominant non-syndromic intellectual disability (0.634); hereditary disease (0.545)
- **Europe PMC papers**: 1731
- **Why important**: DYNC1H1 is the cytoplasmic dynein heavy chain and links GPS1 with HSD17B4 in the module. Its established function includes microtubule-based movement, retrograde transport, organelle movement, and intracellular cargo distribution. It is detected in heart and has substantial literature and strong associations with axonal, motor, and intellectual-disability disorders. It provides a plausible transport axis connecting cellular logistics with organelle metabolism.
- **Conclusion**: Established evidence supports DYNC1H1 as a major intracellular transport motor. Its module association is consistent with coordinated transport of organelles or cargo, but there is no evidence here that it physically complexes with GPS1 or HSD17B4.

#### HSD17B4

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Peroxisomes; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydroxysteroid 17-beta dehydrogenase 4. The protein encoded by this gene is a bifunctional enzyme that is involved in the peroxisomal beta-oxidation pathway for fatty acids. It also acts as a catalyst for the formation of 3-ketoacyl-CoA intermediates from both straight-chain and 2-methyl-branched-chain fatty acids. Defects in this gene that affect the peroxisomal fatty acid beta-oxidation activity are a cause of D-bifunctional protein d…
- **Diseases (Open Targets)**: d-bifunctional protein deficiency (0.830); Perrault syndrome 1 (0.761); Perrault syndrome (0.736); hereditary disease (0.488); hearing loss disorder (0.370)
- **Europe PMC papers**: 1624
- **Why important**: HSD17B4 is linked to DYNC1H1 and is detected in both heart and prostate. It is a peroxisomal bifunctional enzyme involved in fatty-acid beta-oxidation and steroid-related metabolism, with well-established disease associations including D-bifunctional protein deficiency. Its tissue and hepatocyte annotations fit a metabolic component, while its connection to a transport motor raises the possibility that peroxisomal metabolism and intracellular positioning covary in the sampled tissues.
- **Conclusion**: Established evidence supports HSD17B4 as a peroxisomal lipid-metabolism enzyme with major inherited-disease relevance. The proposed connection between peroxisomal metabolism and dynein-dependent transport remains a hypothesis and is not validated by STRING, hu.MAP, or enrichment evidence.

#### ATIC

- **Related proteins** (co-abundance neighbors): TSFM (0.85), APMAP (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase. This gene encodes a bifunctional protein that catalyzes the last two steps of the de novo purine biosynthetic pathway. The N-terminal domain has phosphoribosylaminoimidazolecarboxamide formyltransferase activity, and the C-terminal domain has IMP cyclohydrolase activity. A mutation in this gene results in AICA-ribosiduria. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: AICA-ribosiduria (0.708); cancer (0.571); Intellectual disability (0.463); lung adenocarcinoma (0.390); anaplastic large cell lymphoma (0.374)
- **Europe PMC papers**: 5200
- **Why important**: ATIC is connected to TSFM and APMAP and encodes the bifunctional enzyme catalyzing the final steps of de novo purine biosynthesis. It has extensive literature and disease associations including AICA-ribosiduria and cancer-related annotations. Its presence gives the module a nucleotide-metabolism component and may reflect cellular biosynthetic demand rather than a tissue-specific pathway.
- **Conclusion**: Established evidence supports ATIC as a core purine-biosynthesis enzyme with substantial disease and literature support. Its co-abundance with mitochondrial and membrane-associated genes may indicate a shared cellular state of biosynthetic and energetic demand, but that interpretation is mechanistic speculation rather than an established module function.

## Module 6

**Tissue pair**: heart and prostate  
**Genes (5)**: MTHFD1, DNM2, LTA4H, SEPTIN9, USP5

### Function

The module does not have a globally significant GO or KEGG enrichment term. Its gene content instead suggests a mixed cellular program involving folate-dependent one-carbon metabolism through MTHFD1, cytoskeletal organization and membrane trafficking through SEPTIN9 and DNM2, ubiquitin-chain processing through USP5, and leukotriene and inflammatory mediator metabolism through LTA4H. The co-abundance structure links MTHFD1 to SEPTIN9, DNM2, and USP5, while USP5 links the metabolic component to LTA4H. This is better interpreted as a coordinated cellular-state signature than as evidence for one established pathway. The lack of enrichment does not invalidate the module, particularly because it is small and functionally heterogeneous.

**Cell composition.** The module is not dominated by secreted or plasma proteins: none of its genes are annotated as secreted. HPA indicates generally low tissue specificity for most genes, with MTHFD1 tissue enriched in liver. All genes show cell-type enhancement rather than a single coherent tissue-specific profile, including neutrophils, adipocytes, cardiomyocytes, epicardial cells, erythrocyte progenitors, urothelial cells, germ-cell-related cells, and several myeloid or epithelial populations. HPA reports low immune-cell specificity for every gene and no frequent enriched blood-cell category, so a blood-contamination explanation is not established. The broad expression pattern and detection in both heart and prostate support the possibility that the shared signal reflects broadly expressed cellular machinery or shared cell states rather than a heart-and-prostate-specific pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair reaches the stated high-confidence STRING threshold, and no STRING functional enrichment is reported. No hu.MAP complex contains at least two module members. Therefore, the observed co-abundance edges are not corroborated by the supplied high-confidence physical-interaction or complex resources. The absence of those relationships means the network may represent coordinated regulation, shared cellular context, indirect biology, or data-driven co-abundance rather than a known stable protein complex. Individual gene functions remain biologically interpretable, but the module-level connection among them is not established by these resources.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel co-abundance association, but it cannot be called a newly discovered molecular complex or pathway. The combination is not supported by the supplied STRING or hu.MAP evidence, and there is no globally significant GO or KEGG term. Those absences are compatible with novelty, but they do not prove it: the module is small, contains genes from several functional areas, and could reflect shared abundance regulation or cellular composition. The strongest defensible conclusion is that the heart–prostate co-abundance pattern is a potentially new systems-level observation requiring replication and targeted validation.

**Hypothesis.** Hypothesis: the module reflects a shared, broadly expressed cellular-state program in heart and prostate in which one-carbon metabolic capacity through MTHFD1 covaries with cytoskeletal and membrane-remodeling activity through SEPTIN9 and DNM2, while USP5 may coordinate protein-stability control and LTA4H may report or modulate an inflammatory or myeloid-associated state. The pattern could arise from coordinated regulation within resident cells, shared cellular stress or remodeling, or variation in cell-state composition across samples. This hypothesis predicts that the genes should covary across independent heart and prostate cohorts, while their protein abundances and relevant cell-type proportions should be tested separately to distinguish intracellular coordination from composition effects.

### Important genes

#### MTHFD1

- **Related proteins** (co-abundance neighbors): SEPTIN9 (0.82), DNM2 (0.81), USP5 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methylenetetrahydrofolate dehydrogenase, cyclohydrolase and formyltetrahydrofolate synthetase 1. This gene encodes a protein that possesses three distinct enzymatic activities, 5,10-methylenetetrahydrofolate dehydrogenase, 5,10-methenyltetrahydrofolate cyclohydrolase and 10-formyltetrahydrofolate synthetase. Each of these activities catalyzes one of three sequential reactions in the interconversion of 1-carbon derivatives of tetrahydrofolate, which are substrates for methionine, thymidylate, …
- **Diseases (Open Targets)**: combined immunodeficiency and megaloblastic anemia with or without hyperhomocysteinemia (0.773); severe combined immunodeficiency (0.473); neural tube defects, folate-sensitive (0.414); isolated spina bifida (0.376); atrial fibrillation (0.332)
- **Europe PMC papers**: 1939
- **Why important**: MTHFD1 is the most connected gene in the module and links to SEPTIN9, DNM2, and USP5. It encodes a trifunctional enzyme in folate-dependent one-carbon metabolism supplying substrates for methionine, thymidylate, and purine synthesis. Its HPA profile includes liver enrichment and enhancement in several cell types, including cardiomyocytes and epicardial cells. Its annotations include purine biosynthesis, sulfur amino acid metabolism, heart development, and clinically relevant immune-deficiency, anemia, neural-tube, and cardiac associations. The extensive literature base makes it the best biochemical anchor for the module.
- **Conclusion**: Established evidence supports MTHFD1 as a central metabolic gene with a prominent network position and broad cellular relevance. It is not established that MTHFD1 drives the other module genes; that regulatory interpretation remains a hypothesis.

#### DNM2

- **Related proteins** (co-abundance neighbors): SEPTIN9 (0.85), MTHFD1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 2. Dynamins represent one of the subfamilies of GTP-binding proteins. These proteins share considerable sequence similarity over the N-terminal portion of the molecule, which contains the GTPase domain. Dynamins are associated with microtubules. They have been implicated in cell processes such as endocytosis and cell motility, and in alterations of the membrane that accompany certain activities such …
- **Diseases (Open Targets)**: autosomal dominant centronuclear myopathy (0.844); Charcot-Marie-Tooth disease dominant intermediate B (0.830); fetal akinesia-cerebral and retinal hemorrhage syndrome (0.739); autosomal dominant Charcot-Marie-Tooth disease type 2M (0.715); centronuclear myopathy (0.692)
- **Europe PMC papers**: 2412
- **Why important**: DNM2 is directly connected to SEPTIN9 and MTHFD1 and has a strong network position. Dynamin two is a GTP-binding membrane-remodeling protein involved in endocytosis, vesicle transport, autophagy, cell motility, and cytoskeletal interactions. It is detected in both heart and prostate and is enhanced in neutrophils. Its disease associations include centronuclear and Charcot–Marie–Tooth myopathies and other neuromuscular disorders, and it has a substantial literature base. It provides a plausible link between cellular architecture, trafficking, and tissue remodeling.
- **Conclusion**: Established evidence supports DNM2 as a cytoskeletal and membrane-trafficking component that is relevant to heart and prostate samples. Its co-abundance with the metabolic and septin components may indicate a shared cellular state, but a direct functional relationship within this module is not demonstrated.

#### SEPTIN9

- **Related proteins** (co-abundance neighbors): DNM2 (0.85), MTHFD1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: septin 9. This gene is a member of the septin family involved in cytokinesis and cell cycle control. This gene is a candidate for the ovarian tumor suppressor gene. Mutations in this gene cause hereditary neuralgic amyotrophy, also known as neuritis with brachial predilection. A chromosomal translocation involving this gene on chromosome 17 and the MLL gene on chromosome 11 results in acute myelomonocytic l…
- **Diseases (Open Targets)**: neuralgic amyotrophy (0.564); hypertensive disorder (0.496); cataract (0.437); essential hypertension (0.426); alcohol drinking (0.420)
- **Europe PMC papers**: 748
- **Why important**: SEPTIN9 connects directly to DNM2 and MTHFD1 and is annotated for cytoskeleton organization, intracellular protein localization, cytokinesis, and cilium assembly. HPA places it at actin filaments, detects it in prostate, and reports enhancement in urothelial cells. Its disease and literature associations include hereditary neuralgic amyotrophy, hypertension-related traits, cataract, and leukemia-related genomic rearrangement. It is therefore an informative structural and cell-organization marker despite its more limited network reach.
- **Conclusion**: Established evidence supports SEPTIN9 as a cytoskeletal and cell-organization gene, with a plausible role in the structural side of the module. The prostate detection and urothelial enhancement do not establish prostate specificity, and its connection to folate metabolism remains an association rather than a demonstrated mechanism.

#### USP5

- **Related proteins** (co-abundance neighbors): LTA4H (0.82), MTHFD1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin specific peptidase 5. Ubiquitin (see MIM 191339)-dependent proteolysis is a complex pathway of protein metabolism implicated in such diverse cellular functions as maintenance of chromatin structure, receptor function, and degradation of abnormal proteins. A late step of the process involves disassembly of the polyubiquitin chains on degraded proteins into ubiquitin monomers. USP5 disassembles branched polyubiquitin cha…
- **Diseases (Open Targets)**: neurodegenerative disease (0.532); neoplasm (0.116); hepatocellular carcinoma (0.110); non-small cell lung carcinoma (0.109); cancer (0.104)
- **Europe PMC papers**: 1576
- **Why important**: USP5 connects MTHFD1 with LTA4H and occupies the bridge position between the metabolic and inflammatory branches of the module. It removes ubiquitin from polyubiquitin chains and is annotated for deubiquitination, protein stability, and regulation of proteasomal degradation. It is detected in both tissues and has cell-type enhancement in late primary spermatocytes and syncytiotrophoblasts. Its disease associations include neurodegenerative disease and cancer-related indications, supported by a substantial literature base.
- **Conclusion**: Established evidence supports USP5 as a proteostasis and protein-regulation component with a strategically important network position. It is plausible that USP5 links protein turnover to the other module processes, but the module does not establish a specific USP5 substrate or causal direction.

#### LTA4H

- **Related proteins** (co-abundance neighbors): USP5 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: leukotriene A4 hydrolase. The protein encoded by this gene is an enzyme that contains both hydrolase and aminopeptidase activities. The hydrolase activity is used in the final step of the biosynthesis of leukotriene B4, a proinflammatory mediator. The aminopeptidase activity has been shown to degrade proline-glycine-proline (PGP), a neutrophil chemoattractant and biomarker for chronic obstructive pulmonary disease (COPD). …
- **Diseases (Open Targets)**: hypotensive disorder (0.198); small intestine neuroendocrine neoplasm (0.150); cystic fibrosis (0.104); COVID-19 (0.096); hepatocellular carcinoma (0.086)
- **Europe PMC papers**: 1823
- **Why important**: LTA4H is the terminal gene in the network and connects to USP5. It has dual hydrolase and aminopeptidase activities, produces leukotriene B4 in leukotriene metabolism, and degrades the neutrophil chemoattractant PGP. Its annotations include leukotriene biosynthesis, proteolysis, peptide catabolism, and inflammatory-response-related biology. HPA detects it in both tissues and reports enhancement in monocytes, neutrophil progenitors, alveolar cells, and esophageal cell types. It adds an inflammation and innate-cell context to an otherwise mixed module.
- **Conclusion**: Established evidence supports LTA4H as an inflammatory lipid- and peptide-processing enzyme. Its position and cell-type annotations make it a useful indicator of an inflammatory or myeloid-associated state, but they do not prove that inflammation causes the shared heart–prostate co-abundance pattern.

## Module 7

**Tissue pair**: heart and prostate  
**Genes (5)**: DYNC1I2, SEC23A, SNX6, TKT, TXNDC5

### Function

No GO or KEGG term passed global correction, and STRING supplied no supplementary enrichment. The gene annotations nevertheless converge on intracellular protein handling and transport: TXNDC5 supports ER protein folding, SEC23A supports COPII vesicle budding and ER-to-Golgi transport, SNX6 supports endosomal trafficking, and DYNC1I2 supports dynein-mediated movement of organelles and vesicles. TKT contributes pentose-phosphate metabolism and may provide metabolic support for biosynthetic or stress-response processes. The co-abundance graph links TXNDC5 to TKT, SNX6, and SEC23A, while SEC23A links to DYNC1I2. Thus, the most defensible interpretation is a candidate module related to secretory-pathway protein quality control, vesicle trafficking, and intracellular transport, with a possible metabolic component. Because there is no globally significant enrichment, this is an annotation-based functional interpretation rather than a statistically confirmed pathway assignment.

**Cell composition.** The module is not dominated by plasma or secreted proteins. The HPA summary reports a secreted member, but the gene-level annotation for TXNDC5 describes an intracellular and membrane-associated ER protein rather than a conventionally secreted protein. Most genes have low tissue specificity, and the module is detected in both heart and prostate at the protein level for most members. This broad expression supports a general cellular process rather than a tissue-exclusive program. There is also an immune and blood-cell signal: TKT is enhanced in bone marrow and associated with several myeloid cell types, while TXNDC5 is group-enriched in B-cell and plasmacytoid dendritic-cell populations. These observations raise the possibility that part of the shared co-abundance reflects common stromal, vascular, immune, or other shared cell populations in the samples. The signal is not uniformly blood-cell-specific, because SEC23A, SNX6, and DYNC1I2 have low immune or cell-type specificity.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair met the supplied STRING interaction threshold, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. Therefore, the co-abundance relationships are not corroborated here by high-confidence curated or predicted protein interactions, nor by a shared hu.MAP complex. The absence of these relationships means the module is not an obvious canonical protein complex. It does not exclude indirect cooperation, condition-dependent interactions, shared regulation, common cell-type composition, or technical and biological covariance.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a novel candidate co-abundance association rather than an established molecular module. The combination of genes has no high-confidence STRING pairwise support and no multi-member hu.MAP complex support, while the genes individually have well-established cellular functions. That pattern argues against claiming discovery of a new physical complex. The potentially new observation is their coordinated abundance across heart and prostate, especially the connection between ER quality control, COPII trafficking, endosomal sorting, dynein transport, and transketolase-associated metabolism. Novelty remains provisional because absence from STRING or hu.MAP alone cannot establish novelty, and the module could reflect shared cell composition or broad housekeeping biology.

**Hypothesis.** Mechanistic hypothesis: in shared heart and prostate cellular contexts, increased demand for protein synthesis, folding, export, and intracellular recycling may coordinate TXNDC5-mediated ER quality control with SEC23A-mediated ER exit, SNX6-dependent endosomal sorting, and DYNC1I2-dependent microtubule transport. TKT may support the associated biosynthetic and redox demands through pentose-phosphate metabolism. A second, competing hypothesis is that the co-abundance pattern is partly driven by shared broadly expressed cells or infiltrating immune populations rather than direct pathway coordination. This hypothesis should be tested with cell-type-resolved data, perturbation of trafficking or ER-stress pathways, and independent cohorts.

### Important genes

#### TXNDC5

- **Related proteins** (co-abundance neighbors): TKT (0.91), SNX6 (0.82), SEC23A (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin domain containing 5. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal endoplasmic reticulum (ER)-signal sequence, three catalytically active thioredoxin domains and a C-terminal ER-retention sequence. Its expression is induced by hypoxia and its role ma…
- **Diseases (Open Targets)**: colorectal carcinoma (0.321); spinal stenosis (0.203); neoplasm (0.096); central nervous system cancer (0.092); glioma (0.091)
- **Europe PMC papers**: 1026
- **Why important**: TXNDC5 is the most connected and strongest node in the module. Its ER localization and thioredoxin-domain function provide a direct mechanistic link to protein folding and protection from hypoxia-associated cellular stress. It also has substantial literature support and disease associations, while its HPA pattern suggests possible contributions from plasma-cell, B-cell, and plasmacytoid-dendritic-cell populations.
- **Conclusion**: Established evidence supports TXNDC5 as the leading candidate organizer of the module's ER protein-quality-control interpretation. Its central network position is consistent with, but does not prove, a regulatory role. The proposed role as a bridge between ER folding and the other module processes is a hypothesis.

#### SEC23A

- **Related proteins** (co-abundance neighbors): TXNDC5 (0.82), DYNC1I2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A is connected to TXNDC5 and DYNC1I2, placing it between ER quality control and microtubule-dependent transport. Its established COPII and ER-to-Golgi functions make it a strong mechanistic representative of secretory-pathway trafficking. It is detected in heart and prostate and has disease associations involving skeletal development and male reproductive organ cancer.
- **Conclusion**: SEC23A is an important established trafficking component and is the clearest candidate for linking ER export to downstream intracellular movement. Its role in this shared module is biologically plausible, but the co-abundance data do not establish direct regulation or physical interaction with the neighboring genes.

#### TKT

- **Related proteins** (co-abundance neighbors): TXNDC5 (0.91); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transketolase. This gene encodes a thiamine-dependent enzyme which plays a role in the channeling of excess sugar phosphates to glycolysis in the pentose phosphate pathway. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: transketolase deficiency (0.663); neurodegenerative disease (0.409); cardiomyopathy (0.382); alcohol drinking (0.261); urolithiasis (0.259)
- **Europe PMC papers**: 3981
- **Why important**: TKT is directly connected to TXNDC5 hu.MAP and has the largest literature support among the module genes. Its established role in the non-oxidative pentose-phosphate pathway connects the module to sugar-phosphate handling and biosynthetic metabolism. It is tissue-enhanced in bone marrow and associated with multiple myeloid cell types, and it has a cardiomyopathy association in the supplied disease evidence.
- **Conclusion**: TKT provides an established metabolic component and may indicate biosynthetic or redox support for the trafficking and folding program. Its bone-marrow and myeloid associations also make shared immune-cell composition a credible alternative explanation. Whether TKT is mechanistically coupled to the trafficking genes remains a hypothesis.

#### SNX6

- **Related proteins** (co-abundance neighbors): TXNDC5 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sorting nexin 6. This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. This protein associates with the long isoform of the leptin receptor, the transforming growth factor-beta family of receptor serine-threonine kinases, and with receptor tyrosine kinases for platelet-der…
- **Diseases (Open Targets)**: neurodegenerative disease (0.245); COVID-19 (0.166); Abnormality of the skeletal system (0.104); response to antihypertensive drug (0.068); poisoning (0.068)
- **Europe PMC papers**: 648
- **Why important**: SNX6 is connected to the central TXNDC5 node hu.MAP and is localized to endosomes and lysosomes. Its established sorting-nexin function, including links to receptor trafficking and regulation of receptor signaling, extends the module beyond the ER into endosomal transport and recycling. It is detected in both tissues and has cell-type enhancement in Hofbauer cells.
- **Conclusion**: SNX6 supports an intracellular trafficking interpretation and may represent the endosomal arm of the candidate module. Its direct functional participation in a heart-prostate conserved program is not established by the available interaction resources, so any bridge to ER quality control remains hypothetical.

#### DYNC1I2

- **Related proteins** (co-abundance neighbors): SEC23A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Microtubules, Centrosome, Cytosol, Flagellar centriole, Mid piece, Principal piece; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 1 intermediate chain 2. This gene encodes a member of the dynein intermediate chain family. The encoded protein is a non-catalytic component of the cytoplasmic dynein 1 complex, which acts as a retrograde microtubule motor to transport organelles and vesicles. A pseudogene of this gene is located on chromosome 10. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly and structural brain anomalies (0.698); neurodegenerative disease (0.484); viral infectious disease (0.462); lysosomal storage disease (0.432); neurodevelopmental disorder with microcephaly, hypotonia, and variable brain anomalies (0.425)
- **Europe PMC papers**: 407
- **Why important**: DYNC1I2 is connected to SEC23A hu.MAP and is a non-catalytic component of cytoplasmic dynein, an established retrograde microtubule motor for organelles and vesicles. Its localization across microtubules, centrosomal structures, and specialized cellular regions makes it a plausible transport component. It also has substantial literature support and disease associations involving neurodevelopmental, neurodegenerative, infectious, and lysosomal disorders.
- **Conclusion**: DYNC1I2 supplies an established microtubule-transport mechanism that could connect secretory vesicles with intracellular destinations. Its presence supports a trafficking hypothesis, but the lack of STRING and hu.MAP support means that module-specific cooperation with SEC23A or the other genes is not demonstrated.

## Module 8

**Tissue pair**: heart and prostate  
**Genes (5)**: DHX9, HNRNPL, HNRNPR, SRSF7, DARS1

### Function

The module is most strongly associated with nuclear RNA metabolism, especially pre-mRNA splicing and regulation of mRNA processing. The primary evidence is the globally corrected GO enrichment for RNA splicing, spliceosome-mediated mRNA splicing, mRNA processing, RNA splicing, mRNA binding, mRNA metabolic process, and regulation of mRNA processing (10 globally significant GO/KEGG terms, q_global 0.00145–0.0384; see the table). Four module genes—DHX9, HNRNPL, HNRNPR, and SRSF7—account for this signal. Their annotations support complementary roles: DHX9 is an RNA helicase, HNRNPL and HNRNPR are heterogeneous nuclear RNA-binding proteins, and SRSF7 is an SR-family spliceosomal factor. DARS1 is not included in the primary GO/KEGG terms, but its role in tRNA aminoacylation provides a possible connection to translation rather than the core splicing signal. The co-abundance structure is consistent with a coordinated RNA-processing program, although co-abundance does not by itself establish physical interaction or causality.

**Cell composition.** This does not resemble a plasma-protein, secreted-protein, blood-cell-enriched, or broadly immune-cell-specific module. All module genes have low tissue specificity, none is classified as secreted, and all have low immune-cell specificity in HPA. The proteins are detected in prostate, while most are detected in heart; DARS1 is detected in prostate but not heart. The module is therefore more consistent with a broadly used intracellular program than with blood contamination or a shared circulating-protein signal. HNRNPL and SRSF7 have selected cell-type-enhanced HPA annotations, but the reported cell types are not a recurring blood-cell pattern and do not establish that the module is driven by those cell populations.

**GO/KEGG enrichment**: 10 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA splicing, via transesterification reactions | 0.00145 | DHX9, HNRNPL, HNRNPR, SRSF7 |
| GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile | 0.00145 | DHX9, HNRNPL, HNRNPR, SRSF7 |
| GO:BP mRNA splicing, via spliceosome | 0.00145 | DHX9, HNRNPL, HNRNPR, SRSF7 |
| GO:BP mRNA processing | 0.00313 | DHX9, HNRNPL, HNRNPR, SRSF7 |
| GO:BP RNA splicing | 0.00313 | DHX9, HNRNPL, HNRNPR, SRSF7 |
| GO:MF mRNA binding | 0.0058 | DHX9, HNRNPL, HNRNPR, SRSF7 |
| GO:BP mRNA metabolic process | 0.00971 | DHX9, HNRNPL, HNRNPR, SRSF7 |
| GO:BP regulation of mRNA processing | 0.0145 | DHX9, HNRNPL, SRSF7 |
| GO:BP RNA processing | 0.0149 | DHX9, HNRNPL, HNRNPR, SRSF7 |
| GO:BP regulation of mRNA metabolic process | 0.0384 | DHX9, HNRNPL, SRSF7 |

### STRING and hu.MAP

STRING supports a densely connected RNA-processing core. DHX9 has high-confidence associations with HNRNPL, HNRNPR, and SRSF7; HNRNPL and HNRNPR are strongly associated; and both are associated with SRSF7. These known relationships agree with the globally significant splicing and mRNA-processing terms (10 globally significant GO/KEGG terms, q_global 0.00145–0.0384; see the table) and with the supplementary STRING pathways (15 supplementary STRING terms; within-query FDR 0.00014–0.0182). The STRING results should remain supplementary because their reported significance was not corrected across modules. hu.MAP repeatedly places HNRNPL and HNRNPR together in several heterogeneous nuclear ribonucleoprotein and RNA-processing complexes (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_10625.1). However, each listed complex contains only a subset of this module, so hu.MAP supports a known hnRNP-related context rather than proving that the entire module is one physical complex. DHX9, SRSF7, and DARS1 have no reported hu.MAP complex in this fact sheet, and DARS1 has no reported STRING partner among the module genes.

**STRING interactions (score >= 0.7)**: 6 of 10 gene pairs: DHX9–HNRNPL (0.901); DHX9–HNRNPR (0.909); DHX9–SRSF7 (0.789); HNRNPL–HNRNPR (0.961); HNRNPL–SRSF7 (0.926); HNRNPR–SRSF7 (0.833)
**STRING functional enrichment (supplementary, within-query FDR)**: WikiPathways mRNA processing (FDR = 0.00014, 4 genes); NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex (FDR = 0.00029, 4 genes); RCTM mRNA Splicing - Major Pathway (FDR = 0.00092, 4 genes); Process RNA metabolic process (FDR = 0.002, 5 genes); SMART RNA recognition motif (FDR = 0.0021, 3 genes); NetworkNeighborAL Mixed, incl. CRD-mediated mRNA stabilization, and Zinc finger, CHHC-type (FDR = 0.0029, 3 genes); Process mRNA processing (FDR = 0.0035, 4 genes); Process Gene expression (FDR = 0.0055, 5 genes); Keyword RNA-binding (FDR = 0.0069, 4 genes); InterPro RNA recognition motif domain (FDR = 0.0086, 3 genes); InterPro Nucleotide-binding alpha-beta plait domain superfamily (FDR = 0.0086, 3 genes); InterPro RNA-binding domain superfamily (FDR = 0.0086, 3 genes); Process Negative regulation of mRNA metabolic process (FDR = 0.011, 3 genes); Process Regulation of mRNA processing (FDR = 0.0144, 3 genes); Process mRNA splicing, via spliceosome (FDR = 0.0182, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07225.1 (HNRNPR, HNRNPL; 2/7); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09654.1 (HNRNPR, HNRNPL; 2/13); huMAP3_07581.1 (HNRNPR, HNRNPL; 2/21); huMAP3_10659.1 (HNRNPR, HNRNPL; 2/28); huMAP3_10625.1 (HNRNPR, HNRNPL; 2/57)

### Novelty

The biological theme is not new: spliceosomal RNA processing, hnRNP proteins, DHX9, HNRNPL, HNRNPR, SRSF7, and their interactions are already represented in functional annotations, STRING, and hu.MAP. The potentially novel observation is the conserved co-abundance module shared by heart and prostate, particularly the specific combination with DARS1. Nevertheless, the supplied evidence does not include comparison with previously published co-abundance modules, independent cohorts, perturbation experiments, or a systematic search of all prior tissue-pair analyses. Therefore this should be described as a potentially distinctive tissue-pair co-abundance configuration, not as a definitively new biological discovery. Lack of a hu.MAP or STRING entry for a gene pair would not establish novelty.

**Hypothesis.** Mechanistic hypothesis: in both heart and prostate, a shared intracellular RNA-processing state coordinates DHX9 helicase activity with hnRNP and SR-splicing-factor function to regulate transcript maturation, alternative splicing, RNA stability, and export. DARS1 may couple this RNA-processing state to translational capacity through tRNA charging. This hypothesis is motivated by the hub-like position of DHX9, the recurrent HNRNPL–HNRNPR complex context, the SRSF7 connections, the globally significant splicing terms, and the STRING RNA-processing evidence. It remains a hypothesis because the data are co-abundance and annotation based; they do not demonstrate direct regulation, a single assembled complex, or a causal heart–prostate mechanism.

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): HNRNPR (0.89), SRSF7 (0.86), DARS1 (0.85), HNRNPL (0.84); STRING partners: HNRNPL (0.901), HNRNPR (0.909), SRSF7 (0.789)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is the most connected and strongest module member in the supplied co-abundance network, linking HNRNPR, SRSF7, DARS1, and HNRNPL. It appears in every primary globally corrected GO term (10 globally significant GO/KEGG terms, q_global 0.00145–0.0384; see the table) and in many supplementary RNA-processing terms (4 supplementary STRING terms; within-query FDR 0.00014–0.002), (4 supplementary STRING terms; within-query FDR 0.0029–0.0069), and (STRING Process Negative regulation of mRNA metabolic process; within-query FDR = 0.011) (STRING Process Regulation of mRNA processing; within-query FDR = 0.0144) (STRING Process mRNA splicing, via spliceosome; within-query FDR = 0.0182). Its annotated ATP-dependent RNA helicase activity provides a plausible catalytic component for remodeling RNA or RNA–protein complexes. It also has the largest literature volume among the module genes and disease associations including intellectual developmental disorder and neurodegenerative disease.
- **Conclusion**: Established evidence supports DHX9 as a central RNA-helicase component of the module and as a major contributor to its splicing and mRNA-processing interpretation. The idea that DHX9 organizes the entire conserved heart–prostate module, or couples it directly to DARS1, is a hypothesis requiring perturbation or physical-association experiments.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): DHX9 (0.84), HNRNPR (0.80); STRING partners: DHX9 (0.901), HNRNPR (0.961), SRSF7 (0.926)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, prostate
- **hu.MAP 3.0**: huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_07581.1, huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is a highly connected core member with links to DHX9, HNRNPR, and SRSF7. It occurs in every primary enrichment term (10 globally significant GO/KEGG terms, q_global 0.00145–0.0384; see the table), in nearly all supplementary RNA-binding and splicing terms, and in every reported hu.MAP complex (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_10625.1). Its established hnRNP role in mRNA packaging, processing, regulation of alternative splicing, and RNA processing makes it a strong functional anchor. It also has substantial literature support and disease associations involving neuromuscular disease and cancer-related indications.
- **Conclusion**: Established evidence identifies HNRNPL as a central scaffold-like RNA-binding component connecting the module to known hnRNP complexes and splicing regulation. Its precise contribution to the shared heart–prostate co-abundance pattern, including whether it drives or merely reflects the program, remains unresolved.

#### HNRNPR

- **Related proteins** (co-abundance neighbors): DHX9 (0.89), HNRNPL (0.80); STRING partners: DHX9 (0.909), HNRNPL (0.961), SRSF7 (0.833)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, prostate
- **hu.MAP 3.0**: huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_07581.1, huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR is directly connected to DHX9 and HNRNPL and has the strongest reported STRING association with HNRNPL among the module relationships. It contributes to most primary GO terms (7 globally significant GO/KEGG terms, q_global 0.00145–0.00971; see the table) and (GO:BP RNA processing; q_global = 0.0149), to the supplementary RNA-processing and RNA-binding terms (12 supplementary STRING terms; within-query FDR 0.00014–0.0086) and (STRING Process mRNA splicing, via spliceosome; within-query FDR = 0.0182), and to every hu.MAP complex reported for the module (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_10625.1). Its established membership in the spliceosome C complex and role in pre-mRNA processing and transport give the module a specific spliceosomal interpretation. Its disease associations include neurodevelopmental disorder, intellectual disability, developmental delay, seizure, and microcephaly.
- **Conclusion**: Established evidence supports HNRNPR as a spliceosome- and hnRNP-associated core component, especially in partnership with HNRNPL. The module data do not establish whether HNRNPR has a tissue-specific regulatory role in heart or prostate.

#### SRSF7

- **Related proteins** (co-abundance neighbors): DHX9 (0.86); STRING partners: DHX9 (0.789), HNRNPL (0.926), HNRNPR (0.833)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine and arginine rich splicing factor 7. The protein encoded by this gene is a member of the serine/arginine (SR)-rich family of pre-mRNA splicing factors, which constitute part of the spliceosome. Each of these factors contains an N-terminal RNA recognition motif (RRM) for binding RNA and a C-terminal RS domain for binding other proteins. The RS domain is rich in serine and arginine residues and facilitates interaction between different…
- **Diseases (Open Targets)**: neurodegenerative disease (0.536); dengue disease (0.370); cystitis (0.221); smoking initiation (0.107); neoplasm (0.082)
- **Europe PMC papers**: 1327
- **Why important**: SRSF7 is connected to DHX9 and is strongly associated with HNRNPL and HNRNPR in STRING. It occurs in every primary globally corrected GO term (10 globally significant GO/KEGG terms, q_global 0.00145–0.0384; see the table) and in the supplementary spliceosomal, RNA-binding, and RNA-recognition-motif terms (5 supplementary STRING terms; within-query FDR 0.00014–0.0021) and (9 supplementary STRING terms; within-query FDR 0.0035–0.0182). Its SR-family identity, RNA-recognition motif, and RS domain provide an established mechanism for RNA binding and interaction with spliceosomal proteins. It has substantial literature support and disease associations including neurodegenerative disease and cystitis.
- **Conclusion**: Established evidence supports SRSF7 as the module's SR-family splicing-factor component and as a likely interface between RNA recognition and spliceosomal regulation. Its peripheral network position does not exclude functional importance, but a specific role in the conserved tissue-pair module is presently hypothetical.

#### DARS1

- **Related proteins** (co-abundance neighbors): DHX9 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 1. This gene encodes a member of a multienzyme complex that functions in mediating the attachment of amino acids to their cognate tRNAs. The encoded protein ligates L-aspartate to tRNA(Asp). Mutations in this gene have been found in patients showing hypomyelination with brainstem and spinal cord involvement and leg spasticity. Alternative splicing results in multiple transcript variants. [provided by…
- **Diseases (Open Targets)**: hypomyelination with brain stem and spinal cord involvement and leg spasticity (0.773); atrial fibrillation (0.268); Abnormal brain morphology (0.266); tooth hard tissue disease (0.226); Pancreatic pseudocyst (0.225)
- **Europe PMC papers**: 238
- **Why important**: DARS1 is the least connected and most functionally peripheral member of the module, with a reported network link only to DHX9. It does not appear in the primary GO/KEGG terms, but STRING supplementary evidence places it in broad RNA metabolic and gene-expression categories (STRING Process RNA metabolic process; within-query FDR = 0.002) and (STRING Process Gene expression; within-query FDR = 0.0055). Its established function is aspartyl-tRNA synthetase, linking it to tRNA aminoacylation and protein translation. It has a disease association with hypomyelination involving the brainstem and spinal cord, as well as reported associations with atrial fibrillation and abnormal brain morphology.
- **Conclusion**: Established evidence supports DARS1 as a translation-related RNA enzyme rather than a core spliceosomal factor. Its inclusion may indicate coupling between RNA processing and translational capacity, but that connection is a hypothesis because DARS1 lacks primary enrichment support, reported STRING partners in this module, and reported hu.MAP membership.
