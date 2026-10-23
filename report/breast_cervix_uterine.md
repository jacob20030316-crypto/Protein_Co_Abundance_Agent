# Conserved co-abundance modules: breast and cervix_uterine

## Module 0

**Tissue pair**: breast and cervix_uterine  
**Genes (16)**: PGD, AP1B1, DHRS9, RAP1GDS1, EPHX1, LYPLA1, MYO5B, NBEAL2, NCKAP1, NSDHL, LPCAT2, PFKP, PYGB, RAB18, SH3BGRL2, RARS1

### Function

The module does not have a GO or KEGG term that passes global correction. Therefore, no pathway-level enrichment can be claimed from the primary enrichment analysis. Its structure is nevertheless biologically suggestive: DHRS9 is a highly connected central node, linked to genes involved in steroid and retinoid metabolism, cholesterol biosynthesis, glycolysis, the pentose-phosphate shunt, glycogen breakdown, membrane trafficking, cytoskeletal regulation, translation, and phospholipid metabolism. DHRS9 itself is an SDR-family oxidoreductase with reported roles in hydroxysteroid, androgen, progesterone, and retinol metabolism and epithelial differentiation. The most defensible interpretation is a co-abundance signal joining epithelial metabolic state with lipid and membrane handling, vesicle traffic, and selected immune or blood-cell programs. This is an integrative interpretation of the annotations and network topology, not a claim of statistically enriched GO or KEGG function.

**Cell composition.** The module is not dominated by secreted proteins: the HPA summary reports no secreted genes. Protein detection is broadly concordant in breast and cervix_uterine, although EPHX1, LPCAT2, and LYPLA1 show tissue-specific detection differences. The composition is mixed rather than a simple housekeeping module. HPA shows many cell-type-enhanced genes, especially esophageal epithelial categories, with additional signals in neutrophils, neutrophil progenitors, basophils, eosinophils, and monocytes. PGD and NBEAL2 are particularly compatible with blood or myeloid contributions, while MYO5B and DHRS9 are compatible with epithelial differentiation or specialized epithelial metabolism. Several genes have low tissue specificity and could reflect broadly available cellular machinery. Consequently, the shared breast and cervix_uterine pattern may partly reflect common epithelial cell states, variable immune or blood-cell content, or both; it should not automatically be interpreted as a breast-and-cervix-specific pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING evidence is sparse. The only high-confidence interaction among module members is the LPCAT2–LYPLA1 relationship, linking phospholipid remodeling with lysophospholipase and depalmitoylation activity. No STRING functional-enrichment result is reported, and no hu.MAP complex contains multiple module members. The remaining co-abundance edges are therefore not independently supported here as physical interactions or membership in a known multiprotein complex. This pattern is consistent with a transcriptional or cellular-composition signal, or with several related metabolic and trafficking states, rather than a compact canonical protein complex.

**STRING interactions (score >= 0.7)**: 1 of 120 gene pairs: LPCAT2–LYPLA1 (0.774)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a newly discovered molecular complex or a newly established pathway. Its strongest network feature is a data-derived co-abundance hub around DHRS9, but most relationships are not represented by the supplied high-confidence STRING or hu.MAP evidence. That absence does not prove novelty: co-abundance can arise from shared cell type, regulation, tissue composition, or parallel physiology, and database coverage is incomplete. The potentially novel aspect is the specific cross-tissue co-abundance configuration linking DHRS9 with metabolic, epithelial, trafficking, and immune-associated genes in breast and cervix_uterine. Establishing novelty would require replication in independent cohorts, control for cell composition, comparison with published co-expression modules, and experimental or orthogonal validation.

**Hypothesis.** Hypothesis: the module reflects a shared epithelial metabolic and membrane-remodeling state that is modulated by variable myeloid or blood-cell admixture. In this model, DHRS9 coordinates or marks steroid, retinoid, and epithelial differentiation metabolism, while NSDHL and EPHX1 contribute to sterol and xenobiotic or lipid processing. LPCAT2 and LYPLA1 could alter membrane phospholipids and lipid signaling, with their known STRING relationship providing the clearest direct molecular link. MYO5B and AP1B1 could represent vesicle and membrane trafficking, whereas PGD and PFKP could support redox and glycolytic demands. NBEAL2 could mark a platelet or neutrophil-related component rather than participate in the same epithelial mechanism. This is a testable hypothesis, not an established mechanistic conclusion.

### Important genes

#### DHRS9

- **Related proteins** (co-abundance neighbors): RAB18 (0.96), NCKAP1 (0.94), PGD (0.94), PFKP (0.91), MYO5B (0.90), NSDHL (0.88), RARS1 (0.88), PYGB (0.87), AP1B1 (0.86), NBEAL2 (0.86), EPHX1 (0.85), LPCAT2 (0.83), RAP1GDS1 (0.82), LYPLA1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dehydrogenase/reductase 9. This gene encodes a member of the short-chain dehydrogenases/reductases (SDR) family. The encoded protein has been identified as a moonlighting protein based on its ability to perform mechanistically distinct functions. This protein demonstrates oxidoreductase activity toward hydroxysteroids and is able to convert 3-alpha-tetrahydroprogesterone to dihydroxyprogesterone and 3-alpha-androstanediol t…
- **Diseases (Open Targets)**: Intrahepatic cholestasis of pregnancy (0.362); viral eye infection (0.360); diabetes mellitus (0.219); clear cell renal carcinoma (0.155); macular holes (0.092)
- **Europe PMC papers**: 833
- **Why important**: DHRS9 is the central network hub, with strong connections to nearly every other module member. Its established SDR-family oxidoreductase functions include hydroxysteroid, androgen, progesterone, and retinol metabolism, and its annotations include epithelial differentiation. Its HPA profile links it to heart muscle, intestine, several epithelial cell types, and granulocyte categories. It also has substantial literature coverage, making it the best candidate for distinguishing a metabolic epithelial program from a purely compositional signal.
- **Conclusion**: Established evidence supports DHRS9 as the principal network marker and as a multifunctional steroid, retinoid, and epithelial-metabolism enzyme. It is plausible, but not proven, that DHRS9 is a functional organizer of the module; its hub status may instead reflect shared regulation or cell composition.

#### PGD

- **Related proteins** (co-abundance neighbors): DHRS9 (0.94); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphogluconate dehydrogenase. 6-phosphogluconate dehydrogenase is the second dehydrogenase in the pentose phosphate shunt. Deficiency of this enzyme is generally asymptomatic, and the inheritance of this disorder is autosomal dominant. Hemolysis results from combined deficiency of 6-phosphogluconate dehydrogenase and 6-phosphogluconolactonase suggesting a synergism of the two enzymopathies. Several transcript variants encoding…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); Abnormality of the skeletal system (0.329); autoimmune disorder of central nervous system (0.246); smoking behavior (0.245); essential hypertension (0.199)
- **Europe PMC papers**: 8652
- **Why important**: PGD connects the module to the oxidative branch of the pentose-phosphate shunt, NADPH regeneration, and carbohydrate metabolism. HPA places it in bone marrow and esophageal contexts and in several granulocyte and monocyte categories. It is highly studied and provides a biologically interpretable bridge between epithelial metabolic demand and possible blood-cell content.
- **Conclusion**: Established evidence supports PGD as a pentose-phosphate and redox enzyme with a strong hematopoietic and epithelial expression context in this dataset. Its co-abundance here may reflect metabolic activity, myeloid admixture, or both; the module does not establish which.

#### NBEAL2

- **Related proteins** (co-abundance neighbors): DHRS9 (0.86), SH3BGRL2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neurobeachin like 2. The protein encoded by this gene contains a beige and Chediak-Higashi (BEACH) domain and multiple WD40 domains, and may play a role in megakaryocyte alpha-granule biogenesis. Mutations in this gene are a cause of gray platelet syndrome. [provided by RefSeq, Dec 2011].
- **Diseases (Open Targets)**: gray platelet syndrome (0.816); Thrombocytopenia (0.414); Abnormal bleeding (0.387); type 2 diabetes mellitus (0.253); hereditary disease (0.194)
- **Europe PMC papers**: 462
- **Why important**: NBEAL2 is a peripheral module member connected to DHRS9 and SH3BGRL2, but it has a distinctive biological interpretation. It contains a BEACH domain and WD forty domains, is implicated in megakaryocyte alpha-granule biogenesis, and is associated with gray platelet syndrome and thrombocytopenia. HPA associates it with esophageal epithelial categories, neutrophils, and neutrophil progenitors. Its disease association makes it useful for testing whether the module contains a blood or platelet-related component.
- **Conclusion**: Established evidence supports NBEAL2 as a granule-biogenesis and platelet-disorder gene with myeloid and epithelial expression contexts. It is a strong indicator of possible cellular composition effects, but there is no evidence here that NBEAL2 mechanistically drives the whole module.

#### LPCAT2

- **Related proteins** (co-abundance neighbors): DHRS9 (0.83); STRING partners: LYPLA1 (0.774)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lysophosphatidylcholine acyltransferase 2. This gene encodes a member of the lysophospholipid acyltransferase family. The encoded enzyme may function in two ways: to catalyze the biosynthesis of platelet-activating factor (1-O-alkyl-2-acetyl-sn-glycero-3-phosphocholine) from 1-O-alkyl-sn-glycero-3-phosphocholine, and to catalyze the synthesis of glycerophospholipid precursors from arachidonyl-CoA and lysophosphatidylcholine. The encoded pr…
- **Diseases (Open Targets)**: ocular hypotension (0.350); Torg-Winchester syndrome (0.333); multicentric osteolysis-nodulosis-arthropathy spectrum (0.333); liver disorder (0.212); alopecia areata (0.174)
- **Europe PMC papers**: 761
- **Why important**: LPCAT2 is the module member with the clearest known within-module STRING relationship, namely its interaction with LYPLA1. It catalyzes lysophospholipid and glycerophospholipid remodeling and can contribute to platelet-activating factor biosynthesis and membrane organization. HPA associates it with bone marrow, hematopoietic progenitors, mast cells, microglia, and granulocyte-related categories. Its literature and disease associations are more limited than those of the major metabolic enzymes, which makes it informative for evaluating a possible lipid-inflammatory component.
- **Conclusion**: Established evidence supports LPCAT2 as a membrane-lipid remodeling enzyme and supports a direct relationship with LYPLA1 in the supplied STRING data. A lipid-signaling or inflammatory interpretation of the module is a reasonable hypothesis, but it is not established by enrichment or by the sparse interaction network.

#### MYO5B

- **Related proteins** (co-abundance neighbors): DHRS9 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin VB. The protein encoded by this gene, together with other proteins, may be involved in plasma membrane recycling. Mutations in this gene are associated with microvillous inclusion disease. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: microvillus inclusion disease (0.846); progressive familial intrahepatic cholestasis (0.764); neurodegenerative disease (0.462); progressive familial intrahepatic cholestasis type 1 (0.377); inflammatory bowel disease 1 (0.334)
- **Europe PMC papers**: 995
- **Why important**: MYO5B is connected to the DHRS9 hub and has a well-defined role in plasma-membrane recycling, endocytosis, actin organization, and vesicle-mediated transport. Mutations are associated with microvillus inclusion disease and progressive familial intrahepatic cholestasis. HPA places it in intestinal and multiple epithelial cell categories, including endometrial and esophageal epithelial cells, while excluding immune-cell detection. It therefore provides a useful epithelial trafficking counterpart to the immune-associated genes.
- **Conclusion**: Established evidence supports MYO5B as an epithelial membrane-trafficking gene with important disease associations. Its presence supports an epithelial transport component in the module, but the data do not show that MYO5B physically interacts with DHRS9 or that it mediates the shared tissue signal.

## Module 1

**Tissue pair**: breast and cervix_uterine  
**Genes (5)**: A2M, CP, C3, COL6A1, FGA

### Function

The module is most strongly characterized as a secreted extracellular blood-associated complement, coagulation, and matrix-related module. Primary evidence is provided by (GO:CC endoplasmic reticulum lumen; q_global = 0.0121), endoplasmic reticulum lumen, with C3, COL6A1, CP, and FGA; (GO:CC blood microparticle; q_global = 0.014), blood microparticle, with A2M, C3, CP, and FGA; and (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.041), complement and coagulation cascades, with A2M, C3, and FGA. The gene annotations support complementary roles: C3 is central to complement activation and inflammatory signaling, FGA participates in fibrin formation, A2M inhibits proteases and can modulate inflammatory cascades, CP participates in copper and iron handling and oxidant detoxification, and COL6A1 is an extracellular-matrix collagen. Together, the evidence supports a circulating or extracellular stress, inflammatory, coagulation, and tissue-remodeling interpretation. The GO/KEGG evidence does not by itself establish that these proteins are produced by breast or cervix_uterine tissue.

**Cell composition.** All module genes are secreted according to HPA, and most are secreted to blood or the extracellular matrix. HPA points especially toward liver and hepatocyte enrichment, with additional fibroblast-associated patterns and some lung association. Three genes are not detected in immune cells, while one is immune-cell enhanced and one is immune-cell enriched; therefore this is not primarily a blood-cell structural module. The strong plasma and hepatocyte pattern makes blood or plasma carryover, vascular content, systemic acute-phase biology, or shared extracellular material plausible contributors to the breast and cervix_uterine co-abundance signal. HPA protein detection is absent in breast for the module and present for only A2M in cervix_uterine, which argues against interpreting the module as a uniformly tissue-resident protein program. COL6A1 additionally provides a fibroblast and extracellular-matrix component.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC endoplasmic reticulum lumen | 0.0121 | C3, COL6A1, CP, FGA |
| GO:CC blood microparticle | 0.014 | A2M, C3, CP, FGA |
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 0.041 | A2M, C3, FGA |

### STRING and hu.MAP

STRING supplies three high-confidence pairwise relationships: A2M with CP, A2M with FGA, and C3 with CP. These known links support a coherent extracellular plasma-protein network rather than an arbitrary co-abundance grouping. STRING supplementary enrichment also recovers secretion, signal, endoplasmic reticulum lumen, blood microparticle, plasma-cell, glycoprotein, skeletal-system, and complement/coagulation annotations, but these are not global GO/KEGG significance claims. hu.MAP independently places CP, A2M, C3, and FGA together in several complexes, including complexes with complement, coagulation, fibrinolysis, acute-phase, transport, and plasma proteins. This repeated membership indicates that the four-gene core reflects known biochemical and circulating protein neighborhoods. COL6A1 has no reported STRING partner or hu.MAP complex in the fact sheet, although its links to C3 and A2M in the co-abundance graph connect matrix biology to the better-established plasma-protein core. The complex evidence supports biological coherence but does not prove that every listed protein physically binds every other protein in this module.

**STRING interactions (score >= 0.7)**: 3 of 10 gene pairs: A2M–CP (0.889); A2M–FGA (0.832); C3–CP (0.751)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Secreted (FDR = 0.0023, 5 genes); Keyword Signal (FDR = 0.0043, 5 genes); Component Endoplasmic reticulum lumen (FDR = 0.0054, 4 genes); Component Blood microparticle (FDR = 0.0054, 4 genes); TISSUES Plasma cell (FDR = 0.0055, 4 genes); COMPARTMENTS Blood microparticle (FDR = 0.0056, 4 genes); Keyword Glycoprotein (FDR = 0.0082, 5 genes); Keyword Thioester bond (FDR = 0.0093, 2 genes); KEGG Complement and coagulation cascades (FDR = 0.0111, 3 genes); TISSUES Skeletal system (FDR = 0.0143, 5 genes); PMID (2022) A New Role of Acute Phase Proteins: Local Production Is an Ancient, General Stress-Response System of Mammalian Cells. (FDR = 0.0154, 4 genes); PMID (2019) A quantitative Streptococcus pyogenes-human protein-protein interaction map reveals localization of opsonizing antibodies. (FDR = 0.0154, 4 genes); PMID (2023) A Scd1-mediated metabolic alteration participates in liver responses to low-dose bavachin. (FDR = 0.0168, 4 genes); PMID (2007) Molecular characterisation of the early response in pigs to experimental infection with Actinobacillus pleuropneumoniae using cDNA microarrays. (FDR = 0.0168, 4 genes); PMID (2021) Dataset of why inclusion matters for Alzheimers disease biomarker discovery in plasma. (FDR = 0.0179, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08395.1 (CP, A2M, C3, FGA; 4/43); huMAP3_09531.1 (CP, A2M, C3, FGA; 4/47); huMAP3_10101.1 (CP, A2M, C3, FGA; 4/49); huMAP3_15040.1 (CP, A2M, C3, FGA; 4/64); huMAP3_10678.1 (CP, A2M, C3, FGA; 4/71); huMAP3_07432.1 (CP, C3, FGA; 3/18); huMAP3_02242.1 (C3, FGA; 2/9); huMAP3_07265.1 (CP, A2M; 2/20); huMAP3_08224.1 (C3, FGA; 2/21); huMAP3_09273.1 (CP, A2M; 2/28); huMAP3_09434.1 (C3, FGA; 2/33)

### Novelty

The underlying biology is not a new discovery: C3, A2M, CP, and FGA are already connected by STRING or recurring hu.MAP complexes and have established complement, coagulation, plasma, or extracellular functions. The breast and cervix_uterine co-abundance pattern could still be a new tissue-pair observation, particularly because COL6A1 connects the plasma-associated core with extracellular matrix biology and lacks corresponding STRING or hu.MAP support here. However, the available evidence cannot establish that the module itself is novel. Absence of a database relationship is not proof of novelty, and the strong liver, hepatocyte, and blood-secreted signature raises the alternative explanation that the shared signal reflects circulating proteins, sample vascular content, or a common stromal or extracellular context rather than a newly discovered breast-cervix mechanism. Novelty would require independent replication and tissue-origin or cellular validation.

**Hypothesis.** HYPOTHESIS: A shared extracellular inflammatory and tissue-remodeling state in breast and cervix_uterine samples alters or captures a circulating protein milieu containing complement and coagulation factors, while stromal extracellular matrix contributes COL6A1. In this model, C3 provides complement and inflammatory signaling, A2M buffers proteases and cytokine activity, FGA represents coagulation and matrix-interacting material, CP reflects metal-handling and oxidative-stress biology, and COL6A1 marks stromal matrix context. The observed module may therefore report coordinated exposure to plasma or vascular material and local stromal stress, rather than coordinated transcription by the epithelial cells of both tissues. This is a mechanistic proposal, not established by the co-abundance data alone.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): COL6A1 (0.87), FGA (0.84), CP (0.81); STRING partners: CP (0.751)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_02242.1, huMAP3_08224.1, huMAP3_09434.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is the central network hub, connecting COL6A1, FGA, and CP, and it appears in all primary terms (GO:CC endoplasmic reticulum lumen; q_global = 0.0121), (GO:CC blood microparticle; q_global = 0.014), and (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.041). Its established role in complement activation, inflammatory signaling, and generation of bioactive peptide products makes it the strongest functional anchor. It also has extensive literature and disease associations involving complement deficiency, complement-mediated renal disease, and macular degeneration.
- **Conclusion**: Established evidence supports C3 as the principal complement and inflammatory driver represented by this module. It is a plausible module marker, but the data do not establish local C3 production in breast or cervix_uterine.

#### FGA

- **Related proteins** (co-abundance neighbors): C3 (0.84); STRING partners: A2M (0.832)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_02242.1, huMAP3_08224.1, huMAP3_09434.1
- **Function (MyGene.info)**: fibrinogen alpha chain. This gene encodes the alpha subunit of the coagulation factor fibrinogen, which is a component of the blood clot. Following vascular injury, the encoded preproprotein is proteolytically processed by thrombin during the conversion of fibrinogen to fibrin. Mutations in this gene lead to several disorders, including dysfibrinogenemia, hypofibrinogenemia, afibrinogenemia and renal amyloidosis. Alterna…
- **Diseases (Open Targets)**: familial dysfibrinogenemia (0.789); familial visceral amyloidosis (0.765); congenital afibrinogenemia (0.757); familial hypodysfibrinogenemia (0.659); congenital fibrinogen deficiency (0.619)
- **Europe PMC papers**: 7516
- **Why important**: FGA connects directly to C3 and A2M in the database evidence and occurs in all primary terms (GO:CC endoplasmic reticulum lumen; q_global = 0.0121), (GO:CC blood microparticle; q_global = 0.014), and (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.041). It encodes the fibrinogen alpha chain, linking the module to blood coagulation, platelet-related biology, fibrinolysis, and cell-matrix adhesion. Its liver and hepatocyte enrichment and secretion to blood make it particularly informative for assessing plasma contribution. It also has established disease associations involving abnormal or deficient fibrinogen.
- **Conclusion**: Established evidence supports FGA as a coagulation and circulating-plasma component of the module. Its presence favors a vascular or plasma-origin interpretation over a purely tissue-intrinsic interpretation.

#### A2M

- **Related proteins** (co-abundance neighbors): COL6A1 (0.81); STRING partners: CP (0.889), FGA (0.832)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07265.1, huMAP3_09273.1
- **Function (MyGene.info)**: alpha-2-macroglobulin. The protein encoded by this gene is a protease inhibitor and cytokine transporter. It uses a bait-and-trap mechanism to inhibit a broad spectrum of proteases, including trypsin, thrombin and collagenase. It can also inhibit inflammatory cytokines, and it thus disrupts inflammatory cascades. Mutations in this gene are a cause of alpha-2-macroglobulin deficiency. This gene is implicated in Alzheimer…
- **Diseases (Open Targets)**: myopia (0.206); refractive error (0.151); primary angle-closure glaucoma (0.148); Abnormality of refraction (0.144); Aganglionic megacolon (0.118)
- **Europe PMC papers**: 5133
- **Why important**: A2M is connected to CP and FGA in STRING and appears in the complement and coagulation primary term (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.041) and the blood-microparticle term (GO:CC blood microparticle; q_global = 0.014). Its protease-trapping and cytokine-transport functions provide a regulatory link between extracellular proteolysis and inflammation. It also has broad hu.MAP complex support and is detected by HPA in cervix_uterine but not breast, making it useful for testing tissue-specific versus circulating contributions.
- **Conclusion**: Established evidence supports A2M as an extracellular protease and inflammatory regulator within the module. Its cervix_uterine detection is compatible with local contribution there, but the broader secretion pattern means a systemic source remains plausible.

#### CP

- **Related proteins** (co-abundance neighbors): C3 (0.81); STRING partners: A2M (0.889), C3 (0.751)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09273.1
- **Function (MyGene.info)**: ceruloplasmin. The protein encoded by this gene is a metalloprotein that binds most of the copper in plasma and is involved in the peroxidation of Fe(II)transferrin to Fe(III) transferrin. Mutations in this gene cause aceruloplasminemia, which results in iron accumulation and tissue damage, and is associated with diabetes and neurologic abnormalities. Two transcript variants, one protein-coding and the other not…
- **Diseases (Open Targets)**: aceruloplasminemia (0.827); cerebellar ataxia (0.572); Hermansky-Pudlak syndrome 3 (0.564); Hermansky-Pudlak syndrome (0.543); neurodegeneration with brain iron accumulation (0.510)
- **Europe PMC papers**: 171928
- **Why important**: CP is a network-connected member linked to C3 and A2M by STRING and is present in the primary endoplasmic-reticulum-lumen and blood-microparticle terms (GO:CC endoplasmic reticulum lumen; q_global = 0.0121) and (GO:CC blood microparticle; q_global = 0.014). Its established roles in copper binding, iron handling, and oxidant detoxification add metal and redox biology to the complement-coagulation signal. It has extensive literature and a strong association with aceruloplasminemia and neurologic iron-accumulation phenotypes.
- **Conclusion**: Established evidence supports CP as a secreted plasma redox and metal-handling component that may report systemic or inflammatory state. Its presence does not demonstrate a tissue-local oxidative mechanism in either organ.

#### COL6A1

