# Conserved co-abundance modules: breast and cerebrospinal_fluid

## Module 0

**Tissue pair**: breast and cerebrospinal_fluid  
**Genes (23)**: LRG1, ACE, ADGRG6, CDH13, CADM1, CPM, CD14, ALCAM, CD276, EMILIN1, GOLM1, ICAM1, BPNT2, L1CAM, LGMN, MFAP4, OGN, LCN2, PPM1L, SCUBE2, TENM4, FAS, VNN1

### Function

The module does not have a statistically supported GO or KEGG functional theme: no GO or KEGG term passed global correction, and STRING reports no functional enrichment. Its structure instead suggests a mixed extracellular, adhesion, vascular, epithelial, neural, and innate-immune interface. SCUBE2 is the central network connector and is annotated as an extracellular, lipid- and calcium-binding signaling protein with links to hedgehog and BMP signaling. PPM1L connects several extracellular-matrix and vascular-associated proteins while providing an intracellular signaling and sphingolipid-regulatory component. TENM4 and L1CAM support a neural-development and cell-adhesion aspect, whereas ICAM1, CD14, FAS, LGMN, CPM, VNN1, and LCN2 support leukocyte adhesion, innate immunity, inflammatory response, or myeloid-cell biology. ACE, MFAP4, EMILIN1, OGN, and LRG1 add vascular, extracellular-matrix, proteolytic, or remodeling-related biology. These annotations support a broad cell-surface and extracellular-interface interpretation rather than a single established pathway.

**Cell composition.** The module is compositionally heterogeneous and is not a simple housekeeping module. Many members are secreted, extracellular-matrix, vesicular, or membrane-associated proteins, including SCUBE2, ACE, FAS, MFAP4, EMILIN1, OGN, LRG1, LCN2, and CD14. HPA evidence shows frequent enrichment in non-classical monocytes, classical monocytes, neutrophils, and myeloid dendritic cells, with additional enrichment in Kupffer cells, macrophages, vascular cells, stromal cells, and neural cell types. This pattern raises a substantial sample-composition explanation: the shared breast and cerebrospinal-fluid signal may partly reflect blood-derived or myeloid material, vascular interfaces, or shared cell populations rather than a tissue-intrinsic program. Breast protein detection is mixed, and the fact sheet has no matching HPA tissue assessment for cerebrospinal fluid, so the module should not be interpreted as direct evidence of cerebrospinal-fluid protein abundance. The presence of several tissue-enhanced genes does not establish that all module members originate from the same cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The high-confidence STRING network contains only a small set of known relationships within the module: ALCAM connects to ICAM1 and L1CAM, and CADM1 connects to ICAM1. These links provide established support for a cell-adhesion and immune-contact subnetwork, but they do not explain the entire module. No STRING functional enrichment was reported, and most module genes have no listed STRING partner in the fact sheet. hu.MAP provides convergent complex-level support for ACE, ALCAM, and CD276, especially their recurrence in C1, and for ALCAM with CD276 across several additional complexes. However, these complexes are broad and contain many proteins outside the module; their presence supports shared complex membership or related cellular context, not a demonstrated physical complex composed of the whole module. The combination of sparse STRING edges and repeated hu.MAP membership suggests partial reuse of known adhesion, membrane, vesicular, and immune-associated protein contexts rather than a single fully established molecular assembly.

**STRING interactions (score >= 0.7)**: 3 of 253 gene pairs: ALCAM–ICAM1 (0.755); ALCAM–L1CAM (0.979); CADM1–ICAM1 (0.773)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11349.1 (ACE, ALCAM, CD276; 3/78); huMAP3_07927.1 (ACE, CD276; 2/8); huMAP3_09169.1 (ACE, CD276; 2/9); huMAP3_02887.1 (ALCAM, CD276; 2/9); huMAP3_05555.1 (ALCAM, CD276; 2/9); huMAP3_06308.1 (ALCAM, CD276; 2/20); huMAP3_10503.1 (ALCAM, CD276; 2/27); huMAP3_08689.1 (ALCAM, CD276; 2/37); huMAP3_10980.1 (ALCAM, CD276; 2/44); huMAP3_10848.1 (ALCAM, CD276; 2/46); huMAP3_09336.1 (ALCAM, CD276; 2/50)

### Novelty

This module cannot be declared a new biological mechanism from the available evidence. Its cross-tissue co-abundance pattern may be a potentially novel observation because the module is not represented as a densely connected interaction network in STRING or hu.MAP, and no prior module-level publication is supplied. Nevertheless, absence from those resources does not prove novelty: co-abundance relationships can reflect shared cell composition, secretion, sample handling, or correlated tissue contamination, and database coverage is incomplete. The module should therefore be described as a candidate cross-tissue co-abundance signature requiring independent replication, cell-type deconvolution, protein-level validation, and comparison with published breast, cerebrospinal-fluid, plasma, and myeloid signatures.

**Hypothesis.** Hypothesis: the module represents a shared extracellular and cell-surface interface involving vascular or stromal compartments together with blood-derived myeloid material. In this model, SCUBE2 and extracellular-matrix proteins provide an organizing extracellular context; ALCAM, CADM1, ICAM1, and L1CAM mediate or mark cell-contact and adhesion states; ACE and PPM1L contribute signaling and membrane or lipid-regulatory context; and CD14, VNN1, LCN2, LGMN, CPM, and FAS reflect innate-immune or myeloid-associated activity. Breast and cerebrospinal-fluid samples could therefore show coordinated abundance because they contain related vascular, barrier, secreted, or immune-derived components, rather than because every gene participates in one canonical pathway. This is a hypothesis, not an established causal mechanism.

### Important genes

#### SCUBE2

- **Related proteins** (co-abundance neighbors): CADM1 (1.00), FAS (0.97), LGMN (0.97), ICAM1 (0.97), GOLM1 (0.97), ADGRG6 (0.96), CPM (0.95), BPNT2 (0.87), CD276 (0.84), ALCAM (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal peptide, CUB domain and EGF like domain containing 2. Predicted to enable calcium ion binding activity; hedgehog family protein binding activity; and lipid binding activity. Predicted to be involved in signal transduction. Predicted to act upstream of or within several processes, including positive regulation of chondrocyte proliferation; positive regulation of osteoblast differentiation; and positive regulation of smoothened signaling pathway. Predi…
- **Diseases (Open Targets)**: arteriovenous malformations of the brain (0.266); prostate carcinoma (0.257); anemia (phenotype) (0.198); breast cancer (0.091); glioma (0.076)
- **Europe PMC papers**: 884
- **Why important**: SCUBE2 has the strongest network position in the module and links adhesion-related, immune-associated, extracellular, and signaling-associated neighbors. HPA places it in extracellular secretion and shows enrichment in breast hormone-responsive and prostatic or epididymal cell types, with immune-cell enrichment in non-classical monocytes. Its annotated calcium-binding, lipid-binding, hedgehog-related, and BMP-related functions make it a plausible extracellular organizer. Its disease associations include brain arteriovenous malformations and breast cancer, while its literature volume is substantial but much smaller than that of the most extensively studied immune genes.
- **Conclusion**: Established evidence supports SCUBE2 as the principal network connector and an extracellular signaling protein. It is a strong candidate module marker. Whether it mechanistically coordinates the other module members, or merely tracks a shared extracellular or cell-composition state, remains unresolved.

#### PPM1L

- **Related proteins** (co-abundance neighbors): MFAP4 (0.96), LRG1 (0.90), EMILIN1 (0.89), ACE (0.87), OGN (0.87), BPNT2 (0.86), CDH13 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase, Mg2+/Mn2+ dependent 1L. The protein encoded by this gene is a magnesium or manganese-requiring phosphatase that is involved in several signaling pathways. The encoded protein downregulates apoptosis signal-regulating kinase 1, a protein that initiates a signaling cascade that leads to apoptosis when cells are subjected to cytotoxic stresses. This protein also is an endoplasmic reticulum transmembrane protein that helps r…
- **Diseases (Open Targets)**: placental abruption (0.227); immune system disorder (0.214); hypertensive disorder (0.204); cervical carcinoma (0.186); ovarian neoplasm (0.181)
- **Europe PMC papers**: 354
- **Why important**: PPM1L is the main connector for a separate branch containing MFAP4, LRG1, EMILIN1, ACE, OGN, BPNT2, and CDH13. It is annotated as an endoplasmic-reticulum phosphatase involved in signaling, apoptosis-related regulation, and ceramide transport. Its network position links intracellular membrane biology to vascular and extracellular-matrix proteins, while HPA shows low tissue specificity and immune enhancement in non-classical monocytes. Its disease associations include placental, hypertensive, immune, and ovarian disorders, with a relatively limited literature volume.
- **Conclusion**: Established evidence supports PPM1L as a plausible intracellular and membrane-regulatory bridge within the module. The co-abundance relationship with extracellular-matrix proteins does not establish direct biochemical interaction; it may instead reflect coordinated cell state, secretion, or tissue composition.

#### TENM4

- **Related proteins** (co-abundance neighbors): LCN2 (0.91), CADM1 (0.89), ACE (0.83), CD14 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: teneurin transmembrane protein 4. The protein encoded by this gene plays a role in establishing proper neuronal connectivity during development. Defects in this gene have been associated with hereditary essential tremor-5. [provided by RefSeq, Oct 2016].
- **Diseases (Open Targets)**: essential tremor (0.684); Abnormality of the skeletal system (0.495); bipolar disorder (0.424); type 2 diabetes mellitus (0.407); alcohol drinking (0.372)
- **Europe PMC papers**: 623
- **Why important**: TENM4 links the module to LCN2, CADM1, ACE, and CD14 and is annotated for neuronal connectivity, axon guidance, myelination, and central nervous system development. HPA shows enrichment in brain neurons as well as ovary and parathyroid gland, while it is not detected in immune cells. Its disease associations include essential tremor, bipolar disorder, and skeletal abnormalities. Its literature volume is moderate.
- **Conclusion**: Established evidence supports TENM4 as a neural- and adhesion-associated component that is particularly relevant when interpreting the cerebrospinal-fluid side of the shared module. Its correlation with myeloid-associated genes should not be interpreted as evidence that TENM4 is expressed by immune cells; it may reflect mixed-cell or barrier-related biology.

#### ACE

- **Related proteins** (co-abundance neighbors): VNN1 (0.93), PPM1L (0.87), TENM4 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11349.1, huMAP3_07927.1, huMAP3_09169.1
- **Function (MyGene.info)**: angiotensin I converting enzyme. This gene encodes an enzyme involved in blood pressure regulation and electrolyte balance. It catalyzes the conversion of angiotensin I into a physiologically active peptide angiotensin II. Angiotensin II is a potent vasopressor and aldosterone-stimulating peptide that controls blood pressure and fluid-electrolyte balance. This angiotensin converting enzyme (ACE) also inactivates the vasodilator p…
- **Diseases (Open Targets)**: hypertensive disorder (0.750); renal tubular dysgenesis of genetic origin (0.729); renal tubular dysgenesis (0.724); cardiovascular disorder (0.704); diabetic kidney disease (0.689)
- **Europe PMC papers**: 95248
- **Why important**: ACE connects the PPM1L branch to TENM4 and VNN1 and appears repeatedly in hu.MAP complexes with ALCAM and CD276, including the higher-confidence complex C1. It is a secreted-to-blood enzyme with established roles in angiotensin maturation, blood-pressure regulation, electrolyte balance, vascular remodeling, and neutrophil-mediated immunity. Its disease associations strongly include hypertension, renal developmental disorders, cardiovascular disease, and diabetic kidney disease. ACE has a very large literature base.
- **Conclusion**: Established evidence supports ACE as a vascular, circulating, and inflammatory-context marker with strong disease relevance. Its module membership may indicate vascular or blood-derived material rather than a novel ACE-centered complex. The hu.MAP evidence supports shared complex context but does not prove that ACE directly interacts with every module member.

#### CD14

- **Related proteins** (co-abundance neighbors): TENM4 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD14 molecule. The protein encoded by this gene is a surface antigen that is preferentially expressed on monocytes/macrophages. It cooperates with other proteins to mediate the innate immune response to bacterial lipopolysaccharide, and to viruses. This gene has been identified as a target candidate in the treatment of SARS-CoV-2-infected patients to potentially lessen or inhibit a severe inflammatory response. …
- **Diseases (Open Targets)**: dengue disease (0.393); inborn error of immunity (0.370); Back pain (0.195); Sepsis (0.140); COVID-19 (0.136)
- **Europe PMC papers**: 85222
- **Why important**: CD14 is a surface antigen associated with monocytes and macrophages and is annotated for bacterial-pattern recognition, cytokine production, phagocytosis, endocytosis, and innate immune signaling. HPA shows liver enhancement, Hofbauer-cell enrichment, and classical-monocyte immune enhancement. It connects the neural or adhesion-associated TENM4 branch to the broader extracellular and immune interpretation. Its disease associations include sepsis, inborn errors of immunity, dengue, and COVID-related disease, and it has an extensive literature base.
- **Conclusion**: Established evidence supports CD14 as a strong indicator of myeloid or blood-derived contribution. Its presence makes sample composition a leading explanation for at least part of the shared module. It does not by itself establish a breast–cerebrospinal-fluid mechanism or imply that the complete module is an innate-immune pathway.

## Module 1

**Tissue pair**: breast and cerebrospinal_fluid  
**Genes (9)**: A2M, SERPINA3, APOA1, C3, COL6A2, HP, IGHG1, IGKC, TF

### Function

The module is best interpreted as a circulating extracellular proteostasis, inflammation, lipid-transport, complement, and iron-handling module rather than as a tissue-specific intracellular pathway. Its strongest biological coherence comes from the established functions of C3, A2M, APOA1, HP, TF, and SERPINA3: complement activation, protease and cytokine regulation, lipoprotein transport, hemoglobin handling, iron transport, and inflammatory control. The module also contains extracellular-matrix collagen COL6A2 and immunoglobulin genes IGHG1 and IGKC, suggesting admixture of matrix, plasma, and immune-related signals. No GO or KEGG term passed global correction, so no GO or KEGG enrichment is primary evidence. The STRING literature associations (STRING PMID (2018) Differences in the Plasma Proteome of Patients with Hypothyroidism before and after Thyroid Hormone Replacement: A Proteomic Analysis.; within-query FDR = 0.0022) through (STRING PMID (2023) Quantitative proteomic analysis of human serum using tandem mass tags to predict cardiovascular risks in patients with psoriasis.; within-query FDR = 0.0172) are supplementary and support a plasma-proteome interpretation, not a globally significant pathway enrichment claim.

**Cell composition.** The composition strongly indicates a blood-derived or extracellular signal. HPA classifies every module gene as secreted or belonging to an immunoglobulin secretome. Several members are liver-enriched or hepatocyte-associated, especially APOA1, C3, HP, TF, and SERPINA3, while A2M is associated with hepatocytes and fibroblasts. IGHG1 and IGKC point to plasma-cell and memory-B-cell contributions. COL6A2 points to extracellular matrix and fibroblast or stromal biology. The module therefore could reflect circulating proteins, plasma contamination, vascular or stromal material, and shared immune-cell content rather than a breast-and-cerebrospinal-fluid specific program. Breast protein detection is limited to a subset of members, while the HPA summary has no matching cerebrospinal-fluid tissue measurement; this limits direct tissue-localization claims.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a connected known protein-association backbone involving A2M, APOA1, HP, SERPINA3, TF, and C3. Particularly coherent links connect A2M with APOA1, HP, SERPINA3, and TF; APOA1 with C3, HP, and TF; and HP with C3, SERPINA3, and TF. These are consistent with shared plasma abundance, physical or functional association, and recurrent detection in circulating-proteome studies (STRING PMID (2018) Differences in the Plasma Proteome of Patients with Hypothyroidism before and after Thyroid Hormone Replacement: A Proteomic Analysis.; within-query FDR = 0.0022) through (STRING PMID (2023) Quantitative proteomic analysis of human serum using tandem mass tags to predict cardiovascular risks in patients with psoriasis.; within-query FDR = 0.0172). The immunoglobulin genes have no listed STRING partners, and COL6A2 has no listed STRING or hu.MAP relationship, so their inclusion is less supported by established interaction databases. hu.MAP independently places a repeated six-protein subset consisting of HP, SERPINA3, A2M, C3, APOA1, and TF within several related extracellular or plasma-protein complexes (hu.MAP huMAP3_08395.1) through (hu.MAP huMAP3_09434.1). A smaller complex also contains SERPINA3, C3, and TF (hu.MAP huMAP3_02242.1). Thus, much of the module recapitulates known extracellular protein assemblies, while the co-abundance edges involving COL6A2 and the immunoglobulin genes may represent sample composition or context-dependent association.

**STRING interactions (score >= 0.7)**: 10 of 36 gene pairs: A2M–APOA1 (0.998); A2M–HP (0.997); A2M–SERPINA3 (0.929); A2M–TF (0.82); APOA1–C3 (0.957); APOA1–HP (0.998); APOA1–TF (0.919); C3–HP (0.862); HP–SERPINA3 (0.873); HP–TF (0.805)
**STRING functional enrichment (supplementary, within-query FDR)**: PMID (2018) Differences in the Plasma Proteome of Patients with Hypothyroidism before and after Thyroid Hormone Replacement: A Proteomic Analysis. (FDR = 0.0022, 6 genes); PMID (2022) The Implant Proteome-The Right Surgical Glue to Fix Titanium Implants In Situ. (FDR = 0.0104, 6 genes); PMID (2022) Plasma proteomics reveals an improved cardio-metabolic profile in patients with type 2 diabetes post-liraglutide treatment. (FDR = 0.0104, 6 genes); PMID (2010) Lung cancer serum biomarker discovery using glycoprotein capture and liquid chromatography mass spectrometry. (FDR = 0.0104, 6 genes); PMID (2021) The Utility of Differential Scanning Calorimetry Curves of Blood Plasma for Diagnosis, Subtype Differentiation and Predicted Survival in Lung Cancer. (FDR = 0.0136, 5 genes); PMID (2018) Homocysteine, folate, hs-C-reactive protein, tumor necrosis factor alpha and inflammatory proteins: are these biomarkers related to nutritional status and cardiovascular risk in childhood-onset systemic lupus erythematosus? (FDR = 0.0136, 5 genes); PMID (2024) Plasma Proteomic Signature of Endometrial Cancer in Patients with Diabetes. (FDR = 0.014, 5 genes); PMID (2022) N-Glycan and Glycopeptide Serum Biomarkers in Philippine Lung Cancer Patients Identified Using Liquid Chromatography-Tandem Mass Spectrometry. (FDR = 0.014, 5 genes); PMID (2018) Circulating MicroRNA Expression Levels Associated With Internet Gaming Disorder. (FDR = 0.014, 5 genes); PMID (2018) Proteomic fingerprinting in HIVHCV co-infection reveals serum biomarkers for the diagnosis of fibrosis staging. (FDR = 0.014, 5 genes); PMID (2017) Intermediate and low abundant protein analysis of vitamin D deficient obese and non-obese subjects by MALDI-profiling. (FDR = 0.014, 5 genes); PMID (2010) Critical evaluation of gamma-irradiated serum used as feeder in the culture and demonstration of putative nanobacteria and calcifying nanoparticles. (FDR = 0.014, 5 genes); PMID (2022) Translational Proteomic Approach for Cholangiocarcinoma Biomarker Discovery, Validation, and Multiplex Assay Development: A Pilot Study. (FDR = 0.0147, 5 genes); PMID (2016) Annexin-A1 and caldesmon are associated with resistance to tamoxifen in estrogen receptor positive recurrent breast cancer. (FDR = 0.0147, 5 genes); PMID (2023) Quantitative proteomic analysis of human serum using tandem mass tags to predict cardiovascular risks in patients with psoriasis. (FDR = 0.0172, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08395.1 (HP, SERPINA3, A2M, C3, APOA1, TF; 6/43); huMAP3_09531.1 (HP, SERPINA3, A2M, C3, APOA1, TF; 6/47); huMAP3_10101.1 (HP, SERPINA3, A2M, C3, APOA1, TF; 6/49); huMAP3_15040.1 (HP, SERPINA3, A2M, C3, APOA1, TF; 6/64); huMAP3_10678.1 (HP, SERPINA3, A2M, C3, APOA1, TF; 6/71); huMAP3_07432.1 (HP, SERPINA3, C3, APOA1, TF; 5/18); huMAP3_07265.1 (HP, SERPINA3, A2M, APOA1, TF; 5/20); huMAP3_08224.1 (HP, SERPINA3, C3, APOA1, TF; 5/21); huMAP3_09434.1 (HP, SERPINA3, C3, APOA1, TF; 5/33); huMAP3_02242.1 (SERPINA3, C3, TF; 3/9)

### Novelty

This should not be claimed as a wholly new molecular complex or pathway. Most of the central module is already represented by STRING associations and recurring hu.MAP complexes (hu.MAP huMAP3_08395.1) through (hu.MAP huMAP3_02242.1), and the same proteins repeatedly occur in plasma and serum proteomics studies (STRING PMID (2018) Differences in the Plasma Proteome of Patients with Hypothyroidism before and after Thyroid Hormone Replacement: A Proteomic Analysis.; within-query FDR = 0.0022) through (STRING PMID (2023) Quantitative proteomic analysis of human serum using tandem mass tags to predict cardiovascular risks in patients with psoriasis.; within-query FDR = 0.0172). The potentially novel aspect is the conserved co-abundance observation across breast and cerebrospinal fluid, particularly the joint behavior of the known plasma-protein backbone with COL6A2 and immunoglobulin genes. However, database representation cannot establish whether this cross-tissue conservation is biologically new, because it may arise from shared circulating proteins, blood contamination, common immune or vascular components, or technical effects. Novelty would require independent replication, careful control of blood-derived material, and comparison with previously published cross-tissue co-abundance modules.

**Hypothesis.** Hypothesis: the module represents a circulating extracellular surveillance and repair milieu shared between breast samples and cerebrospinal-fluid samples. In this model, APOA1 transports lipid and may modulate inflammatory signaling; C3 provides complement surveillance; A2M and SERPINA3 constrain proteases and inflammatory mediators; HP manages free hemoglobin and oxidative stress; and TF controls extracellular iron availability. COL6A2 may connect this plasma-like environment to stromal or vascular extracellular matrix, while IGHG1 and IGKC reflect a local or contaminating immunoglobulin contribution. This is a mechanistic hypothesis, not a demonstrated tissue-specific mechanism. Testing it would require orthogonal measurement of plasma contamination, cell-type deconvolution, targeted protein assays, and examination of whether the module persists after adjustment for vascular, immune, and liver-derived signals.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): A2M (0.82), COL6A2 (0.81), APOA1 (0.80); STRING partners: APOA1 (0.957), HP (0.862)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_08224.1, huMAP3_09434.1, huMAP3_02242.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a central complement component with established roles in complement activation, inflammatory signaling, proteolysis, and antimicrobial defense. It occupies a connecting position with A2M, APOA1, and COL6A2 in the module, participates in numerous hu.MAP complexes (hu.MAP huMAP3_08395.1) through (hu.MAP huMAP3_07432.1) and (hu.MAP huMAP3_08224.1) through (hu.MAP huMAP3_02242.1), and has strong STRING support with APOA1 and HP. Its disease associations include complement deficiency, complement-mediated kidney disease, atypical hemolytic-uremic syndrome, and age-related macular degeneration. The literature on C3 is extensive.
- **Conclusion**: Established conclusion: C3 is a biologically informative indicator of complement and inflammatory extracellular biology in this module. Hypothesis: its co-abundance with lipid transport and protease-control proteins may report coordinated regulation of circulating innate immune surveillance rather than a breast-specific complement program.

#### APOA1

- **Related proteins** (co-abundance neighbors): COL6A2 (0.86), C3 (0.80); STRING partners: A2M (0.998), C3 (0.957), HP (0.998), TF (0.919)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_08224.1, huMAP3_09434.1
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is the major HDL protein and mediates cholesterol efflux and lecithin-cholesterol acyltransferase activity. It is liver-enriched, secreted to blood, and connected in the module to C3 and COL6A2. It has strong STRING relationships with A2M, HP, C3, and TF and occurs in most of the recurring hu.MAP complexes (hu.MAP huMAP3_08395.1) through (hu.MAP huMAP3_09434.1). Its disease associations include hypoalphalipoproteinemia and APOA1 deficiency, and its literature is substantial.
- **Conclusion**: Established conclusion: APOA1 strongly supports a circulating lipoprotein component and argues against interpreting the module as a purely local tissue pathway. Hypothesis: APOA1 may provide a lipid-handling interface through which complement and inflammatory proteins become co-abundant.

#### A2M

- **Related proteins** (co-abundance neighbors): C3 (0.82); STRING partners: APOA1 (0.998), HP (0.997), SERPINA3 (0.929), TF (0.82)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07265.1
- **Function (MyGene.info)**: alpha-2-macroglobulin. The protein encoded by this gene is a protease inhibitor and cytokine transporter. It uses a bait-and-trap mechanism to inhibit a broad spectrum of proteases, including trypsin, thrombin and collagenase. It can also inhibit inflammatory cytokines, and it thus disrupts inflammatory cascades. Mutations in this gene are a cause of alpha-2-macroglobulin deficiency. This gene is implicated in Alzheimer…
- **Diseases (Open Targets)**: myopia (0.206); refractive error (0.151); primary angle-closure glaucoma (0.148); Abnormality of refraction (0.144); Aganglionic megacolon (0.118)
- **Europe PMC papers**: 5133
- **Why important**: A2M is a broad-spectrum protease inhibitor and cytokine transporter that can modulate inflammatory cascades and complement-related processes. It is secreted to blood, associated with hepatocytes and fibroblasts, and has multiple STRING relationships with the core plasma proteins. It appears in several hu.MAP complexes (hu.MAP huMAP3_08395.1) through (hu.MAP huMAP3_10678.1) and (hu.MAP huMAP3_07265.1). Its reported associations include A2M deficiency and Alzheimer's disease, and it has a substantial literature base.
- **Conclusion**: Established conclusion: A2M is a plausible regulatory component linking protease control, cytokine handling, and complement-associated extracellular biology. Hypothesis: A2M may buffer proteolytic and inflammatory activity in the shared extracellular environment and thereby help generate the observed co-abundance pattern.

#### TF

- **Related proteins** (co-abundance neighbors): COL6A2 (0.88), IGHG1 (0.84), HP (0.81); STRING partners: A2M (0.82), APOA1 (0.919), HP (0.805)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_08224.1, huMAP3_09434.1, huMAP3_02242.1
- **Function (MyGene.info)**: transferrin. This gene encodes a glycoprotein with an approximate molecular weight of 76.5 kDa. It is thought to have been created as a result of an ancient gene duplication event that led to generation of homologous C and N-terminal domains each of which binds one ion of ferric iron. The function of this protein is to transport iron from the intestine, reticuloendothelial system, and liver parenchymal cells t…
- **Diseases (Open Targets)**: atransferrinemia (0.776); alcohol drinking (0.492); hemochromatosis type 1 (0.471); neurodegenerative disease (0.400); urolithiasis (0.329)
- **Europe PMC papers**: 143656
- **Why important**: TF encodes transferrin, the principal extracellular iron-transport protein in this module. It is liver-enriched and secreted to blood, connects to COL6A2, IGHG1, and HP in the co-abundance graph, and has STRING links to A2M, APOA1, and HP. It is present across the hu.MAP complexes (hu.MAP huMAP3_08395.1) through (hu.MAP huMAP3_02242.1). Its established biology includes iron transport, intracellular iron homeostasis, and antibacterial humoral defense; disease associations include atransferrinemia and hemochromatosis. TF has a very extensive literature.
- **Conclusion**: Established conclusion: TF identifies an extracellular iron-transport and host-defense dimension within the module. Hypothesis: coordinated TF and HP abundance may reflect regulation of iron and hemoglobin-related oxidative stress in blood-derived material rather than a specialized cerebrospinal-fluid process.

#### COL6A2

- **Related proteins** (co-abundance neighbors): TF (0.88), APOA1 (0.86), SERPINA3 (0.85), IGKC (0.84), C3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 2 chain. This gene encodes one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The product of this gene contains several domains similar to von Willebrand Factor type A domains. These domains have been shown to bind extracellular matrix proteins, an interaction that explains the importance of this collagen in organizing matrix components. Mutation…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy 1B (0.770); Bethlem myopathy (0.755); Ullrich congenital muscular dystrophy (0.743); Bethlem myopathy 1B (0.723); Bethlem myopathy 1A (0.713)
- **Europe PMC papers**: 4115
- **Why important**: COL6A2 is the module's strongest co-abundance connector and encodes a collagen type VI chain involved in extracellular-matrix organization. HPA links it to fibroblasts, stromal populations, and hepatic stellate cells, and it is detected in breast tissue. It has no listed STRING partners or hu.MAP complex membership, making it a potentially informative bridge between the established plasma-protein backbone and matrix biology. Its disease associations include Bethlem myopathy and Ullrich congenital muscular dystrophy, and its literature is substantial.
- **Conclusion**: Established conclusion: COL6A2 contributes an extracellular-matrix and stromal interpretation that is distinct from the circulating-protein core. Hypothesis: COL6A2 may reflect vascular or stromal material shared by the sample types, or a context-dependent association with plasma proteins; this relationship requires direct experimental validation.

#### HP

- **Related proteins** (co-abundance neighbors): TF (0.81); STRING partners: A2M (0.997), APOA1 (0.998), C3 (0.862), SERPINA3 (0.873), TF (0.805)
- **HPA**: Tissue enriched; Cell type enriched; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_08224.1, huMAP3_09434.1
- **Function (MyGene.info)**: haptoglobin. This gene encodes a preproprotein, which is processed to yield both alpha and beta chains, which subsequently combine as a tetramer to produce haptoglobin. Haptoglobin functions to bind free plasma hemoglobin, which allows degradative enzymes to gain access to the hemoglobin, while at the same time preventing loss of iron through the kidneys and protecting the kidneys from damage by hemoglobin. Mu…
- **Diseases (Open Targets)**: Hypercholesterolemia (0.581); coronary artery disorder (0.572); metabolic disease (0.571); hyperlipidemia (0.567); metabolic syndrome (0.516)
- **Europe PMC papers**: 125817
- **Why important**: HP encodes haptoglobin, which binds free hemoglobin, limits iron loss, and protects tissues from hemoglobin-associated damage. It is liver-enriched, secreted to blood, and associated with monocytes and eosinophils. HP has strong STRING relationships with A2M, APOA1, C3, SERPINA3, and TF and appears in the recurring hu.MAP complexes (hu.MAP huMAP3_08395.1) through (hu.MAP huMAP3_09434.1). Its disease associations include hypercholesterolemia, coronary artery disease, and metabolic disease, and its literature is extensive.
- **Conclusion**: Established conclusion: HP reinforces the interpretation of the module as a plasma-associated defense and oxidative-stress signature. Hypothesis: HP may cooperate with TF, A2M, and C3 to coordinate extracellular handling of hemoglobin, iron, proteases, and inflammatory signals.

## Module 2

**Tissue pair**: breast and cerebrospinal_fluid  
**Genes (28)**: ADAM10, APLP1, SMPDL3B, BCAM, CD109, CHST3, CPVL, ECE1, ECM2, ENPP5, ERAP2, HEG1, HSPA13, HYOU1, ITGB2, LGALS3BP, LY75, MBP, PDGFRL, PLOD2, ACP2, PRSS23, FAP, SHBG, SIAE, SORL1, SUMF1, AXL

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent, so the module should not be assigned a statistically established pathway label. The gene annotations and network nevertheless suggest a mixed extracellular-interface and cellular-trafficking program. ECM2, FAP, PRSS23, PDGFRL, PLOD2, CHST3, BCAM and CD109 point toward extracellular matrix organization, matrix modification, adhesion and proteolytic processing. ADAM10, ECE1 and CPVL add protease or peptidase-related functions, while SUMF1, ACP2, SMPDL3B and SIAE indicate lysosomal, sulfation or membrane-lipid processing. ERAP2, ITGB2, AXL, LY75 and LGALS3BP provide an immune and endocytic component. MBP and APLP1 provide a nervous-system or myelin-associated component. Thus, the most defensible interpretation is a cross-tissue extracellular-matrix, cell-surface, vesicular and immune-interface module rather than a single canonical pathway.

**Cell composition.** The module is compositionally heterogeneous. Many members are secreted, extracellular, membrane-associated or secreted to blood, including ECM2, FAP, PDGFRL, PRSS23, ERAP2, SORL1, SHBG and LGALS3BP. HPA also shows frequent enhancement in neutrophils, plasma cells, macrophages, monocytes and other immune-related cell types, with immune enhancement for several genes. This raises the possibility that the shared breast and cerebrospinal-fluid signal reflects blood-derived material, vascular or stromal cells, immune-cell admixture, or shared extracellular proteins rather than a uniform resident program. The module is not purely blood-derived: HPA also supports brain, choroid-plexus, ependymal, oligodendrocyte and glial associations, as well as fibroblast and epithelial associations. Breast protein detection is present for several members, whereas there is no matching HPA cerebrospinal-fluid tissue category, so the apparent cross-tissue conservation should not be interpreted as direct protein detection in cerebrospinal fluid.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no STRING high-confidence pairwise interactions among the module genes and no STRING functional-enrichment result. This means the abundance correlations are not recapitulated by the examined STRING interaction layer and should not be treated as a known physical interaction network. hu.MAP provides partial, uneven support. ADAM10, ECE1, SUMF1 and HYOU1 co-occur in hu.MAP complexes C1 and C2, with CD109 also present in C1. BCAM and CHST3 co-occur in C3 and C4, while PRSS23 and PDGFRL co-occur in C5. These complexes provide evidence for selected local biochemical or cellular assemblies, but the partial membership and differing confidence levels do not establish one unified complex for the whole module. The data therefore support several known molecular neighborhoods embedded within a broader co-abundance structure.

**STRING interactions (score >= 0.7)**: 0 of 378 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09327.1 (ADAM10, ECE1, CD109, SUMF1, HYOU1; 5/93); huMAP3_06775.1 (ADAM10, ECE1, SUMF1, HYOU1; 4/60); huMAP3_04786.1 (BCAM, CHST3; 2/9); huMAP3_07949.1 (BCAM, CHST3; 2/12); huMAP3_13422.1 (PRSS23, PDGFRL; 2/20)

### Novelty

The module may represent a novel cross-tissue co-abundance pattern, but novelty is not established by the absence of STRING edges or by the absence of a single hu.MAP complex. Its potentially new aspect is the coordinated association of extracellular matrix and stromal proteins, immune or endocytic proteins, stress and processing proteins, and brain-associated proteins across breast and cerebrospinal-fluid samples. The lack of globally significant GO or KEGG enrichment makes a pathway-level novelty claim weak, while the absence of STRING enrichment argues against a broadly recognized interaction-defined module. A stronger novelty claim would require comparison with published breast and cerebrospinal-fluid co-abundance modules, independent cohorts, preservation testing, and adjustment for blood contamination, cell composition and sample handling.

**Hypothesis.** Hypothesis: the module reflects a shared extracellular-interface and tissue-fluid response involving stromal or matrix-producing cells, vascular or epithelial surfaces, and variable myeloid or lymphoid admixture. In this model, extracellular matrix components and modifiers such as ECM2, FAP, PLOD2, PRSS23 and CHST3 are co-abundant with cell-surface and trafficking regulators such as ADAM10, AXL, ITGB2 and LY75. ERAP2, CPVL, SMPDL3B and SIAE could reflect immune-cell or vesicular processing, while HYOU1 and HSPA13 could reflect secretory or endoplasmic-reticulum stress. MBP and APLP1 may indicate a neural or myelin-related contribution in cerebrospinal-fluid-associated material, but they could also mark sample composition rather than a mechanistically coupled pathway. This hypothesis should be tested by cell-deconvolution, blood-contamination markers, targeted protein measurements, and replication in independent breast and cerebrospinal-fluid cohorts.

### Important genes

#### ECM2

- **Related proteins** (co-abundance neighbors): LY75 (0.94), PRSS23 (0.91), HSPA13 (0.88), FAP (0.87), ECE1 (0.87), CPVL (0.87), ACP2 (0.86), SUMF1 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoli fibrillar center, Endoplasmic reticulum; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: extracellular matrix protein 2. ECM2 encodes extracellular matrix protein 2, so named because it shares extensive similarity with known extracelluar matrix proteins. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2010].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.425); jaw disease (0.166); central nervous system cancer (0.077); glioma (0.073); neoplasm (0.042)
- **Europe PMC papers**: 850
- **Why important**: ECM2 has a prominent position in the co-abundance graph and connects matrix-associated, proteolytic, stress-related and lysosomal-processing genes. HPA describes it as an extracellular-matrix secreted protein with adipose, glial and ependymal cell associations and breast detection. Its annotation supports cell-matrix adhesion and extracellular-matrix organization, making it a plausible structural anchor for the module. Its literature volume is substantial.
- **Conclusion**: Established evidence supports ECM2 as a matrix-associated secreted protein linked to adhesion and extracellular-matrix organization, with strong module connectivity. It is a credible structural marker of the module. It is not established that ECM2 causally organizes the entire cross-tissue module; that role remains a hypothesis.

