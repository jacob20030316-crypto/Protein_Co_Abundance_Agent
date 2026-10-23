# Conserved co-abundance modules: circulatory_system and colon

## Module 0

**Tissue pair**: circulatory_system and colon  
**Genes (10)**: APBB1IP, ALG1, RCSD1, MPP7, OPHN1, DHRS7B, PPCS, RAP1GAP, INPP5D, TRAF3IP3

### Function

The module does not have a statistically supported GO or KEGG functional label: no globally significant GO/KEGG term passed global correction. Its gene content nevertheless suggests a mixed cellular program rather than a single established pathway. The central network position of TRAF3IP3 connects INPP5D, RCSD1, DHRS7B, ALG1, MPP7, and PPCS. Established annotations across the module involve hematopoietic signaling and immune regulation through TRAF3IP3, INPP5D, APBB1IP, and RAP1GAP; cell adhesion, polarity, and junctional organization through MPP7, RAP1GAP, RCSD1, and OPHN1; and membrane, glycosylation, lipid, or CoA-related metabolism through ALG1, DHRS7B, and PPCS. These annotations support a cautious interpretation as a shared immune–cell-interface and cellular-maintenance co-abundance program, not as a proven pathway.

**Cell composition.** The module is not composed of secreted or plasma proteins. HPA indicates a strong cellular-expression pattern, with frequent associations with lymphoid tissue and with microglia, neutrophil-lineage cells, monocytes, and NK cells. Several genes are tissue enhanced in lymphoid tissue or intestine, while others show broad or tissue-specific expression in sites including esophagus, brain, kidney, and skeletal muscle. Most genes have low immune-cell specificity, but the recurrent immune and myeloid associations suggest that shared immune-cell content or related cell-state variation in circulatory-system and colon samples may contribute substantially to the conserved co-abundance signal. Colon protein detection is present for most genes, whereas the circulatory-system protein summary has no informative matching HPA tissue result. The module therefore should not be interpreted as a purely colon epithelial program or as a circulating secretome module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no high-confidence interactions among the module genes and no supplementary STRING enrichment. This means the co-abundance edges are not corroborated by the specified STRING evidence and may reflect coordinated expression, cell composition, context-dependent biology, or indirect relationships rather than a physically interacting protein network. hu.MAP identifies one shared complex, (hu.MAP huMAP3_09592.1), containing DHRS7B and ALG1, but these are only a small part of a much larger complex. The (hu.MAP huMAP3_09592.1) result provides limited support for a membrane or endoplasmic-reticulum-associated relationship, while the absence of hu.MAP assignments for the other genes indicates that most module relationships remain unconfirmed at the complex level.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09592.1 (DHRS7B, ALG1; 2/95)

### Novelty

This is not sufficient evidence to call the module a new biological discovery. The absence of STRING interactions and the limited hu.MAP overlap make the exact co-abundance configuration relatively weakly documented in these resources, but database absence alone does not establish novelty. Several component functions and disease associations are already established, including immune signaling, cell polarity, GTPase regulation, glycosylation, CoA biosynthesis, and inherited disease links. The potentially novel aspect is the tissue-pair-specific co-abundance of these otherwise heterogeneous genes, which requires independent replication, cell-composition adjustment, and ideally perturbational or protein-level validation.

**Hypothesis.** Hypothesis: the conserved signal reflects coordinated abundance of immune-associated cells or immune-related cell states together with epithelial or junctional and general membrane-maintenance programs shared by circulatory-system and colon samples. TRAF3IP3 and INPP5D may mark or regulate immune signaling, RCSD1, APBB1IP, RAP1GAP, and OPHN1 may connect cytoskeletal, adhesion, and small-GTPase control, while MPP7 may represent epithelial junctional organization. ALG1, DHRS7B, and PPCS could reflect concurrent endoplasmic-reticulum, lipid, or metabolic requirements. This is a mechanistic model rather than an established pathway assignment, because no globally significant GO/KEGG term, STRING enrichment, or broad high-confidence interaction network supports it directly.

### Important genes

#### TRAF3IP3

- **Related proteins** (co-abundance neighbors): INPP5D (0.86), DHRS7B (0.82), ALG1 (0.82), MPP7 (0.81), PPCS (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TRAF3 interacting protein 3. The gene encodes a protein that mediates cell growth by modulating the c-Jun N-terminal kinase signal transduction pathway. The encoded protein may also interact with a large multi-protein assembly containing the phosphatase 2A catalytic subunit. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2013].
- **Diseases (Open Targets)**: injury (0.239); neoplasm (0.098); glioma (0.092); central nervous system cancer (0.092); hepatocellular carcinoma (0.080)
- **Europe PMC papers**: 383
- **Why important**: TRAF3IP3 has the highest network connectivity and links the immune-associated branch to DHRS7B, ALG1, MPP7, and PPCS. Established evidence describes roles in c-Jun N-terminal kinase signaling, cytoplasmic pattern-recognition signaling, type I interferon production, and antiviral innate immunity. Its lymphoid tissue enrichment and colon detection make it a plausible anchor for the shared signal, and its substantial literature volume makes the interpretation comparatively well supported.
- **Conclusion**: Established evidence supports TRAF3IP3 as the network hub and an immune or innate-signaling component. It is reasonable to hypothesize that it organizes the module's immune-associated expression pattern, but the co-abundance data do not prove that it regulates the other module genes.

#### INPP5D

- **Related proteins** (co-abundance neighbors): TRAF3IP3 (0.86), RCSD1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inositol polyphosphate-5-phosphatase D. This gene is a member of the inositol polyphosphate-5-phosphatase (INPP5) family and encodes a protein with an N-terminal SH2 domain, an inositol phosphatase domain, and two C-terminal protein interaction domains. Expression of this protein is restricted to hematopoietic cells where its movement from the cytosol to the plasma membrane is mediated by tyrosine phosphorylation. At the plasma membrane…
- **Diseases (Open Targets)**: atopic eczema (0.501); allergic rhinitis (0.488); hypothyroidism (0.459); Alzheimer disease (0.440); respiratory system disorder (0.420)
- **Europe PMC papers**: 2216
- **Why important**: INPP5D is connected to both TRAF3IP3 and RCSD1 and encodes a hematopoietic phosphoinositide phosphatase with an SH two domain and interaction domains. Its established functions include signal-transduction regulation, phosphatidylinositol metabolism, B-cell differentiation, and regulation of neutrophil differentiation. It is enhanced in intestine and lymphoid tissue and enriched in microglia, giving it direct relevance to the tissue pair and the immune-cell composition concern.
- **Conclusion**: Established evidence supports INPP5D as a biologically important immune signaling and membrane-phosphoinositide regulator. Its module membership may reflect immune-cell abundance or state, but a direct functional link to every module member remains hypothetical.

