# Conserved co-abundance modules: placenta and stem_cells

## Module 0

**Tissue pair**: placenta and stem_cells  
**Genes (10)**: PGD, CLIC4, CNDP2, DPYSL2, FASN, HYOU1, LTA4H, SEPTIN9, TARS1, CCT5

### Function

This module does not have a globally significant GO or KEGG annotation: no globally significant GO/KEGG term passed global correction. Its function is therefore inferred from the constituent genes and network structure rather than from enrichment. The strongest biological theme is a cytosolic metabolic and stress-response program combining translation capacity through TARS1, NADPH-generating pentose-phosphate metabolism through PGD, leukotriene and peptide processing through LTA4H, proteolytic and redox-related metabolism through CNDP2, lipid synthesis through FASN, cytoskeletal organization through SEPTIN9 and DPYSL2, protein folding through CCT5, endoplasmic-reticulum stress responses through HYOU1, and membrane or polarity regulation through CLIC4. TARS1 is the main network hub and connects several metabolic and structural genes. The module is best described as a mixed intracellular metabolic, proteostasis, cytoskeletal, and inflammatory-response module rather than a narrowly defined pathway. The absence of significant enrichment does not invalidate the module, but it limits confidence in assigning one unified function.

**Cell composition.** The module is not dominated by plasma or conventionally secreted proteins. HYOU1 is annotated as intracellular and membrane-associated in the secretome, while the other genes have no secretome annotation. Most genes are intracellular enzymes, chaperones, cytoskeletal proteins, or translation machinery, so this is not primarily a plasma-protein module. HPA indicates broadly expressed or low-tissue-specificity behavior for many members, consistent with a housekeeping or general cellular component. At the same time, several genes show cell-type or blood-cell associations: PGD is enriched in bone-marrow, esophageal, granulocyte, and monocyte contexts; DPYSL2 has monocyte and dendritic-cell associations; LTA4H has monocyte and neutrophil-progenitor associations; CLIC4 has B-cell associations; and HYOU1 has plasma-cell associations. The module may therefore partly reflect shared cellular populations, including myeloid or other immune-associated cells, in addition to a general intracellular program. Placental protein detection is present for nearly all members, whereas comparable stem-cell HPA tissue data are unavailable, so the shared placenta and stem-cell signal should not be interpreted as tissue-specific protein production without additional validation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides limited direct support for a physical interaction structure. The only high-confidence STRING relationship is between CCT5 and TARS1, supporting a possible connection between chaperone-mediated protein folding and translation-related biology. There is no STRING functional-enrichment result and no basis for treating any STRING result as globally significant enrichment. hu.MAP identifies complex C1 containing LTA4H and PGD, with many other complex members outside this module. This supports a possible shared biochemical or multiprotein context for those two genes, but the limited representation of the complex within the module means it should not be treated as proof that the whole module is one complex. Most module relationships are not represented by these databases, so the co-abundance edges may reflect co-regulation, shared cell composition, indirect biology, or context-dependent interactions rather than established physical binding.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: CCT5–TARS1 (0.727)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (LTA4H, PGD; 2/57)

### Novelty

The module-level co-abundance pattern may be a new observation because most of its inferred relationships are absent from STRING and hu.MAP, and no established enrichment signature defines the module. However, absence from these resources does not prove novelty: database coverage is incomplete, co-abundance is not equivalent to physical interaction, and several genes have well-established individual functions and disease associations. The defensible conclusion is that the shared placenta–stem-cell co-abundance configuration is potentially novel and hypothesis-generating, while the underlying biology of its members is not novel. Independent replication, preservation testing, cell-composition adjustment, and perturbation or interaction experiments would be needed to establish a genuinely new mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in placenta and stem-cell samples in which metabolically active or stress-exposed cells coordinate translation, redox support, lipid and peptide metabolism, cytoskeletal remodeling, and inflammatory signaling. TARS1 may mark the central intracellular state, while PGD could provide reducing power, LTA4H could connect the state to leukotriene and neutrophil-related signaling, SEPTIN9 and DPYSL2 could organize cytoskeletal responses, and HYOU1 and CCT5 could support protein folding and proteostasis. The immune-cell annotations raise an alternative or complementary hypothesis that part of the shared signal derives from common myeloid or other immune-cell content rather than a conserved program intrinsic to placental and stem cells. This hypothesis is not established by the enrichment results and requires testing with cell-resolved data and functional perturbation.

### Important genes

#### TARS1

- **Related proteins** (co-abundance neighbors): LTA4H (0.89), CNDP2 (0.87), PGD (0.87), SEPTIN9 (0.80), DPYSL2 (0.80), CLIC4 (0.80); STRING partners: CCT5 (0.727)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: threonyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Threonyl-tRNA synthetase belongs to the class-II aminoacyl-tRNA synthetase family [provided by RefSeq, Jul 2008]…
- **Diseases (Open Targets)**: trichothiodystrophy 7, nonphotosensitive (0.520); trichothiodystrophy (0.430); actinic keratosis (0.356); dyshidrosis (0.315); placental abruption (0.307)
- **Europe PMC papers**: 147
- **Why important**: TARS1 has the strongest network connectivity and links several metabolic and structural members of the module. Its established function is threonyl-tRNA aminoacylation and support of protein translation. It has placenta protein detection, low tissue and immune specificity, a known STRING relationship with CCT5, and a substantial literature and disease-association record. Its central network position makes it the most useful candidate for representing the shared intracellular state.
- **Conclusion**: Established evidence supports TARS1 as a translation-related enzyme and as a central co-abundance hub. The hypothesis that it coordinates the broader module is plausible from its network position but is not demonstrated by the available interaction or enrichment evidence.

#### PGD

- **Related proteins** (co-abundance neighbors): CNDP2 (0.87), TARS1 (0.87), LTA4H (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: phosphogluconate dehydrogenase. 6-phosphogluconate dehydrogenase is the second dehydrogenase in the pentose phosphate shunt. Deficiency of this enzyme is generally asymptomatic, and the inheritance of this disorder is autosomal dominant. Hemolysis results from combined deficiency of 6-phosphogluconate dehydrogenase and 6-phosphogluconolactonase suggesting a synergism of the two enzymopathies. Several transcript variants encoding…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); Abnormality of the skeletal system (0.329); autoimmune disorder of central nervous system (0.246); smoking behavior (0.245); essential hypertension (0.199)
- **Europe PMC papers**: 8652
- **Why important**: PGD is a core metabolic enzyme in the oxidative pentose-phosphate pathway and supports NADPH regeneration. It is connected to CNDP2 and LTA4H and is one of the two module members in hu.MAP complex C1. HPA shows strong associations with bone marrow, granulocyte-related populations, classical monocytes, and other blood-cell contexts. PGD also has extensive literature, making its metabolic and blood-cell relevance comparatively well established.
- **Conclusion**: Established evidence supports PGD as a redox and pentose-phosphate enzyme with prominent hematopoietic and myeloid associations. Its participation in a shared placenta–stem-cell metabolic program is a reasonable interpretation, but the module does not establish whether the signal is intrinsic to those cells or driven by shared immune-cell content.

#### LTA4H

