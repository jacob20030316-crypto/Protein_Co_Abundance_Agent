# Conserved co-abundance modules: bone_marrow and heart

## Module 0

**Tissue pair**: bone_marrow and heart  
**Genes (32)**: GOT2, ACADM, ACADVL, ACO2, ACSL1, AIFM1, ATP5F1C, BCS1L, CS, COQ3, MLYCD, DECR1, DHRS4, ETFA, HSDL2, IDH2, LAMA2, SLC25A20, MCCC1, IMMT, MYOM1, NDUFA10, NDUFS1, NNT, PDHB, UQCRC2, SLC25A12, SDHA, SUCLA2, ACAT1, ACAA2, TTN

### Function

This is a mitochondrial energy-metabolism module. The primary evidence is the strong enrichment for mitochondrion (GO:CC mitochondrion; q_global = 0.000333), mitochondrial matrix (GO:CC mitochondrial matrix; q_global = 0.00921), small-molecule metabolic process (GO:BP small molecule metabolic process; q_global = 0.0186), and the tricarboxylic acid cycle (GO:BP tricarboxylic acid cycle; q_global = 0.0466). The genes cover complementary parts of oxidative metabolism: pyruvate entry through PDHB, the tricarboxylic acid cycle through CS, ACO2, IDH2, SDHA, and SUCLA2, respiratory electron transfer through NDUFA10, NDUFS1, BCS1L, and UQCRC2, ATP synthesis through ATP5F1C, and fatty-acid oxidation through ACADM, ACADVL, ACAA2, ETFA, DECR1, SLC25A20, and related genes. The network therefore most plausibly represents coordinated mitochondrial oxidative phosphorylation, TCA-cycle activity, and substrate oxidation, rather than a narrowly specialized single pathway.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins. The HPA summary identifies only LAMA2 as secreted to the extracellular matrix, while the remainder are predominantly intracellular mitochondrial, metabolic, structural, or vesicular proteins. The composition is also not blood-cell enriched: most genes have low immune-cell specificity, with only ACSL1 showing neutrophil enrichment and HSDL2 showing neutrophil cell-type enhancement. Instead, the HPA pattern is strongly compatible with oxidative tissues and contractile cells, especially skeletal muscle, tongue, liver, heart muscle, myonuclei, hepatocytes, and cardiomyocytes. Protein detection is broad in heart and substantial in bone marrow, but several genes are detected in heart and not bone marrow by IHC. Thus, the shared signal is more consistent with conserved mitochondrial metabolism and possibly shared muscle or metabolically active cell populations than with a plasma or blood-cell contamination signature. The presence of MYOM1, TTN, and LAMA2 also indicates a structural or muscle-associated component within an otherwise metabolic module.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrion | 0.000333 | ACAA2, ACADM, ACADVL, ACAT1, ACO2, ACSL1, AIFM1, ATP5F1C, BCS1L, COQ3, CS, DECR1, DHRS4, ETFA, GOT2, HSDL2, IDH2, IMMT, MCCC1, MLYCD, NDUFA10, NDUFS1, NNT, PDHB, SDHA, SLC25A12, SLC25A20, SUCLA2, UQCRC2 |
| GO:CC mitochondrial matrix | 0.00921 | ACAA2, ACADM, ACADVL, ACAT1, ACO2, ATP5F1C, CS, DECR1, ETFA, GOT2, IDH2, MCCC1, MLYCD, NDUFA10, NDUFS1, PDHB, SDHA, SUCLA2 |
| GO:BP small molecule metabolic process | 0.0186 | ACAA2, ACADM, ACADVL, ACAT1, ACO2, ACSL1, ATP5F1C, COQ3, CS, DECR1, DHRS4, ETFA, GOT2, IDH2, MCCC1, MLYCD, NDUFA10, NDUFS1, NNT, PDHB, SDHA, SLC25A12, SUCLA2 |
| GO:BP tricarboxylic acid cycle | 0.0466 | ACO2, CS, IDH2, NNT, PDHB, SDHA, SUCLA2 |

### STRING and hu.MAP

STRING provides extensive prior support for the module's interpretation. The strongest known relationships connect enzymes within fatty-acid oxidation, the TCA cycle, respiratory-chain electron transfer, and ATP production. Examples include the ACO2–CS–IDH2–SDHA core, the NDUFA10–NDUFS1–UQCRC2 respiratory-chain connections, and links among ACADM, ACADVL, ETFA, ACAA2, ACAT1, and related lipid-oxidation proteins. These relationships mean that much of the co-abundance structure recapitulates established biochemical coupling rather than representing entirely unknown associations. The STRING enrichment terms for mitochondrial localization and oxidative energy production (STRING COMPARTMENTS Mitochondrion; within-query FDR = 1.11e-06), (STRING Keyword Mitochondrion; within-query FDR = 6.41e-06), (STRING Component Mitochondrion; within-query FDR = 1.02e-05), (STRING Component Mitochondrial matrix; within-query FDR = 0.0037), (STRING Process Energy derivation by oxidation of organic compounds; within-query FDR = 0.0086), (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.0197), and (STRING Process Generation of precursor metabolites and energy; within-query FDR = 0.0242) are concordant supplementary evidence, but they are not additional globally corrected GO evidence. hu.MAP supports several partial complexes: ACADM, ETFA, and NNT occur together in (hu.MAP huMAP3_12388.1); ACADVL and DHRS4 recur in (hu.MAP huMAP3_08580.1) through (hu.MAP huMAP3_10506.1); MYOM1 and TTN occur in muscle-associated complexes (hu.MAP huMAP3_03011.1) and (hu.MAP huMAP3_10383.1) through (hu.MAP huMAP3_14138.1); and NDUFA10 with NDUFS1 recur in respiratory-complex assemblies (hu.MAP huMAP3_07653.1) and (hu.MAP huMAP3_02819.1) through (hu.MAP huMAP3_14878.1). The ACAA2–MCCC1 association in (hu.MAP huMAP3_13468.1) also supports mitochondrial metabolic organization. However, most hu.MAP complexes contain only a subset of their members in this module, so the module should not be interpreted as a single intact physical complex.

