# Conserved co-abundance modules: myometrium and testis

## Module 0

**Tissue pair**: myometrium and testis  
**Genes (8)**: PPP2R2A, PGD, ATXN10, DDX39B, TUFM, IDH1, MESD, ADSS2

### Function

The module does not support a single statistically established GO or KEGG function: no GO or KEGG term passed global correction, and there was no STRING functional enrichment. Its genes nevertheless suggest a broadly expressed cellular maintenance program spanning RNA processing and export through DDX39B, mitochondrial translation through TUFM, cytosolic redox and carbon metabolism through IDH1 and PGD, purine biosynthesis through ADSS2, protein folding through MESD, and phosphatase regulation through PPP2R2A. The sparse network therefore appears more consistent with coordinated abundance of general metabolic, biosynthetic, and proteostasis functions than with a specialized myometrium or testis pathway. These functional links are biological interpretations of the member annotations, not globally significant enrichment results.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: the HPA summary identifies only a single secreted gene, while the other genes are intracellular or membrane-associated. It is also not broadly blood-cell enriched as a module. Most genes have low immune-cell specificity, although PGD shows group enrichment in bone marrow and several blood-cell populations, and multiple genes show cell-type enhancement in neutrophil-related or esophageal populations. The module is broadly detectable at the protein level in both tissues, with stronger completeness in testis than myometrium. Its sharing between myometrium and testis may therefore reflect common cellular metabolism or shared cell-state composition rather than a tissue-specific reproductive function. HPA also shows cell-type enhancement in late spermatids for TUFM and ADSS2, but this is not sufficient to assign the whole module to germ cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship among module members is the direct IDH1–PGD association. This supports a plausible connection between NADP-linked isocitrate metabolism and the oxidative pentose-phosphate pathway, but it does not establish a complete pathway for the module. hu.MAP provides two overlapping complexes, C1 and C2, both containing IDH1 and PGD; their additional members are ARHGDIA and, for C2, USP14. Thus, the strongest external network support concerns the IDH1–PGD pair and its placement in complexes that are incomplete within this module. DDX39B, TUFM, ADSS2, ATXN10, MESD, and PPP2R2A have no listed STRING partners or hu.MAP complexes within the supplied evidence. The co-abundance network consequently contains a small supported metabolic core embedded in otherwise weakly supported correlations.

**STRING interactions (score >= 0.7)**: 1 of 28 gene pairs: IDH1–PGD (0.877)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01475.1 (IDH1, PGD; 2/3); huMAP3_09400.1 (IDH1, PGD; 2/4)

### Novelty

This is a new shared co-abundance observation in the supplied analysis, but it should not be called a newly discovered molecular complex or pathway. The IDH1–PGD relationship is already represented by STRING and by hu.MAP complexes C1 and C2, so part of the module recapitulates known biology. The remaining co-abundance links lack listed STRING or hu.MAP support, which may indicate tissue-contextual coordination, indirect regulation, shared cell composition, or technical correlation. Absence from those resources alone cannot establish novelty. A defensible novelty claim is therefore that the particular cross-tissue co-abundance configuration may be under-described, while its principal metabolic relationship is not novel.

**Hypothesis.** Hypothesis: the module reflects a shared cellular resource-management state in myometrium and testis. Coordinated mitochondrial translation through TUFM, RNA processing and export through DDX39B, NADPH-generating metabolism through IDH1 and PGD, and purine production through ADSS2 could support protein synthesis, redox control, and biosynthetic demand in cells present in both tissues. MESD, PPP2R2A, and ATXN10 may represent associated folding, signaling, or cell-structural components rather than members of one biochemical pathway. This hypothesis predicts that the module will track metabolic and proteostatic activity or shared cell composition more strongly than a tissue-specific reproductive program. It requires validation with cell-resolved expression, perturbation, and protein-interaction experiments.

### Important genes

#### DDX39B

- **Related proteins** (co-abundance neighbors): PGD (0.86), ATXN10 (0.85), IDH1 (0.84), ADSS2 (0.83), TUFM (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nuclear speckles; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 39B. This gene encodes a member of the DEAD box family of RNA-dependent ATPases that mediate ATP hydrolysis during pre-mRNA splicing. The encoded protein is an essential splicing factor required for association of U2 small nuclear ribonucleoprotein with pre-mRNA, and it also plays an important role in mRNA export from the nucleus to the cytoplasm. This gene belongs to a cluster of genes localized in th…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); Alzheimer disease (0.522); Parkinson disease (0.503); lysosomal storage disease (0.503); neurodevelopmental disorder (0.413)
- **Europe PMC papers**: 1037
- **Why important**: DDX39B has the strongest hub-like position in the module, linking PGD, ATXN10, IDH1, ADSS2, and TUFM. Its established functions in spliceosomal assembly, pre-mRNA splicing, and nuclear mRNA export make it a plausible coordinator of the RNA-processing side of the module. It is detected in both tissues, has low tissue and immune specificity, and has extensive literature coverage. The supplied disease associations include neurodegenerative and neurodevelopmental disease categories.
- **Conclusion**: Established evidence supports DDX39B as a broadly expressed RNA-processing and mRNA-export factor with a central co-abundance position. It is a strong candidate for a module-level coordinator, but the data do not establish that it mechanistically regulates the other module genes.

#### TUFM

- **Related proteins** (co-abundance neighbors): ATXN10 (0.85), ADSS2 (0.82), IDH1 (0.81), DDX39B (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Tu translation elongation factor, mitochondrial. This gene encodes a protein which participates in protein translation in mitochondria. Mutations in this gene have been associated with combined oxidative phosphorylation deficiency resulting in lactic acidosis and fatal encephalopathy. A pseudogene has been identified on chromosome 17. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 4 (0.769); neurodegenerative disease (0.502); COVID-19 (0.471); combined oxidative phosphorylation deficiency (0.370); ulcerative colitis (0.303)
- **Europe PMC papers**: 1391
- **Why important**: TUFM is highly connected within the module and links DDX39B, ATXN10, ADSS2, and IDH1. Its established role in mitochondrial translation provides a direct biological connection to cellular energy and biosynthetic capacity. HPA detects it in both tissues and shows enhancement in late spermatids, while the supplied disease evidence includes combined oxidative-phosphorylation deficiency and fatal encephalopathy. Its literature coverage is substantial.
- **Conclusion**: Established evidence supports TUFM as a mitochondrial translation factor that may mark shared energetic or biosynthetic demand. Its module association is compatible with that role, but a direct mechanistic bridge from TUFM to the other module members remains hypothetical.

#### IDH1

- **Related proteins** (co-abundance neighbors): MESD (0.90), DDX39B (0.84), TUFM (0.81); STRING partners: PGD (0.877)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_01475.1, huMAP3_09400.1
- **Function (MyGene.info)**: isocitrate dehydrogenase (NADP(+)) 1. Isocitrate dehydrogenases catalyze the oxidative decarboxylation of isocitrate to 2-oxoglutarate. These enzymes belong to two distinct subclasses, one of which utilizes NAD(+) as the electron acceptor and the other NADP(+). Five isocitrate dehydrogenases have been reported: three NAD(+)-dependent isocitrate dehydrogenases, which localize to the mitochondrial matrix, and two NADP(+)-dependent isoci…
- **Diseases (Open Targets)**: acute myeloid leukemia (0.779); Ollier disease (0.672); glioblastoma (0.657); cholangiocarcinoma (0.652); glioma (0.637)
- **Europe PMC papers**: 29424
- **Why important**: IDH1 occupies a connector position between MESD and the DDX39B–TUFM side of the network and is directly linked to PGD by STRING. It catalyzes NADP-linked isocitrate metabolism and contributes to NADPH regeneration, making it a strong metabolic anchor. HPA shows tissue enhancement in liver and detection in testis, but not myometrium. It has extensive literature and supplied disease associations spanning acute myeloid leukemia, glioblastoma, glioma, cholangiocarcinoma, and Ollier disease.
- **Conclusion**: Established evidence supports IDH1 as a cytosolic metabolic enzyme and the best-supported bridge between the module and known external interaction resources. The module does not establish whether IDH1 activity drives the shared tissue pattern or merely covaries with it.

#### PGD

- **Related proteins** (co-abundance neighbors): DDX39B (0.86); STRING partners: IDH1 (0.877)
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_01475.1, huMAP3_09400.1
- **Function (MyGene.info)**: phosphogluconate dehydrogenase. 6-phosphogluconate dehydrogenase is the second dehydrogenase in the pentose phosphate shunt. Deficiency of this enzyme is generally asymptomatic, and the inheritance of this disorder is autosomal dominant. Hemolysis results from combined deficiency of 6-phosphogluconate dehydrogenase and 6-phosphogluconolactonase suggesting a synergism of the two enzymopathies. Several transcript variants encoding…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); Abnormality of the skeletal system (0.329); autoimmune disorder of central nervous system (0.246); smoking behavior (0.245); essential hypertension (0.199)
- **Europe PMC papers**: 8652
- **Why important**: PGD is the second member of the directly supported IDH1–PGD pair and is the metabolic anchor for the oxidative pentose-phosphate pathway. Its HPA profile is distinctive within the module, with enrichment in bone marrow, esophageal cell populations, and several blood-cell categories, while protein is detected in testis but not myometrium. Its literature coverage is extensive, and the supplied evidence links deficiency to hemolysis and associates it with several disease categories.
- **Conclusion**: Established evidence supports PGD as a redox and pentose-phosphate enzyme and as a plausible contributor to the known IDH1–PGD relationship. Its blood-cell and bone-marrow expression raises the possibility that part of the cross-tissue signal reflects cell composition, so PGD is both biologically important and a potential confounding marker.

#### ADSS2

- **Related proteins** (co-abundance neighbors): PPP2R2A (0.85), DDX39B (0.83), TUFM (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenylosuccinate synthase 2. This gene encodes the enzyme adenylosuccinate synthetase which catalyzes the first committed step in the conversion of inosine monophosphate to adenosine monophosphate. A pseudogene of this gene is found on chromosome 17.[provided by RefSeq, Nov 2010].
- **Diseases (Open Targets)**: atopic eczema (0.085); respiratory tract infectious disorder (0.077); dermatomycosis (0.062); hyperlipoproteinemia type V (0.056); LCAT deficiency (0.054)
- **Europe PMC papers**: 102
- **Why important**: ADSS2 connects DDX39B and TUFM with PPP2R2A, placing purine biosynthesis beside RNA processing, mitochondrial translation, and phosphatase regulation. Its established enzyme function is the committed step of AMP biosynthesis. HPA shows detection in both tissues and enhancement in late spermatids and neutrophil progenitors. Although its literature volume is more limited than that of the major metabolic genes, its biochemical role is directly relevant to nucleotide demand.
- **Conclusion**: Established evidence supports ADSS2 as a purine-biosynthetic enzyme whose co-abundance may reflect nucleotide requirements. Its connection to the rest of the module is compatible with coordinated biosynthetic activity, but the supplied data do not demonstrate a specific role in myometrium or testis.

## Module 1

**Tissue pair**: myometrium and testis  
**Genes (13)**: SERPINA1, SERPINA3, ALB, SERPINC1, HPX, IGHA1, IGHG1, IGHG2, IGKC, KNG1, LDHB, TF, GC

### Function

The strongest interpretation is a circulating plasma and humoral-defense module rather than a myometrium- or testis-specific intracellular pathway. The primary evidence is the globally corrected enrichment for blood microparticle (GO:CC blood microparticle; q_global = 5.76e-07), antibacterial humoral response (GO:BP antibacterial humoral response; q_global = 0.00339), immunoglobulin complexes (GO:CC immunoglobulin complex; q_global = 0.01), (GO:CC immunoglobulin complex, circulating; q_global = 0.01), (GO:CC IgG immunoglobulin complex; q_global = 0.01), antimicrobial humoral response (GO:BP antimicrobial humoral response; q_global = 0.0133), humoral immune response (GO:BP humoral immune response; q_global = 0.0196), immunoglobulin receptor binding (GO:MF immunoglobulin receptor binding; q_global = 0.0205), circulating-immunoglobulin-mediated humoral response (GO:BP humoral immune response mediated by circulating immunoglobulin; q_global = 0.0334), and B-cell receptor signaling (GO:BP B cell receptor signaling pathway; q_global = 0.0351). Together, these terms indicate coordinated abundance of plasma proteins, immunoglobulin components, protease regulators, and iron- or heme-binding proteins. The immunoglobulin terms are driven by IGHA1, IGHG1, and IGHG2, while the broader humoral terms also include HPX and TF. The module should therefore be interpreted as a blood-associated extracellular defense, transport, and protease-regulatory signal. The enrichment does not establish that these proteins form a tissue-intrinsic signaling pathway.

**Cell composition.** The module is dominated by secreted-to-blood or immunoglobulin proteins. HPA identifies liver or hepatocyte enrichment for ALB, GC, HPX, KNG1, SERPINA1, SERPINA3, SERPINC1, and related evidence for TF; plasma-cell and lymphoid enrichment characterizes IGHA1, IGHG1, IGHG2, and IGKC. Several genes are associated with memory or naive B cells, while most of the module is not detected in immune cells and is instead liver or hepatocyte associated. ALB, HPX, SERPINA1, SERPINA3, SERPINC1, TF, GC, and KNG1 are secreted to blood, and the immunoglobulin genes are immunoglobulin-secreted products. Detection in myometrium and testis is limited and uneven, whereas many of these proteins are absent by tissue immunohistochemistry in the two tissues. This composition strongly raises the possibility that the conserved signal reflects plasma, blood microparticles, vascular or interstitial blood, or shared contaminating blood-derived material rather than a shared resident-cell program. It may also reflect shared plasma-cell or other immune-cell contributions. The presence of LDHB, a cytosolic metabolic enzyme detected in both tissues, provides only a limited non-secreted component and does not overturn the dominant plasma interpretation.

**GO/KEGG enrichment**: 10 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 5.76e-07 | ALB, GC, HPX, IGHA1, IGHG1, IGHG2, KNG1, SERPINA3, SERPINC1, TF |
| GO:BP antibacterial humoral response | 0.00339 | IGHA1, IGHG1, IGHG2, TF |
| GO:CC immunoglobulin complex | 0.01 | IGHA1, IGHG1, IGHG2 |
| GO:CC immunoglobulin complex, circulating | 0.01 | IGHA1, IGHG1, IGHG2 |
| GO:CC IgG immunoglobulin complex | 0.01 | IGHA1, IGHG1, IGHG2 |
| GO:BP antimicrobial humoral response | 0.0133 | IGHA1, IGHG1, IGHG2, TF |
| GO:BP humoral immune response | 0.0196 | HPX, IGHA1, IGHG1, IGHG2, TF |
| GO:MF immunoglobulin receptor binding | 0.0205 | IGHA1, IGHG1, IGHG2 |
| GO:BP humoral immune response mediated by circulating immunoglobulin | 0.0334 | HPX, IGHA1, IGHG1, IGHG2 |
| GO:BP B cell receptor signaling pathway | 0.0351 | IGHA1, IGHG1, IGHG2 |

### STRING and hu.MAP

STRING supports a well-known extracellular plasma-protein association structure. ALB is connected to GC, HPX, KNG1, SERPINA1, SERPINA3, SERPINC1, and TF; SERPINA1, HPX, SERPINC1, KNG1, and TF also interconnect. The STRING literature enrichments repeatedly recover plasma-proteome, inflammation, coagulation, infection, and blood-microparticle contexts (STRING PMID (2018) A proteomic approach of biomarker candidate discovery for alcoholic liver cirrhosis.; within-query FDR = 1.38e-06) through (STRING COMPARTMENTS Blood microparticle; within-query FDR = 7.05e-06), but these are supplementary within-query findings and are not global enrichment evidence. hu.MAP independently places the main plasma-protein group into multiple complexes, especially the complexes represented by (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_08224.1). These complexes include many additional coagulation, complement, acute-phase, transport, and apolipoprotein components outside the module. This convergence means that the non-immunoglobulin portion is consistent with established plasma-protein assemblies and shared biochemical context, not necessarily direct physical interaction among every module member. The immunoglobulin genes have no reported STRING partners or hu.MAP complexes in the supplied evidence, so their co-abundance is better interpreted as a coordinated immune or plasma-cell signal than as a demonstrated physical complex.

**STRING interactions (score >= 0.7)**: 17 of 78 gene pairs: ALB–GC (0.98); ALB–HPX (0.981); ALB–KNG1 (0.962); ALB–SERPINA1 (0.998); ALB–SERPINA3 (0.914); ALB–SERPINC1 (0.933); ALB–TF (0.9); GC–HPX (0.827); GC–SERPINA1 (0.876); GC–SERPINC1 (0.84); GC–TF (0.811); HPX–SERPINA1 (0.897); HPX–SERPINC1 (0.762); HPX–TF (0.852); KNG1–SERPINA1 (0.943); KNG1–SERPINC1 (0.758); SERPINA1–TF (0.848)
**STRING functional enrichment (supplementary, within-query FDR)**: PMID (2018) A proteomic approach of biomarker candidate discovery for alcoholic liver cirrhosis. (FDR = 1.38e-06, 7 genes); PMID (2012) Proteomic investigation of falciparum and vivax malaria for identification of surrogate protein markers. (FDR = 1.77e-06, 7 genes); PMID (2019) Label-Free Proteomics Revealed Oxidative Stress and Inflammation as Factors That Enhance Chemoresistance in Luminal Breast Cancer. (FDR = 2.07e-06, 7 genes); PMID (2023) Analysis of Plasma Proteins Involved in Inflammation, Immune ResponseComplement System, and Blood Coagulation upon Admission of COVID-19 Patients to Hospital May Help to Predict the Prognosis of the Disease. (FDR = 3.33e-06, 7 genes); PMID (2020) Significant correlation between plasma proteome profile and pain intensity, sensitivity, and psychological distress in women with fibromyalgia. (FDR = 3.38e-06, 7 genes); PMID (2019) Chronic kidney disease: a review of proteomic and metabolomic approaches to membranous glomerulonephritis, focal segmental glomerulosclerosis, and IgA nephropathy biomarkers. (FDR = 4.43e-06, 7 genes); PMID (2023) Proteomic and functional analysis of HDL subclasses in humans and rats: a proof-of-concept study. (FDR = 6.17e-06, 7 genes); PMID (2019) Serum Proteomic Analysis Reveals Vitamin D-Binding Protein (VDBP) as a Potential Biomarker for Low Bone Mineral Density in Mexican Postmenopausal Women. (FDR = 6.17e-06, 6 genes); PMID (2017) Subventricular zone involvement in Glioblastoma - A proteomic evaluation and clinicoradiological correlation. (FDR = 6.17e-06, 6 genes); PMID (2016) Biomarkers of systemic inflammation in farmers with musculoskeletal disorders; a plasma proteomic study. (FDR = 6.17e-06, 6 genes); PMID (2015) Plasma proteomic analysis of active and torpid greater mouse-eared bats (Myotis myotis). (FDR = 6.17e-06, 6 genes); PMID (1983) A study on proteins contained in urine of gestosis patients. (FDR = 6.17e-06, 6 genes); PMID (2019) Changes to the Human Serum Proteome in Response to High Intensity Interval Exercise: A Sequential Top-Down Proteomic Analysis. (FDR = 6.91e-06, 6 genes); Component Blood microparticle (FDR = 6.94e-06, 7 genes); COMPARTMENTS Blood microparticle (FDR = 7.05e-06, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINC1, SERPINA1, SERPINA3, KNG1, ALB, GC, TF, HPX; 8/64); huMAP3_10678.1 (SERPINA1, SERPINA3, KNG1, ALB, GC, TF, HPX; 7/71); huMAP3_07265.1 (SERPINA1, SERPINA3, KNG1, ALB, TF, HPX; 6/20); huMAP3_08395.1 (SERPINA1, SERPINA3, KNG1, ALB, TF, HPX; 6/43); huMAP3_09531.1 (SERPINA1, SERPINA3, KNG1, ALB, TF, HPX; 6/47); huMAP3_10101.1 (SERPINA1, SERPINA3, KNG1, ALB, TF, HPX; 6/49); huMAP3_07432.1 (SERPINA1, SERPINA3, ALB, TF, HPX; 5/18); huMAP3_09434.1 (SERPINA1, SERPINA3, ALB, GC, TF; 5/33); huMAP3_08700.1 (SERPINA1, ALB, HPX; 3/11); huMAP3_08224.1 (SERPINA3, GC, TF; 3/21); huMAP3_02236.1 (KNG1, HPX; 2/7); huMAP3_02242.1 (SERPINA3, TF; 2/9); huMAP3_09273.1 (KNG1, HPX; 2/28)

### Novelty

The module is unlikely to represent a newly discovered molecular complex or a previously unknown plasma pathway. Its principal relationships are already represented by STRING and by several hu.MAP plasma-protein complexes, and its annotations are consistent with extensively studied liver-derived plasma proteins and immunoglobulins. A potentially novel aspect is the observation that this blood-associated abundance pattern is conserved across myometrium and testis in the particular co-abundance dataset. However, conservation in this dataset alone does not prove a new tissue mechanism, and the strong HPA evidence for liver, hepatocytes, plasma cells, blood, and secreted proteins offers a more parsimonious explanation involving shared blood-derived material or cell composition. The absence of some immunoglobulin relationships from STRING or hu.MAP is not evidence of novelty. Independent replication with tissue-quality controls, cell-type deconvolution, plasma-marker adjustment, and orthogonal protein or RNA measurements would be required before claiming a new biological finding.

**Hypothesis.** Hypothesis: the conserved module is generated primarily by variable representation of circulating plasma and blood-derived material in both tissue groups. Liver-derived transport and protease-regulatory proteins may enter the measured tissue material through blood or interstitial fluid, while immunoglobulin transcripts or proteins may reflect plasma cells, immune cells, or immunoglobulin-containing microparticles. A secondary possibility is that local vascular or tissue injury produces coordinated extracellular responses involving heme handling, iron transport, coagulation regulation, and humoral defense. This hypothesis predicts that the module will track plasma-volume or vascular signatures and blood-cell or plasma-cell markers more strongly than resident myometrial or testicular cell programs. It remains a hypothesis because the supplied co-abundance, enrichment, STRING, hu.MAP, and HPA evidence cannot establish the physical source of the proteins in the samples.

### Important genes

#### ALB

- **Related proteins** (co-abundance neighbors): TF (0.80); STRING partners: GC (0.98), HPX (0.981), KNG1 (0.962), SERPINA1 (0.998), SERPINA3 (0.914), SERPINC1 (0.933), TF (0.9)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_07265.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_08700.1
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB is a prominent network anchor for the plasma-protein portion of the module and connects to GC, HPX, KNG1, SERPINA1, SERPINA3, SERPINC1, and TF in STRING. HPA assigns it to liver and hepatocytes and identifies it as secreted to blood. Its established functions include maintaining plasma colloid osmotic pressure and transporting hormones, fatty acids, metabolites, and drugs. It is present in the blood-microparticle evidence (GO:CC blood microparticle; q_global = 5.76e-07) and in many supplementary plasma-proteome contexts (STRING PMID (2018) A proteomic approach of biomarker candidate discovery for alcoholic liver cirrhosis.; within-query FDR = 1.38e-06) through (STRING COMPARTMENTS Blood microparticle; within-query FDR = 7.05e-06). Its extensive literature and associations with albumin-related and systemic diseases make it a strong indicator of plasma composition rather than a tissue-specific mechanism.
- **Conclusion**: Established evidence supports ALB as a central marker of circulating plasma material and a carrier protein within the module. The module data do not establish that ALB is mechanistically driving co-abundance in myometrium or testis.

#### SERPINA3

- **Related proteins** (co-abundance neighbors): SERPINA1 (0.96), SERPINC1 (0.94), LDHB (0.92), HPX (0.90), GC (0.87), IGHG1 (0.83); STRING partners: ALB (0.914)
- **HPA**: Group enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_07265.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_08224.1, huMAP3_02242.1
- **Function (MyGene.info)**: serpin family A member 3. The protein encoded by this gene is a member of the serpin family of proteins, a group of proteins that inhibit serine proteases. This gene is one in a cluster of serpin genes located on the q arm of chromosome 14. Polymorphisms in this protein appear to be tissue specific and influence protease targeting. Variations in this protein's sequence have been implicated in Alzheimer's disease, and defic…
- **Diseases (Open Targets)**: prostate carcinoma (0.359); chronic kidney disease (0.217); peripheral arterial occlusive disease 1 (0.118); central nervous system cancer (0.118); glioma (0.105)
- **Europe PMC papers**: 5458
- **Why important**: SERPINA3 has the strongest network position in the supplied module and links the principal protease-regulatory cluster to HPX, SERPINA1, SERPINC1, GC, LDHB, and IGHG1. It is a secreted liver-associated serpin that inhibits serine proteases. It contributes to the globally significant blood-microparticle term (GO:CC blood microparticle; q_global = 5.76e-07) and appears across many supplementary plasma and inflammatory contexts (STRING PMID (2018) A proteomic approach of biomarker candidate discovery for alcoholic liver cirrhosis.; within-query FDR = 1.38e-06), (STRING PMID (2012) Proteomic investigation of falciparum and vivax malaria for identification of surrogate protein markers.; within-query FDR = 1.77e-06), (STRING PMID (2023) Analysis of Plasma Proteins Involved in Inflammation, Immune ResponseComplement System, and Blood Coagulation upon Admission of COVID-19 Patients to Hospital May Help to Predict the Prognosis of the Disease.; within-query FDR = 3.33e-06), (STRING PMID (2019) Serum Proteomic Analysis Reveals Vitamin D-Binding Protein (VDBP) as a Potential Biomarker for Low Bone Mineral Density in Mexican Postmenopausal Women.; within-query FDR = 6.17e-06), (STRING PMID (2017) Subventricular zone involvement in Glioblastoma - A proteomic evaluation and clinicoradiological correlation.; within-query FDR = 6.17e-06), (STRING PMID (1983) A study on proteins contained in urine of gestosis patients.; within-query FDR = 6.17e-06), (STRING PMID (2019) Changes to the Human Serum Proteome in Response to High Intensity Interval Exercise: A Sequential Top-Down Proteomic Analysis.; within-query FDR = 6.91e-06), (STRING Component Blood microparticle; within-query FDR = 6.94e-06), and (STRING COMPARTMENTS Blood microparticle; within-query FDR = 7.05e-06). The supplied evidence also associates it with inflammatory responses, cytokine responses, liver disease, Alzheimer disease, and several disease areas in Open Targets, with a substantial literature.
- **Conclusion**: Established evidence supports SERPINA3 as a hub-like extracellular protease-regulatory marker that helps define the plasma-associated module. Its connection to IGHG1 may reflect shared abundance or extracellular context, but the data do not prove a direct immune mechanism.

#### HPX

- **Related proteins** (co-abundance neighbors): SERPINA1 (0.91), SERPINA3 (0.90), SERPINC1 (0.84), TF (0.82); STRING partners: ALB (0.981), GC (0.827), SERPINA1 (0.897), SERPINC1 (0.762), TF (0.852)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_07265.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_07432.1, huMAP3_08700.1, huMAP3_02236.1, huMAP3_09273.1
- **Function (MyGene.info)**: hemopexin. This gene encodes a plasma glycoprotein that binds heme with high affinity. The encoded protein is an acute phase protein that transports heme from the plasma to the liver and may be involved in protecting cells from oxidative stress. [provided by RefSeq, Apr 2009].
- **Diseases (Open Targets)**: panniculitis (0.116); neoplasm (0.107); familial idiopathic steroid-resistant nephrotic syndrome (0.101); hepatocellular carcinoma (0.101); focal segmental glomerulosclerosis (0.097)
- **Europe PMC papers**: 6894
- **Why important**: HPX connects multiple protease-regulatory and transport proteins, including SERPINA1, SERPINA3, SERPINC1, and TF, and participates in numerous hu.MAP complexes (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_07432.1), (hu.MAP huMAP3_08700.1), (hu.MAP huMAP3_02236.1), and (hu.MAP huMAP3_09273.1). HPA identifies it as liver- and hepatocyte-enriched and secreted to blood. Its established function is high-affinity heme binding and transport to the liver, with a role in limiting heme-associated oxidative stress. It contributes to blood microparticle and humoral-response terms (GO:CC blood microparticle; q_global = 5.76e-07), (GO:BP humoral immune response; q_global = 0.0196), and (GO:BP humoral immune response mediated by circulating immunoglobulin; q_global = 0.0334), and has extensive literature and disease associations involving oxidative, renal, inflammatory, and neoplastic contexts.
- **Conclusion**: Established evidence supports HPX as a biologically informative bridge between plasma transport, heme handling, and extracellular defense. A tissue-protective oxidative-stress role in the two tissues is plausible but remains unproven by this module.

#### SERPINC1

- **Related proteins** (co-abundance neighbors): SERPINA3 (0.94), HPX (0.84), TF (0.83), KNG1 (0.80); STRING partners: ALB (0.933), GC (0.84), HPX (0.762), KNG1 (0.758)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 is embedded in the core STRING network with SERPINA3, HPX, TF, KNG1, ALB, and GC and is present in the high-membership hu.MAP plasma complex (hu.MAP huMAP3_15040.1). It encodes antithrombin, an established plasma serine-protease inhibitor that regulates thrombin and other coagulation proteases, with activity enhanced by heparin. It contributes to (GO:CC blood microparticle; q_global = 5.76e-07) and is repeatedly recovered in the supplementary coagulation, plasma, inflammation, and disease-proteome contexts (STRING PMID (2018) A proteomic approach of biomarker candidate discovery for alcoholic liver cirrhosis.; within-query FDR = 1.38e-06), (STRING PMID (2019) Label-Free Proteomics Revealed Oxidative Stress and Inflammation as Factors That Enhance Chemoresistance in Luminal Breast Cancer.; within-query FDR = 2.07e-06) through (STRING PMID (2017) Subventricular zone involvement in Glioblastoma - A proteomic evaluation and clinicoradiological correlation.; within-query FDR = 6.17e-06), (STRING PMID (2015) Plasma proteomic analysis of active and torpid greater mouse-eared bats (Myotis myotis).; within-query FDR = 6.17e-06) through (STRING COMPARTMENTS Blood microparticle; within-query FDR = 7.05e-06). Its disease associations include hereditary antithrombin deficiency and venous thromboembolic disorders.
- **Conclusion**: Established evidence supports SERPINC1 as a key coagulation-regulatory component and as evidence that the module includes a hemostatic plasma signal. The data do not show that altered coagulation is the cause of the conserved tissue pattern.

#### TF

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.83), HPX (0.82), ALB (0.80); STRING partners: ALB (0.9), GC (0.811), HPX (0.852), SERPINA1 (0.848)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_07265.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_08224.1, huMAP3_02242.1
- **Function (MyGene.info)**: transferrin. This gene encodes a glycoprotein with an approximate molecular weight of 76.5 kDa. It is thought to have been created as a result of an ancient gene duplication event that led to generation of homologous C and N-terminal domains each of which binds one ion of ferric iron. The function of this protein is to transport iron from the intestine, reticuloendothelial system, and liver parenchymal cells t…
- **Diseases (Open Targets)**: atransferrinemia (0.776); alcohol drinking (0.492); hemochromatosis type 1 (0.471); neurodegenerative disease (0.400); urolithiasis (0.329)
- **Europe PMC papers**: 143656
- **Why important**: TF connects HPX, SERPINC1, ALB, GC, and SERPINA1 in STRING and recurs across many hu.MAP complexes (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_09434.1), (hu.MAP huMAP3_08224.1), and (hu.MAP huMAP3_02242.1). HPA assigns it to liver-associated tissue or cell groups and identifies it as secreted to blood. Its established function is iron transport and intracellular iron homeostasis, and it also contributes to antibacterial and humoral-response annotations (GO:CC blood microparticle; q_global = 5.76e-07), (GO:BP antibacterial humoral response; q_global = 0.00339), (GO:BP antimicrobial humoral response; q_global = 0.0133), and (GO:BP humoral immune response; q_global = 0.0196). It has a very extensive literature and disease associations including atransferrinemia, hemochromatosis, and neurodegenerative disease.
- **Conclusion**: Established evidence supports TF as the module component linking plasma transport to iron availability and antimicrobial defense. A coordinated iron-limitation response in the sampled tissues is a hypothesis, not a demonstrated conclusion.