#### ADAM10

- **Related proteins** (co-abundance neighbors): ENPP5 (0.88), HEG1 (0.84), MBP (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_09327.1, huMAP3_06775.1
- **Function (MyGene.info)**: ADAM metallopeptidase domain 10. Members of the ADAM family are cell surface proteins with a unique structure possessing both potential adhesion and protease domains. This gene encodes and ADAM family member that cleaves many proteins including TNF-alpha and E-cadherin. Alternate splicing results in multiple transcript variants encoding different proteins that may undergo similar processing. [provided by RefSeq, Feb 2016].
- **Diseases (Open Targets)**: reticulate acropigmentation of Kitamura (0.679); Alzheimer disease 18 (0.621); Alzheimer disease (0.522); dementia (0.415); schizophrenia (0.354)
- **Europe PMC papers**: 11139
- **Why important**: ADAM10 is connected to ENPP5, HEG1 and MBP and is present in hu.MAP complexes C1 and C2. It is a cell-surface protease that cleaves TNF-alpha and E-cadherin and participates in ectodomain proteolysis and Notch signaling. HPA shows vesicular and plasma-membrane localization, neutrophil enhancement and breast detection. Its large literature base and disease associations make it an important mechanistic candidate.
- **Conclusion**: Established evidence supports ADAM10 as a membrane protease and as a member of selected hu.MAP assemblies. It could link cell adhesion, receptor processing and inflammatory signaling in this module. A causal role in the breast–cerebrospinal-fluid co-abundance pattern is not demonstrated.

#### PLOD2

- **Related proteins** (co-abundance neighbors): PDGFRL (0.98), ENPP5 (0.89), APLP1 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Not detected in immune cells; location Nucleoli, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: procollagen-lysine,2-oxoglutarate 5-dioxygenase 2. The protein encoded by this gene is a membrane-bound homodimeric enzyme that is localized to the cisternae of the rough endoplasmic reticulum. The enzyme (cofactors iron and ascorbate) catalyzes the hydroxylation of lysyl residues in collagen-like peptides. The resultant hydroxylysyl groups are attachment sites for carbohydrates in collagen and thus are critical for the stability of intermolecular…
- **Diseases (Open Targets)**: Bruck syndrome (0.779); osteogenesis imperfecta (0.572); osteoarthritis (0.552); osteoarthritis, hip (0.531); osteoarthritis, knee (0.472)
- **Europe PMC papers**: 3025
- **Why important**: PLOD2 connects PDGFRL, ENPP5 and APLP1 and is directly annotated for collagen biosynthesis, collagen fibril organization, hypoxia response and protein modification. It encodes an endoplasmic-reticulum collagen-lysine hydroxylase, providing a concrete biochemical bridge between matrix remodeling and cellular stress. Its disease associations include connective-tissue and skeletal disorders, and it has substantial literature support.
- **Conclusion**: Established evidence supports PLOD2 as a collagen-maturation enzyme associated with matrix structure and hypoxia-related biology. Its network position is modest but biologically informative because it connects matrix, secretory and neural-associated signals. It is plausible, but unproven, that PLOD2 marks a shared matrix-remodeling state across the tissues.

#### FAP

- **Related proteins** (co-abundance neighbors): ECM2 (0.87), PDGFRL (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibroblast activation protein alpha. The protein encoded by this gene is a homodimeric integral membrane gelatinase belonging to the serine protease family. It is selectively expressed in reactive stromal fibroblasts of epithelial cancers, granulation tissue of healing wounds, and malignant cells of bone and soft tissue sarcomas. This protein is thought to be involved in the control of fibroblast growth or epithelial-mesenchymal inte…
- **Diseases (Open Targets)**: inflammatory bowel disease (0.311); hypothyroidism (0.306); irritable bowel syndrome (0.290); autoimmune disease (0.288); psoriasis (0.261)
- **Europe PMC papers**: 22775
- **Why important**: FAP connects ECM2 and PDGFRL and is a secreted-to-blood, matrix-associated serine protease enriched in reactive stromal fibroblasts and fibro-adipogenic progenitors. Its annotations include collagen catabolism, endothelial migration and epithelial–mesenchymal interactions. It is detected in breast and has a very large literature base, especially in stromal biology and cancer.
- **Conclusion**: Established evidence supports FAP as a marker and mediator of reactive stromal and extracellular-matrix remodeling states. Its presence strengthens the interpretation that a stromal or fibroblast-related component contributes to the module. It does not prove that the module represents malignant stroma or that FAP drives the shared signal.

#### MBP

- **Related proteins** (co-abundance neighbors): CPVL (0.82), ADAM10 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myelin basic protein. The protein encoded by the classic MBP gene is a major constituent of the myelin sheath of oligodendrocytes and Schwann cells in the nervous system. However, MBP-related transcripts are also present in the bone marrow and the immune system. These mRNAs arise from the long MBP gene (otherwise called 'Golli-MBP') that contains 3 additional exons located upstream of the classic MBP exons. Alternative…
- **Diseases (Open Targets)**: alcohol drinking (0.394); preeclampsia (0.273); placenta praevia (0.272); duodenal ulcer (0.270); Abnormality of the dentition (0.269)
- **Europe PMC papers**: 69467
- **Why important**: MBP connects ADAM10 and CPVL and is tissue-enriched in brain, with associations to oligodendrocytes and neutrophils in HPA. It is a major myelin-sheath constituent and is annotated for myelin assembly, axon ensheathment, central nervous-system development and immune response. Its very large literature base makes it the clearest neural-context marker in the module.
- **Conclusion**: Established evidence supports MBP as a myelin-associated neural protein, while the annotation also recognizes immune-related MBP transcripts. Its presence is consistent with a cerebrospinal-fluid or neural contribution, but it may also reflect cellular material or sample composition rather than coordinated matrix biology. A direct functional bridge from MBP to the other module members remains unproven.

#### ERAP2

- **Related proteins** (co-abundance neighbors): HEG1 (0.86), ENPP5 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: endoplasmic reticulum aminopeptidase 2. This gene encodes a zinc metalloaminopeptidase of the M1 protease family that resides in the endoplasmic reticulum and functions in N-terminal trimming antigenic epitopes for presentation by major histocompatibility complex (MHC) class I molecules. Certain mutations in this gene are associated with the inflammatory arthritis syndrome ankylosing spondylitis and pre-eclampsia. This gene is located a…
- **Diseases (Open Targets)**: inflammatory bowel disease (0.321); hypertensive disorder (0.320); Crohn disease (0.294); psoriasis (0.266); pulmonary vascular congestion (0.202)
- **Europe PMC papers**: 1422
- **Why important**: ERAP2 connects ENPP5 and HEG1 and is tissue-enhanced in lymphoid tissue, with B-cell, plasma-cell and T-cell associations. It is an endoplasmic-reticulum aminopeptidase involved in trimming antigenic peptides for MHC class I presentation and has established inflammatory disease associations. Its position links the module to immune and secretory processing despite the absence of STRING support.
- **Conclusion**: Established evidence supports ERAP2 as an antigen-processing aminopeptidase associated with lymphoid biology and inflammatory disease. It is a strong indicator that immune-cell composition or immune-secretory activity may contribute to the shared module. It is not established that ERAP2 mechanistically coordinates the extracellular-matrix component.

## Module 3

**Tissue pair**: breast and cerebrospinal_fluid  
**Genes (17)**: ADA2, CPD, CNTN1, C16orf89, CXADR, EFNB2, EPHB2, EPHB3, FAT2, FUCA2, GOLM2, SERPINA5, LAMA5, NCAM1, PTPRK, SIRPA, SORT1

### Function

No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for this module. Nevertheless, the gene identities and network structure support a cell-surface adhesion and receptor-signaling interpretation. EPHB2 is the most central node and connects with EFNB2, EPHB3, NCAM1, FAT2, SIRPA, CXADR, SERPINA5, GOLM2 and LAMA5. EFNB2 and the Eph receptors indicate ephrin-mediated bidirectional signaling, while NCAM1, CNTN1, FAT2, CXADR, PTPRK and LAMA5 support cell-cell, cell-matrix or junctional adhesion. SIRPA adds a myeloid and glial receptor-signaling component. Thus, the most defensible functional description is a mixed adhesion, developmental guidance and membrane-signaling module rather than a demonstrated canonical pathway.

**Cell composition.** This is not a simple housekeeping module. HPA annotations indicate substantial tissue and cell-type specificity, with brain, astrocyte and neuronal signals prominent, alongside epithelial, skin and breast-associated signals. The module also contains several proteins secreted to blood or extracellular matrix, including C16orf89, FUCA2, SERPINA5, LAMA5, ADA2 and NCAM1 in other tissues; therefore, extracellular or circulating protein abundance could contribute to the cross-tissue association. Immune influence is plausible but not dominant: several genes are not detected in immune cells, whereas SIRPA, SORT1, CPD, ADA2 and other members show monocyte, neutrophil or related blood-cell associations. The presence of secreted proteins and blood-cell-associated genes means that sample composition, vascular interfaces or shared extracellular material should be considered as possible contributors. HPA protein detection is reported for part of the module in breast, while the fact sheet provides no matching HPA tissue assessment for cerebrospinal fluid.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides direct high-confidence support for the EFNB2–EPHB2 and EFNB2–EPHB3 relationships. These are biologically coherent ligand-receptor relationships and anchor the strongest mechanistic interpretation of the module. No STRING functional-enrichment result was available, and most module pairs lack high-confidence STRING support, so the full co-abundance network should not be treated as a validated physical interaction network. hu.MAP independently places EFNB2 and EPHB3 together across several complexes, often with SDC3 and sometimes with RADIL, EPHA5, EFNB1, PHLPP1, DIP2 proteins or FAM171A2. hu.MAP also places CXADR with CNTN1 and NCAM1 with CNTN1 in separate complexes containing neuronal, adhesion and signaling proteins. These complexes provide partial support for membrane-adhesion and neuronal-interface biology, but the repeated membership of only a small subset of module genes means they do not validate the entire module as one physical complex.

**STRING interactions (score >= 0.7)**: 2 of 136 gene pairs: EFNB2–EPHB2 (0.999); EFNB2–EPHB3 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00414.1 (EFNB2, EPHB3; 2/3); huMAP3_03778.1 (EFNB2, EPHB3; 2/4); huMAP3_06853.1 (EFNB2, EPHB3; 2/6); huMAP3_11078.1 (EFNB2, EPHB3; 2/6); huMAP3_08098.1 (EFNB2, EPHB3; 2/7); huMAP3_10509.1 (EFNB2, EPHB3; 2/9); huMAP3_15011.1 (EFNB2, EPHB3; 2/10); huMAP3_12658.1 (CXADR, CNTN1; 2/32); huMAP3_11626.1 (NCAM1, CNTN1; 2/42)

### Novelty

The module-level finding may be a new cross-tissue co-abundance observation, but novelty cannot be established from the fact sheet alone. The direct EFNB2–EPHB2 and EFNB2–EPHB3 relationships are already known, and the EFNB2–EPHB3 combination is represented repeatedly in hu.MAP, so the central receptor-ligand biology is not new. Conversely, the broader co-abundance grouping includes many genes without corresponding STRING or hu.MAP support. That lack of prior database support is compatible with a novel tissue-specific or sample-composition pattern, but it is not proof of novelty. A stronger novelty claim would require comparison with published breast and cerebrospinal-fluid proteomic modules and independent replication.

**Hypothesis.** Hypothesis: the shared module reflects coordinated abundance of an Ephrin-B-centered cell-contact program at epithelial, vascular, glial or neuronal interfaces, with EPHB2 and EPHB3 receiving signals from EFNB2 and interacting functionally with adhesion receptors and extracellular-matrix components. NCAM1, CNTN1, CXADR, FAT2, PTPRK and LAMA5 could represent neighboring adhesion or junctional contexts, while SIRPA, ADA2, CPD and SORT1 could reflect glial, myeloid or vesicular contributions. In breast, this may reflect epithelial or stromal membrane organization; in cerebrospinal fluid, it may reflect neural or glial membrane shedding, extracellular vesicles, or shared interface material. The circulating and immune-associated annotations also make blood contamination or vascular-cell contribution an alternative explanation that should be tested rather than assumed away.

### Important genes

#### EPHB2

- **Related proteins** (co-abundance neighbors): NCAM1 (0.98), FAT2 (0.96), SIRPA (0.92), EFNB2 (0.90), CXADR (0.88), SERPINA5 (0.87), GOLM2 (0.86), LAMA5 (0.85), CPD (0.85), SORT1 (0.84); STRING partners: EFNB2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EPH receptor B2. This gene encodes a member of the Eph receptor family of receptor tyrosine kinase transmembrane glycoproteins. These receptors are composed of an N-terminal glycosylated ligand-binding domain, a transmembrane region and an intracellular kinase domain. They bind ligands called ephrins and are involved in diverse cellular processes including motility, division, and differentiation. A distinguishing …
- **Diseases (Open Targets)**: medullary thyroid gland carcinoma (0.542); Familial prostate cancer (0.477); Rare hemorrhagic disorder due to a constitutional platelet anomaly (0.450); osteoarthritis, hip (0.404); neoplasm (0.398)
- **Europe PMC papers**: 4927
- **Why important**: EPHB2 is the central network node by weighted connectivity and links the module's adhesion, receptor and extracellular components. It has a plasma-membrane receptor-tyrosine-kinase architecture and established roles in cell motility, division, differentiation, angiogenesis, cell adhesion and nervous-system development. Its direct STRING relationship with EFNB2 is exceptionally strong within the supplied evidence, and it has a substantial literature base and multiple disease associations.
- **Conclusion**: Established evidence supports EPHB2 as the principal signaling hub and a plausible driver of the module's adhesion and developmental interpretation. It is not established that EPHB2 causes the shared breast–cerebrospinal-fluid abundance pattern; that causal role remains a hypothesis.

#### EFNB2

- **Related proteins** (co-abundance neighbors): EPHB2 (0.90), EPHB3 (0.89), FUCA2 (0.89), SIRPA (0.88), PTPRK (0.88), SORT1 (0.85), CXADR (0.81); STRING partners: EPHB2 (0.999), EPHB3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_00414.1, huMAP3_03778.1, huMAP3_06853.1, huMAP3_11078.1, huMAP3_08098.1, huMAP3_10509.1, huMAP3_15011.1
- **Function (MyGene.info)**: ephrin B2. This gene encodes a member of the ephrin (EPH) family. The ephrins and EPH-related receptors comprise the largest subfamily of receptor protein-tyrosine kinases and have been implicated in mediating developmental events, especially in the nervous system and in erythropoiesis. Based on their structures and sequence relationships, ephrins are divided into the ephrin-A (EFNA) class, which are anchore…
- **Diseases (Open Targets)**: ovarian neoplasm (0.357); arthropathy (0.317); Cerebral degeneration (0.315); open-angle glaucoma (0.311); chronic laryngitis (0.304)
- **Europe PMC papers**: 2702
- **Why important**: EFNB2 is the principal ligand-side partner for both EPHB2 and EPHB3 in STRING and is the most repeatedly represented module member in the hu.MAP complexes. Its documented functions include cell adhesion, axon guidance, angiogenesis, cell migration and morphogenesis. Its network position connects receptor signaling to SIRPA, PTPRK, CXADR, SORT1 and extracellular or metabolic proteins.
- **Conclusion**: Established evidence identifies EFNB2 as the strongest molecular anchor for an Ephrin-B adhesion-signaling interpretation. The hypothesis that it coordinates the entire module across breast and cerebrospinal fluid is plausible but unproven.

#### EPHB3

- **Related proteins** (co-abundance neighbors): EFNB2 (0.89), SIRPA (0.85); STRING partners: EFNB2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_00414.1, huMAP3_03778.1, huMAP3_06853.1, huMAP3_11078.1, huMAP3_08098.1, huMAP3_10509.1, huMAP3_15011.1
- **Function (MyGene.info)**: EPH receptor B3. Ephrin receptors and their ligands, the ephrins, mediate numerous developmental processes, particularly in the nervous system. Based on their structures and sequence relationships, ephrins are divided into the ephrin-A (EFNA) class, which are anchored to the membrane by a glycosylphosphatidylinositol linkage, and the ephrin-B (EFNB) class, which are transmembrane proteins. The Eph family of recept…
- **Diseases (Open Targets)**: medullary thyroid gland carcinoma (0.543); alcohol drinking (0.421); non-small cell lung carcinoma (0.389); neoplasm (0.386); thyroid tumor (0.373)
- **Europe PMC papers**: 1880
- **Why important**: EPHB3 forms the second direct STRING relationship with EFNB2 and occurs with EFNB2 across several hu.MAP complexes, including complexes containing adhesion-associated and signaling proteins. Its known functions include axon guidance, axonal fasciculation, angiogenesis, cell migration and receptor-tyrosine-kinase signaling. HPA also links it to breast secretory cells and several epithelial cell types.
- **Conclusion**: Established evidence supports EPHB3 as a corroborating Ephrin-B receptor and as a bridge between epithelial and neural interpretations. Its specific contribution to the observed co-abundance module, beyond shared expression or cellular composition, remains unresolved.

#### NCAM1

- **Related proteins** (co-abundance neighbors): EPHB2 (0.98), GOLM2 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11626.1
- **Function (MyGene.info)**: neural cell adhesion molecule 1. This gene encodes a cell adhesion protein which is a member of the immunoglobulin superfamily. The encoded protein is involved in cell-to-cell interactions as well as cell-matrix interactions during development and differentiation. The encoded protein plays a role in the development of the nervous system by regulating neurogenesis, neurite outgrowth, and cell migration. This protein is also involv…
- **Diseases (Open Targets)**: major depressive disorder (0.532); smoking initiation (0.501); gastroesophageal reflux disease (0.498); schizophrenia (0.463); irritable bowel syndrome (0.462)
- **Europe PMC papers**: 6731
- **Why important**: NCAM1 provides a strong neural and cell-adhesion interpretation despite having fewer module connections. It is enriched in brain-related tissues and neuronal or glial cell types, is a plasma-membrane adhesion protein, and is associated with neurogenesis, neurite outgrowth, cell migration and lymphocyte biology. It also appears with CNTN1 in a hu.MAP complex containing numerous neuronal synaptic and cytoskeletal proteins.
- **Conclusion**: Established evidence supports NCAM1 as a neural or glial adhesion component and makes it particularly relevant to the cerebrospinal-fluid side of the shared module. Its presence does not prove that the module is neuron-derived, because extracellular material and cell composition could produce the association.

#### SIRPA

- **Related proteins** (co-abundance neighbors): EPHB2 (0.92), EFNB2 (0.88), CNTN1 (0.87), EPHB3 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal regulatory protein alpha. The protein encoded by this gene is a member of the signal-regulatory-protein (SIRP) family, and also belongs to the immunoglobulin superfamily. SIRP family members are receptor-type transmembrane glycoproteins known to be involved in the negative regulation of receptor tyrosine kinase-coupled signaling processes. This protein can be phosphorylated by tyrosine kinases. The phospho-tyrosine residue…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.376); thrombocytopenia 4 (0.364); neurodegenerative disease (0.361); hemorrhagic disease (0.351); diabetes mellitus (0.324)
- **Europe PMC papers**: 3860
- **Why important**: SIRPA occupies an intermediate network position connecting EPHB2 and EFNB2 to CNTN1 and EPHB3. It is brain-enhanced and associated with astrocytes, macrophages, monocytes and other myeloid populations. Its established receptor biology includes negative regulation of receptor-tyrosine-kinase-linked signaling, cell adhesion, migration and regulation of inflammatory mediators. It therefore links the neural adhesion interpretation to glial and myeloid biology.
- **Conclusion**: Established evidence supports SIRPA as a plausible glial or myeloid interface component and a potential regulator of receptor signaling. Whether it represents genuine biology shared between the tissues or variation in immune and vascular content is a hypothesis requiring cell-composition controls.

#### CNTN1

- **Related proteins** (co-abundance neighbors): SIRPA (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12658.1, huMAP3_11626.1
- **Function (MyGene.info)**: contactin 1. The protein encoded by this gene is a member of the immunoglobulin superfamily. It is a glycosylphosphatidylinositol (GPI)-anchored neuronal membrane protein that functions as a cell adhesion molecule. It may play a role in the formation of axon connections in the developing nervous system. Multiple alternatively spliced transcript variants encoding different isoforms have been found for this gene…
- **Diseases (Open Targets)**: Compton-North congenital myopathy (0.709); Parkinson disease (0.393); urinary system disorder (0.307); exostosis (0.266); escherichia coli infection (0.263)
- **Europe PMC papers**: 1740
- **Why important**: CNTN1 is a GPI-anchored neuronal adhesion molecule with brain-enhanced expression and associations with astrocytes and multiple neuronal cell types. It connects SIRPA in the module and appears in hu.MAP complexes with CXADR and NCAM1. Its documented functions include axon guidance, brain development, central nervous-system myelination and cell adhesion, giving it strong relevance to the neural-interface interpretation.
- **Conclusion**: Established evidence supports CNTN1 as a neural adhesion marker that reinforces the cerebrospinal-fluid and glial interpretation. Its limited network connectivity and lack of direct STRING support mean it should be viewed as contextual evidence rather than proof of a unified physical complex.

## Module 4

**Tissue pair**: breast and cerebrospinal_fluid  
**Genes (21)**: ALDOC, AMBP, C1QC, CP, COL1A1, COL1A2, C4A, COL6A1, COL6A3, CRTAC1, FGA, LAMB2, LAMC1, LGALS1, MCAM, NFASC, HSPG2, PLTP, PRG4, SELENBP1, CLEC3B

### Function

The strongest supported function is extracellular-matrix receptor interaction, based on (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0361), which includes collagen type I, collagen type VI, laminin, and perlecan components. The module therefore most plausibly represents extracellular-matrix organization, basement-membrane structure, and cell–matrix adhesion, with potential relevance to vascular and stromal interfaces. The collagen and laminin genes provide a coherent structural core, while HSPG2 can cross-link extracellular-matrix components and cell-surface molecules. Additional genes suggest associated complement, coagulation, lipid-transport, iron-handling, and neural-adhesion biology, but these are secondary interpretations because they do not have globally corrected GO/KEGG support. The module is not a generic single pathway: it appears to combine a structural extracellular-matrix signal with circulating and tissue-interface proteins.

**Cell composition.** This module is dominated by secreted or extracellular-matrix proteins. HPA classifies most genes as secreted, and many are enhanced in fibroblasts, hepatic stellate cells, pericytes, blood vessels, adipose tissue, or liver. This favors a stromal, vascular, basement-membrane, or tissue-interface interpretation rather than a neuronal-only interpretation. Several genes are liver-enriched plasma proteins, including FGA, AMBP, CP, and C4A, so some co-abundance may reflect circulating protein carryover or vascular exposure in the samples. C1QC and a small subset of other genes have immune or blood-cell associations, but most genes are not detected in immune cells; the module is therefore not primarily a blood-cell program. HPA protein detection in breast is incomplete, and there is no matching HPA tissue category for cerebrospinal fluid, so the shared signal should not be treated as proof that all components are produced locally in both tissues.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG ECM-receptor interaction - Homo sapiens (human) | 0.0361 | COL1A1, COL1A2, COL6A1, COL6A3, HSPG2, LAMB2, LAMC1 |

### STRING and hu.MAP

STRING supports a known extracellular-matrix subnetwork involving COL1A1, COL1A2, COL6A1, COL6A3, LAMC1, LAMB2, and HSPG2. The strongest structural relationships are among collagen chains and between laminin components, with additional links between collagen and laminin or perlecan. STRING also records AMBP–FGA and C1QC–C4A relationships, connecting plasma and complement proteins to the broader module. These relationships indicate that the module contains biologically established protein associations rather than only statistical co-abundance. hu.MAP independently places CP, FGA, and C4A in several broad circulating-protein and complement-associated complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1), and places COL1A1 with COL1A2 in multiple smaller complexes (hu.MAP huMAP3_02141.1) (hu.MAP huMAP3_06460.1) (hu.MAP huMAP3_07562.1) (hu.MAP huMAP3_02069.1) (hu.MAP huMAP3_10780.1) (hu.MAP huMAP3_09231.1) (hu.MAP huMAP3_09523.1) (hu.MAP huMAP3_09606.1) (hu.MAP huMAP3_10652.1) (hu.MAP huMAP3_14070.1). The repeated collagen-pair complexes support a real collagen-related structural component, whereas the broad hu.MAP complexes containing many plasma proteins suggest that some associations may reflect shared extracellular or circulating contexts rather than a single compact molecular complex. hu.MAP does not establish one complete complex containing all module genes.

**STRING interactions (score >= 0.7)**: 12 of 210 gene pairs: AMBP–FGA (0.945); C1QC–C4A (0.972); COL1A1–COL1A2 (0.999); COL1A1–COL6A1 (0.969); COL1A1–COL6A3 (0.974); COL1A1–LAMC1 (0.77); COL1A2–COL6A1 (0.875); COL1A2–COL6A3 (0.968); COL1A2–LAMC1 (0.701); COL6A1–COL6A3 (0.994); HSPG2–LAMC1 (0.82); LAMB2–LAMC1 (0.962)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG ECM-receptor interaction (FDR = 0.0224, 7 genes); KEGG Focal adhesion (FDR = 0.0278, 6 genes); KEGG Human papillomavirus infection (FDR = 0.0278, 6 genes); NetworkNeighborAL Collagen formation, and Protein complex involved in cell adhesion (FDR = 0.0489, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (CP, FGA, C1QC, C4A; 4/64); huMAP3_07432.1 (CP, FGA, C4A; 3/18); huMAP3_08395.1 (CP, FGA, C4A; 3/43); huMAP3_09531.1 (CP, FGA, C4A; 3/47); huMAP3_10101.1 (CP, FGA, C4A; 3/49); huMAP3_10678.1 (CP, FGA, C4A; 3/71); huMAP3_02141.1 (COL1A1, COL1A2; 2/3); huMAP3_06460.1 (COL1A1, COL1A2; 2/3); huMAP3_07562.1 (COL1A1, COL1A2; 2/3); huMAP3_02069.1 (COL1A1, COL1A2; 2/4); huMAP3_10780.1 (COL1A1, COL1A2; 2/5); huMAP3_09231.1 (COL1A1, COL1A2; 2/6); huMAP3_09523.1 (COL1A1, COL1A2; 2/6); huMAP3_09606.1 (COL1A1, COL1A2; 2/6); huMAP3_10652.1 (COL1A1, COL1A2; 2/6); huMAP3_14070.1 (COL1A1, COL1A2; 2/8); huMAP3_02242.1 (FGA, C4A; 2/9); huMAP3_08700.1 (CP, C4A; 2/11); huMAP3_07265.1 (CP, C4A; 2/20); huMAP3_09273.1 (CP, C4A; 2/28)

### Novelty

The module-level finding may be useful and potentially novel as a conserved co-abundance pattern across breast and cerebrospinal fluid, but the available evidence does not justify calling it a wholly new molecular mechanism. Its central collagen, laminin, perlecan, complement, fibrinogen, and plasma-protein relationships are already represented in STRING and hu.MAP, and the ECM-receptor interaction itself is established by (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0361). Absence of some genes from STRING or hu.MAP does not demonstrate novelty, because those resources emphasize known physical or curated associations and may miss tissue-specific co-abundance. The defensible novelty claim is therefore the cross-tissue conservation and the particular combination of extracellular-matrix, vascular, plasma, complement, and neural-interface signals, which should be tested in independent cohorts and with cell-resolved or spatial measurements.

**Hypothesis.** Hypothesis: the conserved module reflects a shared extracellular-interface program in which fibroblast, perivascular, vascular, or related stromal cells produce and organize collagen, laminin, and perlecan-rich matrix, while blood- or liver-derived proteins and complement components enter the same abundance pattern through vascular or fluid exposure. In cerebrospinal fluid, this may represent matrix and barrier-associated material from brain, vascular, choroid-plexus, or meningeal interfaces rather than a free-standing neuronal program. CRTAC1, NFASC, ALDOC, and the brain-associated HPA signals raise the possibility of an additional neural or glial interface component, but that interpretation remains a hypothesis because the only globally corrected pathway evidence is (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0361).

### Important genes

#### COL1A1

- **Related proteins** (co-abundance neighbors): COL1A2 (0.92), CRTAC1 (0.88), COL6A1 (0.85); STRING partners: COL1A2 (0.999), COL6A1 (0.969), COL6A3 (0.974), LAMC1 (0.77)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_02141.1, huMAP3_06460.1, huMAP3_07562.1, huMAP3_02069.1, huMAP3_10780.1, huMAP3_09231.1, huMAP3_09523.1, huMAP3_09606.1, huMAP3_10652.1, huMAP3_14070.1
- **Function (MyGene.info)**: collagen type I alpha 1 chain. This gene encodes the pro-alpha1 chains of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIA, Ehlers-Danlos syndrome Classical type,…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 2 (0.847); osteogenesis imperfecta type 4 (0.837); osteogenesis imperfecta type 3 (0.835); osteogenesis imperfecta type 1 (0.834); osteogenesis imperfecta (0.808)
- **Europe PMC papers**: 45548
- **Why important**: COL1A1 is a central structural representative of the module’s collagen core and is linked in STRING to COL1A2, COL6A1, COL6A3, and LAMC1. It is present in the globally supported ECM-receptor interaction term (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0361), is secreted to the extracellular matrix, and is enhanced in fibroblast and hepatic-stellate-cell contexts. Its extensive disease and literature record, including osteogenesis imperfecta and connective-tissue disorders, makes it the best-established anchor for interpreting the module as matrix biology rather than as an isolated fluid-protein signature.
- **Conclusion**: Established evidence supports COL1A1 as a major extracellular-matrix and collagen-fibril component of the module. The co-abundance pattern is consistent with shared stromal or vascular matrix biology. It does not by itself establish that COL1A1 is produced locally in cerebrospinal fluid.

#### COL6A1

- **Related proteins** (co-abundance neighbors): COL1A1 (0.85), COL1A2 (0.85), SELENBP1 (0.83), CP (0.83), COL6A3 (0.81), FGA (0.81); STRING partners: COL1A1 (0.969), COL1A2 (0.875), COL6A3 (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 has a strong position in the module and connects the type I collagen group with COL6A3, CP, SELENBP1, and FGA. It is part of (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0361) and all listed STRING supplementary terms, and its annotation identifies collagen VI as a structural microfibrillar component. HPA links it to fibroblasts and fibro-adipogenic stromal cells, while its disease associations include Bethlem and Ullrich muscular dystrophies. It therefore bridges the matrix core and the tissue-interface or circulating-protein portion of the module.
- **Conclusion**: Established evidence supports COL6A1 as a matrix-organizing component and a strong integrator of the collagen-related signal. Its association with FGA and CP is compatible with shared extracellular or vascular abundance, but the mechanism connecting these compartments remains unresolved.

#### LAMC1

- **Related proteins** (co-abundance neighbors): LAMB2 (0.83); STRING partners: COL1A1 (0.77), COL1A2 (0.701), HSPG2 (0.82), LAMB2 (0.962)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Plasma membrane; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit gamma 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: Fuchs' endothelial dystrophy (0.487); prostate carcinoma (0.467); colorectal cancer (0.447); eye disorder (0.434); benign colon neoplasm (0.427)
- **Europe PMC papers**: 4227
- **Why important**: LAMC1 is a laminin-chain component of (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0361) and is connected in STRING to LAMB2, HSPG2, COL1A1, and COL1A2. Laminins organize basement membranes and participate in adhesion, migration, and integrin-mediated signaling. HPA places LAMC1 in extracellular and membrane-associated compartments and links it to fibroblast and adipocyte-related cell types. It provides a mechanistic bridge from collagen-rich matrix to basement-membrane and cell-adhesion biology.
- **Conclusion**: Established evidence supports LAMC1 as a basement-membrane and cell–matrix adhesion component that reinforces the module’s ECM interpretation. A role in coordinating matrix signals across breast and cerebrospinal-fluid interfaces is plausible but remains untested.

#### HSPG2

- **Related proteins** (co-abundance neighbors): FGA (0.84), LAMB2 (0.81); STRING partners: LAMC1 (0.82)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 is part of (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0361) and the supplementary ECM-related STRING terms, and its STRING relationship with LAMC1 directly supports a basement-membrane subnetwork. Perlecan is a multidomain extracellular proteoglycan that binds and cross-links matrix and cell-surface molecules, and HPA associates it with blood vessels, fibro-adipogenic progenitors, and hepatic stellate cells. Its disease associations and vascular annotation make it important for interpreting the module as a specialized extracellular scaffold rather than merely a collection of collagens.
- **Conclusion**: Established evidence supports HSPG2 as a matrix scaffold and signaling-interface component. The module may capture basement-membrane remodeling or barrier-associated biology, but the co-abundance data cannot determine whether remodeling, production, or fluid transport is the primary process.

#### C4A

- **Related proteins** (co-abundance neighbors): COL1A2 (0.85), LGALS1 (0.81); STRING partners: C1QC (0.972)
- **HPA**: Tissue enhanced; Not detected; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_07432.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_02242.1, huMAP3_08700.1, huMAP3_07265.1, huMAP3_09273.1
- **Function (MyGene.info)**: complement C4A (Chido/Rodgers blood group). This gene encodes the acidic form of complement factor 4, part of the classical activation pathway. The protein is expressed as a single chain precursor which is proteolytically cleaved into a trimer of alpha, beta, and gamma chains prior to secretion. The trimer provides a surface for interaction between the antigen-antibody complex and other complement components. The alpha chain is cleaved to r…
- **Diseases (Open Targets)**: complement component 4a deficiency (0.603); immunodeficiency due to a classical component pathway complement deficiency (0.560); complement deficiency (0.466); systemic lupus erythematosus (0.403); dengue disease (0.375)
- **Europe PMC papers**: 7019
- **Why important**: C4A represents the complement and circulating-protein side of the module. It is liver-enhanced, secreted to blood, and annotated for classical and lectin complement activation, opsonization, and inflammatory response. It connects to C1QC in STRING and occurs with CP and FGA in several hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) and (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_08700.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09273.1). Its presence prevents an overly narrow interpretation of the module as purely structural ECM.
- **Conclusion**: Established evidence supports C4A as a circulating complement component associated with the module’s plasma and immune-interface signal. Its co-abundance with matrix genes may reflect vascular or fluid exposure, extracellular binding, or shared tissue-interface regulation; a direct functional interaction with the collagen scaffold is not established here.

#### CRTAC1

- **Related proteins** (co-abundance neighbors): COL1A1 (0.88), ALDOC (0.87), MCAM (0.86), CLEC3B (0.84), AMBP (0.83), C1QC (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cartilage acidic protein 1. This gene encodes a glycosylated extracellular matrix protein that is found in the interterritorial matrix of articular deep zone cartilage. This protein is used as a marker to distinguish chondrocytes from osteoblasts and mesenchymal stem cells in culture. The presence of FG-GAP motifs and an RGD integrin-binding motif suggests that this protein may be involved in cell-cell or cell-matrix interac…
- **Diseases (Open Targets)**: smoking initiation (0.403); neurodegenerative disease (0.331); coronary artery disorder (0.327); coronary atherosclerosis (0.321); hypertensive disorder (0.312)
- **Europe PMC papers**: 702
- **Why important**: CRTAC1 has one of the strongest network positions in the module and connects matrix-associated genes with ALDOC, MCAM, CLEC3B, AMBP, and C1QC. It is a secreted extracellular-matrix protein with an RGD integrin-binding motif, is enhanced in blood vessel and lung contexts, and is detected in breast. Its annotations include cell–matrix interaction, axonal fasciculation, and synapse assembly, giving it potential relevance to both stromal and neural-interface interpretations. Its lack of STRING partners and hu.MAP complexes also makes it a potentially informative, less well-connected component for follow-up.
- **Conclusion**: Established evidence supports CRTAC1 as a secreted matrix-associated adhesion protein with vascular and neural-interface annotations. Its position suggests that it could connect the structural module to brain or barrier biology, but this is a hypothesis rather than a demonstrated role in the shared breast–cerebrospinal-fluid pattern.

## Module 5

**Tissue pair**: breast and cerebrospinal_fluid  
**Genes (23)**: NAGLU, BMPR2, CTSL, CGREF1, DCBLD1, EFNA5, EGFR, ERBB3, GGT7, HEXA, HGFAC, CD58, MAN2B1, NCAM2, NEO1, NRCAM, PLXNA1, SDK1, SEZ6L2, SEMA3C, SEMA4D, TFPI, THY1

### Function

The strongest interpretation is a cell-surface adhesion, guidance, and signaling module with a neural differentiation and neuron-generation signature. (GO:BP neuron differentiation; q_global = 0.0119) and (GO:BP generation of neurons; q_global = 0.0156) provide primary evidence for neuron differentiation and generation of neurons, including BMPR2, EFNA5, EGFR, ERBB3, HEXA, NAGLU, NCAM2, NEO1, NRCAM, PLXNA1, SDK1, SEMA3C, SEMA4D, and THY1. (GO:CC plasma membrane region; q_global = 0.0398) independently supports localization to the plasma membrane region. The gene functions support coordinated axon guidance, neuron projection development, cell-cell adhesion, synapse assembly, receptor signaling, lysosomal glycan turnover, and vascular or endothelial signaling rather than one narrowly defined biochemical pathway. The topology is consistent with a connected signaling-and-adhesion system: SEMA4D is the central hub, while the SEMA4D–PLXNA1–SEMA3C and NRCAM–PLXNA1 relationships link semaphorin guidance to neuronal adhesion. EGFR–ERBB3 provides a known receptor signaling pair, and EFNA5 connects ephrin-related guidance biology to EGFR. These observations support a conserved neural-interface or neurovascular cell-surface program, but co-abundance alone does not establish physical interaction, causality, or pathway activation.

**Cell composition.** The module is not uniformly neuronal or uniformly non-secreted. HPA shows brain enrichment or enhancement for several genes and cell-type enhancement in oligodendrocytes, astrocytes, excitatory neurons, and related neural populations, which is compatible with genuine neural or glial biology. At the same time, many members are secreted or extracellularly detected, including TFPI, HGFAC, CGREF1, NRCAM, and SEMA3C, while other members show broad or low tissue specificity. There are also placenta, liver, adrenal, salivary, vascular, and stromal signals, together with selected monocyte, basophil, T-cell, and other immune-cell enrichments. Thus the shared breast–cerebrospinal-fluid module could reflect a mixture of neural, vascular, stromal, and extracellular protein abundance rather than a pure neuronal population. The presence of secreted proteins and breast detection for many members makes blood or extracellular-fluid contribution plausible, although the HPA summary does not support a predominantly blood-cell-enriched module because many genes are not detected in immune cells or have low immune-cell specificity. There is no matching HPA tissue dataset for cerebrospinal fluid, so its protein composition cannot be directly validated from this evidence.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP neuron differentiation | 0.0119 | BMPR2, EFNA5, EGFR, ERBB3, HEXA, NAGLU, NCAM2, NEO1, NRCAM, PLXNA1, SDK1, SEMA3C, SEMA4D, THY1 |
| GO:BP generation of neurons | 0.0156 | BMPR2, EFNA5, EGFR, ERBB3, HEXA, NAGLU, NCAM2, NEO1, NRCAM, PLXNA1, SDK1, SEMA3C, SEMA4D, THY1 |
| GO:CC plasma membrane region | 0.0398 | BMPR2, CTSL, EFNA5, EGFR, ERBB3, NCAM2, NEO1, NRCAM, SEMA4D, TFPI, THY1 |

### STRING and hu.MAP

STRING functional enrichment was absent, so STRING supplies no supplementary pathway enrichment. Nevertheless, STRING contains high-confidence pairwise relationships for EFNA5–EGFR, EGFR–ERBB3, NRCAM–PLXNA1, PLXNA1–SEMA3C, and PLXNA1–SEMA4D. These known relationships reinforce receptor signaling, semaphorin guidance, and neuronal adhesion as plausible components of the module, but they account for only a minority of possible gene pairs and do not validate every co-abundance edge. hu.MAP provides partial complex-level support. (hu.MAP huMAP3_11349.1), (hu.MAP huMAP3_08689.1), and (hu.MAP huMAP3_09336.1) repeatedly contain CD58 and SDK1, with SEZ6L2 additionally present in (hu.MAP huMAP3_11349.1), indicating reproducible association with broad membrane and adhesion-related complex contexts. (hu.MAP huMAP3_09327.1) contains NAGLU and PLXNA1, linking lysosomal or glycan biology with a guidance-receptor context. Because each hu.MAP complex contains many members outside the module, these are contextual overlaps rather than proof that the whole module is one physical complex.

**STRING interactions (score >= 0.7)**: 5 of 253 gene pairs: EFNA5–EGFR (0.753); EGFR–ERBB3 (0.999); NRCAM–PLXNA1 (0.786); PLXNA1–SEMA3C (0.965); PLXNA1–SEMA4D (0.743)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11349.1 (CD58, SEZ6L2, SDK1; 3/78); huMAP3_08689.1 (CD58, SDK1; 2/37); huMAP3_09336.1 (CD58, SDK1; 2/50); huMAP3_09327.1 (NAGLU, PLXNA1; 2/93)

### Novelty

This module should be described as a potentially new cross-tissue co-abundance pattern, not as a newly discovered molecular pathway. The neural guidance, adhesion, receptor, lysosomal, and coagulation-related functions are individually established in the literature and databases. Several internal relationships are already represented in STRING, and the CD58–SDK1, SEZ6L2, and NAGLU–PLXNA1 overlaps are represented in hu.MAP contexts. What may be novel is their coordinated abundance across breast and cerebrospinal fluid, especially the combination of neural differentiation evidence with extracellular, vascular, stromal, and immune-related composition. That claim requires independent replication, assessment of donor and cell-type composition, comparison with existing cross-tissue modules, and targeted protein or single-cell validation. Absence of a complete representation in STRING or hu.MAP cannot by itself establish novelty.

**Hypothesis.** Hypothesis: the module reflects a conserved extracellular-interface program in which semaphorin and adhesion molecules organize neural or glial contacts, while EGFR–ERBB3 and BMPR2-related signaling regulate cell state, migration, differentiation, or vascular support. SEMA4D–PLXNA1 and PLXNA1–SEMA3C could provide guidance-related organization; NRCAM, NCAM2, NEO1, SDK1, and THY1 could stabilize cell-cell or cell-matrix contacts; and lysosomal enzymes such as HEXA and NAGLU could support membrane-glycan remodeling. Secreted or blood-associated components such as TFPI, HGFAC, CGREF1, and NRCAM may connect this interface to extracellular-fluid transport or vascular context. This is a mechanistic model, not an established causal pathway: it should be tested by cell-type-resolved measurements, protein-level co-variation, perturbation of receptor and semaphorin axes, and replication in independent breast and cerebrospinal-fluid cohorts.

### Important genes

#### SEMA4D

- **Related proteins** (co-abundance neighbors): NRCAM (0.99), CD58 (0.98), HEXA (0.97), NAGLU (0.95), PLXNA1 (0.94), SEMA3C (0.93), SEZ6L2 (0.90), ERBB3 (0.90), GGT7 (0.85), MAN2B1 (0.85); STRING partners: PLXNA1 (0.743)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: semaphorin 4D. Enables identical protein binding activity; semaphorin receptor binding activity; and transmembrane signaling receptor activity. Involved in several processes, including positive regulation of phosphatidylinositol 3-kinase signaling; regulation of neuron projection development; and regulation of phosphate metabolic process. Is integral component of plasma membrane. [provided by Alliance of Genome …
- **Diseases (Open Targets)**: skin aging (0.442); sclerosing cholangitis (0.372); intelligence (0.283); placental abruption (0.191); otosclerosis (0.153)
- **Europe PMC papers**: 2198
- **Why important**: SEMA4D is the central network hub and appears in (GO:BP neuron differentiation; q_global = 0.0119), (GO:BP generation of neurons; q_global = 0.0156), and (GO:CC plasma membrane region; q_global = 0.0398). Its established functions include semaphorin receptor binding, axon guidance, cell adhesion, immune response, and phosphatidylinositol signaling. Its STRING relationship with PLXNA1 directly anchors the guidance interpretation, while its extensive literature supports a strong biological prior. HPA shows brain tissue enhancement, several neural or immune-related cell-type signals, plasma-membrane localization, and breast protein detection.
- **Conclusion**: Established: SEMA4D is a membrane guidance and adhesion signal with neural and immune functions and is a major internal connector. Conclusion: it is the strongest candidate for organizing the module's cell-surface guidance axis. Hypothesis: coordinated SEMA4D abundance may mark semaphorin-dependent remodeling of neural, glial, vascular, or immune-cell contacts across the tissues.

#### PLXNA1

- **Related proteins** (co-abundance neighbors): SEMA4D (0.94), GGT7 (0.84); STRING partners: NRCAM (0.786), SEMA3C (0.965), SEMA4D (0.743)
- **HPA**: Low tissue specificity; Cell type enriched; blood Not detected in immune cells; location Nucleoplasm, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_09327.1
- **Function (MyGene.info)**: plexin A1. Predicted to enable semaphorin receptor activity. Predicted to be involved in several processes, including generation of neurons; regulation of GTPase activity; and regulation of cell shape. Predicted to act upstream of or within dichotomous subdivision of terminal units involved in salivary gland branching; neuron projection morphogenesis; and regulation of smooth muscle cell migration. Located i…
- **Diseases (Open Targets)**: Dworschak-Punetha neurodevelopmental syndrome (0.749); developmental and epileptic encephalopathy (0.462); genetic developmental and epileptic encephalopathy (0.462); neurodevelopmental disorder (0.409); skin aging (0.389)
- **Europe PMC papers**: 933
- **Why important**: PLXNA1 is the receptor-side anchor for the semaphorin subnetwork. It is in (GO:BP neuron differentiation; q_global = 0.0119) and (GO:BP generation of neurons; q_global = 0.0156), occurs in hu.MAP context (hu.MAP huMAP3_09327.1), and has high-confidence STRING relationships with NRCAM, SEMA3C, and SEMA4D. Its annotations include semaphorin receptor activity, neuron generation, synapse assembly, neuron projection morphogenesis, cell migration, and semaphorin-plexin signaling. Its disease associations include developmental and epileptic encephalopathy and other neurodevelopmental disorders.
- **Conclusion**: Established: PLXNA1 connects known semaphorin ligands with neuronal guidance and migration functions. Conclusion: it is a mechanistically informative bridge rather than merely a correlated marker. Hypothesis: PLXNA1 may transmit the module's extracellular guidance signal into changes in cell shape, migration, or synaptic organization.

#### EGFR

- **Related proteins** (co-abundance neighbors): EFNA5 (0.84), ERBB3 (0.81); STRING partners: EFNA5 (0.753), ERBB3 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus, Plasma membrane; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: epidermal growth factor receptor. The protein encoded by this gene is a transmembrane glycoprotein that is a member of the protein kinase superfamily. This protein is a receptor for members of the epidermal growth factor family. EGFR is a cell surface protein that binds to epidermal growth factor, thus inducing receptor dimerization and tyrosine autophosphorylation leading to cell proliferation. Mutations in this gene are associat…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.850); lung adenocarcinoma (0.774); cancer (0.737); head and neck squamous cell carcinoma (0.725); lung cancer (0.717)
- **Europe PMC papers**: 223694
- **Why important**: EGFR is a well-characterized receptor tyrosine kinase with extensive literature and strong disease relevance. It appears in (GO:BP neuron differentiation; q_global = 0.0119), (GO:BP generation of neurons; q_global = 0.0156), and (GO:CC plasma membrane region; q_global = 0.0398), and STRING supports its relationships with ERBB3 and EFNA5. Its established functions include MAPK signaling, receptor phosphorylation, cell-surface signaling, and proliferation. HPA reports breast protein detection, plasma-membrane localization, and placenta enhancement.
- **Conclusion**: Established: EGFR supplies a canonical signaling input and is linked within the module to ERBB3 and EFNA5. Conclusion: it is the strongest candidate for coupling extracellular cues to intracellular state changes. Hypothesis: EGFR activity could modulate or integrate the guidance and adhesion program, although co-abundance does not show receptor activation.

#### NCAM2

- **Related proteins** (co-abundance neighbors): BMPR2 (0.95), CGREF1 (0.93), GGT7 (0.89), SDK1 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nuclear bodies, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neural cell adhesion molecule 2. The protein encoded by this gene belongs to the immunoglobulin superfamily. It is a type I membrane protein and may function in selective fasciculation and zone-to-zone projection of the primary olfactory axons. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: smoking initiation (0.437); parasitic infectious disease (0.325); venous thromboembolism (0.320); frozen shoulder (0.294); skin disorder (0.288)
- **Europe PMC papers**: 1069
- **Why important**: NCAM2 is a neural cell-adhesion molecule with brain and adrenal tissue enhancement and cell-type enhancement in astrocytes, glia, and excitatory neurons. It appears in (GO:BP neuron differentiation; q_global = 0.0119), (GO:BP generation of neurons; q_global = 0.0156), and (GO:CC plasma membrane region; q_global = 0.0398) and occupies a connective position near BMPR2, GGT7, CGREF1, and SDK1 in the module network. Its established functions include neuron-neuron adhesion and selective neural fasciculation. Its literature supports a meaningful neuronal adhesion role, although its disease evidence is less specific than that of major receptor genes.
- **Conclusion**: Established: NCAM2 is a neural adhesion molecule aligned with the global enrichment and HPA neural evidence. Conclusion: it is a strong marker of the module's neural cell-contact component. Hypothesis: NCAM2 may help stabilize the cellular interfaces on which semaphorin and receptor signals act.

#### BMPR2

- **Related proteins** (co-abundance neighbors): NCAM2 (0.95), GGT7 (0.94), ERBB3 (0.92), CTSL (0.91), SEZ6L2 (0.91); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: bone morphogenetic protein receptor type 2. This gene encodes a member of the bone morphogenetic protein (BMP) receptor family of transmembrane serine/threonine kinases. The ligands of this receptor are members of the TGF-beta superfamily. BMPs are involved in endochondral bone formation and embryogenesis. These proteins transduce their signals through the formation of heteromeric complexes of two different types of serine (threonine) kinas…
- **Diseases (Open Targets)**: pulmonary hypertension, primary, 1 (0.821); pulmonary arterial hypertension (0.753); pulmonary venoocclusive disease (0.743); pulmonary venoocclusive disease 1 (0.697); idiopathic pulmonary arterial hypertension (0.681)
- **Europe PMC papers**: 8608
- **Why important**: BMPR2 is a transmembrane serine-threonine kinase receptor and appears in (GO:BP neuron differentiation; q_global = 0.0119), (GO:BP generation of neurons; q_global = 0.0156), and (GO:CC plasma membrane region; q_global = 0.0398). Its module connections include NCAM2, GGT7, ERBB3, CTSL, and SEZ6L2. Established annotations include regulation of cell growth, blood-vessel development, endothelial proliferation, and vasculature development. It has extensive literature and strong disease associations with pulmonary hypertension and related vascular disorders. HPA indicates low tissue specificity and vascular endothelial cell enhancement.
- **Conclusion**: Established: BMPR2 provides a vascular and growth-signaling interpretation that complements the neural guidance signal. Conclusion: it is important for evaluating whether the module is neurovascular or endothelial rather than purely neuronal. Hypothesis: BMPR2 may couple extracellular neural-interface signals to vascular support or endothelial state in the shared module.

## Module 6

**Tissue pair**: breast and cerebrospinal_fluid  
**Genes (28)**: ANGPTL2, SMPDL3A, BTD, CACNA2D1, CDH5, CLMP, C9, EPHA4, F10, MAN1A1, MINPP1, NAGA, NEGR1, NPDC1, NRP2, PLXNA3, PTPRF, PTPRJ, PTPRS, RNASET2, ROBO1, SCG2, SEMA4C, SIL1, SULF2, TMEM132A, ABI3BP, VGF

### Function

No GO or KEGG term passed global correction, so the module cannot be assigned a statistically supported pathway label from enrichment. Its gene-level and network evidence instead points to a mixed extracellular and membrane-signaling program. Relevant functions include semaphorin and plexin signaling, axon guidance, cell migration, cell adhesion, endothelial junction biology, receptor tyrosine phosphatase signaling, calcium-channel regulation, glycoprotein processing, and neuroendocrine secretion. The co-abundance pattern is therefore more consistent with coordinated cellular-interface and secretory biology than with a single established biochemical pathway. The presence of neural, vascular, stromal, epithelial, and secreted-protein annotations argues for a biologically heterogeneous module whose interpretation should remain cautious.

**Cell composition.** The module is compositionally mixed rather than a clean tissue-specific neuronal or vascular set. Most genes encode proteins secreted to blood, secreted in other tissues, or associated with extracellular or membrane compartments, including SMPDL3A, VGF, SCG2, PTPRJ, C9, ANGPTL2, F10, MINPP1, and ABI3BP. HPA also shows substantial low tissue specificity, while several genes are tissue enhanced in brain, liver, pituitary gland, skeletal muscle, tongue, ovary, intestine, adipose tissue, or choroid plexus. Immune-cell specificity is not dominant because many genes are not detected in immune cells or have low immune-cell specificity, but selected genes show enrichment in basophils, monocytes, plasmacytoid dendritic cells, neutrophils, or other immune populations. This mixture, together with the blood-secreted component, means that shared sample composition, vascular or stromal material, circulating proteins, or shared cell types could contribute substantially to the breast and cerebrospinal-fluid association. HPA has breast protein detection for many genes, whereas it provides no matching tissue assessment for cerebrospinal fluid.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a small set of high-confidence relationships within the module: CDH5 with PTPRJ, NRP2 with PLXNA3, and SCG2 with VGF. These relationships support specific biological links involving endothelial adhesion or receptor phosphatase biology, semaphorin or neuropilin signaling, and neuroendocrine secretory machinery, but they do not establish a dense known interaction network. hu.MAP provides two-member overlaps in three complexes. BTD and CACNA2D1 occur together in (hu.MAP huMAP3_12928.1), while PTPRF and PTPRS occur together in (hu.MAP huMAP3_11149.1) and (hu.MAP huMAP3_11605.1). Because each hu.MAP overlap contains only a small subset of the corresponding complex, these findings support compatibility with known complexes rather than reconstruction of complete complexes in this module. Overall, the network appears to combine a few known molecular relationships with many co-abundance links that are not represented as established STRING or hu.MAP interactions.

**STRING interactions (score >= 0.7)**: 3 of 378 gene pairs: CDH5–PTPRJ (0.811); NRP2–PLXNA3 (0.996); SCG2–VGF (0.73)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12928.1 (BTD, CACNA2D1; 2/6); huMAP3_11149.1 (PTPRF, PTPRS; 2/32); huMAP3_11605.1 (PTPRF, PTPRS; 2/64)

### Novelty

The module should not be called a newly discovered molecular complex or pathway. No GO or KEGG term passed global correction, STRING reported no supplementary functional enrichment, and only a limited subset of the co-abundance relationships is represented by high-confidence STRING links or hu.MAP overlaps. These observations suggest that the particular cross-tissue co-abundance organization may be undercharacterized. However, absence from STRING or hu.MAP alone cannot prove novelty, because those resources emphasize experimentally supported physical or curated relationships and may not capture tissue-specific co-regulation, shared secretion, sample composition, or indirect signaling. The defensible conclusion is that this is a potentially novel cross-tissue co-abundance pattern built from partly known biology, not evidence for a novel molecular mechanism.

**Hypothesis.** Hypothesis: the shared module reflects coordinated abundance of extracellular, membrane, and secretory proteins contributed by a mixture of vascular, stromal, neural or neuroendocrine, and circulating compartments. Within this mixed program, semaphorin signaling through PLXNA3 and NRP2, adhesion and receptor phosphatase signaling through PTPRF and PTPRJ, and neuroendocrine vesicle biology involving VGF and SCG2 could converge on cell-contact remodeling, guidance, vascular or stromal communication, and regulated secretion. Secreted proteins and liver-associated blood proteins may amplify the apparent cross-tissue signal. This hypothesis requires validation by cell-resolved data, protein localization in cerebrospinal fluid, and independent cohorts; it is not established by the enrichment analysis.

### Important genes

#### PLXNA3

- **Related proteins** (co-abundance neighbors): SEMA4C (0.90), ANGPTL2 (0.88), NRP2 (0.84), PTPRF (0.83), MAN1A1 (0.81), ABI3BP (0.81); STRING partners: NRP2 (0.996)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Golgi apparatus, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plexin A3. This gene encodes a member of the plexin class of proteins. The encoded protein is a class 3 semaphorin receptor, and may be involved in cytoskeletal remodeling and as well as apoptosis. Studies of a similar gene in zebrafish suggest that it is important for axon pathfinding in the developing nervous system. This gene may be associated with tumor progression. [provided by RefSeq, Aug 2013].
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism (0.414); Short stature (0.323); neurodevelopmental disorder (0.150); autism (0.150); disorder of sexual differentiation (0.112)
- **Europe PMC papers**: 564
- **Why important**: PLXNA3 is a highly connected module member and has a direct high-confidence STRING relationship with NRP2. Its annotation as a class three semaphorin receptor links the module to axon guidance, cytoskeletal remodeling, synapse assembly, and possible tumor progression. Its low tissue specificity and lack of immune-cell detection make it a useful candidate for a shared neural or membrane-signaling component rather than a simple blood-cell marker. Its disease associations include neurodevelopmental and reproductive phenotypes, and its literature volume is substantial.
- **Conclusion**: Established evidence supports PLXNA3 as a membrane receptor involved in semaphorin-related guidance and developmental signaling, with a known relationship to NRP2. It is plausible, but not established, that PLXNA3 helps organize the module’s shared cell-interface signal across breast and cerebrospinal-fluid samples.

#### PTPRF

- **Related proteins** (co-abundance neighbors): SCG2 (0.94), SMPDL3A (0.86), NEGR1 (0.85), PLXNA3 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_11149.1, huMAP3_11605.1
- **Function (MyGene.info)**: protein tyrosine phosphatase receptor type F. The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP possesses an extracellular region, a single transmembrane region, and two tandem intracytoplasmic catalytic domains, and thu…
- **Diseases (Open Targets)**: breasts and/or nipples, aplasia or hypoplasia of, 2 (0.505); smoking initiation (0.420); attention deficit-hyperactivity disorder (0.419); isolated congenital breast hypoplasia/aplasia (0.370); substance-related disorder (0.329)
- **Europe PMC papers**: 4709
- **Why important**: PTPRF occupies a central position in the module’s receptor and adhesion-related subnetwork, connecting with SCG2, SMPDL3A, NEGR1, and PLXNA3. It is a receptor-type protein tyrosine phosphatase with annotated roles in cell adhesion, cell migration, nervous-system development, and signal transduction. Its membership in both hu.MAP overlaps (hu.MAP huMAP3_11149.1) and (hu.MAP huMAP3_11605.1) provides complex-level support, although only partial complex membership is observed. It is detected in breast and has a large literature base.
- **Conclusion**: Established evidence supports PTPRF as a plausible signaling and adhesion hub with known complex associations in (hu.MAP huMAP3_11149.1) and (hu.MAP huMAP3_11605.1). Its role as a causal coordinator of the entire module remains a hypothesis because the co-abundance network does not demonstrate direct physical interaction among all connected genes.

#### VGF

- **Related proteins** (co-abundance neighbors): SIL1 (0.98), PTPRS (0.91), SULF2 (0.90), ROBO1 (0.83); STRING partners: SCG2 (0.73)
- **HPA**: Group enriched; Cell type enriched; blood Not detected in immune cells; location Golgi apparatus, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VGF nerve growth factor inducible. This gene is specifically expressed in a subpopulation of neuroendocrine cells, and is upregulated by nerve growth factor. The structural organization of this gene is similar to that of the rat gene, and both the translated and the untranslated regions show a high degree of sequence similarity to the rat gene. The encoded secretory protein also shares similarities with the secretogranin/chromogran…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.144); amyotrophic lateral sclerosis (0.121); Alzheimer disease (0.108); neoplasm (0.099); infection (0.097)
- **Europe PMC papers**: 3253
- **Why important**: VGF is a brain- and pituitary-enriched secreted protein with a direct STRING relationship to SCG2. It is associated with Golgi and vesicle compartments and with neuropeptide-mediated synaptic signaling and neuronal plasticity. Its network links to SIL1, PTPRS, SULF2, and ROBO1 connect secretory biology with guidance and receptor signaling. VGF also has the largest literature volume among the selected genes and disease associations involving neurodegenerative and neurological conditions.
- **Conclusion**: Established evidence supports VGF as a neuroendocrine secretory component and supports its relationship with SCG2. Its presence in a breast and cerebrospinal-fluid module could reflect neural or neuroendocrine material, circulating secretion, or shared secretory regulation; the source cannot be determined from this module alone.

#### PTPRJ

- **Related proteins** (co-abundance neighbors): SMPDL3A (1.00), CLMP (0.82), NEGR1 (0.81); STRING partners: CDH5 (0.811)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cell Junctions; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein tyrosine phosphatase receptor type J. The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes, including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP possesses an extracellular region containing five fibronectin type III repeats, a single transmembrane region, and a single…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); hypertensive disorder (0.480); colon carcinoma (0.418); thrombocytopenia 10 (0.417); Increased blood pressure (0.400)
- **Europe PMC papers**: 1289
- **Why important**: PTPRJ links SMPDL3A, CLMP, and NEGR1 in the module and has a known STRING relationship with CDH5. It is a receptor-type protein tyrosine phosphatase associated with cell-matrix adhesion, signal transduction, cell-population regulation, and axon guidance. HPA places it in cell-junction compartments and reports neutrophil-related enrichment, while also showing breast detection and secretion to blood. Its disease associations include neurodegenerative, vascular, and hematological conditions.
- **Conclusion**: Established evidence supports PTPRJ as an adhesion and signaling regulator with endothelial and immune-cell relevance. The module may capture vascular or circulating-cell-associated biology involving PTPRJ, but the data do not establish whether it is a driver or merely a marker of the shared sample composition.

#### NEGR1

- **Related proteins** (co-abundance neighbors): PTPRF (0.85), C9 (0.85), CACNA2D1 (0.83), NAGA (0.82), PTPRJ (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles, Actin filaments, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neuronal growth regulator 1. Predicted to act upstream of or within several processes, including feeding behavior; locomotory behavior; and positive regulation of neuron projection development. Predicted to be located in extracellular region and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: major depressive disorder (0.585); intelligence (0.571); obesity disorder (0.547); Abnormality of the skeletal system (0.539); schizophrenia (0.505)
- **Europe PMC papers**: 1724
- **Why important**: NEGR1 is among the more connected module members and links PTPRF, C9, CACNA2D1, NAGA, and PTPRJ. It is tissue enhanced in brain and cell-type enhanced in several neuronal and fibro-adipogenic populations. Its annotations include heterophilic cell-cell adhesion, synapse assembly, protein secretion, and plasma-membrane organization. It has extensive literature and disease associations spanning psychiatric, behavioral, metabolic, and skeletal phenotypes.
- **Conclusion**: Established evidence supports NEGR1 as a cell-adhesion and neural-associated protein that can connect neuronal, stromal, and membrane biology. Its module position makes it an informative integrative marker, but a direct role in coordinating the breast and cerebrospinal-fluid pattern is not established.

#### ANGPTL2

- **Related proteins** (co-abundance neighbors): PLXNA3 (0.88), CLMP (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: angiopoietin like 2. Angiopoietins are members of the vascular endothelial growth factor family and the only known growth factors largely specific for vascular endothelium. Angiopoietin-1, angiopoietin-2, and angiopoietin-4 participate in the formation of blood vessels. ANGPTL2 protein is a secreted glycoprotein with homology to the angiopoietins and may exert a function on endothelial cells through autocrine or parac…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.351); spermatogenic failure (0.320); Abnormal male internal genitalia morphology (0.320); open-angle glaucoma (0.262); glaucoma (0.250)
- **Europe PMC papers**: 1583
- **Why important**: ANGPTL2 connects PLXNA3 and CLMP and is secreted to blood. Its annotations describe vascular growth-factor-like biology, cell-cell signaling, and blood coagulation, while HPA reports expression in adipocytes, cardiomyocytes, choroid plexus epithelial cells, and stromal populations. This makes it relevant to a cross-tissue module that may include vascular, stromal, adipose, or circulating components. Its literature and disease associations provide additional biological context, although it is not a high-confidence STRING partner in this module.
- **Conclusion**: Established evidence supports ANGPTL2 as a secreted signaling protein with vascular and stromal relevance. It is a plausible mediator of intercellular communication in the module, but the proposed connection to the other module members remains inferential and requires direct experimental testing.

## Module 7

**Tissue pair**: breast and cerebrospinal_fluid  
**Genes (9)**: AGT, ASAH1, COL5A1, F13B, FREM2, HPX, HRG, ITIH4, PODXL2

### Function

The module is best interpreted as a liver-derived plasma-protein and extracellular-matrix-associated co-abundance program rather than as a coherently enriched intracellular pathway. Its most connected member, F13B, links the plasma proteins ITIH4, HRG, AGT and the tissue-associated proteins PODXL2, ASAH1 and COL5A1. The annotated functions represented by the genes include coagulation and fibrin-clot formation, heme transport, acute-phase and cytokine responses, regulation of blood pressure and fluid balance, sphingolipid metabolism, cell adhesion and collagen-fibril organization. These annotations support a broad extracellular homeostasis, vascular or injury-response interpretation, but not a single specific pathway. No GO or KEGG term passed global correction, so no GO or KEGG enrichment is claimed. There was also no supplementary STRING functional-enrichment result. The module may therefore reflect coordinated abundance of circulating proteins and a smaller tissue or extracellular-matrix signal rather than pathway enrichment.

**Cell composition.** The composition strongly favors secreted or extracellular proteins: F13B, ITIH4, HPX, HRG and AGT are secreted to blood, while COL5A1 is secreted to the extracellular matrix. Most genes are not detected in immune cells, with ASAH1 showing only low immune-cell specificity, arguing against a blood-cell enrichment explanation. HPA tissue evidence is dominated by liver and hepatocyte specificity for F13B, ITIH4, HPX, HRG and AGT. PODXL2 has brain-associated enhancement, COL5A1 includes ependymal-cell enhancement, and FREM2 includes Bergmann-glia enhancement, which could be relevant to the cerebrospinal fluid context. Breast protein detection is limited, and the HPA summary has no matching cerebrospinal fluid tissue category. Overall, shared abundance of liver-derived plasma proteins, sample blood content, or vascular leakage should be considered before assigning a breast or central-nervous-system specific biological role.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest STRING-supported relationships are F13B with HRG, HPX with ITIH4, and HRG with ITIH4. These relationships are concordant with a plasma-protein network, but STRING support represents previously known or inferred association and does not establish that the proteins physically interact in these samples. hu.MAP independently places AGT, HPX, HRG and ITIH4 together in several plasma and extracellular-protein complexes, including (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1) and (hu.MAP huMAP3_10678.1), with smaller overlaps in (hu.MAP huMAP3_09273.1) and (hu.MAP huMAP3_08395.1). The recurrence of this same four-gene set across complexes is important evidence that part of the module recapitulates a known circulating-protein community. Conversely, F13B, PODXL2, ASAH1, COL5A1 and FREM2 have no listed hu.MAP membership, and most module pairings lack listed STRING support. Thus the module combines a known plasma-protein core with peripheral co-abundance links that may arise from shared secretion, tissue composition, extracellular biology or technical covariance.

**STRING interactions (score >= 0.7)**: 3 of 36 gene pairs: F13B–HRG (0.819); HPX–ITIH4 (0.706); HRG–ITIH4 (0.77)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09531.1 (AGT, HPX, HRG, ITIH4; 4/47); huMAP3_10101.1 (AGT, HPX, HRG, ITIH4; 4/49); huMAP3_15040.1 (AGT, HPX, HRG, ITIH4; 4/64); huMAP3_10678.1 (AGT, HPX, HRG, ITIH4; 4/71); huMAP3_09273.1 (AGT, HPX, HRG; 3/28); huMAP3_08395.1 (AGT, HPX; 2/43)

### Novelty

This module should not be called a wholly new molecular complex or pathway. The AGT–HPX–HRG–ITIH4 core is already represented in multiple hu.MAP complexes, and several of its pairwise relationships are already supported by STRING. The particular breast–cerebrospinal-fluid co-abundance pattern may still be a potentially novel observation, especially because it connects this plasma-protein core with PODXL2, FREM2, COL5A1 and ASAH1. However, absence of database support for those peripheral links does not prove novelty. The lack of globally significant GO or KEGG enrichment, the absence of STRING functional enrichment, the liver and hepatocyte bias, and limited breast protein detection all make sample composition and circulating-protein carryover important alternative explanations. Novelty would require replication, control for blood contamination and tissue abundance, and testing whether the cross-tissue association persists independently of total plasma-protein abundance.

**Hypothesis.** Hypothesis: this conserved module reflects coordinated abundance of liver-secreted plasma proteins that participate in heme handling, coagulation, acute-phase or inflammatory regulation and extracellular matrix-associated processes, with additional covariance from brain-barrier, ependymal or stromal components. F13B may act as a network bridge between the plasma-protein core and the peripheral PODXL2, COL5A1, ASAH1 and FREM2 signals. In cerebrospinal fluid, the pattern could arise from transfer or leakage of circulating proteins together with local extracellular or barrier-related biology; in breast, it could reflect vascular or stromal abundance rather than breast-cell expression. This is a testable model, not a demonstrated mechanism, and should be evaluated using matched plasma controls, markers of blood contamination, cell-type deconvolution and independent cohorts.

### Important genes

#### F13B

- **Related proteins** (co-abundance neighbors): PODXL2 (0.99), ASAH1 (0.93), COL5A1 (0.93), ITIH4 (0.84), HRG (0.81), AGT (0.80); STRING partners: HRG (0.819)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coagulation factor XIII B chain. This gene encodes coagulation factor XIII B subunit. Coagulation factor XIII is the last zymogen to become activated in the blood coagulation cascade. Plasma factor XIII is a heterotetramer composed of 2 A subunits and 2 B subunits. The A subunits have catalytic function, and the B subunits do not have enzymatic activity and may serve as a plasma carrier molecules. Platelet factor XIII is comprise…
- **Diseases (Open Targets)**: congenital factor XIII deficiency (0.692); age-related macular degeneration (0.435); macular degeneration (0.360); coagulation protein disease (0.340); factor XIII deficiency (0.334)
- **Europe PMC papers**: 762
- **Why important**: F13B is the principal network connector, linking the largest portion of the module and directly connecting to the plasma proteins HRG and ITIH4 as well as PODXL2, ASAH1, COL5A1 and AGT. It encodes the nonenzymatic plasma carrier subunit of coagulation factor XIII and is liver- and hepatocyte-enriched, secreted to blood, and associated with coagulation and fibrin-clot formation. Its disease associations include factor XIII deficiency and coagulation protein disease, and it has a substantial literature base.
- **Conclusion**: Established: F13B is the strongest organizational candidate for the module and supports a circulating coagulation or extracellular-homeostasis interpretation. Hypothesis: its connector position may reflect coordinated plasma abundance rather than a direct mechanistic bridge between all neighboring proteins.

#### ITIH4

- **Related proteins** (co-abundance neighbors): F13B (0.84); STRING partners: HPX (0.706), HRG (0.77)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 4. The protein encoded by this gene is secreted into the blood, where it is cleaved by plasma kallikrein into two smaller forms. Expression of this gene has been detected only in liver, and it seems to be upregulated during surgical trauma. This gene is part of a cluster of similar genes on chromosome 3. Two transcript variants encoding different isoforms have been found for this gene. [provided by R…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.466); coronary artery disorder (0.417); type 2 diabetes mellitus (0.397); osteoarthritis (0.387); diabetes mellitus (0.363)
- **Europe PMC papers**: 1710
- **Why important**: ITIH4 is part of the recurrent hu.MAP core (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1) and (hu.MAP huMAP3_10678.1), and has STRING support with both HPX and HRG. It is a liver-enriched protein secreted into blood, associated with the acute-phase response, hyaluronan metabolism and cytokine response, and is described as being upregulated during surgical trauma. Its disease associations include coronary artery disorder, metabolic disease and osteoarthritis, with a substantial literature base.
- **Conclusion**: Established: ITIH4 is a biologically plausible marker of a known circulating acute-phase and extracellular-protein community. Hypothesis: it may help couple systemic injury or inflammatory state to extracellular-matrix-related covariance in the shared module.

#### HPX

- **Related proteins** (co-abundance neighbors): PODXL2 (0.81); STRING partners: ITIH4 (0.706)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_09273.1, huMAP3_08395.1
- **Function (MyGene.info)**: hemopexin. This gene encodes a plasma glycoprotein that binds heme with high affinity. The encoded protein is an acute phase protein that transports heme from the plasma to the liver and may be involved in protecting cells from oxidative stress. [provided by RefSeq, Apr 2009].
- **Diseases (Open Targets)**: panniculitis (0.116); neoplasm (0.107); familial idiopathic steroid-resistant nephrotic syndrome (0.101); hepatocellular carcinoma (0.101); focal segmental glomerulosclerosis (0.097)
- **Europe PMC papers**: 6894
- **Why important**: HPX is liver- and hepatocyte-enriched, secreted to blood, and repeatedly present with AGT, HRG and ITIH4 in hu.MAP complexes (hu.MAP huMAP3_09531.1) through (hu.MAP huMAP3_08395.1). Its STRING relationship with ITIH4 supports the plasma-protein core. Hemopexin binds heme and transports it to the liver, linking the module to heme handling and protection from oxidative stress. It also has a large literature base and disease associations involving kidney disease and neoplasia.
- **Conclusion**: Established: HPX supports a circulating heme-handling and oxidative-stress component within the known plasma-protein core. Hypothesis: variation in heme burden or vascular injury could be one physiological driver of the observed cross-tissue co-abundance.

#### HRG

- **Related proteins** (co-abundance neighbors): F13B (0.81); STRING partners: F13B (0.819), ITIH4 (0.77)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_09273.1
- **Function (MyGene.info)**: histidine rich glycoprotein. This histidine-rich glycoprotein contains two cystatin-like domains and is located in plasma and platelets. The physiological function has not been determined but it is known that the protein binds heme, dyes and divalent metal ions. The encoded protein also has a peptide that displays antimicrobial activity against C. albicans, E. coli, S. aureus, P. aeruginosa, and E. faecalis. It can inhibit ro…
- **Diseases (Open Targets)**: hereditary thrombophilia due to congenital histidine-rich (poly-L) glycoprotein deficiency (0.712); Abnormality of refraction (0.321); thrombotic disease (0.119); hepatocellular carcinoma (0.111); neoplasm (0.110)
- **Europe PMC papers**: 3625
- **Why important**: HRG is liver- and hepatocyte-enriched and secreted into blood. It connects to F13B and ITIH4 in STRING and appears with AGT, HPX and ITIH4 across hu.MAP complexes (hu.MAP huMAP3_09531.1) through (hu.MAP huMAP3_09273.1). Its described activities include binding heme, divalent metals, heparin, thrombospondin and plasminogen, as well as regulation of platelet activation, cell adhesion and immune responses. It has a substantial literature base and disease associations involving hereditary deficiency and thrombophilia.
- **Conclusion**: Established: HRG is a strong marker of the known plasma, coagulation and adhesion-associated core. Hypothesis: HRG could contribute to covariance between vascular, platelet-related and extracellular-matrix states, but the module does not demonstrate such causation.

#### PODXL2

- **Related proteins** (co-abundance neighbors): F13B (0.99), FREM2 (0.90), HPX (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: podocalyxin like 2. This gene is a member of the CD34 family of cell surface transmembrane proteins, which are characterized by an N-terminal extracellular mucin domain, globular and stalk domains, a single pass transmembrane region, and a charged cytoplasmic tail. The encoded protein is a ligand for vascular selectins. [provided by RefSeq, Oct 2012].
- **Diseases (Open Targets)**: refractive error (0.414); ovarian neoplasm (0.357); primary angle-closure glaucoma (0.311); Abnormality of refraction (0.283); sialolithiasis (0.221)
- **Europe PMC papers**: 334
- **Why important**: PODXL2 is directly connected to the module hub F13B and also links to FREM2 and HPX. Unlike the dominant liver-secreted genes, it is tissue-enhanced in brain and pituitary contexts, is associated with brain neuronal cell types, is located at the Golgi apparatus, and is detected in breast by HPA. Its encoded protein is a cell-surface mucin-like transmembrane protein and ligand for vascular selectins, with an annotation related to leukocyte tethering or rolling. It has fewer literature records than the major plasma proteins, making it a useful peripheral candidate.
- **Conclusion**: Established: PODXL2 provides a plausible tissue or vascular-interface component distinct from the liver-secreted core. Hypothesis: its covariance with plasma proteins may reflect vascular barrier, endothelial-interface or local brain-associated biology, although blood carryover and indirect abundance effects remain viable explanations.

## Module 8

**Tissue pair**: breast and cerebrospinal_fluid  
**Genes (16)**: APOA4, CD99L2, CACNA2D2, CPE, C6, C8B, ENDOD1, FGFR1, FGB, KIT, NRP1, POFUT4, OLFML1, OMD, PLXDC2, SELENOP

### Function

The module does not support a statistically significant GO or KEGG functional assignment: no term passed global correction. Its biology is therefore best inferred cautiously from its members and network. The strongest themes are extracellular and circulating-protein biology, complement and membrane-attack-complex components through C6 and C8B, coagulation and cell-matrix biology through FGB, lipid transport through APOA4, and receptor or adhesion-associated signaling through CD99L2, KIT, NRP1, FGFR1, PLXDC2 and OLFML1. The co-abundance graph is sparse and appears to contain several small relationship pairs rather than one well-established pathway. The module may therefore represent coordinated abundance of plasma-derived proteins together with signals from stromal, vascular, epithelial or immune-related cells, rather than a single intracellular process. These interpretations are hypotheses supported by the annotations, not globally significant enrichment results.

**Cell composition.** The module is strongly compatible with a circulating or extracellular-protein signal. Most members are secreted or associated with extracellular, vesicular or membrane compartments, and the HPA summary identifies many secreted genes. C6, C8B, FGB, APOA4 and SELENOP are especially consistent with plasma or liver- and intestine-derived proteins. HPA tissue evidence is concentrated mainly in liver and intestine, with additional signals from brain, lung, skeletal muscle and vasculature. Several genes are associated with fibroblasts, fibro-adipogenic progenitors, hepatocytes, macrophages or other specialized cell types, but most genes are not specifically enriched in immune cells. This pattern argues against interpreting the module as a purely breast- or cerebrospinal-fluid-specific cellular program. In breast, protein detection is present for a subset of members, while the HPA summary has no matching cerebrospinal-fluid tissue category. Shared plasma carryover, vascular content, extracellular vesicles, or shared cell types could therefore contribute substantially to the observed conservation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a small set of high-confidence relationships: C6 with C8B, CD99L2 with KIT, and FGFR1 with NRP1. The C6-C8B relationship is biologically coherent because both are complement membrane-attack-complex components. The CD99L2-KIT and FGFR1-NRP1 relationships suggest possible cell-surface adhesion, receptor and signaling structure, but they do not establish that the proteins physically form one complex in this module. hu.MAP repeatedly places FGB and APOA4 together in large, blood-protein-rich complexes (hu.MAP huMAP3_07432.1) through (hu.MAP huMAP3_10101.1) and (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_10678.1), supporting a shared extracellular or plasma-associated abundance pattern rather than a compact module-specific complex. POFUT4 and CACNA2D2 recur together in complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), although those complexes contain many additional trafficking, glycosylation and membrane proteins. Overall, known relationships explain selected edges and substructures, but the available interaction evidence does not support one unified canonical complex.

**STRING interactions (score >= 0.7)**: 3 of 120 gene pairs: C6–C8B (0.984); CD99L2–KIT (0.723); FGFR1–NRP1 (0.826)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07432.1 (FGB, APOA4; 2/18); huMAP3_09434.1 (FGB, APOA4; 2/33); huMAP3_08395.1 (FGB, APOA4; 2/43); huMAP3_09531.1 (FGB, APOA4; 2/47); huMAP3_10101.1 (FGB, APOA4; 2/49); huMAP3_06775.1 (POFUT4, CACNA2D2; 2/60); huMAP3_15040.1 (FGB, APOA4; 2/64); huMAP3_10678.1 (FGB, APOA4; 2/71); huMAP3_09327.1 (POFUT4, CACNA2D2; 2/93)

### Novelty

The exact conserved breast–cerebrospinal-fluid co-abundance module may be a new systems-level observation, because the supplied evidence does not identify an established prior module with this precise membership and cross-tissue context. However, its individual components and several relationships are not novel: complement biology, fibrinogen, apolipoprotein biology, receptor signaling and the hu.MAP associations are already established. The plasma-like composition also provides a non-novel explanation based on shared circulating proteins or sample composition. Absence of a complete match in STRING or hu.MAP would not by itself prove discovery. The defensible conclusion is that the conservation pattern may be novel, while the underlying molecular functions are largely known and the module requires independent replication, control for plasma contamination and cell-composition adjustment before being called a new biological mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared extracellular vascular interface present in both sample groups, combining circulating liver- and intestine-derived proteins with local stromal, endothelial, neural or immune-associated signals. In this model, C6 and C8B represent complement activity, FGB represents coagulation and matrix-interaction potential, APOA4 and SELENOP represent lipid and selenium transport in the extracellular compartment, and the receptor-associated genes represent tissue or cell-state signals that covary with that extracellular milieu. The sparse network may arise from several partially coupled processes—plasma protein abundance, complement/coagulation exposure, and receptor or adhesion signaling—rather than from a single molecular machine. This hypothesis should be tested by measuring plasma-protein depletion, cerebrospinal-fluid and breast cell-type composition, and independent protein-level replication.

### Important genes

#### C8B

- **Related proteins** (co-abundance neighbors): POFUT4 (0.95), CD99L2 (0.81), CACNA2D2 (0.80); STRING partners: C6 (0.984)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C8 beta chain. This gene encodes one of the three subunits of the complement component 8 (C8) protein. C8 is composed of equimolar amounts of alpha, beta and gamma subunits, which are encoded by three separate genes. C8 is one component of the membrane attack complex, which mediates cell lysis, and it initiates membrane penetration of the complex. This protein mediates the interaction of C8 with the C5b-7 membra…
- **Diseases (Open Targets)**: type II complement component 8 deficiency (0.705); immunodeficiency due to a late component of complement deficiency (0.558); complement deficiency (0.462); hereditary disease (0.193); insomnia (0.167)
- **Europe PMC papers**: 1262
- **Why important**: C8B is one of the more connected members of the module and is directly linked to C6 in STRING with very high confidence. Its established function is as a subunit of complement C8 within the membrane attack complex, and its HPA profile points to liver, hepatocytes and secretion into blood. It therefore anchors the complement and circulating-protein interpretation. Its disease associations include complement C8 deficiency and related immunodeficiency, and its literature base is substantial.
- **Conclusion**: Established evidence supports C8B as a circulating complement component and as a biologically coherent partner of C6. Its presence does not demonstrate active complement-mediated lysis in either tissue group; that interpretation remains a hypothesis.

#### C6

- **Related proteins** (co-abundance neighbors): POFUT4 (0.94); STRING partners: C8B (0.984)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C6. This gene encodes a component of the complement cascade. The encoded protein is part of the membrane attack complex that can be incorporated into the cell membrane and cause cell lysis. Mutations in this gene are associated with complement component-6 deficiency. Transcript variants encoding the same protein have been described.[provided by RefSeq, Nov 2012].
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.753); complement deficiency (0.464); hereditary disease (0.416); male reproductive organ cancer (0.257); benign neoplasm of brain (0.199)
- **Europe PMC papers**: 88422
- **Why important**: C6 is a complement membrane-attack-complex component, is secreted to blood, and is enriched in liver-associated HPA evidence. It connects in the module to POFUT4 and has a high-confidence STRING relationship with C8B. Its disease associations include inherited C6 deficiency and immunodeficiency. The very large literature volume makes its annotation particularly well established.
- **Conclusion**: Established evidence supports C6 as a strong marker of complement and plasma biology in this module. The module data alone cannot establish complement activation, cleavage or functional membrane attack.

#### FGB

- **Related proteins** (co-abundance neighbors): KIT (0.85); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07432.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: fibrinogen beta chain. The protein encoded by this gene is the beta component of fibrinogen, a blood-borne glycoprotein comprised of three pairs of nonidentical polypeptide chains. Following vascular injury, fibrinogen is cleaved by thrombin to form fibrin which is the most abundant component of blood clots. In addition, various cleavage products of fibrinogen and fibrin regulate cell adhesion and spreading, display vas…
- **Diseases (Open Targets)**: congenital afibrinogenemia (0.786); familial dysfibrinogenemia (0.705); congenital fibrinogen deficiency (0.622); familial hypodysfibrinogenemia (0.597); cancer (0.592)
- **Europe PMC papers**: 4215
- **Why important**: FGB is a secreted liver- and hepatocyte-associated fibrinogen chain with a central role in blood coagulation, platelet activation, fibrinolysis and cell-matrix adhesion. It connects to KIT in the co-abundance graph and recurs with APOA4 across many hu.MAP complexes (hu.MAP huMAP3_07432.1) through (hu.MAP huMAP3_10101.1) and (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_10678.1). Its disease associations include inherited fibrinogen disorders, and its literature base is strong. It is therefore important both biologically and as a possible indicator of plasma contribution.
- **Conclusion**: Established evidence supports FGB as a coagulation and circulating-protein marker. Its module membership should not be interpreted as evidence that coagulation is occurring locally in breast or cerebrospinal fluid without orthogonal functional measurements.

#### APOA4

- **Related proteins** (co-abundance neighbors): CD99L2 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07432.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: apolipoprotein A4. Apoliprotein (apo) A-IV gene contains 3 exons separated by two introns. A sequence polymorphism has been identified in the 3'UTR of the third exon.  The primary translation product is a 396-residue preprotein which after proteolytic processing is secreted its primary site of synthesis, the intestine, in association with chylomicron particles.  Although its precise function is not known, apo A-IV i…
- **Diseases (Open Targets)**: tubulointerstitial kidney disease, autosomal dominant, 2 (0.482); AL amyloidosis (0.463); metabolic syndrome (0.425); familial hyperlipidemia (0.359); diabetes mellitus (0.336)
- **Europe PMC papers**: 4955
- **Why important**: APOA4 is an intestine-derived secreted apolipoprotein involved in lipid transport, cholesterol biology and mucosal innate immune functions. It is repeatedly paired with FGB in hu.MAP complexes (hu.MAP huMAP3_07432.1) through (hu.MAP huMAP3_10101.1) and (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_10678.1), making it an important indicator of the extracellular plasma-like component of the module. It has associations with metabolic syndrome, familial hyperlipidemia and related disorders, and has a substantial literature base.
- **Conclusion**: Established evidence supports APOA4 as an intestinal, secreted lipid-transport protein and as part of a recurring plasma-protein complex pattern. Its presence more strongly supports shared circulating or extracellular composition than a breast–cerebrospinal-fluid-specific signaling pathway.

#### NRP1

- **Related proteins** (co-abundance neighbors): KIT (0.86), FGFR1 (0.82); STRING partners: FGFR1 (0.826)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Mitochondria; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neuropilin 1. This gene encodes one of two neuropilins, which contain specific protein domains which allow them to participate in several different types of signaling pathways that control cell migration. Neuropilins contain a large N-terminal extracellular domain, made up of complement-binding, coagulation factor V/VIII, and meprin domains. These proteins also contains a short membrane-spanning domain and a sm…
- **Diseases (Open Targets)**: COVID-19 (0.490); Abnormality of the skeletal system (0.466); mathematical ability (0.355); migraine disorder (0.346); obstructive sleep apnea syndrome (0.345)
- **Europe PMC papers**: 12192
- **Why important**: NRP1 forms one of the clearest signaling substructures in the module through its high-confidence STRING relationship with FGFR1 and its co-abundance connection to KIT. It is annotated for angiogenesis, vascular morphogenesis, endothelial proliferation and neuronal migration, providing a plausible bridge between vascular, stromal and neural contexts. HPA evidence includes fibro-adipogenic progenitors, Hofbauer cells, Kupffer cells and plasmacytoid dendritic cells, and its disease and literature record is broad.
- **Conclusion**: Established evidence supports NRP1 as a multifunctional receptor-associated signaling molecule with vascular and neural relevance. The module does not establish a functional NRP1-FGFR1-KIT signaling complex; that integrated mechanism is a hypothesis requiring cell-specific and biochemical validation.

## Module 9

**Tissue pair**: breast and cerebrospinal_fluid  
**Genes (11)**: B3GALNT1, GLB1, GUSB, LRIG1, LRP1, LTBP1, MSLN, PLXNB2, PON1, PTPRG, SGCE

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established pathway assignment. Its gene annotations and co-abundance structure instead suggest convergence across extracellular and cell-surface biology: cell adhesion and receptor signaling, extracellular-matrix regulation, lipid handling, glycosphingolipid and glycosaminoglycan metabolism, and lysosomal or vesicular processing. SGCE is the main network hub and connects membrane or matrix-associated genes with PON1, LRP1, and PLXNB2. The pattern is therefore best interpreted as a mixed extracellular-interface and clearance module, not as a single proven biochemical pathway. The biological interpretation remains provisional because the module is small and its edges are co-abundance relationships rather than demonstrated physical interactions.

**Cell composition.** The module has a strong extracellular and circulating-protein component. PON1 is secreted to blood and is tissue enriched in liver and hepatocytes, while LTBP1 is secreted to extracellular matrix. Six module genes are annotated as secreted, and several others are membrane, vesicular, or extracellular-interface proteins. HPA evidence also points to adipocytes, hepatocytes, fibroblasts, vascular cells, epithelial cells, and several immune populations. LRP1 and PLXNB2 show enrichment in monocyte and dendritic-cell populations, and other genes show blood-cell or myeloid associations. This mixture makes blood-derived protein, vascular or stromal material, and shared immune or support-cell content plausible contributors to the breast and cerebrospinal-fluid signal. It does not establish that the module originates from a single cell type. Breast protein detection is present for some members, whereas HPA provides no matching cerebrospinal-fluid tissue assessment, so the cross-tissue interpretation should be treated cautiously.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no high-confidence pairwise interactions and no supplementary functional enrichment for this gene set. Thus, the co-abundance edges should not be presented as established protein-protein interactions. hu.MAP provides the only direct complex-level support: PLXNB2 and GUSB occur together in huMAP complex C1 and also in huMAP complex C2. In both cases they are only a small subset of much larger complexes, and the two complexes have different confidence annotations. No other module genes are reported in hu.MAP complexes. These findings support limited known molecular context for the PLXNB2-GUSB pair, but they do not validate the entire module as one physical complex.

**STRING interactions (score >= 0.7)**: 0 of 55 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (PLXNB2, GUSB; 2/60); huMAP3_09327.1 (PLXNB2, GUSB; 2/93)

### Novelty

The module may represent a previously unreported co-abundance pattern, but it cannot be called a definitively new biological discovery. Its lack of STRING interactions and lack of broad hu.MAP representation indicate that the precise cross-tissue co-abundance relationship is not well captured by those resources, yet absence from a database is not evidence of novelty. Several members have established functions and substantial literature, including LRP1, PON1, GUSB, MSLN, PLXNB2, and SGCE, and the observed combination can plausibly arise from circulating proteins, extracellular matrix, vesicles, or shared immune and stromal content. A novelty claim would require replication in independent breast and cerebrospinal-fluid datasets, control for blood contamination and cell composition, and comparison with previously reported tissue-pair modules.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of extracellular and vesicular proteins contributed by blood, vascular or stromal cells, and shared support or immune populations in breast and cerebrospinal-fluid samples. Within this mixture, LTBP1 could represent matrix-associated TGF-beta storage and activation potential, LRP1 could represent receptor-mediated uptake and clearance, PON1 could represent circulating HDL-associated lipid and oxidant handling, and GUSB with GLB1 could represent lysosomal degradation of extracellular glycoconjugates. SGCE, PTPRG, PLXNB2, and MSLN could connect this extracellular environment to cell-surface adhesion, migration, and signaling. This is a mechanistic model rather than an established pathway assignment and should be tested with cell-type deconvolution, blood-protein controls, matched protein and transcript measurements, and perturbation or localization experiments.

### Important genes

#### SGCE

- **Related proteins** (co-abundance neighbors): PTPRG (0.90), LRP1 (0.88), LTBP1 (0.83), PON1 (0.81), PLXNB2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sarcoglycan epsilon. This gene encodes the epsilon member of the sarcoglycan family. Sarcoglycans are transmembrane proteins that are components of the dystrophin-glycoprotein complex, which link the actin cytoskeleton to the extracellular matrix. Unlike other family members which are predominantly expressed in striated muscle, the epsilon sarcoglycan is more broadly expressed. Mutations in this gene are associated wi…
- **Diseases (Open Targets)**: myoclonus-dystonia syndrome (0.757); hereditary disease (0.471); movement disorder (0.283); luminal A breast carcinoma (0.189); schizophrenia (0.177)
- **Europe PMC papers**: 1747
- **Why important**: SGCE has the strongest network position in the module, linking PTPRG, LRP1, LTBP1, PON1, and PLXNB2. Its established role as a broadly expressed sarcoglycan links membrane structure, cytoskeletal-extracellular-matrix coupling, and cell adhesion. It also has a disease association with myoclonus-dystonia syndrome and substantial literature, making it a useful network anchor even though it has no STRING or hu.MAP support here.
- **Conclusion**: Established evidence supports SGCE as the module hub and as a membrane-associated structural protein involved in cell-matrix biology. The hypothesis that it coordinates the other module proteins is not established; the hub position may instead reflect shared abundance from a particular cellular or tissue compartment.

#### LRP1

- **Related proteins** (co-abundance neighbors): SGCE (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LDL receptor related protein 1. This gene encodes a member of the low-density lipoprotein receptor family of proteins. The encoded preproprotein is proteolytically processed by furin to generate 515 kDa and 85 kDa subunits that form the mature receptor (PMID: 8546712). This receptor is involved in several cellular processes, including intracellular signaling, lipid homeostasis, and clearance of apoptotic cells. In addition, the …
- **Diseases (Open Targets)**: neurodegenerative disease (0.514); keratosis pilaris atrophicans (0.499); developmental dysplasia of the hip (0.466); Alzheimer disease (0.462); Parkinson disease (0.443)
- **Europe PMC papers**: 10645
- **Why important**: LRP1 is directly connected to SGCE and is annotated as a multifunctional receptor involved in lipid homeostasis, receptor-mediated endocytosis, phagocytosis, and clearance of extracellular material. HPA links it to adipocytes, fibroblasts, hepatocytes, Kupffer cells, and monocyte or dendritic-cell populations, fitting the module's mixed vascular, stromal, hepatic, and immune composition. It also has extensive disease-oriented literature, including neurodegenerative disease associations.
- **Conclusion**: Established evidence supports LRP1 as a plausible interface between extracellular protein clearance, lipid handling, and immune or stromal cell biology. Its participation in a breast-cerebrospinal-fluid mechanism remains a hypothesis because the module contains no significant enrichment and LRP1 has only one observed module edge.

#### PON1

- **Related proteins** (co-abundance neighbors): MSLN (0.84), SGCE (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: paraoxonase 1. This gene encodes a member of the paraoxonase family of enzymes and exhibits lactonase and ester hydrolase activity. Following synthesis in the kidney and liver, the enzyme is secreted into the circulation, where it binds to high density lipoprotein (HDL) particles and hydrolyzes thiolactones and xenobiotics, including paraoxon, a metabolite of the insecticide parathion. Polymorphisms in this gene…
- **Diseases (Open Targets)**: diabetic retinopathy (0.377); atopic eczema (0.354); obesity disorder (0.306); idiopathic pulmonary fibrosis (0.202); malunion fracture (0.148)
- **Europe PMC papers**: 5619
- **Why important**: PON1 is a secreted blood protein with lactonase and ester-hydrolase activity, HDL association, and roles in cholesterol efflux and protection from lipoprotein oxidation. It is tissue enriched in liver and cell-type enriched in hepatocytes, and it connects to SGCE and MSLN in the module. Its circulating nature makes it especially important for evaluating blood contribution to the shared tissue signal.
- **Conclusion**: Established evidence supports PON1 as a circulating enzyme involved in lipid and xenobiotic-related metabolism. Its presence strongly motivates a blood or plasma contribution hypothesis, but it does not demonstrate a breast or cerebrospinal-fluid-specific biological process.

#### GUSB

- **Related proteins** (co-abundance neighbors): LRIG1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: glucuronidase beta. This gene encodes a hydrolase that degrades glycosaminoglycans, including heparan sulfate, dermatan sulfate, and chondroitin-4,6-sulfate. The enzyme forms a homotetramer that is localized to the lysosome. Mutations in this gene result in mucopolysaccharidosis type VII. Alternative splicing results in multiple transcript variants. There are many pseudogenes of this locus in the human genome.[provid…
- **Diseases (Open Targets)**: mucopolysaccharidosis type 7 (0.878); mucopolysaccharidosis type 6 (0.439); hereditary disease (0.415); Non-immune hydrops fetalis (0.391); mucopolysaccharidosis (0.374)
- **Europe PMC papers**: 7068
- **Why important**: GUSB is a lysosomal hydrolase that degrades several glycosaminoglycans and is associated with mucopolysaccharidosis. It connects to LRIG1 and shares membership with PLXNB2 in huMAP complexes C1 and C2, providing the clearest complex-level context in the module. HPA places it in vesicles and in Hofbauer and Kupffer cells, consistent with degradative and phagocytic compartments.
- **Conclusion**: Established evidence supports GUSB as a lysosomal glycosaminoglycan-degradation enzyme and supports limited complex context through C1 and C2. A coordinated lysosomal clearance role for the whole module is plausible but remains hypothetical because there is no globally significant enrichment and no STRING interaction evidence.

#### LTBP1

- **Related proteins** (co-abundance neighbors): SGCE (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: latent transforming growth factor beta binding protein 1. The protein encoded by this gene belongs to the family of latent TGF-beta binding proteins (LTBPs). The secretion and activation of TGF-betas is regulated by their association with latency-associated proteins and with latent TGF-beta binding proteins. The product of this gene targets latent complexes of transforming growth factor beta to the extracellular matrix, where the latent cytokine is subse…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.551); diverticular disease (0.523); autosomal recessive cutis laxa type 2 (0.507); osteoarthritis, knee (0.485); osteoarthritis, hip (0.467)
- **Europe PMC papers**: 2354
- **Why important**: LTBP1 is secreted to extracellular matrix and regulates storage, localization, and activation of latent TGF-beta complexes. It is tissue enhanced in blood vessel and shows cell-type associations with cardiomyocytes, fibroblasts, hepatic stellate cells, and progenitor populations. Its edge to SGCE gives the module a direct extracellular-matrix and growth-factor-regulation dimension.
- **Conclusion**: Established evidence supports LTBP1 as an extracellular-matrix regulator of latent TGF-beta biology. The hypothesis that it links vascular or stromal matrix remodeling to the other module proteins is biologically reasonable but is not demonstrated by the co-abundance data alone.

#### PLXNB2

- **Related proteins** (co-abundance neighbors): SGCE (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location None; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: plexin B2. Members of the B class of plexins, such as PLXNB2 are transmembrane receptors that participate in axon guidance and cell migration in response to semaphorins (Perrot et al. (2002) [PubMed 12183458]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Intellectual disability (0.519); amelogenesis imperfecta (0.518); sensorineural hearing loss disorder (0.516); cutaneous melanoma (0.486); neurodegenerative disease (0.455)
- **Europe PMC papers**: 2109
- **Why important**: PLXNB2 is a cell-surface plexin involved in semaphorin-responsive axon guidance, cell migration, adhesion, endocytosis, and neurodevelopmental processes. It connects to SGCE and is associated by HPA with epithelial populations and several monocyte or dendritic-cell groups. It is also one of the two module members present with GUSB in huMAP complexes C1 and C2, making it important for both signaling interpretation and the limited known-complex evidence.
- **Conclusion**: Established evidence supports PLXNB2 as a membrane receptor involved in migration, adhesion, and neural or epithelial signaling, with limited complex context through C1 and C2. A role in coordinating extracellular signaling across breast and cerebrospinal-fluid compartments is a hypothesis, not a demonstrated function of this module.

## Module 10

**Tissue pair**: breast and cerebrospinal_fluid  
**Genes (15)**: B3GNT2, CD163, C5, CPXM1, F12, FSTL1, ICOSLG, DGCR2, IL6ST, ITGAM, MMRN2, PCDH7, PLXNB1, STAB1, SERPINA7

### Function

The module is best interpreted as a mixed circulating innate-immune, scavenger-receptor, complement/coagulation, and vascular or cell-adhesion signature rather than as a single demonstrated biochemical pathway. IL6ST is the central network connector and is a cytokine-receptor signal transducer associated with inflammatory and JAK-STAT-related signaling. ITGAM, CD163, and STAB1 point toward monocyte/macrophage adhesion, phagocytosis, endocytosis, hemoglobin-complex clearance, and scavenging. C5 and F12 represent complement and intrinsic coagulation or kallikrein-kinin biology, while PLXNB1, PCDH7, and MMRN2 support cell-shape, adhesion, extracellular-matrix, vascular, and angiogenesis-related interpretation. However, no GO or KEGG term passed global correction, so these functional themes are gene-level and network-level interpretations, not globally significant enrichment claims. There are no STRING functional-enrichment terms.

**Cell composition.** The module is strongly compatible with a blood-derived or blood-contaminated component shared between breast and cerebrospinal-fluid samples. Many members are secreted to blood or extracellular compartments, including IL6ST, FSTL1, CPXM1, C5, F12, MMRN2, CD163, and SERPINA7. C5, F12, and SERPINA7 are liver-enriched and hepatocyte-associated in HPA, making circulating plasma contribution a plausible explanation. CD163, STAB1, and ITGAM are associated with monocytes, macrophages, Kupffer cells, Hofbauer cells, microglia, or myeloid populations, and HPA also highlights classical monocytes and other blood-cell categories. Several genes are broadly expressed or have low tissue specificity, whereas the remainder show cell-type rather than organ-specific patterns. Breast protein detection is limited across the module, and HPA has no matching cerebrospinal-fluid tissue category; therefore shared sample composition, vascular material, plasma proteins, or shared myeloid cells should be considered before assigning a breast-to-CSF tissue mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The known STRING relationships are CD163 with ITGAM and CD163 with STAB1. These links are biologically coherent with a monocyte/macrophage scavenging and adhesion program and provide independent support for that small subnetwork. The remaining module relationships are not represented as high-confidence STRING interactions in the fact sheet, despite strong co-abundance edges involving IL6ST, PLXNB1, B3GNT2, and several secreted or extracellular proteins. hu.MAP contains no complex with multiple module members. Thus, the co-abundance structure is not simply a known canonical protein complex; it combines a small established myeloid receptor neighborhood with broader correlated plasma, vascular, and membrane-associated signals.

**STRING interactions (score >= 0.7)**: 2 of 105 gene pairs: CD163–ITGAM (0.819); CD163–STAB1 (0.727)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This should not be called a definitively new biological pathway. The CD163-ITGAM-STAB1 relationships and the individual functions of cytokine signaling, macrophage scavenging, complement, coagulation, and adhesion are established. The potentially novel aspect is the cross-tissue co-abundance configuration linking these established components with PLXNB1, B3GNT2, FSTL1, extracellular-matrix proteins, and liver-derived circulating proteins in breast and cerebrospinal fluid. Because there is no globally significant GO or KEGG enrichment, no STRING functional enrichment, and no hu.MAP complex support, the module currently provides a new observational association rather than proof of a new molecular mechanism. Its novelty should be tested against independent cohorts, cell-composition estimates, plasma-protein measurements, and targeted validation.

**Hypothesis.** Hypothesis: the shared module reflects a circulating or vascular-interface inflammatory-clearance state in which plasma proteins and myeloid cells jointly contribute to the measured abundance pattern. In this model, IL6ST-associated cytokine responsiveness, ITGAM-mediated leukocyte adhesion or phagocytosis, CD163-mediated hemoglobin-complex clearance, and STAB1-mediated scavenging or endocytosis form the cellular core, while C5 and F12 provide circulating innate-defense and contact-system context. PLXNB1, PCDH7, MMRN2, and FSTL1 may represent vascular, extracellular-matrix, or cell-adhesion correlates rather than direct molecular partners. An alternative explanation is technical or biological carryover of blood and shared myeloid-cell abundance, which must be distinguished from coordinated regulation within breast or cerebrospinal-fluid tissue.

### Important genes

#### IL6ST

- **Related proteins** (co-abundance neighbors): B3GNT2 (0.96), C5 (0.93), F12 (0.93), ITGAM (0.92), PLXNB1 (0.91), STAB1 (0.89), CD163 (0.83), CPXM1 (0.82), FSTL1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: interleukin 6 cytokine family signal transducer. The protein encoded by this gene is a signal transducer shared by many cytokines, including interleukin 6 (IL6), ciliary neurotrophic factor (CNTF), leukemia inhibitory factor (LIF), and oncostatin M (OSM). This protein functions as a part of the cytokine receptor complex. The activation of this protein is dependent upon the binding of cytokines to their receptors. vIL6, a protein related to IL6 a…
- **Diseases (Open Targets)**: Autosomal recessive hyper-IgE syndrome (0.703); Stuve-Wiedemann syndrome 2 (0.668); hyper-IgE recurrent infection syndrome 4A, autosomal dominant (0.658); neuromyelitis optica (0.569); immunodeficiency 94 with autoinflammation and dysmorphic facies (0.424)
- **Europe PMC papers**: 11529
- **Why important**: IL6ST is the strongest network connector in the module and links inflammatory, membrane, scavenger, adhesion, complement, and extracellular proteins. Its established role as a shared signal-transducing component for IL six family cytokines makes it a plausible organizing marker for cytokine-responsive biology. It has extensive literature and disease associations involving immune dysregulation and inflammatory disorders. HPA places it at the plasma membrane and in blood secretion, with low tissue specificity, which also makes it relevant to the possibility of a circulating or mixed-cell signal.
- **Conclusion**: Established evidence supports IL6ST as a cytokine-receptor signal transducer and as the network-level anchor of this module. It is a strong marker of the module's inflammatory context, but the co-abundance data do not establish that IL6ST directly regulates the other module members.

#### ITGAM

- **Related proteins** (co-abundance neighbors): ICOSLG (0.95), B3GNT2 (0.92), IL6ST (0.92); STRING partners: CD163 (0.819)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha M. This gene encodes the integrin alpha M chain. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain. This I-domain containing alpha integrin combines with the beta 2 chain (ITGB2) to form a leukocyte-specific integrin referred to as macrophage receptor 1 ('Mac-1'), or inactivated-C3b (iC3b) receptor 3 ('CR3'). The alpha M beta 2 integrin is important in…
- **Diseases (Open Targets)**: systemic lupus erythematosus (0.416); IgA glomerulonephritis (0.338); autoimmune disorder of musculoskeletal system (0.265); hearing loss disorder (0.264); cutaneous lupus erythematosus (0.133)
- **Europe PMC papers**: 8991
- **Why important**: ITGAM is a leukocyte integrin subunit that forms Mac one with ITGB2 and supports monocyte and neutrophil adhesion, complement-receptor activity, phagocytosis, and endocytosis. It is enriched in myeloid-related HPA cell types and is connected in STRING to CD163, providing an established relationship within the module. Its network position connects the central IL6ST region to B3GNT2 and ICOSLG, linking inflammatory co-abundance with immune-cell adhesion and activation.
- **Conclusion**: Established evidence identifies ITGAM as a myeloid-cell adhesion and phagocytosis marker. In this module it supports a monocyte or macrophage contribution, but its presence alone cannot distinguish true tissue-resident myeloid biology from variable blood-cell abundance.

#### CD163

- **Related proteins** (co-abundance neighbors): IL6ST (0.83); STRING partners: ITGAM (0.819), STAB1 (0.727)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD163 molecule. The protein encoded by this gene is a member of the scavenger receptor cysteine-rich (SRCR) superfamily, and is exclusively expressed in monocytes and macrophages. It functions as an acute phase-regulated receptor involved in the clearance and endocytosis of hemoglobin/haptoglobin complexes by macrophages, and may thereby protect tissues from free hemoglobin-mediated oxidative damage. This protein…
- **Diseases (Open Targets)**: arthropathy (0.205); acute tonsillitis (0.205); adolescent idiopathic scoliosis (0.193); stroke disorder (0.191); CINCA syndrome (0.185)
- **Europe PMC papers**: 31467
- **Why important**: CD163 is a monocyte and macrophage scavenger receptor involved in clearance and endocytosis of hemoglobin-haptoglobin complexes and in innate immune responses. It has extensive literature, strong myeloid-cell specificity in HPA, and known STRING relationships with both ITGAM and STAB1. These features make it the clearest cellular marker of a macrophage or monocyte-associated substructure within the module.
- **Conclusion**: Established evidence supports CD163 as a macrophage or monocyte scavenging marker and as part of a known receptor neighborhood. Its co-abundance with plasma proteins is more parsimoniously interpreted as a myeloid or blood-associated signature than as evidence that CD163 directly complexes with every module member.

#### STAB1

- **Related proteins** (co-abundance neighbors): IL6ST (0.89), PLXNB1 (0.87); STRING partners: CD163 (0.727)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: stabilin 1. This gene encodes a large, transmembrane receptor protein which may function in angiogenesis, lymphocyte homing, cell adhesion, or receptor scavenging. The protein contains 7 fasciclin, 16 epidermal growth factor (EGF)-like, and 2 laminin-type EGF-like domains as well as a C-type lectin-like hyaluronan-binding Link module. The protein is primarily expressed on sinusoidal endothelial cells of liver…
- **Diseases (Open Targets)**: isolated hyperferritinemia (0.365); Hodgkins lymphoma (0.312); intelligence (0.256); esophageal disorder (0.152); Abnormality of the skeletal system (0.130)
- **Europe PMC papers**: 1787
- **Why important**: STAB1 is a transmembrane scavenger receptor associated with endocytosis, cell adhesion, lymphocyte homing, angiogenesis, and clearance functions. HPA links it to macrophages, microglia, Kupffer cells, and monocyte or myeloid dendritic-cell categories. Its known STRING relationship with CD163 and its connection to IL6ST and PLXNB1 place it at the interface of scavenging, inflammatory signaling, and vascular or cellular adhesion.
- **Conclusion**: Established evidence supports STAB1 as a scavenger and adhesion receptor expressed in specialized macrophage and endothelial contexts. In this module it strengthens the interpretation of a myeloid-clearance signature, while any mechanistic connection to the other co-abundant proteins remains hypothetical.

#### C5

- **Related proteins** (co-abundance neighbors): IL6ST (0.93); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C5. This gene encodes a component of the complement system, a part of the innate immune system that plays an important role in inflammation, host homeostasis, and host defense against pathogens. The encoded preproprotein is proteolytically processed to generate multiple protein products, including the C5 alpha chain, C5 beta chain, C5a anaphylatoxin and C5b. The C5 protein is comprised of the C5 alpha…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.744); paroxysmal nocturnal hemoglobinuria (0.610); myasthenia gravis (0.586); atypical hemolytic-uremic syndrome (0.544); neuromyelitis optica (0.516)
- **Europe PMC papers**: 81450
- **Why important**: C5 is a highly studied liver-derived secreted complement component with roles in complement activation, chemotaxis, inflammation, and host defense. Its connection to IL6ST in the module links a circulating innate-immune protein to the central cytokine-signaling pattern. HPA identifies liver and hepatocyte enrichment and secretion to blood, making C5 particularly informative for assessing plasma contribution and potential blood carryover.
- **Conclusion**: Established evidence supports C5 as a circulating complement protein and inflammatory mediator. In this module it is more likely to report the extracellular or plasma milieu than to indicate a direct C5-IL6ST molecular interaction.

#### F12

- **Related proteins** (co-abundance neighbors): IL6ST (0.93); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coagulation factor XII. This gene encodes coagulation factor XII which circulates in blood as a zymogen. This single chain zymogen is converted to a two-chain serine protease with an heavy chain (alpha-factor XIIa) and a light chain. The heavy chain contains two fibronectin-type domains, two epidermal growth factor (EGF)-like domains, a kringle domain and a proline-rich domain, whereas the light chain contains only a cat…
- **Diseases (Open Targets)**: congenital factor XII deficiency (0.815); hereditary angioedema type 3 (0.777); hereditary angioedema (0.677); peptic ulcer disease (0.450); angioedema (0.407)
- **Europe PMC papers**: 100014
- **Why important**: F12 is a liver-derived secreted coagulation factor involved in the plasma kallikrein-kinin system, intrinsic coagulation, proteolysis, and plasminogen activation. Its strong connection to IL6ST and its HPA profile parallel C5, providing independent evidence for a circulating plasma component. It also broadens the module beyond cellular immunity toward vascular and contact-system biology and has substantial disease literature involving factor deficiency and angioedema.
- **Conclusion**: Established evidence supports F12 as a plasma coagulation and contact-system protein. Its module membership is consistent with a shared circulating inflammatory or vascular context, but does not establish coordinated regulation with IL6ST or the myeloid receptors.

## Module 11

**Tissue pair**: breast and cerebrospinal_fluid  
**Genes (5)**: CFB, GPX3, IGHG4, CHL1, PLBD2

### Function

No GO/KEGG term passed global multiple-testing correction, so the module has no statistically established pathway annotation from the primary enrichment analysis. Its composition and network suggest a mixed extracellular and tissue-interface signal: CHL1 is a neural cell-adhesion and recognition molecule, GPX3 provides extracellular peroxide and lipid-hydroperoxide detoxification, CFB represents alternative-pathway complement activity, IGHG4 represents immunoglobulin produced by plasma cells, and PLBD2 has a predicted phospholipase role. The co-abundance structure is hub-like, with CHL1 connected to every other module member, while the peripheral genes have no mutual edges. This supports a coordinated biological signal but does not establish that all members participate in one molecular pathway.

**Cell composition.** The HPA summary classifies every module gene as secreted, although the gene-level annotation describes PLBD2 as intracellular and membrane-associated. The module therefore has a strong extracellular or circulating-protein character. CFB and GPX3 are secreted to blood, IGHG4 is an immunoglobulin gene associated with plasma cells, and CHL1 is secreted in brain. Blood-related evidence includes memory and naive B-cell enrichment for CHL1 and IGHG4, neutrophil enrichment for GPX3, and plasma-cell specificity for IGHG4; CFB is not detected in immune cells. The tissue annotations are heterogeneous, involving brain, kidney, liver, lymphoid tissue, adrenal gland, ovary, and other cell types. In breast, three proteins are detected and two are not detected, while there is no matching HPA tissue category for cerebrospinal fluid. Thus, the shared module may partly reflect circulating proteins, blood contamination or exposure, and shared neural or immune-associated material rather than a breast–cerebrospinal-fluid-specific intracellular program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported for any gene pair, and STRING functional enrichment is absent. This means the co-abundance relationships are not supported by the supplied STRING interaction network and should not be interpreted as established direct physical interactions. hu.MAP provides a more limited connection: CFB and GPX3 co-occur in complexes (hu.MAP huMAP3_07701.1), (hu.MAP huMAP3_09273.1), (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), and (hu.MAP huMAP3_10678.1). However, these complexes contain many additional extracellular, complement, coagulation, lipid-transport, and inflammatory proteins, so the shared hu.MAP membership supports a recurring extracellular protein context rather than a compact, module-specific complex. CHL1, PLBD2, and IGHG4 have no supplied hu.MAP membership.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07701.1 (CFB, GPX3; 2/22); huMAP3_09273.1 (CFB, GPX3; 2/28); huMAP3_08395.1 (CFB, GPX3; 2/43); huMAP3_09531.1 (CFB, GPX3; 2/47); huMAP3_10101.1 (CFB, GPX3; 2/49); huMAP3_10678.1 (CFB, GPX3; 2/71)

### Novelty

The breast–cerebrospinal-fluid co-abundance pattern may be a new dataset-level observation, because the supplied evidence shows a distinctive CHL1-centered correlation structure without corresponding high-confidence STRING interactions or a compact hu.MAP complex. However, it cannot be called a newly discovered molecular pathway. The lack of STRING or hu.MAP support alone does not prove novelty, and the strong secreted, blood-associated, and tissue-heterogeneous composition provides plausible non-novel explanations such as shared circulating proteins, sample exposure, or cellular admixture. The absence of globally significant GO/KEGG enrichment further limits claims of pathway-level novelty, while not falsifying the module.

**Hypothesis.** Hypothesis: this module captures coordinated abundance of extracellular proteins encountered in both breast and cerebrospinal-fluid samples, with CHL1 linking a neural or tissue-interface signal to circulating redox, complement, phospholipase, and immunoglobulin components. In this model, GPX3 reflects extracellular oxidative-stress buffering, CFB reflects alternative complement activity, and IGHG4 reflects B-cell or plasma-cell-derived material; PLBD2 may reflect extracellular-vesicle or membrane-associated lipid processing. The apparent coordination could arise from shared extracellular transport or sample composition rather than direct interaction among the proteins. This hypothesis requires validation with independent cohorts, contamination and cell-composition controls, and targeted protein measurements.

### Important genes

#### CHL1

- **Related proteins** (co-abundance neighbors): PLBD2 (0.91), GPX3 (0.85), CFB (0.82), IGHG4 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell adhesion molecule L1 like. The protein encoded by this gene is a member of the L1 gene family of neural cell adhesion molecules. It is a neural recognition molecule that may be involved in signal transduction pathways. The deletion of one copy of this gene may be responsible for mental defects in patients with 3p- syndrome. This protein may also play a role in the growth of certain cancers. Alternate splicing results in bot…
- **Diseases (Open Targets)**: mathematical ability (0.457); alcohol drinking (0.392); idiopathic generalized epilepsy (0.364); risk-taking behaviour (0.338); cervical carcinoma (0.323)
- **Europe PMC papers**: 2812
- **Why important**: CHL1 is the network hub, connected to every other module member with the strongest supplied edge weights. It is a neural cell-adhesion molecule involved in cell adhesion and signal transduction, has brain tissue enhancement and broad neural cell-type enhancement, and is secreted in brain. It also links the module to memory and naive B-cell-associated abundance patterns. Its literature volume is substantial, and the supplied disease associations include neurological and behavioral traits as well as cervical carcinoma.
- **Conclusion**: Established evidence supports CHL1 as the structural anchor of the co-abundance pattern and as a neural extracellular recognition molecule. It is plausible, but not established, that CHL1 reflects a cerebrospinal-fluid or neural-interface component that coordinates the other proteins.

#### GPX3

- **Related proteins** (co-abundance neighbors): CHL1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07701.1, huMAP3_09273.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: glutathione peroxidase 3. The protein encoded by this gene belongs to the glutathione peroxidase family, members of which catalyze the reduction of organic hydroperoxides and hydrogen peroxide (H2O2) by glutathione, and thereby protect cells against oxidative damage. Several isozymes of this gene family exist in vertebrates, which vary in cellular location and substrate specificity. This isozyme is secreted, and is abundan…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.435); disorder of ear (0.351); sensorineural hearing loss disorder (0.351); placental retention (0.146); atrial fibrillation (0.133)
- **Europe PMC papers**: 5897
- **Why important**: GPX3 is a secreted glutathione peroxidase that reduces organic hydroperoxides and hydrogen peroxide and is abundantly present in plasma. It is tissue-enhanced in kidney, enriched in neutrophils, and is the only module gene that participates with CFB in all supplied hu.MAP complex groupings (hu.MAP huMAP3_07701.1), (hu.MAP huMAP3_09273.1), (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), and (hu.MAP huMAP3_10678.1). It has substantial literature and disease associations involving oxidative or systemic physiology.
- **Conclusion**: Established evidence supports GPX3 as an extracellular oxidative-stress defense protein and as a recurring member of broad extracellular hu.MAP contexts with CFB. Its role as a functional driver of this breast–cerebrospinal-fluid module remains a hypothesis rather than a demonstrated causal mechanism.

#### CFB

- **Related proteins** (co-abundance neighbors): CHL1 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07701.1, huMAP3_09273.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: complement factor B. This gene encodes complement factor B, a component of the alternative pathway of complement activation. Factor B circulates in the blood as a single chain polypeptide. Upon activation of the alternative pathway, it is cleaved by complement factor D yielding the noncatalytic chain Ba and the catalytic subunit Bb. The active subunit Bb is a serine protease which associates with C3b to form the alter…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with B factor anomaly (0.764); atypical hemolytic-uremic syndrome (0.705); Immunodeficiency due to a complement cascade protein anomaly (0.614); paroxysmal nocturnal hemoglobinuria (0.561); complement 3 glomerulopathy (0.546)
- **Europe PMC papers**: 7226
- **Why important**: CFB is a circulating component of the alternative complement pathway and supplies the proteolytic activity of the alternative-pathway C3 convertase after activation. It is tissue-enriched in liver, secreted to blood, and appears with GPX3 in every supplied hu.MAP complex group (hu.MAP huMAP3_07701.1), (hu.MAP huMAP3_09273.1), (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), and (hu.MAP huMAP3_10678.1). It has the largest supplied literature volume among the module genes and strong disease associations involving complement dysregulation.
- **Conclusion**: Established evidence supports CFB as a circulating complement protein and a marker of extracellular immune or inflammatory context. It is plausible that CFB contributes to a shared complement-rich extracellular environment, but the module data do not prove local complement activation in breast or cerebrospinal fluid.

#### IGHG4

- **Related proteins** (co-abundance neighbors): CHL1 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Group enriched; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: immunoglobulin heavy constant gamma 4 (G4m marker)
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 1010
- **Why important**: IGHG4 is an immunoglobulin heavy-constant gene associated with lymphoid tissue, plasma cells, and memory and naive B-cell groups. It is classified as an immunoglobulin secretome protein and is detected in breast. Its direct connection to CHL1 makes it important for interpreting the module as potentially immune- or blood-associated rather than as a unified neural pathway. The gene has a substantial literature base, although no Open Targets association is supplied.
- **Conclusion**: Established evidence supports IGHG4 as an immunoglobulin-related signal originating from B-cell or plasma-cell-associated material. Its presence is consistent with immune-cell contribution or circulating antibody abundance; a specific functional interaction with CHL1 is not established.

#### PLBD2

- **Related proteins** (co-abundance neighbors): CHL1 (0.91); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phospholipase B domain containing 2. Predicted to enable phospholipase activity. Predicted to be involved in phospholipid catabolic process. Located in extracellular exosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Hypocalcemia (0.043); type 2 diabetes mellitus (0.038); bronchial disorder (0.034); Alzheimer disease (0.032); hemorrhage (0.032)
- **Europe PMC papers**: 172
- **Why important**: PLBD2 is the only module member whose supplied functional annotation points directly toward phospholipase activity and phospholipid catabolism. It is connected to the CHL1 hub and is associated with extracellular exosomes in the supplied annotation, although HPA describes its secretome location as intracellular and membrane. Its tissue and cell annotations are more restricted than those of the other selected genes, and its literature volume is comparatively limited.
- **Conclusion**: Established evidence supports PLBD2 as a predicted lipid-processing protein with a possible vesicular or membrane-associated context. Its connection to CHL1 may indicate coordinated extracellular-vesicle or membrane turnover biology, but that interpretation is explicitly hypothetical because the functional annotation is predicted and no direct interaction is reported.

## Module 12

**Tissue pair**: breast and cerebrospinal_fluid  
**Genes (9)**: CSF1R, CSF1, FCGBP, FGL2, SERPINE2, KLKB1, LCAT, PROS1, VASN

### Function

No GO or KEGG term passed global multiple-testing correction, so the module should not be assigned a formally enriched pathway. Its gene annotations nevertheless converge on an extracellular and plasma-associated biology involving coagulation and fibrinolysis, lipid transport, vascular regulation, and myeloid growth-factor signaling. KLKB1 supports contact activation, kinin generation, coagulation and fibrinolysis; SERPINE2 opposes several proteolytic and coagulation processes; PROS1 provides anticoagulant activity; and LCAT supports cholesterol esterification and transport. CSF1 and CSF1R represent a cytokine-receptor axis controlling macrophage production and function. FGL2, VASN and FCGBP add secreted, vascular, extracellular and mucosal-associated biology. The co-abundance pattern therefore most plausibly reflects a shared extracellular or biofluid environment with immune, vascular and barrier-related signals, rather than a single demonstrated intracellular pathway.

**Cell composition.** The module is strongly dominated by secreted proteins or proteins associated with plasma, the cell surface or extracellular vesicles. HPA profiles point repeatedly to liver, blood vessel, lymphoid tissue, placenta, choroid plexus, astrocytes, ependymal cells and other glial or barrier-associated cell types. Several genes show blood-cell associations, especially monocyte, eosinophil, dendritic-cell or related myeloid patterns, while some are not detected in immune cells. This mixed profile argues against interpreting the module as a uniform breast epithelial program. In breast and cerebrospinal fluid, the shared signal could reflect circulating or secreted proteins, vascular or barrier interfaces, macrophage-related cells, and shared sample-associated cell types. Breast protein detection is sparse for the module, which further weakens a claim that the pattern represents abundant breast-tissue protein expression. The HPA evidence supports a composition or compartment explanation, but does not by itself establish contamination or a specific cellular source.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship among module members is CSF1 with CSF1R. This is biologically coherent because CSF1 is the ligand and CSF1R is its receptor, and it provides an independently supported signaling link within the module. The other co-abundance edges do not have corresponding high-confidence STRING support in the fact sheet, so they should be treated as abundance associations rather than established physical interactions. No hu.MAP complex contains multiple module members. Together, these results indicate that the module is not a known stable multiprotein complex. It instead combines a validated cytokine-receptor pair with secreted plasma, coagulation, lipid and extracellular proteins that may covary because of shared secretion, transport, compartment or cell-source effects.

**STRING interactions (score >= 0.7)**: 1 of 36 gene pairs: CSF1–CSF1R (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a new cross-tissue co-abundance observation, but the fact sheet does not establish a new molecular mechanism or a previously unknown interaction. The CSF1-CSF1R relationship is already well established, and the functions of the plasma proteins and coagulation regulators are also established individually. The absence of the remaining relationships from STRING and the absence of a hu.MAP complex do not prove novelty, because database coverage, context dependence and co-abundance versus physical interaction are distinct issues. A defensible novelty claim would require replication in independent breast and cerebrospinal-fluid cohorts, control for blood and cellular composition, and comparison with published tissue-pair modules or matched proteomic datasets. At present, the most supportable claim is a potentially novel shared abundance pattern assembled from largely known biology.

**Hypothesis.** Hypothesis: a shared vascular, barrier or biofluid compartment contributes secreted proteins to both tissue groups, while variable myeloid-cell representation adds the CSF1-CSF1R signal. Within this environment, plasma protease and anticoagulant components could covary with lipid transport and extracellular matrix or TGF-beta-modulating proteins. The module may therefore report coordinated abundance of a circulating or barrier-associated inflammatory-coagulation milieu rather than direct co-assembly of its proteins. This hypothesis predicts that the module will weaken after adjustment for plasma exposure, vascularity, macrophage or monocyte abundance, and choroid-plexus or other barrier-cell signatures; it also predicts that CSF1-CSF1R-related abundance may vary with myeloid activation.

### Important genes

#### CSF1R

- **Related proteins** (co-abundance neighbors): FGL2 (0.86), FCGBP (0.86), LCAT (0.84); STRING partners: CSF1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Plasma membrane; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: colony stimulating factor 1 receptor. The protein encoded by this gene is the receptor for colony stimulating factor 1, a cytokine which controls the production, differentiation, and function of macrophages. This receptor mediates most if not all of the biological effects of this cytokine. Ligand binding activates the receptor kinase through a process of oligomerization and transphosphorylation. The encoded protein is a tyrosine kinas…
- **Diseases (Open Targets)**: leukoencephalopathy, diffuse hereditary, with spheroids 1 (0.843); brain abnormalities, neurodegeneration, and dysosteosclerosis (0.793); gastrointestinal stromal tumor (0.626); renal cell carcinoma (0.602); neoplasm (0.591)
- **Europe PMC papers**: 17331
- **Why important**: CSF1R is one of the strongest network-connected genes and is the module’s clearest signaling anchor. Its HPA profile supports lymphoid, macrophage, Kupffer-cell, Hofbauer-cell, dendritic-cell and monocyte-associated biology, and it is detected in breast tissue. Its extensive literature and disease associations make it a well-established biological marker rather than an obscure annotation. STRING independently links it to CSF1.
- **Conclusion**: Established evidence supports CSF1R as a macrophage and myeloid growth-factor receptor and as a plausible indicator of immune-cell or myeloid-context contribution. It is not established that CSF1R drives the entire module or that the module represents CSF1R signaling in both tissue groups.

#### CSF1

- **Related proteins** (co-abundance neighbors): KLKB1 (0.84); STRING partners: CSF1R (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: colony stimulating factor 1. The protein encoded by this gene is a cytokine that controls the production, differentiation, and function of macrophages. The active form of the protein is found extracellularly as a disulfide-linked homodimer, and is thought to be produced by proteolytic cleavage of membrane-bound precursors. The encoded protein may be involved in development of the placenta. Alternate splicing results in multip…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.308); metabolic syndrome (0.267); otosclerosis (0.264); adult-onset Still disease (0.200); triple-negative breast carcinoma (0.127)
- **Europe PMC papers**: 13069
- **Why important**: CSF1 is the known ligand for CSF1R and is independently connected to CSF1R by STRING. It is secreted to blood and is associated with immune and progenitor-cell biology, including macrophage regulation and placental development. Its network link to KLKB1 places the cytokine near the module’s plasma-protease component, although that co-abundance link is not itself a demonstrated physical interaction. Its substantial literature makes it a strong interpretive anchor.
- **Conclusion**: Established evidence supports CSF1 as a secreted regulator of macrophage production, differentiation and function. The module supports a hypothesis of myeloid-associated covariation, but does not demonstrate active CSF1 signaling, receptor occupancy or causal control of the other module genes.

#### KLKB1

- **Related proteins** (co-abundance neighbors): FCGBP (0.93), CSF1 (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kallikrein B1. This gene encodes a glycoprotein that participates in the surface-dependent activation of blood coagulation, fibrinolysis, kinin generation and inflammation. The encoded preproprotein present in plasma as a non-covalent complex with high molecular weight kininogen undergoes proteolytic processing mediated by activated coagulation factor XII to generate a disulfide-linked, heterodimeric serine prot…
- **Diseases (Open Targets)**: inherited prekallikrein deficiency (0.724); prekallikrein deficiency (0.671); hereditary angioedema (0.590); venous thromboembolism (0.533); blood coagulation disease (0.507)
- **Europe PMC papers**: 1278
- **Why important**: KLKB1 is a plasma-secreted serine protease with a central position connecting FCGBP and CSF1 in the co-abundance graph. Its established functions in contact activation, coagulation, fibrinolysis, kinin generation and inflammation provide a mechanistic link to the module’s extracellular and vascular character. Its liver and cerebrovascular or glial-associated HPA pattern is compatible with a circulating or barrier-related source. Its disease associations include prekallikrein deficiency, hereditary angioedema and thromboembolic disease.
- **Conclusion**: Established evidence supports KLKB1 as a plasma contact-system component. Its network position makes it a useful marker of the module’s protease and biofluid axis, but the data do not show that KLKB1 enzymatic activity causes the observed cross-tissue co-abundance.

#### LCAT

- **Related proteins** (co-abundance neighbors): CSF1R (0.84); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lecithin-cholesterol acyltransferase. This gene encodes the extracellular cholesterol esterifying enzyme, lecithin-cholesterol acyltransferase. The esterification of cholesterol is required for cholesterol transport. Mutations in this gene have been found to cause fish-eye disease as well as LCAT deficiency. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: LCAT deficiency (0.836); fish eye disease (0.826); Norum disease (0.735); Abnormality of the cardiovascular system (0.496); small intestine neoplasm (0.473)
- **Europe PMC papers**: 4970
- **Why important**: LCAT connects to CSF1R in the module and represents a distinct lipid-transport axis. It is a liver-enriched secreted enzyme involved in cholesterol esterification, phospholipid metabolism and lipoprotein remodeling, with HPA support in liver and glial-associated contexts. Its extensive literature and strong associations with LCAT deficiency and fish-eye disease make its annotation well established.
- **Conclusion**: Established evidence supports LCAT as a circulating cholesterol-transport enzyme. Its presence suggests that lipid handling may covary with the immune and plasma signals, but the module does not establish a direct biochemical interaction between LCAT and CSF1R.

#### PROS1

- **Related proteins** (co-abundance neighbors): FCGBP (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein S. This gene encodes a vitamin K-dependent plasma protein that functions as a cofactor for the anticoagulant protease, activated protein C (APC) to inhibit blood coagulation. It is found in plasma in both a free, functionally active form and also in an inactive form complexed with C4b-binding protein. Mutations in this gene result in autosomal dominant hereditary thrombophilia. An inactive pseudogene…
- **Diseases (Open Targets)**: thrombophilia due to protein S deficiency, autosomal dominant (0.823); hereditary thrombophilia due to congenital protein S deficiency (0.751); venous thromboembolism (0.746); protein S deficiency (0.700); thrombophilia due to protein S deficiency, autosomal recessive (0.698)
- **Europe PMC papers**: 2437
- **Why important**: PROS1 is a secreted plasma protein linked to FCGBP in the network and is enriched in choroid plexus and liver-related HPA contexts. Its established role as a cofactor for activated protein C places it directly in anticoagulant regulation. Its disease associations with protein S deficiency and hereditary thrombophilia provide strong clinical support for its biological importance.
- **Conclusion**: Established evidence supports PROS1 as an anticoagulant plasma component and a plausible contributor to the module’s coagulation balance. The co-abundance relationship with FCGBP does not establish a direct interaction or show that PROS1 mediates the shared breast and cerebrospinal-fluid pattern.

#### FGL2

- **Related proteins** (co-abundance neighbors): CSF1R (0.86), SERPINE2 (0.85), VASN (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibrinogen like 2. The protein encoded by this gene is a secreted protein that is similar to the beta- and gamma-chains of fibrinogen. The carboxyl-terminus of the encoded protein consists of the fibrinogen-related domains (FRED). The encoded protein forms a tetrameric complex which is stabilized by interchain disulfide bonds. This protein may play a role in physiologic functions at mucosal sites. [provided by RefSe…
- **Diseases (Open Targets)**: neurodegenerative disease (0.331); autoinflammatory syndrome (0.185); Nephropathy (0.136); nephritis (0.134); neoplasm (0.117)
- **Europe PMC papers**: 1690
- **Why important**: FGL2 is a network hub connected to CSF1R, SERPINE2 and VASN, and it is secreted to blood. Its HPA associations with blood vessel, lymphoid tissue, monocytes, dendritic cells, macrophages and granulocyte-related populations make it a strong candidate for the module’s vascular-myeloid interface. Its extracellular fibrinogen-related structure and reported mucosal functions complement the module’s secreted and coagulation-associated character. Its literature and disease associations include inflammatory, renal and neurodegenerative contexts.
- **Conclusion**: Established evidence supports FGL2 as a secreted fibrinogen-related protein associated with vascular and immune contexts. Its network position makes it a plausible integrator of the module, but the fact sheet does not establish that FGL2 coordinates the other proteins or explains the cross-tissue conservation.