- **Related proteins** (co-abundance neighbors): C3 (0.87), A2M (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 has the second most connected position in the co-abundance subgraph, linking C3 and A2M, and is the only module member that clearly introduces extracellular-matrix collagen biology. It appears in (GO:CC endoplasmic reticulum lumen; q_global = 0.0121), is associated with fibroblast and stromal cell patterns in HPA, and is linked to Bethlem and Ullrich collagen-related myopathies. Unlike the plasma-associated core, it has no reported STRING partner or hu.MAP complex in the fact sheet, so its network connection is especially informative but less established.
- **Conclusion**: Established evidence supports COL6A1 as an extracellular-matrix and stromal marker. Its connection to the secreted plasma core is a plausible bridge to tissue remodeling, but whether it reflects a biological interaction or shared sample composition remains unresolved.

## Module 2

**Tissue pair**: breast and cervix_uterine  
**Genes (14)**: ABCD3, ACO2, SLC4A1, CYBB, CYFIP1, HLA-DMB, EHBP1L1, H1-4, ITPRIP, PLEKHA5, PSMB8, SORL1, SUN2, TNFAIP2

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING functional enrichment. Therefore, the function should be inferred from the gene identities and network structure rather than from statistically significant pathway enrichment. The module is consistent with a mixed vesicle, membrane-trafficking, antigen-processing, phagocyte-defense, cytoskeletal, metabolic, and erythroid-associated signal. HLA-DMB is the major network hub, linking genes involved in antigen presentation, oxidative defense, peroxisomal and mitochondrial metabolism, cytoskeletal regulation, erythrocyte biology, and chromatin structure. ITPRIP forms a second local connector among vesicle, membrane, and signaling genes. This pattern is more compatible with a cellular-composition or shared inflammatory-state signal than with a single coherent biochemical pathway. The evidence supports an immune and myeloid-associated module, with additional contributions from blood-cell and general cellular-state programs. These are functional interpretations of the genes, not globally significant enrichment claims.

**Cell composition.** The HPA profile argues strongly against interpreting this as a tissue-intrinsic breast or cervix_uterine program without qualification. Many genes are cell-type enhanced, especially in monocytes, neutrophils, Kupffer cells, microglia, and neutrophil progenitors. Bone marrow and lymphoid tissue recur among enriched tissues, while several genes are associated with skeletal or heart muscle and one with liver. SLC4A1 and H1-4 are associated with erythrocyte or erythroid progenitor biology, and CYBB, HLA-DMB, PSMB8, CYFIP1, ITPRIP, and SORL1 have myeloid or immune-cell associations. SORL1 is the only secreted-to-blood member identified by HPA, so this is not predominantly a plasma-protein module. The combination of blood-cell-associated genes, immune-cell specificity, and detection of most members in both tissues suggests that shared blood, immune-cell, or stromal-cell content may contribute substantially to the co-abundance pattern. It does not establish sample contamination, because several genes are also detected in the tissues and some have nonimmune cellular functions.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

At the specified STRING confidence threshold, none of the possible gene pairs had a recorded STRING interaction, and STRING reported no supplementary functional enrichment. No hu.MAP complex contained multiple module members. Thus, the abundance correlations are not reproduced by the supplied curated protein-interaction or complex resources. The network itself is sparse and organized around HLA-DMB, with ITPRIP providing a smaller local connection to SUN2, EHBP1L1, PLEKHA5, TNFAIP2, and SORL1. The absence of STRING and hu.MAP support means the module should be treated as a co-abundance pattern rather than a demonstrated physical complex. Known biology nevertheless exists for individual components: HLA-DMB participates in peptide loading for antigen-presentation molecules; CYBB is part of the phagocyte microbicidal oxidase; PSMB8 is an immunoproteasome subunit; ITPRIP modulates intracellular calcium signaling; and SLC4A1 functions as an erythrocyte anion exchanger. These established individual functions do not demonstrate direct physical interaction among the module members.

**STRING interactions (score >= 0.7)**: 0 of 91 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel tissue-pair co-abundance observation, but it cannot be called a newly discovered molecular complex or pathway. The combination of shared breast and cervix_uterine co-abundance, a sparse network, no STRING edges, no multi-member hu.MAP complex, and no globally significant GO or KEGG term is not represented as an established interaction module in the supplied resources. However, absence from STRING or hu.MAP alone does not prove novelty. The genes have substantial prior biological literature and several are well-established immune, erythroid, metabolic, or trafficking genes. The most defensible claim is that the cross-tissue co-abundance arrangement may be novel, while the component functions and several pairwise biological roles are not novel.

**Hypothesis.** Hypothesis: the module reflects a shared abundance of myeloid or other blood-associated cells in breast and cervix_uterine samples, together with an inflammatory antigen-processing state. In this model, HLA-DMB marks intracellular antigen-loading machinery, CYBB and PSMB8 represent antimicrobial and interferon-responsive immune activity, and TNFAIP2 together with vesicle-associated genes reflects regulated trafficking or exocytosis. ITPRIP, EHBP1L1, PLEKHA5, and SUN2 could connect calcium sensitivity, membrane trafficking, actin organization, and cell-shape or migration processes. SLC4A1 and H1-4 may indicate an erythroid or blood-derived component, whereas ABCD3 and ACO2 may reflect metabolic variation across the contributing cells. This hypothesis predicts that the module will track cell-composition markers and inflammatory or phagocyte abundance more strongly than a breast- or cervix-specific epithelial program. It requires validation with cell deconvolution, independent cohorts, protein measurements, and perturbation or interaction assays.

### Important genes

#### HLA-DMB

- **Related proteins** (co-abundance neighbors): TNFAIP2 (0.90), CYBB (0.89), ABCD3 (0.86), PSMB8 (0.86), ACO2 (0.84), CYFIP1 (0.83), SLC4A1 (0.81), H1-4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: major histocompatibility complex, class II, DM beta. HLA-DMB belongs to the HLA class II beta chain paralogues. This class II molecule is a heterodimer consisting of an alpha (DMA) and a beta (DMB) chain, both anchored in the membrane. It is located in intracellular vesicles. DM plays a central role in the peptide loading of MHC class II molecules by helping to release the CLIP (class II-associated invariant chain peptide) molecule from the peptide …
- **Diseases (Open Targets)**: asthma (0.074); periodontitis (0.074); endometrial cancer (0.074); neoplasm (0.063); rheumatoid arthritis (0.049)
- **Europe PMC papers**: 2177
- **Why important**: HLA-DMB is the dominant network hub and connects the widest range of module members. Its established function is to help release CLIP and facilitate peptide loading onto MHC class-two molecules in intracellular vesicles. HPA places it in lymphoid and antigen-presenting cell contexts, and it has extensive literature and disease-association evidence. It is therefore the strongest marker of the module's immune and antigen-processing interpretation.
- **Conclusion**: Established evidence supports HLA-DMB as an antigen-presentation component and as the central co-abundance anchor of this module. The hypothesis that it organizes the other module processes is not established, because the supplied STRING and hu.MAP resources show no supporting physical interactions.

#### ITPRIP

- **Related proteins** (co-abundance neighbors): SUN2 (0.89), EHBP1L1 (0.87), PLEKHA5 (0.86), TNFAIP2 (0.83), SORL1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inositol 1,4,5-trisphosphate receptor interacting protein. This gene encodes a membrane-associated protein that binds the inositol 1,4,5-trisphosphate receptor (ITPR). The encoded protein enhances the sensitivity of ITPR to intracellular calcium signaling. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2012].
- **Diseases (Open Targets)**: female genital tract polyp (0.359); femoral neck fracture (0.337); uterine corpus leiomyoma (0.295); aortic stenosis (0.252); Abnormal blistering of the skin (0.245)
- **Europe PMC papers**: 742
- **Why important**: ITPRIP is the second major network connector and links several membrane, vesicle, and signaling-associated genes. Its established function is to bind the inositol trisphosphate receptor and enhance sensitivity to intracellular calcium signaling. HPA associates it with bone marrow, monocytes, and neutrophil progenitors, while its disease associations include reproductive and skeletal conditions. Its position makes it a useful candidate for connecting cell signaling with the immune-cell-associated abundance pattern.
- **Conclusion**: Established evidence supports a calcium-signaling and membrane-associated role, with a relevant bone-marrow and myeloid expression context. It is plausible, but unproven, that ITPRIP helps couple calcium responses to trafficking or migration in the cells contributing to the module.

#### CYBB