#### IGHA1

- **Related proteins** (co-abundance neighbors): IGHG2 (0.92), IGHG1 (0.90), IGKC (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Group enriched; location None; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: immunoglobulin heavy constant alpha 1
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 1712
- **Why important**: IGHA1 is part of the immunoglobulin subnetwork with IGHG1, IGHG2, and IGKC and contributes to every globally significant immunoglobulin and humoral term (GO:CC blood microparticle; q_global = 5.76e-07) through (GO:BP B cell receptor signaling pathway; q_global = 0.0351). HPA assigns it to lymphoid and intestinal-associated tissues, plasma cells, and B-cell groups, and identifies it as an immunoglobulin gene. Unlike the plasma-protein core, it has no supplied STRING partners or hu.MAP complex, making it important as evidence for coordinated immunoglobulin abundance rather than a known physical interaction hub. Its established identity as the immunoglobulin heavy constant alpha gene and its substantial literature support its interpretation as an adaptive humoral marker.
- **Conclusion**: Established evidence supports IGHA1 as a marker of immunoglobulin or plasma-cell contribution to the module. The module does not establish local IgA production by myometrium or testis, nor does it identify the antigenic trigger.

## Module 2

**Tissue pair**: myometrium and testis  
**Genes (9)**: A2M, CFH, C3, C5, FGB, FGG, SERPIND1, ITIH1, ITIH2

### Function

The module is best interpreted as a circulating extracellular protease-control, complement-regulation, and coagulation-associated program. The primary evidence is the globally corrected enrichment for complement and coagulation cascades (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 2.38e-06), blood microparticle (GO:CC blood microparticle; q_global = 0.000177), peptidase and endopeptidase inhibitor or regulator activities (4 globally significant GO/KEGG terms, q_global 0.000329–0.000862; see the table), humoral immunity (GO:BP humoral immune response; q_global = 0.00327), neutrophil extracellular trap formation (KEGG Neutrophil extracellular trap formation - Homo sapiens (human); q_global = 0.00339), alternative-pathway complement activation and complement regulation (GO:BP complement activation, alternative pathway; q_global = 0.0135) (GO:BP regulation of complement activation; q_global = 0.0135), broader complement activation (GO:BP complement activation; q_global = 0.018), and regulation of the humoral response (GO:BP regulation of humoral immune response; q_global = 0.0209). Fibrinogen genes FGB and FGG connect the module to clot formation and extracellular matrix or cell-adhesion effects, whereas C3, C5, and CFH represent complement activation and its regulation. A2M, ITIH1, ITIH2, and SERPIND1 provide protease inhibition or regulation. The infection-related pathway terms (KEGG Staphylococcus aureus infection - Homo sapiens (human); q_global = 0.00441) and (KEGG Coronavirus disease - Homo sapiens (human); q_global = 0.0152) should be read as pathway-overlap evidence rather than evidence that the tissues are infected. The structure is coherent with a plasma protein network, but it does not by itself establish production or action within myometrium or testis.

**Cell composition.** The module is overwhelmingly composed of secreted blood or extracellular proteins: every module gene is annotated as secreted to blood in the HPA summary. HPA indicates liver enrichment for nearly all genes and hepatocyte enrichment for all genes, with one gene showing lung tissue enhancement. Six genes are not detected in immune cells, while the remaining immune-cell signals are limited to enhancement or enrichment for selected cell types rather than a broad leukocyte program. Protein staining is absent in myometrium for every gene and is detected in testis for only a subset. This strongly suggests that the shared tissue association may reflect vascular or plasma carryover, blood microparticles, extracellular vesicles, or a shared blood-exposed compartment rather than a resident myometrial or testicular transcriptional program. The module is therefore not best described as a broadly expressed housekeeping module or as primarily blood-cell derived.

**GO/KEGG enrichment**: 18 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 2.38e-06 | A2M, C3, C5, CFH, FGB, FGG, SERPIND1 |
| GO:CC blood microparticle | 0.000177 | A2M, C3, CFH, FGB, FGG, ITIH1, ITIH2 |
| GO:MF endopeptidase inhibitor activity | 0.000329 | A2M, C3, C5, ITIH1, ITIH2, SERPIND1 |
| GO:MF peptidase inhibitor activity | 0.000329 | A2M, C3, C5, ITIH1, ITIH2, SERPIND1 |
| GO:MF endopeptidase regulator activity | 0.000551 | A2M, C3, C5, ITIH1, ITIH2, SERPIND1 |
| GO:MF peptidase regulator activity | 0.000862 | A2M, C3, C5, ITIH1, ITIH2, SERPIND1 |
| GO:BP humoral immune response | 0.00327 | A2M, C3, C5, CFH, FGB |
| KEGG Neutrophil extracellular trap formation - Homo sapiens (human) | 0.00339 | C3, C5, FGB, FGG |
| KEGG Staphylococcus aureus infection - Homo sapiens (human) | 0.00441 | C3, C5, CFH, FGG |
| GO:MF enzyme inhibitor activity | 0.00622 | A2M, C3, C5, ITIH1, ITIH2, SERPIND1 |
| GO:MF molecular function inhibitor activity | 0.0106 | A2M, C3, C5, ITIH1, ITIH2, SERPIND1 |
| GO:BP complement activation, alternative pathway | 0.0135 | C3, C5, CFH |
| GO:BP regulation of complement activation | 0.0135 | A2M, C3, CFH |
| KEGG Coronavirus disease - Homo sapiens (human) | 0.0152 | C3, C5, FGB, FGG |
| GO:BP complement activation | 0.018 | A2M, C3, C5, CFH |

### STRING and hu.MAP

STRING supports a biologically established complement, coagulation, and protease-regulation network. The strongest reported links include C3 with CFH and C5, FGB with FGG, and fibrinogen or SERPIND1 links; ITIH1-ITIH2 is also supported. The STRING functional results (15 supplementary STRING terms; within-query FDR 3.33e-10–0.00017) consistently recover complement and coagulation, blood microparticles, extracellular or secreted proteins, and plasma-associated biology, but their FDR values are supplementary and are not treated as global enrichment significance. hu.MAP provides convergent complex-level support: the module genes repeatedly occur together in complexes containing complement factors, fibrinogen components, protease inhibitors, plasma proteins, and related extracellular proteins (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_02811.1) (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_00178.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07265.1). These observations show that many relationships are already known and that the module is chemically and functionally coherent. They do not demonstrate that all proteins form one stable complex in either tissue, because the hu.MAP complexes contain additional proteins and may represent overlapping plasma-protein assemblies.

**STRING interactions (score >= 0.7)**: 12 of 36 gene pairs: A2M–FGB (0.841); A2M–FGG (0.761); A2M–SERPIND1 (0.771); C3–C5 (0.974); C3–CFH (0.999); C5–CFH (0.824); FGB–FGG (0.999); FGB–ITIH2 (0.704); FGB–SERPIND1 (0.951); FGG–SERPIND1 (0.96); ITIH1–ITIH2 (0.835); ITIH2–SERPIND1 (0.712)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization (FDR = 3.33e-10, 9 genes); KEGG Complement and coagulation cascades (FDR = 1.67e-07, 7 genes); PMID (2022) Next-generation Proteomics-Based Discovery, Verification, and Validation of Urine Biomarkers for Bladder Cancer Diagnosis. (FDR = 5.65e-07, 7 genes); NetworkNeighborAL Mixed, incl. COVID-19, thrombosis and anticoagulation, and Scavenging of heme from plasma (FDR = 9.82e-07, 6 genes); PMID (2021) An Immunomodulatory Transcriptional Signature Associated With Persistent Listeria Infection in Hepatocytes. (FDR = 1.36e-05, 7 genes); NetworkNeighborAL Mixed, incl. COVID-19, thrombosis and anticoagulation, and Inter-alpha-trypsin inhibitor heavy chain C-terminus (FDR = 1.79e-05, 5 genes); Component Blood microparticle (FDR = 2.97e-05, 7 genes); COMPARTMENTS Blood microparticle (FDR = 3.02e-05, 7 genes); Keyword Glycoprotein (FDR = 5.78e-05, 9 genes); Keyword Signal (FDR = 5.78e-05, 9 genes); COMPARTMENTS Extracellular space (FDR = 7.04e-05, 9 genes); PMID (2023) Macular Edema in Central Retinal Vein Occlusion Correlates With Aqueous Fibrinogen Alpha Chain. (FDR = 7.25e-05, 7 genes); PMID (2020) Aqueous Fibronectin Correlates With Severity of Macular Edema and Visual Acuity in Patients With Branch Retinal Vein Occlusion: A Proteome Study. (FDR = 9.27e-05, 6 genes); Keyword Secreted (FDR = 0.00014, 8 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 0.00017, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10678.1 (A2M, C3, C5, FGB, FGG, SERPIND1, CFH, ITIH2, ITIH1; 9/71); huMAP3_15040.1 (A2M, C3, FGB, FGG, SERPIND1, CFH, ITIH2, ITIH1; 8/64); huMAP3_08395.1 (A2M, C3, C5, FGB, FGG, ITIH2, ITIH1; 7/43); huMAP3_09531.1 (A2M, C3, C5, FGB, FGG, ITIH2, ITIH1; 7/47); huMAP3_10101.1 (A2M, C3, C5, FGB, FGG, ITIH2, ITIH1; 7/49); huMAP3_07541.1 (A2M, C5, FGG, ITIH2, ITIH1; 5/19); huMAP3_09434.1 (C3, C5, FGB, FGG, SERPIND1; 5/33); huMAP3_08224.1 (C3, C5, FGG, SERPIND1; 4/21); huMAP3_07701.1 (A2M, ITIH2, ITIH1; 3/22); huMAP3_09273.1 (A2M, ITIH2, ITIH1; 3/28); huMAP3_02811.1 (C5, ITIH1; 2/8); huMAP3_02242.1 (C3, FGG; 2/9); huMAP3_00178.1 (C5, ITIH1; 2/9); huMAP3_08796.1 (C5, ITIH1; 2/15); huMAP3_07432.1 (C3, FGB; 2/18); huMAP3_09832.1 (C5, ITIH1; 2/18); huMAP3_07265.1 (A2M, ITIH2; 2/20)

### Novelty

The biological theme is not a new molecular pathway: complement, coagulation, fibrinogen, inter-alpha-trypsin inhibitor, SERPIND1, and plasma protease regulation are already represented by STRING and hu.MAP relationships. The potentially new observation is the co-abundance of this established circulating protein ensemble across myometrium and testis in the analyzed dataset. That observation cannot be called a new tissue-intrinsic mechanism from the fact sheet alone. The absence of a specific relationship from STRING or hu.MAP would not establish novelty, and the extensive pre-existing network support argues against presenting the module as a previously unknown protein complex. A defensible novelty claim is limited to the dataset-specific cross-tissue co-abundance pattern, which requires replication, control for blood contamination or vascular content, and comparison with other tissues.

**Hypothesis.** Hypothesis: the shared module reflects a blood-derived or extracellular-vesicle-associated homeostatic interface present in both tissue samples. Hepatocyte-derived complement components, fibrinogen chains, inter-alpha-trypsin inhibitor heavy chains, alpha-2-macroglobulin, SERPIND1, and CFH may co-vary because vascular exposure, local permeability, extracellular matrix interaction, inflammation, or tissue injury jointly alter their abundance. Within that extracellular milieu, C3 and C5 could provide complement effector activity, CFH and A2M could restrain complement or protease-mediated damage, SERPIND1 could limit thrombin and related proteases, and FGB-FGG could support fibrin-associated matrix or adhesion responses. ITIH1 and ITIH2 could contribute to hyaluronan or extracellular-matrix stabilization. This is a mechanistic hypothesis, not proof of local synthesis or action in either tissue; it should be tested using blood-depletion or vascular-content covariates, cell-resolved measurements, and tissue-localization assays.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): SERPIND1 (0.83), ITIH1 (0.82); STRING partners: C5 (0.974), CFH (0.999)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_09434.1, huMAP3_08224.1, huMAP3_02242.1, huMAP3_07432.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a central complement component and occupies a connective position between the complement branch and the protease-regulation side of the module. It is included in nearly all of the primary enrichment themes (18 globally significant GO/KEGG terms, q_global 2.38e-06–0.0327; see the table) except the inhibitor-focused terms that do not list it, has very strong STRING support with CFH and C5, and appears in many hu.MAP complexes (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_09434.1), (hu.MAP huMAP3_08224.1), and (hu.MAP huMAP3_02242.1). HPA supports liver and hepatocyte association, secretion to blood, and detection in testis but not myometrium. It also has the largest literature volume in the module and established associations with complement deficiency, atypical hemolytic-uremic syndrome, and complement-mediated renal and retinal disease.
- **Conclusion**: Established evidence supports C3 as the principal complement hub and a major marker of the module's circulating innate-immune character. Its presence does not establish local complement production in myometrium or testis. A tissue-specific role remains a hypothesis requiring localization and functional testing.

#### C5

- **Related proteins** (co-abundance neighbors): SERPIND1 (0.87); STRING partners: C3 (0.974), CFH (0.824)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_07541.1, huMAP3_09434.1, huMAP3_08224.1, huMAP3_02811.1, huMAP3_00178.1, huMAP3_08796.1, huMAP3_09832.1
- **Function (MyGene.info)**: complement C5. This gene encodes a component of the complement system, a part of the innate immune system that plays an important role in inflammation, host homeostasis, and host defense against pathogens. The encoded preproprotein is proteolytically processed to generate multiple protein products, including the C5 alpha chain, C5 beta chain, C5a anaphylatoxin and C5b. The C5 protein is comprised of the C5 alpha…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.744); paroxysmal nocturnal hemoglobinuria (0.610); myasthenia gravis (0.586); atypical hemolytic-uremic syndrome (0.544); neuromyelitis optica (0.516)
- **Europe PMC papers**: 81450
- **Why important**: C5 is a core complement effector and is represented in the complement and coagulation pathway (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 2.38e-06), humoral immune response (GO:BP humoral immune response; q_global = 0.00327), neutrophil extracellular trap formation (KEGG Neutrophil extracellular trap formation - Homo sapiens (human); q_global = 0.00339), alternative-pathway activation (GO:BP complement activation, alternative pathway; q_global = 0.0135), broader complement activation (GO:BP complement activation; q_global = 0.018), and related terms. It has established STRING links with C3 and CFH and occurs across numerous hu.MAP complexes (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08224.1), (hu.MAP huMAP3_02811.1), (hu.MAP huMAP3_00178.1), (hu.MAP huMAP3_08796.1), and (hu.MAP huMAP3_09832.1). HPA identifies it as liver and hepatocyte enriched and secreted to blood, with no detected protein in either target tissue. Its disease associations include late complement deficiency, paroxysmal nocturnal hemoglobinuria, myasthenia gravis, atypical hemolytic-uremic syndrome, and neuromyelitis optica.
- **Conclusion**: Established evidence supports C5 as an effector-side complement component that reinforces the module's inflammatory and host-defense interpretation. The module does not show that C5 is activated locally; abundance of circulating C5 should not be equated with generation of C5a or membrane-attack-complex activity.

