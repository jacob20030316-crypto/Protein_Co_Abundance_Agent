# Conserved co-abundance modules: cerebrospinal_fluid and colon

## Module 0

**Tissue pair**: cerebrospinal_fluid and colon  
**Genes (13)**: SERPINA1, A2M, ALB, APOA1, C3, COL6A2, EMILIN1, HBA1, HBB, IGKC, TNC, THY1, TF

### Function

The module is most consistent with a circulating extracellular-protein and blood-derived co-abundance program, rather than a confidently established intracellular pathway. Its main biological themes are plasma transport, complement and inflammatory regulation, protease inhibition, iron transport, lipid transport, and hemoglobin-associated signal. C3, A2M, and SERPINA1 support complement, protease-control, and inflammatory functions; ALB, APOA1, and TF support transport functions; HBA1 and HBB represent an erythrocyte-associated component. A smaller extracellular-matrix and stromal branch is represented by COL6A2, TNC, EMILIN1, and THY1. No GO or KEGG term passed global correction, so these functional interpretations are based on the individual gene annotations, network structure, and supplementary STRING and hu.MAP evidence rather than on globally significant pathway enrichment.

**Cell composition.** The module is strongly enriched in secreted or extracellular proteins: HPA identifies ten secreted genes, with many released to blood or extracellular matrix. ALB, APOA1, C3, A2M, SERPINA1, and TF are predominantly liver-associated and secreted plasma proteins. HBA1 and HBB are erythrocyte-associated, with bone-marrow and blood-cell enrichment, making blood-cell contribution or hemolysis a plausible explanation for their co-abundance. IGKC is associated with plasma cells and B-cell populations, adding a possible immunoglobulin or immune-cell component. COL6A2, TNC, EMILIN1, and THY1 provide evidence for stromal, vascular, neural, or extracellular-matrix material, including proteins detected in colon. The HPA pattern therefore favors a mixture of circulating plasma proteins, blood-derived material, and a smaller tissue or stromal contribution rather than a colon-specific cellular program. Detection of only part of the module in colon by HPA is also compatible with sample composition effects.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a known plasma-protein interaction backbone. ALB is linked to A2M, APOA1, C3, SERPINA1, and TF; APOA1 is linked to A2M, ALB, C3, HBB, SERPINA1, and TF; and SERPINA1 is linked to A2M, ALB, APOA1, C3, and TF. The HBA1-HBB relationship is also established. These relationships indicate that much of the module is a recognized biochemical and co-occurrence network rather than an unexplained set of proteins. The repeated STRING tissue and plasma-proteomics annotations in (STRING TISSUES Right atrium; within-query FDR = 3.41e-05) through (STRING PMID (2018) Circulating MicroRNA Expression Levels Associated With Internet Gaming Disorder.; within-query FDR = 0.0252) reinforce a blood or circulating-protein interpretation, but they are supplementary and were not corrected globally across modules. hu.MAP independently places the core proteins SERPINA1, A2M, C3, APOA1, ALB, and TF together in several complexes, including (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_08224.1) and (hu.MAP huMAP3_08700.1). HBA1 and HBB recur together in (hu.MAP huMAP3_04556.1), (hu.MAP huMAP3_06991.1), (hu.MAP huMAP3_10486.1), and (hu.MAP huMAP3_13522.1). By contrast, COL6A2, TNC, EMILIN1, IGKC, and THY1 have little or no direct STRING or hu.MAP support in this module, suggesting that their co-abundance may reflect shared sample origin, extracellular context, or tissue composition rather than a single physical complex.

**STRING interactions (score >= 0.7)**: 15 of 78 gene pairs: A2M–ALB (0.98); A2M–APOA1 (0.998); A2M–SERPINA1 (0.98); A2M–TF (0.82); ALB–APOA1 (0.998); ALB–C3 (0.959); ALB–SERPINA1 (0.998); ALB–TF (0.9); APOA1–C3 (0.957); APOA1–HBB (0.839); APOA1–SERPINA1 (0.927); APOA1–TF (0.919); C3–SERPINA1 (0.859); HBA1–HBB (0.999); SERPINA1–TF (0.848)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Right atrium (FDR = 3.41e-05, 7 genes); TISSUES Left atrium (FDR = 4.31e-05, 7 genes); TISSUES Left ventricle (FDR = 8.01e-05, 6 genes); PMID (2023) Whartons jelly mesenchymal stem cells: a concise review of their secretome and prospective clinical applications. (FDR = 0.0019, 8 genes); PMID (2022) Serum alpha-1-antitrypsin level in the severity prognosis of systemic lupus erythematosus patients: Systematic exploration of novel biomarker. (FDR = 0.0079, 8 genes); PMID (2013) Serum peptidomic biomarkers for pulmonary metastatic melanoma identified by means of a nanopore-based assay. (FDR = 0.0102, 6 genes); PMID (2012) Heart-brain signaling in patent foramen ovale-related stroke:  differential plasma proteomic expression patterns revealed with a 2-pass liquid chromatography-tandem mass spectrometry discovery workflow. (FDR = 0.0102, 6 genes); PMID (2024) Plasma Proteomic Signature of Endometrial Cancer in Patients with Diabetes. (FDR = 0.0252, 6 genes); PMID (2022) Proteomic differences in hippocampus and cortex of sudden unexplained death in childhood. (FDR = 0.0252, 6 genes); PMID (2022) The Implant Proteome-The Right Surgical Glue to Fix Titanium Implants In Situ. (FDR = 0.0252, 7 genes); PMID (2022) Plasma proteomics reveals an improved cardio-metabolic profile in patients with type 2 diabetes post-liraglutide treatment. (FDR = 0.0252, 7 genes); PMID (2022) Nanotechnology Meets Oncology: A Perspective on the Role of the Personalized Nanoparticle-Protein Corona in the Development of Technologies for Pancreatic Cancer Detection. (FDR = 0.0252, 6 genes); PMID (2019) Plasma Proteome Profiling to detect and avoid sample-related biases in biomarker studies. (FDR = 0.0252, 7 genes); PMID (2018) Homocysteine, folate, hs-C-reactive protein, tumor necrosis factor alpha and inflammatory proteins: are these biomarkers related to nutritional status and cardiovascular risk in childhood-onset systemic lupus erythematosus? (FDR = 0.0252, 6 genes); PMID (2018) Circulating MicroRNA Expression Levels Associated With Internet Gaming Disorder. (FDR = 0.0252, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINA1, A2M, C3, APOA1, ALB, TF, HBB, HBA1; 8/64); huMAP3_08395.1 (SERPINA1, A2M, C3, APOA1, ALB, TF; 6/43); huMAP3_09531.1 (SERPINA1, A2M, C3, APOA1, ALB, TF; 6/47); huMAP3_10101.1 (SERPINA1, A2M, C3, APOA1, ALB, TF; 6/49); huMAP3_10678.1 (SERPINA1, A2M, C3, APOA1, ALB, TF; 6/71); huMAP3_07432.1 (SERPINA1, C3, APOA1, ALB, TF; 5/18); huMAP3_07265.1 (SERPINA1, A2M, APOA1, ALB, TF; 5/20); huMAP3_09434.1 (SERPINA1, C3, APOA1, ALB, TF; 5/33); huMAP3_08224.1 (C3, APOA1, TF; 3/21); huMAP3_04556.1 (HBB, HBA1; 2/3); huMAP3_06991.1 (HBB, HBA1; 2/4); huMAP3_10486.1 (HBB, HBA1; 2/4); huMAP3_02242.1 (C3, TF; 2/9); huMAP3_13522.1 (HBB, HBA1; 2/10); huMAP3_08700.1 (SERPINA1, ALB; 2/11)

### Novelty

The module should not be called a new molecular complex or a newly discovered pathway. Its dominant plasma-protein relationships are already represented in STRING and in multiple hu.MAP complexes, and the repeated plasma and cardiovascular STRING annotations show that the core signal is familiar. The cross-tissue observation may still be useful as a dataset-level finding, particularly because cerebrospinal fluid and colon share a module containing both circulating proteins and extracellular-matrix markers. However, absence of a relationship from STRING or hu.MAP for the peripheral genes does not establish novelty. A defensible novelty claim would require independent validation, control for blood contamination and shared cell types, comparison with existing cross-tissue co-abundance modules, and experimental or longitudinal confirmation.

**Hypothesis.** Hypothesis: the shared module reflects a common extracellular milieu sampled in cerebrospinal fluid and colon, dominated by blood-derived plasma proteins and supplemented by local stromal or vascular material. Liver-derived ALB, APOA1, C3, SERPINA1, A2M, and TF may enter or circulate through the sampled compartments, while erythrocyte-associated HBA1 and HBB may report blood exposure. COL6A2, TNC, EMILIN1, and THY1 could represent extracellular-matrix or stromal remodeling that covaries with this circulating-protein background. IGKC may indicate a contribution from local or blood-associated antibody-producing cells. This model predicts that the module will weaken after adjustment for plasma abundance, hemolysis, immune-cell fractions, and stromal-cell fractions, and that the residual tissue-specific component will be concentrated in the extracellular-matrix genes.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): A2M (0.87), TNC (0.83), HBA1; HBA2 (0.81), ALB (0.81), COL6A2 (0.81), APOA1 (0.80); STRING partners: ALB (0.959), APOA1 (0.957), SERPINA1 (0.859)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_08224.1, huMAP3_02242.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a central network node and connects the plasma-protein backbone to complement and inflammatory biology. It is liver-enriched, secreted to blood, associated with a non-classical monocyte population, present in many hu.MAP complexes from (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_08224.1), and repeatedly represented in STRING annotations (STRING TISSUES Right atrium; within-query FDR = 3.41e-05), (STRING TISSUES Left atrium; within-query FDR = 4.31e-05), (STRING PMID (2023) Whartons jelly mesenchymal stem cells: a concise review of their secretome and prospective clinical applications.; within-query FDR = 0.0019) through (STRING PMID (2012) Heart-brain signaling in patent foramen ovale-related stroke:  differential plasma proteomic expression patterns revealed with a 2-pass liquid chromatography-tandem mass spectrometry discovery workflow.; within-query FDR = 0.0102), and (STRING PMID (2022) Proteomic differences in hippocampus and cortex of sudden unexplained death in childhood.; within-query FDR = 0.0252) through (STRING PMID (2018) Circulating MicroRNA Expression Levels Associated With Internet Gaming Disorder.; within-query FDR = 0.0252). Its disease associations include complement deficiency, complement-mediated renal disease, atypical hemolytic-uremic syndrome, and age-related macular degeneration. The large literature base makes C3 one of the best-characterized anchors of the module.
- **Conclusion**: Established evidence supports C3 as a biologically meaningful complement and circulating-protein anchor. It is plausible, but not demonstrated, that C3 drives the shared module; the co-abundance data alone cannot distinguish active complement biology from correlated plasma abundance.

#### ALB

- **Related proteins** (co-abundance neighbors): IGKC (0.91), TF (0.90), COL6A2 (0.82), C3 (0.81), APOA1 (0.80); STRING partners: A2M (0.98), APOA1 (0.998), C3 (0.959), SERPINA1 (0.998), TF (0.9)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08700.1
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB is a highly connected network hub and is linked by STRING to A2M, APOA1, C3, SERPINA1, and TF. It is liver-enriched, secreted to blood, and is the most abundant protein in human blood, with carrier and colloid-osmotic functions. It recurs across the supplementary STRING tissue and plasma annotations, and it appears in many hu.MAP complexes, including (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_09434.1) and (hu.MAP huMAP3_08700.1). Its disease associations include congenital analbuminemia and disorders involving altered protein binding or circulating transport.
- **Conclusion**: Established evidence supports ALB as a major circulating-protein and sample-composition marker in this module. Its prominence is more likely to indicate shared extracellular or plasma content than a colon-specific mechanism.

#### SERPINA1

- **Related proteins** (co-abundance neighbors): HBB (0.93), TF (0.92), HBA1; HBA2 (0.85); STRING partners: A2M (0.98), ALB (0.998), APOA1 (0.927), C3 (0.859), TF (0.848)
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08700.1
- **Function (MyGene.info)**: serpin family A member 1. The protein encoded by this gene is a serine protease inhibitor belonging to the serpin superfamily whose targets include elastase, plasmin, thrombin, trypsin, chymotrypsin, and plasminogen activator. This protein is produced in the liver, the bone marrow, by lymphocytic and monocytic cells in lymphoid tissue, and by the Paneth cells of the gut. Defects in this gene are associated with chronic obs…
- **Diseases (Open Targets)**: alpha 1-antitrypsin deficiency (0.768); chronic obstructive pulmonary disease (0.690); cirrhosis of liver (0.573); cholelithiasis (0.569); pulmonary emphysema (0.569)
- **Europe PMC papers**: 6526
- **Why important**: SERPINA1 is a secreted liver-associated protease inhibitor with links to elastase, plasmin, thrombin, trypsin, chymotrypsin, and plasminogen activator. It is connected in STRING to the central plasma proteins and occurs in many hu.MAP complexes, including (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_09434.1) and (hu.MAP huMAP3_08700.1). HPA also associates it with hepatocytes, cholangiocytes, enterocytes, monocytes, and neutrophils. Its disease associations include alpha-one-antitrypsin deficiency, chronic obstructive pulmonary disease, emphysema, cirrhosis, and cholelithiasis. It is repeatedly present in the supplementary STRING terms.
- **Conclusion**: Established evidence supports SERPINA1 as a plausible protease-control and inflammatory component of the circulating-protein backbone. A role in tissue remodeling within this shared module remains a hypothesis, not a demonstrated causal mechanism.

#### TF

- **Related proteins** (co-abundance neighbors): SERPINA1 (0.92), HBB (0.92), ALB (0.90), HBA1; HBA2 (0.89), IGKC (0.89); STRING partners: A2M (0.82), ALB (0.9), APOA1 (0.919), SERPINA1 (0.848)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08224.1, huMAP3_02242.1
- **Function (MyGene.info)**: transferrin. This gene encodes a glycoprotein with an approximate molecular weight of 76.5 kDa. It is thought to have been created as a result of an ancient gene duplication event that led to generation of homologous C and N-terminal domains each of which binds one ion of ferric iron. The function of this protein is to transport iron from the intestine, reticuloendothelial system, and liver parenchymal cells t…
- **Diseases (Open Targets)**: atransferrinemia (0.776); alcohol drinking (0.492); hemochromatosis type 1 (0.471); neurodegenerative disease (0.400); urolithiasis (0.329)
- **Europe PMC papers**: 143656
- **Why important**: TF is a connected hub joining ALB, APOA1, A2M, SERPINA1, and hemoglobin-associated genes. It is secreted to blood, group-enriched in liver and retina, and functions in iron transport and intracellular iron homeostasis. It appears across numerous hu.MAP complexes, including (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_08224.1) and (hu.MAP huMAP3_02242.1), and across many supplementary STRING annotations. Its disease associations include atransferrinemia, hemochromatosis, urolithiasis, and neurodegenerative disease.
- **Conclusion**: Established evidence supports TF as an iron-transport and plasma-composition marker that helps connect the hemoglobin signal to the broader secreted-protein network. The data do not establish altered iron handling as the cause of the module.