- **Related proteins** (co-abundance neighbors): TARS1 (0.89), CNDP2 (0.82), PGD (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: leukotriene A4 hydrolase. The protein encoded by this gene is an enzyme that contains both hydrolase and aminopeptidase activities. The hydrolase activity is used in the final step of the biosynthesis of leukotriene B4, a proinflammatory mediator. The aminopeptidase activity has been shown to degrade proline-glycine-proline (PGP), a neutrophil chemoattractant and biomarker for chronic obstructive pulmonary disease (COPD). …
- **Diseases (Open Targets)**: hypotensive disorder (0.198); small intestine neuroendocrine neoplasm (0.150); cystic fibrosis (0.104); COVID-19 (0.096); hepatocellular carcinoma (0.086)
- **Europe PMC papers**: 1823
- **Why important**: LTA4H provides a mechanistic bridge between intracellular metabolism and inflammatory biology. It produces leukotriene B4 through its hydrolase activity and can degrade the neutrophil chemoattractant PGP. It is connected to TARS1, CNDP2, and PGD and occurs with PGD in hu.MAP complex C1. HPA associates it with monocytes and neutrophil progenitors, and it has a substantial literature and disease-association record.
- **Conclusion**: Established evidence supports LTA4H as a leukotriene and peptide-processing enzyme with immune-cell relevance. Its co-abundance with PGD suggests a possible metabolic-inflammatory axis, but a direct functional interaction within this module remains a hypothesis.

#### SEPTIN9

- **Related proteins** (co-abundance neighbors): CCT5 (0.84), DPYSL2 (0.83), TARS1 (0.80), HYOU1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: septin 9. This gene is a member of the septin family involved in cytokinesis and cell cycle control. This gene is a candidate for the ovarian tumor suppressor gene. Mutations in this gene cause hereditary neuralgic amyotrophy, also known as neuritis with brachial predilection. A chromosomal translocation involving this gene on chromosome 17 and the MLL gene on chromosome 11 results in acute myelomonocytic l…
- **Diseases (Open Targets)**: neuralgic amyotrophy (0.564); hypertensive disorder (0.496); cataract (0.437); essential hypertension (0.426); alcohol drinking (0.420)
- **Europe PMC papers**: 748
- **Why important**: SEPTIN9 is a highly connected structural member linking CCT5, DPYSL2, TARS1, and HYOU1. Its known functions include cytoskeleton organization, cytokinesis, intracellular protein localization, and cilium-related regulation. HPA places it in actin filaments and shows placenta detection. It has a comparatively extensive literature, including associations with hereditary neuralgic amyotrophy and acute myelomonocytic leukemia.
- **Conclusion**: Established evidence supports SEPTIN9 as a cytoskeletal and cell-organization protein. Its position between translation, chaperone, and stress-associated genes supports a possible role as a structural integrator of the module, but this organizing role is not directly demonstrated.

#### HYOU1

- **Related proteins** (co-abundance neighbors): SEPTIN9 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 contributes an explicit stress and proteostasis dimension. It is an HSP seventy-family protein induced under hypoxic or endoplasmic-reticulum stress conditions and is implicated in protein folding, secretion, stress responses, and apoptosis regulation. It is connected to SEPTIN9 and has placenta detection, plasma-cell single-cell association, and a substantial literature and disease-association record. Although it is a peripheral network member, it may be biologically informative because placenta and stem-cell environments can involve hypoxic or proteostatic stress.
- **Conclusion**: Established evidence supports HYOU1 as a stress-responsive protein-folding factor. Its inclusion supports a proteostasis component in the module, while the proposed connection between HYOU1-mediated stress adaptation and the metabolic or cytoskeletal genes remains a hypothesis.

## Module 1

**Tissue pair**: placenta and stem_cells  
**Genes (19)**: ABRACL, ACTN1, AKAP12, CALU, CNN2, FBN1, FHL2, IGFBP3, ITGA3, ITGB1, JPT1, MAP1B, MDH1, NUCB1, PDLIM5, S100A13, SPARC, CTTN, THBS1

### Function

The most defensible interpretation is an extracellular-matrix, cell-adhesion, focal-adhesion, and cytoskeletal module. The network links matrix-associated proteins such as THBS1, SPARC, FBN1, and IGFBP3 with integrin and actin-associated components including ITGA3, ITGB1, ACTN1, FHL2, and MAP1B. The annotations support roles in cell-matrix attachment, cell shape, mechanical coupling, trophoblast interaction with extracellular matrix, and regulation of growth or vascular responses. However, no GO or KEGG term passed global multiple-testing correction, so this functional interpretation is based on the convergent gene annotations, network structure, STRING relationships, hu.MAP membership, and HPA localization rather than on a globally significant enrichment term. The absence of a corrected GO or KEGG term does not invalidate the module.

**Cell composition.** This is not a uniformly expressed housekeeping module. It contains a substantial extracellular and secreted component, including THBS1, SPARC, IGFBP3, FBN1, and NUCB1, while ITGA3, ITGB1, ACTN1, FHL2, and related proteins connect the matrix to the cytoskeleton. HPA identifies many genes as cell-type enhanced, especially in extravillous trophoblasts, and protein detection in placenta is widespread. The HPA pattern also includes platelets, neutrophils, basophils, monocytes, and other immune-cell signals. Therefore, the shared module could reflect a genuine placental or stem-cell-associated adhesion program, but it could also be partly driven by shared trophoblast, stromal, vascular, platelet, or other blood-related cell content in the samples. HPA has no matching stem-cell tissue for protein detection, so the stem-cell protein-level interpretation remains limited.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a coherent adhesion and matrix interaction backbone. The strongest known relationships include ITGA3 with ITGB1, ITGA3 with THBS1, ITGB1 with THBS1, ACTN1 with ITGB1, ACTN1 with ITGA3, FBN1 with THBS1, FBN1 with ITGB1, and SPARC with THBS1. These relationships show that part of the module recapitulates previously recognized extracellular-matrix and integrin biology rather than being an entirely unexplored interaction system. STRING reports no supplementary functional enrichment for this module. hu.MAP independently places ITGA3 and ITGB1 together in C1, C2, C3, and C4. Because those complexes contain many other proteins and only a pair of module members in each case, the hu.MAP evidence supports a shared adhesion-complex context but does not establish that the entire module is one physical complex. The remaining module relationships are not represented by hu.MAP complexes in the fact sheet.

**STRING interactions (score >= 0.7)**: 8 of 171 gene pairs: ACTN1–ITGA3 (0.744); ACTN1–ITGB1 (0.974); FBN1–ITGB1 (0.716); FBN1–THBS1 (0.801); ITGA3–ITGB1 (0.999); ITGA3–THBS1 (0.965); ITGB1–THBS1 (0.989); SPARC–THBS1 (0.847)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06815.1 (ITGB1, ITGA3; 2/5); huMAP3_10503.1 (ITGB1, ITGA3; 2/27); huMAP3_10980.1 (ITGB1, ITGA3; 2/44); huMAP3_09336.1 (ITGB1, ITGA3; 2/50)

### Novelty

The exact conserved co-abundance module may be a new systems-level observation, especially because it links matrix proteins, integrin adhesion, cytoskeletal scaffolding, calcium or secretory components, and trophoblast-associated genes across placenta and stem-cell samples. Nevertheless, it should not be described as a newly discovered molecular pathway. Several core relationships are already known in STRING, and the ITGA3-ITGB1 pair is represented in multiple hu.MAP complexes. The absence of many genes from hu.MAP or the absence of a STRING functional-enrichment result cannot prove novelty. The appropriate claim is novel conservation and network-level organization, pending validation in independent cohorts, cell-composition-controlled data, and perturbation experiments.

**Hypothesis.** Hypothesis: in placenta and stem-cell-related cellular contexts, a trophoblast, stromal, vascular, or otherwise matrix-interacting cell population co-regulates an extracellular-matrix adhesion program. THBS1, SPARC, FBN1, and IGFBP3 may shape or signal through the extracellular environment; the ITGA3-ITGB1 receptor may transmit matrix attachment and mechanical cues; and ACTN1, FHL2, MAP1B, and related cytoskeletal proteins may couple those cues to actin or microtubule organization. This could influence adhesion, migration, trophoblast invasion, vascular interaction, and cell-state maintenance. The blood-cell and platelet signals provide an alternative explanation in which the module partly reflects cell mixture rather than coordinated regulation within one cell type. Testing this hypothesis requires cell-resolved expression, correction for blood or trophoblast abundance, protein localization, and perturbation of the integrin or matrix components.

### Important genes

#### THBS1

- **Related proteins** (co-abundance neighbors): SPARC (0.94), FHL2 (0.88), AKAP12 (0.86), MAP1B (0.85), ITGA3 (0.83), NUCB1 (0.81); STRING partners: FBN1 (0.801), ITGA3 (0.965), ITGB1 (0.989), SPARC (0.847)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum, Plasma membrane; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thrombospondin 1. The protein encoded by this gene is a subunit of a disulfide-linked homotrimeric protein. This protein is an adhesive glycoprotein that mediates cell-to-cell and cell-to-matrix interactions. This protein can bind to fibrinogen, fibronectin, laminin, type V collagen and integrins alpha-V/beta-1. This protein has been shown to play roles in platelet aggregation, angiogenesis, and tumorigenesis. [pro…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.385); tooth disorder (0.350); autism spectrum disorder (0.336); neurodegenerative disease (0.323); metabolic syndrome (0.309)
- **Europe PMC papers**: 12762
- **Why important**: THBS1 is a highly connected module component and has direct STRING relationships with SPARC, FBN1, ITGA3, and ITGB1. It is a secreted extracellular-matrix adhesive glycoprotein with established roles in cell-matrix interactions, platelet aggregation, angiogenesis, hypoxia response, and inflammatory biology. HPA detects it in placenta and enhances it in fibroblast, hepatic stellate, macrophage, monocyte, and platelet-associated cell contexts. It is extensively studied and has broad disease literature.
- **Conclusion**: Established evidence supports THBS1 as a matrix-interaction hub and a plausible extracellular organizer of the module. It is reasonable to hypothesize that THBS1 helps coordinate integrin and SPARC-associated adhesion signaling here, but the co-abundance data do not prove that THBS1 causally regulates the other genes.

#### SPARC

- **Related proteins** (co-abundance neighbors): THBS1 (0.94), IGFBP3 (0.91), FHL2 (0.84), MAP1B (0.83), NUCB1 (0.81); STRING partners: THBS1 (0.847)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: secreted protein acidic and cysteine rich. This gene encodes a cysteine-rich acidic matrix-associated protein. The encoded protein is required for the collagen in bone to become calcified but is also involved in extracellular matrix synthesis and promotion of changes to cell shape. The gene product has been associated with tumor suppression but has also been correlated with metastasis based on changes to cell shape which can promote tumor …
- **Diseases (Open Targets)**: osteogenesis imperfecta (0.707); neurodegenerative disease (0.443); hereditary disease (0.414); osteogenesis imperfecta type 4 (0.381); Abnormality of the skeletal system (0.358)
- **Europe PMC papers**: 17798
- **Why important**: SPARC is a connected extracellular and vesicular protein linked in the module to THBS1, IGFBP3, FHL2, MAP1B, and NUCB1, with a known STRING relationship to THBS1. Its established functions include extracellular matrix synthesis, regulation of cell shape, endothelial migration, and angiogenesis. HPA associates it with extravillous trophoblasts, stromal cells, fibroblasts, hepatic stellate cells, and several blood-cell categories, and detects it in placenta. It has substantial literature and disease relevance.
- **Conclusion**: Established evidence makes SPARC a strong candidate for remodeling or organizing the extracellular environment represented by the module. Its broad cell-type pattern also means that SPARC could mark shared stromal or blood-related composition rather than a placenta-stem-cell-specific mechanism.

#### ITGA3

- **Related proteins** (co-abundance neighbors): ACTN1 (0.90), ITGB1 (0.84), FHL2 (0.84), THBS1 (0.83); STRING partners: ACTN1 (0.744), ITGB1 (0.999), THBS1 (0.965)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_06815.1, huMAP3_10503.1, huMAP3_10980.1, huMAP3_09336.1
- **Function (MyGene.info)**: integrin subunit alpha 3. The gene encodes a member of the integrin alpha chain family of proteins. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain that function as cell surface adhesion molecules. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha 3 subunit. This subunit joins with a beta 1 subunit to form an …
- **Diseases (Open Targets)**: epidermolysis bullosa, junctional 7, with interstitial lung disease and nephrotic syndrome (0.807); neurodegenerative disease (0.503); junctional epidermolysis bullosa (0.372); junctional epidermolysis bullosa Herlitz type (0.370); epidermolysis bullosa simplex 4, localized or generalized intermediate, autosomal recessive (0.370)
- **Europe PMC papers**: 4167
- **Why important**: ITGA3 is the alpha partner of the module's ITGB1 integrin and is directly connected to ACTN1, ITGB1, and THBS1. It is a plasma-membrane adhesion receptor with established roles in cell adhesion, cell-matrix adhesion, integrin signaling, and interaction with laminin-family proteins. It is present with ITGB1 in all reported hu.MAP complexes and is detected in placenta. Its disease associations include junctional epidermolysis bullosa and related tissue-integrity disorders, and it has substantial literature.
- **Conclusion**: Established evidence identifies ITGA3 as a plausible membrane receptor that converts matrix association into intracellular signaling. The module supports an ITGA3-ITGB1 adhesion axis, but it does not establish whether this axis is active in trophoblasts, stem cells, or contaminating cell populations.

#### ITGB1

- **Related proteins** (co-abundance neighbors): ITGA3 (0.84); STRING partners: ACTN1 (0.974), FBN1 (0.716), ITGA3 (0.999), THBS1 (0.989)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_06815.1, huMAP3_10503.1, huMAP3_10980.1, huMAP3_09336.1
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is the beta partner of ITGA3 and is linked by STRING to ACTN1, FBN1, ITGA3, and THBS1. It is a central integrin-family adhesion component involved in cell adhesion, embryogenesis, angiogenesis, phagocytosis, tissue repair, and immune responses. HPA places it at the plasma membrane and focal-adhesion sites and detects it in placenta. Its membership with ITGA3 in C1, C2, C3, and C4 provides independent complex-context support, while its extensive disease and biological literature makes it a particularly interpretable anchor.
- **Conclusion**: Established evidence supports ITGB1 as the principal receptor-side anchor of the module. A reasonable hypothesis is that ITGB1-mediated matrix sensing couples the THBS1, SPARC, and FBN1 environment to cytoskeletal remodeling, but co-abundance alone cannot distinguish functional signaling from shared cell abundance.

#### FHL2

- **Related proteins** (co-abundance neighbors): MAP1B (0.92), THBS1 (0.88), CALU (0.87), FBN1 (0.86), SPARC (0.84), ITGA3 (0.84), IGFBP3 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Actin filaments, Focal adhesion sites; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: four and a half LIM domains 2. This gene encodes a member of the four-and-a-half-LIM-only protein family. Family members contain two highly conserved, tandemly arranged, zinc finger domains with four highly conserved cysteines binding a zinc atom in each zinc finger. This protein is thought to have a role in the assembly of extracellular membranes. Also, this gene is down-regulated during transformation of normal myoblasts to r…
- **Diseases (Open Targets)**: familial isolated dilated cardiomyopathy (0.372); alcohol drinking (0.367); seasonal allergic rhinitis (0.307); stroke disorder (0.240); poisoning (0.215)
- **Europe PMC papers**: 2785
- **Why important**: FHL2 has the strongest network connectivity in the supplied module and links MAP1B, THBS1, CALU, FBN1, SPARC, ITGA3, and IGFBP3. HPA places it at actin filaments and focal-adhesion sites and enhances it in extravillous trophoblasts and cardiac-related cell types. Its known functions include transcriptional regulation, osteoblast differentiation, hormone response, apoptosis regulation, and cardiac development. It has substantial literature and disease associations including familial dilated cardiomyopathy.
- **Conclusion**: Established evidence supports FHL2 as an intracellular scaffold or signaling integrator connecting adhesion structures with transcriptional and differentiation programs. Its central position makes it a strong candidate mediator of the module, although the absence of reported STRING partners or hu.MAP membership means that this proposed bridging role remains a hypothesis.

## Module 2

**Tissue pair**: placenta and stem_cells  
**Genes (15)**: ACLY, ANXA3, ATP1B3, CANX, SLC2A1, EIF4A2, PDIA4, PLIN3, RRBP1, RTN4, SEPTIN2, SEPTIN7, NARS1, CCT8, TF

### Function

The module does not support a single formally enriched GO or KEGG function: no GO or KEGG term passed global correction. Its gene composition instead points to a composite cellular program involving endoplasmic-reticulum protein folding and quality control, secretory-pathway support, cytoskeletal organization, translation, membrane transport, glucose handling, and lipid-associated trafficking. The strongest network-centered interpretation is an interface between ER proteostasis and membrane or cytoskeletal organization, rather than a well-defined canonical pathway. CANX, PDIA4, and RRBP1 support ER folding, ER organization, and secretory biology; SEPTIN2 and SEPTIN7 support septin-dependent cytoskeletal structure; SLC2A1, PLIN3, and ACLY connect the module to glucose, lipid storage, and acetyl-CoA biology. These are functional annotations of member genes and network relationships, not evidence of globally significant pathway enrichment.

**Cell composition.** The module is predominantly intracellular and broadly expressed rather than a module dominated by plasma or secreted proteins. HPA classifies most members as having low tissue specificity, and most have low immune-cell specificity, arguing against a simple blood-cell module. There is nevertheless cellular-context structure: several genes are enhanced in trophoblast or syncytiotrophoblast populations, while others are associated with epithelial, neural, acinar, or selected immune-cell populations. TF is secreted to blood and has liver- and retina-associated expression, whereas PDIA4 has intracellular and membrane secretome annotation. The presence of tissue-enhanced SLC2A1 and RRBP1, together with trophoblast-associated HPA signals, makes a placenta-related cellular program plausible, but the shared placenta and stem-cell signal could also reflect broadly expressed housekeeping or biosynthetic demands of proliferative or secretory cells. Placental protein detection is extensive for the module, but there is no matching HPA tissue for stem cells, so the cross-tissue interpretation should not be treated as direct protein-level confirmation in stem cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only two high-confidence pairwise relationships within the module: CANX--PDIA4 and SEPTIN2--SEPTIN7. These relationships independently reinforce an ER proteostasis component and a septin cytoskeletal component. hu.MAP adds complex C1, in which SEPTIN2 and SEPTIN7 occur together as module members within a larger septin complex. The fact that only these two module-member pairs are represented in STRING and only the septin pair is represented by the listed hu.MAP complex indicates that most module edges are co-abundance associations rather than established physical interactions. Thus, the network may capture coordinated cell-state or compartment activity instead of one experimentally validated multiprotein complex.

**STRING interactions (score >= 0.7)**: 2 of 105 gene pairs: CANX–PDIA4 (0.931); SEPTIN2–SEPTIN7 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02362.1 (SEPTIN2, SEPTIN7; 2/14)

### Novelty

This is plausibly a new co-abundance pattern shared by placenta and stem cells, because the module links several cellular compartments and has limited overlap with established STRING and hu.MAP relationships. However, it should not be claimed as a new biological pathway or a newly discovered interaction. The CANX--PDIA4 relationship, the SEPTIN2--SEPTIN7 relationship, and the broader septin complex are already known in the supplied resources, while the remaining edges lack corresponding listed support. Absence from STRING or hu.MAP is not proof of novelty: it may reflect incomplete databases, context specificity, indirect regulation, or co-abundance caused by shared cell composition. The defensible novelty claim is therefore the tissue-pair-specific co-abundance configuration and its proposed integration of ER, cytoskeletal, transport, and metabolic genes, pending replication and experimental testing.

**Hypothesis.** Hypothesis: in placental and stem-cell contexts, a shared cellular state increases biosynthetic and secretory demand while requiring coordinated ER quality control, membrane trafficking, glucose uptake, lipid handling, and cytoskeletal remodeling. CANX, PDIA4, and RRBP1 could support folding, ER organization, and ribosome-associated secretory capacity; SLC2A1 and PLIN3 could supply or manage metabolic substrates; and SEPTIN2 with SEPTIN7 could organize membrane-associated structures and trafficking. The observed co-abundance may therefore arise from coordinated adaptation of secretory, metabolic, and structural systems rather than direct binding among most members. This hypothesis predicts that the module should track secretory load, trophoblast or stem-cell state, ER stress, and membrane remodeling, and should be tested using matched cell-composition controls, perturbation of ER proteostasis or glucose transport, and physical-interaction assays.

### Important genes

#### CANX

- **Related proteins** (co-abundance neighbors): SLC2A1 (0.88), PDIA4 (0.84), RRBP1 (0.84), NARS1 (0.83), SEPTIN2 (0.83), SEPTIN7 (0.82); STRING partners: PDIA4 (0.931)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is among the most highly connected module members and links the network to SLC2A1, PDIA4, RRBP1, NARS1, and both septins. Its ER location and established role as a calcium-binding chaperone for folding and quality control provide a strong functional anchor. The CANX--PDIA4 relationship is also a high-confidence STRING relationship. CANX has a substantial literature base and disease links involving neurodegenerative and infectious disease contexts, making it a well-characterized but mechanistically informative hub.
- **Conclusion**: Established evidence supports CANX as an ER folding and quality-control component and as a known partner of PDIA4. It is a plausible organizing marker of the module's proteostasis axis. It remains a hypothesis that CANX drives the shared tissue-pair co-abundance state or directly coordinates the septin and metabolic branches.

#### RRBP1

- **Related proteins** (co-abundance neighbors): SEPTIN7 (0.89), CANX (0.84), NARS1 (0.84), TF (0.81), SEPTIN2 (0.81), PLIN3 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosome binding protein 1. This gene encodes a ribosome-binding protein of the endoplasmic reticulum (ER) membrane. Studies suggest that this gene plays a role in ER proliferation, secretory pathways and secretory cell differentiation, and mediation of ER-microtubule interactions. Alternative splicing has been observed and protein isoforms are characterized by regions of N-terminal decapeptide and C-terminal heptad repeats.…
- **Diseases (Open Targets)**: cancer (0.476); dengue disease (0.462); neurodegenerative disease (0.324); coronary artery disorder (0.292); placental abruption (0.279)
- **Europe PMC papers**: 1654
- **Why important**: RRBP1 is a highly connected bridge among SEPTIN7, CANX, NARS1, TF, SEPTIN2, and PLIN3. Its ER-membrane location and reported roles in ER proliferation, secretory pathways, secretory-cell differentiation, and ER-microtubule interactions make it especially relevant to the network's mixed ER and structural character. HPA associates it with syncytiotrophoblasts, pancreatic and salivary acinar cells, and selected immune cells, while disease associations include cancer, neurodegenerative disease, and placental abruption.
- **Conclusion**: Established evidence supports RRBP1 as a structural and secretory-pathway ER component with relevant trophoblast expression. It is a strong candidate for explaining why this module is shared by a placenta-related tissue and a stem-cell group. Whether it is a causal coordinator rather than a readout of secretory-cell abundance remains unresolved.

#### SEPTIN2

- **Related proteins** (co-abundance neighbors): ATP1B3 (0.92), RTN4 (0.88), EIF4A2 (0.86), CANX (0.83), NARS1 (0.83), RRBP1 (0.81); STRING partners: SEPTIN7 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Actin filaments; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_02362.1
- **Function (MyGene.info)**: septin 2. Enables identical protein binding activity. Predicted to be involved in several processes, including cilium assembly; regulation of exocytosis; and smoothened signaling pathway. Predicted to act upstream of or within regulation of L-glutamate import across plasma membrane and regulation of protein localization. Located in several cellular components, including cytoskeleton; photoreceptor connectin…
- **Diseases (Open Targets)**: hypothyroidism (0.239); squamous cell carcinoma (0.201); ischemic stroke (0.189); coronary artery disorder (0.181); skin cancer (0.181)
- **Europe PMC papers**: 281
- **Why important**: SEPTIN2 has high network connectivity and connects the septin branch to ATP1B3, RTN4, EIF4A2, CANX, NARS1, and RRBP1. It is an actin-filament-associated septin involved in cytoskeletal organization, intracellular localization, cytokinesis, and cilium assembly. Its relationship with SEPTIN7 is the strongest listed STRING interaction, and both genes occur in hu.MAP complex C1. Its literature base is substantial and includes disease associations spanning neurological, vascular, and cancer-related contexts.
- **Conclusion**: Established evidence supports SEPTIN2 as a cytoskeletal and septin-complex component, with direct network support from SEPTIN7. Its position suggests that structural remodeling may connect the ER and metabolic portions of the module. A direct role in the shared placenta and stem-cell state is a hypothesis, not established by this co-abundance analysis.

#### SEPTIN7

- **Related proteins** (co-abundance neighbors): RRBP1 (0.89), EIF4A2 (0.87), CANX (0.82), NARS1 (0.82), ACLY (0.81); STRING partners: SEPTIN2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_02362.1
- **Function (MyGene.info)**: septin 7. This gene encodes a protein that is highly similar to the CDC10 protein of Saccharomyces cerevisiae. The protein also shares similarity with Diff 6 of Drosophila and with H5 of mouse. Each of these similar proteins, including the yeast CDC10, contains a GTP-binding motif. The yeast CDC10 protein is a structural component of the 10 nm filament which lies inside the cytoplasmic membrane and is essen…
- **Diseases (Open Targets)**: glaucoma (0.366); bone fracture (0.264); fracture of pelvis (0.264); open-angle glaucoma (0.262); male reproductive system disorder (0.260)
- **Europe PMC papers**: 304
- **Why important**: SEPTIN7 is a central connector with links to RRBP1, EIF4A2, CANX, NARS1, and ACLY. Its known septin and GTP-binding biology, cytoskeletal localization, roles in cytokinesis, cilium assembly, and embryonic cell shape, together with its high-confidence STRING relationship with SEPTIN2 and membership in hu.MAP complex C1, provide the clearest validated complex-level structure in the module. Its literature base and disease associations also support biological importance.
- **Conclusion**: Established evidence supports SEPTIN7 as a structural septin-complex component and as a likely partner of SEPTIN2. It is a credible marker of cytoskeletal organization within the module. The possibility that septin remodeling couples ER organization to trophoblast or stem-cell behavior remains a hypothesis.

#### SLC2A1

- **Related proteins** (co-abundance neighbors): CANX (0.88), PDIA4 (0.88), PLIN3 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 2 member 1. This gene encodes a major glucose transporter in the mammalian blood-brain barrier. The encoded protein is found primarily in the cell membrane and on the cell surface, where it can also function as a receptor for human T-cell leukemia virus (HTLV) I and II. Mutations in this gene have been found in a family with paroxysmal exertion-induced dyskinesia. [provided by RefSeq, Apr 2013].
- **Diseases (Open Targets)**: encephalopathy due to GLUT1 deficiency (0.852); childhood onset GLUT1 deficiency syndrome 2 (0.833); dystonia 9 (0.804); hereditary cryohydrocytosis with reduced stomatin (0.778); idiopathic generalized epilepsy (0.757)
- **Europe PMC papers**: 14405
- **Why important**: SLC2A1 connects CANX and PDIA4 to PLIN3 and is tissue enhanced in placenta, with cell-type enhancement in several trophoblast populations. Its plasma-membrane localization and role as a major glucose transporter provide a metabolic explanation for coordinated abundance in an active placental or stem-cell state. It has a very substantial literature base and strong disease associations involving GLUT1 deficiency and related neurological phenotypes.
- **Conclusion**: Established evidence supports SLC2A1 as a placental and trophoblast-relevant glucose transport component and as a network bridge to ER and lipid genes. It may report metabolic demand in the shared state. It is not established that SLC2A1 mechanistically controls the other module branches.

#### TF

- **Related proteins** (co-abundance neighbors): PLIN3 (0.84), ANXA3 (0.83), EIF4A2 (0.83), NARS1 (0.83), RRBP1 (0.81), RTN4 (0.81); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transferrin. This gene encodes a glycoprotein with an approximate molecular weight of 76.5 kDa. It is thought to have been created as a result of an ancient gene duplication event that led to generation of homologous C and N-terminal domains each of which binds one ion of ferric iron. The function of this protein is to transport iron from the intestine, reticuloendothelial system, and liver parenchymal cells t…
- **Diseases (Open Targets)**: atransferrinemia (0.776); alcohol drinking (0.492); hemochromatosis type 1 (0.471); neurodegenerative disease (0.400); urolithiasis (0.329)
- **Europe PMC papers**: 143656
- **Why important**: TF is a highly connected module member linking PLIN3, ANXA3, EIF4A2, NARS1, RRBP1, and RTN4. It is a secreted blood protein that transports iron to proliferating cells, with group-enriched HPA expression in liver and retina and no detection in immune cells. Its very extensive literature and strong disease associations make it biologically prominent, while its inclusion raises the possibility of extracellular nutrient or sample-environment contributions to the module.
- **Conclusion**: Established evidence supports TF as a circulating iron-transport protein and as a connected, non-immune module member. Its presence does not by itself establish that the module is blood-derived, because most members are not secreted and HPA indicates low immune specificity for most genes. A contribution from extracellular iron availability or sample composition remains a hypothesis.

## Module 3

**Tissue pair**: placenta and stem_cells  
**Genes (13)**: ACO2, AHNAK, ANXA4, COPB1, CTNNA1, EEA1, FHL1, HBA1, IQGAP1, MYOF, PLEC, SEC23A, TLN1

### Function

The module is most consistent with a membrane–cytoskeleton and intracellular-vesicle organization program rather than a narrowly defined pathway. MYOF, AHNAK, PLEC, TLN1, CTNNA1 and IQGAP1 connect membrane-associated structures, cell junctions, actin or intermediate filaments, adhesion, and mechanosensitive signaling. EEA1, SEC23A and COPB1 support early-endosomal, secretory-pathway and Golgi trafficking functions, while ANXA4 supports calcium-dependent membrane-associated processes. ACO2 may contribute a mitochondrial energy component, and FHL1 is compatible with muscle-associated structural biology. However, no GO or KEGG term passed global correction; therefore the functional interpretation is based on the individual gene annotations and network architecture, not on globally significant enrichment.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and many are detected in placenta, which supports a broadly expressed structural or trafficking signal in the placental samples. There is nevertheless a strong epithelial, muscle-associated and cell-junction flavor, including enrichment signals for skeletal muscle, tongue, urothelial or esophageal cells, and syncytiotrophoblasts. HBA1 is distinctly blood-cell-associated and is not detected in placenta, so it may represent erythrocyte or blood contamination rather than the core placental program. The HPA pattern does not support a predominantly immune-cell module, although isolated immune-cell associations occur. Because the stem-cell samples have no matching HPA tissue protein measurements, tissue-sharing should not be equated with demonstrated protein expression in stem cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a partial, internally coherent interaction backbone. AHNAK is linked to MYOF and PLEC; the CTNNA1–IQGAP1, CTNNA1–TLN1, IQGAP1–TLN1 and PLEC–TLN1 relationships connect adhesion and cytoskeletal proteins. These are already known protein associations and support the interpretation of a membrane–adhesion–cytoskeleton axis. The remaining module edges are not represented by high-confidence STRING interactions, so the co-abundance network is broader than the established physical or functional interaction network. No hu.MAP complex contains multiple members of this module. Thus the module is not evidence for a known stable multiprotein complex; it may instead reflect coordinated cell state, compartmental organization, or shared cellular composition.

**STRING interactions (score >= 0.7)**: 6 of 78 gene pairs: AHNAK–MYOF (0.849); AHNAK–PLEC (0.73); CTNNA1–IQGAP1 (0.859); CTNNA1–TLN1 (0.76); IQGAP1–TLN1 (0.893); PLEC–TLN1 (0.706)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a new tissue-pair co-abundance observation, but the available evidence does not establish that it is a newly discovered biological mechanism. Several component relationships and gene functions are already well established, especially those involving talin, plectin, catenin, IQGAP1, AHNAK and myoferlin. The absence of a multi-member hu.MAP complex and the partial STRING coverage indicate that this particular gene combination and cross-tissue co-abundance pattern is not simply a catalogued complex, but absence from those resources cannot prove novelty. A defensible novelty claim would require comparison with published placenta and stem-cell co-expression modules, independent cohorts, and cell-composition-controlled analyses.

**Hypothesis.** Hypothesis: the conserved module reflects a shared structural and trafficking state in placental and stem-cell-related samples. A membrane-repair and vesicle-trafficking axis involving MYOF, EEA1, SEC23A, COPB1 and ANXA4 may be coordinated with an adhesion and cytoskeletal scaffold involving TLN1, PLEC, AHNAK, CTNNA1 and IQGAP1. This state could support cell spreading, junction remodeling, membrane turnover and resistance to mechanical stress. FHL1 and ACO2 may indicate a muscle-like or energetically demanding cell state, whereas HBA1 may instead mark variable blood contribution. This is a testable hypothesis, not an established pathway assignment: it should be evaluated by single-cell or spatial measurements, removal or adjustment for erythrocyte content, and perturbation of membrane-trafficking or adhesion components.

### Important genes

#### MYOF

- **Related proteins** (co-abundance neighbors): IQGAP1 (0.95), FHL1 (0.87), COPB1 (0.87), EEA1 (0.87), CTNNA1 (0.86); STRING partners: AHNAK (0.849)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Plasma membrane, Centriolar satellite; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myoferlin. Mutations in dysferlin, a protein associated with the plasma membrane, can cause muscle weakness that affects both proximal and distal muscles. The protein encoded by this gene is a type II membrane protein that is structurally similar to dysferlin. It is a member of the ferlin family and associates with both plasma and nuclear membranes. The protein contains C2 domains that play a role in calcium…
- **Diseases (Open Targets)**: hereditary angioedema (0.443); neurodegenerative disease (0.413); cervical carcinoma (0.134); type 2 diabetes mellitus (0.131); neoplasm (0.112)
- **Europe PMC papers**: 1200
- **Why important**: MYOF has the strongest network position and connects IQGAP1, FHL1, COPB1, EEA1 and CTNNA1. Its ferlin-family membrane role and association with calcium-mediated membrane fusion and plasma-membrane repair make it a central bridge between trafficking and structural biology. It also has substantial literature coverage and disease links involving muscle, neurodegeneration, vascular permeability and cancer-related conditions.
- **Conclusion**: Established evidence supports MYOF as a central membrane-repair and membrane-trafficking candidate in this module. It is plausible, but not proven, that MYOF coordinates the module's shared co-abundance state.

#### TLN1

- **Related proteins** (co-abundance neighbors): PLEC (0.91), AHNAK (0.82); STRING partners: CTNNA1 (0.76), IQGAP1 (0.893), PLEC (0.706)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 is connected in STRING to CTNNA1, IQGAP1 and PLEC, placing it at the adhesion–cytoskeleton interface. Its annotation directly supports integrin activation, cell adhesion, actin organization, cell junction assembly and migration. HPA links it to focal adhesions and to megakaryocyte or platelet cell states, while its disease associations and literature base are substantial.
- **Conclusion**: Established evidence identifies TLN1 as a core adhesion and force-transmission component. The hypothesis that it organizes the module's structural arm is consistent with the data but requires direct validation in the relevant cells.

#### PLEC

- **Related proteins** (co-abundance neighbors): TLN1 (0.91), AHNAK (0.80); STRING partners: AHNAK (0.73), TLN1 (0.706)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plectin. Plectin is a prominent member of an important family of structurally and in part functionally related proteins, termed plakins or cytolinkers, that are capable of interlinking different elements of the cytoskeleton. Plakins, with their multi-domain structure and enormous size, not only play crucial roles in maintaining cell and tissue integrity and orchestrating dynamic changes in cytoarchitecture…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 5B, with muscular dystrophy (0.796); epidermolysis bullosa simplex 5A, Ogna type (0.775); autosomal recessive limb-girdle muscular dystrophy type 2Q (0.768); epidermolysis bullosa simplex 5C, with pyloric atresia (0.755); epidermolysis bullosa simplex with nail dystrophy (0.695)
- **Europe PMC papers**: 2578
- **Why important**: PLEC links intermediate filaments with the TLN1 and AHNAK portion of the network. Its plakin function provides a mechanistic connection between cytoskeletal systems, cell shape and tissue integrity. HPA shows skeletal-muscle association and urothelial cell enhancement, and its disease associations include skin fragility and muscular dystrophy, with a substantial literature.
- **Conclusion**: Established evidence supports PLEC as a structural scaffold that could stabilize the adhesion and membrane-repair machinery. Its participation in a specific placenta–stem-cell mechanism remains a hypothesis.

#### AHNAK

- **Related proteins** (co-abundance neighbors): EEA1 (0.85), TLN1 (0.82), PLEC (0.80); STRING partners: MYOF (0.849), PLEC (0.73)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: AHNAK nucleoprotein. The protein encoded by this gene is a large (700 kDa) structural scaffold protein consisting of a central domain with 128 aa repeats. The encoded protein may play a role in such diverse processes as blood-brain barrier formation, cell structure and migration, cardiac calcium channel regulation, and tumor metastasis. A much shorter variant encoding a 17 kDa isoform exists for this gene, and the sho…
- **Diseases (Open Targets)**: Aganglionic megacolon (0.266); neoplasm (0.108); hepatocellular carcinoma (0.093); cancer (0.085); melanoma (0.085)
- **Europe PMC papers**: 2886
- **Why important**: AHNAK is a large membrane and cytosolic scaffold connected to EEA1, TLN1 and PLEC, and STRING also links it to MYOF. Its documented roles in membrane repair, cell structure, migration and calcium-channel regulation make it a plausible organizing bridge. HPA places it in plasma membrane and cytosolic compartments, and it has broad disease-related literature.
- **Conclusion**: Established evidence supports AHNAK as a scaffold connecting membrane-associated and cytoskeletal processes. Its proposed role as an organizer of this conserved module is plausible but not demonstrated by the co-abundance data alone.

#### SEC23A

- **Related proteins** (co-abundance neighbors): FHL1 (0.83), EEA1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A connects FHL1 with EEA1 in the module and supplies a distinct secretory-pathway component. Its COPII function supports export from the endoplasmic reticulum toward the Golgi, protein trafficking and cargo loading. It has a recognizable disease association and enough literature to provide independent functional support, despite its modest network position.
- **Conclusion**: Established evidence supports SEC23A as a trafficking component that broadens the module beyond adhesion and cytoskeletal organization. It may couple biosynthetic cargo transport to membrane remodeling, but that coupling is a hypothesis.

#### CTNNA1

- **Related proteins** (co-abundance neighbors): MYOF (0.86); STRING partners: IQGAP1 (0.859), TLN1 (0.76)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin alpha 1. This gene encodes a member of the catenin family of proteins that play an important role in cell adhesion process by connecting cadherins located on the plasma membrane to the actin filaments inside the cell. The encoded mechanosensing protein contains three vinculin homology domains and undergoes conformational changes in response to cytoskeletal tension, resulting in the reconfiguration of cadhe…
- **Diseases (Open Targets)**: Butterfly-shaped pigment dystrophy (0.750); hereditary neoplastic syndrome (0.557); hereditary diffuse gastric adenocarcinoma (0.555); colorectal cancer (0.506); exudative vitreoretinopathy (0.390)
- **Europe PMC papers**: 2688
- **Why important**: CTNNA1 occupies a membrane-junction position and is linked by STRING to IQGAP1 and TLN1. Its established role is to connect cadherin-based adhesion to actin and to respond to cytoskeletal tension. HPA places it at plasma membranes and cell junctions, and it has substantial literature and disease associations including inherited pigmentary and neoplastic disorders.
- **Conclusion**: Established evidence supports CTNNA1 as a junctional mechanosensing component. Its presence strengthens the interpretation of a cell-adhesion and force-responsive module, while any direct causal role in conservation across the two tissue groups remains untested.

## Module 4

**Tissue pair**: placenta and stem_cells  
**Genes (6)**: AKR1B1, EZR, HEXB, LAMC1, NAGK, TGM2

### Function

This is a provisional placenta- and stem-cell-shared module associated with trophoblast-linked cell biology, extracellular-matrix organization, cell adhesion, and carbohydrate or amino-sugar processing. TGM2 is the network hub and connects the other module components, while the HEXB–NAGK relationship is the only high-confidence STRING interaction. The gene annotations support roles for TGM2 in protein crosslinking, apoptosis, and extracellular-matrix organization; for LAMC1 in basement-membrane biology, adhesion, migration, and signaling; for EZR in membrane–actin linkage and cell shape; and for HEXB and NAGK in lysosomal glycan degradation and amino-sugar metabolism. No GO/KEGG term passed global correction, and there was no supplementary STRING functional-enrichment result. Thus, the functional interpretation is biologically coherent but not statistically established by enrichment testing.

**Cell composition.** The module is not dominated by blood-cell-enriched genes: HPA reports low immune-cell specificity for most annotated genes and no frequent enriched blood-cell type, with some genes not detected in immune cells. It does contain a substantial secreted or extracellular-matrix component, notably TGM2 and LAMC1, while the remaining proteins are mainly cytosolic, membrane-associated, or intracellular. All genes have cell-type-enhanced HPA profiles, especially syncytiotrophoblasts, with additional cytotrophoblast, migrating or extravillous trophoblast, and Hofbauer-cell signals. Placental protein detection is broad, whereas HPA provides no matching stem-cell tissue assessment. The shared signal therefore may reflect a trophoblast-associated cellular program rather than a generic blood contamination signature, although cellular composition remains a possible contributor.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports one specific relationship within the module: HEXB–NAGK is a high-confidence interaction. No other listed pair has a STRING partner annotation, and STRING functional enrichment is absent. No hu.MAP complex contains multiple module members. Accordingly, the network has one externally supported biochemical connection centered on amino-sugar biology, whereas the links from TGM2 to HEXB, NAGK, EZR, AKR1B1, and LAMC1 are co-abundance relationships rather than established physical interactions. The network may therefore capture coordinated cellular state or shared regulation more than a known multiprotein complex.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: HEXB–NAGK (0.913)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be claimed as a wholly new molecular pathway. Its component functions are well established, TGM2, EZR, AKR1B1, and LAMC1 have substantial literature support, and the HEXB–NAGK relationship is already represented in STRING. The absence of a multi-member hu.MAP complex and the limited STRING connectivity suggest that the particular cross-tissue co-abundance configuration may be under-characterized, but database absence alone cannot establish novelty. A cautious conclusion is that the shared placenta–stem-cell module is a potentially novel co-expression or co-abundance configuration built from largely known proteins, requiring validation in independent cohorts and with cell-composition controls.

**Hypothesis.** Hypothesis: trophoblast-associated cells coordinate extracellular-matrix remodeling and membrane organization with glycan turnover and redox or carbohydrate metabolism during tissue interaction and differentiation. In this model, TGM2 provides a central extracellular-matrix and cell-state interface, LAMC1 supplies basement-membrane structure, and EZR links membrane organization to the cytoskeleton. HEXB and NAGK could reflect coordinated amino-sugar and lysosomal glycan handling, with their known STRING relationship providing the strongest external support. AKR1B1 may mark a metabolic component of the same state. This is a mechanistic proposal, not a demonstrated causal pathway, because enrichment was not globally significant and most network edges lack independent interaction support.

### Important genes

#### TGM2

- **Related proteins** (co-abundance neighbors): NAGK (0.88), HEXB (0.83), EZR (0.81), AKR1B1 (0.81), LAMC1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transglutaminase 2. Transglutaminases are enzymes that catalyze the crosslinking of proteins by epsilon-gamma glutamyl lysine isopeptide bonds. While the primary structure of transglutaminases is not conserved, they all have the same amino acid sequence at their active sites and their activity is calcium-dependent. The protein encoded by this gene acts as a monomer, is induced by retinoic acid, and appears to be invo…
- **Diseases (Open Targets)**: neurodegenerative disease (0.495); autoimmune disorder of central nervous system (0.324); placental abruption (0.297); arterial embolism (0.266); seborrheic dermatitis (0.251)
- **Europe PMC papers**: 4586
- **Why important**: TGM2 is the network hub, connected to every other module member, and is annotated as a calcium-dependent protein-crosslinking enzyme involved in extracellular-matrix organization and apoptotic regulation. Its placenta detection, blood-vessel enhancement, extracellular-matrix secretion, disease associations including placental abruption, and extensive literature make it the strongest organizing candidate.
- **Conclusion**: Established: TGM2 has central network position and documented roles in protein crosslinking, matrix biology, apoptosis, and placenta-associated disease. Hypothesis: TGM2 may coordinate the module's extracellular and intracellular arms, but its causal role in the shared co-abundance pattern remains unproven.

#### HEXB

- **Related proteins** (co-abundance neighbors): NAGK (0.86), TGM2 (0.83); STRING partners: NAGK (0.913)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hexosaminidase subunit beta. Hexosaminidase B is the beta subunit of the lysosomal enzyme beta-hexosaminidase that, together with the cofactor GM2 activator protein, catalyzes the degradation of the ganglioside GM2, and other molecules containing terminal N-acetyl hexosamines. Beta-hexosaminidase is composed of two subunits, alpha and beta, which are encoded by separate genes. Both beta-hexosaminidase alpha and beta subunits …
- **Diseases (Open Targets)**: Sandhoff disease (0.839); Sandhoff disease, infantile form (0.570); Sandhoff disease, adult form (0.551); Sandhoff disease, juvenile form (0.551); hereditary disease (0.488)
- **Europe PMC papers**: 337027
- **Why important**: HEXB participates in lysosomal degradation of ganglioside and other terminal N-acetylhexosamine-containing molecules, and it forms the module's only high-confidence STRING pair with NAGK. It has strong trophoblast and Hofbauer-cell enhancement, a placenta-relevant cellular profile, a major disease association with Sandhoff disease, and by far the deepest literature base among the module genes.
- **Conclusion**: Established: HEXB is a lysosomal glycan-processing enzyme and its relationship with NAGK is independently supported by STRING. Hypothesis: HEXB may report coordinated glycan turnover in trophoblast-associated cells, but the co-abundance data do not establish altered lysosomal function.

#### NAGK

- **Related proteins** (co-abundance neighbors): TGM2 (0.88), HEXB (0.86); STRING partners: HEXB (0.913)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-acetylglucosamine kinase. This gene encodes a member of the N-acetylhexosamine kinase family. The encoded protein catalyzes the conversion of N-acetyl-D-glucosamine to N-acetyl-D-glucosamine 6-phosphate, and is the major mammalian enzyme which recovers amino sugars. [provided by RefSeq, Nov 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.201); response to xenobiotic stimulus (0.107); neoplasm (0.086); maturity-onset diabetes of the young (0.078); transient neonatal diabetes mellitus (0.062)
- **Europe PMC papers**: 836
- **Why important**: NAGK is a cytosolic amino-sugar kinase and is the partner of HEXB in the only supported STRING interaction. Its trophoblast and Hofbauer-cell enhancement connects the metabolic interpretation to the relevant cellular context. Although it is less central and less literature-rich than TGM2 or HEXB, it provides a plausible metabolic link within the module.
- **Conclusion**: Established: NAGK recovers amino sugars and is linked to HEXB by STRING. Hypothesis: NAGK could couple cytosolic amino-sugar salvage to lysosomal glycan breakdown in the shared cellular state, but this coupling is not demonstrated by the module alone.

#### LAMC1

- **Related proteins** (co-abundance neighbors): TGM2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Plasma membrane; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit gamma 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: Fuchs' endothelial dystrophy (0.487); prostate carcinoma (0.467); colorectal cancer (0.447); eye disorder (0.434); benign colon neoplasm (0.427)
- **Europe PMC papers**: 4227
- **Why important**: LAMC1 is a placenta-enhanced extracellular-matrix protein and a laminin subunit, with documented roles in basement membranes, adhesion, migration, differentiation, and signaling. Its direct co-abundance link to the TGM2 hub and its broad literature support make it the clearest structural representative of the matrix arm of the module.
- **Conclusion**: Established: LAMC1 contributes to laminin and basement-membrane biology and is detected in placenta. Hypothesis: coordinated LAMC1 and TGM2 abundance may reflect matrix remodeling during trophoblast adhesion or migration, but no physical interaction between them is established here.

#### EZR

- **Related proteins** (co-abundance neighbors): TGM2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ezrin. The cytoplasmic peripheral membrane protein encoded by this gene functions as a protein-tyrosine kinase substrate in microvilli. As a member of the ERM protein family, this protein serves as an intermediate between the plasma membrane and the actin cytoskeleton. This protein plays a key role in cell surface structure adhesion, migration and organization, and it has been implicated in various human…
- **Diseases (Open Targets)**: hair color (0.477); non-small cell lung carcinoma (0.397); lung adenocarcinoma (0.382); autosomal recessive non-syndromic intellectual disability (0.370); glaucoma (0.347)
- **Europe PMC papers**: 4982
- **Why important**: EZR is the membrane–actin interface member of the module and is connected directly to TGM2. Its annotations support roles in cell-surface structure, adhesion, migration, organization, and cell shape, while its HPA profile includes syncytiotrophoblast enhancement and placental protein detection. Its peripheral network position is informative because it may connect the matrix-associated hub to cell architecture.
- **Conclusion**: Established: EZR links the plasma membrane to the actin cytoskeleton and is associated with cell shape and adhesion. Hypothesis: EZR may translate TGM2- and LAMC1-associated matrix changes into trophoblast morphology or migration, but that direction of regulation is not shown.

## Module 5

**Tissue pair**: placenta and stem_cells  
**Genes (13)**: B2M, C1QBP, CAPN2, CD44, COL18A1, CSRP1, FN1, FLNC, LGALS1, PXDN, S100A11, TAGLN2, VIM

### Function

The module is most consistent with a placenta- and stem-cell-associated extracellular-matrix, cell-adhesion, migration, and cytoskeletal-remodelling program. This interpretation is supported by the annotations of FN1, CD44, VIM, LGALS1, PXDN, COL18A1, FLNC, CSRP1, CAPN2, TAGLN2, and S100A11, which collectively involve cell adhesion, cell-matrix adhesion, migration, actin or intermediate-filament organization, angiogenesis, extracellular-matrix formation, and smooth-muscle or stromal behavior. The network topology places FLNC and FN1 near the center of the module, with FN1 connecting several extracellular or adhesion-related genes and FLNC connecting matrix, membrane, and cytoskeletal components. However, no GO or KEGG term passed global correction; therefore, this is a gene- and network-based functional interpretation, not a claim of globally significant pathway enrichment. B2M and C1QBP add a possible antigen-presentation, complement-regulatory, or cellular-stress context, but they do not establish an immune function for the whole module.

**Cell composition.** The module is strongly skewed toward stromal, vascular, trophoblast, and extracellular-matrix biology rather than a blood-cell program. HPA identifies many genes as cell-type enhanced in extravillous trophoblasts, decidual stromal cells, hepatic stellate cells, vascular or smooth-muscle cells, and fibroblast-like populations. Several proteins are secreted or extracellular-matrix associated, including FN1, PXDN, COL18A1, and secreted-to-blood proteins such as CD44, LGALS1, B2M, and C1QBP. FN1 and several other genes are tissue enhanced in blood vessel, liver, or placenta. Most genes have low immune-cell specificity or are not detected in immune cells, although S100A11 and COL18A1 have neutrophil-related HPA signals and B2M is broadly linked to nucleated-cell MHC class I biology. The module could therefore reflect shared vascular, stromal, or trophoblast composition in the tissues, with a possible contribution from extracellular proteins present in blood or tissue fluids. Placental protein detection is present for many module genes, whereas there is no matching HPA tissue category for stem cells, so the stem-cell interpretation should be treated cautiously.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a compact extracellular-matrix and adhesion core: FN1 is linked to CD44, COL18A1, LGALS1, PXDN, and VIM, while LGALS1 is linked to VIM and CD44 is linked to VIM. These are established database-supported relationships and are concordant with the proposed matrix, adhesion, and cytoskeletal interpretation. The module also contains high-confidence co-abundance edges involving FLNC, CSRP1, CAPN2, TAGLN2, B2M, and C1QBP, but several of these genes have no reported STRING partners within the supplied evidence. No STRING functional-enrichment result was available, so STRING supports selected pairwise relationships rather than a globally corrected functional category. No hu.MAP complex contains multiple module members. Thus, the module appears to combine a known FN1-centered interaction neighborhood with additional co-abundance relationships that may reflect shared cell state, tissue composition, or regulation rather than one established physical complex.

**STRING interactions (score >= 0.7)**: 7 of 78 gene pairs: CD44–FN1 (0.999); CD44–VIM (0.809); COL18A1–FN1 (0.838); FN1–LGALS1 (0.878); FN1–PXDN (0.853); FN1–VIM (0.809); LGALS1–VIM (0.879)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is not established as a wholly new molecular pathway. The FN1, CD44, VIM, LGALS1, PXDN, and COL18A1 relationships are already represented in STRING, and the functions of matrix adhesion, trophoblast or stromal biology, cytoskeletal organization, and vascular remodeling are well established. Nevertheless, the conserved co-abundance module shared by placenta and stem cells may be a new systems-level observation, especially because no matching hu.MAP complex is present and the module combines matrix, cytoskeletal, trophoblast, stromal, and limited immune-context genes. Absence from hu.MAP or from parts of STRING cannot by itself establish novelty. A defensible novelty claim is therefore limited to the particular cross-tissue co-abundance configuration and its reproducibility, not to the individual genes or their pairwise biology.

**Hypothesis.** Hypothesis: a shared extravillous-trophoblast or stromal-like state in placenta and stem-cell samples induces coordinated extracellular-matrix deposition, cell-surface adhesion, and cytoskeletal remodeling. FN1 could provide an extracellular scaffold, CD44 could couple matrix or hyaluronan signals to the cell surface, VIM and FLNC could transmit adhesion and mechanical cues through intermediate-filament and actin networks, and LGALS1, PXDN, and COL18A1 could modify matrix organization, crosslinking, or vascular behavior. CSRP1, CAPN2, TAGLN2, and S100A11 may support contractility, calcium-responsive remodeling, and migration. B2M and C1QBP may reflect a parallel stress, antigen-presentation, or complement-regulatory context rather than the central mechanism. This hypothesis requires validation with cell-composition controls, protein-level measurements, spatial localization, and perturbation of matrix or adhesion components.

### Important genes

#### FN1

- **Related proteins** (co-abundance neighbors): PXDN (0.89), LGALS1 (0.88), VIM (0.85), FLNC (0.82), CSRP1 (0.82), TAGLN2 (0.82); STRING partners: CD44 (0.999), COL18A1 (0.838), LGALS1 (0.878), PXDN (0.853), VIM (0.809)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 has a central position in the supplied module network and connects to PXDN, LGALS1, VIM, FLNC, CSRP1, and TAGLN2. It is a secreted extracellular-matrix glycoprotein detected in placenta, enriched in blood vessel, liver, and placenta, and associated with extravillous trophoblasts, fibroblasts, hepatic stellate cells, and hepatocytes. Its established functions include cell adhesion, cell-matrix adhesion, migration, embryogenesis, wound healing, and integrin-mediated signaling. It also has extensive literature and disease evidence, making it the strongest integrative anchor for this module.
- **Conclusion**: Established evidence supports FN1 as a central extracellular-matrix and adhesion component of the module. Its centrality and placenta-associated detection make it a strong candidate driver or marker, but co-abundance does not prove that FN1 causally organizes the module.

#### FLNC

- **Related proteins** (co-abundance neighbors): LGALS1 (0.94), CSRP1 (0.86), CAPN2 (0.85), PXDN (0.85), CD44 (0.83), B2M (0.83), FN1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin C. This gene encodes one of three related filamin genes, specifically gamma filamin. These filamin proteins crosslink actin filaments into orthogonal networks in cortical cytoplasm and participate in the anchoring of membrane proteins for the actin cytoskeleton. Three functional domains exist in filamin: an N-terminal filamentous actin-binding domain, a C-terminal self-association domain, and a membr…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy 26 (0.833); myofibrillar myopathy 5 (0.791); distal myopathy with posterior leg and anterior hand involvement (0.742); dilated cardiomyopathy (0.714); familial restrictive cardiomyopathy (0.660)
- **Europe PMC papers**: 3861
- **Why important**: FLNC has the strongest supplied network position and connects matrix, adhesion, and cytoskeletal genes including LGALS1, CSRP1, CAPN2, PXDN, CD44, B2M, and FN1. It encodes an actin-crosslinking and membrane-protein-anchoring filamin, with annotations involving actin-cytoskeleton and sarcomere organization and muscle-cell development. HPA links it to smooth-muscle and muscle-related cell types, while disease evidence includes cardiomyopathies and myofibrillar myopathy. Its substantial literature makes the cytoskeletal interpretation biologically grounded.
- **Conclusion**: Established evidence supports FLNC as a cytoskeletal integration point and a plausible mediator of mechanical coupling. Its absence from the supplied STRING partner list means the module edge pattern should not be interpreted as a pre-existing FLNC physical complex.

#### CD44

- **Related proteins** (co-abundance neighbors): CAPN2 (0.89), FLNC (0.83), S100A11 (0.82), CSRP1 (0.80); STRING partners: FN1 (0.999), VIM (0.809)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD44 molecule (IN blood group). The protein encoded by this gene is a cell-surface glycoprotein involved in cell-cell interactions, cell adhesion and migration. It is a receptor for hyaluronic acid (HA) and can also interact with other ligands, such as osteopontin, collagens, and matrix metalloproteinases (MMPs). This protein participates in a wide variety of cellular functions including lymphocyte activation, recirculation and …
- **Diseases (Open Targets)**: nephrolithiasis, calcium oxalate (0.523); calcium oxalate urolithiasis (0.521); uterine corpus leiomyoma (0.480); systemic lupus erythematosus (0.467); autoimmune disease (0.330)
- **Europe PMC papers**: 102058
- **Why important**: CD44 connects to CAPN2, FLNC, S100A11, and CSRP1 in the co-abundance network and has high-confidence STRING links to FN1 and VIM. It is a plasma-membrane glycoprotein and receptor for hyaluronic acid that participates in cell adhesion, migration, cell-matrix adhesion, and interactions with collagen, osteopontin, and matrix metalloproteinases. HPA detects it in placenta and identifies it in extravillous trophoblasts as well as several immune-related cell types. Its large literature and broad disease associations make it an important interface between matrix sensing and cell behavior.
- **Conclusion**: Established evidence supports CD44 as a cell-surface matrix-sensing component. Its immune and trophoblast expression means it could mark either a genuine adhesion program or changing cellular composition; causal involvement remains a hypothesis.

#### VIM

- **Related proteins** (co-abundance neighbors): FN1 (0.85); STRING partners: CD44 (0.809), FN1 (0.809), LGALS1 (0.879)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vimentin. This gene encodes a type III intermediate filament protein. Intermediate filaments, along with microtubules and actin microfilaments, make up the cytoskeleton. The encoded protein is responsible for maintaining cell shape and integrity of the cytoplasm, and stabilizing cytoskeletal interactions. This protein is involved in neuritogenesis and cholesterol transport and functions as an organizer of a…
- **Diseases (Open Targets)**: dengue disease (0.516); early-onset non-syndromic cataract (0.462); early-onset partial cataract (0.458); Developmental cataract (0.435); cataract (0.372)
- **Europe PMC papers**: 86568
- **Why important**: VIM is linked in STRING to FN1, LGALS1, and CD44 and is HPA tissue enhanced in blood vessel and detected in placenta. It encodes an intermediate-filament protein that maintains cell shape and cytoplasmic integrity and organizes proteins involved in attachment, migration, and signaling. Its single-cell associations include decidual stromal cells, fibroblasts, hepatic stellate cells, and other mesenchymal or vascular-related populations. The extensive literature supports its value as a marker and mechanistic candidate for mesenchymal remodeling.
- **Conclusion**: Established evidence supports VIM as a structural and migration-associated component of a stromal or vascular state. Because VIM is broadly expressed and often state-associated, its module membership alone does not establish a specific placenta-to-stem-cell mechanism.

#### LGALS1

- **Related proteins** (co-abundance neighbors): FLNC (0.94), FN1 (0.88), CSRP1 (0.86); STRING partners: FN1 (0.878), VIM (0.879)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galectin 1. The galectins are a family of beta-galactoside-binding proteins implicated in modulating cell-cell and cell-matrix interactions. This gene product may act as an autocrine negative growth factor that regulates cell proliferation. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: glaucoma (0.349); open-angle glaucoma (0.343); chronic kidney disease (0.330); smoking initiation (0.162); melanoma (0.121)
- **Europe PMC papers**: 4025
- **Why important**: LGALS1 connects to FLNC, FN1, and CSRP1 in the module and to FN1 and VIM in STRING. It is a beta-galactoside-binding protein involved in cell-cell and cell-matrix interactions, proliferation, apoptosis-related signaling, and NF-kappaB regulation. HPA identifies it in decidual stromal cells, endometrial stromal cells, extravillous trophoblasts, and fibroblasts, and detects it in placenta; it is also secreted to blood. Its literature supports a role at the interface of matrix signaling, trophoblast or stromal biology, and immune modulation.
- **Conclusion**: Established evidence supports LGALS1 as a secreted or cytosolic matrix-interaction and signaling component. Its broad regulatory roles make it a plausible modulator of the module, but the supplied data cannot determine whether it is a driver or a consequence of the shared cellular state.

## Module 6

**Tissue pair**: placenta and stem_cells  
**Genes (8)**: BASP1, COL12A1, FLNA, FLNB, PDLIM7, SPTBN1, SPTAN1, TPM1

### Function

The module is most consistent with a structural cell-interface program centered on actin organization, membrane anchoring, spectrin scaffolding, focal-adhesion or junctional integrity, and extracellular-matrix coupling. FLNB is the central co-abundance hub, linking the filamin pair, the spectrin pair, TPM1, BASP1, and the COL12A1–PDLIM7 branch. The biological interpretation is supported by the gene descriptions and by the recurrent hu.MAP complexes (hu.MAP huMAP3_07940.1), (hu.MAP huMAP3_05473.1), and (hu.MAP huMAP3_09165.1), all of which contain BASP1, SPTBN1, and SPTAN1. No GO or KEGG term passed global correction, so the functional interpretation is network- and annotation-based rather than enrichment-confirmed. The module may therefore reflect coordinated cytoskeletal and matrix organization in shared placental and stem-cell-associated stromal, vascular, contractile, or trophoblast-related populations.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. COL12A1 is the clear extracellular-matrix secreted component, whereas the other genes are mainly cytoskeletal, membrane-associated, or intracellular scaffolds. HPA shows broad tissue and cell-type enhancement rather than a single narrowly restricted lineage: stromal, vascular, smooth-muscle, myoepithelial, trophoblast, and related cell types are represented. Several genes have blood-cell-associated signals, including neutrophil, basophil, eosinophil, or megakaryocyte associations, and BASP1 is immune-cell enriched, so contribution from blood or shared immune-contaminating cells cannot be excluded. However, the overall profile does not support a purely blood-cell module because many members have low immune-cell specificity and the dominant biological theme is structural. Protein detection in placenta is widespread, while there is no matching HPA tissue category for stem_cells, limiting direct cross-tissue protein comparison.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides strong known support for the FLNA–FLNB relationship and for the SPTAN1–SPTBN1 relationship. These interactions independently support a filamin-based and spectrin-based cytoskeletal interpretation, but STRING does not provide enrichment support for the module. hu.MAP identifies the recurring BASP1–SPTBN1–SPTAN1 combination in (hu.MAP huMAP3_07940.1), (hu.MAP huMAP3_05473.1), and (hu.MAP huMAP3_09165.1). The associated complexes also include proteins involved in membrane trafficking, actin regulation, adhesion, and signaling, which places the spectrin-associated members in a broader membrane-cytoskeleton context. The lack of hu.MAP assignment for FLNA, FLNB, COL12A1, PDLIM7, TPM1, and BASP1 outside those complexes does not imply that their co-abundance is artifactual; it indicates that the observed module combines established scaffold relationships with a potentially context-dependent matrix and contractile branch.

**STRING interactions (score >= 0.7)**: 2 of 28 gene pairs: FLNA–FLNB (0.979); SPTAN1–SPTBN1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07940.1 (BASP1, SPTBN1, SPTAN1; 3/5); huMAP3_05473.1 (BASP1, SPTBN1, SPTAN1; 3/7); huMAP3_09165.1 (BASP1, SPTBN1, SPTAN1; 3/39)

### Novelty

The exact conserved co-abundance module may represent a new tissue-pair-specific observation, because the fact sheet does not show a previously catalogued matching module or a complete known complex containing all members. Nevertheless, the underlying biology is not wholly novel: filamin, spectrin, actin, tropomyosin, focal-adhesion, and collagen-associated functions are established, and several relationships are already supported by STRING or hu.MAP. Therefore the defensible conclusion is novelty of the particular cross-tissue co-abundance configuration, not discovery of a new molecular function. Absence from STRING or hu.MAP alone cannot establish novelty, and the lack of globally significant GO or KEGG enrichment limits claims about a distinct pathway.

**Hypothesis.** Hypothesis: in placenta and stem-cell-associated populations, a shared stromal, vascular, contractile, or trophoblast-related state coordinately increases a membrane-to-actin scaffold composed of FLNA, FLNB, SPTAN1, and SPTBN1, while PDLIM7 and TPM1 stabilize actin-linked adhesion or contractile structures and COL12A1 modifies the surrounding collagen matrix. BASP1 may participate in the associated membrane or signaling complex. This could support cell shape, adhesion, migration, mechanical resilience, and matrix remodeling during tissue organization. The blood-cell-associated HPA signals raise an alternative hypothesis that part of the module reflects shared cellular composition or blood-derived material rather than a program active in every cell expressing these genes. Testing these alternatives would require cell-resolved expression, protein localization, and perturbation or interaction measurements.

### Important genes

#### FLNB

- **Related proteins** (co-abundance neighbors): SPTBN1 (0.85), COL12A1 (0.85), FLNA (0.83), SPTAN1 (0.82), TPM1 (0.81), BASP1 (0.80); STRING partners: FLNA (0.979)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin B. This gene encodes a member of the filamin family. The encoded protein interacts with glycoprotein Ib alpha as part of the process to repair vascular injuries. The platelet glycoprotein Ib complex includes glycoprotein Ib alpha, and it binds the actin cytoskeleton. Mutations in this gene have been found in several conditions: atelosteogenesis type 1 and type 3; boomerang dysplasia; autosomal domina…
- **Diseases (Open Targets)**: Larsen syndrome (0.829); spondylocarpotarsal synostosis syndrome (0.775); atelosteogenesis type I (0.763); atelosteogenesis type III (0.756); Boomerang dysplasia (0.723)
- **Europe PMC papers**: 2274
- **Why important**: FLNB is the principal network hub, connecting the filamin, spectrin, contractile, membrane-associated, and matrix-linked branches. Its established role is to link the actin cytoskeleton with membrane-associated structures, and its interaction with glycoprotein Ib alpha is relevant to vascular injury repair. It is detected in placenta and has well-established skeletal and developmental disease associations with substantial literature support.
- **Conclusion**: Established: FLNB is the strongest organizational candidate for the module and provides a coherent cytoskeletal explanation for its network structure. Hypothesis: FLNB may coordinate the module's membrane mechanics with COL12A1-dependent matrix interactions in the shared placental and stem-cell-associated state.

#### FLNA

- **Related proteins** (co-abundance neighbors): FLNB (0.83); STRING partners: FLNB (0.979)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA has a direct high-confidence STRING relationship with FLNB and is a membrane- and actin-associated crosslinker involved in cell shape, migration, integrin-linked complexes, and receptor signaling. It is tissue enhanced in blood vessel and intestine and cell-type enhanced in stromal, myoepithelial, and megakaryocyte-related populations, matching the module's structural and vascular context. It also has extensive literature and established developmental, skeletal, and neurological disease associations.
- **Conclusion**: Established: FLNA is a biologically credible partner of the central FLNB scaffold and supports a membrane-remodeling interpretation. Hypothesis: the FLNA–FLNB pair may provide the principal force-bearing interface through which this module influences adhesion or migration.

#### SPTAN1

- **Related proteins** (co-abundance neighbors): FLNB (0.82); STRING partners: SPTBN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Microtubules; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_07940.1, huMAP3_05473.1, huMAP3_09165.1
- **Function (MyGene.info)**: spectrin alpha, non-erythrocytic 1. Spectrins are a family of filamentous cytoskeletal proteins that function as essential scaffold proteins that stabilize the plasma membrane and organize intracellular organelles. Spectrins are composed of alpha and beta dimers that associate to form tetramers linked in a head-to-head arrangement. This gene encodes an alpha spectrin that is specifically expressed in nonerythrocytic cells. The encod…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 5 (0.749); developmental delay with or without epilepsy (0.681); spastic paraplegia 91, autosomal dominant, with or without cerebellar ataxia (0.681); infantile spasms (0.651); genetic developmental and epileptic encephalopathy (0.651)
- **Europe PMC papers**: 1422
- **Why important**: SPTAN1 is part of the high-confidence STRING spectrin pair with SPTBN1 and recurs with SPTBN1 and BASP1 in all reported hu.MAP complexes (hu.MAP huMAP3_07940.1), (hu.MAP huMAP3_05473.1), and (hu.MAP huMAP3_09165.1). Its established function is to form non-erythrocytic spectrin scaffolds that stabilize membranes and organize intracellular structures. Its disease associations include developmental and epileptic encephalopathy, and its literature supports important roles in neuronal and cellular architecture.
- **Conclusion**: Established: SPTAN1 is a core membrane-stabilizing scaffold with unusually consistent complex-level support in this module. Hypothesis: the SPTAN1-containing spectrin framework may transmit mechanical or trafficking-related signals between the plasma membrane and the actin network in the shared cell state.

#### SPTBN1

- **Related proteins** (co-abundance neighbors): FLNB (0.85); STRING partners: SPTAN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_07940.1, huMAP3_05473.1, huMAP3_09165.1
- **Function (MyGene.info)**: spectrin beta, non-erythrocytic 1. Spectrin is an actin crosslinking and molecular scaffold protein that links the plasma membrane to the actin cytoskeleton, and functions in the determination of cell shape, arrangement of transmembrane proteins, and organization of organelles. It is composed of two antiparallel dimers of alpha- and beta- subunits. This gene is one member of a family of beta-spectrin genes. The encoded protein cont…
- **Diseases (Open Targets)**: developmental delay, impaired speech, and behavioral abnormalities (0.802); cancer (0.597); hereditary disease (0.516); hearing loss disorder (0.459); neurodevelopmental disorder (0.453)
- **Europe PMC papers**: 1635
- **Why important**: SPTBN1 is directly linked to SPTAN1 by STRING and participates with SPTAN1 and BASP1 in (hu.MAP huMAP3_07940.1), (hu.MAP huMAP3_05473.1), and (hu.MAP huMAP3_09165.1). Its established function is to connect the plasma membrane to actin, organize membrane proteins and organelles, and contribute to vesicle-mediated transport and cytokinesis. Its cell-type enhancement in adipocytes, fibro-adipogenic progenitors, lymphatic endothelial cells, and vascular endothelial cells is compatible with the module's stromal and vascular interpretation.
- **Conclusion**: Established: SPTBN1 is a core spectrin partner and a strong candidate for the module's membrane-to-cytoskeleton organization. Hypothesis: SPTBN1 may connect the recurring hu.MAP scaffold to lineage-specific membrane trafficking or adhesion processes in placenta and stem-cell-associated populations.

#### COL12A1

- **Related proteins** (co-abundance neighbors): FLNB (0.85), PDLIM7 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type XII alpha 1 chain. This gene encodes the alpha chain of type XII collagen, a member of the FACIT (fibril-associated collagens with interrupted triple helices) collagen family. Type XII collagen is a homotrimer found in association with type I collagen, an association that is thought to modify the interactions between collagen I fibrils and the surrounding matrix. Alternatively spliced transcript variants encoding di…
- **Diseases (Open Targets)**: Bethlem myopathy 2 (0.794); Ullrich congenital muscular dystrophy 2 (0.709); Bethlem myopathy (0.617); Abnormality of the skeletal system (0.533); Ullrich congenital muscular dystrophy (0.501)
- **Europe PMC papers**: 3324
- **Why important**: COL12A1 is the module's clearest extracellular-matrix component and forms a branch with PDLIM7, while also connecting to the FLNB hub. Its established role is to associate with collagen fibrils and modify interactions between collagen and the surrounding matrix. HPA identifies it as secreted to the extracellular matrix and enhanced in stromal and fibro-adipogenic cell types, making it important for linking intracellular mechanics to extracellular structure. It also has established muscular and skeletal disease associations.
- **Conclusion**: Established: COL12A1 supplies the matrix-facing arm of an otherwise predominantly cytoskeletal module. Hypothesis: the COL12A1–PDLIM7 branch may couple extracellular matrix organization to intracellular actin mechanics, helping explain conservation across distinct tissue groups.

#### PDLIM7

- **Related proteins** (co-abundance neighbors): COL12A1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Actin filaments, Focal adhesion sites; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 7. The protein encoded by this gene is representative of a family of proteins composed of conserved PDZ and LIM domains. LIM domains are proposed to function in protein-protein recognition in a variety of contexts including gene transcription and development and in cytoskeletal interaction. The LIM domains of this protein bind to protein kinases, whereas the PDZ domain binds to actin filaments. The g…
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); nasopharyngeal carcinoma (0.121); neoplasm (0.120); lymphoma (0.115); Hodgkins lymphoma (0.105)
- **Europe PMC papers**: 808
- **Why important**: PDLIM7 is the partner of COL12A1 in the module and is localized to actin filaments and focal-adhesion sites. Its PDZ and LIM domains provide an established molecular basis for linking actin-associated structures with signaling proteins and developmental or muscle-related organization. HPA shows enhancement in blood vessel, intestine, and skeletal muscle, with cell-type associations spanning stromal, myoepithelial, hepatic stellate, megakaryocyte, and neutrophil populations.
- **Conclusion**: Established: PDLIM7 is a plausible intracellular adaptor at the matrix–focal-adhesion–actin interface. Hypothesis: PDLIM7 may stabilize or regulate the COL12A1-associated mechanical branch and thereby couple cell adhesion to the broader FLNB-centered scaffold.