#### CFH

- **Related proteins** (co-abundance neighbors): FGB (0.86), ITIH1 (0.85); STRING partners: C3 (0.999), C5 (0.824)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_15040.1
- **Function (MyGene.info)**: complement factor H. This gene is a member of the Regulator of Complement Activation (RCA) gene cluster and encodes a protein with twenty short consensus repeat (SCR) domains. This protein is secreted into the bloodstream and has an essential role in the regulation of complement activation, restricting this innate defense mechanism to microbial infections. Mutations in this gene have been associated with hemolytic-ure…
- **Diseases (Open Targets)**: complement factor H deficiency (0.769); age-related macular degeneration (0.750); atypical hemolytic-uremic syndrome (0.729); age related macular degeneration 4 (0.711); Doyne honeycomb retinal dystrophy (0.688)
- **Europe PMC papers**: 9287
- **Why important**: CFH provides the principal counter-regulatory complement component in the module. It contributes to (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 2.38e-06), (GO:CC blood microparticle; q_global = 0.000177), (GO:BP humoral immune response; q_global = 0.00327), (KEGG Staphylococcus aureus infection - Homo sapiens (human); q_global = 0.00441), (GO:BP complement activation, alternative pathway; q_global = 0.0135), (GO:BP regulation of complement activation; q_global = 0.0135), (GO:BP complement activation; q_global = 0.018), (GO:BP regulation of humoral immune response; q_global = 0.0209), and (GO:BP regulation of response to external stimulus; q_global = 0.0327), links strongly to C3 and C5 in STRING, and is present in the high-confidence hu.MAP complexes (hu.MAP huMAP3_10678.1) and (hu.MAP huMAP3_15040.1). HPA shows liver enrichment, secretion to blood, enhancement in several stromal or hepatic cell contexts, and testis detection but not myometrium detection. CFH has extensive literature and established disease associations including complement factor H deficiency, atypical hemolytic-uremic syndrome, and age-related macular degeneration.
- **Conclusion**: Established evidence supports CFH as a key regulator that balances the complement effector components in this module. Its co-abundance with C3 and C5 is consistent with coordinated circulating complement homeostasis, but it does not prove that the module represents a locally regulated complement circuit in either tissue.

#### FGB

- **Related proteins** (co-abundance neighbors): CFH (0.86), FGG (0.84); STRING partners: A2M (0.841), FGG (0.999), ITIH2 (0.704), SERPIND1 (0.951)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_09434.1, huMAP3_07432.1
- **Function (MyGene.info)**: fibrinogen beta chain. The protein encoded by this gene is the beta component of fibrinogen, a blood-borne glycoprotein comprised of three pairs of nonidentical polypeptide chains. Following vascular injury, fibrinogen is cleaved by thrombin to form fibrin which is the most abundant component of blood clots. In addition, various cleavage products of fibrinogen and fibrin regulate cell adhesion and spreading, display vas…
- **Diseases (Open Targets)**: congenital afibrinogenemia (0.786); familial dysfibrinogenemia (0.705); congenital fibrinogen deficiency (0.622); familial hypodysfibrinogenemia (0.597); cancer (0.592)
- **Europe PMC papers**: 4215
- **Why important**: FGB is a fibrinogen chain that anchors the module to coagulation, fibrin formation, platelet-associated biology, and extracellular adhesion. It contributes to (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 2.38e-06), (GO:CC blood microparticle; q_global = 0.000177), (GO:BP humoral immune response; q_global = 0.00327), (KEGG Neutrophil extracellular trap formation - Homo sapiens (human); q_global = 0.00339), (KEGG Coronavirus disease - Homo sapiens (human); q_global = 0.0152), and (GO:BP regulation of response to external stimulus; q_global = 0.0327), has a very strong STRING relationship with FGG, and is linked to A2M, ITIH2, and SERPIND1. It occurs in numerous hu.MAP complexes, including (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_09434.1), (hu.MAP huMAP3_08224.1), (hu.MAP huMAP3_02242.1), and (hu.MAP huMAP3_07432.1). HPA identifies liver and hepatocyte enrichment, secretion-related localization, and no detected protein in either target tissue. Its established disease associations include congenital and familial fibrinogen disorders.
- **Conclusion**: Established evidence supports FGB as a plasma coagulation and fibrin-matrix marker that helps explain the module's blood-associated composition. Its co-abundance with complement proteins may indicate shared plasma exposure or inflammatory vascular biology, but does not establish clot formation in the sampled tissues.

#### ITIH1

- **Related proteins** (co-abundance neighbors): ITIH2 (0.88), A2M (0.87), CFH (0.85), C3 (0.82); STRING partners: ITIH2 (0.835)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_07541.1, huMAP3_07701.1, huMAP3_09273.1, huMAP3_02811.1, huMAP3_00178.1, huMAP3_08796.1, huMAP3_09832.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 1. This gene encodes a member of the inter-alpha-trypsin inhibitor family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the heavy chain of the inter-alpha-trypsin inhibitor complex, which is secreted by hepatocytes into the blood. The heavy chain also interacts with hyaluronan, and…
- **Diseases (Open Targets)**: osteoarthritis, hip (0.305); osteoarthritis (0.188); schizophrenia (0.185); major depressive disorder (0.183); psychiatric disorder (0.171)
- **Europe PMC papers**: 963
- **Why important**: ITIH1 has the highest network connectivity in the reported module and connects to ITIH2, A2M, CFH, and C3. It contributes to inhibitor, blood-microparticle, and extracellular terms (5 globally significant GO/KEGG terms, q_global 0.000177–0.000862; see the table), (GO:MF enzyme inhibitor activity; q_global = 0.00622) (GO:MF molecular function inhibitor activity; q_global = 0.0106), and (GO:MF serine-type endopeptidase inhibitor activity; q_global = 0.028), is supported by ITIH2 in STRING, and appears in many hu.MAP complexes (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_07541.1), (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_02811.1), (hu.MAP huMAP3_00178.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_09832.1). HPA identifies it as liver and hepatocyte enriched, secreted to blood, detected in testis but not myometrium. Its annotation links the inter-alpha-trypsin inhibitor family to protease control, hyaluronan metabolism, extracellular-matrix stabilization, ovulation, and fertilization; its disease literature includes osteoarthritis and several neuropsychiatric associations.
- **Conclusion**: Established evidence supports ITIH1 as a network bridge between extracellular-matrix or hyaluronan-associated biology and the complement or protease-regulation components. A plausible but unproven hypothesis is that it contributes to tissue-interface or matrix stabilization in testis and myometrium; the HPA pattern more strongly supports a circulating source than resident tissue production.

## Module 3

**Tissue pair**: myometrium and testis  
**Genes (11)**: AAMDC, CTSC, CNN2, CFL2, CSRP1, DSTN, GLRX, GSTP1, HNRNPH1, LGALS1, PRDX3

### Function

This module is most consistent with a cytoskeletal, contractile-cell, and redox-associated co-abundance pattern rather than a formally enriched pathway. Its strongest internal structure centers on LGALS1, which connects to many module genes, and on the actin-regulatory pair DSTN and CFL2. DSTN and CFL2 have direct high-confidence STRING support and jointly occur in three hu.MAP complexes (hu.MAP huMAP3_03395.1), (hu.MAP huMAP3_09579.1), (hu.MAP huMAP3_11076.1). Their annotations support actin-filament turnover and severing, while CNN2 supports actin-filament and actomyosin organization and smooth-muscle contraction. GSTP1, PRDX3, and GLRX provide compatible oxidative-stress, detoxification, and antioxidant functions. However, no GO or KEGG term passed global correction, so this is an interpretation of the gene functions and network structure, not a globally significant enrichment result.

**Cell composition.** The module does not appear to be dominated by plasma or secreted proteins: only LGALS1 is annotated as secreted to blood, and CTSC is annotated as intracellular and membrane-associated. Most genes have low immune-cell specificity, with only AAMDC showing immune-cell enhancement for basophils. The HPA profile instead points toward structural and stromal or contractile cell biology, including smooth-muscle, vascular, skeletal-muscle, heart-muscle, decidual-stromal, and related cell-type annotations. Most module proteins are detected in both myometrium and testis, although CNN2 and GLRX have tissue-specific detection gaps. Thus, blood contamination is not the leading explanation from the supplied HPA evidence, while shared smooth-muscle, stromal, vascular, or other structural cell populations remain plausible contributors.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

Known physical or functional relationships are concentrated in DSTN and CFL2. They form the only high-confidence STRING interaction reported for the module, and they are co-members in hu.MAP complexes (hu.MAP huMAP3_03395.1), (hu.MAP huMAP3_09579.1), and (hu.MAP huMAP3_11076.1). Those complexes also contain actin-regulatory or cytoskeletal proteins such as CFL1, WDR1, CORO proteins, SYNPO, AFAP1, and related partners, providing external support for an actin-remodeling context. LGALS1 has a central position in the module co-abundance graph but no reported STRING partner or hu.MAP complex. The remaining module relationships are therefore primarily co-abundance relationships rather than independently documented molecular interactions. This distinction argues for a coherent transcriptional or cellular-state signal, but not for a single fully established multiprotein complex containing all module genes.

**STRING interactions (score >= 0.7)**: 1 of 55 gene pairs: CFL2–DSTN (0.921)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03395.1 (DSTN, CFL2; 2/6); huMAP3_09579.1 (DSTN, CFL2; 2/9); huMAP3_11076.1 (DSTN, CFL2; 2/10)

### Novelty

The module may represent a potentially useful tissue-pair co-abundance pattern, but the fact sheet does not establish it as a new biological mechanism. Its actin-related core is not novel in the strong sense because DSTN-CFL2 is already supported by STRING and their shared membership in hu.MAP complexes (hu.MAP huMAP3_03395.1), (hu.MAP huMAP3_09579.1), (hu.MAP huMAP3_11076.1), while the functions of several genes are well established. The potentially novel aspect is the particular cross-tissue co-abundance combination of actin regulation, galectin biology, oxidative-stress control, RNA processing, and proteolysis in myometrium and testis. Absence of STRING or hu.MAP support for many other pairs cannot by itself demonstrate novelty. A claim of new finding would require comparison with prior co-expression modules, independent cohorts, cell-composition controls, and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a shared structural-cell state present in myometrium and testis in which actin-filament turnover and contractile architecture are coordinated with extracellular or cell-matrix signaling through LGALS1, while GSTP1, PRDX3, and GLRX buffer oxidative and electrophilic stress. DSTN-CFL2 may form the mechanistic actin-remodeling core, with CNN2 stabilizing or organizing actomyosin structures. The co-abundance signal could arise from smooth-muscle or stromal cells shared across the tissues, but this remains a hypothesis because the enrichment analyses provide no globally significant GO or KEGG term and the module does not demonstrate direct physical interaction among most members.

### Important genes

#### LGALS1