#### COL6A2

- **Related proteins** (co-abundance neighbors): EMILIN1 (0.86), IGKC (0.84), ALB (0.82), THY1 (0.81), C3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 2 chain. This gene encodes one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The product of this gene contains several domains similar to von Willebrand Factor type A domains. These domains have been shown to bind extracellular matrix proteins, an interaction that explains the importance of this collagen in organizing matrix components. Mutation…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy 1B (0.770); Bethlem myopathy (0.755); Ullrich congenital muscular dystrophy (0.743); Bethlem myopathy 1B (0.723); Bethlem myopathy 1A (0.713)
- **Europe PMC papers**: 4115
- **Why important**: COL6A2 is a network connector between the plasma-associated ALB and C3 signals and the extracellular-matrix genes EMILIN1 and THY1. HPA detects it in colon and associates it with fibroblasts, hepatic stellate cells, stromal populations, and several T-cell populations. Its product is a collagen type VI chain involved in organizing connective-tissue matrix, and mutations are associated with Bethlem and Ullrich muscular dystrophies. Unlike the plasma core, COL6A2 has no listed STRING partner or hu.MAP complex in this module, making it a useful marker of a potentially distinct stromal branch.
- **Conclusion**: Established evidence supports COL6A2 as an extracellular-matrix and stromal indicator rather than a member of the recognized plasma-protein complex. Its connection to the shared module may reflect tissue composition or matrix remodeling; a direct biochemical interaction with the plasma core is not established.

## Module 1

**Tissue pair**: cerebrospinal_fluid and colon  
**Genes (14)**: A1BG, LRG1, AEBP1, IGFALS, APOA4, C1QC, C2, C6, C9, F12, GPX3, ITIH4, SERPINF1, CLEC3B

### Function

The module is best interpreted as a secreted extracellular-plasma protein program combining complement activity, contact coagulation, lipid transport, protease-regulatory functions, extracellular-matrix or acute-phase biology, and oxidative protection. The strongest functional interpretation comes from the identities of C1QC, C2, C6, C9, F12, APOA4, ITIH4, GPX3, SERPINF1, and related secreted proteins, rather than from enrichment statistics. No GO or KEGG term passed global correction, so there is no globally significant GO or KEGG annotation for this module. The absence of a globally enriched term does not invalidate the module. Its shared occurrence in cerebrospinal fluid and colon may primarily reflect coordinated abundance of circulating or extracellular proteins, rather than a tissue-specific intracellular pathway.

**Cell composition.** The composition strongly suggests a plasma or secreted-protein signal. HPA annotates every module gene as secreted, with many secreted to blood and several detected in vesicles. Liver enrichment is the dominant tissue pattern, while APOA4 is intestine enriched and SERPINF1 is choroid-plexus enriched. Several genes have hepatocyte, choroid-plexus, ependymal, neuronal, stromal, or epithelial associations, but immune-cell enrichment is also present for complement and acute-phase related genes. Most genes are not detected in immune cells, although C1QC, LRG1, GPX3, SERPINF1, AEBP1, C2, and F12 show immune-cell enrichment or enhancement. In colon, protein detection is sparse and uneven, whereas no cerebrospinal-fluid HPA protein detection data are available. Therefore, the shared module could reflect blood content, vascular or barrier permeability, liver-derived circulating proteins, or shared extracellular material in the sampled fluids and tissues. It should not be treated as proof of a colon-resident or cerebrospinal-fluid-resident cell program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no functional enrichment for the module. At the high-confidence interaction threshold, the established relationships are C1QC-C2 (hu.MAP huMAP3_09531.1) and C6-C9 (hu.MAP huMAP3_10101.1). The C6-C9 relationship is especially coherent with the complement membrane-attack pathway, while C1QC-C2 connects classical complement recognition with the complement cascade. Most other co-abundance edges are not supported by high-confidence STRING pairwise interactions, so they may represent coordinated secretion, shared source, correlated clearance, or uncurated extracellular associations rather than direct physical binding. hu.MAP provides repeated support for a serum or extracellular protein context. A1BG, APOA4, GPX3, and ITIH4 recur together in several complexes (hu.MAP huMAP3_09531.1) through (hu.MAP huMAP3_08395.1), and A1BG with APOA4 recurs in additional complexes (hu.MAP huMAP3_08700.1), (hu.MAP huMAP3_07432.1), and (hu.MAP huMAP3_07265.1). F12 and C6 recur together in hu.MAP complexes (hu.MAP huMAP3_14445.1) and (hu.MAP huMAP3_14656.1). These complexes contain many complement, coagulation, apolipoprotein, acute-phase, and plasma proteins. The overlap supports a shared extracellular protein environment, but the partial membership of this module in broad complexes does not establish that the entire co-abundance module is one physical complex.

**STRING interactions (score >= 0.7)**: 2 of 91 gene pairs: C1QC–C2 (0.944); C6–C9 (0.996)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09531.1 (A1BG, APOA4, GPX3, ITIH4; 4/47); huMAP3_10101.1 (A1BG, APOA4, GPX3, ITIH4; 4/49); huMAP3_15040.1 (C1QC, A1BG, APOA4, ITIH4; 4/64); huMAP3_10678.1 (A1BG, APOA4, GPX3, ITIH4; 4/71); huMAP3_09434.1 (A1BG, APOA4, ITIH4; 3/33); huMAP3_08395.1 (A1BG, APOA4, GPX3; 3/43); huMAP3_08700.1 (A1BG, APOA4; 2/11); huMAP3_07432.1 (A1BG, APOA4; 2/18); huMAP3_14445.1 (F12, C6; 2/18); huMAP3_07265.1 (A1BG, APOA4; 2/20); huMAP3_14656.1 (F12, C6; 2/21)

### Novelty

This may be a novel tissue-pair co-abundance pattern, but the fact sheet does not establish a new molecular mechanism. The individual proteins and several relationships are already well characterized: complement components, factor XII, apolipoprotein A4, and plasma antioxidant or acute-phase proteins have extensive prior literature. STRING confirms two known pairwise relationships, and hu.MAP places several subsets in previously catalogued extracellular complexes. Conversely, many module edges lack STRING support, which could indicate an uncurated association but cannot by itself prove novelty. A defensible novelty claim would require replication across independent cerebrospinal-fluid and colon datasets, control for blood contamination and protein abundance, and comparison with previously reported tissue-pair modules.

**Hypothesis.** Hypothesis: the conserved module represents a shared extracellular transport and inflammatory-surveillance compartment linking liver-derived plasma proteins with barrier-associated cerebrospinal-fluid and intestinal environments. Coordinated release or passage of apolipoprotein, complement, coagulation, protease-regulatory, and antioxidant proteins could generate the observed co-abundance pattern. APOA4 and IGFALS may reflect transport or carrier-associated abundance, C1QC, C2, C6, and C9 may reflect complement surveillance, F12 may reflect contact-system activity, and GPX3, ITIH4, LRG1, and SERPINF1 may reflect oxidative, acute-phase, vascular, or extracellular-matrix regulation. This remains a hypothesis because the module has no globally significant GO or KEGG term, STRING functional enrichment is absent, and co-abundance does not demonstrate direct interaction or causal activity.

### Important genes

#### APOA4

- **Related proteins** (co-abundance neighbors): CLEC3B (0.85), LRG1 (0.85), IGFALS (0.84), GPX3 (0.81), C9 (0.81), F12 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_08700.1, huMAP3_07432.1, huMAP3_07265.1
- **Function (MyGene.info)**: apolipoprotein A4. Apoliprotein (apo) A-IV gene contains 3 exons separated by two introns. A sequence polymorphism has been identified in the 3'UTR of the third exon.  The primary translation product is a 396-residue preprotein which after proteolytic processing is secreted its primary site of synthesis, the intestine, in association with chylomicron particles.  Although its precise function is not known, apo A-IV i…
- **Diseases (Open Targets)**: tubulointerstitial kidney disease, autosomal dominant, 2 (0.482); AL amyloidosis (0.463); metabolic syndrome (0.425); familial hyperlipidemia (0.359); diabetes mellitus (0.336)
- **Europe PMC papers**: 4955
- **Why important**: APOA4 is a highly connected module member and the clearest intestine-associated component. HPA identifies it as intestine enriched and enterocyte enriched, while the fact sheet describes secretion with chylomicron-associated synthesis and roles in lipid transport, mucosal innate immunity, and responses to lipid hydroperoxide. It recurs across many hu.MAP complexes (hu.MAP huMAP3_09531.1) through (hu.MAP huMAP3_07432.1) and (hu.MAP huMAP3_07265.1), linking it to the broad extracellular plasma-protein context. It also has extensive literature and disease associations involving lipid and metabolic disorders.
- **Conclusion**: Established evidence supports APOA4 as an intestinally sourced, secreted lipid- and stress-associated anchor of the module. Its coordination with complement and plasma proteins is plausible, but a direct mechanistic bridge between APOA4 and the other module members remains hypothetical.

#### C9

- **Related proteins** (co-abundance neighbors): IGFALS (0.85), C6 (0.84), LRG1 (0.84), C2 (0.81), APOA4 (0.81), F12 (0.81); STRING partners: C6 (0.996)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C9. This gene encodes the final component of the complement system. It participates in the formation of the Membrane Attack Complex (MAC). The MAC assembles on bacterial membranes to form a pore, permitting disruption of bacterial membrane organization. Mutations in this gene cause component C9 deficiency. [provided by RefSeq, Feb 2009].
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.747); age-related macular degeneration (0.584); complement component 9 deficiency (0.548); macular degeneration (0.541); complement deficiency (0.463)
- **Europe PMC papers**: 28081
- **Why important**: C9 is a highly connected complement component and encodes the terminal membrane-attack-complex protein. It has a direct high-confidence STRING relationship with C6 (hu.MAP huMAP3_10101.1), and C6 and C9 also recur together in hu.MAP complexes (hu.MAP huMAP3_14445.1) and (hu.MAP huMAP3_14656.1). Its complement function, deficiency phenotype, and very extensive literature make it one of the most biologically interpretable members.
- **Conclusion**: Established evidence supports C9 as a genuine complement-related component of the module and as the strongest directly supported complement pair with C6. The co-abundance pattern may indicate coordinated complement protein availability, but it does not establish active membrane attack in either tissue.

#### C6

- **Related proteins** (co-abundance neighbors): ITIH4 (0.86), C9 (0.84), IGFALS (0.80); STRING partners: C9 (0.996)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14445.1, huMAP3_14656.1
- **Function (MyGene.info)**: complement C6. This gene encodes a component of the complement cascade. The encoded protein is part of the membrane attack complex that can be incorporated into the cell membrane and cause cell lysis. Mutations in this gene are associated with complement component-6 deficiency. Transcript variants encoding the same protein have been described.[provided by RefSeq, Nov 2012].
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.753); complement deficiency (0.464); hereditary disease (0.416); male reproductive organ cancer (0.257); benign neoplasm of brain (0.199)
- **Europe PMC papers**: 88422
- **Why important**: C6 is a connected complement member, has the strongest listed STRING relationship with C9 (hu.MAP huMAP3_10101.1), and participates with C9 in hu.MAP complexes (hu.MAP huMAP3_14445.1) and (hu.MAP huMAP3_14656.1). Its established role in the membrane attack complex and complement deficiency disease gives it a clear functional interpretation despite the absence of global GO or KEGG enrichment.
- **Conclusion**: Established evidence supports C6 as a complement membrane-attack-complex component and as a structurally supported partner of C9. Its additional co-abundance links to ITIH4 and IGFALS should be regarded as module-level associations rather than demonstrated physical interactions.

#### F12

- **Related proteins** (co-abundance neighbors): SERPINF1 (0.86), C1QC (0.81), C9 (0.81), APOA4 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14445.1, huMAP3_14656.1
- **Function (MyGene.info)**: coagulation factor XII. This gene encodes coagulation factor XII which circulates in blood as a zymogen. This single chain zymogen is converted to a two-chain serine protease with an heavy chain (alpha-factor XIIa) and a light chain. The heavy chain contains two fibronectin-type domains, two epidermal growth factor (EGF)-like domains, a kringle domain and a proline-rich domain, whereas the light chain contains only a cat…
- **Diseases (Open Targets)**: congenital factor XII deficiency (0.815); hereditary angioedema type 3 (0.777); hereditary angioedema (0.677); peptic ulcer disease (0.450); angioedema (0.407)
- **Europe PMC papers**: 100014
- **Why important**: F12 connects the complement-associated portion of the module with SERPINF1, C1QC, C9, and APOA4. It is a secreted liver-enriched coagulation zymogen with established roles in the plasma kallikrein-kinin cascade, contact activation, proteolysis, coagulation, and plasminogen activation. It also recurs with C6 in hu.MAP complexes (hu.MAP huMAP3_14445.1) and (hu.MAP huMAP3_14656.1) and has exceptionally extensive literature and well-established disease associations.
- **Conclusion**: Established evidence supports F12 as a coagulation and contact-system bridge within a secreted plasma module. Whether its abundance reflects active coagulation, altered vascular permeability, or merely shared circulation requires functional or activity measurements.

#### SERPINF1

- **Related proteins** (co-abundance neighbors): F12 (0.86), AEBP1 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family F member 1. This gene encodes a member of the serpin family that does not display the serine protease inhibitory activity shown by many of the other serpin proteins. The encoded protein is secreted and strongly inhibits angiogenesis. In addition, this protein is a neurotrophic factor involved in neuronal differentiation in retinoblastoma cells. Mutations in this gene were found in individuals with osteogenesi…
- **Diseases (Open Targets)**: osteogenesis imperfecta (0.716); osteogenesis imperfecta, recessive (0.462); osteogenesis imperfecta type 3 (0.447); osteogenesis imperfecta type 4 (0.371); refractive error (0.348)
- **Europe PMC papers**: 2744
- **Why important**: SERPINF1 is important because it links F12 to AEBP1 and is the module member most specifically associated with the choroid plexus. It is a secreted protein with established anti-angiogenic and neurotrophic activities, and HPA places it in choroid-plexus-related tissue and cell contexts. Its osteogenesis-imperfecta associations and substantial literature support biological relevance beyond simple abundance correlation.
- **Conclusion**: Established evidence supports SERPINF1 as a choroid-plexus-associated secreted regulator with vascular and neuronal relevance. Its position suggests a possible barrier or extracellular-matrix connection to the cerebrospinal-fluid side of the module, but that tissue-specific interpretation remains a hypothesis.