**STRING interactions (score >= 0.7)**: 78 of 496 gene pairs: ACAA2–ACADM (0.937); ACAA2–ACADVL (0.983); ACAA2–ACAT1 (0.963); ACAA2–ACO2 (0.75); ACAA2–ACSL1 (0.788); ACAA2–CS (0.946); ACAA2–ETFA (0.858); ACAA2–HSDL2 (0.918); ACAA2–SDHA (0.753); ACAA2–SUCLA2 (0.898); ACADM–ACADVL (0.713); ACADM–ACAT1 (0.717); ACADM–ACSL1 (0.728); ACADM–DECR1 (0.755); ACADM–ETFA (0.995); ACADM–HSDL2 (0.835); ACADM–SLC25A20 (0.721); ACADM–SUCLA2 (0.755); ACADVL–ACSL1 (0.841); ACADVL–ETFA (0.877); ACADVL–HSDL2 (0.787); ACADVL–SLC25A20 (0.776); ACAT1–CS (0.977); ACAT1–ETFA (0.821); ACAT1–HSDL2 (0.909); ACAT1–MLYCD (0.931); ACAT1–SDHA (0.762); ACAT1–SUCLA2 (0.883); ACO2–CS (0.999); ACO2–GOT2 (0.753); ACO2–IDH2 (0.998); ACO2–NDUFA10 (0.747); ACO2–NDUFS1 (0.865); ACO2–SDHA (0.975); ACO2–SUCLA2 (0.862); ACO2–UQCRC2 (0.879); ATP5F1C–CS (0.726); ATP5F1C–ETFA (0.715); ATP5F1C–NDUFA10 (0.919); ATP5F1C–NDUFS1 (0.959); ATP5F1C–PDHB (0.913); ATP5F1C–SDHA (0.75); ATP5F1C–SUCLA2 (0.751); ATP5F1C–UQCRC2 (0.98); BCS1L–NDUFS1 (0.73); BCS1L–SDHA (0.838); BCS1L–UQCRC2 (0.92); CS–GOT2 (0.952); CS–IDH2 (0.994); CS–NDUFS1 (0.737); CS–PDHB (0.941); CS–SDHA (0.984); CS–SUCLA2 (0.96); CS–UQCRC2 (0.746); ETFA–PDHB (0.728); ETFA–SDHA (0.706); ETFA–UQCRC2 (0.757); GOT2–IDH2 (0.96); GOT2–SDHA (0.981); IDH2–NNT (0.898); IDH2–SDHA (0.869); IDH2–SUCLA2 (0.857); IMMT–NDUFS1 (0.901); IMMT–UQCRC2 (0.811); MYOM1–TTN (0.728); NDUFA10–NDUFS1 (0.999); NDUFA10–SDHA (0.793); NDUFA10–UQCRC2 (0.986); NDUFS1–PDHB (0.809); NDUFS1–SDHA (0.995); NDUFS1–SUCLA2 (0.777); NDUFS1–UQCRC2 (0.998); PDHB–SDHA (0.731); PDHB–SUCLA2 (0.921); PDHB–UQCRC2 (0.905); SDHA–SUCLA2 (0.998); SDHA–UQCRC2 (0.99); SUCLA2–UQCRC2 (0.7)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Mitochondrion (FDR = 1.11e-06, 29 genes); Keyword Mitochondrion (FDR = 6.41e-06, 27 genes); Keyword Transit peptide (FDR = 7.73e-06, 23 genes); Component Mitochondrion (FDR = 1.02e-05, 29 genes); TISSUES Left ventricle (FDR = 2.65e-05, 15 genes); TISSUES Cardiovascular system (FDR = 0.00016, 22 genes); TISSUES Heart (FDR = 0.00023, 20 genes); Component Mitochondrial matrix (FDR = 0.0037, 18 genes); Process Energy derivation by oxidation of organic compounds (FDR = 0.0086, 15 genes); PMID (2023) Transcriptomic Analysis in the Hippocampus and Retina of Tg2576 AD Mice Reveals Defective Mitochondrial Oxidative Phosphorylation and Recovery by Tau 12A12mAb Treatment. (FDR = 0.0195, 13 genes); PMID (2022) The intra-mitochondrial O-GlcNAcylation system rapidly modulates OXPHOS function and ROS release in the heart. (FDR = 0.0195, 14 genes); PMID (2020) Effects of an early life diet containing large phospholipid-coated lipid globules on hepatic lipid metabolism in mice. (FDR = 0.0195, 12 genes); PMID (2019) Maternal diet deficient in riboflavin induces embryonic death associated with alterations in the hepatic proteome of duck embryos. (FDR = 0.0195, 11 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.0197, 16 genes); Process Generation of precursor metabolites and energy (FDR = 0.0242, 16 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12388.1 (ACADM, ETFA, NNT; 3/7); huMAP3_08580.1 (ACADVL, DHRS4; 2/2); huMAP3_02431.1 (ACADVL, DHRS4; 2/3); huMAP3_11915.1 (ACADVL, DHRS4; 2/3); huMAP3_10506.1 (ACADVL, DHRS4; 2/4); huMAP3_03011.1 (MYOM1, TTN; 2/6); huMAP3_07653.1 (NDUFA10, NDUFS1; 2/7); huMAP3_10383.1 (MYOM1, TTN; 2/8); huMAP3_07933.1 (MYOM1, TTN; 2/17); huMAP3_09076.1 (MYOM1, TTN; 2/25); huMAP3_10799.1 (MYOM1, TTN; 2/26); huMAP3_14138.1 (MYOM1, TTN; 2/30); huMAP3_02819.1 (NDUFA10, NDUFS1; 2/34); huMAP3_14018.1 (NDUFA10, NDUFS1; 2/48); huMAP3_06397.1 (NDUFA10, NDUFS1; 2/49); huMAP3_09982.1 (NDUFA10, NDUFS1; 2/49); huMAP3_09567.1 (NDUFA10, NDUFS1; 2/52); huMAP3_14878.1 (NDUFA10, NDUFS1; 2/53); huMAP3_13468.1 (ACAA2, MCCC1; 2/99)

### Novelty

This module is unlikely to be a wholly new molecular pathway: its dominant mitochondrial, TCA-cycle, respiratory-chain, and fatty-acid-oxidation relationships are already represented in STRING and, for selected subsets, in hu.MAP. The finding may nevertheless be novel at the level of cross-tissue co-abundance organization. The particular coordinated module shared by bone marrow and heart, including its mixture of metabolic, respiratory, and muscle-structural genes, is not established as a known complex by the supplied evidence. Absence of some genes or edges from STRING or hu.MAP should not be treated as proof of novelty, because those resources capture curated interactions and experimentally supported complexes rather than every tissue-specific abundance relationship. The appropriate conclusion is therefore partial novelty: established biochemical content arranged in a potentially informative conserved tissue-pair co-abundance pattern.

**Hypothesis.** Hypothesis: the module represents a conserved energetic program that coordinates mitochondrial substrate use with high ATP demand in metabolically active cells shared between bone marrow and heart. Fatty-acid entry and beta-oxidation may feed acetyl-CoA and reducing equivalents into the TCA cycle; the TCA cycle and respiratory-chain components may then support proton-gradient formation and ATP synthesis. NNT and IDH2 could help maintain mitochondrial reducing power and redox buffering, while MYOM1, TTN, and LAMA2 may couple this energetic state to muscle-associated structure or extracellular support. This hypothesis predicts that module abundance should track mitochondrial capacity and oxidative workload, but it does not establish direct regulation or physical interaction among all module genes.

### Important genes

#### ACO2

- **Related proteins** (co-abundance neighbors): NNT (0.91), GOT2 (0.88), IDH2 (0.88), IMMT (0.86), ACADVL (0.86), CS (0.86), TTN (0.85), ACADM (0.84), PDHB (0.84), ACAT1 (0.82), SDHA (0.81), ETFA (0.80); STRING partners: ACAA2 (0.75), CS (0.999), GOT2 (0.753), IDH2 (0.998), NDUFA10 (0.747), NDUFS1 (0.865), SDHA (0.975), SUCLA2 (0.862), UQCRC2 (0.879)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aconitase 2. The protein encoded by this gene belongs to the aconitase/IPM isomerase family. It is an enzyme that catalyzes the interconversion of citrate to isocitrate via cis-aconitate in the second step of the TCA cycle. This protein is encoded in the nucleus and functions in the mitochondrion. It was found to be one of the mitochondrial matrix proteins that are preferentially degraded by the serine proteas…
- **Diseases (Open Targets)**: infantile cerebellar-retinal degeneration (0.814); optic atrophy 9 (0.693); autosomal dominant optic atrophy, classic form (0.619); optic atrophy (0.601); mitochondrial disease (0.505)
- **Europe PMC papers**: 3559
- **Why important**: ACO2 is a central network connector with high weighted connectivity and links to CS, IDH2, SDHA, NDUFA10, NDUFS1, UQCRC2, and fatty-acid-oxidation genes. It is present in every primary enriched term (GO:CC mitochondrion; q_global = 0.000333) through (GO:BP tricarboxylic acid cycle; q_global = 0.0466), is mitochondrial by HPA, and catalyzes a key TCA-cycle step. Its disease associations include mitochondrial disease and optic-atrophy-related disorders, and it has extensive literature support.
- **Conclusion**: Established evidence supports ACO2 as a central TCA-cycle and mitochondrial-energy marker of the module. It is a strong candidate for representing the metabolic backbone of the co-abundance pattern. A module-specific regulatory role remains a hypothesis.

#### CS

- **Related proteins** (co-abundance neighbors): GOT2 (0.91), MYOM1 (0.86), ACO2 (0.86), IDH2 (0.84), NNT (0.81), LAMA2 (0.81); STRING partners: ACAA2 (0.946), ACAT1 (0.977), ACO2 (0.999), ATP5F1C (0.726), GOT2 (0.952), IDH2 (0.994), NDUFS1 (0.737), PDHB (0.941), SDHA (0.984), SUCLA2 (0.96), UQCRC2 (0.746)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS is a highly connected TCA-cycle enzyme linked in STRING to ACO2, IDH2, GOT2, SDHA, SUCLA2, PDHB, and respiratory-chain proteins. It belongs to all primary enriched terms (GO:CC mitochondrion; q_global = 0.000333) through (GO:BP tricarboxylic acid cycle; q_global = 0.0466), is mitochondrial by HPA, and catalyzes citrate formation at the entry point of the TCA cycle. Its very large literature base and established metabolic function make it a particularly robust module anchor.
- **Conclusion**: Established evidence identifies CS as a core indicator of mitochondrial oxidative metabolism and TCA-cycle capacity. Its co-abundance with lipid-oxidation and respiratory-chain genes supports coordinated pathway activity, while direct control of the module cannot be inferred.

#### NNT

- **Related proteins** (co-abundance neighbors): ACO2 (0.91), TTN (0.88), ACADVL (0.87), IDH2 (0.85), MYOM1 (0.85), PDHB (0.82), CS (0.81); STRING partners: IDH2 (0.898)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: huMAP3_12388.1
- **Function (MyGene.info)**: nicotinamide nucleotide transhydrogenase. This gene encodes an integral protein of the inner mitochondrial membrane. The enzyme couples hydride transfer between NAD(H) and NADP(+) to proton translocation across the inner mitochondrial membrane. Under most physiological conditions, the enzyme uses energy from the mitochondrial proton gradient to produce high concentrations of NADPH. The resulting NADPH is used for biosynthesis and in free …
- **Diseases (Open Targets)**: familial glucocorticoid deficiency (0.638); neurodegenerative disease (0.497); hereditary disease (0.453); atypical hemolytic-uremic syndrome with DGKE deficiency (0.416); Abnormality of the skeletal system (0.396)
- **Europe PMC papers**: 6111
- **Why important**: NNT connects ACO2, IDH2, CS, PDHB, ACADVL, and the muscle-associated genes MYOM1 and TTN. It is included in the mitochondrion, small-molecule metabolism, and TCA-cycle primary terms (GO:CC mitochondrion; q_global = 0.000333), (GO:BP small molecule metabolic process; q_global = 0.0186), and (GO:BP tricarboxylic acid cycle; q_global = 0.0466). NNT generates mitochondrial NADPH and contributes to reactive-oxygen-species metabolism, with HPA support for cardiomyocytes and metabolically active tissues. It also has substantial disease and literature support.
- **Conclusion**: Established evidence supports NNT as a redox-balancing component that links mitochondrial energy production to antioxidant capacity. Its position suggests a plausible bridge between substrate oxidation and redox control, but a causal redox role in this specific module remains hypothetical.

#### ACADVL

- **Related proteins** (co-abundance neighbors): NNT (0.87), ACO2 (0.86), GOT2 (0.86), MYOM1 (0.83), IDH2 (0.83), AIFM1 (0.81); STRING partners: ACAA2 (0.983), ACADM (0.713), ACSL1 (0.841), ETFA (0.877), HSDL2 (0.787), SLC25A20 (0.776)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: huMAP3_08580.1, huMAP3_02431.1, huMAP3_11915.1, huMAP3_10506.1
- **Function (MyGene.info)**: acyl-CoA dehydrogenase very long chain. The protein encoded by this gene is targeted to the inner mitochondrial membrane where it catalyzes the first step of the mitochondrial fatty acid beta-oxidation pathway. This acyl-Coenzyme A dehydrogenase is specific to long-chain and very-long-chain fatty acids. A deficiency in this gene product reduces myocardial fatty acid beta-oxidation and is associated with cardiomyopathy. Alternative splic…
- **Diseases (Open Targets)**: very long chain acyl-CoA dehydrogenase deficiency (0.865); hereditary disease (0.531); long chain acyl-CoA dehydrogenase deficiency (0.506); rhabdomyolysis (0.464); Acute rhabdomyolysis (0.436)
- **Europe PMC papers**: 3504
- **Why important**: ACADVL links fatty-acid oxidation with the central metabolic network through ACAA2, ACADM, ACSL1, ETFA, HSDL2, SLC25A20, ACO2, GOT2, IDH2, and NNT. It is included in the mitochondrial and small-molecule primary terms (GO:CC mitochondrion; q_global = 0.000333), (GO:CC mitochondrial matrix; q_global = 0.00921), and (GO:BP small molecule metabolic process; q_global = 0.0186). HPA supports cardiomyocyte and muscle relevance, and its deficiency is associated with impaired myocardial fatty-acid oxidation, cardiomyopathy, and rhabdomyolysis. The gene also participates in several hu.MAP metabolic complexes (hu.MAP huMAP3_08580.1) through (hu.MAP huMAP3_10506.1).
- **Conclusion**: Established evidence supports ACADVL as a biologically important fatty-acid entry point for the module, especially in heart and muscle. It may help explain why the conserved module is prominent in energetically demanding tissues, but the co-abundance data alone do not establish altered fatty-acid flux.

#### NDUFS1

- **Related proteins** (co-abundance neighbors): MYOM1 (0.81); STRING partners: ACO2 (0.865), ATP5F1C (0.959), BCS1L (0.73), CS (0.737), IMMT (0.901), NDUFA10 (0.999), PDHB (0.809), SDHA (0.995), SUCLA2 (0.777), UQCRC2 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_07653.1, huMAP3_02819.1, huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S1. The protein encoded by this gene belongs to the complex I 75 kDa subunit family. Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Thi…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 5 (0.810); mitochondrial complex I deficiency (0.647); type 2 diabetes mellitus (0.608); Parkinson disease (0.603); diabetes mellitus (0.580)
- **Europe PMC papers**: 2567
- **Why important**: NDUFS1 is the largest core subunit of mitochondrial complex I and connects to NDUFA10, UQCRC2, SDHA, ATP5F1C, PDHB, and several TCA-cycle proteins in STRING. It is present in the mitochondrial, matrix, and small-molecule primary terms (GO:CC mitochondrion; q_global = 0.000333), (GO:CC mitochondrial matrix; q_global = 0.00921), and (GO:BP small molecule metabolic process; q_global = 0.0186). Its repeated occurrence with NDUFA10 in hu.MAP respiratory-complex assemblies (hu.MAP huMAP3_07653.1) and (hu.MAP huMAP3_02819.1) through (hu.MAP huMAP3_14878.1), together with associations with complex I deficiency and Parkinson disease, makes it important for interpreting respiratory-chain capacity.
- **Conclusion**: Established evidence supports NDUFS1 as a respiratory-chain component connecting upstream carbon metabolism to oxidative phosphorylation. Its inclusion strengthens the interpretation that the module reflects integrated mitochondrial respiration rather than isolated TCA activity.

#### MYOM1

- **Related proteins** (co-abundance neighbors): AIFM1 (0.95), GOT2 (0.93), NDUFA10 (0.92), ATP5F1C (0.87), CS (0.86), DHRS4 (0.86), MLYCD (0.86), HSDL2 (0.85), NNT (0.85), ACADVL (0.83), SLC25A12 (0.83), SLC25A20 (0.83), ACSL1 (0.83), NDUFS1 (0.81); STRING partners: TTN (0.728)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_03011.1, huMAP3_10383.1, huMAP3_07933.1, huMAP3_09076.1, huMAP3_10799.1, huMAP3_14138.1
- **Function (MyGene.info)**: myomesin 1. The giant protein titin, together with its associated proteins, interconnects the major structure of sarcomeres, the M bands and Z discs. The C-terminal end of the titin string extends into the M line, where it binds tightly to M-band constituents of apparent molecular masses of 190 kD (myomesin 1) and 165 kD (myomesin 2). This protein, myomesin 1, like myomesin 2, titin, and other myofibrillar pr…
- **Diseases (Open Targets)**: Hypoglycemia (0.266); Non-immune hydrops fetalis (0.266); Abnormality of the liver (0.266); breast disorder (0.251); age-related macular degeneration (0.248)
- **Europe PMC papers**: 859
- **Why important**: MYOM1 has among the strongest network connectivity in the module and links structural muscle biology to many metabolic genes, including AIFM1, GOT2, NDUFA10, ATP5F1C, CS, DHRS4, and MLYCD. HPA places it in heart muscle, skeletal muscle, cardiomyocytes, and myonuclei, while its known function concerns sarcomere and M-band organization. It occurs with TTN in multiple muscle-associated hu.MAP complexes (hu.MAP huMAP3_03011.1) and (hu.MAP huMAP3_10383.1) through (hu.MAP huMAP3_14138.1), and STRING supports the MYOM1–TTN relationship (STRING TISSUES Left ventricle; within-query FDR = 2.65e-05) through (STRING TISSUES Heart; within-query FDR = 0.00023).
- **Conclusion**: Established evidence supports MYOM1 as the principal structural and tissue-context marker within the module, rather than as a mitochondrial enzyme. Its connection to metabolic genes may reflect coordinated abundance in muscle-rich samples or energetic coupling to contractile architecture; a direct molecular bridge remains a hypothesis.

## Module 1

**Tissue pair**: bone_marrow and heart  
**Genes (5)**: ACSS1, CPT2, DMD, PLEC, ALDH5A1

### Function

The module most plausibly represents a combined mitochondrial energy-metabolism and muscle-cell structural program. CPT2 supports mitochondrial long-chain fatty-acid oxidation, ACSS1 supports mitochondrial acetyl-CoA production, and ALDH5A1 supports mitochondrial succinate-semialdehyde and GABA-related metabolism. DMD and PLEC support cytoskeletal organization, cell-matrix linkage, muscle integrity, and tissue architecture. DMD is the central co-abundance node and connects the metabolic genes with PLEC, suggesting coordination between energetic capacity and cytoskeletal or contractile-cell state. No GO/KEGG term passed global correction, so this functional interpretation is based on the individual gene annotations, network structure, tissue evidence, and complex data rather than on significant pathway enrichment.

**Cell composition.** The module is not composed of plasma or secreted proteins: the secreted-gene annotation is absent for every member. It is also not blood-cell enriched; the HPA evidence indicates low immune-cell specificity for most members and absence from immune cells for DMD, with no enriched blood-cell category. Instead, the genes show tissue or cell-type enhancement across liver, skeletal muscle, choroid plexus, cardiomyocytes, hepatocytes, glial populations, and other specialized cell types. Protein detection is stronger in heart than in bone marrow, although ALDH5A1 and ACSS1 are detected in both tissues. Therefore, the shared bone-marrow–heart module is more consistent with a conserved metabolic and structural program, or with shared specialized cell populations, than with a circulating-protein or immune-cell contamination signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence known relationship within the module, DMD–PLEC, supporting a real cytoskeletal association between dystrophin and plectin. The other co-abundance links are not represented as high-confidence STRING interactions in the supplied evidence, so they should not be treated as established physical interactions. hu.MAP provides complex evidence (hu.MAP huMAP3_13468.1) linking CPT2 and ACSS1 within a very large mitochondrial and metabolic complex. This supports shared participation in mitochondrial metabolism, but the module members constitute only a small subset of that complex and the evidence does not establish a dedicated five-gene complex. Overall, the resources support a known DMD–PLEC structural relationship and a broader CPT2–ACSS1 metabolic context, while the remaining module edges are primarily co-abundance relationships.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: DMD–PLEC (0.902)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (CPT2, ACSS1; 2/99)

### Novelty

The module-level observation may be a new cross-tissue co-abundance pattern because the supplied resources contain limited direct support for most of its edges and no STRING functional-enrichment result. However, it cannot be claimed as a newly discovered molecular interaction or pathway. DMD–PLEC is already supported by STRING, and CPT2–ACSS1 already co-occur in hu.MAP complex (hu.MAP huMAP3_13468.1). The absence of the other relationships from STRING or hu.MAP does not prove novelty, because those databases are incomplete and measure different kinds of evidence. The defensible novelty claim is therefore the conserved association of mitochondrial metabolic genes with a DMD–PLEC structural program across bone marrow and heart, pending replication in independent data.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of an energy-supply and structural-maintenance state in specialized cells shared between bone marrow and heart. Mitochondrial fatty-acid oxidation and acetyl-CoA generation may support energetic demand, while ALDH5A1 may mark related mitochondrial metabolic capacity and DMD–PLEC may maintain cytoskeletal continuity and mechanical resilience. The shared signal could arise from a conserved cell-state program or from related specialized cell populations present in both tissue preparations. This is a mechanistic hypothesis, not a demonstrated causal pathway; testing would require independent cohorts, cell-resolved data, and perturbation or protein-interaction experiments.

### Important genes

#### DMD

- **Related proteins** (co-abundance neighbors): CPT2 (0.85), ALDH5A1 (0.84), ACSS1 (0.81), PLEC (0.81); STRING partners: PLEC (0.902)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dystrophin. This gene spans a genomic range of greater than 2 Mb and encodes a large protein containing an N-terminal actin-binding domain and multiple spectrin repeats. The encoded protein forms a component of the dystrophin-glycoprotein complex (DGC), which bridges the inner cytoskeleton and the extracellular matrix. Deletions, duplications, and point mutations at this gene locus may cause Duchenne muscular…
- **Diseases (Open Targets)**: Duchenne muscular dystrophy (0.868); Becker muscular dystrophy (0.825); dilated cardiomyopathy 3B (0.786); muscular dystrophy (0.660); progressive muscular dystrophy (0.642)
- **Europe PMC papers**: 23282
- **Why important**: DMD is the central network node, connected to every other module member, and is the strongest bridge between the structural and metabolic portions of the module. Its established role in the dystrophin-glycoprotein complex, cytoskeletal organization, muscle contraction, and heart-rate regulation is consistent with the heart signal. It has extensive disease and literature support, including Duchenne and Becker muscular dystrophies and cardiomyopathy.
- **Conclusion**: Established evidence supports DMD as the principal structural and cardiac-muscle component of the module. It is plausible, but not proven, that DMD coordinates the observed metabolic co-abundance pattern.

#### PLEC

- **Related proteins** (co-abundance neighbors): DMD (0.81); STRING partners: DMD (0.902)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments, Cytosol; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plectin. Plectin is a prominent member of an important family of structurally and in part functionally related proteins, termed plakins or cytolinkers, that are capable of interlinking different elements of the cytoskeleton. Plakins, with their multi-domain structure and enormous size, not only play crucial roles in maintaining cell and tissue integrity and orchestrating dynamic changes in cytoarchitecture…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 5B, with muscular dystrophy (0.796); epidermolysis bullosa simplex 5A, Ogna type (0.775); autosomal recessive limb-girdle muscular dystrophy type 2Q (0.768); epidermolysis bullosa simplex 5C, with pyloric atresia (0.755); epidermolysis bullosa simplex with nail dystrophy (0.695)
- **Europe PMC papers**: 2578
- **Why important**: PLEC is the module's second structural anchor and has the only supplied high-confidence STRING relationship, with DMD. Plectin is an established cytolinker and scaffold for intermediate filaments, cytosol, cell shape, and tissue integrity. Its skeletal-muscle enhancement and associations with epidermolysis bullosa and muscular dystrophy make it biologically important for interpreting the structural side of the module.
- **Conclusion**: Established evidence supports PLEC as a cytoskeletal partner of DMD and a marker of tissue-integrity biology. Its connection to the mitochondrial genes remains a module-level hypothesis rather than a demonstrated direct interaction.

#### CPT2

- **Related proteins** (co-abundance neighbors): DMD (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: carnitine palmitoyltransferase 2. The protein encoded by this gene is a nuclear protein which is transported to the mitochondrial inner membrane. Together with carnitine palmitoyltransferase I, the encoded protein oxidizes long-chain fatty acids in the mitochondria. Defects in this gene are associated with mitochondrial long-chain fatty-acid (LCFA) oxidation disorders. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: carnitine palmitoyl transferase II deficiency, myopathic form (0.830); carnitine palmitoyl transferase II deficiency, severe infantile form (0.800); carnitine palmitoyl transferase II deficiency, neonatal form (0.772); carnitine palmitoyltransferase II deficiency (0.710); hereditary disease (0.505)
- **Europe PMC papers**: 5133
- **Why important**: CPT2 is the clearest lipid-energy gene in the module. It encodes the mitochondrial carnitine palmitoyltransferase component required for long-chain fatty-acid oxidation and is associated with multiple forms of carnitine palmitoyltransferase deficiency. It participates with ACSS1 in hu.MAP complex (hu.MAP huMAP3_13468.1), while its peripheral network position indicates that its importance is functional rather than topological.
- **Conclusion**: Established evidence supports CPT2 as a mitochondrial fatty-acid oxidation component and supports its metabolic association with ACSS1 through (hu.MAP huMAP3_13468.1). Its co-abundance with DMD may reflect shared energetic demand in muscle-related cells, but that interpretation remains a hypothesis.

#### ACSS1

- **Related proteins** (co-abundance neighbors): DMD (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: acyl-CoA synthetase short chain family member 1. This gene encodes a mitochondrial acetyl-CoA synthetase enzyme. A similar protein in mice plays an important role in the tricarboxylic acid cycle by catalyzing the conversion of acetate to acetyl CoA. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Nov 2011].
- **Diseases (Open Targets)**: response to antihypertensive drug (0.284); neurodegenerative disease (0.220); acute myeloid leukemia (0.061); neoplasm (0.048); hepatocellular carcinoma (0.039)
- **Europe PMC papers**: 1022
- **Why important**: ACSS1 provides a complementary mitochondrial metabolic function by producing acetyl-CoA from acetate and contributing to acetate and propionate metabolism. It is detected in both relevant tissues, shows choroid-plexus and glial-related enhancement, and shares hu.MAP complex (hu.MAP huMAP3_13468.1) with CPT2. Its disease literature is more limited than that of DMD or CPT2, which makes the cross-tissue network context especially informative.
- **Conclusion**: Established evidence supports ACSS1 as a mitochondrial acetyl-CoA metabolism gene and supports its complex-level relationship with CPT2. Its possible role in linking substrate metabolism to the DMD–PLEC structural program is a hypothesis.

#### ALDH5A1

- **Related proteins** (co-abundance neighbors): DMD (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 5 family member A1. This protein belongs to the aldehyde dehydrogenase family of proteins. This gene encodes a mitochondrial NAD(+)-dependent succinic semialdehyde dehydrogenase. A deficiency of this enzyme, known as 4-hydroxybutyricaciduria, is a rare inborn error in the metabolism of the neurotransmitter 4-aminobutyric acid (GABA). In response to the defect, physiologic fluids from patients accumulate GHB, a compou…
- **Diseases (Open Targets)**: succinic semialdehyde dehydrogenase deficiency (0.843); epilepsy (0.608); bipolar disorder (0.607); Seizure (0.595); major depressive disorder (0.576)
- **Europe PMC papers**: 1100
- **Why important**: ALDH5A1 adds a distinct mitochondrial metabolic axis through succinic semialdehyde dehydrogenase activity, the GABA shunt, and succinate-related metabolism. It is detected in both bone marrow and heart, is liver-enhanced, and has established associations with succinic semialdehyde dehydrogenase deficiency and neurological disease. Its peripheral network position means that it may be a state marker rather than a physical connector.
- **Conclusion**: Established evidence supports ALDH5A1 as a mitochondrial metabolic component with neurological disease relevance. Its inclusion in this module supports a broad mitochondrial-state interpretation, but no direct biochemical or physical link to DMD, PLEC, CPT2, or ACSS1 is established by the supplied data.

## Module 2

**Tissue pair**: bone_marrow and heart  
**Genes (6)**: AHNAK, HSPA5, GBE1, HSPA8, PALLD, PDLIM1

### Function

No GO/KEGG term passed global correction, so the module does not have a globally significant pathway annotation. Its most coherent functional signal is a structural and proteostasis-related program: PALLD, PDLIM1, and AHNAK are associated with actin filaments, cytoskeletal organization, adhesion, migration, or membrane structure; GBE1 supports glycogen branching and carbohydrate metabolism; and HSPA5 with HSPA8 supports protein folding and cellular stress handling. The supplementary STRING term (STRING COMPARTMENTS Focal adhesion; within-query FDR = 0.0451) identifies focal adhesion, but this is not global enrichment evidence. The sparse network, centered on PALLD, is consistent with a cytoskeletal scaffold connected to metabolic and chaperone functions rather than a well-defined canonical pathway.

**Cell composition.** The module is not predominantly plasma or secreted: only one member is annotated as secreted, while the proteins are mainly intracellular, cytosolic, membrane-associated, or localized to actin filaments. Most genes have low tissue specificity, although PDLIM1 and GBE1 are tissue enhanced in skeletal muscle and several genes are cell-type enhanced in cardiomyocytes or myonuclei. Blood-cell specificity is generally low, with selected enrichment for basophils, eosinophils, memory B cells, or naive B cells. Protein detection in both bone marrow and heart supports genuine presence in both tissues. Thus, the shared signal is more plausibly related to broadly expressed structural, metabolic, and proteostasis biology, with possible contributions from muscle or cardiac cells, than to a predominantly plasma-protein or blood-cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides strong direct support only for the HSPA5-HSPA8 relationship. The supplementary focal-adhesion term (STRING COMPARTMENTS Focal adhesion; within-query FDR = 0.0451) contains HSPA5, PDLIM1, AHNAK, PALLD, and HSPA8, supporting a possible adhesion-associated context but not a globally corrected enrichment claim. The remaining module relationships are not represented as high-confidence STRING interactions in the supplied evidence. No hu.MAP complex contains multiple module members. Therefore, the co-abundance structure extends beyond currently catalogued physical interactions and should not be interpreted as a demonstrated protein complex.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: HSPA5–HSPA8 (0.983)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Focal adhesion (FDR = 0.0451, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is not established as a new molecular complex or pathway: the HSPA5-HSPA8 interaction and the individual functions of the genes are already known, and the focal-adhesion context is represented in STRING. However, the specific conserved co-abundance combination across bone marrow and heart may be a novel systems-level observation because most pairwise relationships lack high-confidence STRING support and no shared hu.MAP complex is reported. The absence of database interactions alone does not prove novelty. A claim of novelty would require replication, comparison with published co-expression modules, and independent validation in additional datasets.

**Hypothesis.** Hypothesis: the conserved module reflects coordinated maintenance of cytoskeletal and adhesion architecture in mechanically active or structurally specialized cells, coupled to proteostasis and energy buffering. PALLD may organize actin-associated structure and connect PDLIM1 and AHNAK-related membrane or cytoskeletal functions, while HSPA5 and HSPA8 may buffer folding and trafficking stress. GBE1 may provide glycogen-branching capacity for local carbohydrate storage or energy demands. In heart, this could relate to cardiomyocyte or muscle structural and metabolic demands; in bone marrow, it could reflect shared stromal, megakaryocytic, or other structurally active cell populations. This is a mechanistic hypothesis, not a demonstrated causal pathway.

### Important genes

#### PALLD

- **Related proteins** (co-abundance neighbors): PDLIM1 (0.84), GBE1 (0.84), HSPA5 (0.83), AHNAK (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: palladin, cytoskeletal associated protein. This gene encodes a cytoskeletal protein that is required for organizing the actin cytoskeleton. The protein is a component of actin-containing microfilaments, and it is involved in the control of cell shape, adhesion, and contraction. Polymorphisms in this gene are associated with a susceptibility to pancreatic cancer type 1, and also with a risk for myocardial infarction. Alternative splicing re…
- **Diseases (Open Targets)**: coronary artery disorder (0.444); exocrine pancreatic carcinoma (0.372); coronary atherosclerosis (0.360); Bicuspid aortic valve (0.325); aortic stenosis (0.319)
- **Europe PMC papers**: 1170
- **Why important**: PALLD has the strongest module connectivity and links the actin-associated members PDLIM1 and AHNAK with HSPA5 and GBE1. Its documented role in actin-cytoskeleton organization, cell shape, adhesion, migration, and contraction makes it the principal structural candidate. It is detected in heart, is cell-type enhanced in cardiomyocytes and myonuclei, has cardiovascular disease associations, and has substantial literature support.
- **Conclusion**: Established evidence supports PALLD as the central structural organizer of this module and as a plausible contributor to the shared heart-associated signal. Its role as the causal bridge between cytoskeletal, chaperone, and glycogen-related components remains a hypothesis.

#### HSPA5

- **Related proteins** (co-abundance neighbors): HSPA8 (0.85), PALLD (0.83); STRING partners: HSPA8 (0.983)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is directly connected to HSPA8 by the strongest STRING relationship in the module and also connects to PALLD in the co-abundance network. It is an ER HSP70 chaperone and regulator of ER homeostasis, protein folding, and the unfolded-protein response. It is detected in both tissues, has very substantial literature support, and is included in the supplementary focal-adhesion term (STRING COMPARTMENTS Focal adhesion; within-query FDR = 0.0451).
- **Conclusion**: Established evidence supports HSPA5 as the module's main proteostasis component and confirms a known relationship with HSPA8. Its participation in a shared cytoskeletal-proteostasis program across heart and bone marrow is a hypothesis.

#### HSPA8

- **Related proteins** (co-abundance neighbors): HSPA5 (0.85); STRING partners: HSPA5 (0.983)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Flagellar centriole, Annulus; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 8. This gene encodes a member of the heat shock protein 70 family, which contains both heat-inducible and constitutively expressed members. This protein belongs to the latter group, which are also referred to as heat-shock cognate proteins. It functions as a chaperone, and binds to nascent polypeptides to facilitate correct folding. It also functions as an ATPase in the disassembly of clathrin-coated…
- **Diseases (Open Targets)**: dengue disease (0.505); systemic lupus erythematosus (0.375); smoking initiation (0.199); Lennox-Gastaut syndrome (0.118); neoplasm (0.105)
- **Europe PMC papers**: 6937
- **Why important**: HSPA8 is connected to HSPA5 in both the module and STRING, providing the clearest externally supported interaction in the network. It is a constitutive HSP70 chaperone involved in nascent-polypeptide folding, unfolded-protein responses, and vesicle trafficking. It is detected in both tissues and has substantial literature support.
- **Conclusion**: Established evidence supports HSPA8 as a constitutive chaperone partner of HSPA5 and as a contributor to cellular protein quality control. Its specific role in the conserved tissue-pair module is not resolved beyond that established chaperone function.

#### PDLIM1

- **Related proteins** (co-abundance neighbors): PALLD (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Actin filaments; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 1. This gene encodes a member of the enigma protein family. The protein contains two protein interacting domains, a PDZ domain at the amino terminal end and one to three LIM domains at the carboxyl terminal. It is a cytoplasmic protein associated with the cytoskeleton. The protein may function as an adapter to bring other LIM-interacting proteins to the cytoskeleton. Pseudogenes associated with this …
- **Diseases (Open Targets)**: ovarian dysfunction (0.167); atrial fibrillation (0.138); liver disorder (0.126); Peyronie disease (0.117); uterine corpus leiomyoma (0.092)
- **Europe PMC papers**: 1123
- **Why important**: PDLIM1 is tissue enhanced in skeletal muscle, cell-type enhanced in megakaryocytes and platelets, and localized to actin filaments. Its PDZ and LIM domains support adaptor functions linking cytoskeletal proteins, and its annotations include actin organization, heart development, polarity, hypoxia, and oxidative-stress responses. It is connected to the central PALLD node and appears in (STRING COMPARTMENTS Focal adhesion; within-query FDR = 0.0451).
- **Conclusion**: Established evidence supports PDLIM1 as an actin-associated adaptor with relevance to muscle, cardiac development, and selected bone-marrow-associated cell types. Its connection to PALLD suggests a structural submodule, but a direct physical interaction or causal role in the conserved module is not established.

#### GBE1

- **Related proteins** (co-abundance neighbors): PALLD (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 1,4-alpha-glucan branching enzyme 1. The protein encoded by this gene is a glycogen branching enzyme that catalyzes the transfer of alpha-1,4-linked glucosyl units from the outer end of a glycogen chain to an alpha-1,6 position on the same or a neighboring glycogen chain. Branching of the chains is essential to increase the solubility of the glycogen molecule and, consequently, in reducing the osmotic pressure within cells. Highest l…
- **Diseases (Open Targets)**: glycogen storage disease due to glycogen branching enzyme deficiency (0.848); adult polyglucosan body disease (0.801); glycogen storage disease due to glycogen branching enzyme deficiency, adult neuromuscular form (0.711); glycogen storage disease due to glycogen branching enzyme deficiency, congenital neuromuscular form (0.591); disorder of glycogen metabolism (0.573)
- **Europe PMC papers**: 1361
- **Why important**: GBE1 is connected to PALLD and is tissue enhanced in skeletal muscle and cell-type enhanced in cardiomyocytes, myonuclei, neutrophils, and neutrophil progenitors. It catalyzes glycogen branching and is associated with glycogen metabolism and glycogen-storage disease. Its disease annotations are particularly strong for glycogen branching enzyme deficiency, making it the clearest metabolic and disease-relevant member.
- **Conclusion**: Established evidence supports GBE1 as the module's glycogen-metabolism component and links it to clinically important glycogen disorders. Its co-abundance with a cytoskeletal scaffold may indicate coordinated structural-energy biology, but that coupling is a hypothesis.

## Module 3

**Tissue pair**: bone_marrow and heart  
**Genes (15)**: ANXA4, HSD17B4, DYNC1H1, EIF3C, FERMT2, SHMT2, HSD17B10, HPRT1, HK1, PFKP, PSMD13, FARSB, QARS1, RARS1, VPS35

### Function

The module appears to be a heterogeneous cellular-maintenance program rather than a narrowly defined pathway. Its strongest biological themes are intracellular glucose use through HK1 and PFKP, mitochondrial one-carbon and amino-acid metabolism through SHMT2 and HSD17B10, protein synthesis through RARS1, QARS1, FARSB and EIF3C, proteostasis through PSMD13, intracellular trafficking through DYNC1H1 and VPS35, and adhesion or membrane-related organization through FERMT2 and ANXA4. These interpretations come from the individual gene annotations and the co-abundance topology, not from enrichment significance. No GO or KEGG term passed global correction, and there were no supplementary STRING functional-enrichment terms. The absence of a globally enriched term means that the module does not support a single overrepresented pathway at the stated significance standard; it does not make the module biologically false.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the secreted-gene annotation is absent, and the proteins are predominantly intracellular, including cytosolic, mitochondrial, peroxisomal, nuclear-speckle, endosomal or focal-adhesion proteins. HPA indicates generally low immune-cell specificity, with only HSD17B4 immune-cell enhanced in basophils and FERMT2 not detected in immune cells. Thus, a blood-cell explanation is not strongly supported. The module is instead compatible with broadly distributed cellular machinery, although several genes show cell-type enhancement in specialized populations and several show tissue enhancement outside the sampled pair. Protein detection in both bone marrow and heart for most annotated genes supports technical or biological detectability in both tissues, but the lack of detection for some genes means the module need not be uniformly expressed by every cell in either tissue.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a small set of established relationships rather than a densely documented interaction network. The strongest known links are HK1-PFKP, QARS1-RARS1, DYNC1H1-HSD17B10 and the weaker FARSB-RARS1 association. These relationships provide coherent anchors for glycolysis, aminoacyl-tRNA synthetase biology and mitochondrial or motor-associated biology, but most co-abundance edges are not represented by high-confidence STRING interactions. hu.MAP independently places QARS1 and RARS1 together in two aminoacyl-tRNA synthetase-related complexes, (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Because only a subset of each complex is represented, the module is not equivalent to a complete translation complex. Overall, STRING and hu.MAP validate selected local relationships while leaving the broader cross-process co-abundance structure unexplained.

**STRING interactions (score >= 0.7)**: 4 of 105 gene pairs: DYNC1H1–HSD17B10 (0.902); FARSB–RARS1 (0.706); HK1–PFKP (0.995); QARS1–RARS1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (QARS1, RARS1; 2/14); huMAP3_13688.1 (QARS1, RARS1; 2/14)

### Novelty

The individual functions and several gene-gene relationships are established, so the module should not be described as a discovery of a new glycolytic enzyme, aminoacyl-tRNA synthetase complex, dynein component or metabolic pathway. What may be novel is the coordinated co-abundance of this particular combination across bone marrow and heart, especially the connection between glycolysis, mitochondrial one-carbon and lipid metabolism, translation, trafficking and proteostasis. That claim remains provisional because the module has no globally significant GO or KEGG term, no STRING functional-enrichment signal, and limited overlap with known complex membership. Absence from STRING or hu.MAP cannot establish novelty; independent replication, tissue-cell deconvolution and comparison with published co-expression resources would be needed.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular-demand state rather than a dedicated tissue-specific pathway. In cells present in both tissues, increased glucose entry and glycolytic flux through HK1 and PFKP may be coordinated with mitochondrial serine and one-carbon metabolism through SHMT2, fatty-acid or steroid-associated metabolism through HSD17B10 and HSD17B4, and increased synthesis, quality control and trafficking of proteins through the RARS1-QARS1-FARSB, EIF3C, PSMD13, VPS35 and DYNC1H1 components. FERMT2 and ANXA4 could connect this intracellular state to adhesion or membrane organization. This is a mechanistic model, not an established causal pathway: the co-abundance data cannot determine directionality, cell-of-origin, physical interaction or whether the relationships are driven by shared cellular composition.

### Important genes

#### DYNC1H1

- **Related proteins** (co-abundance neighbors): HSD17B4 (0.87), HK1 (0.85), PFKP (0.84), EIF3C (0.84), QARS1 (0.84), FERMT2 (0.83); STRING partners: HSD17B10 (0.902)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 1 heavy chain 1. Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polyp…
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy without contractures (0.816); intellectual disability, autosomal dominant 13 (0.815); Charcot-Marie-Tooth disease axonal type 2O (0.799); autosomal dominant non-syndromic intellectual disability (0.634); hereditary disease (0.545)
- **Europe PMC papers**: 1731
- **Why important**: DYNC1H1 is a central network hub with the broadest connectivity in the module and links metabolic, translation-related and adhesion-associated neighbors. Its established role is the heavy chain of cytoplasmic dynein, supporting intracellular transport, organelle movement, microtubule organization and retrograde transport. It has a strong disease literature involving motor-neuron, neuropathy and intellectual-disability phenotypes, and it connects to HSD17B10 in STRING. Its brain and retinal-ganglion-cell enrichment is notable, but its detection in both sampled tissues argues against treating it as exclusively neural.
- **Conclusion**: Established evidence supports DYNC1H1 as a structural and intracellular-transport hub. Its role as the organizing bridge between the module's metabolic and biosynthetic components is a hypothesis suggested by network position, not a demonstrated molecular mechanism.

#### PFKP

- **Related proteins** (co-abundance neighbors): SHMT2 (0.87), DYNC1H1 (0.84), HK1 (0.83), VPS35 (0.83), ANXA4 (0.83), PSMD13 (0.81); STRING partners: HK1 (0.995)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphofructokinase, platelet. This gene encodes a member of the phosphofructokinase A protein family. The encoded enzyme is the platelet-specific isoform of phosphofructokinase and plays a key role in glycolysis regulation. This gene may play a role in metabolic reprogramming in some cancers, including clear cell renal cell carcinomas, and cancer of the bladder, breast, and lung. Alternative splicing results in multiple transc…
- **Diseases (Open Targets)**: alcohol drinking (0.443); response to water (0.426); neurodegenerative disease (0.414); Alzheimer disease (0.372); spinocerebellar ataxia, autosomal recessive 30 (0.353)
- **Europe PMC papers**: 3384
- **Why important**: PFKP is a highly connected module member and forms the strongest STRING-supported metabolic pair with HK1. It is the platelet isoform of phosphofructokinase and regulates a central step of glycolysis. Its presence alongside mitochondrial HK1 gives the module a clear glucose-utilization anchor, while its extensive disease and cancer literature makes it biologically interpretable despite the absence of global enrichment. HPA links it to retina and several germ-cell or glial populations, with low immune-cell specificity.
- **Conclusion**: Established evidence supports PFKP as a glycolytic component and as a credible metabolic anchor of the module. Whether glycolytic flux is the driver of the shared bone-marrow-heart co-abundance pattern remains unproven.

#### SHMT2

- **Related proteins** (co-abundance neighbors): PFKP (0.87), RARS1 (0.85), HSD17B10 (0.82), HPRT1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine hydroxymethyltransferase 2. This gene encodes the mitochondrial form of a pyridoxal phosphate-dependent enzyme that catalyzes the reversible reaction of serine and tetrahydrofolate to glycine and 5,10-methylene tetrahydrofolate. The encoded product is primarily responsible for glycine synthesis. The activity of the encoded protein has been suggested to be the primary source of intracellular glycine. The gene which encodes th…
- **Diseases (Open Targets)**: neurodevelopmental disorder with cardiomyopathy, spasticity, and brain abnormalities (0.771); microcephaly (0.370); polymicrogyria (0.370); neurodevelopmental disorder (0.336); hereditary disease (0.192)
- **Europe PMC papers**: 2579
- **Why important**: SHMT2 occupies a connecting position between PFKP, RARS1, HSD17B10 and HPRT1. Its established mitochondrial role in serine-glycine interconversion and one-carbon metabolism provides a plausible link between energy metabolism, biosynthetic capacity and mitochondrial function. It is tissue enhanced in liver and cell-type enhanced in hepatocytes and several epithelial or trophoblast populations. Its disease associations include neurodevelopmental phenotypes with cardiomyopathy, making it relevant to a cross-tissue cellular-stress interpretation.
- **Conclusion**: Established evidence supports SHMT2 as a mitochondrial metabolic integrator. Its proposed coordination with glycolysis and translation in this module is a biologically plausible hypothesis, not an enrichment result.

#### RARS1

- **Related proteins** (co-abundance neighbors): PSMD13 (0.85), SHMT2 (0.85), FARSB (0.83); STRING partners: FARSB (0.706), QARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 is a network connector joining SHMT2, PSMD13 and FARSB, and it has a very strong STRING relationship with QARS1. It is an arginyl-tRNA synthetase required for translation, and it is represented with QARS1 in both hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Its disease associations include leukodystrophy-related disorders, although its literature volume is more modest than that of the major metabolic hubs. It therefore provides the clearest established translation and complex-membership anchor in the module.
- **Conclusion**: Established evidence supports RARS1 as a translation-related complex component and a validated local network connection. Its placement between metabolism and proteostasis suggests coordinated biosynthetic demand, but does not establish that the module is an aminoacyl-tRNA synthetase module.

#### HK1

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.85), PFKP (0.83); STRING partners: PFKP (0.995)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hexokinase 1. Hexokinases phosphorylate glucose to produce glucose-6-phosphate, the first step in most glucose metabolism pathways. This gene encodes a ubiquitous form of hexokinase which localizes to the outer membrane of mitochondria. Mutations in this gene have been associated with hemolytic anemia due to hexokinase deficiency. Alternative splicing of this gene results in several transcript variants which en…
- **Diseases (Open Targets)**: neurodevelopmental disorder with visual defects and brain anomalies (0.757); non-spherocytic hemolytic anemia due to hexokinase deficiency (0.751); Charcot-Marie-Tooth disease type 4G (0.711); retinitis pigmentosa 79 (0.596); retinitis pigmentosa (0.496)
- **Europe PMC papers**: 51843
- **Why important**: HK1 is the entry enzyme for glucose phosphorylation and forms the strongest STRING-supported pair with PFKP, creating a coherent glycolytic substructure within the otherwise mixed module. It is a ubiquitous mitochondria-associated hexokinase with extensive literature and disease links including hemolytic anemia, neurodevelopmental disease and retinal disorders. Its detection in both tissues and low immune-cell specificity make it a stronger general cellular-metabolism marker than a blood-specific marker.
- **Conclusion**: Established evidence supports HK1 as a glycolytic and mitochondria-associated component, and the HK1-PFKP relationship is a credible local functional unit. Its role in a shared tissue module is consistent with a common energy-demand state, but causality and cell-of-origin remain unresolved.

## Module 4

**Tissue pair**: bone_marrow and heart  
**Genes (26)**: ANXA6, ATP1A1, CAPN1, CLTC, EIF3L, GANAB, HNRNPK, HNRNPL, HSP90AA1, IQGAP1, LMNB2, MATR3, OLA1, PDCD6IP, PGK1, PSMC4, PSMC2, ATIC, RUVBL2, SPTBN1, CCT5, CCT3, CCT7, CCT8, TLN1, USO1

### Function

The strongest interpretation is a conserved intracellular proteostasis and genome-maintenance module. Primary GO evidence links the module to telomere maintenance, telomere maintenance through telomerase, telomere RNA localization to Cajal bodies, chromosome organization, and DNA biosynthesis or regulation (24 globally significant GO/KEGG terms, q_global 6.88e-05–0.00351; see the table), (GO:BP chromosome organization; q_global = 0.0207). The same module also shows ATP-dependent activity, ATP-dependent protein folding, unfolded-protein binding, and the chaperonin-containing T-complex (GO:MF ATP hydrolysis activity; q_global = 0.000251), (GO:MF ATP-dependent activity; q_global = 0.00332), (GO:CC protein folding chaperone complex; q_global = 0.00933), (GO:CC chaperonin-containing T-complex; q_global = 0.0109), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.0196), (GO:MF unfolded protein binding; q_global = 0.0451), (GO:MF pyrophosphatase activity; q_global = 0.0482) (GO:MF hydrolase activity, acting on acid anhydrides; q_global = 0.0482) (GO:MF hydrolase activity, acting on acid anhydrides, in phosphorus-containing anhydrides; q_global = 0.0482). The CCT subunits provide a coherent chaperone core, while HSP90AA1 and RUVBL2 connect protein folding and ATPase activity with nuclear DNA and telomere processes. The sperm-related terms (GO:BP binding of sperm to zona pellucida; q_global = 0.0376) and (GO:BP sperm-egg recognition; q_global = 0.0376) are best treated as context-dependent annotation overlap rather than the central function. The module therefore most plausibly reflects coordinated chaperone-supported maintenance of nuclear proteins, telomere-associated processes, and cellular protein quality control.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the HPA summary identifies only a small secreted component, and most genes have low tissue specificity. All genes have low immune-cell specificity, so the module is not specifically a blood-cell program according to HPA. Nevertheless, the STRING tissue annotations include blood, lymphoblast, lymphocyte, hematopoietic-system, and blood-cancer categories (STRING TISSUES Lymphoblast; within-query FDR = 0.0017), (STRING TISSUES Lymphocyte; within-query FDR = 0.0017), (STRING TISSUES Blood cancer cell; within-query FDR = 0.005), (STRING TISSUES Blood; within-query FDR = 0.0053), (STRING TISSUES Hematopoietic system; within-query FDR = 0.0061). This raises the possibility that the bone-marrow signal partly reflects shared cellular composition or broadly expressed housekeeping activity rather than a tissue-specific heart–marrow mechanism. HPA protein detection is stronger in bone marrow than in heart overall, and several genes are detected in bone marrow but not heart; conversely, the module contains broadly expressed genes detected in both tissues. Cell-type-enhanced annotations are distributed across reproductive, epithelial, vascular, stromal, and hematopoietic-associated cell types, without a coherent immune-cell enrichment. The shared module should therefore be interpreted cautiously as a broadly expressed intracellular program that may be influenced by sample composition.

**GO/KEGG enrichment**: 44 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulation of telomere maintenance | 6.88e-05 | CCT3, CCT5, CCT7, CCT8, HSP90AA1, RUVBL2 |
| GO:BP positive regulation of telomere maintenance | 6.88e-05 | CCT3, CCT5, CCT7, CCT8, HSP90AA1, RUVBL2 |
| GO:MF ATP hydrolysis activity | 0.000251 | ATP1A1, CCT3, CCT5, CCT7, CCT8, HSP90AA1, OLA1, PSMC2, PSMC4, RUVBL2 |
| GO:BP telomere maintenance | 0.000308 | CCT3, CCT5, CCT7, CCT8, HSP90AA1, RUVBL2 |
| GO:BP regulation of chromosome organization | 0.000308 | CCT3, CCT5, CCT7, CCT8, HSP90AA1, RUVBL2 |
| GO:BP positive regulation of chromosome organization | 0.000308 | CCT3, CCT5, CCT7, CCT8, HSP90AA1, RUVBL2 |
| GO:BP RNA-templated DNA biosynthetic process | 0.000877 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP telomere maintenance via telomerase | 0.000877 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP telomere maintenance via telomere lengthening | 0.000877 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP regulation of telomere maintenance via telomerase | 0.000877 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP positive regulation of telomere maintenance via telomerase | 0.000877 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP RNA localization to Cajal body | 0.000877 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP telomerase RNA localization to Cajal body | 0.000877 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP telomerase RNA localization | 0.000877 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP RNA localization to nucleus | 0.000877 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |

### STRING and hu.MAP

STRING supports a real molecular backbone rather than an arbitrary gene grouping. The CCT subunits form a tightly connected interaction clique, with additional links to HSP90AA1 and RUVBL2; PSMC2 and PSMC4 form a proteasome-ATPase pair; HNRNPK, HNRNPL, and MATR3 form an RNA-associated group; and IQGAP1, TLN1, and CAPN1 connect cytoskeletal or adhesion-related proteins. These are established relationships, not evidence that every co-abundance edge is a direct physical interaction. The STRING functional result for ATP hydrolysis (STRING Function ATP hydrolysis activity; within-query FDR = 0.00019) is concordant with the primary GO evidence but remains supplementary. The hu.MAP results independently recover the CCT subunit group in multiple complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), the hnRNP/MATR3 group (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10659.1), and the proteasome ATPase pair (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1). Additional hu.MAP complexes connect ATIC with OLA1 (hu.MAP huMAP3_14442.1) and USO1 with CLTC (hu.MAP huMAP3_12394.1). Thus, much of the module is anchored in known chaperonin, RNA-processing, proteasome, and trafficking machinery, while the cross-group co-abundance organization and its relationship to telomere maintenance are less directly established.

**STRING interactions (score >= 0.7)**: 25 of 325 gene pairs: ATIC–CCT7 (0.881); ATIC–CLTC (0.864); CAPN1–TLN1 (0.77); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT3–HSP90AA1 (0.767); CCT3–RUVBL2 (0.766); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT5–HSP90AA1 (0.868); CCT5–RUVBL2 (0.705); CCT7–CCT8 (0.999); CCT7–HSP90AA1 (0.849); CCT7–RUVBL2 (0.802); CCT8–HSP90AA1 (0.823); CCT8–PSMC2 (0.733); CCT8–RUVBL2 (0.776); HNRNPK–HNRNPL (0.99); HNRNPK–MATR3 (0.923); HNRNPL–MATR3 (0.757); HSP90AA1–PGK1 (0.713); HSP90AA1–RUVBL2 (0.886); IQGAP1–TLN1 (0.893); PSMC2–PSMC4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function ATP hydrolysis activity (FDR = 0.00019, 10 genes); TISSUES Lymphoblast (FDR = 0.0017, 11 genes); TISSUES Lymphocyte (FDR = 0.0017, 13 genes); TISSUES Testis (FDR = 0.0017, 16 genes); TISSUES Adenocarcinoma cell (FDR = 0.0036, 10 genes); TISSUES Digestive gland (FDR = 0.0048, 25 genes); TISSUES Male reproductive gland (FDR = 0.005, 17 genes); TISSUES Blood cancer cell (FDR = 0.005, 13 genes); TISSUES Blood (FDR = 0.0053, 17 genes); TISSUES Liver (FDR = 0.0053, 24 genes); TISSUES Hematopoietic system (FDR = 0.0061, 19 genes); RCTM Disease (FDR = 0.0068, 14 genes); RCTM Diseases of signal transduction by growth factor receptors and second messengers (FDR = 0.0068, 8 genes); TISSUES Melanoma cell line (FDR = 0.0085, 7 genes); TISSUES Gastrointestinal tract (FDR = 0.0133, 17 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_10625.1 (HNRNPL, MATR3, HNRNPK; 3/57); huMAP3_05721.1 (HNRNPL, MATR3; 2/6); huMAP3_07581.1 (HNRNPL, MATR3; 2/21); huMAP3_10659.1 (HNRNPL, HNRNPK; 2/28); huMAP3_05064.1 (PSMC2, PSMC4; 2/31); huMAP3_14442.1 (ATIC, OLA1; 2/57); huMAP3_09656.1 (PSMC2, PSMC4; 2/64); huMAP3_13725.1 (PSMC2, PSMC4; 2/69); huMAP3_12394.1 (USO1, CLTC; 2/98)

### Novelty

The module should not be described as a wholly new molecular pathway. Its core components and several internal relationships are already represented in STRING and hu.MAP, especially the CCT complex, proteasome ATPases, and heterogeneous nuclear ribonucleoprotein assemblies. The potentially novel aspect is the conserved co-abundance configuration shared by bone marrow and heart, including the coordinated presence of chaperone, telomere-associated, proteasome, RNA-processing, cytoskeletal, and trafficking genes. Database absence for some edges does not establish novelty, because co-abundance can arise from shared regulation, cell composition, or indirect functional coupling. The defensible conclusion is that this is a potentially novel tissue-pair co-abundance pattern built largely from established cellular machinery. Direct validation in independent cohorts, cell-resolved data, and perturbation experiments would be required before claiming a new biological mechanism.

**Hypothesis.** Hypothesis: in cells represented in both bone marrow and heart, increased demand for protein folding and proteostasis coordinates the CCT chaperonin system, HSP90AA1, proteasome ATPases, and RNA-associated nuclear factors. This coordination may help preserve the folding, localization, and turnover of proteins involved in telomere and chromosome maintenance, while cytoskeletal and trafficking components support the corresponding cellular architecture. RUVBL2 and the CCT subunits could provide a bridge between ATP-dependent chaperoning and telomere or nuclear-body processes, whereas MATR3 and the hnRNP group could influence RNA handling. This is a mechanistic hypothesis, not a demonstrated causal pathway; the observed co-abundance could also reflect broadly expressed housekeeping activity or shared cellular composition.

### Important genes

#### CCT7

- **Related proteins** (co-abundance neighbors): CCT8 (0.92), MATR3 (0.91), CCT3 (0.90), CCT5 (0.88), CAPN1 (0.88), ATP1A1 (0.85), RUVBL2 (0.85), LMNB2 (0.85), PSMC4 (0.84), OLA1 (0.84), USO1 (0.84), EIF3L (0.82), HSP90AA1 (0.81); STRING partners: ATIC (0.881), CCT3 (0.999), CCT5 (0.999), CCT8 (0.999), HSP90AA1 (0.849), RUVBL2 (0.802)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is among the most connected genes in the module and belongs to the central CCT chaperonin group recovered by STRING and multiple hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It appears in every primary enrichment theme spanning telomere maintenance, chromosome organization, ATP-dependent activity, chaperone complex, and unfolded-protein binding (44 globally significant GO/KEGG terms, q_global 6.88e-05–0.0482; see the table). Its established function is ATP-dependent folding of proteins including actin and tubulin. It is detected in both bone marrow and heart, has low tissue specificity, and has substantial literature support.
- **Conclusion**: Established evidence identifies CCT7 as a central CCT chaperonin component and a major contributor to the module's primary enrichment signal. The hypothesis that CCT7 couples proteostasis to telomere maintenance is plausible from the annotations but is not demonstrated by this co-abundance module.

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT7 (0.92), CCT3 (0.91), MATR3 (0.91), ATP1A1 (0.88), PSMC4 (0.84), HNRNPK (0.84), OLA1 (0.83), CCT5 (0.83), PGK1 (0.83), EIF3L (0.82), LMNB2 (0.82), RUVBL2 (0.81), HSP90AA1 (0.80); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999), HSP90AA1 (0.823), PSMC2 (0.733), RUVBL2 (0.776)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is highly connected and is a core partner of CCT3, CCT5, and CCT7 in STRING, while also recurring in multiple hu.MAP CCT complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It contributes to all of the principal telomere, chromosome, ATPase, chaperone, and Cajal-body enrichment terms (44 globally significant GO/KEGG terms, q_global 6.88e-05–0.0482; see the table). Its established role is as a subunit of the abundant CCT folding machinery. It is detected in both tissues and has broad tissue distribution, making it a strong marker of a general intracellular proteostasis program rather than a secreted or blood-specific signal.
- **Conclusion**: Established evidence supports CCT8 as a structural and functional anchor of the module. Its possible role in coordinating telomerase-RNA or Cajal-body processes should be regarded as a hypothesis derived from the enriched annotations, not as a module-specific causal finding.

#### HSP90AA1

- **Related proteins** (co-abundance neighbors): CCT3 (0.89), PGK1 (0.88), HNRNPK (0.84), CLTC (0.84), CCT5 (0.82), SPTBN1 (0.81), CCT7 (0.81), CCT8 (0.80); STRING partners: CCT3 (0.767), CCT5 (0.868), CCT7 (0.849), CCT8 (0.823), PGK1 (0.713), RUVBL2 (0.886)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein 90 alpha family class A member 1. The protein encoded by this gene is an inducible molecular chaperone that functions as a homodimer. The encoded protein aids in the proper folding of specific target proteins by use of an ATPase activity that is modulated by co-chaperones. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: cancer (0.643); plasma cell myeloma (0.404); non-small cell lung carcinoma (0.394); dengue disease (0.375); Orthomyxoviridae infectious disease (0.375)
- **Europe PMC papers**: 8215
- **Why important**: HSP90AA1 connects the CCT group with PGK1, RUVBL2, and other module members in STRING and contributes to the primary telomere, chromosome, ATPase, chaperone, and unfolded-protein terms (6 globally significant GO/KEGG terms, q_global 6.88e-05–0.000308; see the table), (4 globally significant GO/KEGG terms, q_global 0.000877–0.000877; see the table), (9 globally significant GO/KEGG terms, q_global 0.000877–0.00351; see the table), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.0196), (GO:BP chromosome organization; q_global = 0.0207), (GO:MF unfolded protein binding; q_global = 0.0451), (4 globally significant GO/KEGG terms, q_global 0.0475–0.0482; see the table). It is an inducible ATP-dependent molecular chaperone with extensive literature and broad disease associations. Its HPA profile is broadly distributed, with no immune-cell specificity, although protein detection is not reported in the sampled bone-marrow and heart locations.
- **Conclusion**: Established evidence supports HSP90AA1 as a major proteostasis and stress-responsive component that may stabilize client proteins in the module. A direct HSP90AA1-mediated effect on telomere maintenance in these tissues remains a hypothesis.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): PSMC2 (0.87), MATR3 (0.87), CCT5 (0.86), CAPN1 (0.85), CCT7 (0.85), CCT8 (0.81), EIF3L (0.81), ATP1A1 (0.81), PSMC4 (0.81); STRING partners: CCT3 (0.766), CCT5 (0.705), CCT7 (0.802), CCT8 (0.776), HSP90AA1 (0.886)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 occupies a connected position between the CCT group, HSP90AA1, MATR3, PSMC2, and EIF3L. It contributes directly to the primary telomere-maintenance, telomerase-RNA localization, DNA-metabolism, ATPase, and chaperone-complex evidence (6 globally significant GO/KEGG terms, q_global 6.88e-05–0.000308; see the table), (4 globally significant GO/KEGG terms, q_global 0.000877–0.000877; see the table), (6 globally significant GO/KEGG terms, q_global 0.000898–0.00933; see the table), (GO:CC microtubule cytoskeleton; q_global = 0.0177), (GO:BP chromosome organization; q_global = 0.0207), (5 globally significant GO/KEGG terms, q_global 0.0451–0.0482; see the table). Its established annotation includes ATPase and DNA-helicase activity, telomere maintenance, DNA repair, DNA recombination, and nuclear RNA-associated processes. It is detected in bone marrow but not heart and has tissue enhancement in testis, so composition effects should be considered.
- **Conclusion**: Established evidence makes RUVBL2 the strongest candidate for linking the module's chaperone and ATPase backbone to nuclear genome-maintenance biology. The proposed bridge between RUVBL2, CCT activity, and the shared heart–marrow co-abundance pattern remains a hypothesis.

#### MATR3

- **Related proteins** (co-abundance neighbors): CCT7 (0.91), CCT8 (0.91), CCT5 (0.90), ATP1A1 (0.88), PSMC2 (0.87), RUVBL2 (0.87), CAPN1 (0.86), OLA1 (0.86), CCT3 (0.85), EIF3L (0.82), PSMC4 (0.82), HNRNPL (0.81); STRING partners: HNRNPK (0.923), HNRNPL (0.757)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_05721.1, huMAP3_07581.1
- **Function (MyGene.info)**: matrin 3. This gene encodes a nuclear matrix protein, which is proposed to stabilize certain messenger RNA species. Mutations of this gene are associated with distal myopathy 2, which often includes vocal cord and pharyngeal weakness. Alternatively spliced transcript variants, including read-through transcripts composed of the upstream small nucleolar RNA host gene 4 (non-protein coding) and matrin 3 gene s…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.735); distal myopathy with vocal cord weakness (0.569); neurodegenerative disease (0.529); distal myopathy (0.384); hereditary disease (0.193)
- **Europe PMC papers**: 1756
- **Why important**: MATR3 is highly connected to the CCT subunits, ATP1A1, PSMC2, RUVBL2, CAPN1, and OLA1, and it anchors the hnRNP-associated hu.MAP complexes with HNRNPK and HNRNPL (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10659.1). It has primary support for regulation of metabolism (GO:BP regulation of metabolic process; q_global = 0.0475) and supplementary support for RNA- and blood-associated annotations (STRING TISSUES Lymphoblast; within-query FDR = 0.0017), (STRING TISSUES Lymphocyte; within-query FDR = 0.0017), (STRING TISSUES Adenocarcinoma cell; within-query FDR = 0.0036), (STRING TISSUES Blood; within-query FDR = 0.0053), (STRING TISSUES Hematopoietic system; within-query FDR = 0.0061). Its established functions include nuclear-matrix organization and stabilization or processing of messenger RNA. It is associated with distal myopathy and amyotrophic lateral sclerosis in the supplied disease evidence, and it has substantial literature support.
- **Conclusion**: Established evidence supports MATR3 as a nuclear RNA and structural organizer that may connect the chaperone-rich core to RNA processing. Its contribution to telomere maintenance is indirect and remains a hypothesis rather than an established function of this module.

## Module 5

**Tissue pair**: bone_marrow and heart  
**Genes (13)**: BLVRA, MTHFD1, DHX9, EHD1, GSTP1, MACROH2A1, HNRNPR, IMPDH2, PARVA, SEC22B, SEPTIN7, DARS1, TFRC

### Function

The module appears to combine a core intracellular gene-expression and biosynthetic program with supporting iron handling, redox control, cytoskeletal, adhesion, and vesicle-trafficking functions. DHX9 and HNRNPR are the most connected genes and point toward RNA processing, RNA transport, and transcriptional regulation. IMPDH2 and MTHFD1 support nucleotide and one-carbon metabolism, while TFRC supports cellular iron uptake and is particularly relevant to erythroid biology. PARVA and SEPTIN7 provide links to actin organization, adhesion, and cell structure; BLVRA and GSTP1 are compatible with redox and detoxification processes. This interpretation is integrative rather than enrichment-proven: no GO or KEGG term passed global correction, and there were no supplementary STRING enrichment terms. The absence of a globally significant term does not invalidate the co-abundance module.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins. TFRC is annotated as secreted to blood, but the remaining genes are mainly intracellular, and the module contains no broad secretome pattern. Most genes have low tissue specificity and low immune-cell specificity, arguing against a module that is simply a narrowly defined blood-cell signature. Nevertheless, several genes show cell-type-enhanced patterns involving erythrocyte progenitors, monocytes, neutrophils, cardiomyocytes, adipocytes, esophageal cells, and other cell types. This diversity suggests that shared cellular composition, common metabolic state, or ubiquitous cellular activity may contribute to the bone-marrow and heart co-abundance signal. Protein detection is broadly concordant in both tissues for most genes, whereas DARS1, SEPTIN7, GSTP1, and EHD1 show tissue-specific detection differences that should be considered when interpreting the shared module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The network has a compact, internally connected structure with DHX9 and HNRNPR as the main connectivity hubs. STRING provides a high-confidence known relationship between DHX9 and HNRNPR. No other module pair reaches the supplied STRING confidence threshold, and no STRING functional-enrichment result is available. No hu.MAP complex contains multiple module members. Thus, the co-abundance network is not recapitulated as a known multiprotein complex. The known DHX9-HNRNPR relationship supports a real RNA-associated core, while the remaining edges may reflect indirect co-regulation, shared cell states, shared compartmental biology, or context-specific interactions rather than established physical binding.

**STRING interactions (score >= 0.7)**: 1 of 78 gene pairs: DHX9–HNRNPR (0.909)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should be regarded as a potentially novel tissue-pair co-abundance pattern, not as a newly discovered molecular complex or a proven new pathway. Its novelty comes from the specific coordinated association of RNA handling, one-carbon and nucleotide metabolism, iron uptake, redox biology, and structural processes across bone marrow and heart. The limited STRING support and absence of a multi-member hu.MAP complex mean that much of this module-level organization is not already represented as a canonical molecular assembly. However, absence from those resources does not establish novelty: the genes themselves have substantial prior biological literature and several pairwise links may be indirect. Independent replication, cell-composition adjustment, and perturbation or physical-interaction experiments would be needed to claim a new mechanism.

**Hypothesis.** Hypothesis: this module represents a shared demand for RNA maturation, nucleotide production, iron acquisition, and stress-adaptive cellular maintenance in cell populations present in both bone marrow and heart. DHX9-HNRNPR may form the regulatory RNA-processing core; MTHFD1 and IMPDH2 may provide one-carbon and guanine-nucleotide support for transcription and proliferation; TFRC may connect the program to iron availability and erythroid or myeloid cell states; and PARVA, SEPTIN7, SEC22B, BLVRA, and GSTP1 may reflect structural, trafficking, and oxidative-stress components. This is a mechanistic proposal, not an established pathway assignment, because global enrichment is absent and most edges lack external interaction support.

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): HNRNPR (0.89), TFRC (0.89), MTHFD1 (0.87), BLVRA (0.86), DARS1 (0.85), SEC22B (0.85), MACROH2A1 (0.83); STRING partners: HNRNPR (0.909)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is the strongest network hub and connects the RNA-associated core to TFRC, MTHFD1, BLVRA, DARS1, SEC22B, and MACROH2A1. Its established functions include ATP-dependent unwinding of RNA and DNA-RNA complexes, transcriptional regulation, alternative mRNA splicing, chromatin organization, and interferon-related regulation. It is detected in both tissues, has low tissue and immune-cell specificity, and has extensive literature coverage. Its disease associations include developmental and neurodegenerative disorders, with additional infectious-disease relevance in the supplied evidence.
- **Conclusion**: Established: DHX9 is the best candidate for a central RNA-processing and transcriptional component of the module, supported by its network position and molecular annotation. Hypothesis: its hub position may coordinate RNA metabolism with metabolic and stress-responsive genes in the shared tissue context.

#### HNRNPR

- **Related proteins** (co-abundance neighbors): MTHFD1 (0.91), DHX9 (0.89), IMPDH2 (0.86), GSTP1 (0.82), MACROH2A1 (0.81), EHD1 (0.81), SEPTIN7 (0.81); STRING partners: DHX9 (0.909)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR is co-central with DHX9 and connects to MTHFD1, IMPDH2, GSTP1, MACROH2A1, EHD1, and SEPTIN7. It is an RNA-binding spliceosome-associated protein involved in pre-mRNA processing and transport. The DHX9-HNRNPR relationship is the only high-confidence STRING interaction within the module, giving this gene unusual support as part of a real RNA-associated core. It is detected in both tissues, has low tissue and immune-cell specificity, and has established links to neurodevelopmental and intellectual-disability phenotypes.
- **Conclusion**: Established: HNRNPR is a plausible partner and central RNA-processing component, with direct STRING support for its relationship to DHX9. Hypothesis: coordinated HNRNPR and DHX9 abundance may indicate altered RNA maturation or transport rather than a tissue-specific protein complex.

#### MTHFD1

- **Related proteins** (co-abundance neighbors): TFRC (0.92), HNRNPR (0.91), DHX9 (0.87); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methylenetetrahydrofolate dehydrogenase, cyclohydrolase and formyltetrahydrofolate synthetase 1. This gene encodes a protein that possesses three distinct enzymatic activities, 5,10-methylenetetrahydrofolate dehydrogenase, 5,10-methenyltetrahydrofolate cyclohydrolase and 10-formyltetrahydrofolate synthetase. Each of these activities catalyzes one of three sequential reactions in the interconversion of 1-carbon derivatives of tetrahydrofolate, which are substrates for methionine, thymidylate, …
- **Diseases (Open Targets)**: combined immunodeficiency and megaloblastic anemia with or without hyperhomocysteinemia (0.773); severe combined immunodeficiency (0.473); neural tube defects, folate-sensitive (0.414); isolated spina bifida (0.376); atrial fibrillation (0.332)
- **Europe PMC papers**: 1939
- **Why important**: MTHFD1 is a metabolic bridge between the RNA-associated genes and TFRC, with connections to DHX9 and HNRNPR. It carries three enzymatic activities in folate-mediated one-carbon metabolism, supporting methionine, thymidylate, and de novo purine synthesis. It is tissue-enriched in liver but cell-type-enhanced in cardiomyocytes, adipocytes, erythrocyte progenitors, epicardial cells, and hepatocytes, and it is detected in both module tissues. Its disease associations include combined immunodeficiency, megaloblastic anemia, folate-sensitive neural-tube defects, and atrial fibrillation.
- **Conclusion**: Established: MTHFD1 provides a strong biochemical rationale for coupling the module to one-carbon metabolism and nucleotide supply. Hypothesis: it may connect biosynthetic demand in erythroid or cardiac-associated cells to the RNA-processing core, but the module does not establish causality.

#### TFRC

- **Related proteins** (co-abundance neighbors): MTHFD1 (0.92), DHX9 (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes, Lysosomes; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transferrin receptor. This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: TFRC-related combined immunodeficiency (0.623); type 2 diabetes mellitus (0.518); mucopolysaccharidosis type 2 (0.490); diabetes mellitus (0.471); diabetic retinopathy (0.343)
- **Europe PMC papers**: 14164
- **Why important**: TFRC links the high-connectivity DHX9-MTHFD1 region to iron uptake and has cell-type-enhanced expression in erythrocyte progenitors, macrophages, monocytes, and syncytiotrophoblasts. It is also immune-cell-enhanced for non-classical monocytes and is annotated as secreted to blood. Its established function is receptor-mediated cellular iron uptake, with importance for erythropoiesis and neurological development. It is detected in both tissues and has extensive literature coverage. Its disease associations include TFRC-related combined immunodeficiency and metabolic disorders.
- **Conclusion**: Established: TFRC is the clearest connection between this module and iron-dependent cellular metabolism, especially erythroid or myeloid biology. Hypothesis: its presence may reflect shared iron-handling demands or variable blood-cell contribution rather than a heart-specific mechanism.

#### IMPDH2

- **Related proteins** (co-abundance neighbors): PARVA (0.91), SEPTIN7 (0.87), HNRNPR (0.86), DARS1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inosine monophosphate dehydrogenase 2. This gene encodes the rate-limiting enzyme in the de novo guanine nucleotide biosynthesis. It is thus involved in maintaining cellular guanine deoxy- and ribonucleotide pools needed for DNA and RNA synthesis. The encoded protein catalyzes the NAD-dependent oxidation of inosine-5'-monophosphate into xanthine-5'-monophosphate, which is then converted into guanosine-5'-monophosphate. This gene is up-…
- **Diseases (Open Targets)**: acute lymphoblastic leukemia (0.529); Crohn disease (0.447); acute myeloid leukemia (0.421); lupus nephritis (0.408); myelodysplastic syndrome (0.403)
- **Europe PMC papers**: 1438
- **Why important**: IMPDH2 occupies an intermediate network position connecting PARVA, SEPTIN7, HNRNPR, and DARS1. It is the rate-limiting enzyme in de novo guanine-nucleotide production and therefore supports DNA and RNA synthesis. It is detected in both tissues, has low tissue specificity, and shows cell-type enhancement in several epithelial and reproductive cell types. The supplied disease associations include acute lymphoblastic leukemia, acute myeloid leukemia, Crohn disease, lupus nephritis, and myelodysplastic syndrome, with substantial literature coverage.
- **Conclusion**: Established: IMPDH2 supplies a plausible nucleotide-biosynthetic component and links the metabolic branch to the RNA-processing branch. Hypothesis: its co-abundance with DHX9 and HNRNPR may reflect increased nucleotide demand accompanying RNA production, proliferation, or cellular stress.

## Module 6

**Tissue pair**: bone_marrow and heart  
**Genes (7)**: CALD1, CLIC1, CRIP2, FLNA, GSR, SERPINH1, VIM

### Function

The module is most consistent with a vascular, stromal, and cytoskeletal co-abundance program rather than a single established biochemical pathway. Its genes cover actin and intermediate-filament organization through FLNA, VIM, CALD1, and CRIP2; collagen biosynthetic support and endoplasmic-reticulum protein folding through SERPINH1; cellular redox defense through GSR; and chloride-channel, signaling, and platelet-related functions through CLIC1. The HPA pattern, including frequent enhancement in vascular smooth muscle, stromal, fibroblast-like, and related cell types, supports a vascular or mesenchymal structural interpretation. No GO or KEGG term passed global correction, so no GO/KEGG pathway is claimed as significantly enriched. The lung tissue signal in (STRING TISSUES Lung; within-query FDR = 0.0244) is supplementary and does not establish a globally significant pathway.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: only SERPINH1 has a secretome annotation, and the remaining proteins are intracellular or cytoskeletal. The genes are also not uniformly blood-cell specific. Several have low immune-cell specificity, while individual genes show enhancement in neutrophils, basophils, lymphocyte subsets, megakaryocytes, platelets, or neutrophil progenitors. In contrast, all module genes are cell-type enhanced in HPA, with recurring associations to stromal, fibroblast-like, hepatic stellate, vascular smooth-muscle, or related cell types. This makes a shared vascular or stromal cell component, and possibly differences in cellular mixture between bone marrow and heart, plausible explanations for the cross-tissue co-abundance. Protein detection is stronger in bone marrow than in heart for this set, so the inferred heart component should be treated cautiously.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no high-confidence physical interaction among the module members, and hu.MAP provides no complex containing multiple module members. Thus the module is not supported as a canonical protein complex. All genes appear in the supplementary STRING tissue signal (STRING TISSUES Lung; within-query FDR = 0.0244), but that result is a tissue-level enrichment observation and does not demonstrate direct molecular interaction. The observed co-abundance may therefore reflect shared cell origin, coordinated structural state, or correlated stress and remodeling rather than binding within one complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Lung (FDR = 0.0244, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The cross-tissue co-abundance pattern may be a novel observation in this dataset, because it is not explained by a previously recognized STRING interaction network or hu.MAP complex. However, the module cannot be declared a new biological mechanism from these facts alone. Its genes have established and partly generic roles in cytoskeletal structure, contraction, collagen handling, redox control, and signaling, and several have substantial literature. Absence from STRING or hu.MAP is not evidence that the biological association is novel. Replication in independent cohorts, cell-composition adjustment, and perturbation or spatial validation would be needed.

**Hypothesis.** Hypothesis: the conserved module reflects coordinated abundance of vascular or stromal cells and their structural state in bone marrow and heart. In this model, FLNA, VIM, CALD1, and CRIP2 organize or regulate the cytoskeleton and cell shape; SERPINH1 supports collagen maturation and proteostasis; GSR buffers oxidative stress; and CLIC1 contributes to ion handling, signaling, or platelet-associated activity. Shared vascular or mesenchymal remodeling could produce the co-abundance without requiring direct physical interaction among all proteins. This is a mechanistic hypothesis, not an established pathway assignment.

### Important genes

#### CRIP2

- **Related proteins** (co-abundance neighbors): SERPINH1 (0.83), CLIC1 (0.83), GSR (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cysteine rich protein 2. This gene encodes a putative transcription factor with two LIM zinc-binding domains. The encoded protein may participate in the differentiation of smooth muscle tissue. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2012].
- **Diseases (Open Targets)**: ventricular septal defect (0.248); systemic sclerosis (0.231); thyroid gland disorder (0.229); immunodeficiency disease (0.224); ulcerative colitis (0.206)
- **Europe PMC papers**: 747
- **Why important**: CRIP2 is the most connected gene in the module and links SERPINH1, CLIC1, and GSR, making it the central network candidate. Its LIM zinc-binding domains and reported role in smooth-muscle differentiation fit the vascular and stromal HPA pattern. It is associated in Open Targets with vascular- or immune-relevant disorders including systemic sclerosis and immunodeficiency, and its literature is substantial. It is also included in the supplementary STRING tissue signal (STRING TISSUES Lung; within-query FDR = 0.0244).
- **Conclusion**: Established: CRIP2 is the network hub and has annotations compatible with smooth-muscle or vascular differentiation. Hypothesis: CRIP2 may coordinate the structural and redox-related genes in this co-abundance pattern. Direct regulation within this module is not demonstrated.

#### FLNA

- **Related proteins** (co-abundance neighbors): CALD1 (0.84), VIM (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA connects CALD1 and VIM and is a well-established actin-crosslinking and membrane-cytoskeleton scaffold. Its tissue and single-cell annotations include blood vessels, stromal cells, hepatic stellate cells, and megakaryocytes. It has strong disease associations with multiple developmental skeletal and neurological syndromes and has an extensive literature. It is included in (STRING TISSUES Lung; within-query FDR = 0.0244).
- **Conclusion**: Established: FLNA can provide a structural link between actin-based contractility and intermediate-filament organization. Hypothesis: its position may mark a shared vascular or stromal remodeling state across the two tissues, but the module does not establish a direct FLNA interaction with the other members.

#### VIM

- **Related proteins** (co-abundance neighbors): SERPINH1 (0.83), FLNA (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vimentin. This gene encodes a type III intermediate filament protein. Intermediate filaments, along with microtubules and actin microfilaments, make up the cytoskeleton. The encoded protein is responsible for maintaining cell shape and integrity of the cytoplasm, and stabilizing cytoskeletal interactions. This protein is involved in neuritogenesis and cholesterol transport and functions as an organizer of a…
- **Diseases (Open Targets)**: dengue disease (0.516); early-onset non-syndromic cataract (0.462); early-onset partial cataract (0.458); Developmental cataract (0.435); cataract (0.372)
- **Europe PMC papers**: 86568
- **Why important**: VIM connects FLNA and SERPINH1 and encodes the principal intermediate filament protein vimentin, which supports cell shape, integrity, attachment, migration, and signaling organization. HPA associates it with blood vessels, fibroblasts, decidual stromal cells, hepatic stellate cells, and other mesenchymal cell types. It has the largest literature footprint in the module and is included in (STRING TISSUES Lung; within-query FDR = 0.0244).
- **Conclusion**: Established: VIM is a strong marker of mesenchymal structural state and is consistent with the HPA composition evidence. Hypothesis: VIM may reflect cellular remodeling or migration underlying the shared module. Its broad expression means it is not, by itself, specific for the proposed bone-marrow or heart mechanism.

#### SERPINH1

- **Related proteins** (co-abundance neighbors): VIM (0.83), CRIP2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family H member 1. This gene encodes a member of the serpin superfamily of serine proteinase inhibitors. The encoded protein is localized to the endoplasmic reticulum and plays a role in collagen biosynthesis as a collagen-specific molecular chaperone. Autoantibodies to the encoded protein have been found in patients with rheumatoid arthritis. Expression of this gene may be a marker for cancer, and nucleotide polymo…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 10 (0.714); preterm premature rupture of the membranes (0.559); coronary artery disorder (0.554); myocardial infarction (0.510); Abnormality of the skeletal system (0.474)
- **Europe PMC papers**: 2762
- **Why important**: SERPINH1 links VIM and CRIP2 and encodes an endoplasmic-reticulum collagen-specific molecular chaperone. Its collagen biosynthesis, protein-folding, and unfolded-protein-response annotations connect the structural arm of the module to extracellular-matrix production. It is associated with osteogenesis imperfecta, coronary artery disorder, and myocardial infarction, and has a substantial literature. It is included in (STRING TISSUES Lung; within-query FDR = 0.0244).
- **Conclusion**: Established: SERPINH1 provides the clearest extracellular-matrix and proteostasis rationale for the module. Hypothesis: it may indicate collagen remodeling coupled to vascular or stromal cytoskeletal change. Its lack of protein detection in the assayed tissues argues against treating it as direct proof of an active tissue-localized complex.

#### CALD1

- **Related proteins** (co-abundance neighbors): FLNA (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Actin filaments; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caldesmon 1. This gene encodes a calmodulin- and actin-binding protein that plays an essential role in the regulation of smooth muscle and nonmuscle contraction. The conserved domain of this protein possesses the binding activities to Ca(2+)-calmodulin, actin, tropomyosin, myosin, and phospholipids. This protein is a potent inhibitor of the actin-tropomyosin activated myosin MgATPase, and serves as a mediating…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.499); diaphragmatic hernia (0.447); glaucoma (0.405); diverticular disease (0.393); open-angle glaucoma (0.390)
- **Europe PMC papers**: 3386
- **Why important**: CALD1 is the module's calmodulin- and actin-binding contractility component and connects to FLNA. Its established role in smooth-muscle and nonmuscle contraction, together with HPA enhancement in myoepithelial, stromal, stellate, and Leydig-related cell types, supports the vascular or contractile interpretation. It has a substantial literature and is included in (STRING TISSUES Lung; within-query FDR = 0.0244).
- **Conclusion**: Established: CALD1 supplies a direct contractile explanation for the module's vascular and smooth-muscle-associated composition. Hypothesis: coordinated CALD1 and FLNA abundance may reflect altered cell tension or vessel-wall remodeling. The module does not show direct physical-complex evidence for this proposal.

#### GSR

- **Related proteins** (co-abundance neighbors): CRIP2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutathione-disulfide reductase. This gene encodes a member of the class-I pyridine nucleotide-disulfide oxidoreductase family. This enzyme is a homodimeric flavoprotein. It is a central enzyme of cellular antioxidant defense, and reduces oxidized glutathione disulfide (GSSG) to the sulfhydryl form GSH, which is an important cellular antioxidant. Rare mutations in this gene result in hereditary glutathione reductase deficiency. M…
- **Diseases (Open Targets)**: hemolytic anemia due to glutathione reductase deficiency (0.702); glioblastoma (0.558); plasma cell myeloma (0.537); Hodgkins lymphoma (0.531); non-Hodgkin lymphoma (0.506)
- **Europe PMC papers**: 6439
- **Why important**: GSR is the redox-defense member connected to CRIP2. It regenerates reduced glutathione and is annotated for glutathione metabolism, oxidative-stress response, redox homeostasis, and cellular oxidant detoxification. HPA links it particularly to neutrophil progenitors and basophils, while Open Targets includes hereditary glutathione reductase deficiency and hematologic disorders. Its literature is substantial and it is included in (STRING TISSUES Lung; within-query FDR = 0.0244).
- **Conclusion**: Established: GSR indicates that redox control may accompany the structural program, and it may also reflect a hematopoietic component in bone marrow. Hypothesis: oxidative stress could help couple vascular or stromal remodeling with the observed co-abundance. The data do not distinguish a causal redox role from cell-composition effects.