- **Related proteins** (co-abundance neighbors): GSTP1 (0.88), CNN2 (0.87), AAMDC (0.85), GLRX (0.84), HNRNPH1 (0.83), CSRP1 (0.82), PRDX3 (0.82), DSTN (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galectin 1. The galectins are a family of beta-galactoside-binding proteins implicated in modulating cell-cell and cell-matrix interactions. This gene product may act as an autocrine negative growth factor that regulates cell proliferation. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: glaucoma (0.349); open-angle glaucoma (0.343); chronic kidney disease (0.330); smoking initiation (0.162); melanoma (0.121)
- **Europe PMC papers**: 4025
- **Why important**: LGALS1 is the most connected and strongest node in the module. It is annotated as a beta-galactoside-binding protein involved in cell-cell and cell-matrix interactions and regulation of cell proliferation, is detected in both tissues, and has extensive literature support. Its broad connectivity makes it the best candidate for coordinating the module's structural, stromal, and signaling-associated components. Its annotation as secreted to blood also warrants attention when interpreting tissue-level co-abundance.
- **Conclusion**: Established evidence supports LGALS1 as a central co-abundance hub with cell-matrix and signaling relevance. It is plausible, but not established, that LGALS1 links the actin-associated state to extracellular or stromal signaling in both tissues.

#### DSTN

- **Related proteins** (co-abundance neighbors): CFL2 (0.95), CNN2 (0.88), LGALS1 (0.81); STRING partners: CFL2 (0.921)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in myometrium, testis
- **hu.MAP 3.0**: huMAP3_03395.1, huMAP3_09579.1, huMAP3_11076.1
- **Function (MyGene.info)**: destrin, actin depolymerizing factor. The product of this gene belongs to the actin-binding proteins ADF family. This family of proteins is responsible for enhancing the turnover rate of actin in vivo. This gene encodes the actin depolymerizing protein that severs actin filaments (F-actin) and binds to actin monomers (G-actin). Two transcript variants encoding distinct isoforms have been identified for this gene. [provided by RefSeq, …
- **Diseases (Open Targets)**: Alzheimer disease (0.332); neurodegenerative disease (0.324); Parkinson disease (0.323); lysosomal storage disease (0.323); autoimmune disorder of central nervous system (0.305)
- **Europe PMC papers**: 872
- **Why important**: DSTN is directly connected to CFL2 in STRING and is present with CFL2 in all three reported hu.MAP complexes (hu.MAP huMAP3_03395.1), (hu.MAP huMAP3_09579.1), (hu.MAP huMAP3_11076.1). Its annotated function in actin-filament depolymerization and severing matches the principal supported structural theme of the module. It is tissue-enhanced in blood vessel and cell-type enhanced in smooth and vascular smooth muscle, with protein detected in both tissues.
- **Conclusion**: Established evidence supports DSTN as a core actin-remodeling component and as the best externally corroborated partner of CFL2 in this module. Its role as a driver of the cross-tissue co-abundance pattern remains a hypothesis.

#### CFL2

- **Related proteins** (co-abundance neighbors): DSTN (0.95); STRING partners: DSTN (0.921)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in myometrium, testis
- **hu.MAP 3.0**: huMAP3_03395.1, huMAP3_09579.1, huMAP3_11076.1
- **Function (MyGene.info)**: cofilin 2. This gene encodes an intracellular protein that is involved in the regulation of actin-filament dynamics. This protein is a major component of intranuclear and cytoplasmic actin rods. It can bind G- and F-actin in a 1:1 ratio of cofilin to actin, and it reversibly controls actin polymerization and depolymerization in a pH-dependent manner. Mutations in this gene cause nemaline myopathy type 7, a f…
- **Diseases (Open Targets)**: nemaline myopathy 7 (0.758); typical nemaline myopathy (0.599); atrial fibrillation (0.525); nemaline myopathy (0.376); Takayasu arteritis (0.303)
- **Europe PMC papers**: 1415
- **Why important**: CFL2 is the muscle-associated member of the DSTN-CFL2 pair, is present in the same three hu.MAP complexes (hu.MAP huMAP3_03395.1), (hu.MAP huMAP3_09579.1), (hu.MAP huMAP3_11076.1), and has the reported high-confidence STRING relationship with DSTN. It regulates actin polymerization and depolymerization, is group-enriched in muscle tissues, and is cell-type enhanced in smooth-muscle-related populations. Its disease associations include nemaline myopathy, directly connecting the gene to muscle structural integrity.
- **Conclusion**: Established evidence supports CFL2 as a muscle-relevant actin-dynamics component and a key anchor of the module's known interaction structure. It is plausible that CFL2 helps explain preservation of the module across myometrium and testis, but the module does not prove that it has a causal role.

#### CNN2

- **Related proteins** (co-abundance neighbors): DSTN (0.88), LGALS1 (0.87), CTSC (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calponin 2. The protein encoded by this gene, which can bind actin, calmodulin, troponin C, and tropomyosin, may function in the structural organization of actin filaments. The encoded protein could play a role in smooth muscle contraction and cell adhesion. Several pseudogenes of this gene have been identified, and are present on chromosomes 1, 2, 3, 6, 9, 11, 13, 15, 16, 21 and 22. Alternative splicing resu…
- **Diseases (Open Targets)**: Pulmonary artery atresia (0.416); asthma (0.410); retinitis pigmentosa (0.370); Alzheimer disease (0.366); chronic rhinosinusitis (0.333)
- **Europe PMC papers**: 983
- **Why important**: CNN2 is connected to both DSTN and LGALS1 and is annotated as an actin-, calmodulin-, troponin-C-, and tropomyosin-binding protein involved in actin-filament organization, actomyosin structure, smooth-muscle contraction, adhesion, and mechanical response. Its cell-type annotations include smooth-muscle-related populations, although protein detection was not reported in the two examined tissues.
- **Conclusion**: Established evidence supports CNN2 as a functionally compatible structural and contractile component. Its lack of reported protein detection in myometrium and testis makes it a more cautious marker of the module than DSTN or CFL2, and its contribution should be tested at the transcript and protein levels.

#### GSTP1

- **Related proteins** (co-abundance neighbors): LGALS1 (0.88), PRDX3 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutathione S-transferase pi 1. Glutathione S-transferases (GSTs) are a family of enzymes that play an important role in detoxification by catalyzing the conjugation of many hydrophobic and electrophilic compounds with reduced glutathione. Based on their biochemical, immunologic, and structural properties, the soluble GSTs are categorized into 4 main classes: alpha, mu, pi, and theta. This GST family member is a polymorphic gene…
- **Diseases (Open Targets)**: neurodegenerative disease (0.350); breast cancer (0.117); hepatocellular carcinoma (0.115); neoplasm (0.114); posterior cortical atrophy (0.113)
- **Europe PMC papers**: 12759
- **Why important**: GSTP1 links LGALS1 and PRDX3 in the module and has the largest literature volume among the selected genes. Its established functions include glutathione conjugation, detoxification, response to reactive oxygen species, glutathione metabolism, and xenobiotic metabolism. It is detected in both tissues and is intracellular rather than secreted.
- **Conclusion**: Established evidence supports GSTP1 as a redox and detoxification component that complements the actin-associated core. It is plausible that oxidative or electrophilic stress helps shape the shared module, but the co-abundance data do not establish that stress is the initiating mechanism.

## Module 4

**Tissue pair**: myometrium and testis  
**Genes (27)**: ABCF1, ACTN1, AP1B1, AP2B1, COPB1, DDX6, DNM2, HERC4, NEK9, PFAS, UPF1, SEC23IP, SEC24C, SEC24D, AARS1, VARS1, THOP1, TIMM44, TNPO1, TNPO3, TRNT1, USP5, UGGT1, UNC45A, USO1, CSE1L, XPNPEP1

### Function

The strongest interpretation is a conserved intracellular protein-trafficking and endomembrane-organization module, centered on coated-vesicle biology and transport between the endoplasmic reticulum and Golgi. The primary evidence is the globally corrected enrichment for coated vesicle (GO:CC coated vesicle; q_global = 0.00409), intracellular protein transport (GO:BP intracellular protein transport; q_global = 0.00492), coated vesicle membrane (GO:CC coated vesicle membrane; q_global = 0.0067), vesicle coat (GO:CC vesicle coat; q_global = 0.00764), ER-to-Golgi vesicle-mediated transport (GO:BP endoplasmic reticulum to Golgi vesicle-mediated transport; q_global = 0.0111), ER-to-Golgi transport vesicle membrane (GO:CC ER to Golgi transport vesicle membrane; q_global = 0.041), and establishment of protein localization (GO:BP establishment of protein localization; q_global = 0.045). The cytosol term (GO:CC cytosol; q_global = 0.0181) is broad and should be interpreted as supporting cellular localization rather than as a specific functional conclusion. The genes span COPII cargo selection and vesicle formation through SEC24C, SEC24D, and SEC23IP, Golgi and coatomer functions through COPB1 and USO1, and clathrin-associated trafficking and membrane fission through AP1B1, AP2B1, and DNM2. The module also contains nuclear import, RNA surveillance, translation, mitochondrial import, proteolysis, and cytoskeletal genes, indicating that it is not a single purified vesicle complex. These additional genes may represent coordinated cellular proteostasis and trafficking demands, or may partly reflect co-abundance without direct physical interaction.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the HPA summary identifies only one secreted gene, and most genes have low tissue specificity. Thus, a blood-plasma explanation is not supported by the overall composition. Most genes also have low immune-cell specificity, although several genes show cell-type enrichment in neutrophils, neutrophil progenitors, erythrocyte progenitors, spermatocytes, spermatids, or other specialized cell types. The module therefore includes broadly expressed housekeeping-like machinery together with cell-state-associated signals, especially in germ-cell populations. ACTN1 is tissue enhanced in smooth muscle, USO1 is tissue enhanced in skeletal muscle, and the HPA protein observations show broad detection in testis and substantial detection in myometrium. The shared signal is consequently more consistent with common intracellular trafficking and proteostasis requirements of cells in both tissues than with a simple secreted-protein or blood-contamination signature. Nevertheless, the cell-type enrichment for germ cells and some blood-associated populations means that cellular composition should be considered when interpreting the cross-tissue conservation.

**GO/KEGG enrichment**: 8 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC coated vesicle | 0.00409 | AP1B1, AP2B1, COPB1, DNM2, SEC23IP, SEC24C, SEC24D, USO1 |
| GO:BP intracellular protein transport | 0.00492 | AP1B1, AP2B1, COPB1, CSE1L, SEC23IP, SEC24C, SEC24D, TIMM44, TNPO1, TNPO3, USO1 |
| GO:CC coated vesicle membrane | 0.0067 | AP1B1, AP2B1, COPB1, SEC23IP, SEC24C, SEC24D, USO1 |
| GO:CC vesicle coat | 0.00764 | AP1B1, AP2B1, COPB1, SEC24C, SEC24D |
| GO:BP endoplasmic reticulum to Golgi vesicle-mediated transport | 0.0111 | COPB1, SEC23IP, SEC24C, SEC24D, USO1 |
| GO:CC cytosol | 0.0181 | AARS1, ABCF1, ACTN1, AP1B1, AP2B1, COPB1, CSE1L, DDX6, DNM2, HERC4, NEK9, PFAS, SEC23IP, SEC24C, SEC24D, THOP1, TNPO1, TNPO3, TRNT1, UNC45A, UPF1, USO1, USP5, VARS1, XPNPEP1 |
| GO:CC ER to Golgi transport vesicle membrane | 0.041 | SEC23IP, SEC24C, SEC24D, USO1 |
| GO:BP establishment of protein localization | 0.045 | AP1B1, AP2B1, COPB1, CSE1L, DDX6, DNM2, SEC23IP, SEC24C, SEC24D, TIMM44, TNPO1, TNPO3, USO1 |

### STRING and hu.MAP

STRING provides direct or database-supported relationships within the central trafficking backbone: SEC24C is linked to SEC24D, SEC23IP, COPB1, and USO1; SEC24C and SEC24D form the strongest pair in the listed network; COPB1 is linked to USO1; and AP1B1, AP2B1, and DNM2 form a clathrin-adaptor and membrane-fission neighborhood. STRING also supports AARS1 with VARS1, DDX6 with UPF1, and TNPO1 with TNPO3, while CSE1L is linked to TNPO1. The STRING functional terms independently reinforce coated-vesicle, vesicle-coat, ER-to-Golgi, and intracellular-transport biology, but they remain supplementary evidence and are not global enrichment claims. hu.MAP gives stronger complex-level support for the interpretation. The SEC24C, SEC24D, and SEC23IP combination recurs in multiple COPII-related complexes (hu.MAP huMAP3_07775.1) through (hu.MAP huMAP3_13535.1), while AP1B1 and AP2B1 recur in several adaptor and coated-vesicle complexes, including (hu.MAP huMAP3_12394.1) and (hu.MAP huMAP3_08540.1) through (hu.MAP huMAP3_12918.1). TNPO1 and TNPO3 co-occur in transport-related complexes (hu.MAP huMAP3_11232.1), (hu.MAP huMAP3_09053.1), and (hu.MAP huMAP3_09592.1). These observations show that parts of the module recover known molecular neighborhoods, especially the COPII and adaptor systems. They do not establish that all module genes form one physical complex; the module is better viewed as a co-abundance network containing several connected trafficking and cellular-maintenance subsystems.

**STRING interactions (score >= 0.7)**: 14 of 351 gene pairs: AARS1–VARS1 (0.938); AP1B1–AP2B1 (0.819); AP1B1–DNM2 (0.717); AP2B1–DNM2 (0.759); COPB1–SEC24C (0.714); COPB1–USO1 (0.869); CSE1L–TNPO1 (0.824); DDX6–UPF1 (0.93); SEC23IP–SEC24C (0.737); SEC23IP–SEC24D (0.718); SEC24C–SEC24D (0.989); SEC24C–USO1 (0.761); SEC24D–USO1 (0.751); TNPO1–TNPO3 (0.974)
**STRING functional enrichment (supplementary, within-query FDR)**: InterPro Armadillo-like helical (FDR = 0.00082, 8 genes); Component Coated vesicle (FDR = 0.0039, 8 genes); Component Coated vesicle membrane (FDR = 0.0039, 7 genes); InterPro Armadillo-type fold (FDR = 0.0041, 8 genes); COMPARTMENTS Membrane coat (FDR = 0.0042, 6 genes); COMPARTMENTS Vesicle coat (FDR = 0.0042, 5 genes); Component Vesicle coat (FDR = 0.0049, 5 genes); Keyword Protein transport (FDR = 0.0059, 10 genes); COMPARTMENTS Golgi-associated vesicle (FDR = 0.0146, 5 genes); COMPARTMENTS Coated vesicle (FDR = 0.0146, 6 genes); COMPARTMENTS Transport vesicle (FDR = 0.0153, 5 genes); Component ER to Golgi transport vesicle membrane (FDR = 0.0225, 4 genes); Component Transport vesicle membrane (FDR = 0.0225, 5 genes); Keyword ER-Golgi transport (FDR = 0.0249, 4 genes); Process Intracellular protein transport (FDR = 0.0277, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12394.1 (USO1, SEC24D, SEC24C, AP2B1, AP1B1; 5/98); huMAP3_07775.1 (SEC24D, SEC24C, SEC23IP; 3/5); huMAP3_09282.1 (SEC24D, SEC24C, SEC23IP; 3/6); huMAP3_11128.1 (SEC24D, SEC24C, SEC23IP; 3/8); huMAP3_13535.1 (SEC24D, SEC24C, SEC23IP; 3/14); huMAP3_11232.1 (DNM2, TNPO1, TNPO3; 3/78); huMAP3_00065.1 (SEC24D, SEC23IP; 2/4); huMAP3_00707.1 (SEC24D, SEC24C; 2/4); huMAP3_06453.1 (SEC24D, SEC24C; 2/6); huMAP3_11237.1 (SEC24D, SEC24C; 2/12); huMAP3_08540.1 (AP2B1, AP1B1; 2/19); huMAP3_09107.1 (AP2B1, AP1B1; 2/23); huMAP3_08320.1 (AP2B1, AP1B1; 2/24); huMAP3_09053.1 (TNPO1, TNPO3; 2/25); huMAP3_09403.1 (AP2B1, AP1B1; 2/26); huMAP3_09042.1 (CSE1L, UNC45A; 2/26); huMAP3_12376.1 (AP2B1, AP1B1; 2/32); huMAP3_10876.1 (AP2B1, AP1B1; 2/40); huMAP3_14442.1 (AARS1, XPNPEP1; 2/57); huMAP3_10762.1 (AP2B1, AP1B1; 2/62); huMAP3_12918.1 (AP2B1, AP1B1; 2/62); huMAP3_09592.1 (CSE1L, TNPO1; 2/95)

### Novelty

The module should not be called a newly discovered molecular complex. Its central biological themes are established: COPII trafficking, coatomer function, clathrin adaptor activity, dynamin-dependent membrane remodeling, and nuclear transport are represented by well-characterized genes and are supported by STRING and hu.MAP. The apparent novelty is instead at the systems level: this particular conserved co-abundance combination across myometrium and testis, including a COPII-centered backbone connected to adaptor trafficking, transportin activity, RNA surveillance, translation machinery, and proteostasis genes, is not directly demonstrated by the supplied interaction resources as a previously defined unit. However, absence of a complete matching module from STRING or hu.MAP does not prove novelty, because those resources describe physical interactions or complexes rather than tissue-pair co-abundance patterns. A defensible conclusion is that the tissue-pair module may represent a new context-specific co-abundance organization of largely known cellular machinery, but confirmation would require independent cohorts, preservation testing, cell-composition adjustment, and comparison with published co-expression modules.

**Hypothesis.** Hypothesis: in both myometrium and testis, this module coordinates high-throughput intracellular cargo handling with cellular proteostasis. The SEC23IP–SEC24C–SEC24D–USO1–COPB1 axis may support ER export, COPII vesicle formation, delivery to the Golgi, and retrograde membrane traffic, while AP1B1, AP2B1, and DNM2 may connect this secretory pathway to post-Golgi sorting and endocytosis. Transportin genes, CSE1L, UPF1, and DDX6 could couple trafficking demand to nuclear transport and RNA quality control, whereas AARS1, VARS1, TIMM44, THOP1, and USP5 could reflect the translational, mitochondrial, peptide-processing, and ubiquitin-maintenance requirements of active cells. In testis, the signal may be amplified by differentiating germ cells and spermatids; in myometrium, it may reflect smooth-muscle and stromal cellular activity. This is a mechanistic model rather than a demonstrated causal pathway, and the co-abundance data do not establish directionality, physical binding, or tissue-specific regulation.

### Important genes

#### SEC24C

- **Related proteins** (co-abundance neighbors): DNM2 (0.89), UPF1 (0.86), VARS1 (0.85), TNPO3 (0.83), AP2B1 (0.83), UNC45A (0.83), CSE1L (0.81); STRING partners: COPB1 (0.714), SEC23IP (0.737), SEC24D (0.989), USO1 (0.761)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in myometrium, testis
- **hu.MAP 3.0**: huMAP3_12394.1, huMAP3_07775.1, huMAP3_09282.1, huMAP3_11128.1, huMAP3_13535.1, huMAP3_00707.1, huMAP3_06453.1, huMAP3_11237.1
- **Function (MyGene.info)**: SEC24 homolog C, COPII component. The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec24p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The product of this gene may play a role in shaping the vesicle, as well as in cargo selection and concentration.…
- **Diseases (Open Targets)**: 22q11.2 deletion syndrome (0.370); neurodegenerative disease (0.369); Alzheimer disease (0.281); lysosomal storage disease (0.274); Parkinson disease (0.274)
- **Europe PMC papers**: 693
- **Why important**: SEC24C is the most connected node in the supplied module network and is present in every globally corrected trafficking term (GO:CC coated vesicle; q_global = 0.00409) through (GO:BP establishment of protein localization; q_global = 0.045). It is a COPII component involved in vesicle budding, cargo selection, and ER-to-Golgi transport. It has STRING support with SEC24D, SEC23IP, COPB1, and USO1 and appears in numerous hu.MAP COPII complexes (hu.MAP huMAP3_12394.1) through (hu.MAP huMAP3_13535.1) and (hu.MAP huMAP3_00707.1) through (hu.MAP huMAP3_11237.1). Its protein is detected in both myometrium and testis, and it has substantial literature and disease-resource representation.
- **Conclusion**: Established: SEC24C is a central network and annotation anchor for the module's COPII and intracellular-transport interpretation. Hypothesis: its high co-abundance connectivity may mark a shared demand for regulated ER export in both tissues, although the data do not show that SEC24C controls the abundance of the other genes.

#### SEC24D

- **Related proteins** (co-abundance neighbors): USO1 (0.82), UGGT1 (0.81); STRING partners: SEC23IP (0.718), SEC24C (0.989), USO1 (0.751)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in myometrium, testis
- **hu.MAP 3.0**: huMAP3_12394.1, huMAP3_07775.1, huMAP3_09282.1, huMAP3_11128.1, huMAP3_13535.1, huMAP3_00065.1, huMAP3_00707.1, huMAP3_06453.1, huMAP3_11237.1
- **Function (MyGene.info)**: SEC24 homolog D, COPII component. The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec24p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. This gene product is implicated in the shaping of the vesicle, and also in cargo selection and concentration. Mut…
- **Diseases (Open Targets)**: Cole-Carpenter syndrome (0.753); hereditary disease (0.380); osteogenesis imperfecta type 1 (0.370); Seizure (0.259); Intellectual disability (0.259)
- **Europe PMC papers**: 780
- **Why important**: SEC24D is a core COPII cargo-selection component and is represented in every globally corrected term (GO:CC coated vesicle; q_global = 0.00409) through (GO:BP establishment of protein localization; q_global = 0.045). It is tightly connected to SEC24C and is linked to SEC23IP and USO1 by STRING. It recurs with SEC23IP and SEC24C across several hu.MAP complexes (hu.MAP huMAP3_12394.1) through (hu.MAP huMAP3_11237.1). Its established disease associations include Cole-Carpenter syndrome and osteogenesis imperfecta type one, making it biologically important beyond this module.
- **Conclusion**: Established: SEC24D provides strong molecular and complex-level support for an ER-to-Golgi trafficking backbone. Hypothesis: coordinated SEC24C and SEC24D abundance may tune cargo-selective export in tissue cells with substantial secretory or membrane-renewal demands; this requires experimental testing.

#### USO1

- **Related proteins** (co-abundance neighbors): COPB1 (0.85), TNPO3 (0.83), SEC24D (0.82), TNPO1 (0.81), AARS1 (0.81); STRING partners: COPB1 (0.869), SEC24C (0.761), SEC24D (0.751)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: USO1 vesicle transport factor. The protein encoded by this gene is a peripheral membrane protein which recycles between the cytosol and the Golgi apparatus during interphase. It is regulated by phosphorylation: dephosphorylated protein associates with the Golgi membrane and dissociates from the membrane upon phosphorylation. Ras-associated protein 1 recruits this protein to coat protein complex II (COPII) vesicles during buddin…
- **Diseases (Open Targets)**: psoriatic arthritis (0.184); bipolar disorder (0.150); retinitis pigmentosa (0.085); cone dystrophy (0.076); cone-rod dystrophy (0.076)
- **Europe PMC papers**: 546
- **Why important**: USO1 is a high-connectivity module node and a Golgi-localized vesicle-transport factor. It appears in nearly all of the specific globally corrected trafficking terms, including (GO:CC coated vesicle; q_global = 0.00409), (GO:BP intracellular protein transport; q_global = 0.00492), (GO:CC coated vesicle membrane; q_global = 0.0067), (GO:BP endoplasmic reticulum to Golgi vesicle-mediated transport; q_global = 0.0111), and (GO:CC ER to Golgi transport vesicle membrane; q_global = 0.041), and is linked to COPB1, SEC24C, and SEC24D by STRING. It is present in the large hu.MAP coated-vesicle complex (hu.MAP huMAP3_12394.1). USO1 is tissue enhanced in skeletal muscle, detected in testis, and has disease associations involving retinal and muscular or inflammatory phenotypes.
- **Conclusion**: Established: USO1 connects ER-derived vesicle traffic with Golgi organization and is a key bridge between the COPII and coatomer-related portions of the module. Hypothesis: USO1 may help explain why a trafficking module is conserved between a contractile tissue and a germ-cell-containing tissue, but the supplied data cannot distinguish cell-intrinsic regulation from shared cell composition.

#### DNM2

- **Related proteins** (co-abundance neighbors): SEC24C (0.89), SEC23IP (0.86), COPB1 (0.81); STRING partners: AP1B1 (0.717), AP2B1 (0.759)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in myometrium, testis
- **hu.MAP 3.0**: huMAP3_11232.1
- **Function (MyGene.info)**: dynamin 2. Dynamins represent one of the subfamilies of GTP-binding proteins. These proteins share considerable sequence similarity over the N-terminal portion of the molecule, which contains the GTPase domain. Dynamins are associated with microtubules. They have been implicated in cell processes such as endocytosis and cell motility, and in alterations of the membrane that accompany certain activities such …
- **Diseases (Open Targets)**: autosomal dominant centronuclear myopathy (0.844); Charcot-Marie-Tooth disease dominant intermediate B (0.830); fetal akinesia-cerebral and retinal hemorrhage syndrome (0.739); autosomal dominant Charcot-Marie-Tooth disease type 2M (0.715); centronuclear myopathy (0.692)
- **Europe PMC papers**: 2412
- **Why important**: DNM2 links the module's ER-to-Golgi neighborhood to coated-vesicle remodeling and endocytosis. It is connected in the module to SEC24C, SEC23IP, and COPB1, and STRING supports relationships with AP1B1 and AP2B1. It contributes to the primary coated-vesicle and cytosol terms (GO:CC coated vesicle; q_global = 0.00409) and (GO:CC cytosol; q_global = 0.0181) and to establishment of protein localization (GO:BP establishment of protein localization; q_global = 0.045). Dynamin two has extensive literature and established associations with centronuclear myopathy and Charcot-Marie-Tooth disease, which are relevant to membrane and cytoskeletal biology.
- **Conclusion**: Established: DNM2 is a plausible interface between secretory trafficking, endocytosis, and cytoskeletal membrane remodeling. Hypothesis: its position may indicate that the conserved module coordinates both export and retrieval of membrane cargo, rather than representing ER-to-Golgi transport alone.

#### AP2B1

- **Related proteins** (co-abundance neighbors): USP5 (0.85), SEC24C (0.83), COPB1 (0.82); STRING partners: AP1B1 (0.819), DNM2 (0.759)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_12394.1, huMAP3_08540.1, huMAP3_09107.1, huMAP3_08320.1, huMAP3_09403.1, huMAP3_12376.1, huMAP3_10876.1, huMAP3_10762.1, huMAP3_12918.1
- **Function (MyGene.info)**: adaptor related protein complex 2 subunit beta 1. The protein encoded by this gene is one of two large chain components of the assembly protein complex 2, which serves to link clathrin to receptors in coated vesicles. The encoded protein is found on the cytoplasmic face of coated vesicles in the plasma membrane. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: HIV infectious disease (0.551); dengue disease (0.375); peroxisome biogenesis disorder (0.186); peroxisome biogenesis disorder 3A (Zellweger) (0.186); mathematical ability (0.180)
- **Europe PMC papers**: 866
- **Why important**: AP2B1 is a large subunit of adaptor protein complex two and links receptors to clathrin-coated vesicles at the plasma membrane. It contributes to the globally corrected coated-vesicle, intracellular-transport, coated-vesicle-membrane, vesicle-coat, cytosol, and localization terms (GO:CC coated vesicle; q_global = 0.00409) through (GO:CC vesicle coat; q_global = 0.00764), (GO:CC cytosol; q_global = 0.0181), and (GO:BP establishment of protein localization; q_global = 0.045). It is connected to AP1B1, DNM2, COPB1, and SEC24C in the supplied evidence and recurs in many hu.MAP adaptor complexes (hu.MAP huMAP3_12394.1) and (hu.MAP huMAP3_08540.1) through (hu.MAP huMAP3_12918.1). HPA shows enrichment in late primary spermatocytes and late spermatids, providing a plausible tissue-cell context.
- **Conclusion**: Established: AP2B1 supports a coated-vesicle and endocytic component within the module and has particularly relevant germ-cell expression evidence. Hypothesis: AP2B1 may connect shared secretory-pathway activity to receptor recycling or endocytosis during germ-cell differentiation, but this cannot be inferred as a tissue-specific mechanism from co-abundance alone.

## Module 5

**Tissue pair**: myometrium and testis  
**Genes (24)**: ACO1, ANXA6, CANX, CAPN1, CAPN2, C9, DNM1L, F13A1, FERMT2, H6PD, GSN, GBE1, HSPA8, MYH11, NIBAN2, PFKM, PGM2, PLCD1, SEC23A, SEPTIN9, SNX4, STAT1, TARS1, VPS35

### Function

The module does not support a formally established GO or KEGG function because no term passed global multiple-testing correction. Its gene composition and network structure nevertheless suggest a coordinated cellular-maintenance module spanning intracellular proteostasis, membrane trafficking, cytoskeletal or adhesion regulation, calcium-sensitive proteolysis, mitochondrial organization, and carbohydrate metabolism. The strongest internal themes are calpain biology through CAPN1 and CAPN2, vesicle and endosomal trafficking through SEC23A, VPS35 and SNX4, actin or adhesion biology through FERMT2, ANXA6 and GSN, and glucose or glycogen handling through H6PD, GBE1, PGM2 and PFKM. These are functional interpretations of the member annotations and network, not globally significant enrichment results.

**Cell composition.** The module is predominantly intracellular and broadly expressed rather than a plasma-protein or secreted-protein module. HPA reports low tissue specificity for many members, low immune-cell specificity for most members, and only a small secreted subset: GSN, F13A1 and C9 are secreted to blood, while H6PD is classified as intracellular and membrane-associated. C9 is liver-enriched, absent in the sampled myometrium and testis protein detections, and F13A1 is associated with blood and myeloid or platelet cell types; these members could reflect circulating or sample-associated material rather than the core shared cellular program. The blood-cell signal is limited overall, although GSN, F13A1 and C9 provide plausible blood-related contributions. Several genes show liver, esophageal, adipose, skeletal-muscle, smooth-muscle, or reproductive-cell associations, so the shared signal may represent common structural and metabolic cell states rather than a tissue-exclusive program. Protein detection is extensive in both tissues, with stronger detection in testis than myometrium, but absence of detection for individual genes should not be treated as proof of biological absence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a focused set of high-confidence relationships rather than a connected annotation-enrichment result. The most direct known interaction is CAPN1 with CAPN2. The trafficking relationships DNM1L with VPS35 and SNX4 with VPS35 support links between mitochondrial or peroxisomal dynamics and endosomal-retromer biology. The metabolic relationships GBE1 with H6PD, GBE1 with PGM2, H6PD with PFKM, and H6PD with PGM2 support a carbohydrate-metabolism subnetwork. hu.MAP independently places CAPN1 and CAPN2 together in every listed qualifying complex, with CAPNS1 repeatedly present and CAPN8, CAST, FNTB, KDM8, LIX1L, WNT8B, CAPNS2 or SPDL1 appearing in specific complexes (hu.MAP huMAP3_03767.1) through (hu.MAP huMAP3_12926.1). Thus, the calpain pair is the clearest externally supported complex-like unit. Most other module edges are not represented by the supplied STRING or hu.MAP evidence, so the co-abundance network should not be interpreted as a physical protein complex. Instead, it appears to combine a known calpain unit, a known trafficking unit, a known metabolic neighborhood, and co-varying links among broadly expressed cellular processes.

**STRING interactions (score >= 0.7)**: 7 of 276 gene pairs: CAPN1–CAPN2 (0.978); DNM1L–VPS35 (0.9); GBE1–H6PD (0.712); GBE1–PGM2 (0.714); H6PD–PFKM (0.804); H6PD–PGM2 (0.936); SNX4–VPS35 (0.891)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03767.1 (CAPN1, CAPN2; 2/3); huMAP3_08670.1 (CAPN1, CAPN2; 2/4); huMAP3_09127.1 (CAPN1, CAPN2; 2/5); huMAP3_09328.1 (CAPN1, CAPN2; 2/6); huMAP3_10242.1 (CAPN1, CAPN2; 2/6); huMAP3_13615.1 (CAPN1, CAPN2; 2/7); huMAP3_14229.1 (CAPN1, CAPN2; 2/7); huMAP3_11557.1 (CAPN1, CAPN2; 2/8); huMAP3_12716.1 (CAPN1, CAPN2; 2/8); huMAP3_12926.1 (CAPN1, CAPN2; 2/8)

### Novelty

The module may be a new tissue-pair co-abundance observation, but novelty is not established as discovery of a new molecular complex or pathway. The CAPN1-CAPN2 relationship, the VPS35 trafficking relationships, and the H6PD-centered metabolic relationships are already represented in STRING, while the repeated CAPN1-CAPN2 complexes are represented in hu.MAP. The absence of hu.MAP or STRING support for many remaining edges indicates that those links may be context-specific, indirect, abundance-driven, or insufficiently characterized, but absence from those resources alone does not prove novelty. A defensible novelty claim is therefore that this particular coordinated abundance pattern is a potentially new shared signature of myometrium and testis, requiring replication in independent cohorts and testing against cellular composition, sex, developmental state, and technical covariates.

**Hypothesis.** Hypothesis: the module reflects a shared contractile or mechanically active cellular state in which integrin and actin-associated organization, calcium-sensitive calpain activity, endosomal recycling, ER protein handling, mitochondrial remodeling, and glucose or glycogen utilization are coordinated. FERMT2 and MYH11 could represent adhesion and smooth-muscle or myoid structural context; CAPN1 and CAPN2 could remodel cytoskeletal or adhesion substrates in response to calcium or mechanical input; SEC23A, VPS35 and SNX4 could maintain membrane and receptor trafficking; and H6PD, GBE1, PGM2 and PFKM could provide metabolic support. CANX and HSPA8 could buffer protein-folding and proteostasis demands, while DNM1L could couple the state to mitochondrial remodeling. This is a mechanistic model generated from co-abundance and known annotations, not a demonstrated causal pathway. A critical alternative is that the module partly reflects shared smooth-muscle, myoid, metabolic, or vascular-associated cell populations and, to a lesser extent, blood-derived proteins.

### Important genes

#### CAPN2

- **Related proteins** (co-abundance neighbors): TARS1 (0.92), CANX (0.91), SEC23A (0.90), H6PD (0.90), ACO1 (0.87), GSN (0.87), CAPN1 (0.84), VPS35 (0.83); STRING partners: CAPN1 (0.978)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Connecting piece, Mid piece; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_03767.1, huMAP3_08670.1, huMAP3_09127.1, huMAP3_09328.1, huMAP3_10242.1, huMAP3_13615.1, huMAP3_14229.1, huMAP3_11557.1, huMAP3_12716.1, huMAP3_12926.1
- **Function (MyGene.info)**: calpain 2. The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpa…
- **Diseases (Open Targets)**: Alzheimer disease (0.389); urolithiasis (0.288); alcohol drinking (0.288); aortic stenosis (0.141); neoplasm (0.105)
- **Europe PMC papers**: 1796
- **Why important**: CAPN2 is a high-connectivity module member linking TARS1, CANX, SEC23A, H6PD, ACO1, GSN, CAPN1 and VPS35. It encodes the large catalytic subunit of ubiquitous calpain two, an intracellular calcium-activated cysteine protease, and is annotated for proteolysis, response to mechanical stimulus and hypoxia-related processes. CAPN2 has the strongest direct STRING support in the module through CAPN1 and is present with CAPN1 across the hu.MAP complexes (hu.MAP huMAP3_03767.1) through (hu.MAP huMAP3_12926.1). Its literature record is extensive and its disease associations include neurodegenerative and other disease links.
- **Conclusion**: Established evidence supports CAPN2 as a central calpain component and a plausible regulator of mechanically responsive intracellular remodeling. Its role as the causal organizer of this shared module remains a hypothesis.

#### VPS35

- **Related proteins** (co-abundance neighbors): TARS1 (0.92), SEC23A (0.91), DNM1L (0.87), ANXA6 (0.85), FERMT2 (0.84), CAPN2 (0.83), CAPN1 (0.82), MYH11 (0.81); STRING partners: DNM1L (0.9), SNX4 (0.891)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS35 retromer complex component. This gene belongs to a group of vacuolar protein sorting (VPS) genes. The encoded protein is a component of a large multimeric complex, termed the retromer complex, involved in retrograde transport of proteins from endosomes to the trans-Golgi network. The close structural similarity between the yeast and human proteins that make up this complex suggests a similarity in function. Expression studie…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.743); neurodegenerative disease (0.553); young-onset Parkinson disease (0.503); Parkinson disease (0.482); Parkinson disease, dominant (0.370)
- **Europe PMC papers**: 3611
- **Why important**: VPS35 is a highly connected module member linked to TARS1, SEC23A, DNM1L, ANXA6, FERMT2, CAPN2, CAPN1 and MYH11. It is a retromer complex component involved in retrograde endosome-to-Golgi transport, lysosome organization, protein transport and regulation of mitochondrial organization. The STRING links to DNM1L and SNX4 provide direct external support for a trafficking subnetwork, and VPS35 has extensive literature and strong disease association with Parkinson disease and related neurodegenerative disorders.
- **Conclusion**: Established evidence supports VPS35 as a trafficking and organelle-organization anchor in the module. Its co-abundance with contractile, metabolic and calpain genes suggests coordinated cellular-state regulation, but does not establish direct physical interaction with those partners.

#### FERMT2

- **Related proteins** (co-abundance neighbors): PFKM (0.94), ANXA6 (0.89), CAPN1 (0.89), GSN (0.89), GBE1 (0.88), TARS1 (0.87), DNM1L (0.85), VPS35 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Focal adhesion sites; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FERM domain containing kindlin 2. Enables several functions, including actin binding activity; phosphatidylinositol-3,4,5-trisphosphate binding activity; and type I transforming growth factor beta receptor binding activity. Involved in several processes, including cell surface receptor signaling pathway; positive regulation of cell differentiation; and positive regulation of cellular component biogenesis. Acts upstream of or withi…
- **Diseases (Open Targets)**: open-angle glaucoma (0.501); prostate carcinoma (0.488); glaucoma (0.488); neurodegenerative disease (0.473); primary angle-closure glaucoma (0.407)
- **Europe PMC papers**: 1336
- **Why important**: FERMT2 has high network connectivity and links PFKM, ANXA6, CAPN1, GSN, GBE1, TARS1, DNM1L and VPS35. It encodes kindlin two, with actin-binding, phosphoinositide-binding and transforming-growth-factor-beta-receptor-related activities, and is annotated for cell adhesion, cell-matrix adhesion, integrin signaling and cell-junction localization. HPA places it in focal adhesion sites and identifies smooth-muscle, adipocyte and podocyte cell-type enhancement, with protein detected in both tissues. It has substantial literature and disease associations including glaucoma and prostate carcinoma.
- **Conclusion**: Established evidence supports FERMT2 as the strongest adhesion and cytoskeletal-context candidate in this module. Its position suggests that it may connect mechanical or matrix signals to trafficking and metabolism, but that integrative role is not directly demonstrated here.

#### H6PD

- **Related proteins** (co-abundance neighbors): SEC23A (0.92), CAPN2 (0.90), TARS1 (0.89), CANX (0.88), HSPA8 (0.84), ACO1 (0.83); STRING partners: GBE1 (0.712), PFKM (0.804), PGM2 (0.936)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hexose-6-phosphate dehydrogenase/glucose 1-dehydrogenase. There are 2 forms of glucose-6-phosphate dehydrogenase. G form is X-linked and H form, encoded by this gene, is autosomally linked. This H form shows activity with other hexose-6-phosphates, especially galactose-6-phosphate, whereas the G form is specific for glucose-6-phosphate. Both forms are present in most tissues, but H form is not found in red cells. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: cortisone reductase deficiency (0.735); Abnormality of the skeletal system (0.473); obesity disorder (0.364); stroke disorder (0.325); alcohol drinking (0.324)
- **Europe PMC papers**: 3634
- **Why important**: H6PD is centrally connected to SEC23A, CAPN2, TARS1, CANX, HSPA8 and ACO1, and has direct STRING relationships with GBE1, PFKM and PGM2. It encodes hexose-six-phosphate dehydrogenase, an enzyme associated with carbohydrate metabolism, the oxidative pentose-phosphate shunt and NADP-related metabolism. HPA reports liver tissue enhancement, hepatocyte and myonuclear cell-type enhancement, and protein detection in both tissues. Its literature is extensive and includes a strong association with cortisone reductase deficiency.
- **Conclusion**: Established evidence supports H6PD as a metabolic bridge within the module, especially between carbohydrate handling and ER or proteostasis-associated genes. Whether its activity drives the shared tissue-pair signature, rather than merely covarying with cellular energy demand, remains unresolved.

#### MYH11

- **Related proteins** (co-abundance neighbors): F13A1 (0.86), VPS35 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin heavy chain 11. The protein encoded by this gene is a smooth muscle myosin belonging to the myosin heavy chain family. The gene product is a subunit of a hexameric protein that consists of two heavy chain subunits and two pairs of non-identical light chain subunits. It functions as a major contractile protein, converting chemical energy into mechanical energy through the hydrolysis of ATP. A chromosomal rearrange…
- **Diseases (Open Targets)**: aortic aneurysm, familial thoracic 4 (0.762); megacystis-microcolon-intestinal hypoperistalsis syndrome 2 (0.757); familial thoracic aortic aneurysm and aortic dissection (0.715); visceral myopathy 2 (0.570); neurodegenerative disease (0.527)
- **Europe PMC papers**: 10247
- **Why important**: MYH11 has fewer module connections than the central hubs but is biologically informative because it connects VPS35 with F13A1. It encodes smooth-muscle myosin heavy chain, a contractile protein involved in smooth-muscle contraction, actomyosin organization and elastic-fiber assembly. HPA reports tissue enhancement in blood vessel, intestine and urinary bladder and group enrichment in peritubular myoid, smooth-muscle and vascular smooth-muscle cells. MYH11 has a very large literature base and established associations with thoracic aortic aneurysm, aortic dissection and visceral myopathy.
- **Conclusion**: Established evidence supports MYH11 as a marker of smooth-muscle or myoid structural context and therefore as an important clue to the shared cellular composition of the tissues. Its sparse network connectivity argues against treating it as the molecular hub of the module, while its presence supports a contractile-cell interpretation.

#### CANX

- **Related proteins** (co-abundance neighbors): CAPN2 (0.91), ANXA6 (0.91), SEC23A (0.89), H6PD (0.88), TARS1 (0.86), HSPA8 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX connects CAPN2, ANXA6, SEC23A, H6PD, TARS1 and HSPA8. It encodes the ER calcium-binding chaperone calnexin, which supports folding and assembly of newly synthesized glycoproteins and ER quality control. HPA reports detection in both tissues and enrichment in late spermatids, making it particularly relevant to the shared reproductive-tissue context. CANX has extensive literature and disease associations involving neurodegenerative and infectious disease processes.
- **Conclusion**: Established evidence supports CANX as a proteostasis and ER-quality-control component that could link secretory processing with metabolic and trafficking demands. Its contribution to the module may reflect general cellular protein-handling requirements rather than a tissue-pair-specific mechanism.

## Module 6

**Tissue pair**: myometrium and testis  
**Genes (7)**: ACO2, ACSL1, HSPA5, GARS1, HSP90AA1, KATNAL2, PDIA4

### Function

This is a heterogeneous, conserved co-abundance module rather than a clearly defined canonical pathway. Its genes span endoplasmic-reticulum protein folding and stress control, mitochondrial energy metabolism, protein translation, microtubule organization, and long-chain fatty-acid activation. HSPA5 and PDIA4 provide the clearest functional connection through ER proteostasis, while ACO2, GARS1, KATNAL2, and ACSL1 represent mitochondrial, translational, cytoskeletal, and lipid-metabolic functions respectively. No GO or KEGG term passed global correction, so the pathway interpretation remains hypothesis-generating rather than statistically established. The network may therefore reflect shared cellular state, protein-production demand, or tissue and cell-type composition rather than one unified biochemical pathway.

**Cell composition.** The module is not predominantly composed of plasma or extracellular proteins: the individual annotations mainly describe intracellular, ER, mitochondrial, cytosolic, vesicular, or structural locations, although the HPA summary reports several secreted genes. Most genes have low immune-cell specificity, and only ACSL1 is specifically associated with neutrophils; KATNAL2 is not detected in immune cells. The module includes genes associated with epididymal principal cells, plasma cells, trophoblast-related cells, muscle tissues, liver, adipose tissue, and other cell types, indicating broad and mixed cellular representation. Protein detection is widespread in testis and present for most genes in myometrium, which supports a real tissue-level signal but does not establish that the same cell population drives it in both tissues. The shared module could partly reflect common cell types or general cellular activity in the samples.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports two known relationships within the module: HSPA5 with PDIA4 and HSPA5 with HSP90AA1. These links connect ER protein folding and chaperone biology and make HSPA5 the main molecular bridge between the best-supported interaction relationships. The remaining co-abundance relationships, including those involving ACO2, GARS1, KATNAL2, and ACSL1, are not represented by the reported high-confidence STRING interactions. No hu.MAP complex contains multiple module members. Thus, the network has a limited known interaction backbone but is not a known multiprotein complex.

**STRING interactions (score >= 0.7)**: 2 of 21 gene pairs: HSP90AA1–HSPA5 (0.968); HSPA5–PDIA4 (0.99)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The conserved co-abundance pattern across myometrium and testis may be a new systems-level observation, particularly because most within-module relationships are not supported by the reported STRING interactions and no multi-member hu.MAP complex was identified. However, absence from STRING or hu.MAP does not prove biological novelty: co-abundance can arise from shared regulation, cell composition, protein abundance, stress state, or indirect metabolic coupling. The lack of globally significant GO or KEGG enrichment also prevents claiming discovery of a new pathway. The most defensible conclusion is that this is a potentially novel tissue-shared co-abundance module whose mechanistic novelty requires independent validation.

**Hypothesis.** Hypothesis: the module reflects a shared cellular adaptation involving protein-folding capacity, energy production, translation, cytoskeletal organization, and lipid handling. ER chaperone activity involving HSPA5 and PDIA4 could be coordinated with mitochondrial metabolism through ACO2 and with translational demand through GARS1, while KATNAL2 and ACSL1 capture structural and lipid-metabolic aspects of the same cellular state. In testis, this state may be particularly influenced by epididymal or spermatogenic cell populations; in myometrium, it may reflect smooth-muscle or other metabolically active cells. This model predicts that the co-abundance pattern should track cellular stress, biosynthetic demand, and cell-type proportions, but it should not be treated as established without perturbation or cell-resolved validation.

### Important genes

#### HSPA5

- **Related proteins** (co-abundance neighbors): ACO2 (0.91), GARS1 (0.84), PDIA4 (0.83); STRING partners: HSP90AA1 (0.968), PDIA4 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is the most informative network bridge for the known interaction evidence, connecting PDIA4 and HSP90AA1. It is an ER chaperone and regulator of ER homeostasis, is detected in both tissues, and has broad literature and disease relevance. Its cell-type associations include epididymal cells, trophoblast-related cells, and plasma cells, making it relevant both to the tissue comparison and to possible cell-composition effects.
- **Conclusion**: Established: HSPA5 supports ER folding and homeostasis and has known STRING relationships with PDIA4 and HSP90AA1. Hypothesis: it may coordinate a proteostasis component of the shared module and connect this component to broader cellular stress or biosynthetic demand.

#### PDIA4

- **Related proteins** (co-abundance neighbors): ACO2 (0.84), HSPA5 (0.83), GARS1 (0.83), KATNAL2 (0.83); STRING partners: HSPA5 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 has the strongest network position in the module and is directly connected to HSPA5 in STRING. It is an ER protein-disulfide isomerase with catalytic thioredoxin domains and functions in protein folding, secretion, and ER-stress responses. It is detected in both tissues and has substantial literature support.
- **Conclusion**: Established: PDIA4 is an ER folding and disulfide-bond catalyst with a known relationship to HSPA5. Hypothesis: PDIA4 may mark increased secretory or folding load in the shared tissue state, but the module does not establish that PDIA4 drives the other genes.

#### ACO2

- **Related proteins** (co-abundance neighbors): GARS1 (0.92), HSPA5 (0.91), PDIA4 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aconitase 2. The protein encoded by this gene belongs to the aconitase/IPM isomerase family. It is an enzyme that catalyzes the interconversion of citrate to isocitrate via cis-aconitate in the second step of the TCA cycle. This protein is encoded in the nucleus and functions in the mitochondrion. It was found to be one of the mitochondrial matrix proteins that are preferentially degraded by the serine proteas…
- **Diseases (Open Targets)**: infantile cerebellar-retinal degeneration (0.814); optic atrophy 9 (0.693); autosomal dominant optic atrophy, classic form (0.619); optic atrophy (0.601); mitochondrial disease (0.505)
- **Europe PMC papers**: 3559
- **Why important**: ACO2 occupies a strongly connected position in the co-abundance graph and links to GARS1, HSPA5, and PDIA4, despite lacking a reported STRING partner within the module. It catalyzes a central step of the mitochondrial TCA cycle and is tissue-enhanced in heart muscle, skeletal muscle, and tongue, consistent with a role in energy-demanding cells. It also has substantial disease literature concerning mitochondrial and optic disorders.
- **Conclusion**: Established: ACO2 is a mitochondrial metabolic enzyme involved in citrate-to-isocitrate conversion and precursor-energy generation. Hypothesis: its co-abundance with ER and translation genes may reflect coordinated energy supply for protein synthesis or cellular maintenance rather than a direct physical interaction.

#### GARS1

- **Related proteins** (co-abundance neighbors): ACO2 (0.92), HSPA5 (0.84), PDIA4 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycyl-tRNA synthetase 1. This gene encodes glycyl-tRNA synthetase, one of the aminoacyl-tRNA synthetases that charge tRNAs with their cognate amino acids. The encoded enzyme is an (alpha)2 dimer which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Two transcript variants encoding different isoforms ha…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease type 2D (0.790); neuronopathy, distal hereditary motor, type 5A (0.729); neuronopathy, distal hereditary motor, type 5 (0.698); spinal muscular atrophy, infantile, James type (0.649); Charcot-Marie-Tooth disease type 2 (0.565)
- **Europe PMC papers**: 302
- **Why important**: GARS1 is centrally connected to ACO2, HSPA5, and PDIA4. It encodes glycyl-tRNA synthetase and therefore represents the protein-translation component of the module. Its association with autoimmune myositis and inherited peripheral neuropathies provides disease relevance, although its literature volume is smaller than that of the major chaperone genes.
- **Conclusion**: Established: GARS1 charges glycine tRNAs and participates in cytosolic and mitochondrial translation-related processes. Hypothesis: its co-abundance with ER chaperones and mitochondrial metabolism may indicate coordinated translational and proteostatic demand.

#### KATNAL2

- **Related proteins** (co-abundance neighbors): PDIA4 (0.83), HSP90AA1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: katanin catalytic subunit A1 like 2. Predicted to enable microtubule-severing ATPase activity. Predicted to be involved in cytoplasmic microtubule organization. Located in cytoplasm; microtubule; and spindle pole. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.306); cardiovascular disorder (0.176); alcohol drinking (0.139); hereditary disease (0.118); stroke disorder (0.113)
- **Europe PMC papers**: 340
- **Why important**: KATNAL2 connects the ER-associated portion of the network through PDIA4 and HSP90AA1 and is tissue-enhanced in testis. It is predicted to mediate microtubule severing and cytoplasmic microtubule organization, with cell-type associations including late primary spermatocytes and other specialized epithelial or neural cell types. It is therefore important for interpreting the testis-shared aspect of the module.
- **Conclusion**: Established: KATNAL2 is predicted to participate in microtubule organization and microtubule severing and is associated with testis-related cell populations. Hypothesis: it may connect cytoskeletal remodeling or germ-cell organization to the proteostasis state represented by HSPA5 and PDIA4.

#### ACSL1

- **Related proteins** (co-abundance neighbors): HSP90AA1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 1. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. Several transcript variants enco…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.510); diabetes mellitus (0.501); diabetic neuropathy (0.404); neurodegenerative disease (0.368); menopause (0.334)
- **Europe PMC papers**: 4992
- **Why important**: ACSL1 is a peripheral module member connected to HSP90AA1 and is tissue-enhanced in adipose tissue, liver, and skeletal muscle. It activates long-chain fatty acids for lipid biosynthesis and degradation. Its enrichment in neutrophils and immune-cell specificity distinguishes it from the other largely low-immune-specificity genes and makes it important for evaluating possible sample-composition effects.
- **Conclusion**: Established: ACSL1 participates in long-chain fatty-acid metabolism and is associated with neutrophils as well as metabolically active tissues. Hypothesis: ACSL1 may reflect lipid and inflammatory cell-state contributions to the module, but its peripheral network position argues against treating it as the core driver.

## Module 7

**Tissue pair**: myometrium and testis  
**Genes (5)**: ADK, HNRNPK, HNRNPL, EIF5, PTBP1

### Function

The strongest interpretation is regulation of pre-mRNA processing and alternative splicing. All primary globally significant GO evidence converges on this function: regulation of mRNA splicing via the spliceosome (GO:BP regulation of mRNA splicing, via spliceosome; q_global = 0.0104), regulation of mRNA processing (GO:BP regulation of mRNA processing; q_global = 0.0133), and regulation of RNA splicing (GO:BP regulation of RNA splicing; q_global = 0.0401). The shared core is HNRNPK, HNRNPL, and PTBP1, which are all annotated as nuclear RNA-binding proteins involved in mRNA processing and splicing. The network structure supports a coordinated RNA-regulatory module: HNRNPK connects directly with HNRNPL, PTBP1, and EIF5, while PTBP1 also connects with ADK. EIF5 adds a translation-initiation component, and ADK adds purine and adenosine metabolism, suggesting that the module may couple RNA processing with downstream translation and nucleotide-state regulation. The STRING supplementary results are consistent with mRNA splicing, post-transcriptional regulation, translation-related RNA control, and RNA-binding-protein biology (4 supplementary STRING terms; within-query FDR 0.00079–0.0157). The viral-translation and cancer-related STRING literature terms (10 supplementary STRING terms; within-query FDR 0.0097–0.0328) should be interpreted as contextual associations with RNA regulation rather than as evidence that this tissue module specifically performs antiviral or cancer functions.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and all members have low immune-cell specificity. It therefore does not resemble a blood-contamination module. The composition is instead dominated by broadly expressed, housekeeping-like intracellular RNA and translation regulators. HNRNPK, HNRNPL, PTBP1, and EIF5 have low tissue specificity, while ADK is tissue enhanced in liver and cell-type enhanced in Sertoli cells. EIF5 is cell-type enhanced in late spermatids, and HNRNPL has enhancement in several neural and renal cell types. Protein detection in both myometrium and testis is consistent with a shared intracellular program, although ADK was detected in testis but not myometrium. The shared co-abundance signal may therefore reflect a common basal RNA-processing program present in cells of both tissues, with possible contributions from testicular germ-cell or Sertoli-cell biology, rather than a tissue-exclusive secretory or immune process.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulation of mRNA splicing, via spliceosome | 0.0104 | HNRNPK, HNRNPL, PTBP1 |
| GO:BP regulation of mRNA processing | 0.0133 | HNRNPK, HNRNPL, PTBP1 |
| GO:BP regulation of RNA splicing | 0.0401 | HNRNPK, HNRNPL, PTBP1 |

### STRING and hu.MAP

STRING provides strong known pairwise support for the central RNA-binding-protein core: HNRNPK is connected with HNRNPL and PTBP1, and HNRNPL is connected with PTBP1. These relationships are concordant with the primary GO interpretation and indicate that the central part of the module is not merely a statistical co-abundance pattern. EIF5 and ADK do not have qualifying STRING partners within the supplied gene set, so their module links should be treated as less independently established. hu.MAP places HNRNPK and HNRNPL together in two large RNA-associated complexes (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_10625.1). These complexes contain many additional heterogeneous nuclear ribonucleoproteins, RNA-binding proteins, RNA helicase or RNA-processing factors, and translation-related regulators. Thus, hu.MAP supports membership in established multiprotein RNA-regulatory assemblies, but it does not establish that every gene in this co-abundance module forms one physical complex. The STRING and hu.MAP evidence together supports a known molecular neighborhood centered on HNRNPK, HNRNPL, and PTBP1, with EIF5 and ADK as peripheral functional links.

**STRING interactions (score >= 0.7)**: 3 of 10 gene pairs: HNRNPK–HNRNPL (0.99); HNRNPK–PTBP1 (0.997); HNRNPL–PTBP1 (0.993)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Multisystem proteinopathy, and HnRNP-L/PTB (FDR = 0.00079, 3 genes); PMID (2023) Structural diversity and biological role of the 5 untranslated regions of picornavirus. (FDR = 0.0097, 4 genes); PMID (2022) RNA-Binding Proteins as Regulators of Internal Initiation of Viral mRNA Translation. (FDR = 0.0098, 4 genes); Process Negative regulation of mRNA splicing, via spliceosome (FDR = 0.0103, 3 genes); PMID (2021) The regulation of protein translation and its implications for cancer. (FDR = 0.0118, 4 genes); PMID (2019) Mammalian RNA switches: Molecular rheostats in gene regulation, disease, and medicine. (FDR = 0.0118, 4 genes); WikiPathways mRNA processing (FDR = 0.0118, 3 genes); PMID (2022) Internal Ribosome Entry Site (IRES)-Mediated Translation and Its Potential for Novel mRNA-Based Therapy Development. (FDR = 0.0119, 4 genes); PMID (2013) Post-transcriptional regulatory networks in immunity. (FDR = 0.0157, 4 genes); PMID (2024) CircPPAP2B controls metastasis of clear cell renal cell carcinoma via HNRNPC-dependent alternative splicing and targeting the miR-182-5pCYP1B1 axis. (FDR = 0.0328, 3 genes); PMID (2023) Long Noncoding RNAs and Cancer Stem Cells: Dangerous Liaisons Managing Cancer. (FDR = 0.0328, 3 genes); PMID (2023) CD22 Exon 12 Deletion as an Independent Predictor of Poor Treatment Outcomes in B-ALL. (FDR = 0.0328, 3 genes); PMID (2023) TDP-43 and other hnRNPs regulate cryptic exon inclusion of a key ALSFTD risk gene, UNC13A. (FDR = 0.0328, 3 genes); PMID (2023) Dnmt3bas coordinates transcriptional induction and alternative exon inclusion to promote catalytically active Dnmt3b expression. (FDR = 0.0328, 3 genes); PMID (2023) Lnc-ZEB2-19 Inhibits the Progression and Lenvatinib Resistance of Hepatocellular Carcinoma by Attenuating the NF-kappaB Signaling Pathway through the TRA2ARSPH14 Axis. (FDR = 0.0328, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10659.1 (HNRNPL, HNRNPK; 2/28); huMAP3_10625.1 (HNRNPL, HNRNPK; 2/57)

### Novelty

The molecular components and the central HNRNP and PTBP1 relationships are established biology, so the module should not be presented as a newly discovered splicing complex. What may be novel is the conserved co-abundance pattern linking this RNA-processing core with EIF5 and ADK across myometrium and testis. The supplied STRING and hu.MAP results provide prior evidence for only part of the module, while EIF5 and ADK lack qualifying STRING partners and hu.MAP complex assignments in this module. This pattern is therefore best described as a potentially new tissue-pair co-abundance configuration built around a known RNA-regulatory core. A claim of discovery would require independent replication, comparison with published tissue co-expression modules, and ideally perturbation or physical-interaction evidence. Absence from STRING or hu.MAP alone is not evidence of novelty.

**Hypothesis.** Hypothesis: in both myometrium and testis, a broadly expressed nuclear RNA-regulatory program centered on HNRNPK, HNRNPL, and PTBP1 coordinates alternative splicing and mRNA processing, while EIF5 links this regulation to translation initiation and ADK links it to adenosine and purine-nucleotide metabolism. The shared co-abundance signal may reflect coordinated control of transcript maturation, translation competence, and cellular nucleotide state. In testis, the association could be strengthened by Sertoli-cell and late-spermatid programs, whereas in myometrium it may represent a general intracellular RNA-processing requirement. This is a mechanistic proposal rather than an established causal pathway; the data do not demonstrate direct regulation among all five genes or prove that the module has the same cellular origin in both tissues.

### Important genes

#### HNRNPK

- **Related proteins** (co-abundance neighbors): EIF5 (0.89), PTBP1 (0.88), HNRNPL (0.83); STRING partners: HNRNPL (0.99), PTBP1 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium, testis
- **hu.MAP 3.0**: huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is the most connected central node in the supplied subgraph, linking the two other primary splicing regulators and EIF5. It appears in every primary GO term (GO:BP regulation of mRNA splicing, via spliceosome; q_global = 0.0104) (GO:BP regulation of mRNA processing; q_global = 0.0133) (GO:BP regulation of RNA splicing; q_global = 0.0401), both hu.MAP complexes (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_10625.1), and the main STRING-supported RNA-regulatory associations. Its annotation describes a broadly expressed nuclear RNA-binding protein involved in pre-mRNA processing, RNA metabolism, transcriptional regulation, and nucleocytoplasmic shuttling. It has extensive literature coverage and disease associations including Au-Kline syndrome, neurodevelopmental disease, neurodegenerative disease, and dengue disease.
- **Conclusion**: Established conclusion: HNRNPK is a strong central candidate for the module's RNA-processing function and is supported by network position, primary enrichment, complex membership, and functional annotation. Hypothesis: changes in HNRNPK abundance could help coordinate the shared splicing program across myometrium and testis, but causality is not demonstrated.

#### PTBP1

- **Related proteins** (co-abundance neighbors): HNRNPK (0.88), ADK (0.82), HNRNPL (0.80); STRING partners: HNRNPK (0.997), HNRNPL (0.993)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypyrimidine tract binding protein 1. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA-binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.505); dengue disease (0.372); open-angle glaucoma (0.330); glaucoma (0.309); neoplasm (0.116)
- **Europe PMC papers**: 4849
- **Why important**: PTBP1 is a highly connected core node linked to HNRNPK, HNRNPL, and ADK, and it appears in every primary GO term (GO:BP regulation of mRNA splicing, via spliceosome; q_global = 0.0104) (GO:BP regulation of mRNA processing; q_global = 0.0133) (GO:BP regulation of RNA splicing; q_global = 0.0401). Its annotation specifically emphasizes alternative mRNA splicing, mRNA processing, and regulation of RNA splicing. It is also represented across the STRING supplementary evidence, including post-transcriptional regulation, RNA-binding-protein biology, and disease-related splicing literature (5 supplementary STRING terms; within-query FDR 0.00079–0.0328). PTBP1 has extensive literature coverage and disease associations involving neurodevelopmental disease, dengue disease, glaucoma, and neoplasm.
- **Conclusion**: Established conclusion: PTBP1 is a principal functional marker of the module's splicing interpretation and a likely bridge between the central HNRNP core and the peripheral ADK association. Hypothesis: PTBP1 may help transmit tissue-state signals into alternative-splicing choices, but the co-abundance data cannot identify its specific RNA targets.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): HNRNPK (0.83), PTBP1 (0.80); STRING partners: HNRNPK (0.99), PTBP1 (0.993)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium, testis
- **hu.MAP 3.0**: huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is part of the fully connected central trio with HNRNPK and PTBP1 and appears in every primary GO term (GO:BP regulation of mRNA splicing, via spliceosome; q_global = 0.0104) (GO:BP regulation of mRNA processing; q_global = 0.0133) (GO:BP regulation of RNA splicing; q_global = 0.0401). It is assigned to both hu.MAP RNA-associated complexes (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_10625.1) and has strong STRING relationships with the other two core regulators. Its annotation describes a stable hnRNP component involved in the formation, packaging, processing, and function of messenger RNA. HNRNPL also has broad representation in the supplementary STRING evidence and has substantial literature coverage, with disease associations including dengue disease, neuromuscular disease, and cancer.
- **Conclusion**: Established conclusion: HNRNPL reinforces that the module represents an established hnRNP-centered RNA-processing neighborhood rather than an isolated correlation. Hypothesis: HNRNPL may provide structural or substrate-selective organization within the shared splicing program, but this role requires direct molecular validation.

#### EIF5

- **Related proteins** (co-abundance neighbors): HNRNPK (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 5. Eukaryotic translation initiation factor-5 (EIF5) interacts with the 40S initiation complex to promote hydrolysis of bound GTP with concomitant joining of the 60S ribosomal subunit to the 40S initiation complex. The resulting functional 80S ribosomal initiation complex is then active in peptidyl transfer and chain elongations (summary by Si et al., 1996 [PubMed 8663286]).[supplied by OMIM, May 201…
- **Diseases (Open Targets)**: knee fracture (0.219); hair color (0.161); Abnormality of the skeletal system (0.103); liver disorder (0.088); hypertensive disorder (0.079)
- **Europe PMC papers**: 1989
- **Why important**: EIF5 is a peripheral module node connected to HNRNPK and is the clearest link to cytoplasmic translation initiation. Its annotation supports formation of the translation-initiation complex, translational initiation, regulation of initiation, and ribosome assembly. It is not present in the primary GO terms, but it recurs in supplementary STRING literature relating RNA-binding proteins to internal initiation, viral mRNA translation, translation regulation, immunity, and cancer (6 supplementary STRING terms; within-query FDR 0.0097–0.0328). HPA identifies late spermatids as a cell type with enhanced EIF5 expression, which is relevant to the testis side of the tissue pair.
- **Conclusion**: Established conclusion: EIF5 supplies a plausible translation-related extension to the core RNA-processing module and has a testis-relevant cell-type association. Hypothesis: EIF5 may couple splicing or transcript maturation to translation readiness in this module, but its direct physical or regulatory connection to HNRNPK is not independently established here.

#### ADK

- **Related proteins** (co-abundance neighbors): PTBP1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenosine kinase. This gene an enzyme which catalyzes the transfer of the gamma-phosphate from ATP to adenosine, thereby serving as a regulator of concentrations of both extracellular adenosine and intracellular adenine nucleotides. Adenosine has widespread effects on the cardiovascular, nervous, respiratory, and immune systems and inhibitors of the enzyme could play an important pharmacological role in increasing …
- **Diseases (Open Targets)**: adenosine kinase deficiency (0.780); autosomal recessive non-syndromic intellectual disability (0.370); neurodegenerative disease (0.320); hypertensive disorder (0.294); essential hypertension (0.287)
- **Europe PMC papers**: 5244
- **Why important**: ADK is a peripheral node connected to PTBP1 and is the only module member with tissue-enhanced HPA expression, namely in liver, while also being cell-type enhanced in Sertoli cells. Its annotation identifies adenosine kinase as a regulator of extracellular adenosine and intracellular adenine-nucleotide pools through purine salvage. ADK is not present in the primary GO terms and has no qualifying STRING partner in the supplied network, but it appears in supplementary evidence concerning RNA switches and post-transcriptional regulation (STRING PMID (2019) Mammalian RNA switches: Molecular rheostats in gene regulation, disease, and medicine.; within-query FDR = 0.0118). It has extensive literature coverage and disease associations including adenosine kinase deficiency, intellectual disability, neurodegenerative disease, and hypertension.
- **Conclusion**: Established conclusion: ADK is a biologically meaningful peripheral component that connects nucleotide and adenosine metabolism with the core RNA-regulatory program, and its Sertoli-cell association is relevant to testis. Hypothesis: ADK-dependent metabolic state may influence PTBP1-associated RNA regulation or translation indirectly through nucleotide and adenosine signaling, but this proposed coupling is not demonstrated by the module data.

## Module 8

**Tissue pair**: myometrium and testis  
**Genes (21)**: AKR1B1, RNPEP, CALD1, CDK5RAP3, CNN1, CPNE3, DPYSL2, GALK1, GPX3, PDLIM3, PGM1, PLS3, ATIC, RDX, RECQL, CTTN, NARS1, SARS1, TAGLN2, NAE1, WDR1

### Function

No GO or KEGG term passed global correction. Therefore, the module does not support a statistically established pathway assignment from enrichment. Its gene-level evidence instead suggests a composite cellular program linking actin and membrane-cytoskeleton organization with smooth-muscle contractile machinery, carbohydrate and purine metabolism, amino-acid charging, and genome-maintenance functions. CALD1 and CNN1 provide the clearest contractile axis, while PLS3, PDLIM3, CTTN, RDX, WDR1, DPYSL2, and TAGLN2 support actin remodeling, cell shape, adhesion, or membrane linkage. ATIC, PGM1, GALK1, and AKR1B1 indicate metabolic components, and NARS1, SARS1, RECQL, NAE1, and CDK5RAP3 indicate translation, genome stability, or cell-cycle-related components. This is best interpreted as a coordinated co-abundance signature rather than a single established biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: most members are intracellular proteins, and only GPX3 is clearly secreted to blood, while RNPEP has a secreted-unknown-location annotation. The HPA profile also argues against a strongly blood-cell-driven module: most genes have low immune-cell specificity, although selected genes show enrichment in neutrophils, monocyte or dendritic-cell populations, megakaryocytes, or platelets. The cell-type annotations are heterogeneous, with repeated representation of vascular smooth-muscle, trophoblast, epithelial, muscle, and spermatid-related cell types. This supports a possible shared structural or contractile cell component in the two tissues, while blood or contaminating immune-cell contributions cannot be excluded for individual genes. Protein detection is broadly consistent with the tissues for most members, but the absence of detection for selected genes, including GPX3 and TAGLN2, cautions against treating the whole module as a uniform tissue-resident protein complex.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a direct high-confidence relationship between CALD1 and CNN1 and another between NARS1 and SARS1. These relationships support a contractile actin submodule and an aminoacyl-tRNA-synthetase submodule, respectively, but the absence of other STRING relationships means that most co-abundance links are not established physical interactions in this resource. hu.MAP supports recurring pairwise membership in broader complexes: CALD1 with CTTN (hu.MAP huMAP3_06395.1) (hu.MAP huMAP3_10673.1), PLS3 with RDX (hu.MAP huMAP3_10281.1), NARS1 with RECQL (hu.MAP huMAP3_10088.1) (hu.MAP huMAP3_10115.1) (hu.MAP huMAP3_14982.1), and PLS3 with ATIC (hu.MAP huMAP3_14442.1). Because each listed complex contains only a small subset of the module, these results support convergence on cytoskeletal, regulatory, metabolic, and genome-associated machinery rather than one complete known complex. The network therefore appears to combine established local relationships with tissue-contextual co-abundance associations.

**STRING interactions (score >= 0.7)**: 2 of 210 gene pairs: CALD1–CNN1 (0.867); NARS1–SARS1 (0.843)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06395.1 (CALD1, CTTN; 2/8); huMAP3_10281.1 (PLS3, RDX; 2/9); huMAP3_10088.1 (NARS1, RECQL; 2/10); huMAP3_10673.1 (CALD1, CTTN; 2/14); huMAP3_10115.1 (NARS1, RECQL; 2/14); huMAP3_14982.1 (NARS1, RECQL; 2/28); huMAP3_14442.1 (PLS3, ATIC; 2/57)

### Novelty

The shared co-abundance module may represent a new tissue-pair-level observation, but the evidence does not establish a wholly new molecular mechanism. Its component functions and the CALD1-CNN1 and NARS1-SARS1 relationships are already biologically recognized, and several gene pairs recur in hu.MAP complexes. Conversely, the sparse STRING connectivity, partial hu.MAP overlap, absence of global GO or KEGG enrichment, and mixture of structural, metabolic, translation, and genome-maintenance genes suggest that this particular cross-tissue organization is not simply a canonical annotated complex. The appropriate conclusion is that the module-level association is potentially novel and hypothesis-generating, while novelty should be tested against independent myometrium and testis cohorts, cell-composition controls, and replication of the gene-level co-abundance pattern.

**Hypothesis.** Hypothesis: the module reflects a shared contractile and cytoskeletal state present in smooth-muscle-associated myometrium and selected structural or peritubular-cell populations in testis, coupled to the metabolic and proteostatic demands of those cells. CALD1 and CNN1 may anchor actin-linked contractile organization, with PDLIM3, PLS3, CTTN, RDX, WDR1, DPYSL2, and TAGLN2 coordinating filament architecture, membrane attachment, and remodeling. ATIC, PGM1, GALK1, and AKR1B1 may provide metabolic support, while NARS1, SARS1, RECQL, and NAE1 may reflect translational or genome-maintenance capacity. GPX3 could represent an extracellular oxidative-stress component or a blood-derived signal rather than a core intracellular member. This hypothesis predicts that the module should track contractile-cell abundance or state more strongly than a single pathway, and that its apparent sharing should diminish or change after correction for cell composition.

### Important genes

#### CALD1

- **Related proteins** (co-abundance neighbors): PDLIM3 (0.81); STRING partners: CNN1 (0.867)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Actin filaments; IHC detected in myometrium, testis
- **hu.MAP 3.0**: huMAP3_06395.1, huMAP3_10673.1
- **Function (MyGene.info)**: caldesmon 1. This gene encodes a calmodulin- and actin-binding protein that plays an essential role in the regulation of smooth muscle and nonmuscle contraction. The conserved domain of this protein possesses the binding activities to Ca(2+)-calmodulin, actin, tropomyosin, myosin, and phospholipids. This protein is a potent inhibitor of the actin-tropomyosin activated myosin MgATPase, and serves as a mediating…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.499); diaphragmatic hernia (0.447); glaucoma (0.405); diverticular disease (0.393); open-angle glaucoma (0.390)
- **Europe PMC papers**: 3386
- **Why important**: CALD1 is a central structural marker in the module's contractile interpretation. It is linked directly to CNN1 by STRING and occurs with CTTN in hu.MAP complexes (hu.MAP huMAP3_06395.1) (hu.MAP huMAP3_10673.1). Its annotated function directly connects calmodulin, actin, tropomyosin, myosin, phospholipids, and smooth-muscle contraction. It is detected in both tissues and has a substantial literature base, making it a strong bridge between the network signal and established contractile biology.
- **Conclusion**: Established evidence supports CALD1 as a contractile and actin-associated component of the module. It is reasonable to hypothesize that CALD1 helps define the shared structural-cell state, but the data do not prove that it physically organizes the entire module or that it drives the cross-tissue association.

#### CNN1

- **Related proteins** (co-abundance neighbors): PDLIM3 (0.84), GPX3 (0.82); STRING partners: CALD1 (0.867)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Actin filaments; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calponin 1. Predicted to enable actin binding activity. Involved in negative regulation of vascular associated smooth muscle cell proliferation. Located in cytoskeleton. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.356); self-injurious ideation (0.114); breast cancer (0.096); neoplasm (0.093); breast carcinoma (0.086)
- **Europe PMC papers**: 3024
- **Why important**: CNN1 is tissue-enhanced in blood vessel, intestine, and smooth muscle and is associated with actin organization, actomyosin structure, and regulation of smooth-muscle contraction. Its direct STRING relationship with CALD1 provides the clearest known interaction in the module. Its presence in vascular and peritubular myoid-related cell annotations makes it relevant to a shared contractile or contractile-supporting cell population.
- **Conclusion**: Established evidence supports CNN1 as a smooth-muscle and actin-filament component, with a known relationship to CALD1. Its co-abundance with the broader module is a hypothesis about shared cell state rather than evidence that all module members form one CNN1-centered complex.

#### PGM1

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.91), ATIC (0.88), WDR1 (0.86), NARS1 (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglucomutase 1. The protein encoded by this gene is an isozyme of phosphoglucomutase (PGM) and belongs to the phosphohexose mutase family. There are several PGM isozymes, which are encoded by different genes and catalyze the transfer of phosphate between the 1 and 6 positions of glucose. In most cell types, this PGM isozyme is predominant, representing about 90% of total PGM activity. In red cells, PGM2 is a majo…
- **Diseases (Open Targets)**: PGM1-congenital disorder of glycosylation (0.843); MPDU1-congenital disorder of glycosylation (0.551); developmental and epileptic encephalopathy, 36 (0.551); RFT1-congenital disorder of glycosylation (0.551); disorder of glycogen metabolism (0.506)
- **Europe PMC papers**: 3203
- **Why important**: PGM1 has relatively strong network connectivity and links the actin-associated and metabolic portions of the module through DPYSL2, ATIC, WDR1, and NARS1. It is group-enriched in skeletal muscle and tongue, detected in both tissues, and functions in glucose, glycogen, glycolytic, gluconeogenic, and galactose-related metabolism. Its disease associations include PGM1-related congenital glycosylation and glycogen-metabolism disorders, and it has substantial literature support.
- **Conclusion**: Established evidence supports PGM1 as a metabolic component that could supply carbohydrate-processing capacity to the shared cellular state. A coupling between PGM1 abundance and contractile-cell remodeling is plausible but remains a hypothesis because no globally significant pathway term or physical complex connects these functions here.

#### ATIC

- **Related proteins** (co-abundance neighbors): PGM1 (0.88), NARS1 (0.87), SARS1 (0.86), NAE1 (0.85), GALK1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, testis
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: 5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase. This gene encodes a bifunctional protein that catalyzes the last two steps of the de novo purine biosynthetic pathway. The N-terminal domain has phosphoribosylaminoimidazolecarboxamide formyltransferase activity, and the C-terminal domain has IMP cyclohydrolase activity. A mutation in this gene results in AICA-ribosiduria. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: AICA-ribosiduria (0.708); cancer (0.571); Intellectual disability (0.463); lung adenocarcinoma (0.390); anaplastic large cell lymphoma (0.374)
- **Europe PMC papers**: 5200
- **Why important**: ATIC is among the more connected nodes and links PGM1, NARS1, SARS1, NAE1, and GALK1. It catalyzes the final steps of de novo purine biosynthesis, is detected in both tissues, and has disease associations including AICA-ribosiduria and several malignancy or neurodevelopmental categories. Its hu.MAP co-membership with PLS3 (hu.MAP huMAP3_14442.1) gives it a potential connection between purine metabolism and cytoskeletal biology, although the complex contains many additional proteins.
- **Conclusion**: Established evidence supports ATIC as a purine-biosynthetic enzyme and a network bridge. Its position suggests a possible metabolic-support role in the module, but the proposed link to actin remodeling is inferential and should not be treated as an established mechanism.

#### NARS1

- **Related proteins** (co-abundance neighbors): CTTN (0.87), ATIC (0.87), PGM1 (0.82); STRING partners: SARS1 (0.843)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, testis
- **hu.MAP 3.0**: huMAP3_10088.1, huMAP3_10115.1, huMAP3_14982.1
- **Function (MyGene.info)**: asparaginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids.  Asparaginyl-tRNA synthetase is localized to the cytoplasm and belongs to the class II family of tRNA synthetases.  The N-terminal domain represents the signature sequence for the eukaryotic asparaginyl-tRNA synthetases. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, impaired language, and gait abnormalities (0.762); neurodevelopmental disorder with microcephaly, impaired language, epilepsy, and gait abnormalities (0.679); neurodevelopmental disorder (0.567); complex neurodevelopmental disorder (0.462); developmental disability (0.340)
- **Europe PMC papers**: 216
- **Why important**: NARS1 is a highly connected bridge among CTTN, ATIC, and PGM1 and has a direct STRING relationship with SARS1. It is represented in several hu.MAP complexes with RECQL (hu.MAP huMAP3_10088.1) (hu.MAP huMAP3_10115.1) (hu.MAP huMAP3_14982.1). Asparaginyl-tRNA synthetase supports cytoplasmic translation and aminoacyl-tRNA charging, and it is detected in both tissues. The combination of network bridging, known interaction with SARS1, and complex recurrence makes it informative despite a smaller disease-literature footprint than several structural genes.
- **Conclusion**: Established evidence supports NARS1 as a translational component with known association to SARS1 and recurring complex context with RECQL. Its central placement may indicate a general biosynthetic or growth-state contribution to the module, but it does not establish a specialized reproductive-tissue function.

## Module 9

**Tissue pair**: myometrium and testis  
**Genes (8)**: ANXA5, BAX, CBR1, ENOPH1, IAH1, SCRN1, TIPRL, TMX1

### Function

This is a small, sparse co-abundance module without a statistically supported canonical pathway. No GO/KEGG term passed global correction, and there are no supplementary STRING enrichment terms. The annotations nevertheless point to several compatible cellular processes: ENOPH1 is linked to methionine salvage; CBR1 to redox, xenobiotic, glucocorticoid, vitamin K and prostanoid metabolism; TIPRL to PP2A, PP4, PP6, DNA-damage checkpoint and TOR regulation; TMX1 to ER protein folding, ER stress and calcium transport; BAX to mitochondrial apoptotic signaling; SCRN1 to exocytosis; and ANXA5 to calcium-dependent membrane events, apoptosis and coagulation. The most defensible interpretation is therefore a coordinated cellular-state signal involving redox and metabolic handling, proteostasis or ER stress, membrane trafficking, and survival control, rather than evidence for one established pathway. The sparse network is organized around ENOPH1, with a smaller BAX-TMX1 branch and a CBR1-SCRN1 branch.

**Cell composition.** The module does not look like a plasma-protein or broadly secreted module. Only one gene has an intracellular-and-membrane secretome annotation, while the others are not annotated as secreted. HPA reports low immune-cell specificity for every member and no enriched blood-cell category, arguing against a blood-cell explanation. Most members have low tissue specificity, although several show tissue-enhanced or cell-type-enhanced patterns. The recurring HPA cell annotations include trophoblast populations, with additional signals in brain, choroid plexus, intestine, reproductive cells, monocytes and pancreatic duct cells. Protein detection is broader in testis than in myometrium, while several members are detected in both tissues. Thus, the shared module may reflect a conserved intracellular state or shared cell biology rather than a tissue-specific secretory or hematopoietic program. The trophoblast and reproductive-cell annotations also warrant caution about cellular composition and cell-state effects.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

None of the possible within-module gene pairs reached the supplied STRING interaction threshold, and STRING reported no functional enrichment. No hu.MAP complex contained multiple module members. Consequently, the co-abundance edges are not corroborated as established physical or functional interactions by these resources. The ENOPH1-centered topology is useful for prioritization, but it should not be described as a validated protein-interaction complex. The BAX-TMX1 and CBR1-SCRN1 pairings are co-abundance relationships in this dataset, not known molecular partnerships on the supplied evidence.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module can reasonably be described as a potentially new co-abundance pattern, but not as a newly discovered molecular complex or pathway. Its novelty is supported by the absence of reported STRING interactions, the absence of multi-member hu.MAP complexes, and the lack of a coherent globally significant GO/KEGG annotation. Those absences do not prove biological novelty: they may reflect a small module, incomplete databases, tissue-specific regulation, or a state-dependent correlation pattern. The appropriate claim is that the cross-tissue co-abundance configuration appears under-characterized and requires independent replication and experimental testing.

**Hypothesis.** Hypothesis: the shared myometrium-testis module reflects a conserved stress-adaptation and cellular-remodeling state. In this model, ENOPH1-centered metabolic activity is co-regulated with CBR1-dependent carbonyl and prostanoid handling, TIPRL-mediated phosphatase and TOR control, TMX1-dependent ER redox and calcium responses, and BAX- and ANXA5-related decisions about membrane integrity and cell survival. SCRN1 may represent a vesicle or exocytosis component of the same state. This is a mechanistic hypothesis derived from co-abundance and gene annotations, not an established pathway, and the lack of STRING or hu.MAP support means that direct biochemical coupling remains unproven.

### Important genes

#### ENOPH1

- **Related proteins** (co-abundance neighbors): TIPRL (0.90), IAH1 (0.85), ANXA5 (0.83), CBR1 (0.82), BAX (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: enolase-phosphatase 1. Enables acireductone synthase activity. Involved in L-methionine salvage from methylthioadenosine. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.371); autoimmune disorder of central nervous system (0.370); lysosomal storage disease (0.151); bipolar disorder (0.150); complication (0.145)
- **Europe PMC papers**: 156
- **Why important**: ENOPH1 is the central network gene, connecting to several members with comparatively strong co-abundance relationships. Its established annotation in methionine salvage provides a plausible metabolic anchor for the module, while its HPA tissue and cell annotations indicate context-dependent expression. It also has a substantial literature base relative to several less characterized module members and disease links involving neurological and lysosomal disorders.
- **Conclusion**: Established evidence supports ENOPH1 as the network anchor and a methionine-salvage enzyme. It is reasonable to hypothesize that ENOPH1 marks a metabolic component of the shared module, but the co-abundance network does not establish that it regulates the other genes or drives the module.

#### BAX

- **Related proteins** (co-abundance neighbors): TMX1 (0.87), ENOPH1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BCL2 associated X, apoptosis regulator. The protein encoded by this gene belongs to the BCL2 protein family. BCL2 family members form hetero- or homodimers and act as anti- or pro-apoptotic regulators that are involved in a wide variety of cellular activities. This protein forms a heterodimer with BCL2, and functions as an apoptotic activator. The association and the ratio of BAX to BCL2 also determines survival or death of a cell follo…
- **Diseases (Open Targets)**: T-cell acute lymphoblastic leukemia (0.463); colon carcinoma (0.427); endometrial carcinoma (0.383); neurodegenerative disease (0.380); gastric adenocarcinoma (0.375)
- **Europe PMC papers**: 122372
- **Why important**: BAX forms the most prominent small branch with TMX1 and also connects to ENOPH1. Its established role as a BCL2-family apoptosis regulator, including cytochrome-c release and mitochondrial death signaling, gives the module a clear cell-survival dimension. BAX has exceptionally extensive literature and broad disease relevance, making it an important biological interpreter even though it is not a pathway-enrichment result.
- **Conclusion**: Established evidence supports BAX as an apoptosis and mitochondrial-survival regulator detected in both tissues. The hypothesis that the module reflects coordinated survival control is plausible, but the data do not show that BAX-mediated apoptosis is active in either tissue or directly connected to the other module members.

#### CBR1

- **Related proteins** (co-abundance neighbors): SCRN1 (0.85), ENOPH1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carbonyl reductase 1. The protein encoded by this gene belongs to the short-chain dehydrogenases/reductases (SDR) family, which function as NADPH-dependent oxidoreductases having wide specificity for carbonyl compounds, such as quinones, prostaglandins, and various xenobiotics. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Nov 2013].
- **Diseases (Open Targets)**: neurodegenerative disease (0.371); musculoskeletal system disorder (0.303); osteoporosis (0.276); Burkitt lymphoma (0.265); alcohol drinking (0.263)
- **Europe PMC papers**: 1837
- **Why important**: CBR1 is the central member of the CBR1-SCRN1 branch and is co-abundant with ENOPH1. Its established NADPH-dependent oxidoreductase activity, broad carbonyl substrate range, and links to prostanoid, glucocorticoid, xenobiotic and vitamin K metabolism make it a strong candidate for the metabolic and redox interpretation. It is protein-detected in both tissues and has a substantial literature base.
- **Conclusion**: Established evidence supports CBR1 as a metabolic redox enzyme with potential relevance to lipid-derived and xenobiotic compounds. It may report local metabolic state in the module, but the module does not establish a specific CBR1 substrate, pathway flux, or causal role.