## Module 2

**Tissue pair**: cerebrospinal_fluid and colon  
**Genes (16)**: SERPINF2, SERPINA3, APOB, SERPINA6, CP, CFB, CFI, FGA, SERPIND1, SERPING1, ITIH2, KNG1, PLG, PLTP, SEMA3C, F2

### Function

The strongest interpretation is a circulating extracellular protease-regulatory module centered on complement activation, coagulation, fibrinolysis, and blood microparticles. This is supported directly by the globally corrected KEGG complement and coagulation term (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0188) and the globally corrected blood microparticle term (GO:CC blood microparticle; q_global = 0.0405). The module combines complement components and regulators, coagulation factors, fibrinolytic proteins, and protease inhibitors. F2 and FGA support thrombin generation and fibrin formation; PLG supports plasmin-mediated fibrinolysis; CFB and CFI represent alternative-pathway complement activation and its regulation; SERPING1 regulates complement activation; and the serpins and ITIH2 provide additional protease control and extracellular-matrix stabilization. SEMA3C is a peripheral member with a secreted neuronal-guidance function, but it has no support from the enriched terms or STRING relationships in this module. The result is therefore most consistent with a blood-derived hemostasis and complement signature rather than a cell-intrinsic cerebrospinal-fluid or colon program.

**Cell composition.** All module genes are annotated as secreted proteins, and HPA tissue evidence is dominated by liver enrichment, with hepatocytes the most frequent enriched single-cell population. Most genes are not detected in immune cells, although a small subset shows immune-cell enrichment or enhancement. HPA protein detection in colon is absent for nearly all genes, with only SERPINA3 detected, while cerebrospinal-fluid protein detection has no matching HPA tissue data. This composition strongly suggests that the shared module may reflect circulating plasma proteins entering or being sampled with both biofluids, rather than coordinated expression by colon and cerebrospinal-fluid cells. The blood-microparticle result (GO:CC blood microparticle; q_global = 0.0405), plasma-protein STRING terms (STRING PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers.; within-query FDR = 0.0078), (STRING TISSUES Bone marrow; within-query FDR = 0.0095), (STRING COMPARTMENTS Blood microparticle; within-query FDR = 0.0181), (STRING Component Blood microparticle; within-query FDR = 0.0194), (STRING TISSUES Bone marrow cell; within-query FDR = 0.0236), and the liver and bone-marrow supplementary signals reinforce this interpretation. It does not by itself establish contamination, because secreted proteins can have genuine biological roles in either compartment.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 0.0188 | CFB, CFI, F2, FGA, KNG1, PLG, SERPIND1, SERPINF2, SERPING1 |
| GO:CC blood microparticle | 0.0405 | CFB, CP, F2, FGA, ITIH2, KNG1, PLG, SERPINA3, SERPINF2, SERPING1 |

### STRING and hu.MAP

STRING recapitulates a dense, biologically coherent core involving F2, FGA, PLG, SERPIND1, SERPINF2, KNG1, CFB, CFI, and SERPING1. Particularly strong relationships include the F2-FGA coagulation pair, the PLG-SERPINF2 fibrinolysis-regulatory pair, the CFB-CFI complement pair, and links connecting coagulation, fibrinolysis, and complement regulation. STRING enrichment independently supports complement and coagulation (STRING KEGG Complement and coagulation cascades; within-query FDR = 0.0054), but its FDR is supplementary rather than global evidence. hu.MAP shows repeated membership of the same module genes in several plasma-protein, complement, coagulation, and protease-regulatory complexes, especially complexes (hu.MAP huMAP3_10678.1) through (hu.MAP huMAP3_09832.1). The recurrence across complexes indicates that much of the network reflects known biochemical associations and shared extracellular assemblies. Additional hu.MAP complexes connect narrower pairs such as SERPING1-SERPINF2, SERPINA6-SERPINF2, and CFI-SERPINF2. These relationships support the module's coherence but do not prove that all proteins physically interact in the sampled tissues.

