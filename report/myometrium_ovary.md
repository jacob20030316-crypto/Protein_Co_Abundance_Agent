# Conserved co-abundance modules: myometrium and ovary

## Module 0

**Tissue pair**: myometrium and ovary  
**Genes (5)**: GOT2, CS, MAN2A1, OAT, SUCLG1

### Function

The module is most consistent with coordinated cellular metabolism, especially mitochondrial energy production and amino acid handling. CS, GOT2, OAT, and SUCLG1 are mitochondrial or mitochondria-associated metabolic enzymes involved in the tricarboxylic acid cycle, amino acid metabolism, or both. MAN2A1 adds a Golgi N-glycan maturation function, so the module is not a purely mitochondrial pathway. The strongest network position belongs to CS, which connects the other metabolic genes and is supported by high-confidence STRING links to GOT2 and SUCLG1. The supplementary STRING pathway signal for amino acid metabolism (STRING WikiPathways Amino acid metabolism; within-query FDR = 0.0022) is concordant with this interpretation. No GO or KEGG term passed global correction; therefore, the metabolic interpretation is based on gene functions, network structure, and supplementary STRING evidence rather than a globally significant GO or KEGG enrichment result.

**Cell composition.** This is not a plasma-protein, secreted-protein, or blood-cell-enriched module. HPA reports no secreted genes and low immune-cell specificity for every member, with no enriched blood-cell category. The genes are mainly intracellular metabolic or biosynthetic proteins, although MAN2A1 is localized to the Golgi. HPA profiles are heterogeneous: several genes show tissue or cell-type enhancement in organs and cell types outside the reproductive tissues, while one gene has low tissue specificity. Protein detection is present for part of the module in both myometrium and ovary but absent for other members in one or both tissues. Thus, the shared module is unlikely to be explained by circulating proteins or an obvious immune infiltrate. It could instead reflect shared metabolic activity, a shared nonimmune cell population, or coordinated cellular-state variation in the two tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports established functional connectivity centered on CS: CS-GOT2 and CS-SUCLG1 are high-confidence associations. These relationships are biologically plausible because CS is a tricarboxylic-acid-cycle enzyme, GOT2 participates in amino acid and tricarboxylic-acid-cycle metabolism, and SUCLG1 catalyzes a mitochondrial succinyl-CoA reaction. STRING also reports the supplementary amino-acid-metabolism pathway (STRING WikiPathways Amino acid metabolism; within-query FDR = 0.0022), involving GOT2, CS, OAT, and SUCLG1. OAT is therefore functionally consistent with the metabolic part of the module even though it lacks a listed direct STRING partner within the module. MAN2A1 has no listed STRING partner in this module, so its connection is supplied by the co-abundance network rather than by the reported STRING evidence. hu.MAP reports no complex containing multiple module members. Overall, the module contains a known metabolic core plus co-abundance links that are not fully represented by curated interaction or complex resources.