#### TIPRL

- **Related proteins** (co-abundance neighbors): ENOPH1 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TOR signaling pathway regulator. TIPRL is an inhibitory regulator of protein phosphatase-2A (PP2A) (see PPP2CA; MIM 176915), PP4 (see PPP4C; MIM 602035), and PP6 (see PPP6C; MIM 612725) (McConnell et al., 2007 [PubMed 17384681]).[supplied by OMIM, Nov 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.419); alcohol drinking (0.327); urolithiasis (0.327); neoplasm (0.094); lung carcinoma (0.093)
- **Europe PMC papers**: 341
- **Why important**: TIPRL is directly connected to ENOPH1 and provides a regulatory rather than purely enzymatic interpretation. Its established functions include inhibition of PP2A, PP4 and PP6 and involvement in DNA-damage checkpoint and TOR signaling. It has a smaller literature base than BAX but clear relevance to growth, stress and checkpoint control.
- **Conclusion**: Established evidence supports TIPRL as a regulator of phosphatase and TOR-related signaling. It is a plausible link between metabolic state and stress or growth control in the module, but no direct TIPRL interaction with the other members is supported by STRING or hu.MAP here.

#### TMX1

- **Related proteins** (co-abundance neighbors): BAX (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin related transmembrane protein 1. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, a catalytically active thioredoxin domain, and one transmembrane domain. Unlike most members of this gene family, it lacks a C-terminal ER-retention sequence. The …
- **Diseases (Open Targets)**: adolescent idiopathic scoliosis (0.247); Alkalosis (0.193); cutaneous lupus erythematosus (0.180); cleft lip (0.137); cleft palate (0.106)
- **Europe PMC papers**: 415
- **Why important**: TMX1 creates the BAX-TMX1 branch and supplies the module's strongest ER proteostasis interpretation. It is an ER thioredoxin-related membrane protein associated with disulfide handling, ER stress, calcium transport and ER-associated degradation. Its HPA annotation is compatible with a membrane or ER role, and its disease associations suggest biological relevance despite a more limited literature base than the best-studied genes.
- **Conclusion**: Established evidence supports TMX1 as an ER redox and proteostasis factor. A coordinated ER-stress-to-survival program involving TMX1 and BAX is a reasonable hypothesis, but the co-abundance edge does not demonstrate physical interaction or activation of ER stress.

#### ANXA5

- **Related proteins** (co-abundance neighbors): ENOPH1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A5. The Annexin 5 gene spans 29 kb containing 13 exons, and encodes a single transcript of approximately 1.6 kb and a protein product with a molecular weight of about 35 kDa.The protein encoded by this gene belongs to the annexin family of calcium-dependent phospholipid binding proteins some of which have been implicated in membrane-related events along exocytotic and endocytotic pathways. Annexin 5 i…
- **Diseases (Open Targets)**: habitual spontaneous abortion (0.370); complication (0.124); herpes zoster (0.124); nervous system disorder (0.124); neoplasm (0.118)
- **Europe PMC papers**: 3276
- **Why important**: ANXA5 is connected to ENOPH1 and contributes a membrane, calcium and cell-survival perspective. Its established functions include calcium-dependent phospholipid binding, membrane-related trafficking, inhibition of phospholipase A2 and protein kinase C, negative regulation of apoptosis and coagulation. It is detected in both tissues, has a substantial literature base, and shows cell-type-enhanced HPA annotations.
- **Conclusion**: Established evidence supports ANXA5 as a membrane-associated calcium and phospholipid regulator with links to apoptosis and coagulation. It may reflect membrane remodeling or survival-state biology in the shared module, but the data do not establish a coagulation process in either tissue or a direct interaction with ENOPH1.

## Module 10

**Tissue pair**: myometrium and testis  
**Genes (16)**: CNOT1, CUL4A, DBNL, DPP3, EFHD2, EHD1, EPS15L1, EXOC3, GCLC, EIF4G1, ISYNA1, NSFL1C, RBM12, SAMHD1, YARS1, WASHC5

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. Therefore, this module cannot be assigned a statistically supported canonical pathway from the enrichment results. Its network links suggest a mixed cellular program involving vesicle and endosomal trafficking, membrane organization, cytoskeletal or cadherin-associated processes, translation and RNA regulation, redox protection, inositol biosynthesis, and DNA or innate-immune responses. The strongest internal structure is centered on DBNL, EHD1, EIF4G1, and related trafficking or translation-linked connections, with additional smaller branches involving GCLC, DPP3, CUL4A, ISYNA1, EXOC3, and WASHC5. These annotations support a broadly expressed cellular maintenance or remodeling program more strongly than a specialized tissue-specific pathway. The functional interpretation remains provisional because the module lacks globally significant enrichment and contains biologically heterogeneous branches.

**Cell composition.** The module is not dominated by secreted or plasma proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and protein detection is common in both myometrium and testis, supporting a shared intracellular component rather than a circulating-protein signature. There is, however, evidence for cell-type mixture or shared cell populations. Several genes are enriched in late spermatids, while others are associated with neutrophils, Hofbauer cells, monocytes, or other immune-related cell types. Overall immune-cell specificity is low for most genes, so a blood-cell explanation is not established, but the immune- and spermatid-associated signals warrant attention. The module may therefore reflect broadly expressed housekeeping or cellular-trafficking machinery combined with contributions from germ-cell, smooth-muscle, epithelial, or immune-related populations.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides limited direct support for a unified physical interaction network. The known high-confidence relationships are CNOT1 with EIF4G1 and CUL4A with SAMHD1. These links support established connections between post-transcriptional regulation or translation and between ubiquitin-associated regulation or DNA-immune biology, respectively, but they do not connect the full module. hu.MAP provides additional complex-level support for YARS1 and RBM12 together in (hu.MAP huMAP3_10302.1) and (hu.MAP huMAP3_10115.1), and for YARS1 with EFHD2 in (hu.MAP huMAP3_14442.1). These complexes contain many proteins outside the module, so they indicate that selected module pairs occur in known larger assemblies rather than demonstrating a module-wide complex. The remaining co-abundance edges are not represented by the listed STRING or hu.MAP relationships, consistent with a co-regulation signal that may include indirect relationships, shared cell composition, or coordinated cellular state.

**STRING interactions (score >= 0.7)**: 2 of 120 gene pairs: CNOT1–EIF4G1 (0.814); CUL4A–SAMHD1 (0.761)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10302.1 (YARS1, RBM12; 2/9); huMAP3_10115.1 (YARS1, RBM12; 2/14); huMAP3_14442.1 (YARS1, EFHD2; 2/57)

### Novelty

The module may represent a previously unreported co-abundance pattern, but the fact sheet does not establish that it is a new biological mechanism. Its apparent novelty is supported only in the limited sense that the complete module is not recovered as a known STRING interaction network or as one hu.MAP complex. That absence is not evidence of novelty by itself, because co-abundance can reflect indirect regulation, tissue composition, or condition-dependent coordination, and interaction databases are incomplete. The lack of globally significant enrichment and the mixture of trafficking, translation, redox, DNA-response, and cell-type-associated genes make a claim of a novel unified pathway premature. Independent replication, preservation testing in additional myometrium and testis cohorts, cell-composition adjustment, and perturbation or localization experiments would be needed before calling this a new module mechanism.

**Hypothesis.** Hypothesis: the shared module reflects a conserved intracellular resource-management state present in both tissues, coupling endosomal or vesicle trafficking and actin-associated membrane remodeling with translational and RNA-processing control, antioxidant capacity, and genome or innate-immune surveillance. In this model, EHD1, DBNL, EPS15L1, EXOC3, WASHC5, and EFHD2 represent membrane, endosomal, exocytic, or cytoskeletal remodeling; EIF4G1, CNOT1, RBM12, and YARS1 represent translational or RNA-related regulation; GCLC and DPP3 contribute proteostatic or oxidative-stress handling; and CUL4A, SAMHD1, and ISYNA1 represent DNA-response, immune-response, or metabolic branches. The shared signal could arise from coordinated demands of smooth-muscle and germ-cell biology, possibly amplified by shared cellular subpopulations, rather than from one discrete molecular complex.

### Important genes

#### EHD1

- **Related proteins** (co-abundance neighbors): EFHD2 (0.86), EPS15L1 (0.83), CNOT1 (0.83), EIF4G1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Plasma membrane; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EH domain containing 1. This gene belongs to a highly conserved gene family encoding EPS15 homology (EH) domain-containing proteins. The protein-binding EH domain was first noted in EPS15, a substrate for the epidermal growth factor receptor. The EH domain has been shown to be an important motif in proteins involved in protein-protein interactions and in intracellular sorting. The protein encoded by this gene is thought …
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.107); neoplasm (0.101); device complication (0.091); lung adenocarcinoma (0.079); osteosarcoma (0.074)
- **Europe PMC papers**: 1857
- **Why important**: EHD1 has a strong central position in the co-abundance graph and connects to EFHD2, EPS15L1, CNOT1, and EIF4G1. Its established role in endocytosis, intracellular protein transport, and endocytic recycling provides a plausible bridge between the module's membrane-trafficking and post-transcriptional branches. HPA detects protein in both myometrium and testis, while its tissue and cell-type associations include testis and spermatid-related populations. Its disease and literature associations show that it is a well-studied cellular regulator rather than an uncharacterized marker.
- **Conclusion**: Established evidence supports EHD1 as a membrane-trafficking and endocytic regulator that occupies a central position in this module. It is a strong candidate for coordinating the shared cellular program, but the module does not establish that EHD1 causally drives the co-abundance pattern or that the pattern is specific to spermatids or smooth muscle.