#### MPP7

- **Related proteins** (co-abundance neighbors): OPHN1 (0.82), TRAF3IP3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cell Junctions; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MAGUK p55 scaffold protein 7. The protein encoded by this gene is a member of the p55 Stardust family of membrane-associated guanylate kinase (MAGUK) proteins, which function in the establishment of epithelial cell polarity. This family member forms a complex with the polarity protein DLG1 (discs, large homolog 1) and facilitates epithelial cell polarity and tight junction formation. Polymorphisms in this gene are associated w…
- **Diseases (Open Targets)**: intelligence (0.338); digestive system disorder (0.316); Achilles tendon injury (0.304); vertebral column disorder (0.274); cartilage disease (0.235)
- **Europe PMC papers**: 1606
- **Why important**: MPP7 connects the hub TRAF3IP3 with OPHN1 and is localized to cell junctions. Established annotations assign it roles in epithelial polarity, tight-junction assembly, adherens-junction localization, and protein-complex assembly. Its colon protein detection and association with esophageal and neutrophil-progenitor or neutrophil cell types make it informative for a possible epithelial–immune interface rather than a purely hematopoietic interpretation.
- **Conclusion**: Established evidence supports MPP7 as a junctional and polarity component that could connect tissue architecture to the immune-associated branch. Its proposed bridging role in this module is a hypothesis based on network position and co-abundance, not a demonstrated physical interaction.

#### RCSD1