**STRING interactions (score >= 0.7)**: 28 of 120 gene pairs: APOB–F2 (0.832); APOB–FGA (0.832); APOB–ITIH2 (0.788); APOB–PLG (0.774); APOB–PLTP (0.964); CFB–CFI (0.97); CFB–SERPING1 (0.88); CFI–F2 (0.773); CFI–SERPIND1 (0.7); CP–F2 (0.703); CP–SERPINA3 (0.822); F2–FGA (0.999); F2–ITIH2 (0.852); F2–KNG1 (0.891); F2–PLG (0.826); F2–SERPIND1 (0.999); F2–SERPINF2 (0.928); FGA–ITIH2 (0.811); FGA–KNG1 (0.908); FGA–PLG (0.965); FGA–SERPIND1 (0.96); FGA–SERPINF2 (0.967); ITIH2–SERPIND1 (0.712); KNG1–PLG (0.898); KNG1–SERPIND1 (0.779); KNG1–SERPING1 (0.964); PLG–SERPIND1 (0.952); PLG–SERPINF2 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Complement and coagulation cascades (FDR = 0.0054, 9 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 0.0078, 14 genes); NetworkNeighborAL Complement and coagulation cascades, and Protein-lipid complex (FDR = 0.0079, 11 genes); NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization (FDR = 0.0079, 10 genes); TISSUES Bone marrow (FDR = 0.0095, 14 genes); WikiPathways Complement and coagulation cascades (FDR = 0.0096, 8 genes); DISEASES Monogenic disease (FDR = 0.0166, 13 genes); COMPARTMENTS Blood microparticle (FDR = 0.0181, 10 genes); Component Blood microparticle (FDR = 0.0194, 10 genes); TISSUES Bone marrow cell (FDR = 0.0236, 13 genes); DISEASES Autosomal genetic disease (FDR = 0.0239, 12 genes); DISEASES Blood coagulation disease (FDR = 0.0239, 6 genes); DISEASES Hematopoietic system disease (FDR = 0.027, 7 genes); Keyword Blood coagulation (FDR = 0.0316, 6 genes); TISSUES Liver (FDR = 0.0336, 15 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10678.1 (CP, F2, PLG, CFB, SERPINA3, KNG1, FGA, SERPING1, SERPIND1, ITIH2; 10/71); huMAP3_09531.1 (CP, F2, PLG, CFB, SERPINA3, KNG1, FGA, SERPING1, ITIH2; 9/47); huMAP3_10101.1 (CP, F2, PLG, CFB, SERPINA3, KNG1, FGA, SERPING1, ITIH2; 9/49); huMAP3_15040.1 (CP, PLG, CFB, SERPINA3, KNG1, FGA, SERPING1, SERPIND1, ITIH2; 9/64); huMAP3_08395.1 (CP, F2, PLG, CFB, SERPINA3, KNG1, FGA, ITIH2; 8/43); huMAP3_09273.1 (CP, F2, PLG, CFB, KNG1, SERPING1, ITIH2; 7/28); huMAP3_07701.1 (F2, PLG, CFB, KNG1, ITIH2; 5/22); huMAP3_08796.1 (F2, PLG, CFB, SERPINA6; 4/15); huMAP3_09832.1 (F2, PLG, CFB, SERPINA6; 4/18); huMAP3_07265.1 (CP, SERPINA3, KNG1, ITIH2; 4/20); huMAP3_02236.1 (CP, KNG1, ITIH2; 3/7); huMAP3_07432.1 (CP, SERPINA3, FGA; 3/18); huMAP3_07541.1 (F2, KNG1, ITIH2; 3/19); huMAP3_08224.1 (SERPINA3, FGA, SERPIND1; 3/21); huMAP3_09434.1 (SERPINA3, FGA, SERPIND1; 3/33); huMAP3_08889.1 (SERPING1, SERPINF2; 2/3); huMAP3_05943.1 (SERPINA6, SERPINF2; 2/6); huMAP3_00178.1 (SERPINA6, SERPINF2; 2/9); huMAP3_02242.1 (SERPINA3, FGA; 2/9); huMAP3_14445.1 (CFI, SERPINF2; 2/18); huMAP3_14656.1 (CFI, SERPINF2; 2/21); huMAP3_14295.1 (CFI, SERPINA6; 2/38)

### Novelty

This module should not be presented as a wholly new molecular pathway. Its central biology is already well established through the globally significant complement and coagulation annotation (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0188), blood microparticle annotation (GO:CC blood microparticle; q_global = 0.0405), numerous high-confidence STRING relationships, and repeated hu.MAP complex membership. The potentially novel aspect is the reproducible co-abundance of this particular combination across cerebrospinal fluid and colon, especially the inclusion of liver-derived plasma proteins and the peripheral SEMA3C association. However, the available evidence cannot establish that this cross-tissue co-abundance is a new biological mechanism. It may instead reflect shared exposure to circulating plasma proteins, blood microparticles, vascular permeability, or sample composition. Absence of a STRING or hu.MAP relationship for some members is not evidence of novelty. Replication in independent cohorts, assessment of blood contamination and vascular leakage, and comparison with matched plasma would be required before claiming a new finding.

**Hypothesis.** Hypothesis: the shared module represents a circulating plasma-protein assembly that links alternative-pathway complement surveillance with thrombin generation, fibrin formation, plasmin-dependent fibrinolysis, kinin signaling, and protease inhibition. In cerebrospinal fluid and colon, variation in vascular exchange, barrier integrity, inflammation, or microparticle content may cause these proteins to rise and fall together. SERPINA3 and SEMA3C could provide tissue-contextual links to extracellular inflammation, epithelial or stromal responses, and neural guidance, but this extension is speculative because SEMA3C lacks enrichment and STRING support in the module. A testable prediction is that module abundance will track plasma or blood-microparticle markers more closely than tissue-cell abundance, and that its apparent cross-tissue conservation will weaken after adjustment for matched plasma exposure and vascular leakage.

### Important genes

#### F2

- **Related proteins** (co-abundance neighbors): PLG (0.86); STRING partners: APOB (0.832), CFI (0.773), CP (0.703), FGA (0.999), ITIH2 (0.852), KNG1 (0.891), PLG (0.826), SERPIND1 (0.999), SERPINF2 (0.928)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_09273.1, huMAP3_07701.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07541.1
- **Function (MyGene.info)**: coagulation factor II, thrombin. This gene encodes the prothrombin protein (also known as coagulation factor II). This protein is proteolytically cleaved in multiple steps to form the activated serine protease thrombin. The activated thrombin enzyme plays an important role in thrombosis and hemostasis by converting fibrinogen to fibrin during blood clot formation, by stimulating platelet aggregation, and by activating additional …
- **Diseases (Open Targets)**: congenital prothrombin deficiency (0.827); thrombophilia due to thrombin defect (0.738); venous thromboembolism (0.727); deep vein thrombosis (0.690); blood coagulation disease (0.670)
- **Europe PMC papers**: 109299
- **Why important**: F2 is a central coagulation node in the module and has strong STRING relationships with FGA, SERPIND1, SERPINF2, KNG1, PLG, CFI, and other members. Its product is the thrombin precursor, and thrombin converts fibrinogen to fibrin while also affecting platelet activation, tissue repair, and angiogenesis. F2 is present in both primary enriched terms (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0188) and (GO:CC blood microparticle; q_global = 0.0405), appears across many STRING terms, and is represented in numerous hu.MAP complexes. Its disease associations include inherited prothrombin deficiency, thrombophilia, venous thromboembolism, and deep-vein thrombosis, with extensive literature support.
- **Conclusion**: Established evidence supports F2 as a core coagulation anchor and a major explanation for the module's hemostatic interpretation. The co-abundance pattern does not demonstrate local thrombin activation in cerebrospinal fluid or colon; it may simply reflect shared abundance of circulating prothrombin.

#### PLG

- **Related proteins** (co-abundance neighbors): F2 (0.86), CFI (0.86), SERPINF2 (0.85), ITIH2 (0.84), CFB (0.83); STRING partners: APOB (0.774), F2 (0.826), FGA (0.965), KNG1 (0.898), SERPIND1 (0.952), SERPINF2 (0.999)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_08395.1, huMAP3_09273.1, huMAP3_07701.1, huMAP3_08796.1, huMAP3_09832.1
- **Function (MyGene.info)**: plasminogen. The plasminogen protein encoded by this gene is a serine protease that circulates in blood plasma as an inactive zymogen and is converted to the active protease, plasmin, by several plasminogen activators such as tissue plasminogen activator (tPA), urokinase plasminogen activator (uPA), kallikrein, and factor XII (Hageman factor). The conversion of plasminogen to plasmin involves the cleavage of t…
- **Diseases (Open Targets)**: hypoplasminogenemia (0.813); hereditary angioedema (0.737); hemorrhage (0.605); dysplasminogenemia (0.598); Menorrhagia (0.579)
- **Europe PMC papers**: 17740
- **Why important**: PLG is a highly connected module member linking F2, FGA, CFI, SERPINF2, ITIH2, CFB, KNG1, SERPIND1, and APOB. It encodes plasminogen, the circulating precursor of plasmin, and therefore connects fibrinolysis with extracellular-matrix disassembly and collagen catabolism. PLG occurs in both primary terms (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0188) and (GO:CC blood microparticle; q_global = 0.0405), is represented in many STRING enrichment results, and recurs in a broad set of hu.MAP complexes. Its disease associations include hypoplasminogenemia, hemorrhage, dysplasminogenemia, and hereditary angioedema.
- **Conclusion**: Established evidence supports PLG as the principal fibrinolytic component and a bridge between clot formation and clot removal. The module does not establish that plasmin is active in either tissue; it indicates coordinated abundance of the precursor and its regulators.

#### CFB

- **Related proteins** (co-abundance neighbors): KNG1 (0.92), CFI (0.87), SERPIND1 (0.84), PLG (0.83), SERPINA3 (0.82), FGA (0.80); STRING partners: CFI (0.97), SERPING1 (0.88)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_08395.1, huMAP3_09273.1, huMAP3_07701.1, huMAP3_08796.1, huMAP3_09832.1
- **Function (MyGene.info)**: complement factor B. This gene encodes complement factor B, a component of the alternative pathway of complement activation. Factor B circulates in the blood as a single chain polypeptide. Upon activation of the alternative pathway, it is cleaved by complement factor D yielding the noncatalytic chain Ba and the catalytic subunit Bb. The active subunit Bb is a serine protease which associates with C3b to form the alter…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with B factor anomaly (0.764); atypical hemolytic-uremic syndrome (0.705); Immunodeficiency due to a complement cascade protein anomaly (0.614); paroxysmal nocturnal hemoglobinuria (0.561); complement 3 glomerulopathy (0.546)
- **Europe PMC papers**: 7226
- **Why important**: CFB is one of the strongest network hubs and has a direct high-confidence relationship with CFI, as well as connections to KNG1, SERPIND1, PLG, SERPINA3, FGA, and SERPING1. It is a component of the alternative complement pathway and forms the catalytic alternative-pathway convertase after activation. CFB is present in both primary terms (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0188) and (GO:CC blood microparticle; q_global = 0.0405), occurs in repeated STRING and hu.MAP complexes, and has disease associations involving complement dysregulation, atypical hemolytic-uremic syndrome, paroxysmal nocturnal hemoglobinuria, and complement-mediated glomerulopathy.
- **Conclusion**: Established evidence supports CFB as the complement-activation anchor of the module. Its co-abundance with complement inhibitor CFI and SERPING1 is compatible with coordinated activation and control, but it does not prove complement activation occurred in the sampled material.

#### CFI

- **Related proteins** (co-abundance neighbors): KNG1 (0.90), CFB (0.87), PLG (0.86), ITIH2 (0.82), SERPINF2 (0.82), CP (0.80); STRING partners: CFB (0.97), F2 (0.773), SERPIND1 (0.7)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14445.1, huMAP3_14656.1, huMAP3_14295.1
- **Function (MyGene.info)**: complement factor I. This gene encodes a serine proteinase that is essential for regulating the complement cascade. The encoded preproprotein is cleaved to produce both heavy and light chains, which are linked by disulfide bonds to form a heterodimeric glycoprotein. This heterodimer can cleave and inactivate the complement components C4b and C3b, and it prevents the assembly of the C3 and C5 convertase enzymes. Defect…
- **Diseases (Open Targets)**: complement factor I deficiency (0.798); atypical hemolytic-uremic syndrome with I factor anomaly (0.795); age-related macular degeneration (0.782); atypical hemolytic-uremic syndrome (0.639); macular degeneration (0.571)
- **Europe PMC papers**: 14453
- **Why important**: CFI is a strong network hub positioned between CFB, PLG, KNG1, ITIH2, SERPINF2, and CP. It encodes a complement-regulatory serine protease that inactivates C3b and C4b and prevents formation of complement convertases. CFI is present in the primary complement and coagulation term (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0188), appears repeatedly in STRING enrichment, and occupies dedicated hu.MAP complexes (hu.MAP huMAP3_14445.1) and (hu.MAP huMAP3_14656.1) with SERPINF2. Its disease associations include complement factor I deficiency, atypical hemolytic-uremic syndrome, and age-related macular degeneration, with substantial literature support.
- **Conclusion**: Established evidence supports CFI as a key regulatory counterweight to CFB and as evidence that the module contains both complement effectors and complement brakes. The module supports coordinated regulation, not a conclusion that complement is pathologically overactive.

#### SERPINA3

- **Related proteins** (co-abundance neighbors): SEMA3C (0.88), PLTP (0.84), CFB (0.82), KNG1 (0.81), CP (0.81); STRING partners: CP (0.822)
- **HPA**: Group enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_08395.1, huMAP3_07265.1, huMAP3_07432.1, huMAP3_08224.1, huMAP3_09434.1, huMAP3_02242.1
- **Function (MyGene.info)**: serpin family A member 3. The protein encoded by this gene is a member of the serpin family of proteins, a group of proteins that inhibit serine proteases. This gene is one in a cluster of serpin genes located on the q arm of chromosome 14. Polymorphisms in this protein appear to be tissue specific and influence protease targeting. Variations in this protein's sequence have been implicated in Alzheimer's disease, and defic…
- **Diseases (Open Targets)**: prostate carcinoma (0.359); chronic kidney disease (0.217); peripheral arterial occlusive disease 1 (0.118); central nervous system cancer (0.118); glioma (0.105)
- **Europe PMC papers**: 5458
- **Why important**: SERPINA3 connects CP, CFB, KNG1, PLTP, and SEMA3C in the co-abundance graph and is represented in the primary blood-microparticle term (GO:CC blood microparticle; q_global = 0.0405). It is a secreted serine-protease inhibitor with roles in inflammatory responses, lipid metabolism, gastrointestinal epithelial maintenance, and cytokine responses. HPA places it in liver and pancreas-enriched tissue categories and identifies astrocyte enrichment at the single-cell level; it is also the only module protein detected in colon by the reported HPA immunohistochemistry summary. Its literature volume is substantial, and the fact sheet links it to liver disease and neurodegenerative disease-related observations.
- **Conclusion**: Established evidence supports SERPINA3 as a plausible tissue-contextual and inflammatory modifier of the otherwise plasma-dominated module. Its colon detection and astrocyte annotation make it especially relevant to the tissue pair, but the network does not establish that SERPINA3 drives the module or mediates communication between colon and cerebrospinal fluid.

## Module 3

**Tissue pair**: cerebrospinal_fluid and colon  
**Genes (14)**: ACE, CDH2, EFNA1, EGFR, BPNT2, SERPINA4, LRP1, MAN2A2, MAN2B1, MEGF8, MMP2, NEO1, SEZ6L2, SEMA4D

### Function

No GO or KEGG term passed global correction, so the module does not have a statistically established pathway-level annotation. The available evidence instead supports a mixed extracellular and cell-surface regulatory module involving proteolysis, adhesion, receptor signaling, endocytosis, glycoprotein handling, and neurovascular or epithelial interface biology. SERPINA4 is the strongest network connector and is a secreted serine-protease inhibitor. MMP2 contributes extracellular-matrix proteolysis, while EGFR, LRP1, EFNA1, CDH2, NEO1, and SEMA4D represent receptor, adhesion, guidance, or signaling biology. MAN2A2, MAN2B1, and BPNT2 suggest glycoprotein processing and Golgi or lysosomal metabolism. The module therefore appears biologically heterogeneous rather than a clean canonical pathway. The absence of significant enrichment does not invalidate the module; it indicates that its interpretation should rely on individual gene functions, network structure, and sample-composition considerations.

**Cell composition.** The module contains a substantial secreted or extracellular component, including SERPINA4, EFNA1, ACE, EGFR, and MMP2, with SERPINA4, EFNA1, and ACE explicitly annotated as secreted to blood and MMP2 as secreted to the extracellular matrix. This is not a uniformly secreted module because it also contains membrane, Golgi, vesicular, and intracellular proteins. HPA evidence shows broad tissue diversity, with liver, brain, intestine, heart muscle, and other tissue associations rather than a single tissue program. Cell-type evidence is especially prominent for neutrophils, oligodendrocytes, astrocytes, excitatory neurons, and myeloid populations. Several genes have blood-cell enrichment, including monocyte, dendritic-cell, neutrophil, basophil, and platelet signals, although several other genes are not detected in immune cells. Thus, a shared blood or extracellular-protein contribution, and possibly shared myeloid or neural cell types, should be considered as explanations for co-abundance. HPA protein detection is available for colon for most genes, whereas the cerebrospinal-fluid comparison has no matching HPA tissue protein result; this should not be interpreted as evidence that the proteins are absent from cerebrospinal fluid.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited set of high-confidence physical or functional relationships: CDH2 with EGFR, CDH2 with MMP2, EFNA1 with EGFR, and EGFR with LRP1. These links provide independent support for a small receptor, adhesion, and extracellular-remodeling core, but most module gene pairs are not supported by STRING at the supplied threshold. STRING functional enrichment is absent, so there is no supplementary STRING pathway signal. hu.MAP identifies complex C1 containing ACE and SEZ6L2 among the module genes. Because only a small portion of that large complex is represented in the module, C1 supports a possible shared complex context rather than a complete module-wide complex. Overall, the external interaction resources support selected local relationships and do not establish a single unified biochemical complex.

**STRING interactions (score >= 0.7)**: 4 of 91 gene pairs: CDH2–EGFR (0.78); CDH2–MMP2 (0.834); EFNA1–EGFR (0.79); EGFR–LRP1 (0.838)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11349.1 (ACE, SEZ6L2; 2/78)

### Novelty

This module cannot be claimed as a new biological discovery from the supplied evidence alone. Its limited overlap with STRING and hu.MAP may indicate a co-abundance relationship that is not well represented in interaction databases, but database absence by itself does not demonstrate novelty. Several genes and relationships are already well established, including EGFR signaling, MMP2 extracellular-matrix activity, LRP1 endocytosis and clearance, CDH2 adhesion, and the ACE-containing hu.MAP complex. The potentially novel aspect is the cross-tissue co-abundance of these genes in cerebrospinal fluid and colon, especially the combination of a SERPINA4-centered network with neural, epithelial, myeloid, and extracellular-remodeling components. That possibility requires replication, cell-composition adjustment, protein-level validation, and comparison with other published co-abundance modules.

**Hypothesis.** Hypothesis: the shared module reflects coordinated abundance of extracellular and cell-surface proteins at tissue-fluid interfaces, produced by a mixture of epithelial, neural or glial, stromal, and myeloid sources. SERPINA4 may organize the observed co-abundance through extracellular protease inhibition and association with LRP1, EGFR, MMP2, ACE, NEO1, and BPNT2. In parallel, EGFR, EFNA1, CDH2, and SEMA4D may report adhesion and receptor-signaling states, while MAN2A2, MAN2B1, BPNT2, and the ACE-SEZ6L2 hu.MAP relationship may reflect glycoprotein processing or vesicular trafficking. A biologically plausible model is therefore a shared extracellular-remodeling and cell-contact state, potentially amplified by blood or myeloid material in the samples, rather than a single cell-intrinsic pathway. This is a hypothesis, not an established causal mechanism.

### Important genes

#### SERPINA4

- **Related proteins** (co-abundance neighbors): LRP1 (0.88), ACE (0.86), EGFR (0.85), MAN2B1 (0.84), NEO1 (0.84), MMP2 (0.83), BPNT2 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family A member 4. Predicted to enable serine-type endopeptidase inhibitor activity. Predicted to be involved in negative regulation of endopeptidase activity. Located in extracellular exosome. Biomarker of diabetic retinopathy. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: optic atrophy (0.169); chronic kidney disease (0.129); diabetes mellitus (0.096); triple-A syndrome (0.088); fatty liver disease (0.077)
- **Europe PMC papers**: 909
- **Why important**: SERPINA4 has the strongest network position in the module and connects to LRP1, ACE, EGFR, MAN2B1, NEO1, MMP2, and BPNT2. It is a secreted blood protein with liver enrichment and is annotated as a serine-type endopeptidase inhibitor. Its network centrality and extracellular localization make it the leading candidate for coordinating the module, while its disease and biomarker associations show substantial prior biological attention.
- **Conclusion**: Established evidence: SERPINA4 is a secreted serine-protease inhibitor and the principal network connector. Hypothesis: it may mark or help regulate an extracellular protease-remodeling state shared between the sampled tissues. The data do not establish that SERPINA4 causally drives the module.

#### EGFR

- **Related proteins** (co-abundance neighbors): SERPINA4 (0.85); STRING partners: CDH2 (0.78), EFNA1 (0.79), LRP1 (0.838)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus, Plasma membrane; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: epidermal growth factor receptor. The protein encoded by this gene is a transmembrane glycoprotein that is a member of the protein kinase superfamily. This protein is a receptor for members of the epidermal growth factor family. EGFR is a cell surface protein that binds to epidermal growth factor, thus inducing receptor dimerization and tyrosine autophosphorylation leading to cell proliferation. Mutations in this gene are associat…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.850); lung adenocarcinoma (0.774); cancer (0.737); head and neck squamous cell carcinoma (0.725); lung cancer (0.717)
- **Europe PMC papers**: 223694
- **Why important**: EGFR is linked in STRING to CDH2, EFNA1, and LRP1, providing a supported receptor-signaling bridge between several module components. It is a cell-surface receptor tyrosine kinase with extensive literature and strong cancer associations, and it is detected by HPA in colon. Its network position is modest within the co-abundance graph, but its biological interpretability and external interaction support are strong.
- **Conclusion**: Established evidence: EGFR mediates epidermal-growth-factor receptor signaling and has known relationships with CDH2, EFNA1, and LRP1. Hypothesis: EGFR-related signaling may couple epithelial or stromal state to the extracellular proteins in this module. The co-abundance data do not show that EGFR signaling is activated.

#### MMP2

- **Related proteins** (co-abundance neighbors): NEO1 (0.94), SERPINA4 (0.83); STRING partners: CDH2 (0.834)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: matrix metallopeptidase 2. This gene is a member of the matrix metalloproteinase (MMP) gene family, that are zinc-dependent enzymes capable of cleaving components of the extracellular matrix and molecules involved in signal transduction. The protein encoded by this gene is a gelatinase A, type IV collagenase, that contains three fibronectin type II repeats in its catalytic site that allow binding of denatured type IV and V …
- **Diseases (Open Targets)**: Torg-Winchester syndrome (0.780); multicentric osteolysis-nodulosis-arthropathy spectrum (0.705); Nodulosis-arthropathy-osteolysis syndrome (0.655); non-small cell lung carcinoma (0.370); fibroblastic disorder (0.356)
- **Europe PMC papers**: 40510
- **Why important**: MMP2 is connected to the central SERPINA4 node and NEO1 in the module and has a STRING relationship with CDH2. It is a secreted extracellular-matrix metalloprotease involved in proteolysis, angiogenesis, and response to hypoxia, with extensive literature and multiple disease associations. It provides a direct mechanistic link to matrix remodeling.
- **Conclusion**: Established evidence: MMP2 is an extracellular-matrix protease and is supported by both module connectivity and a STRING interaction with CDH2. Hypothesis: MMP2 may contribute to matrix turnover or release of signaling cues at the cerebrospinal-fluid or colon interface. The module does not establish increased enzyme activity or proteolytic causality.

#### LRP1