#### DBNL

- **Related proteins** (co-abundance neighbors): DPP3 (0.89), GCLC (0.85), EIF4G1 (0.85), NSFL1C (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: drebrin like. Enables cadherin binding activity. Predicted to be involved in several processes, including Rac protein signal transduction; nervous system development; and podosome assembly. Located in cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: glycogen storage disease due to phosphoglycerate mutase deficiency (0.554); rhabdomyolysis (0.259); hereditary disease (0.192); Abnormality of the skeletal system (0.126); neoplasm (0.080)
- **Europe PMC papers**: 541
- **Why important**: DBNL has the strongest network position in the module and connects DPP3, GCLC, EIF4G1, and NSFL1C. Its cadherin-binding, membrane-organization, Rac-signaling, endocytosis, and podosome-related annotations provide a mechanistic link between cytoskeletal remodeling, membrane dynamics, and vesicle handling. HPA places it in vesicles and the plasma membrane and associates it with several specialized cell types, including Hofbauer cells, megakaryocytes, and platelets. It also has substantial literature and disease annotation, making it a biologically informative hub.
- **Conclusion**: Established evidence supports DBNL as a plausible structural and signaling hub for membrane and actin-related organization. Its centrality makes it important for interpreting the module, but the cell-type associations also mean that its co-abundance may partly reflect cellular composition rather than a conserved tissue mechanism.

#### EIF4G1

- **Related proteins** (co-abundance neighbors): RBM12 (0.92), DBNL (0.85), EHD1 (0.80); STRING partners: CNOT1 (0.814)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 is a highly connected module member linked to RBM12, DBNL, and EHD1, and it is the module participant in the known STRING relationship with CNOT1. Its established role as a scaffold in the EIF4F translation-initiation complex directly supports a translational-control interpretation. HPA detects it in both tissues, and its low tissue specificity is consistent with a broadly expressed cellular process. It also has extensive literature and disease associations.
- **Conclusion**: Established evidence supports EIF4G1 as a translational-control component that may connect RNA regulation with the trafficking-centered part of the module. Its presence is compatible with a general cellular maintenance state, but it does not prove that translation initiation is the primary function of the whole module.

#### GCLC

- **Related proteins** (co-abundance neighbors): DPP3 (0.85), DBNL (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in myometrium, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamate-cysteine ligase catalytic subunit. Glutamate-cysteine ligase, also known as gamma-glutamylcysteine synthetase is the first rate-limiting enzyme of glutathione synthesis. The enzyme consists of two subunits, a heavy catalytic subunit and a light regulatory subunit. This locus encodes the catalytic subunit, while the regulatory subunit is derived from a different gene located on chromosome 1p22-p21. Mutations at this locus have been …
- **Diseases (Open Targets)**: gamma-glutamylcysteine synthetase deficiency (0.766); cystic fibrosis (0.375); neurodegenerative disease (0.373); non-autoimmune hemolytic anemia (0.370); lung adenocarcinoma (0.331)
- **Europe PMC papers**: 8941
- **Why important**: GCLC connects DPP3 and DBNL and encodes the catalytic subunit of the rate-limiting enzyme for glutathione synthesis. Its established annotations link it to glutathione biosynthesis and oxidative-stress responses, while HPA detects protein in both tissues and reports liver tissue enhancement and an immune-cell association. It has a large literature base and strong disease relevance, including inherited glutathione-synthesis deficiency and hemolytic disease.
- **Conclusion**: Established evidence supports GCLC as the clearest oxidative-protection component of the module. Its network position suggests coordination with the DBNL and DPP3 branch, but the absence of globally significant enrichment means that an oxidative-stress pathway should remain an interpretation of selected genes rather than a demonstrated module-wide function.

#### YARS1

- **Related proteins** (co-abundance neighbors): EPS15L1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, testis
- **hu.MAP 3.0**: huMAP3_10302.1, huMAP3_10115.1, huMAP3_14442.1
- **Function (MyGene.info)**: tyrosyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Tyrosyl-tRNA synthetase belongs to the class I tRNA synthetase family. Cytokine activities have also been observ…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease dominant intermediate C (0.739); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset 2 (0.707); hereditary disease (0.509); Charcot-Marie-Tooth disease (0.418); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset (0.333)
- **Europe PMC papers**: 215
- **Why important**: YARS1 is connected to EPS15L1 and appears in all listed hu.MAP complexes containing module members: (hu.MAP huMAP3_10302.1), (hu.MAP huMAP3_10115.1), and (hu.MAP huMAP3_14442.1). Its established function in tyrosyl-tRNA aminoacylation supports protein translation, and its documented stress-related and cytokine-related activities broaden its relevance beyond constitutive translation. HPA detects it in both tissues, and its repeated complex-level presence makes it one of the best-supported physical-complex anchors in the module.
- **Conclusion**: Established evidence supports YARS1 as a translation-linked and complex-associated component that may help connect the module to broader protein-production or stress-response machinery. Its repeated hu.MAP representation is stronger evidence than the module's sparse STRING connectivity, but it still does not demonstrate that all module members participate in the same complex.

#### CUL4A

- **Related proteins** (co-abundance neighbors): ISYNA1 (0.90), EXOC3 (0.86); STRING partners: SAMHD1 (0.761)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cullin 4A. CUL4A is the ubiquitin ligase component of a multimeric complex involved in the degradation of DNA damage-response proteins (Liu et al., 2009 [PubMed 19481525]).[supplied by OMIM, Oct 2009].
- **Diseases (Open Targets)**: plasma cell myeloma (0.613); follicular lymphoma (0.566); myelodysplastic syndrome (0.563); mantle cell lymphoma (0.551); immune system disorder (0.503)
- **Europe PMC papers**: 2882
- **Why important**: CUL4A connects ISYNA1 and EXOC3 and is the module participant in the known STRING relationship with SAMHD1. Its established functions include ubiquitin-dependent protein degradation, DNA-damage response, nucleotide-excision repair, and spermatogenesis. HPA reports skeletal-muscle tissue enhancement, while the protein-level evidence in the two target tissues is limited. Its substantial literature and disease associations make it an important regulatory candidate despite its peripheral network position.
- **Conclusion**: Established evidence supports CUL4A as a ubiquitin-ligase and genome-maintenance regulator that could represent a regulatory branch of the module, with possible relevance to germ-cell biology. The CUL4A–SAMHD1 relationship is known, but the data do not show that DNA-damage or spermatogenesis biology explains the full shared module.

## Module 11

**Tissue pair**: myometrium and testis  
**Genes (6)**: PAK2, RARS1, CCT5, CCT3, CCT7, CCT8

### Function

The strongest interpretation is an intracellular protein-folding and proteostasis module centered on the chaperonin-containing T-complex. The primary evidence is the globally corrected enrichment for the chaperonin-containing T-complex and protein-folding chaperone functions (GO:CC chaperonin-containing T-complex; q_global = 3.55e-06), (GO:CC protein folding chaperone complex; q_global = 5.94e-05), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.000346), (GO:MF protein folding chaperone; q_global = 0.00199), (GO:MF unfolded protein binding; q_global = 0.00618), (GO:BP protein folding; q_global = 0.0392), and (GO:MF ATP hydrolysis activity; q_global = 0.0392). CCT3, CCT5, CCT7, and CCT8 form the coherent functional core. The same core is also associated with protein stabilization, localization of proteins and RNA to nuclear and Cajal bodies, telomerase-RNA localization, telomere maintenance, chromosome organization, and DNA biosynthetic processes (7 globally significant GO/KEGG terms, q_global 3.55e-06–3.55e-06; see the table), (8 globally significant GO/KEGG terms, q_global 1.28e-05–1.28e-05; see the table), (5 globally significant GO/KEGG terms, q_global 5.94e-05–5.94e-05; see the table), (9 globally significant GO/KEGG terms, q_global 0.000104–0.00105; see the table), (6 globally significant GO/KEGG terms, q_global 0.00132–0.00399; see the table), (GO:BP protein stabilization; q_global = 0.0102), and (GO:BP regulation of DNA metabolic process; q_global = 0.0155) (GO:BP chromosome organization; q_global = 0.0171) (GO:BP protein localization to nucleus; q_global = 0.0225). These latter annotations should be interpreted as functional associations of the CCT core rather than proof that the complete module directly regulates telomeres or reproduction. The fertilization and sperm-recognition annotations (GO:BP binding of sperm to zona pellucida; q_global = 1.28e-05), (GO:BP sperm-egg recognition; q_global = 3.11e-05), (GO:BP cell-cell recognition; q_global = 0.000104), (GO:BP cell recognition; q_global = 0.000346), (GO:BP single fertilization; q_global = 0.00105), and (GO:BP fertilization; q_global = 0.0024) may reflect the reproductive-cell expression context, shared chaperone biology, or annotation transfer, and are not sufficient by themselves to assign a reproductive-specific function. ATP and adenyl-nucleotide binding annotations involve all module genes (GO:MF ATP binding; q_global = 0.0104), (GO:MF adenyl ribonucleotide binding; q_global = 0.0107), (GO:MF adenyl nucleotide binding; q_global = 0.0278), and (GO:MF purine ribonucleoside triphosphate binding; q_global = 0.0498), but do not establish a single biochemical pathway for PAK2 and RARS1.

**Cell composition.** This is not a plasma-protein, secreted-protein, or blood-cell module. HPA reports no secreted genes and low immune-cell specificity for every member. All genes have low tissue specificity, consistent with broadly expressed intracellular machinery rather than a tissue-exclusive program. The module nevertheless has reproductive-cell signals: CCT7 is enhanced in early spermatids, late primary spermatocytes, and late spermatids; CCT5 is enhanced in late primary spermatocytes; CCT8 is enhanced in oocytes; and HPA reports enrichment of late primary spermatocytes among the represented cell types. Protein detection is stronger in testis than in myometrium, while the absence of detection for some genes in myometrium does not negate their transcript-level co-abundance. The shared module is therefore most plausibly a broadly expressed cellular machinery module that may be particularly visible in germ-cell-rich testis, rather than a blood contamination signature. It may also reflect conserved requirements for protein folding in smooth-muscle and reproductive cells.

**GO/KEGG enrichment**: 57 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chaperonin-containing T-complex | 3.55e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 3.55e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 3.55e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 3.55e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 3.55e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 3.55e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 3.55e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 3.55e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP binding of sperm to zona pellucida | 1.28e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomere maintenance via telomerase | 1.28e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 1.28e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to Cajal body | 1.28e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 1.28e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 1.28e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 1.28e-05 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING provides strong, mutually connected relationships among CCT3, CCT5, CCT7, and CCT8, and its supplementary functional annotations independently identify the TCP-one chaperonin family, the chaperonin-containing T-complex, proteostasis, actin folding, tubulin folding, and association of TRiC with nascent target proteins (15 supplementary STRING terms; within-query FDR 2.47e-06–5.52e-05). These are established relationships and strongly support the core interpretation, but the STRING enrichment statistics are supplementary rather than globally corrected primary evidence. hu.MAP identifies the same four CCT subunits together in several complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1), with a further complex containing CCT3, CCT5, and CCT7 (hu.MAP huMAP3_01951.1). The complexes also contain other CCT subunits, TCP1, prefoldin- and tubulin-related proteins, and multiple regulatory or assembly-associated proteins. Thus, the module captures a reproducible part of a larger CCT-centered protein complex rather than a complete complex. PAK2 is connected to CCT7 and CCT5 in the co-abundance graph but has no reported STRING partner or hu.MAP complex in this fact sheet. RARS1 is connected to CCT8 in the co-abundance graph but likewise has no reported STRING partner or hu.MAP complex. Their inclusion may represent co-regulation, tissue-context coupling, or indirect functional association rather than established physical binding.