- **Related proteins** (co-abundance neighbors): HLA-DMB (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome b-245 beta chain. Cytochrome b (-245) is composed of cytochrome b alpha (CYBA) and beta (CYBB) chain. It has been proposed as a primary component of the microbicidal oxidase system of phagocytes. CYBB deficiency is one of five described biochemical defects associated with chronic granulomatous disease (CGD). In this disorder, there is decreased activity of phagocyte NADPH oxidase; neutrophils are able to phagocytiz…
- **Diseases (Open Targets)**: chronic granulomatous disease (0.864); neurodegenerative disease (0.352); hereditary disease (0.191); discoid lupus erythematosus (0.185); Kartagener Syndrome (0.118)
- **Europe PMC papers**: 6704
- **Why important**: CYBB is a canonical phagocyte-defense gene and is associated by HPA with bone marrow, lymphoid tissue, monocytes, macrophages, Kupffer cells, and microglia. Its established product is the beta chain of the phagocyte NADPH oxidase, and loss of function causes chronic granulomatous disease. Although it has only a single module connection, that connection to HLA-DMB is biologically informative because it joins antigen-presentation and antimicrobial-defense signals.
- **Conclusion**: Established evidence supports CYBB as a marker of myeloid phagocyte activity and oxidative microbial defense. The module does not establish that CYBB directly interacts with HLA-DMB or that the co-abundance represents coordinated regulation, so those remain hypotheses.

#### PSMB8

- **Related proteins** (co-abundance neighbors): HLA-DMB (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 20S subunit beta 8. The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent proc…
- **Diseases (Open Targets)**: proteosome-associated autoinflammatory syndrome (0.829); plasma cell myeloma (0.618); mantle cell lymphoma (0.542); neoplasm (0.536); amyloidosis (0.472)
- **Europe PMC papers**: 3589
- **Why important**: PSMB8 encodes an immunoproteasome subunit and is linked to immune-system processes, peptide degradation, and cytokine-related responses. HPA places it in several cell contexts, including platelets and megakaryocytes, and it has substantial literature and disease-association evidence. Its connection to the HLA-DMB hub is consistent with a broader antigen-processing interpretation, although the supplied interaction resources do not validate a direct relationship.
- **Conclusion**: Established evidence supports PSMB8 as an immune-associated proteasome component. Its co-abundance with HLA-DMB may indicate a shared antigen-processing or inflammatory cellular state, but a direct mechanistic link within this module is not established.

#### SLC4A1

- **Related proteins** (co-abundance neighbors): HLA-DMB (0.81); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 4 member 1 (Diego blood group). The protein encoded by this gene is part of the anion exchanger (AE) family and is expressed in the erythrocyte plasma membrane, where it functions as a chloride/bicarbonate exchanger involved in carbon dioxide transport from tissues to lungs. The protein comprises two domains that are structurally and functionally distinct. The N-terminal 40kDa domain is located in the cytoplasm and acts as an at…
- **Diseases (Open Targets)**: hereditary spherocytosis type 4 (0.818); autosomal dominant distal renal tubular acidosis (0.816); renal tubular acidosis, distal, 4, with hemolytic anemia (0.798); southeast Asian ovalocytosis (0.769); cryohydrocytosis (0.768)
- **Europe PMC papers**: 2632
- **Why important**: SLC4A1 is a strong composition marker because HPA associates it with bone marrow and erythrocytes or erythroid progenitors, while its established function is chloride-bicarbonate exchange in the erythrocyte membrane. Its connection to the HLA-DMB hub is not an obvious pathway relationship and therefore provides important evidence that the module may incorporate blood-derived cellular variation rather than represent a unified immune complex.
- **Conclusion**: Established evidence supports SLC4A1 as an erythrocyte and blood-cell marker with a gas-transport role. Its presence supports the cell-composition interpretation of the module; any functional coupling between erythroid abundance and HLA-DMB-associated immune activity remains a hypothesis.

## Module 3

**Tissue pair**: breast and cervix_uterine  
**Genes (10)**: ACADM, ALDH3B1, AUP1, CLIC3, ARHGAP45, MSLN, TAP2, ACAA2, UTRN, RP2

### Function

No GO/KEGG term passed global correction, and STRING reported no functional enrichment. Therefore, the module has no statistically established pathway-level annotation. Its genes nevertheless suggest a mixed program involving mitochondrial fatty-acid oxidation, aldehyde and lipid-peroxidation handling, antigen processing, epithelial adhesion, membrane biology, vesicles, lipid droplets and small-GTPase regulation. ACADM and ACAA2 provide a mitochondrial fatty-acid oxidation component; ALDH3B1 provides an aldehyde-detoxification and oxidative-stress component; TAP2 provides an antigen-processing component; MSLN provides an adhesion-associated epithelial component; and CLIC3 and AUP1 provide membrane, vesicle, chloride-channel or lipid-droplet-related context. Because these functions are distributed across different biological systems and no term passed global correction, the module is better interpreted as a coordinated cell-state or tissue-composition signal than as a demonstrated canonical pathway.

**Cell composition.** The module is not dominated by secreted or plasma proteins, since only one gene is annotated as secreted. Most genes are intracellular, mitochondrial, membrane-associated, vesicular or nuclear. It is also not a uniform blood-cell module: most genes have low immune-cell specificity, although ALDH3B1, CLIC3, UTRN and MSLN show immune-cell enhancement or enrichment in particular blood-cell types. HPA reports cell-type enhancement for every gene, with recurring epithelial, trophoblast, hepatocyte, alveolar and myeloid populations. Tissue annotations include liver, bone marrow, skeletal muscle, tongue and cervix, while several genes have low tissue specificity. Protein detection is shared between breast and cervix for ALDH3B1, UTRN, CLIC3, ACADM and AUP1. MSLN and RP2 are detected in cervix but not breast, TAP2 is detected in breast but not cervix, and ARHGAP45 is not detected in either tissue. The shared module may therefore reflect a conserved epithelial or epithelial-adjacent state, with possible contributions from shared minor cell populations, rather than blood contamination alone.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship is ACADM–ACAA2, supporting a known connection between two mitochondrial fatty-acid oxidation proteins. This relationship supports a metabolic subcomponent but does not establish that the entire module is a physical complex. The other co-abundance relationships lack corresponding high-confidence STRING support in the supplied evidence. STRING functional enrichment is absent, and no hu.MAP complex contains multiple module members. Consequently, most network edges may represent coordinated regulation, shared cell-type abundance, tissue composition, indirect biology or correlated cellular state rather than direct protein binding.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: ACAA2–ACADM (0.937)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The conserved co-abundance pattern across breast and cervix_uterine is potentially a new observation, particularly because it combines an ALDH3B1-centered network with mitochondrial fatty-acid oxidation genes, epithelial-associated genes, antigen-presentation machinery and membrane or vesicle-related genes. However, it should not be called a newly discovered pathway or complex. The lack of a matching hu.MAP complex and the limited STRING support indicate that this exact assembly is not represented as a known complex in the supplied resources, but absence from those databases does not prove biological novelty. The appropriate conclusion is that the cross-tissue network pattern is hypothesis-generating and requires validation with cell-resolved, protein-level and perturbation experiments.

**Hypothesis.** Hypothesis: the module reflects a conserved epithelial or epithelial-adjacent cell state in which mitochondrial lipid utilization and protection from aldehyde or lipid-peroxidation stress are coordinated with membrane adhesion, vesicle or lipid-droplet organization and antigen-presentation capacity. ALDH3B1 may mark the oxidative-stress component; ACADM and ACAA2 may represent mitochondrial lipid utilization; AUP1 may connect lipid droplets with endoplasmic-reticulum quality control; MSLN and CLIC3 may represent epithelial membrane or vesicle biology; and TAP2 may reflect an immune-interface component. This model predicts that the module will track particular cell states and metabolic or stress conditions more strongly than it will track one stable multiprotein complex. It should be tested using cell-resolved expression, protein measurements, histology and perturbation of the proposed metabolic or stress-response processes.

### Important genes

#### ALDH3B1

- **Related proteins** (co-abundance neighbors): RP2 (0.92), ARHGAP45 (0.91), UTRN (0.91), TAP2 (0.89), ACADM (0.84), ACAA2 (0.83), AUP1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 3 family member B1. This gene encodes a member of the aldehyde dehydrogenase protein family. Aldehyde dehydrogenases are a family of isozymes that may play a major role in the detoxification of aldehydes generated by alcohol metabolism and lipid peroxidation. The encoded protein is able to oxidize long-chain fatty aldehydes in vitro, and may play a role in protection from oxidative stress. Alternative splicing result…
- **Diseases (Open Targets)**: neurodegenerative disease (0.308); alcohol drinking (0.187); neoplasm (0.060); lung adenocarcinoma (0.059); gastric cancer (0.057)
- **Europe PMC papers**: 734
- **Why important**: ALDH3B1 is the central network node, connecting most other module genes through the strongest co-abundance relationships. Its annotated aldehyde metabolism, lipid metabolism and oxidative-stress functions provide a plausible organizing axis for an otherwise heterogeneous module. It is detected in both tissues, has low tissue specificity, and has substantial literature coverage. Its supplied disease associations include neurodegenerative disease, alcohol drinking and neoplasm, although these associations do not establish a role in this module.
- **Conclusion**: Established evidence supports ALDH3B1 as the network hub and as an aldehyde- and oxidative-stress-related enzyme. It is a plausible module anchor. It remains a hypothesis that ALDH3B1 drives the shared breast–cervix program or functionally links the metabolic genes in these tissues.

#### ACADM

- **Related proteins** (co-abundance neighbors): ALDH3B1 (0.84); STRING partners: ACAA2 (0.937)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA dehydrogenase medium chain. This gene encodes the medium-chain specific (C4 to C12 straight chain) acyl-Coenzyme A dehydrogenase. The homotetramer enzyme catalyzes the initial step of the mitochondrial fatty acid beta-oxidation pathway. Defects in this gene cause medium-chain acyl-CoA dehydrogenase deficiency, a disease characterized by hepatic dysfunction, fasting hypoglycemia, and encephalopathy, which can result in infant…
- **Diseases (Open Targets)**: medium chain acyl-CoA dehydrogenase deficiency (0.854); hereditary disease (0.516); rhabdomyolysis (0.370); short chain acyl-CoA dehydrogenase deficiency (0.349); Epileptic spasm (0.333)
- **Europe PMC papers**: 4795
- **Why important**: ACADM is a mitochondrial medium-chain fatty-acid oxidation enzyme and participates in the only high-confidence STRING relationship involving module members, ACADM–ACAA2. It is tissue-enhanced in liver, skeletal muscle and tongue, detected in both tissues, and has extensive literature. The supplied disease association is medium-chain acyl-CoA dehydrogenase deficiency.
- **Conclusion**: Established evidence supports ACADM as a mitochondrial fatty-acid oxidation component and as part of a known relationship with ACAA2. Its participation in a shared breast–cervix metabolic state is plausible but not demonstrated by enrichment, complex data or direct functional experiments.

#### ACAA2

- **Related proteins** (co-abundance neighbors): ALDH3B1 (0.83); STRING partners: ACADM (0.937)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA acyltransferase 2. The encoded protein catalyzes the last step of the mitochondrial fatty acid beta-oxidation spiral. Unlike most mitochondrial matrix proteins, it contains a non-cleavable amino-terminal targeting signal. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: bone remodeling disease (0.270); sinusitis (0.260); refractive error (0.190); kidney disorder (0.151); myopia (0.141)
- **Europe PMC papers**: 3056
- **Why important**: ACAA2 catalyzes the final step of the mitochondrial fatty-acid beta-oxidation spiral and forms the other member of the known ACADM–ACAA2 relationship. It is tissue-enhanced in liver, detected in breast but not cervix_uterine, and has substantial literature. The supplied disease associations include bone-remodeling disease, sinusitis, refractive error and kidney disorder.
- **Conclusion**: Established evidence supports ACAA2 as a mitochondrial fatty-acid oxidation enzyme and as a known partner of ACADM. Its absence of cervix protein detection cautions against treating it as a universal protein-level marker of the shared module. A tissue-dependent metabolic contribution is a reasonable hypothesis.

#### TAP2

- **Related proteins** (co-abundance neighbors): ALDH3B1 (0.89), MSLN (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transporter 2, ATP binding cassette subfamily B member. The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily ar…
- **Diseases (Open Targets)**: MHC class I deficiency (0.729); MHC class I deficiency 2 (0.477); hereditary disease (0.193); neoplasm (0.107); cancer (0.097)
- **Europe PMC papers**: 4557
- **Why important**: TAP2 is an endoplasmic-reticulum transporter involved in TAP-dependent endogenous peptide transport and MHC class I antigen processing. It connects ALDH3B1 and MSLN in the module, is detected in breast but not cervix_uterine, and has extensive literature. Its supplied disease associations include MHC class I deficiency and neoplasm.
- **Conclusion**: Established evidence supports TAP2 as an antigen-processing and peptide-transport component, not as a metabolic enzyme. Its position may indicate an immune-interface or cell-state component within the module. It is not established that TAP2 is mechanistically coupled to the lipid-oxidation genes rather than co-varying because of cell composition or tissue context.

#### MSLN

- **Related proteins** (co-abundance neighbors): CLIC3 (0.87), TAP2 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Plasma membrane; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mesothelin. This gene encodes a preproprotein that is proteolytically processed to generate two protein products, megakaryocyte potentiating factor and mesothelin. Megakaryocyte potentiating factor functions as a cytokine that can stimulate colony formation of bone marrow megakaryocytes. Mesothelin is a glycosylphosphatidylinositol-anchored cell-surface protein that may function as a cell adhesion protein. Th…
- **Diseases (Open Targets)**: mesothelioma (0.141); neoplasm (0.139); ovarian cancer (0.135); malignant pleural mesothelioma (0.134); pancreatic neoplasm (0.131)
- **Europe PMC papers**: 3177
- **Why important**: MSLN is a cell-surface glycosylphosphatidylinositol-anchored protein associated with cell adhesion and cell-matrix adhesion. It connects CLIC3 and TAP2, is tissue-enhanced in adipose tissue and fallopian tube, is detected in cervix_uterine but not breast, and has extensive literature. The supplied disease associations include mesothelioma, ovarian cancer and pancreatic neoplasm.
- **Conclusion**: Established evidence supports MSLN as an epithelial-associated adhesion and membrane protein with disease relevance. Its cervix-restricted protein detection in this summary makes it a candidate marker of tissue-specific contribution to the shared network. It is a hypothesis, not an established fact, that MSLN-mediated adhesion or membrane biology coordinates with the module’s metabolic and antigen-presentation components.

## Module 4

**Tissue pair**: breast and cervix_uterine  
**Genes (23)**: ACAP2, ANXA3, CLU, CPPED1, DGKA, GAN, GNAQ, GYS1, HOOK1, PPP1R13L, KRT1, MVK, PRKCD, MVD, RNF170, SLC27A4, SSH3, STX3, TRIM16, TTC3, TUFT1, UBAP1, UEVLD

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent. The strongest interpretation therefore comes from gene functions, topology, HPA profiles, STRING physical association, and hu.MAP evidence. TTC3 is the central co-abundance hub and is annotated with ubiquitin-protein transferase activity and ubiquitin-dependent protein catabolism. The module also contains genes involved in vesicle and endosome trafficking, cytoskeletal organization, epithelial polarity, lipid and sterol metabolism, signal transduction, and immune-cell functions. This is best interpreted as a mixed epithelial, trafficking, proteostasis, lipid-metabolism, and immune-associated expression program rather than a single established pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: HPA identifies only TUFT1 as secreted with unknown location and CLU as secreted to blood. It is also not uniformly housekeeping-like, because many genes have tissue- or cell-type-enhanced profiles. The recurring HPA signals include esophageal and other epithelial populations, skin-related cells, neutrophils and neutrophil progenitors, basophils, and some other immune populations. Several genes are detected in both breast and cervix_uterine, but tissue detection is heterogeneous. This pattern raises the possibility that the shared module partly reflects epithelial differentiation or shared epithelial cell states, with a possible contribution from blood-cell or immune-cell admixture, especially for ANXA3, STX3, ACAP2, GNAQ, CPPED1, and related genes. The HPA evidence does not support treating the module as a purely circulating-protein signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence pair within the module, MVD--MVK, linking two enzymes in the mevalonate, sterol, and isoprenoid biosynthetic pathway. This is established supporting evidence for a lipid and isoprenoid component, but it does not explain the entire module. hu.MAP identifies a complex containing TRIM16 and TUFT1 (hu.MAP huMAP3_11660.1); most of the reported members of that complex are outside the module, so this supports a shared complex context without demonstrating that the full module is a single physical complex. The limited STRING and hu.MAP overlap indicates that much of the co-abundance structure is not already represented as a known protein-interaction network. Co-abundance edges should therefore not be interpreted as direct physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 253 gene pairs: MVD–MVK (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11660.1 (TRIM16, TUFT1; 2/43)

### Novelty

The module may represent a dataset-specific co-abundance pattern, but the available evidence is insufficient to call it a newly discovered biological complex or pathway. Its constituent functions are largely established individually, including ubiquitin-mediated proteostasis, epithelial keratinization, vesicle trafficking, actin regulation, sterol synthesis, immune-cell biology, and signaling. The MVD--MVK relationship is already known through STRING, and the TRIM16--TUFT1 complex context is represented in hu.MAP (hu.MAP huMAP3_11660.1). Limited database support can indicate an under-characterized co-abundance relationship, but absence from STRING or hu.MAP alone does not prove novelty. A claim of novelty would require independent replication, comparison with prior tissue co-expression studies, and experimental validation.

**Hypothesis.** Hypothesis: the conserved breast--cervix_uterine module reflects a shared epithelial-state program that couples epithelial differentiation and vesicle trafficking to proteostasis, membrane-lipid handling, and variable immune-cell representation. In this model, TTC3 may organize or report a proteostasis-associated transcriptional state, TRIM16 and TUFT1 may mark a secretory or epithelial complex context, and the MVD--MVK pair may represent coordinated mevalonate-pathway activity. The immune-associated genes may reflect epithelial stress, local inflammatory signaling, or sample cell composition rather than a direct physical pathway. This hypothesis is not established by the enrichment analysis because no GO or KEGG term passed global correction.

### Important genes

#### TTC3

- **Related proteins** (co-abundance neighbors): SSH3 (0.92), TUFT1 (0.92), GAN (0.91), ACAP2 (0.90), HOOK1 (0.90), KRT1 (0.90), UBAP1 (0.89), DGKA (0.86), MVK (0.84), ANXA3 (0.83), PPP1R13L (0.83), PRKCD (0.83), SLC27A4 (0.82), CLU (0.82), MVD (0.82), STX3 (0.81), GYS1 (0.81), CPPED1 (0.81), UEVLD (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tetratricopeptide repeat domain 3. Enables ubiquitin-protein transferase activity. Involved in protein K48-linked ubiquitination and ubiquitin-dependent protein catabolic process. Located in cytosol; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); placenta praevia (0.185); stroke disorder (0.149); alcohol drinking (0.145); type 2 diabetes mellitus (0.135)
- **Europe PMC papers**: 742
- **Why important**: TTC3 is the dominant network hub, connecting the otherwise weakly connected branches of the module. Its annotated ubiquitin-protein transferase activity and involvement in ubiquitin-dependent protein catabolism provide a plausible proteostasis axis. It has a substantial literature and disease-association record, although those associations do not establish a role in this breast--cervix_uterine module.
- **Conclusion**: Established: TTC3 is the main topological integrator and has documented ubiquitination-related functions. Hypothesis: its centrality may indicate a shared proteostasis or stress-related state that helps coordinate the other module components.

#### MVK

- **Related proteins** (co-abundance neighbors): TTC3 (0.84); STRING partners: MVD (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mevalonate kinase. This gene encodes the peroxisomal enzyme mevalonate kinase. Mevalonate is a key intermediate, and mevalonate kinase a key early enzyme, in isoprenoid and sterol synthesis. Mevalonate kinase deficiency caused by mutation of this gene results in mevalonic aciduria, a disease characterized psychomotor retardation, failure to thrive, hepatosplenomegaly, anemia and recurrent febrile crises. Defects in …
- **Diseases (Open Targets)**: hyperimmunoglobulinemia D with periodic fever (0.847); mevalonic aciduria (0.838); porokeratosis 3, disseminated superficial actinic type (0.748); mevalonate kinase deficiency (0.590); methylmalonic aciduria cblb type (0.555)
- **Europe PMC papers**: 3311
- **Why important**: MVK is directly paired with MVD by a high-confidence STRING interaction, and both genes participate in successive steps of mevalonate, sterol, and isoprenoid biosynthesis. MVK is tissue-enhanced in liver and detected in both relevant tissues, while its disease associations include mevalonate kinase deficiency and periodic fever syndromes. Its biochemical position makes it an informative marker of the module's lipid and isoprenoid component.
- **Conclusion**: Established: MVK is a mevalonate-pathway enzyme and forms a known relationship with MVD. Hypothesis: coordinated MVK and MVD abundance may indicate altered membrane-lipid, sterol, or prenylation demand in the shared tissue state.

#### MVD

- **Related proteins** (co-abundance neighbors): TTC3 (0.82); STRING partners: MVK (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mevalonate diphosphate decarboxylase. The enzyme mevalonate pyrophosphate decarboxylase catalyzes the conversion of mevalonate pyrophosphate into isopentenyl pyrophosphate in one of the early steps in cholesterol biosynthesis. It decarboxylates and dehydrates its substrate while hydrolyzing ATP. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: disseminated superficial actinic porokeratosis (0.767); porokeratosis 7, multiple types (0.684); neurodegenerative disease (0.547); skin disorder (0.328); linear porokeratosis (0.323)
- **Europe PMC papers**: 9949
- **Why important**: MVD is the enzymatic partner of MVK in the module and is annotated with cholesterol, isoprenoid, and geranylgeranyl-related biosynthetic functions. Its STRING relationship with MVK is the clearest known molecular connection inside the module. MVD also has a substantial disease and literature record, including associations with porokeratosis and other disorders.
- **Conclusion**: Established: MVD participates in the same early mevalonate pathway as MVK and has a high-confidence known interaction with it. Hypothesis: the MVD--MVK pair may be a functional metabolic submodule embedded within a broader epithelial or immune-associated co-abundance pattern.

#### TRIM16

- **Related proteins** (co-abundance neighbors): RNF170 (0.83), HOOK1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_11660.1
- **Function (MyGene.info)**: tripartite motif containing 16. The protein encoded by this gene is a tripartite motif (TRIM) family member that contains two B box domains and a coiled-coiled region that are characteristic of the B box zinc finger protein family. While it lacks a RING domain found in other TRIM proteins, the encoded protein can homodimerize or heterodimerize with other TRIM proteins and has E3 ubiquitin ligase activity. This gene is also a tum…
- **Diseases (Open Targets)**: digestive system disorder (0.114); melanoma (0.105); Hydrocephalus (0.100); non-small cell lung carcinoma (0.096); neuroblastoma (0.096)
- **Europe PMC papers**: 940
- **Why important**: TRIM16 has a comparatively central position within the small non-TTC3 branch and connects to RNF170 and HOOK1. It is represented with TUFT1 in a hu.MAP complex (hu.MAP huMAP3_11660.1). Its documented activities include E3 ubiquitin ligase function, secretory autophagy, retinoic-acid responses, keratinocyte differentiation, and inflammatory regulation. It also has a substantial literature base and cancer-related disease associations.
- **Conclusion**: Established: TRIM16 has documented roles in ubiquitin-related regulation, secretory autophagy, epithelial differentiation, and inflammatory signaling, and it shares a hu.MAP complex context with TUFT1 (hu.MAP huMAP3_11660.1). Hypothesis: TRIM16 could connect epithelial differentiation and secretory trafficking to the proteostasis signal represented by TTC3.

#### STX3

- **Related proteins** (co-abundance neighbors): TTC3 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntaxin 3. The gene is a member of the syntaxin family. The encoded protein is targeted to the apical membrane of epithelial cells where it forms clusters and is important in establishing and maintaining polarity necessary for protein trafficking involving vesicle fusion and exocytosis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010].
- **Diseases (Open Targets)**: retinal dystrophy and microvillus inclusion disease (0.630); diarrhea 12, with microvillus atrophy (0.516); hereditary intrinsic factor deficiency (0.443); microvillus inclusion disease (0.387); Genu varum (0.340)
- **Europe PMC papers**: 879
- **Why important**: STX3 is an epithelial apical-membrane syntaxin involved in vesicle fusion, epithelial polarity, and protein trafficking. HPA places it in several epithelial and immune-associated cell types, including neutrophil-related populations, and detects it in both breast and cervix_uterine. Its function provides a mechanistic bridge between epithelial organization, vesicular transport, and the broader trafficking signals in the module.
- **Conclusion**: Established: STX3 supports apical epithelial trafficking and vesicle fusion and is present in relevant tissue and cell-type contexts. Hypothesis: STX3 may reflect a shared epithelial polarity or secretory-state component rather than a direct interaction with the module hub.

## Module 5

**Tissue pair**: breast and cervix_uterine  
**Genes (17)**: ACBD5, PAM, CCDC91, CD109, CTTNBP2NL, CTDP1, GALNT10, GPAT3, H2AX, ITPRID2, LMO7, MIB1, NUP88, PDZD8, SCEL, TOR1AIP2, UACA

### Function

No GO/KEGG term passed global correction, and there was no supplementary STRING functional enrichment. Therefore, the module does not support a statistically established single pathway annotation. Its gene content instead suggests a mixed cellular-organization program involving membrane and cytoskeletal organization, vesicle and organelle trafficking, protein modification, nuclear transport, lipid handling, epithelial differentiation, DNA-damage response, and signaling regulation. The strongest network-centered interpretation is coordinated control of cell architecture and intracellular trafficking, with possible contributions from epithelial state, membrane glycosylation, and stress or damage responses. These are gene-function-based interpretations rather than globally significant enrichment claims.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only a minority are annotated as secreted, and most proteins are intracellular or membrane-associated. HPA data show broad or tissue-enhanced expression rather than a single tissue identity. Cell-type enhancement is widespread across epithelial, muscle, reproductive, vascular or stromal, and hematopoietic contexts. Immune-cell specificity is generally low, although selected genes show enhancement in myeloid, lymphoid, platelet, or progenitor populations. Thus, the shared breast and cervix_uterine signal is more consistent with a broadly reusable cellular-state or structural program than with a purely blood-derived module, while sample cell composition remains a plausible contributor. Protein detection in both tissues for many members supports tissue presence, but absence of detection for selected genes means that the module need not be uniformly expressed by every local cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes, so STRING does not independently support a known physical interaction network. hu.MAP provides partial, not module-wide, complex support. ITPRID2 and UACA occur together in (hu.MAP huMAP3_05613.1), and ITPRID2 and LMO7 occur together in (hu.MAP huMAP3_09542.1); both complexes contain many additional proteins outside the module. PAM and CD109 occur together in (hu.MAP huMAP3_09327.1), again within a much larger complex. PAM is also assigned to a hu.MAP complex without a demonstrated module-wide interaction structure. These observations support isolated links to known cellular assemblies, especially cytoskeletal or membrane-associated assemblies and a broader processing or trafficking-associated assembly, but they do not establish that all module members form one physical complex. The co-abundance edges should therefore be interpreted primarily as coordinated abundance relationships rather than direct protein binding.

**STRING interactions (score >= 0.7)**: 0 of 136 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05613.1 (ITPRID2, UACA; 2/11); huMAP3_09542.1 (ITPRID2, LMO7; 2/38); huMAP3_09327.1 (PAM, CD109; 2/93)

### Novelty

The module may represent a novel cross-tissue co-abundance pattern, but the evidence does not justify calling it a newly discovered molecular mechanism. Its individual genes have established functions and disease or phenotype associations, and some gene pairs share partial hu.MAP complex membership. Conversely, the lack of STRING interactions, lack of STRING functional enrichment, and lack of globally significant GO/KEGG terms provide no external confirmation of a canonical pathway or established module. The defensible novelty claim is therefore limited: the breast-cervix_uterine co-abundance arrangement and its particular combination of trafficking, structural, epithelial, nuclear, and metabolic genes may be under-described, but it requires replication, cell-composition adjustment, and experimental validation before being considered a new biological module.

**Hypothesis.** Hypothesis: the module reflects a shared tissue-cell state in which epithelial or other adherent cells coordinate cortical architecture, membrane trafficking, glycosylation, organelle contacts, and stress-responsive nuclear functions. MIB1, UACA, LMO7, SCEL, and ITPRID2 could connect signaling, adhesion, and cytoskeletal organization; CCDC91, PDZD8, GPAT3, and GALNT10 could contribute to Golgi, lipid, membrane, and glycan handling; and H2AX, NUP88, and CTDP1 could represent coupled nuclear maintenance or transcriptional responses. PAM and CD109 may connect secretory or extracellular signaling functions to this cellular state. This is a mechanistic model, not an enrichment result or demonstrated physical pathway.

### Important genes

#### MIB1

- **Related proteins** (co-abundance neighbors): PDZD8 (0.87), CCDC91 (0.84), PAM (0.84), UACA (0.81), NUP88 (0.81), CTTNBP2NL (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Microtubules, Primary cilium; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MIB E3 ubiquitin protein ligase 1. This gene encodes a protein containing multiple ankyrin repeats and RING finger domains that functions as an E3 ubiquitin ligase. The encoded protein positively regulates Notch signaling by ubiquitinating the Notch receptors, thereby facilitating their endocytosis. This protein may also promote the ubiquitination and degradation of death-associated protein kinase 1 (DAPK1). [provided by RefSeq, Ju…
- **Diseases (Open Targets)**: left ventricular noncompaction (0.625); hypercholesterolemia, familial, 1 (0.333); type 2 diabetes mellitus (0.268); Abnormality of the skeletal system (0.266); musculoskeletal system disorder (0.250)
- **Europe PMC papers**: 3711
- **Why important**: MIB1 is the most network-connected member and links PDZD8, CCDC91, PAM, UACA, NUP88, and CTTNBP2NL. Its established E3 ubiquitin-ligase function, Notch regulation, and role in endocytosis provide a plausible signaling and membrane-trafficking anchor. It is detected in both tissues, has broad tissue specificity, and has substantial literature and phenotype evidence.
- **Conclusion**: Established: MIB1 regulates ubiquitination, Notch signaling, and endocytosis. Its network position makes it a strong candidate module organizer. Hypothesis: MIB1 may coordinate the module through shared regulation of receptor turnover and intracellular trafficking, but this role is not proven by the co-abundance data.

#### H2AX

- **Related proteins** (co-abundance neighbors): SCEL (0.92), GPAT3 (0.86), PDZD8 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: H2A.X variant histone. Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Two molecules of each of the four core histones (H2A, H2B, H3, and H4) form an octamer, around which approximately 146 bp of DNA is wrapped in repeating units, called nucleosomes. The linker histone, H1, interacts with linker DNA between nucleosomes and functions in the com…
- **Diseases (Open Targets)**: cancer (0.394); breast carcinoma (0.393); melanoma (0.378); neurodevelopmental disorder (0.118); neoplasm (0.116)
- **Europe PMC papers**: 29659
- **Why important**: H2AX connects SCEL, GPAT3, and PDZD8 and is detected in both tissues. Its established roles in DNA-damage response, double-strand-break repair, nucleosome assembly, and chromatin regulation give the module a possible nuclear stress component. It also has very extensive literature and cancer-related disease associations.
- **Conclusion**: Established: H2AX is a central DNA-damage-response histone variant. Its inclusion does not establish enrichment for DNA repair because no GO/KEGG term passed global correction. Hypothesis: H2AX abundance may mark a shared epithelial or tissue stress state that is coordinated with membrane and metabolic remodeling.

#### PAM

- **Related proteins** (co-abundance neighbors): MIB1 (0.84), PDZD8 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09327.1
- **Function (MyGene.info)**: peptidylglycine alpha-amidating monooxygenase. This gene encodes a multifunctional protein. The encoded preproprotein is proteolytically processed to generate the mature enzyme. This enzyme includes two domains with distinct catalytic activities, a peptidylglycine alpha-hydroxylating monooxygenase (PHM) domain and a peptidyl-alpha-hydroxyglycine alpha-amidating lyase (PAL) domain. These catalytic domains work sequentially to catalyze the conve…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.593); diabetes mellitus (0.538); Abnormality of the skeletal system (0.517); intelligence (0.492); diabetic eye disease (0.451)
- **Europe PMC papers**: 50367
- **Why important**: PAM connects MIB1 and PDZD8 and is the module member with a well-defined secretory enzymatic function. It catalyzes peptide amidation, is localized to the Golgi and cytosol, and is tissue-enhanced in heart muscle and epididymis. Its large literature base and disease associations make it an informative indicator of regulated peptide maturation and secretory biology.
- **Conclusion**: Established: PAM performs sequential enzymatic steps required for maturation of alpha-amidated peptides and is present in a hu.MAP complex with CD109 in (hu.MAP huMAP3_09327.1). Hypothesis: PAM may connect secretory peptide processing with the broader trafficking state represented by the module, but the co-abundance pattern does not establish a shared neuroendocrine program.

#### SCEL

- **Related proteins** (co-abundance neighbors): H2AX (0.92), LMO7 (0.87), ITPRID2 (0.82), CD109 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Plasma membrane; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sciellin. The protein encoded by this gene is a precursor to the cornified envelope of terminally differentiated keratinocytes. This protein localizes to the periphery of cells and may function in the assembly or regulation of proteins in the cornified envelope. Transcript variants encoding different isoforms exist. A transcript variant utilizing an alternative polyA signal has been described in the literat…
- **Diseases (Open Targets)**: Genu varum (0.277); Genu valgum (0.277); Moyamoya disease (0.259); diabetes mellitus (0.201); Paralysis (0.188)
- **Europe PMC papers**: 895
- **Why important**: SCEL has a relatively central position and links H2AX, LMO7, ITPRID2, and CD109. It is a plasma-membrane-associated precursor involved in the cornified envelope of terminally differentiated keratinocytes, with annotations related to epidermal development, keratinocyte differentiation, mechanical response, and Wnt signaling. Its enrichment in esophageal apical cells and detection in cervix_uterine make it especially informative for an epithelial structural interpretation, despite lack of breast detection in the HPA summary.
- **Conclusion**: Established: SCEL is linked to epithelial differentiation and peripheral structural organization. Its connections to LMO7 and ITPRID2 are co-abundance relationships, while (hu.MAP huMAP3_05613.1) and (hu.MAP huMAP3_09542.1) provide partial complex context through ITPRID2. Hypothesis: SCEL may mark a shared epithelial or barrier-remodeling state across the tissues.

#### CD109

- **Related proteins** (co-abundance neighbors): SCEL (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09327.1
- **Function (MyGene.info)**: CD109 molecule. This gene encodes a glycosyl phosphatidylinositol (GPI)-linked glycoprotein that localizes to the surface of platelets, activated T-cells, and endothelial cells. The protein binds to and negatively regulates signalling by transforming growth factor beta (TGF-beta). Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2014].
- **Diseases (Open Targets)**: uterine corpus leiomyoma (0.367); color vision disorder (0.282); coronary artery disorder (0.267); myocardial infarction (0.267); glaucoma (0.267)
- **Europe PMC papers**: 2049
- **Why important**: CD109 links to SCEL and is the only member with tissue-enriched HPA expression in parathyroid gland. It is a GPI-linked cell-surface glycoprotein associated with platelets, activated T cells, and endothelial cells, and it negatively regulates TGF-beta signaling and wound healing. Its presence in (hu.MAP huMAP3_09327.1) with PAM supplies partial complex context, while its disease associations include uterine and cardiovascular phenotypes.
- **Conclusion**: Established: CD109 is a cell-surface regulator of TGF-beta signaling and wound-healing biology. The HPA profile does not support treating the module as uniformly immune-cell derived. Hypothesis: CD109 may connect epithelial repair or vascular-interface signaling to the module's structural and secretory features, but this requires tissue-cell-specific validation.

## Module 6

**Tissue pair**: breast and cervix_uterine  
**Genes (32)**: ACAD11, CDK13, CDK16, CDK7, CDK9, CSK, FER, GATB, IKBKB, IMPDH1, IRAK4, CAMK2G, RPS6KA1, RPS6KA3, MAP3K5, MAP2K3, MAP2K6, NSF, PIK3C2A, PCYT2, PI4KB, PIK3C3, RFC4, RIOK1, SAP30BP, SIL1, SMARCAL1, SMG1, STK10, STK4, TLK1, TTL

### Function

The module is strongly characterized by coordinated protein phosphorylation and kinase activity. The primary evidence is the broad enrichment of phosphotransferase, protein kinase, serine/threonine kinase, ATP-binding, and protein phosphorylation functions (4 globally significant GO/KEGG terms, q_global 2.37e-13–2.85e-12; see the table), (GO:MF protein serine kinase activity; q_global = 1.23e-10), (GO:MF protein serine/threonine kinase activity; q_global = 9.49e-10), (GO:BP protein phosphorylation; q_global = 1.17e-07) (GO:BP phosphorylation; q_global = 3.58e-07). The enrichment of the MAPK signaling pathway (KEGG MAPK signaling pathway - Homo sapiens (human); q_global = 0.000454), together with neurotrophin signaling (KEGG Neurotrophin signaling pathway - Homo sapiens (human); q_global = 0.000957) and Yersinia infection pathway (KEGG Yersinia infection - Homo sapiens (human); q_global = 0.047), supports a stress- and inflammation-responsive signaling module rather than a single narrowly defined pathway. The module also contains genes involved in chromatin regulation, transcriptional control, DNA replication and repair, vesicle trafficking, phosphoinositide metabolism, autophagy, and RNA surveillance. Thus, the best-supported interpretation is a kinase-rich signaling and stress-response module integrating MAPK, innate immune, cell-cycle, chromatin, and intracellular trafficking processes. The many closely related kinase and nucleotide-binding terms should be viewed as convergent evidence for this biochemical theme, not as independent biological functions.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the HPA summary identifies only a single secreted gene, and most genes have intracellular or membrane-associated locations. Most genes show low tissue specificity, while many show cell-type-enhanced expression. Neutrophils are the most frequent enriched single-cell type, with additional signals from myeloid, lymphoid, epithelial, glial, and other cell populations. A few genes are enhanced in bone marrow or lymphoid tissue, and several have immune-cell or neutrophil-associated profiles. Protein detection is broad in both breast and cervix_uterine. Therefore, the shared module is unlikely to represent a simple secreted-protein signature, but its preservation may partly reflect shared immune or stromal cell composition, especially myeloid and neutrophil-related contributions. The HPA evidence also supports a broadly expressed intracellular kinase program rather than a tissue-exclusive breast or cervical program.

**GO/KEGG enrichment**: 68 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF phosphotransferase activity, alcohol group as acceptor | 2.37e-13 | CAMK2G, CDK13, CDK16, CDK7, CDK9, CSK, FER, IKBKB, IRAK4, MAP2K3, MAP2K6, MAP3K5, PI4KB, PIK3C2A, PIK3C3, RIOK1, RPS6KA1, RPS6KA3, SMG1, STK10, STK4, TLK1 |
| GO:MF protein kinase activity | 1.97e-12 | CAMK2G, CDK13, CDK16, CDK7, CDK9, CSK, FER, IKBKB, IRAK4, MAP2K3, MAP2K6, MAP3K5, PIK3C3, RIOK1, RPS6KA1, RPS6KA3, SMG1, STK10, STK4, TLK1 |
| GO:MF kinase activity | 2.55e-12 | CAMK2G, CDK13, CDK16, CDK7, CDK9, CSK, FER, IKBKB, IRAK4, MAP2K3, MAP2K6, MAP3K5, PI4KB, PIK3C2A, PIK3C3, RIOK1, RPS6KA1, RPS6KA3, SMG1, STK10, STK4, TLK1 |
| GO:MF transferase activity, transferring phosphorus-containing groups | 2.85e-12 | CAMK2G, CDK13, CDK16, CDK7, CDK9, CSK, FER, IKBKB, IRAK4, MAP2K3, MAP2K6, MAP3K5, PCYT2, PI4KB, PIK3C2A, PIK3C3, RIOK1, RPS6KA1, RPS6KA3, SMG1, STK10, STK4, TLK1 |
| GO:MF ATP binding | 6.35e-11 | CAMK2G, CDK13, CDK16, CDK7, CDK9, CSK, FER, GATB, IKBKB, IRAK4, MAP2K3, MAP2K6, MAP3K5, NSF, PI4KB, PIK3C2A, PIK3C3, RFC4, RIOK1, RPS6KA1, RPS6KA3, SMARCAL1, SMG1, STK10, STK4, TLK1, TTL |
| GO:MF adenyl ribonucleotide binding | 6.66e-11 | CAMK2G, CDK13, CDK16, CDK7, CDK9, CSK, FER, GATB, IKBKB, IRAK4, MAP2K3, MAP2K6, MAP3K5, NSF, PI4KB, PIK3C2A, PIK3C3, RFC4, RIOK1, RPS6KA1, RPS6KA3, SMARCAL1, SMG1, STK10, STK4, TLK1, TTL |
| GO:MF protein serine kinase activity | 1.23e-10 | CAMK2G, CDK13, CDK16, CDK7, CDK9, IKBKB, IRAK4, MAP2K3, MAP2K6, MAP3K5, RIOK1, RPS6KA1, RPS6KA3, SMG1, STK10, STK4, TLK1 |
| GO:MF nucleotide binding | 4.99e-10 | ACAD11, CAMK2G, CDK13, CDK16, CDK7, CDK9, CSK, FER, GATB, IKBKB, IMPDH1, IRAK4, MAP2K3, MAP2K6, MAP3K5, NSF, PI4KB, PIK3C2A, PIK3C3, RFC4, RIOK1, RPS6KA1, RPS6KA3, SMARCAL1, SMG1, STK10, STK4, TLK1, TTL |
| GO:MF adenyl nucleotide binding | 5.9e-10 | CAMK2G, CDK13, CDK16, CDK7, CDK9, CSK, FER, GATB, IKBKB, IRAK4, MAP2K3, MAP2K6, MAP3K5, NSF, PI4KB, PIK3C2A, PIK3C3, RFC4, RIOK1, RPS6KA1, RPS6KA3, SMARCAL1, SMG1, STK10, STK4, TLK1, TTL |
| GO:MF nucleoside phosphate binding | 7.27e-10 | ACAD11, CAMK2G, CDK13, CDK16, CDK7, CDK9, CSK, FER, GATB, IKBKB, IMPDH1, IRAK4, MAP2K3, MAP2K6, MAP3K5, NSF, PI4KB, PIK3C2A, PIK3C3, RFC4, RIOK1, RPS6KA1, RPS6KA3, SMARCAL1, SMG1, STK10, STK4, TLK1, TTL |
| GO:MF protein serine/threonine kinase activity | 9.49e-10 | CAMK2G, CDK13, CDK16, CDK7, CDK9, IKBKB, IRAK4, MAP2K3, MAP2K6, MAP3K5, RIOK1, RPS6KA1, RPS6KA3, SMG1, STK10, STK4, TLK1 |
| GO:MF purine ribonucleoside triphosphate binding | 2.36e-09 | CAMK2G, CDK13, CDK16, CDK7, CDK9, CSK, FER, GATB, IKBKB, IRAK4, MAP2K3, MAP2K6, MAP3K5, NSF, PI4KB, PIK3C2A, PIK3C3, RFC4, RIOK1, RPS6KA1, RPS6KA3, SMARCAL1, SMG1, STK10, STK4, TLK1, TTL |
| GO:MF purine ribonucleotide binding | 2.47e-09 | CAMK2G, CDK13, CDK16, CDK7, CDK9, CSK, FER, GATB, IKBKB, IRAK4, MAP2K3, MAP2K6, MAP3K5, NSF, PI4KB, PIK3C2A, PIK3C3, RFC4, RIOK1, RPS6KA1, RPS6KA3, SMARCAL1, SMG1, STK10, STK4, TLK1, TTL |
| GO:MF heterocyclic compound binding | 3.04e-09 | ACAD11, CAMK2G, CDK13, CDK16, CDK7, CDK9, CSK, FER, GATB, IKBKB, IMPDH1, IRAK4, MAP2K3, MAP2K6, MAP3K5, NSF, PI4KB, PIK3C2A, PIK3C3, RFC4, RIOK1, RPS6KA1, RPS6KA3, SMARCAL1, SMG1, STK10, STK4, TLK1, TTL |
| GO:MF ribonucleotide binding | 3.07e-09 | CAMK2G, CDK13, CDK16, CDK7, CDK9, CSK, FER, GATB, IKBKB, IRAK4, MAP2K3, MAP2K6, MAP3K5, NSF, PI4KB, PIK3C2A, PIK3C3, RFC4, RIOK1, RPS6KA1, RPS6KA3, SMARCAL1, SMG1, STK10, STK4, TLK1, TTL |

### STRING and hu.MAP

STRING provides strong known relationships within several coherent substructures: MAP2K3–MAP2K6 and both MAP2K genes with MAP3K5 define a MAPK-related signaling core; CDK7, CDK9, and CDK13 form a transcription-associated kinase cluster; PI4KB connects with PIK3C2A and PIK3C3 in phosphoinositide and membrane-trafficking biology; RPS6KA1 and RPS6KA3 form an RSK pair; and IKBKB connects with IRAK4 in innate immune signaling. These relationships support the biological validity of portions of the co-abundance module, although STRING enrichment is supplementary and its within-query FDR is not global evidence. hu.MAP independently identifies complexes containing RPS6KA1 and RPS6KA3 (hu.MAP huMAP3_03542.1), (hu.MAP huMAP3_08875.1) (hu.MAP huMAP3_09817.1) (hu.MAP huMAP3_11291.1) (hu.MAP huMAP3_13479.1) (hu.MAP huMAP3_14916.1), and a complex containing MAP2K3 and MAP2K6 (hu.MAP huMAP3_01852.1). The known complexes and high-confidence STRING links show that the module contains real pathway and complex-level structure. However, many module edges lack STRING support, so co-abundance should not be interpreted as direct physical interaction throughout the entire module.

**STRING interactions (score >= 0.7)**: 10 of 496 gene pairs: CDK13–CDK7 (0.808); CDK13–CDK9 (0.867); CDK7–CDK9 (0.99); IKBKB–IRAK4 (0.935); MAP2K3–MAP2K6 (0.989); MAP2K3–MAP3K5 (0.988); MAP2K6–MAP3K5 (0.993); PI4KB–PIK3C2A (0.912); PI4KB–PIK3C3 (0.938); RPS6KA1–RPS6KA3 (0.922)
**STRING functional enrichment (supplementary, within-query FDR)**: InterPro Protein kinase-like domain superfamily (FDR = 6.39e-18, 23 genes); Keyword Kinase (FDR = 6.18e-15, 22 genes); Function Phosphotransferase activity, alcohol group as acceptor (FDR = 1.75e-14, 22 genes); Function Protein kinase activity (FDR = 9.44e-14, 20 genes); Function Kinase activity (FDR = 9.44e-14, 22 genes); Function Transferase activity, transferring phosphorus-containing groups (FDR = 9.44e-14, 23 genes); Function Adenyl nucleotide binding (FDR = 9.44e-14, 28 genes); Keyword ATP-binding (FDR = 1.14e-13, 27 genes); Function Nucleotide binding (FDR = 1.72e-13, 30 genes); Function ATP binding (FDR = 2.14e-13, 27 genes); Function Protein serine kinase activity (FDR = 1.57e-12, 17 genes); Keyword Serine/threonine-protein kinase (FDR = 4.06e-12, 17 genes); Function Protein serine/threonine kinase activity (FDR = 1.04e-11, 17 genes); Process Phosphorylation (FDR = 1.42e-11, 22 genes); InterPro Protein kinase domain (FDR = 3.78e-11, 17 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03542.1 (RPS6KA3, RPS6KA1; 2/2); huMAP3_01852.1 (MAP2K3, MAP2K6; 2/2); huMAP3_08875.1 (RPS6KA3, RPS6KA1; 2/3); huMAP3_09817.1 (RPS6KA3, RPS6KA1; 2/7); huMAP3_11291.1 (RPS6KA3, RPS6KA1; 2/7); huMAP3_13479.1 (RPS6KA3, RPS6KA1; 2/11); huMAP3_14916.1 (RPS6KA3, RPS6KA1; 2/11)

### Novelty

The module should not be called a wholly new molecular pathway. Its MAPK, RSK, CDK, phosphoinositide, and innate immune components are established, as shown by the STRING relationships, hu.MAP complexes, and gene annotations. Nevertheless, the conserved co-abundance organization across breast and cervix_uterine may be a novel systems-level observation, particularly because it brings together several known signaling and cellular-maintenance programs in a tissue-pair-specific module. The absence of some relationships from STRING or hu.MAP does not establish novelty; it may reflect incomplete interaction coverage, context dependence, indirect regulation, or co-regulation rather than physical binding. Novelty is therefore best stated as a potentially new cross-tissue co-abundance configuration of known biology, requiring validation in independent cohorts and perturbation experiments.

**Hypothesis.** Hypothesis: the module represents a coordinated stress-adaptation program in which MAP3K5 activates the MAP2K3/MAP2K6 p38-related arm, while IRAK4 and IKBKB provide innate immune inputs. Downstream RPS6KA1 and RPS6KA3 may transmit these signals to transcriptional, growth, and differentiation outputs. TLK1, CDK7, CDK9, CDK13, SMARCAL1, RFC4, and related nuclear factors could couple the signaling state to chromatin, transcription, replication, and DNA-damage responses. PI4KB, PIK3C2A, PIK3C3, NSF, and PCYT2 could connect the response to membrane trafficking, autophagy, and lipid metabolism. The shared module may therefore reflect a conserved balance between inflammatory signaling, cellular stress, and tissue-maintenance functions, potentially amplified by shared immune-cell composition. This is a mechanistic model, not a demonstrated causal pathway.

### Important genes

#### TLK1

- **Related proteins** (co-abundance neighbors): FER (0.90), IKBKB (0.89), SMARCAL1 (0.88), MAP2K6 (0.87), IRAK4 (0.87), PIK3C3 (0.85), PIK3C2A (0.82), CDK13 (0.82), PCYT2 (0.82), STK4 (0.81), CAMK2G (0.80), SAP30BP (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tousled like kinase 1. The protein encoded by this gene is a serine/threonine kinase that may be involved in the regulation of chromatin assembly. The encoded protein is only active when it is phosphorylated, and this phosphorylation is cell cycle-dependent, with the maximal activity of this protein coming during S phase. The catalytic activity of this protein is diminished by DNA damage and by blockage of DNA replicati…
- **Diseases (Open Targets)**: neurodegenerative disease (0.508); cancer (0.295); mixed connective tissue disease (0.262); autoimmune disorder of central nervous system (0.184); oropharynx cancer (0.145)
- **Europe PMC papers**: 635
- **Why important**: TLK1 has the strongest weighted network position in the supplied subgraph and connects nuclear maintenance, MAPK- and immune-associated genes, phosphoinositide-related genes, and replication or chromatin factors. Its established annotation describes a serine/threonine kinase involved in chromatin assembly, with activity linked to cell-cycle state, DNA replication, and DNA damage. It is supported across the principal kinase and phosphorylation terms (27 globally significant GO/KEGG terms, q_global 2.37e-13–0.0003; see the table) and the supplementary kinase terms (15 supplementary STRING terms; within-query FDR 6.39e-18–3.78e-11). Its disease associations include cancer and neurodegenerative disease, while its literature volume is substantial.
- **Conclusion**: Established evidence supports TLK1 as a central kinase and chromatin-maintenance component of the module. Its network position makes it a plausible integrator, but the co-abundance data do not demonstrate that TLK1 directly regulates all of its module neighbors. A role linking stress signaling to replication or chromatin responses remains a hypothesis.

#### MAP3K5

- **Related proteins** (co-abundance neighbors): MAP2K3 (0.95), PI4KB (0.93), GATB (0.92), MAP2K6 (0.92), CDK9 (0.91), CDK7 (0.88), RPS6KA3 (0.87), SMG1 (0.87), IMPDH1 (0.84), NSF (0.82), SIL1 (0.81); STRING partners: MAP2K3 (0.988), MAP2K6 (0.993)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitogen-activated protein kinase kinase kinase 5. Mitogen-activated protein kinase (MAPK) signaling cascades include MAPK or extracellular signal-regulated kinase (ERK), MAPK kinase (MKK or MEK), and MAPK kinase kinase (MAPKKK or MEKK). MAPKK kinase/MEKK phosphorylates and activates its downstream protein kinase, MAPK kinase/MEK, which in turn activates MAPK. The kinases of these signaling cascades are highly conserved, and homologs exist in yeas…
- **Diseases (Open Targets)**: smoking initiation (0.313); neurodegenerative disease (0.239); metabolic dysfunction-associated steatohepatitis (0.198); cervical carcinoma (0.189); cirrhosis of liver (0.152)
- **Europe PMC papers**: 2289
- **Why important**: MAP3K5 is among the most connected genes and occupies the central upstream position of the MAPK substructure. It has known STRING relationships with MAP2K3 and MAP2K6, and its annotation supports MAPK, JNK, oxidative-stress, starvation, and endoplasmic-reticulum-stress signaling. It contributes to the globally supported MAPK pathway term (KEGG MAPK signaling pathway - Homo sapiens (human); q_global = 0.000454) and several stress- and phosphorylation-related terms. Its disease associations include cervical carcinoma and neurodegenerative and metabolic disease, and it has a substantial literature base.
- **Conclusion**: Established evidence identifies MAP3K5 as a credible upstream stress-signaling hub connected to the MAP2K3/MAP2K6 pair. Its co-abundance with nuclear, metabolic, and immune genes suggests broader coordination, but direct cross-compartment regulation by MAP3K5 is not established by this module alone.

#### MAP2K6

- **Related proteins** (co-abundance neighbors): MAP3K5 (0.92), CDK16 (0.91), TTL (0.91), TLK1 (0.87), FER (0.87), RFC4 (0.85), STK4 (0.83), SMG1 (0.82), RPS6KA3 (0.82), ACAD11 (0.81), STK10 (0.81); STRING partners: MAP2K3 (0.989), MAP3K5 (0.993)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: huMAP3_01852.1
- **Function (MyGene.info)**: mitogen-activated protein kinase kinase 6. This gene encodes a member of the dual specificity protein kinase family, which functions as a mitogen-activated protein (MAP) kinase kinase. MAP kinases, also known as extracellular signal-regulated kinases (ERKs), act as an integration point for multiple biochemical signals. This protein phosphorylates and activates p38 MAP kinase in response to inflammatory cytokines or environmental stress. As…
- **Diseases (Open Targets)**: neurodegenerative disease (0.504); osteoarthritis, hip (0.493); osteoarthritis, knee (0.482); osteoarthritis (0.460); Abnormality of the skeletal system (0.425)
- **Europe PMC papers**: 1961
- **Why important**: MAP2K6 has a highly connected position and is part of the strongest STRING-supported MAPK substructure with MAP2K3 and MAP3K5. Its established function is activation of p38 MAPK in response to inflammatory cytokines and environmental stress. It is represented in the MAPK and Yersinia infection terms (KEGG MAPK signaling pathway - Homo sapiens (human); q_global = 0.000454), (KEGG Yersinia infection - Homo sapiens (human); q_global = 0.047), and in the hu.MAP complex with MAP2K3 (hu.MAP huMAP3_01852.1). Its HPA profile includes neutrophil and monocyte-associated expression, providing a plausible link between the signaling program and immune-cell composition.
- **Conclusion**: Established evidence supports MAP2K6 as a central stress- and inflammation-responsive kinase in the module. The shared breast and cervix_uterine signal may reflect a conserved p38-related program, potentially influenced by immune-cell abundance. Whether MAP2K6 is a causal driver of the full module remains untested.

#### IRAK4

- **Related proteins** (co-abundance neighbors): FER (0.87), TLK1 (0.87); STRING partners: IKBKB (0.935)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules, Cytosol; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: interleukin 1 receptor associated kinase 4. This gene encodes a kinase that activates NF-kappaB in both the Toll-like receptor (TLR) and T-cell receptor (TCR) signaling pathways. The protein is essential for most innate immune responses. Mutations in this gene result in IRAK4 deficiency and recurrent invasive pneumococcal disease. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Au…
- **Diseases (Open Targets)**: immunodeficiency 67 (0.774); inborn error of immunity (0.464); autoimmune disorder of central nervous system (0.371); immunodeficiency 33 (0.333); congenital dyserythropoietic anemia (0.296)
- **Europe PMC papers**: 6476
- **Why important**: IRAK4 is a well-established kinase in Toll-like receptor and T-cell receptor signaling and is essential for many innate immune responses. It has a high-confidence STRING relationship with IKBKB and contributes to the MAPK, neurotrophin, and Yersinia infection terms (KEGG MAPK signaling pathway - Homo sapiens (human); q_global = 0.000454), (KEGG Neurotrophin signaling pathway - Homo sapiens (human); q_global = 0.000957), (KEGG Yersinia infection - Homo sapiens (human); q_global = 0.047), as well as the broad kinase terms. Its neutrophil-associated HPA profile and strong immune-disease associations make it especially informative for evaluating whether the module contains an immune-cell component. It also has a large literature volume.
- **Conclusion**: Established evidence supports IRAK4 as an innate immune signaling component and a plausible explanation for part of the module's immune-associated character. Its presence does not prove that the entire module derives from infiltrating immune cells; it may also reflect signaling within tissue-resident cells.

#### RPS6KA3

- **Related proteins** (co-abundance neighbors): MAP3K5 (0.87), FER (0.86), MAP2K6 (0.82); STRING partners: RPS6KA1 (0.922)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: huMAP3_03542.1, huMAP3_08875.1, huMAP3_09817.1, huMAP3_11291.1, huMAP3_13479.1, huMAP3_14916.1
- **Function (MyGene.info)**: ribosomal protein S6 kinase A3. This gene encodes a member of the RSK (ribosomal S6 kinase) family of serine/threonine kinases. This kinase contains 2 non-identical kinase catalytic domains and phosphorylates various substrates, including members of the mitogen-activated kinase (MAPK) signalling pathway. The activity of this protein has been implicated in controlling cell growth and differentiation. Mutations in this gene have b…
- **Diseases (Open Targets)**: Coffin-Lowry syndrome (0.832); intellectual disability, X-linked 19 (0.764); non-syndromic X-linked intellectual disability (0.660); hereditary disease (0.543); hepatocellular carcinoma (0.536)
- **Europe PMC papers**: 1650
- **Why important**: RPS6KA3 is a downstream serine/threonine kinase in the RSK family, with a dual catalytic-domain architecture and established roles in MAPK signaling, growth, differentiation, transcription, and neural development. It is linked to MAP3K5 in the co-abundance network, pairs with RPS6KA1 in STRING, and appears in multiple hu.MAP complexes (hu.MAP huMAP3_03542.1), (hu.MAP huMAP3_08875.1) (hu.MAP huMAP3_09817.1) (hu.MAP huMAP3_11291.1) (hu.MAP huMAP3_13479.1) (hu.MAP huMAP3_14916.1). It contributes to the MAPK and neurotrophin pathway terms (KEGG MAPK signaling pathway - Homo sapiens (human); q_global = 0.000454), (KEGG Neurotrophin signaling pathway - Homo sapiens (human); q_global = 0.000957) and has a strong disease association with Coffin-Lowry syndrome and related intellectual-disability phenotypes. Its literature volume is substantial.
- **Conclusion**: Established evidence supports RPS6KA3 as a functionally meaningful downstream signaling node and a validated complex-associated component of the module. Its co-abundance with upstream stress kinases is consistent with pathway coordination, but it does not establish direct activation or substrate relationships in breast or cervix_uterine.

## Module 7

**Tissue pair**: breast and cervix_uterine  
**Genes (5)**: ACOX3, ATP11B, BICDL2, TSC22D2, TUBA4A

### Function

This is a small, heterogeneous intracellular module rather than a confidently established GO or KEGG pathway. No GO/KEGG term passed global correction, so there is no globally supported enrichment claim. The strongest functional interpretation comes from the gene annotations and the co-abundance structure: BICDL2 is the central hub and is linked to microtubule-based vesicle transport; TUBA4A represents the microtubule cytoskeleton; ATP11B represents phospholipid and aminophospholipid translocation; ACOX3 represents peroxisomal fatty-acid oxidation; and TSC22D2 represents transcriptional and osmotic-stress regulation. Thus, the module may reflect coordinated epithelial or cellular structural state, trafficking, membrane-lipid handling, and metabolic regulation, but the absence of global enrichment means this interpretation remains gene-annotation-led rather than pathway-proven.

**Cell composition.** The module is not composed of plasma or secreted proteins: no member is annotated as secreted. HPA shows generally low tissue specificity and low immune-cell specificity, with one member not detected in immune cells. The module is therefore not strongly indicative of a blood-cell or circulating-protein signal. Several members show cell-type patterns involving esophageal apical cells, while other signals involve neutrophils, photoreceptors, syncytiotrophoblasts, muscle, tongue, or epithelial cell types. This heterogeneity argues against assigning the shared breast–cervix_uterine module to one highly specific tissue lineage. Detection of several proteins in both breast and cervix_uterine supports biological presence in the sampled tissues, although the absence of TSC22D2 detection in breast and ATP11B detection in either tissue cautions against assuming uniform protein-level expression.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was present among the module members, and STRING functional enrichment was absent. No hu.MAP complex contained multiple module members. The observed co-abundance graph is therefore not supported here as a known physical interaction network or a known multiprotein complex. Its structure is a hub-and-spoke pattern centered on BICDL2, with TUBA4A, ATP11B, ACOX3, and TSC22D2 each connected to that hub in the co-abundance data. These edges should be interpreted as coordinated abundance relationships, not established direct binding relationships.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a novel tissue-pair co-abundance pattern, but it cannot be called a new molecular complex or a newly discovered pathway. The cautious basis for novelty is the breast–cervix_uterine co-abundance pattern together with the lack of a corresponding high-confidence STRING network, STRING enrichment, or hu.MAP complex. Those absences do not prove biological novelty: the pattern could reflect context-dependent regulation, shared epithelial or other cell-state composition, technical or sampling effects, or relationships not captured by the reference resources. Replication in independent breast and cervix_uterine datasets, preservation after cell-composition adjustment, and targeted interaction or perturbation experiments would be needed to establish novelty.

**Hypothesis.** Hypothesis: in a shared epithelial or tissue-cell state, BICDL2-centered microtubule trafficking could coordinate intracellular cargo movement with membrane-lipid handling by ATP11B, while TUBA4A provides the relevant cytoskeletal framework. ACOX3 could couple this state to peroxisomal branched-fatty-acid metabolism, and TSC22D2 could modulate transcriptional adaptation to cellular stress. Under this model, the module is a coordinated cell-state program rather than a stable physical complex. This is a hypothesis: the fact sheet does not establish causality, direct binding, or a single common pathway.

### Important genes

#### BICDL2

- **Related proteins** (co-abundance neighbors): TUBA4A (0.88), ATP11B (0.86), ACOX3 (0.83), TSC22D2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Intermediate filaments, Actin filaments, Cytosol; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BICD family like cargo adaptor 2. Predicted to enable small GTPase binding activity. Predicted to be involved in Golgi to secretory granule transport and vesicle transport along microtubule. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: polycystic kidney disease 5 (0.054); hereditary neutrophilia (0.054); nephronophthisis (0.049); glycoprotein storage disease (0.047); nephronophthisis 19 (0.047)
- **Europe PMC papers**: 37
- **Why important**: BICDL2 is the central network hub, connected to every other module member, and has the strongest weighted connectivity in the module. Its annotated role in small-GTPase binding and Golgi-to-secretory-granule or microtubule-associated vesicle transport provides the clearest functional anchor for the module. HPA places it in cytosolic, actin-filament, and intermediate-filament locations and shows enrichment in esophagus and pancreas, with an esophageal apical-cell pattern. Its disease associations include several renal and neutrophilia-related conditions, while its literature volume is comparatively limited.
- **Conclusion**: Established evidence supports BICDL2 as the best network and trafficking marker of the module. My conclusion is that BICDL2 is the leading candidate driver or organizer of the co-abundance pattern, but a causal role in the breast–cervix_uterine context remains hypothetical because no supporting STRING or hu.MAP relationship is present.

#### TUBA4A

- **Related proteins** (co-abundance neighbors): BICDL2 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tubulin alpha 4a. Microtubules of the eukaryotic cytoskeleton perform essential and diverse functions and are composed of a heterodimer of alpha and beta tubulin. The genes encoding these microtubule constituents are part of the tubulin superfamily, which is composed of six distinct families. Genes from the alpha, beta and gamma tubulin families are found in all eukaryotes. The alpha and beta tubulins represent the…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.778); amyotrophic lateral sclerosis type 22 (0.700); breast cancer (0.607); non-small cell lung carcinoma (0.607); breast carcinoma (0.598)
- **Europe PMC papers**: 1797
- **Why important**: TUBA4A is the module's direct microtubule-associated partner of BICDL2 and provides a strong cytoskeletal interpretation for the hub connection. Its annotations include microtubule organization and microtubule-based processes, and HPA places it in microtubules with tissue enhancement in skeletal muscle and tongue and cell-type enhancement in several epithelial and germ-cell contexts. It has substantial literature and disease associations including amyotrophic lateral sclerosis and breast cancer.
- **Conclusion**: Established evidence supports TUBA4A as a cytoskeletal component compatible with BICDL2-mediated cargo movement. My conclusion is that TUBA4A may report microtubule or cell-architecture state in this module, but the co-abundance edge does not demonstrate direct functional coupling in these tissues.

#### ATP11B

- **Related proteins** (co-abundance neighbors): BICDL2 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Centriolar satellite, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase phospholipid transporting 11B (putative). P-type ATPases, such as ATP11B, are phosphorylated in their intermediate state and drive uphill transport of ions across membranes. Several subfamilies of P-type ATPases have been identified. One subfamily transports heavy metal ions, such as Cu(2+) or Cd(2+). Another subfamily transports non-heavy metal ions, such as H(+), Na(+), K(+), or Ca(+). A third subfamily transports amphipaths, such as ph…
- **Diseases (Open Targets)**: hearing loss disorder (0.461); presbycusis (0.382); alcohol drinking (0.370); androgenetic alopecia (0.299); placenta praevia (0.260)
- **Europe PMC papers**: 370
- **Why important**: ATP11B is directly connected to the hub and contributes a distinct membrane biology dimension through phospholipid, aminophospholipid, and ion-transport annotations. HPA describes low tissue specificity and group-enriched patterns in esophageal apical cells, neutrophil progenitors, and neutrophils, while showing no immune-cell enrichment at the broad blood-cell level. Its disease associations include hearing-related disorders, and it has a substantial but smaller literature than TUBA4A.
- **Conclusion**: Established evidence supports ATP11B as a plausible membrane-lipid transport marker linked to the hub state. My conclusion is that it could connect vesicle trafficking with membrane asymmetry or lipid handling, but this mechanistic connection is a hypothesis rather than an established relationship in the module.

#### ACOX3

- **Related proteins** (co-abundance neighbors): BICDL2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Peroxisomes; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA oxidase 3, pristanoyl. Acyl-Coenzyme A oxidase 3 also know as pristanoyl -CoA oxidase (ACOX3)is involved in the desaturation of 2-methyl branched fatty acids in peroxisomes.  Unlike the rat homolog, the human gene is expressed in very low amounts in liver such that its mRNA was undetectable by routine Northern-blot analysis or its product by immunoblotting or by enzyme activity measurements.  However the human cDNA enco…
- **Diseases (Open Targets)**: atrial fibrillation (0.331); glaucoma (0.277); mouth disorder (0.188); Pathologic fracture (0.185); skin wound (0.177)
- **Europe PMC papers**: 746
- **Why important**: ACOX3 is connected to BICDL2 and introduces peroxisomal metabolism into an otherwise largely structural and trafficking-oriented interpretation. Its annotated functions include branched-fatty-acid desaturation and peroxisomal fatty-acid beta-oxidation. HPA places it in peroxisomes and identifies cell-type enhancement in cone photoreceptors, esophageal apical cells, and syncytiotrophoblasts. It has disease associations involving atrial fibrillation, glaucoma, oral disorders, fracture, and wound biology, with a substantial literature base.
- **Conclusion**: Established evidence supports ACOX3 as a peroxisomal fatty-acid metabolism gene. My conclusion is that its presence broadens the module beyond a simple cytoskeletal program and may indicate metabolic support for a shared cell state, but no evidence proves that ACOX3 participates in BICDL2-dependent trafficking.

#### TSC22D2

- **Related proteins** (co-abundance neighbors): BICDL2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TSC22 domain family member 2. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to act upstream of or within response to osmotic stress. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.413); type 2 diabetes mellitus (0.394); hypertensive disorder (0.384); glaucoma (0.368); essential hypertension (0.360)
- **Europe PMC papers**: 397
- **Why important**: TSC22D2 is connected to the central hub and contributes transcriptional and stress-response biology through regulation of RNA polymerase II transcription, negative cell-cycle regulation, and osmotic-stress response. HPA reports low tissue specificity, cell-type enhancement in distal convoluted tubule, ocular epithelial, and urothelial cells, and protein detection in cervix_uterine but not breast. Its disease associations include skeletal, metabolic, ocular, and hypertensive conditions, and it has a moderate literature volume.
- **Conclusion**: Established evidence supports TSC22D2 as a regulatory and stress-response component rather than a structural complex member. My conclusion is that it may represent transcriptional adaptation associated with the co-abundance state, but its asymmetric tissue protein detection makes it a less secure universal marker of the shared module.

## Module 8

**Tissue pair**: breast and cervix_uterine  
**Genes (12)**: ADCY9, CYTH1, DIP2B, FCHO2, ILK, RPS6KB1, MED12, NUDT12, PLEKHA7, ROCK1, USP25, VPS13B

### Function

The module does not have a GO or KEGG term that passed global correction. Its structure nevertheless suggests a heterogeneous membrane and intracellular signaling module rather than a single established pathway. ADCY9 is the central network hub and provides a cyclic AMP signaling connection. ROCK1 and ILK provide Rho-dependent and integrin-linked signaling functions, while PLEKHA7 and CYTH1 support epithelial adhesion, polarity, membrane association, vesicle traffic, and ARF signaling. The remaining genes connect to transcriptional regulation, vesicle sorting, endocytosis, nutrient-responsive growth signaling, deubiquitination, and nucleotide metabolism. These annotations support a cautious interpretation as a co-abundance module involving membrane signaling, cell adhesion, trafficking, and cellular state regulation, but not as a formally enriched biological pathway.

**Cell composition.** The module is not composed of secreted proteins, so it does not resemble a plasma-protein or secretome module. Most genes have low tissue specificity, and the HPA data show broad protein detection in both breast and cervix_uterine where data are available. Many genes are cell-type enhanced, with neutrophil-related signals recurring in the HPA summary and additional signals from epithelial, muscle, platelet, monocyte, and other cell types. This makes shared cellular composition, including immune-cell or stromal-cell contributions, a plausible explanation for part of the cross-tissue co-abundance. The module should therefore not be interpreted automatically as intrinsic to breast and cervical epithelial cells. The HPA evidence also supports a contribution from broadly expressed intracellular housekeeping or regulatory proteins, although the genes are functionally diverse rather than a canonical housekeeping set.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair reached the supplied high-confidence STRING interaction threshold, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance relationships are not supported here by high-confidence known physical interactions or by a shared hu.MAP complex. The genes do have established individual functions and disease associations, but the module-level network appears to be an expression or abundance association rather than a known protein complex. The absence of STRING and hu.MAP support limits claims of direct molecular assembly and does not by itself establish that the module is novel.

**STRING interactions (score >= 0.7)**: 0 of 66 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module is potentially unusual as a cross-tissue co-abundance pattern because it links genes from several established functional areas without a globally corrected GO or KEGG theme, without STRING enrichment, without high-confidence STRING pairwise support, and without a shared hu.MAP complex. However, it cannot be called a new biological discovery from these results alone. The component functions are already established, the network is sparse, and the pattern could reflect shared cell types, technical or tissue-composition effects, or coordinated regulation of broadly expressed genes. Novelty would require independent replication, control for cellular composition and abundance effects, and experimental testing of the proposed connections.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of membrane-associated signaling and trafficking in a shared cellular component present in both tissues. ADCY9 may couple extracellular or receptor-linked inputs to cyclic AMP production, while ROCK1, ILK, and PLEKHA7 may connect signaling to cytoskeletal organization, focal adhesion, epithelial junctions, and polarity. CYTH1 and FCHO2 may link membrane recruitment and endocytic trafficking, with the other genes representing transcriptional, vesicular, metabolic, growth, and protein-quality-control responses. The recurrent HPA cell-type signals suggest that this coordination may arise partly from a shared immune or stromal contribution rather than from a breast-and-cervix-specific epithelial mechanism. This is a hypothesis, not an established module function.

### Important genes

#### ADCY9

- **Related proteins** (co-abundance neighbors): MED12 (0.86), ROCK1 (0.86), VPS13B (0.84), ILK (0.84), RPS6KB1 (0.83), NUDT12 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenylate cyclase 9. Adenylate cyclase is a membrane bound enzyme that catalyses the formation of cyclic AMP from ATP. It is regulated by a family of G protein-coupled receptors, protein kinases, and calcium. The type 9 adenylyl cyclase is a widely distributed adenylyl cyclase, and it is stimulated by beta-adrenergic receptor activation but is insensitive to forskolin, calcium, and somatostatin. [provided by RefSeq, J…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.540); obesity disorder (0.494); hypertensive disorder (0.466); hypothyroidism (0.464); morbid obesity (0.427)
- **Europe PMC papers**: 1598
- **Why important**: ADCY9 is the central hub of the module, connecting to genes involved in transcriptional regulation, cytoskeletal signaling, vesicle sorting, focal adhesion, growth signaling, and nucleotide metabolism. Its established function is membrane-associated cyclic AMP production regulated by receptor, kinase, and calcium-related inputs. HPA describes tissue enhancement in skeletal muscle and absence from immune cells, while its protein is detected in both relevant tissues. Its substantial literature and disease associations make it the strongest candidate for organizing the module's signaling interpretation.
- **Conclusion**: Established evidence supports ADCY9 as a cyclic AMP signaling enzyme and as the most connected module member. It is plausible that ADCY9 helps coordinate the observed co-abundance pattern, but the network does not establish direct physical interaction or prove that cyclic AMP signaling drives the module.

#### ROCK1

- **Related proteins** (co-abundance neighbors): ADCY9 (0.86), PLEKHA7 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho associated coiled-coil containing protein kinase 1. This gene encodes a protein serine/threonine kinase that is activated when bound to the GTP-bound form of Rho. The small GTPase Rho regulates formation of focal adhesions and stress fibers of fibroblasts, as well as adhesion and aggregation of platelets and lymphocytes by shuttling between the inactive GDP-bound form and the active GTP-bound form. Rho is also essential in cytokinesis and plays a r…
- **Diseases (Open Targets)**: open-angle glaucoma (0.605); ocular hypertension (0.590); glaucoma (0.563); neurodegenerative disease (0.555); graft versus host disease (0.554)
- **Europe PMC papers**: 9251
- **Why important**: ROCK1 is a well-characterized Rho-activated serine/threonine kinase with roles in focal adhesions, stress fibers, cytokinesis, epithelial-to-mesenchymal transition, smooth muscle contraction, and leukocyte adhesion. Within this module it connects ADCY9 and PLEKHA7, placing it at the interface between signaling, cytoskeletal behavior, and epithelial junction biology. It has extensive literature and disease associations, making it an important mechanistic anchor despite its limited local connectivity.
- **Conclusion**: Established evidence supports ROCK1 as a regulator of Rho-dependent cytoskeletal and adhesion processes. A connection between ROCK1, ADCY9, and PLEKHA7 is a reasonable module-level hypothesis, but the co-abundance network does not demonstrate biochemical coupling.

#### PLEKHA7

- **Related proteins** (co-abundance neighbors): CYTH1 (0.87), ROCK1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Nucleoplasm, Cell Junctions; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pleckstrin homology domain containing A7. Enables delta-catenin binding activity. Involved in epithelial cell-cell adhesion; pore complex assembly; and zonula adherens maintenance. Located in several cellular components, including centrosome; nucleoplasm; and zonula adherens. Part of pore complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypertensive disorder (0.496); glaucoma (0.495); open-angle glaucoma (0.494); alcohol drinking (0.440); cleft lip (0.413)
- **Europe PMC papers**: 618
- **Why important**: PLEKHA7 is associated with epithelial cell-cell adhesion, zonula adherens maintenance, epithelial polarity, and pore-complex assembly. It connects CYTH1 and ROCK1, creating the clearest local bridge between membrane trafficking or ARF signaling and junctional cytoskeletal regulation. HPA places it at cell junctions and reports enhancement in several epithelial cell types, while also reporting selected blood-cell enrichment. Its disease associations include ocular and vascular-related conditions, and its literature supports a specialized adhesion role.
- **Conclusion**: Established evidence supports PLEKHA7 as a junctional and polarity regulator. It may indicate an epithelial or barrier-related component of the module, but the blood-cell and cross-cell-type HPA signals mean that a purely epithelial interpretation is not secure.

#### CYTH1

- **Related proteins** (co-abundance neighbors): PLEKHA7 (0.87), USP25 (0.82), FCHO2 (0.82), DIP2B (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytohesin 1. The protein encoded by this gene is a member of the PSCD family. Members of this family have identical structural organization that consists of an N-terminal coiled-coil motif, a central Sec7 domain, and a C-terminal pleckstrin homology (PH) domain. The coiled-coil motif is involved in homodimerization, the Sec7 domain contains guanine-nucleotide exchange protein activity, and the PH domain intera…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.484); diabetes mellitus (0.437); smoking initiation (0.299); diabetic retinopathy (0.262); Alzheimer disease (0.254)
- **Europe PMC papers**: 248
- **Why important**: CYTH1 is a membrane-associated ARF guanine-nucleotide exchange factor with roles in vesicle-mediated transport, cell adhesion, ARF signaling, and epithelial polarity. It is connected to PLEKHA7 and to FCHO2, USP25, and DIP2B, making it the principal branch point for the module's trafficking-related genes. HPA reports enhancement in monocytes and neutrophils, consistent with a possible immune-cell contribution. Its established function and disease associations make it valuable for interpreting the module's membrane-trafficking component.
- **Conclusion**: Established evidence supports CYTH1 as a regulator of ARF-dependent membrane trafficking and adhesion-related processes. Its position supports a trafficking bridge within the module, while the HPA cell-type pattern leaves open whether this signal reflects epithelial biology, immune-cell admixture, or both.

#### ILK

- **Related proteins** (co-abundance neighbors): ADCY9 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin linked kinase. This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastas…
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); familial hypertrophic cardiomyopathy (0.194); Abnormality of the cardiovascular system (0.148); Prolonged QT interval (0.118); neoplasm (0.118)
- **Europe PMC papers**: 8401
- **Why important**: ILK is an integrin-linked signaling protein associated with focal adhesions, cell-matrix adhesion, cell morphogenesis, epithelial-to-mesenchymal transition, and tumor growth or metastasis. It is directly connected to ADCY9 in the module and provides a plausible extracellular-matrix and adhesion context for the signaling hub. HPA places it at focal adhesion sites and reports protein detection in both relevant tissues. Its substantial literature and disease associations strengthen its value as a mechanistic marker.
- **Conclusion**: Established evidence supports ILK as an integrin-associated regulator of adhesion and morphogenesis. Its co-abundance with ADCY9 is compatible with coordinated membrane and adhesion signaling, but it does not prove that ILK mediates the module or that the module is cancer-specific.

## Module 9

**Tissue pair**: breast and cervix_uterine  
**Genes (5)**: ARHGEF10L, C5, NCF2, MPO, ARHGAP27

### Function

The module is most consistent with an innate-immune and myeloid-associated co-abundance program, combining complement biology through C5, neutrophil antimicrobial oxidative defense through MPO and NCF2, and Rho-family signalling and cytoskeletal regulation through ARHGAP27 and ARHGEF10L. MPO is a neutrophil azurophilic-granule enzyme that produces microbicidal hypohalous acids, while NCF2 is a component of the neutrophil NADPH oxidase and supports respiratory burst. C5 is a circulating complement component involved in complement activation, chemotaxis, inflammation, and host defense. ARHGAP27 and ARHGEF10L provide a plausible signalling and cytoskeletal component through regulation of small GTPases, actin organization, endocytosis, and stress-fiber assembly. No GO or KEGG term passed global correction, so these annotations support biological interpretation but do not constitute globally significant enrichment. The module is therefore best interpreted as a biologically coherent but heterogeneous immune-associated signal rather than as a formally enriched pathway.

**Cell composition.** The composition strongly suggests contribution from blood or shared immune-cell content rather than a breast- or cervix_uterine-specific epithelial program. HPA assigns MPO to bone marrow and neutrophil progenitor biology, NCF2 to bone marrow, lung, lymphoid tissue, and neutrophils, and C5 to liver and hepatocytes with secretion to blood. ARHGEF10L has broad tissue specificity and is associated with several epithelial and myeloid cell populations, whereas ARHGAP27 has low immune specificity but is not detected in either target tissue by the reported immunohistochemistry. C5 is secreted to blood, and MPO is an intracellular and membrane-associated vesicular protein. Most module proteins are not detected in breast or cervix_uterine by the reported HPA immunohistochemistry, with ARHGEF10L being the clear exception. The HPA profile includes immune-cell enhancement or enrichment for most of the immune-linked genes, especially monocytes, myeloid dendritic cells, eosinophils, and neutrophils. Thus, the shared module may reflect circulating plasma proteins, infiltrating or contaminating myeloid cells, or a shared immune microenvironment in the two tissue groups.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no reported high-confidence STRING interactions among the module genes, and no supplementary STRING functional enrichment. Consequently, the co-abundance relationships should not be described as known direct protein interactions. hu.MAP supplies the main prior physical-context evidence: C5 and NCF2 co-occur in both (hu.MAP huMAP3_08224.1) and (hu.MAP huMAP3_09434.1). These complexes are broad assemblies containing complement, coagulation, plasma, inflammatory, and immune-related proteins, including APOL1, complement components, immunoglobulin-associated or plasma proteins, PTPRC, and other innate-immune factors. The repeated C5-NCF2 membership supports a connection between complement-associated extracellular biology and myeloid oxidative-defense biology, but the fact that only a minority of each large complex is represented means that the module is not a complete reconstruction of either complex. ARHGAP27, ARHGEF10L, and MPO have no reported hu.MAP or STRING partners within the supplied evidence. Overall, the network is a co-abundance module with limited support from known physical-interaction resources, not a validated molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08224.1 (C5, NCF2; 2/21); huMAP3_09434.1 (C5, NCF2; 2/33)

### Novelty

The shared breast and cervix_uterine co-abundance pattern may be a new observation, but the fact sheet does not establish that it is a new biological mechanism or a previously unknown interaction network. The lack of STRING interactions and the absence of most genes from the reported hu.MAP relationships do not prove novelty, because database coverage, tissue context, cell mixture, and detection thresholds can all limit those resources. Several component functions are well established, especially the roles of MPO, NCF2, and C5 in innate immunity and the roles of ARHGAP27 and ARHGEF10L in Rho-family signalling. The defensible novelty claim is therefore limited: this particular cross-tissue co-abundance combination and its possible relationship to shared immune or blood-derived content warrant validation, but it should not be called a new pathway or new protein interaction system without independent replication and tissue-resolved testing.

**Hypothesis.** Hypothesis: the module reflects a shared blood- or myeloid-associated inflammatory state present in both tissue groups. Circulating C5 and infiltrating or residual myeloid cells could provide complement and oxidative-defense signals, with MPO and NCF2 marking granulocyte-associated antimicrobial capacity. ARHGEF10L and ARHGAP27 could link the immune-cell state to Rho-dependent trafficking, adhesion, endocytosis, or cytoskeletal remodelling. A more tissue-intrinsic interpretation is possible but currently weaker, because HPA detection in the target tissues is sparse and the module contains liver-derived secreted C5 and strong bone-marrow or neutrophil markers. This hypothesis should be tested with cell deconvolution, matched blood measurements, spatial or single-cell data, and independent cohorts.

### Important genes

#### MPO

- **Related proteins** (co-abundance neighbors): ARHGAP27 (0.90), NCF2 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myeloperoxidase. Myeloperoxidase (MPO) is a heme protein synthesized during myeloid differentiation that constitutes the major component of neutrophil azurophilic granules. Produced as a single chain precursor, myeloperoxidase is subsequently cleaved into a light and heavy chain. The mature myeloperoxidase is a tetramer composed of 2 light chains and 2 heavy chains. This enzyme produces hypohalous acids central to…
- **Diseases (Open Targets)**: myeloperoxidase deficiency (0.767); Alzheimer disease type 1 (0.485); multiple system atrophy (0.286); amyotrophic lateral sclerosis (0.242); Alzheimer disease (0.146)
- **Europe PMC papers**: 36383
- **Why important**: MPO is a central functional marker of the module's myeloid and antimicrobial interpretation. Its network position connects ARHGAP27 with NCF2, and its HPA profile points to bone marrow and neutrophil progenitors with immune enhancement in classical monocytes. Its established enzyme function in azurophilic granules and its very extensive literature make it the strongest marker of granulocyte-associated oxidative defense in this module. It is also linked to MPO deficiency and several inflammatory or neurodegenerative disease contexts in the supplied evidence.
- **Conclusion**: Established evidence supports MPO as a neutrophil or myeloid antimicrobial marker and as an important reason to consider blood or immune-cell composition. It is not established that MPO drives the cross-tissue co-abundance pattern; that causal interpretation remains a hypothesis.

#### NCF2

- **Related proteins** (co-abundance neighbors): MPO (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08224.1, huMAP3_09434.1
- **Function (MyGene.info)**: neutrophil cytosolic factor 2. This gene encodes neutrophil cytosolic factor 2, the 67-kilodalton cytosolic subunit of the multi-protein NADPH oxidase complex found in neutrophils. This oxidase produces a burst of superoxide which is delivered to the lumen of the neutrophil phagosome. Mutations in this gene, as well as in other NADPH oxidase subunits, can result in chronic granulomatous disease, a disease that causes recurrent …
- **Diseases (Open Targets)**: chronic granulomatous disease (0.734); systemic lupus erythematosus (0.548); celiac disease (0.525); rheumatoid arthritis (0.442); autoimmune disorder of musculoskeletal system (0.434)
- **Europe PMC papers**: 2695
- **Why important**: NCF2 is the most direct indicator of NADPH-oxidase-dependent respiratory burst in the module. It is connected to MPO in the co-abundance graph and is a member with C5 of both hu.MAP contexts (hu.MAP huMAP3_08224.1) and (hu.MAP huMAP3_09434.1). HPA associates it with bone marrow, lung, lymphoid tissue, neutrophils, and eosinophils. Its established role in superoxide generation, phagocytosis, and cellular defense, together with its association with chronic granulomatous disease, gives it strong mechanistic and disease relevance.
- **Conclusion**: Established evidence supports NCF2 as a myeloid oxidative-defense component and as a plausible bridge between the MPO signal and the hu.MAP context. The module does not establish that NCF2 physically interacts with MPO in these tissues, because STRING reports no qualifying interaction.

#### C5

- **Related proteins** (co-abundance neighbors): ARHGEF10L (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08224.1, huMAP3_09434.1
- **Function (MyGene.info)**: complement C5. This gene encodes a component of the complement system, a part of the innate immune system that plays an important role in inflammation, host homeostasis, and host defense against pathogens. The encoded preproprotein is proteolytically processed to generate multiple protein products, including the C5 alpha chain, C5 beta chain, C5a anaphylatoxin and C5b. The C5 protein is comprised of the C5 alpha…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.744); paroxysmal nocturnal hemoglobinuria (0.610); myasthenia gravis (0.586); atypical hemolytic-uremic syndrome (0.544); neuromyelitis optica (0.516)
- **Europe PMC papers**: 81450
- **Why important**: C5 is the module's principal complement and circulating-protein representative. It is connected to ARHGEF10L and shares membership with NCF2 in both (hu.MAP huMAP3_08224.1) and (hu.MAP huMAP3_09434.1). HPA identifies it as liver and hepatocyte associated and secreted to blood, while the supplied functional annotation supports complement activation, chemotaxis, inflammation, and host defense. Its extensive literature and associations with complement deficiency, paroxysmal nocturnal hemoglobinuria, myasthenia gravis, atypical hemolytic-uremic syndrome, and neuromyelitis optica make it highly informative for interpreting systemic rather than tissue-restricted biology.
- **Conclusion**: Established evidence supports C5 as a blood-borne complement signal that may accompany immune-cell content. Its co-abundance with NCF2 does not by itself demonstrate complement-driven activation of the myeloid cells in either tissue.

#### ARHGEF10L

- **Related proteins** (co-abundance neighbors): ARHGAP27 (0.87), C5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Golgi apparatus, Vesicles, Cytosol; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho guanine nucleotide exchange factor 10 like. This gene belongs to the RhoGEF subfamily of RhoGTPases. Members of this subfamily are activated by specific guanine nucleotide exchange factors (GEFs) and are involved in signal transduction. The encoded protein shows cytosolic distribution. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2016].
- **Diseases (Open Targets)**: neurodegenerative disease (0.392); alcohol drinking (0.282); urolithiasis (0.282); Alzheimer disease (0.276); Rare genetic intellectual disability with developmental anomaly (0.266)
- **Europe PMC papers**: 245
- **Why important**: ARHGEF10L is the most plausible signalling connector in the module: it links ARHGAP27 to C5 and is the only gene reported as detected by immunohistochemistry in both target tissues. Its HPA profile is broad, with epithelial and myeloid cell associations, and its supplied annotations implicate Rho-family signalling, actin organization, and stress-fiber assembly. Although its literature volume is much smaller than that of C5 or MPO, its position at the interface between a Rho regulator and complement-associated C5 makes it important for generating a mechanistic hypothesis.
- **Conclusion**: Established evidence supports ARHGEF10L as a Rho-family signalling protein with broad cellular distribution and as the graph connection between ARHGAP27 and C5. A functional link between ARHGEF10L and complement or myeloid oxidative defense is a hypothesis, not a demonstrated finding.

#### ARHGAP27

- **Related proteins** (co-abundance neighbors): MPO (0.90), ARHGEF10L (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho GTPase activating protein 27. This gene encodes a member of a large family of proteins that activate Rho-type guanosine triphosphate (GTP) metabolizing enzymes. The encoded protein may pay a role in clathrin-mediated endocytosis. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Aug 2013].
- **Diseases (Open Targets)**: neurodegenerative disease (0.536); hypotensive disorder (0.329); systemic lupus erythematosus (0.187); ovarian carcinoma (0.175); refractive error (0.173)
- **Europe PMC papers**: 349
- **Why important**: ARHGAP27 represents the opposing Rho-regulatory side of the signalling component and has the strongest reported weighted connectivity in the module. It connects MPO with ARHGEF10L and is annotated for Rho signalling, small-GTPase regulation, receptor-mediated endocytosis, and signal transduction. Its HPA profile shows low immune specificity, no reported detection in the two target tissues, and no STRING or hu.MAP partner in the supplied evidence. Its moderate literature volume and disease associations make it useful as a regulatory candidate, while also arguing for caution.
- **Conclusion**: Established evidence supports ARHGAP27 as a Rho-family regulatory protein and a network connector. Its apparent association with MPO and ARHGEF10L may reflect coordinated cell-state or trafficking biology, but the module does not establish a direct molecular pathway or tissue-specific role.

## Module 10

**Tissue pair**: breast and cervix_uterine  
**Genes (11)**: CA2, ECHS1, GALNT7, KRT10, KRT2, MMP8, MUC5AC, MUC5B, S100A13, SBSN, ATP6V1A

### Function

The module is most consistent with a mucosal and epithelial-surface program that combines gel-forming mucus, mucin-type glycosylation, epithelial differentiation, vesicular trafficking, and extracellular-matrix remodeling. The strongest functional coherence comes from MUC5AC, MUC5B, and GALNT7: the mucins are gel-forming secreted components, while GALNT7 initiates mucin-type O-linked glycosylation. KRT2 and KRT10 support an epithelial cornification and intermediate-filament component, and MMP8 supports extracellular-matrix proteolysis. SBSN is the principal network hub and connects the mucin, keratin, glycosylation, carbonic-anhydrase, and vesicular-acidification branches. No GO or KEGG term passed global correction, so the proposed function is an integrated interpretation of the gene annotations and network rather than a globally significant pathway-enrichment claim. The STRING mucin-glycosylation results (STRING RCTM O-linked glycosylation of mucins; within-query FDR = 0.0454) and (STRING NetworkNeighborAL O-linked glycosylation of mucins; within-query FDR = 0.0492) are supplementary and were not corrected across modules.

**Cell composition.** The module is compositionally heterogeneous rather than a uniform intracellular housekeeping module. It contains several secreted or vesicle-associated proteins, including MUC5AC, MUC5B, MMP8, SBSN, and S100A13, together with the Golgi enzyme GALNT7 and epithelial structural proteins KRT2 and KRT10. HPA data point to epithelial and mucosal cell states, especially esophageal apical cells, foveolar or goblet-like cells, suprabasal keratinocytes, and endometrial secretory cells. HPA also shows immune-cell enhancement for several genes, particularly neutrophil and monocyte-associated signals, with MMP8 being especially compatible with a neutrophil contribution. The recurrence of stomach, skin, and mucosal expression patterns, together with the presence of secreted proteins, means that the shared breast and cervix_uterine signal could reflect epithelial or mucosal cell composition, secretory material, or low-level inflammatory admixture rather than a pathway active uniformly in every cell. The breast and cervix protein-detection pattern is mixed, and several genes are detected in cervix but not breast, so transcript co-abundance should not be interpreted as uniform protein abundance in both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides two high-confidence physical or functional relationships within the module: MUC5AC with MUC5B, and KRT10 with KRT2. The mucin pair is directly concordant with the supplementary STRING mucin O-glycosylation terms (STRING RCTM O-linked glycosylation of mucins; within-query FDR = 0.0454) and (STRING NetworkNeighborAL O-linked glycosylation of mucins; within-query FDR = 0.0492), while the keratin pair supports a structural epithelial branch. SBSN has no listed STRING partner despite being the network hub, and the remaining module relationships are not represented as high-confidence STRING edges. hu.MAP independently places MUC5AC and MUC5B together in three complexes (hu.MAP huMAP3_06906.1), (hu.MAP huMAP3_08525.1), and (hu.MAP huMAP3_11343.1). Those complexes also contain secretory, mucosal, antimicrobial, epithelial, and immune-associated proteins such as JCHAIN, PIGR, LTF, LYZ, BPIFB proteins, and DMBT1. Thus, the mucin core has independent complex-level support, but the broader co-abundance module is not equivalent to a single established protein complex. The limited overlap between the module and known complexes suggests a mixture of established mucin biology and tissue-contextual co-regulation.

**STRING interactions (score >= 0.7)**: 2 of 55 gene pairs: KRT10–KRT2 (0.904); MUC5AC–MUC5B (0.988)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM O-linked glycosylation of mucins (FDR = 0.0454, 3 genes); NetworkNeighborAL O-linked glycosylation of mucins (FDR = 0.0492, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06906.1 (MUC5AC, MUC5B; 2/9); huMAP3_08525.1 (MUC5AC, MUC5B; 2/12); huMAP3_11343.1 (MUC5AC, MUC5B; 2/54)

### Novelty

This cannot be established as a wholly new molecular pathway from the available evidence. The MUC5AC-MUC5B relationship is already supported by STRING and hu.MAP, and the KRT2-KRT10 relationship is already supported by STRING. The mucin-glycosylation interpretation is also represented by supplementary STRING evidence. Conversely, SBSN's central position and its connections to mucins, keratins, GALNT7, CA2, and ATP6V1A are not supported by listed STRING partners or hu.MAP complexes, so the tissue-pair co-abundance organization may represent a novel contextual association. However, absence from these resources does not prove novelty: it may reflect incomplete interaction coverage, tissue specificity, correlated expression without physical binding, or mixed-cell effects. The most defensible conclusion is that this is a potentially novel breast-cervix_uterine co-abundance module built partly from well-established secretory and epithelial relationships, not a demonstrated new complex or globally enriched pathway.

**Hypothesis.** Hypothesis: a shared epithelial or mucosal cell-state program in breast and cervix_uterine coordinately increases mucin production, mucin O-linked glycosylation, epithelial barrier differentiation, vesicular processing, and surface remodeling. In this model, GALNT7 modifies mucin-type substrates, MUC5AC and MUC5B form the secreted gel-like material, and SBSN organizes or reports the broader epithelial secretory state through co-abundance with keratins, CA2, and ATP6V1A. A concurrent neutrophil or inflammatory component could contribute MMP8 and S100A13, linking extracellular-matrix turnover and cytokine-related activity to the epithelial mucus program. This is a testable hypothesis, not a demonstrated causal mechanism: it should be evaluated with cell-resolved expression, protein localization, and perturbation of mucin glycosylation or epithelial differentiation.

### Important genes

#### SBSN

- **Related proteins** (co-abundance neighbors): GALNT7 (0.88), MUC5B (0.86), MUC5AC (0.86), KRT2 (0.86), CA2 (0.81), KRT10 (0.81), ATP6V1A (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Vesicles; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: suprabasin. Located in extracellular exosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: esophageal squamous cell carcinoma (0.086); myelodysplastic syndrome (0.076); congenital non-bullous ichthyosiform erythroderma (0.056); erythrokeratodermia variabilis (0.055); lamellar ichthyosis (0.055)
- **Europe PMC papers**: 468
- **Why important**: SBSN is the central network hub, connecting the mucins, GALNT7, both keratins, CA2, and ATP6V1A. HPA places it in cervix, esophagus, skin, and vagina-associated expression states and in esophageal apical cells, with vesicular and secreted-unknown-location annotations. It has no listed STRING partners or hu.MAP complex membership, making its hub position particularly informative for the module's tissue-contextual organization. Its literature volume is more limited than that of the mucins or MMP8, which increases its value as a candidate for follow-up.
- **Conclusion**: Established evidence supports SBSN as the co-abundance hub of an epithelial or mucosal module and as a vesicle-associated or secreted protein. It is not established that SBSN physically binds the neighboring proteins or drives the module; that role remains a hypothesis.

#### MUC5AC

- **Related proteins** (co-abundance neighbors): SBSN (0.86); STRING partners: MUC5B (0.988)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Vesicles; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_06906.1, huMAP3_08525.1, huMAP3_11343.1
- **Function (MyGene.info)**: mucin 5AC, oligomeric mucus/gel-forming. Predicted to be an extracellular matrix structural constituent. Involved in phosphatidylinositol-mediated signaling. Located in cytoplasm; extracellular space; and mucus layer. Implicated in dry eye syndrome. Biomarker of several diseases, including Sjogren's syndrome; biliary tract disease (multiple); cystic fibrosis; eye disease (multiple); and pancreatic cancer (multiple). [provided by Alliance…
- **Diseases (Open Targets)**: idiopathic pulmonary fibrosis (0.512); pneumonia (0.384); asthma (0.380); respiratory system disorder (0.366); gastric ulcer (0.357)
- **Europe PMC papers**: 14230
- **Why important**: MUC5AC is a gel-forming mucin with strong secretory and mucosal relevance, including foveolar and conjunctival goblet-cell associations. It is linked to MUC5B by STRING and occurs with MUC5B in all listed hu.MAP complexes (hu.MAP huMAP3_06906.1), (hu.MAP huMAP3_08525.1), and (hu.MAP huMAP3_11343.1). It also contributes to both supplementary mucin O-glycosylation terms (STRING RCTM O-linked glycosylation of mucins; within-query FDR = 0.0454) and (STRING NetworkNeighborAL O-linked glycosylation of mucins; within-query FDR = 0.0492). Its literature volume is extensive, and its disease associations include respiratory, ocular, gastrointestinal, and pancreatic conditions.
- **Conclusion**: Established evidence supports MUC5AC as a central secreted mucin component of the module and as part of a known mucin-associated complex. The module does not establish that MUC5AC is the causal driver of the shared tissue signal or that its protein abundance is uniform across the tissues.

#### MUC5B

- **Related proteins** (co-abundance neighbors): MMP8 (0.92), SBSN (0.86); STRING partners: MUC5AC (0.988)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Vesicles; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_06906.1, huMAP3_08525.1, huMAP3_11343.1
- **Function (MyGene.info)**: mucin 5B, oligomeric mucus/gel-forming. This gene encodes a member of the mucin family of proteins, which are highly glycosylated macromolecular components of mucus secretions. This family member is the major gel-forming mucin in mucus. It is a major contributor to the lubricating and viscoelastic properties of whole saliva, normal lung mucus and cervical mucus. This gene has been found to be up-regulated in some human diseases, includi…
- **Diseases (Open Targets)**: idiopathic pulmonary fibrosis (0.539); interstitial lung disease (0.495); respiratory system disorder (0.480); chronic lung disease (0.429); pulmonary fibrosis (0.428)
- **Europe PMC papers**: 5979
- **Why important**: MUC5B is a major gel-forming mucin contributing to the viscoelastic properties of saliva, lung mucus, and cervical mucus. It connects to MMP8 and SBSN in the co-abundance network, has a high-confidence STRING relationship with MUC5AC, and participates with MUC5AC in the hu.MAP complexes (hu.MAP huMAP3_06906.1), (hu.MAP huMAP3_08525.1), and (hu.MAP huMAP3_11343.1). Its HPA profile includes salivary gland and secretory-cell states, including endometrial secretory and submucosal glandular cells. It has extensive literature and disease associations involving pulmonary and mucosal disorders.
- **Conclusion**: Established evidence supports MUC5B as a biologically plausible secretory-mucus anchor and as part of a known mucin pair and complex. Its connection to MMP8 in this module may reflect mucus-associated remodeling or inflammatory admixture, but causality is not established.

#### GALNT7

- **Related proteins** (co-abundance neighbors): SBSN (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypeptide N-acetylgalactosaminyltransferase 7. This gene encodes GalNAc transferase 7, a member of the GalNAc-transferase family. The enzyme encoded by this gene controls the initiation step of mucin-type O-linked protein glycosylation and transfer of N-acetylgalactosamine to serine and threonine amino acid residues. This enzyme is a type II transmembrane protein and shares common sequence motifs with other family members. Unlike other family …
- **Diseases (Open Targets)**: immune system disorder (0.291); color vision disorder (0.254); Hydrocephalus (0.252); Parkinson disease (0.228); alcohol drinking (0.209)
- **Europe PMC papers**: 758
- **Why important**: GALNT7 supplies the clearest enzymatic link to the mucin branch: it initiates mucin-type O-linked glycosylation and is connected to SBSN in the module. It appears in both supplementary STRING O-glycosylation terms (STRING RCTM O-linked glycosylation of mucins; within-query FDR = 0.0454) and (STRING NetworkNeighborAL O-linked glycosylation of mucins; within-query FDR = 0.0492), and HPA detects it in both breast and cervix_uterine. Its literature volume is more limited than that of MUC5AC, MUC5B, or MMP8, making it a useful mechanistic candidate rather than merely a highly studied marker.
- **Conclusion**: Established evidence supports GALNT7 as a mucin-glycosylation enzyme associated with this module. It is reasonable to hypothesize that its activity influences the properties of the co-abundant mucin program, but the module does not demonstrate substrate specificity, enzymatic activity, or causal control in either tissue.

#### MMP8

- **Related proteins** (co-abundance neighbors): MUC5B (0.92), S100A13 (0.86), ECHS1 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: matrix metallopeptidase 8. This gene encodes a member of the matrix metalloproteinase (MMP) family of proteins. These proteins are involved in the breakdown of extracellular matrix in embryonic development, reproduction, and tissue remodeling, as well as in disease processes, such as arthritis and metastasis. Proteolysis at different sites on this protein results in multiple active forms of the enzyme with distinct N-termin…
- **Diseases (Open Targets)**: acne (0.603); periodontitis (0.582); rosacea (0.576); infection (0.552); spotted fever (0.491)
- **Europe PMC papers**: 8323
- **Why important**: MMP8 links the module to extracellular-matrix turnover and is connected to MUC5B, S100A13, and ECHS1. HPA places it in bone marrow, neutrophil progenitors, neutrophils, and an immune-enhanced monocyte state, while its protein is not detected in the sampled breast or cervix_uterine tissues. Its established collagen-degrading and matrix-remodeling functions, disease associations, and extensive literature make it important for distinguishing a local epithelial program from inflammatory or blood-cell admixture.
- **Conclusion**: Established evidence supports MMP8 as a neutrophil-associated extracellular-matrix protease and as a possible inflammatory branch of the module. Its co-abundance with MUC5B may indicate coordinated mucosal remodeling or sample-composition effects; direct participation in a shared tissue mechanism remains unproven.

## Module 11

**Tissue pair**: breast and cervix_uterine  
**Genes (19)**: CTSH, DHRS1, GPD2, HMOX1, ITIH2, KRT14, KRT16, KRT5, KRT6A, KRT75, KRT80, MGLL, PPL, RAB27A, S100A12, CCT3, CCT8, TPRG1, UTS2

### Function

The module is most strongly an epithelial intermediate-filament and cornified-envelope program. The globally corrected enrichment supports intermediate-filament processes and organization (GO:BP intermediate filament-based process; q_global = 7.15e-05) (GO:BP intermediate filament cytoskeleton organization; q_global = 7.15e-05) (GO:BP intermediate filament organization; q_global = 0.00055), keratinization (GO:BP keratinization; q_global = 0.000189), intermediate-filament and keratin-filament structures (GO:CC intermediate filament; q_global = 0.000199) (GO:CC keratin filament; q_global = 0.00024) (GO:CC intermediate filament cytoskeleton; q_global = 0.000598), keratinocyte and epidermal differentiation (GO:BP keratinocyte differentiation; q_global = 0.000679) (GO:BP epidermal cell differentiation; q_global = 0.0018), skin and epidermis development (GO:BP skin development; q_global = 0.00794) (GO:BP epidermis development; q_global = 0.0106), and structural roles in the epidermis and cytoskeleton (GO:MF structural constituent of skin epidermis; q_global = 0.0282) (GO:MF structural constituent of cytoskeleton; q_global = 0.042) (GO:MF structural molecule activity; q_global = 0.0435). Cornified-envelope formation is also supported by the globally corrected KEGG term (KEGG Cornified envelope formation - Homo sapiens (human); q_global = 0.000223). The module therefore most plausibly reflects the abundance and differentiation state of stratified epithelial cells, rather than a general housekeeping program. CCT3 and CCT8 add a protein-folding or chaperone-related component, while HMOX1, S100A12, CTSH, and other peripheral genes may reflect stress, myeloid, or tissue-mixture signals rather than the core module function. The STRING supplementary results independently agree with the keratin and intermediate-filament interpretation (14 supplementary STRING terms; within-query FDR 9.39e-05–0.0012), but they are supplementary rather than global enrichment evidence.

**Cell composition.** The module is dominated by epithelial and keratin-associated genes, with HPA enrichment in esophagus, skin, cervix, and vagina and single-cell enrichment in esophageal apical cells, basal keratinocytes, and suprabasal keratinocytes. This supports a shared stratified epithelial or squamous-cell signal in breast and cervix_uterine. The module is not predominantly composed of secreted or plasma proteins, although ITIH2, S100A12, and UTS2 are secreted to blood and may introduce extracellular or blood-derived signal. HPA also shows enrichment for monocyte and neutrophil populations for several genes, especially S100A12 and GPD2, while some genes have low immune-cell specificity. Thus, blood contamination or shared myeloid content is a plausible secondary influence, but it does not explain the coherent keratin core. Protein detection is broader in cervix_uterine than breast, and several keratin genes are detected in both tissues or are tissue-enhanced in cervix, consistent with a conserved epithelial component rather than uniform expression across all cells.

**GO/KEGG enrichment**: 18 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP intermediate filament-based process | 7.15e-05 | KRT14, KRT16, KRT5, KRT6A, KRT75, KRT80, PPL |
| GO:BP intermediate filament cytoskeleton organization | 7.15e-05 | KRT14, KRT16, KRT5, KRT6A, KRT75, KRT80, PPL |
| GO:BP keratinization | 0.000189 | KRT16, KRT5, KRT6A, KRT75, KRT80, PPL |
| GO:CC intermediate filament | 0.000199 | KRT14, KRT16, KRT5, KRT6A, KRT75, KRT80, PPL |
| KEGG Cornified envelope formation - Homo sapiens (human) | 0.000223 | KRT14, KRT16, KRT5, KRT6A, KRT75, KRT80, PPL, S100A12 |
| GO:CC keratin filament | 0.00024 | KRT14, KRT16, KRT5, KRT6A, KRT75, KRT80 |
| GO:BP intermediate filament organization | 0.00055 | KRT14, KRT16, KRT5, KRT6A, KRT75, KRT80 |
| GO:CC intermediate filament cytoskeleton | 0.000598 | KRT14, KRT16, KRT5, KRT6A, KRT75, KRT80, PPL |
| GO:BP keratinocyte differentiation | 0.000679 | KRT14, KRT16, KRT5, KRT6A, KRT75, KRT80, PPL |
| GO:BP epidermal cell differentiation | 0.0018 | KRT14, KRT16, KRT5, KRT6A, KRT75, KRT80, PPL |
| GO:CC polymeric cytoskeletal fiber | 0.00723 | CCT3, CCT8, KRT14, KRT16, KRT5, KRT6A, KRT75, KRT80, PPL |
| GO:BP skin development | 0.00794 | KRT14, KRT16, KRT5, KRT6A, KRT75, KRT80, PPL |
| GO:BP epidermis development | 0.0106 | KRT14, KRT16, KRT5, KRT6A, KRT75, KRT80, PPL |
| GO:MF structural constituent of skin epidermis | 0.0282 | KRT5, KRT6A, KRT75, KRT80 |
| GO:CC supramolecular polymer | 0.0321 | CCT3, CCT8, KRT14, KRT16, KRT5, KRT6A, KRT75, KRT80, PPL |

### STRING and hu.MAP

STRING contains strong known relationships among the keratin core, particularly KRT5 with KRT14, KRT16, and KRT6A, together with additional links among KRT14, KRT16, and KRT6A. CCT3 and CCT8 also have a strong known relationship. These interactions show that part of the co-abundance structure recapitulates established keratin-filament and chaperonin biology, strengthening the interpretation that the module contains a real epithelial structural core. STRING does not report partners for many peripheral genes, so the full module is not equivalent to one experimentally established protein complex. hu.MAP supports known or plausible complexes involving KRT14 and KRT16, CCT3 and CCT8, and combinations involving PPL, HMOX1, ITIH2, CTSH, and other proteins. However, most hu.MAP complexes contain only a subset of module genes and often include many proteins outside the module. The network should therefore be interpreted as a co-abundance module that overlaps several known complexes, not as a single physical complex.

**STRING interactions (score >= 0.7)**: 7 of 171 gene pairs: CCT3–CCT8 (0.999); KRT14–KRT16 (0.868); KRT14–KRT5 (0.999); KRT14–KRT6A (0.732); KRT16–KRT5 (0.861); KRT16–KRT6A (0.928); KRT5–KRT6A (0.915)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Intermediate filament (FDR = 9.39e-05, 6 genes); Keyword Keratin (FDR = 9.39e-05, 6 genes); SMART Intermediate filament protein (FDR = 0.00011, 6 genes); COMPARTMENTS Intermediate filament cytoskeleton (FDR = 0.00016, 7 genes); Process Intermediate filament cytoskeleton organization (FDR = 0.00018, 7 genes); RCTM Formation of the cornified envelope (FDR = 0.00021, 7 genes); COMPARTMENTS Intermediate filament (FDR = 0.00027, 6 genes); Component Intermediate filament cytoskeleton (FDR = 0.00031, 7 genes); Process Keratinization (FDR = 0.00035, 6 genes); InterPro Intermediate filament, rod domain (FDR = 0.00055, 6 genes); Process Intermediate filament organization (FDR = 0.00059, 6 genes); Component Intermediate filament (FDR = 0.00069, 6 genes); COMPARTMENTS Polymeric cytoskeletal fiber (FDR = 0.0007, 8 genes); Component Keratin filament (FDR = 0.0012, 5 genes); NetworkNeighborAL Pachyonychia congenita, and Epidermolysis bullosa simplex Dowling-Meara type (FDR = 0.0014, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10678.1 (PPL, HMOX1, ITIH2; 3/71); huMAP3_14922.1 (KRT14, KRT16; 2/7); huMAP3_15329.1 (KRT14, KRT16; 2/8); huMAP3_06323.1 (PPL, HMOX1; 2/15); huMAP3_09833.1 (PPL, HMOX1; 2/16); huMAP3_07938.1 (CCT3, CCT8; 2/23); huMAP3_06559.1 (CCT3, CCT8; 2/25); huMAP3_09191.1 (CCT3, CCT8; 2/32); huMAP3_10656.1 (CCT3, CCT8; 2/36); huMAP3_14584.1 (CCT3, CCT8; 2/61); huMAP3_09929.1 (PPL, CTSH; 2/75)

### Novelty

The broad biological theme is not new: keratin intermediate filaments, epithelial differentiation, cornified-envelope biology, and the KRT5-KRT14 axis are established. The module-level finding may nevertheless be novel because it identifies a conserved breast and cervix_uterine co-abundance pattern that combines a known keratin structural core with a TPRG1-centered set of genes, stress-associated proteins, chaperonins, and possible blood-related signals. Its novelty is therefore best stated as a tissue-pair-specific network configuration or conserved co-abundance signature, not as discovery of a new keratin function or new protein complex. The limited STRING support outside the keratin core and the partial overlap with hu.MAP are compatible with a new network context, but absence from either resource alone cannot establish novelty. Independent validation in additional cohorts, with epithelial and immune-cell composition controlled, would be required.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of stratified epithelial cells undergoing basal-to-suprabasal differentiation and reinforcement of the intermediate-filament and cornified-envelope architecture. KRT5, KRT14, KRT16, and KRT6A may form the structural backbone, with PPL linking intermediate filaments to desmosomes and the cornified envelope. TPRG1 may organize or report a broader epithelial state because it is the most connected node in the module, although its molecular role here is not established by the supplied evidence. CCT3 and CCT8 may support folding of abundant structural proteins. The co-occurrence of S100A12, HMOX1, CTSH, ITIH2, and other peripheral genes may represent epithelial stress, wound or inflammatory context, or variable myeloid and plasma contribution. This is a mechanistic model, not a demonstrated causal pathway.

### Important genes

#### KRT5

- **Related proteins** (co-abundance neighbors): KRT14 (0.89), KRT6A (0.85), KRT16 (0.84), KRT75 (0.81); STRING partners: KRT14 (0.999), KRT16 (0.861), KRT6A (0.915)
- **HPA**: Group enriched; Group enriched; blood Immune cell enriched; location Intermediate filaments; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 5. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the basal layer of the epidermis with family member KRT14. Mutations in t…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 2C, localized (0.768); epidermolysis bullosa simplex 2A, generalized severe (0.761); epidermolysis bullosa simplex 2B, generalized intermediate (0.761); epidermolysis bullosa simplex 2F, with mottled pigmentation (0.729); Dowling-Degos disease 1 (0.697)
- **Europe PMC papers**: 7044
- **Why important**: KRT5 is a central member of the keratin subnetwork and is connected to KRT14, KRT16, KRT6A, and KRT75. It appears in every globally corrected enrichment term (18 globally significant GO/KEGG terms, q_global 7.15e-05–0.0435; see the table) and in all listed STRING supplementary terms (15 supplementary STRING terms; within-query FDR 9.39e-05–0.0014). HPA places it in basal and suprabasal keratinocyte populations and detects it in both tissues. Its established role is as a basal epithelial type two keratin that pairs with KRT14 and supports epithelial structural integrity. Its disease associations include several forms of epidermolysis bullosa simplex, and its literature support is extensive.
- **Conclusion**: Established evidence identifies KRT5 as a core structural and differentiation marker of the module and a biologically important epithelial anchor. The module data do not establish that KRT5 drives the breast or cervix_uterine co-abundance pattern; its centrality may primarily reflect coordinated abundance of the relevant epithelial cell population.

#### KRT14

- **Related proteins** (co-abundance neighbors): KRT5 (0.89), KRT16 (0.82), KRT6A (0.81); STRING partners: KRT16 (0.868), KRT5 (0.999), KRT6A (0.732)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Intermediate filaments; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: huMAP3_14922.1, huMAP3_15329.1
- **Function (MyGene.info)**: keratin 14. This gene encodes a member of the keratin family, the most diverse group of intermediate filaments. This gene product, a type I keratin, is usually found as a heterotetramer with two keratin 5 molecules, a type II keratin. Together they form the cytoskeleton of epithelial cells. Mutations in the genes for these keratins are associated with epidermolysis bullosa simplex. At least one pseudogene has…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 1A, generalized severe (0.823); epidermolysis bullosa simplex 1C, localized (0.818); epidermolysis bullosa simplex 1B, generalized intermediate (0.802); epidermolysis bullosa simplex 1D, generalized, intermediate or severe, autosomal recessive (0.759); Naegeli-Franceschetti-Jadassohn syndrome (0.759)
- **Europe PMC papers**: 6348
- **Why important**: KRT14 is tightly connected to the KRT5, KRT16, and KRT6A core and is represented across nearly all globally corrected epithelial terms (16 globally significant GO/KEGG terms, q_global 7.15e-05–0.0435; see the table). It is detected in both tissues and is enriched in basal keratinocyte-related populations. Its established function is to heteropolymerize with KRT5 in epithelial intermediate filaments, and its disease associations include epidermolysis bullosa simplex and Naegeli-Franceschetti-Jadassohn syndrome. It is also represented in hu.MAP keratin complexes (hu.MAP huMAP3_14922.1) (hu.MAP huMAP3_15329.1).
- **Conclusion**: KRT14 is strong evidence that the module contains a basal epithelial intermediate-filament program. The data support its role as a structural marker and likely functional partner of KRT5, but do not demonstrate a module-specific pathogenic mechanism.

#### KRT6A

- **Related proteins** (co-abundance neighbors): KRT5 (0.85), TPRG1 (0.82), KRT14 (0.81); STRING partners: KRT14 (0.732), KRT16 (0.928), KRT5 (0.915)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Intermediate filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 6A. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. As many as six of this type II cytokeratin (KRT6) have been identified; the multiplicity of the genes is attributed to successi…
- **Diseases (Open Targets)**: pachyonychia congenita (0.825); pachyonychia congenita 1 (0.371); skin neoplasm (0.200); hereditary disease (0.194); skin cancer (0.167)
- **Europe PMC papers**: 2238
- **Why important**: KRT6A is part of the densely connected keratin core with KRT5, KRT14, and KRT16 and appears in all globally corrected enrichment terms (18 globally significant GO/KEGG terms, q_global 7.15e-05–0.0435; see the table). HPA associates it with cervix, esophagus, vagina, and suprabasal epithelial populations, with detection in cervix_uterine. Its established annotations include epithelial morphogenesis, differentiation, keratinization, and regulation of cell migration. It is associated with pachyonychia congenita and related keratin disorders, and it has known STRING relationships with the other core keratins (15 supplementary STRING terms; within-query FDR 9.39e-05–0.0014).
- **Conclusion**: KRT6A is an important marker of the activated or suprabasal epithelial component of the module and may distinguish it from a purely basal KRT5-KRT14 program. The co-abundance data support association with that epithelial state, but do not show that KRT6A controls the other module genes.

#### PPL

- **Related proteins** (co-abundance neighbors): TPRG1 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Plasma membrane, Basal body, Cytosol; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_06323.1, huMAP3_09833.1, huMAP3_09929.1
- **Function (MyGene.info)**: periplakin. The protein encoded by this gene is a component of desmosomes and of the epidermal cornified envelope in keratinocytes. The N-terminal domain of this protein interacts with the plasma membrane and its C-terminus interacts with intermediate filaments. Through its rod domain, this protein forms complexes with envoplakin. This protein may serve as a link between the cornified envelope and desmosomes …
- **Diseases (Open Targets)**: hypertensive disorder (0.495); prostate carcinoma (0.406); seborrheic keratosis (0.367); obesity disorder (0.334); brain cancer (0.332)
- **Europe PMC papers**: 9177
- **Why important**: PPL is connected to the high-connectivity TPRG1 node and contributes to the globally corrected intermediate-filament, keratinization, epidermal differentiation, skin-development, and structural terms (15 globally significant GO/KEGG terms, q_global 7.15e-05–0.0435; see the table). HPA shows enrichment in cervix, esophagus, and vagina and detection in both tissues. Its established function is to link plasma membrane, desmosomes, intermediate filaments, and the cornified envelope. It occurs in several hu.MAP complexes involving epithelial and envelope-associated proteins (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_06323.1) (hu.MAP huMAP3_09833.1) (hu.MAP huMAP3_09929.1).
- **Conclusion**: PPL provides a plausible physical bridge between the keratin filament core and epithelial junction or cornified-envelope organization. This bridging interpretation is biologically supported by its annotation and complex membership, whereas a direct coordinating role within this co-abundance module remains a hypothesis.

#### TPRG1

- **Related proteins** (co-abundance neighbors): DHRS1 (0.95), ITIH2 (0.89), CTSH (0.88), HMOX1 (0.88), PPL (0.87), RAB27A (0.85), UTS2 (0.84), KRT6A (0.82), MGLL (0.81), CCT8 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tumor protein p63 regulated 1. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: asthma (0.430); allergic rhinitis (0.376); respiratory system disorder (0.368); allergic disease (0.361); Crohn disease (0.361)
- **Europe PMC papers**: 318
- **Why important**: TPRG1 is the most connected node in the supplied module and links the keratin-associated genes with DHRS1, ITIH2, CTSH, HMOX1, PPL, RAB27A, and UTS2. HPA shows tissue enhancement in cervix, esophagus, and vagina and enrichment in esophageal apical cells. It has no reported STRING partners, no hu.MAP complex assignment, and no globally corrected GO or KEGG annotation in the fact sheet. Its supplied functional description identifies it as tumor protein p63 regulated one, and its literature volume is substantially smaller than that of the major keratins.
- **Conclusion**: TPRG1 is the most interesting candidate for a module-specific marker because of its network position and epithelial tissue pattern despite limited established molecular annotation. The evidence supports prioritizing it for validation, but does not establish that it is a scaffold, regulator, or driver; those roles remain hypotheses.

#### S100A12

- **Related proteins** (co-abundance neighbors): KRT80 (0.85), GPD2 (0.85), DHRS1 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: S100 calcium binding protein A12. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: tinea pedis (0.282); Alzheimer disease (0.181); Parkinson disease (0.176); neurodegenerative disease (0.174); lysosomal storage disease (0.172)
- **Europe PMC papers**: 6100
- **Why important**: S100A12 connects the module to KRT80, GPD2, and DHRS1 and is the only gene in the globally corrected cornified-envelope term that is not part of the main keratin set (KEGG Cornified envelope formation - Homo sapiens (human); q_global = 0.000223). HPA identifies it as secreted to blood and enriched in monocytes, neutrophils, and their progenitors, while it is not detected by immunohistochemistry in either tissue. Its established annotations include calcium binding, inflammatory response, monocyte chemotaxis, and neutrophil chemotaxis. It has a substantial literature base and disease associations involving inflammatory and neurodegenerative conditions.
- **Conclusion**: S100A12 is important primarily as a potential composition or inflammatory-context indicator rather than as evidence for the epithelial structural core. Its co-abundance with the keratin program could reflect epithelial injury or immune-cell contribution, and this distinction should be tested by cell-composition adjustment and independent tissue measurements.

## Module 12

**Tissue pair**: breast and cervix_uterine  
**Genes (5)**: LIG1, RNGTT, MOCOS, SLK, ZNF106

### Function

This is a heterogeneous intracellular co-abundance module rather than a module with a demonstrated single pathway. No GO or KEGG term passed global correction, so no pathway-level enrichment can be claimed from the primary analysis. The gene annotations suggest several compatible cellular themes: genome maintenance through LIG1, messenger-RNA capping through RNGTT, cytoskeletal and focal-adhesion regulation through SLK, molybdenum-cofactor-dependent metabolism through MOCOS, and RNA-associated nuclear functions through ZNF106. The co-abundance pattern may therefore reflect shared regulation, cell-state composition, or technical and biological covariance rather than a physical complex or one established biochemical process.

**Cell composition.** The module is not a plasma-protein or secreted-protein module: none of its genes is annotated as secreted. Its composition is mixed rather than uniformly tissue-specific. HPA reports tissue enhancement for LIG1 and MOCOS, group enrichment for ZNF106, and low tissue specificity for SLK and RNGTT. All genes have cell-type-enhanced annotations, but the implicated cell types are diverse, including erythrocyte progenitors, neutrophil-related cells, respiratory deuterosomal cells, adrenal cortex cells, endometrial glandular cells, and other epithelial or muscle-associated populations. Most genes have low immune-cell specificity or are not detected in immune cells, while ZNF106 is immune-cell enhanced for neutrophils. Thus, the shared breast and cervix_uterine signal could partly reflect shared cell-type composition or cellular state, but the HPA evidence does not support a simple blood-cell or secreted-protein explanation. Protein detection is broadly concordant between the two tissues for the genes with available HPA measurements, although MOCOS lacks tissue IHC detection in the supplied summary.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no qualifying STRING functional-enrichment result. There is also no hu.MAP complex containing multiple module members. Accordingly, the network edges should not be interpreted as established protein-protein interactions or as evidence for a known multiprotein complex. The relationships already supported in the supplied databases are therefore absent at the specified confidence and complex thresholds. The module is better regarded as a co-abundance association whose molecular coupling remains unresolved.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module is not established as a new biological mechanism. Its lack of STRING interactions and hu.MAP complexes makes the particular gene combination poorly represented in those resources, but database absence alone does not demonstrate novelty. The lack of globally significant GO or KEGG enrichment further limits claims of a newly defined pathway. A cautious conclusion is that the cross-tissue co-abundance pattern is a candidate observation that may be novel as a dataset-level association, but it requires independent replication, control for cell-type composition, and targeted molecular experiments before it can be called a novel biological module.

**Hypothesis.** Hypothesis: the module represents coordinated variation in a mixed intracellular program linking genome maintenance, RNA maturation, cytoskeletal signaling, and mitochondrial or redox-related metabolism across selected cell populations in breast and cervix_uterine. ZNF106 may act as the network-level connector in the observed co-abundance structure, while LIG1, RNGTT, SLK, and MOCOS contribute distinct cellular processes. An alternative hypothesis is that the apparent coordination is driven mainly by shared cellular composition or state rather than direct regulation among these proteins. This hypothesis is not supported by global pathway enrichment, STRING interactions, or hu.MAP complexes and therefore requires experimental testing.

### Important genes

#### ZNF106

- **Related proteins** (co-abundance neighbors): SLK (0.82), RNGTT (0.82), LIG1 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoli; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger protein 106. Enables RNA binding activity. Predicted to be involved in insulin receptor signaling pathway. Predicted to be located in nuclear speck and nucleolus. Predicted to be active in cytosol and membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: urethritis (0.352); hyperaldosteronism (0.191); benign neoplasm of eye (0.179); preeclampsia (0.179); Complete right bundle branch block (0.178)
- **Europe PMC papers**: 130
- **Why important**: ZNF106 is the central connector in the supplied co-abundance subgraph, linking SLK, RNGTT, and LIG1. Its annotations support RNA binding and predicted nuclear-speck and nucleolar localization, while HPA reports group enrichment in muscle-associated tissues and enhancement in several cell types, including neutrophils. It has disease associations in Open Targets and a moderate literature base, making it a plausible regulatory marker despite the absence of STRING or hu.MAP support.
- **Conclusion**: Established evidence: ZNF106 is the network hub in this module and has RNA-associated and nuclear annotations. Hypothesis: it may coordinate the observed association between RNA processing, DNA maintenance, and signaling-related genes. Its regulatory role in this cross-tissue module remains unproven.

#### LIG1

- **Related proteins** (co-abundance neighbors): ZNF106 (0.81), MOCOS (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA ligase 1. This gene encodes a member of the ATP-dependent DNA ligase protein family. The encoded protein functions in DNA replication, recombination, and the base excision repair process. Mutations in this gene that lead to DNA ligase I deficiency result in immunodeficiency and increased sensitivity to DNA-damaging agents. Disruption of this gene may also be associated with a variety of cancers. Alternative…
- **Diseases (Open Targets)**: immunodeficiency 96 (0.689); HIV infectious disease (0.370); neurodegenerative disease (0.245); Epiretinal membrane (0.202); permanent neonatal diabetes mellitus (0.118)
- **Europe PMC papers**: 2295
- **Why important**: LIG1 is directly connected to the central ZNF106 and to MOCOS. Its established function in DNA replication, recombination, base-excision repair, mismatch repair, and lagging-strand elongation gives the module a strong genome-maintenance component. LIG1 also has extensive literature and a prominent immunodeficiency association, while HPA indicates tissue enhancement in bone marrow and lymphoid tissue.
- **Conclusion**: Established evidence: LIG1 is a DNA ligase required for replication and repair, with disease relevance in ligase deficiency and cancer-related biology. Hypothesis: its co-abundance with the other module genes may mark proliferative or repair-active cell states. The supplied data do not establish that LIG1 physically interacts with any module member.

#### SLK

- **Related proteins** (co-abundance neighbors): ZNF106 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: STE20 like kinase. Enables protein homodimerization activity and protein serine/threonine kinase activity. Involved in several processes, including cytoplasmic microtubule organization; protein autophosphorylation; and regulation of focal adhesion assembly. Located in perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.448); uterine corpus leiomyoma (0.408); stroke disorder (0.339); coronary artery disorder (0.288); Menorrhagia (0.202)
- **Europe PMC papers**: 2571
- **Why important**: SLK is connected to ZNF106 and contributes a signaling and cytoskeletal dimension through serine-threonine kinase activity, microtubule organization, cell migration, apoptosis regulation, and focal-adhesion assembly. It has a substantial literature base and disease associations that include uterine corpus leiomyoma and menorrhagia, which are relevant to reproductive-tissue biology. HPA classifies it as having low tissue specificity and detects it in both tissues.
- **Conclusion**: Established evidence: SLK is a kinase involved in cytoskeletal organization, migration, focal adhesions, and apoptotic regulation. Hypothesis: SLK may connect the module to tissue remodeling or cell-state transitions in the two tissues. Its role as a driver of this co-abundance pattern is not demonstrated.

#### RNGTT

- **Related proteins** (co-abundance neighbors): ZNF106 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA guanylyltransferase and 5'-phosphatase. Enables mRNA guanylyltransferase activity and triphosphatase activity. Involved in 7-methylguanosine mRNA capping. Predicted to be located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.515); HIV infectious disease (0.503); autoimmune disorder of central nervous system (0.437); alcohol drinking (0.318); liver disorder (0.314)
- **Europe PMC papers**: 311
- **Why important**: RNGTT is connected to ZNF106 and encodes the RNA guanylyltransferase and triphosphatase required for seven-methylguanosine messenger-RNA capping. Its annotation provides a mechanistic link to RNA processing, and its nucleoplasmic localization is consistent with that function. It has a meaningful literature base and HPA enhancement in neutrophil progenitors, although its tissue specificity is low.
- **Conclusion**: Established evidence: RNGTT is an essential messenger-RNA capping enzyme involved in RNA processing. Hypothesis: its covariation with ZNF106 and LIG1 may reflect coordinated transcriptional or proliferative demand in particular cell populations. The data do not show that RNGTT directly regulates the other module genes.

#### MOCOS

- **Related proteins** (co-abundance neighbors): LIG1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: molybdenum cofactor sulfurase. This gene encodes an enzyme that sulfurates the molybdenum cofactor which is required for activation of the xanthine dehydrogenase (XDH) and aldehyde oxidase (AO) enzymes. XDH catalyzes the conversion of hypoxanthine to uric acid via xanthine, as well as the conversion of allopurinol to oxypurinol, and pyrazinamide to 5-hydroxy pyrazinamide. Mutations in this gene cause the metabolic disorder clas…
- **Diseases (Open Targets)**: xanthinuria type II (0.783); hereditary xanthinuria (0.507); autism spectrum disorder (0.335); stricture (0.192); primary hyperoxaluria (0.131)
- **Europe PMC papers**: 346
- **Why important**: MOCOS is connected to LIG1 and adds a distinct mitochondrial and metabolic component. It sulfurates the molybdenum cofactor required for xanthine dehydrogenase and aldehyde oxidase activity, and pathogenic variants cause classical xanthinuria type two. HPA reports tissue enhancement in adrenal gland and liver and cell-type enhancement in metabolically specialized populations, including hepatocytes and adrenal cortex cells.
- **Conclusion**: Established evidence: MOCOS is required for molybdenum-cofactor activation of specific metabolic enzymes and is associated with hereditary xanthinuria. Hypothesis: MOCOS may mark metabolic state or oxidative and purine-processing differences among the cells contributing to the shared module. Its association with LIG1 does not establish a shared biochemical pathway.

## Module 13

**Tissue pair**: breast and cervix_uterine  
**Genes (5)**: DSC3, DSG1, ALOX12B, MYO1G, PTPRC

### Function

The module most plausibly reflects a mixed epithelial-barrier and immune-cell co-abundance program rather than a single, strongly supported biochemical pathway. The epithelial component is represented by DSG1 and DSC3, which are desmosomal cadherin-family adhesion proteins, while ALOX12B represents epidermal lipid metabolism and PTPRC and MYO1G represent leukocyte-associated signaling and cytoskeletal functions. No GO or KEGG term passed global correction, so the functional interpretation rests on the gene annotations, tissue and cell-type evidence, the sparse network structure, and the supplementary STRING and hu.MAP results. The STRING results support epithelial cadherin biology through (STRING SMART Cadherin repeats.; within-query FDR = 0.0322) and connect the epithelial genes to dermatologic and inflammatory annotations in (STRING DISEASES Autoimmune disease of musculoskeletal system; within-query FDR = 0.0413), (STRING DISEASES Subcorneal pustular dermatosis; within-query FDR = 0.0413), and (STRING HPO Epidermal acanthosis; within-query FDR = 0.0436), but these are supplementary rather than globally corrected enrichment evidence.

**Cell composition.** This is not a plasma-protein or broadly expressed housekeeping module. HPA indicates strong epithelial and skin-associated representation, including basal and suprabasal keratinocyte signals, with additional lymphoid, neutrophil, bone-marrow, and basophil associations. DSG1 and DSC3 are particularly consistent with epithelial or squamous-cell content, whereas PTPRC and MYO1G indicate immune or hematopoietic-cell content. ALOX12B is skin-enriched and associated with tuft cells and basophils. The module therefore may reflect shared epithelial cell states together with variable immune-cell admixture in breast and cervix_uterine samples, rather than a transcriptionally uniform program within one cell type. The HPA protein evidence is also limited in these tissues: the proteins were not detected in breast, and only one module protein was detected in cervix_uterine.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship among the module genes is the established DSC3–DSG1 interaction. This is biologically coherent because desmocollins and desmogleins form adhesive components of desmosomes. The other co-abundance connections, including those involving ALOX12B, PTPRC, and MYO1G, are not supported by listed STRING partner evidence and should not be interpreted as established physical interactions. hu.MAP provides recurring complex-context support for ALOX12B and DSG1 together in (hu.MAP huMAP3_05845.1), (hu.MAP huMAP3_08595.1), (hu.MAP huMAP3_09125.1), and (hu.MAP huMAP3_09929.1), but each complex contains many additional proteins and only a small subset is represented in this module. Thus, the network combines one well-established epithelial interaction with broader complex membership and tissue-level co-abundance, rather than demonstrating a single known molecular complex.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: DSC3–DSG1 (0.933)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Cadherin repeats. (FDR = 0.0322, 2 genes); DISEASES Autoimmune disease of musculoskeletal system (FDR = 0.0413, 3 genes); DISEASES Subcorneal pustular dermatosis (FDR = 0.0413, 2 genes); HPO Epidermal acanthosis (FDR = 0.0436, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05845.1 (ALOX12B, DSG1; 2/24); huMAP3_08595.1 (ALOX12B, DSG1; 2/25); huMAP3_09125.1 (ALOX12B, DSG1; 2/53); huMAP3_09929.1 (ALOX12B, DSG1; 2/75)

### Novelty

The module should not be claimed as a newly discovered molecular complex or pathway. Its epithelial adhesion component is already known through the DSC3–DSG1 STRING relationship, and the ALOX12B–DSG1 pairing occurs in several hu.MAP complex contexts. What may be novel is the observation that these epithelial genes co-abundance with PTPRC and MYO1G across breast and cervix_uterine samples. However, absence of the latter relationships from STRING or hu.MAP does not establish novelty, because co-abundance can arise from shared cell composition, context-specific regulation, or incomplete database coverage. The most defensible conclusion is that this is a potentially interesting cross-tissue co-abundance pattern whose mechanistic novelty requires cell-resolved and experimental validation.

**Hypothesis.** Hypothesis: the module reflects coordinated variation in squamous or epithelial barrier content together with infiltrating or resident immune-cell content. In this model, DSG1 and DSC3 mark desmosomal adhesion and epithelial integrity, ALOX12B contributes epidermal lipid processing, and PTPRC with MYO1G marks leukocyte abundance or activation-related membrane and cytoskeletal behavior. The observed co-abundance could therefore arise from a tissue-state axis linking epithelial differentiation or barrier remodeling with immune-cell presence, rather than from direct physical interaction among all five proteins. This hypothesis predicts that single-cell or spatial measurements would separate an epithelial ALOX12B–DSG1–DSC3 signal from a hematopoietic PTPRC–MYO1G signal.

### Important genes

#### ALOX12B

- **Related proteins** (co-abundance neighbors): PTPRC (0.86), DSG1 (0.84), DSC3 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05845.1, huMAP3_08595.1, huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: arachidonate 12-lipoxygenase, 12R type. This gene encodes an enzyme involved in the conversion of arachidonic acid to 12R-hydroxyeicosatetraenoic acid. Mutations in this gene are associated with nonbullous congenital ichthyosiform erythroderma. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: congenital non-bullous ichthyosiform erythroderma (0.745); self-healing collodion baby (0.733); lamellar ichthyosis (0.639); ichthyosis (0.519); ichthyosis with erythrokeratoderma (0.495)
- **Europe PMC papers**: 2105
- **Why important**: ALOX12B is the principal network connector, linking PTPRC, DSG1, and DSC3 in the module. It is skin-enriched in HPA, participates in the hu.MAP contexts (hu.MAP huMAP3_05845.1), (hu.MAP huMAP3_08595.1), (hu.MAP huMAP3_09125.1), and (hu.MAP huMAP3_09929.1), and encodes a twelve-R lipoxygenase involved in arachidonate and lipid oxidation biology. Its disease associations are dominated by inherited ichthyosis-related disorders, and it has substantial literature support.
- **Conclusion**: Established evidence supports ALOX12B as a skin and epithelial-lipid biology marker and as the central co-abundance connector in this module. It is not established that ALOX12B physically interacts with the other module proteins or mechanistically drives the cross-tissue pattern. Its role as a bridge between epithelial and immune-associated signals is therefore a hypothesis.

#### DSG1

- **Related proteins** (co-abundance neighbors): ALOX12B (0.84); STRING partners: DSC3 (0.933)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_05845.1, huMAP3_08595.1, huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: desmoglein 1. This gene encodes a member of the desmoglein protein subfamily. Desmogleins, along with desmocollins, are cadherin-like transmembrane glycoproteins that are major components of the desmosome. Desmosomes are cell-cell junctions that help resist shearing forces and are found in high concentrations in cells subject to mechanical stress. This gene is found in a cluster with other desmoglein family mem…
- **Diseases (Open Targets)**: palmoplantar keratoderma i, striate, focal, or diffuse (0.738); severe dermatitis-multiple allergies-metabolic wasting syndrome (0.732); striate palmoplantar keratoderma (0.464); hereditary palmoplantar keratoderma (0.455); epidermolytic palmoplantar keratoderma, 1 (0.375)
- **Europe PMC papers**: 3455
- **Why important**: DSG1 is an epithelial desmosomal cadherin and is the partner of DSC3 in the only listed high-confidence STRING interaction. It has the strongest support from the supplementary STRING results, appearing in (STRING SMART Cadherin repeats.; within-query FDR = 0.0322), (STRING DISEASES Autoimmune disease of musculoskeletal system; within-query FDR = 0.0413), (STRING DISEASES Subcorneal pustular dermatosis; within-query FDR = 0.0413), and (STRING HPO Epidermal acanthosis; within-query FDR = 0.0436), and it recurs with ALOX12B in all listed hu.MAP contexts. HPA places it in skin and basal or suprabasal epithelial populations, with protein detection in cervix_uterine. Its keratoderma and dermatitis associations and substantial literature make it a key biological anchor.
- **Conclusion**: Established evidence identifies DSG1 as a desmosomal adhesion protein and a credible marker of epithelial barrier biology in this module. The autoimmune and dermatologic STRING annotations support disease relevance but are supplementary. A specific role for DSG1 in coordinating immune-cell abundance across the two tissues remains unproven.

#### DSC3

- **Related proteins** (co-abundance neighbors): ALOX12B (0.82); STRING partners: DSG1 (0.933)
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: desmocollin 3. The protein encoded by this gene is a calcium-dependent glycoprotein that is a member of the desmocollin subfamily of the cadherin superfamily. These desmosomal family members, along with the desmogleins, are found primarily in epithelial cells where they constitute the adhesive proteins of the desmosome cell-cell junction and are required for cell adhesion and desmosome formation. The desmosomal …
- **Diseases (Open Targets)**: hereditary hypotrichosis with recurrent skin vesicles (0.674); wooly hair-palmoplantar keratoderma syndrome (0.370); systemic inflammatory response syndrome (0.320); sleep apnea syndrome (0.261); ocular hypotension (0.226)
- **Europe PMC papers**: 1514
- **Why important**: DSC3 is a desmosomal cadherin-family adhesion protein with plasma-membrane and cell-junction localization. It is epithelial-cell enriched or enhanced across skin, esophageal, ocular, and basal or suprabasal populations, and it forms the established STRING pair with DSG1. It appears in (STRING SMART Cadherin repeats.; within-query FDR = 0.0322), (STRING DISEASES Autoimmune disease of musculoskeletal system; within-query FDR = 0.0413), (STRING DISEASES Subcorneal pustular dermatosis; within-query FDR = 0.0413), and (STRING HPO Epidermal acanthosis; within-query FDR = 0.0436), and its disease associations include inherited hair, skin, and inflammatory phenotypes. These features make it the clearest structural counterpart to DSG1.
- **Conclusion**: Established evidence supports DSC3 as an epithelial adhesion and desmosome-related component of the module. Its co-abundance with DSG1 is consistent with shared epithelial content and with known molecular association. There is no direct evidence here that DSC3 participates in the immune-associated portion of the module beyond sample-level co-abundance.

#### PTPRC

- **Related proteins** (co-abundance neighbors): ALOX12B (0.86), MYO1G (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein tyrosine phosphatase receptor type C. The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitosis, and oncogenic transformation. This PTP contains an extracellular domain, a single transmembrane segment and two tandem intracytoplasmic catalytic domains, and thus is cl…
- **Diseases (Open Targets)**: immunodeficiency 104 (0.710); immunodeficiency 105 (0.670); T-B+ severe combined immunodeficiency due to JAK3 deficiency (0.566); T-B+ severe combined immunodeficiency due to CD45 deficiency (0.554); asthma (0.542)
- **Europe PMC papers**: 13578
- **Why important**: PTPRC is a receptor-type protein tyrosine phosphatase associated with hematopoietic and immune-cell signaling. It connects to ALOX12B and MYO1G in the module, is lymphoid-tissue enhanced, and is enriched in neutrophils according to HPA. Its annotations include lymphocyte differentiation, cytokine-related signaling, and immunoglobulin production, while its disease associations include immunodeficiency and asthma. Its literature support is extensive.
- **Conclusion**: Established evidence supports PTPRC as an immune-cell composition or signaling marker, not as an epithelial structural protein. Its placement beside ALOX12B and MYO1G strengthens the interpretation that immune-cell admixture contributes to the module. Direct functional coupling between PTPRC and the desmosomal genes is not established by the supplied STRING or hu.MAP evidence.

#### MYO1G

- **Related proteins** (co-abundance neighbors): PTPRC (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin IG. MYO1G is a plasma membrane-associated class I myosin (see MIM 601478) that is abundant in T and B lymphocytes and mast cells (Pierce et al., 2001 [PubMed 11544309]; Patino-Lopez et al., 2010 [PubMed 20071333]).[supplied by OMIM, Jun 2010].
- **Diseases (Open Targets)**: liver disorder (0.205); hypothyroidism (0.096); acute lymphoblastic leukemia (0.090); smoking initiation (0.079); Abnormality of the skeletal system (0.078)
- **Europe PMC papers**: 763
- **Why important**: MYO1G is a plasma-membrane-associated class-one myosin reported to be abundant in lymphocytes and mast cells. It is enhanced in bone marrow and lymphoid tissue and in several immune-cell populations, and its annotations include T-cell immunity, endocytosis, actin organization, phagocytosis-related signaling, and T-cell migration. Its network connection to PTPRC provides an immune-associated branch distinct from the DSG1–DSC3 epithelial relationship.
- **Conclusion**: Established evidence supports MYO1G as a hematopoietic-cell membrane and cytoskeletal marker. Its co-abundance with PTPRC is compatible with shared immune-cell content. A role for MYO1G in regulating the epithelial component or in creating a functional cross-lineage complex is hypothetical.

## Module 14

**Tissue pair**: breast and cervix_uterine  
**Genes (8)**: EPHA2, EPHB4, PTK2, PTK2B, SYK, MET, MAPK14, TJP2

### Function

This is a receptor- and adhesion-linked tyrosine-kinase signaling module. The strongest coherent interpretation is coordinated signaling from cell-surface receptor tyrosine kinases through focal-adhesion and non-receptor kinases, with consequences for endothelial behavior, cell adhesion, migration, chemotaxis, junction organization, and tissue morphogenesis. Primary evidence comes from globally corrected terms for vascular endothelial growth factor receptor signaling (GO:BP vascular endothelial growth factor receptor signaling pathway; q_global = 1.08e-07), protein tyrosine kinase activity (GO:MF protein tyrosine kinase activity; q_global = 1.74e-06), collagen-activated receptor signaling (GO:BP collagen-activated tyrosine kinase receptor signaling pathway; q_global = 9.59e-06) and (GO:BP collagen-activated signaling pathway; q_global = 9.59e-06), cell-surface receptor tyrosine kinase signaling (GO:BP cell surface receptor protein tyrosine kinase signaling pathway; q_global = 1.1e-05), tube morphogenesis (GO:BP tube morphogenesis; q_global = 0.000199), angiogenesis (GO:BP angiogenesis; q_global = 0.000756), endothelial migration (GO:BP endothelial cell migration; q_global = 0.0015), blood-vessel development (GO:BP blood vessel development; q_global = 0.00188) and (GO:BP vasculature development; q_global = 0.00206), cell adhesion (GO:BP cell adhesion; q_global = 0.00351), axon guidance (KEGG Axon guidance - Homo sapiens (human); q_global = 0.00398), PI3K-Akt signaling (KEGG PI3K-Akt signaling pathway - Homo sapiens (human); q_global = 0.0115), and cell-junction organization (GO:BP cell junction organization; q_global = 0.0312). The broad kinase and phosphorylation terms (GO:MF kinase activity; q_global = 1.97e-05), (GO:MF transferase activity, transferring phosphorus-containing groups; q_global = 5.09e-05), (GO:MF protein kinase activity; q_global = 0.000119), (GO:MF phosphotransferase activity, alcohol group as acceptor; q_global = 0.000374), (GO:BP protein phosphorylation; q_global = 0.000839), (GO:BP phosphorylation; q_global = 0.00127), (GO:BP phosphorus metabolic process; q_global = 0.0076), (GO:BP phosphate-containing compound metabolic process; q_global = 0.0076), and (GO:BP peptidyl-tyrosine phosphorylation; q_global = 0.0498) support a signaling-centered rather than a structural-only interpretation. The axon-guidance enrichment should be interpreted as pathway reuse by Eph, MET, and adhesion signaling rather than as evidence that this is a neuronal module.

**Cell composition.** The module is not dominated by secreted or plasma proteins and does not resemble a generic housekeeping module. Most members are membrane, cytosolic, junctional, or nuclear signaling proteins. MET is annotated as secreted to blood, but the module has only a single secreted gene. HPA nevertheless indicates a substantial cell-composition component: several genes are enriched in monocyte or neutrophil progenitors, neutrophils, monocytes, or other immune cells, while others are enriched in endothelial, epithelial, endometrial, or lymphoid cell types. SYK is especially associated with hematopoietic cells, and MAPK14 and PTK2B show myeloid or neutrophil-related enrichment. Therefore, the shared breast and cervix_uterine signal may reflect a biological signaling program in epithelial, endothelial, and stromal compartments, but it may also partly reflect shared immune or vascular cell admixture. The protein-detection evidence supports presence of most members in both tissues, while the cell-type specificity argues against treating the module as uniformly expressed by every cell.

**GO/KEGG enrichment**: 110 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP vascular endothelial growth factor receptor signaling pathway | 1.08e-07 | EPHA2, EPHB4, MAPK14, MET, PTK2, PTK2B |
| GO:MF protein tyrosine kinase activity | 1.74e-06 | EPHA2, EPHB4, MET, PTK2, PTK2B, SYK |
| GO:BP collagen-activated tyrosine kinase receptor signaling pathway | 9.59e-06 | EPHA2, EPHB4, MET, SYK |
| GO:BP collagen-activated signaling pathway | 9.59e-06 | EPHA2, EPHB4, MET, SYK |
| GO:BP cell surface receptor protein tyrosine kinase signaling pathway | 1.1e-05 | EPHA2, EPHB4, MAPK14, MET, PTK2, PTK2B, SYK |
| GO:MF kinase activity | 1.97e-05 | EPHA2, EPHB4, MAPK14, MET, PTK2, PTK2B, SYK, TJP2 |
| GO:MF transferase activity, transferring phosphorus-containing groups | 5.09e-05 | EPHA2, EPHB4, MAPK14, MET, PTK2, PTK2B, SYK, TJP2 |
| GO:BP chemotaxis | 5.93e-05 | EPHA2, MAPK14, MET, PTK2, PTK2B, SYK |
| GO:BP taxis | 5.93e-05 | EPHA2, MAPK14, MET, PTK2, PTK2B, SYK |
| GO:BP epidermal growth factor receptor signaling pathway | 7.65e-05 | EPHA2, EPHB4, MET, PTK2, PTK2B |
| GO:BP enzyme-linked receptor protein signaling pathway | 8.66e-05 | EPHA2, EPHB4, MAPK14, MET, PTK2, PTK2B, SYK |
| GO:BP ERBB signaling pathway | 0.00011 | EPHA2, EPHB4, MET, PTK2, PTK2B |
| GO:MF protein kinase activity | 0.000119 | EPHA2, EPHB4, MAPK14, MET, PTK2, PTK2B, SYK |
| GO:BP ephrin receptor signaling pathway | 0.000184 | EPHA2, EPHB4, MET, PTK2 |
| GO:BP tube morphogenesis | 0.000199 | EPHA2, EPHB4, MAPK14, MET, PTK2, PTK2B, SYK |

### STRING and hu.MAP

STRING supports several established relationships within the module: EPHA2 is linked to EPHB4; MAPK14 is linked to PTK2; MET is linked to PTK2; and PTK2 is linked to PTK2B. These links connect receptor signaling with focal-adhesion signaling and stress or inflammatory kinase signaling. The STRING functional annotations independently reinforce a tyrosine-kinase catalytic-domain and receptor-tyrosine-kinase interpretation (STRING SMART Tyrosine kinase, catalytic domain; within-query FDR = 2.21e-09) through (STRING InterPro Protein kinase, ATP binding site; within-query FDR = 5.09e-07), as well as angiogenesis, tube morphogenesis, and chemotaxis (STRING Process Tube morphogenesis; within-query FDR = 4.41e-06) through (STRING Process Chemotaxis; within-query FDR = 7.47e-06). However, STRING does not support every co-abundance edge, so the remaining edges may represent indirect signaling, shared cell-type abundance, or context-dependent associations rather than direct physical binding. No hu.MAP complex contains multiple module members. Thus, this is better viewed as a coordinated signaling network than as a stable, experimentally defined multiprotein complex.

**STRING interactions (score >= 0.7)**: 4 of 28 gene pairs: EPHA2–EPHB4 (0.808); MAPK14–PTK2 (0.941); MET–PTK2 (0.935); PTK2–PTK2B (0.984)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Tyrosine kinase, catalytic domain (FDR = 2.21e-09, 6 genes); InterPro Tyrosine-protein kinase, catalytic domain (FDR = 1.15e-08, 6 genes); InterPro Tyrosine-protein kinase, active site (FDR = 1.2e-08, 6 genes); InterPro Serine-threonine/tyrosine-protein kinase, catalytic domain (FDR = 1.54e-08, 6 genes); Keyword Tyrosine-protein kinase (FDR = 1.94e-08, 6 genes); Process Transmembrane receptor protein tyrosine kinase signaling pathway (FDR = 2.39e-07, 7 genes); Function Protein tyrosine kinase activity (FDR = 3.2e-07, 6 genes); InterPro Protein kinase, ATP binding site (FDR = 5.09e-07, 7 genes); Function Kinase activity (FDR = 1.77e-06, 8 genes); InterPro Protein kinase domain (FDR = 1.89e-06, 7 genes); Process Tube morphogenesis (FDR = 4.41e-06, 7 genes); Keyword Angiogenesis (FDR = 4.82e-06, 5 genes); InterPro Protein kinase-like domain superfamily (FDR = 4.89e-06, 7 genes); Process Angiogenesis (FDR = 6.82e-06, 6 genes); Process Chemotaxis (FDR = 7.47e-06, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The biological functions represented here are not novel in isolation: Eph receptors, MET, PTK2, PTK2B, SYK, MAPK14, and TJP2 are individually well established in receptor signaling, adhesion, immune signaling, angiogenesis, stress responses, or epithelial junctions. The module therefore should not be claimed as a newly discovered pathway. A potentially novel aspect is the conserved co-abundance configuration shared by breast and cervix_uterine, particularly the combination of Eph receptors, MET, focal-adhesion kinases, SYK, MAPK14, and TJP2. That configuration may be a new tissue-crossing biomarker or systems-level observation, but absence of a matching STRING interaction or hu.MAP complex does not establish novelty. The appropriate conclusion is that the module is a potentially novel association pattern built from largely established signaling components and requires independent validation, ideally with cell-resolved measurements and perturbation experiments.

**Hypothesis.** Hypothesis: the shared module reflects a tissue-interface program in which Eph and MET receptor activity is coupled to focal-adhesion signaling through PTK2 and PTK2B, while MAPK14 and SYK integrate inflammatory or immune-cell inputs. TJP2 may provide a junctional and barrier-related context that couples receptor signaling to epithelial or endothelial organization. In breast and cervix_uterine, variation in vascular, epithelial, stromal, and infiltrating myeloid cell abundance could therefore produce a conserved co-abundance pattern corresponding to coordinated angiogenic remodeling, cell migration, adhesion, and inflammatory communication. This is a mechanistic hypothesis rather than a demonstrated causal model; the co-abundance data and enrichment results do not establish directionality, physical binding, or cell-of-origin.

### Important genes

#### EPHA2

- **Related proteins** (co-abundance neighbors): MET (0.90), PTK2 (0.90), TJP2 (0.83), PTK2B (0.81); STRING partners: EPHB4 (0.808)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EPH receptor A2. This gene belongs to the ephrin receptor subfamily of the protein-tyrosine kinase family. EPH and EPH-related receptors have been implicated in mediating developmental events, particularly in the nervous system. Receptors in the EPH subfamily typically have a single kinase domain and an extracellular region containing a Cys-rich domain and 2 fibronectin type III repeats. The ephrin receptors are d…
- **Diseases (Open Targets)**: early-onset posterior polar cataract (0.770); total early-onset cataract (0.770); early-onset non-syndromic cataract (0.681); colorectal cancer (0.594); chronic myeloid leukemia (0.583)
- **Europe PMC papers**: 8524
- **Why important**: EPHA2 is among the more connected module members and links to MET, PTK2, TJP2, and PTK2B in the co-abundance network. It contributes to globally corrected Eph receptor, receptor tyrosine kinase, angiogenesis, endothelial migration, cell adhesion, tube morphogenesis, and axon-guidance evidence (GO:BP vascular endothelial growth factor receptor signaling pathway; q_global = 1.08e-07), (GO:BP cell surface receptor protein tyrosine kinase signaling pathway; q_global = 1.1e-05), (GO:BP ephrin receptor signaling pathway; q_global = 0.000184), (GO:BP angiogenesis; q_global = 0.000756), (GO:BP endothelial cell migration; q_global = 0.0015), (KEGG Axon guidance - Homo sapiens (human); q_global = 0.00398), and (GO:BP cell junction organization; q_global = 0.0312). Its plasma-membrane and cell-junction localization makes it a plausible interface between receptor signaling and tissue architecture. It has extensive literature and disease associations including colorectal cancer and chronic myeloid leukemia in the supplied Open Targets evidence.
- **Conclusion**: Established: EPHA2 is a central receptor-signaling and adhesion-related member of this module with strong pathway support. Hypothesis: EPHA2 may help couple epithelial or endothelial junction state to the MET and focal-adhesion signaling axis in the shared tissue program.

#### PTK2

- **Related proteins** (co-abundance neighbors): EPHA2 (0.90), MET (0.83), MAPK14 (0.82); STRING partners: MAPK14 (0.941), MET (0.935), PTK2B (0.984)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein tyrosine kinase 2. This gene encodes a cytoplasmic protein tyrosine kinase which is found concentrated in the focal adhesions that form between cells growing in the presence of extracellular matrix constituents. The encoded protein is a member of the FAK subfamily of protein tyrosine kinases but lacks significant sequence similarity to kinases from other subfamilies. Activation of this gene may be an important early…
- **Diseases (Open Targets)**: neurodegenerative disease (0.551); Abnormality of the skeletal system (0.450); atrial fibrillation (0.396); Dupuytren Contracture (0.390); non-small cell lung carcinoma (0.327)
- **Europe PMC papers**: 7056
- **Why important**: PTK2 is a highly connected signaling hub linking EPHA2, MET, and MAPK14, and it has strong STRING support with MAPK14, MET, and PTK2B. It is supported by globally corrected evidence for tyrosine kinase activity, integrin-mediated adhesion, endothelial migration, angiogenesis, PI3K-Akt signaling, chemotaxis, and peptidyl-tyrosine phosphorylation (GO:MF protein tyrosine kinase activity; q_global = 1.74e-06), (GO:BP angiogenesis; q_global = 0.000756), (GO:BP endothelial cell migration; q_global = 0.0015), (GO:BP cell adhesion; q_global = 0.00351), (KEGG PI3K-Akt signaling pathway - Homo sapiens (human); q_global = 0.0115), (GO:BP regulation of cell adhesion mediated by integrin; q_global = 0.013), (GO:MF non-membrane spanning protein tyrosine kinase activity; q_global = 0.0167), and (GO:BP peptidyl-tyrosine phosphorylation; q_global = 0.0498). Its focal-adhesion localization and established role in cell-matrix adhesion make it a mechanistic bridge between receptor activity and cellular movement. It has extensive literature and supplied disease associations involving skeletal abnormalities, atrial fibrillation, and cancer.
- **Conclusion**: Established: PTK2 is a central focal-adhesion kinase that provides a credible integrator for the module's receptor, adhesion, migration, and angiogenesis signals. Hypothesis: PTK2 may be the principal intracellular coupling point that converts coordinated receptor abundance into the observed tissue-level co-abundance pattern.

#### MET

- **Related proteins** (co-abundance neighbors): EPHA2 (0.90), PTK2 (0.83), EPHB4 (0.81); STRING partners: PTK2 (0.935)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MET proto-oncogene, receptor tyrosine kinase. This gene encodes a member of the receptor tyrosine kinase family of proteins and the product of the proto-oncogene MET. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that are linked via disulfide bonds to form the mature receptor. Further processing of the beta subunit results in the formation of the M10 peptide, which has been shown to reduce lung fib…
- **Diseases (Open Targets)**: papillary renal cell carcinoma (0.834); hereditary papillary renal cell carcinoma (0.767); hepatocellular carcinoma (0.758); renal cell carcinoma (0.729); non-small cell lung carcinoma (0.724)
- **Europe PMC papers**: 433916
- **Why important**: MET is a connected receptor linking EPHA2, PTK2, and EPHB4 and is present in the primary evidence for receptor tyrosine kinase, collagen-activated, growth-factor, chemotaxis, angiogenesis, and PI3K-Akt-related processes (GO:BP vascular endothelial growth factor receptor signaling pathway; q_global = 1.08e-07) through (GO:BP cell surface receptor protein tyrosine kinase signaling pathway; q_global = 1.1e-05), (GO:BP epidermal growth factor receptor signaling pathway; q_global = 7.65e-05), (GO:BP ERBB signaling pathway; q_global = 0.00011), (GO:BP angiogenesis; q_global = 0.000756), (GO:BP hepatocyte growth factor receptor signaling pathway; q_global = 0.0018), (KEGG Axon guidance - Homo sapiens (human); q_global = 0.00398), and (KEGG PI3K-Akt signaling pathway - Homo sapiens (human); q_global = 0.0115). It is detected in both tissues, is enriched in several endometrial and epithelial cell types, and is annotated as secreted to blood, making it relevant both to tissue signaling and possible sample-level circulating contribution. MET has exceptionally extensive literature and strong supplied disease associations with renal and hepatic cancers.
- **Conclusion**: Established: MET is a biologically plausible receptor-level driver of growth-factor, migration, and morphogenetic signaling in this module. Hypothesis: MET activity may coordinate epithelial repair or remodeling with PTK2-dependent motility and Eph-receptor signaling across the two tissues.

#### SYK

- **Related proteins** (co-abundance neighbors): TJP2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cytosol; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: spleen associated tyrosine kinase. This gene encodes a member of the family of non-receptor type Tyr protein kinases. This protein is widely expressed in hematopoietic cells and is involved in coupling activated immunoreceptors to downstream signaling events that mediate diverse cellular responses, including proliferation, differentiation, and phagocytosis. It is thought to be a modulator of epithelial cell growth and a potential t…
- **Diseases (Open Targets)**: immunodeficiency 82 with systemic inflammation (0.635); cutaneous leishmaniasis (0.573); immunodeficiency disease (0.569); Decreased circulating immunoglobulin concentration (0.565); autoimmune thrombocytopenic purpura (0.520)
- **Europe PMC papers**: 19675
- **Why important**: SYK is a non-receptor tyrosine kinase with globally corrected support for receptor tyrosine kinase signaling, chemotaxis, cytokine-mediated signaling, cell adhesion, immune-related responses, and integrin-mediated adhesion (GO:MF protein tyrosine kinase activity; q_global = 1.74e-06), (GO:BP cell surface receptor protein tyrosine kinase signaling pathway; q_global = 1.1e-05), (GO:BP chemotaxis; q_global = 5.93e-05), (GO:BP cell chemotaxis; q_global = 0.000513), (GO:BP cytokine-mediated signaling pathway; q_global = 0.00227), (GO:BP cell adhesion; q_global = 0.00351), and (GO:BP regulation of cell adhesion mediated by integrin; q_global = 0.013). Its HPA profile is strongly associated with hematopoietic and immune cell types, including B cells, myeloid cells, monocytes, and neutrophils. The supplied functional description places SYK in immunoreceptor coupling, proliferation, differentiation, phagocytosis, and macrophage activation, and its literature volume is extensive. Its network position is peripheral, but it is important because it identifies a likely immune-cell component that is not captured by the receptor-only interpretation.
- **Conclusion**: Established: SYK provides strong evidence that the module can include immune or myeloid signaling in addition to epithelial and endothelial signaling. Hypothesis: SYK-related co-abundance may partly mark infiltrating or resident immune cells that communicate with the MET, Eph, and adhesion program.

#### TJP2

- **Related proteins** (co-abundance neighbors): EPHA2 (0.83), SYK (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cell Junctions; IHC detected in breast, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tight junction protein 2. This gene encodes a zonula occluden that is a member of the membrane-associated guanylate kinase homolog family. The encoded protein functions as a component of the tight junction barrier in epithelial and endothelial cells and is necessary for proper assembly of tight junctions. Mutations in this gene have been identified in patients with hypercholanemia, and genomic duplication of a 270 kb regio…
- **Diseases (Open Targets)**: cholestasis, progressive familial intrahepatic, 4 (0.800); hypercholanemia, familial 1 (0.647); autosomal dominant nonsyndromic hearing loss (0.558); progressive familial intrahepatic cholestasis type 2 (0.527); deafness (0.467)
- **Europe PMC papers**: 1748
- **Why important**: TJP2 is a junctional scaffold connected to EPHA2 and SYK in the module and is annotated as a component of epithelial and endothelial tight-junction barriers. It contributes to globally corrected kinase, cell adhesion, cell-junction organization, and cell-development evidence (GO:MF kinase activity; q_global = 1.97e-05), (GO:BP cell adhesion; q_global = 0.00351), (GO:BP cell junction organization; q_global = 0.0312), and (GO:BP cell development; q_global = 0.0351). It is detected in both tissues and has supplied disease associations involving hypercholanemia, cholestasis, and inherited hearing loss. Although it is less connected and has fewer pathway annotations than the kinase-rich members, it anchors the module in tissue-barrier architecture.
- **Conclusion**: Established: TJP2 supports a junctional and barrier-related interpretation and is not merely a generic kinase annotation. Hypothesis: TJP2 may provide the structural context through which receptor and immune signaling alter epithelial or endothelial organization.