**STRING interactions (score >= 0.7)**: 2 of 10 gene pairs: CS–GOT2 (0.952); CS–SUCLG1 (0.929)
**STRING functional enrichment (supplementary, within-query FDR)**: WikiPathways Amino acid metabolism (FDR = 0.0022, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The specific conserved co-abundance module shared by myometrium and ovary may represent a novel tissue-pair observation, because the supplied resources do not report a matching hu.MAP complex and do not provide established STRING support for every co-abundance edge. However, its central biological relationships are not wholly novel: the CS-GOT2 and CS-SUCLG1 associations are already supported by STRING, and the biochemical roles of all members are established. Therefore, the defensible claim is not discovery of a new metabolic pathway, but possible novelty of the cross-tissue co-abundance configuration, particularly the inclusion and placement of MAN2A1. Novelty would require independent replication, comparison with published tissue co-expression modules, and experimental or perturbational testing.

**Hypothesis.** Hypothesis: a shared cellular state in myometrium and ovary coordinates mitochondrial carbon flux, amino acid interconversion, and Golgi glycan maturation. In this model, CS acts as the metabolic hub, GOT2 and OAT connect amino-acid-derived carbon and nitrogen handling to central metabolism, and SUCLG1 supports mitochondrial succinyl-CoA utilization and nucleotide production. MAN2A1 may report a coupled biosynthetic or secretory-processing state rather than a direct physical interaction with the mitochondrial enzymes. An alternative explanation is that the module reflects shared proportions of a metabolically active nonimmune cell population. These possibilities should be distinguished by cell-resolved expression, mitochondrial and glycosylation measurements, and perturbation of the central metabolic genes.

### Important genes

#### CS

- **Related proteins** (co-abundance neighbors): OAT (0.81), MAN2A1 (0.81), GOT2 (0.80); STRING partners: GOT2 (0.952), SUCLG1 (0.929)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in myometrium, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS is the central network connector and has the strongest weighted connectivity in the module. It is a mitochondrial citrate-synthesis enzyme at the entry point of the tricarboxylic acid cycle, is detected in both myometrium and ovary by HPA, and participates in the supplementary STRING amino-acid-metabolism signal (STRING WikiPathways Amino acid metabolism; within-query FDR = 0.0022). Its extensive literature and disease-association record make it the best-supported anchor for interpreting the module.
- **Conclusion**: Established evidence supports CS as the metabolic hub and a plausible marker of oxidative metabolic state. It is hypothesized, but not demonstrated here, that CS organizes the cross-tissue co-abundance pattern or drives the other genes.

#### GOT2

- **Related proteins** (co-abundance neighbors): CS (0.80); STRING partners: CS (0.952)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamic-oxaloacetic transaminase 2. Glutamic-oxaloacetic transaminase is a pyridoxal phosphate-dependent enzyme which exists in cytoplasmic and inner-membrane mitochondrial forms, GOT1 and GOT2, respectively. GOT plays a role in amino acid metabolism and the urea and tricarboxylic acid cycles. The two enzymes are homodimeric and show close homology. Two transcript variants encoding different isoforms have been found for this gene. […
- **Diseases (Open Targets)**: genetic developmental and epileptic encephalopathy (0.618); developmental and epileptic encephalopathy (0.393); Encephalopathy (0.370); neurodegenerative disease (0.356); lagophthalmos (0.298)
- **Europe PMC papers**: 2463
- **Why important**: GOT2 is directly connected to CS in the co-abundance network and by high-confidence STRING evidence. It is a mitochondrial aminotransferase involved in amino acid, aspartate, glutamate, glutamine, and tricarboxylic-acid-related metabolism. HPA places it in a group-enriched pattern involving metabolically active tissues and detects it in ovary. Its disease associations and substantial literature support its biological importance.
- **Conclusion**: Established evidence supports GOT2 as the strongest amino-acid-metabolism component of the module and as a known partner of CS. Its specific contribution to the shared myometrium and ovary state remains a hypothesis because protein detection is not uniform across the two tissues.

#### SUCLG1

- **Related proteins** (co-abundance neighbors): MAN2A1 (0.81); STRING partners: CS (0.929)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in myometrium, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase GDP/ADP-forming subunit alpha. This gene encodes the alpha subunit of the heterodimeric enzyme succinate coenzyme A ligase. This enzyme is targeted to the mitochondria and catalyzes the conversion of succinyl CoA and ADP or GDP to succinate and ATP or GTP. Mutations in this gene are the cause of the metabolic disorder fatal infantile lactic acidosis and mitochondrial DNA depletion. [provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome 9 (0.811); neurodegenerative disease (0.520); mitochondrial DNA depletion syndrome (0.507); post term pregnancy (0.280); lysosomal storage disease (0.245)
- **Europe PMC papers**: 1277
- **Why important**: SUCLG1 is part of the mitochondrial tricarboxylic-acid-cycle machinery, catalyzing the succinate-CoA ligase reaction, and is linked to CS by high-confidence STRING evidence. It is detected by HPA in both tissues and has established associations with mitochondrial DNA depletion and related metabolic disease. Its position provides an independent connection between the co-abundance module and mitochondrial energy metabolism.
- **Conclusion**: Established evidence supports SUCLG1 as a mitochondrial energy-metabolism member that reinforces the CS-centered interpretation. A direct causal role in the shared tissue module is not established and remains hypothetical.

#### OAT

- **Related proteins** (co-abundance neighbors): CS (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ornithine aminotransferase. This gene encodes the mitochondrial enzyme ornithine aminotransferase, which is a key enzyme in the pathway that converts arginine and ornithine into the major excitatory and inhibitory neurotransmitters glutamate and GABA. Mutations that result in a deficiency of this enzyme cause the autosomal recessive eye disease Gyrate Atrophy. Alternatively spliced transcript variants encoding different isof…
- **Diseases (Open Targets)**: ornithine aminotransferase deficiency (0.852); inherited retinal dystrophy (0.524); eye disorder (0.371); Pain (0.266); Abnormal choroid morphology (0.266)
- **Europe PMC papers**: 19682
- **Why important**: OAT connects to CS in the network and is included in the supplementary STRING amino-acid-metabolism signal (STRING WikiPathways Amino acid metabolism; within-query FDR = 0.0022). It is a mitochondrial enzyme in ornithine, arginine, glutamate, glutamine, and proline-related metabolism, with a substantial literature and well-established links to ornithine aminotransferase deficiency and inherited retinal disease. HPA shows tissue and cell-type enhancement in metabolically specialized contexts, although protein was not detected in the sampled myometrium or ovary.
- **Conclusion**: Established evidence supports OAT as a functionally coherent amino-acid-metabolism component. Its absence of HPA protein detection in the sampled reproductive tissues weakens a direct tissue-protein interpretation, so its role may reflect transcript-level co-abundance, condition dependence, or cellular composition rather than active protein function in every sample.

#### MAN2A1

- **Related proteins** (co-abundance neighbors): SUCLG1 (0.81), CS (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Golgi apparatus; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosidase alpha class 2A member 1. This gene encodes a glycosyl hydrolase that localizes to the Golgi and catalyzes the final hydrolytic step in the asparagine-linked oligosaccharide (N-glycan) maturation pathway. Mutations in the mouse homolog of this gene have been shown to cause a systemic autoimmune disease similar to human systemic lupus erythematosus. [provided by RefSeq, Dec 2013].
- **Diseases (Open Targets)**: alcohol drinking (0.456); schizophrenia (0.455); COVID-19 (0.370); smoking initiation (0.364); dislocation (0.344)
- **Europe PMC papers**: 663
- **Why important**: MAN2A1 is a network-linked member that connects to CS and SUCLG1 despite having no listed STRING partner in the module. It encodes a Golgi glycosyl hydrolase involved in the final step of N-glycan maturation, providing a biosynthetic and protein-processing dimension distinct from the mitochondrial enzymes. HPA describes low tissue specificity, an oligodendrocyte-enriched cell pattern, and detection in myometrium but not ovary. Its literature is smaller than that of the metabolic hub genes, making its co-abundance link especially informative for assessing module novelty.
- **Conclusion**: Established evidence supports MAN2A1 as a Golgi glycan-processing enzyme, but does not establish a direct biochemical interaction with the mitochondrial genes. Its membership may indicate coordinated cellular biosynthesis or a composition effect; a functional bridge between glycosylation and mitochondrial metabolism is a hypothesis requiring experimental validation.

## Module 1

**Tissue pair**: myometrium and ovary  
**Genes (5)**: ALB, SERPINC1, EHD2, TF, VTN

### Function

The strongest interpretation is a blood-derived extracellular transport, coagulation-regulatory, and adhesion-associated module. The primary globally corrected evidence is enrichment for blood microparticles (GO:CC blood microparticle; q_global = 0.00333), with ALB, SERPINC1, TF, and VTN contributing to that term. SERPINC1 provides anticoagulant activity, TF provides iron transport, ALB provides abundant plasma transport and binding capacity, and VTN supports extracellular adhesion, migration, and integrin-related signaling. The subgraph is centered on ALB, which connects to SERPINC1, TF, and VTN, while SERPINC1 also connects to VTN and to EHD2. Thus, the network is coherent for a plasma-protein association pattern, but its biological meaning as an intrinsic myometrial or ovarian program is uncertain. The STRING enrichment terms (STRING COMPARTMENTS Blood microparticle; within-query FDR = 0.0014) and (STRING Component Blood microparticle; within-query FDR = 0.0014) support the blood-microparticle interpretation but are supplementary rather than independent globally corrected evidence.

**Cell composition.** The module is dominated by secreted blood proteins. ALB, SERPINC1, VTN, and TF are secreted to blood, are enriched mainly in liver or hepatocyte contexts, and are not detected in immune cells according to HPA. Their proteins are not detected in myometrium or ovary, whereas EHD2 is detected in both tissues and has membrane-associated localization. This composition strongly raises the possibility that the shared module reflects circulating plasma, blood microparticles, vascular material, or a shared sample-associated component rather than a resident tissue cell program. The absence of immune-cell enrichment argues against a simple blood-leukocyte explanation, but it does not exclude plasma contamination or blood-derived extracellular material. EHD2 is the main tissue-compatible exception: it has broader tissue specificity and single-cell enhancement in stromal, fibroblast, and related cell contexts, but it lacks a globally significant GO or KEGG annotation in this module.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 0.00333 | ALB, SERPINC1, TF, VTN |

### STRING and hu.MAP

STRING supports established relationships among the plasma proteins: ALB is linked to SERPINC1, VTN, and TF, and SERPINC1 is linked to VTN. These relationships overlap strongly with the module structure and indicate that much of the module is already a recognized plasma-protein association network. The supplementary STRING results repeatedly recover blood microparticles and plasma, coagulation, hemostasis, and extracellular or endoplasmic-reticulum-associated contexts (STRING COMPARTMENTS Blood microparticle; within-query FDR = 0.0014), (STRING Component Blood microparticle; within-query FDR = 0.0014), (STRING NetworkNeighborAL Hemostasis, and Dissolution of Fibrin Clot; within-query FDR = 0.0179), and (STRING Component Endoplasmic reticulum lumen; within-query FDR = 0.018). Several hu.MAP complexes also contain ALB and TF together, while the highest-confidence listed complex contains SERPINC1, ALB, and TF (hu.MAP huMAP3_15040.1); the remaining complexes reinforce recurring plasma-protein assemblages involving ALB and TF (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1). VTN and EHD2 have no listed hu.MAP complex membership, and EHD2 has no listed STRING partner. Therefore, the network combines well-known plasma-protein relationships with a less-established EHD2–SERPINC1 co-abundance connection.

**STRING interactions (score >= 0.7)**: 4 of 10 gene pairs: ALB–SERPINC1 (0.933); ALB–TF (0.9); ALB–VTN (0.988); SERPINC1–VTN (0.949)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Blood microparticle (FDR = 0.0014, 4 genes); Component Blood microparticle (FDR = 0.0014, 4 genes); PMID (2021) Insight into the human pathodegradome of the V8 protease from Staphylococcus aureus. (FDR = 0.0055, 4 genes); PMID (2020) Regulating Protein Corona Formation and Dynamic Protein Exchange by Controlling Nanoparticle Hydrophobicity. (FDR = 0.0055, 4 genes); PMID (2019) Quantitative Comparative Proteomics Reveal Biomarkers for Dengue Disease Severity. (FDR = 0.0055, 4 genes); PMID (2022) Systematic Review and Meta-Analysis on MS-Based Proteomics Applied to Human Peripheral Fluids to Assess Potential Biomarkers of Bipolar Disorder. (FDR = 0.0057, 4 genes); PMID (2016) Human plasma protein N-glycosylation. (FDR = 0.006, 4 genes); PMID (2023) Analysis of Plasma Proteins Involved in Inflammation, Immune ResponseComplement System, and Blood Coagulation upon Admission of COVID-19 Patients to Hospital May Help to Predict the Prognosis of the Disease. (FDR = 0.0066, 4 genes); PMID (2019) Label-Free Proteomics Revealed Oxidative Stress and Inflammation as Factors That Enhance Chemoresistance in Luminal Breast Cancer. (FDR = 0.0066, 4 genes); PMID (2015) Candida albicans Shaving to Profile Human Serum Proteins on Hyphal Surface. (FDR = 0.01, 4 genes); PMID (2014) Proteomic analysis of human plasma in chronic rheumatic mitral stenosis reveals proteins involved in the complement and coagulation cascade. (FDR = 0.0134, 4 genes); NetworkNeighborAL Hemostasis, and Dissolution of Fibrin Clot (FDR = 0.0179, 3 genes); Component Endoplasmic reticulum lumen (FDR = 0.018, 4 genes); PMID (2022) Changes in Whey Proteome between Mediterranean and Murrah Buffalo Colostrum and Mature Milk Reflect Their Pharmaceutical and Medicinal Value. (FDR = 0.0265, 4 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 0.0265, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINC1, ALB, TF; 3/64); huMAP3_07432.1 (ALB, TF; 2/18); huMAP3_07265.1 (ALB, TF; 2/20); huMAP3_09434.1 (ALB, TF; 2/33); huMAP3_08395.1 (ALB, TF; 2/43); huMAP3_09531.1 (ALB, TF; 2/47); huMAP3_10101.1 (ALB, TF; 2/49); huMAP3_10678.1 (ALB, TF; 2/71)

### Novelty

This is not strong evidence for a newly discovered molecular complex or pathway. Most of the central relationships are already represented by high-confidence STRING associations and recurring hu.MAP plasma-protein complexes, and the globally significant annotation is a well-established blood-microparticle context (GO:CC blood microparticle; q_global = 0.00333). A potentially novel aspect could be the reproducible co-abundance of EHD2 with the plasma-protein component across myometrium and ovary, but the available evidence cannot distinguish a true tissue-associated interaction from indirect co-presence, vascular material, or technical and biological confounding. Absence of EHD2 from the listed STRING and hu.MAP relationships does not establish novelty. The appropriate conclusion is that the tissue-pair observation may be worth follow-up, but it should not be presented as a new mechanistic module without tissue-resolved validation.

**Hypothesis.** Hypothesis: the shared signal arises primarily from circulating blood microparticles or plasma proteins retained similarly in myometrium and ovary samples. Within that extracellular milieu, ALB, TF, SERPINC1, and VTN may form or travel within overlapping protein assemblies related to transport, protease regulation, coagulation control, and cell-matrix interactions. EHD2 may reflect a local membrane or stromal component that covaries with this vascular or extracellular material, possibly through shared tissue structure or vesicle-associated processes. This hypothesis predicts that the module should decrease after careful removal or modeling of vascular and plasma-derived signal, while EHD2 should show more tissue-localized expression than the other module members. The proposed connection between EHD2 and SERPINC1 is a hypothesis, not an established physical interaction.

### Important genes

#### ALB

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.95), VTN (0.83), TF (0.80); STRING partners: SERPINC1 (0.933), TF (0.9), VTN (0.988)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB is the central network gene, connecting to SERPINC1, TF, and VTN. It is a highly abundant secreted blood protein with broad carrier and transport functions, is strongly represented in the primary blood-microparticle term (GO:CC blood microparticle; q_global = 0.00333), recurs across the STRING evidence, and participates in every listed hu.MAP complex (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1). Its very large literature base and established plasma biology make it the clearest indicator of sample-associated blood or plasma signal.
- **Conclusion**: Established evidence supports ALB as the structural and interpretive anchor of a plasma-protein module, not as evidence for an ovary- or myometrium-specific ALB program. A local tissue role is not supported by the HPA detection pattern in this fact sheet.

#### SERPINC1

- **Related proteins** (co-abundance neighbors): ALB (0.95), EHD2 (0.90); STRING partners: ALB (0.933), VTN (0.949)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 occupies a connecting position between ALB, VTN, and EHD2 and is present in the primary blood-microparticle term (GO:CC blood microparticle; q_global = 0.00333). It encodes antithrombin, a plasma protease inhibitor that regulates blood coagulation, and it has established disease associations involving antithrombin deficiency and venous thrombosis. Its association with ALB and VTN is supported by STRING, and its presence with ALB and TF in hu.MAP complex (hu.MAP huMAP3_15040.1) reinforces a plasma and hemostatic interpretation.
- **Conclusion**: Established evidence supports SERPINC1 as a coagulation-regulatory component of a circulating plasma or microparticle signal. The EHD2–SERPINC1 edge may be biologically interesting, but the fact sheet does not establish a direct interaction or a tissue-specific mechanism.

#### VTN

- **Related proteins** (co-abundance neighbors): ALB (0.83); STRING partners: ALB (0.988), SERPINC1 (0.949)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vitronectin. The protein encoded by this gene functions in part as an adhesive glycoprotein. Differential expression of this protein can promote either cell adhesion or migration as it links cells to the extracellular matrix through a variety of ligands. These ligands include integrins, plasminogen activator inhibitor-1, and urokinase plasminogen activator receptor. This secreted protein can be present in the …
- **Diseases (Open Targets)**: hypertensive disorder (0.421); dengue disease (0.376); neurodegenerative disease (0.343); temporal arteritis (0.338); age-related macular degeneration (0.313)
- **Europe PMC papers**: 3940
- **Why important**: VTN connects to ALB and SERPINC1 and contributes to the primary blood-microparticle annotation (GO:CC blood microparticle; q_global = 0.00333). It is a secreted adhesive glycoprotein that can link integrins and extracellular-matrix-related ligands and is associated with cell adhesion, cell-matrix adhesion, and smooth-muscle-cell migration. Its STRING relationships with ALB and SERPINC1 are strong established network support, while its absence from the listed hu.MAP complexes makes it a useful extracellular-matrix-related complement to the plasma transport proteins.
- **Conclusion**: Established evidence supports VTN as an extracellular adhesive and plasma component that could connect circulating material to tissue interfaces. A role in myometrial or ovarian remodeling remains a hypothesis because HPA places the gene mainly in liver-associated contexts and does not detect its protein in the sampled tissues.

#### TF

- **Related proteins** (co-abundance neighbors): ALB (0.80); STRING partners: ALB (0.9)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: transferrin. This gene encodes a glycoprotein with an approximate molecular weight of 76.5 kDa. It is thought to have been created as a result of an ancient gene duplication event that led to generation of homologous C and N-terminal domains each of which binds one ion of ferric iron. The function of this protein is to transport iron from the intestine, reticuloendothelial system, and liver parenchymal cells t…
- **Diseases (Open Targets)**: atransferrinemia (0.776); alcohol drinking (0.492); hemochromatosis type 1 (0.471); neurodegenerative disease (0.400); urolithiasis (0.329)
- **Europe PMC papers**: 143656
- **Why important**: TF connects directly to the central ALB node and contributes to (GO:CC blood microparticle; q_global = 0.00333). It is a secreted iron-transport glycoprotein with functions in iron movement and intracellular iron homeostasis. It is repeatedly recovered with ALB and other plasma proteins in the supplementary STRING results and appears with ALB in many hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1). Its extensive literature and well-established systemic transport function make it an important indicator of the module's circulating-protein character.
- **Conclusion**: Established evidence supports TF as a systemic plasma transport component that reinforces the blood-derived interpretation. The fact sheet does not support a resident TF-driven mechanism in myometrium or ovary.

#### EHD2

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in myometrium, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EH domain containing 2. This gene encodes a member of the EH domain-containing protein family. These proteins are characterized by a C-terminal EF-hand domain, a nucleotide-binding consensus site at the N terminus and a bipartite nuclear localization signal. The encoded protein interacts with the actin cytoskeleton through an N-terminal domain and also binds to an EH domain-binding protein through the C-terminal EH domai…
- **Diseases (Open Targets)**: disorder of patella (0.201); neuromuscular disease (0.201); muscular disease (0.201); triple-negative breast carcinoma (0.095); breast cancer (0.094)
- **Europe PMC papers**: 1131
- **Why important**: EHD2 is the only module member with HPA protein detection in both myometrium and ovary and has plasma-membrane localization. It is linked in the module to SERPINC1, but it has no listed STRING partner or hu.MAP complex and no globally significant GO or KEGG term. Its functions in endocytosis, endocytic recycling, plasma-membrane tubulation, and actin-cytoskeleton connection provide a plausible tissue or membrane context that differs from the secreted plasma proteins.
- **Conclusion**: Established evidence supports EHD2 as the most plausible resident-tissue or membrane-associated component of the module. Whether it forms a biologically meaningful bridge to SERPINC1, or merely covaries with vascular or extracellular material, is unresolved and should be treated as a hypothesis requiring spatial and biochemical validation.