**STRING interactions (score >= 0.7)**: 6 of 15 gene pairs: CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam TCP-1/cpn60 chaperonin family (FDR = 2.47e-06, 4 genes); Component Chaperonin-containing T-complex (FDR = 9.44e-06, 4 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 9.6e-06, 4 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 1.26e-05, 4 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 1.26e-05, 4 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 1.26e-05, 4 genes); InterPro GroEL-like apical domain superfamily (FDR = 1.26e-05, 4 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 1.26e-05, 4 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 1.26e-05, 4 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis (FDR = 2.53e-05, 4 genes); RCTM Folding of actin by CCT/TriC (FDR = 2.57e-05, 4 genes); RCTM Association of TriC/CCT with target proteins during biosynthesis (FDR = 2.57e-05, 4 genes); RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding (FDR = 2.57e-05, 4 genes); RCTM Formation of tubulin folding intermediates by CCT/TriC (FDR = 3.62e-05, 4 genes); RCTM Prefoldin mediated transfer of substrate  to CCT/TriC (FDR = 5.52e-05, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8)

### Novelty

The molecular function of the core is not a new discovery: CCT3, CCT5, CCT7, and CCT8 are known components of the TRiC/CCT chaperonin, and their relationships are supported by both STRING and hu.MAP (9 supplementary STRING terms; within-query FDR 2.47e-06–1.26e-05), (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). The potentially novel aspect is the reproducible co-abundance of this CCT-centered module across myometrium and testis, together with PAK2 and RARS1, and its particular association with reproductive-cell contexts. However, the fact sheet does not establish whether this cross-tissue module has been reported previously, whether it is driven by cell composition, or whether PAK2 and RARS1 are mechanistically coupled to CCT. Absence of database relationships for PAK2 or RARS1 is not evidence of novelty. The defensible conclusion is that this is a potentially novel tissue-pair co-abundance configuration built around an established chaperonin system, not a newly discovered protein complex or biological function.

**Hypothesis.** Hypothesis: a conserved, broadly expressed CCT-dependent proteostasis program is active in both myometrium and testis, with enhanced visibility in germ-cell populations. The CCT subunits may coordinate ATP-dependent folding of cytoskeletal and other newly synthesized proteins, thereby supporting cell architecture, protein stability, and nuclear or Cajal-body processes represented by the primary annotations (8 globally significant GO/KEGG terms, q_global 3.55e-06–3.55e-06; see the table), (GO:CC protein folding chaperone complex; q_global = 5.94e-05), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.000346), (GO:MF protein folding chaperone; q_global = 0.00199), (GO:MF unfolded protein binding; q_global = 0.00618), and (GO:BP protein stabilization; q_global = 0.0102). PAK2 may connect this proteostasis core to Rho-family-dependent cytoskeletal remodeling, nuclear signaling, migration, or apoptosis-related responses, while RARS1 may couple it to the high translational demand of cells producing new proteins. This proposed coupling is not established by the available physical-interaction evidence and should be tested with cell-type-resolved expression, perturbation of CCT subunits, and direct assessment of PAK2 and RARS1 dependency.