- **Related proteins** (co-abundance neighbors): SERPINA4 (0.88); STRING partners: EGFR (0.838)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LDL receptor related protein 1. This gene encodes a member of the low-density lipoprotein receptor family of proteins. The encoded preproprotein is proteolytically processed by furin to generate 515 kDa and 85 kDa subunits that form the mature receptor (PMID: 8546712). This receptor is involved in several cellular processes, including intracellular signaling, lipid homeostasis, and clearance of apoptotic cells. In addition, the …
- **Diseases (Open Targets)**: neurodegenerative disease (0.514); keratosis pilaris atrophicans (0.499); developmental dysplasia of the hip (0.466); Alzheimer disease (0.462); Parkinson disease (0.443)
- **Europe PMC papers**: 10645
- **Why important**: LRP1 connects to SERPINA4 in the module and to EGFR in STRING. It is a plasma-membrane receptor involved in lipid homeostasis, receptor-mediated endocytosis, phagocytosis, apoptotic-cell clearance, and astrocyte immune responses. Its HPA associations include fibroblasts, hepatocytes, Kupffer cells, and monocyte populations, making it relevant to both tissue and sample-composition interpretations.
- **Conclusion**: Established evidence: LRP1 is a multifunctional clearance and signaling receptor with neural, stromal, hepatic, and myeloid relevance. Hypothesis: LRP1 may couple uptake or clearance of secreted extracellular proteins to the observed SERPINA4 and EGFR-associated module. The data cannot distinguish a functional LRP1 program from co-abundance caused by shared cell sources.

#### SEZ6L2

- **Related proteins** (co-abundance neighbors): MEGF8 (0.84), MAN2A2 (0.84), SEMA4D (0.83), BPNT2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_11349.1
- **Function (MyGene.info)**: seizure related 6 homolog like 2. This gene encodes a seizure-related protein that is localized on the cell surface. The gene is located in a region of chromosome 16p11.2 that is thought to contain candidate genes for autism spectrum disorders (ASD), though there is no evidence directly implicating this gene in ASD. Increased expression of this gene has been found in lung cancers, and the protein is therefore considered to be a no…
- **Diseases (Open Targets)**: neurodegenerative disease (0.274); colorectal carcinoma (0.077); hepatocellular carcinoma (0.075); intrahepatic cholangiocarcinoma (0.074); neoplasm (0.065)
- **Europe PMC papers**: 559
- **Why important**: SEZ6L2 has a neural tissue signature, is enriched in excitatory and inhibitory brain neurons and pituitary cell types, and is detected in colon. It participates in the hu.MAP complex C1 with ACE and has module connections to MEGF8, MAN2A2, SEMA4D, and BPNT2. Its annotations include synapse maturation and adult locomotory behavior, while disease resources connect it to neurodegenerative disease and cancer. It therefore represents the strongest neural-facing component of the shared module.
- **Conclusion**: Established evidence: SEZ6L2 is a cell-surface seizure-related protein with neural expression and membership in hu.MAP complex C1. Hypothesis: it may indicate a neural or glial contribution to the cerebrospinal-fluid side of the module, or a shared membrane-trafficking state. The available evidence does not demonstrate a direct functional interaction with the other module genes.

## Module 5

**Tissue pair**: cerebrospinal_fluid and colon  
**Genes (12)**: AMBP, APOC1, ITIH1, KLKB1, LUM, OGN, NEGR1, DCN, PRELP, SOD3, TNXB, AZGP1

### Function

The strongest supported function is extracellular-matrix organization and resistance to compression. The globally corrected GO term (GO:MF extracellular matrix structural constituent conferring compression resistance; q_global = 0.0377) identifies an extracellular-matrix structural-constituent function involving DCN, LUM, OGN, and PRELP. These genes are small leucine-rich proteoglycans or related matrix proteins involved in collagen fibril assembly, collagen binding, basement-membrane anchoring, and regulation of matrix spacing. TNXB adds an extracellular glycoprotein associated with matrix maturation and cell adhesion, while SOD3 can provide extracellular protection from oxidative stress. The STRING domain results (STRING SMART Leucine rich repeat N-terminal domain; within-query FDR = 0.0463) and (STRING SMART Leucine-rich repeats, outliers; within-query FDR = 0.0463) independently support a shared leucine-rich-repeat architecture among the core matrix genes, but they are supplementary rather than globally corrected enrichment evidence. No additional GO or KEGG term passed global correction. The sparse network therefore appears to represent a matrix-centered program with peripheral circulating and neuronal or vascular proteins, rather than a broad intracellular pathway.

**Cell composition.** The module is strongly enriched for extracellular and secreted proteins: almost all members have HPA secretome annotations, including proteins secreted to blood, secreted to extracellular matrix, or secreted in other tissues. Several genes are liver-enriched and hepatocyte-enriched, including AMBP, KLKB1, ITIH1, APOC1, and AZGP1, indicating a substantial plasma or liver-derived component. Other members are enriched in fibroblasts, hepatic stellate cells, blood vessels, choroid plexus, or neural cell types. HPA also reports immune-cell enrichment or enhancement for several genes, although many members are not detected in immune cells. This combination means the shared CSF-colon module could reflect extracellular matrix biology, but it could also partly reflect circulating plasma proteins, vascular or stromal material, or shared sample-associated cell types. HPA provides no matching protein-detection data for cerebrospinal fluid, while colon protein detection is limited and incomplete, so tissue origin should not be inferred from the co-abundance pattern alone.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF extracellular matrix structural constituent conferring compression resistance | 0.0377 | DCN, LUM, OGN, PRELP |

### STRING and hu.MAP

STRING supports a coherent extracellular-matrix subnetwork: DCN is connected with LUM and OGN, LUM is connected with DCN, OGN, and PRELP, and PRELP is connected with OGN. STRING also supports the plasma-protein relationship between AMBP and ITIH1. These are already known or database-supported relationships and make the matrix portion of the module biologically credible, but they also show that the network is not uniformly connected: several module genes have no listed high-confidence STRING partner within the module. The leucine-rich-repeat annotations (STRING SMART Leucine rich repeat N-terminal domain; within-query FDR = 0.0463) and (STRING SMART Leucine-rich repeats, outliers; within-query FDR = 0.0463) reinforce the shared domain architecture of DCN, LUM, PRELP, and OGN. hu.MAP identifies APOC1 and LUM together in complex C1. However, that complex contains many proteins associated with immune, myeloid, and secreted biology, so the hu.MAP result is better viewed as evidence of a broad molecular context than as proof of a dedicated module-specific complex. Overall, STRING and hu.MAP show that parts of the module reproduce established protein relationships, while the full cross-tissue co-abundance structure extends beyond currently documented physical complexes.

**STRING interactions (score >= 0.7)**: 6 of 66 gene pairs: AMBP–ITIH1 (0.951); DCN–LUM (0.978); DCN–OGN (0.711); LUM–OGN (0.859); LUM–PRELP (0.771); OGN–PRELP (0.8)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Leucine rich repeat N-terminal domain (FDR = 0.0463, 4 genes); SMART Leucine-rich repeats, outliers (FDR = 0.0463, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14295.1 (APOC1, LUM; 2/38)

### Novelty

The individual biology is not new: the matrix proteins, plasma proteins, lipid-associated proteins, and known STRING relationships are established. The data therefore do not justify calling the molecular components newly discovered. The potentially novel observation is the conserved co-abundance of this particular extracellular-matrix and circulating-protein combination across cerebrospinal fluid and colon. That module-level cross-tissue relationship may be a new systems-level finding, but it requires replication, control for blood or stromal carryover, and comparison with independent tissue cohorts. Absence of a complete match in STRING or hu.MAP would not by itself establish novelty, because those resources primarily document physical interactions or complexes rather than every conserved co-abundance relationship.

**Hypothesis.** Hypothesis: the module reflects a composite extracellular-matrix and fluid-protein program. A stromal or vascular matrix component, centered on DCN, LUM, PRELP, OGN, and TNXB, may organize collagen-rich extracellular material and influence tissue compression, adhesion, and matrix maturation. In parallel, liver-derived or circulating proteins such as AMBP, ITIH1, KLKB1, APOC1, and AZGP1 may enter or influence both sample types through blood or extracellular-fluid exposure. The conserved signal could therefore arise from genuine matrix biology shared by colon and cerebrospinal-fluid-associated tissues, from shared vascular or stromal material, or from a mixture of matrix and plasma contributions. This hypothesis predicts that the matrix genes should co-vary in stromal or vascular compartments, whereas the liver-secreted genes should track blood exposure or fluid contamination more strongly.

### Important genes

#### DCN

- **Related proteins** (co-abundance neighbors): TNXB (0.87), LUM (0.81); STRING partners: LUM (0.978), OGN (0.711)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: decorin. This gene encodes a member of the small leucine-rich proteoglycan family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature protein. This protein plays a role in collagen fibril assembly. Binding of this protein to multiple cell surface receptors mediates its role in tumor…
- **Diseases (Open Targets)**: congenital stromal corneal dystrophy (0.696); lagophthalmos (0.295); refractive error (0.234); type 2 diabetes mellitus (0.224); hereditary disease (0.193)
- **Europe PMC papers**: 11630
- **Why important**: DCN is a central member of the matrix subnetwork, linking TNXB and LUM, and it belongs to the globally supported extracellular-matrix term (GO:MF extracellular matrix structural constituent conferring compression resistance; q_global = 0.0377) and both supplementary STRING domain terms (STRING SMART Leucine rich repeat N-terminal domain; within-query FDR = 0.0463) and (STRING SMART Leucine-rich repeats, outliers; within-query FDR = 0.0463). Its established functions include collagen fibril assembly, extracellular-matrix organization, and receptor-mediated effects on angiogenesis, endothelial migration, autophagy, and inflammation. It also has a particularly extensive literature base among the module genes, making it a strong biological anchor.
- **Conclusion**: Established evidence supports DCN as an extracellular-matrix organizer and a credible driver of the matrix portion of the module. The co-abundance data support its participation in the shared matrix program, but do not establish that DCN causes the cross-tissue association or that its signaling functions are active in these samples.

#### LUM

- **Related proteins** (co-abundance neighbors): KLKB1 (0.83), DCN (0.81); STRING partners: DCN (0.978), OGN (0.859), PRELP (0.771)
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14295.1
- **Function (MyGene.info)**: lumican. This gene encodes a member of the small leucine-rich proteoglycan (SLRP) family that includes decorin, biglycan, fibromodulin, keratocan, epiphycan, and osteoglycin. In these bifunctional molecules, the protein moiety binds collagen fibrils and the highly charged hydrophilic glycosaminoglycans regulate interfibrillar spacings. Lumican is the major keratan sulfate proteoglycan of the cornea but is …
- **Diseases (Open Targets)**: lumbar disc herniation (0.359); Dupuytren Contracture (0.357); fibroblastic disorder (0.357); Hallux valgus (0.357); preeclampsia (0.154)
- **Europe PMC papers**: 14825
- **Why important**: LUM is part of the core matrix cluster and is linked in STRING to DCN, OGN, and PRELP. It appears in the globally supported term (GO:MF extracellular matrix structural constituent conferring compression resistance; q_global = 0.0377), in the supplementary domain terms (STRING SMART Leucine rich repeat N-terminal domain; within-query FDR = 0.0463) and (STRING SMART Leucine-rich repeats, outliers; within-query FDR = 0.0463), and in the hu.MAP complex C1 with APOC1. Lumican binds collagen fibrils and regulates interfibrillar spacing, making it directly relevant to the compression-resistance interpretation. It also has a substantial literature base and tissue evidence for stromal and vascular association.
- **Conclusion**: Established evidence supports LUM as a structural extracellular-matrix proteoglycan that helps explain the module's functional enrichment and network coherence. Its hu.MAP association with APOC1 may indicate a broader extracellular or sample-context connection, but does not prove a specific physical bridge between the matrix and plasma components in this module.

#### PRELP

- **Related proteins** (co-abundance neighbors): NEGR1 (0.87), OGN (0.82); STRING partners: LUM (0.771), OGN (0.8)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proline and arginine rich end leucine rich repeat protein. The protein encoded by this gene is a leucine-rich repeat protein present in connective tissue extracellular matrix. This protein functions as a molecule anchoring basement membranes to the underlying connective tissue. This protein has been shown to bind type I collagen to basement membranes and type II collagen to cartilage. It also binds the basement membrane heparan sulfate proteoglycan perlec…
- **Diseases (Open Targets)**: osteoarthritis, hip (0.299); cervical carcinoma (0.230); ovarian neoplasm (0.219); arthropathy (0.169); liver disorder (0.167)
- **Europe PMC papers**: 1236
- **Why important**: PRELP is a matrix leucine-rich-repeat protein in (GO:MF extracellular matrix structural constituent conferring compression resistance; q_global = 0.0377), (STRING SMART Leucine rich repeat N-terminal domain; within-query FDR = 0.0463), and (STRING SMART Leucine-rich repeats, outliers; within-query FDR = 0.0463). It connects the matrix-associated OGN branch with NEGR1 in the co-abundance network and is known to anchor basement membranes to connective tissue by binding collagen and perlecan. Its fibroblast and vascular expression pattern makes it relevant to a stromal interpretation, while its literature and disease associations provide independent biological context.
- **Conclusion**: Established evidence supports PRELP as a basement-membrane and connective-tissue organizer. Its network placement is consistent with a matrix scaffold hypothesis, but the co-abundance data alone cannot determine whether PRELP is structurally causal, a shared marker of fibroblasts, or both.

#### TNXB

- **Related proteins** (co-abundance neighbors): AZGP1 (0.89), DCN (0.87), SOD3 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tenascin XB. This gene encodes a member of the tenascin family of extracellular matrix glycoproteins. The tenascins have anti-adhesive effects, as opposed to fibronectin which is adhesive. This protein is thought to function in matrix maturation during wound healing, and its deficiency has been associated with the connective tissue disorder Ehlers-Danlos syndrome. This gene localizes to the major histocompatib…
- **Diseases (Open Targets)**: Ehlers-Danlos syndrome due to tenascin-X deficiency (0.795); vesicoureteral reflux 8 (0.703); Abnormality of the cardiovascular system (0.550); Ehlers-Danlos syndrome (0.522); hereditary disease (0.390)
- **Europe PMC papers**: 2382
- **Why important**: TNXB has the strongest apparent network connectivity within the module and links AZGP1, DCN, and SOD3, thereby connecting matrix-associated proteins with secreted blood and antioxidant proteins. It is a secreted extracellular-matrix glycoprotein involved in matrix maturation and cell adhesion, and deficiency is associated with Ehlers-Danlos syndrome. Unlike the core leucine-rich-repeat cluster, it has no listed STRING partner or hu.MAP complex in the fact sheet, making its co-abundance placement informative beyond previously catalogued interactions.
- **Conclusion**: Established evidence supports TNXB as a biologically important extracellular-matrix component with disease relevance. Its network position suggests that it may help connect the matrix signal to circulating or vascular proteins, but that bridging role remains an inference rather than a demonstrated molecular interaction.

#### AMBP

- **Related proteins** (co-abundance neighbors): NEGR1 (0.88), KLKB1 (0.87), ITIH1 (0.82); STRING partners: ITIH1 (0.951)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alpha-1-microglobulin/bikunin precursor. This gene encodes a complex glycoprotein secreted in plasma. The precursor is proteolytically processed into distinct functioning proteins: alpha-1-microglobulin, which belongs to the superfamily of lipocalin transport proteins and may play a role in the regulation of inflammatory processes, and bikunin, which is a urinary trypsin inhibitor belonging to the superfamily of Kunitz-type protease inhi…
- **Diseases (Open Targets)**: systemic lupus erythematosus (0.086); ovarian neoplasm (0.072); posterior cortical atrophy (0.064); breast carcinoma (0.060); diabetes mellitus (0.060)
- **Europe PMC papers**: 1653
- **Why important**: AMBP has high network connectivity and links NEGR1, KLKB1, and ITIH1. It is liver- and hepatocyte-enriched, secreted into blood, and forms a known STRING relationship with ITIH1. Its processed products participate in inflammatory regulation and protease inhibition, so it is a useful marker of the module's circulating-protein component rather than its core matrix function. It also has substantial literature and disease-context coverage.
- **Conclusion**: Established evidence supports AMBP as a liver-derived plasma protein with inflammatory and protease-regulatory functions. In this module, its presence may reflect genuine extracellular-fluid biology or blood contribution to the samples; it should not be interpreted as evidence that AMBP is an extracellular-matrix structural constituent.

## Module 6

**Tissue pair**: cerebrospinal_fluid and colon  
**Genes (22)**: ANGPTL2, APOA2, APOE, C1R, C1S, CTSC, CPB2, C5, C7, C8B, C8G, EFNB2, EPHB2, ITIH5, LAMB1, LAMC1, MAN1A1, OLFML3, PTPRF, PLXDC2, GM2A, SPINT2

### Function

No GO or KEGG term passed global multiple-testing correction, so the module does not have statistically established pathway enrichment from those analyses. The strongest biological interpretation comes from the gene identities and network structure: a circulating extracellular protease, complement, membrane-attack-complex, lipid-transport, and extracellular-matrix module. C1R and C1S form the classical complement protease pair; C5, C7, C8B, and C8G connect to terminal complement and membrane-attack-complex biology; CPB2 links the complement subnetwork to proteolysis and fibrinolysis; and LAMB1 with LAMC1 represents basement-membrane laminin. APOA2 and APOE indicate a lipid-transport component, while ANGPTL2, OLFML3, and the laminins provide extracellular signaling or matrix context. This is therefore best described as a mixed circulating innate-defense, protease-regulatory, lipid-transport, and matrix-associated module rather than a single proven pathway. STRING supports the complement and laminin interpretations through known protein relationships, while hu.MAP supports C1R–C1S and LAMB1–LAMC1 complexes and places C5 with APOA2 in broad plasma-protein complexes.

**Cell composition.** The module is strongly dominated by secreted or extracellular proteins, with many proteins secreted to blood or to extracellular matrix. HPA tissue annotations are especially frequent for liver, and hepatocytes are a recurring enriched cell type. Most genes are not detected as immune-cell specific, although a small subset has myeloid or other blood-cell associations. This pattern is more consistent with circulating plasma proteins, liver-derived proteins, and extracellular matrix material than with a colon-resident immune-cell program. The shared cerebrospinal-fluid and colon signal could therefore reflect common exposure to circulating proteins, vascular or barrier-associated material, or shared stromal and epithelial biology. Colon protein detection is present for several membrane, matrix, and intracellular members, whereas many liver-enriched secreted proteins are not detected in colon tissue by HPA. The module should consequently not be interpreted as evidence that all of its genes are produced by the same colon cell population.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING contains established high-confidence relationships among APOA2 and APOE, C1R and C1S, the C5–C7–C8B–C8G terminal-complement group, and LAMB1 and LAMC1. STRING also connects CPB2 to C5 and to C8B, providing a plausible protease-regulatory bridge. EFNB2 and EPHB2 are a separate known receptor–ligand relationship, although they are peripheral in the co-abundance network. hu.MAP independently supports a C1R–C1S complex and a LAMB1–LAMC1 laminin complex. Additional hu.MAP complexes place C5 and APOA2 within broad plasma-protein assemblies, but those complexes contain many members outside this module and therefore do not establish a module-specific physical complex. Overall, the database evidence supports several real molecular subassemblies embedded in a co-abundance module; it does not show that all module proteins physically interact or form one unified complex.

**STRING interactions (score >= 0.7)**: 13 of 231 gene pairs: APOA2–APOE (0.999); C1R–C1S (0.999); C1R–C8G (0.717); C5–C7 (0.999); C5–C8B (0.999); C5–C8G (0.997); C5–CPB2 (0.847); C7–C8B (0.991); C7–C8G (0.994); C8B–C8G (0.999); C8B–CPB2 (0.716); EFNB2–EPHB2 (0.999); LAMB1–LAMC1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04360.1 (C1R, C1S; 2/2); huMAP3_01175.1 (LAMB1, LAMC1; 2/2); huMAP3_00148.1 (C1R, C1S; 2/3); huMAP3_10944.1 (C1R, C1S; 2/5); huMAP3_08112.1 (LAMB1, LAMC1; 2/5); huMAP3_14233.1 (LAMB1, LAMC1; 2/14); huMAP3_08395.1 (C5, APOA2; 2/43); huMAP3_09531.1 (C5, APOA2; 2/47); huMAP3_10101.1 (C5, APOA2; 2/49); huMAP3_10678.1 (C5, APOA2; 2/71)

### Novelty

The module is not convincingly a wholly new molecular mechanism. Its central complement, lipid-transport, laminin, and plasma-protein relationships are already represented in STRING and hu.MAP, and the individual functions of many genes are well established. The potentially novel observation is the coordinated co-abundance of these already known components across cerebrospinal fluid and colon. That cross-tissue association could be biologically informative, but novelty cannot be established from the supplied evidence alone. In particular, absence of some genes or edges from STRING or hu.MAP would not prove novelty, because those resources emphasize known physical or curated relationships rather than every tissue-specific co-abundance pattern. Independent replication, comparison with existing cerebrospinal-fluid and colon proteomic modules, and adjustment for blood or liver-derived protein contribution would be needed to claim a new conserved mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared extracellular and vascular-barrier environment in which liver-derived circulating complement, lipid-transport, and protease-regulatory proteins co-vary with tissue or barrier-associated laminin and signaling proteins. In cerebrospinal fluid, this could arise from transport across or activity near the choroid-plexus or other vascular barriers; in colon, it could reflect exposure of the tissue proteome to plasma together with basement-membrane and epithelial components. Complement activation and protease regulation may influence extracellular matrix or epithelial states, while APOA2 and APOE may provide a lipid-associated carrier context. This is a mechanistic proposal, not a demonstrated causal pathway, and the strong secreted-protein composition makes a shared circulating source or sample-blood contribution an important alternative explanation.

### Important genes

#### C5

- **Related proteins** (co-abundance neighbors): C8B (0.88), C1S (0.85), C7 (0.84), C1R (0.84), C8G (0.80); STRING partners: C7 (0.999), C8B (0.999), C8G (0.997), CPB2 (0.847)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: complement C5. This gene encodes a component of the complement system, a part of the innate immune system that plays an important role in inflammation, host homeostasis, and host defense against pathogens. The encoded preproprotein is proteolytically processed to generate multiple protein products, including the C5 alpha chain, C5 beta chain, C5a anaphylatoxin and C5b. The C5 protein is comprised of the C5 alpha…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.744); paroxysmal nocturnal hemoglobinuria (0.610); myasthenia gravis (0.586); atypical hemolytic-uremic syndrome (0.544); neuromyelitis optica (0.516)
- **Europe PMC papers**: 81450
- **Why important**: C5 is a central high-connectivity complement node and links directly to C7, C8B, C8G, and C1S in the module network. Its established biology spans complement activation, inflammatory signaling, chemotaxis, and generation of terminal-complement products. It has very extensive literature and strong disease associations involving complement deficiency and immune-mediated disorders. STRING also supports its relationships with the terminal-complex proteins and with CPB2, while hu.MAP places it in broad complement and plasma-protein assemblies.
- **Conclusion**: Established evidence supports C5 as a major complement hub and a biologically important anchor of the module. The module data support coordinated abundance with other complement components, but do not demonstrate that C5 activation is occurring or that C5 drives the cerebrospinal-fluid–colon association.