- **Related proteins** (co-abundance neighbors): RAP1GAP (0.85), APBB1IP (0.84), INPP5D (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RCSD domain containing 1. Enables actin filament binding activity. Involved in cellular hyperosmotic response. Predicted to be located in actin filament. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Bicuspid aortic valve (0.291); lobular capilliary hemangioma (0.230); alcohol drinking (0.229); stroke disorder (0.229); venous thromboembolism (0.219)
- **Europe PMC papers**: 321
- **Why important**: RCSD1 occupies an internal network position connecting RAP1GAP, APBB1IP, and INPP5D. It is annotated for actin-filament binding, endosomal protein localization, retrograde endosome-to-Golgi transport, and cellular hyperosmotic response. HPA links it particularly to lymphoid tissue and several macrophage, Kupffer-cell, and hematopoietic populations, making it relevant to both cytoskeletal organization and possible cell-composition effects.
- **Conclusion**: Established evidence supports RCSD1 as a cytoskeletal and trafficking-related factor with immune-associated expression. Its position suggests a possible interface between phosphoinositide signaling, adhesion, and actin organization, but the module does not establish causality.

#### ALG1

- **Related proteins** (co-abundance neighbors): TRAF3IP3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: ALG1 chitobiosyldiphosphodolichol beta-mannosyltransferase. The enzyme encoded by this gene catalyzes the first mannosylation step in the biosynthesis of lipid-linked oligosaccharides. This gene is mutated in congenital disorder of glycosylation type Ik. [provided by RefSeq, Dec 2008].
- **Diseases (Open Targets)**: ALG1-congenital disorder of glycosylation (0.857); congenital disorder of glycosylation (0.613); neurodegenerative disease (0.536); hereditary disease (0.510); congenital disorder of glycosylation type I (0.436)
- **Europe PMC papers**: 695
- **Why important**: ALG1 is one of the two module members in hu.MAP complex (hu.MAP huMAP3_09592.1) and encodes the enzyme catalyzing an early mannosylation step in lipid-linked oligosaccharide and protein N-linked glycosylation. It is localized to the endoplasmic reticulum, is detected in colon, and has an established association with congenital disorders of glycosylation. Its connection to TRAF3IP3 and its (hu.MAP huMAP3_09592.1) membership provide the clearest complex-level support within the module.
- **Conclusion**: Established evidence supports ALG1 as an endoplasmic-reticulum glycosylation enzyme and as one component of the (hu.MAP huMAP3_09592.1) complex evidence. Its co-abundance with immune and junctional genes may reflect shared cellular demand or cell-state composition; a direct role in the proposed immune–epithelial program is hypothetical.

## Module 1

**Tissue pair**: circulatory_system and colon  
**Genes (5)**: ABHD11, FAM193B, ING3, PSMB10, PSMB9

### Function

The strongest interpretation is a proteasome-centered co-abundance module, with particular emphasis on proteasome beta-subunit activity and the proteasome core complex. All primary globally corrected terms (GO:MF threonine-type endopeptidase activity; q_global = 0.00973) through (GO:CC proteasome core complex; q_global = 0.026) are driven by PSMB9 and PSMB10, linking these genes to threonine-type peptidase activity, the proteasome core, the beta-subunit complex, and the spermatoproteasome. Their supplied functional annotations also support proteasomal protein catabolism, immune-system processes, and antigen processing and presentation. The module network is sparse and organized around FAM193B, which connects to PSMB9, PSMB10, ING3, and ABHD11. Thus, the proteasome interpretation is well established for the PSMB9–PSMB10 pair, whereas the biological meaning of the connections involving FAM193B is less certain. The lack of globally significant terms for FAM193B, ING3, and ABHD11 means that their roles in the shared module should not be inferred from enrichment alone.

**Cell composition.** This is not a plasma-protein or secreted-protein module: none of the genes is annotated as secreted. The HPA profile instead suggests a mixture of broadly detected intracellular proteins and cell- or tissue-associated signals. PSMB9 and PSMB10 are tissue enhanced in lymphoid tissue and have cell-type enhancement including NK-cells, while ING3 is tissue enriched in bone marrow and ABHD11 has enhancement in several specialized cell types including megakaryocytes. FAM193B has low tissue and cell-type specificity and is not detected in immune cells. Most genes have low immune-cell specificity, and no blood cell category is identified as the predominant enriched blood-cell class. Protein detection in colon is reported for most genes, whereas the supplied circulatory-system protein evidence is unavailable. Consequently, the shared signal could reflect intracellular proteasome activity present in colon and circulating-associated samples, with possible contributions from lymphoid or other shared cell populations, but the HPA evidence does not establish a purely blood-cell-derived module.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF threonine-type endopeptidase activity | 0.00973 | PSMB10, PSMB9 |
| GO:CC proteasome core complex, beta-subunit complex | 0.00973 | PSMB10, PSMB9 |
| GO:CC spermatoproteasome complex | 0.00973 | PSMB10, PSMB9 |
| GO:MF threonine-type peptidase activity | 0.0145 | PSMB10, PSMB9 |
| GO:CC proteasome core complex | 0.026 | PSMB10, PSMB9 |

### STRING and hu.MAP

STRING provides strong direct support for a known PSMB9–PSMB10 relationship, and the supplementary STRING annotations (STRING Keyword Threonine protease; within-query FDR = 0.0131) through (STRING InterPro Nucleophile aminohydrolases, N-terminal; within-query FDR = 0.0379) consistently place this pair in proteasome beta-subunit, proteasome core, proteasome activator, and spermatoproteasome contexts. The pair also occurs together in the three hu.MAP complexes (hu.MAP huMAP3_00356.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1), all of which contain many additional proteasome subunits and associated factors. These results show that the PSMB9–PSMB10 portion of the module corresponds to a recognized proteasome-associated molecular system. In contrast, FAM193B, ING3, and ABHD11 have no reported STRING partners or hu.MAP complexes in the supplied evidence. Therefore, the external interaction resources validate the proteasome core of the module but do not independently validate the star-shaped co-abundance connections from FAM193B to the other genes. The co-abundance structure may therefore contain a known proteasome component embedded in a tissue-level expression relationship that is not yet represented as a physical complex or high-confidence interaction.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: PSMB10–PSMB9 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Threonine protease (FDR = 0.0131, 2 genes); Component Proteasome core complex, beta-subunit complex (FDR = 0.0133, 2 genes); Component Spermatoproteasome complex (FDR = 0.0133, 2 genes); COMPARTMENTS Proteasome activator complex (FDR = 0.0154, 2 genes); COMPARTMENTS Proteasome core complex, beta-subunit complex (FDR = 0.0154, 2 genes); COMPARTMENTS Spermatoproteasome complex (FDR = 0.0154, 2 genes); Pfam Proteasome subunit (FDR = 0.016, 2 genes); Function Threonine-type endopeptidase activity (FDR = 0.0209, 2 genes); InterPro Peptidase T1A, proteasome beta-subunit (FDR = 0.0209, 2 genes); InterPro Proteasome, subunit alpha/beta (FDR = 0.0209, 2 genes); InterPro Proteasome beta-type subunit, conserved site (FDR = 0.0209, 2 genes); InterPro Proteasome B-type subunit (FDR = 0.0209, 2 genes); KEGG Proteasome (FDR = 0.023, 2 genes); Keyword Proteasome (FDR = 0.0247, 2 genes); InterPro Nucleophile aminohydrolases, N-terminal (FDR = 0.0379, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00356.1 (PSMB9, PSMB10; 2/33); huMAP3_09656.1 (PSMB9, PSMB10; 2/64); huMAP3_13725.1 (PSMB9, PSMB10; 2/69)

### Novelty

The module should not be presented as a newly discovered proteasome complex or as a new physical interaction, because the PSMB9–PSMB10 relationship and their participation in proteasome complexes are already supported by STRING and hu.MAP. A potentially less-established aspect is the cross-tissue co-abundance pattern connecting FAM193B with both proteasome genes and with ING3 and ABHD11, since those relationships are not supported by the supplied STRING or hu.MAP records. However, absence from those resources does not prove novelty, and the fact sheet does not provide independent replication, perturbation evidence, or literature evidence for a new mechanism. The defensible conclusion is that this is a potentially interesting tissue-pair co-abundance association built around a known proteasome signal, not a demonstrated novel molecular complex.

**Hypothesis.** Hypothesis: the shared module reflects coordinated intracellular proteostasis and immune-related peptide processing in cells or cell mixtures represented in both tissue groups. PSMB9 and PSMB10 may provide the proteasome and immunoproteasome-related functional core, while FAM193B may mark or participate in a broader nuclear or cytoplasmic state associated with this proteasome program. ING3 could connect that state to chromatin remodeling, cell-cycle regulation, and apoptosis, and ABHD11 could connect it to mitochondrial or lipid-metabolic status. The proposed links from FAM193B to ING3 and ABHD11 are hypotheses based on co-abundance and supplied annotations, not established physical or causal interactions. Testing this model would require cell-resolved expression, perturbation experiments, and validation across independent samples.

### Important genes

#### PSMB9

- **Related proteins** (co-abundance neighbors): FAM193B (0.80); STRING partners: PSMB10 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_00356.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 20S subunit beta 9. The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent proc…
- **Diseases (Open Targets)**: plasma cell myeloma (0.608); MHC class I deficiency (0.565); proteasome-associated autoinflammatory syndrome 6 (0.556); mantle cell lymphoma (0.542); neoplasm (0.537)
- **Europe PMC papers**: 3004
- **Why important**: PSMB9 is one of the two genes responsible for every globally corrected enrichment term (GO:MF threonine-type endopeptidase activity; q_global = 0.00973) through (GO:CC proteasome core complex; q_global = 0.026). It is a proteasome beta subunit with supplied annotations for proteasomal protein catabolism, immune-system processes, antigen processing and presentation, and regulation of inflammatory cytokine production. It is also linked to the known PSMB9–PSMB10 STRING interaction and all three hu.MAP complexes (hu.MAP huMAP3_00356.1) through (hu.MAP huMAP3_13725.1). Its extensive literature and disease associations involving MHC class I deficiency, plasma cell myeloma, mantle cell lymphoma, neoplasm, and proteasome-associated autoinflammation make it a strong biological anchor.
- **Conclusion**: Established evidence supports PSMB9 as a central proteasome and immune-related component of the module. Its role in the module is more secure than any proposed role for the non-proteasome genes. A tissue-specific immunoproteasome mechanism is plausible, but the co-abundance data alone do not establish that the module is produced by a particular immune cell type or that PSMB9 drives the other module genes.

#### PSMB10

- **Related proteins** (co-abundance neighbors): FAM193B (0.81); STRING partners: PSMB9 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_00356.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 20S subunit beta 10. The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent proc…
- **Diseases (Open Targets)**: proteasome-associated autoinflammatory syndrome 5 (0.634); plasma cell myeloma (0.604); immunodeficiency 121 with autoinflammation (0.578); mantle cell lymphoma (0.542); neoplasm (0.529)
- **Europe PMC papers**: 1477
- **Why important**: PSMB10 is the second gene responsible for every globally corrected enrichment term (GO:MF threonine-type endopeptidase activity; q_global = 0.00973) through (GO:CC proteasome core complex; q_global = 0.026). Its supplied annotation identifies it as a proteasome twenty-S beta subunit and associates it with proteasomal degradation, immune-system processes, antigen presentation, and humoral immune response. It has the strongest known STRING relationship in the module through its pair with PSMB9 and is present in all three hu.MAP proteasome complexes (hu.MAP huMAP3_00356.1) through (hu.MAP huMAP3_13725.1). Its substantial literature and disease associations involving proteasome-associated autoinflammation, plasma cell myeloma, lymphoma, immunodeficiency, and neoplasm further support its importance.
- **Conclusion**: Established evidence identifies PSMB10 as a core proteasome component and a major explanation for the module's enrichment. Its coordinated abundance with PSMB9 is consistent with shared proteasome or immunoproteasome biology. It remains a hypothesis, rather than an established conclusion, that the pair specifically reports an activated immune or inflammatory state in both tissue groups.

#### FAM193B

- **Related proteins** (co-abundance neighbors): ING3 (0.87), ABHD11 (0.85), PSMB10 (0.81), PSMB9 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm, Nucleoli; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: family with sequence similarity 193 member B. Located in cytoplasm; nuclear speck; and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.321); Alzheimer disease (0.204); dementia (0.201); nonpapillary renal cell carcinoma (0.075); oculopharyngodistal myopathy (0.017)
- **Europe PMC papers**: 96
- **Why important**: FAM193B has the central network position: it is connected to every other module gene in the supplied co-abundance subgraph and therefore forms the bridge between the known PSMB9–PSMB10 signal and ING3 and ABHD11. It has low tissue and cell-type specificity, is localized to the nucleoplasm and nucleoli, and is detected in colon. It has no supplied STRING partners, hu.MAP complexes, or enriched GO/KEGG or STRING terms, so its importance arises mainly from network position and its potential to organize the shared expression pattern. Its literature volume and disease associations indicate that it is studied, but the fact sheet does not establish a specific function in this module.
- **Conclusion**: The network supports FAM193B as the principal co-abundance connector, but not as a demonstrated proteasome regulator. Its central position may reflect coordinated regulation, a shared cell-state signal, or indirect expression coupling. Any mechanistic role for FAM193B in proteostasis, chromatin, or tissue-specific biology remains a hypothesis requiring direct experimental validation.

#### ING3

- **Related proteins** (co-abundance neighbors): FAM193B (0.87); STRING partners: none
- **HPA**: Tissue enriched; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inhibitor of growth family member 3. The protein encoded by this gene is similar to ING1, a tumor suppressor protein that can interact with TP53, inhibit cell growth, and induce apoptosis. This protein contains a PHD-finger, which is a common motif in proteins involved in chromatin remodeling. This gene can activate p53 trans-activated promoters, including promoters of p21/waf1 and bax. Overexpression of this gene has been shown to i…
- **Diseases (Open Targets)**: neurodegenerative disease (0.546); Alzheimer disease (0.403); Parkinson disease (0.402); lysosomal storage disease (0.402); Proptosis (0.259)
- **Europe PMC papers**: 608
- **Why important**: ING3 is connected only to FAM193B in the module, so it is peripheral in graph position but potentially informative biologically. Its supplied annotation links it to chromatin organization, chromatin remodeling, transcriptional regulation, apoptosis, and cell-cycle control, and its protein is localized to the nucleoplasm. It is tissue enriched in bone marrow, has substantial literature volume, and has disease associations involving neurodegenerative and other disorders. These features make it a plausible indicator of a nuclear regulatory state that could accompany proteasome-related cellular stress or immune-cell composition.
- **Conclusion**: Established evidence supports ING3 as a chromatin- and growth-regulatory protein, but not as a proteasome component. Its membership in this module is supported by co-abundance with FAM193B only. A connection between ING3-mediated transcriptional control and the proteasome signal is a testable hypothesis, not a demonstrated mechanism.

#### ABHD11

- **Related proteins** (co-abundance neighbors): FAM193B (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: abhydrolase domain containing 11. This gene encodes a protein containing an alpha/beta hydrolase fold domain. This gene is deleted in Williams syndrome, a multisystem developmental disorder caused by the deletion of contiguous genes at 7q11.23. [provided by RefSeq, Mar 2016].
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); colorectal carcinoma (0.103); familial pancreatic carcinoma (0.097); thyroid gland papillary carcinoma (0.097); pancreatic neoplasm (0.089)
- **Europe PMC papers**: 565
- **Why important**: ABHD11 is connected only to FAM193B and has no supplied STRING partners, hu.MAP complexes, or enriched GO/KEGG or STRING terms. Its supplied annotation describes an alpha/beta hydrolase fold protein associated with lipid metabolic processes, with mitochondrial localization and colon detection. HPA cell-type enhancement includes megakaryocytes and several other specialized cell types, while its disease associations include colorectal carcinoma and other neoplasms. It is therefore useful as a possible metabolic or cell-composition marker within the otherwise proteasome-centered module.
- **Conclusion**: Established evidence supports ABHD11 as a mitochondrial, hydrolase-domain-associated protein with a possible lipid-metabolic role, but does not connect it directly to proteasome biology. Its inclusion may reflect a shared metabolic state or sample-cell composition rather than a physical pathway with PSMB9 and PSMB10. Any functional bridge is therefore hypothetical.

## Module 2

**Tissue pair**: circulatory_system and colon  
**Genes (6)**: EHD1, SPART, STAT1, TTL, YY2, VPS45

### Function

No GO/KEGG term passed global correction, so the module has no statistically established pathway-level annotation. Its gene content instead supports a mixed intracellular-trafficking, cytoskeletal, and regulatory signal. TTL links tubulin tyrosination to microtubule organization; EHD1, SPART, and VPS45 support endocytosis, endosomal recycling, vesicle-mediated transport, and intracellular sorting; STAT1 provides cytokine- and interferon-responsive transcriptional regulation; and YY2 is a transcription factor. The co-abundance structure therefore suggests coordinated regulation of microtubule-associated trafficking and cell-state responses, but this functional interpretation remains gene-based rather than enrichment-based.

**Cell composition.** This is not a plasma-protein or secreted-protein module: all member proteins are intracellular or membrane-associated, and the secretome annotation is absent for every member. Most genes have low tissue specificity, arguing against a narrowly tissue-restricted program. HPA nevertheless indicates cell-context structure, including testis and spermatid enrichment for YY2, EHD1, and VPS45, bone-marrow enhancement for EHD1, basophil enrichment for SPART, and cardiomyocyte, epicardial, mesothelial, oligodendrocyte, or neutrophil-associated signals among other members. Thus, the shared circulatory-system and colon pattern could partly reflect common cellular composition or broadly expressed intracellular machinery rather than a colon–circulation-specific biological pathway. Colon protein detection is present for several members, while circulatory-system protein evidence is unavailable in the supplied HPA tissue comparison.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only supplied high-confidence STRING relationship among module members is EHD1–VPS45. This is biologically coherent because EHD1 participates in endocytosis and recycling, whereas VPS45 participates in vesicle-mediated protein transport. No hu.MAP complex contains multiple module members. The remaining co-abundance links are therefore not corroborated by the supplied STRING or hu.MAP evidence. This pattern supports a small, partially connected trafficking-related core rather than a known stable multiprotein complex.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: EHD1–VPS45 (0.867)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported co-abundance association, because no multi-member hu.MAP complex is reported and STRING supports only the EHD1–VPS45 relationship. However, these absences do not establish novelty: co-abundance can arise from shared expression, cell composition, or indirect regulation, and lack of database coverage is not evidence that the association is new. The strongest defensible conclusion is that the cross-tissue co-abundance configuration is not explained by a well-established canonical complex in the supplied resources, but independent replication and comparison with published co-expression studies would be required before calling it a new biological module.

**Hypothesis.** Hypothesis: the module reflects coordinated control of intracellular membrane traffic and microtubule organization in cells represented in both tissues, with TTL and SPART linking microtubule or mitochondrial and endosomal processes, EHD1 and VPS45 forming the best-supported vesicle-trafficking pair, and STAT1 and YY2 representing transcriptional or cell-state regulators that covary with this machinery. In circulation, the signal may be influenced by blood-associated cell populations; in colon, it may reflect epithelial, stromal, vascular, or immune cellular composition. This model predicts that the module will track vesicle transport, cytoskeletal remodeling, and inflammatory or cytokine-responsive states, but these predictions are not established by global GO/KEGG enrichment.

### Important genes

#### STAT1

- **Related proteins** (co-abundance neighbors): TTL (0.87), YY2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal transducer and activator of transcription 1. The protein encoded by this gene is a member of the STAT protein family. In response to cytokines and growth factors, STAT family members are phosphorylated by the receptor associated kinases, and then form homo- or heterodimers that translocate to the cell nucleus where they act as transcription activators. The protein encoded by this gene can be activated by various ligands including interferon-…
- **Diseases (Open Targets)**: immunodeficiency 31B (0.786); chronic mucocutaneous candidiasis (0.775); autoimmune enteropathy and endocrinopathy - susceptibility to chronic infections syndrome (0.772); cancer (0.554); immunodeficiency disease (0.482)
- **Europe PMC papers**: 66602
- **Why important**: STAT1 is the most biologically interpretable regulatory hub after TTL in the supplied network, connecting TTL with YY2. It is activated by interferons, cytokines, and growth factors and mediates transcriptional responses, including antiviral defense and regulation of cellular proliferation. It has extensive disease and literature support, including immunodeficiency and chronic infection associations, making it the strongest candidate for linking intracellular machinery to tissue or inflammatory state.
- **Conclusion**: Established evidence supports STAT1 as a cytokine-responsive transcriptional regulator with major immune and disease relevance. Its membership in this module supports a hypothesis of coordinated cell-state regulation, but does not establish that STAT1 directly controls the other module genes or that the module is an interferon pathway.

#### TTL

- **Related proteins** (co-abundance neighbors): STAT1 (0.87), SPART (0.80), VPS45 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tubulin tyrosine ligase. TTL is a cytosolic enzyme involved in the posttranslational modification of alpha-tubulin (see MIM 602529). Alpha-tubulin within assembled microtubules is detyrosinated over time at the C terminus. After microtubule disassembly, TTL restores the tyrosine residues and consequently participates in a cycle of tubulin detyrosination and tyrosination (Erck et al., 2003 [PubMed 14571137]).[supplied by O…
- **Diseases (Open Targets)**: smoking initiation (0.414); corneal dystrophy (0.346); nicotine dependence (0.338); substance abuse (0.338); attention deficit-hyperactivity disorder (0.338)
- **Europe PMC papers**: 3903
- **Why important**: TTL has the highest network connectivity in the supplied subgraph and connects STAT1, SPART, and VPS45. Its established function is restoration of the tyrosine residue on alpha-tubulin after microtubule detyrosination, with roles in microtubule organization, mitotic control, and chromosome congression. It also has substantial literature support, so it provides a mechanistic bridge between the network topology and cytoskeletal biology.
- **Conclusion**: Established evidence supports TTL as a microtubule-regulating enzyme and a plausible structural organizer of the module. The network supports a hypothesis that tubulin modification covaries with trafficking and regulatory genes, but it does not prove direct physical interaction or causal control.

#### EHD1

- **Related proteins** (co-abundance neighbors): YY2 (0.83); STRING partners: VPS45 (0.867)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Plasma membrane; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EH domain containing 1. This gene belongs to a highly conserved gene family encoding EPS15 homology (EH) domain-containing proteins. The protein-binding EH domain was first noted in EPS15, a substrate for the epidermal growth factor receptor. The EH domain has been shown to be an important motif in proteins involved in protein-protein interactions and in intracellular sorting. The protein encoded by this gene is thought …
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.107); neoplasm (0.101); device complication (0.091); lung adenocarcinoma (0.079); osteosarcoma (0.074)
- **Europe PMC papers**: 1857
- **Why important**: EHD1 is a membrane-associated endocytic and recycling factor and is the module member participating in the supplied high-confidence STRING relationship with VPS45. It is enhanced in bone marrow and spermatid-related cell contexts and is detected in colon tissue by the supplied HPA evidence. Its endosomal function makes it central to the proposed trafficking interpretation.
- **Conclusion**: Established evidence supports EHD1 in endocytosis, intracellular sorting, and recycling, with an internally corroborated relationship to VPS45. Its module position supports a trafficking-core interpretation, while the tissue-shared co-abundance remains an association rather than proof of a common vesicle pathway.

#### VPS45

- **Related proteins** (co-abundance neighbors): TTL (0.80); STRING partners: EHD1 (0.867)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vacuolar protein sorting 45 homolog. Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene is a member of the Sec1 domain family, and shows a high degree of sequence similarity to mouse, rat and yeast Vps45. The exact func…
- **Diseases (Open Targets)**: congenital neutropenia-myelofibrosis-nephromegaly syndrome (0.787); severe congenital neutropenia (0.549); neurodegenerative disease (0.462); COVID-19 (0.371); hereditary disease (0.192)
- **Europe PMC papers**: 811
- **Why important**: VPS45 is a vesicle-mediated transport factor and forms the supplied high-confidence STRING pair with EHD1. It is also connected to TTL in the co-abundance network, providing a link between vesicle transport and microtubule biology. Its associations with severe congenital neutropenia and related disease phenotypes make it relevant to the possibility that blood-cell composition contributes to the circulatory-system signal.
- **Conclusion**: Established evidence supports VPS45 in intracellular protein sorting and vesicle transport, and the EHD1 relationship is the strongest known interaction in this module. The blood-related disease associations motivate a cell-composition hypothesis, but do not demonstrate that neutrophils or immune cells generate the module.

#### SPART

- **Related proteins** (co-abundance neighbors): TTL (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Immune cell enriched; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: spartin. This gene encodes a protein containing a MIT (Microtubule Interacting and Trafficking molecule) domain, and is implicated in regulating endosomal trafficking and mitochondria function. The protein localizes to mitochondria and partially co-localizes with microtubules. Stimulation with epidermal growth factor (EGF) results in protein translocation to the plasma membrane, and the protein functions i…
- **Diseases (Open Targets)**: Troyer syndrome (0.802); Neurodevelopmental delay (0.455); hereditary disease (0.415); Global developmental delay (0.262); cerebellar ataxia (0.260)
- **Europe PMC papers**: 269
- **Why important**: SPART connects to TTL in the co-abundance network and has functions involving endosomal trafficking, mitochondria, microtubules, lipid transport, and degradation or trafficking of the EGF receptor. It is the only member with an HPA immune-cell-enriched signal for basophils and has a strong disease association with Troyer syndrome. Its combination of trafficking, mitochondrial, and cytoskeletal functions makes it useful for interpreting the module as a cellular logistics program rather than a single canonical pathway.
- **Conclusion**: Established evidence supports SPART as a regulator of endosomal, mitochondrial, and microtubule-related processes with disease relevance. Its network placement supports a hypothesis that it helps connect cytoskeletal and membrane-trafficking states, but the module does not establish a direct SPART–TTL mechanism.

## Module 3

**Tissue pair**: circulatory_system and colon  
**Genes (5)**: KRT16, KRT5, JUP, SERPINB12, ZC3HAV1

### Function

The module is most strongly interpreted as a cornified-envelope and epithelial intermediate-filament program. The primary evidence is the globally significant enrichment for cornified envelope (GO:CC cornified envelope; q_global = 0.00332), intermediate filament (GO:CC intermediate filament; q_global = 0.0099), cornified envelope formation (KEGG Cornified envelope formation - Homo sapiens (human); q_global = 0.0189), and intermediate-filament cytoskeleton (GO:CC intermediate filament cytoskeleton; q_global = 0.0271). JUP, KRT5, and KRT16 support epithelial junction and cytoskeletal structure, while SERPINB12 is compatible with regulation of protease activity during epithelial differentiation. ZC3HAV1 contributes an antiviral and innate-immune interpretation, but it has no globally significant GO/KEGG annotation in this module. The coherent structural interpretation is therefore epithelial barrier differentiation, with a possible context-dependent antiviral component rather than a principally circulatory or plasma-protein function.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Its composition is strongly epithelial and keratin-associated. HPA links most of the genes to skin, esophageal, cervical, or vaginal tissues and to basal or suprabasal keratinocyte populations. KRT5 and KRT16 are especially characteristic of basal and suprabasal epithelial cells, while JUP is localized to plasma membranes and cell junctions and is detected in colon. The module is not broadly representative of blood cells: SERPINB12 is not detected in immune cells, KRT16 is not detected in immune cells, and KRT5 has immune-cell enrichment in a limited cell type. Because the module is shared by circulatory_system and colon despite its epithelial signature, the shared signal could reflect epithelial material, epithelial-cell admixture, tissue injury, or sample composition rather than a blood-specific biological program. The circulatory-system HPA protein comparison has no matching tissue data, so it cannot resolve that possibility.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC cornified envelope | 0.00332 | JUP, KRT16, SERPINB12 |
| GO:CC intermediate filament | 0.0099 | JUP, KRT16, KRT5 |
| KEGG Cornified envelope formation - Homo sapiens (human) | 0.0189 | JUP, KRT16, KRT5 |
| GO:CC intermediate filament cytoskeleton | 0.0271 | JUP, KRT16, KRT5 |

### STRING and hu.MAP

STRING provides direct high-confidence support for the KRT5–KRT16 relationship, consistent with their established role as paired epithelial intermediate-filament proteins. The remaining module relationships are not represented by high-confidence STRING interactions, so the co-abundance edges should not be treated as a fully established physical interaction network. STRING functional annotations independently reinforce cornified-envelope formation, intermediate filaments, keratosis, skin-barrier disease, and epithelial blistering (15 supplementary STRING terms; within-query FDR 5.8e-06–0.0191), but these are supplementary annotations rather than globally corrected GO/KEGG evidence. hu.MAP places JUP and SERPINB12 together in several complexes (hu.MAP huMAP3_05845.1) (hu.MAP huMAP3_08595.1) (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1). Those complexes are broad epithelial or cornification-associated assemblies containing many additional structural, junctional, protease-regulatory, and barrier genes; the repeated co-membership supports biological plausibility but does not establish that all module genes form a single physical complex. ZC3HAV1 has no reported hu.MAP or STRING support in the supplied evidence.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: KRT16–KRT5 (0.861)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Formation of the cornified envelope, and Serpin, conserved site (FDR = 5.8e-06, 4 genes); Component Cornified envelope (FDR = 0.0018, 3 genes); DISEASES Keratosis (FDR = 0.002, 3 genes); Component Intermediate filament (FDR = 0.0029, 3 genes); RCTM Formation of the cornified envelope (FDR = 0.003, 3 genes); PMID (2020) Skin tape proteomics identifies pathways associated with transepidermal water loss and allergen polysensitization in atopic dermatitis. (FDR = 0.0049, 4 genes); NetworkNeighborAL Pachyonychia congenita, and Epidermolysis bullosa simplex Dowling-Meara type (FDR = 0.0059, 2 genes); DISEASES Nonepidermolytic palmoplantar keratoderma (FDR = 0.0177, 2 genes); HPO Hyperhidrosis (FDR = 0.0191, 3 genes); HPO Palmoplantar keratoderma (FDR = 0.0191, 3 genes); HPO Alopecia (FDR = 0.0191, 3 genes); HPO Absent toenail (FDR = 0.0191, 2 genes); HPO Palmoplantar blistering (FDR = 0.0191, 2 genes); HPO Hypohidrosis or hyperhidrosis (FDR = 0.0191, 3 genes); HPO Abnormal blistering of the skin (FDR = 0.0191, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05845.1 (JUP, SERPINB12; 2/24); huMAP3_08595.1 (JUP, SERPINB12; 2/25); huMAP3_09125.1 (JUP, SERPINB12; 2/53); huMAP3_09929.1 (JUP, SERPINB12; 2/75)

### Novelty

The underlying biology is not new: keratin intermediate filaments, JUP-mediated epithelial junctions, cornified-envelope formation, and SERPINB12-associated epithelial programs are established themes, and the disease associations in (STRING DISEASES Keratosis; within-query FDR = 0.002) and (9 supplementary STRING terms; within-query FDR 0.0059–0.0191) reinforce that conclusion. The potentially novel aspect is the specific co-abundance configuration shared between circulatory_system and colon, particularly the inclusion of ZC3HAV1 with an epithelial cornification signature. However, the supplied evidence does not establish that this exact tissue-pair module has been reported previously, and absence from STRING or hu.MAP alone cannot demonstrate novelty. The defensible conclusion is that this may be a new tissue-level co-abundance observation built from largely known epithelial biology, not a newly discovered molecular pathway.

**Hypothesis.** Hypothesis: the module reflects coordinated epithelial barrier remodeling or epithelial-cell admixture shared across the sampled circulatory and colon material. KRT5 and KRT16 may provide the structural intermediate-filament scaffold, JUP may couple that scaffold to epithelial junctions, and SERPINB12 may regulate proteolysis during differentiation or barrier turnover. ZC3HAV1 may mark an accompanying antiviral or inflammatory state in the same epithelial or neighboring cellular context. This hypothesis predicts that module abundance should track epithelial-cell content, barrier injury or differentiation, and possibly local innate-immune activation; it should be tested with epithelial-cell deconvolution, tissue localization, and independent protein or transcript measurements.

### Important genes

#### SERPINB12

- **Related proteins** (co-abundance neighbors): JUP (0.89), ZC3HAV1 (0.89), KRT5 (0.84), KRT16 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05845.1, huMAP3_08595.1, huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: serpin family B member 12. Enables serine-type endopeptidase inhibitor activity. Predicted to be involved in negative regulation of endopeptidase activity. Predicted to act upstream of or within hematopoietic progenitor cell differentiation. Part of collagen-containing extracellular matrix. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.074); familial digital arthropathy-brachydactyly (0.069); brachydactyly type A1 (0.066); spondylolisthesis (0.065); neoplasm (0.064)
- **Europe PMC papers**: 248
- **Why important**: SERPINB12 has the strongest module connectivity and links the principal epithelial genes in the co-abundance graph, including JUP, KRT5, and KRT16. It is the only module gene present in the globally significant cornified-envelope term (GO:CC cornified envelope; q_global = 0.00332) without being a canonical keratin or junctional scaffold. Its HPA profile is enriched in skin-related and suprabasal epithelial contexts, and its annotated serine-type endopeptidase inhibitor activity is mechanistically compatible with epithelial barrier maturation. It is also represented with JUP across the hu.MAP complexes (hu.MAP huMAP3_05845.1) (hu.MAP huMAP3_08595.1) (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1). Its literature volume is smaller than that of the keratins or JUP, making it especially informative for determining whether this module contains a distinctive regulatory component.
- **Conclusion**: Established evidence supports SERPINB12 as an epithelial, cornification-associated protease-regulatory gene that occupies a central position in this module. It is a plausible module organizer or marker, but the co-abundance data do not prove that it directly regulates KRT5, KRT16, or JUP. A coordinating role is a hypothesis requiring perturbation or spatial validation.

#### JUP

- **Related proteins** (co-abundance neighbors): SERPINB12 (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cell Junctions; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_05845.1, huMAP3_08595.1, huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: junction plakoglobin. This gene encodes a major cytoplasmic protein which is the only known constituent common to submembranous plaques of both desmosomes and intermediate junctions. This protein forms distinct complexes with cadherins and desmosomal cadherins and is a member of the catenin family since it contains a distinct repeating amino acid motif called the armadillo repeat. Mutation in this gene has been associa…
- **Diseases (Open Targets)**: Naxos disease (0.784); arrhythmogenic right ventricular dysplasia 12 (0.755); arrhythmogenic right ventricular cardiomyopathy (0.597); lethal acantholytic epidermolysis bullosa (0.383); familial isolated arrhythmogenic ventricular dysplasia, biventricular form (0.370)
- **Europe PMC papers**: 3429
- **Why important**: JUP is the module gene with the broadest annotation support: it contributes to every globally significant GO/KEGG term (4 globally significant GO/KEGG terms, q_global 0.00332–0.0271; see the table), appears in nearly all supplementary STRING themes, and is a member of the hu.MAP complexes (hu.MAP huMAP3_05845.1) (hu.MAP huMAP3_08595.1) (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1). Its established function as junction plakoglobin connects desmosomes and intermediate junctions, making it a mechanistic bridge between epithelial adhesion and the keratin cytoskeleton. HPA detects it in colon and places it in plasma-membrane and cell-junction compartments. Its association with Naxos disease and arrhythmogenic cardiomyopathy also makes it relevant to the circulatory-system context. Its extensive literature provides strong prior support.
- **Conclusion**: Established evidence identifies JUP as a central epithelial adhesion and cytoskeletal component and a strong anchor for the module interpretation. Its role as a tissue-specific driver of the observed cross-tissue co-abundance pattern remains hypothetical; the module alone cannot distinguish altered JUP biology from variation in epithelial-cell abundance.

#### KRT5

- **Related proteins** (co-abundance neighbors): SERPINB12 (0.84); STRING partners: KRT16 (0.861)
- **HPA**: Group enriched; Group enriched; blood Immune cell enriched; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 5. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the basal layer of the epidermis with family member KRT14. Mutations in t…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 2C, localized (0.768); epidermolysis bullosa simplex 2A, generalized severe (0.761); epidermolysis bullosa simplex 2B, generalized intermediate (0.761); epidermolysis bullosa simplex 2F, with mottled pigmentation (0.729); Dowling-Degos disease 1 (0.697)
- **Europe PMC papers**: 7044
- **Why important**: KRT5 is a basal epithelial type-II keratin and contributes to the intermediate-filament and cornified-envelope terms (GO:CC intermediate filament; q_global = 0.0099) (KEGG Cornified envelope formation - Homo sapiens (human); q_global = 0.0189) (GO:CC intermediate filament cytoskeleton; q_global = 0.0271). HPA places it in basal keratinocytes and esophageal epithelial populations, while the supplied disease associations connect it to epidermolysis bullosa simplex and related keratinization disorders. It is directly connected to KRT16 in STRING and is repeatedly represented in supplementary keratinization, keratosis, blistering, and epithelial-disease themes (STRING NetworkNeighborAL Formation of the cornified envelope, and Serpin, conserved site; within-query FDR = 5.8e-06), (5 supplementary STRING terms; within-query FDR 0.002–0.0059), and (7 supplementary STRING terms; within-query FDR 0.0191–0.0191). Its substantial literature volume makes its biological interpretation well established.
- **Conclusion**: Established evidence supports KRT5 as a structural basal-epithelial marker and a major contributor to the module's intermediate-filament interpretation. Its presence in circulatory_system samples should be interpreted cautiously as evidence of epithelial material, epithelial injury, or cellular admixture unless independently localized.

#### KRT16

- **Related proteins** (co-abundance neighbors): SERPINB12 (0.81); STRING partners: KRT5 (0.861)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 16. The protein encoded by this gene is a member of the keratin gene family. The keratins are intermediate filament proteins responsible for the structural integrity of epithelial cells and are subdivided into cytokeratins and hair keratins. Most of the type I cytokeratins consist of acidic proteins which are arranged in pairs of heterotypic keratin chains and are clustered in a region of chromosome 1…
- **Diseases (Open Targets)**: pachyonychia congenita (0.777); palmoplantar keratoderma, nonepidermolytic, focal 1 (0.666); pachyonychia congenita 1 (0.657); diffuse nonepidermolytic palmoplantar keratoderma (0.556); focal palmoplantar keratoderma (0.463)
- **Europe PMC papers**: 1935
- **Why important**: KRT16 contributes to every globally significant term (4 globally significant GO/KEGG terms, q_global 0.00332–0.0271; see the table) and is linked in STRING to KRT5 with strong support. HPA associates it with basal, apical, and suprabasal epithelial populations in skin and esophageal tissues. Its annotations include keratinocyte differentiation, keratinization, cytoskeleton organization, and inflammatory response, and its disease associations include pachyonychia congenita and palmoplantar keratoderma. It is repeatedly present in the supplementary cornification, keratosis, blistering, and skin-disease themes. Its literature volume is substantial, supporting a well-established epithelial structural and stress-response interpretation.
- **Conclusion**: Established evidence supports KRT16 as a differentiation- and stress-associated epithelial intermediate-filament gene that reinforces the module's cornified-barrier identity. Its inflammatory annotation may indicate epithelial stress, but an inflammatory mechanism for this module is hypothetical without independent evidence.

#### ZC3HAV1

- **Related proteins** (co-abundance neighbors): SERPINB12 (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger CCCH-type containing, antiviral 1. This gene encodes a CCCH-type zinc finger protein. This antiviral protein inhibits viral replication by recruiting cellular RNA degradation machineries to degrade viral mRNAs. The encoded protein plays an important role in the innate immune response against multiple DNA and RNA viruses, including Ebola virus, HIV and SARS-CoV-2 (which causes COVID-19). [provided by RefSeq, Sep 2021].
- **Diseases (Open Targets)**: cancer (0.549); hypothyroidism (0.429); neurodegenerative disease (0.358); autoimmune disease (0.308); Hashimoto thyroiditis (0.306)
- **Europe PMC papers**: 979
- **Why important**: ZC3HAV1 is the most functionally divergent module member. It is directly connected to SERPINB12 in the co-abundance graph but has no supplied STRING interaction, hu.MAP complex membership, or significant GO/KEGG term. Its annotated function is antiviral RNA surveillance through recruitment of RNA-degradation machinery, with roles in interferon production, NF-kappa-B signaling, and inhibition of viral replication. HPA places it in bone marrow and several immune-related or glandular cell populations, and it is detected in colon. Its substantial literature volume and disease associations make it biologically consequential even though its relationship to the cornification genes is not established.
- **Conclusion**: Established evidence supports ZC3HAV1 as an antiviral and innate-immune regulator rather than a canonical cornified-envelope protein. Its co-abundance with the epithelial module may indicate an epithelial antiviral state, neighboring immune influence, or sample-composition coupling, but that interpretation remains a hypothesis because external interaction and enrichment support are absent.