### Important genes

#### CCT7

- **Related proteins** (co-abundance neighbors): PAK2 (0.91), CCT3 (0.91); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is part of the tightly connected CCT core supported by STRING and every hu.MAP complex reported for the core (9 supplementary STRING terms; within-query FDR 2.47e-06–1.26e-05), (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It has the strongest weighted position in the module subgraph and connects to both CCT3 and PAK2. Its annotations cover ATP-dependent folding, protein stabilization, telomere-related processes, and Cajal-body localization (8 globally significant GO/KEGG terms, q_global 3.55e-06–3.55e-06; see the table), (8 globally significant GO/KEGG terms, q_global 1.28e-05–1.28e-05; see the table), (GO:CC protein folding chaperone complex; q_global = 5.94e-05), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.000346), (GO:MF protein folding chaperone; q_global = 0.00199), (GO:MF unfolded protein binding; q_global = 0.00618), and (GO:BP protein stabilization; q_global = 0.0102). HPA additionally links it to several spermatogenic cell types. The gene has a substantial literature and reported Open Targets associations including preeclampsia, myocardial infarction, neurodegenerative disease, and hepatocellular carcinoma.
- **Conclusion**: Established evidence supports CCT7 as a core TRiC/CCT chaperonin subunit and a central member of this module. Its germ-cell expression and disease associations support biological relevance but do not demonstrate a myometrium-testis-specific mechanism. A role for CCT7 in linking chaperone activity to PAK2-associated cytoskeletal signaling remains a hypothesis.

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT7 (0.91), CCT8 (0.82); STRING partners: CCT5 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a core CCT member with strong STRING relationships to CCT5, CCT7, and CCT8 and membership in all listed hu.MAP complexes (9 supplementary STRING terms; within-query FDR 2.47e-06–1.26e-05), (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It participates in the broadest set of primary annotations in the module, including chaperonin complex, protein folding, protein stabilization, nuclear and Cajal-body localization, telomere maintenance, chromosome organization, and fertilization-related terms (57 globally significant GO/KEGG terms, q_global 3.55e-06–0.0498; see the table). HPA detects it in both myometrium and testis, and it has a substantial literature with reported associations involving neurodevelopmental, neurodegenerative, musculoskeletal, and cardiac phenotypes.
- **Conclusion**: Established evidence makes CCT3 a robust marker of the conserved CCT-centered function and of the shared intracellular proteostasis program. Its broad annotations should not be interpreted as evidence that CCT3 independently controls every associated process. A tissue-pair-specific role beyond generic CCT activity is not established.

#### CCT8

- **Related proteins** (co-abundance neighbors): RARS1 (0.85), CCT3 (0.82); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is a core CCT component connected to CCT3, CCT5, and CCT7 in STRING and present in the principal hu.MAP complexes (9 supplementary STRING terms; within-query FDR 2.47e-06–1.26e-05), (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). It contributes to the globally corrected chaperone, protein-folding, nuclear-localization, telomere, cell-recognition, and fertilization-related annotations (57 globally significant GO/KEGG terms, q_global 3.55e-06–0.0498; see the table). Its HPA localization includes the connecting and end pieces of sperm-related structures, and its single-cell enhancement in oocytes is relevant to the reproductive context. It also has a substantial literature and reported cancer-related Open Targets associations.
- **Conclusion**: Established evidence supports CCT8 as a core folding-chaperone subunit and as a plausible contributor to the reproductive-cell signal. The sperm and oocyte observations are contextual expression evidence, not proof of a specialized gamete function. Its proposed coupling to RARS1 is suggested by the co-abundance edge but is not an established physical interaction.

#### CCT5

- **Related proteins** (co-abundance neighbors): PAK2 (0.84); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 completes the principal four-subunit CCT core, with strong STRING links to CCT3, CCT7, and CCT8 and membership in all listed hu.MAP complexes (9 supplementary STRING terms; within-query FDR 2.47e-06–1.26e-05), (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It shares the primary chaperone, folding, stabilization, telomere, and Cajal-body annotations of the core (8 globally significant GO/KEGG terms, q_global 3.55e-06–3.55e-06; see the table), (8 globally significant GO/KEGG terms, q_global 1.28e-05–1.28e-05; see the table), (GO:CC protein folding chaperone complex; q_global = 5.94e-05), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.000346), (GO:MF protein folding chaperone; q_global = 0.00199), (GO:MF unfolded protein binding; q_global = 0.00618), and (GO:BP protein stabilization; q_global = 0.0102). HPA identifies enhancement in late primary spermatocytes and protein detection in testis. The gene has a substantial literature and reported associations with hereditary sensory and autonomic neuropathy, spastic paraplegia, and neurodegenerative disease.
- **Conclusion**: Established evidence supports CCT5 as an essential interpretive component of the conserved CCT-centered module and as a plausible contributor to its testis-associated signal. Disease associations show that perturbing this chaperone subunit can have systemic consequences, but they do not establish a role in myometrium or testis in this dataset. Its co-abundance relationship with PAK2 may indicate regulatory coupling, but physical interaction is not demonstrated.

#### PAK2

- **Related proteins** (co-abundance neighbors): CCT7 (0.91), CCT5 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: p21 (RAC1) activated kinase 2. The p21 activated kinases (PAK) are critical effectors that link Rho GTPases to cytoskeleton reorganization and nuclear signaling. The PAK proteins are a family of serine/threonine kinases that serve as targets for the small GTP binding proteins, CDC42 and RAC1, and have been implicated in a wide range of biological activities. The protein encoded by this gene is activated by proteolytic cleavage …
- **Diseases (Open Targets)**: Knobloch syndrome 2 (0.525); Knobloch syndrome (0.454); HIV infectious disease (0.370); atrial fibrillation (0.210); ovarian carcinoma (0.175)
- **Europe PMC papers**: 3704
- **Why important**: PAK2 is important because it is the module's most functionally distinct connector to the CCT core: it is co-abundant with CCT7 and CCT5, while no STRING partner or hu.MAP complex is reported for it here. Its established function is as a serine/threonine kinase linking RAC1 and CDC42 signaling to cytoskeletal reorganization and nuclear signaling, with roles in signal transduction, cell migration, starvation responses, phosphorylation, and apoptosis-related activation. It contributes to the globally corrected nucleotide-binding annotations (GO:MF ATP binding; q_global = 0.0104), (GO:MF adenyl ribonucleotide binding; q_global = 0.0107), (GO:MF adenyl nucleotide binding; q_global = 0.0278), and (GO:MF purine ribonucleoside triphosphate binding; q_global = 0.0498). HPA places it in nucleoplasm and nuclear speckles and reports enhancement in neutrophils, while its literature is substantial and includes disease associations such as Knobloch syndrome, HIV infection, atrial fibrillation, and ovarian carcinoma.
- **Conclusion**: Established evidence supports PAK2 as a signaling and cytoskeletal kinase, not as a CCT complex member. Its co-abundance with CCT5 and CCT7 may connect proteostasis to cytoskeletal or nuclear signaling, but this is a hypothesis because database-supported physical relationships are absent in the fact sheet. Its neutrophil signal does not imply blood contamination because overall immune-cell specificity is low for the module.

#### RARS1

- **Related proteins** (co-abundance neighbors): CCT8 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 is the module's translation-linked component. It encodes arginyl-tRNA synthetase, an enzyme required for arginyl-tRNA aminoacylation and protein translation, and contributes to the globally corrected ATP and adenyl-nucleotide binding annotations (GO:MF ATP binding; q_global = 0.0104), (GO:MF adenyl ribonucleotide binding; q_global = 0.0107), (GO:MF adenyl nucleotide binding; q_global = 0.0278), and (GO:MF purine ribonucleoside triphosphate binding; q_global = 0.0498). It has a co-abundance edge with CCT8 but no reported STRING partner or hu.MAP complex. HPA detects it in testis but not myometrium, and its reported Open Targets associations include hypomyelinating leukodystrophy and related hereditary disease. Its literature is more limited than that of the CCT genes but directly supports its translation-related function.
- **Conclusion**: Established evidence supports RARS1 as a translation enzyme that could supply newly synthesized substrates to a proteostasis system. Its testis detection and link to CCT8 make it relevant to the tissue-pair interpretation, but they do not establish a direct interaction or a reproductive-specific role. The proposed connection between translational demand and CCT-mediated folding remains a hypothesis.