#### C1R

- **Related proteins** (co-abundance neighbors): C1S (0.87), C5 (0.84), ANGPTL2 (0.82), C8B (0.81), C7 (0.80), C8G (0.80); STRING partners: C1S (0.999), C8G (0.717)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_04360.1, huMAP3_00148.1, huMAP3_10944.1
- **Function (MyGene.info)**: complement C1r. This gene encodes a member of the peptidase S1 protein family. The encoded protein is a proteolytic subunit in the complement system C1 complex. The complement system acts as a mediator in the innate immune response by ultimately triggering phagocytosis, inflammation, and rupturing the bacterial cell wall. Mutations in this gene are associated with Ehlers-Danlos Syndrome. [provided by RefSeq, Dec …
- **Diseases (Open Targets)**: Ehlers-Danlos syndrome, periodontitis type (0.715); immunodeficiency due to a classical component pathway complement deficiency (0.555); coronary artery disorder (0.486); systemic lupus erythematosus (0.467); complement deficiency (0.463)
- **Europe PMC papers**: 5739
- **Why important**: C1R has high network connectivity to C1S and several downstream complement proteins. It is the proteolytic subunit of the C1 complement complex, and its known roles include classical complement activation, zymogen activation, and proteolysis. It has substantial literature and disease associations involving complement deficiency and connective-tissue disease. Its C1R–C1S relationship is supported by STRING and by a high-confidence hu.MAP complex.
- **Conclusion**: Established evidence identifies C1R as a credible entry-point or organizational component of the classical complement subnetwork. The co-abundance pattern is compatible with coordinated complement availability, but it cannot distinguish intact circulating protein from local synthesis or activation.

#### C7

- **Related proteins** (co-abundance neighbors): CPB2 (0.91), ANGPTL2 (0.89), OLFML3 (0.87), C5 (0.84), C1S (0.81), PLXDC2 (0.81), C1R (0.80); STRING partners: C5 (0.999), C8B (0.991), C8G (0.994)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C7. This gene encodes a serum glycoprotein that forms a membrane attack complex together with complement components C5b, C6, C8, and C9 as part of the terminal complement pathway of the innate immune system. The protein encoded by this gene contains a cholesterol-dependent cytolysin/membrane attack complex/perforin-like (CDC/MACPF) domain and belongs to a large family of structurally related molecules…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.785); complement deficiency (0.463); alcohol drinking (0.271); inflammatory bowel disease (0.207); hereditary disease (0.194)
- **Europe PMC papers**: 36065
- **Why important**: C7 is among the highest-connectivity genes in the module and connects the terminal complement proteins with CPB2, ANGPTL2, OLFML3, PLXDC2, and the C1 components. It is a secreted blood protein that participates in membrane-attack-complex formation. It has strong literature and established associations with late complement deficiency and inflammatory bowel disease. STRING supports its relationships with C5, C8B, and C8G.
- **Conclusion**: Established evidence supports C7 as a terminal-complement hub and a useful marker of the module's circulating innate-defense component. Its additional co-abundance links to matrix and signaling proteins are observational and should not be interpreted as direct physical interactions without independent validation.

#### LAMC1

- **Related proteins** (co-abundance neighbors): OLFML3 (0.84), LAMB1 (0.80); STRING partners: LAMB1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Plasma membrane; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_01175.1, huMAP3_08112.1, huMAP3_14233.1
- **Function (MyGene.info)**: laminin subunit gamma 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: Fuchs' endothelial dystrophy (0.487); prostate carcinoma (0.467); colorectal cancer (0.447); eye disorder (0.434); benign colon neoplasm (0.427)
- **Europe PMC papers**: 4227
- **Why important**: LAMC1 is a matrix-secreted laminin subunit with a direct module relationship to LAMB1 and an additional connection to OLFML3. Laminins are established basement-membrane components involved in adhesion, migration, tissue development, signaling, and neurite outgrowth. HPA detects LAMC1 in colon and associates it with fibroblast- and stromal-related cell types. STRING and hu.MAP independently support the LAMC1–LAMB1 laminin relationship, and the gene has substantial disease and cancer literature.
- **Conclusion**: Established evidence supports LAMC1 as the clearest extracellular-matrix anchor of the module and as a plausible tissue-associated counterpart to its circulating protein component. It remains unproven whether LAMC1 abundance is locally regulated by complement or merely co-varies because of shared tissue, vascular, or sample-composition effects.

#### APOE

- **Related proteins** (co-abundance neighbors): OLFML3 (0.80); STRING partners: APOA2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein E. The protein encoded by this gene is a major apoprotein of the chylomicron. It binds to a specific liver and peripheral cell receptor, and is essential for the normal catabolism of triglyceride-rich lipoprotein constituents. This gene maps to chromosome 19 in a cluster with the related apolipoprotein C1 and C2 genes. Mutations in this gene result in familial dysbetalipoproteinemia, or type III hype…
- **Diseases (Open Targets)**: hyperlipoproteinemia type 3 (0.803); coronary artery disorder (0.782); lipoprotein glomerulopathy (0.759); Alzheimer disease (0.696); familial hypercholesterolemia (0.651)
- **Europe PMC papers**: 74272
- **Why important**: APOE represents the lipid-transport component and is tissue-enhanced in brain, liver, and adrenal gland, making it particularly relevant to a cerebrospinal-fluid context while also fitting a circulating-protein interpretation. It participates in lipoprotein metabolism and receptor-mediated uptake, has extensive literature, and has established associations with dyslipidemia, coronary disease, and Alzheimer disease. STRING supports its relationship with APOA2, and hu.MAP places APOA2 with C5 in broad plasma-protein complexes.
- **Conclusion**: Established evidence supports APOE as a biologically important carrier and lipid-homeostasis marker that may help explain the module's presence in cerebrospinal fluid and blood-exposed tissues. The module does not establish a direct mechanistic interaction between APOE and complement or prove that lipid metabolism regulates the other module members.

## Module 7

**Tissue pair**: cerebrospinal_fluid and colon  
**Genes (9)**: COL1A1, COL1A2, COL6A1, COL6A3, COL12A1, FBN1, LAMA4, HSPG2, VTN

### Function

The module is a coherent extracellular-matrix structural and adhesion program. Every module gene supports the globally corrected extracellular-matrix structural-constituent and external-encapsulating-structure annotations (GO:MF extracellular matrix structural constituent; q_global = 3.28e-05) (GO:CC external encapsulating structure; q_global = 3.87e-05) (GO:CC extracellular matrix; q_global = 3.87e-05), while the structural-molecule and tensile-strength annotations reinforce a role in matrix assembly and mechanical support (GO:MF structural molecule activity; q_global = 7.35e-05) (GO:MF extracellular matrix structural constituent conferring tensile strength; q_global = 0.00204). The collagen-trimer and basement-membrane annotations (GO:CC complex of collagen trimers; q_global = 0.00118) (GO:CC collagen trimer; q_global = 0.0142) (GO:CC basement membrane; q_global = 0.0493), together with ECM-receptor interaction, integrin signaling, focal adhesion, and PI3K–Akt pathway enrichment (4 globally significant GO/KEGG terms, q_global 0.000123–0.00389; see the table), indicate a matrix scaffold that can influence cell attachment, migration, mechanotransduction, and signaling. The infection-related pathway terms should be interpreted as pathway-gene overlap rather than evidence that the module is an infection-specific program (KEGG Human papillomavirus infection - Homo sapiens (human); q_global = 0.00122) (STRING KEGG Human papillomavirus infection; within-query FDR = 0.00012).

**Cell composition.** All module genes are secreted extracellular-matrix or blood-associated proteins according to the HPA summary. HPA reports that the genes are not detected in immune cells, arguing against a blood-cell or leukocyte module. The dominant single-cell associations are fibroblasts, fibro-adipogenic progenitors, hepatic stellate cells, and stromal cell populations, supporting a mesenchymal or stromal source rather than a hematopoietic source. Several genes are enhanced in reproductive, smooth-muscle, vascular, adipose, or liver-related tissues, and VTN is liver-enriched. FBN1 and VTN are secreted to blood, so circulating protein contribution is plausible. In colon, some proteins are detected and others are not; HPA provides no matching tissue result for cerebrospinal fluid. Thus, the shared signal may reflect a broadly distributed extracellular-matrix or stromal program, transport of secreted matrix proteins, or shared sample-associated extracellular material, rather than local production by the same cell type in both tissues.

**GO/KEGG enrichment**: 16 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF extracellular matrix structural constituent | 3.28e-05 | COL12A1, COL1A1, COL1A2, COL6A1, COL6A3, FBN1, HSPG2, LAMA4, VTN |
| GO:CC external encapsulating structure | 3.87e-05 | COL12A1, COL1A1, COL1A2, COL6A1, COL6A3, FBN1, HSPG2, LAMA4, VTN |
| GO:CC extracellular matrix | 3.87e-05 | COL12A1, COL1A1, COL1A2, COL6A1, COL6A3, FBN1, HSPG2, LAMA4, VTN |
| GO:MF structural molecule activity | 7.35e-05 | COL12A1, COL1A1, COL1A2, COL6A1, COL6A3, FBN1, HSPG2, LAMA4, VTN |
| KEGG ECM-receptor interaction - Homo sapiens (human) | 0.000123 | COL1A1, COL1A2, COL6A1, COL6A3, HSPG2, LAMA4, VTN |
| KEGG Integrin signaling - Homo sapiens (human) | 0.000642 | COL1A1, COL1A2, COL6A1, COL6A3, FBN1, LAMA4, VTN |
| KEGG Focal adhesion - Homo sapiens (human) | 0.000879 | COL1A1, COL1A2, COL6A1, COL6A3, LAMA4, VTN |
| GO:CC complex of collagen trimers | 0.00118 | COL12A1, COL1A1, COL1A2, COL6A1, COL6A3 |
| KEGG Human papillomavirus infection - Homo sapiens (human) | 0.00122 | COL1A1, COL1A2, COL6A1, COL6A3, LAMA4, VTN |
| KEGG Cytoskeleton in muscle cells - Homo sapiens (human) | 0.00168 | COL1A1, COL1A2, COL6A1, COL6A3, FBN1, HSPG2 |
| GO:MF extracellular matrix structural constituent conferring tensile strength | 0.00204 | COL12A1, COL1A1, COL1A2, COL6A1, COL6A3 |
| KEGG PI3K-Akt signaling pathway - Homo sapiens (human) | 0.00389 | COL1A1, COL1A2, COL6A1, COL6A3, LAMA4, VTN |
| KEGG Protein digestion and absorption - Homo sapiens (human) | 0.00739 | COL12A1, COL1A1, COL1A2, COL6A1, COL6A3 |
| GO:CC supramolecular complex | 0.00981 | COL12A1, COL1A1, COL1A2, COL6A1, COL6A3, FBN1 |
| GO:CC collagen trimer | 0.0142 | COL12A1, COL1A1, COL1A2, COL6A1, COL6A3 |

### STRING and hu.MAP

STRING provides strong prior support for the module: collagen genes form a densely connected core, particularly the COL1A1–COL1A2 pair and connections involving COL6A1 and COL6A3. FBN1 connects with the collagen network, while HSPG2 and VTN provide additional extracellular-matrix links. These relationships are consistent with known collagen assembly, fibril-associated matrix organization, basement-membrane structure, and cell adhesion (6 supplementary STRING terms; within-query FDR 6.08e-07–2.43e-05). The STRING evidence therefore supports biological coherence but is not independent proof of a newly discovered interaction. hu.MAP contains recurrent complexes involving COL1A1 and COL1A2 (hu.MAP huMAP3_02141.1) (hu.MAP huMAP3_06460.1) (hu.MAP huMAP3_07562.1) (hu.MAP huMAP3_02069.1) (hu.MAP huMAP3_10780.1) (hu.MAP huMAP3_09231.1) (hu.MAP huMAP3_09523.1) (hu.MAP huMAP3_09606.1) (hu.MAP huMAP3_10652.1) (hu.MAP huMAP3_14070.1), and a separate complex involving COL6A3 and COL12A1 (hu.MAP huMAP3_13038.1). The hu.MAP complexes include additional collagen and matrix-associated proteins, indicating that the module overlaps known matrix protein groupings, although many module members are not represented in a hu.MAP complex.

**STRING interactions (score >= 0.7)**: 18 of 36 gene pairs: COL12A1–COL1A1 (0.836); COL12A1–COL1A2 (0.793); COL12A1–COL6A1 (0.781); COL12A1–COL6A3 (0.788); COL1A1–COL1A2 (0.999); COL1A1–COL6A1 (0.969); COL1A1–COL6A3 (0.974); COL1A1–FBN1 (0.929); COL1A2–COL6A1 (0.875); COL1A2–COL6A3 (0.968); COL1A2–FBN1 (0.965); COL6A1–COL6A3 (0.994); COL6A1–FBN1 (0.743); COL6A1–LAMA4 (0.743); COL6A3–FBN1 (0.786); FBN1–HSPG2 (0.849); FBN1–VTN (0.806); HSPG2–VTN (0.797)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Extracellular matrix structural constituent (FDR = 6.08e-07, 9 genes); NetworkNeighborAL Extracellular matrix organization (FDR = 1.85e-06, 9 genes); COMPARTMENTS Collagen-containing extracellular matrix (FDR = 4.24e-06, 9 genes); NetworkNeighborAL Collagen formation, and Protein complex involved in cell adhesion (FDR = 4.33e-06, 8 genes); COMPARTMENTS External encapsulating structure (FDR = 7.25e-06, 9 genes); KEGG ECM-receptor interaction (FDR = 2.43e-05, 7 genes); PMID (2023) Ten Years of Extracellular Matrix Proteomics: Accomplishments, Challenges, and Future Perspectives. (FDR = 4.17e-05, 8 genes); RCTM Extracellular matrix organization (FDR = 6.67e-05, 9 genes); Keyword Extracellular matrix (FDR = 8.79e-05, 8 genes); KEGG Focal adhesion (FDR = 0.00012, 6 genes); KEGG Human papillomavirus infection (FDR = 0.00012, 6 genes); PMID (2022) Mice Placental ECM Components May Provide A Three-Dimensional Placental Microenvironment. (FDR = 0.00015, 8 genes); PMID (2015) Nascent osteoblast matrix inhibits osteogenesis of human mesenchymal stem cells in vitro. (FDR = 0.00015, 7 genes); PMID (2013) Correlated mRNAs and miRNAs from co-expression and regulatory networks affect porcine muscle and finally meat properties. (FDR = 0.00015, 7 genes); RCTM Degradation of the extracellular matrix (FDR = 0.00016, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02141.1 (COL1A1, COL1A2; 2/3); huMAP3_06460.1 (COL1A1, COL1A2; 2/3); huMAP3_07562.1 (COL1A1, COL1A2; 2/3); huMAP3_02069.1 (COL1A1, COL1A2; 2/4); huMAP3_10780.1 (COL1A1, COL1A2; 2/5); huMAP3_09231.1 (COL1A1, COL1A2; 2/6); huMAP3_09523.1 (COL1A1, COL1A2; 2/6); huMAP3_09606.1 (COL1A1, COL1A2; 2/6); huMAP3_10652.1 (COL1A1, COL1A2; 2/6); huMAP3_14070.1 (COL1A1, COL1A2; 2/8); huMAP3_13038.1 (COL6A3, COL12A1; 2/40)

### Novelty

The molecular function of this module is not novel in isolation: its collagen, fibrillin, perlecan, laminin, and vitronectin relationships are already supported by STRING, hu.MAP, GO, KEGG, and prior gene-disease literature. The potentially novel aspect is the conserved co-abundance of this particular extracellular-matrix protein set across cerebrospinal fluid and colon. The fact sheet alone does not establish that this cross-tissue module has never been reported, and absence of a complete module match in STRING or hu.MAP would not prove novelty. A defensible conclusion is that the module represents a biologically well-established matrix program with a potentially new cross-tissue co-abundance pattern requiring comparison against published tissue-network studies and independent cohorts.

**Hypothesis.** Hypothesis: the module reflects a shared mesenchymal extracellular-matrix program in which collagen I and collagen VI provide fibrillar and pericellular scaffolding, COL12A1 organizes interactions around collagen I, FBN1 contributes force-bearing microfibrils, and HSPG2, LAMA4, and VTN connect the matrix to basement-membrane and integrin-mediated adhesion signaling. In colon, this could represent fibroblast or stromal matrix production. In cerebrospinal fluid, the signal could arise from secreted or transported matrix proteins, vascular or meningeal-associated material, or a related stromal extracellular-matrix source. This hypothesis predicts coordinated changes in matrix abundance and adhesion signaling, but the co-abundance data do not by themselves establish physical assembly, tissue of origin, or direction of signaling.

### Important genes

#### COL1A1

- **Related proteins** (co-abundance neighbors): COL1A2 (0.85), COL6A1 (0.80); STRING partners: COL12A1 (0.836), COL1A2 (0.999), COL6A1 (0.969), COL6A3 (0.974), FBN1 (0.929)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_02141.1, huMAP3_06460.1, huMAP3_07562.1, huMAP3_02069.1, huMAP3_10780.1, huMAP3_09231.1, huMAP3_09523.1, huMAP3_09606.1, huMAP3_10652.1, huMAP3_14070.1
- **Function (MyGene.info)**: collagen type I alpha 1 chain. This gene encodes the pro-alpha1 chains of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIA, Ehlers-Danlos syndrome Classical type,…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 2 (0.847); osteogenesis imperfecta type 4 (0.837); osteogenesis imperfecta type 3 (0.835); osteogenesis imperfecta type 1 (0.834); osteogenesis imperfecta (0.808)
- **Europe PMC papers**: 45548
- **Why important**: COL1A1 is a central structural member of the collagen network, connects strongly with COL1A2 and COL6A1 in STRING, and participates in the recurrent hu.MAP complexes containing COL1A1 and COL1A2 (hu.MAP huMAP3_02141.1) (hu.MAP huMAP3_06460.1) (hu.MAP huMAP3_07562.1) (hu.MAP huMAP3_02069.1) (hu.MAP huMAP3_10780.1) (hu.MAP huMAP3_09231.1) (hu.MAP huMAP3_09523.1) (hu.MAP huMAP3_09606.1) (hu.MAP huMAP3_10652.1) (hu.MAP huMAP3_14070.1). It is present across the primary matrix, collagen, ECM-receptor, integrin, focal-adhesion, and basement-membrane evidence (16 globally significant GO/KEGG terms, q_global 3.28e-05–0.0493; see the table). Its established function is to encode a principal alpha chain of type I collagen, and its disease associations include osteogenesis imperfecta and Ehlers-Danlos syndromes. The extensive literature makes it an anchor gene for interpreting the module.
- **Conclusion**: Established evidence supports COL1A1 as a core type I collagen scaffold component and a major contributor to the module's matrix interpretation. Its central network position supports structural importance, but the data do not show that COL1A1 initiates the shared cerebrospinal-fluid and colon co-abundance pattern.

#### COL1A2

- **Related proteins** (co-abundance neighbors): COL1A1 (0.85), COL6A1 (0.84); STRING partners: COL12A1 (0.793), COL1A1 (0.999), COL6A1 (0.875), COL6A3 (0.968), FBN1 (0.965)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_02141.1, huMAP3_06460.1, huMAP3_07562.1, huMAP3_02069.1, huMAP3_10780.1, huMAP3_09231.1, huMAP3_09523.1, huMAP3_09606.1, huMAP3_10652.1, huMAP3_14070.1
- **Function (MyGene.info)**: collagen type I alpha 2 chain. This gene encodes the pro-alpha2 chain of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIB, recessive Ehlers-Danlos syndrome Classi…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 2 (0.845); osteogenesis imperfecta type 3 (0.830); osteogenesis imperfecta type 4 (0.820); Ehlers-Danlos syndrome, cardiac valvular type (0.777); osteogenesis imperfecta type 1 (0.770)
- **Europe PMC papers**: 67901
- **Why important**: COL1A2 is the partner chain of the type I collagen heterotrimer and has one of the strongest STRING relationships with COL1A1. It is also the most recurrent module member in hu.MAP complexes (hu.MAP huMAP3_02141.1) (hu.MAP huMAP3_06460.1) (hu.MAP huMAP3_07562.1) (hu.MAP huMAP3_02069.1) (hu.MAP huMAP3_10780.1) (hu.MAP huMAP3_09231.1) (hu.MAP huMAP3_09523.1) (hu.MAP huMAP3_09606.1) (hu.MAP huMAP3_10652.1) (hu.MAP huMAP3_14070.1) and appears in the globally corrected collagen, ECM, adhesion, and signaling terms (16 globally significant GO/KEGG terms, q_global 3.28e-05–0.0493; see the table). Its established disease associations include osteogenesis imperfecta, Ehlers-Danlos syndromes, osteoporosis, and atypical Marfan syndrome. Its network and complex context make it essential for distinguishing a genuine collagen-assembly program from a generic secreted-protein signal.
- **Conclusion**: Established evidence identifies COL1A2 as a type I collagen assembly partner and a strong marker of the module's fibrillar matrix core. A hypothesis that altered COL1A2 abundance changes matrix mechanics or adhesion signaling is biologically plausible, but is not demonstrated by this co-abundance module alone.

#### COL6A1

- **Related proteins** (co-abundance neighbors): COL1A2 (0.84), COL12A1 (0.83), COL6A3 (0.81), COL1A1 (0.80); STRING partners: COL12A1 (0.781), COL1A1 (0.969), COL1A2 (0.875), COL6A3 (0.994), FBN1 (0.743), LAMA4 (0.743)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is among the more connected module genes and links the type I collagen group with COL6A3 and COL12A1 in STRING. It occurs in every globally corrected GO and KEGG term listed for the module (16 globally significant GO/KEGG terms, q_global 3.28e-05–0.0493; see the table), making it a particularly broad annotation bridge. It encodes a chain of collagen VI, a major microfibrillar extracellular-matrix component, and is associated with Bethlem myopathy and Ullrich congenital muscular dystrophy. HPA places it in fibroblast and stromal-associated cell populations and reports extracellular secretion.
- **Conclusion**: Established evidence supports COL6A1 as a bridge between fibrillar collagen and collagen-VI matrix organization, helping explain the module's coherent structure and adhesion biology. Its presence in both tissue-associated and secreted-matrix contexts makes it a strong candidate for a shared extracellular-matrix signal, but not proof of a common cellular source.

#### HSPG2

- **Related proteins** (co-abundance neighbors): COL6A3 (0.91), LAMA4 (0.85), FBN1 (0.83), VTN (0.80); STRING partners: FBN1 (0.849), VTN (0.797)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 is a network bridge connecting COL6A3, LAMA4, FBN1, and VTN, and it is supported by the primary extracellular-matrix, structural, ECM-receptor, and basement-membrane annotations (7 globally significant GO/KEGG terms, q_global 3.28e-05–0.0493; see the table). It encodes perlecan, a multidomain proteoglycan that cross-links extracellular-matrix and cell-surface molecules. HPA places it in extracellular matrix and vascular-associated contexts, with fibro-adipogenic and hepatic-stellate cell associations. Its disease associations include Schwartz-Jampel syndrome and dyssegmental dysplasia, and it has substantial literature support.
- **Conclusion**: Established evidence supports HSPG2 as an interface between basement-membrane structure, matrix organization, and cell-surface signaling. Its bridging position makes it a plausible coordinator of the module, but the available data do not establish that it mediates the cross-tissue conservation.

#### FBN1

- **Related proteins** (co-abundance neighbors): COL6A3 (0.86), HSPG2 (0.83); STRING partners: COL1A1 (0.929), COL1A2 (0.965), COL6A1 (0.743), COL6A3 (0.786), HSPG2 (0.849), VTN (0.806)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibrillin 1. This gene encodes a member of the fibrillin family of proteins. The encoded preproprotein is proteolytically processed to generate two proteins including the extracellular matrix component fibrillin-1 and the protein hormone asprosin. Fibrillin-1 is an extracellular matrix glycoprotein that serves as a structural component of calcium-binding microfibrils. These microfibrils provide force-bearing s…
- **Diseases (Open Targets)**: Marfan syndrome (0.892); ectopia lentis 1, isolated, autosomal dominant (0.811); Acromicric dysplasia (0.802); geleophysic dysplasia 2 (0.802); stiff skin syndrome (0.799)
- **Europe PMC papers**: 9216
- **Why important**: FBN1 connects with COL1A1, COL1A2, COL6A1, COL6A3, HSPG2, and VTN in STRING, placing it at the interface between collagenous and non-collagenous matrix components. It contributes to the external-encapsulating-structure, integrin-related, structural, and basement-membrane evidence (8 globally significant GO/KEGG terms, q_global 3.28e-05–0.0493; see the table). Its established product, fibrillin one, forms force-bearing calcium-binding microfibrils; its processed product also includes asprosin. FBN1 is associated with Marfan syndrome and related connective-tissue disorders and has extensive literature support.
- **Conclusion**: Established evidence supports FBN1 as a mechanically relevant microfibrillar organizer that can connect the collagen scaffold to broader matrix architecture. Its network position supports a role in matrix integration, while any effect on signaling or tissue-specific co-abundance remains a hypothesis.

## Module 8

**Tissue pair**: cerebrospinal_fluid and colon  
**Genes (5)**: FBLN1, FTH1, FUCA1, THSD7A, GC

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING enrichment. The strongest interpretation therefore comes from the annotated proteins and the co-abundance topology rather than formal pathway enrichment. THSD7A is the central network gene and is linked to cytoskeletal organization, endothelial migration, and tube formation. FBLN1 supports extracellular-matrix organization, cell adhesion, and integrin-mediated signaling. GC transports vitamin D and participates in vitamin transport and vitamin D metabolism. FTH1 stores iron and contributes to intracellular iron homeostasis, while FUCA1 supports lysosomal degradation of fucose-containing glycoconjugates. Taken together, the module is most consistent with a secreted or extracellular-matrix-associated tissue-interface program connected to epithelial or endothelial biology, nutrient and vitamin handling, lysosomal carbohydrate turnover, and iron homeostasis. This is a functional interpretation rather than evidence of a single significantly enriched pathway.

**Cell composition.** The module is dominated by secreted or extracellular proteins: THSD7A, GC, and FBLN1 are secreted to blood or extracellular matrix, while FUCA1 is intracellular and membrane-associated and FTH1 is vesicular. The HPA evidence shows that most genes have cell-type-enhanced expression, with recurring associations to colonocytes, enterocytes, choroid plexus epithelial cells, hepatocytes, and placental cell types. GC is liver-enriched, FBLN1 is choroid-plexus-enhanced, and THSD7A is kidney-enhanced. The blood-cell evidence is mixed rather than uniformly immune-cell-specific, with associations involving basophils and non-classical monocytes alongside genes with low, absent, or broader immune-cell specificity. The shared cerebrospinal-fluid and colon signal could therefore reflect circulating or extracellular proteins, epithelial or barrier-associated cell types, and sample composition, rather than a process unique to either tissue. All module proteins were detected by immunohistochemistry in colon, whereas there was no matching HPA protein-detection evidence for cerebrospinal fluid.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module members, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. The co-abundance relationships are therefore not corroborated by the queried physical-interaction or complex resources. The network is organized around THSD7A, which is co-abundant with every other member, while the remaining genes are peripheral and are not mutually connected in the module. This pattern may represent coordinated abundance across samples, shared secretion or tissue composition, or an indirect biological relationship rather than a known protein complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a new co-abundance observation, because its specific cross-tissue organization is not represented by the available STRING interaction or hu.MAP complex evidence. However, it cannot be claimed as a newly discovered molecular mechanism. The component proteins and several of their functions are already well established, and the absence of database interactions or complexes does not prove novelty. The most defensible claim is that the coordinated abundance pattern is potentially novel and requires validation in independent cohorts, with controls for blood contamination, epithelial composition, and extracellular-protein abundance.

**Hypothesis.** Hypothesis: this module reflects a shared epithelial or barrier-interface environment in colon and cerebrospinal-fluid-associated sampling, in which extracellular-matrix and adhesion biology represented by THSD7A and FBLN1 is coordinated with circulating vitamin-D transport represented by GC, lysosomal glycan processing represented by FUCA1, and iron storage represented by FTH1. THSD7A may act as the network-centered marker of this state, while the other proteins may report distinct biochemical features of the same tissue, vascular, or sample-composition context. This hypothesis predicts that the module will track epithelial or barrier-cell abundance and extracellular-protein content more strongly than a discrete intracellular complex.

### Important genes

#### THSD7A

- **Related proteins** (co-abundance neighbors): GC (0.93), FTH1 (0.90), FUCA1 (0.89), FBLN1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thrombospondin type 1 domain containing 7A. The protein encoded by this gene is found almost exclusively in endothelial cells from placenta and umbilical cord. The encoded protein appears to interact with alpha(V)beta(3) integrin and paxillin to inhibit endothelial cell migration and tube formation. This protein may be involved in cytoskeletal organization. Variations in this gene may be associated with low bone mineral density in osteoporo…
- **Diseases (Open Targets)**: glaucoma (0.538); open-angle glaucoma (0.532); bipolar disorder (0.485); mathematical ability (0.438); Fuchs' endothelial dystrophy (0.434)
- **Europe PMC papers**: 822
- **Why important**: THSD7A is the network-centered gene and is connected to every other module member. Its annotation links it to endothelial-cell biology, cytoskeletal organization, integrin and paxillin interactions, endothelial migration, and tube formation. HPA identifies kidney enhancement, basophil enrichment, and secretion to blood, while the protein is detected in colon. Its disease associations include glaucoma, open-angle glaucoma, bipolar disorder, mathematical ability, and Fuchs' endothelial dystrophy. It has a moderate literature base relative to the other central candidates.
- **Conclusion**: Established evidence supports THSD7A as the structural and network-organizing marker of the module, with plausible relevance to endothelial or barrier biology. The module does not establish that THSD7A drives the co-abundance pattern or mediates a cerebrospinal-fluid–colon connection.

#### GC

- **Related proteins** (co-abundance neighbors): THSD7A (0.93); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GC vitamin D binding protein. The protein encoded by this gene belongs to the albumin gene family. It is a multifunctional protein found in plasma, ascitic fluid, cerebrospinal fluid and on the surface of many cell types. It binds to vitamin D and its plasma metabolites and transports them to target tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq,…
- **Diseases (Open Targets)**: vitamin D deficiency (0.574); vitamin deficiency (0.552); chronic obstructive pulmonary disease (0.499); squamous cell carcinoma (0.339); central nervous system cancer (0.334)
- **Europe PMC papers**: 363974
- **Why important**: GC is the liver-enriched, blood-secreted vitamin-D-binding protein and is the only direct carrier-like component in the module. Its established functions include vitamin-D binding, vitamin transport, response to nutrient levels, and vitamin-D metabolism. It is detected in colon and has a very large literature base. Its disease associations include vitamin-D deficiency, vitamin deficiency, chronic obstructive pulmonary disease, squamous cell carcinoma, and central nervous system cancer.
- **Conclusion**: Established evidence supports GC as a circulating nutrient-transport marker that could contribute substantially to a shared extracellular or plasma-related signal. Its presence does not demonstrate local vitamin-D metabolism in either tissue or a causal role in the module.

#### FTH1

- **Related proteins** (co-abundance neighbors): THSD7A (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ferritin heavy chain 1. This gene encodes the heavy subunit of ferritin, the major intracellular iron storage protein in prokaryotes and eukaryotes. It is composed of 24 subunits of the heavy and light ferritin chains. Variation in ferritin subunit composition may affect the rates of iron uptake and release in different tissues. A major function of ferritin is the storage of iron in a soluble and nontoxic state. Defects …
- **Diseases (Open Targets)**: hemochromatosis type 5 (0.582); neurodegeneration with brain iron accumulation 9 (0.548); inherited retinal dystrophy (0.531); autosomal recessive bestrophinopathy (0.528); vitelliform macular dystrophy 2 (0.517)
- **Europe PMC papers**: 8350
- **Why important**: FTH1 is a broadly relevant intracellular iron-storage protein with roles in iron ion transport, intracellular iron homeostasis, autophagy, immune response, cell-population regulation, and erythrocyte differentiation. It is enhanced in colonocytes and enterocytes, is detected in colon, and has extensive literature and disease associations involving iron-related neurodegeneration and inherited retinal disorders. Its peripheral position in the module makes it a useful biochemical readout even though it is not a network hub.
- **Conclusion**: Established evidence supports FTH1 as an iron-homeostasis and cellular-state marker. In this module it may report epithelial abundance, vesicular material, stress, or sample composition; the available evidence does not show that iron biology is the central function of the entire module.

#### FUCA1

- **Related proteins** (co-abundance neighbors): THSD7A (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alpha-L-fucosidase 1. The protein encoded by this gene is a lysosomal enzyme involved in the degradation of fucose-containing glycoproteins and glycolipids. Mutations in this gene are associated with fucosidosis (FUCA1D), which is an autosomal recessive lysosomal storage disease. A pseudogene of this locus is present on chr 2.[provided by RefSeq, Oct 2009].
- **Diseases (Open Targets)**: fucosidosis (0.834); hereditary disease (0.415); Intellectual disability (0.371); Seizure (0.370); Abnormality of the nervous system (0.340)
- **Europe PMC papers**: 1004
- **Why important**: FUCA1 is a lysosomal alpha-L-fucosidase involved in degradation of fucose-containing glycoproteins and glycolipids, with annotations in carbohydrate metabolism, fucose metabolism, and glycoside and glycolipid catabolism. It is enhanced in colonocytes and enterocytes, is detected in colon, and is associated with fucosidosis and related neurological manifestations. Its literature base is substantial, and its position connected to THSD7A makes it a peripheral biochemical component of the module.
- **Conclusion**: Established evidence supports FUCA1 as a lysosomal glycan-processing marker, particularly relevant to intestinal epithelial biology. The module does not establish coordinated fucose metabolism across the two tissues or imply that FUCA1 is mechanistically linked to THSD7A.

#### FBLN1

- **Related proteins** (co-abundance neighbors): THSD7A (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibulin 1. Fibulin 1 is a secreted glycoprotein that becomes incorporated into a fibrillar extracellular matrix. Calcium-binding is apparently required to mediate its binding to laminin and nidogen. It mediates platelet adhesion via binding fibrinogen. Four splice variants which differ in the 3' end have been identified. Each variant encodes a different isoform, but no functional distinctions have been ident…
- **Diseases (Open Targets)**: synpolydactyly type 2 (0.447); FBLN1-related developmental delay-central nervous system anomaly-syndactyly syndrome (0.377); synpolydactyly (0.371); adolescent idiopathic scoliosis (0.306); alcohol drinking (0.219)
- **Europe PMC papers**: 2655
- **Why important**: FBLN1 is a secreted extracellular-matrix glycoprotein involved in matrix organization, cell adhesion, integrin-mediated signaling, and platelet adhesion. It is enhanced in choroid plexus, associated with choroid plexus epithelial cells and non-classical monocytes, secreted to extracellular matrix, and detected in colon. Its disease associations include synpolydactyly, developmental delay with central nervous system anomalies, and adolescent idiopathic scoliosis. Its literature base is substantial.
- **Conclusion**: Established evidence supports FBLN1 as the strongest extracellular-matrix and choroid-plexus-related marker in the module. It provides a plausible tissue-interface link between cerebrospinal-fluid-associated biology and colon, but the co-abundance data do not establish a direct inter-tissue mechanism or a specific FBLN1-dependent process.
